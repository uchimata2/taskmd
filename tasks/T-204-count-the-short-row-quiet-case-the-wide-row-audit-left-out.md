---
id: T-204
title: Count the short-row quiet case the wide-row audit left out
type: fix
status: done
phase: review
parent: T-198
blocked_by: []
related: [T-201, T-202]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: [tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md]
---

# T-204 — Count the short-row quiet case the wide-row audit left out

## 1. Specify

**Outcome**
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 records `wide-table-row`
as carrying **four** quiet cases. It carries **five**, and the fifth — *A short row, which Markdown
pads* — appears nowhere in that record: not examined, not unproven, not true by construction. The
record names five and says what is known about each.

**Why this one**
Found while doing [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md), whose
scope reaches the fixture's fenced and quoted cases and stops there. The test asserting the fixture
silent names three quiet cases in its own words — blank excess, an escaped pipe and a short row
(`test_the_three_quiet_cases_are_quiet`). T-198 exercised blank excess and the escaped pipe, then
added the fence and the front matter and reached four. **The short row was substituted out rather
than counted.**

**It is already in reach, which is why this is small rather than why it should be dropped.** Measured
2026-08-21 on a copy of the fixture, by widening a row under that same three-column header:

```text
WIDE ROW      tasks/T-002-three-rows-that-lose-nothing.md:47 has 4 cells against a 3-column header
```

So the check reads that table, and the case is quiet because the row is short. Nothing is broken.
What is wrong is the record. T-198's third criterion requires a case that was not mutated to be
recorded as **unproven**; a case absent from the table is not recorded at all, which is the state
that criterion exists to prevent. And
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) will reconcile a computed set
against T-198's hand count, so a count that is one short is a discrepancy it has to spend work
resolving before it can trust either side.

**Scope**
- In: T-198 §3's case list and table, annotated so the fifth case is present with what is now known
- In: whether the other four fixtures T-198 examined case by case carry the same omission
- Out: **the mechanism** that would compute the set instead of counting it by hand, which is
  [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)
- Out: the fixture itself, which is correct and which
  [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) repaired

**Inputs**
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 steps 2–4 — the case
  list, the alarms and the table
- [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) §3 — where the omission
  was found, and the trial quoted above
- `tests/test_cli.py`, class `TableRowWiderThanItsHeader` — the docstring naming three quiet cases
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md`

**Acceptance criteria**
- [ ] T-198's record names five quiet cases for `wide-table-row`, each carrying what is known about
      it — proven, unproven, or true by construction
- [ ] The addition is written as an annotation: it says what was added and when, and does not rewrite
      what the audit said it did (METHOD rule 5)
- [ ] The other four fixtures T-198 examined are each stated as checked for the same omission
- [ ] The totals T-198 quotes elsewhere — fifteen cases, thirteen positives — are reconciled with the
      new count, or shown to be unaffected and why

**Open questions**
- none

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-run the reach measurement §1 quotes, rather than carrying it forward. A quoted output in a task reads as evidence and so nobody re-checks it. Diff against the unedited fixture, which is [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)'s own rule: an alarm counts only if it is new. | The alarm quoted from a run made here, or the finding that it does not arrive |
| 2 | Decide what is **known** about the fifth case against T-198's own standard — proven, unproven, or true by construction — and record what the other readings were. | The classification and its rejected alternative, in §3 |
| 3 | Check the other four fixtures for the same omission, **both directions**: every case `tests/fixtures/README.md` names appears in T-198's list, and every case in T-198's list appears in the README. A one-way sweep cannot report what it never looked for. | A row per fixture in §3, with both counts |
| 4 | Ask whether `wide-table-row` has a **sixth**. The fifth was missed by a count that summed; a corrected count that stops at five for the same reason has learned nothing. | The candidate named, and kept or rejected with the reason |
| 5 | Annotate T-198 §3 so all five are named with their status — as an annotation saying what was added and when, never a rewrite of what the audit said it did. | The annotation in T-198 §3 |
| 6 | Reconcile every total T-198 quotes, **found by searching that record** rather than from the two §1 remembers. | Each occurrence listed in §3, with whether it moved |
| 7 | Gates. | `taskmd index`, `taskmd check`, suite |

**Outputs this task will produce** (plain paths):
- tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md

## 3. Implement

### Step 1 — the measurement, re-run here

Run against a copy of the fixture, diffed against the same fixture unedited, refusing any output
holding a traceback — T-198's instrument, reused:

```text
unedited fixture, T-002 alarms: none

