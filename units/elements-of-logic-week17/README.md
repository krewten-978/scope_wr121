# Elements of Logic — Week 17

## Week 17 — Literary Self-Deception

**Core focus:** self-deception, motivated reasoning, rationalization, private argument vs public cover, and multi-tool Whately autopsy.

**Essential question:** How do people use reasoning to hide from themselves?

## Student-facing materials

- `student-packets/Whately_Logic_Week17_Student_Reading.tex`
- `student-packets/Whately_Logic_Week17_Student_Reading.pdf`
- `../../../graded-assignments/U1L17LL/worksheet.tex`
- `../../../graded-assignments/U1L17LL/worksheet.pdf`
- `lit-examples/U1L17LE_lit_example_reader.tex`
- `lit-examples/U1L17LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L17LE/worksheet.tex`
- `../../../graded-assignments/U1L17LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L17LL.md`
- `answer-keys/U1L17LE.md`

## Graded-assignment packaging (Krewone)

Authoritative gradable worksheets live only under:

- `graded-assignments/U1L17LL/{worksheet.tex,worksheet.pdf,template.json}`
- `graded-assignments/U1L17LE/{worksheet.tex,worksheet.pdf,template.json}`

Do not create new authority under `logic-labs/` or `lit-examples/*_worksheet.*`. LE **readers** stay in `lit-examples/`.

## Build commands

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week17_Student_Reading.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L17LE_lit_example_reader.tex
cd ../../../graded-assignments/U1L17LL && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
cd ../U1L17LE && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
# from repo root:
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L17LL
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L17LE
```

## Verification

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Confirm QR payload at 150 DPI and `Part N QN` boxes for both graded IDs.
