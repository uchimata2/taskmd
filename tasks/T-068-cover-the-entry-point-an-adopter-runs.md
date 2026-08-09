---
id: T-068
title: Cover the entry point an adopter runs
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-054, T-061]
work_package: v0.1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-068 — Cover the entry point an adopter runs

## 1. Specify

**Outcome**
`plugin/bin/taskmd` and `plugin/bin/taskmd.cmd` are exercised by the suite, so deleting, renaming or
breaking either one turns the suite red instead of leaving it green.

**Why this one**
Raised as **F-10** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 3. `plugin/bin/` is the whole of the adoption path:
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) raised its absence as
`critical` — *"the adoption path not working at all"* — and
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) built it. It is what
`SKILL.md` names and what the harness puts on `PATH`.

What the suite covers today:

| Test | Reaches |
| :--- | :--- |
| `Launchers::test_both_launchers_exist_at_the_root_where_a_clone_will_look` | `taskmd.sh`, `taskmd.ps1` |
| `Launchers::test_neither_launcher_names_a_command_a_flag_or_a_field` | `taskmd.sh`, `taskmd.ps1` |
| `Launchers::test_the_shell_launcher_produces_what_the_module_produces` | `taskmd.sh` |
| `Launchers::test_every_posix_shell_script_is_recorded_executable` | `bin/taskmd` — its **mode bit** only |

Nothing runs either `bin/` file. Their existence, their delegation, and whether they produce the same
output as the module are all unasserted. T-054 verified them by hand, once.

**The gap is not hypothetical: it already hid a defect.**
[T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) is a live failure that reaches
`bin/taskmd` through its delegation to `taskmd.sh`, and no test saw it. A test of the entry point
under a fixed environment would have.

**Why `medium` and not `high`.** Nothing is broken by the absence itself — the files work. What is
missing is the thing that keeps them working, and the cost lands on whoever next moves or renames
something under `plugin/`, which after two restructures in one week is not a remote prospect.

**Requirements served**
R-16 (`docs/SCOPE.md`) — a mechanism only ever watched succeeding proves that it can run, not that a
project can rely on it; R-18, R-20.

**Scope**
- In: tests for `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd` — that they exist, that they delegate
  rather than duplicate, and that each produces what the module produces.
- In: the environment the tests run them under, which must be **set** rather than inherited — the
  reason the existing launcher test could not see T-061.
- In: whether the two `Launchers` assertions that enumerate `taskmd.sh`/`taskmd.ps1` should derive
  their subject from the tree rather than from a written pair, so a third entry point is covered the
  day it is added.
- Out: fixing the `PYTHONPATH` defect, which is T-061's. This task makes it visible; that one makes
  it stop.
- Out: whether `bin/` is the right mechanism, settled in T-054.

**Inputs**
`plugin/bin/taskmd`, `plugin/bin/taskmd.cmd`, `plugin/taskmd.sh`, `plugin/taskmd.ps1`,
`tests/test_runtime.py` (`Launchers`),
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-10.

**Acceptance criteria**
- [ ] Both `bin/` entry points are run by the suite and their output compared against the module's
- [ ] Shown failing first, per R-16 — renaming or emptying one of them turns the suite red, and the
      failure names the file
- [ ] The tests set the environment they run under, so an ambient variable cannot change the result
- [ ] A test skips honestly where the platform cannot run it, rather than passing vacuously — a
      `.cmd` on a POSIX machine is the case, and a skip that reads as a pass is worse than no test
- [ ] The subject of the launcher assertions is derived from the tree, or it is recorded why a
      written pair is correct

**Open questions**
- ~~**Does `bin/taskmd.cmd` get a real run, or only a structural check?**~~ **Decided at `plan` on
  2026-08-09: a real run wherever the platform allows one, and a reported skip where it does not.**
  It got one — this is a Windows host, so all four entry points were executed. The skip path was
  exercised separately rather than assumed; see §3 D2.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the subject: what counts as an entry point, read from the tree — the plugin root's `taskmd.*` and everything in `bin/` | `Launchers.entry_points()` |