short row given a fourth cell        WIDE ROW  tasks/T-002-three-rows-that-lose-nothing.md:47
                                     has 4 cells against a 3-column header; Markdown drops the rest
                                     and that text renders nowhere
```

§1's quoted line said `:47 has 4 cells against a 3-column header` and the re-run agrees. Worth the
run rather than the carry-forward: a figure inside a specification reads as evidence, so it is the
one nobody checks.

### Step 2 — what is known about it

**D1 — true by construction, and its line shown in reach — 2026-08-21.** A short row cannot be made
to speak while staying short: the only mutation available adds a cell, and a row with more cells than
its header **is the class**. That is exactly the reasoning T-198 used to decline `malformed-date`'s
`keep-me`, so applying it differently here would make the audit's own standard depend on which case
it was pointed at. *Rejected: counting it as a fourteenth positive*, which the step 1 alarm would
support on a literal reading of "edited so it ought to speak" — the edit does not make the case speak,
it replaces the case. What the measurement **does** buy is stronger than `keep-me`'s, which was never
run: it rules out the silence being produced by the check not reading that table, which is precisely
the F-1 failure one case over in the same fixture.

### Step 3 — the other four fixtures, swept both directions

`tests/fixtures/README.md` is the classification T-198 examined against, so it is the other side of
the count. Every case it names, against every case T-198 listed:

| Fixture | README names | T-198 lists | Reconciles |
| :--- | ---: | ---: | :--- |
| `abandoned-slot` | 2 | 2 | yes — the slot in an open task, and the slot inside a fence |
| `label-shaped-value` | 3 | 3 | yes — a real version, a version inside a list, a quantity in the exempt estimate field |
| `malformed-date` | 1 | 3 + `keep-me` | yes, and T-198 counted **more** than the README named. The README's one — a date written without zero padding — is in T-198's three |
| `section-reference` | 5 | 3 exercised + 2 unproven | yes — one that resolves, a wrong citation in a fence, one in a code span, a sub-number against a list item, a mark nothing binds |
| `wide-table-row` | **5** | **4** | **no.** The omission this task exists for |

**D2 — the omission is in one fixture only, and the README already said so — 2026-08-21.** The other
four reconcile in both directions. The one that does not is the one where the README's own number was
five and T-198's was four, with nothing comparing them — which is [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)'s
finding arriving a second time, from the other end.

**Why the heading sweep does not generalise.** The fifth case was findable in `wide-table-row`
because that fixture names each case in a Markdown heading. The other four carry their cases in
front-matter values and task bodies, so there is no heading list to count — which is why step 3 used
the README rather than the trick that worked once.

### Step 4 — the sixth candidate

`wide-table-row`'s last table, *And a real table after the fence, which is read*. **Rejected as a
case, with its reach measured anyway** — 2026-08-21:

```text
table after the fence, row widened   WIDE ROW  tasks/T-002-three-rows-that-lose-nothing.md:67
                                     has 3 cells against a 2-column header
