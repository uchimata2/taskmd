---
id: T-124
title: Stop a test asserting this repository has open M2 work
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-087, T-110]
work_package: M2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [tests/test_list.py]
---

# T-124 — Stop a test asserting this repository has open M2 work

## 1. Specify

**Outcome**
`tests/test_list.py`'s proof that a non-enumerated field can be filtered on survives this repository
finishing a milestone. Today it asserts that `list --work_package M2 --open` returns rows against
the live tree, so closing the last open `M2` task turns it red.

**Why this one**
Found by running the suite after closing `T-090`, which was the last open `M2` task:

```
FAIL: test_a_stored_field_the_schema_does_not_enumerate_can_be_selected_on
AssertionError: [] is not true : no rows; the filter matched nothing at all
```

**Nothing is wrong with the tool.** `list --work_package M2 --open` correctly returns nothing,
because there is nothing. The failure is a test that pinned a fact about the *project's progress* in
order to prove a fact about the *filter*, and progress is the one thing in this tree guaranteed to
change. It is the same shape as the counted-set lessons this project keeps re-learning: a hand-named
membership goes stale exactly when the work it describes succeeds.

**It is worth `medium`, not `low`.** A red suite is the condition under which every other claim in
this repository stops being checkable — and it fails in the most misleading direction, since a
session that has just changed `list` or the schema will read this as their regression.

**Requirements served**
R-16, at the level of the suite that carries it: a test that can fail for a reason unrelated to what
it proves is a test that teaches sessions to discount failures.

**Scope**
- In: how that test chooses the value it filters on, and how it knows what to expect back.
- In: whether any neighbouring test in the same file has the same coupling to live project data.
- Out: `list`'s behaviour, which is correct and is not in question.
- Out: the work-package grouping itself, settled in [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md).

**Inputs**
- `tests/test_list.py`, `FiltersOnAFieldNoVocabularyEnumerates`.
- [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md), for what the test exists to prove.

**Acceptance criteria**
- [ ] The full suite passes on the current tree, shown by running it
- [ ] The test still fails if `list` stops filtering on a non-enumerated field — shown by breaking
      that, not by reading the assertion
- [ ] No test in `tests/test_list.py` asserts a value that depends on which tasks are open
- [ ] The replacement names, in the test itself, what would now falsify it

**Open questions**
- none.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Sweep `tests/test_list.py` for every assertion made against the live tree, and say which of them depend on *which tasks are open* rather than on the tree merely having tasks. | The list, in §3 |
| 2 | Have the test take its filter value from the data it is about to filter, rather than naming one. | `tests/test_list.py` |
| 3 | Break `list`'s non-enumerated filtering and show the replacement goes red — the assertion has to be earning its place, not merely surviving. | Recorded output |
| 4 | Run the suite. | Recorded output |

**Shape decisions.**

**D1 — The test derives the value it filters on from `list --json`, and asserts that same task comes
back.** The claim under test is *a field the schema does not enumerate can be filtered on*, and that
needs a real non-enumerated field with a real value — not a particular one. Deriving it makes the
test say what it means and removes every way the project's own progress can falsify it.

*Rejected: keep `M2` and drop `--open`.* It is one word, it fixes today's failure, and `M2`'s
membership is now permanent. It was rejected because the defect is not that `--open` expired — it is
that a test named a value from a list somebody maintains, and the next re-grouping renames the
milestones (T-110 has already done this once). The one-word fix leaves that intact and moves the
expiry date.

**D2 — The falsifier is named in the test and then demonstrated.** A derived-value test can pass by
comparing something to itself, which is exactly the failure mode of the assertion it replaces. Step 3
breaks the filter and records the red run, so the test is known to be able to fail.

**Planned outputs**
- tests/test_list.py

## 3. Implement

### Step 1 — the sweep

`tests/test_list.py` runs against the live tree in 15 places. Sorted by what each depends on:

- **Which tasks are open — one, and it is the failing one.** `--work_package M2 --open`, asserting
  rows come back.
- **The tree merely having tasks** — `--limit 1` for the tab-separated form, `--json` for the JSON
  one, and the closing-line test. A repository with no tasks at all is a different situation and
  these say so by failing; none of them can be falsified by work being finished.
- **Nothing in the tree** — the eleven rejection tests, which assert an error message and a non-zero
  exit for an argument no project accepts.

