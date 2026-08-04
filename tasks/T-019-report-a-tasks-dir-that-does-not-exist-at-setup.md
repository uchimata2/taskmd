---
id: T-019
title: Report a tasks_dir that does not exist at setup
type: fix
status: proposed
phase: specify
parent: T-002
blocked_by: []
related: []
work_package: none
owner: maintainer
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-019 — Report a tasks_dir that does not exist at setup

## 1. Specify

**Outcome**
A config whose `tasks_dir` names a folder that is not there fails when the config is read, naming
the key and the path — instead of yielding a project with no tasks in it.

**Why this one**
Found in T-002's review, by testing the half of class 8 that `implement` had not demonstrated. A
config key can be misspelled, and so can a key's **value**; only the first is caught. With
`tasks_dir: taks` against a real `tasks/` folder holding one task:

```
check            exit 0 | OK - 0 task(s), vocabulary valid, references resolve, no broken links
context T-001    exit 1 | No such task: T-001
index            exit 0 | Wrote taks/README.md - 0 active, 0 closed
```

Three separate failures, and the first is the worst: **`check` returns success on a project it
never read.** A validator that says OK because it found nothing to look at is worse than no
validator, because it is trusted. `context` then reports the problem exactly where R-17 says it must
not — inside a task the user is trying to start, phrased as though the task were missing. And
`index` silently creates the misspelled folder, so the mistake acquires a plausible-looking
artefact.

**Requirements served**
R-17 (`docs/SCOPE.md`).

**Scope**
- In: `tasks_dir` resolving to nothing, and any other config value that names a filesystem path.
- Out: a genuinely empty tasks folder, which is legitimate for a new project and must stay legal —
  the distinction is *the folder is absent*, not *the folder has no tasks in it*.

**Inputs**
`taskmd/schema.py` (`load_schema`, `load_tasks`), `docs/SCOPE.md` R-17, T-002 §4.

**Acceptance criteria**
- [ ] A `tasks_dir` that does not exist is an error naming the key and the path, raised when the
      config is read — not on first use, and not by any of the three commands individually
- [ ] `check` cannot exit 0 on a project whose task folder was never found
- [ ] `index` does not create the folder named by a mistyped value
- [ ] An existing but **empty** tasks folder is still legal and still exits 0
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
| 2026-08-05 | → proposed | Raised by T-002's review against criterion 6 and class 8. `implement` proved the unknown-key half of that class and not the missing-file half; the review tested the untested half and it failed. |