```

It is the fenced case's **control**: it exists to show the fence's skip ends, and it is quiet because
its row is not wide — which is true of every correct table in the repository. Counting it would make
the quiet-case set unbounded. Measured rather than argued, because a corrected count that stops
where the corrector's attention stopped is the failure this task was raised for.

### Steps 5–6 — the annotation, and every total reconciled

T-198 §3 gains a five-row table naming each quiet case with its status, the sixth candidate as
considered-and-rejected, and a line saying the totals do not move. The step 4 table's
`wide-table-row` row says its **4** is what was examined rather than what is there. Nothing the audit
said it did is rewritten (METHOD rule 5).

Every figure that record quotes, found by searching it rather than from the two §1 remembers:

| Where | Figure | Moves? |
| :--- | :--- | :--- |
| §3 steps 2–3 heading | "fifteen cases, each edited so it ought to speak" | no — the fifth was not edited |
| §3 step 3 code block | `13 of 14 quiet cases shown able to fire` | no |
| §3 after the block | "The fifteenth is the front-matter case" | no |
| §3 step 3 closing | "thirteen positives before its one negative was believed" | no |
| §4 criterion 3 | "Fifteen alarm lines quoted" | no |
| §4 criterion 4 | "Thirteen positives arrived" | no |
| Log, `→ review` row | "Fifteen quiet cases exercised across five fixtures" | no |

Seven occurrences, none moved — which is D1 doing its work: a case that is true by construction was
never in the exercised count, so correcting the record cannot disturb it.

**Outputs produced**
- `tasks/T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md` — §3's annotation, the
  step 4 table row, and a Log row

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| T-198's record names five quiet cases for `wide-table-row`, each carrying what is known about it | met | §3 steps 5–6: a five-row table in T-198 §3, one status per case — two exercised, one repaired by T-201, one proven through the code guard, and the fifth true by construction with its line shown in reach |
| The addition is written as an annotation: it says what was added and when, and does not rewrite what the audit said it did | met | Every insertion is dated and attributed to this task. The step 4 table keeps its **4** and gains a clause saying that is what was examined; §4's verdict rows are untouched |
| The other four fixtures T-198 examined are each stated as checked for the same omission | met | §3 step 3, a row each and **both directions** — README against T-198 and T-198 against README. All four reconcile; `malformed-date` reconciles with T-198 having counted more than the README named |
| The totals T-198 quotes elsewhere are reconciled with the new count, or shown to be unaffected and why | met | The second branch, and **seven occurrences were found by searching that record**, not the two §1 remembered. None moves, because a case true by construction was never inside the exercised fifteen |

**Child fix tasks raised**
- none. The sixth candidate of step 4 is recorded as considered and rejected rather than left for
  someone to find again, and [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)
  already carries the reason a count like this is kept by hand at all.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | `specify` was complete when this was raised, so `plan` → `review` ran under the grant below. **Four criteria, four met.** The fifth case is recorded as **true by construction** — `keep-me`'s twin, since the only mutation available turns a short row into the class — and its line is shown in reach anyway, which `keep-me`'s never was. So the exercised totals do not move, and **all seven places T-198 quotes them were found by searching that record** rather than the two §1 remembered. Two things beyond the criteria: the other four fixtures were swept **both directions** against `tests/fixtures/README.md`, which is where the omission was visible all along — the README said five while the audit said four — and a **sixth** candidate was hunted rather than assumed absent, then rejected as the fenced case's control with its reach measured regardless. |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** the next steps by the project's own ordering rule, each through its **full lifecycle**. Resolved against `taskmd list --open` on 2026-08-21, the grant is [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), then [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md), then [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) — **these three and no others.** Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **What the grant skips, and why, so nobody reads the order as arbitrary**: T-182, T-199, T-202, T-203 and T-206 each carry a live open question that is the owner's, and T-176 needs an uninvolved reader, who is a person and not a session. T-191 and T-198 are audit umbrellas that close when their children do, so neither is work to start. **This one is third.** Closing it also clears one of the two children holding [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) open; the other is T-202, which the grant does not reach, so **neither umbrella closes**. |
| 2026-08-21 | (no change) | **Confirmed by the owner on 2026-08-21 as belonging**, having been raised outside the two-task grant of the same day. Worth asking because that grant said it reached two tasks and no others; the answer is that raising is not starting, and `CLAUDE.md`'s *surface what you discover* binds whatever the grant covers. Written into this record rather than left in the reporting thread, for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) gives. |
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* while doing [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md), and outside its scope, which reaches the fixture's fenced and quoted cases only. `low` and `xs`: the case is proven in reach, so this corrects a record rather than a behaviour — what it buys is that [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) reconciles against a count that is right. A child of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), which does not close until this resolves (`audit.md` step 5). |
