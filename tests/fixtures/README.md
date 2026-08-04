# Fixtures

Miniature taskmd projects the real CLI is pointed at. They are projects, not test data: a fixture
you can run the tool against is also the reproduction case for the day a class regresses.

`alt-project` is the positive case — a schema unlike the default in every configurable dimension,
which is what proves the schema is configuration rather than code (T-001).

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
| `broken-config` | Config error at setup — a **key** | `id_witdh` — a typo in a key name |
| `broken-tasks-dir` | Config error at setup — a **value** | `tasks_dir: taks`, beside a real `tasks/` |

The two config fixtures are the two halves of one class, and the split is the finding: a misspelled
**key** was caught from the start, a misspelled **value** was not, and only the first had ever been
exercised. `broken-tasks-dir` also has no committed sibling for the case where the value is fine and
the folder simply has not been made yet — a project with neither a config nor a tasks folder is an
empty directory, which git cannot store, so that one is built in a temp directory by the test.

`broken-link`'s defect is in `.notes/` rather than in a task, and that is the interesting part:
`glob`'s `**` skips dot-directories, which is how a broken link in a live handoff pointer stayed
invisible. A fixture that put the dead link in an ordinary folder would pass a walk that misses the
case that actually bit.

**These projects are not part of this one.** `check` skips a nested project — a directory holding
its own `.taskmd/` or its own tasks folder — so the host repository does not report the defects
these exist to hold. A taskmd project inside a taskmd project is validated on its own.
