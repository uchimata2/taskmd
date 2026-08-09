---
id: T-063
title: Measure the tier-1 member the rule declares
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-047, T-028]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-063 — Measure the tier-1 member the rule declares

## 1. Specify

**Outcome**
The command `CLAUDE.md` names for checking the tier-1 budget measures everything `CLAUDE.md` says is
in tier 1 — so the rule can be failed by the thing it was written to catch.

**Why this one**
Raised as **F-6** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 4. `CLAUDE.md` states two things a few lines apart:

1. tier 1 is *"this file **plus the taskmd `description`**"* — membership defined as a property, which
   is what [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) proved correct by
   measuring a session that was handed it;
2. *"both sides are counted from the tree (`wc -l CLAUDE.md reference/TASK-WORKFLOW.md`), so
   re-measuring never rewrites the rule"* — a command that counts one file.

The second cannot see the member the first just added. Measured 2026-08-09:

```
wc -l CLAUDE.md reference/TASK-WORKFLOW.md
164 CLAUDE.md
173 reference/TASK-WORKFLOW.md
```

The description is a further **397 characters**, which at this file's own 83-character average is
about five lines — so the stated 9-line margin is really about four. `CLAUDE.md` half-acknowledges
this (*"with less room than a count of this file shows"*) and then attributes the shortfall to the 26
lines [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) owes, not to
the description at all.

**What is new against T-047.** T-047 owns the move and the cut, and its log already records that tier
1 grows whenever a task closes. Two things it does not have:

- **The rule's own check is blind**, which is a defect in `CLAUDE.md` rather than a number T-047 has
  to chase. Nothing about re-measuring fixes a measurement that omits a member.
- **Tier 1 has grown 153 → 164** since T-047's last recorded measurement on 2026-08-08, so its
  projection moves from 153 + 26 = 179 (over by six) to 164 + 26 = 190 (over by seventeen). That is
  not a correction to T-047's arithmetic; it is a change in what that task has to find room for, and
  it arrived from ordinary reconcile edits with nobody touching the budget.

**Requirements served**
R-21 (`docs/SCOPE.md`) — *falsified by measuring a session*, which is exactly what a blind measurement
prevents; §1 *Token cost*.

**Scope**
- In: how the tier-1 side of the comparison is counted, given that one member is a file and one is a
  character count served by the harness.
- In: whether the rule's stated command stays a command someone can run, which is the property that
  keeps the rule from needing a written number.
- Out: **what leaves tier 1.** T-047's, explicitly, and this task must not pre-empt it — a
  measurement that also chooses the cut is the failure
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) declined to make.
- Out: the bound itself and the choice of `reference/TASK-WORKFLOW.md` as the comparator, both
  settled in T-028.
- Out: moving §3.1 and §3.3, which is T-047's whole content.

**Inputs**
`CLAUDE.md` *Working method*, `plugin/skills/taskmd/SKILL.md` front-matter (the description),
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md),
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) and its four
re-measurement log entries, [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-6.

**Acceptance criteria**
- [ ] The stated check counts every declared member of tier 1, and is a command a reader can run
- [ ] Running it today produces a result, and that result is stated — pass or fail, both count
- [ ] A character count and a line bound are reconciled explicitly; the conversion is written down
      once rather than left to whoever next re-measures
- [ ] Adding a second served skill would change the measured figure — the check tests the property,
      not a list of two files
- [ ] T-047's open question is untouched: nothing here says what should leave

**Open questions**
- **Does the bound become a character count on both sides?** Lines are what `reference/TASK-WORKFLOW.md`
  is naturally measured in and what every prior figure in T-047 is stated in; characters are what the
  harness actually serves and the only unit the description has. Converting both sides to characters
  makes the comparison exact and invalidates every recorded figure in T-028 and T-047, which is a real
  cost against a real gain. `plan` decides, and either answer has to survive the next skill being
  added.

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
| 2026-08-09 | → proposed | Raised as F-6 from the T-059 audit, clauses 1 and 4. Measured before write-up: 164 against 173, with a 397-character member the named command cannot see. `high` because it is a rule paid on every turn whose check cannot fail, and because T-047 is currently sized against a figure that moved by eleven lines without anyone editing the budget. Deliberately narrow: what leaves tier 1 stays T-047's, since a measurement that also chooses the cut is what T-028 refused to do. |
