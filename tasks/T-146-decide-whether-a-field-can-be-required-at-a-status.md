---
id: T-146
title: Decide whether a field can be required at a status
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-065, T-089, T-100, T-106]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-146 — Decide whether a field can be required at a status

## 1. Specify

**Outcome**
It is settled whether taskmd can express *this field matters once a task reaches this point*, or
whether it cannot and says so — so a project whose convention is exactly that stops finding out by
hand which tasks broke it.

**Why this one**
Raised from the htmldeck adopter report, row `O-T6`. Three instances there, and they are not the same
shape, which is the reason the row was written as one observation rather than two:

1. A field the project requires at close. Their convention sets `shipped_in` when a task closes.
   `check` validates the *value* of a declared field and nothing ties a field's presence to a status.
   113 of 138 files carried it; three closed tasks did not, found by hand.
2. A field required from a phase onward — the same shape one step earlier.
3. **Two fields that must agree.** `status` and `phase` move together, and two sessions in that
   project chose differently on the same day: one wrote `status: specified, phase: specify`, the other
   `status: specified, phase: plan`. `check` passes both. Neither is obviously wrong, because *the
   phase just completed* and *the phase to do next* are both readable from a table that pairs them.

**The report's cross-reference is wrong, and it matters.** It names *your `T-063`* as the adjacent
case already filed — an open task at `specified` or later declaring no deliverable.
[T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) is the tier-1 budget measurement and has
nothing to do with this. Nothing in this backlog covers a field bound to a status; the nearest are
[T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md), which moved in the
opposite direction, and [T-039](T-039-let-a-plan-name-a-deliverable-that-does-not-exist-yet.md). So
the general form is unraised here.

**The third instance is live in this repository too, and unenforced.** `METHOD.md` §2 says *phase says
where the work has got to* and pairs nothing to a status. The shipped template starts a task at
`status: proposed, phase: specify`, which reads as the phase the work is *at*. Every one of this
repository's 143 files happens to follow that reading — 131 `done`/`review`, 5 `proposed`/`specify`, 2
`specified`/`specify`, 1 `in_progress`/`implement` — and nothing in the tool would have noticed if one
had not. The consistency is a habit, not a property.

**Why the answer may well be no, and why that is still the outcome.**
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) established that the shipped config
cannot gain a key without breaking every project that has written its own, and a rule of this kind is
project vocabulary by construction: `shipped_in` is a field taskmd does not name and never interprets
([T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md)). So the general form needs
somewhere to be declared, and the one obvious place is closed. A decision that this is out of scope,
written down with that reasoning, is a real result and is what two projects hitting it are owed.

**Requirements served**
R-11 (which fields exist is configuration) and R-15, in the sense the non-goal 11 carve-out was
amended on. R-16, for whether a rule of this kind can be believed.

**Scope**
- In: whether taskmd can express a constraint that binds a field to a status or a phase, and where such
  a rule would be declared given T-106.
- In: whether *presence at a status* and *two fields agreeing* are one mechanism or two. The report
  argues the second is what makes the general form worth having, since a required-field rule cannot
  express it.
- In: whether `METHOD.md` §2 should say which phase pairs with which status, independent of any
  checking. It is a method question, and the two readings the report found are both defensible under
  the current wording.
- Out: building any check before the shape is decided.
- Out: `deliverables` in particular, and any other single field. This is the class.
- Out: reversing T-106.

**Inputs**
- The adopter report, row `O-T6`, for the three instances and their counts.
- [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) — the constraint that governs the
  answer.
- [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) — carried, never interpreted.
- `plugin/skills/taskmd/docs/METHOD.md` §2, and `tasks/_task-template.md`, for what this project's own
  pairing currently is and where it is stated.

**Acceptance criteria**
- [ ] The decision covers both shapes — a field required at a status, and two fields that must agree —
      and says whether one mechanism serves both or the second is out
- [ ] Wherever it lands, the reasoning names T-106 and says what the rule would be declared in
- [ ] If the answer is no, one document says so and says what a project relying on such a convention
      does instead, and `check`'s scope statement does not imply it is covered
- [ ] The `status` and `phase` pairing this project uses is either stated in `METHOD.md` or
      deliberately left unstated, and which was chosen is recorded
- [ ] Whatever is decided is measured against this repository's own 143 files, in both directions —
      a rule that reports nothing here is as informative as one that reports something

**Open questions**
- ~~**Is the status–phase pairing a method question or a schema question?**~~ **Answered by the
  project owner on 2026-08-15: a method question — `METHOD.md` states which phase pairs with which
  status.** Two projects have now read §2 differently, and the pairing is a property of the lifecycle
  the method already mandates rather than of any project's vocabulary. Stating it makes the pair
  checkable for everyone following the method, at the cost of one sentence.

  *Rejected: leave the pairing to each project.* It is what §2 does today — *phase and status are
  independent* and nothing more — and it keeps the method free of an opinion it cannot enforce, which
  is a shape this project has rejected before. What decided it against: the two readings are both
  defensible under the current wording, so silence is not neutrality, it is a coin toss written into
  every adopting backlog. A method whose lifecycle is mandatory (§1.2) already owns this.

  **This does not answer the task.** Whether anything *checks* the pair, and whether the general form
  — a field required at a status — can be expressed at all under T-106, are still `specify`'s.

- **Does stating the pairing make the general form unnecessary?** If the method fixes the pairing,
  the third instance becomes checkable without any project-declared rule, which removes the strongest
  argument for the general mechanism and leaves the two weaker ones. Decide at `specify`; it may
  narrow this task to the method sentence alone.

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
| 2026-08-15 | (no change) | **The status–phase pairing is the method's to state**, decided by the project owner on 2026-08-15. Recorded here rather than carried in a reply, because it changes what this task's fourth acceptance criterion can say. It authorises no phase. It also raised a second question the answer creates and the first one could not: if the method fixes the pairing, the instance that argued hardest for a general mechanism no longer needs one, so this task may narrow to a sentence in `METHOD.md`. That is in §1 and is `specify`'s. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T6`. The row's cross-reference to *your T-063* is wrong and is corrected in §1: T-063 is the tier-1 budget measurement, and nothing in this backlog covers a field bound to a status. Two projects have now hit the class, which is the argument for deciding it rather than leaving it to each backlog. `medium` because both projects have a hand sweep that works and neither is blocked. `m` because the answer is probably constrained to nothing by T-106 and saying so properly is most of the work. The third instance is live here too: `METHOD.md` §2 pairs no phase to any status, and this repository's 143 files are consistent by habit rather than by anything the tool would report. |
