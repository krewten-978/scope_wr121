#!/usr/bin/env python3
"""Migrate one scope_wr121 graded worksheet into graded-assignments/<ID>/.

Usage (from repo root):
  .venv-grader/bin/python scripts/migrate-one-worksheet.py U1L1LL
  .venv-grader/bin/python scripts/migrate-one-worksheet.py U1L1LL --skip-git
  .venv-grader/bin/python scripts/migrate-one-worksheet.py U1L1LL --no-push
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# assignment_id -> relative path to current graded .tex (before migration)
SOURCE_MAP: dict[str, str] = {}

def _build_source_map() -> dict[str, str]:
    m: dict[str, str] = {}
    for week in range(1, 16):
        base = f"units/elements-of-logic-week{week}"
        m[f"U1L{week}LL"] = f"{base}/logic-labs/U1L{week}LL_logic_lab.tex"
        m[f"U1L{week}LE"] = f"{base}/lit-examples/U1L{week}LE_lit_example_worksheet.tex"
    m["U1F1LD"] = "finals/logic-dungeon-1/U1F1LD_logic_dungeon_final.tex"
    m["U1F2LD"] = "finals/logic-dungeon-2/U1F2LD_logic_dungeon_final.tex"
    m["U1F3LD"] = "finals/logic-dungeon-3/U1F3LD_logic_dungeon_final.tex"
    # already-migrated pilot uses graded-assignments path
    if (ROOT / "graded-assignments/U1F1LD/worksheet.tex").is_file():
        m["U1F1LD"] = "graded-assignments/U1F1LD/worksheet.tex"
    return m


SOURCE_MAP = _build_source_map()

ANSWERBOX_RE = re.compile(
    r"\\answerbox\{(?:ANSWER LABEL:\s*)?(Part\s+\d+\s+Q\d+)\}(\{[^}]+\})",
    re.IGNORECASE,
)
LOGICLABBOX_RE = re.compile(
    r"\\logiclabbox\{(?:ANSWER LABEL:\s*)?(Part\s+\d+\s+Q\d+)\}(\{[^}]+\})",
    re.IGNORECASE,
)


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    print("+", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=str(cwd or ROOT), capture_output=True, text=True)
    if check and proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit(f"command failed ({proc.returncode}): {' '.join(cmd)}")
    return proc


def _remove_balanced_newcommand(text: str, macroname: str) -> str:
    """Remove \\newcommand{\\macroname}[n]{...} with brace-balanced body."""
    needle = f"\\newcommand{{\\{macroname}}}"
    while True:
        start = text.find(needle)
        if start < 0:
            return text
        i = start + len(needle)
        # optional [n]
        if i < len(text) and text[i] == "[":
            j = text.find("]", i)
            if j < 0:
                raise ValueError(f"unclosed [ in newcommand {macroname}")
            i = j + 1
        if i >= len(text) or text[i] != "{":
            raise ValueError(f"expected {{ after newcommand {macroname}")
        depth = 0
        k = i
        while k < len(text):
            ch = text[k]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    k += 1
                    break
            k += 1
        else:
            raise ValueError(f"unbalanced newcommand {macroname}")
        # swallow following blank lines
        end = k
        while end < len(text) and text[end] == "\n":
            end += 1
        text = text[:start] + text[end:]


def transform_tex(text: str, assignment_id: str) -> str:
    """Drop local fancyhdr/lastpage/pagestyle and answerbox macro; use shared package."""
    text = text.replace("\r\n", "\n")

    text = re.sub(
        r"\\usepackage\[margin=0\.6in,top=0\.85in,bottom=0\.55in\]\{geometry\}",
        r"\\usepackage[margin=0.6in,top=1.15in,bottom=0.55in]{geometry}",
        text,
    )

    for pkg in ("fancyhdr", "lastpage"):
        text = re.sub(rf"\\usepackage\{{{pkg}\}}\n?", "", text)

    if "grader-worksheet" not in text:
        if r"\usepackage[hidelinks]{hyperref}" in text:
            text = text.replace(
                r"\usepackage[hidelinks]{hyperref}",
                "\\usepackage[hidelinks]{hyperref}\n"
                "\\usepackage{../../latex/grader-worksheet}",
            )
        else:
            text = re.sub(
                r"(\\usepackage\[[^\]]*\]\{geometry\})",
                r"\1\n\\usepackage{../../latex/grader-worksheet}",
                text,
                count=1,
            )

    text = re.sub(r"\\setlength\{\\headheight\}\{[^}]+\}\n?", "", text)

    # fancyhdr setup: from \pagestyle{fancy} through head/footrule renewcommands
    text = re.sub(
        r"\\pagestyle\{fancy\}.*?(?:\\renewcommand\{\\footrulewidth\}\{[^}]*\}|"
        r"\\renewcommand\{\\headrulewidth\}\{[^}]*\})\n?",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )
    # leftovers
    text = re.sub(r"\\fancyhf\{\}\n?", "", text)
    text = re.sub(r"\\fancyhead\[[^\]]*\]\{.*?\}\n?", "", text, flags=re.DOTALL)
    text = re.sub(r"\\renewcommand\{\\headrulewidth\}\{[^}]*\}\n?", "", text)
    text = re.sub(r"\\renewcommand\{\\footrulewidth\}\{[^}]*\}\n?", "", text)

    text = _remove_balanced_newcommand(text, "answerbox")
    text = _remove_balanced_newcommand(text, "logiclabbox")

    if r"\GraderSetup" not in text:
        text = text.replace(
            r"\begin{document}",
            f"\\GraderSetup{{assignment-id={assignment_id},template-revision=1}}\n\n"
            r"\begin{document}",
        )
    else:
        text = re.sub(
            r"\\GraderSetup\{[^}]+\}",
            f"\\GraderSetup{{assignment-id={assignment_id},template-revision=1}}",
            text,
        )

    def repl(m: re.Match) -> str:
        label = re.sub(r"\s+", " ", m.group(1).strip())
        lm = re.match(r"Part\s+(\d+)\s+Q(\d+)", label, re.I)
        if not lm:
            raise ValueError(f"bad label: {label}")
        label = f"Part {int(lm.group(1))} Q{int(lm.group(2))}"
        return f"\\GraderAnswerBox{{{label}}}{m.group(2)}"

    text2, n1 = ANSWERBOX_RE.subn(repl, text)
    text3, n2 = LOGICLABBOX_RE.subn(repl, text2)
    if n1 + n2 == 0 and r"\GraderAnswerBox" not in text3:
        raise ValueError(f"{assignment_id}: no answerbox macros found to convert")

    text3 = re.sub(r"\n{3,}", "\n\n", text3)
    # safety: no leftover local answerbox def/use
    if re.search(r"\\newcommand\{\\answerbox\}", text3):
        raise ValueError(f"{assignment_id}: failed to remove answerbox definition")
    if r"\answerbox" in text3:
        raise ValueError(f"{assignment_id}: leftover \\answerbox uses")
    return text3


def update_index(assignment_id: str) -> None:
    path = ROOT / "graded-assignments.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    row = {
        "assignment_id": assignment_id,
        "template_revision": 1,
        "tex": f"graded-assignments/{assignment_id}/worksheet.tex",
        "pdf": f"graded-assignments/{assignment_id}/worksheet.pdf",
        "template": f"graded-assignments/{assignment_id}/template.json",
        "answer_key": f"answer-keys/{assignment_id}.md",
    }
    found = False
    for i, a in enumerate(data["assignments"]):
        if a["assignment_id"] == assignment_id:
            data["assignments"][i] = row
            found = True
            break
    if not found:
        data["assignments"].append(row)
    # stable sort: F first then L by natural id
    data["assignments"].sort(key=lambda a: a["assignment_id"])
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_answer_key_path(assignment_id: str) -> None:
    key = ROOT / "answer-keys" / f"{assignment_id}.md"
    if not key.is_file():
        return
    text = key.read_text(encoding="utf-8")
    new_path = f"`graded-assignments/{assignment_id}/worksheet.tex` / `.pdf`"
    # Common paired lines
    patterns = [
        (
            r"(\*\*Paired worksheet:\*\*\s*).*",
            rf"\1{new_path} (Assignment ID **{assignment_id}**).",
        ),
        (
            r"(\*\*Paired final:\*\*\s*).*",
            rf"\1{new_path} (Assignment ID **{assignment_id}**).",
        ),
        (
            r"(\*\*Paired dungeon(?: final)?:\*\*\s*).*",
            rf"\1{new_path} (Assignment ID **{assignment_id}**).",
        ),
        (
            r"(\*\*Paired exam:\*\*\s*).*",
            rf"\1{new_path} (Assignment ID **{assignment_id}**).",
        ),
    ]
    new = text
    for pat, rep in patterns:
        new = re.sub(pat, rep, new)
    # generic path rewrite of old source location
    src = SOURCE_MAP.get(assignment_id, "")
    if src and src.endswith(".tex"):
        stem = src[:-4]
        new = new.replace(f"`{src}`", f"`graded-assignments/{assignment_id}/worksheet.tex`")
        new = new.replace(f"`{stem}.pdf`", f"`graded-assignments/{assignment_id}/worksheet.pdf`")
        new = new.replace(
            f"`{src}` / `.pdf`",
            f"`graded-assignments/{assignment_id}/worksheet.tex` / `.pdf`",
        )
    if new != text:
        key.write_text(new, encoding="utf-8")


def update_readme_pointers(assignment_id: str, old_tex: str) -> None:
    """Update README mentions of old tex/pdf paths to graded-assignments."""
    old_pdf = old_tex[:-4] + ".pdf" if old_tex.endswith(".tex") else old_tex
    old_rel_tex = Path(old_tex).name
    old_rel_pdf = Path(old_pdf).name
    new_tex = f"graded-assignments/{assignment_id}/worksheet.tex"
    new_pdf = f"graded-assignments/{assignment_id}/worksheet.pdf"

    candidates: list[Path] = []
    # unit/finals folder readmes
    parent = (ROOT / old_tex).parent if (ROOT / old_tex).parent.exists() else None
    # After git mv parent may still exist
    # week README is two levels up from logic-labs/lit-examples
    for p in ROOT.rglob("README.md"):
        if ".git" in p.parts:
            continue
        candidates.append(p)

    for readme in candidates:
        text = readme.read_text(encoding="utf-8")
        orig = text
        # full relative from repo
        text = text.replace(old_tex, new_tex)
        text = text.replace(old_pdf, new_pdf)
        # bare filenames only if assignment id is mentioned nearby or path component matches
        if assignment_id in text or old_rel_tex in text:
            # Prefer explicit replacements of known basename paths under units/finals
            text = re.sub(
                rf"`(?:logic-labs|lit-examples)/{re.escape(old_rel_tex)}`",
                f"`../../../{new_tex}`",
                text,
            )
            text = re.sub(
                rf"`(?:logic-labs|lit-examples)/{re.escape(old_rel_pdf)}`",
                f"`../../../{new_pdf}`",
                text,
            )
            text = re.sub(
                rf"`{re.escape(old_rel_tex)}`",
                f"`{new_tex}`",
                text,
            )
            text = re.sub(
                rf"`{re.escape(old_rel_pdf)}`",
                f"`{new_pdf}`",
                text,
            )
            # latexmk lines
            text = text.replace(old_rel_tex, f"../../../{new_tex}")
        if text != orig:
            # Keep relative compile instructions sensible from week dirs
            readme.write_text(text, encoding="utf-8")
            print(f"  updated README: {readme.relative_to(ROOT)}")


def compile_worksheet(dest_dir: Path) -> None:
    # clean auxiliaries lightly
    for ext in (".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".toc"):
        p = dest_dir / f"worksheet{ext}"
        if p.exists():
            p.unlink()
    proc = run(
        [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-pdflatex=pdflatex -interaction=nonstopmode -halt-on-error %O %S",
            "worksheet.tex",
        ],
        cwd=dest_dir,
        check=False,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout[-4000:])
        sys.stderr.write(proc.stderr[-4000:])
        raise SystemExit(f"latexmk failed for {dest_dir}")
    # remove aux noise from worktree before commit consideration
    run(
        ["latexmk", "-c", "worksheet.tex"],
        cwd=dest_dir,
        check=False,
    )


def verify_qr_and_layout(assignment_id: str) -> dict:
    import cv2
    import fitz
    import numpy as np

    pdf_path = ROOT / "graded-assignments" / assignment_id / "worksheet.pdf"
    doc = fitz.open(pdf_path)
    detector = cv2.QRCodeDetector()
    payloads = []
    issues = []

    question_re = re.compile(r"Question\s+(\d+)\.(\d+)")
    label_re = re.compile(r"^Part\s+(\d+)\s+Q(\d+)$")

    def decode_qr(page: fitz.Page) -> str:
        """OpenCV often needs a quiet-zone pad and a tight top-right crop."""
        for dpi in (200, 300):
            mat = fitz.Matrix(dpi / 72, dpi / 72)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
                pix.height, pix.width, 3
            )
            bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            h, w = bgr.shape[:2]
            crops = [
                bgr[0 : int(h * 0.28), int(w * 0.55) : w],
                bgr[0 : int(h * 0.22), int(w * 0.65) : w],
                bgr[
                    int(45 * dpi / 72) : int(100 * dpi / 72),
                    int(520 * dpi / 72) : int(575 * dpi / 72),
                ],
                bgr,
            ]
            for crop in crops:
                if crop.size == 0:
                    continue
                gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
                pad = 40
                padded = cv2.copyMakeBorder(
                    gray, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=255
                )
                for im in (padded, gray):
                    data, _, _ = detector.detectAndDecode(im)
                    if data:
                        return data
                    ok, infos, _, _ = detector.detectAndDecodeMulti(im)
                    if ok and infos:
                        for info in infos:
                            if info:
                                return info
        return ""

    for i, page in enumerate(doc):
        expected = f"krewone:v1|assignment={assignment_id}|revision=1|page={i + 1}"
        data = decode_qr(page)
        if data != expected:
            issues.append(f"page {i+1}: QR want {expected!r} got {data!r}")
        else:
            payloads.append(data)

        text = page.get_text()
        if "Student Name" not in text or "Student ID" not in text:
            issues.append(f"page {i+1}: missing name/id")
        if assignment_id not in text:
            issues.append(f"page {i+1}: missing assignment id")

    labels_by_page: dict[int, list[str]] = {}
    questions_by_page: dict[int, list[str]] = {}
    for i, page in enumerate(doc):
        labels_by_page[i] = []
        questions_by_page[i] = []
        for block in page.get_text("dict").get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                t = "".join(s.get("text", "") for s in line.get("spans", [])).strip()
                if label_re.match(t):
                    labels_by_page[i].append(t)
                if question_re.search(t):
                    questions_by_page[i].append(t)

    label_page: dict[str, int] = {}
    for i, labs in labels_by_page.items():
        for lb in labs:
            label_page[lb] = i
    for i, qs in questions_by_page.items():
        for q in qs:
            m = question_re.search(q)
            if not m:
                continue
            want = f"Part {int(m.group(1))} Q{int(m.group(2))}"
            if want in label_page and label_page[want] != i:
                issues.append(
                    f"SPLIT: {want}: question heading on page {i+1}, "
                    f"label/box on page {label_page[want]+1}"
                )

    page_count = doc.page_count
    doc.close()
    return {
        "pages": page_count,
        "qr_ok": len(payloads) == page_count and not any("QR" in x for x in issues),
        "payloads": payloads,
        "issues": issues,
    }


def review_pages_render(assignment_id: str, out_dir: Path) -> list[Path]:
    import fitz

    pdf_path = ROOT / "graded-assignments" / assignment_id / "worksheet.pdf"
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    paths = []
    mat = fitz.Matrix(150 / 72, 150 / 72)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        p = out_dir / f"{assignment_id}_p{i+1}.png"
        pix.save(str(p))
        paths.append(p)
    doc.close()
    return paths


def fix_question_splits(tex_path: Path, issues: list[str]) -> int:
    """Insert \\newpage before question stems orphaned from their answer boxes.

    Returns number of newpage insertions applied.
    """
    split_re = re.compile(
        r"SPLIT:\s+Part\s+(\d+)\s+Q(\d+):\s+question heading on page"
    )
    targets: list[tuple[int, int]] = []
    for iss in issues:
        m = split_re.search(iss)
        if m:
            targets.append((int(m.group(1)), int(m.group(2))))
    if not targets:
        return 0

    text = tex_path.read_text(encoding="utf-8")
    applied = 0
    # Process later questions first so earlier insertions don't shift patterns oddly
    for part, q in sorted(targets, reverse=True):
        # Match \textbf{Question N.M} not already preceded by \newpage
        pat = re.compile(
            rf"(?<!\\newpage\n\n)(?<!\\newpage\n)"
            rf"(\\textbf\{{Question {part}\.{q}\}})"
        )
        new_text, n = pat.subn(rf"\\newpage\n\n\1", text, count=1)
        if n == 0:
            # broader: Question with optional spacing variants
            pat2 = re.compile(
                rf"(\\textbf\{{Question {part}\.{q}\}})"
            )
            # only insert if previous non-empty line is not newpage
            m = pat2.search(text)
            if not m:
                print(f"  warn: could not locate Question {part}.{q} for split fix")
                continue
            before = text[: m.start()]
            if re.search(r"\\newpage\s*$", before.rstrip()):
                continue
            new_text = text[: m.start()] + "\\newpage\n\n" + text[m.start() :]
            n = 1
        if n:
            text = new_text
            applied += n
            print(f"  inserted \\newpage before Question {part}.{q}")
    if applied:
        tex_path.write_text(text, encoding="utf-8")
    return applied


def migrate(assignment_id: str, push: bool = True, skip_git_mv: bool = False) -> None:
    if assignment_id not in SOURCE_MAP:
        raise SystemExit(f"unknown id {assignment_id}")
    key = ROOT / "answer-keys" / f"{assignment_id}.md"
    if not key.is_file():
        raise SystemExit(f"missing answer key {key}")

    dest_dir = ROOT / "graded-assignments" / assignment_id
    dest_tex = dest_dir / "worksheet.tex"
    dest_pdf = dest_dir / "worksheet.pdf"

    old_tex_rel = SOURCE_MAP[assignment_id]
    old_tex = ROOT / old_tex_rel
    old_pdf = ROOT / (old_tex_rel[:-4] + ".pdf")

    if dest_tex.is_file() and old_tex_rel.startswith("graded-assignments/"):
        print(f"{assignment_id}: already under graded-assignments; re-transform/recompile")
        raw = dest_tex.read_text(encoding="utf-8")
        if r"\GraderAnswerBox" not in raw:
            dest_tex.write_text(transform_tex(raw, assignment_id), encoding="utf-8")
    else:
        if not old_tex.is_file():
            if dest_tex.is_file():
                print(f"{assignment_id}: source already moved")
            else:
                raise SystemExit(f"missing source tex {old_tex}")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            if not skip_git_mv:
                if not dest_tex.exists():
                    run(
                        [
                            "git",
                            "mv",
                            str(old_tex.relative_to(ROOT)),
                            str(dest_tex.relative_to(ROOT)),
                        ]
                    )
                if old_pdf.is_file() and not dest_pdf.exists():
                    run(
                        [
                            "git",
                            "mv",
                            str(old_pdf.relative_to(ROOT)),
                            str(dest_pdf.relative_to(ROOT)),
                        ]
                    )
            else:
                dest_tex.write_text(old_tex.read_text(encoding="utf-8"), encoding="utf-8")
                if old_pdf.is_file():
                    dest_pdf.write_bytes(old_pdf.read_bytes())

        raw = dest_tex.read_text(encoding="utf-8")
        if r"\GraderSetup" not in raw or r"\answerbox" in raw:
            dest_tex.write_text(transform_tex(raw, assignment_id), encoding="utf-8")

    update_index(assignment_id)
    update_answer_key_path(assignment_id)
    if not old_tex_rel.startswith("graded-assignments/"):
        update_readme_pointers(assignment_id, old_tex_rel)

    # compile + verify loop; auto-fix page splits up to a few times
    layout = None
    for attempt in range(1, 5):
        compile_worksheet(dest_dir)
        run(
            [
                str(ROOT / ".venv-grader/bin/python"),
                str(ROOT / "scripts/build-grader-templates.py"),
                "--assignment",
                assignment_id,
            ]
        )
        t1 = (dest_dir / "template.json").read_bytes()
        run(
            [
                str(ROOT / ".venv-grader/bin/python"),
                str(ROOT / "scripts/build-grader-templates.py"),
                "--assignment",
                assignment_id,
            ]
        )
        t2 = (dest_dir / "template.json").read_bytes()
        if t1 != t2:
            raise SystemExit("template.json not stable across rebuilds")

        layout = verify_qr_and_layout(assignment_id)
        splits = [i for i in layout["issues"] if i.startswith("SPLIT:")]
        other_hard = [
            i for i in layout["issues"] if ("QR" in i or "missing" in i) and not i.startswith("SPLIT:")
        ]
        if layout["issues"]:
            print(f"LAYOUT/QR ISSUES (attempt {attempt}):")
            for iss in layout["issues"]:
                print(" -", iss)
        if other_hard:
            raise SystemExit(f"{assignment_id}: verification failed (non-split)")
        if not splits:
            break
        n = fix_question_splits(dest_tex, splits)
        if n == 0:
            raise SystemExit(f"{assignment_id}: split detected but auto-fix failed")
    else:
        raise SystemExit(f"{assignment_id}: splits remain after auto-fix attempts")

    render_dir = ROOT / ".cache" / "grader-review" / assignment_id
    pages = review_pages_render(assignment_id, render_dir)
    print(f"Rendered {len(pages)} pages to {render_dir}")

    tmpl = json.loads((dest_dir / "template.json").read_text(encoding="utf-8"))
    print(
        f"OK {assignment_id}: {tmpl['page_count']} pages, "
        f"{len(tmpl['answer_boxes'])} boxes, sha={tmpl['pdf_sha256'][:12]}"
    )

    for p in dest_dir.glob("worksheet.*"):
        if p.suffix in {".tex", ".pdf"}:
            continue
        p.unlink(missing_ok=True)

    run(
        [
            "git",
            "add",
            "-A",
            "graded-assignments",
            "graded-assignments.json",
            "answer-keys",
            "units",
            "finals",
            "README.md",
            "scripts/migrate-one-worksheet.py",
        ],
        check=False,
    )
    status = run(["git", "status", "--short"], check=False)
    print(status.stdout)
    msg = f"Migrate {assignment_id} to graded-assignments grader layout."
    diff = run(["git", "diff", "--cached", "--name-only"], check=False)
    if not diff.stdout.strip():
        print("nothing to commit")
        return
    run(["git", "commit", "-m", msg])
    if push:
        run(["git", "push", "origin", "main"])
    print(f"Committed and {'pushed' if push else 'not pushed'}: {assignment_id}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("assignment_id")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--skip-git", action="store_true")
    args = ap.parse_args()
    migrate(args.assignment_id, push=not args.no_push, skip_git_mv=args.skip_git)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
