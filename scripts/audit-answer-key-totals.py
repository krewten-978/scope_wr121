#!/usr/bin/env python3
"""Audit answer-keys: listed **Total Points:** vs sum of graded section headers.

Recognizes:
  ## Question N: Part X QY – … (N points)
  ## Part X QY – … (N points)

Usage:
  python3 audit-answer-key-totals.py [answer-keys-dir]

Exit 0 if all keys match; exit 1 if any mismatch (prints discrepancies).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TOTAL_PAT = re.compile(r"\*\*Total Points:\*\*\s*(\d+)")
SECTION_PAT = re.compile(r"^## (?:Question \d+: )?Part \d+ Q\d+", re.I)


def points_for_section_line(line: str) -> int | None:
    matches = list(re.finditer(r"\((\d+)\s*points?\)", line, re.I))
    if matches:
        return int(matches[-1].group(1))
    m = re.search(r"\((\d+)\s*point\b", line, re.I)
    return int(m.group(1)) if m else None


def is_graded_section(line: str) -> bool:
    if line.startswith("## Question"):
        return True
    return bool(SECTION_PAT.match(line))


def audit_file(path: Path) -> tuple[int | None, int | None, list[int]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = TOTAL_PAT.search(text)
    listed = int(m.group(1)) if m else None
    q_pts: list[int] = []
    for line in text.splitlines():
        if not is_graded_section(line):
            continue
        p = points_for_section_line(line)
        if p is not None:
            q_pts.append(p)
    actual = sum(q_pts) if q_pts else None
    return listed, actual, q_pts


def main() -> int:
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    else:
        root = Path("answer-keys")
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 2

    files = sorted(p for p in root.glob("*.md") if p.name.upper() != "README.MD")
    mismatches = []
    for path in files:
        listed, actual, q_pts = audit_file(path)
        if listed is None or actual is None or listed != actual:
            mismatches.append((path.name, listed, actual, q_pts))

    print(f"Checked {len(files)} keys in {root.resolve()}")
    if not mismatches:
        print("All listed totals match section-header sums.")
        return 0

    print(f"Mismatches: {len(mismatches)}")
    for name, listed, actual, q_pts in mismatches:
        print(f"  {name}: listed={listed} actual={actual} breakdown={q_pts}")
    print(
        "\nFix: set **Total Points:** and Overall Notes 'Total:' arithmetic to actual.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())