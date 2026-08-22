---
id: T-176
title: Have an uninvolved reader test the sourced survivor bullet
type: research
status: proposed
phase: specify
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

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

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
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **Acceptance criteria written, and written late — which is stated in §1 rather than hidden.** The owner directed this on 2026-08-22, after the reader had already run. **Criteria written once a verdict is known can be tuned to it**, so none of the six judges what the verdict says; each judges the instrument, the record or the scope, whose right answers were all fixed before anyone read anything. The verdict itself is the measurement, and a measurement cannot be an acceptance criterion of the task that commissioned it. Recorded this way rather than by writing criteria the run is already known to pass, which would make `review` decorative. Status is unchanged: `specify` is now complete, `plan` has not been written, and no phase beyond this one was authorised. |
| 2026-08-22 | (no change) | **The reader ran, and the record is deliberately not advanced.** The owner ran the instrument on 2026-08-22 and returned its answers, which are recorded in §3 in full. **Status stays `proposed` because §1's acceptance criteria are still the placeholder `<written at specify>`** — the run happened ahead of `specify` finishing, so there is nothing written down for the verdict to be judged against, and advancing the record would let criteria be written after the result is known. That is the shape [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md)'s criterion 5 exists to stop, applied to a different phase. Recorded rather than repaired: writing the criteria is `specify`, and no phase was authorised on this task. **Two findings left the run and neither was absorbed.** The fifth question — added before the run, for the scope half T-166's four cannot reach — answered §1's second scope item, and the sourced bullet's unobserved half was read as **honest**. And question 3 turned up a contradiction of fact rather than of framing, which a command settled the same day and which leaves as [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md). |
| 2026-08-22 | (no change) | **The reader is a fresh AI agent — answered by the owner in the batched round of 2026-08-22.** One question covered this task and [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), which were blocked on it and on nothing else, so one answer unblocks two. The instrument is the one this task's own *Inputs* already name: [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 step 9 — `plugin/skills/taskmd/docs/bindings/github-issues.md` extracted **whole** and verbatim to a scratch path outside the repository, the agent told to open nothing else, the four questions unchanged, *sales pitch* offered as an available answer, and no mention that neutrality is being measured. Extracting the bullet alone is ruled out there: the repair under test points at a section above the listing, so a slice would test a document nobody receives. Taken with the row of 2026-08-19, both halves are settled — one reader, the count fixed in advance, and who. *Rejected: a friend who is a potential user*, priced in T-199's row of this date. This row is the answer, not authorisation to start. |
| 2026-08-22 | (no change) | **Re-edged from `parent: T-168` to a soft edge, by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md).** [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) was not raised from a failed criterion — five of its six were met and the sixth went to T-174. This task came out of `review` step 5, as a residue nobody there could settle: the bullet has not had an **uninvolved reader**, and no session can supply one. T-168's own outcome — the price, with the evidence behind it — exists and was checked. So this is a stronger test of a finished result, not a part of it, and holding T-168 open would park a closed research task on a person who may never be available. `related` was already recorded here, so the repair is one field. The alternative — reopening T-168 — is rejected on that reasoning and is recorded in T-216 §3. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: one reader, count fixed now.** Asked in the backlog-wide round of 2026-08-19. One reader with the verdict standing is the recorded precedent and the cheaper option, and setting the count before anyone reads is the whole of what makes it a check. *Rejected: the fuller [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) protocol*, which buys more confidence at more of the owner's time — and buys it only if the count is fixed in advance either way, since a second reader added after an unwelcome verdict converts the check into editing until somebody agrees. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review. Its §3 step 7 declared the gap rather than papering over it, which is what [`implement`](../plugin/skills/taskmd/docs/method/implement.md) asks for when no use is available; this is the task that makes the declaration actionable instead of a sentence in a closed record. **Not covered by the authorisation of 2026-08-18.** |
