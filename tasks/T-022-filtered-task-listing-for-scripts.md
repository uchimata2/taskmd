---
id: T-022
title: Filtered task listing for scripts
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-003, T-007, T-021]
work_package: v0.1
owner: maintainer
business_value: critical
effort: l
created: 2026-08-05
updated: 2026-08-05
deliverables:
  - plugin/skills/taskmd/taskmd/cli.py
  - plugin/skills/taskmd/taskmd/schema.py
  - plugin/skills/taskmd/taskmd/defaults/config.md
  - tests/test_list.py
  - tests/fixtures/ordering/.taskmd/config.md
  - tasks/_task-template.md
---

# T-022 — Filtered task listing for scripts

## 1. Specify

**Outcome**
A way to ask taskmd for *a subset* of the tasks, in a form a script or an agent can consume without
parsing the human index — for example "everything not yet specified", "everything that depends on
something open", "the children of T-002".

**Requested as** (maintainer, 2026-08-05):

```
/taskmd [list|table] [new|specified|planning|dependent|parents|children]
```

**Why this one**
`index` already computes the whole graph and renders it; what it cannot do is answer a narrower
question. Today the answer is grep over `tasks/`, which works for a person reading and badly for a
script: it re-parses front-matter that taskmd has already parsed, and it cannot see a derived edge
at all — `blocks` and the far end of a soft link exist nowhere on disk, so no grep will ever find
them. That is the gap this task is really about.

**The collision is settled — the owner overrode the non-goal on 2026-08-05.** Shape **2**: a fourth
command, and [`docs/SCOPE.md`](../docs/SCOPE.md) §4 non-goal 11 is amended rather than worked
around. The reasoning, in the owner's terms: token efficiency is a **main requirement**, not a
convenience — §1 and R-15 — so a listing an agent can call instead of reading every task file serves
the goal rather than costing it. Shape 1 was rejected as hiding a first-class instrument behind
options on another command; shape 3 was rejected because it leaves the script case exactly where
grep already fails it. The amendment is narrow: a *filtered listing* is in, the query *language* is
still out, and the three decisions built on the old wording (T-002, T-013, T-019) were checked and
all stand.

**Two design constraints the owner set with the override**, which the criteria below now carry:

1. **Built for the calling agent, not only for a script.** The two shapes it must serve are "give me
   the next task to work on" and "render the list I was asked for" — in a form that is usable as
   printed, so the caller neither parses task files nor re-renders the result.
2. **No cache, no second index.** Nothing derived may be persisted anywhere a later read could find
   it stale. This is the project's design rule (`CLAUDE.md`) applied to a feature that invites
   breaking it: a query result stored is a second copy of a fact, and the maintenance it demands
   costs more than the lookup it saves.

**The original collision, kept because the amendment is only legible against it.**
[`docs/SCOPE.md`](../docs/SCOPE.md) §4 non-goal 11 reads: *"A query language. `context`, `index` and
`check` are the surface. Anything else is grep."* Decided in
[T-007](T-007-define-the-project-scope-goals-and-requirements.md) and reaffirmed on 2026-08-05 in
[T-002](T-002-implement-the-core-cli-context-index-check.md), where it was the stated reason
`decisions` and `deliverables` were **not** built. Building a fourth command now would reverse a
decision two tasks have already been built on, so it is the owner's call, not this task's.

There is a shape that may not need the reversal. Non-goal 11 names `index` as part of the sanctioned
surface, and filtering is what `index` already does internally to split active from closed. Options,
in rough order of how much scope they cost:

1. **Options on `index`** — `index --status <v> --phase <v> --parent <id> --format list|table`. No
   fourth command, so non-goal 11 stands unamended. Least cost; least discoverable.
2. **A fourth command, `list`**, and non-goal 11 is amended to name four. Honest and explicit —
   but it reopens the boundary, and the next request after this one arrives at the same door.
3. **Nothing in the CLI; the skill composes it** — the agent runs `index` and filters. Cheapest of
   all, and worthless to the *script* case in the request, which is the case grep already fails.

**A trap in the requested vocabulary.** `new`, `specified` and `planning` are not taskmd's words —
the default vocabulary has `proposed`, `specified`, `planned`, and a project may rename all of them
(`tests/fixtures/alt-project` uses `todo`/`doing`/`waiting`). A filter that accepts a fixed alias
list would hardcode one project's vocabulary, which is exactly the defect
[T-002](T-002-implement-the-core-cli-context-index-check.md) criterion 7 forbids. Whatever the
filter accepts must come from the schema. Likewise `dependent`, `parents` and `children` are edge
**names**, and those are configurable too — `alt-project` calls them `depends_on`, `epic` and
`stories`.

