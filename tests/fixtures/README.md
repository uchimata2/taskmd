# Fixtures

Miniature taskmd projects the real CLI is pointed at. They are projects, not test data: a fixture
you can run the tool against is also the reproduction case for the day a class regresses.

`alt-project` is the positive case — a schema unlike the default in every configurable dimension,
which is what proves the schema is configuration rather than code (T-001). It also carries the
renamed-ordering case: its effort field is `size`, and it declares no value field at all, so `list`
must order without either of the words the default config uses (T-022).

`ordering` is the second positive case, and it is built to be **decisive rather than
representative**. Four tasks arranged so that the two readings of "highest value, lowest effort,
dependencies first" give different answers: T-001 is the least valuable and cheapest task and
blocks T-002, the most valuable. Under the rule taskmd implements, T-001 leads because its
effective value is T-002's; under the plain reading, T-003 would lead. A fixture where both
readings agree would have passed either implementation and proved nothing (T-022).

`leak-check` is **not a taskmd project** — the only folder here that is not, which is worth saying
because every neighbour is, and a reader following the convention would look for a `.taskmd/` that
is deliberately absent. It is nine lines of text for the pre-publish grep in `CLAUDE.md`: five that
must be caught and four safe forms that must not. It is excluded by name from the normal run and
included in the proof run, which is the whole of the arrangement (T-018). Every path in it is
fabricated.

The `broken-*` projects are the negative cases. **Each holds exactly one defect**, so a `check` run
that reports two classes on one fixture is itself a finding. They were written **before** `check`
existed (T-002, plan step 3): a validator is worth what you believe it would catch, and the only
way to earn that is to have watched it fail on a case it should catch — so the cases came first,
where they could not be quietly trimmed to whatever turned out to be easy.

| Project | Class | The defect it holds |
| :--- | :--- | :--- |
| `broken-vocabulary` | Bad enumerated value | `status: in-progres` |
| `broken-dangling` | Dangling reference | `blocked_by: [T-404]`, which does not exist |
| `broken-missing-blocker` | Missing blocker | `status: blocked` with an empty `blocked_by` |
| `broken-cycle` | Dependency cycle | T-001 and T-002 each block the other |
| `broken-link` | Broken link | A dead Markdown link inside a **dot-directory** |
| `broken-derived-field` | Stale stored-derived field | A task stores `children:`, which is derived |
| `broken-deliverable` | Missing deliverable | Declares `out/report.md`, which is not there |
| `broken-duplicate-id` | Duplicate id | Two files both carrying `id: T-001` |
| `broken-id-width` | Id width | `id: T-0001`, one digit too wide for `id_width: 3` |
| `broken-config` | Config error at setup — a **key** | `id_witdh` — a typo in a key name |
| `broken-tasks-dir` | Config error at setup — a **value** | `tasks_dir: taks`, beside a real `tasks/` |
| `broken-hook` | Config error at setup — a **command** | `after_write` naming a file the project does not ship |

The three config fixtures are one class in three parts, and each part was a finding: a misspelled
**key** was caught from the start, a misspelled **value** was not, and only the first had ever been
exercised. `broken-hook` is the third — a declared command that could never run — and it is
catchable at all only because a hook is declared as a program plus arguments rather than as a shell
line, so the question can be asked without running anything (T-011).
`broken-tasks-dir` also has no committed sibling for the case where the value is fine and
the folder simply has not been made yet — a project with neither a config nor a tasks folder is an
empty directory, which git cannot store, so that one is built in a temp directory by the test.

`broken-duplicate-id` and `broken-id-width` are the two cases where the defect is that a file is
**not** the task it looks like, and both were silent before T-062 and T-075. The first is the only
fixture whose file count and task count differ on purpose: two task files, one task, and before the
fix the survivor was whichever the filesystem happened to yield last. The second carries an
ordinary sibling as well, so what it shows is a *file* being rejected rather than a project failing
to load.

`broken-link`'s defect is in `.notes/` rather than in a task, and that is the interesting part:
`glob`'s `**` skips dot-directories, which is how a broken link in a live handoff pointer stayed
invisible. A fixture that put the dead link in an ordinary folder would pass a walk that misses the
case that actually bit.

**These projects are not part of this one.** `check` skips a nested project — a directory holding
its own `.taskmd/` or its own tasks folder — so the host repository does not report the defects
these exist to hold. A taskmd project inside a taskmd project is validated on its own.
