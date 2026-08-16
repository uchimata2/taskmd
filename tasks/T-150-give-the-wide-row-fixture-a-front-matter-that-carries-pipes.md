---
id: T-150
title: Give the wide-row fixture a front matter that carries pipes
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-032, T-141, T-151]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-15
updated: 2026-08-16
deliverables: []
---

# T-150 — Give the wide-row fixture a front matter that carries pipes

## 1. Specify

**Outcome**
`WIDE ROW` staying silent on a front matter full of pipes is protected by the fixture rather than by
the accident that this repository's corpus happens to contain one.

**Why this one**
From the deck-building sibling's comment on `github.com/uchimata2/taskmd/issues/1`, 2026-08-14. Their
own scanner reported this project's shipped task template as the only defect in their tree, because
`effort: xs | s | m | l | xl` has five pipes and no table. It is one of three false positives they
hit, and the only one of the three ours could plausibly share.

**Ours does not fire, and that was measured rather than reasoned.** A specimen carrying all three of
their traps was run on 2026-08-15: a front matter with two pipe-carrying menus produced no alarm,
because a header line is only a header when the next line is a delimiter row, and no front-matter
line is. The evidence is in T-151 §1, which holds the whole specimen result.

**What is missing is the promise, not the behaviour.**
`tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md` is a genuinely strong
negative fixture — a blank excess cell, an escaped pipe, a short row, a fenced table, and a real
table after the fence, with the test asserting an exact count of three. Front matter carrying pipes
is the one class of theirs it does not hold. So the silence is currently proven by the corpus, and a
corpus is a weaker instrument than a fixture: it changes without anyone deciding to change it, and
the shipped template could stop using a `|`-separated menu for reasons that have nothing to do with
this check.

**Requirements served**
R-16 (`docs/SCOPE.md`) — read in the direction the reporter names: a check is unproven where it has
no case that must *not* fire.

**Scope**
- In: one section added to the existing negative fixture, or its front matter extended, whichever the
  fixture's own shape prefers.
- In: the count the test asserts, which has to stay exact for the negative to mean anything.
- Out: changing `check_wide_rows`. It behaves correctly; this is about what holds it there.
- Out: the other two traps. Neither can arise here, and the reasoning is in T-151 §1.
- Out: whether the negative-case discipline earns a documented home, which is
  [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md).

**Inputs**
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md`
- `tests/test_cli.py` — `test_a_pipe_inside_a_code_span_is_still_a_cell_boundary`, which asserts the
  count.
- [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) — why the check reads code
  spans rather than blanking them.
- `tasks/_task-template.md` — the file their scanner reported, and the corpus evidence this replaces.

**Acceptance criteria**
- [x] The fixture carries a front matter with a `|`-separated menu, and the asserted count does not
      move — shown by running the test, not by reading it
- [x] Deleting the guard in `check_wide_rows` that keeps it quiet makes the test fail, so the new case
      is proven to be doing work rather than merely present

**Open questions**
- None.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Check the front matter is even walked — `FENCE` must not treat `---` as a fence, or the case is skipped and every assertion about it is vacuous | The answer in §3 |
| 2 | Extend the existing negative fixture's front matter with the template's menus | `tests/fixtures/wide-table-row/tasks/T-002-…md` |
| 3 | Run `check` on the fixture and read the counts: `WIDE ROW` must stay 3 and `table row(s)` must stay 12 | The output in §3 |
| 4 | Delete the guard and show the new case reporting, with a **control** run that removes the front matter so the report is attributable to it | The three runs in §3 |
| 5 | Reconcile the fixture's own description, which counts its behaviours in prose | `tests/fixtures/wide-table-row/.taskmd/config.md` |
| 6 | Suite and `check` | Their output in §3 |

Step 1 is first because it is the cheapest thing that could invalidate the rest: a front matter the
scanner never reaches is a fixture that cannot fail.

## 3. Implement

**Step 1 — the front matter is walked.** `FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")` matches
backticks and tildes only, so `---` opens nothing and `check_wide_rows` reads the front-matter lines
like any others. Had it matched, this whole task would have been a fixture for a code path that never
runs.

**Step 2 — the menus, and why there are three of them.** The fixture's front matter now carries the
shipped template's three menu fields:

```
type: fix | research
business_value: high | low
effort: xs | s | m | l | xl
```

**The first attempt used two lines and proved nothing.** With `type` and `effort` alone, deleting the
guard left the test passing and produced no `WIDE ROW` at all:

```text
--- guard deleted, front matter present  (the new case must now report)
    test exit 0   PASSED - VACUOUS
```

The reason is in the check's own shape: it reads `lines[index + 1]` as the delimiter row and starts
rows at `index + 2`. So a two-line menu has a header and no row under it, guard or no guard. The
fixture would have sat in the tree looking like the strongest case in the file and firing on nothing
— which is precisely the failure this task exists to remove, reproduced while removing it. Widths
ascend for the same reason: `type` is a 2-column header, `business_value` is consumed as the
delimiter, and `effort` is the 5-cell row that reports.

**Step 3 — the counts did not move**, with the fixture's front matter in place:

