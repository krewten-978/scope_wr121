# Elements of Logic — Week 13

## Week 13 — Whom Should We Trust?

**Core focus:** testimony, authority, credibility, access, relevant expertise, bias, corroboration, probability, and careful trust judgments.

**Essential question:** When should we trust a source?

## Student-facing materials

- `student-packets/Whately_Logic_Week13_Student_Reading.tex`
- `student-packets/Whately_Logic_Week13_Student_Reading.pdf`
- `../../../graded-assignments/U1L13LL/worksheet.tex`
- `../../../graded-assignments/U1L13LL/worksheet.pdf`
- `lit-examples/U1L13LE_lit_example_reader.tex`
- `lit-examples/U1L13LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L13LE/worksheet.tex`
- `../../../graded-assignments/U1L13LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L13LL.md`
- `answer-keys/U1L13LE.md`

## Build commands

Run from this week folder:

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week13_Student_Reading.tex
latexmk -pdf -output-directory=logic-labs -interaction=nonstopmode -halt-on-error logic-labs/../../../graded-assignments/U1L13LL/worksheet.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L13LE_lit_example_reader.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L13LE/worksheet.tex
```

## Verification

Before pushing, run:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Then inspect `pdftotext -layout` output for assignment IDs, question headings, and answer labels on the worksheets.
