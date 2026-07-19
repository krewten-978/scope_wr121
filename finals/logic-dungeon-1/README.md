# U1F1LD — Logic Dungeon I (grader pilot)

**Authoritative student worksheet (Krewone graded-assignments layout):**

- `../../graded-assignments/U1F1LD/worksheet.tex`
- `../../graded-assignments/U1F1LD/worksheet.pdf`
- `../../graded-assignments/U1F1LD/template.json` (generated box coordinates)
- Answer key (unchanged): `../../answer-keys/U1F1LD.md`

Build from repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=graded-assignments/U1F1LD \
  graded-assignments/U1F1LD/worksheet.tex
# or cd graded-assignments/U1F1LD && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex

.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1F1LD
```

Legacy filenames `U1F1LD_logic_dungeon_final.tex/.pdf` were moved with `git mv` into `graded-assignments/U1F1LD/worksheet.*`.