```text
3 problem(s) - ... 12 table row(s), ... 9 front-matter value(s)
WIDE ROW  tasks/T-001-…:16, :22, :31          (all three in the *reporting* task)
```

`12 table row(s)` is the second witness and the more direct one: the three new pipe-carrying lines
were counted as **front matter**, which rose from 6 to 9, and as **no** table rows at all.

**Step 4 — the guard deleted, with a control.** Removing `and is_delimiter_row(lines[index + 1])`:

```text
--- baseline: guard present, front matter present
    test exit 0   1 passed
    WIDE ROW in T-002: none

--- guard deleted, front matter present  (the new case must now report)
    test exit 1   FAILED as intended
    WIDE ROW  tasks/T-002-three-rows-that-lose-nothing.md:7 has 5 cells against a
              2-column header; Markdown drops the rest and that text renders nowhere

--- guard deleted, front matter REMOVED  (control: the rest of the file)
    none

--- restored
    test exit 0   1 passed
```

The control is what makes this evidence rather than a coincidence: with the guard gone, everything
else in that file — the blank excess cell, the escaped pipe, the short row, the fence — still reports
nothing. The single failure is line 7, the `effort` menu, and it exists only because this task added it.

**Step 5 — the fixture's description was falsified by the change.** Its `.taskmd/config.md` read
*all six behaviours … the second holds the three it must ignore*. It is now seven and four, and says
which the fourth is. Left alone, the file explaining the fixture would have miscounted the fixture.

**Step 6**

```text
264 passed, 3 skipped, 6 subtests passed
OK - 161 task(s), ... 3313 table row(s), ...          exit=0
```

**Decisions & assumptions**

- **Three menu lines, not two** — 2026-08-16, forced by the vacuous run above. *Rejected:* the
  two-line front matter the draft implies, which passes its own criterion 1 and cannot fail criterion
  2. Recorded rather than quietly corrected, because the vacuous version left no trace once fixed.
- **The three fields are the template's own** (`type`, `business_value`, `effort`) — 2026-08-16.
  The reporter's scanner fired on `tasks/_task-template.md`, so the specimen should be that file's
  shape rather than an invented one. Ascending width is the only liberty taken, and it is stated in
  the fixture so the next reader does not tidy it away.
- **The fixture's prose count was updated, not left** — 2026-08-16. *Rejected:* treating it as out of
  scope on the ground that the task named one file; a fixture whose description miscounts it is the
  same class of defect as the corpus-shaped silence this task removes.
- **`check_wide_rows` is untouched** — 2026-08-16, per the scope. It behaves correctly; the whole
  change is what holds it there.

**Outputs produced**
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md` — the front matter and
  the paragraph saying what it is for.
- `tests/fixtures/wide-table-row/.taskmd/config.md` — the behaviour count.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The fixture carries a `\|`-separated front matter and the asserted count does not move — shown by running | met | Run, not read: `WIDE ROW` stays 3 and all three are in T-001, the reporting task. `12 table row(s)` is unchanged and `front-matter value(s)` rose 6 → 9, so the new lines are provably being read as front matter rather than skipped. |
| Deleting the guard makes the test fail, so the case is doing work | met | And with a control the criterion did not ask for. Guard present → silent; guard deleted → `T-002:7 has 5 cells against a 2-column header`, test exit 1; guard deleted **and** front matter removed → silent again. The middle result is attributable to this task's lines and nothing else in the file. **The first shape of the fixture failed this criterion** — two menu lines, guard deleted, test still green — and the reason is recorded in §3 rather than repaired out of sight. |

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | Both criteria met, and the task **reproduced the fault it was raised to remove** before fixing it. The obvious fixture — the two menu fields the draft's evidence names — passes criterion 1 and cannot fail criterion 2: `check_wide_rows` consumes `index + 1` as the delimiter, so two pipe lines make a header with no row under it, and the case fires on nothing with the guard deleted. Recorded rather than silently corrected, because a vacuous pass leaves no trace once it is repaired. Three lines with ascending widths fixes it, and they are the shipped template's own three fields, which is what the reporter's scanner actually hit. Two things outside the named file also moved: the fixture's `.taskmd/config.md` counts its own behaviours in prose and now says seven and four. `low` and `xs` were right about the stakes and right about the size. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): the maintainer asked for this task's full lifecycle**, given 2026-08-16 as the subject of a handoff — *work all 4 from the list, full lifecycle*. The list is the four unblocked `fix` tasks named that day: [T-145](T-145-stop-help-answering-for-a-command-that-does-not-exist.md), [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md), [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md). It covers those four and **nothing else** — not the five `decision` tasks beside them on the same list, and not anything these four raise. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. |
| 2026-08-15 | → proposed | Raised from triaging the newest comment on issue #1. **Not a defect** — the specimen run that day shows the check already silent on this class, and the row is filed as a fixture gap rather than as the false positive the reporter met in their own code. `low` and `xs` because nothing is broken and the whole change is one section in a file that already exists. The second criterion is there because a negative case that would pass without the code under test is the failure mode this task exists to remove, one level up. |
