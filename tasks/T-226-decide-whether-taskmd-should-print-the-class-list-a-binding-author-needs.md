---
id: T-226
title: Decide whether taskmd should print the class list a binding author needs
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-222, T-197, T-191]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-226 — Decide whether taskmd should print the class list a binding author needs

## 1. Specify

**Outcome**
An answer, recorded, on whether taskmd gains a way to print the set of classes `check` can report —
and if so, what shape it takes.

**Why this one**
`BINDING.md` §4 requires a binding to name the classes its mapping makes impossible, in the
validator's own names. **Nothing an adopter installs tells them what those names are.** The set has
one home and it is source code — the literal at each `problems.append` site and the
`ADVISORY_PREFIXES` constant, both in `taskmd/cli.py`. On 2026-08-22
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) repaired the
clause to say so, which is honest and is not the same as reachable: it asks a binding author to read
Python to write Markdown.

**The alternative is not a document.** A list written into any document is the per-check coverage
table §4 refuses, with its second column removed — falsified by the same event, and one class was
added to this validator on 2026-08-22. So the only shapes that do not re-create the defect are ones
that **derive** the set: a command that prints it, or nothing.

**Scope**
- In: whether to add it, and if yes its shape — a subcommand, a flag on `check`, or something else
- In: what it costs. A fifth command is adopter-visible surface and this project has kept to four
- In: whether `tests/classes.py`'s derivation moves into the package or stays in `tests/`. It is the
  derivation that exists; a command would need one, and two would be the defect T-191 found
- Out: building it. This task answers whether and what shape; the build is its own task if the answer
  is yes
- Out: changing what the classes are

**Inputs**
- `tests/classes.py` — the derivation that exists today, and its recorded reasons
- `plugin/skills/taskmd/taskmd/cli.py` — the two places the names live
- `plugin/skills/taskmd/docs/BINDING.md` §4 *Where the class names come from* — the clause that
  currently sends a reader to the source

**Acceptance criteria**
- [ ] The answer is recorded with its reason, and the rejected shapes are named
- [ ] If the answer is yes, the shape is specific enough that a build task could start from it
- [ ] Whether the derivation gets one home or two is answered either way — a yes that leaves two
      derivations has re-created T-191

**Open questions**
- **Is a fifth command worth it, against reading two places in `cli.py`?** — the project owner. The
  recommendation is **yes, as `check --classes` rather than a fifth command**: it adds no verb to the
  surface, it sits on the command that owns the classes, and it makes the clause's instruction
  runnable. The cost is one flag and moving the derivation into the package.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

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
| 2026-08-22 | → proposed | Raised from [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md), whose §1 puts changing the validator out of scope. The repaired clause tells a binding author where the class names live and that place is source code, which is the honest answer and is not a usable one — so the gap is recorded as a decision rather than left as a shrug in a shipped document. `decision` by the schema's own test: the outcome is an answer somebody else could act on, and the change follows from it. |
