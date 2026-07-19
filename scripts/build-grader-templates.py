#!/usr/bin/env python3
"""Build Krewone grader template.json files from compiled worksheet PDFs.

Uses structured PDF APIs (PyMuPDF): text + vector strokes. Does not parse LaTeX.

Coordinate convention: PDF points, top-left origin, boxes as [x0, y0, x1, y1].

Run from repository root:

  .venv-grader/bin/python scripts/build-grader-templates.py
  .venv-grader/bin/python scripts/build-grader-templates.py --assignment U1F1LD
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyMuPDF is required. Create .venv-grader and install deps from "
        "requirements-grader.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
INDEX_NAME = "graded-assignments.json"
LABEL_RE = re.compile(r"^Part\s+(\d+)\s+Q(\d+)$")
KEY_HEADING_RE = re.compile(
    r"^##\s+Question\s+\d+:\s+(Part\s+\d+\s+Q\d+)\b", re.MULTILINE
)
VISIBLE_ID_RE = re.compile(r"Assignment\s+ID:\s*([A-Za-z0-9]+)")
VISIBLE_REV_RE = re.compile(r"Rev:\s*(\d+)")


@dataclass
class LabelHit:
    label: str
    page_index: int  # 0-based
    y0: float
    y1: float
    x0: float
    x1: float


def load_index(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("graded-assignments.json must have schema_version: 1")
    assignments = data.get("assignments")
    if not isinstance(assignments, list) or not assignments:
        raise ValueError("graded-assignments.json assignments must be a non-empty list")
    seen: set[str] = set()
    for row in assignments:
        if not isinstance(row, dict):
            raise ValueError("each assignment must be an object")
        aid = row.get("assignment_id")
        if not aid or not isinstance(aid, str):
            raise ValueError("assignment_id required")
        if aid in seen:
            raise ValueError(f"duplicate assignment_id: {aid}")
        seen.add(aid)
        for key in ("tex", "pdf", "template", "answer_key", "template_revision"):
            if key not in row:
                raise ValueError(f"{aid}: missing field {key}")
    return data


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_label(text: str) -> str | None:
    s = " ".join(text.split())
    m = LABEL_RE.fullmatch(s)
    if not m:
        return None
    return f"Part {int(m.group(1))} Q{int(m.group(2))}"


def extract_labels(page: fitz.Page, page_index: int) -> list[LabelHit]:
    hits: list[LabelHit] = []
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = "".join(span.get("text", "") for span in line.get("spans", [])).strip()
            label = normalize_label(text)
            if not label:
                continue
            x0, y0, x1, y1 = line["bbox"]
            hits.append(
                LabelHit(label=label, page_index=page_index, y0=y0, y1=y1, x0=x0, x1=x1)
            )
    return hits


def extract_box_rects(page: fitz.Page) -> list[fitz.Rect]:
    """Reconstruct full-width answer fbox rectangles from stroke drawings."""
    horizontals: list[fitz.Rect] = []
    verticals: list[fitz.Rect] = []
    for d in page.get_drawings():
        r = fitz.Rect(d["rect"])
        # Skip filled QR modules
        if d.get("fill") is not None and d.get("color") is None:
            continue
        w, h = r.width, r.height
        if h < 1.6 and w > 400:
            horizontals.append(r)
        if w < 1.6 and h > 50:
            verticals.append(r)

    candidates: list[fitz.Rect] = []
    horizontals = sorted(horizontals, key=lambda r: r.y0)
    for i, a in enumerate(horizontals):
        for b in horizontals[i + 1 : i + 6]:
            if abs(a.x0 - b.x0) > 3 or abs(a.x1 - b.x1) > 3:
                continue
            top = min(a.y0, b.y0)
            bot = max(a.y1, b.y1)
            height = bot - top
            width = max(a.x1, b.x1) - min(a.x0, b.x0)
            if not (40 < height < 520 and width > 400):
                continue
            left = min(a.x0, b.x0)
            right = max(a.x1, b.x1)
            # Require vertical strokes near both sides spanning most of the height.
            left_ok = any(
                abs(v.x0 - left) < 3 and v.y0 <= top + 3 and v.y1 >= bot - 3
                for v in verticals
            )
            right_ok = any(
                abs(v.x0 - right) < 3 and v.y0 <= top + 3 and v.y1 >= bot - 3
                for v in verticals
            )
            if left_ok and right_ok:
                candidates.append(fitz.Rect(left, top, right, bot))

    # Dedupe near-identical rectangles
    out: list[fitz.Rect] = []
    for c in candidates:
        if any(abs(c.y0 - o.y0) < 2 and abs(c.y1 - o.y1) < 2 for o in out):
            continue
        out.append(c)
    return out


def associate_boxes(
    labels: list[LabelHit], boxes: list[fitz.Rect], page_index: int, page_rect: fitz.Rect
) -> list[dict[str, Any]]:
    used: set[int] = set()
    associated: list[dict[str, Any]] = []
    page_labels = [lb for lb in labels if lb.page_index == page_index]
    for lb in sorted(page_labels, key=lambda x: x.y0):
        best_i = None
        best_d = 1e9
        for i, br in enumerate(boxes):
            if i in used:
                continue
            # Box top should sit just under the label.
            if br.y0 + 1 < lb.y0:
                continue
            d = br.y0 - lb.y1
            if d < -2 or d > 90:
                continue
            if d < best_d:
                best_d = d
                best_i = i
        if best_i is None:
            raise ValueError(
                f"page {page_index + 1}: no rectangle for label {lb.label!r}"
            )
        used.add(best_i)
        br = boxes[best_i]
        if (
            br.x0 < page_rect.x0 - 1
            or br.y0 < page_rect.y0 - 1
            or br.x1 > page_rect.x1 + 1
            or br.y1 > page_rect.y1 + 1
        ):
            raise ValueError(
                f"page {page_index + 1}: rectangle for {lb.label} out of page bounds"
            )
        associated.append(
            {
                "label": lb.label,
                "page": page_index + 1,
                "rect_topleft": [
                    round(br.x0, 2),
                    round(br.y0, 2),
                    round(br.x1, 2),
                    round(br.y1, 2),
                ],
            }
        )
    unused = [boxes[i] for i in range(len(boxes)) if i not in used]
    # Extra full-width frames (e.g. rare artifacts) are ignored if unused.
    _ = unused
    return associated


def parse_answer_key_labels(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    labels = KEY_HEADING_RE.findall(text)
    out: list[str] = []
    for raw in labels:
        norm = normalize_label(raw)
        if not norm:
            raise ValueError(f"{path}: unparsable key heading label {raw!r}")
        out.append(norm)
    if not out:
        raise ValueError(f"{path}: no Question N: Part X QY headings found")
    if len(out) != len(set(out)):
        raise ValueError(f"{path}: duplicate Part labels in answer key")
    return out


def verify_visible_identity(doc: fitz.Document, assignment_id: str, revision: int) -> None:
    for i, page in enumerate(doc):
        text = page.get_text()
        m_id = VISIBLE_ID_RE.search(text)
        m_rev = VISIBLE_REV_RE.search(text)
        if not m_id or m_id.group(1) != assignment_id:
            raise ValueError(
                f"page {i + 1}: visible Assignment ID mismatch "
                f"(want {assignment_id}, got {m_id.group(1) if m_id else None})"
            )
        if not m_rev or int(m_rev.group(1)) != revision:
            raise ValueError(
                f"page {i + 1}: visible Rev mismatch "
                f"(want {revision}, got {m_rev.group(1) if m_rev else None})"
            )
        if "Student Name" not in text or "Student ID" not in text:
            raise ValueError(f"page {i + 1}: missing Student Name/ID header fields")


def build_template_for_assignment(root: Path, row: dict[str, Any]) -> dict[str, Any]:
    aid = row["assignment_id"]
    revision = int(row["template_revision"])
    pdf_path = root / row["pdf"]
    key_path = root / row["answer_key"]
    template_path = root / row["template"]
    tex_path = root / row["tex"]

    for p, label in (
        (pdf_path, "pdf"),
        (key_path, "answer_key"),
        (tex_path, "tex"),
    ):
        if not p.is_file():
            raise FileNotFoundError(f"{aid}: missing {label} at {p}")

    key_labels = parse_answer_key_labels(key_path)
    digest = sha256_file(pdf_path)
    doc = fitz.open(pdf_path)
    try:
        verify_visible_identity(doc, aid, revision)
        all_labels: list[LabelHit] = []
        page_boxes: dict[int, list[dict[str, Any]]] = {}
        page_dims: list[dict[str, float]] = []

        for i, page in enumerate(doc):
            page_dims.append(
                {
                    "page": i + 1,
                    "width": round(page.rect.width, 2),
                    "height": round(page.rect.height, 2),
                }
            )
            labels = extract_labels(page, i)
            all_labels.extend(labels)
            boxes = extract_box_rects(page)
            page_boxes[i] = associate_boxes(labels, boxes, i, page.rect)

        found_labels = [lb.label for lb in all_labels]
        if len(found_labels) != len(set(found_labels)):
            raise ValueError(f"{aid}: duplicate visible labels in PDF: {found_labels}")

        ordered_boxes: list[dict[str, Any]] = []
        for i in range(doc.page_count):
            ordered_boxes.extend(page_boxes[i])

        pdf_label_order = [b["label"] for b in ordered_boxes]
        if pdf_label_order != key_labels:
            raise ValueError(
                f"{aid}: PDF labels {pdf_label_order} != answer-key labels {key_labels}"
            )
        if len(ordered_boxes) != len(key_labels):
            raise ValueError(f"{aid}: box count mismatch")

        for kl in key_labels:
            if kl not in pdf_label_order:
                raise ValueError(f"{aid}: answer-key label {kl} has no box")

        template = {
            "schema_version": 1,
            "assignment_id": aid,
            "template_revision": revision,
            "pdf": row["pdf"],
            "pdf_sha256": digest,
            "page_count": doc.page_count,
            "coordinate_system": {
                "units": "pt",
                "origin": "top-left",
                "axis": "x right, y down",
                "box_format": "[x0, y0, x1, y1]",
            },
            "pages": page_dims,
            "answer_boxes": ordered_boxes,
        }
    finally:
        doc.close()

    write_json_atomic(template_path, template)
    return template


def write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=False)
            f.write("\n")
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--assignment",
        action="append",
        dest="assignments",
        help="limit to assignment_id (repeatable)",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    index_path = root / INDEX_NAME
    if not index_path.is_file():
        print(f"missing index: {index_path}", file=sys.stderr)
        return 2

    index = load_index(index_path)
    rows = index["assignments"]
    if args.assignments:
        want = set(args.assignments)
        rows = [r for r in rows if r["assignment_id"] in want]
        missing = want - {r["assignment_id"] for r in rows}
        if missing:
            print(f"unknown assignment ids: {sorted(missing)}", file=sys.stderr)
            return 2

    for row in rows:
        aid = row["assignment_id"]
        print(f"building template for {aid} ...")
        template = build_template_for_assignment(root, row)
        print(
            f"  ok: {len(template['answer_boxes'])} boxes, "
            f"{template['page_count']} pages, "
            f"sha256={template['pdf_sha256'][:12]}..."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
