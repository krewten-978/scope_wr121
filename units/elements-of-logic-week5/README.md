# Week 5 — Elements of Logic

- Student packet: `student-packets/Whately_Logic_Week5_Student_Reading.pdf`
- **Practice Addendum (high-rep mood/form/validity):** `student-packets/Whately_Logic_Week5_Practice_Addendum.tex` / `.pdf`
- **Practice Addendum Teacher Guide (full key + pacing):** `student-packets/Whately_Logic_Week5_Practice_Addendum_Teacher_Guide.tex` / `.pdf`
- Logic lab: `../../../graded-assignments/U1L5LL/worksheet.tex` / `.pdf` (**U1L5LL**)
- Answer key: `answer-keys/U1L5LL.md`
- Lit Example reader: `lit-examples/U1L5LE_lit_example_reader.tex` / `.pdf` (**U1L5LE**)
- Lit Example worksheet: `../../../graded-assignments/U1L5LE/worksheet.tex` / `.pdf` (**U1L5LE**)
- Lit Example answer key: `answer-keys/U1L5LE.md`

**Suggested path:** Reading → Practice Addendum → Logic Lab U1L5LL → Lit Example.

The Practice Addendum is formative volume practice (not a second AI-graded lab). Barbara / Celarent / Darii / Ferio are taught as the four strong first-figure home-base forms.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week5_Practice_Addendum.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week5_Practice_Addendum_Teacher_Guide.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/../../../graded-assignments/U1L5LL/worksheet.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/U1L5LE_lit_example_reader.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error lit-examples/../../../graded-assignments/U1L5LE/worksheet.tex
```
