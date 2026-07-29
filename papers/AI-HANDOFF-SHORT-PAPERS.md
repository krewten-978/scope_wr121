# AI Handoff — `scope_wr121` Handwritten Short Papers

Use this document when asking an AI to build the remaining short-paper assignments for `/home/tcoop/scope_wr121`.

## Reusable instruction to the next AI

> Work in `/home/tcoop/scope_wr121`. Read `papers/AI-HANDOFF-SHORT-PAPERS.md` and inspect the complete model under `papers/U1L6SP/`. Build only the next requested short paper, including its neutral textual-evidence supplement. Compile and visually inspect every page, update the relevant README files, commit the complete `.tex` + `.pdf` artifacts, and push `main` for review. Do not alter existing assignments unless required for a pointer or explicitly authorized.

Build and review **one paper at a time**. Do not bulk-build the entire sequence in one commit unless Wayne explicitly asks.

---

## 1. Why these papers exist

`scope_wr121` is a writing course using Whately's logic as a thinking spine. The weekly Logic Labs and Lit Examples give students many discrete analytical tools, but students also need practice combining those tools in sustained prose.

The short papers should bridge this progression:

1. worksheet-sized logical analysis;
2. one successful handwritten paper with strong scaffolding;
3. increasingly independent short literary arguments;
4. revision of a real piece of prose in Week 18;
5. readiness for a formal late-course paper or portfolio defense.

These are **writing assignments informed by logic**, not enlarged Logic Labs. The paper—not a filled planning sheet—is the product.

---

## 2. Locked student conditions

Every short paper is a **closed-world, handwritten composition**.

Students may use only:

- the supplied textual-evidence supplement;
- the assigned play or course-provided primary text;
- course handouts;
- notes the student made during class.

Students may not use:

- AI;
- the internet;
- online summaries;
- outside criticism;
- tutors;
- parents, friends, or other people;
- anyone else's planning, revising, correcting, sentences, or ideas.

Every assignment should require the student to write and sign:

> I wrote this paper without outside help.

The prohibition is not merely a citation rule. Outside assistance defeats the purpose of seeing the student's own reasoning develop.

---

## 3. Students watched the plays but did not read them

This condition governs the evidence design.

Do not tell students simply to “find two quotations” somewhere in a full play. That creates unnecessary search difficulty and temptation to use AI or the internet.

Every new short paper should include a separate, self-contained textual-evidence supplement:

```text
papers/<ASSIGNMENT_ID>/
  text-supplement.tex
  text-supplement.pdf
```

The supplement should:

1. print two focused scenes or excerpt groups sufficient for close reading;
2. give only brief factual context;
3. define difficult Shakespearean words neutrally;
4. tell students these are **lines worth focusing on, not limits on their evidence**;
5. allow students to use anything accurate from the play;
6. allow remembered later events to be paraphrased accurately;
7. tell students not to invent quotations from memory;
8. avoid reader notes that reveal the expected thesis, logical diagnosis, or “correct” interpretation.

A student should be able to complete the paper honestly using the assignment, supplement, course handouts, and class notes alone.

### Textual anchors versus broader consequences

Use two evidence levels:

- **Textual anchors:** exact quotations from the supplied excerpts for careful analysis.
- **Broader consequences:** actions and outcomes remembered from viewing the play; these may be paraphrased without exact quotation.

The supplement may name a few later events as reminders, but must label them as optional evidence rather than conclusions.

### Source accuracy

Prefer passages already transcribed in the repository's Lit Example readers. Verify them against the exact existing `.tex` and, when needed, a public-domain Shakespeare text. Preserve scene references and do not silently modernize Shakespeare's words. Vocabulary glosses may modernize meaning, not the quoted text.

---

## 4. Naming and folder contract

Use:

- Assignment ID: `U1L<week>SP`
- Folder: `papers/U1L<week>SP/`
- `SP` = Short Paper
- The lesson number identifies the week after which the paper is assigned.

Every completed paper folder should contain:

```text
papers/U1L<week>SP/
  README.md
  assignment.tex
  assignment.pdf
  text-supplement.tex
  text-supplement.pdf
```

Update together:

- `papers/README.md` sequence table;
- `papers/U1L<week>SP/README.md`;
- the relevant `units/elements-of-logic-week<week>/README.md`;
- the root `README.md` only if the repository-level convention changes.

These papers are not Krewone answer-box worksheets. Do **not** create:

- `graded-assignments/<ID>/` entries;
- `template.json`;
- QR codes or OCR boxes;
- AI-grading answer keys.

The student writes the final paper on separate lined paper.

---

## 5. Completed model — do not redesign casually

The authoritative model is:

```text
papers/U1L6SP/
  README.md
  assignment.tex
  assignment.pdf
  text-supplement.tex
  text-supplement.pdf
```

Assignment:

- ID: `U1L6SP`
- Title: *Prophecy Is Not Proof?*
- Placement: after Week 6
- Length: 1–2 handwritten pages
- Score: 10 points
- Text anchors: *Macbeth* 1.3 and 1.7
- Broader-play reminders include Birnam Wood and other consequences.

