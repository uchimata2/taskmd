---
id: T-232
title: Repair the coverage clause against what two readers found
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-225, T-222, T-199, T-231, T-233]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-23
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
- [ ] Each of the **nineteen** contract questions Reader B recorded is answered or declined by name
      — *original text, 2026-08-22: "Each of the fifteen single-mention questions is answered or
      declined by name". Corrected 2026-08-23 by
      [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md),
      which supplied the set and showed fifteen was a count of table rows. Corrected upward, so it
      asks for more than it did.*
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
- **Criterion 5 names a set that does not exist, so what should it be?** — the **project owner**,
  who agreed it. *the fifteen single-mention questions in T-225 §3* were looked for on 2026-08-23 and
  **§3 lists none of them**: it carries the two declarations, the eight walked one by one and the
  divergence, with six of Reader B's questions inline in that walk and no group beyond them. T-225 §4
  says nineteen and this record says fifteen; 19 − 6 = 13, and no list of any size is written
  anywhere, `control/` included. Raised as
  [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md),
  which now blocks this record. **Recommendation: narrow criterion 5 to the six questions T-225 §3
  actually names**, unless the owner still holds the run output — in which case it goes into T-225 as
  an annexe and the criterion stands unchanged. *Rejected: answer whichever questions this session can
  find and tick the criterion* — that is silent under-coverage recorded as coverage, which is the
  defect this whole record exists to repair, reproduced in its own review.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the scan's rule out of the code rather than out of the paragraph describing it, since finding 4 is that the paragraph describes behaviour instead of stating a rule | the pattern, and what it does to the three shapes no specimen covered |
| 2 | Fix the two findings that are one-way repairs — the closing-line fact, and the heading, level and position | the edited clause |
| 3 | Fix finding 3 without re-opening defect 1: make the two named classes read as examples **while still naming them** | the edited clause, with both names still in it |
| 4 | Answer the remaining contract questions in the clause, each by name | the edited clause |
| 5 | Measure both shipped bindings against the repaired clause and **report**, never fix | what each complies with |
| 6 | Run `check` and the publishing suite, which is what reads the marked regions | the outputs |

**Step 1 first, because finding 4's repair cannot be written from the document.** The paragraph
reports what four specimens did; the three shapes the reader could not resolve are exactly the ones no
specimen covered, so the answer is only in the code.

**Step 3 is the one with a trap, and §1 names it.** A repair that solves *examples or the set* by
deleting the names re-opens defect 1 — a reader describing the stale-index state correctly and then
guessing what it is called. So the test is that both names survive the edit.

**Step 5 reports and does not fix**, for T-222's reason: editing a binding inside the task that
changed the contract hides which of the two moved.

**Outputs**

- `plugin/skills/taskmd/docs/BINDING.md` — §4

## 3. Implement

**Decisions & assumptions**

- **Finding 3 was repaired by saying it outright, not by removing the names** — 2026-08-23. The clause
  now states that the two worked classes are examples and that **a declaration naming only them is
  incomplete by definition**, and it cites the measurement: two readers, one declaring exactly those
  two *"because they were explicitly identified in Section 4"*. Both names survive, so defect 1 is not
  re-opened. *Rejected: drop the names and describe the states* — that is defect 1 verbatim.
  *Rejected: keep the names and add nothing* — it is the state that produced two shippable
  declarations claiming different things.
- **The closing line keys on one fact, and it is neither of the two the clause used** — 2026-08-23.
  Not *the adopter kept a working copy* (a fact about them) and not *the backend is remote-only* (a
  fact about the service). It is **whether documents the validator can walk are still on disk after
  the move**, which answers the remote-backend-with-a-local-mirror case that fell between the old two
  sentences.
- **The heading, level and position are the ones `local-markdown.md` already used** — 2026-08-23,
  which is why they are chosen rather than invented. Measured against both shipped bindings before
  choosing; see *Verification*.
- **The scan's rule was taken from the code, and it corrects the paragraph in one place** — 2026-08-23.
  The old text said *a single two-letter word is still not a class name and still does not match*,
  which is true of the scan and misleading on its own: the guard counting from the other side **does**
  report such a token, because it is capitals throughout and the scan cannot read it. The clause now
  says both halves.
- **Reader B's three Linear assumptions are declined by name** — 2026-08-23. Items 20, 21 and 22 are
  facts about a service, and §1 puts them out of scope: *they are facts about a service and are not
  this document's to settle*. The reader said the same thing about them unprompted, which is the
  clause's *hygiene is not truth* paragraph working.

**Outputs produced**

- `plugin/skills/taskmd/docs/BINDING.md` — §4

**Verification**

**The four findings.**

| # | Finding | Repair |
| :-- | :--- | :--- |
| 1 | which fact chooses the closing line | One fact named — documents still on disk — with the two forms as a two-item list, and the mirror case answered explicitly |
| 2 | the section's heading and position | `What the validator cannot check here`, at `###`, after the mapping section and before the write step. All three stated |
| 3 | examples, or the set | Stated outright, with the measurement behind it. **Both names survive**: a sweep of the section returns `STALE INDEX` twice and `DUPLICATE ID` twice |
| 4 | the scan described by measurement | Replaced with the rule and a six-row table covering every shape a reader raised |

