---
id: T-193
title: Make the standing GitHub check fail before trusting it
type: deliverable
status: done
phase: review
parent: T-178
blocked_by: []
related: [T-108, T-151, T-181]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-19
updated: 2026-08-21
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-193 — Make the standing GitHub check fail before trusting it

## 1. Specify

**Outcome**
The standing verification in the GitHub Issues binding has been run against a live issue backlog,
made to fail on a backlog broken on purpose, and then made to pass — with what it printed recorded.
The binding says so where a reader meets the procedure.

**Why this one**
[T-178](T-178-give-the-github-binding-a-standing-verification.md) shipped the procedure and closed
with this criterion **not met**, which is the criterion this repository cares about most: a check
that has only ever succeeded has not been tested, and this one has not even succeeded — nobody has
run it. Its §3 step 5 says why: breaking a backlog on purpose means creating and mutating issues on
a hosting service, and the session that wrote it was running unattended under a grant that covers
records rather than writes to anything outside them.

**The neighbouring procedure sets the standard, and it is not a high bar in principle.** The
migration *Verify* was run end to end into a private repository created for the day and deleted
after it, and **failed three times before it passed** — once at 324, once at 8 with every one of
those spurious, and once at 13 against a deliberately broken migration. Two of those failures are
the reason anybody trusts it. This task is the same day's work for the standing half.

**Requirements served**
R-16 (`docs/SCOPE.md`); [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s
rule, which is the general statement of what this task is an instance of.

**Scope**
- In: creating a scratch backlog, running the nine rows, breaking two things, running again,
  repairing, running again, deleting the scratch repository
- In: recording what each run printed, including the counts
- In: correcting the binding if a row turns out to be unanswerable from `enumerate`'s output — which
  is the thing an unrun procedure most plausibly gets wrong
- Out: changing what the nine rows check. That is
  [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s and is closed; a row that is
  *wrong* is in scope, a row somebody would rather were different is not
- Out: the migration procedure, which has its own recorded runs
- Out: automating any of it. Non-goal 10

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *Checking a backlog that is already here*,
  and *Verify — and make it fail first* for the standard
- [T-178](T-178-give-the-github-binding-a-standing-verification.md) §3 step 5 — the five numbered
  steps, written so this task does not re-derive them
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — how the
  scratch repository was made and disposed of

**Acceptance criteria**
- [ ] The procedure has been run against a live backlog, and what it printed is recorded — the
      actual output, not a verdict
- [ ] It has been run against a backlog broken on purpose in **two** ways, and **row 2 and row 3
      each named their own defect**. A run naming one and not the other is recorded as a
      half-proven procedure rather than as a pass
- [ ] The repair run passes, so the failure is shown to be the backlog's rather than the procedure's
- [ ] Any row that could not be answered from `enumerate`'s output is corrected in the binding, and
      the correction says what the run showed
- [ ] The scratch repository is deleted, and the record says the destination was never the evidence
- [ ] The binding no longer implies the procedure is unrun, and the *has been run against* register
      covers both verifications

**Open questions**
- ~~**Who runs it, and where?**~~ **Answered 2026-08-19: a session is authorised to run it.** The
  project owner granted this in a question round on 2026-08-19, and the grant covers **this task's
  run only**: creating a throwaway hosted repository, creating and mutating issues in it, running
  the standing verification against them, and recording what it printed. It is written here because
  a handoff is consumed once and renamed
  ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)), and an authorisation kept
  anywhere else is one a later session can miss or stretch to a task it never reached.

  **Two limits were measured when the grant was given, rather than assumed.** The credential a
  session can reach carries the scope needed to create the repository and its issues; it does
  **not** carry the scope that deletes a repository. So **removing the throwaway repository is the
  owner's step**, taken after the run unless that scope is added first — and a plan whose last row
  is a session deleting it is a plan that cannot execute.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run `gh auth status` and read the scope list, rather than assuming §1's two limits still hold. | The scopes, quoted in §3, and the consequence stated: creation is in reach, deleting a repository is not. |
