# Logic Dungeon Finals

Cumulative puzzle assessments for the `scope_wr121` Whately logic course live in this folder, separate from weekly student readings, Logic Labs, and Lit Examples.

## Sequence

| Assignment | Placement | Title | Status |
|---|---|---|---|
| **U1F1** | After Weeks 1–3 | Logic Dungeon I: The Hall of Inscriptions | Prototype built |
| **U1F2LD** | After Weeks 4–6 | Logic Dungeon II: The Syllogism Labyrinth | Built |
| **U1F3LD** | After Weeks 7–9 | Logic Dungeon III: The Court of the False Oracle | Provisional |
| **U1F4LD** | After Weeks 10–12 | Logic Dungeon IV: The Archive of Broken Proofs | Provisional |
| **U1F5LD** | After Week 17 | Logic Dungeon V: The Gates of Castrum Malae Ratiocinationis | Final cumulative assessment; provisional content |

There is no separate checkpoint after Weeks 13–15. Weeks 13–17 accumulate toward U1F5LD, which precedes the Week 18 portfolio workshop and supplies one possible revision/reflection artifact for the official Logic Portfolio.

## Format

Finals use the established OCR worksheet conventions:

- Assignment ID and page count in every header
- `Part X QY` prompts
- exact `Part X QY ANSWER BOX` labels above full-width boxes
- no shaded answer areas
- no more than two graded prompts per page
- self-contained Markdown key matching the assignment ID

Beginning with Logic Dungeon II, final IDs use the six-character pattern **U1F#LD** so they remain distinct from weekly **U1L#LL** and **U1L#LE** assignments. U1F1 retains its original prototype ID.

## U1F1 files

- `logic-dungeon-1/U1F1_logic_dungeon_final.tex`
- `logic-dungeon-1/U1F1_logic_dungeon_final.pdf`
- Answer key: `../answer-keys/U1F1.md`

Build from `finals/logic-dungeon-1/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error U1F1_logic_dungeon_final.tex
```

## U1F2LD files

- `logic-dungeon-2/U1F2LD_logic_dungeon_final.tex`
- `logic-dungeon-2/U1F2LD_logic_dungeon_final.pdf`
- Answer key: `../answer-keys/U1F2LD.md`

Build from `finals/logic-dungeon-2/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error U1F2LD_logic_dungeon_final.tex
```

Validate keys from the repository root:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```
