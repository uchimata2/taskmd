---
id: T-008
title: Write the backend-neutral method document
type: deliverable
status: done
phase: review
parent: null
blocked_by: [T-007]
related: [T-003, T-013]
work_package: none
owner: maintainer
business_value: critical
effort: l
created: 2026-08-04
updated: 2026-08-05
deliverables:
  - plugin/docs/METHOD.md
  - plugin/docs/method/specify.md
  - plugin/docs/method/plan.md
  - plugin/docs/method/implement.md
  - plugin/docs/method/review.md
  - plugin/docs/method/audit.md
  - tasks/_task-template.md
  - tasks/_audit-umbrella-template.md
  - CLAUDE.md
---

# T-008 — Write the backend-neutral method document

## 1. Specify

**Outcome**
One document that defines how work is tracked — lifecycle, edges, audit, when to ask — containing
**no instruction specific to any backend**. It is the plugin's shipped standard and the thing a
GitHub-based project and a Markdown-based project follow identically.

**Requirements served**
R-3, R-4, R-5, R-6, R-7, R-8, R-9, R-13, R-21, R-22 (`docs/SCOPE.md`).

**Why this one**
R-13 splits the method from the technical spec, and nothing implements the split yet. There is
also a live defect: four references point at a workflow document that **does not exist** — only
`reference/TASK-WORKFLOW.md` does, and that is one project's copy: it hard-codes a folder contract,
a work-package vocabulary, a decisions register and `task.py` commands, none of which a
GitHub-backed project has. (Its *tools and vocabulary* are project-shaped; it carries no
identifiable project data — `reference/` was scanned clean on 2026-08-04, see
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md).) `check` does not catch any
of the four because they are plain-text mentions rather than links. Verified 2026-08-04:

| Pointer | Target | Resolves? |
| :--- | :--- | :---: |
| `tools/tasks/task.py:247` (context footer) | `tasks/TASK-WORKFLOW.md` | no |
| `tools/tasks/task.py:247` (context footer) | `docs/LESSONS.md` | no |
| `tasks/_templates/task-template.md:18` | `tasks/TASK-WORKFLOW.md` §3–§4 | no |
| `tasks/_templates/audit-umbrella-template.md:28` | `TASK-WORKFLOW.md` | no |
| `CLAUDE.md:47` | `reference/TASK-WORKFLOW.md` | yes — deliberate, points at prior art |

**Scope**
- In: the lifecycle and its exit criteria; the two edge kinds and when to use which; the audit
  mechanism (umbrella → child findings); one-phase-per-request; the ask-to-the-exit-criterion rule
  and discovery escalation; where each kind of fact lives. Repointing every reference in the table
  above at `docs/METHOD.md`, and deleting the `docs/LESSONS.md` half of the CLI footer.
- Out: field names, file layout, id format, folder contract, any command — all backend-specific
  (T-009, T-010) or already decided (T-001). Creating a lessons document: this project has no
  lessons file, no requirement asks for one, and `SCOPE.md`/`BRIEF.md` already hold the carried
  lessons — so the footer loses the pointer rather than gaining a target.

**Inputs**
- `docs/SCOPE.md` §3A — the requirements this document implements
- `reference/TASK-WORKFLOW.md` — the proven standard, to be generalised, not copied
- the Notion-backed project — the same lifecycle run against a non-file backend, with the exit
  criteria and preflights that survived real use. Read from a local checkout outside this tree; no
  path to it is recorded here (R-23)

**Acceptance criteria**
- [ ] Contains no field name, file path, id format or command — proven by reading it against a
      GitHub-only project and finding nothing that does not apply
- [ ] Every phase has a written exit criterion, so R-7 has something to measure "enough" against
- [ ] The audit mechanism is defined such that a finding cannot be fixed inline
- [ ] Reads sensibly for research, a deck and a training course — verified by walking one
      non-software example through all four phases
