---
id: T-203
title: Detect an issue whose state disagrees with its status label
type: deliverable
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-178, T-193, T-108]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-21
updated: 2026-08-22
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
- **A live backlog on GitHub — and it does not exist today.** Criteria 2 and 3 cannot be met by
  reading anything. [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) built
  `uchimata2/taskmd-standing-check-scratch` for its own run and left step 10 — deleting it — to the
  owner, because the token carries no `delete_repo` scope. That deletion has happened, measured on
  2026-08-22:

  ```text
  $ gh repo view uchimata2/taskmd-standing-check-scratch
  GraphQL: Could not resolve to a Repository with the name
  'uchimata2/taskmd-standing-check-scratch'. (repository)
  ```

  Credentials are present and sufficient — `gh auth status` reports account `uchimata2` with scopes
  `gist, project, read:org, repo, workflow`, so `repo` would create one. What is missing is not
  access but **permission**: creating a repository on the owner's account is an outward-facing act,
  and no grant here covers it. Recorded as an open question below rather than assumed, because
  specify treats an input nobody can reach as a dependency in disguise

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
- [ ] **The mapping is untouched, shown by a diff**: `state` is still written from the `status:`
      label, *update*'s two-writes rule reads as it did, and no vocabulary moves. The owner's answer
      of 2026-08-22 rejected both revisiting the mapping and dropping `state`, so a task that
      quietly did either would have taken a decision it was told not to take

**Open questions**
- ~~**Is a detected divergence enough, or does the mapping itself need revisiting?** The owner's wider
  point on 2026-08-21 was that taskmd on this backend should be a guardrail over `gh` rather than
  anything holding its own copy — which the binding already is. This task takes the narrow reading: a
  fact stored twice, with nothing checking the two agree. If the answer is that a rendering nobody
  can be stopped from editing should not be materialised at all, that is a larger decision and the
  owner's.~~ **Answered by the owner on 2026-08-22: report the divergence; the mapping is not revisited** — see the Log row of that date.
- **Raised at `specify` on 2026-08-22, and it blocks `implement` rather than the outcome: may a
  scratch repository be created on the owner's GitHub account for the run criteria 2 and 3 require?**
  **The owner decides** — it is an outward-facing act on their account, and the previous one is gone
  (see *Inputs*). **Recommended: yes, one private scratch repository, deleted by the owner
  afterwards** — the same arrangement
  [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) ran under, which worked and
  whose cleanup step the owner has demonstrably performed. *The cost if that is wrong*: a private
  repository exists on their account until they remove it, and this token cannot remove it for them.
  *The alternative*: meet the criteria against a **fixture** rather than a live backlog — cheaper and
  needs no permission, but the thing under test is what GitHub's API returns for `state`, so a fixture
  would be this repository's own belief about that API rather than the API, and criterion 2 says *run
  against a live backlog* for exactly that reason. **This does not stop `specify`** — the criteria are
  written and agreed, and the method holds that a question blocking only a later phase is noted and
  left open.

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
| 2026-08-22 | → specified | **Specify agreed. The owner's answer is folded in, one criterion is added, and one new question is opened.** The added criterion pins the mapping by diff: the answer rejected both revisiting it and dropping `state`, and neither rejection was written anywhere a review would read, so a task that quietly did either would have passed. **The new question is a precondition, found by checking that this task's own criteria can be met.** Criteria 2 and 3 require a run against a live backlog, and [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s scratch repository is gone — `gh repo view` returns *Could not resolve to a Repository*, quoted in *Inputs*, which is the owner performing that task's step 10 rather than anything going wrong. Credentials are present and carry `repo`; what is absent is permission to create a repository on the owner's account. **It blocks `implement`, not the outcome**, so `specify` ends with it noted rather than waiting on it (`specify.md` step 5) — and it is the *phases, not answers* limit in advance: no grant of phases could answer it. Phase stays at `specify`; `plan` is not authorised. |
