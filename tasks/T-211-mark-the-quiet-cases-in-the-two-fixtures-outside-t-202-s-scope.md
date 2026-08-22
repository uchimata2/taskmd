---
id: T-211
title: Mark the quiet cases in the two fixtures outside T-202's scope
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-202, T-198, T-210]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - tests/test_quiet_cases.py
  - tests/fixtures/migrated-away/docs/notes.md
---

# T-211 — Mark the quiet cases in the two fixtures outside T-202's scope

## 1. Specify

**Outcome**
`migrated-away` and `planned-deliverable` carry marks for the quiet cases
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)'s record names in them, so
the reading `tests/test_quiet_cases.py` produces covers every case that record names rather than
every case inside one document's list.

**Why this one**
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) made the marks the authority
for the quiet-case set, and its agreed scope was **the five fixtures `tests/fixtures/README.md`
named**, plus `leak-check`. Those five were the set because that document was the thing being
dethroned as the authority.

**Three cases named by T-198 are outside that five**, added to its record on 2026-08-22 by
[T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md):

| Fixture | Quiet case | Named by |
| :--- | :--- | :--- |
| `planned-deliverable` | `MISSING OUTPUT` must not fire on an **open** task declaring a path that is not there | `test_an_open_task_declaring_a_path_that_does_not_exist_passes` |
| `migrated-away` | exactly one `BROKEN LINK`, and no report of `notes.md` | `test_a_link_that_resolves_is_not_reported` |
| `migrated-away` | **no** `CONFIG ERROR`, on a fixture where `index` and `context` still report one | `test_it_reports_a_document_defect_it_used_to_refuse_to_look_for` |

Until they are marked, the reading is short by three against what T-198 names, and the difference is
carried by prose in T-202's §3 — which is the shape F-2 exists to remove, one document over.

**Scope**
- In: marking those three cases in the two fixtures, in the form
  `tests/test_quiet_cases.py` defines
- In: re-stating the two counts in that module's reading, so the difference against T-198 closes or
  is explained by something other than scope
- Out: **exercising them.** Neither fixture has been mutated to show its cases in reach, and T-198
  declined that for all eighteen of its unexercised set. Marking is not exercising, and the reach
  assertion the reader already makes — that the class fires somewhere in the same fixture — is what
  will judge them
- Out: the sixteen `broken-*` fixtures, whose quiet case is the cross-fixture `fails()` silence
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) owns and closed

**Inputs**
- `tests/test_quiet_cases.py` — the mark's form, its anchors and its three assertions
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3, the corrected
  partition below step 4 — where the three cases are named, with the assertion that states each
- [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) §3 step 4 — the
  reconciliation this task closes

**Acceptance criteria**
- [ ] The three cases are marked, and the reading names them
- [ ] The reading's count and the count T-198 names are stated together, and either agree or differ
      for a reason that is **not** "one fixture was out of scope"
- [ ] `migrated-away`'s `CONFIG ERROR` case is marked or is recorded as unmarkable with the reason —
      `CONFIG ERROR` is excluded from the derived class set by name in `tests/classes.py`, so a mark
      naming it fails the reader's first assertion, and that is a real constraint rather than an
      oversight to work around

**Open questions**
- **None.** The scope is the residual T-202's plan named; nothing here is new ground.

## 2. Plan

