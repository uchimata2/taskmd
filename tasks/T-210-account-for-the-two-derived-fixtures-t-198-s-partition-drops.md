---
id: T-210
title: Account for the two derived fixtures T-198's partition drops
type: fix
status: done
phase: review
parent: T-198
blocked_by: []
related: [T-202, T-204]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: no
deliverables: [tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md]
---

# T-210 — Account for the two derived fixtures T-198's partition drops

## 1. Specify

**Outcome**
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)'s step-4 table accounts for
every member of the fixture set it derived. `migrated-away` and `planned-deliverable` are covered by a
row, the count in the row covering the unexercised fixtures is true of the set it names, and the
record says why its second criterion read as **met** while two members had no row at all. Nothing the
audit said about the past is rewritten — the correction is an annotation, as
[T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md)'s was.

**Why this one**
Found on 2026-08-22 while [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)'s
specify checked the figures its own criterion cited. T-198 derives **21** fixtures from the tests and
examines **5**; its step-4 table gives the five a row each and the remainder one row reading *the
other 16 fixtures of the derived 21*. That sum is quoted in §4 as the evidence for criterion 2.

**Only three of the five examined are members of the twenty-one.** `wide-table-row` and
`abandoned-slot` are the two the derivation is *shown* to miss — the audit names them as missed, in
the paragraph above the table — so they cannot also be subtracted from it. The unexamined remainder is
**18**, not 16.

**16 is not a slip of arithmetic; it is a number that is right about something else.** It is exactly
the count of `broken-*` fixtures in the derived list. So `5 + 16 = 21` balances, the row's own
description — *their quiet cases are the cross-fixture `fails()` silence* — is true of the sixteen it
accidentally names, and `migrated-away` and `planned-deliverable` fall out of the accounting
entirely. They appear once in the whole record, inside the derived list, and in no row.

**A double-counted member is invisible in a total**, which is why the audit's own criterion caught
nothing: two different sets of size five are what make the sum read correctly. This is
[T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md)'s class one level up —
that task counted a *case* the fixture carried and the audit did not, this one covers a *fixture* the
derivation carried and the table does not.

**Scope**
- In: annotating T-198 so every member of its derived 21 is covered by exactly one row, and the count
  in the unexercised row is true of the set that row names
- In: saying what `migrated-away` and `planned-deliverable` carry, since the existing row describes
  the unexercised set as the cross-fixture `fails()` silence and neither is a `broken-*` fixture
- In: an annotation on §4's criterion-2 verdict recording what the sum concealed
- Out: **exercising either fixture.** Both belong in the unexercised bucket and stay in it; mutating
  the unexamined set is what T-198 declined to do for all of them, and it is not reopened here
- Out: **rewriting any verdict or table row as it was written.** METHOD rule 5 — correct what a
  record says about the present, annotate what it says about the past
- Out: re-deriving the fixture set, which is
  [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)'s
- Out: T-198's closure, gated on its children (`audit.md` step 5) and not this task's to move

**Inputs**
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 step 1 for the derived
  list, step 4 for the table, and §4 for the verdict that rests on the sum
- [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) — the precedent for how
  this record is annotated rather than rewritten
- `tests/fixtures/README.md` — what `migrated-away` and `planned-deliverable` actually are

**Acceptance criteria**
- [ ] Every member of T-198's derived 21 is covered by exactly one row of its step-4 table, shown by
      listing the members against the rows rather than by asserting a total
- [ ] The unexercised row's count is the number of derived fixtures not examined, and **the two
      coincident fives are named** — so a reader meeting the corrected number can see what made the
      old one look right, and cannot re-make it
- [ ] `migrated-away` and `planned-deliverable` are described by what they carry, not by the
      `broken-*` characterisation they inherited by falling into that row
- [ ] §4's criterion-2 verdict carries an annotation and its original wording is unchanged
- [ ] `check` is clean and the suite passes

**Open questions**
- **None.** The finding is arithmetic and the repair shape is settled by
  [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md)'s precedent on this
  same record.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the partition from T-198's **own record** — parse the derived list out of its fenced block and the examined set out of its step-4 table rows — and name every member no row covers. | The membership listing, quoted in §3. |
