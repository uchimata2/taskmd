---
id: T-021
title: Settle what the context closing line may say
type: decision
status: specified
phase: specify
parent: T-002
blocked_by: []
related: [T-003, T-022]
work_package: none
owner: maintainer
business_value: medium
effort: xs
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
- none. ~~Is a closing line that gives no direction a loss, or exactly the R-6 behaviour?~~
  **Answered by the owner on 2026-08-05: exactly the R-6 behaviour.** The owner asked for whichever
  option causes least trouble in the long term and fits what has since been designed; that is
  **(a) with (c)** — the criterion is replaced with wording a backend-neutral tool can satisfy, the
  CLI's closing line is confirmed as final, and direction-giving belongs to the skill.

**Why (a) + (c), and not (b)**

(b) — a config key declaring which status means each phase is finished — is the expensive answer.
The lifecycle would then be written in two places, `docs/METHOD.md` and every project's config, and
the copy in the config would be the one nobody re-reads when the method changes. That is the drift
this plugin exists to remove, bought for one line of output.

What settled it is a decision taken *after* this task was raised.
[T-022](T-022-filtered-task-listing-for-scripts.md) gives taskmd a command whose entire job is to
answer "what should I work on next", ordered by business value, effort and dependencies. "What next"
therefore has a home, and it is not a hint appended to `context`. Had (b) been built, taskmd would
have shipped two answers to one question — a per-task guess from `context` and a graph-wide answer
from the listing — which is the same defect one altitude up.

So the division is: **`context` reports state, the listing answers "what next", and the skill says
what to do about it.** Each fact keeps one home.

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
| 2026-08-05 | → specified | Owner chose (a) with (c): criterion 9 is replaced, the CLI's state-only closing line is final, and direction-giving is the skill's. (b) was rejected as a second home for the lifecycle. The deciding argument arrived after this task was raised — T-022 gives "what next" a command of its own, so a hint on `context` would have been a second answer to one question; soft edge added to record that. Implement is two edits: criterion 9's replacement text in T-002 §1 with the original kept, and its §4 row pointing here. |
| 2026-08-05 | → proposed | Raised by T-002's review. Flagged during `implement` rather than reinterpreted, and carried here rather than ticked — a reviewer cannot agree a criterion change with themselves. |
