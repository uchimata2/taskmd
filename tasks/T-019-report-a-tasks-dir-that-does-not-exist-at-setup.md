---
id: T-019
title: Report a tasks_dir that does not exist at setup
type: fix
status: done
phase: review
parent: T-002
blocked_by: []
related: [T-003, T-006, T-023, T-024]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-05
updated: 2026-08-05
deliverables:
  - plugin/taskmd/schema.py
  - plugin/taskmd/defaults/config.md
  - tests/test_cli.py
  - tests/fixtures/broken-tasks-dir/.taskmd/config.md
  - tests/fixtures/README.md
---

# T-019 — Report a tasks_dir that does not exist at setup

## 1. Specify

**Outcome**
A config whose `tasks_dir` names a folder that is not there fails when the config is read, naming
the key and the path — instead of yielding a project with no tasks in it. The rule is
unconditional: it does not matter whether the value was written by the project or inherited from
the shipped default, so a project adopting taskmd is told to create the folder rather than having
one made for it by a side effect of `index`.

**Why this one**
Found in T-002's review, by testing the half of class 8 that `implement` had not demonstrated. A
config key can be misspelled, and so can a key's **value**; only the first is caught. With
`tasks_dir: taks` against a real `tasks/` folder holding one task:

```
check            exit 0 | OK - 0 task(s), vocabulary valid, references resolve, no broken links
context T-001    exit 1 | No such task: T-001
index            exit 0 | Wrote taks/README.md - 0 active, 0 closed
```

Three separate failures, and the first is the worst: **`check` returns success on a project it
never read.** A validator that says OK because it found nothing to look at is worse than no
validator, because it is trusted. `context` then reports the problem exactly where R-17 says it must
not — inside a task the user is trying to start, phrased as though the task were missing. And
`index` silently creates the misspelled folder, so the mistake acquires a plausible-looking
artefact.

**A second case, found while re-running the reproduction.** With the *shipped default* config and no
`tasks/` folder at all — a project that has just adopted taskmd — the output is identical:

```
check            exit 0 | OK - 0 task(s), vocabulary valid, references resolve, no broken links
index            exit 0 | Wrote tasks/README.md - 0 active, 0 closed   (and creates tasks/)
```

The two cases are indistinguishable in code: both are `tasks_dir` naming a folder that is not
there. So the fix cannot catch the typo without also catching the fresh project, and `index`
creating the folder is currently the only thing standing in for an `init` command that non-goal 11
rules out. Whether that is a bug or the adoption path is the owner's call — see *Open questions*.

**Requirements served**
R-17 (`docs/SCOPE.md`).

**Scope**
- In: `tasks_dir` resolving to nothing. *Assumption:* it is the only config value naming a
  filesystem path today, so the rule is written for path-valued keys generally but has exactly one
  subject; if another is added later it inherits the rule rather than needing this task reopened.
- In: what taskmd tells a project that has adopted it but has no tasks folder yet (the second case
  above), because the same code decides both.
- Out: a genuinely empty tasks folder, which is legitimate and must stay legal — the distinction is
  *the folder is absent*, not *the folder has no tasks in it*.
- Out: an `init` command or any fourth command (`docs/SCOPE.md` non-goal 11). Whatever the fresh
  project is told, it is told by one of the three that exist.

**Inputs**
`taskmd/schema.py` (`load_schema`, `load_tasks`), `docs/SCOPE.md` R-17, T-002 §4.

**Acceptance criteria**
- [ ] A `tasks_dir` that does not exist is an error naming the key and the path, raised when the
      config is read — not on first use, and not by any of the three commands individually
- [ ] `check` cannot exit 0 on a project whose task folder was never found
- [ ] `index` does not create the folder named by a mistyped value
- [ ] An existing but **empty** tasks folder is still legal and still exits 0
- [ ] A project with no tasks folder at all is the *same* error, whether `tasks_dir` came from a
      project config or the shipped default, and all three commands agree — none exits 0
- [ ] The error says what to do about it, since for a new project creating the folder is the
      correct response and there is no command that will do it
- [ ] Shown failing per R-16, on all three cases above — typo'd value, absent folder,
      present-but-empty folder — each carried by a committed fixture **or, where git cannot store
      one, by a case the test builds and the fixture README names**
      <br>*Amended 2026-08-05 by the owner. Original: "Shown failing on a fixture, per R-16 — the
      fixture covers all three cases above: typo'd value, absent folder, present-but-empty folder."
      The original demanded a committed fixture for a case that cannot have one: a project with
      neither a config nor a tasks folder is an empty directory, and git stores no such thing. Kept
      per [`review`](../plugin/docs/method/review.md) — the original text is the record, the amendment is
      what a future author is held to. Amended rather than left as a review footnote because R-16
      will be cited by every future validator task, and a criterion demanding the impossible would
      be either violated or re-argued each time.*