| 2 | Create a private scratch repository, and one label per value in every vocabulary the config enumerates, as *Setup* requires. | The repository name, and the label count `gh label list` reports against the count the config's vocabulary table implies. |
| 3 | Load a subset of this project's own backlog into it as issues — chosen for hierarchy, dependencies, soft links, cross-references and closed tasks — with `parent` and `blocked_by` native at creation and the property block carrying the rest. | The issue count, and the `T-NNN` -> issue-number mapping, recorded in §3. |
| 4 | Write a scratch instrument that answers the nine rows from one `enumerate` fetch, and run it against the healthy backlog. | The instrument's actual output, quoted in §3. A pass is expected and proves nothing on its own. |
| 5 | Break exactly two things: delete one `related` line from one body, and repoint one property-block reference at an issue number nothing holds. | The two edits named — which issue, which line, what the reference now points at. |
| 6 | Run the instrument again. | The actual output. **Row 2 must name the repointed reference and row 3 must name the issue that lost its `related`.** A run naming one and not the other is recorded here as a half-proven procedure, not as a pass. |
| 7 | Repair both edits and run a third time. | The actual output, showing the failure was the backlog's and not the instrument's. |
| 8 | For each of the nine rows, say whether it was answerable from `enumerate`'s output alone; correct the binding where it was not. | Either a binding edit with what the run showed, or a recorded finding that every row was answerable. |
| 9 | Rewrite the binding so it no longer implies the standing procedure is unrun, and so *What this procedure has been run against* covers both verifications. | The edited section of `plugin/skills/taskmd/docs/bindings/github-issues.md`. |
| 10 | Hand the scratch repository to the owner for deletion and record that the destination was never the evidence. | A line in §3 naming the repository, saying deletion is the owner's step, and saying what would have to be re-run rather than re-read. |

**Sequencing.** Step 1 is first because the whole plan rests on it: a credential that had lost the
`repo` scope would invalidate steps 2-7 before any of them cost anything. Step 4 comes before step 5
for the reason *Verify* gives about the migration — the clean run is the baseline the broken run is
read against, and a procedure whose first ever run is against a broken backlog cannot tell a defect
it caught from a defect it invented.

**Decisions**

- **The nine rows are answered by a scratch instrument, not by eye — and the instrument is not
  shipped.** Twenty-odd issues against nine rows is more comparison than a reading can be trusted
  with, and the run has to be repeatable three times over for steps 4, 6 and 7 to mean anything.
  *Rejected:* answering the rows by inspection, which cannot produce the identical third run step 7
  needs; and *rejected:* keeping the instrument in the repository, which is non-goal 10 and is what
  the scope line excludes. It lives outside the working tree for the run and goes with the scratch
  repository.
- **The scratch backlog is drawn from this project's own tasks rather than invented.** Invented
  issues would be shaped by what the nine rows look for, which is the way a check comes to pass on
  a corpus built to satisfy it. *Rejected:* a synthetic backlog, for that reason.

**Outputs**

- `tasks/T-193-make-the-standing-github-check-fail-before-trusting-it.md` (§3, the three runs and
  what each printed)
- `plugin/skills/taskmd/docs/bindings/github-issues.md`

## 3. Implement

**Run on 2026-08-21**, under the grant §1 records. Destination:
`github.com/uchimata2/taskmd-standing-check-scratch`, private, created for this run.

### Step 1 — the two scope limits, measured rather than assumed

```text
$ gh auth status
  Logged in to github.com account uchimata2 (keyring)
  Token scopes: 'gist', 'project', 'read:org', 'repo', 'workflow'
```

`repo` creates the repository and its issues; `delete_repo` is absent, so §1's second limit still
holds and step 10 is the owner's. `gh` is 2.96.0 — the version the binding's `{"nodes": [...],
"totalCount": N}` note was measured on, and the fetch confirmed that shape unchanged.

### Step 2 — the repository and its labels

28 labels created, one per value in the five vocabularies `.taskmd/config.md` enumerates, derived
from that table rather than typed: status 8, phase 4, type 7, business_value 4, effort 5.
`gh label list` reported 28 carrying a `:`.

