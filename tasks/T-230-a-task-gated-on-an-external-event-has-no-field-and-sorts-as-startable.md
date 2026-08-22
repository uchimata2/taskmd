---
id: T-230
title: A task gated on an external event has no field, and sorts as startable
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-182, T-199, T-087]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-230 — A task gated on an external event has no field, and sorts as startable

## 1. Specify

**Outcome**
An answer, recorded, on whether a task held up by something that is **not another task** gets a way to
say so that the ordering rule can read — and if so, what it is.

**Why this one**
[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) cannot be started. It
waits on there being a release to make, which is nobody's to schedule. That fact lives in an *Open
questions* bullet, and no view can see prose, so `list --open --limit 1` will hand it to a session as
the next thing to work.

**Neither existing mechanism reaches it, and both were checked by running.** Measured 2026-08-22:

```text
blocked_by needs a task, and a release is not one. Nothing to point the edge at.

$ ./plugin/bin/taskmd check --root tests/fixtures/broken-missing-blocker
NO BLOCKER    T-001 is 'blocked' with nothing in blocked_by
1 problem(s) - ...
exit 1
```

So marking it `blocked` is a validator failure, and the edge has no target. The task has **no field**,
and the ordering rule sorts it on value then effort then id, exactly as if it were ready.

**This is the shape a commit already fixed once, in the only case where the fix was available.**
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s wait was a
sentence in a Log row until it was made a `blocked_by` edge, on the stated ground that *prose in a Log
row is invisible to every view*. That repair worked because the blocker was a task. Here it is an
event, so the same defect has no remedy and nobody has said so.

**Scope**
- In: whether this is worth a mechanism at all, and if so which. **A new shipped-config key is very
  nearly ruled out before this starts**: [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
  records that a config *replaces* the default rather than merging, so every key is required and adding
  one errors every existing adopter's config on upgrade. What is left is code-only or nothing —
  relaxing the *no blocker* rule so `blocked` is legal without an edge, teaching the ordering rule to
  read the status value, a convention with no tool support, or nothing
- In: the tension inside the second of those. `is_blocked` reads edges and **says why in its own
  docstring** — *"Not a status value — a task can be marked anything and still be held"*. Any
  answer that has the ordering rule read a status must overturn that sentence on the record, not
  around it
- In: whether the answer also covers *waiting on a person* — a reader nobody can summon, an owner
  question — which is the same shape and is currently carried by soft edges and prose
- Out: fixing T-182. It is the instance; if a mechanism arrives it can adopt it, and if none does then
  T-182 keeps a prose gate and that is the recorded answer
- Out: changing what `blocked_by` means. The derived flag reads edges deliberately, and `cli.py` says
  so in `is_blocked`'s own docstring

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `is_blocked`, `effective_values`, and
  `check_blocked_without_blocker`; the three places that decide what *held up* means today
- [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) *Open questions* —
  the instance, and the only one currently open
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) Log,
  2026-08-22 — the same defect where a remedy existed, and the argument for why prose does not do

**Acceptance criteria**
- [ ] The answer is recorded with its reason, and every candidate that was rejected is named with what
      it would have cost
- [ ] How many open tasks are in this state **today** is counted, not estimated — a mechanism for a
      class with one member is a different decision from one with eight
- [ ] If the answer is *nothing*, what a session should do when `list` hands it an unstartable task is
      stated somewhere a session reads
- [ ] Any shipped-schema change is checked against what it does to an adopter's existing config on
      upgrade

**Open questions**
- **Is this worth a mechanism, given the class may have one member?** — the project owner. The
  recommendation is to **count first and decide after**: the second criterion is deliberately ahead of
  the decision, because *ask whether the remedy's target class is empty* is the question this kind of
  proposal skips. If the count is one, *nothing, plus a stated convention* is likely right.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, after a survey of the open backlog put [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) last on a gate the tool cannot see while `list --open` put it first. **Both existing mechanisms were run rather than reasoned about**: `blocked_by` has no target when the blocker is an event, and `status: blocked` without an edge is `NO BLOCKER`, exit 1, shown on this project's own fixture. **A decision and not a fix**, by the schema's own test — the change is not known until the question is answered. **The candidate that looks obvious is nearly closed already**: [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) records that the shipped config cannot gain a key without erroring every adopter on upgrade, which was read here rather than remembered — the guessed title of that record was wrong and its real one is the sharper fact. **The second criterion is placed deliberately ahead of the decision**: a mechanism argued at size and applied to a class with one member is the failure this kind of proposal makes, so the count comes first. |
