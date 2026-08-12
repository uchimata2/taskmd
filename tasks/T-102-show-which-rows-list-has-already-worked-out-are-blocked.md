---
id: T-102
title: Show which rows list has already worked out are blocked
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-022, T-031, T-070, T-087]
work_package: M2
owner: maintainer
business_value: high
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, plugin/skills/taskmd/taskmd/defaults/config.md, tests/test_list.py]
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
- None. **Q1 — a trailing marker or a column? — answered at `plan`, 2026-08-10: a trailing column,
  which is both.** The two options were not as far apart as the question assumed. What matters is
  that nothing already being read moves, and appending *after* the title achieves that whether the
  cell carries a word or a symbol — so it carries the word, and is self-describing at no cost. See
  **D1**.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the tests first, against `tests/fixtures/ordering/`, and run them on unmodified `HEAD` in a worktree | A recorded failure — the *before*, per `CLAUDE.md` *Verifying* |
| 2 | Add one test the fixture cannot pass by accident: a held task whose **status** is not the blocked value | The test that separates a derived fact from an echoed column |
| 3 | Print the mark in `cmd_list` | `plugin/skills/taskmd/taskmd/cli.py` |
| 4 | Write the rule where the blocked-last rule already lives | `plugin/skills/taskmd/taskmd/defaults/config.md` §*Ordering* |
| 5 | Suite, `index`, `check`, pre-publish check | Recorded output |

Step 1 before step 3 because a test written after the change passes for reasons nobody checked. Step
2 is separate from step 1 because `tests/fixtures/ordering/` happens to give its blocked task
`status: blocked`, so every assertion in step 1 would also pass if the new cell merely echoed the
status column — and the case the report described was a task marked `proposed`.

**Shape decisions.**

**D1 — A trailing column, appended after the title, present only when the project has a blocked task
at all.** Three properties, each chosen against a named alternative:

- *Appended last.* Every field a caller cuts today keeps its index; the title stays the field before
  it. *Rejected: a cell between the configured columns and the title* — self-describing, lines up,
  and shifts the one field every reader and every script already depends on.
- *Carrying a word.* `blocked` and `-`, the latter being the character `list` already prints for an
  empty cell. *Rejected: a bare symbol* — one character, and needs a legend that would have to live
  somewhere.
- *Omitted when the project has none.* This is the rule *Views* already states for a column no task
  has a value for, and the test is **project-wide** for the reason stated there — so `list` and
  `list --limit 1` have the same shape. *Rejected: always present* — it changes the field count for
  every existing caller in order to carry a fact most projects never have, and `list --json` already
  serves the caller who needs it unconditionally.

**D2 — `--json` is not touched.** It has carried `blocked` on every task since the command existed.
That is why this task is `xs`: the fact was already derived, already exported once, and only the
surface a person reads dropped it.

**Planned outputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_list`
- `plugin/skills/taskmd/taskmd/defaults/config.md` — §*Ordering*, sort key 1
- `tests/test_list.py` — `MarksWhatCannotBeStarted`

## 3. Implement

### Steps 1–2 — the tests, and what they do on unmodified `HEAD`

Seven tests in `MarksWhatCannotBeStarted`, run in a worktree of `HEAD` before the change:

```text
Ran 7 tests                                                        FAILED (failures=5)
```

**The two that pass are the two that describe unchanged behaviour** — a project with nothing blocked
prints what it always printed, and `--json` already carries `blocked`. The five that fail are the
whole of the new behaviour. That split is the evidence the suite is measuring the change rather than
the fixture: a test that passed on `HEAD` and after would have told nobody anything.

Step 2's test is the one that matters most. `tests/fixtures/ordering/` gives its held task
`status: blocked`, so a wrong implementation that simply echoed the status column would satisfy every
other assertion. The test copies the fixture, rewrites that task to `status: proposed` — the state
the reported case was actually in — and asserts that no field but the mark says `blocked` and that
the mark still does.

### Steps 3–4 — the change

`cmd_list` appends the cell; the rule is written into §*Ordering* beside blocked-last, which is
where [T-031](T-031-give-the-list-rationale-one-home.md) put that rule's one home, and the code
comment points there rather than restating it. On the fixture:

```text
T-001   proposed   Cheap blocker      -
T-003   proposed   Standalone work    -
T-004   proposed   Unestimated        -
T-002   blocked    The valuable one   blocked
```

### Step 5 — the suite and this repository

```text
Ran 154 tests in 5.972s                                                                      OK
OK - 105 task(s), 525 field value(s), 321 reference(s), 22 dependency edge(s), 134 declared
     output(s), 1 index file(s), 133 document(s), 1002 link(s)
