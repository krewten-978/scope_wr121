# Elements of Logic — Week 18

## Week 18 — Logic Portfolio Workshop

**Core focus:** selecting evidence of growth, recovering original reasoning, criterion-based diagnosis, substantive revision, reflective captions, and transfer.

**Essential question:** Which habits of logic have become visible in my own work?

## Student-facing materials

- `student-packets/Whately_Logic_Week18_Student_Reading.tex`
- `student-packets/Whately_Logic_Week18_Student_Reading.pdf`
- `../../../graded-assignments/U1L18LL/worksheet.tex`
- `../../../graded-assignments/U1L18LL/worksheet.pdf`
- `lit-examples/U1L18LE_lit_example_reader.tex`
- `lit-examples/U1L18LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L18LE/worksheet.tex`
- `../../../graded-assignments/U1L18LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L18LL.md`
- `answer-keys/U1L18LE.md`

## Graded-assignment packaging (Krewone)

Authoritative gradable worksheets live only under:

- `graded-assignments/U1L18LL/{worksheet.tex,worksheet.pdf,template.json}`
- `graded-assignments/U1L18LE/{worksheet.tex,worksheet.pdf,template.json}`

The LE reader remains in `lit-examples/`; no legacy worksheet authority belongs in the unit folder.

## Build commands

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week18_Student_Reading.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L18LE_lit_example_reader.tex
cd ../../../graded-assignments/U1L18LL && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
cd ../U1L18LE && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
# from repo root:
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L18LL
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L18LE
```

## Verification

Run both answer-key validators and confirm every graded page has the Krewone header, registration marks, a QR payload that decodes at 150 DPI, and canonical `Part N QN` answer boxes.
