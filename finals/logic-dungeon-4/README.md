# Logic Dungeon IV — The Archive of Broken Proofs

Authoritative U1F4LD files:

- `../../graded-assignments/U1F4LD/worksheet.tex`
- `../../graded-assignments/U1F4LD/worksheet.pdf`
- `../../graded-assignments/U1F4LD/template.json`
- `../../answer-keys/U1F4LD.md`
- Lore bible: `../../docs/lore-archive-of-broken-proofs.md`

Build from `graded-assignments/U1F4LD/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
```

Regenerate the grader template from the repository root:

```bash
.venv-grader/bin/python scripts/build-grader-templates.py --assignment U1F4LD
```
