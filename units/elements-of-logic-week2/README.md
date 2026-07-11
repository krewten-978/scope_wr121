# Week 2 — Elements of Logic

## Student packet

- `student-packets/Whately_Logic_Week2_Student_Reading.pdf`

## Logic lab (companion worksheet)

- `logic-labs/U1L2LL_logic_lab.tex`
- `logic-labs/U1L2LL_logic_lab.pdf` — Assignment ID **U1L2LL**


## Lit example (Macbeth application)

- `lit-examples/U1L2LE_lit_example_reader.tex`
- `lit-examples/U1L2LE_lit_example_reader.pdf`
- `lit-examples/U1L2LE_lit_example_worksheet.tex`
- `lit-examples/U1L2LE_lit_example_worksheet.pdf` — Assignment ID **U1L2LE**

Answer key: `answer-keys/U1L2LE.md`

Format rules: `docs/logic-lab-format.md`

Answer key: `answer-keys/U1L2LL.md`

## Build logic lab

From this folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1L2LL_logic_lab.tex
```

## Build lit example

From the repo root:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error units/elements-of-logic-week2/lit-examples/U1L2LE_lit_example_reader.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error units/elements-of-logic-week2/lit-examples/U1L2LE_lit_example_worksheet.tex
```
