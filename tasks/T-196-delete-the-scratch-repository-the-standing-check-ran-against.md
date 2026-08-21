---
id: T-196
title: Delete the scratch repository the standing check ran against
type: admin
status: proposed
phase: specify
parent: T-193
blocked_by: []
related: [T-108]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-196 — Delete the scratch repository the standing check ran against

## 1. Specify

**Outcome**
`github.com/uchimata2/taskmd-standing-check-scratch` no longer exists, and
[T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s fifth acceptance criterion
is met in full rather than in half.

**Why this is a task and not a line in T-193**
T-193's criterion reads *the scratch repository is deleted, and the record says the destination was
never the evidence*. The second half is met; the first cannot be met by the session that ran the
work, and that was **measured rather than assumed** — `gh auth status` reports `gist`, `project`,
`read:org`, `repo`, `workflow`, and deleting a repository needs `delete_repo`. T-193 §1 records the
same limit from the day the grant was given, and says a plan whose last row is a session deleting the
repository cannot execute.

So the remainder belongs to whoever holds the account. It is a task rather than a sentence in a
closing record because **views read open work**: T-193 closes, and a note inside it stops being
anywhere anyone looks. The maintainer deleted [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)'s
scratch repository the same day for the same reason, and that disposal is the precedent this follows.

**Scope**
- In: deleting the repository, and recording that it is gone
- Out: adding `delete_repo` to any credential. Widening what a session can do to a hosting account
  is a decision for the owner, taken on its own evidence and not as a side effect of tidying up
- Out: anything about the nine rows or the binding. Both are T-193's, and T-193 is closed

**Inputs**
- [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) §3 step 10 — the
  repository name and why it was never the evidence
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the same
  disposal, done once before

**Acceptance criteria**
- [ ] `gh repo view uchimata2/taskmd-standing-check-scratch` fails with *not found*, and what it
      printed is recorded here
- [ ] This record says the repository held nothing that is not reproducible by re-running the
      procedure, so nothing was lost with it

**Open questions**
- none. The owner said on 2026-08-21, in the session that raised this, that they would do it by
  hand.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

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
| 2026-08-21 | → proposed | Raised by [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s review as the one criterion it did not meet. `medium` and `xs`: the repository is private and holds a copy of 24 public task records, so leaving it costs tidiness rather than exposure — but the criterion is not met until it is gone. A child of T-193 rather than a soft link, because T-193's criterion is what this closes. |
