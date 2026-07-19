#!/usr/bin/env python3
"""Automated checks for Krewone graded-assignments index + template builder."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "build_grader_templates", ROOT / "scripts" / "build-grader-templates.py"
)
assert _spec is not None and _spec.loader is not None
bgt = importlib.util.module_from_spec(_spec)
sys.modules["build_grader_templates"] = bgt
_spec.loader.exec_module(bgt)


class IndexTests(unittest.TestCase):
    def test_load_real_index(self):
        data = bgt.load_index(ROOT / "graded-assignments.json")
        self.assertEqual(data["schema_version"], 1)
        ids = [a["assignment_id"] for a in data["assignments"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_reject_duplicate_ids(self):
        bad = {
            "schema_version": 1,
            "assignments": [
                {
                    "assignment_id": "X",
                    "template_revision": 1,
                    "tex": "a.tex",
                    "pdf": "a.pdf",
                    "template": "a.json",
                    "answer_key": "a.md",
                },
                {
                    "assignment_id": "X",
                    "template_revision": 1,
                    "tex": "b.tex",
                    "pdf": "b.pdf",
                    "template": "b.json",
                    "answer_key": "b.md",
                },
            ],
        }
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "graded-assignments.json"
            p.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaises(ValueError):
                bgt.load_index(p)

    def test_reject_malformed_schema(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "graded-assignments.json"
            p.write_text(json.dumps({"schema_version": 2, "assignments": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                bgt.load_index(p)

    def test_label_normalization(self):
        self.assertEqual(bgt.normalize_label("Part 1 Q2"), "Part 1 Q2")
        self.assertEqual(bgt.normalize_label("Part  3  Q10"), "Part 3 Q10")
        self.assertIsNone(bgt.normalize_label("ANSWER LABEL: Part 1 Q1"))
        self.assertIsNone(bgt.normalize_label("Part 1 Q1 ANSWER BOX"))

    def test_answer_key_labels_u1f1ld(self):
        labels = bgt.parse_answer_key_labels(ROOT / "answer-keys" / "U1F1LD.md")
        self.assertEqual(len(labels), 14)
        self.assertEqual(labels[0], "Part 1 Q1")
        self.assertEqual(labels[-1], "Part 8 Q2")

    def test_sha256_stable(self):
        pdf = ROOT / "graded-assignments" / "U1F1LD" / "worksheet.pdf"
        a = bgt.sha256_file(pdf)
        b = bgt.sha256_file(pdf)
        self.assertEqual(a, b)
        self.assertEqual(len(a), 64)

    def test_build_u1f1ld_template(self):
        row = {
            "assignment_id": "U1F1LD",
            "template_revision": 1,
            "tex": "graded-assignments/U1F1LD/worksheet.tex",
            "pdf": "graded-assignments/U1F1LD/worksheet.pdf",
            "template": "graded-assignments/U1F1LD/template.json",
            "answer_key": "answer-keys/U1F1LD.md",
        }
        # Build into a temp copy of template path then compare structure via API
        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            # minimal fake root with needed files
            (td_path / "answer-keys").mkdir()
            shutil.copy(ROOT / "answer-keys" / "U1F1LD.md", td_path / "answer-keys" / "U1F1LD.md")
            gdir = td_path / "graded-assignments" / "U1F1LD"
            gdir.mkdir(parents=True)
            shutil.copy(ROOT / row["pdf"], gdir / "worksheet.pdf")
            shutil.copy(ROOT / row["tex"], gdir / "worksheet.tex")
            local_row = dict(row)
            local_row["template"] = "graded-assignments/U1F1LD/template.json"
            template = bgt.build_template_for_assignment(td_path, local_row)
            self.assertEqual(template["assignment_id"], "U1F1LD")
            self.assertEqual(template["template_revision"], 1)
            self.assertEqual(len(template["answer_boxes"]), 14)
            self.assertEqual(template["coordinate_system"]["origin"], "top-left")
            self.assertEqual(template["pdf_sha256"], bgt.sha256_file(gdir / "worksheet.pdf"))
            # boxes in reading order
            labels = [b["label"] for b in template["answer_boxes"]]
            self.assertEqual(labels, bgt.parse_answer_key_labels(td_path / "answer-keys" / "U1F1LD.md"))
            for box in template["answer_boxes"]:
                x0, y0, x1, y1 = box["rect_topleft"]
                self.assertLess(x0, x1)
                self.assertLess(y0, y1)

    def test_cli_runs(self):
        py = shutil.which("python3")
        script = ROOT / "scripts" / "build-grader-templates.py"
        # Prefer project venv if present
        venv_py = ROOT / ".venv-grader" / "bin" / "python"
        exe = str(venv_py if venv_py.is_file() else py)
        proc = subprocess.run(
            [exe, str(script), "--assignment", "U1F1LD"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertTrue((ROOT / "graded-assignments" / "U1F1LD" / "template.json").is_file())


if __name__ == "__main__":
    unittest.main()
