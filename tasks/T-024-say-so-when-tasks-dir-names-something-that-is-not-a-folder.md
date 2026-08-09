---
id: T-024
title: Say so when tasks_dir names something that is not a folder
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-019, T-023]
work_package: v0.2
owner: maintainer
business_value: low
effort: xs
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-024 — Say so when tasks_dir names something that is not a folder

## 1. Specify

**Outcome**
When `tasks_dir` names a path that exists but is not a directory, the error says that, instead of
telling the reader there is no such folder while the name sits in front of them.

**Why this one**
Found in [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md)'s review, by testing a
neighbour that task's plan had not: `tasks_dir: tasks` where `tasks` is a **file**.

```
check   exit 2 | CONFIG ERROR  ./.taskmd/config.md: tasks_dir is 'tasks', but the project root
                 has no such folder. Create it, or correct tasks_dir.
```

The rejection is right — `os.path.isdir` is the correct test and this is not a usable tasks folder.
Only the sentence is wrong, and it is wrong in the direction that costs the most: it denies the
existence of something the reader can see, and then advises creating it, which will fail. The
remedy the message gives cannot be followed.

This is **low value** and is recorded as such. The case is rare, nothing depends on it, and it is
one sentence of code. It is a task rather than a note because METHOD §3.3 leaves no third option
for something actionable and out of scope, and a note in a closed task is how observations get lost.

**Requirements served**
R-17 (`docs/SCOPE.md`) — the same requirement T-019 serves, at the granularity of what the message
actually tells the user.

**Scope**
- In: the wording of `_check_tasks_dir` when the path exists but is not a directory.
- Out: the test itself. `isdir` is correct and stays; this is not a proposal to accept a file.
- Out: the absolute-install-path prefix, which is [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md).

**Inputs**
`taskmd/schema.py` (`_check_tasks_dir`), T-019 §4.

**Acceptance criteria**
- [ ] A `tasks_dir` naming a file is reported as "not a folder", not as "no such folder"
- [ ] The advice given matches the case — it does not tell the reader to create a name that is
      already taken
- [ ] The absent-folder case is unchanged, and T-019's tests still pass untouched
- [ ] Shown failing on a fixture, per R-16

**Open questions**
- none.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Raised by T-019's review, from a neighbour case that task's plan had not tested. Not fixed where it was found. Recorded as low value on purpose — the backlog is more useful when the cheap items say so. |
