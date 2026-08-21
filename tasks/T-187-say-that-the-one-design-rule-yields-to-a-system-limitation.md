---
id: T-187
title: Say that the one design rule yields to a system limitation
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-179, T-012]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-19
updated: 2026-08-19
deliverables: []
---

# T-187 — Say that the one design rule yields to a system limitation

## 1. Specify

**Outcome**
The one design rule — *store the forward edge; derive the rest* — states its own purpose and the
condition under which a project may deviate from it, so that a decision to write a fact twice can be
judged against a written test instead of argued from first principles each time.

**Why this one**
**The owner ruled it on 2026-08-19**, while answering
[T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md)'s open question in the backlog-wide
round of that date. The words were that single source of truth is the *ultimate goal* rather than an
absolute, that its purpose is to minimise inconsistency and unnecessary administration, and that a
system configuration or comparable limitation is grounds to deviate.

**It is raised here rather than folded into T-179 for the reason that task's answer gives.** T-179
changes one binding document; this changes the rule every design decision in the repository is
checked against, and it lives at a different tier — `CLAUDE.md` carries the pointer, and the rule is
stated in full in `plugin/skills/taskmd/docs/METHOD.md` §4. A ruling of that reach recorded inside a
binding task is one a later session reads as being about bindings.

**The rule already admits one exception and does not say why.** METHOD §4 draws a line around what
the word *requires* does and does not forbid, and
[T-012](T-012-decide-whether-soft-edges-are-symmetric.md) settled that a derived inverse may be
written twice. So the amendment is expected to make an existing tolerance explicit rather than to
open a new one — which is also the risk: a deviation clause loose enough to cover any inconvenience
retires the rule.

**Scope**
- In: the amended wording of the rule in its own home, carrying its purpose and the deviation
  condition
- In: whether `CLAUDE.md`'s pointer needs any change, judged against the tier-1 budget rather than
  assumed
- In: whether the existing tolerances — T-012's derived inverse, and the two rules `CLAUDE.md`
  restates verbatim — are instances of the new clause or remain separately stated
- Out: re-opening any decision the rule has already been used to settle. A clause that arrives with
  a list of decisions it reverses is a rewrite, not an amendment
- Out: T-179's own answer, which stands on the binding's precedent and does not wait on this

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the rule in full, and the text this amends
- `CLAUDE.md` — the pointer, and the two-rule exception it already carries
- [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md) — the answer this ruling arrived
  with, and the case that prompted it
- [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) — the one deviation already settled

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**What stops the clause swallowing the rule?**~~ **Answered 2026-08-21: the amendment must name
  what does *not* qualify.** The owner required it. The argument given is this project's own
  [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) rule applied to prose: a
  check is trusted only once it has been seen to refuse something, and a deviation clause with no
  refusal case retires the rule it is attached to. Stating the condition alone was the alternative
  and was rejected. **No phase was started on this answer**
  ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)): it settles what `specify`
  owes, and the work is done when it is asked for.

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
| 2026-08-21 | (no change) | **Answered by the owner: the amendment must name a case that does not qualify.** Stating the deviation condition alone was offered and rejected, on [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s ground - a rule trusted without having refused anything is a licence. §1's question is struck through with both. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised from the owner's answer to [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md), given in the backlog-wide question round of 2026-08-19. `high` because the rule is the one every design decision here is checked against, and an unwritten deviation condition is currently settled by argument each time. **Not covered by any standing authorisation** — the round of 2026-08-19 answered questions and authorised [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) alone. |
