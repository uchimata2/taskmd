---
id: T-023
title: Stop config errors printing an absolute install path
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-006, T-019, T-020]
work_package: M2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-05
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/schema.py, tests/test_schema.py]
---

# T-023 — Stop config errors printing an absolute install path

## 1. Specify

> **Read this first — the leak in the title is gone, and what is left is one string.**
> `_display()` landed in commit `580d22b` (closing
> [T-011](T-011-runtime-discovery-and-project-hook-commands.md)) **after** this task was raised and
> after its decision was recorded, and it removed the absolute path from every config error. Run
> today on a project outside this repository with no `.taskmd/config.md`, the error opens
> `CONFIG ERROR  taskmd/defaults/config.md: …` — machine-independent already.
>
> So this task is **not** the fix its title describes. What remains is the wording the maintainer
> chose on 2026-08-07 and which the code does not implement: the prefix should read
> `<shipped default>`, and it currently reads the file's real name — *precisely* the form that
> answer rejected. That is the whole of the work, and it is one string.
>
> Reconciled by [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) on 2026-08-09.
> Everything below is kept as written, with the two criteria the fix overtook marked in place.

**Outcome**
~~A `SchemaError` raised against the **shipped default** config names that config in a form that is
the same on every machine, instead of the absolute path to wherever taskmd happens to be installed.~~
**Achieved by T-011, not by this task.** The live outcome is the one the maintainer's answer names:
that prefix reads `<shipped default>` rather than the file's own path.

**Why this one** *(as it stood on 2026-08-05 — the code below has since changed; see the note above)*
Found while verifying [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md). Every
`SchemaError` is prefixed with the config's `source`, and when the project had no `.taskmd/config.md`
that source was `DEFAULT_CONFIG` — built from `os.path.abspath(__file__)`, so it was an absolute path
into the installation:

```
CONFIG ERROR  <absolute install path>/taskmd/defaults/config.md: tasks_dir is 'tasks', but the
project root has no such folder. ...
```

The behaviour is **older than T-019** and applies to every one of the config errors, not just the
new one — this task is not a defect in that fix. What T-019 changed is the exposure: a project that
has adopted taskmd and not yet made its tasks folder is now an error, so this string is plausibly
the **first output a new user ever sees**, and it names a directory that means nothing to them.

Two requirements are in tension with it. R-20 asks for byte-identical output across Windows, macOS
and Linux — this string cannot be, since it differs per machine, never mind per platform, which
makes it a concrete obstacle to [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md)
rather than a cosmetic one. R-23 forbids absolute local paths; that rule governs the repository and
this is runtime output, so it is not a publishing leak — but a tool whose first line of output is
someone's home directory is a poor advertisement for it, and pasting that line into an issue leaks
it for them.

**Requirements served**
R-20, and R-23 in spirit (`docs/SCOPE.md`).

**Scope**
- In: how the shipped default config is named in error messages.
- Out: the project-config case, which already prints a root-relative path and is correct.
- Out: the wording of any individual error — this is the prefix, not the messages.

**Inputs**
`taskmd/schema.py` (`DEFAULT_CONFIG`, `load_schema`, `SchemaError`), `docs/SCOPE.md` R-20 and R-23.

**Acceptance criteria**

Criteria 1 and 4 were overtaken by T-011. Both are kept as written and marked, per
[`review.md`](../plugin/skills/taskmd/docs/method/review.md) *Changing a criterion* — a criterion edited to match
what happened is a description, not a criterion.

- [x] A config error against the shipped default prints the same bytes regardless of where taskmd
      is installed — **already met**, by `_display()` in `580d22b`, before this task started
- [ ] It is still unambiguous which file is meant — a reader can find it
- [ ] The project-config case is unchanged
- [ ] ~~Shown failing on a fixture, per R-16~~ — **unmeetable, and kept to say so.** Nothing fails:
      the behaviour this would have demonstrated no longer exists. The remaining change is a wording
      preference with no failing case to build, so the fixture that would prove it cannot be written
      and its absence is not a gap in the work

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: `<shipped default>`.** The error says which
  config is in force, and a repo-relative path is relative to *taskmd's* repository rather than the
  adopter's — so it would still be wrong for the person reading it, while the absolute form is the
  R-23 leak this task exists to remove. *Rejected: printing `taskmd/defaults/config.md`.* It is the
  file's real name and findable, which is exactly what the bracketed label costs: a reader learns a
  default is in force without learning where to read it.

