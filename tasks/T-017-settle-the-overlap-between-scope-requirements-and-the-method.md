---
id: T-017
title: Settle the overlap between SCOPE requirements and the method rules
type: decision
status: done
phase: review
parent: T-008
blocked_by: []
related: [T-003]
work_package: v0.1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - docs/SCOPE.md
  - tasks/T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md
---

# T-017 — Settle the overlap between SCOPE requirements and the method rules

## 1. Specify

**Outcome**
A decided, written answer to whether a requirement in `docs/SCOPE.md` may state the rule it
requires, or must only state that a rule is required — applied to the three cases where it
currently does both.

**Requirements served**
R-1 (`docs/SCOPE.md`).

**Why this one**
Found reviewing [T-008](T-008-write-the-backend-neutral-method-document.md), against its acceptance
criterion 7 ("R-6, R-7 and R-8 are stated **here and nowhere else**"). They are not:

| Rule | In the method | In the requirements |
| :--- | :--- | :--- |
| One phase per request | `docs/METHOD.md` §3.1 | `docs/SCOPE.md` R-6 |
| Ask to the exit criterion, batched | `docs/METHOD.md` §3.2 | `docs/SCOPE.md` R-7 |
| Discovery surfaced, never absorbed | `docs/METHOD.md` §3.3 | `docs/SCOPE.md` R-8 |

The overlap is close to verbatim — R-6 and §3.1 both say a next-step pointer "is context, not
authorization."

This is genuinely arguable, which is why it is a decision and not a fix. Both readings are
defensible:

- **Not duplication.** SCOPE states *what must be true* and is the register tasks cite; METHOD states
  the operative rule. The two serve different readers and R-1 is not engaged.
- **Duplication.** The same sentence exists twice. If someone sharpens the rule in METHOD, R-6 still
  reads the old way, and nothing reports the disagreement — which is the definition of drift, and
  SCOPE §3 requires every requirement to be testable, not to be the implementation.

The second reading is uncomfortable because SCOPE.md is a settled document (T-007) and its
requirements are cited by nine tasks. That is a reason to decide deliberately, not a reason to leave
it.

**Scope**
- In: the three rows above; the general rule that settles them; whichever document changes.
- Out: requirements that name a property rather than a rule (R-15, R-20 and similar) — they were
  never at risk. Re-opening any decision in `docs/SCOPE.md` §6.

**Acceptance criteria**
- [ ] A written rule for when a requirement may restate what it requires, in whichever document
      owns that convention
- [ ] The three rows resolved consistently with it
- [ ] Every task citing R-6, R-7 or R-8 still resolves and still means what it meant
- [ ] If the answer is "leave it", the reasoning is recorded where the next reviewer will find it —
      an unrecorded acquittal gets re-litigated

**Open questions**
- ~~Whose call?~~ **Decided by the maintainer, 2026-08-04** — see *Decisions*.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish the real extent of the overlap before deciding — three rows was the reported symptom. | the §3 finding |
| 2 | Put the decision to the maintainer with both readings and their costs. | a decision |
| 3 | Write the general rule where a future editor of §3A will meet it. | `docs/SCOPE.md` §3 preamble |
| 4 | Reword the instruction-shaped rows into testable properties. | `docs/SCOPE.md` R-6, R-7, R-8 |
| 5 | Sweep for further copies of the same three rules elsewhere in the tree. | whatever it turns up |
| 6 | Prove no phrase is now shared between the two documents. | `grep` output in §4 |

## 3. Implement

**Decisions & assumptions**
- **The overlap is §3A entire, not three rows** (2026-08-04, step 1). T-008's review reported R-6,
  R-7 and R-8. In fact every row of §3A restates something `METHOD.md` now says — R-1↔§1 rule 3,
  R-2↔§4, R-3↔§2, R-4↔§2, R-5↔§1 rule 4 and §5. Deciding on three rows would have set a precedent for
  nine, so the extent had to be established before the decision, not after.
- **The framing was the defect, not the duplication** (2026-08-04, maintainer). A requirement states
  a property the method must have; the method states the rule producing it. Two documents agreeing is
  what conformance *is*, and a requirement that could not be compared against the method could not do
  its only job. Rejected: making §3A point at `METHOD.md`, which reads as the tidier fix but is
  circular — a requirement saying "the method must say X" cannot judge whether the method got X
  right. Also rejected: leaving it and recording why, which preserves the near-verbatim wording that
  triggered this.
- **The boundary is what-must-be-true vs what-to-do** (2026-08-04). The licence is narrow and needed
  stating, or the next editor takes it as permission to copy freely. The written test: a row must
  survive someone rewriting the method completely — a property does, an instruction does not.
- **The project already had this rule; it had simply not been applied** (2026-08-04). §3's preamble
  said requirements must be testable. R-4 obeyed it ("cannot leave `implement` without recorded
  evidence"); R-6 did not ("never auto-advance" is an order). So the change extends an existing rule
  rather than inventing one, and the three rows needing work were exactly the three T-008's review
  found — arrived at independently, which is a reasonable check that the boundary is the real one.
- **A third copy existed outside both documents** (2026-08-04, step 5). `T-003` restated all three
  rules in the pre-rewrite wording — in the task whose stated purpose is stopping the skill becoming
  a second copy of the method. Replaced with a pointer to `METHOD.md` §3.

**Outputs produced**
- `docs/SCOPE.md` §3 preamble — the requirement/method relationship and the property-vs-instruction
  boundary
- `docs/SCOPE.md` R-6, R-7, R-8 — reworded as falsifiable properties
- `tasks/T-003-…md` — the third copy replaced by a pointer

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A written rule for when a requirement may restate what it requires | met | `docs/SCOPE.md` §3 preamble, immediately above the tables it governs — where an editor adding a row will meet it. |
| The three rows resolved consistently with it | met | Each now opens with a property and names what falsifies it. R-6 additionally states what the *method* must say, rather than saying it. |
| Every task citing R-6/R-7/R-8 still resolves and still means what it meant | met | Six files cite them (T-002, T-003, T-007, T-008, T-014, T-017); the numbers and their subject matter are unchanged, only the form. `check` reports 0 broken links. |
| If the answer is "leave it", the reasoning is recorded | n/a | The answer was not "leave it". The reasoning for the answer taken is recorded in the preamble, which is the same requirement in substance. |

**Verification** — no phrase now appears in both documents:

```
"context, not authorization"  -> docs/METHOD.md only
"never drip-fed"              -> gone (was SCOPE only)
"never absorbed"              -> gone (was SCOPE only)
"batched into a single turn"  -> gone (was SCOPE only)
"obvious continuation"        -> docs/SCOPE.md only
```

This also closes T-008's acceptance criterion 7, which its review carried here.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → done | Maintainer decided: the framing was the defect, not the duplication. §3's preamble gained the requirement/method relationship and the property-vs-instruction boundary; R-6, R-7 and R-8 reworded as falsifiable properties. Scope was wider than reported — §3A entire — and a third copy of the three rules was found in T-003 and replaced with a pointer. |
| 2026-08-04 | → proposed | Raised by T-008's review: acceptance criterion 7 not met as written. Flagged during T-008's implement phase and deliberately left for review to judge rather than settled by the author. |
