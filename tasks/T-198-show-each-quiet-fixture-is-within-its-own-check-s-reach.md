---
id: T-198
title: Show each quiet fixture is within its own check's reach
type: audit
status: review
phase: review
parent: T-191
blocked_by: []
related: [T-150, T-151]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-198 — Show each quiet fixture is within its own check's reach

## 1. Specify

**Outcome**
For every fixture a test asserts a class is silent about, a statement of whether **that fixture** is
within **that check's** reach — shown by mutating the fixture so it ought to trip, and quoting what
arrived. Each fixture that cannot be made to trip becomes its own child task.

**Why this one**
Finding **F-2** of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md).
That audit proved every class **can** speak, by planting each one's defect in a tree where a test
asserts silence. It did not prove that each **particular quiet fixture** is somewhere the check can
see — and those are different claims.

**They came apart once already, which is why this is worth doing rather than assuming.**
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) found a `WIDE ROW`
negative fixture that could not fire at all: the check consumed the line under the header as a
delimiter, so the fixture sat outside its reach while the class itself worked perfectly elsewhere. A
class-level exercise — which is exactly what T-191 ran — cannot see that, and would have passed
`WIDE ROW` on the day T-150 was raised.

**Why T-191 did not simply do this.** Its criteria are written per class (*each has a quiet case*,
*each can fire*), and it met them. Widening to per fixture is more work than those criteria ask for,
so the audit recorded the distinction as a finding rather than quietly doing extra and leaving the
next reader unable to tell which claim had been tested. That is the same rule
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) states, applied to the
audit itself.

**Scope**
- In: every fixture named by a must-not-catch assertion, and the trees the bespoke quiet tests build
  inline. The set is read from the tests, not from a list in a document
- In: for each, whether mutating it trips the class it is asserted silent about
- Out: **repairing any fixture found out of reach.** A finding is never fixed where it is found
  (METHOD §5); each is a child task
- Out: re-deriving the class set, which is
  [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md)'s and is recorded
  there
- Out: the cross-fixture `LABELS` list, which is
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)'s

**Inputs**
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) §3 — the class table,
  and which quiet case belongs to which class
- [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) — the worked instance
  of a fixture out of reach
- `tests/fixtures/` and `tests/test_cli.py`

**Acceptance criteria**
- [ ] The fixture set is derived from the tests and the derivation is shown, so a quiet case added
      since cannot be missing
- [ ] Every fixture has a row; the rows sum to the derived set
- [ ] Each *is in reach* claim quotes the alarm that arrived when the fixture was mutated; a fixture
      not mutated is recorded as unproven rather than as passing
- [ ] **The instrument is shown able to produce a positive result before any negative one is
      believed** — T-191's own first run reported every class silent because it never invoked
      `check`, and that is the failure mode this task is most exposed to
- [ ] Every fixture out of reach is a child task, and this audit closes only when each resolves

**Open questions**
- none

## 2. Plan

**What counts as a finding** (`audit.md` step 2, fixed before looking). A quiet case is a finding if
**it cannot be made to fire** — the state it is asserted silent about, planted in that same fixture,
produces no alarm. A case that speaks on demand is recorded as checked and produces no work. How good
the case is, or whether it is worth having, is outside the threshold.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the fixture set from the tests, and say what the derivation misses rather than assuming it misses nothing. | The derived set, its size, and its known gaps. |
| 2 | For each quiet case, make a minimal edit that ought to make it fire, run `check`, and diff the alarms against the same fixture unedited. | One alarm line per case, quoted. |
| 3 | Prove the instrument can produce a positive before believing any negative. | A run where most cases fire. |
| 4 | Record every case, exercised or not; a case not mutated is *unproven*, never *passing*. | The table. |
| 5 | Raise a child task per finding. Fix nothing. | The child tasks. |

**Sequencing.** Step 3 is not a step so much as a condition on step 2 — T-191's instrument reported
every class silent while never invoking `check`, and this task is exposed to exactly that. The diff
against the unedited fixture is the guard: an alarm only counts if it is **new**.

**Decisions**

- **Each case is exercised by editing the fixture, never the check.** The one exception is the
  front-matter case, whose whole claim is about a guard in `check_wide_rows` — there the guard is
  removed on a copy of the code and put back, which is the only way that case can be made to speak.
