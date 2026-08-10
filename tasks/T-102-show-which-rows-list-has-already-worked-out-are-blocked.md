---
id: T-102
title: Show which rows list has already worked out are blocked
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-022, T-031, T-070, T-087]
work_package: v0.2
owner: maintainer
business_value: high
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-102 — Show which rows list has already worked out are blocked

## 1. Specify

**Outcome**
`list` says which of its rows cannot be started, so the command that answers *what do I work on next*
answers it without a second command.

**Why this one**
Raised as **R-4** by the first adopting project (`control/LOCAL-CONTEXT.md`). `list --open` sorts
blocked tasks last, deliberately and correctly — it is the first of the four sort keys in the shipped
schema's *Ordering* section. Nothing in the output says which rows those are, so a reader sees eight
startable tasks and one of them is not. Sorting is not a signal a reader can act on: it tells you
there is a boundary and not where it falls.

**The fact is computed on every call and then discarded from the view.** `is_blocked` is evaluated in
`order` for the sort key and again in the `--json` payload, which carries a `blocked` field. The
human-readable and tab-separated rows carry `id`, the configured columns and the title, and nothing
else. So the contract surface already answers the question and the surface a person reads does not —
which is the one place this project's design rule cannot be the reason, since deriving it twice is
already what happens.

**What it cost there.** The project checked rather than assumed, then had to write the fact into a
handoff so the next session would not pick up a blocked task — a fact the tool derives on every call.

**Requirements served**
R-1 (`docs/SCOPE.md`) — derived facts are computed, and this one is computed and dropped. R-2, in
spirit: the dependency is visible from both ends when a task is opened, and invisible in the view
that decides which task to open.

**Scope**
- In: the human-readable output of `list`, and what marks a blocked row.
- In: whether the tab-separated form gains it too. Its comment states its contract — *"a line format
  a caller can read as printed and a script can cut"* — so a cell added anywhere but the end moves
  every column after it, and the title is currently last.
- Out: hiding blocked rows. The shipped schema rejects that explicitly: it would make `list` and
  `list --limit 1` describe different sets and conceal the graph from someone asking why nothing is
  moving.
- Out: changing the ordering rule, which is right.
- Out: `--json`, which already carries `blocked`.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `is_blocked`, `order`, `cmd_list`.
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Ordering*, sort key 1, and §*Views* for the rule
  that a contract surface emits every column whether used or not.
- [T-031](T-031-give-the-list-rationale-one-home.md), so whatever is added is documented where the
  ordering rule already lives rather than in a second place.

**Acceptance criteria**
- [ ] A project with an open dependency shows the marker on the blocked row and not on the others,
      demonstrated by running it
- [ ] A project with no blocked task produces output identical to today's, byte for byte
- [ ] Whether the tab-separated form changes is decided, and if it does, what a script that cuts
      columns sees is stated
- [ ] The rule is described in one place, not restated in the code
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- **A trailing marker or a column?** *Recommended: a trailing marker on the row.* It costs one
  character, it cannot shift a column a script already reads, and R-4 asks for exactly that.
  *Alternative: a real column*, which is self-describing and lines up under a header — and moves the
  title, which is the one cell whose position every reader and every `cut` already depends on.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Raised as R-4 from the first adopting project's recommendations. `high` because `list --open` is the command the skill opens with and the one an agent runs first, and a reader acting on it can start a task that cannot move; `xs` because the value is already computed twice per call — once for the sort key, once for the `--json` payload, which carries `blocked` — and the only missing step is printing it. Confirmed against `cli.py` rather than taken from the report: the tab-separated rows are id, configured columns, title, and nothing else. The tab form's own comment pins the constraint any answer works under — a script cuts those columns, and the title is last. |
