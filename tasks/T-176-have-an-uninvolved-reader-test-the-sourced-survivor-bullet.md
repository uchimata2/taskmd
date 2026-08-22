---
id: T-176
title: Have an uninvolved reader test the sourced survivor bullet
type: research
status: done
phase: review
parent: null
blocked_by: []
related: [T-168, T-166, T-167]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-22
deliverables: []
---

# T-176 — Have an uninvolved reader test the sourced survivor bullet

## 1. Specify

**Outcome**
A verdict from a reader who was not involved on whether the sourced survivor bullet in the migration
listing reads as evidence or as advocacy — the check every other claim in that document passed, and
the one [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) declared
rather than ran.

**Why this one**
**[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3 step 7
records this as an honest gap rather than implying it was covered.** Its mechanical checks all passed
— `check`, `index`, the suite, and a diff confirming one hunk — and none of them can see the thing
that matters here.

**The risk is specific and it has a history.** The bullet now attaches a per-session cost to one of
four survivors in a document whose lean
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed as **accepted**. A number can
re-balance a document without changing a single other sentence, and
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 is the precedent: a fresh
reader found five framing mechanisms nobody had seen, on a document that had already passed a
claim-by-claim check. A claim-by-claim check cannot see framing, which is exactly what this needs
looking at.

**Set the reader count before the result is known.** T-166 ran one reader and let the verdict stand,
deliberately, because a second reader after an unwelcome first is iteration wearing a fresh reader's
clothes. That decision is the one to copy.

**Scope**
- In: whether the sourced bullet reads as evidence or tilts the document, judged by someone who was
  not involved in producing it
- In: whether the *unobserved* half of the bullet reads as an honest limit or as a hedge
- Out: re-balancing the listing. The five framing mechanisms accepted in
  [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) stay out, and a reader's opinion does not
  re-open a decision the maintainer took
- Out: the figures themselves, which are
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s and are not
  in doubt

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md`, *What survives* — the bullet, and the three
  beside it that set the form
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 — the reader protocol, and
  the extraction lesson: a slice that cuts what the document points at tests a document nobody
  receives

**Acceptance criteria**

**Written 2026-08-22, after the reader had already run**, at the owner's direction. The ordering is
stated because it decides what these may say: criteria written once a verdict is known can be tuned
to it, so **none of these judges what the verdict says**. Each judges the instrument, the record, or
the scope — things whose right answer was fixed before anyone read anything. What the reader
concluded is the measurement, and a measurement cannot be an acceptance criterion of the task that
commissioned it.

- [ ] The reader was uninvolved, and that is **shown by how they were run** rather than asserted —
      the document extracted whole and verbatim to somewhere outside this repository, with nothing
      else within reach
- [ ] The number of readers was fixed before any verdict was read, and the run matches it
- [ ] The verdict is recorded as given — including anything in it that is factually wrong — and the
      record does not argue with it
- [ ] Both halves of §1's scope are answered: whether the sourced bullet tilts the document, and
      whether its unobserved half reads as an honest limit or as a hedge. Where one was not reached,
      the record says so and says why
- [ ] Anything the reader turned up that is outside this task's scope left as its own task, rather
      than being repaired inside the task that measured it
- [ ] The listing is unchanged by this task

**Open questions**
- ~~**One reader, or does this need the same protocol T-166 used?** One reader with the verdict
  standing is the recorded precedent and the cheaper option. **The maintainer decides**, and the
  count is set before the reader runs, not after the verdict is read.~~ **Answered by the owner on
  2026-08-19: one reader, and the count is fixed now** — see the Log row of that date.

## 2. Plan

**Written 2026-08-22, after the run, and it is a record of what was done rather than a plan for what
to do.** The owner ran the instrument before this record reached `plan`, so writing a forward-looking
plan now would be writing steps whose outcome is already known — the same defect §1 states about its
own criteria, one phase earlier. What is worth having is the steps in the order they were taken, so
the next reader run has something to copy and something to disagree with. **A plan written this way
cannot fail**, and that is exactly why nothing in §4 is judged against it: the six criteria judge the
instrument, the record and the scope, and this table is none of those.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Extract the binding **whole** and verbatim to a path outside this repository, per T-166 §3 step 9 — never the bullet alone, because the repair under test points at a section above it | the extract, 43,912 characters on the day |
| 2 | Put **five** questions to **one** fresh reader in one prompt, no repository within reach, framing never mentioned, *sales pitch* offered as an available answer | the reader's five answers |
| 3 | Record the verdict as given, including anything in it that is factually wrong, and do not argue with it | §3 |
| 4 | Settle by **running** anything the verdict asserts about behaviour, rather than by reasoning about it | the command output, and which half of the contradiction it kills |
| 5 | Route what the run turned up outside this task's scope to its own task, rather than repairing it here | [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) |
| 6 | Judge the six criteria, none of which judges the verdict | §4 |

**Step 2's fifth question is the step that could have been skipped and would have cost half the
scope.** The four-question set belongs to [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md),
which judged the whole listing; §1 here has a second scope item those four structurally cannot reach.
A run that cannot answer half a scope returns a partial answer that reads as complete — which is why
the fifth was added **before** the run and recorded as an addition.

**Step 4 is the step that turns a reader's doubt into a fact.** The reader made their recommendation
conditional on something they could not check. A session had the command, so the condition was
settled the same day — and it resolved against the document rather than against the reader.

## 3. Implement

**Run 2026-08-22, by the owner.** Instrument as
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 step 9 fixed it: the whole
binding — 43,912 characters, verbatim, grown from the 26,226 that record measured — embedded in one
prompt, a fresh chat with no repository within reach, the reader put in the position of advising a
team that had just migrated, and no mention that framing was being measured.

**Five questions, not four, and the change is recorded rather than absorbed.** T-166 fixed four. This
task's §1 has a **second** scope item those four cannot reach — whether the *unobserved* half of the
sourced bullet reads as an honest limit or as a hedge — so a fifth was added, asking generally
whether the document states limits on what it knows and whether each reads as honest or as
softening. It does not name the bullet, so it does not lead. **It paid for itself**: the answer to
§1's second scope item came from it and from nothing else.

**Question 4 — the document leans mildly toward keeping, and not through its claims.** The reader
found several claims that cut against taskmd. The lean is arrangement: *What survives* lists four
items flatly, *What is gone* lists three and rebuts two in place, so **"the losses shrink under
inspection. The survivals do not."** They named two things pulling the other way — *"None of them is
a reason to keep taskmd installed"* and *"the method is a document you could follow without the skill
installed"* — and called them *"unusual things for a tool to ship about itself, and they are the
reason this is a mild lean and not a pitch."*

**The sharpest observation is about a sentence T-166 wrote as a repair.** On *"It is a list of facts
and it stops short of a recommendation"*: **"Declaring no opinion, in a document you wrote and
ordered, is a position."**

**Question 5 — the limits split five honest to three softening.**

| Honest | Softening |
| :--- | :--- |
| *Enterprise Server is untested* — "names the untested surface and the reason it could fail. It costs the document a claim it would want" | *True as behaviour, overstated as necessity* — "the weakest point in the section, and the softening creates the contradiction in question 3 rather than resolving it" |
| **The sourced bullet's unobserved half** — "It refuses to read a null result as evidence in either direction, including the flattering one" | *The destination is gone and was never the evidence* — "converts a missing artefact into a principle. You cannot check the runs. You can only rerun them" |
| Closed parent with an open child — "a defect class the procedure misses, named rather than omitted" | *It stops short of a recommendation* — "True about scope. It also excuses the arrangement, which is where the lean sits" |
| The two limits of the coverage list itself | |
| *The totals that used to open this paragraph are gone rather than corrected* | |

**§1's second scope item is answered in the direction that needs no change.** The sourced bullet's
*"Whether it still triggers there is unobserved… a zero drawn from that is not a negative"* was read
as **honest**, by a reader who was separately willing to call three other limits softening. The first
scope item — whether the bullet itself tilts the document — was not what they picked out: the lean
they found is in the section's arrangement, and the bullet was not among the mechanisms they named.

**Question 3 — the missing fact, and it is a finding of fact rather than of framing.** The reader
found the document saying two incompatible things about the five document checks, both citing the
same 2026-08-18 measurement, and made their recommendation conditional on which is true. **Measured
the same day, and it resolves against the half they expected to win:**

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md
CONFIG DRIFT  status: shipped default adds 'specified', 'planned', ...
Scope  no task file was read, and the checks that open one did not run. ...
exit 1

$ ./plugin/bin/taskmd context|index|list --root tests/fixtures/migrated-away
exit 2, exit 2, exit 2
```

The five checks **are** reached and do fire. So the coverage table is right, the *No validator* note
is wrong, and *"the commands exit 2 either way"* is wrong for one of the four. **The reader's own
recommendation resolves to keep on its own stated condition** — *"if there is a way to run those five
on a project with no tasks folder, the install still does unique work and I would keep it."*

*Annotated 2026-08-22, later the same day.* **It is not five and the membership was wrong too**, which
[T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) established by
running the checks rather than by reading the table this paragraph trusted: `duplicate index` never
ran on such a project and `section reference` was missing from the list. The paragraph above is left
as written because it is what this run concluded on the day; the conclusion it carries — that checks
are reached, that the note is wrong, and that the reader's condition resolves to *keep* — is
unaffected by the count.

**Both falsified sentences leave as [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)**, not repaired here: §1 puts re-balancing and the figures out of scope, and correcting a document inside the task that measures how it reads destroys the evidence that the measurement happened — which is T-166's own reasoning applied to itself.

**Decisions & assumptions**
- **The reader's verdict is recorded as the result, not weighed against ours** — 2026-08-22, copying
  T-165's decision. Where the document defeated them, that is recorded as evidence about the
  document.
- **A fifth question was added before the run, not after** — 2026-08-22. The four-question set was
  built for [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md), which judged
  the whole listing; this task's scope has a half they cannot see. *Rejected: run the four unchanged*
  — comparability with a task asking a different question is worth less than reaching this task's own
  scope, and a run that structurally cannot answer half a scope returns a partial answer that reads
  as complete.
- **The contradiction was measured rather than reasoned about** — 2026-08-22. A session had the
  command; `CLAUDE.md` *Verifying* makes running it the only way to settle a claim about behaviour.
- **One run, and the verdict stands** — 2026-08-22, T-166 §3 step 9 unchanged.

**Outputs produced**
- the reader's finding, above
- [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The reader was uninvolved, **shown by how they were run** — the document extracted whole and verbatim outside this repository, nothing else within reach | met | The extract is 43,912 characters, and that figure is checkable rather than asserted: the binding at `2af1b6e`, the commit the reader was given, measures 43,912 bytes exactly. Whole, not sliced, per T-166 §3 step 9 |
| The number of readers was fixed before any verdict was read, and the run matches it | met | One, fixed by the owner on 2026-08-19 in the Log below — three days before the run — and one ran |
| The verdict is recorded as given, including anything factually wrong in it, and the record does not argue with it | met | §3 carries all three answers in the reader's own words, including the recommendation they made conditional. Nothing in the verdict was wrong: what was wrong was the document, and the record settles that by running a command rather than by disputing the reader |
| Both halves of §1's scope are answered; where one was not reached, the record says so and why | met | The second half is answered directly and in the reader's own classification — the unobserved clause is **honest**, from someone who called three other limits softening the same turn. **The first half is answered by a non-nomination and the record says so**: asked what makes the document lean, the reader named specific mechanisms and the bullet was not among them, while engaging closely enough with the same bullet elsewhere to classify half of it. That is evidence rather than proof, and it is the strongest form the question admits without leading them to the bullet |
| Anything outside this task's scope left as its own task rather than being repaired here | met | Two. The contradiction of fact left as [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md), now closed. The framing findings — the located lean, *declaring no opinion is a position*, and two limits still reading as softening — left as [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), raised as a decision for the owner rather than as a repair, because T-167 accepted that balance |
| The listing is unchanged by this task | met | `git log` on `plugin/skills/taskmd/docs/bindings/github-issues.md` names no commit from this task. It did change on 2026-08-22, by T-221 — which is the separation working rather than a breach of this row |

**The one thing this task could not do, stated rather than left as a clean sweep.** A single reader
answering five questions is not a survey of the document's framing, and the first scope item rests on
what they did *not* name. §1 fixed the count at one on purpose, and the alternative to accepting that
limit is a second reader, which is iteration. So the honest reading of this result is: **one competent
outsider, told nothing about what was being measured, did not find the bullet tilting the document,
and did find something else.**

**Child fix tasks raised**
- [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) — the two falsified sentences, closed 2026-08-22
- [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md) — the framing findings, as a decision for the owner

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | proposed → done | `plan` and `review` — the remaining phases and not the usual set — under the four-task grant recorded below. **No second reader ran**, which the grant warns against by name; one reader with the verdict standing is the owner's decision of 2026-08-19 and it holds. **The plan is written as a record of what was done and says so**: the run preceded the record, so a forward-looking plan would have been steps whose outcome was already known, which is the defect §1 already states about its own criteria. It is judged against nothing for that reason. **All six criteria met, and the fourth is the one worth reading.** The second scope half is answered in the reader's own classification — the unobserved clause is *honest*, from someone who called three other limits softening in the same turn. The first is answered by a **non-nomination**: asked what makes the document lean, they named mechanisms and the bullet was not among them. The review says that out loud rather than reporting it as a clean result, because one reader who did not name something is evidence and not proof. **The instrument's own figure was checked rather than trusted** — 43,912 characters, and the binding at the commit the reader was given measures 43,912 bytes. **One task raised**: the framing findings had no home and criterion 5 required one, so [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md) puts them to the owner as a decision — which is also where [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) said a revisit of the accepted balance belongs. **§3 was annotated, not rewritten**: T-221 found the *five checks* count wrong later the same day, and METHOD rule 5 says correct the present and annotate the past. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md), [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md), this task's **remaining phases** and [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) be worked through the **full lifecycle**, and the result committed and pushed. **What *remaining* means here, and it is not the usual set:** `specify` is complete and §3 already holds the reader run of 2026-08-22, so what is left is `plan` and `review`. A session must not read *full lifecycle* as licence to run a second reader - one reader with the verdict standing is the owner's decision of 2026-08-19, and a second after an unwelcome first is iteration wearing a fresh reader's clothes. **What it does not cover:** any other task; re-balancing the listing, which §1 puts out and [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) settled; and the two falsified sentences, which left as [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md). **It authorises phases, not answers.** Written into this record rather than kept in the session's handoff (`CLAUDE.md`, *one phase per request*). |
| 2026-08-22 | (no change) | **Acceptance criteria written, and written late — which is stated in §1 rather than hidden.** The owner directed this on 2026-08-22, after the reader had already run. **Criteria written once a verdict is known can be tuned to it**, so none of the six judges what the verdict says; each judges the instrument, the record or the scope, whose right answers were all fixed before anyone read anything. The verdict itself is the measurement, and a measurement cannot be an acceptance criterion of the task that commissioned it. Recorded this way rather than by writing criteria the run is already known to pass, which would make `review` decorative. Status is unchanged: `specify` is now complete, `plan` has not been written, and no phase beyond this one was authorised. |
| 2026-08-22 | (no change) | **The reader ran, and the record is deliberately not advanced.** The owner ran the instrument on 2026-08-22 and returned its answers, which are recorded in §3 in full. **Status stays `proposed` because §1's acceptance criteria are still the placeholder `<written at specify>`** — the run happened ahead of `specify` finishing, so there is nothing written down for the verdict to be judged against, and advancing the record would let criteria be written after the result is known. That is the shape [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md)'s criterion 5 exists to stop, applied to a different phase. Recorded rather than repaired: writing the criteria is `specify`, and no phase was authorised on this task. **Two findings left the run and neither was absorbed.** The fifth question — added before the run, for the scope half T-166's four cannot reach — answered §1's second scope item, and the sourced bullet's unobserved half was read as **honest**. And question 3 turned up a contradiction of fact rather than of framing, which a command settled the same day and which leaves as [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md). |
| 2026-08-22 | (no change) | **The reader is a fresh AI agent — answered by the owner in the batched round of 2026-08-22.** One question covered this task and [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), which were blocked on it and on nothing else, so one answer unblocks two. The instrument is the one this task's own *Inputs* already name: [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 step 9 — `plugin/skills/taskmd/docs/bindings/github-issues.md` extracted **whole** and verbatim to a scratch path outside the repository, the agent told to open nothing else, the four questions unchanged, *sales pitch* offered as an available answer, and no mention that neutrality is being measured. Extracting the bullet alone is ruled out there: the repair under test points at a section above the listing, so a slice would test a document nobody receives. Taken with the row of 2026-08-19, both halves are settled — one reader, the count fixed in advance, and who. *Rejected: a friend who is a potential user*, priced in T-199's row of this date. This row is the answer, not authorisation to start. |
| 2026-08-22 | (no change) | **Re-edged from `parent: T-168` to a soft edge, by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md).** [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) was not raised from a failed criterion — five of its six were met and the sixth went to T-174. This task came out of `review` step 5, as a residue nobody there could settle: the bullet has not had an **uninvolved reader**, and no session can supply one. T-168's own outcome — the price, with the evidence behind it — exists and was checked. So this is a stronger test of a finished result, not a part of it, and holding T-168 open would park a closed research task on a person who may never be available. `related` was already recorded here, so the repair is one field. The alternative — reopening T-168 — is rejected on that reasoning and is recorded in T-216 §3. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: one reader, count fixed now.** Asked in the backlog-wide round of 2026-08-19. One reader with the verdict standing is the recorded precedent and the cheaper option, and setting the count before anyone reads is the whole of what makes it a check. *Rejected: the fuller [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) protocol*, which buys more confidence at more of the owner's time — and buys it only if the count is fixed in advance either way, since a second reader added after an unwelcome verdict converts the check into editing until somebody agrees. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review. Its §3 step 7 declared the gap rather than papering over it, which is what [`implement`](../plugin/skills/taskmd/docs/method/implement.md) asks for when no use is available; this is the task that makes the declaration actionable instead of a sentence in a closed record. **Not covered by the authorisation of 2026-08-18.** |
