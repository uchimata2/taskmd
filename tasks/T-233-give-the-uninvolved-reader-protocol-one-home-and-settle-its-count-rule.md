---
id: T-233
title: Give the uninvolved-reader protocol one home, and settle its count rule
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-225, T-232, T-199, T-176, T-166, T-165]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/method/uninvolved-reader.md
---

# T-233 — Give the uninvolved-reader protocol one home, and settle its count rule

## 1. Specify

**Outcome**
The procedure this project uses to put a document in front of a reader who was not involved in
writing it exists as one document, rather than as a citation five task records pass between them —
and its rule about how many readers run says what it actually means.

**Why this one**
**It has run five times and has never been written down.** Every run cites the one before it:
[T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) built it,
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) fixed the extraction rule,
and [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md),
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) and
[T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) each
name *T-166 §3 step 9* as the instrument. **T-166 is closed.** A procedure whose only home is a
closed record is one every future run re-derives by reading a task, and it is the shape this project
has a rule against.

**The count rule failed on 2026-08-22 and that is the concrete occasion.** It says **one reader**, and
its stated purpose is to stop *a second reader after an unwelcome first* — which is iteration, because
it needs an edit or a verdict in between. Two readers ran in parallel on the same text with neither
between them, which the rule forbids and its purpose does not. **The deviation produced that run's
sharpest finding**, and it could not have been produced by one reader: the two declared different sets
from the same clause. So the rule is wrong as written and right in what it was for, which is the
narrow case worth writing down carefully rather than loosening.

**What the protocol already is, gathered rather than invented.** Every rule below was written after a
run that needed it, and each has a record behind it: the document extracted **whole** and verbatim to
somewhere outside this repository, because a slice tests a document nobody receives; the reader given
nothing else and told to open nothing else; the reader's own statement of prior exposure rather than
an assumption; the pass bar and the reader count fixed **before** any result is read; the verdict
recorded as given, including anything factually wrong in it; and **no repair inside the task that
measured**, because a document repaired mid-reading has been tested against nothing.

**Scope**
- In: the protocol as it stands, each rule traced to the run that produced it
- In: the count rule, rewritten so it distinguishes readers running **in parallel on one text** from a
  reader added **after** a result is known, and says which of those is the thing being prevented
- In: where the document lives, and whether an adopter receives it
- In: holding the five prior runs against the written protocol, and naming any that deviated
- Out: re-running any reader, on any document. This writes down what is done, it does not do it again
- Out: the repairs [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)
  carries. Its second open question waits on this record's count rule and says so; the rest of it does
  not, so this is a soft edge and not a blocker
- Out: deciding whether a reader must be a person. That was answered on 2026-08-22 and the answer is
  in T-199 and T-176; this record carries it rather than re-opening it

**Inputs**
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 step 9 — the instrument as
  it stands, and the extraction lesson behind it
- [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) §3 —
  the run where the count rule failed, and why the deviation is recorded as a deviation
- [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md),
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md),
  [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) — the other
  three runs, and the rules each of them added

**Acceptance criteria**
- [ ] Every rule in the document names the run that produced it, so a later reader can tell a measured
      rule from a preference
- [ ] The count rule distinguishes parallel readers from a reader added after a result, and states
      which one it exists to prevent
- [ ] The five prior runs are held against the written protocol and any that deviated is **named**,
      including the one that already has
- [ ] Where the document lives is decided and stated, with what that choice costs
- [ ] Nothing in it restates a rule [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) or
      [`audit`](../plugin/skills/taskmd/docs/method/audit.md) already owns; where it extends one, it
      says so

