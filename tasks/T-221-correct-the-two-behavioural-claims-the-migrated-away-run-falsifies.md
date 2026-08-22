---
id: T-221
title: Correct the two behavioural claims the migrated-away run falsifies
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-176, T-166, T-168]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-221 — Correct the two behavioural claims the migrated-away run falsifies

## 1. Specify

**Outcome**
`plugin/skills/taskmd/docs/bindings/github-issues.md` no longer states two things about `check` that
running it against a project with no tasks folder disproves, and the record says what the tool
actually does.

**Why this one**
**An adopter's decision turns on these two sentences, and both are wrong in the direction that costs
them the tool.** They were found by [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s
uninvolved reader on 2026-08-22, who could not resolve them from the document and named the missing
fact as the one that would most change their recommendation. Measured the same day:

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md
1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), ...
CONFIG DRIFT  status: shipped default adds 'specified', 'planned', ...
Scope  no task file was read, and the checks that open one did not run. ...
exit 1

$ ./plugin/bin/taskmd context|index|list --root tests/fixtures/migrated-away
exit 2, exit 2, exit 2
```

**Claim 1 — the *No validator* note, line 628.** It says *"You lose all seventeen only because the
config error is raised while the schema loads, before any check is reached."* Checks **are** reached:
two fired and were reported. The note carries a 2026-08-18 date, so the likeliest history is that it
was true when written and the tool changed under it — which is why this is a fix and not a dispute.

**Claim 2 — the *What is gone* rebuttal, line 618.** It says *"the commands exit 2 either way"*, and
that sentence is doing the whole work of *"None of them is a reason to keep taskmd installed"*.
`context`, `index` and `list` do exit 2. **`check` exits 1 and reports real problems**, so one of the
four commands does work an uninstalled taskmd cannot, and the rebuttal overstates.

**The coverage table at line 553 is the one that is right** — *"Still local, and still run"*, verified
by the run above. So the document contradicts itself and the correct half is already in it.

**Scope**
- In: the two sentences, corrected against a run rather than against reasoning
- In: whether any other behavioural sentence in the document has drifted the same way — the two found
  were found by a reader answering a different question, which is not a sweep
- Out: the document's framing and arrangement. That is
  [T-167](T-167-stop-the-listing-pricing-only-the-rival.md)'s closed decision and
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s subject, not this one
- Out: changing `check`'s behaviour. The behaviour is right; the document describes the old one

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` lines 553, 618 and 620-630
- `tests/fixtures/migrated-away/` — the project shape the claims are about, and the one the run used
- [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) §3 — the reader's
  question 3, which is where both were found

**Acceptance criteria**
- [ ] Each corrected sentence is backed by a quoted command and its exit code, dated
- [ ] The document no longer says two different things about whether the five checks run
- [ ] Every other behavioural claim in the document is checked the same way, and the ones that were
      re-run are listed — including those that turned out to be right
- [ ] Whether `check` exiting 1 rather than 2 changes what *What is gone* concludes is stated, not
      left for a reader to work out

**Open questions**
- **None.** Both claims are measured and the direction of each correction is fixed by the measurement.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-run all four commands against `tests/fixtures/migrated-away` and capture the output with its date — the evidence every correction below cites | the quoted runs and their exit codes, dated |
| 2 | Correct the *No validator* note against that output, keeping its 2026-08-18 date visible | the corrected note |
| 3 | Correct the *What is gone* rebuttal, and state whether the section's conclusion changes now that one of the four commands does work an uninstalled taskmd cannot | the corrected sentence, and that statement |
| 4 | **Sweep every other behavioural claim in the document**, re-running each rather than reasoning about it | the list of claims re-run, including the ones that were right |
| 5 | Read the document against itself: no two sentences left disagreeing about whether the five checks run | the consistency pass, and anything it moved |

**Step 1 measures before steps 2–4 commit**, and the reason is this task's own subject: the two
defects exist because sentences about behaviour were written once and never re-run. A correction
argued from reasoning would be the same mistake in the opposite direction.

