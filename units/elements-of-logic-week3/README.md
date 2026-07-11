# Week 3 — Elements of Logic

## Student packet

- `student-packets/Whately_Logic_Week3_Student_Reading.pdf`

## Logic lab (companion worksheet)

- `logic-labs/U1L3LL_logic_lab.tex`
- `logic-labs/U1L3LL_logic_lab.pdf` — Assignment ID **U1L3LL**


## Lit example (Macbeth application)

- `lit-examples/U1L3LE_lit_example_reader.tex`
- `lit-examples/U1L3LE_lit_example_reader.pdf`
- `lit-examples/U1L3LE_lit_example_worksheet.tex`
- `lit-examples/U1L3LE_lit_example_worksheet.pdf` — Assignment ID **U1L3LE**

Answer key: `answer-keys/U1L3LE.md`

Format rules: `docs/logic-lab-format.md`

Answer key: `answer-keys/U1L3LL.md`

## Build logic lab

From this folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1L3LL_logic_lab.tex
```

## Build lit example

From the repo root:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error units/elements-of-logic-week3/lit-examples/U1L3LE_lit_example_reader.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error units/elements-of-logic-week3/lit-examples/U1L3LE_lit_example_worksheet.tex
```
