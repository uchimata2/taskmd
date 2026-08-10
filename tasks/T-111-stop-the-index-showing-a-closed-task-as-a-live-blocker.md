---
id: T-111
title: Stop the index showing a closed task as a live blocker
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-102]
work_package: v0.2
owner: maintainer
business_value: high
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-111 — Stop the index showing a closed task as a live blocker

## 1. Specify

**Outcome**
The generated index resolves a dependency edge against the far end's status, the way `context` and
the sort already do. An open task whose every blocker has closed reads as startable in the artifact
people actually open to choose work.

**Why this one**
**This is [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) one command
over, and T-102's own reasoning applies unchanged:** the fact is computed on every call and then
discarded from the view. There, `list` sorted blocked rows last and never said which they were.
Here, `index` prints the raw edge and never says the blocker is gone.

**The evidence.** taskmd 0.1.1, against an adopting project's tree. `index` writes this row for a
task whose only blocker closed the day before:

```
| T-019 | Build the capability preflight every deck ships with | `v0.3` | `proposed` | `specify` |
- | - | T-002 | - |
```

`Blocked By: T-002`. `context` on the same task, in the same tree, in the same minute:

```
BLOCKED BY
  T-002        done        Build mode — the self-contained deck generator

STATE  open, no blocker outstanding
```

And `list --open` ranks it **third of fifteen**, ahead of everything genuinely held.

**Two of the three surfaces already implement the rule.** `context` sets its `<-- still open` flag
only when `other.is_open`, and prints `STATE open, no blocker outstanding` when nothing is
outstanding; `is_blocked` resolves each dependency target against `tasks[target].is_open` for the
sort's first key. `index_block`'s `row` renders `", ".join(task.links(n))` for every link name
alike, so a satisfied dependency and a live one are the same string. **So this is an internal
inconsistency, not an imported preference** — the only surface that disagrees is the one a person
reads.

**What it cost the adopting project.** Three of fifteen open rows named a closed blocker on the day
this was written, and the board was read as having three fewer startable tasks than it had. The
`Blocks` side has the same shape: a closed downstream task still appears, overstating what finishing
a task releases.

**Scope**
- In: dependency-kind edges in `index_block`'s `row`, both directions — `blocked_by` and `blocks`.
- In: **the column-in-use test.** `names` comes from `any(t.links(n) for t in tasks.values())`,
  evaluated before any filtering, so filtering only the cells would leave a project whose dependency
  edges are all satisfied reading a column of dashes — which is the defect `index_block`'s own
  docstring records as already fixed for `work_package`: *a column appears only when some task uses
  it*. Both halves move together or the fix reintroduces the older defect one edge kind over.
- Out: `parent`, `children` and every soft edge. A closed parent is still a parent; a closed blocker
  is not still a blocker.
- Out: the front-matter, which keeps the edge either way, and `context`, which is already correct.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `index_block`, `is_blocked`, and the `context` flag that
  already tests `other.is_open`.
- [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) — the same defect on
  `list`, and the precedent for what to do about it.

**Acceptance criteria**
- [ ] A row whose every dependency has closed shows `-` in that column, and `index` and `context`
      agree on whether the task is held.
- [ ] A row with one closed and one open blocker shows only the open one.
- [ ] A project whose dependency edges are all satisfied loses the column rather than printing a
      column of dashes.
- [ ] `parent`, `children` and soft edges are unchanged, closed members included.

**Open questions**
- Which release phase this belongs in. Set to `v0.2` to mirror T-102, the nearest analogue; the
  maintainer's call, and T-110 may move it anyway.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Filter dependency-kind edges to open tasks in `index_block`'s `row` | `cli.py` |
| 2 | Apply the same view to `names`, so an emptied column disappears | `cli.py` |
| 3 | Cover the four criteria, including the all-satisfied project | `tests/test_cli.py` |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <none yet>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | **Written by an adopting project** — htmldeck, `github.com/uchimata2/htmldeck` — and placed here rather than sent as prose, at the maintainer's request. Ids in the evidence above are that project's, not this one's. It reached the same conclusion independently and had already made this exact change to its own pre-taskmd index generator, recording the reason as *the cell is for what gates the task, and nothing else does*; reading `cli.py` then found T-102, which is the better argument and is this project's own. Estimated `high`/`xs` to match T-102 — the maintainer should re-scope, re-estimate or reject freely. |