**Step 4 is the point of this task, not steps 2 and 3.** The two defects were found by a reader
answering an entirely different question — that is an accident, not a sweep, and a document that
drifted twice has no reason to have drifted exactly twice. Finding the claims: any sentence naming a
command, an exit code, a count, or what the tool does or does not do. Grepping the command names and
`exit` is the floor; reading the document is the ceiling, because a claim can be phrased without
naming anything. *Rejected: correct the two and stop* — it leaves the document trusted precisely
where nobody has checked it, and makes the next reader's accident into the next task.

**The dates stay in.** The *No validator* note carries `measured 2026-08-18` and was most likely true
when it was written. Deleting the date while correcting the sentence would hide the thing worth
knowing — that the tool moved and the document did not — and would make the third acceptance
criterion uncheckable by whoever comes next.

**Step 3 has an outcome this plan must not pre-empt.** If `check` doing real work changes what *What
is gone* concludes, that touches the document's balance, which
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed as accepted and
[T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) §1 puts out of scope.
So step 3 **states** the consequence and stops; re-balancing on the back of it would be reversing a
decision the owner took, on evidence that was not collected for that purpose.

**What this task must not do is change `check`.** Every defect here is in the description. The
behaviour the run showed — document checks reached, task checks skipped, and a `Scope` line saying
which — is the behaviour the coverage table already promises.

## 3. Implement

### Step 1 — the run every correction below cites

All four commands against `tests/fixtures/migrated-away`, 2026-08-22. `context` was given an id, so
its exit code is the config error and not a usage error — the §1 evidence block ran it bare and could
not have distinguished the two:

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md

1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), 0 template(s), 0 template field value(s), 1 vocabulary row(s), 0 section reference(s)
CONFIG DRIFT  status: shipped default adds 'specified', 'planned', ...
Scope  no task file was read, and the checks that open one did not run. ...
exit 1

$ ./plugin/bin/taskmd context T-1 --root tests/fixtures/migrated-away
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but the project root has no such folder. ...
exit 2

