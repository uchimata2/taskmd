---
id: T-224
title: Re-run the binding's GitHub-side measurements, or say in the document that they were not
type: audit
status: done
phase: review
parent: null
blocked_by: []
related: [T-221, T-166, T-168]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-23
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
| 1 | Sweep the document for every dated or measured claim and split it into `gh`-side and taskmd-side, so the list is derived from the text rather than from §1's four named areas | one row per claim, each with where it sits |
| 2 | Re-run everything that needs no write, before anything is created | the commands and their output |
| 3 | Create one private scratch repository and build a corpus **aimed at the rows the 2026-08-21 run could not reach**, rather than reproducing a corpus that no longer exists | the repository name, and the corpus |
| 4 | Run those rows, break nothing that is not already broken, then repair and re-run — a row that stays quiet proves nothing until it has spoken once | the findings per row, before and after |
| 5 | Re-run the round-trip measurement, which needs an issue and nothing else | the byte counts for both forms |
| 6 | Give every claim from step 1 a disposition, and write the not-re-run ones **into the document** | a new section in the binding, and §3 here |
| 7 | Name the scratch repository for the owner to delete, and re-measure whether a session could delete it | a line in §3 |

**Step 3 is a judgement and it changes what this task measures, so it is written down here rather
than taken in passing.** Reproducing the 2026-08-21 corpus faithfully is impossible — it was 24 tasks
of this project's backlog as it then stood, and the backlog is past 230. A corpus of the same *shape*
would produce different numbers with no more authority than the recorded ones. **What has never been
measured at all is worth more**: three rows examined nothing that day, and a tenth row was added
afterwards and has never run. So the corpus is built for those four.

**Step 2 before step 3** because a write that turns out to be unnecessary is still a write. Two of
the claims needed no repository at all.

**Outputs**

- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the re-run results, dated where each claim
  sits, and one new section naming what was not re-run

## 3. Implement

**Decisions & assumptions**

- **The corpus was built for the rows nobody has ever run, not to reproduce the 2026-08-21 one**
  — 2026-08-23. The old corpus cannot be reproduced: it was 24 tasks of a backlog that has since
  passed 230, so a same-shaped corpus would give different numbers with no more standing than the
  recorded ones. Three rows examined nothing that day and row 10 did not exist, so the five-issue
  corpus is aimed at those four. *Rejected: reproduce 24 tasks and re-run all ten* — several hundred
  API calls to re-derive figures that are already recorded and dated, and it would still leave rows
  4, 8 and 9 unexamined, because it is the project's own config that starves them.
- **The outward-facing write was confirmed in the session as well as in this record** — 2026-08-23.
  The owner authorised a private scratch repository on 2026-08-22. Creating a repository and issues
  is a write on somebody's account, so it was put to the person driving the session before anything
  was created rather than taken from the record alone. Recorded because the next session should do
  the same rather than read this as precedent.
- **Nothing touched this project's own repository or its issues** — 2026-08-23, which the grant's
  limit names. The only read against `uchimata2/taskmd` was `gh issue view 1 --json` for the JSON
  shapes, which writes nothing.
- **Row 10's repair was made by its own rule, not by the convenient route** — 2026-08-23. The defect
  is a closed issue carrying an open `status:` label; the fix was `gh issue reopen`, re-rendering
  `state` from the label, and **not** relabelling the issue to match the button. The row's own text
  says which of the two is the repair, so doing the other would have tested nothing.

**Outputs produced**

- `plugin/skills/taskmd/docs/bindings/github-issues.md` — four claims re-dated where they sit, the
  nine/ten drift corrected, and a new *What has and has not been re-run* section

**Verification**

**Step 1 — the sweep, and every claim's disposition.** Derived by sweeping the document for dated and
measured language rather than from §1's four named areas, so the list cannot inherit §1's blind spots.

| Claim | Where | Disposition |
| :--- | :--- | :--- |
| `--template` holds, `--jq .body` grows one byte a round trip (204; 230 → 231 → 232) | *update* | **Re-run.** Behaviour reproduced exactly on a different body |
| `blockedBy`/`blocking`/`subIssues` are `{nodes,totalCount}`; `parent` plain or absent, on `gh` 2.96.0 | *read* | **Re-run**, read-only |
| the credential carries `repo` and not `delete_repo` | *The standing check* | **Re-run**, read-only |
| rows 4, 8 and 9 examined nothing on the 2026-08-21 corpus | *The standing check* | **Re-run** on a corpus built to reach them |
| row 10 — never run, added after 2026-08-21 | *Checking a backlog that is already here* | **Run for the first time** |
| *the nine rows below*, twice | *The standing check* | **Corrected.** The table has had ten since row 10 was added; both sentences now say *the nine that existed then* |
| *Two of the nine other rows* | *Checking a backlog…* | **Correct as written** and left alone — it counts the rows *other than* the one its paragraph is about, and its *the other eight* only adds up under ten |
| the four Run/Result rows (FAIL 14 / PASS / FAIL 3 / PASS) | *The standing check* | **Restated as a dated record.** Corpus-specific and unreproducible |
| *14 failures, all 14 spurious* on a healthy 24-issue backlog | *Checking a backlog…* | **Restated as a dated record.** Same corpus |
| the 165-task migration, eight spurious failures | *Verify* | **Restated as a dated record.** Needs that source |
| the 2026-08-17 end-to-end run, 28 labels and 165 tasks | *What this procedure has been run against* | **Restated as a dated record.** Destination deleted the same day |
| `list --machine` carried no `type`, `owner`, `business_value`, `effort` or `deliverables` | *enumerate* | **Out of scope and listed anyway** — a taskmd command, which §1 excludes, and already re-checked on 2026-08-22 |

