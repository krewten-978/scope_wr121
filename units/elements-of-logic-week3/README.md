# Elements of Logic — Week 3

## Unit Working Title

**Thinking Straight: Richard Whately and the Art of Reasoning**

## Week 3 Focus

**What We Say and What We Mean: Propositions and Clear Claims**

Week 3 moves from terms to propositions. Students identify subject, predicate, quality, quantity, and the A/E/I/O forms of categorical propositions. A key habit is spotting overreaches in scope: "All" or "None" when only "Some" holds, or unsupported "Most." The test uses four category riddles (Mammals, Birds, Insects, Planets) in the voice of a Department of Science professor asking students to locate where her statements go wrong. The revised 12th-grade version corrects the O-proposition distribution rule and connects proposition work to recurring Shakespeare anchors from *Macbeth* and *Julius Caesar*.

The Macbeth lit-anchor for this week focuses on the manhood exchange in *Macbeth* Act 1, Scene 7 and the banquet scene in Act 3, Scene 4. Students translate claims such as “When you durst do it, then you were a man,” “Who dares do more is none,” and “What man dare, I dare” into clear propositions so they can test what the play is really claiming about courage, murder, fear, and moral limits.

## Included Products

- `pdfs/Whately_Logic_Week3_Teacher_Guide.pdf`
- `pdfs/Whately_Logic_Week3_Student_Reading.pdf`
- `pdfs/Whately_Logic_Week3_Logic_Test.pdf`
- `pdfs/Whately_Logic_Week3_Macbeth_Lit_Anchor.pdf`
- LaTeX sources in `tex/`
- Source notes in `source-notes/`

Argument labs were removed (fresh worksheet rules TBD).

## Portfolio Artifact

Students produce a proposition translation/window note: ordinary sentence, standard form, subject and predicate, quality and quantity, and explanation of how the clearer proposition can be supported or challenged. The test additionally practices identifying and repairing scope errors in AEIO claims ("All," "None," or "Most" overreaches).

The lit-anchor adds a Macbeth proposition translation chart focused on one Shakespeare line or claim about manhood, courage, fear, or guilt.

## Build

From this folder:

```bash
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Teacher_Guide.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Student_Reading.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Logic_Test.tex
latexmk -pdf -lualatex -interaction=nonstopmode -halt-on-error -outdir=pdfs tex/Whately_Logic_Week3_Macbeth_Lit_Anchor.tex
```
