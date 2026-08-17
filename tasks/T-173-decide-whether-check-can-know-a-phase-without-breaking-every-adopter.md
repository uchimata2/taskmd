---
id: T-173
title: Decide whether check can know a phase without breaking every adopter
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-172, T-151]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-173 — Decide whether check can know a phase without breaking every adopter

## 1. Specify

**Outcome**
A recorded answer to whether `check` should be able to reason about a task's *phase*, and at what
price — or a recorded decision that it should not, so the next person to want it finds the reason
rather than the gap.

**Why this one**
Raised from [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md)'s `review`,
carrying the unmet half of its first acceptance criterion. `check_abandoned_slots` reports a slot left
in a **closed** record. The criterion agreed at `specify` was wider: no record carrying a slot in a
section it has **already passed**. A task sitting at `review` with an unfilled `implement` satisfies
the wider text and is not reported.

**The narrowing was a decision, not an omission**, taken by the owner during T-172's `implement` once
the price was known. Three things the tool does not know stand in the way, and they are in T-172 §3
with the evidence:

- which front-matter field carries the phase — `phase` appears nowhere in `schema.py`
- that a body heading corresponds to a phase value
- that `done` and `cancelled` differ, where `open_statuses` says only open or closed

Each is project vocabulary. Carrying them means new config keys, and `defaults/config.md` §*Adding a
key to this file is a breaking change* is unambiguous about the consequence: a config replaces the
default rather than merging, so **every project that wrote its own config fails on its next upgrade**,
naming a key nobody there has heard of. No key has been added since the schema shipped.

**Why it is Low.** The shape it would catch — a record past a section it never filled — occurs **0
times in 172 tasks** here. The value is entirely in whether the capability is wanted for other
reasons; if it is not, the honest outcome is a recorded *no* and this task closes having spent one
record.

**Scope**
- In: whether `check` gains any notion of phase at all, and if so how the vocabulary reaches it
- In: whether the `done` / `cancelled` distinction is worth a key on its own, independently of phase.
  T-172 had to treat them alike and repair two cancelled records by stating the phase was never run
- In: what a *no* is written against, so this is not re-asked. T-172's docstring and the binding both
  carry the reason today, which may already be enough
- Out: any change to `check_abandoned_slots`' current behaviour. It is verified and closed; a widening
  is this task's product, not a repair of that one
- Out: the general question of optional keys or merge-on-upgrade. That is the mechanism
  `defaults/config.md` already considered and rejected, and reopening it is a much larger task than
  this one

**Inputs**
- [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md) §3 — the three unknowns,
  measured, and the 0-in-172 figure
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Adding a key to this file is a breaking change*
- `plugin/skills/taskmd/taskmd/schema.py` — `CONFIG_KEYS`, and the comment above it saying what adding
  a name to it costs
- The adopter count, in `control/LOCAL-CONTEXT.md`, which is what turns "breaking" into a number

**Acceptance criteria**
- To be written at `specify` with the owner. Not drafted here, for the reason T-172 recorded: criteria
  written by the finder are criteria the answer passes by construction.

**Open questions**
- **Is the target class empty enough to close this unanswered?** 0 occurrences in 172 tasks is the
  strongest argument against spending anything, and it is also exactly the kind of measurement that
  says more about this project's habits than about the tool. The owner decides whether a class nobody
  here has produced is a class worth building for.

## 2. Plan

Not run — the task is at `proposed`.

## 3. Implement

Not run — the task is at `proposed`.

## 4. Review

Not run — the task is at `proposed`.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → proposed | Raised from [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md)'s `review`, carrying the unmet half of its first criterion so the gap is a task with an owner rather than a caveat in a closed record. Filed as a `decision` because the work is not blocked on anyone's skill — it is blocked on whether the capability is worth a breaking change to three adopters for a shape that occurs 0 times in 172 tasks. Deliberately **not** a child of T-172: it does not belong to that task, it is the question T-172 was told to stop at. `low` for the same reason the parent was, and because a recorded *no* is a legitimate and cheap outcome. |