**Open questions**
- none. **Q1 — a project with no tasks folder yet: error, or tolerated? — answered by the owner
  on 2026-08-05: error, always.** A conditional rule would need the loader to know whether a value
  was written or inherited, and would re-admit `check` exiting 0 on a project it never read, which
  is the failure this task exists to remove. The adopter creates the folder once; the skill names
  that step. `index` creating the folder it writes into is withdrawn as an adoption path.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the three cases **before** the fix, as `tests/fixtures/README.md` says the `broken-*` set was written before `check` existed. The typo'd value gets a committed fixture; the absent-folder case cannot have one, because a project with no config and no tasks folder is an empty directory and git stores no such thing — that case is built in a temp directory by the test. | `tests/fixtures/broken-tasks-dir/` (a config naming `taks`, beside a real `tasks/` holding one task), its row in `tests/fixtures/README.md`, and three tests in `tests/test_cli.py` — typo'd value, absent folder under the shipped default, present-but-empty folder — all three run against **all three commands**, and all failing |
| 2 | Settle the error's exit code, label and wording. Exit 2 under the `CONFIG ERROR` label is the existing shape for a config that cannot be trusted (`cli.main`), and it is what makes "all three commands agree" fall out rather than needing to be arranged. The wording has to carry the value's provenance: naming `taskmd/defaults/config.md` at someone who never wrote a config would be true and useless. | A decision recorded in §3, with the rejected alternatives and why |
| 3 | Add the existence check to `load_schema`, **after** the existing key and table validation. Ordering is the decision, not an implementation detail: a config that is both malformed and points at a missing folder must be reported as malformed, and ~20 `SchemaError` tests build a project from a config alone with no tasks folder — they keep passing only if the earlier errors still win. | The change in `taskmd/schema.py`, and the ordering stated in §3 |
| 4 | Sweep the suite for anything that builds a project without a tasks folder and expects it to load. Ordering (step 3) is expected to spare the `reject` helper; expected is not verified, and the number found is the point of the step. | The updated tests, and the count recorded in §3 — including zero, if that is the answer |
| 5 | Annotate `tasks_dir` in the default config: the folder must exist, and creating it is the adopter's one setup action, since non-goal 11 leaves no command to do it. | The annotated key and its paragraph in `taskmd/defaults/config.md` |
| 6 | Run the three commands against all three cases, plus the full suite, and paste the actual output — not "passes". | The before/after transcript in §3, and the suite count |

**Deliverable shape — decided here.** The check goes in `load_schema` rather than in `cli.load()`
or `load_tasks`. `cli.load()` was rejected because `python -m taskmd.schema` and any future binding
reach the schema without going through the CLI, and the guarantee would not hold for them.
`load_tasks` was rejected outright: it is first use, which is the thing R-17 forbids and the
acceptance criteria name explicitly.

**Not in this task.** Telling a new adopter to create the folder belongs to whoever writes the
skill (T-003) and the README (T-006); both now carry a soft edge to this task so the instruction
lands there rather than being invented twice. This task's own doc change is the config annotation
in step 5.

**Output paths**

- `taskmd/schema.py`
- `taskmd/defaults/config.md`
- `tests/test_cli.py`, `tests/test_schema.py` (step 4, if the sweep finds anything)
- `tests/fixtures/broken-tasks-dir/` and `tests/fixtures/README.md`

The `deliverables:` front-matter field stays empty until `implement`: `check` validates that every
declared path exists, so declaring them now would make this project fail its own validator for the
length of the plan.

## 3. Implement

**Decisions & assumptions**
- **The check lives in `load_schema`, and runs last** — 2026-08-05. Last is the load-bearing half:
  a config that is both malformed and points at a missing folder is reported as malformed, which is
  what keeps the 20 `RejectsBadConfig` tests meaningful — they each build a project from a config
  file alone, with no tasks folder, so any earlier position would have replaced 20 specific
  diagnoses with one generic one.
- **Exit 2 under `CONFIG ERROR`** — 2026-08-05. Not a new code path: `cli.main` already turns a
  `SchemaError` into exactly that, before any command runs. Choosing the existing shape is what
  makes "all three commands agree" a consequence rather than something to arrange, and it is why
  no change to `cli.py` was needed at all.
