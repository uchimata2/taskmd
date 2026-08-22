---
id: T-202
title: Mark a fixture's quiet cases so a sweep can find them
type: deliverable
status: done
phase: review
parent: T-198
blocked_by: []
related: [T-197, T-151, T-134]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-22
adopter_visible: no
deliverables:
  - tests/test_quiet_cases.py
  - tests/fixtures/README.md
  - tests/fixtures/abandoned-slot/tasks/T-002-open-and-has-not-reached-the-section.md
  - tests/fixtures/abandoned-slot/tasks/T-003-closed-and-quoting-a-slot-to-explain-it.md
  - tests/fixtures/broken-parked-task/tasks/_drafts/notes.md
  - tests/fixtures/label-shaped-value/tasks/T-002-the-defect-under-another-name.md
  - tests/fixtures/label-shaped-value/tasks/T-003-the-same-label-again.md
  - tests/fixtures/malformed-date/tasks/T-001-the-accident-that-found-this.md
  - tests/fixtures/malformed-date/tasks/T-002-a-month-and-a-day-that-do-not-exist.md
  - tests/fixtures/section-reference/docs/guide.md
  - tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md
---

# T-202 — Mark a fixture's quiet cases so a sweep can find them

## 1. Specify

**Outcome**
The cases a fixture carries **in order to stay silent** are marked in the fixture itself, so the set
can be read from the tree rather than from prose — and a quiet case added tomorrow is in the next
sweep with nothing edited anywhere. **The marks are the authority**: `tests/fixtures/README.md`
keeps a short note on why quiet cases exist, points at them, and carries no list of its own (the
owner's answer of 2026-08-22, below).

**Why this one**
Finding **F-2** of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), and it
is the reason that audit's first criterion is **not met**. Two derivations were tried and neither
answers the question:

| Attempt | Found | Why it is the wrong set |
| :--- | ---: | :--- |
| Fixtures named by a must-not-catch assertion, parsed from `tests/test_cli.py` | 21 | Mostly the cross-fixture `fails()` silence. It **misses `abandoned-slot` and `wide-table-row`**, whose quiet tests iterate the fixture directory or build a tree, so no fixture name appears as a literal |
| `tests/fixtures/README.md`, which names five fixtures shaped to carry their own quiet cases | 5 | Prose. A classification somebody wrote, not a fact the tree states |

**So the set that matters is the one nothing can compute.** T-198 examined the five, and it examined
them because a document said so. A sixth fixture given a quiet case next week appears in neither
derivation, and the audit that was supposed to catch exactly that would not see it.

**The mechanism already exists in this repository, twice.** `leak-check` marks its own lines with
`CAUGHT` and `IGNORED`, and `tests/test_publishing.py` reads them to prove the pattern fires on one
and not the other — a fixture stating its own expectations. `<!-- taskmd:… -->` marked regions
([T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md)) are the same idea
for prose. Neither is applied here.

**This is the same class as [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md), one level down.** That
task removed a hand-typed list of check classes. This removes a hand-written list of quiet cases. Both
are a set the tree owns, described somewhere else.

**Scope**
- In: how a quiet case declares itself — a marker, a naming convention, or a manifest the fixture
  carries
- In: applying it to the quiet cases carried by the five fixtures `tests/fixtures/README.md` names
  **today** — that document is where the set is read from now and stops being its home — and to
  `leak-check`, whose markers may already be the answer generalised
- In: a test that reads the marks, so the set is exercised rather than merely readable
- Out: **repairing any quiet case the marks then expose.** Each is its own finding, as
  [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) is
- Out: the cross-fixture silence assertion, which is
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)'s and is closed

**Inputs**
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 — the two failed
  derivations and what each missed
- `tests/fixtures/leak-check/` and its reader in `tests/test_publishing.py` — the mechanism to
  generalise or reject
- `tests/fixtures/README.md` — the prose the marks would replace as the authority

**Acceptance criteria**
- [ ] The quiet-case set is read from the tree, and the reading is shown
- [ ] **The reading answers to what [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)
      *names*, not to what it exercised.** That audit exercised fifteen cases and its record names
      more: `malformed-date`'s `keep-me`, `section-reference`'s two unmutated marks, and
      `wide-table-row`'s short row — the last of which
      [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) had to add after
      the fact. The two counts are stated together and any difference is explained, so a reading
      that reproduces the fifteen and drops the rest fails here
