---
id: T-199
title: Have an uninvolved reader write a coverage declaration from the clause
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-192, T-176]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-199 — Have an uninvolved reader write a coverage declaration from the clause

## 1. Specify

**Outcome**
Someone who has not read either shipped binding writes a `cannot-occur` declaration for a backend of
their choosing, from `BINDING.md` §4 alone — and what they produce is compared against what the
clause meant, so the clause is judged by how it reads rather than by how it was written.

**Why this one**
[T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) met its fourth criterion by
writing a Notion-shaped fragment from the clause, and **that exercise immediately found the clause
wrong**: it said *cannot occur on this backend* when what decides the answer is the binding's
mapping, not the service. Two backends that both allocate identifiers answer differently on
`DUPLICATE ID`, depending on whether the binding uses the service's identifier as the task id.

**So the residue is not a doubt, it is a demonstrated rate.** One reading of the clause by its own
author, in a session that had already read both shipped bindings, produced one defect. That is the
weakest form of the test — the author cannot un-know the examples, and the clause is a contract every
binding anybody ever writes inherits. What a stranger does with it is the thing worth knowing, and it
is the one thing a session cannot stand in for.

**Scope**
- In: one reader, one backend of their choosing, one fragment written from `BINDING.md` §4 without
  reading `plugin/skills/taskmd/docs/bindings/`
- In: what they asked, what they got wrong, and what they could not decide — those are the clause's
  defects, not the reader's
- Out: **rewriting the clause during the exercise.** Whatever the reading turns up is recorded first
  and repaired afterwards; a clause edited while somebody is reading it has been tested against
  nothing
- Out: adopting the fragment as a third binding. §1 of
  [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) rules a third binding out
  and that is unchanged — this produces a reading, not a document to ship

**Inputs**
- `plugin/skills/taskmd/docs/BINDING.md` §4 — *The coverage a binding declares* — which is all the
  reader gets
- [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) §3 step 5 — the author's
  own fragment and the defect it found, read **after** the reader has finished and not before

**Acceptance criteria**
- [ ] The reader had not read either shipped binding, and that is stated rather than assumed
- [ ] What they produced is recorded verbatim, including anything they left blank
- [ ] Every question they asked is recorded as a defect in the clause, with what the clause should
      have said
- [ ] Whether their fragment classifies any class differently from the author's, and why, is stated
- [ ] The clause is repaired afterwards, or the reasons for leaving it are recorded

**Open questions**
- ~~**Who reads it?** The owner's to choose. It cannot be a session: `BINDING.md` is in this
  repository, so any session working here has the shipped bindings within reach and cannot honestly
  claim not to have read them. This is the same constraint
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) waits on.~~ **Answered
  by the owner in two parts, both on 2026-08-22: one route, chosen once and used for both tasks; and
  the reader is a fresh AI agent, given the extracted clause outside this repository** — see the Log
  rows of that date, which record how that meets the constraint struck through above.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Run 2026-08-22, by the owner.** `BINDING.md` §4 embedded verbatim in one prompt, a fresh chat, no
other file within reach and no taskmd binding available to open.

**Criterion 1 is met by the reader's own statement, not by assumption** — their first line: *"I have
not read any taskmd binding document, and did not search for one."*

**Backend chosen: Jira Cloud**, and they said why in the clause's own terms — *"the two things this
clause turns on: who allocates the identifier, and whether the list is stored or computed."*

**They had to invent §3's mapping, and declared that before writing**: one task = one Jira issue;
task id = the issue key, allocated by Jira on create; the list = a JQL query run at read time,
nothing materialised; status through a fixed table. *"Every sentence in the declaration is downstream
of a mapping I made up."*

### What they produced, verbatim

````markdown
<!-- taskmd:cannot-occur -->
**You do not rely on check to catch duplicate ids or a stale index.**

Under this binding neither state can exist, so those reports stop arriving. The task id is the
Jira issue key. Jira allocates the key on create and does not hand the same key out twice in a
project, and this binding never writes an id of its own, so `DUPLICATE ID` has no way to arise.
The task list is a JQL query, run when you read it. No file and no page holds a copy of it, so
[BLANK: class name for the stale-index state — §4 describes the state but never names it, and
the name here must match what the validator reports] has nothing to go stale against.

This holds only while the §3 mapping holds. If you keep your own id in a custom field and use
that field as the task id, Jira does not police it and `DUPLICATE ID` is live again. If you add
a generated backlog page, a roadmap doc or an exported sheet that the team reads as the list,
you have re-created the state named above, somewhere check cannot see it. Moving an issue
between projects changes its key. Jira redirects the old key, but a task id you wrote down
elsewhere does not follow.

