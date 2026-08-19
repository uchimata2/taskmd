---
id: T-178
title: Give the GitHub binding a standing verification, not only a migration-day one
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-108, T-177, T-041]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-18
updated: 2026-08-19
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-178 — Give the GitHub binding a standing verification, not only a migration-day one

## 1. Specify

**Outcome**
A procedure in the GitHub Issues binding that a project can run at any time to check its own issue
backlog — the standing counterpart of the migration-day *Verify* that binding already carries.

**Why this one**
**There is one verification in that binding and it runs once.**
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) built a real one —
165 tasks to 165 issues, five checks, and three recorded failing states including a rule that was
wrong when first written. It compares a source against a destination, so it can only run on the day
there is a source. The day after a migration, nothing checks anything again, ever.

**The gap this leaves is silent data loss, not degraded convenience.** The binding's own *update*
rules say it plainly: `related` lives in the property block and nowhere else on this backend, there
is no far end holding a copy and no derived view that can notice one has gone, a partial body
rewrite deletes it — and **`gh` exits 0 for the destructive edit exactly as for the correct one**.
On the local backend `check` catches a dangling reference. Here nothing does. A warning in prose is
not a control.

**It belongs in the binding and not in the tool**, and that is settled rather than open: non-goal 5
keeps every network call out of the core, and says anything remote is the agent's job through its
own tools. The migration *Verify* is already built that way, so this follows a shape that has been
walked on a live repository rather than inventing one.

**Scope**
- In: a procedure an agent can run against a live issue backlog, checking what the local `check`
  checks and this backend can still answer — references resolving, vocabularies, edges present in
  both directions, and `related` surviving
- In: making it fail first, on a deliberately broken issue, before it is allowed to pass. That is
  this repository's rule and it is the reason the migration verification is trustworthy
- Out: putting any of it in the CLI. Non-goal 5, and it is not a close call
- Out: the local-Markdown binding, which has `check` and needs nothing
- Out: continuous or scheduled running. Non-goal 10, and a procedure is what is being asked for

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *Operations* for what a write can destroy,
  and *Verify — and make it fail first* for the shape and the standard
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the three
  failing states the migration verification was made to produce, including `gh` exiting 0 on the
  destructive edit
- [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md) — the body-rewrite rule proven by
  being made to fail

**Acceptance criteria**
- [ ] The binding carries a procedure a project can run against a live backlog at any time, using
      `gh` only
- [ ] It covers what this backend can still answer, including **`related` surviving**, which is the
      one with a documented path to unrecoverable loss and a zero exit code
- [ ] **All seventeen of the local checks are walked**, and each is placed as covered here, cannot
      occur here, or still runs locally — with the reason, not the verdict
- [ ] The coverage statement ships **with** the procedure, so no run is read as reaching further
      than it does
- [ ] The procedure has been **made to fail** on a deliberately broken backlog before it is trusted,
      and what it printed is recorded — or the gap is stated, with what would have been done
- [ ] `specify` says whether the generic half — every binding declaring its own coverage, in
      `BINDING.md` — is in scope here or a sibling task, and does not leave it implied

**Scope, decided at `specify` from the owner's widening**
- Out, and raised instead: **the generic half.** The owner's answer of 2026-08-19 says the coverage
  belongs to whichever backend is in use, declared per binding, and names
  `plugin/skills/taskmd/docs/BINDING.md` as what would carry that. Making the contract *require* a
  coverage statement changes what every binding must satisfy, including
  `plugin/skills/taskmd/docs/bindings/local-markdown.md`, and it is a different deliverable with a
  different blast radius. It is [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md).
  **What this task does instead** is ship the GitHub table in the shape a contract could later
  require, and say in the document that the coverage is *this* backend's — so the generic task
  inherits an example rather than a rewrite.

**Open questions**
- ~~**How much of `check` can this backend actually answer, and is the honest answer worth
  shipping?** Some of the 17 checks have no meaning here — a stale index cannot exist where the issue
  list *is* the index. **Answer at `specify` by walking the list of checks against the backend**, so
  the procedure ships with a stated coverage rather than an implied one; a verification whose reach
  nobody wrote down is the failure this repository keeps re-learning.~~ **Answered by the owner on
  2026-08-19: walk all seventeen, and the coverage belongs to whichever backend is in use rather
  than to GitHub** — see the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the seventeen checks from `cmd_check` rather than from any document that lists them, and record which of them take a task as input | The derived set, in §3 |
