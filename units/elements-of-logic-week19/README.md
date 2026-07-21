# Elements of Logic — Week 19

## Week 19 — Final Portfolio Defense

**Core focus:** defining disciplined thought, making a controlling claim, using artifacts as evidence, stating warrants, testing the defense, qualifying honestly, and transferring one habit beyond the course.

**Essential question:** What does it mean to be a disciplined thinker?

## Student-facing materials

- `student-packets/Whately_Logic_Week19_Student_Reading.tex`
- `student-packets/Whately_Logic_Week19_Student_Reading.pdf`
- `../../../graded-assignments/U1L19LL/worksheet.tex`
- `../../../graded-assignments/U1L19LL/worksheet.pdf`
- `lit-examples/U1L19LE_lit_example_reader.tex`
- `lit-examples/U1L19LE_lit_example_reader.pdf`
- `../../../graded-assignments/U1L19LE/worksheet.tex`
- `../../../graded-assignments/U1L19LE/worksheet.pdf`

## Answer keys

- `answer-keys/U1L19LL.md`
- `answer-keys/U1L19LE.md`

## Final defense requirements

The `U1L19LL` defense uses at least three portfolio artifacts, including at least one substantively revised artifact and one *Macbeth* or *Julius Caesar* application. It includes a qualification and a concrete transfer beyond the unit.

## Graded-assignment packaging (Krewone)

Authoritative gradable worksheets live only under:

- `graded-assignments/U1L19LL/{worksheet.tex,worksheet.pdf,template.json}`
- `graded-assignments/U1L19LE/{worksheet.tex,worksheet.pdf,template.json}`

The LE reader remains in `lit-examples/`; no legacy worksheet authority belongs in the unit folder.

## Build commands

```bash
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week19_Student_Reading.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L19LE_lit_example_reader.tex
cd ../../../graded-assignments/U1L19LL && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
cd ../U1L19LE && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
# from repo root:
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L19LL
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L19LE
```

## Verification

Run both answer-key validators and confirm every graded page has the Krewone header, registration marks, a QR payload that decodes at 150 DPI, and canonical `Part N QN` answer boxes.