**All nineteen contract questions, each answered by name.** None declined.

| # | Answer now in the clause |
| :-- | :--- |
| 1 | whether documents remain on disk decides the closing form |
| 2 | the line is a sense, not boilerplate; nothing mechanical reads it |
| 3 | it sits inside the markers |
| 4 | heading `What the validator cannot check here` |
| 5 | after the mapping section, before the write step |
| 6 | the lead carries the names, not a count |
| 7 | per-class reasoning is required, a short paragraph each |
| 8 | restate the mapping-not-service point once per affected class |
| 9 | a specimen gap sentence, and: describe no unnamed state |
| 10 | a declaration built from this page's two names is incomplete by definition |
| 11 | examples, not the set |
| 12 | state the property — no second copy of the list — not the instance |
| 13 | a claim may rest on the mapping forbidding something; the prohibition lives in the mapping section |
| 14 | point at the *derived / materialised* entry rather than duplicating it |
| 15 | the *hygiene, not truth* sentence is required in every declaration |
| 16 | the pattern written out, with `ENG-42`, `GraphQL` and a two-letter run each given a row |
| 17 | the region is the declaration, not only its classified part |
| 18 | bindings number no sections; cite by name and never as `§3` |
| 19 | an optional fuller table must be complete or not attempted |

**Items 20 to 22 are declined by name**, being assumptions about Linear: identifier uniqueness,
non-editability, and key churn on a team move. §1 puts a reader's assumptions about their own backend
out of scope, and the reader volunteered that these are the part they had least right to assert.

**Step 5 — both shipped bindings measured against the repaired clause, and reported.**

| Binding | Heading | Level | Position |
| :--- | :---: | :---: | :--- |
| `local-markdown.md` | matches | `###` | after *Operations*, before *After any write* — **matches** |
| `github-issues.md` | **no** — *What this does not cover, and why* | **no** — `####` | **no** — after its *After any write*, inside the migration-verification material |

**`github-issues.md` is left non-compliant on all three and is not touched here**, which is §1's
instruction and T-222's reason: a binding edited inside the task that changed the contract makes it
impossible to see which of the two moved. Raised as its own record.

**Step 6 — the gates.**

```text
taskmd check                        ->  exit 0
python -m pytest tests/test_publishing.py -q  ->  21 passed
```

`test_publishing.py` is the one that reads the marked regions, and it is the check that would fail if
this edit had put an unreadable capitalised token inside one. **The clause's own new table backticks
`API`, `JQL` and `ID` deliberately**, and that is safe because the region scan runs over bindings and
`BINDING.md` is not one — a document explaining a scanner is the classic way to trip it, and this one
was checked rather than assumed.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each of the four findings is repaired or declined **by name**, and every decline carries a reason | met | Four repaired, none declined. The table in §3 names each with what was done |
| The closing-line rule says **which fact decides**, and answers the remote-backend-with-a-local-mirror case | met | One fact — whether documents the validator can walk are still on disk — with the mirror case answered in its own sentence, because that case is what fell between the old two |
| Whether the named classes are examples or the set is unambiguous from the text alone — **and defect 1 is not re-opened**, checked by confirming the clause still names them | met | Both halves. The clause says *examples of the reasoning, not the set* and *incomplete by definition*; a sweep of the section returns `STALE INDEX` twice and `DUPLICATE ID` twice, so the names are still there |
| The scan is described by its **rule**, and the rule answers the three shapes no reader could resolve | met | Taken from the code, not the paragraph. `ENG-42`, `GraphQL` and a bare two-letter run each have a row — and the two-letter row carries the half the old text got wrong: the scan does not read it and the guard reports it anyway |
| Each of the **nineteen** contract questions is answered or declined by name | met | Nineteen answered, none declined; the table in §3 is one row per question. Items 20–22 are declined by name as assumptions about Linear, which §1 excludes |
| Both shipped bindings are checked against the repaired clause and any non-compliance is named | met | Measured, not assumed. `local-markdown.md` matches all three — which is why those are the canonical values rather than invented ones — and `github-issues.md` matches none. Reported, not fixed |

**Child fix tasks raised**
- [T-238](T-238-bring-the-github-binding-s-coverage-declaration-into-line-with-the-repaired-clause.md)
  — `github-issues.md`'s declaration, non-compliant on heading, level and position. **A soft edge and
  not a child**: this record's outcome is the contract, and the contract is complete; a binding that
  has not caught up does not make it incomplete, and a hierarchy edge would hold the release's
  blocker open for an edit to something else.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds two. The first is struck
