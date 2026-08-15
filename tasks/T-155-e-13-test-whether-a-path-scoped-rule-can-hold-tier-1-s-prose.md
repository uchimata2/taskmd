---
id: T-155
title: E-13 — Test whether a path-scoped rule can hold tier 1's prose about itself
type: decision
status: proposed
phase: specify
parent: T-152
blocked_by: [T-154]
related: [T-118]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-155 — E-13: test whether a path-scoped rule can hold tier 1's prose about itself

## 1. Specify

**Outcome**
A measured answer to whether the block of `CLAUDE.md` that is prose about `CLAUDE.md` can be scoped to
that file — **reported, and not carried**. What survives is the boundary: which loads the mechanism
reached and which it did not.

**Why this one**
Finding [E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), whose portable half is
[E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03). Both are stated there.

**Tested, not carried — the maintainer's ruling, 2026-08-15.** The remedy re-opens
[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md), which settled that an unannounced
activity is the exception that keeps a rule in tier 1. **New evidence licenses re-opening a recorded
decision, never reversing it**, so this task measures and reports; whether anything moves is a
separate decision taken on what it finds.

**Blocked by [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md)**, which settles the policy
question this task cites. Specifying the two independently produces inconsistent answers.

**Scope**
- In: the settling test the finding names — write the rule, restart, and read the `InstructionsLoaded`
  hook's log rather than the harness's documentation.
- In: the compaction case, which is the risk that decides the answer: compact, edit the instruction
  file, and observe whether the rule fires a second time.
- In: the objection that `.claude/rules/` is harness-specific while this repository ships a plugin
  meant to work anywhere. A mechanism an adopter cannot receive is worth less here than the size says.
- In: re-measuring the carve-out — how much of the block is operative for the agent rather than
  addressed to the maintainer. The audit's estimate is an estimate and says so.
- Out: moving anything in `CLAUDE.md`. Nothing moves in this task.
- Out: the justification passages that can stay in the file at no per-turn cost. That is
  [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md), taken first, and it may
  leave less here to argue about.

**Inputs**
- [E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) — the measured block and its three
  risks
- [E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03) — the mechanism and the named test
- [E-20](../docs/audits/2026-08-15-context-economy-portable.md#e-20) — why this remedy is measured
  rather than obeyed
- [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) — the decision this re-opens, and
  the reason it was taken

**Acceptance criteria**
- [ ] The test was run: a rule written, a session restarted, and the load **observed** — a document's
      claim about its own loading is not evidence
- [ ] The compaction case is answered by observation, or recorded as not answered and why
- [ ] The report names which loads the mechanism reached and which it did not, rather than a verdict
- [ ] Two failed attempts stop the task, with what survives recorded
- [ ] Nothing in `CLAUDE.md` moved as part of this task
- [ ] The carve-out is re-measured at the time of the test, not carried from the audit
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Where does the carry decision go if the test succeeds?** A follow-up task, or
  [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) re-opened in place. Re-opening a
  closed record has a cost this project has not paid before. **The maintainer answers, at `specify`.**

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
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), finding E-13. `decision` and not `fix`, on the maintainer's explicit ruling the same day: the remedy re-opens a decision recorded with a reason, so this task measures and reports and carries nothing. `s` — the work is one write, one restart and one observation, twice. |
