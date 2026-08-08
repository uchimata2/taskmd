---
id: T-054
title: Give an adopter a way to run the commands the skill names
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-053, T-006, T-003]
work_package: none
owner: maintainer
business_value: critical
effort: s
created: 2026-08-08
updated: 2026-08-08
deliverables: []
---

# T-054 — Give an adopter a way to run the commands the skill names

## 1. Specify

**Outcome**
Someone who installs this plugin and asks their agent what to work on next gets an answer, because
the command the skill tells it to run is one their machine can actually execute.

**Why this one**
Found during [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)'s restructure,
and **it is not caused by it** — the same hole was there before, hidden by this repository being the
only place the plugin had ever run.

`plugin/skills/taskmd/SKILL.md` opens with `python -m taskmd list --open --limit 1`, and
[`../plugin/skills/taskmd/adopt.md`](../plugin/skills/taskmd/adopt.md) ends with
`python -m taskmd check`. For an adopter, neither can work: the package sits in the plugin's
install cache, their working directory is their own project, and nothing puts the two together.
`python -m taskmd` raises `No module named taskmd`. The launchers solve it only for someone standing
in the plugin directory, which an adopter never is. So **every command the skill names fails for the
only audience the skill exists for**, and it has never been noticed because in this repository the
package happens to be in the tree.

That makes it critical rather than merely important: it is not a rough edge in the adoption path, it
is the adoption path not working at all, and [T-006](T-006-package-document-and-publish.md) would
publish it as-is.

**The mechanism to fix it is already established.** Read out of the shipped binary during T-053: the
harness collects `<plugin-root>/bin` for every enabled non-builtin plugin and puts those directories
on `PATH` (dropping any containing shell metacharacters). So a `bin/` entry point in the plugin
subtree becomes a command an adopter can type from anywhere, with no install step, no `PYTHONPATH`,
and no path editing — which is what `CLAUDE.md` *Publishing constraints* means by out-of-the-box.

**Requirements served**
**R-18** (`docs/SCOPE.md`) most directly — *"the repository root are auto-discovered so a clone runs
unedited"*. That requirement is currently **unmet for anyone who is not standing in this repository**,
which is the whole of this task. Also `docs/SCOPE.md` §1 *Invisibility* — a tool the agent cannot
invoke is not invisible, it is absent — and R-19 with the dependency-free constraint in `CLAUDE.md`,
which bind the shape of the answer.

**Scope**
- In: how an adopter invokes the four commands, and what the skill and `adopt.md` tell them to type.
- In: whether the `bin/` mechanism is the answer, or whether the skill should name something else.
- In: what this repository itself types, so the instruction has one form rather than two.
- Out: what the plugin contains — [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md).
- Out: install instructions and published shapes — [T-006](T-006-package-document-and-publish.md).
- Out: adding a command. The four exist; this is about reaching them.

**Inputs**
`plugin/skills/taskmd/SKILL.md`, `plugin/skills/taskmd/adopt.md`, `plugin/taskmd.sh` and
`plugin/taskmd.ps1` for how the path is set today, and
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) §2 D1 for what was read out
of the harness.

**Acceptance criteria**
- [ ] The command the skill names runs from a directory that is **not** this repository and not the
      plugin folder — demonstrated by running it in a scratch project and showing the output
- [ ] The failure is demonstrated first, on the current arrangement, so the fix is shown to fix
      something rather than to coincide with something working
- [ ] `SKILL.md` and `adopt.md` name one form of the command, not one each
- [ ] The suite still passes and `check` is still clean on this repository

**Open questions**
- **Does this repository use the same entry point it ships?** Using it proves it on every turn, which
  is this project's usual argument. Against: `bin/` is only on `PATH` when the plugin is *installed
  and enabled*, so a contributor who has merely cloned would find the documented command missing —
  the same class of defect as T-052's global-ignore finding, where the thing worked only where it had
  been tested. `specify` cannot settle this alone; it needs the `bin/` shape to be known.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <not yet decided>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | → proposed | Raised from T-053's restructure and **not caused by it**: the same hole predates the move and was hidden by this repository being the only place the plugin had ever run. Every command `SKILL.md` and `adopt.md` name — `python -m taskmd …` — fails for an adopter, because the package is in the install cache and their working directory is their own project. `critical` because it is not a rough edge in the adoption path but the adoption path not working at all, and T-006 would publish it as-is; `s` because the mechanism is already known. Read out of the shipped binary during T-053: the harness puts `<plugin-root>/bin` on `PATH` for every enabled plugin, so a `bin/` entry point is a command an adopter can type from anywhere with no install step and no `PYTHONPATH`. The open question is whether this repository should then type that same command, which proves it continuously but is only on `PATH` when the plugin is installed — the T-052 shape, where a thing works only where it was tested. |