| 2 | Place each one against this backend: covered, cannot occur, or still local — with the reason | The coverage table |
| 3 | Write the procedure from the covered rows, working from one `enumerate` fetch | The new section in the binding |
| 4 | Write the fail-first instruction, naming the two rows a broken backlog must trip | The same section |
| 5 | Try to run it against a deliberately broken backlog | The output, or a stated gap |
| 6 | Run `check`, `index` and the suite, and read the document's diff | The output, in §3 |

**Decisions taken at `plan`**

- **The procedure works from one fetch, not one call per check.** *enumerate*'s command already
  returns every field the nine rows need, and nine `gh` calls over a 165-issue backlog is the shape
  that gets a check switched off. *Rejected: a call per row*, which reads more simply and is slower
  by two orders of magnitude on the corpus this was measured against. — 2026-08-19
- **The coverage table states reasons, never verdicts.** *Cannot occur* is a claim, and a reader has
  to be able to disagree with it: GitHub allocating issue numbers is why duplicate ids cannot occur,
  and that is checkable where the word *no* is not. — 2026-08-19
- **The table's own weakness is written into the document.** It is a hand-kept list of a set the code
  owns, which is the class [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)
  guards on the local side and nothing guards here. Saying so costs two sentences and is the only
  honest way to ship it before [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)
  exists. — 2026-08-19

**Outputs this task will produce**

- plugin/skills/taskmd/docs/bindings/github-issues.md

## 3. Implement

### Step 1 — the seventeen, derived

```text
grep -c "^    counted += check_" plugin/skills/taskmd/taskmd/cli.py
17
```

Read from `cmd_check`, not from a document — and that mattered on the day: the binding's own
*No validator* note already said *seventeen* when `cmd_check` ran **sixteen**, and
[T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) had added the seventeenth hours
earlier. A count taken from the prose would have been right by accident.

Five take no task as input, which is a signature fact rather than a judgement: `check_links`,
`check_unreachable_templates`, `check_template_fields`, `check_config_drift`, `check_wide_rows`.

### Step 2 — the coverage, and how it comes out

| Placement | Checks | Count |
| :--- | :--- | ---: |
| **Covered by the new procedure** | vocabularies, references, blocked-without-blocker, cycles, stored-derived, abandoned slots, dates, label shape, and `related` surviving — which is not a local class at all, because locally the file *is* the copy | 9 rows |
| **Cannot occur here** | duplicate id, id width, parked task (one `check_anomalies`), stale index | 2 checks |
| **Still local, and still run** | broken/ignored link, wide row, config drift, duplicate index — the five-minus-one that take no task — plus declared outputs, which compares against a working tree the project still has | 6 checks |

**The nine rows are not nine checks**, and the table above is written so that is visible: `related`
surviving has no local counterpart, and `check_anomalies` is one check carrying three classes. A
coverage table that summed to seventeen would be tidier and would be arithmetic rather than a
statement.

**One row of the local side is deliberately not carried across**: the two template checks. They read
a task template in a folder, and a project keeping a GitHub issue template gets nothing — stated in
the document rather than left for someone to discover.

### Steps 3–4 — the procedure

`### Checking a backlog that is already here`, placed after *What this procedure has been run
against* and before *The reverse direction*, so the two verifications sit together. One fetch, nine
rows, and a fail-first instruction naming rows 2 and 3 as the ones a deliberately broken backlog
must trip — the same two the migration verification got wrong twice.

### Step 5 — the gap, stated rather than implied

**The procedure has not been made to fail, and it has not been run at all.**

The migration verification is trustworthy because it was run against a private repository created
for the day and deleted after it, and it failed three times before it passed. The equivalent here
needs a live issue backlog to break on purpose: creating a repository, creating issues, then
deleting a `related` line and pointing a reference at an issue that does not exist. **Creating and
mutating issues on a hosting service is not something this session may do unattended** — the grant
it runs under authorises a lifecycle over these records, not writes to anything outside them, and
the repository the migration used was deleted the same day, so nothing exists to read either.

What would be done, written so the next attempt does not re-derive it:

1. A private scratch repository, 20-odd issues with labels, `blockedBy`, `parent` and property
   blocks, created from this project's own backlog as the migration procedure does it.
2. Run the nine rows. Expect a pass.
3. Break exactly two things: delete one `related` line, repoint one property-block reference at an
   issue number nothing holds.