- **The instrument is scratch and is not shipped.** What it does by hand is what
  [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) would make repeatable.

**Outputs**

- `tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md` (§3)
- one task file per finding

## 3. Implement

### Step 1 — two derivations, neither of which is the set

**From the tests**, parsing `tests/test_cli.py` for functions that assert a class silent and reading
the fixtures they name:

```text
fixtures named by a must-not-catch assertion: 21
  broken-cancelled-deliverable, broken-config, broken-cycle, broken-dangling, broken-deliverable,
  broken-derived-field, broken-duplicate-id, broken-id-width, broken-link, broken-missing-blocker,
  broken-parked-task, broken-stale-index, broken-tasks-dir-root, broken-template-field,
  broken-unreachable-template, broken-vocabulary, label-shaped-value, malformed-date,
  migrated-away, planned-deliverable, section-reference
```

**It is demonstrably incomplete.** `abandoned-slot` and `wide-table-row` both carry quiet cases and
appear in neither line, because their quiet tests iterate the fixture directory or build a tree —
so no fixture name appears as a literal for a parser to find. That is the same miss T-191 made one
level up, and it is why criterion 1 is recorded **not met** rather than approximately met.

**From `tests/fixtures/README.md`**, which names five fixtures *shaped* to carry the defect and the
cases that must stay silent beside it: `wide-table-row`, `abandoned-slot`, `label-shaped-value`,
`malformed-date`, `section-reference`. That is the set this audit examined, and it is **prose** — a
classification somebody wrote, not a fact the tree states. Raised as
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md).

### Steps 2–3 — fifteen cases, each edited so it ought to speak

Every line below is the alarm that was **not** there before the edit, on the same fixture.

```text
open task holding a slot it has not reached    IN REACH ABANDONED SLOT ...T-002-open-and-has-not-reached-the-section.md body line 20 still reads '- <
closed record quoting a slot inside a fence    IN REACH ABANDONED SLOT ...T-003-closed-and-quoting-a-slot-to-explain-it.md body line 11 still reads '
a real date beside a malformed one             IN REACH MALFORMED DATE T-001...: created is '2026-08-99', which is shaped like a date and is not one
a real date written without zero padding       IN REACH MALFORMED DATE T-002...: created is '2026-8-45', which is shaped like a date and is not one
an ordinary date inside a list                 IN REACH MALFORMED DATE T-002...: windows is '2026-08-45', which is shaped like a date and is not one
a real three-part version                      IN REACH LABEL SHAPE  shipped_in: '0.4' on 1 task(s) reads as a version
a three-part version inside a list             IN REACH LABEL SHAPE  targets: '1.4' on 1 task(s) reads as a version
a quantity in an exempt estimate field         IN REACH LABEL SHAPE  duration: '1.5' on 1 task(s) reads as a version
a citation that resolves                       IN REACH SECTION REF  docs/handbook.md has no section 7; 1 reference(s) name it
a wrong citation quoted inside a fence         IN REACH SECTION REF  docs/handbook.md has no section 404; 1 reference(s) name it
a wrong citation inside a code span            IN REACH SECTION REF  docs/handbook.md has no section 404; 1 reference(s) name it
a trailing cell with nothing in it             IN REACH WIDE ROW      ...T-002...:35 has 3 cells against a 2-column header
an escaped pipe, which is content              IN REACH WIDE ROW      ...T-002...:41 has 3 cells against a 2-column header
a table inside a fence                         SILENT   (nothing new named 'T-002')

13 of 14 quiet cases shown able to fire
```

**The fifteenth is the front-matter case, and it needs the code moved rather than the fixture.** Its
claim is that a `|`-separated front-matter menu is not a table because no front-matter line is a
delimiter row. Removing that guard on a copy of `cli.py`:

```text
with the delimiter guard removed, T-002 reports 1 line(s):
   WIDE ROW      tasks/T-002-three-rows-that-lose-nothing.md:7 has 5 cells against a 2-column header
restored - T-002 lines now: 0
```

So **[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md)'s fix is
load-bearing and proven**, and the fixture's prose claim about it — which nothing had ever run — is
true.

**The instrument produced thirteen positives before its one negative was believed**, and each alarm
is diffed against the unedited fixture so a pre-existing line cannot be read as a new one. It also
refuses any run whose output contains a traceback, which is the failure T-191 met.

