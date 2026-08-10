---
id: T-100
title: Report a project config that has drifted from the shipped default
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-001, T-023, T-088]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-100 — Report a project config that has drifted from the shipped default

## 1. Specify

**Outcome**
A project that copied the shipped schema and then fell behind it is told so, by a command it already
runs — so a schema improvement reaches the projects that pinned before it existed.

**Why this one**
Raised as **R-2** by the first adopting project (`control/LOCAL-CONTEXT.md`). It copied the shipped
default to `.taskmd/config.md` on 2026-08-09 — correctly, since a config *replaces* the default
rather than merging with it. taskmd added `audit` to the `type` vocabulary the same day
([T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md)). The project
could not see that, and raised a task to "fix" a template for naming a type the schema lacked — **a
defect that had stopped existing.** It was caught a day later only because somebody opened the
plugin's shipped default by hand and compared the two.

So the cost is not a stale value. It is a task specified against a false premise, whose planned fix
would have edited a valid field to satisfy a constraint that no longer existed.

**The replace-not-merge rule is right and this does not reopen it.**
`plugin/skills/taskmd/taskmd/defaults/config.md` argues it twice — every key must be written, because
a silently absent key would hand you a schema you did not write. Drift is the accepted price of that
rule. What is being asked for is a **report**, not a merge: a project that pinned deliberately reads
the line and ignores it; a project that pinned and forgot gets told.

**Both files are already parsed**, so the comparison costs a walk of two dictionaries and no new
input.

**Requirements served**
R-11 (`docs/SCOPE.md`) — the schema is configuration, which is what makes a shipped default something
a project can fall behind. R-17, since this is a fact about the config that surfaces once rather than
inside a task somebody is trying to finish.

**Scope**
- In: whether `check` gains a drift line, and what counts as drift — a missing key, an extra
  vocabulary value, a row the default has since changed.
- In: whether a project that pinned on purpose can say so, and where. A line nobody can silence is a
  line everybody learns to skip.
- In: what the line says. R-2's suggested shape names the row and the difference:
  `CONFIG DRIFT  type: shipped default adds 'audit'; this project's row does not carry it`.
- Out: merging a project config with the default, at read time or at any other time. That is the rule
  above, and it is not this task's to change.
- Out: a `config` command. `docs/SCOPE.md` non-goal 11 keeps the CLI to four, so if this is reported
  it is reported by `check` — the same constraint T-032 works under.
- Out: telling a project its config is *wrong*. Drift is not an error; the default is a default.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the shipped default, and its own argument for
  replace-not-merge.
- `plugin/skills/taskmd/taskmd/schema.py` — where both files are already read.
- [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md), the change
  that went unseen, and its note that two independent projects reached for `audit`.

**Acceptance criteria**
- [ ] Shown failing first, per R-16: a project config missing a value the shipped default carries
      produces the line, demonstrated on a fixture
- [ ] A project whose config matches the default produces nothing, and a project with no config of
      its own produces nothing
- [ ] The line names the key and the difference, not merely that a difference exists — a report that
      sends the reader to diff two files by hand is the thing that already happened
- [ ] Whether a drift line changes the exit status is decided and recorded with its alternative
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- **Is drift a problem or an advisory?** *Recommended: advisory — reported, exit unchanged.* A pinned
  config is legal, and making `check` exit non-zero on a legal state turns a validator a project
  trusts into one it starts passing flags to. *Alternative: a counted problem*, which guarantees it is
  seen — and guarantees a project that pinned deliberately can never have a clean run again. The
  maintainer decides; this bears on the acceptance criterion above.

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
| 2026-08-10 | → proposed | Raised as R-2 from the first adopting project's recommendations. `high` because the failure is not a stale value but a task specified against a false premise — the project raised work to fix a defect that had already been fixed upstream, and would have edited a valid field to satisfy a constraint that no longer existed; it was caught by accident. `s` because both files are already parsed and the comparison is a walk of two dictionaries. Recorded here so `specify` does not relitigate it: the replace-not-merge rule is deliberate and argued twice in the shipped default, drift is its accepted price, and what is asked for is a report rather than a merge. Non-goal 11 rules out the `config --diff` verb R-2 offered as an alternative, so `check` is the only surface. |
