# Logic Dungeon Finals

Cumulative puzzle assessments for the `scope_wr121` Whately logic course live in this folder, separate from weekly student readings, Logic Labs, and Lit Examples.

## Sequence

| Assignment | Placement | Title | Status |
|---|---|---|---|
| **U1F1LD** | After Weeks 1–3 | Logic Dungeon I: The Hall of Inscriptions | Built |
| **U1F2LD** | After Weeks 4–6 | Logic Dungeon II: The Surveyor's Rotunda | Built |
| **U1F3LD** | After Weeks 7–9 | Logic Dungeon III: The Court of the False Oracle | Built |
| **U1F4LD** | After Weeks 10–12 | Logic Dungeon IV: The Archive of Broken Proofs | Provisional |
| **U1F5LD** | After Week 17 | Logic Dungeon V: The Gates of Castrum Malae Ratiocinationis | Final cumulative assessment; provisional content |

There is no separate checkpoint after Weeks 13–15. Weeks 13–17 accumulate toward U1F5LD, which precedes the Week 18 portfolio workshop and supplies one possible revision/reflection artifact for the official Logic Portfolio.

## Format

Finals use the established OCR worksheet conventions, with **U1F1LD** on the
Krewone graded-assignments pilot layout:

- Student Name, Student ID, Assignment ID, template revision, and page count on every page
- Registration marks and a per-page QR payload `krewone:v1|assignment=<ID>|revision=<N>|page=<X>`
- Printed prompts as `Question N.M`
- Canonical answer labels `Part X QY` above full-width boxes (shared `latex/grader-worksheet.sty`)
- no shaded answer areas
- no more than two graded prompts per page
- self-contained Markdown key matching the assignment ID

All Logic Dungeon final IDs use the six-character pattern **U1F#LD** so they remain distinct from weekly **U1L#LL** and **U1L#LE** assignments.

## U1F1LD files (grader pilot)

Authoritative sources:

- `../graded-assignments/U1F1LD/worksheet.tex`
- `../graded-assignments/U1F1LD/worksheet.pdf`
- `../graded-assignments/U1F1LD/template.json`
- Answer key: `../answer-keys/U1F1LD.md`
- Index entry: `../graded-assignments.json`
- Pointer: `logic-dungeon-1/README.md`

Build from `graded-assignments/U1F1LD/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
```

Regenerate template metadata from the repository root:

```bash
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1F1LD
```

## U1F2LD files

- `logic-dungeon-2/../../../graded-assignments/U1F2LD/worksheet.tex`
- `logic-dungeon-2/U1F2LD_logic_dungeon_final.pdf`
- Answer key: `../answer-keys/U1F2LD.md`

Build from `finals/logic-dungeon-2/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error ../../../graded-assignments/U1F2LD/worksheet.tex
```

## U1F3LD files

- `logic-dungeon-3/../../../graded-assignments/U1F3LD/worksheet.tex`
- `logic-dungeon-3/U1F3LD_logic_dungeon_final.pdf`
- Answer key: `../answer-keys/U1F3LD.md`
- Lore bible (design, not student-facing): `../docs/lore-court-of-the-false-oracle.md`

Build from `finals/logic-dungeon-3/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error ../../../graded-assignments/U1F3LD/worksheet.tex
```

Validate keys from the repository root:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```