### Step 4 — the table

| Fixture | Quiet cases examined | In reach |
| :--- | ---: | :--- |
| `abandoned-slot` | 2 | both |
| `malformed-date` | 3 | all three. A fourth — `keep-me`, a value that is not date-shaped — cannot be made to fire without becoming date-shaped, which is the class itself; recorded as **true by construction**, not as exercised |
| `label-shaped-value` | 3 | all three |
| `section-reference` | 3 | all three. Two further marks — a sub-number resolving against a list item, and a mark with no document beside it — were not mutated and are **unproven** |
| `wide-table-row` | 4 | three, plus the front-matter case via the code guard. **One not in reach** → F-1. *Annotated 2026-08-21 by [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md): the fixture carries a **fifth** quiet case this audit did not reach, and the count of 4 is what was examined rather than what is there — see below the table* |
| The other 16 fixtures of the derived 21 | — | **not exercised.** Their quiet cases are the cross-fixture `fails()` silence, which [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) exercised per class and this task did not exercise per fixture. Recorded as unproven. *Annotated 2026-08-22 by [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md): 16 is the count of `broken-*` fixtures, not of the derived fixtures this audit did not examine, which is 18 — two are covered by no row at all, see below the table* |

**Annotation, 2026-08-21 — `wide-table-row`'s fifth quiet case, added by
[T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md).** This audit examined
four and the fixture carries five; the fifth was substituted out rather than counted, so it appeared
in the list above as neither proven nor unproven. `tests/fixtures/README.md` said *five* at the time
and nothing compared the two. The five, each with what is known:

| # | Quiet case | Status |
| :-- | :--- | :--- |
| 1 | A trailing cell with nothing in it | **in reach**, exercised above |
| 2 | An escaped pipe, which is content | **in reach**, exercised above |
| 3 | A table inside a fence | not in reach when this audit ran → F-1 → [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md), which repaired the fixture on 2026-08-21 |
| 4 | A `\|`-separated front-matter menu | **in reach**, proven by removing the delimiter guard on a copy of `cli.py` |
| 5 | **A short row, which Markdown pads** | **True by construction**, and **its line is shown in reach.** A short row cannot be made to speak while staying short — the only mutation is to add a cell, which turns it into the class — so it is `keep-me`'s twin and is *not* counted among the fifteen exercised. Unlike `keep-me` its reach was measured: giving line 47 a fourth cell reports `has 4 cells against a 3-column header`, so the silence is the row's shortness and not the check failing to read that table |

**The totals above do not move, and that is the point of the row 5 classification.** Fifteen cases
exercised, thirteen positives, one silence: the fifth case joins `keep-me` and
`section-reference`'s two unmutated marks in the set this record names *outside* the exercised count.

**A sixth candidate was considered and is not a case.** The fixture's last table — *And a real table
after the fence, which is read* — is the fenced case's **control**, there to show the skip ends;
counting it would make every correct table in the repository a quiet case. Its reach was measured
anyway rather than argued: widening its row reports `tasks/T-002-...:67 has 3 cells against a
2-column header`.

**Annotation, 2026-08-22 — two members of the derived twenty-one are covered by no row, added by
[T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md).** The table above gives five fixtures a row each and the remainder one row reading *the
other 16*. **Only three of the five are members of the twenty-one**: `wide-table-row` and
`abandoned-slot` are the two this audit *names* as missed by the derivation, in the paragraph above
the table, so they cannot also be subtracted from it. The remainder is **18** — and 16 is not a slip,
it is a number that is right about something else, being exactly the count of `broken-*` fixtures in
the derived list. So `5 + 16 = 21` balances, while `migrated-away` and `planned-deliverable` appear
once in this whole record — inside the derived list — and in no row.

The partition, recomputed by parsing this record's own two lists rather than by retyping them:

| Row | Members | Count | Status |
| :--- | :--- | ---: | :--- |
| Examined **and** derived | `label-shaped-value`, `malformed-date`, `section-reference` | 3 | exercised above |
| Examined, **not** derived | `wide-table-row`, `abandoned-slot` | 2 | exercised above; these are the derivation's two known misses |
| Derived, not examined — the `broken-*` set | the sixteen `broken-*` fixtures | 16 | unproven, as the last row of the table says |
| Derived, not examined — **not** `broken-*` | `migrated-away`, `planned-deliverable` | 2 | unproven, and **previously covered by no row** |

