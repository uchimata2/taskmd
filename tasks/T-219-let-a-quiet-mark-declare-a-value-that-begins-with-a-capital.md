---
id: T-219
title: Let a quiet mark declare a value that begins with a capital
type: fix
status: done
phase: review
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
| 1 | Put a declared value back on the `T-003` mark in `tests/fixtures/broken-closed-parent/`, and run the reading and assertion 1 against the **committed** module. | The reading's line for that mark and the assertion's failure, quoted in §3 |
| 2 | Read the class as whole words rather than as a run of capitals-and-spaces, with a guard that refuses a word touching a hyphen or a digit. | The new `MARK_RE` in `tests/test_quiet_cases.py`, with the reason written beside it |
| 3 | Run the reading again. | The same mark's line, quoted in §3 |
| 4 | **Diff the whole reading**, committed module against new, over the same tree — not the totals, which cannot see a swap. | The diff in §3 |
| 5 | Run the suite and `check`. | Their output in §3 |

**Shape decision — the class is words, not a character run.** Every class `check` can print is made
of words of two or more capitals, so a one-letter word is a value and not a class. **Rejected:
requiring the value to be quoted or bracketed in the mark**, which would change the mark syntax every
existing fixture is written in, for a defect that is in the reader. **Rejected: a non-greedy class
group**, which would stop `CLOSED PARENT` matching its second word.

**Step 4 exists because step 3 cannot see a regression.** A totals line — *29 cases in 27 marks* — is
identical whether the other 26 marks parse as before or two of them swapped values, which is the
exact failure `TheReadingLosesNothing` was written for one level up.

**Outputs**
- tests/test_quiet_cases.py
- tests/fixtures/broken-closed-parent/tasks/T-003-closed-with-every-child-closed.md

## 3. Implement

**Step 1 — the defect, against the committed module**

```text
$ python tests/test_quiet_cases.py --list
  broken-closed-parent/tasks/T-003-closed-with-every-child-closed.md  line 9  CLOSED PARENT T closed, and its only child T-004 is closed too, ...

$ python -m pytest tests/test_quiet_cases.py -q -k "names_a_class"
E  AssertionError: 'CLOSED PARENT T' not found in {..., 'CLOSED PARENT', ...} :
   broken-closed-parent/tasks/T-003-closed-with-every-child-closed.md line 9 marks a quiet case
   for 'CLOSED PARENT T', which `check` cannot print - the class set is derived in tests/classes.py
1 failed, 9 deselected in 0.10s
```

**Both halves of the finding are in that output.** The class is read as `CLOSED PARENT T`, and the
message names the class as the thing `check` cannot print — while the set it prints beside it
contains `CLOSED PARENT`. The value is gone too: the `T` went to the class and `-003` to `values`.

**Step 2 — the repair**

```python
MARK_RE = re.compile(
    r"(?:#|<!--)\s*quiet:\s*(?P<cls>[A-Z]{2,}(?:\s+[A-Z]{2,})*)(?![\w-])"
    r"\s*(?P<values>.*?)\s+-\s+"
    r"(?P<why>.+?)\s*(?:-->)?\s*$")
```

The reason is written above it in the module, in the same form as the note already there about the
`values` group: what the old pattern did, on which mark, and what it cost.

**Step 3 — the same mark, after**

```text
$ python tests/test_quiet_cases.py --list
  broken-closed-parent/tasks/T-003-closed-with-every-child-closed.md  line 9  CLOSED PARENT  closed, and its only child T-004 is closed too, ...
```

**Step 4 — the whole reading, diffed**

The committed module was checked out beside the new one and both were run over the same tree:

```text
$ git show HEAD:tests/test_quiet_cases.py > tests/_old_quiet.py
$ python tests/_old_quiet.py --list > before.txt ; python tests/test_quiet_cases.py --list > after.txt
$ diff before.txt after.txt
15c15
<   ...T-003-closed-with-every-child-closed.md  line 9  CLOSED PARENT T closed, and its only child ...
---
>   ...T-003-closed-with-every-child-closed.md  line 9  CLOSED PARENT  closed, and its only child ...
```

**One line, and it is the mark under repair.** Every other mark in the tree parses byte for byte as
before. The totals were identical on both sides — *29 quiet case(s) in 27 mark(s), across 9
fixture(s)* — which is exactly why the diff and not the totals is the evidence.

**Decisions & assumptions**

1. **The class is matched as words of two or more capitals** — 2026-08-22 — with `(?![\w-])` after
   the last one, so a word touching a hyphen or a digit fails the class and falls through to
   `values`. Both halves are needed: the word rule alone would still swallow `AB` out of `AB-1`.
