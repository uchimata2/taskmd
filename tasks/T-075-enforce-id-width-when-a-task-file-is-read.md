---
id: T-075
title: Enforce id width when a task file is read
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-062, T-004]
work_package: v0.1
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-075 — Enforce id width when a task file is read

## 1. Specify

**Outcome**
`id_width` means something when tasks are read, so the binding's *enumerate* rule — keep the files
whose id matches the configured prefix **and width** — is true of the tool.

**Why this one**
Raised as **F-16** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. `Schema.is_id` compiles `^<prefix>\d+$` — prefix plus any run of digits, with
`id_width` used only by `format_id` when a new id is composed. Shown alongside T-062, on a project
using the default `id_width: 3`:

```
taskmd list --root <a scratch project>
T-0001  proposed  -  specify  over-wide id, width is 3
T-001   proposed  -  specify  SECOND file alphabetically
```

`T-0001` is accepted as a task. [`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)
*enumerate* says the opposite:

> read every `.md` file; keep the ones whose `id` field matches the configured prefix **and width**.

**Consequence, stated honestly: mild.** The task loads, sorts and links; nothing is lost. What it
costs is that an id no `create` would ever produce is silently a task, so a typo in an id — the most
likely way to reach this — is indistinguishable from a deliberate one, and the file sorts by string
rather than where its number belongs. It is `low` for that reason and not because the binding's
sentence matters less than the others.

**Why it is a separate task from [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md).**
Same function, same likely commit, different evidence and different severity — T-062 loses a task,
this one accepts an odd one. Splitting them keeps each judgeable on what it actually costs, and the
soft edge records that they are one piece of work in practice. Whoever plans T-062 should plan this
with it.

**Requirements served**
R-13 (`docs/SCOPE.md`) — a binding's stated behaviour is what an adopter builds on; R-11, since
`id_width` is a config key that currently does less than the config implies.

**Scope**
- In: whether `is_id` honours `id_width`, and what happens to a file whose id does not — ignored as
  not-a-task, or reported.
- In: the third possibility, that the **binding** is what should change: a project migrating from
  another scheme may hold historical ids of mixed width, and rejecting them is not obviously right.
- Out: id format, the merge-conflict policy and the scale ceiling, all
  [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md)'s.
- Out: duplicate ids, which is T-062.

**Inputs**
`plugin/taskmd/schema.py` (`Schema.is_id`, `format_id`, `number_of`, `load_tasks`),
[`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) *enumerate*,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-16.

**Acceptance criteria**
- [ ] The code and the binding agree about what `id_width` does when a task is read — whichever way
      the disagreement is resolved
- [ ] Shown failing first on a fixture, per R-16
- [ ] `tests/fixtures/alt-project`, which uses a different prefix and width, still loads unchanged
- [ ] If an out-of-width id stops being a task, that is **reported** rather than silently ignored —
      a file dropping out of the project with no signal is the failure T-062 exists to remove

**Open questions**
- ~~**Does the code change, or the binding?**~~ **Answered by the maintainer on 2026-08-09: the code —
  enforce the width, and report the mismatch.**

  So `is_id` honours `id_width`, and a file whose `id` does not match it is **not silently ignored**:
  it is reported, which is criterion 4 and the same failure mode
  [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) exists to remove. `id_width`
  then means one thing in both directions — what `format_id` composes and what `is_id` accepts —
  instead of being a formatting rule the reader is told is a filter.

  *Rejected: relaxing the binding's* enumerate *sentence to drop "and width".* It costs nothing and
  tolerates whatever a migration produces, and that is the whole of its appeal. It also leaves
  `id_width` doing less than the config implies, which is the R-11 half of the finding, and leaves a
  typo in an id indistinguishable from a deliberate one — the failure this task was raised for.

  *Rejected: accepting the file but warning.* Nothing drops out of the project, which is attractive.
  It needs the binding **and** the tool reworded to describe a third behaviour that is neither
  "matches" nor "does not", and it turns `check`'s output into advice on a file that is a task
  anyway. Two documents changed to avoid changing one function.

  **What a migrating project pays, stated rather than waved past:** an existing backlog with
  mixed-width ids must normalise them or declare a wider `id_width`. Non-goal 8 puts migration tooling
  out of v1, so this project offers neither — the error message has to be good enough to make the
  manual route obvious, which is what criterion 4 is now carrying.

