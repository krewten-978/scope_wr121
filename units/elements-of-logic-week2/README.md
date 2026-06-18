# Elements of Logic — Week 2

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 2 Focus

**One Word, Two Ideas: Why Ambiguity Breaks Arguments**

Week 2 builds on the Week 1 four-step argument test by focusing on terms. Students learn that an argument can appear strong when a key word quietly changes meaning. The revised 12th-grade version connects Whately's treatment of terms to recurring Shakespeare anchors from *Macbeth* and *Julius Caesar*.

## Included Products

- `pdfs/Whately_Logic_Week2_Teacher_Guide.pdf`
- `pdfs/Whately_Logic_Week2_Student_Reading.pdf`
- `pdfs/Whately_Logic_Week2_Argument_Lab.pdf`
- LaTeX sources in `tex/`
- Source notes in `source-notes/`

## Portfolio Artifact

Students produce a term investigation: contested word, possible meanings, meaning in the argument, clarified definition, and explanation of how the clarified term changes the argument.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week2_Teacher_Guide.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week2_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week2_Argument_Lab.tex
```
