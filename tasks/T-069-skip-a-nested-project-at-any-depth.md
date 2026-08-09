---
id: T-069
title: Skip a nested project at any depth, not below the first
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-078, T-011]
work_package: v0.1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-069 — Skip a nested project at any depth, not below the first

## 1. Specify

**Outcome**
`check` skips a nested taskmd project wherever it sits, including directly inside the project root —
so a host project never reports another project's defects as its own.

**Why this one**
Raised as **F-7** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Shown, not asserted — an outer project with one task, and a complete
taskmd project one directory below it holding a deliberately dead link:

```
taskmd check --root <the outer project>
BROKEN LINK   inner/tasks/T-001-b.md -> ./nope.md

1 problem(s) over 1 task(s)
exit=1
```

One task, one problem, and the problem belongs to a different project.

**The mechanism.** `markdown_files()` guards its nested-project test with `base != root`, so while
walking the top level of the tree it never asks whether a subdirectory is a project. One level down
it does, which is why this repository has never seen it: every fixture project sits at
`tests/fixtures/<name>`, two levels down, and is correctly skipped.

**A documented claim is broader than the behaviour.** `tests/fixtures/README.md` closes with
*"`check` skips a nested project — a directory holding its own `.taskmd/` or its own tasks folder —
so the host repository does not report the defects these exist to hold. A taskmd project inside a
taskmd project is validated on its own."* True at depth two and greater; false at depth one.

**Who pays.** An adopter whose repository holds a sub-project at the top level — a monorepo with a
`frontend/` or a `docs-site/` that tracks its own tasks — gets that project's problems reported
against theirs, with no way to tell which is which. `load_tasks` is unaffected (it walks only
`tasks_dir`), so the damage is confined to the link sweep, which is also the only check that reads
the whole tree.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`) — the validator must be believable, and a report naming another
project's file is the kind of noise that trains people to ignore it.

**Scope**
- In: the `base != root` guard in `plugin/taskmd/cli.py::markdown_files`, and whether it has a reason
  nobody wrote down.
- In: a fixture exercising the depth-one case, since none of the ten existing `broken-*` projects
  can — they are all at depth two by construction.
- In: the sentence in `tests/fixtures/README.md`, which states the rule without its exception.
- Out: `discovery.is_project` and the nearest-wins resolution rule, both settled in
  [T-011](T-011-runtime-discovery-and-project-hook-commands.md) and correct.
- Out: whether nested projects should be validated *by* the host, which is settled the other way and
  not reopened.

**Inputs**
`plugin/taskmd/cli.py` (`markdown_files`, `is_nested_project`), `plugin/taskmd/discovery.py`
(`is_project`), `tests/fixtures/README.md`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-7.

**Acceptance criteria**
- [ ] A project holding another project **directly** inside its root does not report that project's
      problems
- [ ] Shown failing first on a fixture, per R-16 — the current behaviour is reproduced before the
      change
- [ ] The ten existing `broken-*` fixtures each still report exactly one class, and this repository's
      own `check` is unchanged
- [ ] The guard's removal or replacement is explained — if `base != root` was protecting something,
      that thing still works
- [ ] `tests/fixtures/README.md`'s claim is true of the code afterwards, checked against the sentence

**Open questions**
- ~~**Can the root itself be caught by its own test?**~~ **Established at `plan` on 2026-08-09: no,
  and the guard was protecting nothing that works.** The question asked for evidence rather than a
  reading, and got it — including one configuration where removing the guard *does* change
  behaviour, which turned out to be broken either way. See §3 D1.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Find out why the guard exists — `git log -S` on the expression, and read the commit that introduced it | Its provenance, or the absence of one |
| 2 | Build the depth-one fixture none of the ten existing ones can be, and reproduce | The failing evidence |
| 3 | Remove the guard and sweep **every** project in the tree, not only the new fixture | The per-project transcript |
| 4 | Hunt for the case the guard could be protecting: a configuration where `is_project` answers differently at the top level | Either a counter-example or a clean bill |
| 5 | If a counter-example exists, establish whether the guard *fixes* it or merely defers it | The comparison, guard on and off |
| 6 | Apply, with the reason written where the guard was — a removed guard leaves no trace otherwise | `plugin/taskmd/cli.py` |
| 7 | A test, and the fixtures README's sentence made true | `tests/test_cli.py`, `tests/fixtures/README.md` |

**Why step 4 is a hunt and not a check.** "The guard protects nothing" is unfalsifiable by passing
tests — every fixture passing is what it looked like *before* the fix too. The only honest move is to
go looking for the configuration that would need it.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — the guard goes, and the counter-example does not save it** — 2026-08-09. Three findings, in
  order:

  1. **It has no recorded reason.** `git log -S "base != root"` puts it in `f73488d`, the original
     implementation of the three commands (T-002), with no comment and nothing in that commit's
     message about it. It was never argued for.
  2. **Removing it changes nothing across fifteen projects**: this repository, `alt-project`,
     `ordering`, and all twelve `broken-*` — each still reporting exactly one class, including
     `broken-link`, whose defect is in a dot-directory and is the case most at risk from a walk
     change.
  3. **There is exactly one configuration where it matters, and it is broken either way.** With
     `tasks_dir: .`, `discovery.is_project(folder, ".")` is true of *every* folder, because it asks
     whether `<folder>/.` is a directory. Measured on a scratch project with a task at the root and
     notes one and two levels below:

     ```
     guard in place    T-001-x.md and sub/note.md read;  sub/deeper/note.md never read
     guard removed     T-001-x.md read;                  sub/note.md never read either
     ```

     So the guard bought **one level** on a walk that was already wrong below it. That is failing
     later, not protecting — and it is the shape of the answer criterion 4 asks for.

  *Rejected: keeping the guard and special-casing depth one.* It would preserve the one extra level
  for a configuration nobody has, at the price of keeping the defect this task exists to remove.

  *Rejected: fixing `tasks_dir: .` here.* Out of scope by §1 — `is_project` is T-011's — and it is a
  different defect with a different owner. Raised as
  [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) rather than absorbed, with both transcripts, so
  a later reader can see this task's change did not cause it.

- **D2 — the fixture is a positive case, and its name says so** — 2026-08-09. `nested-at-root` is not
  a `broken-*` project: its host must report **nothing**, and the defect it carries belongs to a
  project the host is supposed to ignore. Naming it `broken-` would have put it in the family whose
  contract is "reports exactly one class", which it must never do.

- **What the fixture set was hiding, recorded because it generalises:** all ten `broken-*` projects
  sit two levels down, so the shape of the fixture folder was hiding the shape of the bug. A rule
  about depth cannot be tested by a set that is uniform in depth.

### Step 2 — shown failing first (R-16)

```
taskmd check --root tests/fixtures/nested-at-root
BROKEN LINK   inner/tasks/T-001-inner.md -> ./nope.md
1 problem(s) over 1 task(s)                                        exit 1
```

The host has nothing wrong with it. `inner/` is a project in its own right, sitting directly inside
the root.

### Steps 6–7 — after

```
taskmd check --root tests/fixtures/nested-at-root
OK - 1 task(s), vocabulary valid, references resolve, no broken links     exit 0

