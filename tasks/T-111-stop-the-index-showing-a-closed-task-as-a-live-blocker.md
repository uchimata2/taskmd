---
id: T-111
title: Stop the index showing a closed task as a live blocker
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-102]
work_package: M2
owner: maintainer
business_value: high
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
adopter_visible: yes
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
| T-019 | Build the capability preflight every deck ships with | `M3` | `proposed` | `specify` |
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
- ~~Which release phase this belongs in.~~ **Settled: `M2`.** Checked against
  [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md)'s rule — all
  dependencies plus every minor-to-moderate correction — rather than inherited from T-102, which is
  what the writer proposed. An `xs` correction to one view, holding nothing up: M2 by the rule, and
  the same answer the analogue gave for a different reason. The rejected alternative was M3, which
  takes the bigger work and the new capabilities; this is neither.

**Authorisation**
The maintainer authorised, on 2026-08-10, working **every open `M2` task through its full
lifecycle** — specify, plan, implement, review, fix, commit and push — one task at a time, stopping
to hand off before the remaining work outgrows the session. That covers this task end to end and
nothing outside the `M2` set (METHOD §3.1).

**Verified here before starting.** This task was written by an adopting project against its own tree,
so its premises were treated as leads. Both reproduce in *this* repository:
`tasks/README.md` gave T-005 `Blocked By: T-009` and T-047 `Blocked By: T-003` while `context` on
each printed `STATE  open, no blocker outstanding` — the two surfaces disagreeing, in the same tree,
exactly as reported.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | A helper naming **both** ends of a dependency edge, since `schema.edges` is keyed by the stored field and a membership test against it answers "not a dependency" for every derived name | `dependency_names` in `cli.py` |
| 2 | Filter dependency-kind edges to open tasks in `index_block`'s `row` | `cli.py` |
| 3 | Apply the same view to `names`, so an emptied column disappears | `cli.py` |
| 4 | Cover the four criteria, including the all-satisfied project | `tests/test_cli.py` |
| 5 | Regenerate this repository's own index and show what moved | `tasks/README.md` |

Step 1 is the one the drafted plan did not have and the fix does not work without: `context`'s
existing test is `name in schema.edges and ...kind == "dependency"`, which is correct there because
it only ever flags the stored side, and wrong here because the scope covers `blocks` too.

## 3. Implement

**Decisions & assumptions**
- **The filter belongs in `index`, and `context` still needs none** — 2026-08-10. The two surfaces
  are not inconsistent once you ask what each prints: `context` puts the far end's status beside its
  id, so a closed blocker is visible as closed, while an index cell is ids alone and a satisfied edge
  is byte-identical to a live one. So the rule is *a cell that cannot show status must resolve it*,
  which leaves `context`'s `BLOCKS` section listing closed tasks and correct in doing so. Rejected:
  filtering both surfaces for symmetry, which would delete information `context` is able to show.
- **A dangling id is kept in the cell** — 2026-08-10. It cannot be resolved to closed, and `check`
  already reports it. Dropping it would hide from the one artifact people read the very edge the
  validator is complaining about. This differs on purpose from `is_blocked`, which treats a dangling
  target as *not* blocking: that answers "is this task held?", where a target that does not exist
  cannot hold anything, and the cell answers "what is recorded here?". A tree can only be in that
  state while `check` is failing, so the two never disagree in a healthy project.
- **`dependency_names` was needed and the drafted plan did not have it** — 2026-08-10. `schema.edges`
  is keyed by the stored field, so `blocks` is not a key: the membership test `context` uses would
  have silently skipped the entire derived half of the scope. Covered by its own test.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `dependency_names`; `index_block`'s `shown`, applied to both
  the cells and the column-in-use test. `dependency_fields` moved up beside `link_names` so the two
  live where the views read them.
- `tests/test_cli.py` — six tests, one per criterion plus the derived side and the dangling id.
- `tasks/README.md` — regenerated.

**Evidence — checked by being used, on this repository rather than a fixture**
- Before: `tasks/README.md` gave T-005 `Blocked By: T-009` and T-047 `Blocked By: T-003`, both
  blockers `done`, while `context` on each printed `STATE  open, no blocker outstanding`.
- After: **the `Blocked By` column is gone from this repository's index entirely** — every recorded
  blocker in this tree has closed — and the two surfaces now agree. That is criterion 3 demonstrated
  on the real corpus, which no fixture could have shown.
- `Blocks` survives, and filters independently: T-003 listed `T-006, T-047` and now names only
  `T-047`; T-009 listed `T-005, T-006, T-010` and now names only `T-005`.
- Suite **175 passed** (169 before), `check` clean:

```
OK - 112 task(s), 560 field value(s), 353 reference(s), 22 dependency edge(s), 154 declared
output(s), 1 index file(s), 140 document(s), 1078 link(s), 2 template(s), 0 vocabulary row(s)
```

- The change was **shown failing before it passed**: with the renderer changed and the index not yet
  regenerated, six tests failed on one cause — `STALE INDEX   tasks/README.md no longer matches the
  tasks it was generated from` — which is T-025's detector doing its job on a real regression rather
  than a seeded one.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A row whose every dependency has closed shows `-`, and `index` and `context` agree | met | On this repository the column goes rather than the cell, which is the stronger form of the same criterion — the next row covers a cell that survives. `test_a_satisfied_blocker_leaves_the_cell_rather_than_reading_as_live` asserts both surfaces. |
| A row with one closed and one open blocker shows only the open one | met | `test_one_closed_and_one_open_blocker_leaves_only_the_open_one`; and on real data T-003 went from `T-006, T-047` to `T-047`. |
| A project whose dependency edges are all satisfied loses the column | met | Demonstrated twice: the test walks a project to that state, and this repository entered it — `Blocked By` is no longer in the generated header. |
| `parent`, `children` and soft edges unchanged, closed members included | met | `test_a_closed_parent_is_still_a_parent`; `Parent`, `Children` and `Related` are all still in the header with closed members in them. |

**Beyond the written criteria**
- The derived half (`blocks`) was in scope but had no criterion of its own, and it is the half a
  `schema.edges` membership test silently skips. Covered by `test_the_derived_side_is_filtered_too`.
- A dangling blocker had no criterion either. Covered by `test_a_blocker_no_task_claims_is_still_shown`.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Whole lifecycle in one session, under the maintainer's `M2` authorisation recorded in §1. The adopter's premises were re-measured here first and both held. The one thing their write-up missed is that `blocks` is not a key in `schema.edges`, so the test `context` uses would have skipped half the scope without failing anything. |
| 2026-08-10 | → proposed | **Written by an adopting project** — htmldeck, `github.com/uchimata2/htmldeck` — and placed here rather than sent as prose, at the maintainer's request. Ids in the evidence above are that project's, not this one's. It reached the same conclusion independently and had already made this exact change to its own pre-taskmd index generator, recording the reason as *the cell is for what gates the task, and nothing else does*; reading `cli.py` then found T-102, which is the better argument and is this project's own. Estimated `high`/`xs` to match T-102 — the maintainer should re-scope, re-estimate or reject freely. |
