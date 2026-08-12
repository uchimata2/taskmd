---
id: T-066
title: Reconcile two open tasks with the fix that already landed
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-023, T-030, T-011]
work_package: M1
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
      [`review.md`](../plugin/skills/taskmd/docs/method/review.md) *Changing a criterion* — not silently rewritten
- [ ] What each task is actually still for is stated in one sentence a reader meets first
- [ ] The maintainer's recorded answers survive unchanged in both
- [ ] No absolute path is written into either record while correcting them (R-23)

**Open questions**
- ~~**Does T-023 stay open?**~~ **Answered by the maintainer on 2026-08-09: it stays open, rescoped to
  the wording.**

  So T-023 is not the task it says it is, and the fix is to make it say what it is: **one string** —
  whether a config error names `<shipped default>` or the file's real name. Its outcome sentence and
  its transcript describe a leak that no longer exists; both are corrected. Criterion 1 is marked
  **already met** by T-011, and criterion 4 (*shown failing on a fixture, per R-16*) is marked
  **unmeetable** with the original text kept, per
  [`review.md`](../plugin/skills/taskmd/docs/method/review.md) *Changing a criterion* — nothing fails, so nothing
  can be shown failing.

  **The decision that survives is the one that was actually taken.** On 2026-08-07 the maintainer
  chose `<shipped default>` and rejected *"printing `taskmd/defaults/config.md`"* — which is precisely
  what the code prints today, by accident rather than by reversal. The argument they gave (*"a
  repo-relative path is relative to taskmd's repository rather than the adopter's"*) is untouched by
  T-011, so keeping the task keeps a live preference rather than a stale one.

  *Rejected: cancelling T-023 and folding the wording into T-030.* T-030 does touch the same output on
  its success path, so the string would have a home — but it would be a home on a task raised to
  decide an entry point's existence, which is a different question. A decision parked on the nearest
  passing task is how a decision gets lost.

  *Rejected: cancelling T-023 outright.* Cheapest, and it would let the rejected string stand as the
  shipped behaviour by default. Discarding a deliberate decision because the defect that prompted it
  was fixed by something else is not the same as reversing it.

  **What this costs, stated:** a backlog entry for a one-string change, and a reader who opens T-023
  expecting the leak fix in its title. The second is what this task removes.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-run both commands each task quotes, on a project outside this repository, before editing either record | The evidence that both premises are stale |
| 2 | T-023: a note a reader meets **before** the outcome, saying the leak is gone and naming the one string that is left | `tasks/T-023-…md` §1 |
| 3 | T-023: strike the achieved outcome, tick criterion 1 as met-by-another-task, and mark criterion 4 unmeetable — all with the original text kept | The marked criteria |
| 4 | T-030: replace the *harder half* passage with what is now true, and tick its criterion 2 the same way | `tasks/T-030-…md` §1 |
| 5 | Check both maintainer answers are byte-for-byte what they were, and that no absolute path entered either record | The two greps |

**Why step 1 comes first and is a re-run.** The audit already proved this on 2026-08-09, and the
cheapest failure available here is to edit two records on the strength of a finding rather than on
the behaviour — which is the exact mistake being corrected. It takes one command each.

**Why the note goes above the outcome and not in the log.** A reader opening T-023 reads the title
and the outcome, and both describe a fix that has happened. The log is where they would find out
last.

## 3. Implement

**Decisions & assumptions**

- **D1 — struck through, never deleted** — 2026-08-09. Every overtaken sentence and both criteria are
  kept with the original text visible and marked. A record edited to match what turned out to happen
  is a description, and a reader could no longer tell which parts predated the work — which is
  [`review.md`](../plugin/skills/taskmd/docs/method/review.md) *Changing a criterion*, applied to a `specify`
  rather than to a `review`.

- **D2 — T-030's dedupe paragraph is rewritten rather than struck** — 2026-08-09. It reasoned about
  a T-023 that no longer exists in that form — *"if T-023's fix is to change `source` at the point it
  is built, this finding's output half is resolved with it"*. Both halves of that sentence have
  resolved, so keeping it struck would leave a reader working out which. The replacement says the
  live relationship: the two still share a string, so check them together, and that is not a reason
  to merge them.

- **What was deliberately not done:** neither task's status moved, and neither decision was reopened.
  T-023 is still `specified`, still open, and still the maintainer's `<shipped default>` call; T-030
  is still a removal. This task corrects what a reader is told, not what either task is for.

### Step 1 — both premises re-run today

On a project outside this repository with no `.taskmd/config.md`:

```
taskmd check --root <a project elsewhere>
CONFIG ERROR  taskmd/defaults/config.md: tasks_dir is 'tasks', but the project root has no such
folder. This project has no .taskmd/config.md, so taskmd is using its shipped default; ...   exit 2

python -m taskmd.schema <a project elsewhere>
SCHEMA ERROR: taskmd/defaults/config.md: tasks_dir is 'tasks', but the project root has no such
folder. ...
```

Machine-independent on both paths — the error path T-023 is about and the entry point T-030 is
about. Neither names an installation.

### Steps 2–4 — what each record now says

- **T-023** opens with a block quote a reader meets before the outcome: the leak is gone, and what is
  left is one string — `<shipped default>` against the file's real name, which is *precisely* the
  form the 2026-08-07 answer rejected and precisely what the code prints today. Its outcome is struck
  and replaced by the live one; its *Why this one* is dated *(as it stood on 2026-08-05)* so the
  transcript below it reads as history; criterion 1 is ticked **already met, by another task**, and
  criterion 4 is struck as **unmeetable, and kept to say so**.
- **T-030** loses *"The output is the harder half"* — it was, and it is gone. The passage now says
  when it stopped being true, shows today's output, and states plainly that criterion 2 is satisfied
  and therefore **cannot drive the removal**. What still stands is set out in its own paragraph,
  because it is now the whole task: an entry point no statement of the surface names, taking a
  positional directory where everything else takes `--root`.

### Step 5 — the two checks

```
grep "Answered by the maintainer" over both records
  T-023:95  Answered by the maintainer on 2026-08-07: `<shipped default>`
  T-030      Q1 answered 2026-08-06: remove          (both unedited)

grep for an absolute path over T-023, T-030 and this record
  none
```

**Outputs produced**
- `tasks/T-023-stop-config-errors-printing-an-absolute-install-path.md` — rescoped in place
- `tasks/T-030-settle-the-schema-module-s-own-entry-point.md` — evidence corrected, decision intact

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Neither task's `specify` asserts a behaviour the current code does not have — checked by running the commands each one quotes | met | §3 step 1, both re-run rather than taken from the audit. T-023's original transcript survives, marked as of its date, so it is history rather than a claim |
| Where a criterion has become unmeetable, it is marked so with the original kept | met | T-023 criterion 4 struck and annotated; T-023 criterion 1 and T-030 criterion 2 ticked as met **by another task**, which is the distinction that matters — satisfied is not the same as satisfied by this work |
| What each task is actually still for is stated in one sentence a reader meets first | met | T-023: a block quote above the outcome. T-030: *"What still stands, and it is the whole task"*, before the scope |
| The maintainer's recorded answers survive unchanged in both | met | §3 step 5. Neither answer block was touched; T-023's rejected option and its cost are still recorded as written on 2026-08-07 |
| No absolute path is written into either record while correcting them (R-23) | met | §3 step 5, and the pre-publish check run last over the whole tree |

**Child fix tasks raised**
- none. Both tasks stay open and keep their decisions; correcting what a reader is told is the whole
  outcome, and neither correction revealed work that is not already T-023's or T-030's.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met. Both premises were **re-run** rather than taken from the audit — the cheapest available failure here would have been to edit two records on the strength of a finding rather than on the behaviour, which is the exact mistake being corrected. Everything overtaken is struck through and kept, never deleted: a record edited to match what turned out to happen is a description, and a reader could no longer tell which parts predated the work. The distinction the criteria turn on is *met by another task* rather than plain *met* — T-023's criterion 1 and T-030's criterion 2 are both satisfied, by T-011, which is exactly why neither can still be evidence for the work its own task proposes. Neither status moved and neither decision was reopened. |
| 2026-08-09 | → in_progress | Plan puts T-023's reader-facing note **above the outcome** rather than in the log: someone opening that task reads the title and the outcome, both of which describe a fix that has already happened, and the log is where they would find out last. |
| 2026-08-09 | → specified | Answered: **T-023 stays open, rescoped to the wording**. So this task's work is not "delete a stale task" but "make two open tasks say what they are for" — T-023's outcome and transcript describe a leak T-011 removed, its criterion 1 is marked already-met and its criterion 4 marked unmeetable with the original kept per `review.md` *Changing a criterion*; T-030 keeps its decision and loses only its stale evidence. The alternatives are recorded with what each would have cost: folding the string into T-030 parks a decision on a task raised for a different question, and cancelling outright would let the string the maintainer explicitly rejected on 2026-08-07 stand as shipped behaviour by default. Criteria unchanged — the answer settles what the correction says, not how it is judged. |
| 2026-08-09 | → proposed | Raised as F-9 from the T-059 audit, clause 1. Verified before write-up by running both commands against a project outside this repository: neither prints an absolute path, and `git log -S` puts `_display()` in T-011's closing commit, after both tasks were raised. `medium`/`xs` — two `specify` sections, and the cost is a session hunting a defect that is gone. The distinction that makes this a finding at all: T-026 excluded task records as dated accounts, which is right for closed tasks and wrong for open ones, whose premises are instructions rather than history. |
