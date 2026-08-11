---
id: T-078
title: Say what a tasks_dir of dot means
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-069, T-024, T-019]
work_package: v0.2
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/schema.py, tests/test_cli.py, tests/fixtures/README.md, tests/fixtures/broken-tasks-dir-root/.taskmd/config.md]
---

# T-078 — Say what a tasks_dir of dot means

## 1. Specify

**Outcome**
A project that writes `tasks_dir: .` is either told it cannot, or gets a walk that means something —
rather than a `check` that silently declines to read most of the project.

**Why this one**
Found in [T-069](T-069-skip-a-nested-project-at-any-depth.md)'s `plan`, under METHOD §3.3, while
establishing whether the `base != root` guard was protecting anything. It was not — but the probe
that answered the question turned up this, which is a different defect and outside that task's scope
(`is_project` is explicitly out of it).

`tasks_dir: .` is legal today. It passes `_require`, it passes `_check_tasks_dir` — the root is
certainly a directory — and then `discovery.is_project(folder, ".")` is **true of every folder in
existence**, because it asks whether `<folder>/.` is a directory. So every subdirectory looks like a
nested project and is skipped. Shown, on a scratch project with `tasks_dir: .`, one task file at the
root and two notes below it:

```
before T-069 (the base != root guard still in place)
  BROKEN LINK   T-001-x.md   -> ./nope.md
  BROKEN LINK   sub/note.md  -> ./nope.md          sub/deeper/note.md never read

after T-069
  BROKEN LINK   T-001-x.md   -> ./nope.md          sub/note.md never read either
```

**T-069 did not cause this and does not make it worse in kind.** The guard bought exactly one level
on a walk that was already wrong below it — which is why T-069 recorded it as *failing later* rather
than as protection, and removed it anyway. Either way the project is not fully read and nothing says
so.

**Why it is worth a record rather than a shrug.** This is the class the project names as its worst
failure twice over ([T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md),
[T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md)): a validator reporting
success over something it never examined. `check` exits 0 having read a fraction of the tree, and a
project that believes it is validated is worse off than one with no validator.

**Requirements served**
R-17 (`docs/SCOPE.md`) — a configuration problem is reported when the config is read; R-16, since a
validator has to be believable.

**Scope**
- In: what `tasks_dir: .` should do — be rejected when the config is read, or be made to walk
  correctly.
