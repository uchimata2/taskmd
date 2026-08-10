---
id: T-106
title: Say that the shipped config cannot gain a key without breaking every project that wrote one
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-001, T-011, T-023, T-100]
work_package: v0.3
owner: maintainer
business_value: high
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-106 — Say that the shipped config cannot gain a key without breaking every project that wrote one

## 1. Specify

**Outcome**
The constraint that governs every future schema change is written down in one place, so the next
person proposing a config key meets it before designing around it rather than after.

**Why this one**
Found while planning [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md),
whose §1 asked whether a project could switch the new advisory off with a config key. It cannot, and
the reason is not local to that task:

- A config **replaces** the shipped default rather than merging with it.
- Therefore every key is **required to be written**, and `schema._require` raises on a missing one —
  deliberately, because a silently absent key would hand a project a schema nobody wrote.
- Therefore **adding a key to the shipped default invalidates every existing project's config the
  moment they upgrade**, with an error naming a key they have never heard of.

Each of those three is written down. **Their conjunction is not**, and it is the one that constrains
design. T-100 met it as a surprise mid-plan; the next task to propose a key will meet it the same
way unless it is stated.

**It is not a defect to fix.** Every step in the chain is a decision this project made on purpose and
would make again. What is missing is the sentence saying what they cost together.

**Requirements served**
R-11 (`docs/SCOPE.md`) — the schema is configuration, and this is the price of the rule that makes it
so. R-17, in that the failure mode is a config error appearing at the worst possible moment: on
upgrade, in a project that changed nothing.

**Scope**
- In: one paragraph, in the shipped config beside the replace-not-merge rule it follows from.
- In: whether anything can be done for a project caught by it — a named upgrade path, or the plain
  statement that a new key means every config is edited.
- Out: changing `_require`. Making a key optional is exactly what it exists to forbid, and
  [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) D2 rejected the
  carve-out already.
- Out: adding any key. This says what it would cost, not that one is wanted.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Format*, and the new *When this file moves ahead
  of yours*.
- `plugin/skills/taskmd/taskmd/schema.py` — `_require`, `CONFIG_KEYS`.
- [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) **D2**, where
  the chain was first written out.

**Acceptance criteria**
- [ ] The three rules and their consequence are stated together, once
- [ ] It says what a project that hits it should do, rather than only that it will
- [ ] It is placed where someone *proposing a key* will read it, not only where someone debugging the
      error will
- [ ] `check` is clean on this repository

**Open questions**
- **Does the answer include a migration route?** *Recommended: no — state the cost and stop.* A
  route means either optional keys or a version marker in every config, and both are larger than the
  problem, which has arisen zero times in a shipped schema. *Alternative: a documented one-line
  upgrade* — cheap to write and reassuring, and it commits this project to keeping it true through a
  change it has never made.

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
| 2026-08-10 | → proposed | Raised from [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md)'s plan under METHOD §3.3, and deliberately not fixed there: T-100 needed the answer to shape one decision, and the constraint governs every future one. `high` because it is a trap with no warning sign — the three rules that produce it are each documented and each individually right, and only their conjunction bites; `xs` because the whole work is a paragraph in a file that already carries the rules it follows from. Not a defect: nothing here would be decided differently, and what is missing is the sentence naming the cost. |
