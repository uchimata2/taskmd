---
id: T-189
title: Say whether the audit's method finding reached the repository that owns it
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-170, T-152]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: []
---

# T-189 — Say whether the audit's method finding reached the repository that owns it

## 1. Specify

**Outcome**
A decision on whether finding **E-08** of the context-economy audit was delivered to the repository
that owns the audit method, and [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)
§3's disposition of it corrected to say whichever it is. Second: a statement of whether *published,
therefore handed over* is a class worth checking for, now that two members of it are known.

**Why this one**
Found by [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) widening
its own sweep. T-170 corrected the U-01/U-02 disposition, whose false clause was *they stay in the
deliverable, which is the handover*. Its first sweep filtered on the ids it was about and found nine
hits; dropping the filter found a tenth, four rows above the one it had just fixed:

> **E-08** — Screen a figure on its source and on where the effect concentrates. A rule for the
> audit **method**, which is another repository's. Carried in the portable deliverable, which is the
> handover.

Same sentence, different recipient, and no evidence that anybody received it either.

**This one has a recipient, which is what makes it a different question from T-170's.** T-170 was
answered *no route exists* because the harness is not something this project can reach. The audit
method belongs to a sibling repository, and that sibling is **cloned beside this one on the owner's
machine** — so a route not only exists, the owner's own standing rule says what it is: a defect one
of these repositories finds in another arrives as a branch with a failing test, not as a report.
A finding about the method is not a defect in code, so whether that rule reaches it is exactly the
question.

**Scope**
- In: the decision, and the correction to T-152 §3's E-08 disposition
- In: naming the recipient and the route, if the answer is that it should be sent
- In: whether *published, therefore handed over* is worth a rule, or whether two instances is two
  instances
- Out: re-opening E-08 itself, its severity or its band. It is a finding about another repository's
  method and this task does not judge it
- Out: writing anything into the dated audit deliverables, for the reason
  [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) §1 gives

**Inputs**
- [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 — the disposition
  table, rows E-08 and U-01/U-02
- [`docs/audits/2026-08-15-context-economy-portable.md`](../docs/audits/2026-08-15-context-economy-portable.md) — E-08 in full
- [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) §3 — the sweep,
  and what its filter cost

**Acceptance criteria**
- [ ] The decision is recorded, with the rejected option named
- [ ] T-152 §3's E-08 disposition says what was actually done, and what it said before stays legible
- [ ] **The tree is swept for the claim as a phrase, not as an id**, and the count is stated. Two
      instances are known; the sweep says whether there are more
- [ ] The ruling says whether the class is worth a check, and if it says no, why two instances is
      not evidence of one
- [ ] The dated audit deliverables are unchanged, shown rather than asserted

**Open questions**
- **Should the finding be sent, given that a route exists?** T-170's answer turned on there being
  none. Here there is one, and the owner's standing cross-repository rule prefers a branch to a
  report — which does not obviously fit a finding about a method rather than about code. **The owner
  answers, at `specify`**; the alternative is that publishing it in this repository's own deliverable
  is what this project meant, and the wording says so.

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
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) raised it. **It does not answer §1's question** — that one asks whether to send something to another repository, which is the owner's to decide and not a phase to run. Under the grant's own instruction, this task therefore ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md)'s review, from widening a sweep that had been filtered by the ids the task was about. `xs` and `low`, like T-170, and for the same reason: the likeliest outcome is a recorded answer and a corrected clause. |
