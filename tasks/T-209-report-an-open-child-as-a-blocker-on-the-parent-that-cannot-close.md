---
id: T-209
title: Report an open child as a blocker on the parent that cannot close
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-191, T-198]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-209 — Report an open child as a blocker on the parent that cannot close

## 1. Specify

**Outcome**
A task whose child is still open is reported as waiting on that child, rather than as having nothing
outstanding. The edge is already stored, so nothing new is written anywhere — the derivation is the
whole of the change.

**Why this one**
`audit.md` step 5 says it plainly: *Close the umbrella only when every child is resolved — done, or
dropped with a recorded reason.* Two umbrellas in the current backlog are in exactly that state, and
the tool says otherwise. Measured 2026-08-22:

| Task | Children | What `context` reports |
| :--- | :--- | :--- |
| [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) | T-197 done, **T-198 review** | `STATE  open, no blocker outstanding` |
| [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) | T-201 done, **T-202 proposed**, T-204 done | `STATE  open, no blocker outstanding` |

**Re-measured later on 2026-08-22, after this repository's own work moved one of the rows.** The
table above is left as it was taken. T-198 has since gained a fourth child and T-202 has moved
`proposed` → `specified`, so the row's detail is no longer current — and the defect it was taken to
show is unchanged, which is the point of re-running it rather than reasoning about it:

```text
$ taskmd context T-191
CHILDREN
  T-197        done        Derive the test harness's problem-class list from the code
  T-198        review      Show each quiet fixture is within its own check's reach
STATE  open, no blocker outstanding

$ taskmd context T-198
CHILDREN
  T-201        done        Give the fenced-table case a row that could be reported
  T-202        specified   Mark a fixture's quiet cases so a sweep can find them
  T-204        done        Count the short-row quiet case the wide-row audit left out
  T-210        done        Account for the two derived fixtures T-198's partition drops
STATE  open, no blocker outstanding
```

**Three of T-198's four children are now resolved and the fourth is further along than it was, and
the line has not moved** — because it never read them. `CHILDREN` prints the very thing `STATE`
claims is absent, four lines above it, which is the sharpest form the defect takes.

`check` is green over both, and `list --open` ranks them alongside tasks that really are free to
start. So a session choosing what to work on is told that two of the ten open tasks have nothing in
front of them, when each is behind a chain it cannot shorten.

**The shape is the one this project keeps finding.** The rule exists, the data supporting it exists,
and nothing reads the place it lives — the same class as
[T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md)'s second index, which
`check` passed twice in a row. It is worse than silence here: `no blocker outstanding` is an active
claim, so a reader has no reason to look further.

**What is not wrong.** `STATE` is accurate about `blocked_by`, which is empty on both. The defect is
that `blocked_by` is not the only thing that stops a task closing, and the line does not say which
question it answered.

**Scope**
- In: what `context` reports for a parent with at least one unresolved child, and whether the same
  belongs in `check`
- In: a case that must not fire — a parent whose children are all resolved keeps reporting no
  blocker outstanding
- Out: **any new front-matter field.** The parent edge is already stored and children are already
  derived; a field here would be the same fact written twice, which `CLAUDE.md`'s one design rule
  forbids
- Out: waits that are not tasks. **Settled by the owner on 2026-08-22**: they stay as prose, they are
  not folded in here, and no task is raised for them — so this scope is now closed rather than
  pending an answer

**Inputs**
- `plugin/skills/taskmd/docs/method/audit.md` step 5 — the rule being enforced
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the edge kinds, and what may be derived

**Acceptance criteria**
- [ ] The gap is demonstrated **failing first**: the command output above, re-run and recorded,
      before anything changes
- [ ] After the change, the same command on the same task names the unresolved child as the
      outstanding wait
- [ ] A parent whose children are all resolved still reports no blocker outstanding, proven by
      running it rather than by reading the code
- [ ] Whether `check` reports it too is decided, and the decision is recorded either way — including
      if the answer is that it does not

