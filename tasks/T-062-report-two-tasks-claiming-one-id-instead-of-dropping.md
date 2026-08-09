---
id: T-062
title: Report two tasks claiming one id instead of dropping one
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-004, T-075]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-062 — Report two tasks claiming one id instead of dropping one

## 1. Specify

**Outcome**
Two files claiming the same id are reported by `check`, naming both files, instead of one of them
silently ceasing to exist for every command and every derived view.

**Why this one**
Raised as **F-4** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Shown, not asserted — a three-file project, two of the files carrying
`id: T-001`:

```
taskmd check
OK - 2 task(s), vocabulary valid, references resolve, no broken links
exit=0

taskmd list
T-0001  proposed  -  specify  over-wide id, width is 3
T-001   proposed  -  specify  SECOND file alphabetically
```

Three task files went in; two tasks came out; `check` called it clean. `load_tasks` assigns into a
dict keyed by id, so **walk order decides which file is the task** and the other disappears — from
`list`, from the generated index, from `context`, and from every derived edge on both ends. Nothing
prints a warning and nothing exits non-zero.

**The binding promises the opposite, in terms.**
[`local-markdown.md`](../plugin/docs/bindings/local-markdown.md) *find* says the front-matter is what
is matched, *"so a renamed file is still found and two files claiming one id are a conflict rather
than a coin toss"*. It is a coin toss, decided by `sorted(files)`.

**This is also T-004's open question, already answered by the code.**
[T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) still asks *"What happens on a
merge conflict?"* — and two branches each taking the next free number is precisely how a project
reaches this state. The implementation's current answer is silent data loss, which is the answer
nobody would choose deliberately.

**Why High.** Everything else this audit found costs a reader work; this one loses a task. It is also
the failure shape the project has already named twice as the worst kind — a validator reporting
success over something it never examined ([T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md),
[T-025](T-025-let-check-notice-a-stale-generated-index.md)).

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`); R-13 — a binding's stated guarantee is what an adopter builds on.

**Scope**
- In: a duplicate-id class in `check`, naming the id and every file claiming it.
- In: what `load_tasks` does meanwhile. A reported conflict that still silently picks a winner leaves
  every other command answering from a coin toss.
- In: a `broken-*` fixture holding exactly this defect, per the convention in
  `tests/fixtures/README.md`.
- Out: id **format** and the merge-conflict *policy* — T-004's. This task makes the collision
  visible; it does not decide how a project should recover from one.
- Out: `id_width` enforcement, which is the same function and is
  [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) — deliberately split so each can be
  judged on its own evidence.

**Inputs**
`plugin/taskmd/schema.py` (`load_tasks`, `is_id`), `plugin/taskmd/cli.py` (`cmd_check`),
[`local-markdown.md`](../plugin/docs/bindings/local-markdown.md) *find*,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-4,
[T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md).

**Acceptance criteria**
- [ ] `check` reports two files claiming one id, naming the id and **both** paths, and exits non-zero
- [ ] Shown failing on a fixture first, per R-16
- [ ] A project with no duplicates is unaffected, and the existing fixtures each still report exactly
      one class
- [ ] It is stated what the other commands do while a duplicate exists — whichever answer is chosen,
      the choice is written down rather than left to `os.walk`
- [ ] The binding's *find* sentence is true of the tool afterwards, checked against the sentence

**Open questions**
- **Does anything other than `check` refuse?** A duplicate makes `context`, `list` and `index`
  answer from an arbitrary pick, which R-17's reasoning would put at load time rather than leaving to
  a validator the user may not have run. Against that: refusing to load makes an unrelated command
  fail on a defect in a file it was not asked about, and `check` exists precisely so problems have
  one place to surface. `plan` decides; the question is which of R-17 and least-surprise wins here.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised as F-4 from the T-059 audit, clauses 1 and 3. Reproduced before write-up on a scratch project outside the repository: three task files, `OK - 2 task(s)`, exit 0, and the loser gone from every view. `high` because it is the only finding in the set that loses data rather than costing a reader time, and because the binding states the opposite guarantee in terms. Related to T-004, whose open merge-conflict question the implementation currently answers by dropping a task. |
