---
id: T-024
title: Say so when tasks_dir names something that is not a folder
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-019, T-023]
work_package: M2
owner: maintainer
business_value: low
effort: xs
created: 2026-08-05
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/schema.py, tests/test_cli.py, tests/fixtures/README.md, tests/fixtures/broken-tasks-dir-file/.taskmd/config.md]
adopter_visible: yes
---

# T-024 — Say so when tasks_dir names something that is not a folder

## 1. Specify

**Outcome**
When `tasks_dir` names a path that exists but is not a directory, the error says that, instead of
telling the reader there is no such folder while the name sits in front of them.

**Why this one**
Found in [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md)'s review, by testing a
neighbour that task's plan had not: `tasks_dir: tasks` where `tasks` is a **file**.

```
check   exit 2 | CONFIG ERROR  ./.taskmd/config.md: tasks_dir is 'tasks', but the project root
                 has no such folder. Create it, or correct tasks_dir.
```

The rejection is right — `os.path.isdir` is the correct test and this is not a usable tasks folder.
Only the sentence is wrong, and it is wrong in the direction that costs the most: it denies the
existence of something the reader can see, and then advises creating it, which will fail. The
remedy the message gives cannot be followed.

This is **low value** and is recorded as such. The case is rare, nothing depends on it, and it is
one sentence of code. It is a task rather than a note because METHOD §3.3 leaves no third option
for something actionable and out of scope, and a note in a closed task is how observations get lost.

**Requirements served**
R-17 (`docs/SCOPE.md`) — the same requirement T-019 serves, at the granularity of what the message
actually tells the user.

**Scope**
- In: the wording of `_check_tasks_dir` when the path exists but is not a directory.
- Out: the test itself. `isdir` is correct and stays; this is not a proposal to accept a file.
- Out: the absolute-install-path prefix, which is [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md).

**Inputs**
`plugin/skills/taskmd/taskmd/schema.py` (`_check_tasks_dir`), T-019 §4. *(The path was written as
`taskmd/schema.py`; the package moved under `plugin/skills/taskmd/` in T-083, and this is the
present-tense pointer being corrected, not the record of where it was.)*

**Acceptance criteria**
- [ ] A `tasks_dir` naming a file is reported as "not a folder", not as "no such folder"
- [ ] The advice given matches the case — it does not tell the reader to create a name that is
      already taken
- [ ] The absent-folder case is unchanged, and T-019's tests still pass untouched
- [ ] Shown failing on a fixture, per R-16

**Open questions**
- none.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the case as a committed fixture — a project whose `tasks_dir` names a file that is there — and run the three commands on it before changing anything. | `tests/fixtures/broken-tasks-dir-file/`, and the wrong message recorded in §3 |
| 2 | Split the message on `os.path.exists`, so the sentence and the remedy both follow the case. | `_check_tasks_dir` in `plugin/skills/taskmd/taskmd/schema.py` |
| 3 | Add the new case to `AbsentTasksDirIsReportedAtSetup`, through the same `all_three_commands_refuse` helper the absent cases use. | A test in `tests/test_cli.py` |
| 4 | Give the fixture its row in the negative-case table, and say what its one defect is. | `tests/fixtures/README.md` |
| 5 | Run the three commands on the fixture, then `check`, `index` and the suite. | Recorded output |

**Shape decisions.**

**D1 — The case is split on `os.path.exists`, not on `os.path.isfile`.** What the reader needs to be
told apart is *there is nothing here* from *there is something here and it is not a folder*; `exists`
is that question. `isfile` would answer a narrower one and leave anything that is neither file nor
directory falling back to the sentence this task exists to remove.

**D2 — Both hints move, not just the project-config one.** The inherited-default hint ends "create
the folder, or write a config naming a different one", which is the same unfollowable advice one
sentence longer. A fix that corrected only the case the bug report happened to use would leave the
defect intact for a project that has not written a config — the likelier of the two, since it is the
shipped `tasks` value that collides with an existing name.

**D3 — A committed fixture, even though the case can be built in a temp directory.** R-16 is about
`check` having been *seen* to fail on each class, and the class already has a committed negative case
for its neighbour. The middle case in `AbsentTasksDirIsReportedAtSetup` has no fixture because git
cannot store an empty directory; that reason does not apply here, so the exception should not spread
by imitation.

**Planned outputs**
- tests/fixtures/broken-tasks-dir-file/
- plugin/skills/taskmd/taskmd/schema.py
- tests/test_cli.py
- tests/fixtures/README.md

## 3. Implement

### Step 1 — the wrong message, reproduced before anything changed

`tests/fixtures/broken-tasks-dir-file/` is a config naming `tasks_dir: tasks` beside a `tasks` that
is a file. All three commands, before the fix:

```text
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but the project root has no such folder.
              Create it, or correct tasks_dir.
exit 2
```

