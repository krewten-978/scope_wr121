# Logic lab authoring guide (scope_wr121)

**Audience:** Humans and AI agents creating new Whately logic labs in a fresh context. Read this file first; then `docs/logic-lab-format.md` and `answer-keys/README.md`.

## Product line (do not confuse with scope_tenth)

| | scope_tenth | scope_wr121 |
|---|-------------|-------------|
| Worksheet | Focus lab / origin ladder | **Logic lab (LL)** |
| ID pattern | `U#L#FL`, `U#L#OL` | **`U#L#LL`** (e.g. `U1L3LL` = unit 1, lesson/week 3) |
| Pedagogy | Literary reading + focus questions | **Fresh argument practice** tied to weekly Whately reading skill |
| Rule doc | `focus-lab-ocr-optimized-format.md` | **This repo** — do not merge rule sets |

**Retired in scope_wr121:** Argument Lab (`AL`), Anchor Worksheet (`AW`), `lit-anchors` skill, `docs/lit-anchor-format.md`. Do not recreate.

## Repo layout per week

```
units/elements-of-logic-weekN/
  student-packets/Whately_Logic_WeekN_Student_Reading.pdf
  logic-labs/U1LNLL_logic_lab.tex
  logic-labs/U1LNLL_logic_lab.pdf
  README.md
answer-keys/U1LNLL.md
```

Copy LaTeX shell from an existing lab (e.g. `units/elements-of-logic-week3/logic-labs/U1L3LL_logic_lab.tex`): `article` 12pt, geometry, `fancyhdr` with **Student Name** + **Assignment ID: U1LNLL** + **Page X of Y**, `\answerbox{Part X QY ANSWER BOX}{height}`, numbered **Parts**, bold **Part X QY:** prompts.

**OCR rules:** Label **above** each box exactly `Part X QY ANSWER BOX`. No colored backgrounds. Prefer ≤2 graded prompts per page; `\newpage` between pairs when needed.

## Pedagogy

1. **Transfer, not recap** — Practice the **week’s reading skill** on **new** sentences/scenarios. Do **not** reuse the handout’s worked examples (e.g. Week 2: no bank/liberal/equal/tolerance from the packet; Week 4: no copy-paste Socrates/Macbeth syllogism from the reading).
2. **Difficulty ramp** — Easier identification → harder multi-step (paragraph extraction, fix term, validity + facts).
3. **Prompts without clues** — Do not tell students which word shifts, which fallacy name applies, or “textbook case (light as weight).” Give the sentence/argument and the task only. See `U1L2LL` after `dd22afd` for the intended tone.
4. **Quality examples** — Prefer arguments/sentences used in logic teaching (undistributed middle: maples/oaks/trees; two negatives; feathers/light; right/right; only-X-may-Y translation). Modernize wording; do not paste copyrighted blocks. Avoid **artificial** equivocation no one would say (“the song is cold”).
5. **Purpose line** — One short line: apply Week N skills; do not copy handout examples.

## Part 5: Review (required from Week 2 onward)

- Final part: **2–3 questions** reusing **earlier weeks only**.
- **Never** review the **current** week’s main skill on the same worksheet (e.g. Week 3 lab must not review A/E/I/O in Part 5 if that is the week’s focus — user removed U1L3LL Part 5 Q3 for this reason).
- Use **new** wording, not copies of prior worksheet prompts.
- Typical mix: Week 1 four-step; Week 2 equivocation; Week 3 proposition form; Week 4 syllogism map; Week 5 validity — pick 2–3 as appropriate.

## Answer keys (Python grader)

- File: `answer-keys/U1LNLL.md`
- **Must match scope_tenth** heading shape:

  `## Question N: Part X QY – Title (Z points)`

- Sequential `Question 1…N` in file order (not necessarily same as Part order if you renumber — keep consistent with grader).
- Sections: **Expected Answer**, **Rubric**, **Notes for grading** (optional).
- `**Total Points:**` must equal sum of all `(Z points)` in `## Question` headings.
- Model answers must match **worksheet prompts only** (not reading handout text students weren’t asked to quote).

Validate before commit:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Reference: `scope_tenth/answer-keys/README.md`, `~/.hermes/skills/productivity/classical-unit-engine/references/focus-lab-answer-keys.md` (structure only).

## Build PDF

From `units/elements-of-logic-weekN/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error logic-labs/U1LNLL_logic_lab.tex
```

Do not commit `*.aux`, `*.log`, `*.fls`, `*.fdb_latexmk`, `*.out` (see root `.gitignore`).

## Weekly skill map (pair lab to reading)

| Week | ID | Reading focus (lab should practice fresh examples) |
|------|-----|-----------------------------------------------------|
| 1 | U1L1LL | Four-step argument test (conclusion, reason, assumption, follows) |
| 2 | U1L2LL | Terms, ambiguity, equivocation, fix the term |
| 3 | U1L3LL | Propositions, A/E/I/O, translation, distribution, quantity clarity |
| 4 | U1L4LL | Syllogism map: premises, conclusion, middle/major/minor |
| 5 | U1L5LL | Mood, formal validity / invalidity (undistributed middle, two negatives, illicit process) |
| 6 | U1L6LL | Form test vs fact test, soundness, valid-but-unsound, weak proof |
| 7 | U1L7LL | Fallacy as appearance of proof; false claim vs bad inference; emotional/rhetorical force; fallacy autopsy |

Read `student-packets/Whately_Logic_WeekN_Student_Reading.pdf` (pdftotext) before authoring.

## Point totals

- Recent labs use **12** or **14** points; common pattern **12** with 8–10 gradable boxes.
- Whole points only in rubrics.
- Align worksheet box count with answer key question count.

## Git / review

- Branch: `main` on `krewten-978/scope_wr121`.
- Commit: `.tex`, `.pdf`, `answer-keys/U1LNLL.md`, week `README.md`, doc updates if rules change.
- User expects **push to main** for review after completion.

## AI checklist (new context)

1. Read this guide + week N student PDF (skills, not example sentences to copy).
2. Read prior week’s lab for Part 5 review eligibility.
3. Copy `U1L3LL_logic_lab.tex` (or latest week) → new `U1LNLL_logic_lab.tex`; change ID, title, parts.
4. Write `answer-keys/U1LNLL.md` with `Question N: Part X QY` headings.
5. Run both validation scripts (exit 0).
6. Build PDF; commit; push `main`.
7. Do not add instructional spoilers in prompts; do not put current-week skills in Part 5 review.

## Hermes

- Skill: `logic-labs` (productivity) — high-level; **this file is authoritative** for scope_wr121 specifics.
- Layout reference: `classical-unit-engine` → `focus-lab-standard.tex`, `focus-lab-ocr-optimized-format.md` (scope_tenth).

## Completed reference implementations

| ID | Commit era | Notes |
|----|------------|--------|
| U1L1LL | Part 4 paragraph dissect | Week 1 baseline |
| U1L2LL | `edf669d` / `dd22afd` | Standard equivocation examples; minimal prompts |
| U1L3LL | `41f9cfb` | Part 5 = 2 review items only (no current-week syllogism review) |
| U1L4LL–U1L6LL | `d6531da` | Weeks 4–6 complete |
| U1L7LL / U1L7LE | Week 7 | Fallacy intro + Macbeth LE |