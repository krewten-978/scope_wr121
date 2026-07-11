# Week 1 — Elements of Logic

## Student packet

- `student-packets/Whately_Logic_Week1_Student_Reading.pdf`

## Logic lab (companion worksheet)

- `logic-labs/U1L1LL_logic_lab.tex`
- `logic-labs/U1L1LL_logic_lab.pdf` — Assignment ID **U1L1LL**

## Lit example (Macbeth application)

- `lit-examples/U1L1LE_lit_example_reader.tex`
- `lit-examples/U1L1LE_lit_example_reader.pdf`
- `lit-examples/U1L1LE_lit_example_worksheet.tex`
- `lit-examples/U1L1LE_lit_example_worksheet.pdf` — Assignment ID **U1L1LE**

Answer key: `answer-keys/U1L1LE.md`

Format rules: `docs/logic-lab-format.md`

Answer key: `answer-keys/U1L1LL.md` — validate with `python3 scripts/validate-answer-key-headings.py answer-keys` from repo root.

## Build logic lab

From this folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1L1LL_logic_lab.tex
```

## Build lit example

From the repo root:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error units/elements-of-logic-week1/lit-examples/U1L1LE_lit_example_reader.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error units/elements-of-logic-week1/lit-examples/U1L1LE_lit_example_worksheet.tex
```