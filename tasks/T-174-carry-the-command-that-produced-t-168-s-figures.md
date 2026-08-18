---
id: T-174
title: Carry the command that produced T-168's figures into a record that can re-run it
type: fix
status: proposed
phase: specify
parent: T-168
blocked_by: []
related: [T-168]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-174 — Carry the command that produced T-168's figures into a record that can re-run it

## 1. Specify

**Outcome**
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3's figures —
414 characters, 10 of 11 sessions, the three classes — can be produced again by someone who has only
the record. Today they cannot: the record describes the rule in prose and the scripts that ran it
were left in a scratchpad that does not survive the session.

**Why this one**
**Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s
review, where its criterion 2 failed.** That criterion asked for the cost "with the command that
produced it"; the record gives the figure, the unit and what was counted, and no command.

**The cause is a plan decision that changed at `implement` without being flagged**, which is the thing
[`implement`](../plugin/skills/taskmd/docs/method/implement.md) step 3 forbids. `plan` decided the
script would be "written to the scratchpad and **quoted in §3**, not committed"; §3 records it as
"described here rather than pasted". Quoted and described are not the same promise, and the narrower
one was substituted silently. Worth fixing as a record defect and worth noticing as a habit.

**Committing the script is not obviously the answer** and this task should not assume it is. T-168's
own reasoning still holds: the script reads a machine-private transcript store, and a test under
`tests/` reading it could never run for an adopter. Quoting it inside the record, which is what `plan`
actually decided, may be the whole fix.

**Scope**
- In: making T-168 §3's figures reproducible from the record alone
- In: whether the same gap exists in the other measurements this repository has taken against
  machine-private data, since the constraint that produced it is not unique to T-168
- Out: re-taking the measurement. The figures are not in doubt; their reproducibility is
- Out: changing what `tests/` may read. If the answer argues for that, it is its own task

**Inputs**
- [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §2 and §3 —
  the decision as planned and as carried out, which are the two texts that disagree
- `plugin/skills/taskmd/docs/method/implement.md` step 3 — the rule the substitution broke

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Does quoting the script in the record satisfy the criterion, or does reproducibility require
  something runnable?** A quoted script is copy-and-run for anyone with the store, and unrunnable for
  everyone else — which is also true of the measurement itself. **The maintainer decides**; the
  publishing constraint is the part nobody here can weigh alone.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review as the one criterion it did not meet. Raised rather than fixed in place, per [`review`](../plugin/skills/taskmd/docs/method/review.md) step 4 — repairing a criterion during its own review destroys the record of what was wrong. **Not covered by the authorisation of 2026-08-18**, which named T-168 and excluded everything it raises. |
