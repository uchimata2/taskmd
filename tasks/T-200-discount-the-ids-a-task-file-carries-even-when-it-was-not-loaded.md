---
id: T-200
title: Discount the ids a task file carries even when it was not loaded
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-121, T-197, T-062]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-21
adopter_visible: yes
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-200 — Discount the ids a task file carries even when it was not loaded

## 1. Specify

**Outcome**
`check_duplicate_index` stops reporting a task file for naming its own id, in the case where that
file was excluded from `tasks` by a different check — so `DUPLICATE INDEX` no longer fires on the
`broken-duplicate-id` fixture, and the exception recorded against it in `tests/test_cli.py` is
deleted.

**Why this one**
Found on 2026-08-21 while [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)
derived the harness's class list and the owner ruled the advisory classes into the cross-fixture
silence assertion. The first run with advisories included failed immediately:

```text
AssertionError: 'DUPLICATE INDEX' unexpectedly found in
  DUPLICATE ID  T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md ...
  DUPLICATE INDEX  tasks/T-001-second.md: a second table of 1 known task ids sits outside
  the taskmd markers
```

**The mechanism, which is the part worth stating.** `check_duplicate_index` discounts *structural*
ids — the ones a task file is entitled to carry, being its own and those in its own edge fields —
and it builds that discount from `tasks`. A file that lost the duplicate-id race is **not in
`tasks`**: `T-001-second.md` declares `T-001` and is not loaded, so it gets no entitlement and is
judged as an arbitrary document that happens to name every known id. With one loaded task, a
majority of the known set is one, so a single mention of its own id fires the rule.

**It is the small-N case the check already knew about, arriving by a door it did not.** The
docstring for that check records exactly this shape — *it is arithmetic at three* — and closes it by
discounting structural ids. The discount is right; its **input** is a set that a different check has
already pruned. Three checks prune it that way: duplicate id, id width and parked task
([T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) is why the
first of those is visible at all).

**Requirements served**
R-16 (`docs/SCOPE.md`).

**Scope**
- In: what `check_duplicate_index` treats as a task file's own entitlement
- In: the same question for the other two prunings — id width and parked task — since the cause is
  shared and fixing one shape and not the others leaves the finding half-closed
- In: deleting the `also=[("DUPLICATE INDEX", "T-200")]` exception in `tests/test_cli.py`, which is
  written to fail once this is fixed
- Out: the majority threshold itself, which is
  [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md)'s and was decided
  with its reasons
- Out: whether an unloaded file should be excluded from the scan entirely — a different and larger
  question, and a rule that stops reading a file because another check complained about it is how a
  second defect hides behind a first

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_duplicate_index`, and the `structural` map
- `tests/fixtures/broken-duplicate-id/` — the fixture that shows it, with no edit needed
- [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) — the threshold and
  the discount, and why each is what it is

**Acceptance criteria**
- [ ] `check` on `tests/fixtures/broken-duplicate-id` reports `DUPLICATE ID` and not
      `DUPLICATE INDEX`, and the run is quoted
- [ ] The same is answered for a file pruned by id width and by a parked-task folder — each either
      shown not to have the problem, or fixed with it
- [ ] **The check is still shown to fire on a real duplicate table**, so the repair narrows the rule
      rather than switching it off — broken on purpose, with the output quoted
- [ ] The `also=` exception is deleted from `tests/test_cli.py` and the suite passes without it

**Open questions**
- none

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Show, **before touching anything**, whether each of the three prunings can produce the false positive. `broken-duplicate-id` already does. The other two fixtures are quiet today, and quiet is not the same as safe — their pruned files simply happen to name no loaded id — so build the minimal case for each and run `check` on it. | Three runs quoted in §3, each with the exact line it printed or did not |
| 2 | Fix the **cause**, not the three shapes: `check_duplicate_index` builds its entitlement map from `tasks`, so a file's right to name its own id depends on its having won a race a different check adjudicates. Derive the entitlement from the file's own front-matter instead. | The changed `check_duplicate_index` in `plugin/skills/taskmd/taskmd/cli.py` |
| 3 | Re-run all three cases from step 1. | The same three runs, after, quoted beside the before |
| 4 | **Break a real duplicate table on purpose** and show the check still fires. A repair that narrows a rule and a repair that switches it off look identical from a clean run. | The failing run quoted, on a tree built to trip it |
| 5 | Delete `also=[("DUPLICATE INDEX", "T-200")]` from `tests/test_cli.py` and run the whole suite. The entry was written to fail once this is fixed, so leaving it is a failing suite, not a tidy-up. | The suite's output |
| 6 | Run this repository's own gates, which are also a real corpus of 200-odd tasks the changed check now scans. | `taskmd index` and `taskmd check` output |

**Where the step 1 and step 4 cases live — decided at `plan`, 2026-08-21.** They are built in a
scratch directory outside the repository and thrown away, **not added to `tests/fixtures/`**.
*Rejected: two new fixtures, one per pruning.* After step 2 there is exactly one code path computing
entitlement, for every file, so `broken-duplicate-id` exercises it for all three shapes; a fixture
per shape would be three copies of one guard, and each would need a class expectation of its own in
the harness [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) derives.
The cost is named rather than hidden: the id-width and parked shapes are demonstrated **once, here**,
and afterwards nothing re-runs them.

**Outputs this task will produce** (plain paths — at `plan` neither is written yet):
- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py

## 3. Implement

### Step 1 — all three prunings produce it, and two of the fixtures were quiet by accident

`broken-id-width` and `broken-parked-task` print no `DUPLICATE INDEX` today. That is a property of
what is written in them, not of the code: neither pruned file happens to name a **loaded** id. Give
each pruned file one `related:` edge to the task that does load, and both fire. Three trees, built
outside the repository, `check` run on each **before** any change:

```text
dup-id     DUPLICATE ID     T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md ...
           DUPLICATE INDEX  tasks/T-001-second.md: a second table of 1 known task ids sits outside ...

