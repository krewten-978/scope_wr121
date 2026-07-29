# Week 6B — Elements of Logic (**optional enrichment**)

**Status:** Materials are built and kept in the repo for review, but Week 6B is **not** on the default required course path.

The default sequence remains **Week 6 → Week 7** (form/fact → fallacies). Use 6B only if you deliberately want a compound-inference stretch (advanced track, optional project, or future reconsideration).

Does **not** renumber Weeks 7–19. Does **not** alter existing Week 6 materials or Logic Dungeons. Later weeks do **not** assume 6B vocabulary.

## Focus (if taught)

Either/or (disjunction, disjunctive syllogism, false choice) and if/then (antecedent/consequent, valid moves, affirming the consequent, denying the antecedent), still under Whately’s form test and fact test.

## Student-facing materials

- `student-packets/Whately_Logic_Week6B_Student_Reading.tex`
- `student-packets/Whately_Logic_Week6B_Student_Reading.pdf`
- `../../../graded-assignments/U1L6BLL/worksheet.tex` / `.pdf` (**U1L6BLL**)
- `lit-examples/U1L6BLE_lit_example_reader.tex` / `.pdf`
- `../../../graded-assignments/U1L6BLE/worksheet.tex` / `.pdf` (**U1L6BLE**)

## Answer keys

- `answer-keys/U1L6BLL.md` (16 points)
- `answer-keys/U1L6BLE.md` (16 points)

## Graded-assignment packaging (Krewone)

Authoritative gradable worksheets live only under:

- `graded-assignments/U1L6BLL/{worksheet.tex,worksheet.pdf,template.json}`
- `graded-assignments/U1L6BLE/{worksheet.tex,worksheet.pdf,template.json}`

LE **reader** stays in `lit-examples/`. No dungeon changes in this week.

## Suggested path (only if offering 6B)

Reading → Logic Lab **U1L6BLL** → Lit Example reader + **U1L6BLE**.

## Source note

Whately voice and structure; compound-form pedagogy adapted from Matthew Knachel, *Fundamental Methods of Logic* (CC BY 4.0), Chapter 4. Credit appears on the student reading.

## Build commands

```bash
# from units/elements-of-logic-week6b/
latexmk -lualatex -output-directory=student-packets -interaction=nonstopmode -halt-on-error student-packets/Whately_Logic_Week6B_Student_Reading.tex
latexmk -pdf -output-directory=lit-examples -interaction=nonstopmode -halt-on-error lit-examples/U1L6BLE_lit_example_reader.tex

# from repo root
cd graded-assignments/U1L6BLL && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
cd ../U1L6BLE && latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
cd ../..
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L6BLL
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1L6BLE
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```