3 + 16 + 2 = 21 derived, with the 2 examined-but-not-derived sitting outside that set, which is what
*the derivation misses two* means. **A double-counted member is invisible in a total**, which is why
the audit's own second criterion caught nothing: two different sets of size five made the sum read
correctly.

**Neither of the two is described by the row that should have held them.** That row says the
unexercised set's quiet cases are the cross-fixture `fails()` silence. Both of these are named by an
assertion of their own:

- **`planned-deliverable`** — `MISSING OUTPUT` must not fire on an **open** task declaring a path
  that is not there. `test_an_open_task_declaring_a_path_that_does_not_exist_passes` asserts exit 0
  and no `MISSING OUTPUT`. It is the positive half of T-089's pair, `broken-deliverable` being the
  negative.
- **`migrated-away`** — **two** quiet cases rather than one.
  `test_a_link_that_resolves_is_not_reported` asserts exactly one `BROKEN LINK` and no report of
  `notes.md`; `test_it_reports_a_document_defect_it_used_to_refuse_to_look_for` asserts **no**
  `CONFIG ERROR`, on a fixture where `index` and `context` still report one.

**Neither is exercised here and neither changes status** — both move from *absent* to *unproven*,
which is where the other sixteen already sat. Mutating them is the question this audit declined to
ask of any of the eighteen, and [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md) does not reopen it.

### Findings

**F-1 — `wide-table-row`'s fenced-table case cannot fire.** Its row has two cells against a
two-column header, so it is not wide. Unfenced it stays silent; unfenced with a genuinely wide row it
reports. The silence the fixture records is produced by the row's width and not by the fence, so a
regression in fence skipping would not be caught here — and the exact-count test would not move
either. **This is T-150's defect, in T-150's own fixture, one case over.** →
[T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md). Severity: medium.

**F-2 — the quiet-case set cannot be computed.** Step 1's two derivations answer different questions
and neither is the set: the parser finds 21 and misses two fixtures it should have found; the README
names five and is prose. A sixth fixture given a quiet case next week is in neither. →
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md). Severity: medium, and it is
why criterion 1 below is not met.

### Recorded as examined, no action

- **`malformed-date`'s `keep-me`** — a value that is not date-shaped. Making it fire would mean making
  it date-shaped, which is the class rather than the case. True by construction, and stated so rather
  than counted as a pass.
- **The front-matter case** — in reach, proven by removing the guard. It is the case T-150 built and
  it works.

**Decisions & assumptions**

- **An alarm counts only if it is new** — every run is diffed against the same fixture unedited.
  Rejected: reading the alarm list after the edit, which counts a fixture's own pre-existing defect
  as evidence for a case beside it — 2026-08-21.
- **Criterion 1 is recorded not met rather than approximately met — rationale: the derivation has two
  known misses and I can name them, so calling it derived would be the exact failure this audit
  reports in F-2.** Rejected: widening the parser until it happened to find the two, which fits the
  answer to the known cases and tells you nothing about the unknown one — 2026-08-21.

**Outputs produced**

