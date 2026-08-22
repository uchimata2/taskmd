---
id: T-227
title: The marked-region scan cannot see a class whose first word is two letters
type: fix
status: done
phase: review
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
| 1 | **Record the vacuous pass before repairing it.** Put a class the validator does not report into a shipped region, with a two-letter first word, and run the check. Then do the same with a three-letter first word, as the control that proves the check is alive at all | the pair of runs, before any edit |
| 2 | Measure which classes the pattern misses **against the whole derived set**, not against what the two shipped bindings happen to name | the list of invisible classes |
| 3 | Widen the pattern by the narrowest arm that covers them, and measure what it newly matches across every shipped document — the cost side of the trade | the pattern, and what it newly catches |
| 4 | Re-run step 1's case. It must now fail | the run after the repair |
| 5 | Add the guard the absence of which made this silent: count from the other side, so a future narrowing fails rather than going quiet | the new test, shown failing on the old pattern |
| 6 | Look for the same floor anywhere else a class name is matched, and act on what is found | what was found, and what was done |
| 7 | Correct `BINDING.md` §4's paragraph about what the scan misses | the corrected paragraph |

**Step 1 is first because a repair destroys its own evidence.** A test that passed for the wrong
reason leaves no trace once the reason is fixed, and *the check now fails on a bad name* is not the
finding — *it passed on one, and here is the run* is. The control in the same step is what stops that
pair proving nothing: without it, a failure after the repair could be a test that had never worked.

**Step 2 exists because the first measurement was taken from the wrong population.** The defect was
found while reading what the two shipped bindings declare, which is a sample and not the set. Whether
the pattern misses one class or six is a question about the validator, and the derived set is where
it is answered.

**Step 5 is the task's real product.** Widening a regular expression is one line; the reason this
survived is that nothing anywhere compared *what a region offers* with *what the scan reads*, so the
narrower the pattern got the quieter the check became. A repair without that guard leaves the next
narrowing exactly as silent as this one.

## 3. Implement

### Step 1 — the vacuous pass, recorded before it was repaired

`github-issues.md`'s region, edited in the working tree and restored after each run, 2026-08-22:

```text
`ID WIDTH`   -> `ID WIDTHS`    (not a class the validator reports)
  pytest -k class_named   ->  1 passed        <- the vacuous pass

`PARKED TASK` -> `PARKED TASKS` (control: same defect, three-letter first word)
  pytest -k class_named   ->  AssertionError: ... names `PARKED TASKS`
```

So the check is alive and it was blind, and the pair says which. Without the control, the failure in
step 4 could not be told apart from a test that had never worked.

### Step 2 — the population the first measurement missed

Against the derived set rather than against the two shipped declarations, **two** classes were
invisible, not one: `ID WIDTH` **and** `NO BLOCKER`. The figure written into
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) and into
`BINDING.md` on the same day said *exactly one class*, because it was counted from what
`github-issues.md` declares. Both are corrected, and T-222's record is annotated rather than
rewritten.

### Steps 3 and 4 — the pattern, and the case that now fails

```text
was:  `([A-Z]{3,}(?: [A-Z]+)*)`
now:  `([A-Z]{2,}(?: [A-Z]{2,})+|[A-Z]{3,})`

every class in the derived set matched:            22 of 22   (was 20 of 22)
newly matched across all 13 shipped documents:     ID WIDTH   (and nothing else)
`ID WIDTHS` in a region, re-run:                   AssertionError ... names `ID WIDTHS`
```

**A single two-letter word still does not match**, which is what makes the widening free. The floor
moves only where a second word confirms the shape.

### Step 5 — the guard on the guard

`test_the_pattern_reads_every_name_a_region_carries` counts from the other side: anything a region
backticks that is capitals and spaces throughout is a name the region is **offering**, and the
pattern must read all of them. Shown failing on the old pattern before the repair was kept, so it is
known to be capable of failing rather than assumed to be.

### Step 6 — the same floor, in a second place

The expression was written out **twice** in the same file — the *cannot occur* region check and the
`advisories` kind in `KINDS` — and both copies carried the defect. It does not bite in the second
place today, because every value in `ADVISORY_PREFIXES` has a first word of three or more; it would
bite the day one does not. Both now read one constant, `CLASS_IN_BACKTICKS`, so the next repair
cannot land in one copy. **The recorded reason for the old floor survives the widening and was
checked rather than assumed**: the advisory region contains `` `OK` ``, a floor of two would read it
as a fourth advisory, and a single two-letter word does not match the new pattern either.

