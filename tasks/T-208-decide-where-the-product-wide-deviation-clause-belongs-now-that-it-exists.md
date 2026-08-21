---
id: T-208
title: Decide where the product-wide deviation clause belongs now that it exists
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-187, T-045, T-027]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-21
updated: 2026-08-21
deliverables: []
---

# T-208 — Decide where the product-wide deviation clause belongs now that it exists

## 1. Specify

**Outcome**
A decided, written answer to whether the deviation clause
[T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) added belongs in
`plugin/skills/taskmd/docs/METHOD.md` §4, and `docs/SCOPE.md` §2 brought back into agreement with
whichever answer is given — including §2's own header, which currently describes a pointer this
repository no longer only has.

**Why this one**
**Found after T-187 closed, by applying that task's own criterion 6 one paragraph wider.** That
criterion asked that the rule's other statements not contradict the amended one, and it was judged
against `docs/SCOPE.md` §2 **principles 1 and 2**. It did not reach §2's **header**, which says:

> They govern the **whole product** … which is why they are stated here in full rather than pointed
> at. Where a principle *also* holds as a narrower rule about how work is tracked, `METHOD.md` states
> that version and this section points at it.

So §2 points at METHOD **only for a narrower, tracking-scoped version of a principle**. T-187's clause
is not narrower and is not about tracking: it is the product-wide rule's exception, and principle 1
now points at METHOD §4 for it. That is the header's condition unmet.

**[T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) said this in advance
and nobody re-read it.** Its §3 records the pointer being written to name *what case* METHOD §4
covers — the inverse of a link — "rather than implying METHOD states the qualification for facts in
general, **which it does not**". Since 2026-08-21 it does. The premise under a decided task expired,
and the only reason it was noticed is that T-187 edited the sentence resting on it.

**The deeper question is which document is the clause's home**, and T-187 did not ask it. METHOD.md's
own first line is *how work is tracked*, and §4 is *Edges*; `docs/SCOPE.md` §2 is where the
product-wide rule is stated in full, by that section's own explanation of itself. T-187 placed the
clause in METHOD on the strength of the owner's phrase *the rule's own home* and `CLAUDE.md`'s
pointer, both of which name §4 — and neither was written when a product-wide exception existed.

**It is a decision and not a fix**, which is why it is raised rather than repaired: every available
repair presumes the answer.

**Scope**
- In: where the clause lives — METHOD §4 as it stands, `docs/SCOPE.md` §2 principle 1, or both with
  one pointing
- In: `docs/SCOPE.md` §2's header, made true of whatever §2 then does
- In: whether `CLAUDE.md`'s pointer still says something true afterwards, judged against the tier-1
  figure rather than assumed
- Out: the **wording** of the clause, which T-187 settled and which this does not reopen. Its purpose,
  its condition and its refusal case stand wherever it ends up
- Out: T-045's decision that §2 **points** rather than states a narrower rule. That holds; what has
  changed is that a wider one now exists, which its wording did not anticipate

**Inputs**
- [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) §3 step 5 — the
  per-document read that reached principles 1 and 2 and stopped
- [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) §3 — the sentence-by-sentence
  boundary, and the premise that expired
- `docs/SCOPE.md` §2 — the header and principle 1
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the clause as written, and §1 rule 3 which defers to it

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**Where does a product-wide qualification belong — `METHOD.md` §4, or `docs/SCOPE.md` §2
  principle 1?** **The owner decides**, because it is the placement of the rule every design decision
  here is checked against and the two documents have different audiences: METHOD ships to adopters and
  says it is about *how work is tracked*; SCOPE is this project's own and says its principles govern
  the *whole product*. **Recommended: leave the clause in METHOD §4 and widen §2's header**, on the
  ground that an adopter reading METHOD is the reader who most needs it and is the one reader SCOPE
  never reaches — `CLAUDE.md`'s pointer already promises §4 states what the word *requires* does and
  does not forbid, so moving it would falsify tier 1 as well. *The cost if that is wrong*: METHOD
  carries a product-wide rule under a heading about edges, and §2's explanation of why it states
  things in full gets a second clause. *The alternative*: state the clause in §2 principle 1 and have
  METHOD §4 point up at it — truer to each document's stated scope, and it moves the clause out of
  everything an adopter receives, which is the half that made T-187 write the case generically in the
  first place.~~ **Answered by the owner on 2026-08-22: the clause stays in `METHOD.md` §4, and `docs/SCOPE.md` §2's header is widened** — see the Log row of that date.

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
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* immediately after [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) closed, by re-reading `docs/SCOPE.md` §2 whole rather than the two principles that task's criterion named. `high` because it is the placement of the one rule every design decision here is checked against, and `s` because the argument is written and only the choice is missing. **Not covered by the grant T-187 ran under**, which reached three named tasks and nothing any of them raised. It carries an open question that is the owner's, so nothing starts on it. |
| 2026-08-22 | (no change) | **The open question is answered by the owner: leave the clause in `METHOD.md` §4 and widen `docs/SCOPE.md` §2's header.** Asked in the batched round of 2026-08-22, and it is the recommendation §1 carried. An adopter receives METHOD and never receives SCOPE, so they are the reader who most needs the clause; `CLAUDE.md` already promises §4 states what *requires* does and does not forbid, so moving it would falsify tier 1 as well. *Rejected: state it in §2 principle 1 and have METHOD §4 point up*, truer to each document's stated scope, but it moves the clause out of everything an adopter receives — the half that made [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) write the case generically — and falsifies `CLAUDE.md`'s pointer too. The known inconsistency in §2's header is now repairable, but repairing it is this task's work and is not authorised by this row. |
