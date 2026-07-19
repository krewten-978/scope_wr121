# Elements of Logic — Week 11

## Week 11 — When Comparisons Prove Too Much

**Core focus:** analogy, source case, target case, relevant similarity, disanalogy, overextension, and decorative comparison.

**Essential question:** When does a comparison actually prove something?

## Student-facing materials

- `student-packets/Whately_Logic_Week11_Student_Reading.tex`
- `student-packets/Whately_Logic_Week11_Student_Reading.pdf`
- `logic-labs/U1L11LL_logic_lab.tex`
- `logic-labs/U1L11LL_logic_lab.pdf`
- `lit-examples/U1L11LE_lit_example_reader.tex`
- `lit-examples/U1L11LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L11LE/worksheet.tex`
- `../../../graded-assignments/U1L11LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L11LL.md`
- `answer-keys/U1L11LE.md`

## Build commands

Run from this week folder:

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week11_Student_Reading.tex
latexmk -pdf -output-directory=logic-labs -interaction=nonstopmode -halt-on-error logic-labs/U1L11LL_logic_lab.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L11LE_lit_example_reader.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L11LE/worksheet.tex
```

## Verification

Before pushing, run:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Then inspect `pdftotext -layout` output for assignment IDs, question headings, and answer labels on the worksheets.
