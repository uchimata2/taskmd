---
id: T-208
title: Decide where the product-wide deviation clause belongs now that it exists
type: decision
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-187, T-045, T-027]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-21
updated: 2026-08-22
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

Written on 2026-08-22, once the owner's answer fixed which repair they judge. The decision itself is
recorded and is not one of these: what remains is `docs/SCOPE.md` §2's header, and showing that
nothing else rested on the sentence it replaces.

- [ ] **§2's header is true of principle 1 as principle 1 now stands.** A reader who applies the
      header to that principle finds no pointer the header does not license. What failure looks like:
      the header still licenses only a *narrower rule about how work is tracked*, while principle 1
      points at METHOD §4 for a product-wide exception that is neither narrower nor about tracking
- [ ] **The header is checked against every principle in §2, and the check is shown** — not against
      the one that prompted this. A header is a claim about its section, and this task exists because
      [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md)'s criterion was
      judged against two named principles and never reached the header above them. Judging the repair
      the same narrow way would be the same mistake one turn later
- [ ] **The header names the kind of thing METHOD may hold on a principle's behalf, and that kind
      covers a product-wide exception.** A header widened only far enough to admit T-187's clause by
      name leaves the next widening to re-open this silently, which is the failure mode
      [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md)'s wording
      already demonstrated once
- [ ] **Principle 1's own wording is unchanged**, shown by a diff — the owner's answer confines the
      repair to the header, and a principle edited to fit its header would be the decision reversed
      without being re-asked
- [ ] **The clause in `plugin/skills/taskmd/docs/METHOD.md` §4 is byte-identical afterwards**, shown
      by a diff. Its wording is out of scope and this task must be able to prove it did not drift
- [ ] **T-045's decision is left standing and the record says so.** §2 still *points* rather than
      stating a narrower rule; what changed is that a wider one now exists, which T-045's wording did
      not anticipate. What failure looks like: a header that reads as reversing T-045, so the next
      reader cannot tell which of the two decisions is live
- [ ] **`CLAUDE.md`'s pointer is shown still true, not assumed true** — §4 is read and confirmed to
      state what the pointer promises about the word *requires*. If `CLAUDE.md` is edited at all, the
      tier-1 figure is re-measured by running the suite and the number is stated
- [ ] `check` is clean and the suite passes

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
- **None outstanding.** The acceptance criteria above were written after the answer, so they judge the
  repair the owner chose rather than the choice.

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
| 2026-08-22 | → specified | **Specify agreed: eight criteria written, where §1 had carried a placeholder.** They judge only what the owner's answer leaves to do — `docs/SCOPE.md` §2's header — and they say twice, in different words, that the header must not be repaired the narrow way. **That is deliberate and is this task's own lesson turned on itself**: T-208 exists because [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md)'s criterion was judged against two named principles and never reached the header above them, so a criterion here requires the header be checked against **every** principle in §2, and another requires it name a *kind* of thing rather than admit T-187's clause by name — a header widened to fit one clause re-opens this the next time the clause widens, which is exactly how [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md)'s wording expired. Two criteria are diffs — principle 1 and METHOD §4's clause must both come out byte-identical — because the answer confines the repair to the header and a task that widened anything else would have reversed a decision without re-asking. Phase stays at `specify`; `plan` is not authorised (METHOD §3.1). |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its outcome edits `docs/SCOPE.md` §2's header, which the live handoff names as not to be tidied by a reconcile sweep.** That instruction is aimed at a sweeping session; this grant is what makes the repair this task's own authorised work. |