- [ ] **A quiet case added to a fixture with nothing else edited appears in the reading**, shown by
      adding one and quoting the result
- [ ] **A mark that names a case the check cannot reach fails**, shown by breaking one on purpose —
      otherwise this ships the same silence it is removing
- [ ] `tests/fixtures/README.md` states **why** quiet cases exist and points at the marks; it names
      no fixture's cases and carries no list, so nothing is left there to go stale

**Open questions**
- ~~**Does this replace the prose in `tests/fixtures/README.md`, or sit beside it?** The README is
  read by a person deciding where to add a fixture, and a marker is read by a test. Both may be
  wanted, and then the question is which is authoritative — the maintainer's, at `specify`.~~ **Answered by the owner on 2026-08-22: markers in the fixture are the authoritative list, and the README keeps a short note pointing at them** — see the Log row of that date.
- **None outstanding.** Specify is agreed.

## 2. Plan

**Sequencing.** Step 1 is first because it can invalidate every step after it: these fixtures are
live taskmd projects whose tests assert exact line numbers and exact counts, so a marker form that
adds a line or a table cell breaks the very cases it is marking. Step 2 may reshape steps 5–7, and
the plan is edited in place when it does rather than guessed at now.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Settle the marker **form**, against the one constraint that decides it: a mark must not change what `check` reports on the fixture it sits in. Run each candidate on the six fixtures in scope and run the suite. `wide-table-row` is the hard case — three of its quiet cases are table rows, and a trailing mark after the closing pipe is a further cell. | A decision in §3 naming the form, with each rejected form and the **measured** reason — the `check` or suite output it produced, not an argument |
| 2 | Settle what a mark must **state**. A line number is not a quiet case: the reading has to know which class the case must stay silent for, and that class name has to answer to `tests/classes.py`, which is its one home since [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md). | The mark's fields and their allowed values, recorded as a decision with the rejected alternatives |
| 3 | Mark the quiet cases in the six fixtures in scope — the five `tests/fixtures/README.md` names today, plus `leak-check`, whose `CAUGHT` / `IGNORED` markers are the mechanism being generalised and may already be the answer unchanged. | The marks, in the fixture files |
| 4 | Reconcile the marks against what [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) **names**, fixture by fixture and case by case. That record names cases it did not exercise, and it also names quiet cases in two fixtures this task's scope excludes — see the note below the table. | A table in §3, one row per fixture, giving cases marked against cases that record names, every difference explained; **and a new task** for any named case the agreed scope leaves unmarked |
| 5 | Write the reader: a test that derives the quiet-case set from the marks, asserts each marked case is silent on an unedited fixture, and asserts the class each mark names is one the validator reports. | The test file, and its output quoted in §3 |
| 6 | Show the reading is live — add one quiet case to a fixture, edit nothing else, read again. | Both readings quoted in §3, and a recorded decision on whether the added case stays in the tree |
| 7 | Show that a mark naming a case the check cannot reach **fails**. Break one on purpose. | The failing run quoted in §3 |
| 8 | Cut `tests/fixtures/README.md` back to why quiet cases exist and a pointer to the marks. | The edited section — no fixture's cases named, no list |
| 9 | Run the binding's *after any write*, run the suite, and sweep what this change made stale. | `index`, `check` and the suite output quoted in §3, and every document the sweep touched named |

**Shape of the deliverable, decided — 2026-08-22.** Three parts: **marks inside the fixtures**, a
**reader in `tests/`**, and a **shortened note** in `tests/fixtures/README.md`. *Rejected: a manifest
file listing each fixture's cases*, easier to read in one place, but adding a quiet case would then
mean editing the case and the manifest, which is the second write §4 of
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) forbids and the defect this task exists to
remove, one file over. *Rejected: teaching `check` to report quiet cases*, which would put a
test-fixture concept inside the shipped tool and hand every adopter a class they have no use for.

**A residual is already visible and step 4 is where it lands.** T-198's record names quiet cases in
`migrated-away` (two) and `planned-deliverable` (one) — added to it on 2026-08-22 by
[T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md) — and neither
fixture is among the five §1's scope names. Working the agreed scope leaves those three named cases
unmarked, so step 4 states the difference and raises a task for it rather than widening the scope
here: scope was agreed at `specify`, and the grant in the Log authorises phases, not answers.