| 2 | For each uncovered fixture, read what its quiet case actually is from the assertion in `tests/test_cli.py` that names it. | One line per fixture, naming the test and what it asserts is silent. |
| 3 | Annotate §3 step 4 of T-198: give the two a row, correct the count in the unexercised row, and name the two coincident fives that made the old one balance. | The annotation, below the step-4 table. |
| 4 | Annotate §4's criterion-2 verdict, leaving its wording as written. | The annotation, in the verdict row's note. |
| 5 | Run `index`, `check` and the suite. | Their output, in §3. |

**Decisions**

- **The instrument parses T-198's record; it does not retype it.** A hand-typed copy of the
  twenty-one is the defect this task reports, one level down — the same reasoning
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) applied to the class
  list, and the reason step 1 reports the declared count and the parsed count together.
- **Neither uncovered fixture is exercised.** The scope forbids it, and the reason is that this task
  corrects an accounting: both belong in the unexercised bucket and their evidential status does not
  change by being named in it. Mutating them would make this an audit and would answer a question
  T-198 declined to ask of any of the eighteen.

**Outputs**

- `tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md` (§3 step 4, §4)

## 3. Implement

### Step 1 — the partition, parsed from T-198's own record

The derived list is read out of the fenced block that announces it, the examined set out of the
step-4 table's rows. Nothing is retyped, so the listing cannot agree with the record by accident:

```text
derived declared / parsed : 21 / 21
examined rows             : 5 -> abandoned-slot, malformed-date, label-shaped-value,
                                 section-reference, wide-table-row

examined AND derived      : 3
examined NOT derived      : abandoned-slot, wide-table-row
derived NOT examined      : 18  <- the row says 16
broken-* in derived       : 16

COVERED BY NO ROW         : migrated-away, planned-deliverable

mentions in the whole record:
  migrated-away            1
  planned-deliverable      1
```

**The declared count and the parsed count are printed together**, so a parser that silently found
fewer than the record claims would be visible rather than convincing. One mention each is the whole
of the finding: both appear inside the derived list and nowhere else in a 200-line record.

### Step 2 — what the two actually carry

Read from the assertions in `tests/test_cli.py` that name them, not from the row they fell into:

| Fixture | Its quiet case | Asserted by |
| :--- | :--- | :--- |
| `planned-deliverable` | `MISSING OUTPUT` must not fire on an **open** task declaring a path that is not there | `test_an_open_task_declaring_a_path_that_does_not_exist_passes` — exit 0, and `MISSING OUTPUT` absent |
| `migrated-away` | a link that **resolves** must not be reported | `test_a_link_that_resolves_is_not_reported` — exactly one `BROKEN LINK`, and no report of `notes.md` |
| `migrated-away` | `check` must not report the absent `tasks_dir` as a config error | `test_it_reports_a_document_defect_it_used_to_refuse_to_look_for` — no `CONFIG ERROR`, on a fixture where `index` and `context` still report one |

So `migrated-away` carries **two**, and neither fixture's silence is the cross-fixture `fails()`
silence that row ascribes to the unexercised set. That is criterion 3's substance: falling into a row
gave them a description nobody had ever checked against them.

### Steps 3–4 — the annotation

Three edits to `tasks/T-198-...md`, each appending and none replacing. The step-4 row keeps its `16`
and gains a pointer; a partition table below the table accounts for all 21 in four rows and names
both coincident fives; §4's criterion-2 verdict keeps its wording and gains a pointer. A Log row
records the lot.

### Step 5 — verification

```text
Wrote tasks/README.md - 12 active, 198 closed
OK - 210 task(s), ... 242 document(s), 2808 link(s), 4468 table row(s), ...
CHECK_EXIT=0
309 passed, 3 skipped, 6 subtests passed in 41.83s
```

**Decisions & assumptions**

- **The corrected count is stated in the annotation and the original row keeps its `16`** — rationale:
  METHOD rule 5 forbids rewriting what a record says about the past, and
  [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) set that precedent on
  this same table, keeping a count of 4 it had just shown to be 5. *Rejected: editing the row to read
  18*, which is the most literal reading of the criterion and would have made the record read as
  though the audit had always accounted for the two — destroying the only evidence that its second
  criterion was ticked on a coincidence — 2026-08-22.
- **The instrument parses the record; it does not retype it** — rationale: a hand-typed copy of the
  twenty-one is this task's own defect one level down. *Rejected: asserting the membership from the
  list already quoted in §1*, which would have proved my reading of the record rather than the
  record — 2026-08-22.
