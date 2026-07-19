# Week 7 — Elements of Logic

- Student packet: `student-packets/Whately_Logic_Week7_Student_Reading.tex` / `.pdf`
- Logic lab: `../../../graded-assignments/U1L7LL/worksheet.tex` / `.pdf` (**U1L7LL**)
- Answer key: `answer-keys/U1L7LL.md`
- Lit Example reader: `lit-examples/U1L7LE_lit_example_reader.tex` / `.pdf` (**U1L7LE**)
- Lit Example worksheet: `../../../graded-assignments/U1L7LE/worksheet.tex` / `.pdf` (**U1L7LE**)
- Lit Example answer key: `answer-keys/U1L7LE.md`

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week7_Student_Reading.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/../../../graded-assignments/U1L7LL/worksheet.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/U1L7LE_lit_example_reader.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L7LE/worksheet.tex
```