**Step 2 — the read-only re-runs.**

```text
$ gh --version                    -> gh version 2.96.0 (2026-07-02)
$ gh issue view 1 --repo uchimata2/taskmd --json number,blockedBy,blocking,subIssues,parent
{"blockedBy":{"nodes":[],"totalCount":0},"blocking":{"nodes":[],"totalCount":0},
 "number":1,"parent":null,"subIssues":{"nodes":[],"totalCount":0}}
$ gh auth status                  -> Token scopes: 'gist', 'project', 'read:org', 'repo', 'workflow'
```

Both held. `parent` came back `null`, which is the *absent* form the document names. No `delete_repo`.

**Steps 3 and 4 — the corpus, and the four rows.** `uchimata2/taskmd-scratch-20260823`, private,
eight labels and five issues: one healthy, one labelled with the blocked status and no blocker, one
carrying `updated: 2026-13-45`, one labelled `work_package:v1.2`, and one closed while labelled
`status:proposed`.

```text
row 4  examined 5 issue(s), 1 finding(s)
        #2 is labelled status:blocked with nothing in blockedBy
row 8  examined 5 issue(s), 1 finding(s)
        #3 updated: '2026-13-45' is date-shaped and is not a date
row 9  examined 5 issue(s), 1 finding(s)
        #4 work_package:v1.2 reads as a version
row 10 examined 5 issue(s), 1 finding(s)
        #5 state=CLOSED with an open status label 'status:proposed'
```

Then repaired — #2 relabelled, #3's date corrected, #4 regrouped, #5 **reopened** — and re-run:

```text
row 4  examined 5 issue(s), 0 finding(s)
row 8  examined 5 issue(s), 0 finding(s)
row 9  examined 5 issue(s), 0 finding(s)
row 10 examined 5 issue(s), 0 finding(s)
```

**The `examined 5` is the half worth reading.** Each row reported one finding out of five issues, so
it was silent about four while able to speak — and after repair it was silent about five from inside
the same reach. A row that examined nothing scores like a row that found nothing, which is the
document's own warning, and printing the denominator is what stops this run making that mistake.

**Step 5 — the round trip.**

```text
template round trips: 102 -> 102 -> 102 -> 102 -> 102 -> 102   HELD
jq       round trips: 96 -> 97 -> 98 -> 99                     GREW by 3 over 3
```

The byte figures are not the document's 204 and 230 → 231 → 232 because the body is a different one.
**What re-ran is the behaviour** — one byte per `jq` round trip, none per `--template` — and it
reproduced exactly.

**Step 7 — the scratch repository.** `uchimata2/taskmd-scratch-20260823`, confirmed private by
`gh repo view --json isPrivate` at creation. **It is the owner's to delete**, as the fourth criterion
settles, and the session could not delete it in any case: the credential carries `repo` and not
`delete_repo`, re-measured today. It holds five issues and eight labels and nothing else.

*Annotated 2026-08-23, after the phase ran: the owner deleted it the same day, confirmed by
running rather than reported — `gh repo view` now answers* Could not resolve to a Repository. *The
paragraph above is left as written, being true of the day it describes (METHOD rule 5).*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every `gh`-side measured claim is listed with one of the three dispositions, and none is left unlisted | met | Twelve rows in §3, derived by sweeping the document for dated and measured language rather than from §1's four named areas — which is why it caught two §1 did not name: the *nine rows* drift, and row 10 never having run. The one taskmd-side claim the sweep returned is listed and marked out of scope rather than dropped |
| A claim that was re-run carries the command, the result and the date | met | Six re-runs, each with its command and output quoted in §3, all dated 2026-08-23 |
| A claim that was not re-run says so **in the document**, not only in this record | met | *What has and has not been re-run* is a new section in the binding, naming all four historical measurements and why each stays as a dated record |
| Any scratch repository created is private, and its deletion is recorded — the owner removes it | met | `uchimata2/taskmd-scratch-20260823`, private confirmed by `gh repo view --json isPrivate`. Named here and not deleted, which the criterion asks for; and the credential carries no `delete_repo`, re-measured today, so a session could not have deleted it either way |

