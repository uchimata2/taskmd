---
id: T-023
title: Stop config errors printing an absolute install path
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-006, T-019, T-020]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-05
updated: 2026-08-07
deliverables: []
---

# T-023 — Stop config errors printing an absolute install path

## 1. Specify

**Outcome**
A `SchemaError` raised against the **shipped default** config names that config in a form that is
the same on every machine, instead of the absolute path to wherever taskmd happens to be installed.

**Why this one**
Found while verifying [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md). Every
`SchemaError` is prefixed with the config's `source`, and when the project has no `.taskmd/config.md`
that source is `DEFAULT_CONFIG` — built from `os.path.abspath(__file__)`, so it is an absolute path
into the installation:

```
CONFIG ERROR  <absolute install path>/taskmd/defaults/config.md: tasks_dir is 'tasks', but the
project root has no such folder. ...
```

The behaviour is **older than T-019** and applies to every one of the config errors, not just the
new one — this task is not a defect in that fix. What T-019 changed is the exposure: a project that
has adopted taskmd and not yet made its tasks folder is now an error, so this string is plausibly
the **first output a new user ever sees**, and it names a directory that means nothing to them.

Two requirements are in tension with it. R-20 asks for byte-identical output across Windows, macOS
and Linux — this string cannot be, since it differs per machine, never mind per platform, which
makes it a concrete obstacle to [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md)
rather than a cosmetic one. R-23 forbids absolute local paths; that rule governs the repository and
this is runtime output, so it is not a publishing leak — but a tool whose first line of output is
someone's home directory is a poor advertisement for it, and pasting that line into an issue leaks
it for them.

**Requirements served**
R-20, and R-23 in spirit (`docs/SCOPE.md`).

**Scope**
- In: how the shipped default config is named in error messages.
- Out: the project-config case, which already prints a root-relative path and is correct.
- Out: the wording of any individual error — this is the prefix, not the messages.

**Inputs**
`taskmd/schema.py` (`DEFAULT_CONFIG`, `load_schema`, `SchemaError`), `docs/SCOPE.md` R-20 and R-23.

**Acceptance criteria**
- [ ] A config error against the shipped default prints the same bytes regardless of where taskmd
      is installed
- [ ] It is still unambiguous which file is meant — a reader can find it
- [ ] The project-config case is unchanged
- [ ] Shown failing on a fixture, per R-16

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: `<shipped default>`.** The error says which
  config is in force, and a repo-relative path is relative to *taskmd's* repository rather than the
  adopter's — so it would still be wrong for the person reading it, while the absolute form is the
  R-23 leak this task exists to remove. *Rejected: printing `taskmd/defaults/config.md`.* It is the
  file's real name and findable, which is exactly what the bracketed label costs: a reader learns a
  default is in force without learning where to read it.

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
| 2026-08-07 | → specified | Answered: `<shipped default>`. The rejected option's cost is recorded rather than glossed — a bracketed label tells a reader a default is in force but not where to read it, and if that turns out to bite, the fix is to name the file next to the label rather than to reverse this. |
| 2026-08-05 | → proposed | Raised from T-019's implement phase. Pre-existing behaviour, surfaced because T-019 made the fresh-project case an error and so put this string in front of new users. Not fixed where it was found (METHOD §3.3, rule 4). |