id-width   ID WIDTH         tasks/T-0001-over-wide.md declares 'T-0001', which is not T- plus 3 digit(s) ...
           DUPLICATE INDEX  tasks/T-0001-over-wide.md: a second table of 1 known task ids sits outside ...

parked     PARKED TASK      tasks/_drafts/T-002-parked.md declares 'T-002', a valid id, but it sits ...
           DUPLICATE INDEX  tasks/_drafts/T-002-parked.md: a second table of 1 known task ids sits outside ...
```

**D1 — the answer to §1's second scope item is *all three have it*, not *two do not* — 2026-08-21.**
Had the two fixtures been run as they stand and the quiet read as an answer, this task would have
closed having fixed one third of itself with two ticks against it. The fixtures were the wrong
instrument, and the criterion's own wording — *each either shown not to have the problem, or fixed
with it* — is what made the difference visible.

### Step 2 — the fix is aimed at the cause

`check_duplicate_index` built its entitlement map by walking `tasks`, so a file's right to name its
own id depended on its having **won a race a different check adjudicates**. Replaced with a helper
that reads the entitlement out of the file's own front-matter:

```python
def entitlement(path, schema, text):
    fields, _ = split_front_matter(text)
    if not fields:
        return set()
    task = Task(path, schema, fields)
    entitled = {task.id} if task.id else set()
    for ids in task.edges.values():
        entitled.update(ids)
    return entitled
```

**D2 — the cause, not the three shapes — 2026-08-21.** *Rejected: carrying the pruned files'
entitlements on `Anomaly`*, which is more surgical and covers exactly the three prunings that exist
today. A fourth reason to prune would reintroduce this silently, and the enumeration would be a
second statement of "which files are not loaded" living beside the one in `load_tasks`. Reading the
front-matter costs nothing extra: the scan has already read the file's text.

**D3 — an ordinary document is entitled to nothing, and that is the right answer — 2026-08-21.** The
helper runs on every scanned Markdown file, not only on task files. One with no front-matter returns
the empty set, so nothing changes for it. One that *does* carry an id and edges is entitled to them
by the same rule as a task, whether or not the loader took it — which is the whole point.

The check's docstring now carries where the entitlement comes from and what depending on `tasks`
cost, so the next reader meets the reason rather than the code.

### Step 3 — the three cases, after

```text
dup-id     DUPLICATE ID     T-001 is claimed by ...              (DUPLICATE INDEX gone)
id-width   ID WIDTH         tasks/T-0001-over-wide.md ...        (DUPLICATE INDEX gone)
parked     PARKED TASK      tasks/_drafts/T-002-parked.md ...    (DUPLICATE INDEX gone)
```

Each still reports its own class and exits 1 on it. Nothing was switched off but the false line.

### Step 4 — it still fires, and the narrowing is exact

Two trees built to trip it, four tasks each, run **after** the fix:

```text
still-fires       DUPLICATE INDEX  docs/old-index.md: a second table of 4 known task ids sits
                                   outside the taskmd markers
still-fires-task  DUPLICATE INDEX  tasks/T-005-holder.md: a second table of 3 known task ids sits
                                   outside the taskmd markers
