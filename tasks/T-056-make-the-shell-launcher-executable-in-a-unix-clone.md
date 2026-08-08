---
id: T-056
title: Make the shell launcher executable in a Unix clone
type: fix
status: proposed
phase: specify
parent: T-054
blocked_by: []
related: [T-054, T-011]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-08
updated: 2026-08-08
deliverables: []
---

# T-056 — Make the shell launcher executable in a Unix clone

## 1. Specify

**Outcome**
Someone who clones this repository on Linux or macOS can run the command `CLAUDE.md` tells them to
run, without first being told to repair the checkout.

**Why this one**
Found during [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) `implement`,
while deciding how `plugin/bin/taskmd` should invoke its target, and raised at that task's `review`
under METHOD §3.3 rather than fixed there.

`plugin/taskmd.sh` is recorded in the index as **`100644`**. Git stores the executable bit and
applies it on checkout, so on any Unix checkout the file arrives non-executable and
`./plugin/taskmd.sh check` — the form `CLAUDE.md`, `tasks/README.md` and the task template all
name — fails on permission before it reaches a shell. `plugin/bin/taskmd`, added by T-054, is
`100755` and is unaffected; so are the two Windows files, where the mode bit means nothing.

**It has never been visible here.** This project is developed on Windows, whose filesystem does not
enforce the bit, and Git Bash runs the script regardless — so every recorded run of the documented
command has succeeded on the one platform where the defect cannot appear. That is the same shape as
[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md)'s finding and T-054's PowerShell
5.1 defect: a thing that works only where it was tested.

**Requirements served**
**R-18** (`docs/SCOPE.md`) — *"the repository root are auto-discovered so a clone runs unedited"* —
and `CLAUDE.md` *Publishing constraints*, which requires that someone who clones this can run it
with no path editing. A clone that needs `chmod` before its documented command works has not met
either, and this repository is going to be published.

**Scope**
- In: the mode recorded for `plugin/taskmd.sh`, and whether anything else in the tree that is meant
  to be executed carries the wrong one.
- In: whether this is checkable, so it cannot silently regress on a Windows-developed repository —
  the mode is readable from the index without a Unix machine.
- Out: what the launchers do. T-054 settled the entry points and this changes none of them.
- Out: the harness `PATH` mechanism and anything about installs —
  [T-006](T-006-package-document-and-publish.md).

**Inputs**
- `git ls-files -s plugin/` — the recorded modes, which is the whole of the evidence.
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 3, for why
  `bin/taskmd` invokes its target through `sh` and therefore does not depend on this.
- `CLAUDE.md` and `tasks/README.md` — the places that name `./plugin/taskmd.sh`.

**Acceptance criteria**
- [ ] `plugin/taskmd.sh` is recorded `100755`, shown by reading the index rather than the filesystem
- [ ] The defect is demonstrated before the fix, in a form that does not need a second machine — a
      checkout of the current mode into a fresh worktree, with the failure the command actually gives
- [ ] Nothing else in the tree that is meant to be executed is left with the wrong mode — answered
      by enumerating what is executed, not by inspecting what looks like a script
- [ ] The suite still passes and `check` is still clean on this repository

**Open questions**
- **Is a mechanical guard worth it, or is the fix enough?** A test asserting the recorded mode would
  catch a regression on the Windows machine where the bit is invisible, which is exactly where it
  would recur. Against: it is a test about git metadata rather than about taskmd, and the file is
  changed roughly never. Decide at `specify`; it changes what `plan` has to produce.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | → proposed | Raised at T-054's `review` under METHOD §3.3, having been found during that task's `implement`; not fixed there, because review does not repair what it finds. `plugin/taskmd.sh` is recorded `100644`, so a Unix clone gets it non-executable and `./plugin/taskmd.sh` — the form `CLAUDE.md`, the index preamble and the task template all name — fails on permission. Invisible here because Windows does not enforce the bit and Git Bash runs the file anyway, so every recorded run of the documented command has been on the one platform where the defect cannot appear. `high`/`xs`: one mode bit, but it is R-18 failing for every non-Windows contributor of a repository that is about to be published. T-054's `bin/taskmd` is `100755` and invokes its target through `sh`, so nothing shipped to an adopter depends on this. The open question is whether to add a guard asserting the recorded mode, since a regression would recur exactly where it cannot be seen. |
