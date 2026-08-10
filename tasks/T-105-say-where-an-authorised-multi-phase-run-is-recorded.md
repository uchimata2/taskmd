---
id: T-105
title: Say where an authorised multi-phase run is recorded
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-005, T-036, T-047]
work_package: v0.3
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-105 — Say where an authorised multi-phase run is recorded

## 1. Specify

**Outcome**
When the owner waives *one phase per request* for particular tasks, the method says where that
authorisation is written — so two projects record it the same way and a later session can neither
miss it nor over-apply it.

**Why this one**
Raised as **R-7** by the first adopting project (`control/LOCAL-CONTEXT.md`), which calls it the
least of its seven and recommends nothing structural. METHOD §3.1 is the right default and that
project holds to it. It was also explicitly waived once, by the owner, for four small tasks. Nothing
in a task file can carry that, so the authorisation lived in a handoff document and in Log rows on
the tasks — and it had to say, in prose, which tasks it covered and that it did not generalise.

**The failure it leaves is two-sided.** An authorisation recorded outside the tracker can be missed —
the next session re-asks for permission already given — or applied to a task it never covered, which
is §3.1's rule silently disabled. Neither is visible.

**A waiver is state, and §3.1 is a rule about requests.** That tension is the whole of the question,
and it is why the answer is a sentence rather than a field: the rule says a pointer is context and
not authorization, and a waiver written into a file is precisely a pointer that later claims to be
authorization. Wherever it is recorded has to survive that reading.

**One constraint on the size of the answer.**
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) moves §3.1 into the
always-loaded tier. Anything added to it is then paid on **every turn of every session**, against a
budget that already does not pass. So this is one sentence in §3.1 if it must be there, or a
paragraph in a phase file if it need not be — and which of those it is, is the decision.

**Requirements served**
R-6 (`docs/SCOPE.md`) — a phase is worked only when it was requested, which is the rule being waived.
R-8, since an authorisation is exactly the kind of thing that must leave a trace.

**Scope**
- In: one sentence or paragraph saying where a waiver is recorded — the task's own log, naming who
  gave it and what it covers.
- In: whether it belongs in METHOD §3.1 itself or in a phase file, given the tier-1 cost above.
- In: whether a waiver may cover more than one task, and how that is written without becoming a
  standing permission.
- Out: a front-matter field for waivers. That stores an authorisation as task state, and the whole
  point of §3.1 is that state is not a request.
- Out: reopening the rule. It is right and this does not touch it.

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §3.1 and `docs/method/rationale.md`.
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md), for the budget any
  addition to §3.1 is charged against.
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, for what a task's log is here.

**Acceptance criteria**
- [ ] The method says where a waiver is recorded, in one place
- [ ] It says what the record must name — who gave it and which tasks it covers — so it cannot be
      read as general
- [ ] If it lands in §3.1, the tier-1 measurement in `CLAUDE.md` is re-run and the cost is stated
- [ ] `check` is clean on this repository

**Open questions**
- **§3.1 or a phase file?** *Recommended: one sentence in §3.1.* The waiver is met at the moment the
  rule is, and a reader who has only tier 1 is exactly the reader who needs it. *Alternative: a
  paragraph in `method/implement.md`*, which costs the always-loaded tier nothing and is not read
  until after the moment it was needed.

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
| 2026-08-10 | → proposed | Raised as R-7 from the first adopting project's recommendations, which ranks it last of seven and asks for nothing structural. `medium` because the failure is silent in both directions — a later session can miss a permission already given, or apply it to a task it never covered — and `xs` because the whole work is a sentence and where to put it. Two things recorded here rather than left to `specify`: a waiver is *state* while §3.1 is a rule about *requests*, which is why the rule's own "a pointer is context, not authorization" line has to survive whatever is written; and T-047 moves §3.1 into the always-loaded tier, so anything added there is billed on every turn against a budget that already does not pass. That is the constraint on the size of the answer, and it is what makes the placement a decision rather than a formality. |
