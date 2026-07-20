# Elements of Logic — Week 16

## Week 16 — Logic and Rhetoric

**Core focus:** persuasion vs proof, logos/ethos/pathos, audience, rhetorical force, and rhetoric-vs-proof analysis.

**Essential question:** How do style, emotion, character, and persuasion relate to proof?

## Student-facing materials

- `student-packets/Whately_Logic_Week16_Student_Reading.tex`
- `student-packets/Whately_Logic_Week16_Student_Reading.pdf`
- `../../../graded-assignments/U1L16LL/worksheet.tex`
- `../../../graded-assignments/U1L16LL/worksheet.pdf`
- `lit-examples/U1L16LE_lit_example_reader.tex`
- `lit-examples/U1L16LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L16LE/worksheet.tex`
- `../../../graded-assignments/U1L16LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L16LL.md`
- `answer-keys/U1L16LE.md`

## Graded-assignment packaging (Krewone)

Authoritative gradable worksheets live only under:

- `graded-assignments/U1L16LL/{worksheet.tex,worksheet.pdf,template.json}`
- `graded-assignments/U1L16LE/{worksheet.tex,worksheet.pdf,template.json}`

Do not create new authority under `logic-labs/` or `lit-examples/*_worksheet.*`. LE **readers** stay in `lit-examples/`.

## Build commands

Run from this week folder (readings/readers) or graded-assignments dirs (worksheets):

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week16_Student_Reading.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L16LE_lit_example_reader.tex
cd ../../../graded-assignments/U1L16LL && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
cd ../U1L16LE && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
# from repo root:
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L16LL
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L16LE
```

## Verification

Before pushing, run from repo root:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Confirm QR payload at 150 DPI and `Part N QN` boxes for both graded IDs.
