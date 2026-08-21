---
id: T-203
title: Detect an issue whose state disagrees with its status label
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-178, T-193, T-108]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-21
updated: 2026-08-21
adopter_visible: yes
deliverables: []
---

# T-203 — Detect an issue whose state disagrees with its status label

## 1. Specify

**Outcome**
The GitHub Issues binding's standing check can report an issue whose `state` contradicts its
`status:` label — so assumption 2 stops being a request nobody can enforce and becomes a condition
something notices.

**Why this one**
Raised by the owner on 2026-08-21, reading the binding's assumption 2: *Nobody on your project closes
or reopens an issue in the GitHub UI.* Their objection is the one the single-source-of-truth rule
makes: on this backend the answer to *is this task open?* is written in two places, and one of them
is a button.

**The hole is sharper than the assumption admits, and it is structural.** The binding says `state` is
*the one materialised derived view this binding has*, written from the `status:` label and only from
it. METHOD §4 allows a materialised derived view; what it does not allow is one that nothing
regenerates or reconciles. And **the standing check cannot see the divergence even in principle**:

- none of the nine rows of *Checking a backlog that is already here* compares `state` with the
  `status:` label;
- `enumerate` fetches `number,title,body,labels,parent,subIssues,blockedBy,blocking` and
  **deliberately does not fetch `state`** — assumption 2's own *no operation reads it*.

So the one procedure that could notice is looking away by design. The assumption is not merely
fragile; it is unenforceable by construction, and a click that breaks it leaves a task contradicting
itself with every view saying it is fine. **That is the same shape as
[T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md)'s duplicated index** —
a defect no validator could see because nothing read the place it lives.

**The interesting half is what *reading* `state` costs.** Assumption 2 exists to stop `state` being
read **as** the status — a rendering treated as the fact. Reading it **against** the fact is the
opposite move, and the binding's own text does not distinguish them. Whether that distinction
survives contact with the rest of the document is this task's question, not a detail.

**Requirements served**
R-9, R-16 (`docs/SCOPE.md`).

**Scope**
- In: whether `enumerate` fetches `state`, and what assumption 2 has to say once it does
- In: a row in *Checking a backlog that is already here* for the disagreement, if the answer is yes
- In: what the row tells a reader to do — the label is the fact, so the repair is to re-render
  `state`, and saying so is the difference between a check and a puzzle
- Out: **any change to how status is stored.** The `status:` label carries eight values and `state`
  carries two; making `state` the fact is not available and is not what this asks
- Out: reconciling automatically. Non-goal 10, and a check that silently repaired the thing it found
  would destroy the evidence that anybody clicked
- Out: the other bindings. `local-markdown` has no second place for this fact

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — assumption 2, *update*'s two-writes rule,
  *enumerate*, and the nine rows
- [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) §3 — the four runs, and
  which rows examined nothing
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the migration
  that established `state` as a rendering

**Acceptance criteria**
- [ ] The binding says whether `state` is fetched, and assumption 2 reads correctly beside that
      answer — a reader must not be able to conclude both *never read it* and *read it here*
- [ ] If a row is added, it is **run against a live backlog and made to fail** on an issue closed in
      the UI while its label says otherwise, with the output quoted — the standard
      [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) set
- [ ] It is shown **not** to fire on an issue whose `state` and label agree, in both directions —
      open with an open status, closed with a closed one
- [ ] The row says which side is the fact, so the repair is unambiguous
- [ ] Whether this makes assumption 2 removable is answered either way, and the answer is argued
      rather than asserted

**Open questions**
- ~~**Is a detected divergence enough, or does the mapping itself need revisiting?** The owner's wider
  point on 2026-08-21 was that taskmd on this backend should be a guardrail over `gh` rather than
  anything holding its own copy — which the binding already is. This task takes the narrow reading: a
  fact stored twice, with nothing checking the two agree. If the answer is that a rendering nobody
  can be stopped from editing should not be materialised at all, that is a larger decision and the
  owner's.~~ **Answered by the owner on 2026-08-22: report the divergence; the mapping is not revisited** — see the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised by the owner on 2026-08-21, from reading assumption 2 of the GitHub binding. `high` and `s`: the row is small and what it guards is the only fact this backend stores twice, in a place one click changes and nothing reads. The evidence that it is unenforceable rather than merely fragile came out of [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s run - `enumerate` does not fetch `state`, so no row could compare it even if one wanted to. |
| 2026-08-22 | (no change) | **The open question is answered by the owner: detecting the divergence is enough, and the mapping stands.** Asked in the batched round of 2026-08-22. METHOD §4 allows a materialised derived view but not one nothing reconciles, and a comparison of `state` against the `status:` label is that reconcile — reading `state` *against* the fact rather than *as* it. *Rejected: revisit the mapping first*, which avoids building a guard for something that might be removed, but leaves the hole open while it is decided and a click still leaves a task contradicting itself with every view reporting it fine. *Rejected: stop writing `state` at all*, which removes the second copy outright, but GitHub's own search, filters and UI read it, so the backlog gets harder to use in the tool people already have open. This row is the answer, not authorisation to start. |
