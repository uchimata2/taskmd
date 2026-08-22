---
id: T-219
title: Let a quiet mark declare a value that begins with a capital
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-212, T-202, T-211]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-22
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-219 — Let a quiet mark declare a value that begins with a capital

## 1. Specify

**Outcome**
A quiet mark in `tests/fixtures/` can declare a value beginning with a capital letter — a task id,
most obviously — and either it parses, or the failure says the value was eaten rather than blaming
the class.

**Why this one**
Found on 2026-08-22 while working
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), by writing a mark for a class
whose values are task ids:

```text
<!-- quiet: CLOSED PARENT T-003 - closed, and its only child is closed too -->
```

`MARK_RE` in [`tests/test_quiet_cases.py`](../tests/test_quiet_cases.py) reads the class as
`(?P<cls>[A-Z][A-Z ]*[A-Z])`, which is greedy over capitals and spaces. It swallowed the `T` of
`T-003`, leaving the class as `CLOSED PARENT T` and the declared value as `-003`.

**It failed loudly, and that is the reason this is small rather than urgent.** Assertion 1 —
*every mark names a class `check` can print* — reported it on the next full run. But it reported
**the class** as unknown while printing a set that plainly contains `CLOSED PARENT`, so the message
sends a reader to look at the class name, which is correct, instead of at the value, which is not
parsed. T-212 worked around it by dropping the declared values; the mark syntax is still unable to
carry one.

**Scope**
- In: `MARK_RE`'s class group, and whatever the fix costs the values group beside it
- In: a fixture mark that declares a capital-initial value, so the repair is shown working rather
  than argued
- In: showing the current behaviour **failing first**
- Out: assertion 2's inability to bite on a class that writes ids bare — a different limit, stated
  in that module's docstring, and recorded in T-212 §3 decision 4
- Out: any change to what a mark *means* or to the three assertions

**Inputs**
- `tests/test_quiet_cases.py` — `MARK_RE`, and the docstring stating what a mark's `<values>` are for
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §3 decision 4 and §4 — where
  the finding was recorded
- `tests/fixtures/broken-closed-parent/` — the two marks that had to drop their values

**Acceptance criteria**
- [ ] The current behaviour is shown **failing first**, with the output quoted — a mark declaring a
      capital-initial value, and what the reading makes of it
- [ ] After the fix, a mark in a committed fixture declares a capital-initial value and the reading
      holds it, with `--list` quoted
- [ ] `test_a_declared_value_really_is_on_the_marked_line` still passes on that mark, so the value is
      parsed as itself and not as a fragment
- [ ] Every existing mark parses exactly as before — the reading's totals are quoted from before and
      after and compared
- [ ] The suite is green and the output is quoted

**Open questions**
- **None.** The behaviour is measured and the repair is a pattern; nothing here needs an answer from
  anyone.

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
| 2026-08-22 | → proposed | Raised from [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)'s review, which hit it while marking the two quiet cases of the `CLOSED PARENT` class and worked around it by dropping the declared values. `xs` and `medium`: one regular expression, but it silently narrows what every future mark can say, and the class of defect — a reader that cannot report its own incompleteness — is the one `tests/test_quiet_cases.py` exists to close. **Covered by the multi-phase grant**, per the row below. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — this task is covered by it, and it is covered *because of how it arose*.** The **project owner** extended the grant on **2026-08-22**, at the start of the session that resumed the eight, in these words: *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it covers:** this task — raised while working [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), one of the eight — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed. **What it does not cover:** it authorises **phases, not answers**. A task that reaches an open question belonging to the owner stops there, which is what *where my involvement is not needed* means; §1 records that this one has none. The grant reaches this record because the work that raised it was inside the eight — **not** because the backlog happens to contain no owner-facing alternative, and not by any description of what needs nobody. A task raised by a later session is outside it. The eight, and the three earlier steps that built the grant, are recorded in each of those records. |
