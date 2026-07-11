# Answer keys (`answer-keys/`)

Markdown rubrics for the krewone-style AI student evaluator. File names match **Assignment ID** on student PDFs:

- `U#L#LL.md` — logic lab (paired `logic-labs/U#L#LL_logic_lab`)
- `U#L#LE.md` — lit example worksheet (paired `lit-examples/U#L#LE_lit_example_worksheet`; **do not** use Lit Anchor / `LA` / `AW` naming)
- `U1F#.md` — Logic Dungeon final (paired student artifact under `finals/`; final IDs remain distinct from weekly lesson IDs)

Same heading contract as `scope_tenth/answer-keys/README.md`.

## Grader heading contract (required)

Every **gradable** question section must use this exact heading shape:

```markdown
## Question N: Part X QY – Question Title (Z points)
```

Rules:

1. Start with `## Question N:` (N = 1, 2, 3… **sequential within the file**).
2. Include the worksheet label `Part X QY` (same as the logic lab).
3. Include point value in parentheses: `(2 points)`, `(4 points)`, etc.
4. **Invalid:** `## Part 1 Q1 – …` without `Question N:` — the grader will not parse it.

Below each gradable heading, keep: **Expected Answer**, **Rubric**, **Notes for grading**.

## Before commit

From repo root:

```bash
python3 scripts/validate-answer-key-headings.py answer-keys
python3 scripts/audit-answer-key-totals.py answer-keys
```

Both must exit 0 when adding or editing keys.

## Authoring

- **scope_wr121 logic labs (start here):** `docs/logic-lab-authoring-guide.md`
- Layout / pedagogy summary: `docs/logic-lab-format.md`
- Hermes skill: `logic-labs` (high-level; repo guide wins for WR121)
- Focus-lab reference (layout only): `classical-unit-engine` → `references/focus-lab-answer-keys.md`

Student worksheets show **Part X QY** only; `Question N` exists in the key for the evaluator, not on the PDF.