## 2. Plan

One string, as §1 says. The plan is short because the work is; what it spends its steps on is the
reach of the change and the evidence, neither of which the edit itself shows.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give `_display()` the label: when the path it is asked to name is the shipped default, return `<shipped default>` instead of a relative path to it. | The edited `plugin/skills/taskmd/taskmd/schema.py` |
| 2 | Establish the reach before editing — every place a config's name is printed, so the label is judged where it will actually appear and not only in the error it was raised for. | A list of the call sites, recorded in §3 |
| 3 | Run the case: a project with no config and no tasks folder, which is the first output a new adopter can see. | The literal command output in §3 |
| 4 | Run the suite and record what moved, including the four failures this machine reports for reasons of its own. | The literal counts in §3 |
| 5 | Run `check` and `index`. | The literal output in §3 |

**Where the label goes — decided.** In `_display()`, which is already the one place that turns a
config path into a name for messages. *Rejected:* substituting at the two call sites in
`load_schema()`. It puts the same rule in two places and leaves a third caller free to print the
path, which is the drift this project's own design rule exists to stop.

**Not in scope, and deliberately not linked.** `schema.py` has a `main()` of its own that prints
`schema   <source>`, so it will print the label too. Whether that entry point should exist at all is
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md)'s question, and it is not made harder by
a shorter string, so no edge is recorded — a graph that links everything says nothing
(`METHOD.md` §4).

**No fixture, and §1 says why.** Criterion 4 is marked unmeetable in `specify`: nothing fails, so
there is no failing case to build. The evidence in steps 3–5 is a run, not a test that would pass
before the change as well as after.

**Outputs promised**

- plugin/skills/taskmd/taskmd/schema.py
- tasks/T-023-stop-config-errors-printing-an-absolute-install-path.md
- tasks/README.md

## 3. Implement

**Decisions & assumptions**
- **The label is returned by `_display()`, before it tries to relativise anything** — 2026-08-10, as
  planned. Compared by `os.path.abspath` on both sides rather than by string equality, because the
  two callers pass `DEFAULT_CONFIG` as it was built and a future one may not.
- **The reason is written where the code is**, in `_display()`'s docstring: what the label costs, and
  that the recorded answer to it biting is to name the file beside the label rather than to go back
  to the path. Without that, the next reader sees a string that is less informative than the one it
  replaced and no reason not to revert it.
- **The reach is three call sites, all of them correct with the label** — 2026-08-10. `load_schema`
  builds `source` once, and every `SchemaError` in the module opens with it; `load_schema` also names
  the shipped default separately when reading its vocabularies for the drift comparison; and
  `schema.py`'s own `main()` prints `schema   <source>`, which now reads `schema   <shipped default>`.
  That third one is the only non-error use, and saying *which* config is in force is what that line
  is for, so the label suits it. `cli.py` never prints `schema.source`.
- **The test that asserted the old contract was replaced, not deleted** — 2026-08-10.
  `test_no_config_file_falls_back_to_the_shipped_default` resolved `source` against the plugin root
  and compared it to `DEFAULT_CONFIG`; that is the path form the maintainer's answer rejected, so it
  had to go. It is now an equality against `<shipped default>`, which fails if any path form comes
  back — a weaker assertion (`assertNotIn(os.sep, ...)`) would pass for a bare basename too.
- **The project-config half gained the assertion it never had** — 2026-08-10.
  Criterion 3 says the project-config case is unchanged, and nothing in the suite was checking what
  that case prints; `check`'s `broken-config` fixture asserts the error's *body* and not its prefix.
  So "unchanged" was unfalsifiable before this task and is now `.taskmd/config.md`, asserted.

**Outputs produced**
- plugin/skills/taskmd/taskmd/schema.py — `_display()` returns the label, and says why
- tests/test_schema.py — the replaced assertion, and a new class for the project-config half
- tasks/T-023-stop-config-errors-printing-an-absolute-install-path.md — this record
- tasks/README.md — regenerated