The rest of the validator's classes either apply as written or still run locally against the
working copy.

Nothing running locally can confirm the two paragraphs above. They are claims about Jira, and a
person has to review them. The marked region confirms only that the classes named here are
classes the validator reports.
<!-- taskmd:end-cannot-occur -->
````

### Every question they asked, as a defect in the clause

| What §4 did not tell them | What the clause should have said |
| :--- | :--- |
| **The name of the stale-index class.** §4 describes the state twice and never names it. They left it blank rather than guess: *"Guessing `STALE INDEX` would pass a human and fail the one check the region exists to support"* | Name the classes it uses as examples. **Their guess was correct** — the validator reports exactly that class, as this repository's own `check` printed while this task was being written — and the clause still gave them no way to know it |
| **Where the validator's class list lives.** *"I do not have the validator's class list… I cannot tell whether that default is quietly hiding a class that really is impossible under this mapping"* | The clause requires class names in backticks and never says where they come from |
| **Whether this is an entry or a section.** The row sits in the minimum-entries table for *Assumptions this binding makes*, which requires a bold lead; the coverage subsection reads like its own section | Say which, because the bold-lead requirement and the thirty-second budget both hang on the answer |
| **What the bold lead is a claim about.** *"The section demands a claim about the adopter's project; the row asks for a fact about the mapping."* They bridged it with a reliance claim — *"You do not rely on check to…"* | Say that the coverage entry's lead is about reliance, or exempt it from the claim-about-your-project rule |
| **How long the lead may be.** *"The spec gives whole-section figures (65 and 44 words for all leads) and six minimum entries. I divided and aimed at about thirteen words"* | Give a per-lead figure, or say the budget is per section |
| **Where the marked region starts and ends.** *"The example shows only 'the statement' inside them. I wrapped the whole entry so that no class name sits outside the region the machine reads"* | Say whether the region wraps the statement or the whole entry |
| **What the hygiene check scans.** They deliberately did not backtick `check` inside the region: *"If the hygiene check reads every backticked token in the region as a class name, backticking the command would fail it"* | The clause says what the check confirms and never what it reads |
| **Whether *still runs locally* presumes a working copy.** *"If a Jira binding is remote-only, that closing line should read 'apply as written' and nothing more"* | Offer both closing forms, or say which applies when nothing is local |

### Four places the clause had to be read twice

- ***"It is the mapping that decides, not the service."*** *"First pass I read the `DUPLICATE ID`
  example as two different services. The paragraph says 'comparable services' and then 'the same
  service' two lines later. I settled on: the point is one service, two mappings."*
- **The thirty-second budget.** *"498/401 and 65/44 read like four bindings on first pass. They are
  two bindings measured twice — whole sections, then bold leads only."*
- ***"Say the rest either applies or still runs locally."*** *"I first read this as a bucket that
  needs no writing at all, because the next line says it 'needs no entry'. No entry per class, but
  one sentence covering the remainder — so I wrote one."*
- ***"A binding that says so plainly is easier to trust."*** *"Whether that instructs the binding or
  the method document. I put the line in the binding."*

### Criterion 4 — how their classification compares with the author's

**The repaired wording carries, and it carried further than it was repaired.**
[T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) §3 step 5 found the clause
wrong because it said *cannot occur on this backend* when the mapping decides. This reader, meeting
only the corrected wording, **used the mapping and not the service without being told to** — and then
wrote the reversal into the declaration as a live condition: *"If you keep your own id in a custom
field and use that field as the task id, Jira does not police it and `DUPLICATE ID` is live again."*
That is the defect T-192 found, restated by a stranger as a warning to their own adopter.

- On `DUPLICATE ID` they classify as the author would, and for the author's reason.
- On the stale-index class they **could not classify at all**, for lack of a name. That is not a
  disagreement; it is the clause failing to be usable.

**The clause is not repaired here, and criterion 5 allows that with the reason recorded.** The
reason: `BINDING.md` §4 is a contract every binding anybody writes inherits, eight defects is a
rewrite rather than an edit, and the owner has not seen these findings. Put to them rather than made.

**Decisions & assumptions**
- **The reader's output is recorded as the result, including the blank** — 2026-08-22. The blank is
  the strongest single finding, and filling it in would have destroyed it.