- [ ] Structured for progressive disclosure: a spine short enough to always load, details on demand
- [ ] Reads whole without a Claude Code harness — no skill, plugin, slash command or agent-harness
      vocabulary anywhere in it (the D1 test, below)
- [ ] R-6, R-7 and R-8 are stated **here and nowhere else**, so T-003's skill can point at them
      rather than restate them
- [ ] Every pointer in the *Why this one* table targets `docs/METHOD.md` and resolves, and the
      `docs/LESSONS.md` half of the CLI footer is gone — proven by opening each of the four
      references and following it

**Decisions**
- **D1 — the method is a standalone document; the skill points at it** (2026-08-04, maintainer).
  Rejected: making the method document double as the skill's spine. Rationale: R-13/R-14 require the
  method to be followable by a GitHub-based project and by non-software work, and a skill spine is a
  Claude Code artifact — binding the standard to one harness would put the method out of reach of
  the very adopters R-13 exists for. It also gives R-6/R-7/R-8 one home instead of two: T-003's skill
  carries only what neither the CLI nor the method can (how the agent behaves) and links here.
  Closes the open question this task carried, and answers the same question in T-003.
- **D2 — it lives at `docs/METHOD.md`** (2026-08-04, maintainer). Rejected: `tasks/TASK-WORKFLOW.md`,
  which three of the four dangling pointers already name — closing the defect by creating that file
  would cost no pointer edits, but a standard living inside the task folder reads as project-local,
  and T-006 would have to move it at packaging time. Also rejected: `taskmd/METHOD.md`, which mixes
  prose into an importable Python package.
- **D3 — the CLI footer drops `docs/LESSONS.md`** (2026-08-04, maintainer) — see *Scope, out*.

**Open questions**
- none.

## 2. Plan

**Shape** — **D4 (2026-08-04, maintainer): a spine plus per-phase files**, not one document. The
spine is what always loads; each phase's procedure loads when its moment arrives, which is how
acceptance criterion 5 becomes checkable rather than a judgement about length. Both prior arts
converged on this shape independently. Rejected: a single `docs/METHOD.md` — simplest and proven at
~174 lines, but then criterion 5 is only met by the whole document staying short, which caps the
detail the method can carry and makes the criterion untestable.

**The filter** — every rule in the prior art is classified before it is carried, into one of three
buckets. Two are dropped, and dropping them is a decision, not an omission:

| Bucket | Disposition | Examples from the prior art |
| :--- | :--- | :--- |
| Method | carry | lifecycle + exit criteria; forward-edge-only linking; audit umbrella → children; one phase per request; batch questions; "undocumented progress does not exist" |
| Backend-specific | drop → T-009 / T-010 | field names, status vocabulary, folder contract, `task.py` commands, work packages, a decisions register, "fetch every child page and comment" |
| Harness-specific | drop, permanently | **per-phase model & effort gate** and the cost-guard section — `SCOPE.md` §4 non-goal 7: which model runs a phase is agent-harness policy, not tracking |

**Two deliberate divergences from the prior art**, to be stated in the document so a reader coming
from either one is not confused:
- **Audit is a task type, not a phase** (R-5). The Notion-backed prior art runs audit as a fifth
  workflow branch; taskmd's four phases stay four, and an audit is a task that produces children.
- **Verification is `implement`'s exit criterion** (R-4). The file-backed prior art exits
  `implement` on "all planned outputs exist", which a broken output satisfies.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Apply the filter above to both prior arts rule by rule; record anything that resists classification, since that is where the method/binding seam actually is. | classification + seam notes → §3 *Decisions & assumptions* |