- **Neither fixture was exercised**, per the scope. They move from *absent* to *unproven*, which is
  where the other sixteen already sat, so no evidential claim changes — only the accounting.

**Outputs produced**
- `tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md` — the §3 step-4 row, the
  partition annotation below it, §4's criterion-2 note, and a Log row

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every member of T-198's derived 21 is covered by exactly one row, shown by listing the members against the rows rather than by asserting a total | met | The annotation's partition table has four rows; its three derived rows are 3 + 16 + 2 = 21, no member sits in two of them, and the membership was **parsed** from the record's own two lists rather than retyped. The listing is quoted in §3 step 1, declared count beside parsed count |
| The unexercised row's count is the number of derived fixtures not examined, and the two coincident fives are named | **met by annotation, not by edit** | Stated this way because the difference matters. The original row **still reads 16**, deliberately, and carries a pointer; the corrected **18** and both fives — five examined, five non-`broken-*` members of the twenty-one — are in the annotation below the table. The literal reading of this criterion is *edit the row*, and that was rejected under METHOD rule 5, with the rejection recorded in §3. A reader who wants the criterion's words met exactly will not find them met in the row |
| `migrated-away` and `planned-deliverable` are described by what they carry, not by the `broken-*` characterisation they inherited | met | §3 step 2, and the annotation: three quiet cases across the two, each named with the assertion that states it. `migrated-away` carries two, which the single row they fell into could not have shown |
| §4's criterion-2 verdict carries an annotation and its original wording is unchanged | met | The note is appended after the original sentence, which is byte-identical; the Result cell still reads `met`, because that is what this audit judged, and annotating the past is what rule 5 asks for instead of correcting it |
| `check` is clean and the suite passes | met | `CHECK_EXIT=0` on 210 tasks; `309 passed, 3 skipped, 6 subtests passed`. Quoted in §3 step 5 |

**Open questions, re-read before closing** (`review.md` step 5). §1 recorded none and none arose: the
finding was arithmetic, and its repair shape was settled by T-204's precedent on this same record.
Nothing here waits on the owner.

**What this task did not do.** It did not exercise either fixture, so neither is shown to be within
its own check's reach — which is the claim T-198 exists to make. Both are recorded *unproven*,
alongside the sixteen, and whether those eighteen are ever exercised is a question that stays exactly
where T-198 left it.

**Child fix tasks raised**
- none — every criterion is met, and the one met by a different mechanism than its words describe is
  recorded as such rather than quietly ticked

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised while working [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)'s specify, which cited T-198's counts and could not, because two members of the derived 21 are covered by no row of the table those counts describe. Typed `fix` and parented to T-198, matching [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md), the previous correction to this same record; it therefore gates T-198's closure like every other child (`audit.md` step 5). `medium` rather than `low`: T-204 corrected a count inside one row, and this one is a criterion marked **met** on a sum that balanced because two different sets both had five members. `s` — the repair is an annotation to one file, and the scope forbids exercising anything. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that raised this task: *"while you are working on these 6 task, new findings might raise, and I don't want you to skip them. Create those task item too"*, and *"execute the full lifecycle on them too."* **What it covers:** this task, raised as a finding while working one of the six named for that session, taken through specify → plan → implement → review in one run. **What it does not cover:** any other task, including the six themselves, which stay at one phase each; and it authorises **phases, not answers** — an open question belonging to the owner would still stop this record where it stands. Written here rather than in the session's handoff because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). This task records **no** open question, so the limit does not bind it. |
| 2026-08-22 | → done | **Full lifecycle in one run, under the authorisation recorded above.** T-198's step-4 partition now accounts for all 21 derived fixtures; `migrated-away` and `planned-deliverable` have a row, and the three quiet cases they carry are named from the assertions that state them rather than from the `broken-*` description they inherited by falling into the wrong row. **The original row and verdict are unchanged and both carry a pointer** — the row still reads 16, which is what keeps the coincidence visible to a reader. `check` exits 0 and the suite is `309 passed, 3 skipped`. One criterion is recorded **met by annotation, not by edit**, with the literal reading and its rejection in §3, because a criterion quietly satisfied by a different mechanism is the failure `review.md` names. T-198 stays open: [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) is still open (`audit.md` step 5). |