$ ./plugin/bin/taskmd index --root tests/fixtures/migrated-away   → exit 2, same CONFIG ERROR
$ ./plugin/bin/taskmd list  --root tests/fixtures/migrated-away   → exit 2, same CONFIG ERROR
```

**One dead link here, not two.** The 2026-08-18 note said *two dead links*, and it was measured
against a real migrated project rather than against this fixture. Both corrections now cite the
fixture, because a fixture ships with the repository and reproduces for anyone.

### Step 4 — the sweep, and what it found

The sweep found **a third defect the two known ones did not predict**, and it is not the same kind of
defect. The coverage table listed `duplicate index` among the checks that survive a migration. It
does not: it recognises a second table by the task ids it already knows, and a project with no task
folder gives it none, so it is not reached at all. **It was wrong on the day it was written, not
drifted into being wrong** — the row and the code split were committed on the same day, 2026-08-19,
and the code has `check_duplicate_index` inside the branch that does not run. Measured 2026-08-22, on
a scratch copy of `tests/fixtures/alt-project` carrying one `BACKLOG.md` that repeats its three ids:

```text
with the task folder present:  DUPLICATE INDEX  BACKLOG.md: a second table of 3 known task ids ...
with the task folder removed:  OK - 2 document(s), 0 link(s), 8 table row(s), ...   (silent)
```

The same document, unedited, in both runs. The sweep also found `section reference` — added
2026-08-22 — missing from the table altogether; it does survive, and it now has the row
`duplicate index` vacated.

**Every claim re-run, including the ones that were right:**

| Claim | Method | Result |
| :--- | :--- | :--- |
| `check`, `context`, `index`, `list` against a project with no task folder | step 1's run | `check` **wrong**, the other three right |
| The five that survive a migration | step 1's counted units, which name every check that ran | **wrong** — `duplicate index` swapped for `section reference` |
| `duplicate index` survives | the two-project experiment above | **wrong**, and wrong from the day it was written |
| `list --json` carries no `type`, `owner`, `business_value`, `effort`, `deliverables`, no body | `taskmd list --json --limit 1` | right as amended 2026-08-22 — four arrived, `deliverables` did not, no body |
| The skill costs 414 characters in the listing | recomputed from the shipped `SKILL.md` | right — 397 for the description, 414 for the listing line |
| `blockedBy` / `blocking` / `subIssues` are `{nodes, totalCount}`; `parent` is a plain object or absent; `gh` 2.96.0 | read-only `gh issue list --json …` against this project's own repository | right, on `gh` 2.96.0, which is this machine's version |
| The four commands cannot reach a network | every import in the package, listed | right — no network module is imported. Stated as an inventory, not as a run, because absence of a call is not a thing a run shows |

**What was not re-run, and why.** Four measurements describe `gh` against a real backlog: the five
`--template` round trips holding at 204, the 165-task migration's eight spurious failures, the
24-issue backlog's fourteen, and the token scope. Re-running any of them means **creating issues on
GitHub**, an outward-facing write nothing here authorises, and a new repository does not reproduce
the backlog each was measured on. Raised as
[T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) rather
than left implicit, because a half-swept document reads as a swept one.

**Decisions & assumptions**
- **Cite the shipped fixture, not the real project the 2026-08-18 note used** — a fixture reproduces
  for any reader and a private project does not; the figure changes from two dead links to one, and
  that is the fixture's data rather than a correction — 2026-08-22
- **Give `duplicate index` its own row rather than deleting it from the surviving list** — the state
  it describes *can* occur on GitHub, so it belongs beside *closed parent with an open child* rather
  than nowhere, and a reader who remembers it in the old row needs to be told where it went —
  2026-08-22
- **Rename the section heading** *The four commands do not come with you* — it is itself the claim
  being corrected, and leaving it while correcting the paragraph beneath would keep the contradiction
  at the one altitude a skimming reader reads — 2026-08-22
- **Drop the counts `seventeen` and `five` from the *No validator* note** — the document already
  states, three sections earlier, that a count of a set the code owns is either dated as a
  measurement or not written at all; the note is being rewritten anyway, so keeping them would be
  re-adding what that paragraph removed — 2026-08-22
- **Leave *the four commands cannot reach a network* alone** — a project's declared `after_write`
  hook is a file in its own repository and could contain anything, so the sentence is defeasible at
  the edge, but it is a claim about taskmd's own code and it holds there. Recorded rather than
  silently kept — 2026-08-22

**Outputs produced**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the coverage table, the four-commands
  section and its heading, the command table's `check` row, the *What is gone* preamble, and the
  *No validator* note

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each corrected sentence is backed by a quoted command and its exit code, dated | met | Four corrections, each carrying its run and `exit 1` or `exit 2`, dated 2026-08-22. The `duplicate index` row carries the two-project experiment instead, because the defect is a check *not firing* and one run cannot show that |
| The document no longer says two different things about whether the five checks run | met | The coverage table, the four-commands section, the command table and the *No validator* note now all say the same thing: the checks that open a task file stop, the ones that walk documents run, and a `Scope` line says which half went unexamined. Re-read end to end after the edits |
| Every other behavioural claim is checked the same way, and the ones re-run are listed | met | Seven claims listed above, three wrong and four right. **Read against §1's scope**, which says *drifted the same way* — a sentence about taskmd that was true when written and that the tool then falsified. Four `gh`-side measurements cannot drift that way and were not re-run; they are the wider sweep, carried by [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) as a soft edge. *Rejected: mark this unmet and hold the task open* — it would make T-224 a part of this outcome, and T-224 waits on an authorisation nobody here has, which METHOD §4 names as the residual case a soft edge is for |
| Whether `check` exiting 1 rather than 2 changes what *What is gone* concludes is stated | met | Stated in the document, in the *What is gone* preamble: the *either way* argument is weaker for one command of four, item 1 says what that command still does, and the reader weighs it. Not acted on, per the owner's ruling of 2026-08-22 |

**Child fix tasks raised**
- [T-223](T-223-correct-the-migrated-away-fixture-s-own-prose-which-still-says-all-four-commands-refuse.md) — the same defect in the fixture this task's evidence is measured against
- [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) — the half of the sweep this task could not run

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | planned → done | `implement` and `review` in one session, under the four-task grant recorded below. **Step 4 earned the task, as the plan predicted it would.** The two known defects were corrected and a **third** was found that neither predicted, and it is a different kind: the coverage table put `duplicate index` among the checks that survive a migration, and that row was **wrong on the day it was written** rather than drifted — the row and the code split were committed on the same day. So the document's failure mode is wider than *the tool moved under it*; a claim can also be written without being run. Shown with a two-project experiment rather than a single run, because the defect is a check **not** firing. The sweep also found `section reference` missing from that table altogether. **Seven claims were re-run and are listed in §3, four of them right** — including the `gh` field shapes, checked read-only against this project's own repository on `gh` 2.96.0, the version the document names. **Two tasks raised rather than absorbed**: [T-223](T-223-correct-the-migrated-away-fixture-s-own-prose-which-still-says-all-four-commands-refuse.md) for the same defect in the fixture this task's evidence is measured against, and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) for the `gh`-side measurements, which need writes to GitHub that nothing here authorises. **Both are soft edges, not children**, and §4 records the alternative that was rejected — holding this task open on T-224 would make an outcome depend on an authorisation nobody here has. Step 3's balance consequence is stated in the document and not acted on, per the owner's ruling below. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that this task, [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md), [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s remaining phases and [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) be worked through the **full lifecycle**, and the result committed and pushed. **What it covers here:** this record, carried from `planned` through `implement` and `review` to closure without stopping to ask for each phase. **What it does not cover:** any other task. It does not reach [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), which waits on a project-wide audit and then a release, nor [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), whose own grant of the same date covered `plan` and said so. **It authorises phases, not answers** - an open question that is the owner's stops this record where it stands, because no grant of phases can settle one. **Specific to this task**: the owner ruled the same day that step 3 states the balance consequence and does not act on it, and this grant does not loosen that. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). |
| 2026-08-22 | (no change) | **The owner's answer: state the consequence, do not act on it.** Put to them on 2026-08-22 because §2's step 3 had taken that position as a plan judgement, and the judgement is theirs. **Answered: confirmed.** So step 3 stands as written and the record now carries the ruling rather than my reasoning for it. **What this forecloses matters more than what it permits.** [T-167](T-167-stop-the-listing-pricing-only-the-rival.md)'s balance was accepted while the document said *the commands exit 2 either way*, and that premise is now false for one of the four - which is exactly the argument a later session could use to treat the acceptance as void and re-balance under cover of this task. It may not. The evidence here was collected to test how the document reads and to correct two sentences of fact, not to reopen a decision the owner took. **If T-167 should be revisited on the changed premise, that is a new task and a new request**, raised on its own terms where the owner can weigh it as a decision rather than meet it as a side effect. |
| 2026-08-22 | proposed → planned | Plan written under the owner's authorisation of 2026-08-22, which covers **this phase and no more**. **Step 4 is the task and steps 2-3 are the occasion**: the two defects were found by a reader answering a different question, so they are an accident rather than a sweep, and a document that drifted twice has no reason to have drifted exactly twice. *Rejected: correct the two and stop* — it leaves the document trusted exactly where nobody has checked it. **One decision is deliberately deferred to a statement rather than an action**: if `check` doing real work changes what *What is gone* concludes, that touches the document's balance, which [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed as accepted and [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) §1 puts out of scope — so step 3 states the consequence and stops. **The dates stay in the corrected sentences**: the note carries `measured 2026-08-18` and was probably true then, and deleting the date while fixing the sentence would hide that the tool moved and the document did not. |
| 2026-08-22 | → proposed | Raised from [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s reader run, which is a task about framing and turned up two defects of fact. Raised rather than absorbed: T-176's §1 puts the figures and the re-balancing out of scope, and correcting a shipped document is not a thing to do inside a task measuring how that document reads. **The reader could not settle it and did not pretend to** — they named the contradiction, named the fact that resolves it, and made their recommendation conditional on it. A session had the command and ran it, which is what turned a reader's doubt into two measured defects in one turn. `high` because an adopter reading either sentence uninstalls a tool that is still doing work for them, and the document's own coverage table already says so three sections earlier. |
