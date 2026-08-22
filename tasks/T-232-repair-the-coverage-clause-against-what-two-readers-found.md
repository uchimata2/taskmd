---
id: T-232
title: Repair the coverage clause against what two readers found
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-225, T-222, T-199, T-231, T-233]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/BINDING.md
---

# T-232 — Repair the coverage clause against what two readers found

## 1. Specify

**Outcome**
`plugin/skills/taskmd/docs/BINDING.md` §4 answers what
[T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md)'s two
readers had to settle by guessing — including the one question on which they settled it differently.

**Why this one**
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) repaired
eight defects on 2026-08-22 and T-225 measured the repair the same day, against a pass bar fixed
before the prompt existed. **The verdict is FAIL on the first half of that bar**, and the reason is
worth more than the verdict: seven of the eight held under readers trying to break them, one recurred
in a sharper form, and **the repair introduced a defect that only two readers could reveal**.

**The four findings, ranked by what stands behind each.**

1. **Which fact chooses the closing line — both readers, and confirmed by reading the paragraph.**
   The repair named the two forms and left the choice keyed on the project in one sentence
   (*the adopter kept a working copy*) and on the backend in the next (*a binding whose backend is
   remote-only*). A remote backend with a local mirror falls between them and is unanswerable.
2. **The section's heading and position — both readers.** *A section of its own* gives no title, no
   heading level, and no rule about where in the binding it goes. One reader asked for all three;
   the other invented a heading and asked for a canonical one.
3. **Are the two named classes examples, or the set? The readers diverged, and it changed a
   declaration.** Reader A declared only `STALE INDEX` and `DUPLICATE ID`, *"because they were
   explicitly identified in Section 4"*. Reader B read them as examples and wrote a paragraph
   declaring the gap. **Both declarations are shippable and they claim different things**, and no
   check can tell them apart, because every name in A's region is a real class.
4. **The scan's rule is described by measurement rather than stated — one reader, and it explains
   the other's mistake.** The paragraph reports what four specimens did instead of writing the rule,
   so an identifier like a team key plus number, a mixed-case name and a bare two-letter word are all
   unanswerable. The same paragraph carries the acronym rule explicitly, and Reader A missed it and
   asked for it — one paragraph, two readers, two symptoms.

Fifteen further questions came from Reader B alone, one mention each; they are listed in T-225 §3 and
are inputs here rather than a separate task.

**The tension this repair has to hold, and it is why finding 3 is not a one-line fix.** T-222 named
two classes *because* the clause naming none was defect 1 — a reader who described the stale-index
state correctly and then could not name it. Removing the names re-opens that. Keeping them as written
leaves an illustration that reads as an inventory. **The repair must make the clause name classes
without reading as a list**, and a repair that solves finding 3 by deleting the names has traded one
measured defect for another.

**Scope**
- In: the four findings above, and the fifteen single-mention questions in T-225 §3, each repaired or
  declined **by name** with a reason for each decline
- In: whether either shipped binding is left non-compliant by the repair — **reported, not fixed**,
  for T-222's reason: editing a binding inside the task that changed the contract hides which moved
- Out: the readers' assumptions about **their** chosen backend. Reader B named three it had not
  verified and said so; they are facts about a service and are not this document's to settle
- Out: enumerating the validator's class list, which §4's own anti-table argument forbids and which
  T-222 was held to
- Out: changing the validator, its classes, or the marked-region check
- Out: running a third reader. That is a decision, not a step, and it is an open question below

**Inputs**
- [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) §3 —
  both declarations verbatim, the eight walked one by one, and the divergence
- [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) §3 — what
  each of the eight was repaired to, and the two decisions findings 1 and 3 are about
- `plugin/skills/taskmd/docs/BINDING.md` §4 as it stands after 2026-08-22

**Acceptance criteria**
- [ ] Each of the four findings is repaired or declined **by name**, and every decline carries a reason
- [ ] The closing-line rule says **which fact decides**, and answers the remote-backend-with-a-local-
      mirror case that falls between the current two sentences
