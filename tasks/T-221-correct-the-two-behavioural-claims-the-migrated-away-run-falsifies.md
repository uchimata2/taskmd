---
id: T-221
title: Correct the two behavioural claims the migrated-away run falsifies
type: fix
status: planned
phase: plan
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

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | proposed → planned | Plan written under the owner's authorisation of 2026-08-22, which covers **this phase and no more**. **Step 4 is the task and steps 2-3 are the occasion**: the two defects were found by a reader answering a different question, so they are an accident rather than a sweep, and a document that drifted twice has no reason to have drifted exactly twice. *Rejected: correct the two and stop* — it leaves the document trusted exactly where nobody has checked it. **One decision is deliberately deferred to a statement rather than an action**: if `check` doing real work changes what *What is gone* concludes, that touches the document's balance, which [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed as accepted and [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) §1 puts out of scope — so step 3 states the consequence and stops. **The dates stay in the corrected sentences**: the note carries `measured 2026-08-18` and was probably true then, and deleting the date while fixing the sentence would hide that the tool moved and the document did not. |
| 2026-08-22 | → proposed | Raised from [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s reader run, which is a task about framing and turned up two defects of fact. Raised rather than absorbed: T-176's §1 puts the figures and the re-balancing out of scope, and correcting a shipped document is not a thing to do inside a task measuring how that document reads. **The reader could not settle it and did not pretend to** — they named the contradiction, named the fact that resolves it, and made their recommendation conditional on it. A session had the command and ran it, which is what turned a reader's doubt into two measured defects in one turn. `high` because an adopter reading either sentence uninstalls a tool that is still doing work for them, and the document's own coverage table already says so three sections earlier. |