- **The message names the configured value, not the resolved path** — 2026-08-05. `tasks_dir is
  'taks'` rather than the `os.path.join` of root and value. The value is the thing the user can
  act on; the join is machine-specific, and R-20 asks for identical output everywhere. Rejected:
  printing both, which doubles the length of the line for the reader who needs it least.
- **The message carries the value's provenance** — 2026-08-05. A project that wrote its own config
  is told to fix it; a project with no config is told that the value came from the shipped default
  and that creating the folder is the fix. Naming `taskmd/defaults/config.md` at someone who never
  wrote a config would be true and useless.
- **The empty-folder case was already legal and was left alone** — 2026-08-05. `os.path.isdir` is
  the whole distinction; no code was needed for the third case, and its test passed before the fix
  as well as after, which is the evidence that the fix did not narrow what is legal.

**Escalated, not fixed here**
- [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) — a config error against
  the shipped default prints the absolute install path, because `DEFAULT_CONFIG` is built from
  `os.path.abspath(__file__)`. Visible in the case-B transcript below. It is **older than this
  task** and affects every config error, but this task is what puts it in front of a new user, so
  it is raised rather than absorbed (METHOD §3.3).

**Outputs produced**
- `taskmd/schema.py` — `_check_tasks_dir`, called last from `load_schema`
- `taskmd/defaults/config.md` — `## The tasks folder`, and the annotation on the key
- `tests/test_cli.py` — `AbsentTasksDirIsReportedAtSetup`, three cases against all three commands
- `tests/fixtures/broken-tasks-dir/` — the misspelled-value fixture
- `tests/fixtures/README.md` — the row, and why one of the three cases has no committed fixture

**Verification**

The negative cases were written first and run before the fix. Both failed, in the way the task was
raised for — `check` exiting 0 on a project it never read:

```
FAIL: test_a_misspelled_value_beside_the_real_folder
AssertionError: 0 != 2 : check exited 0:
OK - 0 task(s), vocabulary valid, references resolve, no broken links

FAIL: test_a_project_that_has_not_created_the_folder_yet
AssertionError: 0 != 2 : check exited 0:
OK - 0 task(s), vocabulary valid, references resolve, no broken links

Ran 3 tests — FAILED (failures=2)
```

The third case passed before the fix and after it, which is the point of including it.

After the fix, all three commands on all three cases:

```
A) tasks_dir: taks  (project config, real tasks/ next door)
  check          exit 2 | CONFIG ERROR  ./.taskmd/config.md: tasks_dir is 'taks', but the project
                          root has no such folder. Create it, or correct tasks_dir.
  context T-001  exit 2 | (same)
  index          exit 2 | (same)
   folder 'taks' created: False

B) shipped default, project with no tasks/ folder
  check          exit 2 | CONFIG ERROR  <install path>/taskmd/defaults/config.md: tasks_dir is
                          'tasks', but the project root has no such folder. This project has no
                          .taskmd/config.md, so taskmd is using its shipped default; create the
                          folder, or write a config naming a different one.
  context T-001  exit 2 | (same)
  index          exit 2 | (same)
   folder 'tasks' created: False

C) tasks_dir: tasks, folder exists but EMPTY
  check          exit 0 | OK - 0 task(s), vocabulary valid, references resolve, no broken links
  index          exit 0 | Wrote tasks/README.md - 0 active, 0 closed
```

`<install path>` is the literal absolute path in the real output — that is T-023, quarantined here
rather than reproduced.

Suite: **74 tests, 74 pass**, up from 71. Step 4's sweep found **zero** tests needing a change: the
ordering decision above is what spared them, and the count is recorded because "expected to be
spared" is not the same as checked.

This repository, which is a taskmd project with a real `tasks/`, is unaffected:

