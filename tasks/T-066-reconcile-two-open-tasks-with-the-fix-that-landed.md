---
id: T-066
title: Reconcile two open tasks with the fix that already landed
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-023, T-030, T-011]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-066 — Reconcile two open tasks with the fix that already landed

## 1. Specify

**Outcome**
[T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) and
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md) state what is true of the code today, so
a session that picks either one up is not sent looking for a defect that was removed months of
sessions ago.

**Why this one**
Raised as **F-9** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. Both tasks are built on an absolute install path appearing in output. Run today,
on a project outside this repository with no `.taskmd/config.md`:

```
taskmd check --root <a project elsewhere>
CONFIG ERROR  taskmd/defaults/config.md: tasks_dir is 'tasks', but the project root has no such
folder. This project has no .taskmd/config.md, so taskmd is using its shipped default; ...

python -m taskmd.schema <a project elsewhere>
schema   taskmd/defaults/config.md
```

Machine-independent, both paths. `_display()` is what does it, and it landed in commit `580d22b`,
which closed [T-011](T-011-runtime-discovery-and-project-hook-commands.md) — **after** both tasks
were raised and after T-023's own decision was recorded.

**What that changes for each.**

- **T-023.** Its outcome — *"names that config in a form that is the same on every machine, instead
  of the absolute path"* — is already achieved. Criterion 1 is met; criterion 4, *"shown failing on a
  fixture, per R-16"*, **cannot** be met, because nothing fails. What genuinely remains is a wording
  preference: the maintainer answered on 2026-08-07 that the string should be `<shipped default>`,
  and explicitly rejected *"printing `taskmd/defaults/config.md`"* — which is precisely what the code
  now prints. So the task is live, and it is a different task from the one it says it is.
- **T-030.** Its decision to remove the entry point is untouched: the entry point still exists, is
  still absent from every statement of the command surface, and still takes a positional directory.
  Only its *evidence* is stale — the finding it quotes as "the harder half" is gone, so criterion 2
  (*no entry point prints an absolute path on any path*) is already satisfied and cannot drive the
  removal.

**Why an open task's premise counts where a closed one's does not.**
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) ruled that task records are dated
accounts of decisions and not copies to keep in step, and T-059 kept that ruling for **closed** tasks.
An open task's `specify` section is not a record of anything — it is what the next session acts on.
A premise the code has falsified therefore costs real work, which is the difference and the reason
this is a finding rather than history.

**Requirements served**
R-1 (`docs/SCOPE.md`) — the task is the one home for what that task is for; §1 *Invisibility*, in the
sense that nobody should have to remember which of two open tasks was overtaken.

**Scope**
- In: T-023 §1 — the outcome, the quoted transcript, the R-20/R-23 tension argument, and criteria 1
  and 4.
- In: T-030 §1 — the *"the output is the harder half"* passage and criterion 2.
- In: whether T-023 survives at all once its premise is gone, or whether the remaining wording
  preference is worth the task.
- Out: the maintainer's answers in either task. Both were decisions and neither is reopened; this is
  about the evidence around them.
- Out: doing either task's work.
- Out: closed tasks' records, which are dated accounts and stay as written.

**Inputs**
[T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) §1,
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md) §1, `plugin/taskmd/schema.py`
(`_display`), commit `580d22b`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-9.

**Acceptance criteria**
- [ ] Neither task's `specify` asserts a behaviour the current code does not have — checked by
      running the commands each one quotes
- [ ] Where a criterion has become unmeetable, it is marked so with the original kept, per
      [`review.md`](../plugin/docs/method/review.md) *Changing a criterion* — not silently rewritten
- [ ] What each task is actually still for is stated in one sentence a reader meets first
- [ ] The maintainer's recorded answers survive unchanged in both
- [ ] No absolute path is written into either record while correcting them (R-23)

**Open questions**
- **Does T-023 stay open?** With the leak gone, what is left is choosing between `<shipped default>`
  and the file's real name — a wording call the maintainer has already made once, on an argument
  (*"a repo-relative path is relative to taskmd's repository rather than the adopter's"*) that still
  holds. Keeping it costs a task in the backlog for one string; cancelling it discards a decision that
  was taken deliberately. The maintainer's call, and the only one in this task.

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
| 2026-08-09 | → proposed | Raised as F-9 from the T-059 audit, clause 1. Verified before write-up by running both commands against a project outside this repository: neither prints an absolute path, and `git log -S` puts `_display()` in T-011's closing commit, after both tasks were raised. `medium`/`xs` — two `specify` sections, and the cost is a session hunting a defect that is gone. The distinction that makes this a finding at all: T-026 excluded task records as dated accounts, which is right for closed tasks and wrong for open ones, whose premises are instructions rather than history. |