| 2 | Give each one a platform-aware invocation that returns **None** rather than a guess when this machine cannot run it | `Launchers.how_to_run()` |
| 3 | Replace the two enumerating assertions with derived ones, and extend the no-logic check over `bin/` | `tests/test_runtime.py` |
| 4 | Run every entry point against the module's own output, with `PYTHONPATH` **set hostile** by the test | The comparison test |
| 5 | Show it red twice, in the two ways a file actually breaks: renamed away, and emptied | Both transcripts |
| 6 | Exercise the skip path itself, rather than trusting that a `.cmd` would be skipped somewhere else | The POSIX-host transcript |
| 7 | Full suite under both runners | The transcripts |

**Why step 4 sets a hostile `PYTHONPATH` rather than a clean one.** `bin/taskmd` reaches
`taskmd.sh` by delegation, so it inherited [T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md)'s
defect in full and no test saw it. Running it under a value that used to break it is what makes this
a test of the delegation rather than of a happy path.

**Why step 6 exists.** Criterion 4 is about a skip that reads as a pass. A skip nobody has watched
happen is exactly that.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — the subject is derived, and the rule is "two audiences"** — 2026-08-09. An entry point is
  `plugin/taskmd.*` or anything in `plugin/bin/`, read from the tree. That is not an arbitrary
  pattern: the plugin root is what a contributor with a clone types and `bin/` is what the harness
  puts on an adopter's `PATH`, so the two directories *are* the two ways in. A fifth file dropped
  into either is covered the day it lands, which a written pair never is — and the day someone adds
  one is exactly the day nobody remembers to extend a list.

- **D2 — a real run on Windows, a reported skip elsewhere, and the skip is itself run** —
  2026-08-09. All four ran here. The skip branch was then exercised on its own by standing in a
  POSIX `os.name` and asking `how_to_run` for each entry point:

  ```
  taskmd.ps1      -> runnable
  taskmd.sh       -> runnable
  bin/taskmd      -> runnable
  bin/taskmd.cmd  -> SKIP (reported)
  ```

  One skip, and it is the right one. The test reports it through `subTest`, so it appears as a skip
  in both runners rather than as a silent pass — and `assertTrue(ran, ...)` at the end fails outright
  if a platform could run *nothing*, which is the vacuous-pass case criterion 4 names.

- **D3 — `test_the_shell_launcher_produces_what_the_module_produces` is kept, not replaced** —
  2026-08-09. It is the assertion T-059 F-3 criticised, and the new test supersedes its purpose. It
  is kept because it is now the only one that runs a launcher under the **ambient** environment,
  which is a real case — the developer's own shell — and the new tests deliberately do not. Two
  assertions with different environments is coverage; the defect was having only the first.

- **The comment-marker map is a small piece of knowledge and is recorded as one:** `.cmd` comments
  start with `rem` or `@`, everything else with `#`. Without it the no-logic check would read a
  `.cmd`'s prose as body and fail on wording rather than on logic.

### Step 5 — shown failing first (R-16), in the two ways a file breaks

**Renamed away.** Two tests caught it, and the first is not one of this task's:

```
MISSING OUTPUT T-054 declares 'plugin/bin/taskmd', which does not exist
1 problem(s) over 77 task(s)
```

`check`'s deliverables class already guarded the file's **existence**, because T-054 declares it —
which is worth recording, since it means the gap this task closes was never existence but
**behaviour**. `test_every_entry_point_exists_where_the_one_who_runs_it_will_look` failed alongside
it.

**Emptied.** The file still exists, so nothing about existence fires; only the run does:

```
Launchers.test_every_entry_point_produces_what_the_module_produces (entry='bin/taskmd.cmd')
AssertionError: b'OK - 77 task(s), vocabulary valid, references resolve, no broken links' != b''
SUBFAILED(entry='bin/taskmd.cmd')
1 failed, 27 passed, 3 subtests passed
```

The failure names the file, and the other three entry points still pass — which is what `subTest`
buys and what a single combined assertion would have lost.

### Step 7 — validation

```
python -m pytest tests -q             125 passed, 4 subtests passed in 5.62s
python -m unittest discover -s tests  Ran 125 tests ... OK
```

Suite cost, recorded rather than discovered: **5.6s**, from 4.0s. All of the increase is process
startup — `taskmd.ps1` and `bin/taskmd.cmd` each launch PowerShell. It is the price of running the
adopter's own command instead of reading it.

**Outputs produced**
- `tests/test_runtime.py` — `entry_points()`, `how_to_run()`, three tests replacing or extending two

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Both `bin/` entry points are run by the suite and their output compared against the module's | met | §3 step 7 — four entry points, four subtests, all four executed on this host. Compared against `python -m taskmd check` byte for byte |
| Shown failing first, per R-16 — renaming or emptying one turns the suite red, and the failure names the file | met | §3 step 5, both ways. The renamed case revealed that `check` already guarded existence through T-054's `deliverables:` — so what this task actually adds is behaviour, which is a sharper statement of the gap than the finding had |
| The tests set the environment they run under | met | `PYTHONPATH` is set **hostile** — to the relative value that used to break `taskmd.sh`, which `bin/taskmd` inherits by delegation. A clean value would have tested less than the ambient one did |
| A test skips honestly where the platform cannot run it, rather than passing vacuously | met | §3 D2 — the skip branch was exercised rather than trusted, and `assertTrue(ran, …)` fails outright on a platform that could run nothing |
| The subject of the launcher assertions is derived from the tree, or it is recorded why a written pair is correct | met | Derived. D1 records the rule it is derived by — two directories, two audiences — so the derivation is a statement about the design rather than a glob that happens to match |

**Child fix tasks raised**
- none. All five criteria met, and the one thing worth knowing beyond them is recorded in the review
  above: existence was already covered, by a mechanism nobody had noticed was covering it.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met. The subject is now **derived** from the tree by a rule that says something — an entry point is `plugin/taskmd.*` or anything in `plugin/bin/`, which is the two directories because they are the two audiences: a contributor with a clone, and an adopter with the harness's `PATH`. All four run, on this Windows host, under a **hostile** `PYTHONPATH` rather than a clean one, because `bin/taskmd` reaches `taskmd.sh` by delegation and that is the defect it silently inherited. Shown red both ways a file breaks, and the renamed case taught something the finding had not: `check` already guarded the file's *existence*, through T-054's own `deliverables:` declaration, so what was actually missing was behaviour. The skip branch was exercised on a stood-in POSIX host rather than trusted, which is the difference between an honest skip and a silent pass. Suite 124 → 125 plus 4 subtests, 4.0s → 5.6s, all of it PowerShell startup. |
| 2026-08-09 | → in_progress | Plan keeps the old ambient-environment launcher test rather than replacing it: it is the assertion the audit criticised, and it is now the only one that runs a launcher under whatever the developer's shell happens to hold, which is a real case. Two assertions with different environments is coverage; the defect was having only the first. |
| 2026-08-09 | → specified | Criteria stand as raised. The open question is a `plan` question and names its own likely answer, so nothing needed the owner beyond the authorisation to run the lifecycle. |
| 2026-08-09 | → proposed | Raised as F-10 from the T-059 audit, clause 3. Established by reading what the four `Launchers` tests actually assert: only the mode bit reaches `bin/`. `medium`/`s`. The evidence that the gap is real rather than tidy-minded is T-061 — a live launcher defect that reaches `bin/taskmd` by delegation and that the suite could not see, because the one test near it inherits its environment instead of setting it. |