The model succeeds because it:

- permits `yes`, `no`, or `partly`;
- tells students the goal is earned reasoning, not guessing the teacher's answer;
- guides claim, argument reconstruction, form test, fact test, evidence, objection, qualification, and opening sentences;
- gives a simple writing path without requiring a five-paragraph essay;
- makes grammar low stakes on the first paper;
- supplies quotations without supplying the judgment.

Do not revise `U1L6SP` while building a later paper unless Wayne explicitly requests a change or a new pointer is necessary.

---

## 6. Scaffold without directing the answer

A scaffold should tell students **what intellectual work to perform**, not what conclusion to reach.

Good scaffold moves:

- State your present answer.
- Reconstruct the argument under examination.
- Identify an unstated bridge or assumption.
- Test whether the conclusion follows.
- Identify which claim needs evidence.
- Select quotations and explain what each helps show.
- Name a reasonable objection.
- Qualify the claim.
- Draft possible opening sentences.

Avoid:

- model theses;
- prewritten topic sentences;
- labeling a character's argument “invalid” in advance;
- naming the hidden assumption for students;
- selecting the “winning” definition;
- loaded section headings that reveal the expected judgment;
- a rigid five-paragraph template;
- a checklist so long that the paper becomes prose wrapped around a worksheet.

For each prompt, explicitly allow more than one defensible conclusion. Grade the relationship among claim, logic, and evidence—not agreement with a preferred interpretation.

---

## 7. Difficulty progression

Remove scaffolding gradually.

### Early paper

- 1–2 handwritten pages
- 10 points
- extensive planning scaffold
- two supplied textual anchors
- one clear logical distinction
- spelling and grammar do not reduce the score unless meaning is obstructed

### Middle paper

- approximately 2 handwritten pages
- 10–12 points
- shorter planning scaffold
- students choose which of several relevant tools best fits
- require a reasonable objection or qualification
- continue supplying focused excerpts

### Late practice paper

- 2–3 handwritten pages
- approximately 15 points
- minimal planning scaffold
- require an independently organized comparison or multi-tool judgment
- require counterpressure and qualification
- still supply focused excerpts because students watched rather than read the plays

Week 18 should ask students to revise one actual short paper, preserving the original and showing substantive changes to reasoning. Do not let Week 18 collapse back into revising only isolated worksheet answers.

---

## 8. Recommended remaining sequence

This is the approved design direction, but build one assignment at a time for review. If Wayne changes a prompt or placement, his latest direction controls.

### `U1L10SP` — recommended second paper

**Working title:** *Must Caesar Die?*

**Placement:** after Week 10, when students have studied irrelevant proof and the point at issue.

**Core question:** Does Brutus prove that Caesar must die, or does he prove only that Caesar might become dangerous?

**Natural logic tools:**

- point at issue;
- nearby claim versus required claim;
- possibility versus necessity;
- hidden assumption;
- relevant evidence;
- qualified conclusion.

**Recommended textual anchors:**

1. *Julius Caesar* 2.1 — Brutus's orchard soliloquy: “It must be by his death,” “How that might change his nature,” and the serpent's-egg analogy.
2. A focused counterpressure passage that supplies evidence about Caesar or exposes the gap between possible ambition and required death. Inspect existing Week 9–12 Lit Example readers before choosing; do not invent a new source set when a reliable transcript already exists.

**Length/scaffold:** 1–2 handwritten pages; slightly less scaffolded than `U1L6SP`; 10 points is an acceptable default.

### `U1L15SP` — manhood and definition paper

**Working title:** *What Makes a Man?*

**Placement:** after Week 15, when students can distinguish verbal, real, and mixed disputes. Week 16 rhetoric may later be used for revision.

**Core question:** What does it mean to be a man in *Macbeth*? By the competing definitions used by Macbeth and Lady Macbeth, which character better deserves the name?

Preserve the provocative underlying question—whether Macbeth is a man or Lady Macbeth is “more a man” than he is—but frame it as a dispute over definitions and judgment rather than endorsing aggression as masculinity.

**Natural logic tools:**

- competing meanings of `man` and `manhood`;
- equivocation;
- hidden assumptions;
- verbal, real, or mixed dispute;
- rhetoric as identity pressure;
- qualification.

**Recommended textual anchors:**

1. *Macbeth* 1.5 — Lady Macbeth's “unsex me here” language and preparation for Duncan's murder.
2. *Macbeth* 1.7 — “When you durst do it, then you were a man” and Macbeth's “I dare do all that may become a man; / Who dares do more is none.”

Students may use later actions and consequences to test whether either definition survives the play.

**Length/scaffold:** approximately 2 handwritten pages; 12 points; shorter planning scaffold than `U1L6SP`; require at least one competing definition and a qualified judgment, but do not supply either definition.

### `U1L17SP` — late comparative practice paper

**Working title:** *Who Reasons More Dishonestly with Himself?*

**Placement:** after Week 17, when students have the self-deception tool stack.

**Core question:** Who reasons more dishonestly with himself: Macbeth or Brutus?

**Natural logic tools:**

