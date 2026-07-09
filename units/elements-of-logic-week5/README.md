# Elements of Logic — Week 5

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 5 Focus

**The Shape of an Argument — Mood, Figure, and Formal Validity**

Week 5 builds on the practical syllogism maps from Week 4. Students now classify simple categorical syllogisms by mood and figure, using the A/E/I/O proposition forms and the placement of the middle term. The week deliberately keeps traditional mood-and-figure terminology light: students should learn to test form, not memorize every valid medieval mnemonic.

## Included Products

Current build:

- `pdfs/Whately_Logic_Week5_Student_Reading.pdf`
- `pdfs/Whately_Logic_Week5_Julius_Caesar_Lit_Anchor.pdf`
- `pdfs/Whately_Logic_Week5_Teacher_Guide.pdf`
- LaTeX sources in `tex/`
- Source notes in `source-notes/`

Argument labs were removed (fresh worksheet rules TBD).

## Portfolio Artifact

Students produce a **Mood-and-Figure Classification Card**: one valid syllogism, its A/E/I/O mood, S/P/M terms, a simple figure diagram, a form judgment, and a warning about a nearby invalid form.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week5_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week5_Julius_Caesar_Lit_Anchor.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week5_Teacher_Guide.tex
```
