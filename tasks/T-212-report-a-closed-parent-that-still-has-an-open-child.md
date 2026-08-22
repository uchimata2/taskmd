---
id: T-212
title: Report a closed parent that still has an open child
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-209, T-191, T-198]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-212 — Report a closed parent that still has an open child

## 1. Specify

**Outcome**
`check` reports a task that has closed while one of its children is still open — the state
[`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 5 forbids, and the one nothing
currently notices.

**Why this one**
Found while working
[T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md), by asking that
task's own fourth criterion — *whether `check` reports it too* — and then running the case rather
than reasoning about it. T-209 answered **no** for the open parent, because an open umbrella with an
open child is the ordinary condition of every audit mid-flight and reporting it would make a healthy
backlog noisy. **The closed parent is the opposite**, and it is not covered:

```text
$ taskmd check --root <a project holding T-001 done, with child T-002 proposed>
OK - 2 task(s), 10 field value(s), 11 front-matter value(s), 1 reference(s), ...
```

The rule is written, the edge is stored, the derivation exists — and nothing reads it, which is the
class [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) and T-209 both
belong to. It is a *validator* concern rather than a `context` one: `context` answers about one task
somebody is already looking at, and this state is one nobody is looking at by definition, because
the parent is closed and off every open view.

**It is not the same defect as T-209 and must not be folded into it.** T-209 changed what a derived
line *says* about a task somebody opened. This asks the validator to report a contradiction between
two records, which is a new class, a fixture and a row in the coverage tables — a different size and
a different set of things to get right.

**Scope**
- In: a `check` class for a closed task with at least one open child
- In: the case that must not fire — a closed parent whose children are all closed, and an **open**
  parent with an open child, which is the ordinary state T-209 decided is not a defect
- In: the class's row wherever the shipped coverage tables enumerate classes, including each
  binding's *cannot occur* statement
- Out: `context`'s closing line, which [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) settled
- Out: a dependency whose blocker is still open on a closed task — a different edge kind and its own
  question, if it is one

**Inputs**
- [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) §3 — the
  `check` decision, its reason, and the run above
- `plugin/skills/taskmd/docs/method/audit.md` step 5 — the rule
- `tests/fixtures/` — the `broken-*` convention, one defect per fixture, and
  `tests/test_quiet_cases.py` for how a fixture's quiet cases now declare themselves

**Acceptance criteria**
- [ ] The class is shown **failing first**, on a committed fixture holding exactly one such defect
- [ ] It is shown **not** to fire on a closed parent whose children are all closed, and not on an
      open parent with an open child — both quiet cases marked in the fixture so
      `tests/test_quiet_cases.py` reads them
- [ ] The class appears wherever the shipped documents enumerate classes, derived rather than
      hand-listed where a derivation exists — `tests/classes.py` is the one home for the set
- [ ] Each shipped binding's *cannot occur* statement is judged against the new class, since
      `BINDING.md` §4 requires every binding to name what its backend makes impossible
- [ ] `check` is clean on this repository afterwards, or the tasks it names are real

**Open questions**
- **None.** The scope is the residual T-209 named while answering its own criterion.

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
| 2026-08-22 | → proposed | Raised from [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) while answering that task's fourth criterion — *whether `check` reports it too* — by building the case and running it rather than reasoning about it. The answer for the **open** parent is no: an umbrella with an open child is the ordinary state of every audit mid-flight, and reporting it would make a healthy backlog noisy. The **closed** parent is the opposite and returns `OK`, quoted in §1. Raised rather than folded into T-209 because it is a new validator class with a fixture and coverage rows, not a change to what a derived line says — a different size and a different set of things to get right. `medium` and `s`: the rule, the edge and the derivation all exist, so this is a reader for data already there. |
