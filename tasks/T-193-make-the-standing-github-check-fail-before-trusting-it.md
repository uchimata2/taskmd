---
id: T-193
title: Make the standing GitHub check fail before trusting it
type: deliverable
status: proposed
phase: specify
parent: T-178
blocked_by: []
related: [T-108, T-151, T-181]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-19
updated: 2026-08-19
adopter_visible: yes
deliverables: []
---

# T-193 — Make the standing GitHub check fail before trusting it

## 1. Specify

**Outcome**
The standing verification in the GitHub Issues binding has been run against a live issue backlog,
made to fail on a backlog broken on purpose, and then made to pass — with what it printed recorded.
The binding says so where a reader meets the procedure.

**Why this one**
[T-178](T-178-give-the-github-binding-a-standing-verification.md) shipped the procedure and closed
with this criterion **not met**, which is the criterion this repository cares about most: a check
that has only ever succeeded has not been tested, and this one has not even succeeded — nobody has
run it. Its §3 step 5 says why: breaking a backlog on purpose means creating and mutating issues on
a hosting service, and the session that wrote it was running unattended under a grant that covers
records rather than writes to anything outside them.

**The neighbouring procedure sets the standard, and it is not a high bar in principle.** The
migration *Verify* was run end to end into a private repository created for the day and deleted
after it, and **failed three times before it passed** — once at 324, once at 8 with every one of
those spurious, and once at 13 against a deliberately broken migration. Two of those failures are
the reason anybody trusts it. This task is the same day's work for the standing half.

**Requirements served**
R-16 (`docs/SCOPE.md`); [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s
rule, which is the general statement of what this task is an instance of.

**Scope**
- In: creating a scratch backlog, running the nine rows, breaking two things, running again,
  repairing, running again, deleting the scratch repository
- In: recording what each run printed, including the counts
- In: correcting the binding if a row turns out to be unanswerable from `enumerate`'s output — which
  is the thing an unrun procedure most plausibly gets wrong
- Out: changing what the nine rows check. That is
  [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s and is closed; a row that is
  *wrong* is in scope, a row somebody would rather were different is not
- Out: the migration procedure, which has its own recorded runs
- Out: automating any of it. Non-goal 10

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *Checking a backlog that is already here*,
  and *Verify — and make it fail first* for the standard
- [T-178](T-178-give-the-github-binding-a-standing-verification.md) §3 step 5 — the five numbered
  steps, written so this task does not re-derive them
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — how the
  scratch repository was made and disposed of

**Acceptance criteria**
- [ ] The procedure has been run against a live backlog, and what it printed is recorded — the
      actual output, not a verdict
- [ ] It has been run against a backlog broken on purpose in **two** ways, and **row 2 and row 3
      each named their own defect**. A run naming one and not the other is recorded as a
      half-proven procedure rather than as a pass
- [ ] The repair run passes, so the failure is shown to be the backlog's rather than the procedure's
- [ ] Any row that could not be answered from `enumerate`'s output is corrected in the binding, and
      the correction says what the run showed
- [ ] The scratch repository is deleted, and the record says the destination was never the evidence
- [ ] The binding no longer implies the procedure is unrun, and the *has been run against* register
      covers both verifications

**Open questions**
- **Who runs it, and where?** It needs a hosting account and permission to create, mutate and delete
  a repository. **The owner decides** — either authorising a session to do it, or doing it and
  handing back the output. Nothing else about this task is undecided; it is the one thing a session
  cannot take for itself.

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
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-178](T-178-give-the-github-binding-a-standing-verification.md) raised it. **The grant does not make this runnable**, and that is not a reading of its boundary but of what it authorises: creating and mutating issues on a hosting service is a write outside these records, and §1's question asks for exactly that permission. So the task ends in its written question, which is what the grant's own instruction says to do. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s review as the one criterion it did not meet. `high` and `m`: the procedure guards a documented path to unrecoverable loss, and until it has failed once nobody knows whether it guards anything. A child of T-178 rather than a soft link, because T-178 is not finished until this is — its own §4 says so. |