taskmd check --root tests/fixtures/nested-at-root/inner
BROKEN LINK   tasks/T-001-inner.md -> ./nope.md                          exit 1
```

Skipped by the host, validated on its own — which is the rule stated, now at every depth. Twelve
`broken-*` fixtures each still report exactly one class; `alt-project`, `ordering` and this
repository are unchanged.

```
python -m pytest tests -q             126 passed, 4 subtests passed
python -m unittest discover -s tests  Ran 126 tests ... OK
taskmd check                          OK - 78 task(s), ...
```

**Outputs produced**
- `plugin/taskmd/cli.py` — `markdown_files`, with the removed guard's history in its docstring
- `tests/fixtures/nested-at-root/` — the only fixture whose nested project is a direct child
- `tests/test_cli.py` — `test_a_project_directly_inside_the_root_is_still_skipped`
- `tests/fixtures/README.md` — the sentence, and why this fixture exists
- [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) — the counter-example, raised not absorbed

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A project holding another project **directly** inside its root does not report that project's problems | met | §3 step 6, and the nested project still reports its own defect when asked directly — so this is an exclusion, not a blind spot |
| Shown failing first on a fixture, per R-16 | met | §3 step 2, on a fixture built for it because no existing one could be: all ten `broken-*` sit two levels down |
| The ten existing `broken-*` fixtures each still report exactly one class, and this repository's own `check` is unchanged | met | Twelve now, not ten — T-062 and T-075 added two this session. All twelve swept, plus both positive fixtures and this repository |
| The guard's removal or replacement is explained — if `base != root` was protecting something, that thing still works | met | D1, and this is the criterion the work actually turned on. It protected one configuration by one level, on a walk already wrong below that level; the evidence is both transcripts, guard on and off. The configuration is [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) |
| `tests/fixtures/README.md`'s claim is true of the code afterwards, checked against the sentence | met | The sentence gained *"at any depth, including directly inside the root"* — it was true of the rule and false of the code, which is why it read as complete |

**Child fix tasks raised**
- **[T-078](T-078-say-what-a-tasks-dir-of-dot-means.md)** — `tasks_dir: .` makes every folder look
  like a nested project. Not a criterion this task failed: it is the counter-example the guard hunt
  produced, it predates this change, and `is_project` is out of scope here by §1.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met, and the one that carried the work was the fourth — *if `base != root` was protecting something, that thing still works*. Three findings answer it: the guard has **no recorded reason** (`git log -S` puts it in the original T-002 implementation with no comment and nothing in the commit message); removing it changes nothing across fifteen projects; and there is exactly **one** configuration where it matters, `tasks_dir: .`, which makes `is_project` true of every folder and where the guard bought one level on a walk already wrong below it. Failing later is not protecting. That counter-example is raised as T-078 with both transcripts rather than absorbed, so a later reader can see this change did not cause it. The generalisable point is about the fixtures rather than the code: all ten `broken-*` projects sit two levels down, so a set uniform in depth could never test a rule about depth. |
| 2026-08-09 | → in_progress | Plan makes the counter-example a **hunt** rather than a check, because "the guard protects nothing" is unfalsifiable by passing tests — every fixture passing is exactly what it looked like before the fix. The hunt found one, which is why the answer is worth more than a deletion. |
| 2026-08-09 | → specified | Criteria stand as raised. The open question is a `plan` question and asks for evidence rather than a reading, which is what it got. |
| 2026-08-09 | → proposed | Raised as F-7 from the T-059 audit, clauses 1 and 3. Reproduced before write-up on a scratch project outside the repository. `medium`/`s`: invisible here because every fixture is two levels down, real for a monorepo adopter, and it makes a documented claim broader than the behaviour. Confined to the link sweep — `load_tasks` walks only `tasks_dir` and is unaffected. |