## 2. Plan

Planned and implemented **inside [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md)'s
plan**, which is what §1 asked for: same function, same commit, different evidence. T-062 §2 holds
the eight steps; the two that are this task's are below, and this record judges its own criteria.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Make `is_id` width-strict, and add the near-miss predicate that makes a rejection *reportable* rather than merely a rejection | `Schema.is_id`, `Schema.looks_like_id` |
| 2 | A fixture holding exactly this defect, with an ordinary sibling so what is shown is a **file** being rejected and not a project failing to load | `tests/fixtures/broken-id-width/` |
| 3 | Report it as its own `check` class, on the same channel T-062 built | `ID WIDTH` in `cli.check_anomalies` |
| 4 | Prove `alt-project` — a different prefix **and** a different width — is untouched, at the schema level and through the CLI | Both transcripts |
| 5 | State the reading rule in the binding, which currently describes only what is kept | `local-markdown.md` *enumerate* |

**Why step 1 needs two predicates and not one stricter one.** Tightening `is_id` alone would have
made the file simply stop being a task — which is criterion 4's failure, and the same silence T-062
exists to remove. `looks_like_id` is the whole reason a near-miss can be told from a README.

## 3. Implement

**Decisions & assumptions**

- **D1 — two predicates: `is_id` enforces, `looks_like_id` recognises the intent** — 2026-08-09.
  `is_id` becomes `^<prefix>\d{<width>}$`; `looks_like_id` keeps the old `\d+` and exists only so a
  file that meant to be a task can be reported instead of ignored. Without the second, enforcement
  is indistinguishable from a file dropping out of the project, which criterion 4 forbids in terms.

- **D2 — one call site, checked rather than assumed** — 2026-08-09. `is_id` is called in exactly one
  place (`load_tasks`); `format_id` and `number_of` are unaffected. Swept before the change, because
  a predicate used in five places would have made a strict version a much larger decision than the
  `xs` this was estimated at.

- **Assumption, recorded:** that `alt-project` is a sufficient guard for the configurable case. It
  differs from the default in both prefix and width, which is the pair this change is about — but it
  is one project, and a schema with `id_width: 1` is untested. Nothing in the tree uses one.

### Step 2–3 — shown failing first (R-16), then reporting

Against the pre-fix tool, restored from the index for the run:

```
taskmd check --root tests/fixtures/broken-id-width
OK - 2 task(s), vocabulary valid, references resolve, no broken links     exit 0
taskmd list  --root tests/fixtures/broken-id-width
T-0001  proposed  -  specify  An id one digit too wide for the configured width
T-002   proposed  -  specify  An ordinary task, here so the project is not empty
```

`T-0001` is a task, under `id_width: 3`. After:

```
taskmd check --root tests/fixtures/broken-id-width
ID WIDTH      tasks/T-0001-over-wide.md declares 'T-0001', which is not T- plus 3 digit(s), so it
              is not loaded as a task
1 problem(s) over 1 task(s)                                               exit 1

taskmd list --root tests/fixtures/broken-id-width
taskmd: 1 problem(s) with the task files - run 'taskmd check'   [stderr]
T-002   proposed  -  specify  An ordinary task, here so the project is not empty
```

The `list` line is criterion 4 in one transcript: the file is out of the project **and** something
said so, on both channels.

### Step 4 — the configurable case

At the schema level, against `alt-project`'s own config (`ISSUE-`, width 4):

