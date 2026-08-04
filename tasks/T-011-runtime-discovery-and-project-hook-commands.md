---
id: T-011
title: Runtime auto-discovery and project hook commands
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-002]
related: []
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-011 — Runtime auto-discovery and project hook commands

## 1. Specify

**Outcome**
taskmd runs on a clone without anyone naming an interpreter or editing a path, and a project can
plug in its own commands — written in bash, PowerShell, Python or anything else — that taskmd
invokes at defined points.

**Requirements served**
R-18, R-19 (`docs/SCOPE.md`). Bounded by assumption **A1**: the logic exists once, in Python.

**Why this one**
This is what "use bash, PowerShell and Python — auto-discovery / configurable" resolves to once
R-1 is applied. Three implementations of one command set would be three copies of one fact; one
implementation plus discovered launchers plus configurable project hooks gives the same reach with
one home. The hooks also cover the case the reference project needed — an external consistency
check run after every write.

**Scope**
- In: locating the interpreter (`py` / `python3` / `python`) and the repository root; thin
  launchers for bash and PowerShell; a config-declared hook mechanism with defined invocation
  points; failure reporting.
- Out: any second implementation of the commands. Any hook that taskmd itself ships — hooks are
  the project's, not the plugin's.

**Inputs**
- `docs/SCOPE.md` §3C and §6 (A1)
- `CLAUDE.md` — dependency-free, cross-platform, explicit newline, cp1252-safe console
- Handoff `local-markdown-dir.md` `tracker_lint` — the same idea, proven in use: a project-supplied
  command run after a write, with errors resolved before finishing

**Acceptance criteria**
- [ ] A clone runs with no configuration on Windows, macOS and Linux — demonstrated on at least
      two, with the actual command output
- [ ] The launchers contain no logic: proven by deleting one and showing behaviour is unchanged
- [ ] A hook is declared, invoked, and its **failure surfaces** — proven with a hook that exits
      non-zero
- [ ] A hook written in a language other than Python is proven to run
- [ ] A missing or unrunnable hook is reported when the config is read, not mid-command (R-17)
- [ ] The repository root resolves from the repository, not the working directory — proven by
      running from a subdirectory and from outside the repository

**Open questions**
- Which invocation points earn a hook? `tracker_lint` proved "after a write"; anything more is
  speculative until asked for.

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
| 2026-08-04 | → proposed | Raised by T-007 to carry R-18/R-19 under assumption A1. |