| 2 | Write the spine: what the method is, the core rules, the lifecycle table with one exit criterion per phase, the divergence notes, and the load-on-demand pointer table. | `docs/METHOD.md` |
| 3 | Write the four phase procedures, each ending in its exit criterion and what evidence satisfies it. `implement` carries R-4 explicitly. | `docs/method/specify.md`, `plan.md`, `implement.md`, `review.md` |
| 4 | Write the edges section: the three edge kinds, the choose-an-edge test, and store-the-forward-edge — naming no field. | `docs/METHOD.md` (spine — short, and every phase needs it) |
| 5 | Write the audit procedure as a task type: umbrella → child findings, and the inline-fix prohibition stated so a violation is identifiable. | `docs/method/audit.md` |
| 6 | Write agent conduct — R-6 one phase per request, R-7 ask to the exit criterion, R-8 discovery surfaced never absorbed. Per **D1** this is their sole home; T-003's skill will link here. | `docs/METHOD.md` (spine — R-6/R-7/R-8 gate every turn, so they cannot be on-demand) |
| 7 | Write "where each kind of fact lives" as **roles** (the work item, the project's conventions, the resume pointer), never paths — the role→path mapping belongs to the binding. | `docs/METHOD.md` |
| 8 | Walk a **research** task through all four phases against the finished text; fix every place that only reads for software. R-4 is the hard case — name what counts as verification when there is nothing to run. | corrections applied; walk recorded in §4 |
| 9 | Repoint the four dangling references at `docs/METHOD.md` and delete the `docs/LESSONS.md` half of the CLI footer (**D3**). | `tools/tasks/task.py:247`, `tasks/_templates/task-template.md:18`, `tasks/_templates/audit-umbrella-template.md:28`, `CLAUDE.md:47` |
| 10 | Run the criteria: the D1 test (read it whole with no Claude Code harness assumed), the GitHub-only read for criterion 1, `grep` for R-6/R-7/R-8 stated twice, and `task.py check`. | §4 *Review* table, with the actual command output |

**Inputs not in this repository** — the Notion-backed prior art (core + its five phase files +
rationale) is read from a local checkout outside the tree. It is an input to steps 1–2 only; no
path to it is written into any tracked file (R-23, [T-013](T-013-quarantine-local-only-information-behind-gitignore.md)).

**Output paths, collected**
- `docs/METHOD.md` — the spine (steps 2, 4, 6, 7)
- `docs/method/specify.md`, `plan.md`, `implement.md`, `review.md` — phase procedures (step 3)
- `docs/method/audit.md` — audit as a task type (step 5)
- `tools/tasks/task.py`, `tasks/_templates/task-template.md`,
  `tasks/_templates/audit-umbrella-template.md`, `CLAUDE.md` — pointer repairs (step 9)

## 3. Implement

**Decisions & assumptions**
- **The method's noun is "task", not "work item"** (2026-08-04). "Work item" is neutral but reads as
  jargon in every non-software example; an issue, a card and a row are all tasks. Neutrality is
  bought by never naming what a task *is made of*, not by renaming it.
- **Statuses are not enumerated in the method** (2026-08-04). The lifecycle needs the phase names to
  mean anything, so those are named; the status vocabulary is the project's and belongs to the
  schema. The method says only that phase and status are independent.
- **`docs/method/` is a folder, not a suffix on one file** (D4). The five procedure files each end
  in their exit criterion, so a reader who loads one gets the whole of what that phase requires
  without the spine.
- **The seam that resisted classification** (plan step 1): *"done means consistent"*. Its method
  half is "the evidence exists and the record is current"; its backend half is what "current" means
  mechanically (which artifacts, which validator). Split accordingly — the spine states the rule,
  and `CLAUDE.md` states this project's mechanical version. Everything else in the two prior arts
  fell cleanly into carry / drop.
- **Plan step 10 was mis-scoped, and was corrected while running it** (2026-08-04). It routed the
  criteria checks into §4 *Review*. Under the method being written, checking the outcome by use is
  `implement`'s exit criterion (R-4) and the verdict against the criteria is `review`'s — two
  different acts. The evidence therefore lands here; §4 stays empty until the review phase is asked
  for (R-6).
- **Assumption: `docs/method/` will move under packaging** (T-006). Nothing in the method or its
  pointers depends on the location beyond the relative links between the six files, which move
  together.

**Outputs produced**
- `docs/METHOD.md` — 188 lines: core rules, lifecycle + exit criteria, conduct (R-6/R-7/R-8), edges,
  audit summary, where facts live, deliberate departures, load-on-demand table
- `docs/method/specify.md` (63), `plan.md` (71), `implement.md` (86), `review.md` (69),
  `audit.md` (72)
- Repointed: `tools/tasks/task.py:247` (footer now `Method: docs/METHOD.md`, `docs/LESSONS.md` half
  deleted per D3), `tasks/_templates/task-template.md:18`,
  `tasks/_templates/audit-umbrella-template.md:28`, `CLAUDE.md` (status line + *Working method*,
  which restated the four rules and now points instead)

**Verification — checked by use, not by re-reading**

1. **Read as a project with no local task files** (criterion 1). Walked the method against an
   issue-tracker-shaped project: tasks → issues, phase/status → two independent properties,
   hierarchy → sub-issues, dependency → blocked-by, soft → a reference, the derived list → a saved
   query, audit umbrella → an issue with child issues. Nothing in the six files failed to apply.
   Mechanical backstop, no hits:

   ```
   grep -rnE "front-matter|task\.py|work_package|blocked_by|YAML|kebab|folder|filename|repository|commit|test suite" docs/METHOD.md docs/method/*.md
   --- exit 1 (1 = no hits) ---
   ```

2. **Read with no agent harness assumed** (criterion 6). One hit, and it is the intended one:
   `docs/METHOD.md:171` names effort/tools/model only to state that the method does **not** legislate
   them (non-goal 7). No occurrence of a product, vendor or harness name anywhere in the six files.

3. **Non-software walk** (criterion 4). One research task — *does the onboarding material reduce
   first-month support contacts* — carried through all four procedure files as the same continuous
   example: criteria in `specify`, a five-step plan in `plan`, verification by an uninvolved reader
   plus a two-figure trace in `implement`, a four-row verdict in `review` with one criterion carried
   to a child task. R-4 was the hard case as predicted; it forced the *When there is nothing to run*
   section, whose rule is that the substitute for a mechanical check is the smallest real **use**,
   because use can surprise you and re-reading cannot.

4. **Conduct rules stated once** (criterion 7). `grep` finds R-6/R-7/R-8 stated as rules only in
   `docs/METHOD.md` §3. `docs/SCOPE.md` R-6/R-7 also match — that is the requirement register
   stating the requirement, not a second copy of the rule, and the two are not interchangeable.
   Flagged for review to judge rather than settled here.

5. **Pointers** (criterion 8). All six files exist; every remaining `TASK-WORKFLOW.md` mention is
   either `reference/` (resolves — deliberate prior-art pointer) or T-008's own record of the
   defect. Footer re-run:

   ```
   NEXT: read the file above, then work the 'specify' phase.
   Method: docs/METHOD.md
   ```

6. **Validator and tests**:

   ```
   OK - 13 tasks, vocabulary valid, references resolve, 0 broken links
   31 passed in 0.08s
   ```

**Not verified here** — criterion 2 (an exit criterion per phase) and criterion 3 (a finding cannot
be fixed inline) are judgements about the text, not things a use can establish. They are `review`'s
to settle.

## 4. Review

Judged against the criteria as agreed in §1, not against what the document turned out to be good at.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| 1 — no field name, file path, id format or command | **not met** | The issue-tracker read found nothing that fails to apply, and the vocabulary grep is clean — but two `T-x` placeholders survive in worked examples (`plan.md:26`, `review.md:60`), and a prefixed short code is a local-Markdown convention. → **[T-016](T-016-remove-the-id-format-placeholders-from-the-method.md)** |
| 2 — every phase has a written exit criterion | met | All four, in `METHOD.md` §2 and again at each phase file's head. That they are written *twice* is a separate defect (T-014); the criterion only asked that they exist. |
| 3 — audit defined so a finding cannot be fixed inline | met | `audit.md` states it as the rule the mechanism exists for, gives the four things an inline fix destroys, and closes the "too small to be a task" loophole by naming it a threshold problem instead. The one exception (a finding that blocks the audit) requires stopping, not repairing. |
| 4 — reads for research, a deck and a training course | met | One research task walked end to end across all four procedure files as a single continuous example, which is what the criterion asked for. The deck and course cases appear in `implement.md`'s verification table but were not walked — within the criterion as written, and worth knowing. |
| 5 — spine short enough to always load, details on demand | **not met** | 188 lines, against 173 for the single-file option D4 rejected. The always-loaded part is larger than the flat alternative, which inverts the purpose. → **[T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md)** |
| 6 — reads whole with no agent harness assumed | met | No product, vendor or harness name in the six files. One occurrence of "model" (`METHOD.md:171`), in the sentence declaring that the method does *not* legislate it — the absence being stated, not an assumption leaking. |
| 7 — R-6/R-7/R-8 stated here and nowhere else | **not met** | `SCOPE.md` R-6/R-7/R-8 state the same three rules in near-identical wording — R-6 and §3.1 share the phrase "context, not authorization" verbatim. Arguable rather than clear-cut, so it is a decision, not a fix. → **[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md)** |
| 8 — pointers repointed and resolving | met | All four repointed and followed; the six files exist; the footer now prints `Method: docs/METHOD.md` with the `docs/LESSONS.md` half gone (D3). Every surviving `TASK-WORKFLOW.md` mention is either `reference/` (resolves, deliberate) or this task's own record of the defect. |

**Beyond the criteria** — one defect in the deliverable that no criterion covered: each phase's exit
criterion is stated verbatim in both `METHOD.md` §2 and the phase file's header, which is the
project's one design rule broken inside the document that defines it. Raised as
**[T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md)**. It is a child rather than an
audit because it is a fault in *this* task's own output; an audit is for problems surfaced in other
work.

Five met, three carried, one extra raised. The task closes with the gaps visible as tasks with
owners rather than as caveats in a paragraph.

**Child fix tasks raised**
- [T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) — exit criteria stated twice
- [T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) — spine exceeds the flat alternative
- [T-016](T-016-remove-the-id-format-placeholders-from-the-method.md) — `T-x` placeholders in the method
- [T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) — SCOPE/METHOD rule overlap

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Raised by T-007: R-13 requires the split, and the referenced workflow document does not exist. |
| 2026-08-04 | → specified | Specify worked. D1–D3 settled the open question and the document's home; the dangling-pointer defect turned out to be four references across three files, not two, so the scope and criterion 8 widened to match. Criteria 6–7 added to make D1 falsifiable. |
| 2026-08-04 | → done | Review worked. Five criteria met, three not (1, 5, 7), one further defect found beyond the criteria — four child tasks T-014…T-017. Nothing fixed during review. Criterion 5 is the substantive one: the spine is longer than the single-file option D4 rejected, so progressive disclosure currently costs more than it saves. |
| 2026-08-04 | → review | Implement worked. Six files written; four pointers repaired; `CLAUDE.md` stopped restating the four rules and now points at the method. Verified by use — an issue-tracker read, a no-harness read, and one research task walked through all four procedures — with results recorded in §3. Phase stays `implement`; the §4 verdict is the review phase's (R-6). |
| 2026-08-05 | (no change) | `tools/tasks/task.py` removed from `deliverables`: T-002 deleted the interim tool it named. Found by `check`'s missing-deliverable class on its first run against this repository — the declaration outlived the file by one commit, which is the whole reason that class exists. |
| 2026-08-04 | → planned | Plan worked against both prior arts. D4 chose spine + per-phase files. The filter drops the model/effort gate permanently (non-goal 7) and the backend specifics to T-009/T-010; two divergences from the prior art recorded as deliberate. Raised T-013 — the R-23 risk is repo-wide, not T-008's to absorb. |