```
ISSUE-0001    is_id=True   looks_like_id=True
ISSUE-001     is_id=False  looks_like_id=True     <- a near miss: reportable
ISSUE-00001   is_id=False  looks_like_id=True     <- the same, one digit the other way
T-001         is_id=False  looks_like_id=False    <- another project's id: not a near miss
notes         is_id=False  looks_like_id=False
```

And through the CLI, unchanged:

```
taskmd check --root tests/fixtures/alt-project   OK - 3 task(s), ...
taskmd list  --root tests/fixtures/alt-project   ISSUE-0001 / ISSUE-0002 / ISSUE-0003
```

The `T-001` row is the one worth keeping: a stray file from a different scheme stays a non-task and
is **not** reported, which is what stops the new class firing on every neighbour's notes.

**Outputs produced**
- `plugin/taskmd/schema.py` — `is_id` width-strict, `looks_like_id` beside it
- `plugin/taskmd/cli.py` — the `ID WIDTH` class
- `tests/fixtures/broken-id-width/` — the over-wide id and an ordinary sibling
- `tests/test_cli.py` — `test_an_id_that_is_the_right_prefix_and_the_wrong_width`
- `plugin/docs/bindings/local-markdown.md` — *enumerate*'s reading rule

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The code and the binding agree about what `id_width` does when a task is read | met | The code changed, per the maintainer's answer. *enumerate*'s existing "prefix **and width**" sentence is now true, and it gained the sentence saying what happens to the file that fails it |
| Shown failing first on a fixture, per R-16 | met | §3 — `OK - 2 task(s)`, exit 0, `T-0001` listed as a task under `id_width: 3` |
| `tests/fixtures/alt-project` still loads unchanged | met | §3 step 4, at both altitudes: the predicates against its own schema, and `check`/`list` through the CLI |
| If an out-of-width id stops being a task, that is **reported** rather than silently ignored | met | `ID WIDTH` on `check` with exit 1, and the stderr line on every other command. This is the criterion `looks_like_id` exists for — without it, enforcement would have been the silence it was meant to remove |

**Child fix tasks raised**
- none. Worked with [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) in one
  commit, as §1 predicted; the two records judge their own criteria separately, which is what the
  split was for.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met, in one commit with T-062. The design point is that enforcement needed **two** predicates, not one stricter one: tightening `is_id` alone would have made the file quietly stop being a task, which is criterion 4's own failure and the exact silence T-062 exists to remove — so `looks_like_id` exists to tell a near-miss from a README. Swept first and recorded: `is_id` has exactly one call site, which is what kept this the `xs` it was estimated at. `alt-project` proved untouched at both altitudes, and a stray `T-001` under an `ISSUE-` schema is correctly *not* a near miss, which is what stops the new class firing on a neighbour's notes. |
| 2026-08-09 | → in_progress | Planned inside T-062's plan, which is what §1 asked for. |
| 2026-08-09 | → specified | Answered: **the code changes** — `is_id` honours `id_width`, and a file whose id does not match is **reported**, not silently ignored. That makes criterion 4 the load-bearing one: the failure mode this shares with T-062 is a file leaving the project with no signal, so an enforcement that merely drops the file would trade one silent loss for another. Relaxing the binding was rejected for leaving `id_width` doing less than the config implies (the R-11 half of the finding) and a typo indistinguishable from intent; accept-but-warn was rejected for needing two documents reworded to describe a third behaviour. The cost is stated rather than waved past: a migrating backlog with mixed-width ids must normalise or widen `id_width`, and non-goal 8 ships no tool for it — so the error message has to make the manual route obvious. |
| 2026-08-09 | → proposed | Raised as F-16 from the T-059 audit, clause 1. Reproduced alongside T-062 on a scratch project: an over-wide id is accepted under `id_width: 3`. `low`/`xs` — nothing is lost, only a rule the config implies and the binding states is not applied. Split from T-062 deliberately: same function and probably the same commit, but different evidence and a different cost, and merging them would hide one behind the other. |
