---
id: T-049
title: Demonstrate a clone running on a second platform
type: fix
status: proposed
phase: specify
parent: T-011
blocked_by: []
related: [T-006]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-049 — Demonstrate a clone running on a second platform

## 1. Specify

**Outcome**
The claim that a clone runs unedited on Windows, macOS and Linux is carried by output from **two**
of them rather than one. Today it is carried by Windows alone.

**Why this one**
Raised by [T-011](T-011-runtime-discovery-and-project-hook-commands.md)'s review. Its first
acceptance criterion asks for at least two platforms, and the environment T-011 was built in had no
Linux distribution installed and no container runtime — so the second platform could not be run.
Recording it as a child rather than counting the criterion met is METHOD §2's rule for `review`: a
criterion is met, or it carries a task that will meet it.

**This is not a code task.** Nothing is known to be wrong. Auto-discovery and the launchers were
written to be portable and the portability constraints in `CLAUDE.md` were followed, but written-to-be
and shown-to-be are exactly the distinction that section draws. If it turns out something *is* wrong
— a `#!` line, a path separator, a shell builtin — that is a finding this task raises, not one it
fixes.

**Requirements served**
R-18, R-20 (`docs/SCOPE.md`), and §9's first bullet.

**Scope**
- In: running the CLI and both launchers on a second platform from a fresh clone, with no
  configuration and no path editing, and recording the output.
- Out: any second implementation of the commands (assumption A1), and any change to the tool unless
  the run turns one up.

**Inputs**
`T-011` §3 *Verification* — the Windows half, and the commands to repeat; `CLAUDE.md` *Publishing
constraints*; `docs/SCOPE.md` R-20.

**Acceptance criteria**
- [ ] A fresh clone runs `check`, `index`, `list` and `context` on a second platform with no
      configuration, no dependency install and no path editing — with the actual output
- [ ] Both launchers are exercised there, or the absent one is stated as absent with the reason
- [ ] The generated index is **byte-identical** to the one this repository already carries, which is
      what R-20 actually claims and what a platform difference would break first
- [ ] A hook written in that platform's own shell is run, since criterion 4 of T-011 was proven with
      PowerShell and the mechanism's language-freedom is the point

**Open questions**
- **When, and on what.** The maintainer's answer on 2026-08-07 was "hand it to T-006, or after the
  first version is published" — so the route (a CI runner at packaging time, or a real machine after
  publication) is chosen with T-006 rather than here. That is why this task is `related` to T-006
  and not blocked by it: it could be done sooner if a second platform becomes available.

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
| 2026-08-07 | → proposed | Raised by T-011's review, which met five of six criteria and could not run the sixth's second half: no Linux distribution and no container runtime in the environment, so the platform claim rests on Windows alone. Recorded as a child rather than as a caveat, because METHOD §2 lets a criterion be unmet only if a task carries it. Soft-linked to T-006 rather than blocked by it, on the maintainer's routing — it should travel with packaging, but nothing stops it being done the moment a second platform exists. |
