---
id: T-198
title: Show each quiet fixture is within its own check's reach
type: audit
status: proposed
phase: specify
parent: T-191
blocked_by: []
related: [T-150, T-151]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-198 — Show each quiet fixture is within its own check's reach

## 1. Specify

**Outcome**
For every fixture a test asserts a class is silent about, a statement of whether **that fixture** is
within **that check's** reach — shown by mutating the fixture so it ought to trip, and quoting what
arrived. Each fixture that cannot be made to trip becomes its own child task.

**Why this one**
Finding **F-2** of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md).
That audit proved every class **can** speak, by planting each one's defect in a tree where a test
asserts silence. It did not prove that each **particular quiet fixture** is somewhere the check can
see — and those are different claims.

**They came apart once already, which is why this is worth doing rather than assuming.**
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) found a `WIDE ROW`
negative fixture that could not fire at all: the check consumed the line under the header as a
delimiter, so the fixture sat outside its reach while the class itself worked perfectly elsewhere. A
class-level exercise — which is exactly what T-191 ran — cannot see that, and would have passed
`WIDE ROW` on the day T-150 was raised.

**Why T-191 did not simply do this.** Its criteria are written per class (*each has a quiet case*,
*each can fire*), and it met them. Widening to per fixture is more work than those criteria ask for,
so the audit recorded the distinction as a finding rather than quietly doing extra and leaving the
next reader unable to tell which claim had been tested. That is the same rule
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) states, applied to the
audit itself.

**Scope**
- In: every fixture named by a must-not-catch assertion, and the trees the bespoke quiet tests build
  inline. The set is read from the tests, not from a list in a document
- In: for each, whether mutating it trips the class it is asserted silent about
- Out: **repairing any fixture found out of reach.** A finding is never fixed where it is found
  (METHOD §5); each is a child task
- Out: re-deriving the class set, which is
  [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md)'s and is recorded
  there
- Out: the cross-fixture `LABELS` list, which is
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)'s

**Inputs**
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) §3 — the class table,
  and which quiet case belongs to which class
- [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) — the worked instance
  of a fixture out of reach
- `tests/fixtures/` and `tests/test_cli.py`

**Acceptance criteria**
- [ ] The fixture set is derived from the tests and the derivation is shown, so a quiet case added
      since cannot be missing
- [ ] Every fixture has a row; the rows sum to the derived set
- [ ] Each *is in reach* claim quotes the alarm that arrived when the fixture was mutated; a fixture
      not mutated is recorded as unproven rather than as passing
- [ ] **The instrument is shown able to produce a positive result before any negative one is
      believed** — T-191's own first run reported every class silent because it never invoked
      `check`, and that is the failure mode this task is most exposed to
- [ ] Every fixture out of reach is a child task, and this audit closes only when each resolves

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
| 2026-08-21 | → proposed | Raised as finding F-2 of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md). Typed `audit` rather than `fix` because it examines a body of fixtures for a problem nobody has alleged of any particular one, and its findings become children (METHOD §5). `m`: the condition means mutating each fixture, not reading it. A child of T-191, which does not close until this resolves (`audit.md` step 5). |