**Child fix tasks raised**
- none from the criteria. **One thing found while reading was raised rather than fixed**:
  [T-237](T-237-the-softening-clause-t-228-repaired-has-a-second-instance-and-an-idiom-behind-it.md),
  a second instance of the clause [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md)
  had judged softening hours earlier. It sits in the standing-check section this task edited, and
  §1 puts the document's framing out of scope by name, so it was left untouched while the
  measurements around it were re-dated.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds one, struck through and
answered on 2026-08-22. **Two things are flagged for the owner rather than left in a closing record**:
the scratch repository above is theirs to delete, and **row 10 had never been run until today** — it
shipped on 2026-08-22 in a section whose surrounding prose said nine rows had been verified, which is
the exact shape of the *half-swept document reads as a swept one* problem this task exists for, found
inside the task raised to find it.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **The scratch repository is deleted, which closes the last thing this record left with somebody.** The owner removed `uchimata2/taskmd-scratch-20260823` on 2026-08-23 and it was **confirmed by running rather than reported**: `gh repo view` answers *Could not resolve to a Repository*. §3's step 7 is annotated and its original sentences are left as written, being true of the day the phase ran (METHOD rule 5). **The fourth criterion is unaffected** — it asked that the deletion be *recorded* and that the repository be named, both of which it was at close; this row records that it then happened. |
| 2026-08-23 | proposed → done | **Closed: four criteria, four met.** Six measurements re-run and four restated as dated records, every one of the twelve listed with a disposition. **The sweep found two things §1 did not name**, which is why it was derived from the document's own dated language instead of from §1's four areas: *the nine rows below* has been false since row 10 was added, and **row 10 had never been run at all** — it shipped into a section whose prose said nine rows were verified. That is *a half-swept document reads as a swept one* occurring inside the task raised to remove it. **The corpus was built for what has never been measured rather than to reproduce what has**: the 2026-08-21 backlog cannot be rebuilt, and rows 4, 8 and 9 examined nothing that day because this project's own config starves them. All four rows fired on their own case, stayed silent on the other four issues, and went silent on all five after repair — and each line prints its denominator, because a row that examined nothing scores like a row that found nothing. **Row 10 was repaired by its own rule**, reopening the issue to re-render `state` from the label rather than relabelling to match the button. **The write was confirmed in the session as well as in this record**, since creating a repository is a write on somebody's account and a record is not the person. `uchimata2/taskmd-scratch-20260823` is private and is the owner's to delete. |
| 2026-08-22 | (no change) | **The grant was extended a third time**, to [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md), scoped there to finishing that record and not to building what it decides. The rows below are what the grant covered when each was written and are left as written; **T-234's own row carries the membership as it now stands**. Nothing about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **Confirmed for unattended work, and the deletion moved to the owner.** They confirmed on 2026-08-22 that this record may be worked while they are away, and that **they will remove the scratch repository the following day**. Two consequences. The fourth criterion is met by *naming* the repository, not by deleting it — a session that deleted it would destroy the evidence the run happened, and one that left it unnamed would leave the owner hunting for it. And **the unattended limit in the grant row is unchanged**: stop before any outward-facing write that cannot be undone, and before anything touching this project's own repository or its issues. A repository the owner has undertaken to delete is not the same thing as a write nobody can undo. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task, and it is the one limit that is not about phases.** The scratch repository is authorised — private, on the account the earlier row names, deleted afterwards. **Unattended, stop before any outward-facing write that cannot be undone**, and before anything that touches this project's own repository or its issues, which carry two adopter reports. A write the session cannot delete is one the owner has not authorised. |
| 2026-08-22 | (no change) | **The owner authorises a scratch repository: answered 2026-08-22.** Put to them with the alternative priced: *reject and file every row as a dated historical record*, which costs nothing, needs no outward-facing write, and proves nothing — the document would say *not re-run* four times and a reader would still not know whether the numbers hold. **Answered: yes.** The fourth acceptance criterion already binds the shape — private, and its deletion recorded. **What the answer did not say is which account**, and this session decided it rather than asking again: `uchimata2`, the only account `gh` is authenticated as on this machine, which is also where this project's own repository lives. That is an implementation detail under the owner's standing delegation and it is written here so the task confirms it at the start rather than discovering it. **The authorisation is for phases and for the write it names**, not for anything else outward-facing: a scratch repository is not permission to touch `uchimata2/taskmd`'s own issues, which carry two adopter reports. |
| 2026-08-22 | → proposed | Raised from [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s step 4, whose criterion asked for **every** other behavioural claim in the document to be checked by running it. That was met for taskmd's commands and not for `gh`'s, and the gap is named in T-221's review rather than hidden in it. **Raised rather than absorbed** because closing it needs something T-221 had no authorisation for — writes to GitHub — and a task that quietly stopped short of its own criterion would leave the document looking swept. `medium`: the un-run claims are older and carry less weight than the two T-221 corrected, and the two read-only checks that were available were run on 2026-08-22 and held. **Read the `gh` version first** — the document names 2.96.0 and this machine ran 2.96.0 on 2026-08-22, so the field-shape claims were confirmed rather than assumed; a later session on a newer `gh` is in a different position. |
