---
id: T-228
title: Decide whether the reader's framing verdict reopens the accepted balance
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-176, T-167, T-166, T-221]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
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
| 1 | Read the reader's three *softening* limits back out of [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) §3 verbatim, and locate each in the binding as it stands today | the three, quoted, each with the line it sits on |
| 2 | Answer the third criterion first: diff limit 1 against its pre-[T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) text and judge whether the rewrite removed the softening **the reader actually named**, rather than whether the text improved | a recorded judgement in §3, quoting both versions' mechanism |
| 3 | Judge limit 2 — *The destination is gone and was never the evidence* — as softening or as an honest limit reasonably misread, against what the document elsewhere says can be checked | a recorded judgement, and if softening, the clause named |
| 4 | Make the change the owner already answered yes to, and any the judgements above warrant, sentence by sentence | the edited sentences in `github-issues.md` |
| 5 | State what would change the *no* on the arrangement | §3 |

**Step 2 goes before step 3 because it can invalidate the shape of this record.** If T-221's rewrite
did not touch the softening, then two limits stand and the *no* on the arrangement is under more
pressure than the owner's answer assumed. If it did, one limit stands and the question narrows. Either
way it is the step whose result changes what the rest is for, which is the sequencing rule.

**Step 2 judges the mechanism the reader named, not the prose.** The reader's words were *"the
softening creates the contradiction in question 3 rather than resolving it"* — so the test is whether
the contradiction is gone, not whether the paragraph now reads better. A rewrite can improve a
paragraph and leave its fault exactly where it was, and reading it fresh would not tell the
difference.

**Nothing here re-runs a reader.** §1 puts that out of scope and T-225 is the record of why: a second
reader after an unwelcome first is iteration, not measurement.

**Outputs**

- no new file. The answer's home is §3; the edits land in
  `plugin/skills/taskmd/docs/bindings/github-issues.md`

## 3. Implement

**Decisions & assumptions**

- **Finding 1, the arrangement: no, and the reason is T-167's own and not this record's** —
  2026-08-23. [T-167](T-167-stop-the-listing-pricing-only-the-rival.md)'s closing row states what
  would justify re-opening it, and states the negative first: *"not another reading of the same
  document — two runs have each found a fresh layer, and a third would too, which is the reason to
  stop rather than a reason to continue."*
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s run **is** that third
  reading. So the verdict does not re-open the balance, not because a reader's opinion counts for
  little, but because this exact evidence was named in advance as the kind that would not count. The
  owner's answer of 2026-08-22 and T-167's condition agree, and the condition is the better citation
  because it predates the result.
- **Finding 2, the one sentence: changed, as the owner answered** — 2026-08-23. *"It is a list of
  facts and it stops short of a recommendation"* claimed a neutrality the document cannot have. It now
  keeps the true half — the deciding facts are about your project — and adds that the selection and
  its order were made by the people who wrote taskmd, so *no selection made by an interested party is
  neutral because it declares itself to be*. That answers the reader's sentence directly: **declaring
  no opinion, in a document you wrote and ordered, is a position.**
- **Finding 3a, limit 1 — *True as behaviour, overstated as necessity* — is no longer softening**
  — 2026-08-23, and checked against both texts rather than assumed. **The reader's complaint was
  mechanical, not stylistic**: *"the softening creates the contradiction in question 3 rather than
  resolving it."* The contradiction was that the section's heading, its table row and its *either way*
  argument all said `check` gives you nothing, while this blockquote said five checks still run.
  [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) (`88b2cc1`)
  resolved it in **four** places, not one: the heading became *Three of the four commands do not come
  with you, and `check` half does*; the table row went from *nothing / Everything it checked is now
  unchecked* to *partly itself*, with the split named; the *either way* argument was narrowed to three
  commands with a paragraph saying `check` is not covered by it; and the blockquote was re-measured.
  **There is no longer a headline the blockquote quietly walks back**, which is what the softening
  was. The document also now carries the reader's own phrase as that annotation's heading, which is
  the opposite move.
