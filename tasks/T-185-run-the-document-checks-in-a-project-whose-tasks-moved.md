---
id: T-185
title: Run the document checks in a project whose tasks moved
type: fix
status: proposed
phase: specify
parent: T-177
blocked_by: []
related: [T-095, T-108, T-178]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-18
updated: 2026-08-18
adopter_visible: yes
deliverables: []
---

# T-185 — Run the document checks in a project whose tasks moved

## 1. Specify

**Outcome**
`check` in a migrated project reports what it can still check, refuses only what needs a task file,
and says plainly that the task half was not examined.

**Why this one**
[T-177](T-177-run-the-checks-that-need-no-task-folder.md) ruled that it should, and measured what it
buys: two dead links and a config advisory in a migrated project that today gets `CONFIG ERROR` and
exit 2. The ruling, its three rejections and the evidence are there and are not repeated here.

**The ruling is conditional, and the condition is the risky half.** T-177 answered *no, a
document-only pass does not mislead* **only** on the basis that the `Scope` line gains what it
currently has no words for. As it stands the line says *every document read*, which is true and reads
as *everything checked* — to a reader who has just been handed real defects. Shipping the first half
without the second turns a refusal into a false assurance, which is worse than the behaviour it
replaces.

**Scope**
- In: moving the `tasks_dir` guard so the five no-`tasks` checks run when `id_width: none`.
- In: the `Scope` line saying the task half was not checked, and why.
- In: the exit status for such a run.
- Out: a mistyped `tasks_dir`. It keeps refusing — T-177 part 2.
- Out: a fifth command or a `--documents-only` flag. Both rejected by T-177.
- Out: re-opening the ruling.

**Inputs**
- [T-177](T-177-run-the-checks-that-need-no-task-folder.md) §3 — the ruling in three parts
- `plugin/skills/taskmd/taskmd/schema.py` — `_check_tasks_dir`, and `load_schema` which calls it
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_check` and the five signatures without `tasks`
- `tests/fixtures/migrated-away/` — **which holds a config and no documents**, and so cannot test
  this. T-177 had to build one; this task needs the fixture to grow or a sibling beside it
- [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) — the `Scope` line's own task

**Acceptance criteria**
- [ ] A migrated project reports document-level problems that a clean one does not — shown by a
      fixture carrying a real defect, failing before the fix
- [ ] A mistyped `tasks_dir` still exits 2 with the message it has today, proven by the existing
      `broken-tasks-dir` fixture still passing
- [ ] The output states that the task half was not checked, in a form a reader meets without looking
      for it. A run whose only signal is the absence of task counts does not satisfy this
- [ ] The exit status for a clean document-only run is stated and justified — a pass is not obviously
      right when a third of the validator did not run
- [ ] The `migrated-away` fixture holds documents, so this behaviour is testable at all
- [ ] No new command and no new flag

**Open questions**
- ~~**What exit status does a clean document-only run take?** `0` reads as validated and is what
  criterion 4 is suspicious of; a distinct non-zero code says *incomplete* but makes every migrated
  project's gate red for ever. T-177 did not settle this and marked it out of its own scope.~~
  **Answered by the owner on 2026-08-19: exit `0`, and the run states what it skipped** — see the
  Log row of that date for the rejected option and its cost.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 7 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). Its dependency on T-177's loader change is inside the grant: §1 requires the loader and the `Scope` line to ship together, and both are this task's. |
| 2026-08-19 | (no change) | **The one open question is answered by the owner: exit `0`, with the run stating what it skipped.** Asked in the backlog-wide round of 2026-08-19. *Rejected: a distinct non-zero code.* It would make the status itself say *incomplete*, which is the honest reading, but it turns every migrated project's gate red permanently — and a gate that is always red is switched off or ignored, which loses more than a mis-read `0` does. *Rejected: holding this task until T-177's condition ships*, which would have left the question open rather than settled. The honesty therefore has to live in the `Scope` line, which T-177 §3 part 3 already requires; that requirement is now load-bearing rather than supporting, and `specify` writes a criterion for it. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-177](T-177-run-the-checks-that-need-no-task-folder.md)'s review. **Carries T-177's condition as its own risk**: the loader change without the `Scope` change is a false assurance, so the two ship together or not at all. One genuinely open question — the exit status of a clean document-only run — which is why this is not simply the code T-177 declined to write. Outside the standing grant of 2026-08-18, which covers the six named tasks and nothing any of them raises. |