### Step 3 — the backlog

24 tasks, taken as the closure of the four granted tasks under `parent` and `blocked_by` and then
grown to 24: T-001, T-002, T-004, T-005, T-007–T-011, T-014–T-018, T-079, T-083, T-108, T-151,
T-178, T-181, T-190–T-193. 20 closed and 4 open; 4 sub-issue edges, 7 dependency edges, 15 issues
carrying a `Related` line. Created in dependency order with `--parent` and `--blocked-by` native,
then every body round-tripped through `--template` to rewrite references to their `#N`.

### Step 4 — the first run, and what it was worth

**FAIL, 14 — and all fourteen spurious.**

```text
row 7  FAIL  no closed issue carries a template slot - examined 20 closed issues
        #20: closed and still holds the template slot '<value>'
        #20: closed and still holds the template slot '<venue>'
        #16: closed and still holds the template slot '<plugin-root>'
        #14: closed and still holds the template slot '<pattern>'
        #6:  closed and still holds the template slot '<backend>'
        ... 14 in total, across #2, #6, #7, #8, #14, #16 and #20
```

Row 7 had been read as *any angle-bracket span*, which is what its one line invites, and every hit
was ordinary notation in ordinary prose. **This is the failure the migration *Verify* records for
references — eight failures, all eight spurious — one row over, and the standing half carried no
equivalent warning.** `check_abandoned_slots` in `plugin/skills/taskmd/taskmd/cli.py` settles it: the
slot set is `slot_lines(root, schema)`, read from the project's own templates; the comparison is a
whole stripped line; and `without_code` runs first. Nine slot lines came from
`tasks/_task-template.md`.

**The correction went into the binding and not only into the instrument** — that is step 8, and it is
the acceptance criterion about a row that cannot be answered as written.

### Step 4, continued — the clean run

```text
row 1  pass  enumerated field values - examined 120 labels on 24 issues
row 2  pass  every reference resolves - examined 37 references
row 3  pass  related still exists - examined 15 issues that carried a Related line in the baseline
row 4  pass  a blocked issue has an open blocker - examined 0 issues labelled status:blocked
row 5  pass  no dependency cycle - examined 7 blockedBy edges
row 6  pass  no body stores a derived edge - examined 24 property blocks
row 7  pass  no closed issue carries a template slot - examined 20 closed issues against 9 template slot lines
row 8  pass  no date-shaped value that is not a date - examined 0 date-shaped property values
row 9  pass  no label reads as a version - examined 0 non-enumerated labels

PASS - all nine rows
```

### Steps 5–6 — broken on purpose, and what each row named

```text
#17 Related line deleted; it held: #3, #6, #8
#23 property-block reference #19 repointed at #999
```

```text
row 2  FAIL  every reference resolves - examined 34 references
        #23: property block references #999, which is not an issue here
row 3  FAIL  related still exists - examined 15 issues that carried a Related line in the baseline
        #23: Related changed from '#19, #6' to '#999, #6'
        #17: the Related line is gone; it held #3, #6, #8

FAILED rows: 2, 3
```

**Row 2 named the repointed reference and row 3 named the issue that lost its `Related` line**, so
the criterion is met rather than half-met. Row 3 also named #23, which is correct and is not noise:
the repoint changed a `Related` line, and comparing the whole line is what lets row 3 see a *changed*
edge rather than only a deleted one. The two rows overlap on that line by construction.

### Step 7 — the repair run

Both edits reversed. `PASS - all nine rows`, with the same nine counts as the clean run — 37
references again, 15 `Related` lines again. The failure was the backlog's and not the instrument's.

### Steps 8–9 — what the runs sent back into the binding

Three edits to `plugin/skills/taskmd/docs/bindings/github-issues.md`:

- **Row 7 rewritten** to say a slot is a whole line of your task template, code blanked first, and
  explicitly *not any angle-bracket span* — with a paragraph carrying the fourteen-spurious
  measurement, written in the same voice as the reference-shape warning it mirrors.
