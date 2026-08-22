---
id: T-228
title: Decide whether the reader's framing verdict reopens the accepted balance
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-176, T-167, T-166, T-221]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-228 — Decide whether the reader's framing verdict reopens the accepted balance

## 1. Specify

**Outcome**
An answer, recorded, on whether the migration listing's balance is re-opened on the strength of the
2026-08-22 reader run — and if it is, what specifically changes.

**Why this one**
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed the listing's balance as **accepted**.
[T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s reader then found a
mild lean and located it precisely, in a document that has already passed a claim-by-claim check.
Three things are on the table and none is carried anywhere yet:

- **The lean is in the arrangement, not the claims.** *What survives* lists four items flatly, *What
  is gone* lists three and rebuts two in place, so *"the losses shrink under inspection. The
  survivals do not."*
- **The sharpest line is about a sentence written as a repair.** On *"It is a list of facts and it
  stops short of a recommendation"*: *"Declaring no opinion, in a document you wrote and ordered, is
  a position."* That sentence came out of
  [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md).
- **Two limits still read as softening**, of three the reader named. The third — *True as behaviour,
  overstated as necessity* — was rewritten by
  [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) on
  2026-08-22 as a correction of fact; **whether that rewrite also removed the softening the reader
  saw is unmeasured**, and assuming it did would be the comfortable answer.

**This is a decision and not a fix, and the reason is recorded twice already.** T-176 §1 puts
re-balancing out of scope, and T-221's Log states that a revisit on a changed premise is a new task
and a new request, *raised on its own terms where the owner can weigh it as a decision rather than
meet it as a side effect*. This is that task. **The default answer is no** — an accepted decision is
not reversed by a reader's opinion — and the reason to ask anyway is that the evidence is new and
came from outside.

**Scope**
- In: whether to change anything, and if yes what — named sentence by sentence
- In: whether the two remaining *softening* limits are softening, or are honest limits a reader
  reasonably misread
- In: whether T-221's rewrite of the third one changed how it reads, which nobody has checked
- Out: the claims themselves. Every one of them is measured and T-221 corrected the two that were
  wrong
- Out: running another reader. That is
  [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md)'s
  hazard in a different document — a second reader after an unwelcome first is iteration

**Inputs**
- [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) §3 — the verdict, the
  honest/softening split, and the two counter-pulls the reader credited
- [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) — the decision this would re-open, and
  the five framing mechanisms it accepted
- `plugin/skills/taskmd/docs/bindings/github-issues.md`, *What taskmd still gives you here* — the
  three sections the verdict is about, as they stand after 2026-08-22

**Acceptance criteria**
- [ ] The answer is recorded with its reason, in T-167's own terms rather than in this task's
- [ ] Each of the three findings is answered separately — a single yes or no across all three would
      hide which one carried the decision
- [ ] Whether T-221's rewrite changed how the third limit reads is checked against the text, not
      assumed
- [ ] If the answer is no, what would change it is stated — otherwise the same verdict arrives again
      with nothing to compare it against

**Open questions**
- ~~**Does a reader's framing verdict re-open an accepted balance?** — the project owner. The
  recommendation is **no for the arrangement and yes for the one sentence**: the arrangement was
  weighed and accepted, and a reader who calls the result a *mild* lean while crediting two sentences
  that cut against the tool has largely confirmed it. *"Declaring no opinion is a position"* is
  different — it is a claim the document makes about itself, not a matter of proportion, and it is
  cheap to drop.~~ **Answered by the owner on 2026-08-22: no for the arrangement, yes for the one
  sentence.** See the Log row of that date. **It covers two of the three findings**, and the third —
  whether the two remaining limits are softening — is judgement this record still has to do.

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
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task:** two of its three findings were answered on 2026-08-22. The third — whether the two remaining limits are softening, and whether T-221's rewrite changed how the third reads — is judgement made by reading the text, and it is this record's own work. **If that reading concludes the balance should change, it returns to the owner and stops here**: the answer of 2026-08-22 was that the arrangement stands. |
| 2026-08-22 | (no change) | **The owner answers two of the three findings: no for the arrangement, yes for the one sentence.** Answered 2026-08-22. **The arrangement stands** — [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) weighed it and accepted it, and a reader who calls the result a *mild* lean while separately crediting two sentences that cut against the tool has largely confirmed that decision rather than overturned it. ***"It is a list of facts and it stops short of a recommendation"* goes** — it is not a matter of proportion but a claim the document makes about itself, the reader's line on it is unanswerable (*"Declaring no opinion, in a document you wrote and ordered, is a position"*), and dropping it costs nothing the section needs. *Rejected: re-balance on the verdict* — it would reverse an owner decision on evidence collected for another purpose, which is the thing [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s Log forbade in advance. *Rejected: change nothing* — it treats every finding as proportion when one is not. **The third finding is not covered and is this record's own work**: whether the two remaining limits are softening, and whether T-221's rewrite of the third changed how it reads. That is judgement made by reading the text, and it returns to the owner only if it changes the balance. |
| 2026-08-22 | → proposed | Raised by [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s fifth criterion, which requires anything the reader turned up outside that task's scope to leave as its own task rather than be repaired where it was found. Three findings had no home: the located lean, the *declaring no opinion* line, and two limits still reading as softening. **A decision rather than a fix**, by the schema's own test — the outcome is an answer somebody else could act on, and any change follows from it. **Raised with its default answer stated**: an accepted decision is not reversed by a reader's opinion, and the reason to put it up anyway is that the evidence is new, came from outside, and was collected without the reader knowing framing was the subject. **The unmeasured half is the one to watch** — [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) rewrote one of the three limits the same day for an unrelated reason, and whether that removed the softening is nobody's finding yet. |
