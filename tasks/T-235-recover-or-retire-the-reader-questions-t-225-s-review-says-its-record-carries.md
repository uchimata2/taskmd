---
id: T-235
title: Recover or retire the reader questions T-225's review says its record carries
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-225, T-232, T-233]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
deliverables: []
---

# T-235 — Recover or retire the reader questions T-225's review says its record carries

## 1. Specify

**Outcome**

Either Reader B's questions exist in this repository, one per line, or
[T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) says
plainly that they were not kept — and
[T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s fifth acceptance
criterion is settled either way, so the release blocker can move.

**Where this came from**

Found on 2026-08-23 while T-232's `specify` was being closed under the owner's unattended grant.
T-225 §4 marks the criterion *Every question settled by guessing is listed, and each matched against
the eight* as **met**, noting *"the questions falling outside them are grouped there rather than
dropped"*. **§3 carries no such group.** It carries the two declarations verbatim, the eight walked
one by one, and the divergence finding — and nothing else. Six of Reader B's questions appear inline
in rows 3, 4, 6 and 7 of that walk; the rest are named nowhere in the repository. `control/` was
checked too, being gitignored and therefore easy to forget: three files, none of them the run.

**Three counts, and they do not reconcile.** This is how it was found, and it is the substance of the
task rather than a detail of it.

| Source | Says | Count |
| :--- | :--- | :---: |
| T-225 §4, the review note | Reader B produced *n* questions about the contract, plus three about Linear | **19** |
| T-225 §3, the eight walked one by one | B's questions actually named, inline in rows 3, 4, 6, 7 | **6** |
| T-232 §1 and its criterion 5 | *the fifteen single-mention questions in T-225 §3* | **15** |

19 − 6 = 13, which is neither 15 nor anything else written down, and **no list of any of the three
sizes exists**. A criterion cannot be met against a set nobody can enumerate, and the failure mode is
the one T-232 exists to repair, one level up: a session answers whichever questions it can find,
records that the criterion is met, and the gap is invisible because every question it *did* answer is
real.

**Why it is not repaired inside T-232.** T-232's outcome is `BINDING.md` §4. Correcting a closed
record and recovering an owner's run output are different work with a different owner, and folding
them in would let a repair to the contract be judged by a criterion about a task record. It is a
**dependency** rather than a child: T-232's own outcome is not incomplete without this: it cannot
*proceed* until the fifth criterion has a set or has been withdrawn.

**Scope**

- In: whether the raw reader output survives anywhere the owner holds, and if so, its arrival in the
  repository as a dated annexe to T-225 §3
- In: T-225's review note brought into line with what its record carries — **annotated, not
  rewritten**, since it is a dated statement about a past run (METHOD rule 5)
- In: the disposition of T-232's criterion 5, which is the owner's because the owner agreed it
  ([`review`](../plugin/skills/taskmd/docs/method/review.md), *Changing a criterion*)
- In: reconciling the three counts above, or showing that each answers a different question
- Out: repairing `BINDING.md` §4 — that is T-232, and this record exists so that it can be judged
- Out: re-running any reader. Whether a further reader runs at all is T-232's second open question,
  and the count rule it waits on is
  [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md)
- Out: changing T-225's verdict. The FAIL rests on defect 8 recurring, which two readers reported and
  reading the paragraph confirmed; nothing here touches it

**Inputs**

- [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) §3
  and §4 — the walk, the declarations, and the review note that claims the group
- [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) §1 — the scope line and
  criterion 5 that depend on the set

**Acceptance criteria**

- [ ] Either Reader B's questions are in the repository, one per line, or T-225 carries a dated
      annotation saying they were not kept and are not recoverable
- [ ] T-225's review note no longer claims §3 groups them, **and the 2026-08-22 row is not rewritten**
- [ ] T-232's criterion 5 is supplied with its set, narrowed by the owner to what the record can
      support, or withdrawn by the owner with a reason — recorded in T-232 with the original text
      beside the replacement
- [ ] The three counts are reconciled, or each is shown to answer a different question and the table
      above says which

**Open questions**

- ~~**Does the raw reader output still exist?**~~ **Answered 2026-08-23: yes, and the owner supplied it in full.** It is recorded in T-225 §3. Original question: — the **project owner**, who ran both readers on
  2026-08-22. Nothing in this repository holds it. **Recommendation: if it exists, paste B's question
  list into T-225 §3 as a dated annexe** — the record is its only possible home, and a second run
  cannot reproduce it because a different reader asks different questions. Cost if wrong: a long
  annexe in a closed record, which is cheap. If it does not exist, say so there in one dated line;
  cost of *not* saying so is that every later reader re-derives this mismatch, as this one did.
- ~~**If the output is gone, which way does T-232's criterion 5 go?**~~ **Moot from 2026-08-23** — the output was not gone. Original question: — the **project owner**, who
  agreed it. **Recommendation: narrow it to the six questions T-225 §3 actually names**, and say in
  T-232 that it was narrowed, why, and what was lost. *Against:* those six are already visible in the
  walk, so narrowing buys honesty rather than coverage. *Rejected: withdraw the criterion* — it loses
  the fifteen without leaving a record that they were lost, which is the same silent gap in a
  different place. *Rejected: let the repairing session answer whatever questions it can find* — that
  is the under-declaration failure T-232 is repairing, reproduced in T-232's own review.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Put the reader's reply into [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) §3 as a dated annexe, adding and never rewriting | the annexe, all twenty-two questions |
| 2 | Map every one of the nineteen contract questions against what T-225 §3 already named, one at a time | a membership list, and two counts that sum to nineteen |
| 3 | Reconcile the three figures — 19, 6 and 15 — or show what each was counting | the arithmetic, and the unit each figure used |
| 4 | Annotate T-225's review note so it no longer claims §3 groups them, leaving its verdict and its 2026-08-22 row untouched | the annotated row |
| 5 | Settle [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s fifth criterion now that its set exists | the criterion, with its original text beside the replacement |

**Step 2 maps per question and not per row, because the discrepancy is a unit error until proved
otherwise.** Counting how many of B's questions T-225 mentions is a different operation from counting
how many table rows mention one, and the gap between 15 and anything derivable is exactly the size of
that difference.

**Outputs**

- no new file. The annexe is added to `tasks/T-225-…`, and the criterion is corrected in `tasks/T-232-…`

## 3. Implement

**Decisions & assumptions**

- **The reply exists and is recorded, so nothing is retired** — 2026-08-23. The owner supplied Reader
  B's answer in full the same day this record was raised. §1's first branch applies: the questions go
  into T-225 §3 as a dated annexe, which is their only possible home, and the second branch — an
  annotation saying they were not kept — is not taken.
- **Added to a closed record, never rewritten** — 2026-08-23. The annexe is dated for what it is and
  nothing from 2026-08-22 was altered. The review note that over-claimed keeps its **met** verdict and
  its wording, with the correction appended inside the same cell: the counts it gives are right and
  the claim about where the questions live was not, and both halves are now visible.
- **T-232's fifth criterion is corrected upward, not narrowed** — 2026-08-23. It read *the fifteen
  single-mention questions*; fifteen is not a figure anything produces (see below), and the set that
  exists is **nineteen**. Since the data is now in the record, the criterion asks for more than it did
  rather than less, so this is not the narrowing §1 warned about. Original text kept beside the
  replacement in T-232 §1, per [`review`](../plugin/skills/taskmd/docs/method/review.md),
  *Changing a criterion*.

**Outputs produced**

- `tasks/T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md`
  — the annexe, and the annotated review note
- `tasks/T-232-repair-the-coverage-clause-against-what-two-readers-found.md` — the corrected criterion

**Verification**

**Step 2, mapped per question.** Each of the nineteen was checked against T-225 §3 individually.

| Appears in §3 | Where | Items |
| :--- | :--- | :--- |
| yes | the eight walked one by one | 1 (row 8), 3 and 17 (row 6), 4 and 5 (row 3), 6 (row 4), 16 (row 7) |
| yes | *The finding neither reader could have produced alone* | 11 |
| **no — appears nowhere** | — | 2, 7, 8, 9, 10, 12, 13, 14, 15, 18, 19 |

**8 named + 11 unnamed = 19**, which is every contract question. The three about Linear are
summarised in §3's paragraph after Reader B's declaration and are now recorded in full.

**Step 3, the three figures reconciled — and the third was counting rows.**

| Figure | Where | What it counted | Right? |
| :--- | :--- | :--- | :--- |
| **19** and **3** | T-225 §4 | questions, by category | **Right.** Confirmed against the reader's reply: nineteen numbered contract items, three about Linear |
| **6** | T-225 §3 | questions named inline in the eight-walk | **Right**, and it is seven if item 11's separate mention is added, eight in total across §3 |
| **15** | T-232 §1 and criterion 5 | *single-mention questions* | **Wrong, and wrong by unit.** Nineteen minus **four table rows** is fifteen. Rows 3, 4, 6 and 7 of the eight-walk each report a question of B's in the words *B asked*; row 8 reports item 1 as *B named the mismatch exactly*, which reads as a finding and not as a question. A count scanning for questions and landing on rows produces exactly 15 |

**So the figure was produced by counting the wrong things, not by dropping members** — the eleven that
appear nowhere were never enumerated anywhere, which is why the criterion could not be met and why
this record exists. The correct residual is **eleven**, and the criterion now names all nineteen
because the whole set is available and answering only the residual would leave eight answered by a
walk that was checking whether a *defect* recurred, not whether a *question* was settled.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Either the questions are in the repository, one per line, or T-225 carries a dated annotation saying they were not kept | met | The first branch. All twenty-two are in T-225 §3 as *Reader B's questions in full*, dated 2026-08-23, one row each, with what the reader wanted the text to say |
| T-225's review note no longer claims §3 groups them, **and the 2026-08-22 row is not rewritten** | met | The note keeps its verdict and its wording; the correction is appended inside the cell and dated. The Log row of 2026-08-22 is byte-identical |
| T-232's criterion 5 is supplied with its set, narrowed, or withdrawn — recorded with the original text beside the replacement | met | **Supplied**, and corrected from fifteen to nineteen, which asks for more rather than less. Original text kept beside it in T-232 §1 |
| The three counts are reconciled, or each is shown to answer a different question | met | Reconciled. 19 and 3 are right; 6 is right; **15 counted table rows where it meant questions** — 19 − 4 rows = 15, and the four are rows 3, 4, 6 and 7. The true residual is eleven, and 8 named + 11 unnamed = 19 sums |

**Child fix tasks raised**
- none. T-232 is unblocked by this record and its `blocked_by` is cleared there, not here.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 held two, both the owner's, and
both are answered: the output existed and was supplied on 2026-08-23, so the second — *which way does
criterion 5 go if it is gone* — never arose and is struck as moot rather than left looking open.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed the same day it was raised: the owner supplied Reader B's reply in full, so nothing had to be retired.** All twenty-two questions are now in T-225 §3 as a dated annexe — added, with nothing from 2026-08-22 altered. **The three counts reconcile, and the wrong one was wrong by unit**: nineteen and three are right, six is right, and **fifteen counted table rows where it meant questions** — 19 minus the four walk rows that say *B asked* is exactly 15. So no member was dropped; the residual was simply never enumerated. Mapped per question, not per row: **8 named in §3 + 11 named nowhere = 19**. **T-232's criterion 5 is corrected upward**, from fifteen to nineteen, with its original text beside the replacement — supplying a set is not the narrowing §1 warned about. T-232's `blocked_by` is cleared in T-232. |
| 2026-08-23 | → proposed | Raised from [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s `specify`, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure, without stopping to ask for each phase. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit** — unchanged. **It authorises phases, not answers, and that binds immediately here**: both open questions above are the owner's, and one of them asks for data only the owner can still hold, so **this record stops at `specify`** rather than being carried further. **Why it is a dependency of T-232 and not a child of T-225**: T-225 is closed and its outcome — two declarations and a verdict against a bar fixed first — is complete and unaffected; what is missing is an annexe its review note promised. A child would re-open a finished task to hold it open for somebody else's data. **Nothing in T-225 was edited when this was raised**, deliberately: its review note is wrong about the present and correcting it is this task's first criterion, not a tidy-up on the way past. |
