# Week 6 — Elements of Logic

- Student packet: `student-packets/Whately_Logic_Week6_Student_Reading.pdf`
- Logic lab: `logic-labs/U1L6LL_logic_lab.tex` / `.pdf` (**U1L6LL**)
- Answer key: `answer-keys/U1L6LL.md`
- Lit Example reader: `lit-examples/U1L6LE_lit_example_reader.tex` / `.pdf` (**U1L6LE**)
- Lit Example worksheet: `../../../graded-assignments/U1L6LE/worksheet.tex` / `.pdf` (**U1L6LE**)
- Lit Example answer key: `answer-keys/U1L6LE.md`

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1L6LL_logic_lab.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/U1L6LE_lit_example_reader.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L6LE/worksheet.tex
```