**Sequencing.** Step 1 is first because it decides how many of the three cases this task actually
marks, and so whether steps 2 and 3 have one row each or three. §1's *Out: exercising them* already
names the judge — the reader's own assertions — and **two of the three cases have a visible reason to
fail one of them before anything is run**: `CONFIG ERROR` is subtracted from the derived class set by
name in `tests/classes.py`, which is what assertion 1 reads; and `check` on
`tests/fixtures/planned-deliverable` returns `OK` with no `MISSING OUTPUT` line anywhere, which is
what assertion 3 looks for. Neither is measured until step 1, because a visible reason is not a
result — and the third criterion's constraint was written into `specify` from exactly such a reading.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Put each of the three marks in place, one at a time, and run `python tests/test_quiet_cases.py`. Record which assertion judges each case and what it said. Revert every mark the run rejects, so the tree carries only what step 2 keeps. | A table in §3, one row per case: the mark as written, the assertion that judged it, and the **run output** rather than an argument |
| 2 | Keep the marks step 1 admits, in the form the module already defines — a trailing `#` inside front matter, a trailing HTML comment on a body heading. | The marks, in the fixture files |
| 3 | For each case step 1 rejects, record it as unmarkable **with the measured reason**, and decide whether its repair is work this scope excludes. Where it is, raise a task; where the reason is in-principle rather than scope, say so and raise nothing. | The reasons in §3, and a new task for any rejected case whose repair is real work outside this scope |
| 4 | Decide how the module's reading states itself against the count [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) names, and write it. The constraint that decides the form: a hand-written total is a derived value and decays, which is the shape F-2 exists to remove one document over. | The edited `tests/test_quiet_cases.py`, and a decision in §3 naming the form with each rejected alternative and its reason |
| 5 | Read again and quote the reading before and after, so the three cases' arrival is visible rather than asserted. | Both `--list` readings in §3 |
| 6 | Run the binding's *after any write*, run the suite, and sweep what this change made stale — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) §3 step 4's reconciliation table is the first place to look, because it names this task as the residual of its own last two rows. | `index`, `check` and suite output in §3, and every document the sweep touched named |

**Shape of the deliverable, decided — 2026-08-22.** Two parts: **marks inside the two fixtures**, and
an **edit to `tests/test_quiet_cases.py`** carrying the reconciliation. *Rejected: putting the
reconciliation in this record only*, which is where T-202 put its own and is why that table now reads
as prose naming a task rather than as a state — §1 puts the re-statement in the module's reading for
that reason. *Rejected: a third artifact holding the named-versus-marked comparison*, which would be
the manifest T-202 already rejected, one level up: a case added tomorrow would then mean editing the
case, the reading and the comparison.

**Not planned past its horizon.** Step 1 determines whether step 3 raises one task, two, or none, so
the plan does not invent that detail now. Step 4's form is likewise a decision that step takes rather
than one this table pre-empts.

**Outputs** — plain paths, because none of the edits exists yet:

- tests/fixtures/migrated-away/docs/notes.md
- tests/fixtures/planned-deliverable/tasks/T-001-x.md
- tests/test_quiet_cases.py
- this record
- a new task for any case step 1 rejects whose repair is outside this scope, if step 3 confirms one

## 3. Implement

### Step 1 — each mark put in and run, one at a time

**The judge is the reader, not an argument** — §1's *Out: exercising them* says so. Each mark was
written, `python tests/test_quiet_cases.py` was run, and the mark was reverted before the next.

| Case | Verdict | What the run said |
| :--- | :--- | :--- |
| `migrated-away` — `BROKEN LINK` | **marked** | `Ran 7 tests` / `OK`. `check --root tests/fixtures/migrated-away` was identical before and after — `1 problem(s)`, `2 link(s)`, `2 table row(s)` — so the mark is invisible to the tool, which is the constraint T-202 settled the form against |
| `planned-deliverable` — `MISSING OUTPUT` | **refused by assertion 3** | `AssertionError: [] is not true : planned-deliverable marks a case quiet for MISSING OUTPUT and nothing in that fixture reports MISSING OUTPUT, so the silence may be the check not reaching it rather than the case` |
| `migrated-away` — `CONFIG ERROR` | **refused by assertions 1 and 3** | `AssertionError: 'CONFIG ERROR' not found in {...}` — the class set is derived and does not hold it; **and** the same reach failure as the row above |