- [ ] Whether the named classes are examples or the set is unambiguous from the text alone — **and
      defect 1 is not re-opened**, which a reviewer checks by confirming the clause still names them
- [ ] The scan is described by its **rule**, and the rule answers the three shapes no reader could
      resolve from the measurement
- [ ] Each of the fifteen single-mention questions is answered or declined by name
- [ ] Both shipped bindings are checked against the repaired clause and any non-compliance is named

**Open questions**
- ~~**Does this block the release?** — the project owner. `BINDING.md` ships, and
  [T-231](T-231-cut-the-next-release.md) would publish this clause with a measured failing verdict
  against it. The recommendation is **yes, block it**: the defect is in a contract every binding
  inherits, the repair is `m` rather than `l`, and the alternative is shipping a document this
  project has already measured and found wanting. Against: nothing an adopter meets is *wrong* — one
  reader under-declared and both shipped — so the cost of shipping is a worse binding somebody writes
  later, not a broken one today.~~ **Answered 2026-08-22: yes.** [T-231](T-231-cut-the-next-release.md) carries `blocked_by` naming this record. See the Log row of that date.
- **What tests this repair, given a third reader is the obvious answer and probably the wrong one?**
  — the project owner. The recommendation is **not a third reader by default**: the same instrument a
  third time is the loop T-225 §1 warns about. Finding 3 suggests a test that is different in kind —
  give two readers the repaired clause and check whether they now declare the **same** set, which is
  what actually failed. That is still two readers, so the count rule needs settling first.

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
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it, and **extended that grant to this record later the same day** — because holding the release behind a repair nobody was authorised to do would have left the release waiting on one person. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total, as extended:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md), [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) and this record, and nothing else. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), which this record unblocks but which is the owner's act to make; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit** — no umbrella may be raised and none started. **It authorises phases, not answers.** **Specific to this task:** §1 fixes the shape and the grant does not loosen it — the repair must make the clause **name** classes without reading as an inventory, and one that solves finding 3 by deleting the names has traded one measured defect for another. The scope is T-225's findings and the fifteen single-mention questions; nothing [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) settled is re-opened. **The one remaining open question does not stop this record**, and that is stated so a session does not stall on it: *what tests this repair* is put out of scope by §1 in the same breath as it is asked, so it is recorded as a follow-on decision and closure does not wait on it. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). |
| 2026-08-22 | (no change) | **The owner answers the first open question: yes, this blocks the release.** [T-231](T-231-cut-the-next-release.md) now carries `blocked_by` naming this record, so the ordering rule sorts it last and reports it blocked rather than a session having to remember a sentence. **What that commits to**: the repair is on the critical path of a release the owner wants soon, so its scope is the four findings and the fifteen single-mention questions, and not a re-opening of anything T-222 settled. **The second open question is untouched and now has a record beside it** — what tests this repair, where the obvious answer is a third reader and the obvious answer is probably the loop T-225 was built to avoid. [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md) settles the count rule that question waits on; it is a soft edge because the repair itself does not wait on it, only its test does. |
| 2026-08-22 | → proposed | Raised from [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md)'s run, whose §1 puts repairing out of scope by name — a clause repaired inside the task measuring it has been tested against nothing. **`high`, and higher than the defect count suggests**: one of the four findings is a defect the previous repair *introduced*, and its failure mode is silent under-declaration that no check can see, because every class name involved is real. **The verdict it comes from is a FAIL against a bar written before the prompt existed**, which is the only reason the fail can be trusted rather than argued with. **Two questions go up rather than being decided here**: whether this blocks [T-231](T-231-cut-the-next-release.md), since the clause ships and would ship measured-and-failing; and what tests the repair, where the obvious answer is a third reader and the obvious answer is probably the loop T-225 was built to avoid. **Not in the unattended grant of 2026-08-22** — that grant names five records and this is not one, and its scope was fixed before this run existed. |