- **The real class name is confirmed and recorded beside their refusal to guess it** — 2026-08-22,
  from this repository's own `check` output while writing this record. It makes the defect sharper
  rather than softer: a correct guess they were right to refuse.
- **The clause is not repaired in the run that measured it** — 2026-08-22, the reasoning
  [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) and
  [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) established: repairing inside
  the measuring task destroys the evidence that the measurement happened.

**Outputs produced**
- the reading above, and the eight clause defects it produced

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **Criterion 5's repair is raised as [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)**, by the owner's decision of 2026-08-22. The criterion permits repair in place or a recorded reason; the reason is size, not process — eight defects in a contract every binding anybody writes inherits is a rewrite rather than an edit. This record stays open on that criterion alone, and closes when T-222 does. **The repair's shape is already constrained and T-222 carries the constraint**: §4 argues against a per-check coverage table because one new check would falsify every binding's table at once, so the class-name defect must not be answered by writing the list into the clause. Nothing else about this record changes. |
| 2026-08-22 | (no change) | **The reader ran, and produced eight defects in a clause every binding inherits.** The owner ran the instrument on 2026-08-22 and returned the reply, recorded verbatim in §3 including the blank the reader refused to fill. **Four of the five acceptance criteria are already met by that record** — criterion 1 by the reader's own opening line rather than by assumption, criteria 2 and 3 by §3, criterion 4 by the comparison against [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)'s own fragment. **Criterion 5 is open by design**: it permits repair or a recorded reason, and the reason is recorded — eight defects in a contract every binding anybody writes inherits is a rewrite, not an edit, and the owner has not seen them. **Status stays `proposed` and the record is not advanced**, because the run happened ahead of `plan`, so a review would be judging a phase the record never passed through. **The strongest single result is the blank.** §4 describes the stale-index state twice and never names its class; the reader guessed the name correctly in their notes and refused to write it, on the ground that a guess would pass a human and fail the machine check the marked region exists to support. The guess was right, which makes the defect sharper rather than softer. |
| 2026-08-22 | (no change) | **The remaining half is answered by the owner: a fresh AI agent, not a person.** Asked in the batched round of 2026-08-22, after the same day's earlier answer had settled the route. **It resolves an apparent contradiction in §1 rather than passing over it.** §1 says the reader cannot be a session, because `plugin/skills/taskmd/docs/BINDING.md` sits in this repository and any session working here has the shipped bindings within reach. The instrument that satisfies both is [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md)'s: §4 is extracted verbatim to a scratch path **outside** this repository, carrying whatever it points at, and the agent is told to open nothing else — so the reader has no reach to `plugin/skills/taskmd/docs/bindings/` at all, which is what the constraint was protecting. *Rejected: a friend who is a potential user of the plugin* — the thing the criterion means, and what [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s Log calls the subagent a **proxy** for; it costs a favour and an unknown wait, and holds both tasks open until they reply. The owner had that asymmetry stated when choosing, so the proxy is adopted knowingly rather than by default. This row is the answer, not authorisation to start. |
| 2026-08-22 | (no change) | **Re-edged from `parent: T-192` to a soft edge, by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md).** The clearest of the three: every one of [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)'s criteria is **met**, and its §4 already says in its own words why it closed — this task is *"a stronger test of a clause that already works rather than a gap in it"*. It waits on an uninvolved reader, which no session can supply. The soft edge keeps the pointer in both directions without holding a finished deliverable open. Reopening T-192 was rejected because there is no criterion to reopen it against; recorded in T-216 §3. |
| 2026-08-21 | → proposed | Raised by [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)'s review. Its criterion 4 was **met** — a fragment was written from the clause and changed it — so this is not a gap left behind but the stronger version of a test that already paid for itself once. Raised rather than noted, because it needs a person and a note inside a closing task leaves every view a project has. `medium` and `s`: the exercise is short and the clause it judges is inherited by every binding anybody writes. **Waits on a person**, so the 2026-08-19 grant does not reach it. |
| 2026-08-22 | (no change) | **The open question is answered in part by the owner: one route, chosen once and used for this task and for [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md).** Asked in the batched round of 2026-08-22. Both are blocked on this and on nothing else, so one answer unblocks two. *Rejected: a different reader for each*, which makes each reading true first contact, but needs two people and blocks both tasks until they are found. *Rejected: the owner reads both*, available immediately, but they cannot un-know material they have already ruled on — the exact weakness this task exists to remove. **Still open: who that reader is.** The shape is settled and the person is not, so §1's question is narrowed rather than closed. This row is the answer, not authorisation to start. |
