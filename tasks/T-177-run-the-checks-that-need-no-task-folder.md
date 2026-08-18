---
id: T-177
title: Decide whether check runs the checks that never look at a task file
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-163, T-178, T-179]
work_package: M6
owner: maintainer
business_value: high
effort: m
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-177 — Decide whether check runs the checks that never look at a task file

## 1. Specify

**Outcome**
A decision, and if it is yes the behaviour, on whether `check` still runs in a project whose
`tasks_dir` does not resolve — reporting the checks that do not read a task file, and refusing only
the ones that do.

**Why this one**
**Measured on 2026-08-18, reading `cmd_check`: it runs 17 checks, and five of them take no `tasks`
argument at all** — `check_links`, `check_wide_rows`, `check_unreachable_templates`,
`check_template_fields` and the `check_config_drift` advisory. They walk the document tree from the
project root. The task folder is not an input to any of them.

**A migrated project loses all seventeen anyway**, because the config error is raised while loading,
before `cmd_check` is entered. So the shipped listing's *No validator. Everything it checked is now
unchecked* is true as behaviour and **overstated as necessity**: roughly a third of the validator
never needed the folder, and the documents it reads — the binding, the method, the project's own
docs and deliverables — are exactly what a migrated project still keeps locally.

**This is the cheapest large thing available to a migrated project**, and it is why it is raised
ahead of the two beside it. It adds no command (non-goal 11 holds at four), makes no network call
(non-goal 5), and writes nothing (non-goal 6). It changes when the loader refuses, not what checking
means.

**It is a decision and not a fix, because the honest answer might be no.** A `check` that prints
`OK` in a project it cannot validate is a worse failure than one that refuses, and the *Scope* line
is the mechanism that would have to carry the difference.

**Scope**
- In: whether the four checks and one advisory that take no `tasks` argument should run when the
  task folder does not resolve
- In: what such a run must print so that nobody reads a document-only pass as a full one — the
  existing `Scope` line is the candidate and may not be enough
- In: whether the refusal message changes, given it currently tells a migrated project the commands
  do not apply
- Out: any check that reads a task file. Those refuse, and the reason is not in doubt
- Out: reading the remote backend. Non-goal 5 keeps every network call out of the core; that is
  [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s subject and it lives in a
  binding, not here
- Out: a fifth command or a flag that means "documents only" if the answer can be reached without
  one

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_check` and the five check functions whose signatures
  carry no `tasks`
- `tests/fixtures/migrated-away/` — the project shape this is about, and `broken-tasks-dir`, which
  is the shape that must keep refusing
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *What is gone and has no replacement here*,
  item 1, which this task would make partly false and which is then its to correct

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Does a document-only pass mislead more than a refusal helps?** The whole case rests on the
  `Scope` line being read. It is printed on both branches today and was built for exactly this class
  of misreading, but it has never had to carry a *pass* that covers a third of what the reader thinks
  it covers. **Answer at `specify`, by running the command against the fixture and reading the output
  as an adopter would** — not by arguing about it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question about what survives a migration to GitHub Issues. **The finding is a measurement, not an opinion**: `cmd_check` runs 17 checks and 5 take no `tasks` argument, while the config error aborts before any of them run. Checked against `docs/SCOPE.md` §4 before raising — it touches non-goals 5, 6 and 11 and violates none, which is why it is raised in this shape rather than as a GitHub-aware validator. `high` because it is the largest thing a migrated project could get back for the least weight. **Not covered by any standing authorisation.** |
