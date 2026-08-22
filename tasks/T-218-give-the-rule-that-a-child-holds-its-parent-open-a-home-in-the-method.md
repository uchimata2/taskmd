---
id: T-218
title: Give the rule that a child holds its parent open a home in the method
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-212, T-216, T-209]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-218 — Give the rule that a child holds its parent open a home in the method

## 1. Specify

**Outcome**
The rule *a child holds its parent open — a task may not close while one of its children is open*
has one durable home in the shipped method, so it survives the closure of the task records that
currently carry it.

**Why this one**
The **project owner** settled the rule on **2026-08-22**, answering a question raised by
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md): a child holds **every** parent
open, not only an audit umbrella. **Right now that ruling exists in exactly two places, and both are
task records** — T-212 §1 and
[T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) §1.

**Both of those will close, and a premise inside a closed record expires in silence.** Views read
open work, so the day T-212 closes the rule leaves every list a session consults. It does not go
stale — it goes invisible, which is worse, because nothing reports its absence.

**What the shipped documents say today is narrower than the rule.**

- [`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 5 reads *"Close the **umbrella**
  only when every child is resolved"* — an audit's umbrella, which is the reading T-212 had to put
  to the owner precisely because it does not cover an ordinary parent.
- [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4 defines the hierarchy edge — *"This task
  belongs to that one. The inverse is that task's children."* — and says nothing about closure.
- `cli.py`'s `holds_open()` states the rule in full and qualifies it to nothing, but it is code and
  the method is not derived from it.

So the method's own text has a gap that the tool and the owner have both already filled.

**Scope**
- In: deciding where the rule belongs — `METHOD.md` §4 beside the edge it constrains, or a phase
  file — and writing it there once
- In: deciding what happens to `audit.md` step 5, which becomes either an application of the general
  rule or a pointer to it. **It must not become a second copy**
- Out: the `check` class that reports the state, which is
  [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)
- Out: repairing this repository's three cases, which is
  [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md)
- Out: the **open** parent case. [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md)
  settled that an open parent with an open child is the ordinary state and is not reported; this
  task documents when a parent may *close*, which is the other side

**Inputs**
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1 — the question, the two
  readings, and the owner's answer with its date
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the edge definition, and the *store the forward edge*
  rule that governs where a fact may be written
- `plugin/skills/taskmd/docs/method/audit.md` step 5 — the narrower statement
- `plugin/skills/taskmd/taskmd/cli.py` — `holds_open()`, which already states it

**Acceptance criteria**
- [ ] The rule is stated **once** in the method, and the decision records where and why, with the
      rejected location and its reason
- [ ] `audit.md` step 5 is left as an application or a pointer, and a reader of either place can tell
      which is the source — no second copy of the rule
- [ ] The owner's ruling is cited where the rule now lives, with its date, so a later reader can find
      the argument without opening a closed task
- [ ] `check`, `index` and the suite are green, and the tier-1 budget test still passes

**Open questions**
- **None.** The rule is settled; where it lives is this task's work.

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
| 2026-08-22 | → proposed | Raised by the handoff's backward sweep, not by a task: the owner's ruling of 2026-08-22 was recorded in the two task records that needed it and in no shipped document, and both of those records are destined to close. `medium` and `s` — one rule, one home, one decision about `audit.md`, but the cost of losing it is that a rule the tool enforces has no written source. `adopter_visible` because the method ships. **Not covered by the multi-phase grant of 2026-08-22**, which names six tasks by id and was given before this was found. |
