---
id: T-212
title: Report a closed parent that still has an open child
type: fix
status: done
phase: review
parent: null
blocked_by: [T-216]
related: [T-209, T-191, T-198, T-219]
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

- ~~**None.** The scope is the residual T-209 named while answering its own criterion.~~
  **Superseded on 2026-08-22, before `plan` began** — the question below was found by measuring this
  repository rather than by reading the rule, and it decides what the class means.

- **Does a child hold *every* parent open, or only an audit umbrella? — the project owner.**
  §1 above cites [`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 5 as the rule this
  class enforces. That step reads *"Close the **umbrella** only when every child is resolved"*, and an
  umbrella is an **audit's** umbrella task. The class as scoped would report every closed parent.

  **The two readings are not equivalent here, and this repository is the evidence.** Run against the
  live tree, the proposed class fires **three** times, and not one parent is an audit:

  | Parent | type | Open child | type |
  | :--- | :--- | :--- | :--- |
  | [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) | `deliverable` | [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) | `deliverable` |
  | [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) | `research` | [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) | `research` |
  | [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) | `deliverable` | [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) | `research` |

  All three are the same shape: a task finished its own work and left a residual that is parked on an
  external condition. **The tool's own model says they are defects** — `cli.py`'s `holds_open()`
  states that the derived side of a hierarchy edge is the only side that holds a task open, without
  qualifying it to audits. **The method's written rule says they are not**, because it names the
  umbrella.

  **Neither reading is free:**

  - *Every parent.* The three above are real defects and must be repaired before this class can ship,
    because five tests in `tests/test_cli.py` assert `check --root ROOT` exits 0 — so a class that
    fires here turns the suite red rather than merely reporting. The natural repair is **not** to
    reopen three finished tasks but to move those children from `parent` to `related`, which is what
    this project already does for a residual: [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)
    raised its two on 2026-08-22 with `parent: null` and a `related` edge.
  - *Audit umbrellas only.* The class must then read `type: audit`, which is **project vocabulary**
    rather than method vocabulary, so it needs a config key — and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
    shows a new key errors every adopter's config on upgrade. The class fires zero times on this
    repository, so it would also ship with no live case.

  **This is not a plan question and it cannot be assumed away.** It decides the class's meaning, its
  shipped behaviour, whether three records in this repository are wrong, and whether the suite can be
  green with it. The grant on this record authorises phases and not answers, so it was put to the owner.

  **Answered by the project owner on 2026-08-22: a child holds *every* parent open.** Not only an
  audit umbrella. Three consequences, and none of them is a plan detail: the class is a **problem**
  rather than an advisory; it needs no `type` filter and therefore no config key; and the three cases
  above are **real defects in this repository** →
  [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), raised on the same
  instruction and not covered by this record's grant. The two readings that were rejected are priced
  in §2's shape decision, where the alternatives to a rejected choice belong.

## 2. Plan

**The question above is answered, and the answer is what this plan is built on.** The owner settled
on **2026-08-22** that a child holds **every** parent open, not only an audit umbrella. So the class
is a **problem** rather than an advisory, it needs no `type` filter and therefore no config key, and
the three cases in this repository are real defects →
[T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), which this task now
waits on.

**Sequencing.** Step 1 is first because it is the failing-first evidence *and* the step that can
invalidate the rest: if the fixture cannot hold the defect and both quiet cases in one project, the
shape of steps 2–4 changes. Step 6 is placed before the gates rather than after them because the
counts it corrects are prose that a green run does not read — the way this addition goes wrong
silently is by leaving *seventeen checks* and *twelve checks* behind where they are now eighteen and
thirteen.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the fixture — one closed parent with an open child, plus the two cases that must stay silent: a closed parent whose children are all closed, and an **open** parent with an open child. Write the test that asserts the class is reported, run it, and record it **failing** before any check exists. | The fixture under `tests/fixtures/`, the test in `tests/test_cli.py`, and the failing run quoted in §3 |
| 2 | Name the class and write the check. The name answers to `tests/classes.py`'s derivation, so it must be a `problems.append("<NAME> ...` literal in the shape `PROBLEM_PREFIX_RE` reads; the message names the parent, its status and the open child. | `check_closed_parent_open_child` in `cli.py`, registered in `cmd_check`, and a decision in §3 naming the class with the rejected names and why |
| 3 | Run `check` on the fixture. It must report **exactly one** problem, of the new class, and be silent on both quiet cases. | The run quoted in §3, beside step 1's failing run |
| 4 | Mark the two quiet cases in the fixture, in the form `tests/test_quiet_cases.py` defines, and read them back. The reach assertion is satisfiable here because the firing case is in the same fixture — which is the property [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md) records `planned-deliverable` as lacking. | The marks, and the `--list` reading quoted in §3 |
| 5 | Confirm every other fixture is asserted silent about the new class. `tests/test_cli.py` reads the class set from `tests/classes.py`, so this should follow with no edit — **verify it rather than assume it**, by checking the new name appears in the derived set and that the per-fixture silence assertion covers it. | The derived set printed in §3, and a statement of which assertion covers the new class |
| 6 | Judge each shipped binding's *cannot occur* statement against the new class, and correct every count the addition falsifies. Known: `cmd_check`'s docstring says *twelve checks open a task file*; `github-issues.md` says *seventeen checks run on the local backend*. Both are prose the addition makes wrong. | Each binding's judgement recorded in §3 with its reason, the edited regions, and every corrected count named |
| 7 | Run `check` on this repository. It must be clean — which needs [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) closed, since until then the class reports three real records here and five tests in `tests/test_cli.py` assert exit 0. | The run quoted in §3 |
| 8 | Run the binding's *after any write*, run the suite, and sweep what this change made stale. | `index`, `check` and suite output in §3, and every document the sweep touched named |

**Shape of the deliverable, decided — 2026-08-22.** A **problem** class in `cli.py`, one **fixture**
carrying the defect and both quiet cases, and **rows in the shipped documents that enumerate
classes**. *Rejected: an advisory*, which would keep this repository green without T-216 and was
offered to the owner as one of three readings on 2026-08-22; it was not chosen, and it would report
as advice a state the method forbids. *Rejected: scoping the class to `type: audit`*, also offered
and not chosen — it needs project vocabulary, so a config key, and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
records that a new key errors every adopter's config on upgrade.

**Not planned past its horizon.** Step 1 decides whether one fixture can carry all three cases; if it
cannot, steps 2–4 are re-cut and this table is edited in place rather than guessed at now.

**Outputs** — plain paths, because none of them exists yet:

- plugin/skills/taskmd/taskmd/cli.py
- plugin/skills/taskmd/docs/bindings/github-issues.md
- plugin/skills/taskmd/docs/bindings/local-markdown.md
- tests/fixtures/ — one new fixture directory, named at step 1
- tests/test_cli.py

## 3. Implement

**Step 1 — the fixture, and the class failing before it existed**

`tests/fixtures/broken-closed-parent/` carries all three cases in one project, which is what step 1
was placed first to find out: T-001 `done` with T-002 open under it (the defect), T-003 `done` with
its only child T-004 also `done` (quiet), and T-005 `in_progress` with T-006 open under it (quiet).
One fixture holds them, so steps 2–4 were not re-cut.

Two tests were written and run **before any check existed**:

```text
$ python -m pytest tests/test_cli.py -q -k "closed_while_a_child or two_cases_the_closed_parent"
E       AssertionError: 1 != 0 : OK - 6 task(s), 30 field value(s), 33 front-matter value(s), ...
FAILED tests/test_cli.py::CheckFailsOnEveryClassItClaims::test_closed_while_a_child_is_still_open
FAILED tests/test_cli.py::CheckFailsOnEveryClassItClaims::test_the_two_cases_the_closed_parent_check_must_not_catch
2 failed, 172 deselected in 0.33s
```

The `OK -` in the failure message is the evidence that matters: `check` read the fixture, found the
defect entirely legible, and reported nothing.

**Step 3 — the same fixture once the check existed**

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/broken-closed-parent
CLOSED PARENT T-001 is 'done' with child T-002 still open

1 problem(s) - 6 task(s), 30 field value(s), 33 front-matter value(s), 3 reference(s), 0 dependency edge(s), 0 declared output(s), 0 index file(s), 3 closed record(s), 6 document(s), ...
EXIT=1
```

**Exactly one problem**, of the new class, naming the pair that is wrong — and silent on T-003 and
T-005, the two that must not fire.

**Step 4 — the marks, read back**

```text
$ python tests/test_quiet_cases.py --list
29 quiet case(s) in 27 mark(s), across 9 fixture(s):
  ...
  broken-closed-parent    2 case(s) in 2 mark(s)
```

**Step 5 — the cross-fixture silence assertion, verified rather than assumed**

```text
$ python -c "import sys; sys.path.insert(0,'tests'); import classes; c=sorted(classes.check_classes()); print(len(c)); print('CLOSED PARENT' in c)"
22
True
```

`tests/test_cli.py`'s `CheckFailsOnEveryClassItClaims.LABELS` **is** `sorted(check_classes())`, and
its `fails()` helper asserts every label but the fixture's own is absent from that fixture's output.
So every `broken-*` fixture is now asserted silent about `CLOSED PARENT` with no edit anywhere —
which is what T-197 built the derivation for, and the suite below is the run that exercises it.

**Decisions & assumptions**

1. **The class is `CLOSED PARENT`** — 2026-08-22. It names the record at fault. **Rejected:
   `OPEN CHILD`** — the child is in a perfectly ordinary state and is not the record to repair, so a
   class named for it sends a reader to the wrong file. **Rejected: `HIERARCHY`** — it names the edge
   kind rather than the state, and `STORED DERIVED` is already about edges, so the two would read as
   variants of one thing.
2. **The message names both ids bare and quotes the status** — 2026-08-22 — which is
   `NO BLOCKER`'s shape exactly (`%s is '%s' with ...`), and the family convention throughout
   `cli.py`: ids bare, values quoted.
3. **The check reads the *derived* side of the hierarchy edge** — 2026-08-22 — the same side
   `holds_open()` names, so a project that renames `parent` or `children` in its config needs no edit
   here. Both ends are looked up in `tasks`, so a dangling edge stays `DANGLING`'s to report rather
   than being reported twice under two names.
4. **The two quiet marks carry no declared value, and `tests/test_cli.py` carries the real
   assertion** — 2026-08-22. This is a limit worth stating plainly rather than leaving for a reader
   to discover. `tests/test_quiet_cases.py` assertion 2 matches a value written as `'<value>'`; this
   class writes ids bare, so **assertion 2 cannot bite on it** — the limit that module's own
   docstring states under *What this cannot see*. Assertions 1 and 3 do bite: the class is one
   `check` can print, and it fires elsewhere in the same fixture. The non-vacuous form of the
   silence is `test_the_two_cases_the_closed_parent_check_must_not_catch`, which asserts the
   **exact firing set** — one alarm, naming T-001 and T-002, with neither quiet parent in it.
5. **The counts the addition falsified were deleted, not corrected** — 2026-08-22. `cmd_check`'s
   docstring said *twelve checks open a task file* and `github-issues.md` said *seventeen checks run
   on the local backend*. **Rejected: bump them to thirteen and eighteen** — the next class to be
   added would falsify them again, which is exactly the drift `tests/test_publishing.py` records as
   policy (T-188): *a count of one of these sets is either dated as a measurement or not written at
   all*. Each place now says what it means without a number and says why the number went.
   **One count was deliberately left**: `github-issues.md`'s blockquote is explicitly *measured
   2026-08-18*, which is the exemption that policy names, and editing it would rewrite what a record
   says about the past (METHOD rule 5).
6. **Each shipped binding judged, and they came out differently** — 2026-08-22.
   *`local-markdown.md`*: its declaration is *nothing cannot occur here*, and that survives — a file
   marked `done` beside an open file naming it as `parent` is two ordinary files. The judgement is
   written into the declaration rather than left to be re-derived. *`github-issues.md`*: the class
   **can** occur, because GitHub lets you close a parent issue with a sub-issue still open, so it does
   **not** join the four in the `cannot-occur` region. Its coverage table gains a row saying so and
   admitting that no row of the procedure looks for it — a declared gap, which is what
   [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 asks for. Writing a procedure row would
   need a run against a real backlog, the standard every row there is held to, and that is not this
   task's scope.
7. **The fixture is named in `tests/fixtures/README.md`** — 2026-08-22 — because
   `tests/test_publishing.py` asserts every fixture directory is named there, and it failed on the
   first full run. Recorded because it is the kind of step a plan does not think to include.

**Step 7 — `check` on this repository**

```text
$ ./plugin/bin/taskmd check
OK - 218 task(s), 1090 field value(s), 3673 front-matter value(s), 721 reference(s), 25 dependency edge(s), 331 declared output(s), 1 index file(s), 208 closed record(s), 250 document(s), 3298 link(s), 4734 table row(s), 2 template(s), 10 template field value(s), 5 vocabulary row(s), 3694 section reference(s)
EXIT=0
```

Clean, and it is clean **because**
[T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) closed first. Run
before that repair, this class reported three real records here and would have turned five tests in
`tests/test_cli.py` red, which is why the dependency was recorded as an edge rather than as a
sentence.

**Step 8 — the suite, and the sweep**

```text
$ python -m pytest tests -q
327 passed, 8 subtests passed in 44.14s
```

325 before, 327 after: the two tests of step 1. Swept for what the addition made stale, by searching
every shipped document for a written-out number of checks:

```text
$ grep -rn -iE "\b(twelve|thirteen|...|twenty-two)\b" README.md docs/ plugin/ --include=*.md
```

Every remaining hit is either a dated measurement or about something else — slot lines, spurious
angle-bracket matches, published documents. The two that were about this set are handled in decision
5. No marked region enumerates the problem classes, and that is deliberate rather than an omission:
`tests/test_publishing.py` records that `README.md` describes one class without claiming to describe
them all, so a region there would assert something the document does not mean.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py)
- [`plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
- [`plugin/skills/taskmd/docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)
- `tests/fixtures/broken-closed-parent/` — six task files
- [`tests/fixtures/README.md`](../tests/fixtures/README.md)
- [`tests/test_cli.py`](../tests/test_cli.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The class is shown **failing first**, on a committed fixture holding exactly one such defect | met | §3 step 1. Two tests run before the check existed, both failing, and the failure message carries `check`'s own `OK -` line on the fixture — the defect fully legible and nothing reported. The fixture holds one defect and two quiet cases |
| It is shown **not** to fire on a closed parent whose children are all closed, and not on an open parent with an open child — both quiet cases marked in the fixture so `tests/test_quiet_cases.py` reads them | met | §3 step 3 shows exactly one alarm, naming neither. Step 4 shows the reading holding both marks. **§3 decision 4 states which of that module's three assertions can bite on this class and which cannot**, and names the test that carries the part it cannot |
| The class appears wherever the shipped documents enumerate classes, derived rather than hand-listed where a derivation exists — `tests/classes.py` is the one home for the set | met | §3 step 5: the derivation returns 22 and includes it, with no edit to `tests/classes.py`. No shipped document enumerates the problem classes — checked, and §3 step 8 records why that is by design |
| Each shipped binding's *cannot occur* statement is judged against the new class, since `BINDING.md` §4 requires every binding to name what its backend makes impossible | met | §3 decision 6, one judgement each and they differ: `local-markdown` keeps *nothing cannot occur* and now says why for this class; `github-issues` judges that it **can** occur, so it stays out of the four, and declares that no row of its procedure looks for it |
| `check` is clean on this repository afterwards, or the tasks it names are real | met | §3 step 7, exit 0 — and clean because T-216 closed first, which is what the dependency edge was for |

**What review found beyond the table.** The mark syntax in `tests/test_quiet_cases.py` **cannot carry
a declared value that begins with a capital letter**: its class pattern is `[A-Z][A-Z ]*[A-Z]`, so
`quiet: CLOSED PARENT T-003 - ...` parses the class as `CLOSED PARENT T` and the value disappears.
It failed loudly rather than silently — assertion 1 reported an unknown class — but it reported the
*class* as wrong when the class was right, which is a diagnostic that sends a reader to the wrong
place. Raised as [T-219](T-219-let-a-quiet-mark-declare-a-value-that-begins-with-a-capital.md) rather
than fixed here.

**Open questions, re-read before closing** (`review` step 5). §1's one question was answered by the
owner on 2026-08-22 and is recorded there with both readings; it produced T-216 and T-218, both now
closed. Nothing is addressed to anyone else.

**Child fix tasks raised**
- none. The one finding is a soft-linked task —
  [T-219](T-219-let-a-quiet-mark-declare-a-value-that-begins-with-a-capital.md) — because this
  task's outcome is complete without it (`METHOD.md` §4).

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | All five criteria met. `CLOSED PARENT` is class 22, shown failing first on `tests/fixtures/broken-closed-parent/` and then reporting exactly one alarm there, silent on both cases it must not catch. Unblocked by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), which is why `check` is clean here. Two counts the addition falsified were **deleted rather than corrected**, per the policy in `tests/test_publishing.py` (T-188). One finding went to [T-219](T-219-let-a-quiet-mark-declare-a-value-that-begins-with-a-capital.md). **Worked under the multi-phase grant recorded at the top of this Log.** |
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **This row supersedes the *set and its bounds* in the rows below** — the grant as first given (six) and its first extension (seven). It does **not** supersede the limit specific to this task, which is stated below and still binds. |
| 2026-08-22 | (no change) | **The grant was extended to a seventh task, later the same day.** The **project owner** added [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) to the six named in the row below, on the same terms and after reading why it was raised. **The set now in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). The row below records the instruction as first given — six ids — and its *what it does not cover* clause is amended by exactly this one addition. [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) remains outside it, as does every task waiting on the owner. Nothing else changes: it still authorises **phases, not answers**. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that wrote the handoff carrying this work forward, that **six tasks** — [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) — be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the six — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply; nor [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), raised the same day and after the instruction was given. **The set is six ids and not a description** — it was asked for as *all six tasks which does not need me*, and T-217 already makes that description name seven, so the ids are what bind. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its `blocked_by` on [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) is real and not a formality.** Plan step 7 needs `check` clean on this repository, and until those three records are repaired the class reports them, which turns five tests in `tests/test_cli.py` red. So that task closes first. Its `specify` question was answered by the owner on 2026-08-22 and the plan is written against that answer — do not re-open it. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that raised this task, that [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) and [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the two — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), raised the same day and not named; nor [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) or [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), whose closure the earlier grant of the same date already confined away from. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it adds a check class, so it owes the two things a class owes here.** A committed fixture holding exactly one defect, shown failing first; and a judgement of every shipped binding's *cannot occur* statement against the new class, which `plugin/skills/taskmd/docs/BINDING.md` §4 requires and `tests/test_publishing.py` reads. Its quiet cases mark themselves, per [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md). |
| 2026-08-22 | proposed → blocked | Question answered by the **project owner** on 2026-08-22 - a child holds **every** parent open - and the plan written against it. The class is a problem, not an advisory, and needs no config key. **Blocked on [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md)** rather than merely waiting on it: step 7 needs `check` clean on this repository, and until those three records are repaired the class reports them, which turns five tests in `tests/test_cli.py` red. T-216 was raised on the owner's own instruction and is **outside this record's grant**, which names T-211 and T-212 and no other task - so this task stops at the end of `plan`. |
| 2026-08-22 | (no change) | **Stopped at an open question before `plan`, under the grant recorded above.** Measuring this repository rather than reading the rule showed the class as scoped would fire three times here, on parents that are `deliverable` and `research` and not one of them an audit - while the rule §1 cites, `audit.md` step 5, is written about an audit's **umbrella**. So the class's meaning is unsettled, and with it whether three records here are wrong. It is not a plan detail: five tests assert `check` is clean on this repository, so a class that fires here turns the suite red rather than reporting. The grant authorises phases and not answers, so no plan was written. The question, both readings and what each costs are in §1. |
| 2026-08-22 | → proposed | Raised from [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) while answering that task's fourth criterion — *whether `check` reports it too* — by building the case and running it rather than reasoning about it. The answer for the **open** parent is no: an umbrella with an open child is the ordinary state of every audit mid-flight, and reporting it would make a healthy backlog noisy. The **closed** parent is the opposite and returns `OK`, quoted in §1. Raised rather than folded into T-209 because it is a new validator class with a fixture and coverage rows, not a change to what a derived line says — a different size and a different set of things to get right. `medium` and `s`: the rule, the edge and the derivation all exist, so this is a reader for data already there. |