- desire-first conclusion;
- stated reason versus motive;
- hidden assumption;
- rationalization;
- private argument versus public cover;
- evidence proportional to judgment;
- fair comparison and qualification.

**Recommended textual anchors:**

1. *Macbeth* 1.7 — Macbeth knows the duties and consequences, then names ambition.
2. *Julius Caesar* 2.1 — Brutus moves from possible future danger to present necessity.

The existing `U1L17LE` reader already contains reliable excerpts from both scenes. Use it as a transcription source, but remove its answer-directing reader notes from the paper supplement.

**Length/scaffold:** 2–3 handwritten pages; approximately 15 points; minimal scaffold; require an independently organized comparison, one fair counterpressure, and a qualified conclusion.

### Week 18 and Week 19

- **Week 18:** revise one of the short papers substantively and preserve the original. A useful revision changes the claim, evidence, inference, definition, qualification, or response to an objection—not merely spelling.
- **Week 19:** do not automatically replace `U1L19LL`. A formal final paper or conversion of the portfolio defense requires a separate explicit decision from Wayne.

---

## 9. Student assignment anatomy

A short-paper assignment should normally include:

1. Assignment ID, title, week, name/date.
2. One central question.
3. Explicit permission for more than one defensible answer.
4. Length and handwritten format.
5. Evidence requirement.
6. Reference to the supplied text supplement and permission to use the whole play.
7. Closed-world rule and signed authorship statement.
8. A small transparent rubric.
9. A planning scaffold appropriate to the paper's stage in the progression.

Keep the early rubric simple. A useful pattern is:

- clear claim;
- logical work;
- textual evidence;
- explanation/warrants;
- completion.

Later rubrics may add counterpressure, qualification, organization, or comparison. Do not reward plot summary as analysis.

---

## 10. Text-supplement anatomy

A supplement should normally fit in two pages:

1. Title and assignment ID.
2. Box stating that anything from the play may be used.
3. Passage 1 with factual context.
4. Neutral vocabulary glosses.
5. Passage 2 with factual context.
6. Neutral vocabulary glosses.
7. A short reminder that later events may be paraphrased accurately.
8. A warning not to invent quotations from memory.

Do not add a teacher interpretation, model analysis, or answer key to the student supplement.

---

## 11. Build and verification procedure

Before editing:

```bash
cd /home/tcoop/scope_wr121
git status --short --branch
git pull --ff-only origin main
```

Stop if unrelated changes are present.

For each paper:

1. Read this handoff and the complete `U1L6SP` model.
2. Read the relevant week in `docs/full-course-plan/README.md`.
3. Inspect that week's student reading, Logic Lab, Lit Example reader/worksheet, and answer keys for conceptual alignment.
4. Select two passages; prefer exact transcripts already in the repository.
5. Author `README.md`, `assignment.tex`, and `text-supplement.tex`.
6. Compile both PDFs with shell escape disabled:

```bash
cd papers/<ASSIGNMENT_ID>
latexmk -pdf -interaction=nonstopmode -halt-on-error assignment.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error text-supplement.tex
```

7. Require no LaTeX errors, overfull boxes, accidental blank pages, or stranded headings.
8. Use `pdftotext` to confirm the prompt, closed-world rule, scene headings, quotations, and whole-play permission are present.
9. Render and visually inspect **every page** of both PDFs for clipping, crowding, readable type, neutral framing, and balanced pagination.
10. Clean auxiliary files with `latexmk -c`; commit `.tex` + `.pdf`, not auxiliaries.
11. Update `papers/README.md`, the assignment README, and the week README.
12. Run `git diff --check` and inspect the full diff.
13. Fetch before pushing and ensure `origin/main` has not advanced unexpectedly.
14. Commit one focused assignment and push `main`.
15. Verify local `HEAD` equals remote `refs/heads/main`, and verify the worktree is clean.

Do not report success from source creation alone. The deliverable is the compiled, visually inspected PDF set pushed to `main`.

---

## 12. Common failure modes

Avoid these:

- Turning the paper into another answer-box Logic Lab.
- Asking watched-only students to hunt through a full play for quotations.
- Supplying a model thesis or hidden assumption.
- Treating the supplement's excerpts as the only allowable evidence.
- Requiring exact quotations for later events students remember from viewing.
- Letting a consequence such as Birnam Wood serve as direct proof for an unrelated earlier inference without explanation.
- Confusing motive with justification or prediction with command.
- Grading early spelling and grammar so heavily that students fear the first paper.
- Requiring a five-paragraph structure.
- Using modernized quotation text without labeling it.
- Copying analytical reader notes into the neutral supplement.
- Building all remaining papers before Wayne can review the next step in the progression.
- Creating Krewone templates, AI keys, or `graded-assignments` entries for handwritten papers.
- Committing LaTeX auxiliary files.

---

## 13. Completion report format

After each paper, report:

- assignment ID, title, and placement;
- question, length, and point value;
- passages included in the supplement;
- how the scaffold is lighter than the previous paper;
- closed-world safeguards;
- files created or changed;
- PDF page counts and visual-QA result;
- commit SHA;
- confirmation that local and remote `main` match.