**The `CONFIG ERROR` case fails on two independent grounds, where §1 anticipated one.** Its third
criterion names the class-set exclusion; the reach assertion refuses it as well, because `check` is
silent about that class on that fixture by construction — it never gets to report one there.

### Step 2 — the one mark that holds

`tests/fixtures/migrated-away/docs/notes.md`, on the heading, so it covers the whole document:

```text
migrated-away/docs/notes.md   line 1   BROKEN LINK   the file is there, so the whole document is
quiet for this class and the fixture cannot pass by reporting every link
```

Assertion 3 is satisfied from inside the same fixture: `docs/guide.md -> plan.md` is the firing
direction, and it is the reason this fixture can carry a marked quiet case at all.

### Step 3 — the two that do not, and where the work went

Neither is recorded as *out of scope*, which §1's second criterion rules out as a reason:

- **`CONFIG ERROR` is refused in principle.** `cli.py` prints it from the config loader before any
  check runs, so it is not a class `check` owns and cannot be one a fixture is asserted silent
  about. No task raised — there is nothing to do. This is the outcome §1's third criterion
  describes.
- **`MISSING OUTPUT` is refused by a limitation of the reader.** `planned-deliverable` is the silent
  half of the pair [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md)
  built and `broken-deliverable` is the firing half, so a **per-fixture** reach assertion cannot see
  the direction that would earn the mark. Making the fixture fire on its own would make it a second
  `broken-deliverable` and destroy the pair, which is why it is not done here →
  [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md).

### Step 4 — how the reading states its own residual

`NAMED_AND_UNMARKED` in `tests/test_quiet_cases.py`: one row per refused case, each carrying the
reason, and **three assertions that run the reasons rather than read them** —
`test_neither_named_case_is_marked`, `test_the_config_error_row_is_refused_by_the_derived_class_set`
and `test_the_missing_output_row_is_refused_by_reach`. `listing()` prints the rows under the reading.

**Each of the three was shown failing on a case it should catch**, which is the half of METHOD's
`implement` criterion that a green run cannot supply:

```text
marking a named case         FAIL test_neither_named_case_is_marked
                             ('planned-deliverable', 'MISSING OUTPUT') unexpectedly found in {...}
the reach reason lapses      FAIL test_the_missing_output_row_is_refused_by_reach
                             Lists differ: [] != ["T-001 declares 'out/report.md', which does not exist"]
the class-set reason lapses  FAIL test_the_config_error_row_is_refused_by_the_derived_class_set
                             'CONFIG ERROR' unexpectedly found in {..., 'CONFIG ERROR', ...}
```

**The third took three attempts, and the first two failures are the useful part.** Emptying
`NOT_A_CHECK_CLASS` left the assertion green; so did turning `cli.py`'s `print("CONFIG ERROR ...")`
into a `problems.append`. Only both together put the class into the set. The reason is that
`PROBLEM_PREFIX_RE` reads `problems.append` sites and `CONFIG ERROR` is a bare `print`, so the union
never holds it and **the subtraction removes nothing today** — a guard for a world one edit away,
with nothing saying so →
[T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md). The
row's stated reason was corrected to the operative mechanism once measured; it had named the
subtraction, which is not what keeps the class out.

### Step 5 — the reading, before and after

```text
before   26 quiet case(s) in 24 mark(s), across 7 fixture(s)
after    27 quiet case(s) in 25 mark(s), across 8 fixture(s)
           migrated-away         1 case(s) in 1 mark(s)
           (no fixture)          2 case(s) named by T-198 and not marked - reasons below

Named by T-198 and not marked - the reading is short by 2, and not because a fixture was out of scope:
  migrated-away          CONFIG ERROR    no CONFIG ERROR, on a fixture where index and context still report one
  planned-deliverable    MISSING OUTPUT  MISSING OUTPUT must not fire on an open task declaring a path that is not there
```

### Step 6 — gates and sweep