- **Finding 3b, limit 2 — *The destination is gone and was never the evidence* — is softening, in one
  clause, and the clause is changed** — 2026-08-23. The reader: *"converts a missing artefact into a
  principle. You cannot check the runs. You can only rerun them."* Half of it is a real property: the
  comparison needs a source and a destination at the same moment, so it is genuinely a run-time check.
  **The overclaim is *and was never the evidence***, and the document refutes it three hundred lines
  earlier — *Verify* computes both its rows from the source's own id set against the destination, so a
  kept destination could have been re-compared by somebody else. The sentence now says the artefact is
  gone, that the rows are the runners' own record, and that keeping it **would** have allowed an
  independent re-comparison. *Rejected: leave it and record the judgement* — that is noticing a
  softening in a shipped document and moving on. *Rejected: delete the sentence* — the run-time
  property is true and worth stating, and deleting it would lose the honest half to fix the other.
- **The two edits are sentence-level and change nothing the owner's *no* protects** — 2026-08-23.
  Neither alters what the section lists nor the order it lists it in, which is what T-167 accepted.
  Named here so that reversing either is one line rather than an archaeology.

**Outputs produced**

- `plugin/skills/taskmd/docs/bindings/github-issues.md` — two sentences

**Verification**

**T-167's two re-opening conditions were tested rather than quoted, because a condition nobody checks
is the same as no condition.** They are *an adopter reporting that the listing pushed them* and
*[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) returning a
number that makes the unpriced side material rather than merely absent*.

- **The second has fired and did not trigger.** T-168 closed on 2026-08-18 with the number: **414
  characters** in the skill listing, the standing cost of keeping taskmd installed on a project with
  no tasks. The unpriced side is therefore priced, and 414 characters does not make it material —
  which is the condition failing to be met rather than never having been reached. The listing already
  carries that figure.
- **The first has not.** No adopter has reported being pushed. The nearest thing on the roster is a
  project that read the GitHub binding and **declined** to adopt it, which is evidence in the
  opposite direction.

**The edits were checked by running.** `taskmd check` exits 0, and the suite reports
`337 passed, 8 subtests passed` — the same figure as before the edits, so the two rewritten sentences
moved nothing the tests read. Both sentences were located by exact match before replacing, so neither
edit could land in a paragraph it was not meant for.

**What is not verified, said plainly.** Whether the two rewritten sentences read as less leaning *to
a reader* is unmeasured, and cannot be measured here: the only instrument is another reader, and
T-167 named a third reading as the thing that would not count. So this phase can show what changed
and why, and cannot show how it now lands.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is recorded with its reason, **in T-167's own terms** rather than in this task's | met | The reason given is T-167's closing condition verbatim — *not another reading of the same document* — and T-176's run is that third reading. Cited in preference to the owner's answer of 2026-08-22 because it predates the result, which is what makes it a rule rather than a reaction |
| Each of the three findings is answered separately | met | Four rows in §3, since finding 3 splits into the two limits it is about: arrangement **no**, the one sentence **yes and changed**, limit 1 **no longer softening**, limit 2 **softening and changed**. The decision was carried by finding 3b, which no single yes or no across the three would have shown |
| Whether T-221's rewrite changed how the third limit reads is checked against the text, not assumed | met | Diffed against `88b2cc1`. The rewrite touched **four** places, and the test applied was whether the mechanism the reader named — a contradiction the softening created rather than resolved — is gone, not whether the paragraph reads better. Judging the new prose fresh would not have separated those |
| If the answer is no, what would change it is stated | met | Not restated but **tested**: T-167's own two conditions. T-168 has returned its number, 414 characters, and it does not make the unpriced side material; no adopter has reported being pushed, and the nearest roster entry read the binding and declined. So the *no* stands on two conditions checked today rather than on a sentence nobody re-ran |

