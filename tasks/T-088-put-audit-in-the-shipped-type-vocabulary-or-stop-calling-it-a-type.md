---
id: T-088
title: Put audit in the shipped type vocabulary, or stop calling it a type
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-001, T-026, T-032]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-088 — Put audit in the shipped type vocabulary, or stop calling it a type

## 1. Specify

**Outcome**
The method and the shipped schema agree about what an audit is, so a project that follows METHOD §5
literally does not fail `check`.

**Why this one**
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5 opens: *"An audit is a **task type**, not a
phase."* The shipped schema's `type` vocabulary is `analysis, decision, deliverable, research, fix,
admin`. There is no `audit` in it, so writing the thing the method names produces:

```
VOCABULARY    T-NNN.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
```

**Two projects have now hit this, and neither noticed on its own.** This repository types its audit
umbrellas `analysis` (T-026, T-059) and never remarked on it. The first adopting project
(`control/LOCAL-CONTEXT.md`) carried two tasks typed `audit` for five days: its own standard had no
such value either, and nothing said so until taskmd's validator read them on 2026-08-09. A rule that
two independent projects work around by inventing the same substitute is a rule whose vocabulary is
wrong, not two projects making the same mistake.

**Requirements served**
R-5 (`docs/SCOPE.md`) — audit is a task type and findings become child tasks. R-11, since the answer
is a schema question rather than a code one.

**Scope**
- In: the `type` row of `plugin/skills/taskmd/taskmd/defaults/config.md`, or METHOD §5's wording.
- In: whether `decision` and `audit` are the same kind of addition, since `decision` is in the
  shipped list and is not named by the method at all.
- Out: any behaviour. Nothing branches on `type` today; it is vocabulary and display.
- Out: the audit *procedure*, which is `docs/method/audit.md` and is not at issue.

**Inputs**
- METHOD §5 and [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md).
- The `type` row in `plugin/skills/taskmd/taskmd/defaults/config.md`.
- T-026 and T-059 in this repository, both audit umbrellas typed `analysis`.

**Acceptance criteria**
- [ ] A task following METHOD §5 word for word passes `check` on a project with no config, shown by
      creating one in a fixture rather than by reading the vocabulary
- [ ] Whichever way it is settled, the method and the schema say the same thing afterwards, checked
      by reading both
- [ ] The existing umbrellas in this repository are either retyped or explicitly left, with the
      reason

**Open questions**
- **Which of the two moves.** Adding `audit` to the vocabulary makes the method literally true and
  costs one word, but it also adds a value that changes nothing the tool does. Rewording §5 to say
  an audit is a *kind of task* rather than a *task type* removes the collision and gives up a
  distinction the method leans on elsewhere. The maintainer's, because it is the method's wording.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `plugin/skills/taskmd/taskmd/defaults/config.md` or `plugin/skills/taskmd/docs/METHOD.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised the day the first project outside this repository adopted taskmd, whose validator immediately reported two of its tasks as having an invalid `type: audit`. The value is absent from the shipped vocabulary and present in the method's own sentence about what an audit is. This repository has been working around it since T-026 without noticing, which is the part that makes it worth a task rather than a note: the workaround was invisible because everyone reached for the same substitute. |
