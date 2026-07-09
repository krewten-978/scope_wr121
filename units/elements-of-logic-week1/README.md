# Week 1 — Elements of Logic

## Student packet

- `student-packets/Whately_Logic_Week1_Student_Reading.pdf`

## Logic lab (companion worksheet)

- `logic-labs/U1L1LL_logic_lab.tex`
- `logic-labs/U1L1LL_logic_lab.pdf` — Assignment ID **U1L1LL**

Format rules: `docs/logic-lab-format.md`

## Build logic lab

From this folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1L1LL_logic_lab.tex
```