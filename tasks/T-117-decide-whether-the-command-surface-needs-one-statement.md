---
id: T-117
title: Decide whether the command surface needs one statement
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-030, T-031]
work_package: v0.3
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-117 — Decide whether the command surface needs one statement

## 1. Specify

**Outcome**
A decision, recorded with its rejected alternative: either what taskmd's command surface is gets one
home and the other places point at it, or the several statements are confirmed as different registers
that legitimately each say it.

**Why this one**
Raised from [T-030](T-030-settle-the-schema-module-s-own-entry-point.md)'s review. That task's first
acceptance criterion asks for *"exactly one statement of what taskmd's command surface is, and it is
true"*. Its falsifier — no runnable entry point the surface does not name — is met. Its first clause
is not, and was not on the day it was written. Four places say what the surface is:

| Where | What it says |
| :--- | :--- |
| `README.md` | A table of the four commands, one row each, with what each is for |
| `plugin/skills/taskmd/taskmd/cli.py` | The module docstring opens *"The four commands"* and lists their invocations |
| `docs/SCOPE.md` | *"CLI at four commands"*, inside the decision that fixed the number |
| `CLAUDE.md` | Points at `README.md` for the list rather than repeating it — already the shape the others might take |

**This is a decision and not a fix**, which is why T-030 did not absorb it. The four are not obviously
one fact repeated: `README.md`'s table is a front door for someone who has not installed anything,
`cli.py`'s docstring answers *what is this file* for someone reading the source, and `docs/SCOPE.md`
records a bounded decision rather than describing a tool. The T-026 threshold's clause 2 asks whether
they would all have to be revised together — a fifth command would touch all four, which is what
makes the question worth asking rather than answering here.

**One of them cannot point at another**, and the answer must survive it: `cli.py` is inside `plugin/`,
and T-064 forbids anything there from naming `README.md`'s neighbours — `SCOPE.md`, `BRIEF.md`,
`CLAUDE.md`, an `R-NN` or a non-goal. Whatever home is chosen, the shipped docstring can point at it
only if it ships too. [T-031](T-031-give-the-list-rationale-one-home.md) hit exactly this and settled
for naming the task rather than the document.

**Requirements served**
R-1, R-18 (`docs/SCOPE.md`); the design rule — one home per fact.

**Scope**
- In: the four statements above, and whether the count of commands is one fact or several.
- Out: what the surface *is*. Four commands, settled by `docs/SCOPE.md` non-goal 11's amendment.
- Out: T-030's removal, which is done and which this does not reopen.

**Inputs**
`README.md`, `plugin/skills/taskmd/taskmd/cli.py` module docstring, `docs/SCOPE.md`, `CLAUDE.md`;
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md) §4;
[T-031](T-031-give-the-list-rationale-one-home.md) §3, for what the plugin boundary costs a pointer.

**Acceptance criteria**
- [ ] One of two outcomes is chosen and recorded with what it rejects: the surface gets one home and
      the others point at it, or the statements are confirmed as distinct registers
- [ ] If one home is chosen, it is stated how `cli.py`'s docstring reaches it without breaking T-064
- [ ] If distinct registers is chosen, it is stated what would have to be true for the answer to
      change — so the next reader who notices the repetition finds the reasoning and not just the fact

**Open questions**
- Is the count of commands a fact each of the four repeats, or does each state something different
  that happens to contain the same number? *Recommended: distinct registers, no change.* Three of the
  four are addressed to different readers and one is already a pointer, so the repetition is a number
  rather than an argument — and a number is cheap to correct, unlike the `list` rationale T-031 moved.
  *Alternative: one home, the others point at it.* It is the design rule applied literally, and it
  would have caught nothing here — no statement of the surface was wrong when T-030 found the fifth
  entry point; what was wrong was the entry point.

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
| 2026-08-11 | → proposed | Raised from T-030's review. Not a finding T-030 could absorb: its criterion asks for one statement, four exist, and collapsing them is outside a task scoped to `schema.py`'s `main()`. Typed `decision` because the answer may legitimately be "leave them" — three address different readers and the fourth is already a pointer. Put in `v0.3` rather than `v0.2`: nothing is wrong today, and the clause it comes from was already unmet when it was written. |
