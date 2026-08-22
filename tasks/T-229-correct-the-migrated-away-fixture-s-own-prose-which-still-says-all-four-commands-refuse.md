---
id: T-229
title: Correct the migrated-away fixture's own prose, which still says all four commands refuse
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-221, T-185, T-164, T-177]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - tests/fixtures/migrated-away/.taskmd/config.md
---

# T-229 — Correct the migrated-away fixture's own prose, which still says all four commands refuse

## 1. Specify

**Outcome**
`tests/fixtures/migrated-away/.taskmd/config.md` no longer tells a reader that all four commands
refuse on this fixture, because `check` does not, and this fixture is the project it is measured
against.

**Why this one**
The file says *"Refusing is right — all four read a folder, and there is no folder"*, written
2026-08-17 by [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md). On
2026-08-19 [T-185](T-185-run-the-document-checks-in-a-project-whose-tasks-moved.md) split `check` so
the checks that read documents run on exactly this shape, and the sentence was not revisited.
Measured 2026-08-22:

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md
1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), ...
exit 1
```

This is the same defect class as
[T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) in a second
document — a sentence about behaviour written once and never re-run — and it sits in the one file a
contributor opens to learn what the fixture is for.

**Scope**
- In: the two sentences under *The point of the fixture*, corrected against a run
- In: whether any other sentence in that file describes behaviour the 2026-08-19 split changed
- Out: the fixture's data. The config keys and the two documents are what they should be, and T-185
  proved it
- Out: the other fixtures' prose. If this class is wider than one file it is a sweep, and a sweep is
  its own task rather than a quiet widening of this one

**Inputs**
- `tests/fixtures/migrated-away/.taskmd/config.md` — the sentences, and the date they carry
- [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) §3 — the run
  that falsifies them, and the same defect corrected in the binding document

**Acceptance criteria**
- [ ] The corrected sentences are backed by a quoted command and its exit code, dated
- [ ] The fixture's stated purpose still distinguishes it from `broken-tasks-dir`, which is the
      distinction the file exists to hold
- [ ] Whether the 2026-08-17 date stays visible is decided and stated, not dropped by default

**Open questions**
- **None.** The direction of the correction is fixed by the run above.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-22 | (no change) | **Renumbered from T-223 on the day it was raised**, before it was pushed. A concurrent branch had already taken that id and merged it as pull request #2, so two files claimed `T-223` the moment the two lines met. The one that had been published keeps the id and this one moves — the ordering rule is which was reachable by anybody else, not which was written first. `check` reports the state as `DUPLICATE ID`, which is what would have caught it had the merge been pushed unread. Recorded because a record whose id changed is a record whose old id may still be written somewhere: [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) carried two references and both were rewritten in the same commit. |
| 2026-08-22 | → proposed | Raised from [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s step-4 sweep, which was reading the binding document and found the same defect in the fixture that document's evidence is measured against. **Raised rather than absorbed**: T-221 declares one deliverable and this is a second, so folding it in would have made that record false about what it changed. `medium` rather than `high` because it misleads a contributor rather than an adopter — no clone of the plugin receives `tests/`. **The sweep bound is deliberate**: this file was found by opening it, not by a sweep of the fixture tree, and a second instance would make the sweep the task instead of the fix. |