**Outputs** — plain paths, because none of them exists yet:

- tests/fixtures/README.md
- tests/fixtures/abandoned-slot/
- tests/fixtures/label-shaped-value/
- tests/fixtures/leak-check/samples.txt
- tests/fixtures/malformed-date/
- tests/fixtures/section-reference/
- tests/fixtures/wide-table-row/
- tests/test_quiet_cases.py
- a new task for the named cases the scope leaves unmarked, if step 4 confirms any

## 3. Implement

### Step 1 — the marker form, decided by measurement

Four candidate forms, each applied to a scratch copy of the fixture and run through `check`. The
question each had to answer is the plan's constraint: **does the mark change what `check` reports?**

| # | Form | Measured |
| :-- | :--- | :--- |
| A | trailing `#` comment on a **front-matter** line | **inert.** `malformed-date` reported the same 4 problems on the same 4 lines, and `label-shaped-value` the same 3, before and after marking |
| B | trailing `<!-- -->` at the end of a **table row** | **rejected — it creates the defect.** `wide-table-row` went from 3 problems to 4: `T-002...:35 has 4 cells against a 2-column header`. The comment is a further cell, so the mark turns the quiet case into the class it is marked as quiet for |
| C | trailing `<!-- -->` on the **`##` heading** that introduces the case | **inert.** `wide-table-row` reported the same 3 problems |
| D | `<!-- -->` on **its own line** above the case | inert to `check`, and rejected on a second ground below |

**A is inert *and* keeps the case's reason intact — measured, not argued.** The worry with A is that
the value becomes `2026-08-18  # quiet: MALFORMED DATE`, which is no longer a date, so the case would
stay silent for the wrong reason and nothing would show it. Putting a malformed date on the *marked*
line answers it:

```text
created: 2026-08-99  # quiet: MALFORMED DATE   -> 5 MALFORMED DATE lines
created: 2026-08-99                            -> 5 MALFORMED DATE lines
```

Baseline is 4. The marked line fires exactly as the unmarked one does, so the rule reads the date
inside the marked value and the silence is still the real date's doing.

**D is rejected against C, and not because `check` can see the difference.** Both are inert. A mark
on its own line binds to the case **by adjacency**, which nothing checks and a later edit can break
silently; a mark on the heading binds to the section, which is the unit `check`'s own line-numbered
alarms fall inside. The one that can go wrong without a signal loses.

**Decision — 2026-08-22: a mark sits on the line that carries the case, in that line's own comment
syntax.** Two anchors, because a quiet case is one of exactly two things here:

- a **front-matter field** → form A, and the anchor is the field name, which is what `check` prints
  in a `MALFORMED DATE` / `LABEL SHAPE` alarm;
- a **body section** → form C, and the anchor is the section, which is what a line-numbered
  `WIDE ROW` / `ABANDONED SLOT` alarm falls inside.

*Rejected: one universal form.* Form B is the only single form that would reach a table-row case
directly, and it is the one measured to create the defect. *Rejected: writing the line number into
the mark*, which is a derived value copied by hand — it decays the first time a line is inserted
above it, and silently.

### Step 2 — what a mark states

**Decision — 2026-08-22: `quiet: <CLASS> - <why it stays silent>`.** The class name answers to
`tests/classes.py`, its one home since
[T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md), so a mark naming a
class the validator does not report is a failure rather than a comment. *Rejected: a free-text
note*, which is the README's prose moved into the fixture and checkable by nothing.

`leak-check` is left on its own `<- must be caught` / `<- must be ignored` markers rather than
converted: it is a plain-text file with no comment syntax, its markers already are a fixture stating
its own expectations, and `tests/test_publishing.py` already reads them. The reading takes it as the
same declaration in a second syntax.

### Step 3 - the marks, and the proof they changed nothing

18 marks written across the five fixtures. **The evidence that a mark is inert is a byte-for-byte
comparison of `check`'s output**, pristine against marked, with both copies extracted outside git so
the `Scope` line's git-presence branch is not read as a difference:

```text
IDENTICAL  abandoned-slot   4 lines
IDENTICAL  label-shaped-value   8 lines
IDENTICAL  malformed-date   8 lines
IDENTICAL  section-reference   6 lines
IDENTICAL  wide-table-row   7 lines
```