### Steps 2–3 — the split, and both hints

```text
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but that name is a file, not a folder.
              Rename or remove it, or correct tasks_dir.
```

and, for a project inheriting the shipped value rather than writing one:

```text
CONFIG ERROR  <shipped default>: tasks_dir is 'tasks', but that name is a file, not a folder. This
              project has no .taskmd/config.md, so taskmd is using its shipped default; rename or
              remove that file, or write a config naming a different folder.
```

The absent case is untouched, which criterion 3 is about — `broken-tasks-dir` still answers:

```text
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'taks', but the project root has no such folder.
              Create it, or correct tasks_dir.
```

Two tests, both through `all_three_commands_refuse`, so the new case is held to the same three
commands as the old ones; the second asserts the inherited-default wording specifically, since D2 is
the half a narrower fix would have missed.

### Steps 4–5 — the fixture's row, and the runs

`tests/fixtures/README.md` gains the row and one paragraph saying what the case is. Worth recording
about the new fixture: **it does not move the repository's document count**, which stayed at 151
across the change. That is not the fixture being missed — `markdown_files` skips a subdirectory that
is itself a taskmd project, and a fixture with a `.taskmd/config.md` is one, exactly like its
fifteen neighbours.

```text
Wrote tasks/README.md - 12 active, 111 closed
OK - 123 task(s), 615 field value(s), 391 reference(s), 22 dependency edge(s), 209 declared
     output(s), 1 index file(s), 151 document(s), 1240 link(s), 2 template(s), 10 template field
     value(s), 0 vocabulary row(s)
```

Suite: `test_cli` **96** OK (94 before, plus these two), `test_list` 35 OK, `test_schema` 53 OK,
`test_budget` 5 OK, `test_runtime` 27 `OK (skipped=3)`.

**Decisions & assumptions**
- **D1 — split on `os.path.exists`, not `os.path.isfile`** — 2026-08-11, §2.
- **D2 — the inherited-default hint moves too** — 2026-08-11, §2; asserted by its own test rather
  than left to the shared one, because the two hints are built separately.
- **The test `isdir` is untouched**, per the scope: this was never a proposal to accept a file.
- **Assumption: `exists and not isdir` may be reported as "a file".** On the platforms this runs on
  the remainder is empty in practice; if it is ever wrong it is wrong in naming the kind, having
  already told the reader the true and useful part — that the name is taken and by what to stop
  being told to create it.

**Outputs produced**
- [`tests/fixtures/broken-tasks-dir-file/`](../tests/fixtures/broken-tasks-dir-file)
- [`plugin/skills/taskmd/taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py)
- [`tests/test_cli.py`](../tests/test_cli.py)
- [`tests/fixtures/README.md`](../tests/fixtures/README.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A `tasks_dir` naming a file is reported as "not a folder", not as "no such folder" | met | §3 step 2, quoted from the run; the tests also assert `no such folder` is **absent**, so the new sentence cannot pass by being appended to the old one |
| The advice given matches the case — it does not tell the reader to create a name that is already taken | met | `Rename or remove it, or correct tasks_dir.`, and the inherited form likewise; both asserted, and `Create it` / `create the folder` asserted absent |
| The absent-folder case is unchanged, and T-019's tests still pass untouched | met | `broken-tasks-dir` answers exactly as before (§3 step 3); the three tests of `AbsentTasksDirIsReportedAtSetup` were not edited, and the class runs 5 |
| Shown failing on a fixture, per R-16 | met | §3 step 1 is the fixture answering wrongly before the change, run rather than reasoned about. The fixture is committed, so the case stays exercised |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met, no child raised. **Authorisation (METHOD §3.1):** the maintainer's standing grant to work every open `M2` task through its full lifecycle, given 2026-08-10, re-confirmed and widened 2026-08-11 to *the remaining tasks, full lifecycle, continuously*. `specify` had no open questions and needed no new agreement; its **Inputs** line named `taskmd/schema.py`, a path the T-083 relocation retired, and that is corrected as a present-tense pointer rather than rewritten as history. **The fix is one sentence wider than the report.** The bug arrived from a project with its own config, but the shipped default names `tasks`, which is the value likeliest to collide with a name already in use — so the inherited hint carried the same unfollowable advice one sentence longer, and correcting only the reported half would have left the commoner case broken. Two things worth carrying: the new fixture **does not move the repository's document count**, because a subdirectory holding a `.taskmd/config.md` is a nested project and is skipped — expected, not a fixture being missed; and the tests assert the old sentence is **absent** rather than only that the new one is present, since a message can satisfy the second while still saying both. |
| 2026-08-05 | → proposed | Raised by T-019's review, from a neighbour case that task's plan had not tested. Not fixed where it was found. Recorded as low value on purpose — the backlog is more useful when the cheap items say so. |