**Decisions & assumptions**
- **Give the pattern one home rather than widening it twice** — 2026-08-22. The second copy is inside
  this task's own deliverable and §1 scopes finding it in; two copies of an expression that already
  carried one defect in both is the project's own rule arriving in the file that enforces it.
- **The narrowest arm that covers the miss** — 2026-08-22. `[A-Z]{2,}` on its own would match `OK`,
  `ID` and `AND` inside a region and would break the advisories kind for a reason already recorded
  there. Requiring a second word of two or more keeps every existing exclusion.
- **Correct the *exactly one class* figure in two places and annotate the third** — 2026-08-22.
  `BINDING.md` and this record state the present, so they are corrected;
  [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) is closed
  and records what was measured that day, so it is annotated (METHOD §1 rule 5).
- **A destructive shell command lost the deliverable mid-run and it was restored from a copy taken
  minutes earlier** — 2026-08-22. `git checkout --` was used to revert a deliberately-broken pattern
  and reverted every edit to the file. Recorded because the recovery was luck rather than method:
  the evidence step 4 needed had already been captured, and the file had been copied aside first for
  an unrelated reason.

**Outputs produced**
- `tests/test_publishing.py` — `CLASS_IN_BACKTICKS` as one home for the expression, the widened
  pattern, and `test_the_pattern_reads_every_name_a_region_carries`
- `plugin/skills/taskmd/docs/BINDING.md` §4 — the paragraph about what the scan reads, corrected

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every class name a shipped binding's region carries is read by the scan, shown by a count that matches | met | And held by a test rather than by a measurement, which is step 5. `github-issues.md`'s four names are four read; the old pattern read three |
| A deliberately wrong two-letter-first-word class name **fails**, shown before and after | met | `ID WIDTHS` passed before the repair and fails after, with a three-letter control failing in both — the pair is in §3 step 1 |
| Widening is shown not to start reporting ordinary backticked prose | met | Across all 13 shipped documents the wider arm newly matches exactly one token, and it is a real class name. The one recorded exclusion the old floor existed for — `` `OK` `` in the advisory region — still does not match |
| `BINDING.md` §4's paragraph is corrected or removed, and which is stated | met | Corrected, not removed: the limit is gone and the paragraph now says so, along with what was true until 2026-08-22. **It also carried a wrong figure** — *exactly one class*, counted from the two shipped declarations instead of from the class set — and that is corrected here and annotated in [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md), where it was first written |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | proposed → done | `specify` through `review` in one session. **Authorisation:** the **project owner**, on **2026-08-22**, extended the same day's four-task full-lifecycle grant to cover a task **raised during** that work. This record is one of six so raised; it is worked because it carries no open question of theirs, and four of the six stop where they stand because they do. **The extension authorises phases, not answers**, exactly as the grant it extends. **The vacuous pass is recorded before the repair**, with a control beside it, because a test that passed for the wrong reason leaves no trace once the reason is gone. **The first measurement was taken from the wrong population and this task found that too**: counted against the derived class set rather than against the two shipped declarations, **two** classes were invisible and not one, so the figure written into `BINDING.md` and into [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) hours earlier was wrong. Corrected where it states the present, annotated where it records the past. **The pattern had two homes and both carried the defect**, so the repair gave it one — the project's own rule arriving in the file that enforces it. **The product is the guard, not the regular expression**: nothing compared what a region offers against what the scan reads, so every narrowing of that pattern was silent by construction, and a test now counts from the other side. |
| 2026-08-22 | → proposed | Found by [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) while establishing what the scan reads, so the clause could say it. **Nobody was looking for this** — the question was what a writer may safely backtick, and the answer arrived with a second half about what a writer may backtick and have ignored. Raised rather than absorbed: T-222 puts changing the marked-region check out of scope by name, and a shipped clause was repaired on the strength of the measurement, so the finding needs its own record whatever is done about it. `xs` because the pattern is one line; the criteria are what make it more than a one-line edit, since a loosened pattern that starts matching prose would be a worse failure than the one it fixes. |