```
python -m taskmd check
OK - 23 task(s), vocabulary valid, references resolve, no broken links
```

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Error names the key and the path, raised when the config is read — not on first use, not by any of the three commands individually | met | The check is in `load_schema`, so it fires for callers that never touch the CLI: `python -m taskmd.schema` on the fixture reports the same sentence (`SCHEMA ERROR: ... tasks_dir is 'taks' ...`, exit 1). "The path" is the configured **value**, not the resolved absolute path — a deliberate `implement` decision, recorded there, taken for R-20 |
| `check` cannot exit 0 on a project whose task folder was never found | met | Was the raising failure. Exit 2 on both the misspelled value and the absent folder; shown failing at exit 0 before the fix, transcript in §3 |
| `index` does not create the folder named by a mistyped value | met | `folder 'taks' created: False`. Review also ran the neighbour the plan did not: `tasks_dir: docs/tasks` where `docs/` exists and the leaf does not — exit 2, `docs/tasks` not created, so it is not merely `makedirs` declining a two-level path |
| An existing but **empty** tasks folder is still legal and exits 0 | met | Passed before the fix and after — the same test, unchanged, either side. That is what shows the fix narrowed nothing |
| A project with no tasks folder at all is the same error whichever way the value arrived, and all three commands agree — none exits 0 | met | Both cases exit 2 from all three commands. Agreement is structural rather than arranged: `cli.main` already routed `SchemaError` to `CONFIG ERROR` / exit 2 before any command runs, which is why `cli.py` was not touched |
| The error says what to do about it | met | Two hints, chosen on provenance: "Create it, or correct tasks_dir" for a project config; for the shipped default, that the value was inherited and a config may be written instead. Judged on the text, not on a user — no uninvolved reader was available, which is a weaker proof than `implement`'s |
| Shown failing per R-16 on all three cases, each carried by a committed fixture or a test-built case the fixture README names | met | All three cases were shown, and the two negative ones shown *failing* first (§3). Only one is a committed fixture: a project with neither a config nor a tasks folder is an empty directory, which git cannot store, so that case is a temp directory built by the test, and `tests/fixtures/README.md` says so. The criterion was written before `plan` found that constraint and read "the fixture covers all three cases"; **the owner amended it on 2026-08-05** — original text kept in §1, per [`review`](../plugin/docs/method/review.md). Nothing about the outcome changed |

**Also checked, beyond the criteria**

- The new fixture reports **only** its own class — one line of output, none of the other seven
  labels — which is the property `tests/fixtures/README.md` asserts of every fixture.
- Suite 74/74; `check` clean on this repository, 23 tasks; pre-publish check unchanged at five
  hits, all in T-013's fixture (T-018's, not new).

**Child fix tasks raised**
- none — every criterion is met.

**Raised, not fixed here** (outside these criteria, so not child fixes — METHOD §3.3)
- [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) — raised during
  `implement`; the shipped-default error prints the absolute install path.
- [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md) — raised here.
  `tasks_dir` pointing at a **file** is correctly rejected, but the message says the project root
  "has no such folder" while the name is sitting there. Low value; recorded so it is not lost.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Raised by T-002's review against criterion 6 and class 8. `implement` proved the unknown-key half of that class and not the missing-file half; the review tested the untested half and it failed. |
| 2026-08-05 | (no status change) | Criterion 7's wording amended by the owner, closing the one item this task left open. It now accepts a test-built case where git cannot store a fixture; the original text is kept beside it and the §4 row reads plainly *met*. Chosen over leaving a footnote because R-16 is cited by every future validator task, and a criterion demanding a committed fixture for an empty directory would be re-argued each time. No code, test or output changed. |
| 2026-08-05 | → done | Review worked. All seven criteria met, no child fixes. Review exercised three neighbours `implement` had not: the non-CLI entry point (`taskmd.schema` reports the same sentence, so the check really is at config read), a nested `tasks_dir` whose leaf is missing, and `tasks_dir` naming a file — the last is correctly rejected with a misleading sentence → T-024, raised not fixed. Criterion 7's wording was overtaken by a git constraint the plan found; recorded openly rather than ticked, and the text is the owner's to amend. |
| 2026-08-05 | → review | Implemented in plan order. `cli.py` needed no change — reusing the existing `SchemaError` → exit 2 path made "all three commands agree" fall out. Negative cases were written and run first: both failed with `check` exit 0, the failure the task was raised for. Suite 71 → 74, all passing; the step 4 sweep found zero tests to update. One thing escalated rather than absorbed: the shipped-default config error prints the absolute install path, which is older than this task but newly in front of new users → T-023. |
| 2026-08-05 | → planned | Six steps, negative cases first per the `broken-*` precedent. Two things the code decided rather than the plan: the check belongs in `load_schema` (the CLI is not the only caller), and it must run *after* the existing validation, because the `SchemaError` suite builds projects from a config alone. Soft edges added to T-003 and T-006 — the "create the folder" instruction is theirs to carry, and prose in this plan would have been invisible to them. |
| 2026-08-05 | → specified | Specify agreed by the owner. Reproduction re-confirmed on a fresh fixture, which turned up a second case sharing the same code path: the shipped default config on a project with no `tasks/` folder behaves identically, and `index` creating that folder was the de-facto `init`. Q1 settled it as one unconditional rule — absent is an error however the value arrived — which widened the scope and added two criteria (consistency across the three commands, and an error that says what to do). |