The first attempt at this compared the marked tree against `git archive HEAD`, and every fixture
came back different on one line: *every document read; no git here* against *0 document(s) not
read*. That is the comparison method showing, not the marks - a working tree is not a clone.

`leak-check` keeps its own `<- must be caught` / `<- must be ignored` markers, per step 2.

### Step 5 - the reader, and the two marks it silently dropped

`tests/test_quiet_cases.py`. It walks the fixtures, parses the marks, and asserts three things: the
class is one `check` can print, no alarm names what a mark covers, and **the class fires at least
once elsewhere in the same fixture** - `leak-check`'s both-directions structure, generalised.

**Its first run read 20 cases where 18 marks plus 4 `leak-check` lines had been written.** The
`values` group was a class excluding hyphens, and a date is full of them, so the two marks narrowed
to a list of values - `2026-08-01, keep-me` and `1.4.2, keep-me` - matched nothing and vanished.
Every other assertion stayed green over a set that was short by two.

**So the reader gained an assertion it did not have**: every line under `tests/fixtures/` carrying a
mark inside a comment is either parsed into a case or named as unparsed. A reader cannot report its
own incompleteness; a partition can. Its first run failed on `tests/fixtures/README.md` line 64,
which used the words *stay quiet:* in a sentence - so the mark word was tightened to the word inside
a comment, which is what a mark actually looks like, and the parser and the guard now agree on what
one is.

### Step 6 - the reading is live

One line added to `label-shaped-value/tasks/T-003`, a real three-part version with its mark, and
nothing else edited anywhere:

```text
BEFORE   22 quiet case(s) marked, across 6 fixture(s)
AFTER    23 quiet case(s) marked, across 6 fixture(s)
  label-shaped-value/tasks/T-003-the-same-label-again.md  line 7  LABEL SHAPE  a real three-part
  version in a second task, so one task's silence is not the whole of the evidence
```

**The added case stays in the tree.** It is a real quiet case and the suite is green over it, so
removing it after the demonstration would leave the fixture weaker in order to keep a number round.

### Step 7 - a mark that names a case out of reach fails

Three breaks, each applied on purpose and reverted, each quoting what arrived:

```text
a class that never fires in this fixture
  AssertionError: [] is not true : wide-table-row marks a case quiet for MALFORMED DATE and nothing
  in that fixture reports MALFORMED DATE, so the silence may be the check not reaching it rather
  than the case

a mark on a case that is not quiet at all
  AssertionError: malformed-date/tasks/T-001-...md line 6 marks '2026-08-165' quiet for MALFORMED
  DATE and it reports: ... updated is '2026-08-165', which is shaped like a date and is not one

a mark naming a class `check` cannot print
  AssertionError: 'ABANDONED SLOTS' not found in {'DANGLING', 'PARKED TASK', ...}
```

The fourth break was not staged: the completeness guard's own first run, above.

### Step 8 - the README, and the case its own criterion found

The five bullets naming each fixture's quiet cases are gone, replaced by why quiet cases exist and
the command that reads them. `leak-check`'s paragraph loses *five that must be caught and four safe
forms that must not* - a hand-written count of exactly the kind this task removes - and points at
its markers instead.

**Checking that criterion against the whole file rather than the section just edited found one
more.** The `broken-*` table's row for `broken-parked-task` read *beside a `notes.md` that must stay
unreported*, which is a quiet case named in the README, in a table nobody would look at while
editing the paragraph above it. `notes.md` now marks itself and the cell states the defect alone.
So the marking reaches a sixth fixture, which no plan step named.

**One hand-written ordinal was removed inside a fixture**, for the same reason and recorded here
rather than done quietly: `wide-table-row/T-002` called its front-matter menu *the fourth quiet
case*, an ordinal into an enumeration that no longer exists anywhere.

### Step 4 - the reading against what T-198 names

```text
26 quiet case(s) in 24 mark(s), across 7 fixture(s):
  abandoned-slot          2 case(s) in 2 mark(s)
  broken-parked-task      1 case(s) in 1 mark(s)
  label-shaped-value      5 case(s) in 4 mark(s)
  leak-check              4 case(s) in 4 mark(s)
  malformed-date          4 case(s) in 3 mark(s)
  section-reference       5 case(s) in 5 mark(s)
  wide-table-row          5 case(s) in 5 mark(s)
```

