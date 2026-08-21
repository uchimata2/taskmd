---
id: T-200
title: Discount the ids a task file carries even when it was not loaded
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-121, T-197, T-062]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-21
adopter_visible: yes
deliverables: []
---

# T-200 — Discount the ids a task file carries even when it was not loaded

## 1. Specify

**Outcome**
`check_duplicate_index` stops reporting a task file for naming its own id, in the case where that
file was excluded from `tasks` by a different check — so `DUPLICATE INDEX` no longer fires on the
`broken-duplicate-id` fixture, and the exception recorded against it in `tests/test_cli.py` is
deleted.

**Why this one**
Found on 2026-08-21 while [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)
derived the harness's class list and the owner ruled the advisory classes into the cross-fixture
silence assertion. The first run with advisories included failed immediately:

```text
AssertionError: 'DUPLICATE INDEX' unexpectedly found in
  DUPLICATE ID  T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md ...
  DUPLICATE INDEX  tasks/T-001-second.md: a second table of 1 known task ids sits outside
  the taskmd markers
```

**The mechanism, which is the part worth stating.** `check_duplicate_index` discounts *structural*
ids — the ones a task file is entitled to carry, being its own and those in its own edge fields —
and it builds that discount from `tasks`. A file that lost the duplicate-id race is **not in
`tasks`**: `T-001-second.md` declares `T-001` and is not loaded, so it gets no entitlement and is
judged as an arbitrary document that happens to name every known id. With one loaded task, a
majority of the known set is one, so a single mention of its own id fires the rule.

**It is the small-N case the check already knew about, arriving by a door it did not.** The
docstring for that check records exactly this shape — *it is arithmetic at three* — and closes it by
discounting structural ids. The discount is right; its **input** is a set that a different check has
already pruned. Three checks prune it that way: duplicate id, id width and parked task
([T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) is why the
first of those is visible at all).

**Requirements served**
R-16 (`docs/SCOPE.md`).

**Scope**
- In: what `check_duplicate_index` treats as a task file's own entitlement
- In: the same question for the other two prunings — id width and parked task — since the cause is
  shared and fixing one shape and not the others leaves the finding half-closed
- In: deleting the `also=[("DUPLICATE INDEX", "T-200")]` exception in `tests/test_cli.py`, which is
  written to fail once this is fixed
- Out: the majority threshold itself, which is
  [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md)'s and was decided
  with its reasons
- Out: whether an unloaded file should be excluded from the scan entirely — a different and larger
  question, and a rule that stops reading a file because another check complained about it is how a
  second defect hides behind a first

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_duplicate_index`, and the `structural` map
- `tests/fixtures/broken-duplicate-id/` — the fixture that shows it, with no edit needed
- [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) — the threshold and
  the discount, and why each is what it is

**Acceptance criteria**
- [ ] `check` on `tests/fixtures/broken-duplicate-id` reports `DUPLICATE ID` and not
      `DUPLICATE INDEX`, and the run is quoted
- [ ] The same is answered for a file pruned by id width and by a parked-task folder — each either
      shown not to have the problem, or fixed with it
- [ ] **The check is still shown to fire on a real duplicate table**, so the repair narrows the rule
      rather than switching it off — broken on purpose, with the output quoted
- [ ] The `also=` exception is deleted from `tests/test_cli.py` and the suite passes without it

**Open questions**
- none

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
| 2026-08-21 | → proposed | Found by [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) on the first run after the owner ruled advisories into the cross-fixture silence assertion — which is the answer paying for itself the day it was given. `medium` and `s`: it is a false positive on an advisory, so it moves no exit status, but a noisy advisory trains a reader to skim the failing lines beside it, which is [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s argument. Not fixed where it was found (METHOD §5). |
