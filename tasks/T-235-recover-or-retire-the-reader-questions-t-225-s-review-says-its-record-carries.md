---
id: T-235
title: Recover or retire the reader questions T-225's review says its record carries
type: fix
status: proposed
phase: specify
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

- **Does the raw reader output still exist?** — the **project owner**, who ran both readers on
  2026-08-22. Nothing in this repository holds it. **Recommendation: if it exists, paste B's question
  list into T-225 §3 as a dated annexe** — the record is its only possible home, and a second run
  cannot reproduce it because a different reader asks different questions. Cost if wrong: a long
  annexe in a closed record, which is cheap. If it does not exist, say so there in one dated line;
  cost of *not* saying so is that every later reader re-derives this mismatch, as this one did.
- **If the output is gone, which way does T-232's criterion 5 go?** — the **project owner**, who
  agreed it. **Recommendation: narrow it to the six questions T-225 §3 actually names**, and say in
  T-232 that it was narrowed, why, and what was lost. *Against:* those six are already visible in the
  walk, so narrowing buys honesty rather than coverage. *Rejected: withdraw the criterion* — it loses
  the fifteen without leaving a record that they were lost, which is the same silent gap in a
  different place. *Rejected: let the repairing session answer whatever questions it can find* — that
  is the under-declaration failure T-232 is repairing, reproduced in T-232's own review.

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
| 2026-08-23 | → proposed | Raised from [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s `specify`, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure, without stopping to ask for each phase. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit** — unchanged. **It authorises phases, not answers, and that binds immediately here**: both open questions above are the owner's, and one of them asks for data only the owner can still hold, so **this record stops at `specify`** rather than being carried further. **Why it is a dependency of T-232 and not a child of T-225**: T-225 is closed and its outcome — two declarations and a verdict against a bar fixed first — is complete and unaffected; what is missing is an annexe its review note promised. A child would re-open a finished task to hold it open for somebody else's data. **Nothing in T-225 was edited when this was raised**, deliberately: its review note is wrong about the present and correcting it is this task's first criterion, not a tidy-up on the way past. |