One more was worth a second look and is left alone: `--blocked-by T-004` asserts only `exit 0`, so it
cannot fail if nothing is blocked by `T-004` — a vacuousness risk rather than the coupling this task
is about, and its claim genuinely is *the hyphenated spelling is accepted*.

### Step 2 — the value comes from the data

The test now reads `list --json`, takes the first task carrying a `work_package` at all, filters on
that task's own value, and asserts both that the task comes back and that every row carries the
value. Nothing names a milestone, so no re-grouping and no finished milestone can reach it. What
falsifies it is written into the docstring rather than left to be inferred.

### Step 3 — shown red

`parse_filters` was temporarily made to reject a non-vocabulary field, and the replacement failed:

```text
FAIL: test_a_stored_field_the_schema_does_not_enumerate_can_be_selected_on
AssertionError: 2 != 0 : unknown filter: --work_package. This project accepts: …, --work_package
```

The message is its own joke — the flag is in the accepted list it prints — which is what a
deliberately broken branch looks like. The break was reverted before the suite run below; `git diff
--stat plugin/` reports nothing.

### Step 4 — the suite

`test_cli` 100 OK, `test_list` 37 OK, `test_schema` 53 OK, `test_budget` 5 OK, `test_runtime` 27
`OK (skipped=3)`.

**Six failures in `test_cli` arrived between two of those runs and were not this fix.** They were a
`STALE INDEX`, from adding this task's own file — the trap the previous session recorded, met again
in the same session that wrote it down. Every one of the six was a count assertion about this
repository, which is the shape most easily read as a regression in whatever was last touched:

```text
Wrote tasks/README.md - 8 active, 116 closed
OK - 124 task(s), 620 field value(s), … 152 document(s), 1261 link(s), …
```

**Decisions & assumptions**
- **D1 — the filter value is derived from the data, not named** — 2026-08-11, §2; the one-word
  alternative is recorded there with why it only moves the expiry date.
- **D2 — the falsifier is named in the test and demonstrated** — 2026-08-11, §2, step 3.
- **Assumption: the tree always has at least one task carrying a `work_package`.** If it does not,
  the test raises `IndexError` rather than passing quietly — the failure mode of a repository with no
  tasks, which is not a state this suite is meaningful in.

**Outputs produced**
- [`tests/test_list.py`](../tests/test_list.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The full suite passes on the current tree, shown by running it | met | §3 step 4, all five modules, after the index was regenerated |
| The test still fails if `list` stops filtering on a non-enumerated field — shown by breaking that, not by reading the assertion | met | §3 step 3: the branch was broken, the run quoted, and the break reverted with `git diff --stat plugin/` empty |
| No test in `tests/test_list.py` asserts a value that depends on which tasks are open | met | §3 step 1 partitions all 15 live-tree assertions by what each depends on, so the answer is a walk rather than a spot check |
| The replacement names, in the test itself, what would now falsify it | met | The docstring says what breaks it and which assertion catches which case, and step 3 is that sentence being tested |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met, no child raised. Worked end to end under the standing `M2` full-lifecycle authorization the filing rule brings this task inside (METHOD §3.1); raised and closed in the same session, but not in the same task, which is the distinction rule 4 turns on. **The fix is not the one-word one**, and that is the whole of the decision: dropping `--open` clears today's failure and leaves a test naming a milestone label the maintainer has already re-cut once, so the expiry date moves rather than the coupling going. The value is now taken from the data it is about to filter. **The replacement was shown red before it was accepted** — `parse_filters` temporarily rejected non-vocabulary fields, and the run is quoted — because a derived-value test is exactly the kind that can pass by comparing something to itself. Two things worth carrying. The sweep in §3 step 1 **partitions all 15 live-tree assertions** rather than checking the neighbours that looked similar, which is what turned up that only one of them could ever be falsified by work being finished. And six `test_cli` failures appeared mid-run and were a **stale index** caused by this task's own file — the previous session recorded that trap in its handoff, and it was met again by the session that had just read it. |
| 2026-08-11 | → proposed | Raised from the run that followed closing T-090, not from reading — and by the session that caused it, which closed the last six open `M2` tasks in a row. Not fixed where it was found (METHOD rule 4): the finding belongs to none of those six, and a test edit inside one of their diffs would be indistinguishable from tidying. **Filed `M2` by `tasks/README.md`'s rule** — a minor correction blocking nothing — which brings it inside the standing full-lifecycle authorization as a consequence of the filing rule, the same way T-123 was. Worth knowing before it is worked: `master` is red as this is raised, and the failing assertion is about the project's progress rather than about the tool. |
