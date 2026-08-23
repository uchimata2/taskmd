---
id: T-166
title: Stop the post-migration listing framing toward keeping taskmd
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-163, T-165, T-108]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-17
updated: 2026-08-17
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
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

**The evidence cannot be cited — it has to be restated.** The listing lives inside `plugin/`, and the
run that proves the operations is in
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3, which an install
does not receive. `test_no_relative_path_in_the_plugin_climbs_out_of_it` fails a link out of the
subtree, and a bare `T-108` passes every test while resolving to nothing an adopter holds — the worse
of the two failures, because it is silent. So the survivor claim carries the **dated result and its
counts** in its own words. This is the same boundary that caught T-108's own reverse-direction
sentence, which was sound reasoning and still unshippable.

**Acceptance criteria**
- [ ] A **fresh** uninvolved reader — spawned at `review`, given the edited listing standalone and
      nothing else, asked [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s
      four questions unchanged — does **not** answer that the document argues for an answer, in
      either direction. *Fails if* they name a lean **and** a mechanism in the document for it.
- [ ] Each of the three mechanisms T-165 named — the *What is gone* section, the *what was never
      local* heading, the disclaimer — is answered by a change in the document, and §3 names the
      change and the mechanism it answers. *Fails if* a mechanism has no corresponding edit, or the
      record leaves the reader to work out which edit answered what.
- [ ] At least one survivor claim rests on the operations having been **run**: the date, the
      destination's nature, and the counts, restated in the document. *Fails if* the claim cites
      anything outside `plugin/`, or if `by construction` still carries a claim a run could have
      settled and did not.
- [ ] The disclaimer is still present and no longer buys trust. *Fails if* it was deleted, or if it
      still volunteers the conflict of interest ahead of any reason to doubt.
- [ ] The closing menu's third outcome — *keep both deliberately* — is decided either way, with the
      rationale recorded. *Fails if* it is left standing with no decision written down.
- [ ] Every claim in the edited listing is still a measured output or a pointer, the property
      [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 established. *Fails if*
      the repair introduces an assertion with no source — a neutral document that has stopped being
      checkable is a worse artefact than the leaning one.
- [ ] The suite, `check` and `index` are green. *Fails if* any of the three reports a problem —
      `test_no_relative_path_in_the_plugin_climbs_out_of_it` and
      `test_no_file_in_the_plugin_cites_something_it_does_not_ship` are the two that this task's
      shape puts at risk.

**Open questions**
- **How is this judged? Answered by the maintainer, 2026-08-17: `review` spawns a fresh reader, same
  protocol.** One, not the T-165 reader, given the same four questions. *Rejected: re-use the T-165
  reader* — they hold the objections, so they can only confirm the objections were addressed, which
  is the definition of tuned. *Rejected: no new reader, check the three mechanisms instead* — that is
  the claim-by-claim substitute T-165 §3 already showed cannot see framing, and it passed this very
  document.
- **What verdict passes, decided here rather than asked:** no lean, **or** a lean the reader cannot
  ground in a mechanism of the document. An impression a reader cannot attribute is not something an
  edit can act on. *Rejected: no lean at all* — unfalsifiable in practice and it invites editing
  until a reader says the agreeable thing, which is the failure this task exists to stop.
  *Rejected: the three mechanisms are gone, whatever the verdict* — same defect as the rejected
  option above. Raise it if this bar is wrong; it is one line to change and it decides closure.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide the closing menu's third outcome — whether *keep both deliberately* stays, goes, or is reframed. It comes first because it decides whether the closing section is edited or rewritten | A decision in §3, with what it rejects |
| 2 | Work out which of [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3's facts a document inside `plugin/` may state on its own, and which die at the boundary | The usable facts, and a note of anything dropped and why |
| 3 | Rewrite the survivor section so at least one claim rests on step 2's run rather than on *by construction*, and retitle the heading that reframes losing the commands as incidental | The edited *What survives…* section, heading included |
| 4 | Reframe *What is gone* so each loss says what keeping taskmd would and would not restore — the reader's first mechanism, which is placement rather than falsehood | The edited *What is gone…* section |
| 5 | Rewrite the disclaimer so it stops buying trust, without deleting it | The edited *If this is not enough…* section |
| 6 | Apply step 1's decision to the closing paragraph | The edited final paragraph |
| 7 | Re-walk every claim in the edited listing: still a measured output or a pointer, and no pointer leaves `plugin/` | The walk's result, in §3 |
| 8 | Run the suite, `check` and `index` | The three outputs, in §3 |
| 9 | Spawn a fresh uninvolved reader — the edited listing standalone, nothing else, [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s four questions unchanged — and record the answer verbatim enough to be re-read, including what disagrees with us | The finding, in §3 |

**Decisions taken at `plan`**

- **The repair is edits in place to three sections of one shipped document, not a rewrite of the
  listing** — 2026-08-17. *Rejected: rewrite the listing whole.* It is the tempting shape, because the
  defect is structural rather than sentence-level. It would also make the reader test at step 9
  uninterpretable: with everything changed at once, a passing verdict cannot say which mechanism it
  answered, and a failing one cannot say which edit to undo. It would additionally throw away
  [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3's per-claim measurement,
  which is not in dispute and which criterion 6 requires to survive.
- **Step 9 sits in `implement`, not in `review`** — 2026-08-17. The reader is the outcome being *used*,
  which is [`../plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §2's
  exit criterion for `implement`; `review` then judges all seven criteria, reading criterion 1 off the
  evidence step 9 produced. *Rejected: run the reader at `review`* — it would make `review` the place
  where verification happens, which is the arrangement METHOD §2 names and refuses.
- **Steps 3–6 change no fact in the commands table** — 2026-08-17. That table is the half the reader
  found trustworthy and the half T-163 measured. Touching it to improve balance would trade the
  document's one uncontested asset for the appearance of neutrality.

**Outputs this task will produce**

- plugin/skills/taskmd/docs/bindings/github-issues.md — the sections *What survives…*, *What is
  gone…*, and *If this is not enough…*
- the reader's finding, in §3 of this record

## 3. Implement

**Step 1 — the closing menu keeps its third outcome, and stops being free.** *Keep both* is a real
answer and removing it to look even-handed trades one distortion for a worse one. What the reader
actually caught was that the document states the overlap's cost against a rival skill and then drops
it at the moment of choosing, so the menu reads as three equal ends. The cost now travels with the
option. *Rejected: cut the third outcome* — dishonest. *Rejected: leave it* — the sentence
*the listing exists so that the third option is a decision rather than an accident* made keeping both
the document's stated purpose, which is the strongest possible endorsement of it.

**Step 2 found something better than restating, and it changed step 3.** The plan assumed the run had
to be described again inside `plugin/`, because
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 is not shipped.
Reading the binding showed the run has **no home in the shipped document at all** — *Verify* carries
two measurements from it (`gh` 2.96.0, the eight spurious failures) and never says the procedure was
run. So the fact got its one home, `What this procedure has been run against`, placed where *Verify*
can be read against it, and the survivor claim points **within the document**. One write, no second
copy, and no pointer that leaves the plugin. Facts deliberately dropped at the boundary: the task id,
and the destination repository's name — it is deleted, so naming it buys a reader nothing and costs
the publishing constraint.

**The suite caught a stale index, which is the mechanism working.** The first run after the document
edits reported `FAILED (failures=7, skipped=3)`. The cause was `T-166`'s own front-matter moving
`proposed → in_progress` without `index` being re-run; regenerating it and changing nothing else gave
`Ran 270 tests in 28.411s / OK (skipped=3)`. Recorded rather than quietly fixed because the seven
failures named a task file and not the document under edit, which is the moment it would be easy to
go looking in the wrong place.

**Step 7 — the claim walk.** Every claim in the edited listing is a measured output (`exit=2` and its
error text, dated), an in-document pointer (*read*, *enumerate*, *After any write*, *What this
procedure has been run against*), or a document a reader holds and can open (the method, the binding,
the schema). Two duplicates removed on the way: `by construction` on the method bullet, replaced by
the property that makes it checkable, and a second statement of the overlap's cost in the closing
paragraph, replaced by a pointer to the first.

**Steps 3–6 — which edit answers which mechanism.**

| [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s mechanism | The edit |
| :--- | :--- |
| *What is gone* argues against the migration rather than about the tool | The section now opens by saying none of the three is a reason to keep taskmd, because the commands exit 2 either way, so they are costs of the move and already paid |
| The heading *What survives, and it is the part that was never local* reframes losing the whole executable surface as incidental | Retitled to *What survives*. The editorial clause was the whole mechanism |
| The disclaimer buys trust | The self-characterisation is gone; the paragraph states what the document has, and the conflict of interest now follows the facts as a reason to check one at random rather than preceding them as a reason to believe |

The listing's intro lost the same move in miniature — *the tool is the last thing that should be
making it* — replaced by why it cannot make the judgement: it holds none of the facts that would
decide it.

**Step 9 — the reader, and the decision that governs it.** **One reader, one run, and the verdict
stands.** Editing against the objections of a reader you have already heard and spawning a second is
this task's own defect performed one turn later, and it is how a document gets tuned while every
individual reader stays fresh. So a failing verdict is a finding that leaves as its own task; it is
not a retry. *Rejected: iterate until a reader passes it* — it cannot fail, which makes the test
decorative.

**The extraction changed, and the reason matters.**
[T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) gave the reader the
listing section alone. The repair's central move is a pointer to a section *above* the listing, so
that slice would have tested a document nobody receives — the reader would meet the citation and not
its referent, which is the exact failure being repaired. The whole binding was extracted instead
(26,226 characters, verbatim, to a scratch path outside the repository, with the instruction to open
nothing else). That also removes the last selection decision from the author of the edits, which is
the thing under test. Everything else held: a fresh reader, the four questions unchanged, *sales
pitch* offered as an available answer, and no mention that neutrality was being measured.

**The maintainer's answer said "at `review`"; the reader ran at `implement`.** The instrument, the
protocol, the count and its position before closure are all unchanged — what moved is which phase
owns it, on
[`../plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §2, and the
one-run rule above is what stops that move turning verification into iteration. Flagged rather than
absorbed.

**The result: it still argues, softly, toward keep — and not for any of the three reasons.**

The three mechanisms [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)
found are gone, and the reader confirmed two of them from the other side without being asked. On
*What is gone*: "The three named losses — no validator, no ordering rule, no offline copy — are
correctly excluded from this decision, and the document says so ... Don't let anyone on your team
relitigate that; it's right." On the disclaimer: "Not a sales pitch. It's more honest than most
documents of its kind, and it still has a thumb on the scale."

Asked whether it argues for an answer, they said **yes, softly, toward keeping**, and named five
mechanisms — **all five new**:

1. **The listing's own heading, `What taskmd still gives you here`**, presupposes that it gives you
   something and "sets the reader's question to *what remains?* instead of *is what remains worth the
   standing cost?*" Under it, three of the four survivors are things you keep after deleting taskmd.
2. **The dead-command table's third column, `What that costs you`.** Three of its four rows lead with
   a minimiser — *Nothing material*, *Nothing*, *The enumeration survives* — turning "four commands,
   four exit-2s" into a graded loss where most of it does not matter.
3. **The verb *survives*.** "A Markdown file in your repo did not survive anything; it was never at
   risk. Borrowing the migration's drama makes inertness read as resilience."
4. **The asymmetry that is the sharpest of the five.** The document knows the unit of cost — the
   overlap paid on every session — and spends it **only** against a hypothetical rival skill. It
   prices keeping both. "It never once prices keeping taskmd alone, though the same meter is running."
5. **Placement.** The installation question is the last section of a long, rigorously evidenced spec,
   so "whatever survives the migration inherits the halo of the section that proved the migration."

**Their decisive missing fact is the same shape as last time, and it lands on the one unevidenced
claim.** They asked whether the skill still fires, and still routes to this binding, in a repository
with no task folder — and what that costs per session. Their argument for why that gap is decisive
rather than a nitpick is worth keeping whole: the document "is obsessive about evidence" — `gh`
2.96.0, 165 tasks, 28 labels, `FAIL, 324` then `FAIL, 8` then `PASS`, the exit code quoted with its
error text — "and the single claim carrying the entire installation decision — *The skill that routes
an agent through them* — has no command, no measurement, no exit code, and no source." Three of the
four survivors are documents, which need nothing installed; the fourth is the only one installation
buys, and it is four words.

**Their recommendation was uninstall**, on the reasoning that the method and the binding can be copied
into the adopter's own repository — which the document itself says, and which the binding's own
*homes* mapping already assumes. That is the listing working: a reader reached a decision and named
what would change it.

**Decisions & assumptions**

- **The closing menu keeps three outcomes; the third carries its cost** — 2026-08-17, step 1 above.
- **The run's evidence gets one home in the shipped document and is pointed at, not restated** —
  2026-08-17, step 2 above.
- **One reader, one run; a failing verdict leaves as its own task** — 2026-08-17, step 9 above.
- **The five new mechanisms are not repaired here** — 2026-08-17. They arrived from the measurement
  this task's outcome had to survive, and repairing them in the same breath destroys the evidence
  that the measurement happened — which is the reasoning that raised this task out of
  [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) rather than fixing it
  there. They leave as [T-167](T-167-stop-the-listing-pricing-only-the-rival.md), gated on
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md). *Rejected:
  fix mechanisms 1, 2, 3 and 5 now and leave only the pricing* — it is the same substitution in a
  smaller frame, and it would leave the next reader unable to tell which edits their verdict judged.

**Outputs produced**
- plugin/skills/taskmd/docs/bindings/github-issues.md — `What this procedure has been run against`
  (new), and the three edited sections of the listing
- the reader's finding, above

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A fresh uninvolved reader does not answer that the document argues for an answer | **FAIL** | *Yes, softly, toward keeping*, with five mechanisms named. Carried by [T-167](T-167-stop-the-listing-pricing-only-the-rival.md). The bar this is judged against — a lean **and** a mechanism — was set at `specify` before the run, and it is met in the failing direction on all five |
| Each of the three mechanisms is answered by a change, and §3 names the change and the mechanism | PASS | §3, *Steps 3–6*. The reader named none of the three and volunteered two of them as correct, which is independent confirmation rather than our own reading |
| At least one survivor claim rests on the operations having been **run** — date, destination's nature, counts — and cites nothing outside `plugin/` | PASS | The run has a home in the shipped document for the first time (`What this procedure has been run against`); the survivor bullet points at it. The reader read the counts back — *165 tasks, 28 labels ... 324, then 8, then passed, then 13* — so the citation reaches its referent |
| The disclaimer is still present and no longer buys trust | PASS | Present. "Not a sales pitch. It's more honest than most documents of its kind" — and the reader's remaining complaint about it is that the check-one-at-random line aims scepticism at the two bullets that **do** have sources, which is mechanism 4's asymmetry rather than the disclaimer |
| The closing menu's third outcome is decided either way, with the rationale recorded | PASS | Kept, with its cost attached; §3 step 1 records both rejections |
| Every claim is still a measured output or a pointer | PASS | §3, *Step 7*. Two duplicates removed rather than added |
| The suite, `check` and `index` are green | PASS | `Ran 270 tests in 28.411s / OK (skipped=3)`; `OK - 166 task(s) …`; `Wrote tasks/README.md`. The three skips are this machine's launcher checks, unrelated. An intermediate `FAILED (failures=7)` from a stale index is recorded in §3 rather than hidden by the green line that followed it |

**The failing criterion is the task working, not the task failing.** The outcome it defends —
*the listing does not lean* — is not reached, and the three mechanisms it was scoped to remove are
gone and independently confirmed gone. What the second reader found is a different document's worth
of framing, invisible until the first layer was removed, which is what a second measurement is for.
Closing here rather than editing on is the same rule that created this task out of
[T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md).

**Child fix tasks raised**
- [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) — the five mechanisms, carrying the failed
  criterion
- [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) — the missing
  measurement that mechanism 4 and the reader's decisive gap both reduce to; blocks T-167

**Annotation, 2026-08-17 — the failed criterion is now accepted, not carried.** The maintainer
cancelled [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) the same day, answering its open
question with *stop here, the document is good enough*. The table above is left as it was written,
because it is a true record of what `review` judged; what has changed is what happens next. **The
listing still argues mildly toward keep, by the five mechanisms in §3, and that is a decision rather
than an outstanding defect.** Anyone reading this record for the state of the document should read it
as: three mechanisms repaired and independently confirmed, five accepted, and the reasoning for
accepting them — including what would justify re-opening — in
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md)'s Log.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | — | **Annotation after close, on METHOD rule 5.** [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) was cancelled by the maintainer hours after being raised, so §4's *carried by T-167* is no longer what happens next — the failed criterion is **accepted**. §4 carries the annotation; nothing above it was rewritten, because what `review` judged is a fact about the past. |
| 2026-08-17 | → done | `plan` → `implement` → `review` under the same authorisation, which also covered the commit and push and **nothing this task raises**. **The repair landed and the outcome did not.** A fresh reader — one run, verdict standing, which is the decision §3 records and the one that keeps this from becoming iteration — confirmed two of [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s three mechanisms repaired, named none of the three, and still answered *yes, softly, toward keep* on five mechanisms nobody had seen, because the first layer had to come off before they were visible. The sharpest is not editorial at all: the document prices the overlap **against a rival skill** and never prices keeping taskmd alone, and the one claim carrying the whole installation decision — *the skill that routes an agent through them* — is the only unevidenced sentence in a document that quotes exit codes. That is a missing measurement wearing a framing defect's clothes, so it leaves as [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) blocking [T-167](T-167-stop-the-listing-pricing-only-the-rival.md). Also worth carrying: the extraction given to the reader had to grow to the whole binding, because the repair's central move is a pointer to a section above the listing and the old slice would have cut its referent — **an extraction that cuts what the document points at tests a document nobody receives.** |
| 2026-08-17 | → specified | The open question is answered — **a fresh reader at `review`, same protocol**, given by the maintainer when asked. Both rejections are recorded with it, and the second is the one worth keeping: *check the three mechanisms instead* is the claim-by-claim test that passed this document in [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3, so adopting it would have re-run the check that failed. **The pass bar was decided here rather than asked**, under the standing delegation, and it is stated with what it rejects because it is the line that decides closure. `specify` also found a constraint nobody had noticed: **the evidence for the survivor claim cannot be cited at all.** [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 is outside `plugin/`, a link to it fails a shipped test, and a bare id passes every test while resolving to nothing an adopter holds — so the run is restated in the document rather than pointed at. |
| 2026-08-17 | — | **The maintainer authorised this task's whole lifecycle** — `specify` → `plan` → `implement` → `review` — **and a commit and push at the end**, given as the subject of a handoff (`create - work T-166, full lifecycle, commit and push`). It covers **this task and nothing else**: no other task, and nothing this one raises, which takes one phase per request unless separately authorised (METHOD §3.1). Recorded here and not only in the handoff, which is consumed once and archived. **The open question below is inside that authorisation and still needs the maintainer**, because it decides whether the task can be closed honestly rather than how to do a step: a document edited to satisfy a reader whose objections you already hold is tuned, not neutral. Answering it by picking the convenient option would make `review` decorative. |
| 2026-08-17 | → proposed | Raised from [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md), which found the listing argues mildly toward keeping taskmd and named three mechanisms for it. Raised rather than fixed there because T-165's `specify` put editing the listing out of scope on purpose: **a repair made in the same breath as the measurement leaves no evidence the measurement happened.** `high` — the listing's whole claim is that it lets someone decide, so a lean in it is the failure of the feature and not a blemish on it. `s`: the edits are small and the difficulty is judgement, not volume. The open question is the one that decides whether this can be closed honestly — a document edited to satisfy a reader whose objections you hold is tuned rather than neutral, so `review` probably needs a reader who has not seen it. **Not covered by the authorisation of 2026-08-17**, which named T-164 and T-165 and excluded what they raise. |
