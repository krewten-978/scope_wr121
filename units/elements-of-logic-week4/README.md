# Elements of Logic — Week 4

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 4 Focus

**Because: How Syllogisms Work — Two Claims and a Conclusion**

Week 4 moves from individual propositions to practical syllogism structure. Students identify two premises, a conclusion, major/minor/middle terms, and the role of the middle term as the bridge or medium of proof. This week intentionally stops short of full mood-and-figure classification; Week 5 will take up formal validity more directly.

## Included Products

Current build:

- `pdfs/Whately_Logic_Week4_Student_Reading.pdf`
- `pdfs/Whately_Logic_Week4_Argument_Lab.pdf`
- `pdfs/Whately_Logic_Week4_Julius_Caesar_Lit_Anchor.pdf`
- `pdfs/Whately_Logic_Week4_Teacher_Guide.pdf`
- LaTeX sources in `tex/`
- Source notes in `source-notes/`

## Portfolio Artifact

Students produce a practical syllogism map: major premise, minor premise, conclusion, major term, minor term, middle term, and a short judgment about whether the middle term really connects the conclusion. The lab includes a four-window note titled **Two Claims and a Conclusion**. The lit-anchor adds a **Julius Caesar Practical Syllogism Map** focused on Brutus's serpent's egg argument and Cassius's Colossus argument.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week4_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week4_Argument_Lab.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week4_Julius_Caesar_Lit_Anchor.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week4_Teacher_Guide.tex
```