```

The `check` line is the run taken **after** this record was written, not during step 5 — it counts
this task's own references, and a figure quoted from before the write is one no later reader can
reproduce.

**This repository's own output does not change, and that is the feature working.** Nothing here is
blocked, so `list --open` prints exactly what it printed this morning. The demonstration is
necessarily the fixture — which is also why step 1's worktree run matters: it is the only place the
*absence* was recorded before it was filled.

**Decisions & assumptions**

- **The project-wide test is taken over every task, not over the rows selected.** — `list --state
  closed` in a project with one blocked open task therefore prints a column of dashes. That is odd
  read in isolation and it is the rule *Views* states, chosen so every call has one shape; the
  alternative makes `--limit 1` lose a column for the reason it was asked for. — 2026-08-10
- **No new command, flag or config key.** — R-4 asked for the fact to be shown, not for a way to ask
  for it. A flag would be a switch nobody remembers to pass, which is the failure shape T-080 and
  T-095 were both raised for. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — the mark
- `plugin/skills/taskmd/taskmd/defaults/config.md` — §*Ordering*, sort key 1, now *Blocked last, and
  marked*
- `tests/test_list.py` — `MarksWhatCannotBeStarted`, seven tests

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A project with an open dependency shows the marker on the blocked row and not on the others, demonstrated by running it | met | §3 steps 3–4, transcript on `tests/fixtures/ordering/`. Also shown on a case the fixture does not cover on its own — a held task whose status is `proposed` — so the mark is proven derived rather than an echo of the status column. |
| A project with no blocked task produces output identical to today's, byte for byte | met | Two ways: the test asserts the title is the last field on `alt-project`, and this repository's own `list --open` is unchanged, which §3 step 5 states rather than hides. |
| Whether the tab-separated form changes is decided, and if it does, what a script that cuts columns sees is stated | met | **D1**: it changes, by appending only. Every existing field keeps its index and the title stays the field before the new one — asserted by a test, not by inspection. |
| The rule is described in one place, not restated in the code | met | §*Ordering* sort key 1; the code comment points at it. This is [T-031](T-031-give-the-list-rationale-one-home.md)'s arrangement, unchanged. |
| The suite still passes and `check` is clean on this repository | met | `Ran 154 tests … OK` — seven more than before, all seven new — and `check` OK on 105 tasks. |

**Child fix tasks raised**
- none.

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Reviewed against the five criteria as written; **all five met, none carried**, so the task closes. Criterion 2 is met in two ways rather than one, because the byte-identical claim is about a *whole* output and a test on one fixture is not that: `alt-project` asserts the title is still last, and this repository's own `list --open` is unchanged, which the record states plainly rather than treating as an absence of evidence. `deliverables` names the three files. Pre-publish check run last, after this record was written: **189 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All five steps taken, tests first. **Shown failing on unmodified `HEAD`** in a worktree — `Ran 7 tests … FAILED (failures=5)` — and the two that passed are exactly the two describing behaviour that must *not* change, which is what makes the split evidence rather than noise. Step 2 earned its place: `tests/fixtures/ordering/` gives its held task `status: blocked`, so every other assertion would also pass if the new cell merely echoed the status column; the added test rewrites that task to `proposed` — the state the reported case was in — and pins the mark to the derived fact. The change is four lines in `cmd_list` plus the rule in §*Ordering*, where T-031 put blocked-last's one home. `Ran 154 tests … OK`, seven more than before. Recorded because it looks like a gap and is not: **this repository's own output does not change**, since nothing here is blocked — which is the omit-when-unused rule working, and is why the worktree run is the only place the absence was ever captured. |
| 2026-08-10 | → planned | Plan written; §1's Q1 settled as **D1** — a trailing column, which turned out to be both of the options the question offered. What actually mattered was that no field already being cut may move, and appending after the title gives that whether the cell holds a word or a symbol, so it holds the word and is self-describing for free. Two further properties decided against named alternatives: the column is omitted when the project has no blocked task, per the omit-when-unused rule *Views* already states and tested project-wide so `--limit 1` keeps the same shape; and `--json` is untouched, having carried `blocked` since the command existed. That last point is why this is `xs` — the fact was already derived and already exported once, and only the surface a person reads dropped it. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"move on in the suggested order. Full lifecycle."* It covers this task and [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md), the two named in that reply's next steps, and **it does not generalise**. Recorded here for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) exists: there is nowhere else for it yet. |
| 2026-08-10 | → proposed | Raised as R-4 from the first adopting project's recommendations. `high` because `list --open` is the command the skill opens with and the one an agent runs first, and a reader acting on it can start a task that cannot move; `xs` because the value is already computed twice per call — once for the sort key, once for the `--json` payload, which carries `blocked` — and the only missing step is printing it. Confirmed against `cli.py` rather than taken from the report: the tab-separated rows are id, configured columns, title, and nothing else. The tab form's own comment pins the constraint any answer works under — a script cuts those columns, and the title is last. |
