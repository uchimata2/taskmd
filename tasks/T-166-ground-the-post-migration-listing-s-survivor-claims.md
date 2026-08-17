---
id: T-166
title: Stop the post-migration listing framing toward keeping taskmd
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-163, T-165, T-108]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-166 — Stop the post-migration listing framing toward keeping taskmd

## 1. Specify

**Outcome**
The listing in
[`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
— *What taskmd still gives you here* — holds its survivors to the same standard of evidence it holds
its failures to, and stops leaning toward keeping the tool by arrangement rather than by assertion.

**Why this one**
[T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) put the document in front
of an uninvolved reader, who found it argues **mildly toward keep** and named three mechanisms. The
full result is in that record and is not restated here.

**The defect is real and it is not in any sentence.** Every claim in the listing is a measured output
or a pointer — [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) checked exactly
that, and it is true. Framing lives in what is *selected*, what is *placed next to what*, and what a
heading implies, none of which a claim-by-claim check can see. That is why this is its own task
rather than a correction inside T-165: the repair is editorial and the measurement had to survive it.

**The sharpest half is an asymmetry with a cheap fix.** The failures carry dated command output; the
survivors carry the word *by construction*. The reader's decisive missing fact was whether the
binding's operations have ever actually been run — and
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) ran them the same
day, at scale, against a real repository. **The evidence exists and the document does not cite it.**

**Scope**
- In: the three mechanisms the reader named — the *What is gone* section arguing against the
  migration rather than about the tool; the heading that reframes losing the executable surface as
  incidental; the disclaimer doing persuasive work.
- In: citing what [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)
  proved, so a survivor claim rests on a run rather than on *by construction*.
- In: whether the closing menu should stop offering *keep both deliberately* as a third outcome.
- Out: re-running the reader test. That is how this is judged, and re-running it is
  [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s shape, not this
  task's work — though `review` will need a fresh reader, which `specify` must decide.
- Out: removing the conflict-of-interest disclaimer outright. The reader's complaint was that it
  buys trust, not that it is false; deleting it trades one problem for a worse one.
- Out: anything about the migration procedure. That is
  [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) and it is closed.

**Inputs**
- [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) §3 — the reader's
  finding, the three mechanisms, and what they got factually wrong
- [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 — the measurements the
  listing rests on, which are not in dispute
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the
  operations actually exercised against a real repository, and their counts

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **How is this judged?** A fresh uninvolved reader is the only test that caught it, and a document
  edited to pass a known reader is not neutral, it is tuned. Whether `review` spawns a *new* reader,
  and how many, decides whether this task can be honestly closed. **The maintainer answers, at
  `specify`.**

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | — | **The maintainer authorised this task's whole lifecycle** — `specify` → `plan` → `implement` → `review` — **and a commit and push at the end**, given as the subject of a handoff (`create - work T-166, full lifecycle, commit and push`). It covers **this task and nothing else**: no other task, and nothing this one raises, which takes one phase per request unless separately authorised (METHOD §3.1). Recorded here and not only in the handoff, which is consumed once and archived. **The open question below is inside that authorisation and still needs the maintainer**, because it decides whether the task can be closed honestly rather than how to do a step: a document edited to satisfy a reader whose objections you already hold is tuned, not neutral. Answering it by picking the convenient option would make `review` decorative. |
| 2026-08-17 | → proposed | Raised from [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md), which found the listing argues mildly toward keeping taskmd and named three mechanisms for it. Raised rather than fixed there because T-165's `specify` put editing the listing out of scope on purpose: **a repair made in the same breath as the measurement leaves no evidence the measurement happened.** `high` — the listing's whole claim is that it lets someone decide, so a lean in it is the failure of the feature and not a blemish on it. `s`: the edits are small and the difficulty is judgement, not volume. The open question is the one that decides whether this can be closed honestly — a document edited to satisfy a reader whose objections you hold is tuned rather than neutral, so `review` probably needs a reader who has not seen it. **Not covered by the authorisation of 2026-08-17**, which named T-164 and T-165 and excluded what they raise. |