- In: the same question for any value that resolves to the project root (`./`, `.\`, an empty
  segment), since a rejection that one spelling escapes is not a rejection.
- Out: `tasks_dir` naming a file, which is [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md).
- Out: `tasks_dir` naming a folder that does not exist, which is
  [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) and is done.
- Out: the nested-project exclusion itself, settled in [T-069](T-069-skip-a-nested-project-at-any-depth.md).

**Inputs**
`plugin/skills/taskmd/taskmd/schema.py` (`_check_tasks_dir`), `plugin/skills/taskmd/taskmd/discovery.py` (`is_project`),
`plugin/skills/taskmd/taskmd/cli.py` (`markdown_files`, `is_nested_project`),
[T-069](T-069-skip-a-nested-project-at-any-depth.md) §3.

**Acceptance criteria**
- [ ] A project with `tasks_dir: .` either fails at config-read time with a message naming the key,
      or has every file under its root read by `check`
- [ ] Shown failing first on a fixture, per R-16
- [ ] Whichever way it is resolved, the other spellings of "the root" get the same treatment,
      demonstrated on more than one
- [ ] A project with an ordinary `tasks_dir` is unaffected, and every existing fixture still reports
      exactly one class

**Open questions**
- ~~**Reject, or support?**~~ **Answered by the maintainer on 2026-08-09: reject, when the config
  is read.**

  So `tasks-at-the-root` is not a shape taskmd offers. One condition in `_check_tasks_dir`, which is
  already the place a `tasks_dir` problem surfaces — R-17's own rule, and the same treatment
  [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) and
  [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md) give the other two bad
  values. The message has to name the key and say what to do, as those two do.

  **The deciding argument is that the damage is not local.** `discovery.is_project` answers *"is this
  a project"* by looking for `.taskmd/` **or** the tasks folder. With `tasks_dir: .`, the second test
  is true of every directory in existence — so the defect is not that this project reads itself
  oddly, it is that the nested-project exclusion breaks for the whole tree. A configuration that
  silently makes `check` skip most of the project is the failure this repository has twice named as
  its worst ([T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md),
  [T-025](T-025-let-check-notice-a-stale-generated-index.md)): a validator reporting success over
  something it never examined.

  *Rejected: supporting it.* Tasks living at a small project's root is not an unreasonable shape and
  that is the case for it. Making it work means the nesting test can no longer use the tasks folder
  when `tasks_dir` is `.` — a special case, which is a rule somebody has to remember, which §1
  *Invisibility* rejects — or replacing `is_project`'s marker outright, which reopens
  [T-011](T-011-runtime-discovery-and-project-hook-commands.md) for every project in order to serve
  one that has not been asked for.

  **What this obliges, and it is criterion 3's whole content:** every spelling of "the root" gets the
  same answer, not just `.`. A rejection one form escapes is not a rejection.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build `tasks_dir: .` as a committed fixture with files below the root, and run `check` on it before changing anything — the point is what it *misses*, which a message cannot show. | `tests/fixtures/broken-tasks-dir-root/`, and the silent partial walk recorded in §3 |
| 2 | Reject a `tasks_dir` that resolves to the project root, in `_check_tasks_dir`, before the `isdir` test — the root is a directory, so that test returns early and never sees it. | `_check_tasks_dir` in `plugin/skills/taskmd/taskmd/schema.py` |
| 3 | Cover the spellings: the fixture for `.`, and a temp project for each of `./`, `sub/..` and an absolute path naming the root. | Tests in `tests/test_cli.py` |
| 4 | Show an ordinary `tasks_dir` is untouched, and every `broken-*` fixture still reports exactly one class — by running them all, not by the suite passing. | Recorded output |
| 5 | Give the fixture its row and its paragraph. | `tests/fixtures/README.md` |
| 6 | `check`, `index`, the suite. | Recorded output |

**Shape decisions.**

**D1 — The test is path equality against the root, not a list of spellings.** `.`, `./`, `.\`, an
empty value and `sub/..` are all the same directory, and a rule enumerating the forms is a rule that
the next form escapes — which criterion 3 exists to prevent. Comparing the resolved paths asks the
question the rejection is actually about.

**D2 — Resolved with `os.path.realpath`, so a symlink pointing at the root is caught too.** For an
ordinary project this is `abspath` with one extra syscall and the same answer. It costs nothing and
removes the one alias the spelling test would miss; without it, criterion 3's *a rejection one form
escapes is not a rejection* would hold for links even after holding for spellings.

**D3 — One message, with no shipped-default variant.** The other two `tasks_dir` errors branch on
whether the value was written or inherited, because the reader needs to know where it came from. This
one cannot be inherited: the shipped default names `tasks`. A branch would be a case that no project
can reach.

**Planned outputs**
- tests/fixtures/broken-tasks-dir-root/
- plugin/skills/taskmd/taskmd/schema.py
- tests/test_cli.py
- tests/fixtures/README.md

## 3. Implement

### Step 1 — what the fixture answered before anything changed

`tests/fixtures/broken-tasks-dir-root/` carries `tasks_dir: .`, one task at the root and two notes
below it, each with a dead link:

```text
BROKEN LINK   T-001-x.md -> ./nowhere.md

1 problem(s) - 1 task(s), 1 field value(s), … 1 document(s), 1 link(s), …
Scope  0 document(s) not read: a clone would not receive them
```

**One document of three, and the `Scope` line says nothing was skipped.** That is the finding stated
exactly: the two files below the root were dropped by the nested-project rule, which is not an
exclusion the scope note knows about, so the run reported full reach over a third of the tree. The
message was never the defect — the silence was.

### Step 2 — refused when the config is read

```text
CONFIG ERROR  .taskmd/config.md: tasks_dir is '.', which is the project root. Tasks live in a
              folder of their own; name one, and create it if it is not there.
exit 2
```

Placed **before** the `isdir` test, which the root passes trivially and so never reached this. ASCII
only, like every other message the CLI prints.

### Step 3 — the spellings

`.`, `./`, `sub/..` and the root's own absolute path, each a `subTest` over a temp project built
from the shipped config. `sub/..` is the one that matters to D1: it names the root without
containing a dot-segment anyone would think to enumerate, and it is refused for the same reason as
the others because the comparison is between resolved paths.

### Step 4 — nothing else moved

`check` run over every fixture, class per fixture:

```text
broken-config                  exit 2  CONFIG ERROR
broken-cycle                   exit 1  CYCLE
broken-dangling                exit 1  DANGLING
broken-duplicate-id            exit 1  DUPLICATE ID
broken-id-width                exit 1  ID WIDTH
broken-link                    exit 1  BROKEN LINK
broken-missing-blocker         exit 1  NO BLOCKER
broken-parked-task             exit 1  PARKED TASK
broken-stale-index             exit 1  STALE INDEX
broken-vocabulary              exit 1  VOCABULARY
broken-deliverable             exit 1  MISSING OUTPUT
broken-derived-field           exit 1  STORED DERIVED
broken-template-field          exit 1  TEMPLATE FIELD (its three)
broken-unreachable-template    exit 1  TEMPLATE UNREACHABLE
broken-hook                    exit 2  CONFIG ERROR
broken-tasks-dir               exit 2  CONFIG ERROR
broken-tasks-dir-file          exit 2  CONFIG ERROR
broken-tasks-dir-root          exit 2  CONFIG ERROR
alt-project / backend-allocated-ids / nested-at-root / ordering / planned-deliverable   exit 0
```

`alt-project` carries `tasks_dir: issues` and this repository carries `tasks`, so the ordinary case
is shown from two schemas rather than one. `leak-check` exits 2 and always did — it is a text
fixture for the publish check, not a taskmd project, and its message is the inherited-default one
from T-024's neighbour case.

**The new fixture reports exactly one class only after the fix.** Before it, the run also printed a
`CONFIG DRIFT` advisory, because a config that is read gets compared; a config that is refused is
not. Worth recording because it is the fixture-set rule arriving from an unexpected direction — the
count of what a fixture says depends on how far the run gets.

### Steps 5–6 — the runs

Suite: `test_cli` **98** OK (96 before, plus these two), `test_list` 35 OK, `test_schema` 53 OK,
`test_budget` 5 OK, `test_runtime` 27 `OK (skipped=3)`.

**Decisions & assumptions**
- **D1 — path equality against the root, not a list of spellings** — 2026-08-11, §2; `sub/..` is the
  case that shows the difference.
- **D2 — resolved with `os.path.realpath`** — 2026-08-11, §2, so a link to the root is refused too.
- **D3 — one message, no shipped-default variant** — 2026-08-11, §2: the default names `tasks`, so
  the inherited form of this error is unreachable.
- **Assumption: refusal cannot strand an existing project.** No fixture, and nothing in this
  repository, names the root; the shipped default cannot produce the value. A project that had
  written it was already being validated over a fraction of itself, so the refusal replaces a false
  pass rather than a working setup.

**Outputs produced**
- [`tests/fixtures/broken-tasks-dir-root/`](../tests/fixtures/broken-tasks-dir-root)
- [`plugin/skills/taskmd/taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py)
- [`tests/test_cli.py`](../tests/test_cli.py)
- [`tests/fixtures/README.md`](../tests/fixtures/README.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A project with `tasks_dir: .` either fails at config-read time with a message naming the key, or has every file under its root read by `check` | met | The first branch: `CONFIG ERROR … tasks_dir is '.', which is the project root`, from all three commands. The test also asserts no `BROKEN LINK` appears, so the refusal precedes the walk rather than accompanying it |
| Shown failing first on a fixture, per R-16 | met | §3 step 1 is the committed fixture answering wrongly before the change — and the wrong answer is a **pass over a third of the tree** with a `Scope` line claiming full reach, which is why the fixture has files two levels down |
| Whichever way it is resolved, the other spellings of "the root" get the same treatment, demonstrated on more than one | met | Four: `.`, `./`, `sub/..` and the absolute path. Path equality rather than enumeration, so the demonstration is of a rule and not of a list; `realpath` extends it to a link at no cost |
| A project with an ordinary `tasks_dir` is unaffected, and every existing fixture still reports exactly one class | met | §3 step 4 ran `check` on all 24 fixtures and lists the class each reports; two ordinary `tasks_dir` values (`tasks`, `issues`) pass. The suite's per-fixture tests, unedited, are the other half |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met, no child raised. **Authorisation (METHOD §3.1):** the maintainer's standing grant to work every open `v0.2` task through its full lifecycle, given 2026-08-10 and widened on 2026-08-11 to *the remaining tasks, full lifecycle, continuously*. `specify` was already agreed on 2026-08-09 and its question already answered — reject when the config is read — so this run is `plan` onward against a decision it did not re-open. Three things worth carrying. **The fixture's evidence is an absence, not a message**: before the fix it reported one dead link of three and a `Scope` line saying nothing had been skipped, because the nested-project rule is not an exclusion that note knows about — so the fixture had to carry files two levels down or it would have passed while the bug was fully present. **The rejection is path equality, not a list of spellings**, which is why `sub/..` is refused alongside `.` and `./`; `realpath` extends the same rule to a link at the cost of one syscall. And **the new fixture reports one class only after the fix** — before it, the run also printed a `CONFIG DRIFT` advisory, since a config that is read gets compared and a config that is refused is not. |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-09 | → specified | Answered: **reject when the config is read**, so tasks-at-the-root is not a shape taskmd offers. The deciding argument is that the damage is not local: `is_project` tests for `.taskmd/` **or** the tasks folder, so `tasks_dir: .` makes every directory a project and breaks the nested-project exclusion for the whole tree — a validator reporting success over something it never examined, which this repository has twice named as its worst failure. Supporting it was a real option and is recorded with its cost: either a special case in the nesting test, which is a rule somebody has to remember, or a new marker for `is_project`, which reopens T-011 for every project to serve one nobody has asked for. Criterion 3 is what the answer leans on — a rejection that one spelling of the root escapes is not a rejection. |
| 2026-08-09 | → proposed | Raised from T-069's `plan` under METHOD §3.3 — found by the probe that answered whether the `base != root` guard protected anything, and outside that task's scope, which puts `is_project` explicitly out. `low`/`xs` because no project in the tree writes `tasks_dir: .` and the likely fix is one condition; not lower, because the failure shape is the one this project has twice named as its worst — `check` exiting 0 over a tree it never read. Recorded with both transcripts so a later reader can see the guard's removal did not cause it. |