```

The second is the one that matters. `T-005-holder.md` is a **task file** holding a pasted table of
four ids, and it declares one of them as a `related` edge. The count is **3**, not 4 and not 0: its
own id and its one declared edge are discounted, the three ids it never declared are not. That is the
narrowing stated as arithmetic rather than as a verdict.

### Step 5 — the exception is deleted and the suite is green

`also=[("DUPLICATE INDEX", "T-200")]` removed from `tests/test_cli.py`. The suite:

```text
309 passed, 3 skipped, 6 subtests passed in 38.54s
```

**It failed first, and the reason is worth recording.** The first run after the deletion reported
**8 failures**, seven of them in classes that run `check` over this repository. None was the change:
this task's own edits to its record had left `tasks/README.md` stale, and `check` says so — the
behaviour [T-025](T-025-let-check-notice-a-stale-generated-index.md) added. `taskmd index`, then
green. Recorded because a first run of 8 failures against a repair is exactly the moment a session
starts editing the repair.

### Step 6 — this repository's gates

```text
taskmd index   Wrote tasks/README.md - 11 active, 196 closed
taskmd check   OK - 207 task(s), ... 239 document(s), 2759 link(s), 4404 table row(s) ...   exit 0
```

207 tasks and 239 documents is the largest corpus available here, and the changed check scans every
one of them: no `DUPLICATE INDEX` line appeared where none appeared before.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — the `entitlement` helper, `check_duplicate_index`, and its
  docstring
- `tests/test_cli.py` — the `also=` exception deleted

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `check` on `tests/fixtures/broken-duplicate-id` reports `DUPLICATE ID` and not `DUPLICATE INDEX`, and the run is quoted | met | §3 steps 1 and 3, the same fixture before and after. `DUPLICATE ID` still fires and still exits 1 |
| The same is answered for a file pruned by id width and by a parked-task folder — each either shown not to have the problem, or fixed with it | met | **Both had it.** Step 1 shows all three firing before the change and step 3 all three quiet after. The two fixtures were quiet only because neither pruned file named a loaded id (D1) |
| The check is still shown to fire on a real duplicate table | met | Step 4, two trees. The stronger is a task file holding a pasted table: it fires with a count of **3** — its own id and its one declared edge discounted, the three ids it never declared counted |
| The `also=` exception is deleted from `tests/test_cli.py` and the suite passes without it | met | `309 passed, 3 skipped, 6 subtests passed`. The first run failed 8, all from a stale index this task's own record edits caused, recorded in step 5 rather than quietly re-run |

**Child fix tasks raised**
- none. The plan's recorded cost stands and is not a gap in this task: the id-width and parked shapes
  were demonstrated once and nothing re-runs them. After step 2 there is a single code path computing
  entitlement for every file, and `broken-duplicate-id` exercises it, so a fixture per shape would be
  three copies of one guard.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | `implement` and `review` under the grant below. **Four criteria, four met, no child task.** The finding that changed the shape of the work is D1: the id-width and parked fixtures print no `DUPLICATE INDEX`, and reading that quiet as an answer would have closed this task having fixed one third of it. Give each pruned file one edge to a loaded task and all three fire — so the repair went at the cause, an entitlement that depended on winning a race a *different* check adjudicates. Still fires on a real pasted table, with a count of 3 that shows exactly what is discounted and what is not. |
| 2026-08-21 | (no change) | `specify` needed nothing: the outcome, the scope, four criteria and *no open questions* were written when this was raised on 2026-08-21, and the phase's exit criterion was already met. Recorded rather than passed over silently, so the phase is not read as skipped. `plan` written the same day under the grant below — six steps. **Step 1 comes first because the other two prunings are quiet and that is not evidence**: their fixtures name no loaded id, which is a property of the fixtures and not of the code. The fix in step 2 is aimed at the cause — an entitlement that depends on winning a race a different check adjudicates — rather than at the three shapes, so a fourth pruning cannot reintroduce it. |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** the next steps by the project's own ordering rule, each through its **full lifecycle**. Resolved against `taskmd list --open` on 2026-08-21, the grant is [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), then [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md), then [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) — **these three and no others.** Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **What the grant skips, and why, so nobody reads the order as arbitrary**: T-182, T-199, T-202, T-203 and T-206 each carry a live open question that is the owner's, and T-176 needs an uninvolved reader, who is a person and not a session. T-191 and T-198 are audit umbrellas that close when their children do, so neither is work to start. **This one is second**, being the next by that ordering with no question outstanding. |
| 2026-08-21 | → proposed | Found by [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) on the first run after the owner ruled advisories into the cross-fixture silence assertion — which is the answer paying for itself the day it was given. `medium` and `s`: it is a false positive on an advisory, so it moves no exit status, but a noisy advisory trains a reader to skim the failing lines beside it, which is [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s argument. Not fixed where it was found (METHOD §5). |