**Open questions**
- ~~**Does an adopter receive this, or is it this project's own practice?**~~ **Answered
  2026-08-23: ship it, as a tier-3 method document.** The count rule was put to the owner in the
  same turn and answered **two readers in parallel, fixed in advance** — a rejection re-opened on
  new evidence rather than reversed here. Original question follows. — the project owner. The
  recommendation is **ship it, as a tier-3 method document**: it names no artefact type and no tool,
  it is the only instrument this project has for judging a document it wrote itself, and an adopter
  writing a binding has exactly that problem — which is what T-199 and T-225 were both for. Against:
  it is one more document in what an install copies, it has been proven on documents of one kind only,
  and keeping it in `docs/` costs nothing and can be promoted later. **The cheaper mistake is
  internal**, because moving a document out of `plugin/` is what this project did on 2026-08-22 and it
  cost three link edits.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Gather each rule with the run behind it, and write each **descriptively** rather than by identifier | the rule list, with provenance |
| 2 | Write the count rule so it separates *parallel on one text* from *added after a result*, and says which is forbidden | the rule |
| 3 | Write the document, and check it restates nothing [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) or [`audit`](../plugin/skills/taskmd/docs/method/audit.md) owns | the deliverable |
| 4 | Hold all five prior runs against it and name every one that deviates, including under the **new** count rule | the table |
| 5 | Put it at its home, add the §7 row, and point [`implement`](../plugin/skills/taskmd/docs/method/implement.md)'s verification table at it | the three edits |
| 6 | `check`, the suite, and the tier-1 bound | the outputs |

**Step 1 writes provenance descriptively, and that is a decision rather than a style.** A shipped
document cannot cite this project's task ids: an adopter receives the document and none of the
records, so every id in it would resolve to nothing on their machine. Naming what went wrong carries
the same weight and travels.

**Step 4 is the one that can embarrass the deliverable**, which is why it is a step rather than a
formality: the new count rule is stricter than the old one, so runs that were compliant when they ran
may not be now.

## 3. Implement

**Decisions & assumptions**

- **It ships, at `plugin/skills/taskmd/docs/method/uninvolved-reader.md`, tier 3** — 2026-08-23, on
  the owner's answer. **What that costs**: one more document in what an install copies, and it is
  proven on documents of one kind only — bindings and a migration listing. **And un-shipping it later
  is the expensive direction**: moving a document out of `plugin/` is what this project did on
  2026-08-22 and it cost three link edits, which is why the cheaper mistake would have been to keep
  it internal. The owner weighed both and chose to ship.
- **Provenance is written descriptively, never as a task id** — 2026-08-23. An adopter receives the
  document and none of these records, so *added after a run that handed over an excerpt* travels
  where *T-166 §3 step 9* does not. The id trail stays here, in §1's inputs.
- **The count rule is stricter than the one it replaces, and that is faced rather than smoothed**
  — 2026-08-23. Two in parallel, fixed in advance. It means three of the five prior runs would not
  satisfy the protocol they produced. See the table below; nothing is re-run, because §1 puts that
  out of scope.
- **A disagreement between the two readers is a finding, not a tie** — 2026-08-23. Written in
  explicitly, because the obvious next move on a split is a third reader, and a third reader after a
  result is exactly what the count rule forbids.

**Outputs produced**

- `plugin/skills/taskmd/docs/method/uninvolved-reader.md` — the deliverable
- `plugin/skills/taskmd/docs/METHOD.md` — one row in §7
- `plugin/skills/taskmd/docs/method/implement.md` — the verification table's *written analysis* row
  points at it

**Verification**

**Step 4 — the five prior runs held against the written protocol.**

| Run | Against the protocol as written | Deviates? |
| :--- | :--- | :--- |
| The post-migration listing, first run | Built the instrument. Most of these rules did not exist to be followed | — the origin |
| The survivor-claim grounding | Handed the reader an **excerpt**. That failure is rule 1 | **yes**, and rule 1 exists because of it |
| The sourced survivor bullet | One reader | **yes**, on the count rule only |
| The coverage declaration, first reading | One reader; its unprompted blank is rule 5 | **yes**, on the count rule only |
| The coverage declaration, second reading | **Two readers, in parallel, neither shown the other's answer** | **no** — it is the only run that satisfies the current protocol |

**The only compliant run is the one recorded as a deviation.** It broke the rule in force by running
two, and the finding that deviation produced is why the rule now says two. That is stated here
because it looks like an error until it is read the other way round.

