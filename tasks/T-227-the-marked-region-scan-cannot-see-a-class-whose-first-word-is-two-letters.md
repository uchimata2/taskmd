---
id: T-227
title: The marked-region scan cannot see a class whose first word is two letters
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-222, T-192, T-197]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - tests/test_publishing.py
---

# T-227 — The marked-region scan cannot see a class whose first word is two letters

## 1. Specify

**Outcome**
The check that holds each binding's *cannot occur* declaration against the validator's class set
reads every class name the declaration carries, not most of them.

**Why this one**
The scan's pattern requires a backticked run of **three or more** capitals, so a class name whose
first word is shorter escapes it entirely — neither passing nor failing. Measured 2026-08-22, on the
shipped bindings:

```text
github-issues.md  region names four classes, the scan reads three
                  DUPLICATE ID, PARKED TASK, STALE INDEX read; ID WIDTH invisible
local-markdown.md region names four classes, the scan reads four
```

**The check is a guard against a stale name, and here it is silently not guarding one.** If the
invisible name were misspelled, or renamed in the validator, nothing would report it — which is the
exact failure the marked region exists to prevent. It is not a wrong answer, it is no answer, and no
answer looks like a pass.

**Scope**
- In: the pattern in `tests/test_publishing.py`, and whatever it must become to read a two-letter
  first word without swallowing ordinary prose
- In: a case that **fails before the repair** — a declaration naming a class the validator does not
  report, whose first word is two letters. A clean run proves nothing here
- In: whether the same floor appears anywhere else a class name is matched
- Out: the class names themselves, and the validator
- Out: the declarations. Both shipped bindings are correct today; this is about what would be caught
  if one stopped being

**Inputs**
- `tests/test_publishing.py` — `EveryBindingDeclaresWhatCannotOccur`, and the pattern it uses
- `tests/classes.py` — the derived class set the names are held against
- `plugin/skills/taskmd/docs/BINDING.md` §4 *What that check reads*, which states the floor and its
  consequence as of 2026-08-22 and will need re-reading if the floor moves

**Acceptance criteria**
- [ ] Every class name a shipped binding's region carries is read by the scan, shown by a count that
      matches the names in the region
- [ ] A deliberately wrong two-letter-first-word class name in a region **fails** the check, shown by
      running it before the repair and after
- [ ] Widening the pattern is shown not to start reporting ordinary backticked prose — the failure
      mode a looser pattern trades into
- [ ] `BINDING.md` §4's paragraph about what the scan misses is corrected or removed, and which is
      stated

**Open questions**
- **None.** The direction is fixed by the measurement.

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
| 2026-08-22 | → proposed | Found by [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) while establishing what the scan reads, so the clause could say it. **Nobody was looking for this** — the question was what a writer may safely backtick, and the answer arrived with a second half about what a writer may backtick and have ignored. Raised rather than absorbed: T-222 puts changing the marked-region check out of scope by name, and a shipped clause was repaired on the strength of the measurement, so the finding needs its own record whatever is done about it. `xs` because the pattern is one line; the criteria are what make it more than a one-line edit, since a loosened pattern that starts matching prose would be a worse failure than the one it fixes. |
