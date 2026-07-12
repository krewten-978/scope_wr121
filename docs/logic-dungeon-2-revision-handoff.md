# Fresh-Context Handoff: Logic Dungeon II (current built state)

## Status

Logic Dungeon II has been rewritten as an authentic four-route mystery set in the **Surveyor's Rotunda**. The culminating safe route is **Rootbridge Path**, not Lantern Gallery.

## Files

- Student final: `finals/logic-dungeon-2/U1F2LD_logic_dungeon_final.tex`
- Generated PDF: `finals/logic-dungeon-2/U1F2LD_logic_dungeon_final.pdf` (9 pages)
- Evaluator key: `answer-keys/U1F2LD.md` (**56** points)
- Assignment ID: **U1F2LD**

## Lore and route design

Setting: Surveyor's Rotunda after the Hall of Inscriptions; four routes toward the Upper Archive of *Castrum Malae Ratiocinationis*.

| Route | Surface appeal | Logical profile | Final diagnosis |
|---|---|---|---|
| **Raven Stair** | Official scholarly stair, seals, recent shoring | AAA Figure 1 valid; seal premise undermined by Mason Ledger B | Valid but not sound / not proved safe |
| **Well Passage** | Cold moving air | AAA Figure 2 invalid (undistributed middle); true cold air explained by ice cistern C | Invalid with true observation; moisture risk |
| **Lantern Gallery** | Blue survey thread, professional look | AAA Figure 1 valid; minor doubtful early; Record E undermines full-company safety after collapse re-thread | Valid but not sound for safety |
| **Rootbridge Path** | Water, pits, insects, panic warnings | Early scare arguments fail (two negatives; undistributed middle). Records F/G establish sound AAA Figure 1 safety syllogism; H removes insect distractor | **Sound under the records; best-supported safest path** |

## Station pattern preserved

Each station: (1) graded form/fact logic analysis, (2) expedition consequence. Cumulative chart in Part 7; final movement plan and guide-repair in Part 8. Delayed discovery: Rootbridge looks worst early and only becomes sound after recovered fragments.

## Weeks 4–6 coverage

- premises/conclusion; S/P/M; mood/figure
- AAA Figures 1 and 2; undistributed middle; two negative premises
- form test vs fact test; pressure points; validity/soundness
- true observation inside bad proof; valid form with undermined premises

## Verification commands

```bash
cd finals/logic-dungeon-2
latexmk -pdf -interaction=nonstopmode -halt-on-error U1F2LD_logic_dungeon_final.tex
pdftotext -layout U1F2LD_logic_dungeon_final.pdf -
# check same-page Part X QY / ANSWER BOX; no blank content pages

cd ../..
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

## Quality notes

- Keep one primary logic skill per station plus one short consequence question.
- Do not announce that Rootbridge is correct before the chart/final.
- Distinguish best-supported safe path from guaranteed free of every hazard.
- Carry-forward grading: score early errors once.
- Clean LaTeX aux before commit; ship `.tex` + `.pdf` + key only.