- **Row 3 now says it needs two fetches**, and that a first run cannot answer it. The section is
  headed *Fetch once*, which is true of eight rows and was never true of this one.
- **A paragraph naming both rows as needing something the fetch does not carry**, because a row that
  examined nothing scores exactly like a row that found nothing.

Plus the register: *What this procedure has been run against* now covers both verifications, with the
four runs above as a table and the three-vacuous-rows note.

**Decisions & assumptions**

- **`Related` was trimmed to the 24-task subset — the subset *is* this migration's source, so an id
  outside it names nothing here and is prose, exactly as the binding's own `T-999` example is.**
  Rejected: carrying all 195 ids, which would have made row 2 fire around two hundred times on the
  clean run and buried the deliberate break it exists to catch — 2026-08-21.
- **The instrument answering the nine rows is not shipped — non-goal 10, and §1's scope line.** It
  lives outside the working tree and goes with the scratch repository. Rejected: keeping it, which
  would make this task ship the automation its scope excludes — 2026-08-21.
- **The register keeps both its name and its position.**
  [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) cites *What this procedure
  has been run against* by name three times and by position once, including in a PASS row of its own
  review; renaming or moving it would falsify a closed record while every link still resolved. So the
  standing half is documented above the procedure it describes, and one sentence says why. Rejected:
  retitling it to cover both, and moving it below the standing section — 2026-08-21.

**Surfaced, not absorbed**

- **Three of the nine rows examined nothing on this corpus** — row 4 (no issue labelled
  `status:blocked`), row 8 (`created` and `updated` have native carriers, so no date reaches a
  property block) and row 9 (this project's grouping field `work_package` is not enumerated, so it is
  a property-block line and not a label at all). Rows 8 and 9 cannot fire for *any* project
  configured like this one, which is a property of the config rather than of the backlog. It is
  recorded in the binding, and it is evidence
  [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) will want — whether
  it needs a task of its own is that task's question and not this one's.

**Outputs produced**

- `plugin/skills/taskmd/docs/bindings/github-issues.md`
- this record

### Step 10 — the destination

`github.com/uchimata2/taskmd-standing-check-scratch` is **the owner's to delete**: the credential a
session reaches carries `repo` and not `delete_repo`, measured in step 1, and §1 says a plan whose
last row is a session deleting it cannot execute. **It was never the evidence.** The counts above are,
and they were produced by running the procedure — anyone doubting them re-runs it against a backlog
of their own rather than looking for this repository.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The procedure has been run against a live backlog, and what it printed is recorded — the actual output, not a verdict | met | Four runs against 24 live issues, each quoted in §3 row by row **with what each row examined**: 120 labels, 37 references, 15 `Related` lines, 7 dependency edges, 24 property blocks, 20 closed issues against 9 slot lines. The counts are in the record because a row that examined nothing prints the same word as a row that found nothing |
| It has been run against a backlog broken on purpose in **two** ways, and **row 2 and row 3 each named their own defect**. A run naming one and not the other is recorded as a half-proven procedure rather than as a pass | met | Two breaks, on two different issues. Row 2 named #23's reference repointed at #999; row 3 named #17's deleted `Related` line. Each named its own, so this is not the half-proven case. Row 3 additionally named #23, which is the repoint showing in the line row 3 compares — correct, and noted in §3 rather than counted as noise |
| The repair run passes, so the failure is shown to be the backlog's rather than the procedure's | met | Run 4: `PASS - all nine rows`, returning to the clean run's counts — 37 references and 15 `Related` lines, from 34 and a changed line while broken |
| Any row that could not be answered from `enumerate`'s output is corrected in the binding, and the correction says what the run showed | met | Two rows, not one. **Row 7** needs the project's template slot lines, which are not issue data — read by shape it produced **14 failures, all 14 spurious**, on the first run this procedure ever had, and that measurement is now the paragraph warning against it. **Row 3** needs a fetch kept from before, so *fetch once* was true of eight rows and never of it. Both corrections are in `plugin/skills/taskmd/docs/bindings/github-issues.md` |
| The scratch repository is deleted, and the record says the destination was never the evidence | **not met** | Second half met — §3 step 10 says it, and says what the evidence is instead. First half cannot be met by a session: `gh auth status` reports no `delete_repo`, which is §1's measured limit and not a reading of the grant's boundary → **child task: [T-196](T-196-delete-the-scratch-repository-the-standing-check-ran-against.md)** |
| The binding no longer implies the procedure is unrun, and the *has been run against* register covers both verifications | met | The register carries a *The standing check* half with the four runs; the *make it fail first* instruction now says it has been done and why it stays. The register kept its name and position on purpose — [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) cites it by both, and moving it would have falsified a closed record while every link still resolved |