**Cases, not marks, because the two differ and a record that counted marks would undercount.** One
line can hold two quiet cases and a firing one - the `windows` list in `malformed-date/T-002` is
that line - so a mark narrowed to a list of values carries one case per value, and the reading says
both numbers.

| Fixture | Marked | [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) names | Difference |
| :--- | ---: | ---: | :--- |
| `abandoned-slot` | 2 | 2 | - |
| `malformed-date` | 4 | 4 | - (3 exercised, plus `keep-me`, recorded there as true by construction) |
| `section-reference` | 5 | 5 | - (3 exercised, plus the two marks it did not mutate) |
| `wide-table-row` | 5 | 5 | - (4 examined, plus the short row [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) added after the fact) |
| `label-shaped-value` | 5 | 3 | **+2**: `keep-me` inside `targets`, which that record does not name, and the case added at step 6 |
| `leak-check` | 4 | 0 | **+4**: never one of the five, and its checker is `tests/test_publishing.py` |
| `broken-parked-task` | 1 | 0 | **+1**: found by criterion 5's whole-file check, step 8 |
| `migrated-away` | 0 | 2 | **-2** to [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) |
| `planned-deliverable` | 0 | 1 | **-1** to [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) |

**The partition sums both ways, which is the only reason to trust either total.** 19 cases are named
and marked; 7 are marked and not named; 3 are named and not marked. 19 + 7 = 26 marked, and
19 + 3 = 22 named. A double-counted member is invisible in a single total, which is how this same
audit's second criterion passed on a coincidence -
[T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md).

**Annotation, 2026-08-22 by [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) — one of the three is now marked and two never can be.**
The table above and its arithmetic are what this task measured on the day it ran, and they stay as
written. Since then T-211 put each of the three marks in and ran the reader: `migrated-away`'s
`BROKEN LINK` case is **marked**, so that row's **-2** is now **-1**; and the remaining two are
refused by the reader itself, for reasons that are not scope. `CONFIG ERROR` is not a class `check`
owns, so assertion 1 refuses it; `planned-deliverable`'s `MISSING OUTPUT` fires nowhere inside its own
fixture, so assertion 3 refuses it. **The reading no longer defers to this table** — both refusals,
with their reasons asserted rather than described, are in `tests/test_quiet_cases.py`'s
`NAMED_AND_UNMARKED`, which is where a later reader should look. The residual work is
[T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md).

**The three unmarked cases are [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)**, raised rather than
absorbed. `migrated-away` and `planned-deliverable` are outside the five this task's agreed scope
names, and widening a scope the owner agreed at `specify` is the owner's - the grant in this record
authorises phases, not answers.

### Step 9 - the gates

```text
Wrote tasks/README.md - 12 active, 199 closed
OK - 211 task(s), ... 243 document(s), 2886 link(s), ... 3425 section reference(s)
317 passed, 8 subtests passed in 49.15s
```

310 before, 317 after: the seven assertions in the new module. **The sweep found nothing else
stale.** Every other mention of `tests/fixtures/README.md` is inside a closed task's record of what
it did at the time, which METHOD rule 5 says to annotate rather than rewrite, and none of them
claims that document is the *current* home of the quiet-case set.

**Decisions & assumptions**

- **A mark sits on the line that carries the case, in that line's own comment syntax** - a trailing
  `#` in front matter, a trailing HTML comment on the heading of a body section. Rejected: a single
  universal form, because the only one that reaches a table row directly is measured to add a cell
  and create the defect - 2026-08-22.
- **A mark binds to a section, never to the line below it** - rejected: a mark on its own line, which
  binds by adjacency and can be broken by an edit with nothing to report it - 2026-08-22.
- **The class a mark names answers to `tests/classes.py`** - rejected: a free-text note, which is the
  README's prose relocated and checked by nothing - 2026-08-22.
- **A mark carries no line number; the anchor is computed from where the mark sits.** A heading
  covers its section, any other line covers itself. Rejected: writing the line into the mark, which
  is a derived value copied by hand and decays the first time a line is inserted above it -
  2026-08-22.
- **The reading counts cases, not marks** - one line can vouch for two values, so counting marks
  would undercount against a record that counts cases - 2026-08-22.
- **The reach assertion is that the class fires elsewhere in the same fixture**, not that each case
  is mutated. Rejected: mutating every marked case on each run, which is T-198's instrument and
  turns a test into an audit; rejected: marking the firing cases too, which duplicates what `check`
  already prints - 2026-08-22.