**Child fix tasks raised**
- none. Both changes were sentence-level and made in `implement`; nothing is carried.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds one, struck through and
answered by the owner on 2026-08-22. **One residual is recorded rather than left implicit**: §3 says
that whether the two rewritten sentences now read as less leaning is unmeasured and unmeasurable here,
because the only instrument is another reader and T-167 named a third reading as the evidence that
would not count. That is a limit of the answer, not a task — raising one would raise the very run both
T-167 and T-225 refuse.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | planned → done | **Closed: four criteria, four met, no child raised.** The answer is **no to the arrangement, yes to the one sentence, and one of the two remaining limits was softening after all.** **The strongest thing in it is not the verdict but its citation**: T-167 wrote down in advance that *another reading of the same document* would not re-open the balance, and T-176's run is exactly that third reading — so the *no* rests on a condition set before the result rather than on anyone's reaction to it. **T-221's rewrite did remove the softening the reader named**, checked by diffing `88b2cc1` and testing for the mechanism they described rather than reading the new prose, which improved in four places at once. **Limit 2 was softening and is changed**: *and was never the evidence* is refuted by the document's own *Verify*, which compares a destination against the source's id set — so a kept artefact could have been re-checked, and the clause converted a loss into a principle. **T-167's two re-opening conditions were run, not quoted**: T-168 has returned its number and 414 characters does not make the unpriced side material, and no adopter has reported being pushed — the nearest read the binding and declined. **`deliverables` now names the binding**, since this record produced two of its sentences. |
| 2026-08-23 | proposed → planned | **`specify` closed and `plan` written under the unattended grant.** `specify` needed nothing added: the owner answered on 2026-08-22 — no for the arrangement, yes for the one sentence — and explicitly left the third finding as judgement this record still has to do, which is a delegation rather than an open question, so the record does not stop. **The plan puts the third criterion first**, because whether [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s rewrite removed the softening decides whether one limit stands or two, and two would put the owner's *no* under pressure their answer did not weigh. **It also fixes what that step tests**: the reader's complaint was that the softening *creates a contradiction rather than resolving it*, so the test is whether the contradiction is gone — a rewrite can read better and leave the fault untouched, and judging the new prose fresh could not tell those apart. |
| 2026-08-22 | (no change) | **The grant was extended a third time**, to [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md), scoped there to finishing that record and not to building what it decides. The rows below are what the grant covered when each was written and are left as written; **T-234's own row carries the membership as it now stands**. Nothing about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task:** two of its three findings were answered on 2026-08-22. The third — whether the two remaining limits are softening, and whether T-221's rewrite changed how the third reads — is judgement made by reading the text, and it is this record's own work. **If that reading concludes the balance should change, it returns to the owner and stops here**: the answer of 2026-08-22 was that the arrangement stands. |
| 2026-08-22 | (no change) | **The owner answers two of the three findings: no for the arrangement, yes for the one sentence.** Answered 2026-08-22. **The arrangement stands** — [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) weighed it and accepted it, and a reader who calls the result a *mild* lean while separately crediting two sentences that cut against the tool has largely confirmed that decision rather than overturned it. ***"It is a list of facts and it stops short of a recommendation"* goes** — it is not a matter of proportion but a claim the document makes about itself, the reader's line on it is unanswerable (*"Declaring no opinion, in a document you wrote and ordered, is a position"*), and dropping it costs nothing the section needs. *Rejected: re-balance on the verdict* — it would reverse an owner decision on evidence collected for another purpose, which is the thing [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s Log forbade in advance. *Rejected: change nothing* — it treats every finding as proportion when one is not. **The third finding is not covered and is this record's own work**: whether the two remaining limits are softening, and whether T-221's rewrite of the third changed how it reads. That is judgement made by reading the text, and it returns to the owner only if it changes the balance. |
| 2026-08-22 | → proposed | Raised by [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s fifth criterion, which requires anything the reader turned up outside that task's scope to leave as its own task rather than be repaired where it was found. Three findings had no home: the located lean, the *declaring no opinion* line, and two limits still reading as softening. **A decision rather than a fix**, by the schema's own test — the outcome is an answer somebody else could act on, and any change follows from it. **Raised with its default answer stated**: an accepted decision is not reversed by a reader's opinion, and the reason to put it up anyway is that the evidence is new, came from outside, and was collected without the reader knowing framing was the subject. **The unmeasured half is the one to watch** — [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) rewrote one of the three limits the same day for an unrelated reason, and whether that removed the softening is nobody's finding yet. |
