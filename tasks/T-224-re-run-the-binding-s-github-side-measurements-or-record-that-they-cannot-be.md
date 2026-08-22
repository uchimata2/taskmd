---
id: T-224
title: Re-run the binding's GitHub-side measurements, or say in the document that they were not
type: audit
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-221, T-166, T-168]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-224 — Re-run the binding's GitHub-side measurements, or say in the document that they were not

## 1. Specify

**Outcome**
Every measured claim in `plugin/skills/taskmd/docs/bindings/github-issues.md` that describes `gh` or
a real backlog has either been re-run and dated, or says in the document itself why it was not — so
no reader has to guess which of its numbers are current.

**Why this one**
[T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) swept the
document for behavioural drift and finished half of it. Every claim about **taskmd's own commands**
was re-run on 2026-08-22, and two were wrong. Every claim about **`gh` or a real backlog** was left:
re-running one means creating issues on GitHub, which is an outward-facing write nothing in this
project authorises, and the recorded runs are of specific backlogs that a new repository does not
reproduce. Two `gh` claims were checkable read-only and both held; the rest were not attempted.
**A half-swept document reads as a swept one**, which is the condition T-221 existed to remove and
removed only partly.

**Scope**
- In: the measurements at *update* (five `--template` round trips holding at 204), *Verify* (the
  165-task migration and its eight spurious failures), *What this procedure has been run against*
  (the 24-issue healthy backlog and its 14 spurious failures), and the token-scope note
- In: deciding, per claim, between re-run, restate as a dated historical record, or delete
- Out: taskmd's own command behaviour — T-221 covered it on 2026-08-22 and its runs are in that record
- Out: the document's framing and balance. A closed decision, and T-221 records the ruling that a
  correction of fact does not reopen it

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the measured claims, each carrying its date
- [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) §3 — the list
  of what was re-run on 2026-08-22 and what was not, with the reason for each

**Acceptance criteria**
- [ ] Every `gh`-side measured claim in the document is listed with one of the three dispositions,
      and none is left unlisted
- [ ] A claim that was re-run carries the command, the result and the date
- [ ] A claim that was not re-run says so in the document, not only in this record
- [ ] Any scratch repository created is private, and its deletion is recorded — **by whom is settled:
      the owner said on 2026-08-22 that they would remove it the day after**, so this record names it
      and does not delete it

**Open questions**
- ~~**Is a scratch repository authorised, and on which account?** — the project owner. Creating issues
  is an outward-facing write and nothing here authorises one. The alternative is the second
  disposition for every row, which costs nothing and proves nothing.~~ **Answered by the owner on
  2026-08-22: yes** — see the Log row of that date, which also records what the answer did not say.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-22 | (no change) | **Confirmed for unattended work, and the deletion moved to the owner.** They confirmed on 2026-08-22 that this record may be worked while they are away, and that **they will remove the scratch repository the following day**. Two consequences. The fourth criterion is met by *naming* the repository, not by deleting it — a session that deleted it would destroy the evidence the run happened, and one that left it unnamed would leave the owner hunting for it. And **the unattended limit in the grant row is unchanged**: stop before any outward-facing write that cannot be undone, and before anything touching this project's own repository or its issues. A repository the owner has undertaken to delete is not the same thing as a write nobody can undo. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task, and it is the one limit that is not about phases.** The scratch repository is authorised — private, on the account the earlier row names, deleted afterwards. **Unattended, stop before any outward-facing write that cannot be undone**, and before anything that touches this project's own repository or its issues, which carry two adopter reports. A write the session cannot delete is one the owner has not authorised. |
| 2026-08-22 | (no change) | **The owner authorises a scratch repository: answered 2026-08-22.** Put to them with the alternative priced: *reject and file every row as a dated historical record*, which costs nothing, needs no outward-facing write, and proves nothing — the document would say *not re-run* four times and a reader would still not know whether the numbers hold. **Answered: yes.** The fourth acceptance criterion already binds the shape — private, and its deletion recorded. **What the answer did not say is which account**, and this session decided it rather than asking again: `uchimata2`, the only account `gh` is authenticated as on this machine, which is also where this project's own repository lives. That is an implementation detail under the owner's standing delegation and it is written here so the task confirms it at the start rather than discovering it. **The authorisation is for phases and for the write it names**, not for anything else outward-facing: a scratch repository is not permission to touch `uchimata2/taskmd`'s own issues, which carry two adopter reports. |
| 2026-08-22 | → proposed | Raised from [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s step 4, whose criterion asked for **every** other behavioural claim in the document to be checked by running it. That was met for taskmd's commands and not for `gh`'s, and the gap is named in T-221's review rather than hidden in it. **Raised rather than absorbed** because closing it needs something T-221 had no authorisation for — writes to GitHub — and a task that quietly stopped short of its own criterion would leave the document looking swept. `medium`: the un-run claims are older and carry less weight than the two T-221 corrected, and the two read-only checks that were available were run on 2026-08-22 and held. **Read the `gh` version first** — the document names 2.96.0 and this machine ran 2.96.0 on 2026-08-22, so the field-shape claims were confirmed rather than assumed; a later session on a newer `gh` is in a different position. |