- **The case added at step 6 stays in the tree** - it is a real quiet case and the suite is green
  over it; removing it would weaken the fixture to keep a number round - 2026-08-22.
- **`broken-parked-task` is marked although no plan step named it** - criterion 5 binds the whole
  README and that fixture's quiet case was named in it. Rejected: cutting the phrase and leaving the
  case unmarked, which satisfies the criterion by deleting information that then has no home -
  2026-08-22.

**Outputs produced**

- tests/test_quiet_cases.py
- tests/fixtures/README.md
- tests/fixtures/abandoned-slot/tasks/T-002-open-and-has-not-reached-the-section.md
- tests/fixtures/abandoned-slot/tasks/T-003-closed-and-quoting-a-slot-to-explain-it.md
- tests/fixtures/broken-parked-task/tasks/_drafts/notes.md
- tests/fixtures/label-shaped-value/tasks/T-002-the-defect-under-another-name.md
- tests/fixtures/label-shaped-value/tasks/T-003-the-same-label-again.md
- tests/fixtures/malformed-date/tasks/T-001-the-accident-that-found-this.md
- tests/fixtures/malformed-date/tasks/T-002-a-month-and-a-day-that-do-not-exist.md
- tests/fixtures/section-reference/docs/guide.md
- tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md
- [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The quiet-case set is read from the tree, and the reading is shown | met | `python tests/test_quiet_cases.py --list` prints 26 cases in 24 marks across 7 fixtures, quoted in §3 step 4. The marks are the authority and no document holds the set |
| The reading answers to what T-198 **names**, not to what it exercised; the two counts are stated together and any difference explained | met | §3 step 4, one row per fixture. 19 named and marked, 7 marked and not named, 3 named and not marked; 19 + 7 = 26 and 19 + 3 = 22, so the partition sums both ways. All four cases T-198 names outside its exercised fifteen - `keep-me`, `section-reference`'s two unmutated marks, `wide-table-row`'s short row - are marked |
| **A quiet case added to a fixture with nothing else edited appears in the reading**, shown by adding one and quoting the result | met | §3 step 6: one line added to `label-shaped-value/T-003`, reading goes 22 to 23, both quoted. The case stays in the tree |
| **A mark that names a case the check cannot reach fails**, shown by breaking one on purpose | met | §3 step 7: three breaks, each quoting the assertion that arrived - a class that never fires in the fixture, a mark on a case that does fire, and a class `check` cannot print. A fourth was unstaged: the completeness guard failed on its own first run |
| `tests/fixtures/README.md` states **why** quiet cases exist and points at the marks; it names no fixture's cases and carries no list | met | The five bullets and `leak-check`'s hand-written counts are gone. Judged against the **whole** file, which is what found the `broken-parked-task` row naming a quiet case in the `broken-*` table - §3 step 8. That case is now marked and the cell states the defect alone |

**What this does not settle.** The reading is complete against what T-198 *names* only for the seven
fixtures marked. Three cases in two fixtures outside this task's agreed scope are unmarked and
carried by [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md); the
sixteen `broken-*` fixtures' cross-fixture silence is
[T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)'s and closed. And the
reader matches a value named as a quoted string or as a section number - a class naming one some
third way would pass a mark unearned, which its own docstring states.

**This closes finding F-2 of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)**, whose first criterion that
record puts as *not met*. Re-judging it is that audit's own review work and is **not** covered by
the grant below, which the owner confined to these six tasks on 2026-08-22.

**Open questions, re-read before closing.** §1 recorded none outstanding: the one it had was
answered by the owner on 2026-08-22 and folded into the outcome, the scope and the last criterion.
Nothing in §3 raised a question for the owner - the one thing that could have, whether to widen the
scope to two more fixtures, is [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) rather than a question.

