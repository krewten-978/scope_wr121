# Week 10 — Elements of Logic

- Student packet: `student-packets/Whately_Logic_Week10_Student_Reading.tex` / `.pdf`
- Logic lab: `../../../graded-assignments/U1L10LL/worksheet.tex` / `.pdf` (**U1L10LL**)
- Answer key: `answer-keys/U1L10LL.md`
- Lit Example reader: `lit-examples/U1L10LE_lit_example_reader.tex` / `.pdf` (**U1L10LE**)
- Lit Example worksheet: `../../../graded-assignments/U1L10LE/worksheet.tex` / `.pdf` (**U1L10LE**)
- Lit Example answer key: `answer-keys/U1L10LE.md`
- Short paper: `../../papers/U1L10SP/assignment.tex` / `.pdf` (**U1L10SP**)
- Short-paper text supplement: `../../papers/U1L10SP/text-supplement.tex` / `.pdf`

`U1L10SP` is a closed-world, handwritten 1–2 page paper asking whether Brutus proves Caesar must die or only that Caesar might become dangerous. It is not a Krewone worksheet and has no template or AI answer key.

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week10_Student_Reading.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/../../../graded-assignments/U1L10LL/worksheet.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/U1L10LE_lit_example_reader.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L10LE/worksheet.tex
```