**Requirements served**
R-15, R-18, R-20 (`docs/SCOPE.md`). Which further requirements apply depends on the shape chosen.

**Scope**
- In: selecting a subset of tasks by stored field value and by edge relationship; a machine-readable
  output form; the surface question above; the two estimate fields and the default order below,
  including their config keys and the backfill of this repository's own tasks.
- Out: sorting, aggregation, counting, boolean expressions, saved queries — each is a step further
  into the thing non-goal 11 exists to prevent, and none is in the request.
- Out: how an agent is told to use it — [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md).

**Reconcile debt this task carries.** Three live statements assert a three-command surface and
become false the moment the fourth lands. They are listed here rather than edited now, because a
task does not fix things outside itself (METHOD §3.3) and none of them is false yet:
`taskmd/cli.py` module docstring ("Three, and no more"); `taskmd/defaults/config.md` §*The tasks
folder* and §*Deliverables*, both of which cite non-goal 11 as keeping the surface at three — the
reasoning survives the amendment, the count does not; and `docs/BRIEF.md` ("keeps the surface at
three, and anything else is grep").

**Inputs**
`docs/SCOPE.md` §4 non-goal 11 and §1; `taskmd/schema.py` (`links`, `derived`, vocabularies);
`taskmd/cli.py` (`index_block` already filters and renders); T-002 §1 criterion 7.

**Acceptance criteria**
- [ ] Every filter value the tool accepts is drawn from the resolved schema, never from a built-in
      alias list — demonstrated against a project whose vocabulary shares no word with the default
- [ ] Filtering on a **derived** edge works (what blocks a task, the far end of a soft link), since
      that is the half grep cannot do and the reason the feature is not redundant
- [ ] The machine-readable form is stable enough to parse without knowing the terminal width
- [ ] An unknown filter value is an error naming what *is* accepted, reported before any output
- [ ] `docs/SCOPE.md` non-goal 11 and the chosen shape agree — met by the 2026-08-05 amendment;
      re-checked at review in case the shape moved during `plan`
- [ ] **Asking for the next task returns one task**, decided by a rule written down in exactly one
      place, and the answer is reproducible — the same tree gives the same task. Falsified by a rule
      that lives in both the tool and the method, or by a tie the tool resolves arbitrarily
- [ ] **`effort` and `business_value` are schema config, not code** — enumerated vocabularies with
      configurable names, settable to `none`. Demonstrated on a project that sets both to `none`
      (ordering degrades to dependencies-first, no error) and on one that renames them
- [ ] **A blocker is pulled forward by what it releases** — shown on a case where the plain reading
      and the effective-value reading disagree, so the rule is proven rather than asserted
- [ ] **Every existing task in this repository carries both values**, and `check` passes with the
      new vocabularies enumerated — the backfill is part of the work, not a follow-up
- [ ] **Nothing the user must maintain** (`docs/SCOPE.md` §1 *Invisibility*). A task whose estimates
      were never filled in still appears and still orders; an estimate a person edits is honoured
      and never overwritten behind their back. Falsified by any state where the tool is wrong until
      someone updates something
- [ ] **The output is usable as printed.** Falsified if the intended caller has to re-render it, or
      has to open a task file to act on the answer
- [ ] **The command writes nothing.** Running it leaves the working tree byte-identical — no cache,
      no manifest, no query log, nothing under a dot-directory. Falsified by any file appearing or
      changing, `tasks/README.md` included

**The default order — decided by the owner, 2026-08-05**

Two new **stored, estimated** fields, filled in by the agent rather than by hand: **effort** and
**business value**. The default order is *highest business value, lowest effort, dependencies
first*, and it applies unless a caller asks for another.

*How "dependencies first" is read — proposed as an assumption, confirmed by the owner 2026-08-05.* Not
merely "a task never precedes its blockers", which would leave a low-value blocker sitting behind
unrelated work and never actually release the valuable task. Instead a task's **effective** business
value is the highest business value among itself and everything it transitively unblocks; the order
is then effective value descending, effort ascending. A blocker is thereby pulled forward *by* what
it releases, which is what makes the rule mean anything, and it is consistent with the earlier
observation that a task releasing three others outranks one releasing none. Effective value is
**derived**, so it adds no third field. If the plain reading was meant instead, one comparison
function changes.

*Two scale choices are assumptions, not decisions* — the work survives either being wrong, since
both are vocabulary rows in the schema config. Effort as a small ordered set rather than hours or
points, because hours are a time estimate and would drag the tool toward the thing non-goal 1
excludes; business value on a comparable small ordered set. Whatever the values, they are
**enumerated in the config like every other vocabulary**, so `check` catches a typo and a project
can rename them (T-001, and T-002 criterion 7 — no built-in alias list).

*Both fields must be optional.* Like `blocked_status` and `deliverables_field`, a project sets them
to `none` and the tool then orders on dependencies alone and names ties rather than inventing a
ranking. A tracker that forces two estimate fields on an adopting project has stopped being
lightweight (§1).

*Nothing derived from them is stored.* Effective value, the order, and the chosen "next" are all
computed per call — the no-cache constraint above, which these fields make tempting to break.

**Open questions**
- ~~Which of the three shapes, and does non-goal 11 change?~~ **Answered by the owner 2026-08-05:
  shape 2, a fourth command, and non-goal 11 is amended** — see above.
- ~~What orders "next"?~~ **Answered by the owner 2026-08-05:** two estimated fields and the rule
  above. The earlier recommendation — a purely derived ranking with no new stored fact — was **not**
  taken; the owner's reason is that an estimate the agent maintains is cheap, and dependents-count
  alone does not distinguish valuable work from merely well-connected work.
- ~~Line format or JSON?~~ **Answered by the owner 2026-08-05: line format by default, JSON behind
  a flag.** Two renderers over one derivation, not two sources of truth.
- ~~`docs/SCOPE.md` §4 non-goal 1 excludes estimates, and `effort` is literally an estimate.~~
  **Answered by the owner 2026-08-05: amended, as narrowly as non-goal 11 was.** Two estimated
  fields that exist **only** to order a listing are in; time tracking, velocity, burndown, capacity
  and Gantt stay out. The carve-out is tested by use — a field read by anything other than the
  ordering has left it.
- ~~Which reading of "dependencies first"?~~ **Confirmed by the owner 2026-08-05: effective value**
  — a blocker is pulled forward by the highest value it transitively releases. No longer an
  assumption.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Settle where the ranking comes from, before any code.** Two estimated fields need an order over their values, and the obvious move — a second table mapping each value to a number — would be a second copy of a fact the vocabulary already carries. Decide, and record the rejected alternatives. | The decision in §3, and the two new keys plus their vocabulary rows in `taskmd/defaults/config.md` |
| 2 | **Write the ordering rule down in one place, in prose, before implementing it.** It is the thing criterion 6 says must have exactly one home, and code plus a doc paragraph is two. | The rule's authoritative statement in `taskmd/defaults/config.md`, which the code will point at rather than restate |
| 3 | **Tests first, failing.** The cases that matter are the ones the rule was written for: a cheap blocker pulled ahead of the valuable task it releases; the plain reading and the effective-value reading disagreeing; a task with no estimates still listed; a project with both fields set to `none`; a renamed vocabulary; an unknown filter value. Per R-16 and the `broken-*` precedent. | New tests in `tests/`, all failing, and a fixture project whose vocabulary shares no word with the default |
| 4 | Resolve the two fields in `taskmd/schema.py` — nullable like `deliverables_field`, with the value-to-rank lookup derived from vocabulary order. | The change in `taskmd/schema.py` |
| 5 | Implement the ordering and the fourth command, with both renderers. The default renderer is the one the caller reads; `--json` is the one a script parses. | `cmd_list` and the ordering in `taskmd/cli.py` |
| 6 | **Backfill every task in this repository** with both estimates. This project runs on its own tool, so an ordering nothing has values for is untested by construction. | The 25 task files, and the basis for the estimates recorded in §3 |
| 7 | **Pay the reconcile debt listed in §1** — three live statements asserting a three-command surface become false when the fourth lands. | `taskmd/cli.py` docstring, `taskmd/defaults/config.md` (two places), `docs/BRIEF.md` |
| 8 | Run the suite, `check`, `index`, the pre-publish check and the new command against this repository, and paste the actual output. | The transcript in §3 |

**Deliverable shape — decided here.**

**"Next" is not a separate concept.** `list` orders by the rule and `--limit 1` is therefore the
next task. *Rejected:* a `next` sub-mode or a fourth-and-a-half command — it would be a second
entry point to one computation, and the first time the two disagreed the tool would have two
answers to the question the owner asked it to settle.

**Blocked tasks sort last rather than being hidden.** *Rejected:* filtering them out, which would
make `list` and `list --limit 1` describe different sets and would hide the graph from a caller
trying to understand why something is not moving.

**Output paths**

- `taskmd/defaults/config.md`, `taskmd/schema.py`, `taskmd/cli.py`
- `tests/` — new tests and one fixture project
- `tasks/*.md` — the backfill
- `docs/BRIEF.md` — step 7

The `deliverables:` field stays empty until step 8, for the reason T-019 recorded: `check`
validates that every declared path exists.

## 3. Implement

### Decisions & assumptions

- **The vocabulary row *is* the ranking, best value first** — 2026-08-05, step 1. `critical`
  outranks `high` because it is written first; `xs` is cheaper than `s` for the same reason.
  *Rejected:* a second table mapping each value to a number, which is the obvious design and is a
  second copy of a fact the vocabulary row already carries — the two would disagree the first time
  someone added a value to one of them, and the tool would have no way to tell which was right.
  The cost is that the ordering of a config table is now load-bearing, which is stated in the key's
  own section rather than left to be discovered.
- **The rule's one home is `taskmd/defaults/config.md` §*Ordering*** — 2026-08-05, step 2. The code
  points at it and does not restate it; both `effective_values` and `order` carry a one-line
  reference instead of a paragraph. That is what criterion 6 asks for, and it is the reason the
  rule was written in prose before it was written in Python.
- **`--limit 1` is "the next task"; there is no `next`** — 2026-08-05. Decided in `plan` and worth
  restating as an implementation fact, because it is what makes the ordering testable: one code
  path answers both questions, so they cannot disagree.
- **Blocked-last is computed from open dependencies, not from a status value** — 2026-08-05. A
  project may have no `blocked` status at all (`alt-project` sets `blocked_status: none`), and a
  task can carry any status while genuinely being held. Reading the graph rather than the label
  means the ordering works on a project whose vocabulary has no word for it.
- **Tab-separated, not padded columns** — 2026-08-05. Padding is prettier and makes the second half
  of the criterion impossible: a caller cannot split a padded line without knowing the widths, and
  the widths depend on the data. Tabs are readable as printed *and* cuttable. *Rejected:* JSON as
  the default, which would have made the common case — an agent reading the answer — the expensive
  one.
- **A dependency cycle is `check`'s to report, not this command's to hang on** — 2026-08-05. The
  effective-value walk carries a seen-set and stops rather than recursing forever. `list` on a
  cyclic project returns an order; `check` is what says the cycle is there.

### Escalated, not fixed here

- **Adding a required config key breaks every existing config**, because a config *replaces* the
  default rather than merging with it (T-001). Three fixture configs and one test template had to
  be edited before the suite would run. This is the settled rule working as designed, not a
  defect — but it means an adopting project's config breaks on upgrade, and `docs/SCOPE.md`
  non-goal 8 puts migration tooling out of scope for v1. Recorded here rather than raised as a
  task: nothing is actionable until there is a released version to upgrade *from*, and T-006 owns
  the moment that becomes true.

### Outputs produced

- `taskmd/defaults/config.md` — `value_field`, `effort_field`, two vocabulary rows, and the
  `## Ordering` section that is the rule's only home
- `taskmd/schema.py` — the two nullable keys and `Schema.rank`
- `taskmd/cli.py` — `cmd_list`, `order`, `effective_values`, `parse_filters`; docstring reconciled
- `tests/test_list.py` — 18 tests; `tests/fixtures/ordering/` — the decisive fixture
- `tests/fixtures/README.md`, `tests/test_cli.py`, `tests/test_schema.py`,
  `tests/fixtures/alt-project/`, `tests/fixtures/broken-tasks-dir/` — the new keys and the new rows
- `tasks/*.md` (25 files) and `tasks/_templates/task-template.md` — the backfill
- `docs/BRIEF.md` — step 7

**The estimates** were assigned on one basis, stated so a later reader can disagree with it
specifically: **value** is worth to the goal in `docs/SCOPE.md` §1 — the tasks that release
publication are `critical`, the ones that make the tool trustworthy are `high`, and cosmetic fixes
are `low`; **effort** is the size of the work *remaining*, not the work already done, which is why
several closed tasks carry small values.

### Verification

**Tests first, and they failed.** Written before any code, against a fixture built so the two
readings of the rule disagree:

```
Ran 92 tests — FAILED (failures=32, errors=15)
  test_a_cheap_blocker_is_pulled_ahead_by_what_it_releases  ... usage: python -m taskmd {check,context,index}
  test_ordering_degrades_to_blocked_last_then_id            ... CONFIG ERROR unknown config key(s): effort_field, value_field
```

After implementing: **92 tests, 92 pass**, up from 74.

**The ordering, on the fixture built to catch the wrong reading.** `tests/fixtures/ordering/` holds
T-001 (`low`/`xs`, blocking T-002), T-002 (`critical`/`l`, blocked), T-003 (`high`/`s`) and T-004
(no estimates). The order is `T-001, T-003, T-004, T-002` — the cheapest, least valuable task
leads, because it releases the most valuable one. Under the plain reading T-003 would lead, and
`test_the_plain_reading_would_have_answered_differently` fails if anyone reverts to it.

**On this repository, which is the real case.** `list --open --limit 1` answers the question that
was being answered by hand two sessions ago:

```
T-018    proposed  -  specify  Stop the pre-publish fixture tripping its own check
```

That matches the manual working recorded then — four tasks tie on effective value because each
releases T-006, and the tie breaks on effort. The tool now derives what a person previously had to
reason out from the index.

**Filtering on a derived edge**, which is the half grep cannot do at all:

```
python -m taskmd list --blocks T-006
T-018 ... T-010 ... T-011 ... T-003 ... T-008 ... T-009 ... T-002
```

`blocks` is written on no task and exists in no file; every one of those rows was computed.

**A project whose vocabulary shares no word with the default.** `alt-project` renames the effort
field to `size` and sets `value_field: none`. `list` orders it, `--state todo` filters it, and
`--state proposed` — the default vocabulary's word — is rejected with this project's values named.

**Rejections arrive before output.**

```
python -m taskmd list --status nonsense
--status does not take 'nonsense'. This project's status values are: proposed, specified, planned,
in_progress, blocked, review, done, cancelled          exit=2
```

**It writes nothing.** `test_the_tree_is_byte_identical_afterwards` snapshots every file in the
fixture, runs the three forms of the command, and compares bytes.

**Publishing checks:** `check` clean on 25 tasks; pre-publish grep at five hits, all in T-013's
fixture (T-018's, unchanged) — the new command, fixture and tests added none.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every filter value is drawn from the resolved schema, never a built-in alias list — demonstrated against a project sharing no word with the default | met | `alt-project` renames the effort field to `size` and declares no value field; `list` orders and filters it, `--state todo` works, and `--state proposed` is rejected *naming this project's* values. The accepted filter names are computed from `schema.vocabularies` and `link_names(schema)`, so a project that renames a field renames its flag. The requested words `new`/`specified`/`planning` from §1 were **not** implemented as aliases, which was the trap this criterion was written for |
| Filtering on a **derived** edge works | met | `list --blocks T-006` returns seven tasks. `blocks` is stored on no task and appears in no file — it is the inverse of `blocked_by`, computed at read time. This is the case grep cannot reach, and the reason the command is not redundant with it |
| The machine-readable form is stable without knowing the terminal width | met | Tab-separated, so a caller splits on `\t` and a script can `cut`. Padded columns were rejected in `implement` precisely because they would have failed this. `--json` is the second renderer over the same derivation, and `test_json_parses_and_carries_the_same_ids` asserts the two forms list the same tasks in the same order |
| An unknown filter value is an error naming what *is* accepted, before any output | met | Verified in both directions: an unknown **value** names the project's vocabulary, an unknown **name** names the accepted flags. `test_nothing_is_printed_before_the_error` asserts no tab ever reaches stdout on the error path, so the check is that parsing completes before rendering starts, not that the message happens to come first |
| `docs/SCOPE.md` non-goal 11 and the chosen shape agree | met | The non-goal was amended on 2026-08-05 to carve out a filtered listing and nothing else. Review re-checked the three claims that became false with the fourth command — `taskmd/cli.py`'s docstring, two paragraphs in `taskmd/defaults/config.md`, and `docs/BRIEF.md` — all four reconciled in step 7, and each now states that the carve-out is the listing, not a licence to add commands |
| Asking for the next task returns one task, by a rule with exactly one home, reproducibly | met | `--limit 1` over the same ordering, so there is no second code path to disagree with the first. The rule's home is `## Ordering` in the schema config; the two functions that implement it carry a pointer, not a paragraph. Reproducibility is asserted by running the command twice and comparing output, and the final sort key is the id, so ties are total rather than arbitrary |
| `effort` and `business_value` are schema config — nullable, renameable, enumerated | met | Demonstrated both ways: `alt-project` renames one and nulls the other; `WorksWithoutEstimates` copies the ordering fixture with both set to `none` and asserts the order degrades to blocked-last-then-id with no error. The tool contains no literal `effort`, `business_value`, `xs` or `critical` |
| A blocker is pulled forward by what it releases — shown on a case where the two readings disagree | met | The whole point of `tests/fixtures/ordering/`: T-001 is the least valuable and cheapest task in the project and it leads, because it blocks T-002. A second test asserts T-003 — what the plain reading would return — is *not* first, so a silent reversion fails rather than passing quietly |
| Every existing task carries both values, and `check` passes | met | 25 of 25 backfilled, template updated so the next task carries them from creation. `check` clean on 25 tasks. The basis for the estimates is recorded in `implement` rather than left as unexplained values |
| Nothing the user must maintain (§1 *Invisibility*) | met | A task with no estimates is still listed and still ordered, after the ones that have them — asserted on T-004 in the fixture. Hand-written values are read and never rewritten; nothing in this command writes at all |
| The command writes nothing — the tree is byte-identical | met | `WritesNothing` snapshots every file under the fixture, runs the line form, the JSON form and `--limit`, and compares bytes. No cache, no manifest, no timestamp file: effective value is recomputed per call |

**Also checked, beyond the criteria**

- Suite 92/92, up from 74. Pre-publish check unchanged at five hits, all T-013's fixture.
- `list` was run against a project with a dependency **cycle** (`broken-cycle`): it returns both
  tasks and exits 0, while `check` on the same project reports `CYCLE dependency loop: T-001 ->
  T-002 -> T-001` and exits 1. The guard was written during `implement`; review is where it was
  actually exercised, and the division holds — listing answers, validating judges.
- The generated index is unchanged in shape by the two new fields, because `index_columns` was not
  extended — the estimates are orderable without being on screen in every view.

**Child fix tasks raised**
- none — every criterion is met.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → done | Review worked. All eleven criteria met, no child fixes. Review exercised two things `implement` had not: `list` against a cyclic project (returns an order and exits 0, while `check` reports the loop), and the reconcile debt re-checked in all four places. The tool now answers the question a session was answering by hand two turns ago, and gives the same answer. |
| 2026-08-05 | → review | Implemented in plan order. The load-bearing decision was step 1's: the vocabulary row *is* the ranking, so there is no value-to-number table to disagree with it — the cost being that a config table's ordering is now load-bearing, which the key's own section states. The rule was written in prose before Python, and the code points at it rather than restating it. 18 new tests written first and failing; 74 → 92. One consequence recorded rather than raised: adding a required config key breaks every existing config, which is the replace-not-merge rule working as designed and is nothing to act on until there is a release to upgrade from. |
| 2026-08-05 | → planned | Eight steps, with the ranking's source settled before any code because the obvious design — a value-to-number table — is a second copy of the vocabulary. Two shape decisions: `--limit 1` *is* "the next task", so one code path answers both questions and they cannot disagree; and blocked tasks sort last rather than being filtered out, so `list` and `list --limit 1` describe the same set. |
| 2026-08-05 | → specified | Last two questions answered by the owner: non-goal 1 amended as narrowly as 11 was, and the effective-value reading of "dependencies first" confirmed. A new project-wide property arrived with them — `docs/SCOPE.md` §1 *Invisibility*, the tool asks nothing of the user to stay correct — which added an eleventh criterion and is the reason the estimate fields are agent-filled, overridable and optional rather than required. |
| 2026-08-05 | (no status change) | Owner overrode non-goal 11: shape 2, a fourth command, with the amendment written into `docs/SCOPE.md` §4 and the now-false rationale in `CLAUDE.md` corrected. Blast radius checked before amending — T-002, T-013 and T-019 each cite the non-goal, and all three decisions stand under the narrowed wording. Two design constraints came with the override (built for the calling agent; no cache or second index) and became three criteria. Status stays `proposed`: two questions the override *created* are open — what orders "next", and the output format — and both change the outcome. |
| 2026-08-05 | → proposed | Requested by the maintainer. Recorded with the non-goal 11 collision as its first open question rather than as a straightforward feature — two tasks have already been built on that non-goal, so reversing it is the owner's decision. The requested filter words were checked against the schema and are aliases, not vocabulary; noted so `specify` does not inherit them by default. |
