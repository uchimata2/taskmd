---
id: T-062
title: Report two tasks claiming one id instead of dropping one
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-004, T-075]
work_package: M1
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-062 — Report two tasks claiming one id instead of dropping one

## 1. Specify

**Outcome**
Two files claiming the same id are reported by `check`, naming both files, instead of one of them
silently ceasing to exist for every command and every derived view.

**Why this one**
Raised as **F-4** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Shown, not asserted — a three-file project, two of the files carrying
`id: T-001`:

```
taskmd check
OK - 2 task(s), vocabulary valid, references resolve, no broken links
exit=0

taskmd list
T-0001  proposed  -  specify  over-wide id, width is 3
T-001   proposed  -  specify  SECOND file alphabetically
```

Three task files went in; two tasks came out; `check` called it clean. `load_tasks` assigns into a
dict keyed by id, so **walk order decides which file is the task** and the other disappears — from
`list`, from the generated index, from `context`, and from every derived edge on both ends. Nothing
prints a warning and nothing exits non-zero.

**The binding promises the opposite, in terms.**
[`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) *find* says the front-matter is what
is matched, *"so a renamed file is still found and two files claiming one id are a conflict rather
than a coin toss"*. It is a coin toss, decided by `sorted(files)`.

**This is also T-004's open question, already answered by the code.**
[T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) still asks *"What happens on a
merge conflict?"* — and two branches each taking the next free number is precisely how a project
reaches this state. The implementation's current answer is silent data loss, which is the answer
nobody would choose deliberately.

**Why High.** Everything else this audit found costs a reader work; this one loses a task. It is also
the failure shape the project has already named twice as the worst kind — a validator reporting
success over something it never examined ([T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md),
[T-025](T-025-let-check-notice-a-stale-generated-index.md)).

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`); R-13 — a binding's stated guarantee is what an adopter builds on.

**Scope**
- In: a duplicate-id class in `check`, naming the id and every file claiming it.
- In: what `load_tasks` does meanwhile. A reported conflict that still silently picks a winner leaves
  every other command answering from a coin toss.
- In: a `broken-*` fixture holding exactly this defect, per the convention in
  `tests/fixtures/README.md`.
- Out: id **format** and the merge-conflict *policy* — T-004's. This task makes the collision
  visible; it does not decide how a project should recover from one.
- Out: `id_width` enforcement, which is the same function and is
  [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) — deliberately split so each can be
  judged on its own evidence.

