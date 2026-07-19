# Elements of Logic — Week 14

## Week 14 — Can Logic Discover Anything New?

**Core focus:** reasoning, discovery, proof, observation, testimony, memory, imagination, judgment, and choosing the right intellectual tool.

**Essential question:** Does reasoning discover truth, or does it only arrange what we already know?

## Student-facing materials

- `student-packets/Whately_Logic_Week14_Student_Reading.tex`
- `student-packets/Whately_Logic_Week14_Student_Reading.pdf`
- `logic-labs/U1L14LL_logic_lab.tex`
- `logic-labs/U1L14LL_logic_lab.pdf`
- `lit-examples/U1L14LE_lit_example_reader.tex`
- `lit-examples/U1L14LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L14LE/worksheet.tex`
- `../../../graded-assignments/U1L14LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L14LL.md`
- `answer-keys/U1L14LE.md`

## Build commands

Run from this week folder:

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week14_Student_Reading.tex
latexmk -pdf -output-directory=logic-labs -interaction=nonstopmode -halt-on-error logic-labs/U1L14LL_logic_lab.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L14LE_lit_example_reader.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L14LE/worksheet.tex
```

## Verification

Before pushing, run:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Then inspect `pdftotext -layout` output for assignment IDs, question headings, and answer labels on the worksheets.
