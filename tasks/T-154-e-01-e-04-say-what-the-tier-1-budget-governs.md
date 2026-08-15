---
id: T-154
title: E-01/E-04 — Say what the tier-1 budget governs, and what it cannot see
type: decision
status: proposed
phase: specify
parent: T-152
blocked_by: []
related: [T-028]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-154 — E-01/E-04: say what the tier-1 budget governs, and what it cannot see

## 1. Specify

**Outcome**
The tier-1 budget states its own scope, so a passing check is never read as a clean load path; and the
constraint the character figure cannot see is recorded beside it, marked as unmeasured.

**Why this one**
Two findings of [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), stated
there and not restated here:
[E-01](../docs/audits/2026-08-15-context-economy-portable.md#e-01) — the repository controls a
minority of the tier 1 it can see, and its own check passes, and both are true at once;
[E-04](../docs/audits/2026-08-15-context-economy-portable.md#e-04) — the limit that actually binds is
instruction count, and a size budget sees none of it.

**They are folded into one task because they are one edit to one rule.** Both say what the budget does
not govern, and separate tasks would each rewrite the same sentence. The alternative — two tasks — was
rejected in [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s implement,
with the reason.

**This task settles the policy question that
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) cites** — *what is
tier 1 for, and whose tier 1 does the budget govern*. Specifying the two independently produces
inconsistent answers, which is why that task is blocked on this one.

**Scope**
- In: where the bound is stated, and what `tests/test_budget.py` reports when it passes.
- In: recording instruction count as a second constraint — unmeasured, and said to be unmeasured.
- Out: changing the bound, the membership rule, or the unit. All three are
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md)'s and stand.
- Out: measuring instruction count, or acting on it. E-04 proposes no measurement and no remedy.
- Out: what is *in* tier 1. That is [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md)'s
  and [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md)'s.

**Inputs**
- [E-01](../docs/audits/2026-08-15-context-economy-portable.md#e-01) and
  [E-04](../docs/audits/2026-08-15-context-economy-portable.md#e-04)
- `CLAUDE.md`, the paragraph stating the bound
- `tests/test_budget.py`, and the line it prints on a pass

**Acceptance criteria**
- [ ] The rule names whose tier 1 the budget governs, in words that survive being read alone
- [ ] The second constraint is recorded as unmeasured, and nothing in the repository implies otherwise
- [ ] No figure from the audit is written into `CLAUDE.md`
- [ ] The budget test passes, and the effect of the change on the figure is stated — including zero
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Where does the scope statement live?** In `CLAUDE.md`, which every session pays, or beside the
  check in `tests/test_budget.py`, which only a reader of the check pays. The misreading it prevents
  happens where the *result* is read, which is the check — but the rule it qualifies is stated in the
  instruction file. **The maintainer answers, at `specify`.**

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
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), findings E-01 and E-04. `decision` rather than `fix`: neither finding names a defect, and both ask what a rule should claim about itself. `xs` because the change is a clause; `medium` because it saves nothing and makes two other findings decidable — the audit's own ranking says if only one item is ever taken, take this one. |