**Child fix tasks raised**
- [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) - the three cases T-198 names in the two fixtures this task's scope excludes

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised as finding F-2 of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), which is why that audit's first criterion is not met. `medium` and `s`: the mechanism exists twice in this repository already, and what it buys is that the audit above becomes repeatable instead of being a reading of a document. A child of T-198, which does not close until this resolves (`audit.md` step 5). |
| 2026-08-22 | (no change) | **The open question is answered by the owner: the markers are authoritative, and `tests/fixtures/README.md` keeps a short note on why quiet cases exist that points at them.** Asked in the batched round of 2026-08-22. The set is then read from the tree, so a quiet case added next week is in the next sweep with nothing edited anywhere — which is the whole of F-2. *Rejected: markers only, deleting the prose*, one home and no possible drift, but a marker tells a test what to do and does not tell a newcomer why the case is there. *Rejected: the README stays authoritative*, no change for its existing readers, but the set stays hand-written and the defect this task removes survives. This row is the answer, not authorisation to start. |
| 2026-08-22 | → specified | **Specify agreed.** The owner's answer of the same date is folded into the outcome, the scope and the last criterion, so the record states the decision where the work is judged rather than only where it was asked. **One criterion is sharpened rather than restated.** It read *finds every case T-198 examined by hand*, and that audit's record **names more cases than it exercised** — fifteen exercised, beside `keep-me`, `section-reference`'s two unmutated marks and `wide-table-row`'s short row, the last of which [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) had to add after the fact. A marking that reproduced the fifteen would have passed the old wording while dropping exactly the cases this task exists to make findable. **No total is written into the criteria**: a count derived by hand here would be this task's own defect one level up, so the criterion names the set by rule and asks for the two counts to be stated together. Phase stays at `specify` — `plan` is not authorised (METHOD §3.1). **A finding raised while checking those counts is [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md)**, and it is why the criterion above could not simply cite T-198's figures. |
| 2026-08-22 | → done | **All five criteria met; 26 quiet cases now read from the tree across 7 fixtures.** The marks are the authority and no document holds the set. **Three things this run found that the plan did not**: the reader's first version silently dropped the two marks whose values carry hyphens, so it gained a partition assertion that every mark-word line is parsed or named - a reader cannot report its own incompleteness; the first inert-mark comparison measured a working tree against a `git archive` copy and read the `Scope` line's git branch as a difference; and judging the README criterion against the **whole** file rather than the section just edited found a quiet case named in the `broken-*` table, so the marking reaches a sixth fixture no plan step named. **The residual is [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)**, not a widened scope: T-198 names three cases in two fixtures outside the five agreed at `specify`, and the grant authorises phases rather than answers. **This closes F-2 of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)**; re-judging that audit's first criterion is its own review work and the owner confined the grant to these six tasks. `check` OK over 211 tasks, index regenerated, 317 tests passed against 310 before. |
| 2026-08-22 | → in_progress | **Implement started; steps 1 and 2 done and measured.** Four marker forms were run against scratch copies of the fixtures. **A trailing `<!-- -->` on a table row creates the defect it marks** - `wide-table-row` went from 3 problems to 4, the comment being a further cell - so no single universal form survives, and the mark goes on the line that carries the case in that line's own comment syntax. **The front-matter form was checked for the failure that would not show**: a marked value is no longer a bare date, so the case could have gone silent for the wrong reason; putting a malformed date on the marked line fired exactly as the unmarked one did, so the silence is still the real date's doing. A mark on its own line was rejected against a mark on the section heading even though `check` cannot tell them apart - adjacency binding breaks with nothing to report it. **Steps 3-9 are not run and §3 says so**; nothing below step 2 is claimed. |
| 2026-08-22 | → planned | **Plan written under the multi-phase grant recorded above.** Nine steps. **Step 1 is the marker form and it is first because it can invalidate the rest**: these fixtures are live taskmd projects whose tests assert exact line numbers and exact counts, so a mark on its own line shifts them and a mark appended inside a table row is a further cell — which is three of `wide-table-row`'s quiet cases. **The deliverable's shape is decided with its rejections**: marks in the fixtures, a reader in `tests/`, a shortened README note; a manifest file was rejected because adding a quiet case would then need two writes, which is this task's own defect one file over, and extending `check` was rejected because it would ship a test-fixture concept to every adopter. **A residual is named in the plan rather than absorbed**: T-198's record names quiet cases in `migrated-away` and `planned-deliverable`, neither of which is among the five fixtures §1's scope covers, so step 4 states the difference and raises a task instead of widening scope the owner agreed. Phase stays at `plan` until `implement` runs. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it is the head of the chain and the grant stops at its own closure.** Closing it resolves the last open child of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), whose closure would in turn resolve [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md)'s. Neither is covered — see the limit above, which was put to the owner as this exact case. |