2. **The fixture keeps the declared value** — 2026-08-22. Criterion 2 asks for a committed mark that
   exercises the repair, and the natural one is the mark that found the defect. Only `T-003`'s carries
   a value; `T-005`'s is a whole-record mark with nothing to narrow, and inventing one to make a pair
   would be a fixture written for the test rather than for the case.
3. **The diagnostic message was not changed** — 2026-08-22. §1 offered *either it parses, or the
   failure says the value was eaten*. It parses, so the second arm is not needed, and a message about
   a state that can no longer arise is a sentence nobody will ever read. **Rejected: writing it
   anyway** — it would be untestable without re-introducing the defect.
4. **[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §3 decision 4 is
   annotated, not edited** — 2026-08-22. It says the two marks carry no declared value, which was
   true when it was written and is now false for one of them. That is a statement about the past, so
   METHOD rule 5 says annotate: a Log row on T-212 points here. Its other half — that assertion 2
   cannot bite on a class writing ids bare — is **unchanged by this task** and stays true.

**Step 5 — the gates**

```text
$ python -m pytest tests -q
327 passed, 8 subtests passed in 43.46s

$ ./plugin/bin/taskmd check
OK - 219 task(s), 1095 field value(s), 3690 front-matter value(s), 725 reference(s), 25 dependency edge(s), ...
EXIT=0
```

**Outputs produced**
- [`tests/test_quiet_cases.py`](../tests/test_quiet_cases.py)
- `tests/fixtures/broken-closed-parent/tasks/T-003-closed-with-every-child-closed.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The current behaviour is shown **failing first**, with the output quoted | met | §3 step 1: the reading shows the class as `CLOSED PARENT T`, and assertion 1 fails against the committed module. Run before any edit to the pattern |
| After the fix, a mark in a committed fixture declares a capital-initial value and the reading holds it, with `--list` quoted | met | §3 step 3. `tests/fixtures/broken-closed-parent/tasks/T-003-closed-with-every-child-closed.md` declares `T-003`, and the reading now shows the class as `CLOSED PARENT` |
| `test_a_declared_value_really_is_on_the_marked_line` still passes on that mark, so the value is parsed as itself and not as a fragment | met | It is in the 327 of §3 step 5, and it is the assertion that would fail on a `values` of `-003`: that string is not on the marked line, `T-003` is |
| Every existing mark parses exactly as before — the reading's totals are quoted from before and after and compared | met | §3 step 4 does **more** than the criterion asks: the totals match (*29 in 27 across 9*), and the full readings were diffed line by line, giving one changed line, the mark under repair. The criterion's own instrument — totals — is stated there as insufficient |
| The suite is green and the output is quoted | met | §3 step 5, `327 passed, 8 subtests passed`, with `check` at exit 0 beside it |

**What review found beyond the table.** Nothing new. The one thing worth carrying is already in §3
decision 4: this repair does not touch the *other* limit found in the same place — assertion 2 cannot
bite on a class that writes ids bare — and that limit is stated in the module's own docstring, so it
has a home.

**Open questions, re-read before closing** (`review` step 5). §1 recorded none and none arose.
Nothing is addressed to anyone else.

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | All five criteria met. The class is now read as whole words of two or more capitals with a guard against a word touching a hyphen or digit, so a mark can declare `T-003`. Shown failing first against the committed module, then **diffed line by line** over the same tree — one changed line, the mark under repair. [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §3 decision 4 is annotated there rather than edited (METHOD rule 5). Raised and closed the same day, under the grant recorded below. |
| 2026-08-22 | → proposed | Raised from [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)'s review, which hit it while marking the two quiet cases of the `CLOSED PARENT` class and worked around it by dropping the declared values. `xs` and `medium`: one regular expression, but it silently narrows what every future mark can say, and the class of defect — a reader that cannot report its own incompleteness — is the one `tests/test_quiet_cases.py` exists to close. **Covered by the multi-phase grant**, per the row below. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — this task is covered by it, and it is covered *because of how it arose*.** The **project owner** extended the grant on **2026-08-22**, at the start of the session that resumed the eight, in these words: *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it covers:** this task — raised while working [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), one of the eight — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed. **What it does not cover:** it authorises **phases, not answers**. A task that reaches an open question belonging to the owner stops there, which is what *where my involvement is not needed* means; §1 records that this one has none. The grant reaches this record because the work that raised it was inside the eight — **not** because the backlog happens to contain no owner-facing alternative, and not by any description of what needs nobody. A task raised by a later session is outside it. The eight, and the three earlier steps that built the grant, are recorded in each of those records. |
