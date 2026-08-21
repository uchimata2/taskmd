---
id: T-209
title: Report an open child as a blocker on the parent that cannot close
type: fix
status: proposed
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
- Out: waits that are not tasks — see the open question, which decides whether those become a task
  of their own rather than being folded in here

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
- **Do waits that are not tasks belong in the model at all?** Every one of the ten open tasks is
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
  nothing can validate and nothing clears when the wait ends.

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
