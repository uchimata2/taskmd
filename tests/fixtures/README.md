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
is deliberately absent. It is nine lines of text for the pre-publish grep in `docs/PUBLISHING.md`
§6 — moved there from `CLAUDE.md` by T-047 — five that
must be caught and four safe forms that must not. It is excluded by name from the normal run and
included in the proof run, which is the whole of the arrangement (T-018). Every path in it is
fabricated.

`planned-deliverable` is the third positive case, and it exists as a **pair** with
`broken-deliverable`: the same missing `out/report.md`, declared by an open task instead of a closed
one. One must pass and one must fail, which is the whole of the rule T-089 settled — `deliverables`
asserts production, so it is only checked once the task claims to have produced. Before that task,
`broken-deliverable`'s own task was `proposed`, so the negative case was being proved by an *open*
task and nobody had written the positive one at all.

`backend-allocated-ids` is the fourth positive case, and the second **pair**: it sets
`id_width: none` and carries `#7`, `#41` and `#1024`, which no number could describe, while
`broken-id-width` keeps `id_width: 3` and still catches `T-0001`. Both directions have to hold at
once — the value exists for a backend that hands ids out, and it must not become a way to switch
off the check that catches a typo where you compose them yourself (T-082). Its status vocabulary is
`open, closed`, which used to make it the one fixture printing a `CONFIG DRIFT` line while passing:
a row still called `status` was read as behind the shipped one on all eight values.
[T-123](../../tasks/T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md) settled that a row
sharing no value with the shipped one has been **replaced** rather than left behind, so the run is
now silent — which is also why this fixture is the standing case for that rule, alongside the two
scratch projects in `test_cli.py` that draw its boundary from both sides.

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
| `broken-deliverable` | Missing deliverable | A **closed** task declares `out/report.md`, which is not there |
| `broken-duplicate-id` | Duplicate id | Two files both carrying `id: T-001` |
| `broken-stale-index` | Stale generated index | The task says `specified`; the generated region still says `proposed` |
| `broken-id-width` | Id width | `id: T-0001`, one digit too wide for `id_width: 3` |
| `broken-unreachable-template` | Unreachable template | A template in `tasks/_templates/`, which nothing lists |
| `broken-template-field` | Rotted template front-matter | A reachable template storing `children:`, naming a `type` the schema lacks, and offering a `business_value` menu one value short |
| `broken-parked-task` | Parked task | A valid `T-002` in `tasks/_drafts/`, beside a `notes.md` that must stay unreported |
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

`broken-unreachable-template` is the one fixture whose defect is a file the tool is *right* to skip:
`tasks/_templates/` is excluded by the same rule that keeps a template out of the task set, so the
listing that finds templates came back empty — and empty is the documented shape of a project that
has none. It is placed where an adopter naturally puts templates rather than somewhere contrived;
this repository used that folder itself until T-076.

`broken-template-field` is its pair, and the split is the same one the class rests on: that fixture
is a good template in the wrong **place**, this one a template in the right place with the wrong
**content**. It carries three defects rather than one — the deliberate exception to the rule above,
because they are one class and dropping any of them would leave the fixture proving less than the
check claims. The third is the one that matters: a menu one value short, where everything it still
offers is legal, so nothing a reader could spot distinguishes it from a correct template. That is
the form that had gone unnoticed in this repository's own shipped task template, and the new check
found it on its first run (T-032).

`broken-duplicate-id` and `broken-id-width` are the two cases where the defect is that a file is
**not** the task it looks like, and both were silent before T-062 and T-075. The first is the only
fixture whose file count and task count differ on purpose: two task files, one task, and before the
fix the survivor was whichever the filesystem happened to yield last. The second carries an
ordinary sibling as well, so what it shows is a *file* being rejected rather than a project failing
to load.

`broken-link`'s defect is in `.notes/` rather than in a task, and that is the interesting part:
`glob`'s `**` skips dot-directories, so a fixture that put the dead link in an ordinary folder would
pass a walk that never opens one. What it pins is the **tracked** half of that problem — its
`.notes/scratch.md` is committed, so a clone receives it and `check` reads it.

**It no longer covers the case that motivated it**, and the wording above used to say it did
(T-098). That case was a live handoff pointer, which is gitignored as well as hidden, and since
T-094 the document side of the link walk reads only what a clone would receive. Nothing validates
the links in a document a clone would not receive — decided, with the alternatives priced, in T-098.
So this fixture proves the walk, not the exclusion, and the two must not be read as one.

`nested-at-root` is the third positive case, and it exists because of the shape of this folder
rather than because of a feature. Every `broken-*` project sits **two** levels down, and the nested-
project exclusion below used to begin one level down — so a project holding another project as a
*direct* child had that child's defects reported as its own, and no fixture here could show it
(T-069). Its `inner/` is the only nested project in this tree that is a direct child, and the host
must report nothing.

**These projects are not part of this one.** `check` skips a nested project — a directory holding
its own `.taskmd/` or its own tasks folder — **at any depth, including directly inside the root**.
So the host repository does not report the defects these exist to hold. A taskmd project inside a
taskmd project is validated on its own.
