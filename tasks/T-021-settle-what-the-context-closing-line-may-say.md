---
id: T-021
title: Settle what the context closing line may say
type: decision
status: proposed
phase: specify
parent: T-002
blocked_by: []
related: [T-003]
work_package: none
owner: maintainer
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-021 — Settle what the context closing line may say

## 1. Specify

**Outcome**
A decision by the owner of T-002's criteria: either the criterion is replaced with wording a
backend-neutral tool can satisfy, or the closing line gains something it does not have.

**Why this one**
T-002's ninth criterion reads:

> **`context`'s `NEXT:` hint reads phase *and* status** (R-3) — proven on a task whose status has
> moved past its phase, where the current tool tells you to redo the phase you just finished.

It was **not met as written**, and the reason is structural rather than an oversight. `phase` is one
project's vocabulary field. The tool can print its value — it does — but it cannot know that status
`planned` means the `plan` phase is *finished*, because that mapping lives in `docs/METHOD.md`, not
in the schema. A tool that inferred it would be hardcoding this project's vocabulary, which
criterion 7 forbids in the same list.

What was built: the header prints every `context_fields` value, so both axes are on screen, and the
closing line carries only derived state and names no phase at all. On T-002 at
`status planned | phase plan` — planning finished:

```
interim  NEXT: read the file above, then work the 'plan' phase.
new      STATE  open, no blocker outstanding
```

The defect the criterion was written against is gone: nothing instructs, so nothing can instruct you
to redo the phase you just finished, which also settles the R-6 concern the criterion carried. What
is unresolved is whether "gone" is what was wanted, or whether a correct hint was.

`docs/method/review.md` is explicit that a criterion which turns out to be wrong may be replaced —
openly, with the original recorded, **and agreed by whoever agreed the original**. This task is that
agreement. A reviewer cannot grant it to themselves; that is the whole point of the rule.

**Requirements served**
R-3, R-6 (`docs/SCOPE.md`).

**Scope**
- In: what the closing line of `context` may say, and the wording of T-002's criterion 9.
- Out: anything the skill says. If the answer is "the agent should be told what to do next", that is
  T-003's to carry, not the CLI's — the CLI would then keep its line unchanged.

**Inputs**
T-002 §1 criterion 9 and §3 *A criterion that could not be met as literally worded*;
`docs/METHOD.md` §2 (phase and status are independent) and §3.1 (a pointer is not authorization);
`docs/method/review.md` *Changing a criterion*.

**Acceptance criteria**
- [ ] One of three outcomes is chosen and recorded with its rejected alternatives: (a) the criterion
      is replaced, with the original text kept alongside; (b) the CLI gains a phase-aware line and a
      config key that makes the status-to-phase mapping declarable; (c) the whole concern moves to
      the skill and the CLI line is confirmed as final
- [ ] If (b), it is stated how the mapping avoids becoming a second home for the lifecycle that
      `docs/METHOD.md` already defines
- [ ] T-002's criterion row is updated to point here, so no future reader finds a bare "not met"
      with no resolution

**Open questions**
- Is a closing line that gives *no* direction a loss for an agent starting a task cold, or exactly
  the R-6 behaviour the method asks for? — maintainer. This is the substantive question; the wording
  follows from it.

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
| 2026-08-05 | → proposed | Raised by T-002's review. Flagged during `implement` rather than reinterpreted, and carried here rather than ticked — a reviewer cannot agree a criterion change with themselves. |