**Open questions**
- ~~**This question is why `specify` is worked but not agreed, and the status stays `proposed`.** It
  changes the outcome rather than only a later phase — the scope's last *Out* defers to it, and the
  effort estimate covers the child half alone — so `specify.md` step 5 says it must be answered before
  this phase can end. It was **not** part of the batched round the owner answered on 2026-08-22: this
  task was raised after that round went out. No grant of phases can answer it.~~ **Answered by the
  owner on 2026-08-22, later the same day** — see the Log row. `specify` is now agreed and the status
  is `specified`; the phase does not advance.
- ~~**Do waits that are not tasks belong in the model at all?** Every one of the ten open tasks is
  waiting on something, and only two of those waits are task-to-task. The rest are an owner's
  answer, a person who has not been named ([T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md),
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)) and an event that
  cannot be scheduled ([T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)).
  **The owner decides**, because it is a change to what the schema means rather than to what the tool
  derives from it. **Recommended: leave them as prose and close this task on the child half alone**,
  on the ground that a wait on a person or an event has no second party to store the edge against, so
  any field for it is a hand-kept status — the class this project removes rather than adds. *The cost
  if that is wrong*: `list --open` keeps ranking a task nobody can start beside one anybody can, and
  the only thing that says so is a sentence somebody has to read. *The alternative*: a `waiting_on`
  free-text field, which makes the wait visible in every generated view at the price of a value
  nothing can validate and nothing clears when the wait ends.~~ **Answered: the child half alone,
  and the `s` estimate stands.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* while answering a request for the open list with a blocks column. Building that column meant reading `blocked_by` on all ten open tasks, finding it empty on every one, and then checking `context` against the two parents that visibly cannot close — which is where the disagreement with `audit.md` step 5 turned up. `medium` rather than `high`: nothing is corrupted and no gate passes work it should stop, so the damage is a misread rather than a bad state — but the rival was argued, on the ground that the method states a rule nothing enforces and `no blocker outstanding` is an assertion rather than a silence. `s` because both the parent edge and the derived children already exist, so nothing is stored and only the report changes; that estimate covers the child half only, and the open question could widen it. It carries an open question that is the owner's, so nothing starts on it. |
| 2026-08-22 | (no change) | **`specify` worked and deliberately not agreed; the status stays `proposed`.** The evidence was re-run rather than re-read, and it needed to be: this session's own work gave T-198 a fourth child and moved T-202 to `specified`, so §1's table was stale within hours of being written. The table is **left as it was taken** and the re-measurement sits below it (METHOD rule 5). **The defect is unchanged and now shows more sharply** — three of T-198's four children are resolved, the fourth has advanced a phase, and `STATE` still prints `open, no blocker outstanding` four lines under a `CHILDREN` block that lists them. **What does not move is the phase.** The open question — whether waits that are not task-to-task belong in the model — changes this task's outcome and not merely a later phase: the scope's last *Out* defers to it and the `s` estimate covers the child half alone. So `specify.md` step 5 forbids ending the phase, and the multi-phase grant this session ran under authorises **phases, not answers**. The question was never in the batched round of 2026-08-22 — this task was raised after it went out — and it is carried to the owner with the recommendation and both costs §1 already records. |
| 2026-08-22 | → specified | **The open question is answered by the owner: leave waits that are not task-to-task as prose, and close this task on the child half alone.** Put to them in a two-question round the same day, after the phase had been worked and stopped at exactly this point. It is the recommendation §1 carried: a wait on a person or an unschedulable event has no second party to store the edge against, so any field for it is a hand-kept status — the class this project removes rather than adds — while the child half stores nothing at all, because `parent` is already recorded and `children` is already derived. *Rejected: a `waiting_on` free-text field*, which makes every wait visible in every generated view, at the price of a value nothing can validate and nothing clears when the wait ends, and which would widen this task past its `s` estimate. **The known cost of the answer, recorded with it**: `list --open` keeps ranking a task nobody can start beside one anybody can, and the only thing that says so is a sentence somebody has to read. The scope's last *Out* is now closed rather than pending, the four criteria are unchanged, and the estimate stands. **The phase does not advance** — this row ends `specify`; `plan` is not authorised (METHOD §3.1). |