**Evidence — the case a new adopter meets first.** A directory with no config and no tasks folder,
which is what `taskmd check` now says to them:

```
CONFIG ERROR  <shipped default>: tasks_dir is 'tasks', but the project root has no such folder. This project has no .taskmd/config.md, so taskmd is using its shipped default; create the folder, or write a config naming a different one.
exit=2
```

The prefix was `taskmd/defaults/config.md` before the edit — machine-independent since T-011, and
still a path into a tree the reader has not got.

**Evidence — the suite, before and after.** Every module, run as CI runs them, one process each:

```
=== test_budget.py (exit 0)
=== test_cli.py (exit 0)
=== test_list.py (exit 0)
=== test_runtime.py (exit 1)   FAILED (failures=4)
=== test_schema.py (exit 0)    Ran 46 tests
```

`test_schema.py` failed 1 immediately after the code edit and before the test was updated — the old
assertion, catching exactly the change it was written to catch. `test_runtime.py`'s four are the
`Launchers` failures this machine reports for its own reasons
([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)); the same four failed before
this task's first edit, and they are absent on the Linux runner.

```
Wrote tasks/README.md - 19 active, 97 closed
OK - 116 task(s), 580 field value(s), 367 reference(s), 22 dependency edge(s), 181 declared output(s), 1 index file(s), 144 document(s), 1144 link(s), 2 template(s), 10 template field value(s), 0 vocabulary row(s)
```

Two declared outputs more, which are this task's two — and `check` reads them as paths that must
exist, so the declaration is checked rather than decorative.

## 4. Review

Judged against the four criteria as they stand in §1 — two of which `specify` had already marked,
one met by another task and one unmeetable, both kept as written rather than edited to fit.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A config error against the shipped default prints the same bytes wherever taskmd is installed | met | Met by `_display()` in `580d22b` before this task started, and not undone here: a constant string is as machine-independent as a relative path, and more so than one that has to be computed against two bases. |
| It is still unambiguous which file is meant — a reader can find it | **partly — priced** | *Which* file is unambiguous: there is exactly one shipped default, and the same message names `.taskmd/config.md` as the config this project has not got, so the two are distinguishable in the one line. *Findable* it is not — the label gives no path, which is the cost the maintainer weighed and accepted on 2026-08-07 against the alternative of printing a path into taskmd's own tree. Not raised as a child task: the recorded answer if it bites is to name the file beside the label, and nothing has yet reported it biting. |
| The project-config case is unchanged | met | `TheConfigInForceIsNamedForItsReader` in `tests/test_schema.py` asserts `source` is `.taskmd/config.md` for a project with its own config. Worth saying plainly: this criterion was **unfalsifiable until now** — no test read that value, so "unchanged" would have been a claim about code I had just edited, checked by reading it. |
| ~~Shown failing on a fixture, per R-16~~ | **unmeetable — as recorded in `specify`** | Nothing fails, so no fixture can be built. What replaced it is not nothing: the old assertion in `test_schema.py` failed on the code change before the test was updated, which is a failing case for the contract even though it is not a fixture for the behaviour. Recorded because "no fixture" and "no evidence" are different things. |

**Child fix tasks raised**
- none. The one partial is a cost the owner priced before the work started, with the remedy recorded
  in §1 for the day it is needed; raising a task for it now would be tracking a contingency, not work.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Plan through review in one session, under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1), which covers each task in that set end to end and nothing outside it. The one-string fix cost two test changes, and the second was the find: criterion 3 says the project-config case is unchanged and **nothing in the suite read that value**, so the criterion could not have been failed by any edit. Nothing raised — the one partial is the cost §1 priced on 2026-08-07. |
| 2026-08-07 | → specified | Answered: `<shipped default>`. The rejected option's cost is recorded rather than glossed — a bracketed label tells a reader a default is in force but not where to read it, and if that turns out to bite, the fix is to name the file next to the label rather than to reverse this. |
| 2026-08-05 | → proposed | Raised from T-019's implement phase. Pre-existing behaviour, surfaced because T-019 made the fresh-project case an error and so put this string in front of new users. Not fixed where it was found (METHOD §3.3, rule 4). |
