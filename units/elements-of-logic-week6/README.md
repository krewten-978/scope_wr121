# Elements of Logic — Week 6

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 6 Focus

**Good Form, Bad Facts — Valid Does Not Mean True**

Week 6 builds on the mood-and-figure work from Week 5. Students now distinguish formal validity from truth and soundness. A valid argument can still fail if a premise is false or unproved; a true conclusion can also be badly proved. The week trains students to diagnose arguments using two questions: the form test and the fact test.

## Included Products

Current build:

- `pdfs/Whately_Logic_Week6_Student_Reading.pdf`
- `pdfs/Whately_Logic_Week6_Julius_Caesar_Lit_Anchor.pdf`
- `pdfs/Whately_Logic_Week6_Teacher_Guide.pdf`
- LaTeX sources in `tex/`
- Source notes in `source-notes/`

Argument labs were removed (fresh worksheet rules TBD).

## Portfolio Artifact

Students produce a **Form Test / Fact Test Diagnosis**: argument, conclusion, form judgment, fact judgment, pressure-point premise, final diagnosis, and one sentence explaining why validity alone is not enough.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week6_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week6_Julius_Caesar_Lit_Anchor.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week6_Teacher_Guide.tex
```