**Step 3 — restatement check.** Read against [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md)
and [`audit`](../plugin/skills/taskmd/docs/method/audit.md) clause by clause. One overlap and it is
declared in the text: rule 7, *repair nothing inside the task that measured*, is METHOD rule 4
arriving in a different instrument, and the document says so in that sentence rather than restating
the rule. The opening states that the file changes no rule in
[`implement`](../plugin/skills/taskmd/docs/method/implement.md) and is one way of meeting its exit
criterion — which is an extension declared, not a copy.

**Step 6 — the gates.**

```text
taskmd check                                   ->  exit 0
python -m pytest tests/test_budget.py -q       ->  8 passed
python -m pytest tests/ -q                     ->  342 passed, 8 subtests passed
```

Tier 1 is untouched: the deliverable is tier 3, and its two pointers are in tier-2 and tier-3 files.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every rule names the run that produced it, so a later reader can tell a measured rule from a preference | met | Five of the seven carry an *added after a run that…* clause; the two that do not (give them nothing else; do not prompt for the answer) are stated as what the instrument **is**, and the second carries its run anyway. **Named descriptively, not by id** — a shipped document cannot cite records an adopter does not receive, and §3 records that as a decision |
| The count rule distinguishes parallel readers from a reader added after a result, and states which it exists to prevent | met | It defines *parallel* explicitly — same extract, same time, neither shown the other, no edit and no verdict between — and says the thing prevented is a reader added **after** a result you did not like, which needs an edit or a verdict in between and is therefore impossible in parallel |
| The five prior runs are held against the written protocol and any that deviated is **named** | met | All five in §3, three deviating. **The only compliant run is the one recorded as a deviation**, which is stated rather than glossed |
| Where the document lives is decided and stated, with what that choice costs | met | Shipped, tier 3, on the owner's answer. §3 names both costs — one more document an install copies, proven on one kind of document — and that un-shipping later is the expensive direction, priced at the three link edits it cost on 2026-08-22 |
| Nothing restates a rule `METHOD.md` or `audit` already owns; where it extends one, it says so | met | One overlap, declared in the text: rule 7 is METHOD rule 4 in a different instrument and the sentence says so. The opening declares the whole file an extension of `implement`'s verification row and states it changes no rule there |

**Child fix tasks raised**
- none.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 held one, the owner's, answered
2026-08-23 and struck through. **One thing is recorded rather than left implicit**: the count rule
this record settles is what
[T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s second open question was
waiting on, and that question is answered in T-232's own review — the test that differs in kind from
the one that failed is two readers in parallel checking whether they now declare the **same** set.
Running it is the owner's to schedule.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed: five criteria, five met.** The protocol that had run five times and lived only in a closed record is now `plugin/skills/taskmd/docs/method/uninvolved-reader.md`, tier 3, shipped on the owner's answer — with what that costs written down, including that un-shipping it later is the expensive direction at three link edits. **The count rule is two readers in parallel, fixed in advance**, and the owner re-opened their own 2026-08-22 rejection of two on the evidence rather than having it reversed here. It now separates *parallel on one text* from *a reader added after a result*, and says only the second is the hazard — which is what the old rule described correctly and banned wrongly. **Holding the five prior runs against it produced the sharpest line in the record**: three of them deviate, and **the only run that satisfies the current protocol is the one recorded as a deviation** — it broke the rule in force by running two, and that is why the rule now says two. **Provenance is written descriptively rather than by task id**, because an adopter receives the document and none of these records. |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, after [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) ran two readers where its bar fixed one and the deviation turned out to be the reason its best finding exists. **The occasion is the count rule; the defect is the missing home.** Five runs have each cited the run before, the earliest of them closed, so the instrument is re-derived from a closed record every time — which is the failure mode this project has a rule against and had not applied to its own practice. **`medium` rather than `high`**: nothing is broken today and no release waits on it, but the cost is paid again on every reader run and the rule that just failed will fail the same way next time. **Not in the unattended grant of 2026-08-22** — that grant names five records, was fixed before this one existed, and its own boundary says so. |
