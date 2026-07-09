#!/usr/bin/env python3
"""Validate scope_wr121 / scope_tenth answer-key gradable headings for krewone-style grader.

Usage: validate-answer-key-headings.py /path/to/answer-keys
Exit 0 if all .md files pass; exit 1 and print failures otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

VALID = re.compile(r"^##\s+Question\s+\d+\s*:\s*Part\s+\d+\s+Q\d+", re.MULTILINE)
INVALID = re.compile(r"^##\s+Part\s+\d+\s+Q\d+", re.MULTILINE)
SEQ = re.compile(r"^##\s+Question\s+(\d+)\s*:\s*Part\s+\d+\s+Q\d+", re.MULTILINE)


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if not VALID.search(text):
        issues.append("no heading matching ## Question N: Part X QY")
    if INVALID.search(text):
        issues.append("still has invalid ## Part X QY heading(s)")
    nums = [int(m.group(1)) for m in SEQ.finditer(text)]
    if nums and nums != list(range(1, len(nums) + 1)):
        issues.append(f"non-sequential Question N: {nums}")
    return issues


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate-answer-key-headings.py <answer-keys-dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    failed = []
    for fp in sorted(root.glob("*.md")):
        if fp.name.upper() == "README.MD":
            continue
        issues = check_file(fp)
        if issues:
            failed.append((fp.name, issues))
    if failed:
        print("VALIDATION FAILED")
        for name, issues in failed:
            print(f"  {name}: " + "; ".join(issues))
        return 1
    n = len([p for p in root.glob("*.md") if p.name.upper() != "README.MD"])
    print(f"OK: {n} files, all have valid Question N: Part X QY headings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())