---
id: T-055
title: Settle what the tool calls itself when it prints its own usage
type: fix
status: proposed
phase: specify
parent: T-054
blocked_by: []
related: [T-054, T-029]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-08
updated: 2026-08-08
deliverables: []
---

# T-055 — Settle what the tool calls itself when it prints its own usage

## 1. Specify

**Outcome**
Someone who mistypes a command is told how to retype it in a form they can actually run.

**Why this one**
Raised from [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3, which fixed
every place the *documentation* names a command and deliberately left this one, because it is not a
substitution.

`plugin/taskmd/cli.py` prints `usage: python -m taskmd {check,context,index}` on a bad argument,
and names the same form in its module docstring. That is the form T-054 established **nobody can
type**: an adopter has the package in an install cache and no `PYTHONPATH`, and a contributor in a
clone needs `PYTHONPATH` set. So the tool's own error message is the last place still naming it.

**Why it is not simply a substitution.** T-054 **D2** decided the two audiences type different
things on purpose — an adopter types `taskmd`, which the harness puts on `PATH`; a contributor types
`./plugin/taskmd.sh`, which works in a clone with nothing installed. A usage line is printed by one
process to whoever happened to run it, and **it cannot know which of the two it is talking to**.
Every answer therefore gives up something, which is why this needs deciding rather than editing.

**Requirements served**
**R-18** (`docs/SCOPE.md`) — the same one T-054 serves, at the one surface T-054 left: a message
telling you to run something unrunnable is the "clone runs unedited" promise failing at the moment
the user is already stuck. Also `docs/SCOPE.md` §1 *Invisibility*.

**Scope**
- In: what `usage:` names, and the same question for the module docstring in `plugin/taskmd/cli.py`
  and `plugin/taskmd/__main__.py`.
- In: whether the answer is one fixed string, or derived from how the process was actually invoked.
- Out: adding, renaming or removing a command — the surface is settled.
- Out: `python -m taskmd.schema` in `plugin/taskmd/schema.py`, which is
  [T-030](T-030-settle-the-schema-module-s-own-entry-point.md)'s question, not this one.

**Inputs**
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §2 **D2** — why the two
  audiences differ, and why that was chosen rather than unified.
- `plugin/taskmd/cli.py` — the usage string and the module docstring.
- [T-029](T-029-reject-unknown-arguments-on-every-command.md) — which made the usage line something
  users actually reach, by rejecting unknown arguments instead of ignoring them.

**Acceptance criteria**
- [ ] A bad argument, run through the shipped `bin/` entry point from a directory that is not this
      repository, prints a command line that can be copied and run as printed — demonstrated
- [ ] The same is true when the invocation was `./plugin/taskmd.sh`, or the record says explicitly
      which audience was chosen over the other and why
- [ ] The suite still passes and `check` is still clean on this repository

**Open questions**
- **One string, or derived from the invocation?** `sys.argv[0]` distinguishes the cases at no cost —
  a `bin/` invocation and a `-m` invocation do not look alike — so "it cannot know" may be false.
  Against: derivation is logic in a place that currently has none, and it has to be right on both
  platforms. Settle it at `specify`, since it decides whether there is anything to implement.

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
| 2026-08-08 | → proposed | Raised from T-054 §3 under METHOD §3.3, as the one naming site that is a decision rather than a substitution. T-054 changed every document that names a command to `taskmd`, the form the harness puts on `PATH`; the tool's own `usage:` line still says `python -m taskmd`, which T-054 established nobody can type. It was left because **D2** deliberately gives the two audiences different commands, and a usage line cannot tell which one it is printing to — so the choice costs something either way. `medium`/`xs` because it is one string in one file, reached only on a mistyped command, but reached exactly when the user is already stuck. The open question is whether `sys.argv[0]` makes "it cannot know" false, which decides whether this is a one-line edit or nothing at all. |
