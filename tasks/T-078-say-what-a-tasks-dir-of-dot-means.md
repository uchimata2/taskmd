---
id: T-078
title: Say what a tasks_dir of dot means
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-069, T-024, T-019]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-078 — Say what a tasks_dir of dot means

## 1. Specify

**Outcome**
A project that writes `tasks_dir: .` is either told it cannot, or gets a walk that means something —
rather than a `check` that silently declines to read most of the project.

**Why this one**
Found in [T-069](T-069-skip-a-nested-project-at-any-depth.md)'s `plan`, under METHOD §3.3, while
establishing whether the `base != root` guard was protecting anything. It was not — but the probe
that answered the question turned up this, which is a different defect and outside that task's scope
(`is_project` is explicitly out of it).

`tasks_dir: .` is legal today. It passes `_require`, it passes `_check_tasks_dir` — the root is
certainly a directory — and then `discovery.is_project(folder, ".")` is **true of every folder in
existence**, because it asks whether `<folder>/.` is a directory. So every subdirectory looks like a
nested project and is skipped. Shown, on a scratch project with `tasks_dir: .`, one task file at the
root and two notes below it:

```
before T-069 (the base != root guard still in place)
  BROKEN LINK   T-001-x.md   -> ./nope.md
  BROKEN LINK   sub/note.md  -> ./nope.md          sub/deeper/note.md never read

after T-069
  BROKEN LINK   T-001-x.md   -> ./nope.md          sub/note.md never read either
```

**T-069 did not cause this and does not make it worse in kind.** The guard bought exactly one level
on a walk that was already wrong below it — which is why T-069 recorded it as *failing later* rather
than as protection, and removed it anyway. Either way the project is not fully read and nothing says
so.

**Why it is worth a record rather than a shrug.** This is the class the project names as its worst
failure twice over ([T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md),
[T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md)): a validator reporting
success over something it never examined. `check` exits 0 having read a fraction of the tree, and a
project that believes it is validated is worse off than one with no validator.

**Requirements served**
R-17 (`docs/SCOPE.md`) — a configuration problem is reported when the config is read; R-16, since a
validator has to be believable.

**Scope**
- In: what `tasks_dir: .` should do — be rejected when the config is read, or be made to walk
  correctly.
- In: the same question for any value that resolves to the project root (`./`, `.\`, an empty
  segment), since a rejection that one spelling escapes is not a rejection.
- Out: `tasks_dir` naming a file, which is [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md).
- Out: `tasks_dir` naming a folder that does not exist, which is
  [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) and is done.
- Out: the nested-project exclusion itself, settled in [T-069](T-069-skip-a-nested-project-at-any-depth.md).

**Inputs**
`plugin/taskmd/schema.py` (`_check_tasks_dir`), `plugin/taskmd/discovery.py` (`is_project`),
`plugin/taskmd/cli.py` (`markdown_files`, `is_nested_project`),
[T-069](T-069-skip-a-nested-project-at-any-depth.md) §3.

**Acceptance criteria**
- [ ] A project with `tasks_dir: .` either fails at config-read time with a message naming the key,
      or has every file under its root read by `check`
- [ ] Shown failing first on a fixture, per R-16
- [ ] Whichever way it is resolved, the other spellings of "the root" get the same treatment,
      demonstrated on more than one
- [ ] A project with an ordinary `tasks_dir` is unaffected, and every existing fixture still reports
      exactly one class

**Open questions**
- **Reject, or support?** Rejecting is one condition in `_check_tasks_dir` and closes the class
  outright; it also forbids a shape nobody has asked for but which is not obviously wrong — a small
  project whose tasks simply live at its root. Supporting it means `is_project` can no longer answer
  "is this a project" by looking for the tasks folder, which is the mechanism
  [T-011](T-011-runtime-discovery-and-project-hook-commands.md) settled and which T-069 kept out of
  scope for good reason. `specify` needs the owner's view on whether tasks-at-the-root is a shape
  taskmd wants at all.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised from T-069's `plan` under METHOD §3.3 — found by the probe that answered whether the `base != root` guard protected anything, and outside that task's scope, which puts `is_project` explicitly out. `low`/`xs` because no project in the tree writes `tasks_dir: .` and the likely fix is one condition; not lower, because the failure shape is the one this project has twice named as its worst — `check` exiting 0 over a tree it never read. Recorded with both transcripts so a later reader can see the guard's removal did not cause it. |
