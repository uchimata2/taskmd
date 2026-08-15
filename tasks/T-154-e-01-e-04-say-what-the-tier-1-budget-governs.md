---
id: T-154
title: E-01/E-04 — Say what the tier-1 budget governs, and what it cannot see
type: decision
status: done
phase: review
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
| 1 | Settle the placement question — where is the misreading actually made? | The decision below, and its rejected alternatives |
| 2 | State the scope as a line the check prints, naming what is loaded unasked and counted by nothing | `SCOPE` in `tests/test_budget.py` |
| 3 | State instruction count as a second constraint, and say in the same breath that nothing measures it | `UNMEASURED`, beside it |
| 4 | Point at where the share was measured instead of carrying the figure, so the line cannot go stale | Both lines name a finding id and no number |
| 5 | Reconcile the file's own header, which enumerated four proofs and now has six | The docstring of `tests/test_budget.py` |
| 6 | Run it and read the output | The output below |

## 3. Implement

**Decisions & assumptions**

- **Both statements go in the check's output, not in `CLAUDE.md`** — 2026-08-15, the open question,
  answered by the maintainer. The misreading is *a pass means the load path is clean*, and it is made
  where the pass is read. Putting the caveat in `CLAUDE.md` would charge every session, on every turn,
  for a footnote about a check it never runs — which is what that file's own membership rule forbids.
  **The effect on the counted figure is exactly zero.** *Rejected:* a clause in `CLAUDE.md`; and both,
  which would state one fact twice.
- **Neither line carries a number** — 2026-08-15. A share is two measurements and the denominator
  moves faster than the numerator, so the lines say *the larger part when last measured* and name the
  finding. The figure has one home, in [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s report, dated.
- **E-04 is recorded and nothing acts on it** — 2026-08-15. The finding proposes no remedy and no
  measurement; writing a line that says *unmeasured* is the whole of it. Anything more would be this
  task inventing work the finding declined to ask for.

**Outputs produced**

`tests/test_budget.py` — two statements, and the header reconciled from four proofs to six. Run:

```
tier 1 6305 chars under by 1541 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       836 chars of block comment are not counted: the harness is documented to strip them before injecting and this check follows it - not yet observed here (T-153)
scope  this repository's own tier 1 - the files named above. The harness, the user's own files
       and the skill catalogue are loaded unasked as well, are counted by nothing here, and
       were the larger part when last measured. A pass is not a clean load path (E-01)
also   instruction count is a second constraint on the same file, and it is the one reported to
       bind - for adherence, not for tokens. Nothing here measures it, and nothing claims to (E-04)
```

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The rule names whose tier 1 the budget governs, in words that survive being read alone | met | The `scope` line above. It is printed by the passing test and by the failure message, so it arrives with the verdict it qualifies. |
| The second constraint is recorded as unmeasured, and nothing implies otherwise | met | The `also` line says both halves in one sentence. |
| No figure from the audit is written into `CLAUDE.md` | met | Nothing was written into `CLAUDE.md` at all by this task. |
| The budget test passes, and the effect on the figure is stated — including zero | met | 7 tests, OK. **The effect is zero**: both statements live in the check, which is not counted. |
| The measured outcome is written into this record on the day it is known | met | Above, 2026-08-15. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), findings E-01 and E-04. `decision` rather than `fix`: neither finding names a defect, and both ask what a rule should claim about itself. `xs` because the change is a clause; `medium` because it saves nothing and makes two other findings decidable — the audit's own ranking says if only one item is ever taken, take this one. |
| 2026-08-15 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review` — in a request covering T-153, T-154, T-155, T-156 and T-157 and **nothing else**. Any task raised from here takes one phase per request unless separately authorised (METHOD §3.1). Recorded in each of the five records because an authorisation kept anywhere else is one a later session can miss or stretch. |
| 2026-08-15 | → done | All four phases run and all five criteria met. Both statements went into the check's output on the maintainer's answer, so the counted tier-1 figure is unchanged by this task — the finding's gain was `enabler` and it bought exactly what an enabler buys. [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) is unblocked by this closing. |
