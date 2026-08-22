---
id: T-233
title: Give the uninvolved-reader protocol one home, and settle its count rule
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-225, T-232, T-199, T-176, T-166, T-165]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables: []
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
- **Does an adopter receive this, or is it this project's own practice?** — the project owner. The
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
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, after [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) ran two readers where its bar fixed one and the deviation turned out to be the reason its best finding exists. **The occasion is the count rule; the defect is the missing home.** Five runs have each cited the run before, the earliest of them closed, so the instrument is re-derived from a closed record every time — which is the failure mode this project has a rule against and had not applied to its own practice. **`medium` rather than `high`**: nothing is broken today and no release waits on it, but the cost is paid again on every reader run and the rule that just failed will fail the same way next time. **Not in the unattended grant of 2026-08-22** — that grant names five records, was fixed before this one existed, and its own boundary says so. |
