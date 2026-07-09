# Logic Lab Format — scope_wr121

Logic labs are companion worksheets for Whately student reading handouts. They use the same OCR-oriented layout as scope_tenth focus labs, but they are a **separate** product line with their own IDs and pedagogy.

## Assignment ID

- Pattern: **U# L# LL** (Logic Lab).
- Example: **U1L1LL** = Unit/Week 1, Lesson 1, Logic Lab.
- Header on every page: `Student Name:` (empty space, no underline) `Assignment ID: U# L# LL` `Page X of Y`.

## Layout (matches focus-lab OCR standard)

- Plain bold label **above** each box: `Part # Q# ANSWER BOX`.
- Full-width empty `\answerbox` frames; no background colors on the worksheet.
- Numbered **Parts** with **Part X QY** prompts.
- No window notes, drawings, or picture tasks.
- Prefer no more than two graded prompts per page; use `\newpage` between pairs when needed.

## Pedagogy

- Transfer the week's logic habit into **fresh** sentences and scenarios—not recap or summary of the reading.
- Do not reuse the reading handout's worked examples; build new practice material.
- Start with easier identification tasks; increase difficulty (full four-step test, weaker assumptions, original argument + self-diagnosis).
- Real-world, school, civic, and everyday arguments are preferred unless the week targets literary application elsewhere.

## Repo layout

- Per week folder: `logic-labs/U#L#L_logic_lab.tex` and matching `.pdf`.
- Keep student reading handouts in `tex/`; logic labs stay in `logic-labs/`.

## Related

- scope_tenth: `focus-lab-ocr-optimized-format.md` (layout reference only; do not merge rule sets or FL IDs).