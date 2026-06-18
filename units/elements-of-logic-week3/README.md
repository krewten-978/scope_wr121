# Elements of Logic — Week 3

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 3 Focus

**What We Say and What We Mean: Propositions and Clear Claims**

Week 3 moves from terms to propositions. Students identify subject, predicate, quality, quantity, and the A/E/I/O forms of categorical propositions. The revised 12th-grade version corrects the O-proposition distribution rule and connects proposition work to recurring Shakespeare anchors from *Macbeth* and *Julius Caesar*.

## Included Products

- `pdfs/Whately_Logic_Week3_Teacher_Guide.pdf`
- `pdfs/Whately_Logic_Week3_Student_Reading.pdf`
- `pdfs/Whately_Logic_Week3_Argument_Lab.pdf`
- LaTeX sources in `tex/`
- Source notes in `source-notes/`

## Portfolio Artifact

Students produce a proposition translation/window note: ordinary sentence, standard form, subject and predicate, quality and quantity, and explanation of how the clearer proposition can be supported or challenged.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Teacher_Guide.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Argument_Lab.tex
```
