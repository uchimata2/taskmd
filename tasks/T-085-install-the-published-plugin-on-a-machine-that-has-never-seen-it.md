---
id: T-085
title: Install the published plugin on a machine that has never seen it
type: analysis
status: proposed
phase: specify
parent: T-006
blocked_by: []
related: [T-049, T-067, T-020]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-085 — Install the published plugin on a machine that has never seen it

## 1. Specify

**Outcome**
It is known, by running it, whether `claude plugin marketplace add uchimata2/taskmd` followed by
`claude plugin install taskmd@taskmd` works for someone whose machine has never held this project,
and whether the command the README then tells them to type resolves.

**Why this one**
[T-006](T-006-package-document-and-publish.md) criterion 4 says *installs from a clean clone on a
machine that has never seen it*, and that is the one criterion its review could not tick. Everything
around it was proven at publication: the route was exercised from the published remote, the harness
cloned it fresh, the install materialised 24 files, and both entry points ran on an unrelated
project. All of that happened on the machine the project was written on.

What that machine cannot answer is the part the criterion is actually about: another operating
system, another Python, another user profile, and a `PATH` that has never been touched by any of
this. Two known local facts make it worth asking rather than assuming. `taskmd` does not resolve by
name here at all, which [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)
diagnosed as this machine's truncated shell snapshot and not the plugin's defect, and the README's
first install section ends in the bare name. And the install cache here already held a stale layout
from an earlier install, which is a state a fresh machine cannot be in.

**Requirements served**
R-20 (`docs/SCOPE.md`) — runs on a clone with no configuration; `docs/SCOPE.md` §1 *No install*.

**Scope**
- In: the marketplace-plus-install route from the published repository, on a machine that has never
  held taskmd.
- In: whether bare `taskmd` resolves there, which is the half T-054 could not settle locally and
  [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) settled only for a clone on
  `PATH`.
- In: the plain skill shape by the same test, since a copied folder depends on a launcher finding an
  interpreter it did not choose.
- Out: macOS specifically. [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) owns
  the platform claim and the README says macOS is untested rather than unsupported.
- Out: changing anything. If the install fails, the finding is the outcome and the fix is its own
  task.

**Inputs**
- [T-006](T-006-package-document-and-publish.md) §3 steps 7 and 8 — what was proven, and where.
- [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) — the same test against a
  throwaway remote, including that a remote marketplace silently replaces a same-named local one.
- [`README.md`](../README.md) — the two install sections, which are what is being tested.

**Acceptance criteria**
- [ ] Both install sections of the README are followed **as written** on a machine that has never
      held this project, and each ends in the command it names, with the transcript recorded
- [ ] Whether bare `taskmd` resolves there is stated either way, because a negative is the finding
      that T-054 left open
- [ ] Anything the README has to change is named, with the wording, rather than fixed here

**Open questions**
- **What stands in for the machine.** A container, a fresh virtual machine, or a second physical
  machine each answer a slightly different question, and a container that ships no Python answers a
  more interesting one than a developer machine that has three. The maintainer's, since it depends
  on what they have.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- This record

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised by [T-006](T-006-package-document-and-publish.md)'s review as the child carrying its criterion 4. The route was proven end to end from the published remote on the day of publication, and the part that could not be proven is the phrase *a machine that has never seen it*: another OS, another Python, another profile, and a `PATH` this project has never touched. Carried as a task rather than ticked, because the local `PATH` failure T-054 recorded means the README's first install section ends in a command nobody has yet watched resolve by name on a stranger's machine. |