- this record
- [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md)
- [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The fixture set is derived from the tests and the derivation is shown, so a quiet case added since cannot be missing | **not met** | The derivation is shown and it is shown to miss: 21 found, `abandoned-slot` and `wide-table-row` absent though both carry quiet cases, because their tests name no fixture literally. A quiet case added since **can** be missing → **[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)** |
| Every fixture has a row; the rows sum to the derived set | met | §3 step 4: five fixtures examined case by case, and one row covering the other sixteen of the derived twenty-one as unexercised. 5 + 16 = 21, and the two the derivation missed are named above it. *Annotated 2026-08-22 by [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md): the sum balances on a coincidence — only three of the five examined are members of the twenty-one, so the remainder is eighteen and `migrated-away` and `planned-deliverable` are covered by no row. This verdict is left as written; the corrected partition is in §3* |
| Each *is in reach* claim quotes the alarm that arrived when the fixture was mutated; a fixture not mutated is recorded as unproven rather than as passing | met | Fifteen alarm lines quoted, each diffed against the unedited fixture. The unexercised sixteen, two unmutated `section-reference` marks, and `keep-me` are each recorded as unproven or true-by-construction — none as passing |
| **The instrument is shown able to produce a positive result before any negative one is believed** | met | Thirteen positives arrived before the one silence was read as a finding, and the silence was then confirmed by a second trial: unfenced-as-is stays silent, unfenced-and-widened reports. The instrument also refuses any run whose output holds a traceback — T-191's failure, guarded against by name |
| Every fixture out of reach is a child task, and this audit closes only when each resolves | **carried** | One case out of reach → [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md); the derivation gap → [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md). Both open, so **this umbrella stays open** — the criterion being met, not deferred |

**What this audit is worth, stated plainly.** It examined the five fixtures a document points at, and
found one real defect in them — a case that has never been able to fire, in the fixture built to fix
exactly that. It did **not** examine the other sixteen, and it cannot promise there is not a sixth
fixture nobody has classified. Those two limits are F-2 and the reason criterion 1 fails; recording
them is worth more than a fuller-looking table would have been.

**Open questions, re-read before closing.** §1 recorded none.
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) carries one of its own —
whether marks replace the README's prose or sit beside it — written into that record where a view
will show it.

**Child fix tasks raised**
- [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) — F-1, the fenced-table case that cannot fire
- [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) — F-2, the quiet-case set that cannot be computed

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **§3's partition and §4's second verdict annotated by [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md), which closed the same day.** Two members of the derived twenty-one — `migrated-away` and `planned-deliverable` — were covered by no row of the step-4 table, and the row that should have held them says **16** where the derived-and-unexamined set is **18**. The 16 is exactly the count of `broken-*` fixtures, so `5 + 16 = 21` balanced and the audit's own second criterion, which asks that the rows sum to the derived set, was marked met on it — only three of the five examined are members of the twenty-one. The corrected partition is a table below step 4, and both fixtures' quiet cases are named there from the assertions that state them, because the row they fell into describes the unexercised set as the cross-fixture `fails()` silence and neither is a `broken-*` fixture. **Nothing this audit said it did has been rewritten** (METHOD rule 5): the row keeps its 16, the verdict keeps its wording, and both carry a pointer. **Neither fixture was exercised** — they move from absent to unproven, where the other sixteen already sat. **This umbrella still does not close**: [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) remains open (`audit.md` step 5). |
| 2026-08-21 | (no change) | **§3 annotated by [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md), which closed the same day.** The fifth quiet case is now named with what is known about it, the step 4 table row says its 4 is what was examined rather than what is there, and a sixth candidate is recorded as considered and rejected with its reach measured. **The totals are unchanged and shown to be** — fifteen exercised, thirteen positives — because the fifth case is true by construction and joins `keep-me` outside that count. Nothing this audit said it did has been rewritten (METHOD rule 5). **This umbrella still does not close**: [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) remains open (`audit.md` step 5). |
| 2026-08-21 | (no change) | **A third child was raised against this record, so the two named in §4's last row are no longer the whole of what gates closure.** [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md), from [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md)'s run: this audit counted **four** quiet cases for `wide-table-row` and the fixture carries **five** — the short row named by the test's own docstring is in neither the case list nor the table, so it is recorded as neither proven nor unproven. It was shown in reach on a copy, so the omission is in this record and not in the fixture. §4's verdict rows are left as written: they state what this audit did, and annotating the past is what METHOD rule 5 asks for instead. [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) closed the same day; [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) and [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) are open, so this umbrella stays open (`audit.md` step 5). |
| 2026-08-21 | → review | **Fifteen quiet cases exercised across five fixtures; fourteen in reach, one not.** [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md): `wide-table-row`'s fenced table has two cells against a two-column header, so unfencing it reports nothing and the case cannot catch the regression it exists for - T-150's defect in T-150's own fixture. [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md): criterion 1 is **not met** - the derivation finds 21 fixtures and misses two it should have found, so a quiet case added since can still be missing. **Stays open**: `audit.md` step 5 gates closure on both children. |
| 2026-08-21 | → proposed | Raised as finding F-2 of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md). Typed `audit` rather than `fix` because it examines a body of fixtures for a problem nobody has alleged of any particular one, and its findings become children (METHOD §5). `m`: the condition means mutating each fixture, not reading it. A child of T-191, which does not close until this resolves (`audit.md` step 5). |
