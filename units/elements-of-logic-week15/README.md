# Elements of Logic — Week 15

## Week 15 — Are We Actually Disagreeing?

**Core focus:** verbal disputes, real disputes, mixed disputes, contested terms, definitions, shared claims, remaining disagreement, and dispute maps.

**Essential question:** How can we tell whether people disagree about reality or only about words?

## Student-facing materials

- `student-packets/Whately_Logic_Week15_Student_Reading.tex`
- `student-packets/Whately_Logic_Week15_Student_Reading.pdf`
- `logic-labs/U1L15LL_logic_lab.tex`
- `logic-labs/U1L15LL_logic_lab.pdf`
- `lit-examples/U1L15LE_lit_example_reader.tex`
- `lit-examples/U1L15LE_lit_example_reader.pdf`
- `lit-examples/U1L15LE_lit_example_worksheet.tex`
- `lit-examples/U1L15LE_lit_example_worksheet.pdf`

## Answer keys

- `answer-keys/U1L15LL.md`
- `answer-keys/U1L15LE.md`

## Build commands

Run from this week folder:

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week15_Student_Reading.tex
latexmk -pdf -output-directory=logic-labs -interaction=nonstopmode -halt-on-error logic-labs/U1L15LL_logic_lab.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L15LE_lit_example_reader.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L15LE_lit_example_worksheet.tex
```

## Verification

Before pushing, run:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Then inspect `pdftotext -layout` output for assignment IDs, question headings, and answer labels on the worksheets.