**Inputs**
`plugin/taskmd/schema.py` (`load_tasks`, `is_id`), `plugin/taskmd/cli.py` (`cmd_check`),
[`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) *find*,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-4,
[T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md).

**Acceptance criteria**
- [ ] `check` reports two files claiming one id, naming the id and **both** paths, and exits non-zero
- [ ] Shown failing on a fixture first, per R-16
- [ ] A project with no duplicates is unaffected, and the existing fixtures each still report exactly
      one class
- [ ] It is stated what the other commands do while a duplicate exists — whichever answer is chosen,
      the choice is written down rather than left to `os.walk`
- [ ] The binding's *find* sentence is true of the tool afterwards, checked against the sentence

**Open questions**
- ~~**Does anything other than `check` refuse?**~~ **Decided at `plan` on 2026-08-09: nothing
  refuses; every other command warns on stderr and still answers.** R-17 turned out to settle it
  rather than to compete with least-surprise — see §3 D1.

## 2. Plan

Planned **with [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md)**, which that task's §1
asks for: same function, same commit, different evidence. The steps below produce both classes; each
task's record judges its own criteria.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Settle the open question by reading what R-17 actually claims, in the one place it is written as code | The decision in §3 D1 |
| 2 | Build the two `broken-*` fixtures, each holding exactly one defect, per `tests/fixtures/README.md` | `broken-duplicate-id/`, `broken-id-width/` |
| 3 | Run both fixtures against the **pre-fix** tool and record what it says (R-16) | The failing evidence |
| 4 | Give `load_tasks` somewhere to put what it could not load, without changing four command signatures to carry it | `TaskSet`, `Anomaly` in `schema.py` |
| 5 | Report both classes from `check`; warn once on stderr from everything else | `cli.py` |
| 6 | Confirm every existing fixture still reports exactly one class, and that `alt-project` — a different prefix **and** width — is untouched | The per-fixture sweep |
| 7 | Tests: the two classes, and the three properties the stderr line has to have | `tests/test_cli.py` |
| 8 | Make the binding's *find* and *enumerate* sentences true of the tool, checked against the sentences | `plugin/docs/bindings/local-markdown.md` |

**Why step 6 is a step.** Both changes are inside the function every fixture goes through, so the
cheap way to break ten fixtures is to fix two. The sweep is what makes "exactly one class per
fixture" a measured property rather than a convention.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — `check` reports; no other command refuses, and none is silent** — 2026-08-09. The open
  question framed this as R-17 against least-surprise. Reading R-17 where it is actually written —
  `cli.load()`'s own docstring — dissolves the contest: *"a **configuration** problem is reported
  here, when the config is read, and the command never starts. **It is never raised from inside a
  task the user is trying to finish.**"* A duplicate id is task content, not configuration, and the
  second sentence is explicitly about this case. So R-17 does not ask for refusal here; it forbids
  it.

  That leaves the finding's real content, which was never that `check` was wrong — it was that
  **nothing** was. So every other command emits one line on **stderr** and answers as before:
  `stdout` stays byte-for-byte what it was, so a script cutting the tab-separated form or parsing
  `--json` sees exactly what it saw, and R-20's byte-identical claims are untouched.

  *Rejected: refusing to load.* It makes `context T-099` fail because of a collision in two files
  nobody asked about, and it puts a task-content problem in the one place the code reserves for
  configuration.

  *Rejected: `check` alone, with the other commands left silent and merely made deterministic.*
  Cheapest, and it satisfies criterion 4 by writing the choice down. It also leaves the failure
  intact for anyone who does not run `check` — which is the population the finding is about.

  *Rejected: printing the detail on stderr too.* It gives one fact two homes and two formats to keep
  in step. The line points at `check` instead.

- **D2 — the anomalies ride on the returned tasks** — 2026-08-09. `load_tasks` returns a `TaskSet`,
  a `dict` subclass carrying `.anomalies`, so every caller that treats the result as `{id: Task}` is
  unchanged and the four command signatures stay as they were. The alternative was a fifth argument
  threaded through `context`, `index`, `check` and `list` to reach the two places that care.

- **D3 — the walk is sorted, so the winner is reproducible** — 2026-08-09. `dirs[:]` was filtered
  but not sorted, so which file won a collision could differ between machines. It is still a
  collision and it is still reported; this only means one project gives one answer twice. Recorded
  because criterion 4 asks for the choice to be written down rather than left to `os.walk`, and this
  is the half of it that is not about reporting.

### Step 3 — shown failing first (R-16)

Both fixtures against the pre-fix tool, restored from the index for the run:

```
taskmd check --root tests/fixtures/broken-duplicate-id
OK - 1 task(s), vocabulary valid, references resolve, no broken links      exit 0
taskmd list  --root tests/fixtures/broken-duplicate-id
T-001   proposed  -  specify  Second file alphabetically, and the one that used to disappear
```

Two task files went in and one task came out, with `OK` and exit 0 — and note **which** survived:
the *second*, because it overwrote the first. Nothing anywhere named the file that stopped existing.

### Steps 5–6 — after, and the sweep

```
taskmd check --root tests/fixtures/broken-duplicate-id
DUPLICATE ID  T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md. Only the first
              is loaded, so the other is in no view and on no edge
1 problem(s) over 1 task(s)                                                exit 1

taskmd list --root tests/fixtures/broken-duplicate-id
taskmd: 1 problem(s) with the task files - run 'taskmd check'   [stderr]
T-001   proposed  -  specify  First file alphabetically, and the one that loads
```

Every fixture, one class each — the sweep that stops a fix inside `load_tasks` breaking ten
projects to mend two:

```
broken-config            CONFIG ERROR
broken-cycle             CYCLE
broken-dangling          DANGLING
broken-deliverable       MISSING OUTPUT
broken-derived-field     STORED DERIVED
broken-duplicate-id      DUPLICATE ID
broken-hook              CONFIG ERROR
broken-id-width          ID WIDTH
broken-link              BROKEN LINK
broken-missing-blocker   NO BLOCKER
broken-tasks-dir         CONFIG ERROR
broken-vocabulary        VOCABULARY

taskmd check --root tests/fixtures/alt-project   OK - 3 task(s), ...   (ISSUE-, width 4)
taskmd check --root tests/fixtures/ordering      OK - 4 task(s), ...
taskmd check                                     OK - 76 task(s), ...
```

### Step 8 — the binding

*find*'s sentence — *"two files claiming one id are a conflict rather than a coin toss"* — needed no
change and is now true: it is a reported conflict, and the pick is sorted rather than tossed.
*enumerate* gained the half it never stated, which is what the two files that **leave** the step
without becoming a task do, and that neither may do so quietly.

**Outputs produced**
- `plugin/taskmd/schema.py` — `TaskSet`, `Anomaly`, and a `load_tasks` that records instead of losing
- `plugin/taskmd/cli.py` — `check_anomalies`, and the stderr line in `main`
- `tests/fixtures/broken-duplicate-id/` — two files, one id
- `tests/test_cli.py` — the class, plus `ADuplicateIsNeverSilent`
- `plugin/docs/bindings/local-markdown.md` — *enumerate*
- `tests/fixtures/README.md` — the two new rows and what makes them different from the rest

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `check` reports two files claiming one id, naming the id and **both** paths, and exits non-zero | met | §3 step 5. Paths are printed repo-relative through `rel()`, as every other class does, so no machine path reaches output |
| Shown failing on a fixture first, per R-16 | met | §3 step 3 — `OK - 1 task(s)`, exit 0, and the survivor was the file that overwrote the other |
| A project with no duplicates is unaffected, and the existing fixtures each still report exactly one class | met | §3 step 6 — twelve fixtures, twelve single classes, and this repository still `OK - 76 task(s)` |
| It is stated what the other commands do while a duplicate exists | met | D1 and D3, and asserted three ways in `ADuplicateIsNeverSilent`: `list` still answers, its stdout carries no warning, and `check` does not tell you to run `check` |
| The binding's *find* sentence is true of the tool afterwards, checked against the sentence | met | Checked against it and unchanged — the sentence was already right and the tool was wrong. *enumerate* is where the new behaviour is written |

**Child fix tasks raised**
- none. Implemented alongside [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) as that
  task's §1 asked; the two records judge their own criteria against the same commit.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met. The open question dissolved rather than being decided: R-17 is written as code in `cli.load()`'s docstring, and its second sentence — *never raised from inside a task the user is trying to finish* — is explicitly about this case, so R-17 forbids the refusal it looked like it demanded. What was left is that the finding was never about `check` being wrong but about **nothing** being wrong, so every other command now warns once on stderr and answers exactly as before, stdout byte-for-byte untouched. Two things worth knowing beyond the fix: the pre-fix survivor of a collision was the file that *overwrote* the other, and the walk was unsorted, so which task vanished could differ between machines. |
| 2026-08-09 | → in_progress | Planned with T-075 as its §1 asked — same function, same commit, two records. The step that earns its place is the per-fixture sweep: both changes live inside the function every fixture goes through, so the cheap way to break ten projects is to mend two. Twelve fixtures, twelve single classes. The anomalies ride on a `dict` subclass rather than a fifth argument through four commands, which is what kept an `s` an `s`. |
| 2026-08-09 | → specified | Criteria stand as raised. The open question is a `plan` question and names the two principles it is between, so nothing needed the owner beyond the authorisation to run the lifecycle. |
| 2026-08-09 | → proposed | Raised as F-4 from the T-059 audit, clauses 1 and 3. Reproduced before write-up on a scratch project outside the repository: three task files, `OK - 2 task(s)`, exit 0, and the loser gone from every view. `high` because it is the only finding in the set that loses data rather than costing a reader time, and because the binding states the opposite guarantee in terms. Related to T-004, whose open merge-conflict question the implementation currently answers by dropping a task. |
