# Elements of Logic — Week 1 Test Run

This repository contains the first-week opening for a 12th-grade long logic unit based on Richard Whately's *Elements of Logic*.

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 1 Focus

**Logic Is Not Magic: What Logic Can and Cannot Do**

Students begin by reading a modernized, student-facing adaptation drawn heavily from Whately's introduction to *Elements of Logic*. The week establishes logic as a discipline for examining reasoning, not as a machine that automatically discovers truth or makes people wise. In the revised long-unit plan, students also begin applying Whately's method to recurring Shakespeare anchors: *Macbeth* and *Julius Caesar*.

## Included Products

- `pdfs/Whately_Logic_Week1_Teacher_Guide.pdf`
- `pdfs/Whately_Logic_Week1_Student_Reading.pdf`
- `logic-labs/U1L1LL_logic_lab.pdf` (Week 1 logic lab companion)
- `pdfs/Whately_Logic_Week1_Macbeth_Lit_Anchor.pdf`
- `pdfs/Whately_Logic_Week1_Logic_Test.pdf`
- LaTeX sources in `tex/`
- Logic lab sources in `logic-labs/`
- Source notes in `source-notes/`

Logic lab format: `docs/logic-lab-format.md` (Assignment ID **U# L# LL**).

## Source Base

Primary source: Richard Whately, *Elements of Logic*, public-domain editions available through Internet Archive. Week 1 draws chiefly from the Introduction, especially Whately's definition of logic as the science and art of reasoning and his defense of logic against exaggerated expectations.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week1_Teacher_Guide.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week1_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week1_Macbeth_Lit_Anchor.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week1_Logic_Test.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1L1LL_logic_lab.tex
```
