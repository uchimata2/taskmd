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
- [ ] Any scratch repository created is private, and its deletion is recorded

**Open questions**
- **Is a scratch repository authorised, and on which account?** — the project owner. Creating issues
  is an outward-facing write and nothing here authorises one. The alternative is the second
  disposition for every row, which costs nothing and proves nothing.

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
| 2026-08-22 | → proposed | Raised from [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s step 4, whose criterion asked for **every** other behavioural claim in the document to be checked by running it. That was met for taskmd's commands and not for `gh`'s, and the gap is named in T-221's review rather than hidden in it. **Raised rather than absorbed** because closing it needs something T-221 had no authorisation for — writes to GitHub — and a task that quietly stopped short of its own criterion would leave the document looking swept. `medium`: the un-run claims are older and carry less weight than the two T-221 corrected, and the two read-only checks that were available were run on 2026-08-22 and held. **Read the `gh` version first** — the document names 2.96.0 and this machine ran 2.96.0 on 2026-08-22, so the field-shape claims were confirmed rather than assumed; a later session on a newer `gh` is in a different position. |
