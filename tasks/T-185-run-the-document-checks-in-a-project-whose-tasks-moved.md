---
id: T-185
title: Run the document checks in a project whose tasks moved
type: fix
status: done
phase: review
parent: T-177
blocked_by: []
related: [T-095, T-108, T-178]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-18
updated: 2026-08-19
adopter_visible: yes
deliverables: [plugin/skills/taskmd/taskmd/schema.py, plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-185 — Run the document checks in a project whose tasks moved

## 1. Specify

**Outcome**
`check` in a migrated project reports what it can still check, refuses only what needs a task file,
and says plainly that the task half was not examined.

**Why this one**
[T-177](T-177-run-the-checks-that-need-no-task-folder.md) ruled that it should, and measured what it
buys: two dead links and a config advisory in a migrated project that today gets `CONFIG ERROR` and
exit 2. The ruling, its three rejections and the evidence are there and are not repeated here.

**The ruling is conditional, and the condition is the risky half.** T-177 answered *no, a
document-only pass does not mislead* **only** on the basis that the `Scope` line gains what it
currently has no words for. As it stands the line says *every document read*, which is true and reads
as *everything checked* — to a reader who has just been handed real defects. Shipping the first half
without the second turns a refusal into a false assurance, which is worse than the behaviour it
replaces.

**Scope**
- In: moving the `tasks_dir` guard so the five no-`tasks` checks run when `id_width: none`.
- In: the `Scope` line saying the task half was not checked, and why.
- In: the exit status for such a run.
- Out: a mistyped `tasks_dir`. It keeps refusing — T-177 part 2.
- Out: a fifth command or a `--documents-only` flag. Both rejected by T-177.
- Out: re-opening the ruling.

**Inputs**
- [T-177](T-177-run-the-checks-that-need-no-task-folder.md) §3 — the ruling in three parts
- `plugin/skills/taskmd/taskmd/schema.py` — `_check_tasks_dir`, and `load_schema` which calls it
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_check` and the five signatures without `tasks`
- `tests/fixtures/migrated-away/` — **which holds a config and no documents**, and so cannot test
  this. T-177 had to build one; this task needs the fixture to grow or a sibling beside it
- [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) — the `Scope` line's own task

**Acceptance criteria**
- [ ] A migrated project reports document-level problems that a clean one does not — shown by a
      fixture carrying a real defect, failing before the fix
- [ ] A mistyped `tasks_dir` still exits 2 with the message it has today, proven by the existing
      `broken-tasks-dir` fixture still passing
- [ ] The output states that the task half was not checked, in a form a reader meets without looking
      for it. A run whose only signal is the absence of task counts does not satisfy this
- [ ] The exit status for a clean document-only run is stated and justified — a pass is not obviously
      right when a third of the validator did not run
- [ ] The `migrated-away` fixture holds documents, so this behaviour is testable at all
- [ ] No new command and no new flag

**Open questions**
- ~~**What exit status does a clean document-only run take?** `0` reads as validated and is what
  criterion 4 is suspicious of; a distinct non-zero code says *incomplete* but makes every migrated
  project's gate red for ever. T-177 did not settle this and marked it out of its own scope.~~
  **Answered by the owner on 2026-08-19: exit `0`, and the run states what it skipped** — see the
  Log row of that date for the rejected option and its cost.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give `migrated-away` documents, one carrying a real dead link and one whose link resolves | `tests/fixtures/migrated-away/docs/` |
| 2 | Write the tests, including the `Scope` one and the must-not-fire one, and show them failing | The failing run, in §3 |
| 3 | Move the guard: the loader returns the error instead of raising it, in the migrated case only | `schema.py` |
| 4 | Split `cmd_check` on that, and write the `Scope` note before any check runs | `cli.py` |
| 5 | Keep the other three commands' output identical, message and exit status | `cli.py`, and the T-164 test |
| 6 | Run the suite, `check` and `index` | The output, in §3 |

**Decisions taken at `plan`**

- **The loader returns the error rather than a boolean.** The message is built in one place and used
  by both paths, so the `Scope` note and the `CONFIG ERROR` line cannot drift apart. *Rejected: a
  `migrated` flag with the message rebuilt at the command layer*, which is a second home for a
  sentence T-164 argued over. — 2026-08-19
- **The `Scope` note is written before any check runs, not appended if something is found.** It is
  the condition the ruling was granted on, and a note that only appears sometimes is a note a reader
  cannot rely on. — 2026-08-19
- **The T-164 test is edited, not deleted.** Its subject — the third remedy in the message — is
  untouched by this task; what changes is which commands say it. Editing it keeps the assertion that
  matters and records the behaviour change in the same place somebody will look. — 2026-08-19

**Outputs this task will produce**

- plugin/skills/taskmd/taskmd/schema.py
- plugin/skills/taskmd/taskmd/cli.py
- tests/fixtures/migrated-away/docs/
- tests/test_cli.py

## 3. Implement

### Steps 1–2 — the fixture, and the tests failing first

`migrated-away` held a config and nothing else, which §1 already named as the reason it could not
test this. It now holds two documents: one with a dead link on purpose, and one whose link resolves
and **must not** be reported — the must-not-fire case
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) ruled on hours earlier, in
its first use since.

Seven tests, run before any code changed:

```text
Ran 7 tests ... FAILED (failures=5)
AssertionError: [] is not true : CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but the
project root has no such folder. ...
```

Five failed and **two passed**, and the two are the ones asserting that `index`, `context` and a
mistyped `tasks_dir` keep refusing. That is the right shape for a change that must move one
behaviour and leave three alone.

### Steps 3–5 — the guard, moved

`_check_tasks_dir` now **returns** the error in exactly one case — folder absent *and*
`id_width: none` — and raises in every other. `load_schema` hangs it on the schema as
`tasks_unreadable`; `cmd_check` splits on it; `main` prints it and exits 2 for the other three
commands. The message is constructed in one place and neither path can drift from the other.

### Step 6 — what it does

```text
BROKEN LINK   docs/guide.md -> plan.md

1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), 0 template(s), 0 template field value(s), 1 vocabulary row(s)
CONFIG DRIFT  status: shipped default adds ...; this project's row does not carry them
Scope  no task file was read, and the checks that open one did not run. .taskmd/config.md: tasks_dir is 'tasks', but the project root has no such folder. Create it, or correct tasks_dir. Or nothing here is broken and these commands do not apply: id_width is 'none', ...
Scope  0 document(s) not read: a clone would not receive them
EXIT=1
```

**The summary carries no `task(s)` denominator**, which is [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)'s
design doing its job without being asked: the narrowed scan reports a smaller set of nouns rather
than reporting zeros for things it never opened. A run printing `0 task(s)` here would be the exact
false assurance T-177 made its ruling conditional on avoiding.

### The suite, and the thing it caught

```text
Ran 295 tests in 22.593s
OK
```

**One failure before that**, and it is the same class as T-184's earlier the same day:
`README.md`'s quoted `check` transcript stopped matching, because moving three checks out of the
task branch changed the order the denominators merge in — `closed record(s)` moved ahead of
`document(s)`. Regenerated by running the command the test runs.

`index` and `check` on this repository are clean, and `check` here still reports 15 nouns because
nothing about an ordinary project changed.

**Decisions & assumptions**

- All three `plan` decisions held. — 2026-08-19
- **Exit `0` on a clean document-only run**, per the owner's answer of 2026-08-19, with the honesty
  carried by the `Scope` line. *Rejected: a distinct non-zero code*, whose cost that row records —
  a permanently red gate is a switched-off gate. — 2026-08-19
- **Twelve checks moved into the task branch, not eleven.** `check_label_shape` and
  `check_duplicate_index` take `tasks` and are advisories; they went with the twelve because the
  question is what they read, not how loudly they report. — 2026-08-19
- **Assumption, recorded as one**: the five document checks are the whole no-`tasks` set, read from
  their signatures rather than from any document. T-177 recorded the same assumption on 2026-08-18
  and this run re-derived it rather than inheriting it. — 2026-08-19

**Outputs produced**
- plugin/skills/taskmd/taskmd/schema.py
- plugin/skills/taskmd/taskmd/cli.py
- tests/fixtures/migrated-away/docs/guide.md
- tests/fixtures/migrated-away/docs/notes.md
- tests/test_cli.py
- README.md — the quoted sample run

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A migrated project reports document problems a clean one does not, shown by a fixture failing first | **met** | §3 steps 1–2. Five of seven tests failed on the unchanged tree, and `BROKEN LINK docs/guide.md -> plan.md` is what the fixture now produces |
| A mistyped `tasks_dir` still exits 2 with today's message | **met** | `broken-tasks-dir` still passes, and `test_a_mistyped_tasks_dir_still_refuses` asserts it directly rather than relying on the older test still being green |
| The output states the task half was not checked, met without looking for it | **met** | The `Scope` line, written before any check runs. It carries the loader's own sentence, so the reason is there and not only the fact |
| The exit status is stated and justified | **met** | `0`, per the owner's ruling, with the rejected option and its cost in §3. `test_a_clean_document_only_run_exits_zero` holds it |
| The `migrated-away` fixture holds documents | **met** | Two, and the second exists to stay quiet — the negative case T-151 ruled on the same day |
| No new command and no new flag | **met** | The change is where one guard sits, what one line says, and which branch three checks are in. `COMMANDS` and `LIST_OPTIONS` are untouched |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner on 2026-08-19 and is struck through there. Nothing here
is addressed to anyone else.

**T-177's condition is met, and it is worth saying which half was the risky one.** The loader change
took three lines and the `Scope` line took one. The condition was never about difficulty; it was
that shipping the first without the second turns a refusal into a false assurance, and the two are
in the same commit.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 7 of the eight. **`check` in a migrated project now reads its documents**: the loader returns the `tasks_dir` error instead of raising it, in the one case where the folder is absent *and* `id_width: none` says a backend allocates the ids, and `cmd_check` runs the five checks that never open a task file. The other three commands print the same message and exit 2 as before, and a mistyped `tasks_dir` still refuses — which is T-177 part 2 and the reason the ruling is not *run the five whenever the folder is missing*. **T-177's condition ships in the same commit**: the `Scope` line says the task half was not read and carries the loader's own sentence for why, and it is written before any check runs rather than appended. The summary carries no `task(s)` denominator, which is T-095's design refusing to report zeros for something never opened. Exit 0 on a clean run, per the owner. Written test-first: five of seven tests failed on the unchanged tree, and the two that passed were the ones asserting the three unchanged behaviours. |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 7 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). Its dependency on T-177's loader change is inside the grant: §1 requires the loader and the `Scope` line to ship together, and both are this task's. |
| 2026-08-19 | (no change) | **The one open question is answered by the owner: exit `0`, with the run stating what it skipped.** Asked in the backlog-wide round of 2026-08-19. *Rejected: a distinct non-zero code.* It would make the status itself say *incomplete*, which is the honest reading, but it turns every migrated project's gate red permanently — and a gate that is always red is switched off or ignored, which loses more than a mis-read `0` does. *Rejected: holding this task until T-177's condition ships*, which would have left the question open rather than settled. The honesty therefore has to live in the `Scope` line, which T-177 §3 part 3 already requires; that requirement is now load-bearing rather than supporting, and `specify` writes a criterion for it. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-177](T-177-run-the-checks-that-need-no-task-folder.md)'s review. **Carries T-177's condition as its own risk**: the loader change without the `Scope` change is a false assurance, so the two ship together or not at all. One genuinely open question — the exit status of a clean document-only run — which is why this is not simply the code T-177 declined to write. Outside the standing grant of 2026-08-18, which covers the six named tasks and nothing any of them raises. |