```text
Wrote tasks/README.md - 10 active, 205 closed
OK - 215 task(s), ... 247 document(s), 2963 link(s), ... 3558 section reference(s)
325 passed, 8 subtests passed in 44.59s
```

322 before, 325 after: the three new assertions. **`check` earned its place mid-task** — it caught a
link in [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md)
pointing at a T-089 filename that had been guessed rather than resolved, which is exactly the failure
this project's note about citing another record's id describes.

**The sweep found one stale home and one that only looked like one.**
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) §3 step 4's table says
`migrated-away −2` and `planned-deliverable −1`, both deferred here; it is **annotated, not
rewritten**, because it is a closed record of what that task measured on the day it ran (METHOD rule
5). `tests/fixtures/README.md` names both fixtures and needed nothing: it already refuses to hold the
case list and points at the module, which is F-2's repair working as intended. `control/`'s two
mentions of *migrated-away* are the project class in T-175, not the fixture.

**Decisions & assumptions**

- **The residual is held in the module as data with asserted reasons, not as prose** — rationale: a
  reason nobody runs is the shape F-2 exists to remove, and both of these reasons are mechanical, so
  they can be run. *Rejected: a sentence in the docstring*, which is what T-202's table already is
  and is why this task exists. *Rejected: a hand-written total for what T-198 names*, because a count
  is a derived value that decays, and T-198 is still open so its record can still move — 2026-08-22.
- **The mark sits on `notes.md`'s heading rather than on the link line** — rationale: the whole
  document is quiet for `BROKEN LINK`, and the heading form already exists in `broken-parked-task`.
  *Rejected: an inline comment on the link line*, which would put an HTML comment mid-sentence in a
  fixture whose prose is written to be read — 2026-08-22.
- **Assumed: a refused mark is a result to report, not a scope to widen** — the grant on this task
  authorises phases and not answers, and §1 puts exercising these fixtures out by name. Recorded as
  an assumption because it is what makes the first criterion honestly not met rather than worked
  around — 2026-08-22.

**Outputs produced**

- `tests/fixtures/migrated-away/docs/notes.md`
- `tests/test_quiet_cases.py`
- [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md)
- [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md)
- an annotation on [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) §3 step 4

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The three cases are marked, and the reading names them | **not met** | **One of three is marked.** `migrated-away`'s `BROKEN LINK` case holds; the other two are refused by the reader itself, on runs quoted in §3 step 1. The second half of the criterion *is* met — the reading names all three, the marked one in the listing and the other two in `NAMED_AND_UNMARKED` with their reasons. The `CONFIG ERROR` half is governed by criterion 3 below and is met there; the live gap is `planned-deliverable` → **carried by [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md)** |
| The reading's count and the count T-198 names are stated together, and either agree or differ for a reason that is **not** "one fixture was out of scope" | met | The listing prints `27 quiet case(s) in 25 mark(s), across 8 fixture(s)` and, beneath it, `the reading is short by 2, and not because a fixture was out of scope`, with each case and its reason. Neither reason is scope: one is in-principle, one is a limitation of the reader. **Read as: *the count of cases T-198 names that this reading does not hold*.** Under the other available reading — T-198's absolute total, 22 at T-202's step 4 — this is **not** met, and deliberately: a hand-written total is a derived value that decays, T-198 is still open so its record can still move, and §3 records that rejection. Flagged rather than resolved here, because choosing between the two readings is the owner's |
| `migrated-away`'s `CONFIG ERROR` case is marked or is recorded as unmarkable with the reason | met | Recorded as unmarkable, with **two** measured reasons where §1 anticipated one: it is not a class `check` owns, so assertion 1 refuses it; and `check` is silent about that class on that fixture by construction, so assertion 3 refuses it too. Held in `NAMED_AND_UNMARKED` with the first reason asserted by `test_the_config_error_row_is_refused_by_the_derived_class_set`, which was shown failing. The criterion said to record it rather than work around it, and the class set was not touched |