4. Run again. **Row 2 must name the repointed reference and row 3 must name the issue that lost its
   `related`.** A run that names one and not the other is a half-proven procedure and is worth
   recording as such.
5. Repair, run again, expect a pass. Delete the repository.

Raised as [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md).

### Step 6 — verification of the change itself

```text
Wrote tasks/README.md
OK - ... task(s) ...
Ran 288 tests ... OK
```

The document's diff is **one hunk**: the new section. Nothing else in the file moved.

**Decisions & assumptions**

- All three `plan` decisions held. — 2026-08-19
- **The generic half is a sibling task, decided at `specify` and recorded in §1** rather than folded
  in. The owner's widening is real and the contract is the right home for it; changing what every
  binding must satisfy is not a paragraph in one binding. — 2026-08-19
- **Assumption, recorded as one**: the nine rows are answerable from *enumerate*'s output, checked
  field by field against the command in the same document. They have not been answered against a
  response, which is the gap step 5 states and [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) carries. — 2026-08-19

**Outputs produced**
- plugin/skills/taskmd/docs/bindings/github-issues.md — *Checking a backlog that is already here*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A procedure runnable at any time, `gh` only | **met** | *Checking a backlog that is already here*. One fetch, nine rows, no taskmd command anywhere in it |
| Covers what the backend can answer, including `related` surviving | **met** | Row 3, and it is the row with no local counterpart — the file is its own copy locally, which is why the class exists only here |
| All seventeen walked, each placed with its reason | **met** | §3 steps 1–2. Derived from `cmd_check`, and the derivation caught the shipped prose being wrong by one |
| The coverage ships with the procedure | **met** | *What this does not cover, and why*, in the same section, and it states its own two weaknesses rather than only the backend's |
| Made to fail before being trusted, or the gap stated with what would be done | **not met** | §3 step 5. It has not been run at all, and the reason is that it needs issues created and broken on a hosting service. Five numbered steps are written down for whoever can → **child task [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)** |
| `specify` says whether the generic half is in scope | **met** | §1 *Scope, decided at `specify`*: out, and raised as [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md), with what this task ships instead |

**Five met, one carried.** The one not met is the one this repository's own rule cares about most —
a check that has only ever succeeded has not been tested, and this one has not even done that. The
document says so where a reader meets it, not only here.

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner on 2026-08-19 and is struck through there. The widening
that came with it is routed to [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)
and named in §1 rather than left in a log row. Nothing else here is addressed to anyone else.

**Child fix tasks raised**
- [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) — run it, and break a backlog first
- [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) — the generic half, in the contract

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 6 of the eight. The binding gains **Checking a backlog that is already here** — one `enumerate` fetch, nine rows, `gh` only — beside the migration-day verification it is the standing counterpart to. All seventeen local checks were walked, **derived from `cmd_check` rather than from any document**, which is what caught the shipped prose saying seventeen while sixteen ran. The coverage ships with the procedure and states its own weaknesses: it is a hand-kept list of a set the code owns, and it is this backend's rather than every backend's. **Closed with one criterion carried, and it is the important one**: the procedure has not been made to fail, because that needs issues created and broken on a hosting service, which this session may not do unattended. Five numbered steps are written for whoever can, as [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md); the owner's widening about per-binding coverage is [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md). |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 6 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered by the owner: walk all seventeen checks first — and the outcome must not be GitHub-shaped.** Asked in the backlog-wide round of 2026-08-19. The coverage statement ships with the procedure rather than being implied, for the reason §1 gives: a verification whose reach nobody wrote down is the failure this repository keeps re-learning. *Rejected: shipping the procedure without the coverage list*, which is faster and turns a green result into a false assurance. **The answer widens the outcome, and the widening is the owner's own words**: today the backend is GitHub, tomorrow it may be Notion or another service, so what ships must be flexible — the coverage belongs to whichever backend is in use, declared per binding, rather than being seventeen rows written once about GitHub. `plugin/skills/taskmd/docs/BINDING.md` is the contract that would carry that, so `specify` judges whether the generic half is in scope here or is a sibling task, and says which. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question about whether taskmd is prepared to keep providing controls after a migration. The honest answer was no on the enforcing side, and this is the sharpest instance: **a documented path to unrecoverable loss of every soft edge, with a zero exit code and no detector**. Shaped as a binding procedure rather than a tool feature because `docs/SCOPE.md` §4 non-goal 5 settles that, and because the migration verification beside it is already built that way and was proven on a live repository. **Not covered by any standing authorisation.** |