**The criterion this task cared about most is the one that failed first.** T-193 exists because
[T-178](T-178-give-the-github-binding-a-standing-verification.md) closed with an unrun check, and the
first run found the defect in the **procedure** rather than in the backlog — 14 spurious failures,
from the same shape mistake *Verify* records one row over. That is the whole argument for running a
check before trusting it, made again on the check written to make it.

**Open questions, re-read before closing.** §1's one question was answered by the owner on
2026-08-19 and is struck through; nothing in it is still live. §3 raises no question aimed at anyone
else — the three vacuous rows are recorded as evidence for
[T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) to weigh, which is that
task's judgement to make and not a question left hanging here.

**Child fix tasks raised**
- [T-196](T-196-delete-the-scratch-repository-the-standing-check-ran-against.md) — delete the scratch repository

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **Five criteria met, one carried by [T-196](T-196-delete-the-scratch-repository-the-standing-check-ran-against.md).** The run found its first defect in the procedure rather than in the backlog: row 7 read by shape gave 14 spurious failures on a healthy 24-issue backlog, the same mistake *Verify* records for references. Rows 7 and 3 were corrected in the binding and the register now covers both verifications. The scratch repository at `uchimata2/taskmd-standing-check-scratch` is the owner's to delete - `gh auth status` carries no `delete_repo`, measured on the day. |
| 2026-08-21 | → planned | **Plan written under the 2026-08-19 grant**, which covers this task's full lifecycle. Ten steps, ordered so the scope check comes first and the clean run precedes the broken one. Two decisions recorded in §2: the nine rows are answered by a scratch instrument rather than by eye, and that instrument is not shipped (non-goal 10, and §1's scope line); the scratch backlog is drawn from this project's own tasks rather than invented, because a corpus built to satisfy the rows is one the rows cannot fail on. |
| 2026-08-21 | → specified | **`specify` closed with nothing added.** Its exit criterion is acceptance criteria written and agreed by whoever owns the outcome; the criteria were written when the task was raised, and the one open question was answered by the owner on 2026-08-19 and struck through in §1. Recorded rather than skipped, because a phase that needed no work still has to be seen to have met its criterion. |
| 2026-08-19 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-19, and not yet acted on.** The owner granted a later session the four tasks that need nobody else - T-193, T-190, T-191 and T-192 - **each through its full lifecycle, committed and pushed**. It is written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)), and an authorisation kept only there is one the session after next cannot find. **It reaches these four and no others**: the remaining open tasks each wait on a person, an external event, or a question still the owner's. **The grant does not extend to deleting the throwaway repository** - §1 records why, and a plan whose last row is a session deleting it cannot execute. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round: a session is authorised to run this.** The alternative — the owner running it and handing back the output — was offered and declined. The grant and its two measured scope limits are in §1, where a later session will find them; deleting the throwaway repository falls outside it. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)): the grant authorises this task's work when it is asked for, not now. |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-178](T-178-give-the-github-binding-a-standing-verification.md) raised it. **The grant does not make this runnable**, and that is not a reading of its boundary but of what it authorises: creating and mutating issues on a hosting service is a write outside these records, and §1's question asks for exactly that permission. So the task ends in its written question, which is what the grant's own instruction says to do. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s review as the one criterion it did not meet. `high` and `m`: the procedure guards a documented path to unrecoverable loss, and until it has failed once nobody knows whether it guards anything. A child of T-178 rather than a soft link, because T-178 is not finished until this is — its own §4 says so. |