**Open questions** — §1 states none, and none arose. Two discoveries were routed to tasks rather than
left as questions, because both are actionable by whoever picks them up:
[T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md) and
[T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md). **One
thing is put to the owner and is not a blocker**: criterion 2's two readings, above.

**Child fix tasks raised**

- [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md) —
  carries criterion 1's live gap
- [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md) —
  raised from `implement`, not from a failed criterion

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that raised this task, that [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) and [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the two — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), raised the same day and not named; nor [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) or [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), whose closure the earlier grant of the same date already confined away from. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its third criterion may be unmeetable and that is a legitimate outcome.** `CONFIG ERROR` is excluded from the derived class set by name in `tests/classes.py`, so a mark naming it fails `tests/test_quiet_cases.py`'s first assertion. The criterion already says to record that with the reason rather than work around it, and the grant does not license changing the class set to make a mark fit. |
| 2026-08-22 | review → done | Reviewed and closed. **Two criteria met, one not met and carried** by [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md). The task's outcome as §1 states it is partly reached and the record says which part: one of the three named cases is marked, and the other two are held in the reading with reasons that are asserted rather than described. **Closing with a visible gap rather than a widened scope** is what the grant on this record allows - it authorises phases, not answers, and §1 puts exercising these fixtures out by name. One matter is put to the owner and blocks nothing: criterion 2 has two readings, met under one and not under the other, and §4 states both with the reason the stricter one was not built for. |
| 2026-08-22 | planned → review | Implemented. **One of the three cases is marked; two are refused by the reader and neither refusal is scope.** `migrated-away`'s `BROKEN LINK` case holds. `CONFIG ERROR` is refused in principle - it is not a class `check` owns - which is the outcome §1's third criterion describes. `planned-deliverable`'s `MISSING OUTPUT` is refused by the reach assertion, because this fixture is the silent half of a **pair** and the firing half is `broken-deliverable`, where a per-fixture assertion cannot see it → [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md). **Two things were found that `specify` did not anticipate and neither was absorbed**: the `CONFIG ERROR` case fails on two grounds rather than one, and `tests/classes.py`'s `NOT_A_CHECK_CLASS` subtraction removes nothing today → [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md). The second was only found because METHOD requires a new check be shown failing, and the first two attempts to break one left it green. |
| 2026-08-22 | proposed → planned | Plan written under the owner's 2026-08-22 multi-phase grant recorded above. **Step 1 measures before steps 2–3 commit**, because two of the three cases carry a visible reason to fail one of the reader's assertions: `CONFIG ERROR` is subtracted from the derived class set by name in `tests/classes.py` (assertion 1), which §1's third criterion already anticipated; and `check --root tests/fixtures/planned-deliverable` returns `OK` with no `MISSING OUTPUT` line at all, so assertion 3 — *the class fires somewhere in the same fixture* — has nothing to find. **The second of those was not anticipated at `specify`** and is recorded here rather than absorbed: §1's *Out: exercising them* names that assertion as the judge of these marks, so a mark it rejects is a result this task reports, not a scope to widen. Step 3 decides whether the repair is a task; nothing is raised in advance of the measurement. |
| 2026-08-22 | → proposed | Raised from [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)'s plan step 4, which named the residual before implement met it. T-202's scope is the five fixtures `tests/fixtures/README.md` named, because that document was the authority being replaced; T-198's record names three quiet cases in two fixtures outside that five, added by [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md) on the same date. Raised rather than absorbed into T-202: widening a scope the owner agreed at `specify` is the owner's, and the grant on those six tasks authorises phases and not answers. `xs` because the mechanism exists and this is applying it; `medium` because until it lands the reading's difference against T-198 is carried by prose, which is the shape F-2 exists to remove. **The third criterion may turn out to be unmarkable**: `CONFIG ERROR` is excluded from the derived class set by name, so a mark naming it fails the reader's first assertion — recorded here so `specify` meets it rather than `implement`. |