through and answered. **The second — *what tests this repair* — is answered today rather than carried
forward**: [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md)
settled the count rule on 2026-08-23 as **two readers in parallel, fixed in advance**, which is the
test that differs in kind from the one that failed — it measures whether two readers now declare the
**same** set, which is exactly what diverged. Running it is T-233's protocol and the owner's to
schedule, and §1 already says closure does not wait on it.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | blocked → done | **Closed: six criteria, six met. The release's blocker is clear.** Unblocked when the owner supplied Reader B's reply and [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md) put it in T-225 §3. **All four findings repaired and all nineteen contract questions answered by name**, one row each in §3; items 20–22 declined by name as assumptions about Linear. **Finding 3 was repaired by saying it outright rather than by deleting the names** — the clause now says the two worked classes are examples and that a declaration naming only them is incomplete by definition, and both names survive, so defect 1 is not re-opened. **The closing line keys on a fact neither old sentence used**: whether documents the validator can walk are still on disk, which is what answers the mirror case that fell between them. **Finding 4's repair came from the code**, and it corrected the paragraph in one place nobody had noticed — a two-letter token is not read by the scan **and is reported anyway** by the guard counting from the other side. **The canonical heading, level and position are the ones `local-markdown.md` already used**, measured before choosing; `github-issues.md` matches none of the three and is reported rather than fixed, as [T-238](T-238-bring-the-github-binding-s-coverage-declaration-into-line-with-the-repaired-clause.md). **The second open question is answered rather than carried**: T-233 settled the count rule the same day, so the test that differs in kind now exists. |
| 2026-08-23 | proposed → blocked | **`specify` cannot close: the fifth criterion names a set nobody can enumerate.** Worked under the unattended grant, and stopped by the rule the grant states rather than by the grant running out — *it authorises phases, not answers*, and the question is the owner's twice over: they ran the readers, and they agreed the criterion. **What was checked before calling it a finding**, because a scope line is a poor thing to contradict: T-225 §3 was read whole; its six inline mentions of Reader B's questions were counted in rows 3, 4, 6 and 7; the tree was swept for `fifteen` and `nineteen`; and `control/` was opened, being gitignored and the one home a sweep forgets. No list exists. **The three counts are 19, 6 and 15 and none derives from another.** Raised as [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md) and recorded as `blocked_by`, so the release path shows where it actually stops instead of a sentence saying so. **A dependency and not a child**: this record's outcome is `BINDING.md` §4 and is not incomplete without T-235 — it cannot *proceed* until criterion 5 has a set or has been withdrawn. **The other five criteria were not started**, and that is the phase rule rather than caution: a `specify` whose outcome is still moving cannot be exited, and repairing four findings against a sixth criterion nobody has settled would decide the owner's question by making it expensive to answer. **Nothing in T-225 was edited**; its review note is wrong about the present and correcting it is T-235's first criterion, not a tidy-up taken on the way past. |
| 2026-08-22 | (no change) | **The grant was extended a third time**, to [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md), scoped there to finishing that record and not to building what it decides. The rows below are what the grant covered when each was written and are left as written; **T-234's own row carries the membership as it now stands**. Nothing about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it, and **extended that grant to this record later the same day** — because holding the release behind a repair nobody was authorised to do would have left the release waiting on one person. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total, as extended:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md), [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) and this record, and nothing else. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), which this record unblocks but which is the owner's act to make; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit** — no umbrella may be raised and none started. **It authorises phases, not answers.** **Specific to this task:** §1 fixes the shape and the grant does not loosen it — the repair must make the clause **name** classes without reading as an inventory, and one that solves finding 3 by deleting the names has traded one measured defect for another. The scope is T-225's findings and the fifteen single-mention questions; nothing [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) settled is re-opened. **The one remaining open question does not stop this record**, and that is stated so a session does not stall on it: *what tests this repair* is put out of scope by §1 in the same breath as it is asked, so it is recorded as a follow-on decision and closure does not wait on it. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). |
| 2026-08-22 | (no change) | **The owner answers the first open question: yes, this blocks the release.** [T-231](T-231-cut-the-next-release.md) now carries `blocked_by` naming this record, so the ordering rule sorts it last and reports it blocked rather than a session having to remember a sentence. **What that commits to**: the repair is on the critical path of a release the owner wants soon, so its scope is the four findings and the fifteen single-mention questions, and not a re-opening of anything T-222 settled. **The second open question is untouched and now has a record beside it** — what tests this repair, where the obvious answer is a third reader and the obvious answer is probably the loop T-225 was built to avoid. [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md) settles the count rule that question waits on; it is a soft edge because the repair itself does not wait on it, only its test does. |
| 2026-08-22 | → proposed | Raised from [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md)'s run, whose §1 puts repairing out of scope by name — a clause repaired inside the task measuring it has been tested against nothing. **`high`, and higher than the defect count suggests**: one of the four findings is a defect the previous repair *introduced*, and its failure mode is silent under-declaration that no check can see, because every class name involved is real. **The verdict it comes from is a FAIL against a bar written before the prompt existed**, which is the only reason the fail can be trusted rather than argued with. **Two questions go up rather than being decided here**: whether this blocks [T-231](T-231-cut-the-next-release.md), since the clause ships and would ship measured-and-failing; and what tests the repair, where the obvious answer is a third reader and the obvious answer is probably the loop T-225 was built to avoid. **Not in the unattended grant of 2026-08-22** — that grant names five records and this is not one, and its scope was fixed before this run existed. |
