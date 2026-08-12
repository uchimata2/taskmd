---
id: T-011
title: Runtime auto-discovery and project hook commands
type: deliverable
status: done
phase: review
parent: null
blocked_by: [T-002]
related: []
work_package: M1
owner: maintainer
business_value: medium
effort: m
created: 2026-08-04
updated: 2026-08-07
deliverables:
  - plugin/skills/taskmd/taskmd/discovery.py
  - plugin/skills/taskmd/taskmd/schema.py
  - plugin/skills/taskmd/taskmd/cli.py
  - plugin/skills/taskmd/taskmd/__main__.py
  - plugin/skills/taskmd/taskmd/defaults/config.md
  - plugin/skills/taskmd/taskmd.sh
  - plugin/skills/taskmd/taskmd.ps1
  - tests/test_runtime.py
  - tests/fixtures/broken-hook/.taskmd/config.md
---

# T-011 — Runtime auto-discovery and project hook commands

## 1. Specify

**Outcome**
taskmd runs on a clone without anyone naming an interpreter or editing a path, and a project can
plug in its own commands — written in bash, PowerShell, Python or anything else — that taskmd
invokes at defined points.

**Requirements served**
R-18, R-19 (`docs/SCOPE.md`). Bounded by assumption **A1**: the logic exists once, in Python.

**Why this one**
This is what "use bash, PowerShell and Python — auto-discovery / configurable" resolves to once
R-1 is applied. Three implementations of one command set would be three copies of one fact; one
implementation plus discovered launchers plus configurable project hooks gives the same reach with
one home. The hooks also cover the case the reference project needed — an external consistency
check run after every write.

**Scope**
- In: locating the interpreter (`py` / `python3` / `python`) and the repository root; thin
  launchers for bash and PowerShell; a config-declared hook mechanism with defined invocation
  points; failure reporting.
- Out: any second implementation of the commands. Any hook that taskmd itself ships — hooks are
  the project's, not the plugin's.

**Inputs**
- `docs/SCOPE.md` §3C and §6 (A1)
- `CLAUDE.md` — dependency-free, cross-platform, explicit newline, cp1252-safe console
- Handoff `local-markdown-dir.md` `tracker_lint` — the same idea, proven in use: a project-supplied
  command run after a write, with errors resolved before finishing

**Acceptance criteria**
- [ ] A clone runs with no configuration on Windows, macOS and Linux — demonstrated on at least
      two, with the actual command output
- [ ] The launchers contain no logic: proven by deleting one and showing behaviour is unchanged
- [ ] A hook is declared, invoked, and its **failure surfaces** — proven with a hook that exits
      non-zero
- [ ] A hook written in a language other than Python is proven to run
- [ ] A missing or unrunnable hook is reported when the config is read, not mid-command (R-17)
- [ ] The repository root resolves from the repository, not the working directory — proven by
      running from a subdirectory and from outside the repository

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: one invocation point — after a write.**
  `tracker_lint` is the only point with evidence behind it, and every additional point is a config
  key an adopting project pays to have documented, validated and kept true for a need nobody has
  stated. *Rejected: a pre-write point as well.* It would catch a bad edit before it lands rather
  than after, which is a genuine advantage — but it is speculative, and a second point can be added
  later at the cost of a schema change rather than carried unused from the start.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Settle what marks the repository root, before any code.** The obvious marker is the config folder — and this repository does not have one, because it runs on the shipped default. A marker only a *configured* project carries would fail on the very tree that has to prove the feature, and `.git` is the other obvious candidate and is forbidden by R-9. Decide, and record what was rejected. | The decision in §3, and the resolution rule stated once in `taskmd/discovery.py`'s docstring |
| 2 | **Settle how a hook is declared, and what makes one "unrunnable", before any code.** Criterion 5 is only satisfiable if the declaration names something taskmd can resolve *without running it*; a free shell string is the convenient form and makes the question undecidable. Decide, and record what was rejected. | The decision in §3, and the new key with its annotation in `taskmd/defaults/config.md` |
| 3 | **Establish how criterion 1's second platform is demonstrated.** This session's environment has no Linux environment, no container runtime and no remote, so "demonstrated on at least two" cannot be satisfied by running commands in it. Placed before the build because it is the one criterion that could turn out unprovable, and finding that out at review is expensive. **Needs the maintainer:** every route costs something outside this repository. | A recorded decision naming the route, and — only if the route is CI — one workflow file |
| 4 | **Tests first, failing**, per R-16 and the `broken-*` precedent. The cases that matter are the ones the criteria name: a hook that exits non-zero, a hook that is not Python, a config naming a hook that is not there, a root resolved from a subdirectory, and a root that cannot be found at all. | New tests in `tests/`, all failing, and the fixture projects they need |
| 5 | Resolve the hook declaration in `taskmd/schema.py` — nullable like `deliverables_field`, and validated where the config is read so criterion 5 is structural rather than remembered. | The change in `taskmd/schema.py` |
| 6 | Implement root discovery, and demote `--root` from *default* to *override*. | `taskmd/discovery.py`, and the change in `taskmd/cli.py` |
| 7 | Implement the invocation: after the one command that writes, run the declared hook and surface its exit code and its output. | The change in `taskmd/cli.py` |
| 8 | Write the two launchers. Each finds an interpreter and delegates; neither knows a command name, a flag or a file path. | `taskmd.sh`, `taskmd.ps1` |
| 9 | Pay the reconcile debt listed below. | `taskmd/__main__.py`, `docs/bindings/local-markdown.md`, `CLAUDE.md` |
| 10 | Run the suite, `check`, `index`, the pre-publish check and every criterion's demonstration, and paste the actual output. | The transcript in §3 |

**Deliverable shape — decided here.**

**`--root` becomes an override, not a default.** Discovery runs when the flag is absent, so the
out-of-the-box case needs no flag at all. *Rejected:* keeping `.` as the default and adding a
separate opt-in flag for discovery — two ways to say one thing, and it would leave the case
criterion 1 is about (a fresh clone, no configuration) as the one that still needs an argument.

**A hook failure fails the command that ran it.** *Rejected:* printing a warning and exiting 0. The
argument against it is the one already settled in [T-025](T-025-let-check-notice-a-stale-generated-index.md)
— a tool that reports success over something it did not check is worse than none — and it applies
harder here, because the need this mechanism was drawn from is an external consistency check, which
is worthless if the caller can miss it.

**The launchers sit at the repository root and carry no path.** *Rejected:* a `bin/` folder, which
buys tidiness and costs the one thing the launchers exist for — being obvious to someone who has
just cloned the repository and has not read anything yet.

**Reconcile debt this task carries.** Listed rather than edited now, because a task does not fix
things outside itself (METHOD §3.3) and none of these is false yet:

- `taskmd/__main__.py`'s docstring points forward at "the launchers in T-011" as something that does
  not exist. When they exist, that sentence is describing the present.
- `docs/bindings/local-markdown.md` *After any write* prescribes two commands. It does not become
  false, but a project that declares the hook can have the second run automatically, and the binding
  should say whether that is an alternative or a supplement.
- `CLAUDE.md` *Publishing constraints* already requires paths to resolve "relative to the repository
  root, not the working directory". This task is what makes that true rather than intended.
- **[T-025](T-025-let-check-notice-a-stale-generated-index.md) §1 mitigation 1 asserts more than this
  task can deliver, and that is a question for the maintainer rather than debt to pay silently.** It
  says wiring the binding's *After any write* step to the hook "makes a stale index unreachable in
  ordinary use", leaving T-025's error for "edits made outside the hook — by hand, by another tool,
  or arriving in a merge". But taskmd never writes a task file: every task-file edit is made by an
  agent or a person, so the carve-out is the entire set and the hook catches none of it. Under R-19
  — *taskmd invokes what is configured* — the only write taskmd can hook is its own, which is
  `index` writing the generated file. A mechanism that *would* deliver the claim is a **harness**
  hook that runs `taskmd index` after an edit, and that is the project's to configure, explicitly
  out of this task's scope.

**Output paths**

- `taskmd/discovery.py`
- `taskmd/cli.py`, `taskmd/schema.py`, `taskmd/defaults/config.md`, `taskmd/__main__.py`
- `taskmd.sh`, `taskmd.ps1`
- `tests/` — new tests and the hook and discovery fixtures
- `docs/bindings/local-markdown.md`, `CLAUDE.md` — step 9
- `.github/workflows/` — **only if** step 3 chooses the CI route

The `deliverables:` field stays empty until step 10, for the reason T-019 recorded: `check`
validates that every declared path exists.

## 3. Implement

### Decisions & assumptions

- **Two root markers, not one: a config of its own, or a folder with the default `tasks_dir`
  name** — 2026-08-07, step 1. Nearest ancestor wins. Either mark alone is wrong in a way that
  matters here: the config alone would fail on any project that never wrote one, *including this
  repository*, so the tree the feature has to be proven on would be the one it could not find — and
  it would mean a clone had to write a config before the first command worked, which is the "no
  install" property in `docs/SCOPE.md` §1. The folder alone would fail on a project that renamed it,
  because the new name is only knowable from the config that has not been found yet. The default
  folder name is read out of `taskmd/defaults/config.md` rather than repeated in the code (R-1).
  *Rejected:* `.git`, which R-9 forbids — nothing in this method assumes version control — and
  which would also pick the wrong folder for a repository holding more than one project.
  *Rejected:* an environment variable, which is a value someone has to remember to set and so fails
  §1 *Invisibility* by construction.
- **`--root` is the override; discovery is the default** — 2026-08-07, step 6. Decided in `plan` and
  worth restating because it is what makes the out-of-the-box case need no argument at all.
- **A hook is a program followed by arguments, never a shell line** — 2026-08-07, step 2. This is
  the decision criterion 5 rests on: taskmd can ask whether a program is there without running it,
  so an unrunnable hook is caught when the config is read. A first token containing a slash is a
  file in the project; anything else is looked up on PATH. *Rejected:* a free shell string, which is
  more convenient to write and makes "is this runnable?" unanswerable short of running it — the
  mid-command report R-17 exists to prevent — and which would be interpreted by a different shell on
  each platform, which R-20 does not allow. The same decision is what makes the hook language-free:
  name an interpreter, or name an executable the project ships.
- **A hook's failure fails the command, and the write is not undone** — 2026-08-07, step 7. The file
  is on disk before the hook sees it, so the message says so rather than leaving the reader to
  guess. *Rejected:* a warning and exit 0, on T-025's own argument — a tool that runs your
  consistency check and reports success anyway is worse than one that never ran it.
- **The hook's output is captured and re-printed, not inherited** — 2026-08-07, step 7. Two reasons,
  and the second was not anticipated: a caller redirecting the command's output would otherwise get
  the hook's on a different stream, and the console is reconfigured to UTF-8 here while a child
  process's is not. It also made the mechanism testable in-process, which an inherited stream is not.
- **`Schema.source` became a display name rather than the path that was opened** — 2026-08-07,
  step 6. Not planned, and forced by the root becoming absolute: every `SchemaError` opens with this
  string, so without the change a config error would print one machine's disk. That is R-20, and it
  is what the pre-publish check in `CLAUDE.md` is aimed at. The latent form of this was already
  present — a project with no config printed the shipped default's absolute path — and it had never
  surfaced because the root was `.` and no test read that message.
- **What counts as a project has one home, and `check` now shares it** — 2026-08-07, step 6.
  Resolving a root asks, one folder at a time, the identical question `is_nested_project` already
  answered for skipping nested fixtures. Two copies would have drifted the first time a mark was
  added, so `cli.is_nested_project` calls `discovery.is_project` with the *resolved* tasks folder
  while discovery passes the default's.
- **A launcher must check that its candidate interpreter runs, not merely that it exists** —
  2026-08-07, step 8. Found by the launcher test failing rather than by reasoning: on Windows
  `python3` is usually a Microsoft Store stub that is on `PATH`, answers `command -v`, and then
  exits 49 telling you to visit a shop. Asking a candidate to execute nothing is the cheapest
  question that tells a real interpreter from a stub. `taskmd.ps1` tries `py` first and `taskmd.sh`
  tries it last, for the same reason from the other side.

### Escalated, not fixed here

- **`docs/bindings/local-markdown.md` *After any write* cannot be fully delegated to the hook, and
  [T-025](T-025-let-check-notice-a-stale-generated-index.md) §1 mitigation 1 says it can.** The
  binding was reconciled to state the limit. T-025's text was left alone here, because it records a
  decision the maintainer asked for and narrowing it was theirs to do — **and they did, the same
  day**: the error stands, so it is the mechanism rather than the backstop, and T-025's mitigation 1
  is now struck through with the reason. The mechanism as built runs a
  project's command after **taskmd's own** write, which is `index` regenerating the index — so
  `after_write: python -m taskmd check` collapses that step's two commands into one. What no
  configuration here can reach is the edit that makes an index stale in the first place: taskmd
  never writes a task file, so the write is one it never saw. T-025's error is therefore the
  mechanism rather than the backstop, unless a harness hook is added — which is the project's, and
  explicitly outside this task's scope.

### Outputs produced

- `taskmd/discovery.py` — the root rule and the project predicate, in one place
- `taskmd/schema.py` — `after_write` resolved at config-read time; `_display` for message paths
- `taskmd/cli.py` — `run_after_write`, discovery wired into `main`, `is_nested_project` delegating
- `taskmd/defaults/config.md` — the key and the `## The hook` section that is its only description
- `taskmd/__main__.py`, `tests/fixtures/README.md`, `docs/bindings/local-markdown.md`, `CLAUDE.md`
  — the reconcile debt from step 9
- `taskmd.sh`, `taskmd.ps1` — the launchers
- `tests/test_runtime.py` — 22 tests; `tests/fixtures/broken-hook/` — the third config-error fixture
- `tests/test_schema.py`, `tests/test_cli.py`, and three fixture configs — the new required key

### Verification

**Tests first, and they failed.** 22 written before any code, against fixtures built for the
criteria rather than for the implementation:

```
Ran 22 tests - FAILED (failures=15, errors=1)
  test_a_project_declaring_no_hook_is_unaffected ... CONFIG ERROR unknown config key(s): after_write
  test_the_write_still_happened_when_the_hook_failed ... AssertionError: False is not true
```

The second failure in that run printed an absolute path from the config-error message, which is how
the `Schema.source` decision above was found — by a test written for a different criterion.

After implementing: **114 tests, 114 pass**, up from 92.

**Criterion 6 — the root resolves from the repository.** From `docs/method/`, with no flag:

```
OK - 48 task(s), vocabulary valid, references resolve, no broken links
```

From an empty folder outside any project:

```
No taskmd project here. Looking upwards from the working directory, no folder holds
.taskmd/config.md or a 'tasks' folder. Run the command inside a project, or name one with --root.
exit=2
```

It names the two marks and no path, which is deliberate: the reader knows where they are, and
printing where the search started would put a machine's disk into output R-20 requires to be
identical everywhere.

**Criterion 1 — a clone runs unedited.** Both launchers, from the repository root, no configuration
and no arguments beyond the command:

```
sh ./taskmd.sh check     -> OK - 48 task(s), vocabulary valid, references resolve, no broken links
pwsh -File ./taskmd.ps1 check -> OK - 48 task(s), vocabulary valid, references resolve, no broken links
```

**Demonstrated on Windows only.** The environment this ran in has no Linux distribution installed
and no container runtime, so the second platform could not be run rather than being skipped. On the
maintainer's decision of 2026-08-07 this is handed to
[T-006](T-006-package-document-and-publish.md) — at packaging, or at first publication — and
criterion 1 is recorded below as **partly met** rather than quietly counted.

**Criterion 2 — the launchers carry no logic.** `taskmd.sh` was moved aside; the module and the
surviving launcher both printed the same line, and the deleted one was simply gone:

```
python -m taskmd check        -> OK - 48 task(s), ...
pwsh -File ./taskmd.ps1 check -> OK - 48 task(s), ...
sh ./taskmd.sh check          -> sh: ./taskmd.sh: No such file or directory   exit=127
```

A test asserts the stronger form continuously: neither launcher's code may contain any command
name, `--root`, or a field name, so neither can acquire logic without the suite noticing.

**Criteria 4 and 3 — a hook in another language, and its failure.** A throwaway project declaring
`after_write: pwsh -NoProfile -File hooks/audit.ps1`:

```
Wrote tasks/README.md - 1 active, 0 closed
Hook   pwsh -NoProfile -File hooks/audit.ps1
  audit: 2 markdown file(s) in tasks/, index present = True
exit=0
```

The same hook, changed to exit 7:

```
Wrote tasks/README.md - 1 active, 0 closed
Hook   pwsh -NoProfile -File hooks/audit.ps1
  audit: this project is inconsistent
HOOK FAILED   'pwsh -NoProfile -File hooks/audit.ps1' exited 7; the write happened, the check did not pass
exit=1
```

The index file was still there afterwards, which is the claim the message makes.

**Criterion 5 — an unrunnable hook is reported when the config is read.** `broken-hook` declares a
file it does not ship. All four commands refuse identically, before doing anything:

```
CONFIG ERROR  .taskmd/config.md: after_write names 'hooks/after-write.sh', which is not a file in
this project. A hook is resolved when the config is read, so a project cannot discover halfway
through a command that it had none.
exit=2
```

`index` among them, and it wrote nothing — the fixture's tasks folder still holds one file. The
other half of "unrunnable" — a program that is neither a project file nor on `PATH` — is covered by
a test rather than a committed fixture, since it needs nothing on disk to reproduce.

**Publishing checks:** `check` clean on 48 tasks; the pre-publish grep prints nothing with its
exclusion, and exactly five lines without it, all in `tests/fixtures/leak-check/samples.txt`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A clone runs with no configuration on Windows, macOS and Linux — demonstrated on at least two, with the actual command output | **partly met** | Windows is demonstrated, with both launchers and with the module directly, on a repository that has no `.taskmd/` of its own — so the no-configuration half is the real case rather than a contrived one. The second platform could not be run: no Linux distribution is installed here and there is no container runtime, and the maintainer's decision on 2026-08-07 was to hand it to T-006 at packaging or first publication. Carried by [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md), which also asks for the byte-identical index that is what R-20 actually claims |
| The launchers contain no logic: proven by deleting one and showing behaviour is unchanged | met | `taskmd.sh` was moved aside; `python -m taskmd check` and `taskmd.ps1 check` printed the same line as before, and the deleted launcher was simply absent. Review strengthened this from a one-off into something continuous: `test_neither_launcher_names_a_command_a_flag_or_a_field` fails if either launcher's code mentions any command name, `--root`, or a field name — so a launcher cannot acquire logic later without the suite saying so. The one thing they *do* carry is interpreter discovery, which is what they exist for, and it earned a fix during `implement` rather than being assumed |
| A hook is declared, invoked, and its **failure surfaces** — proven with a hook that exits non-zero | met | A hook exiting 7 produced `HOOK FAILED ... exited 7` and `index` returned 1. Two things were checked beyond the wording: the hook's own output is shown, so a project's check can explain itself rather than only failing, and the index file was still on disk afterwards — the hook runs after the write, so a failure reports a problem rather than silently undoing one, and the message says so instead of leaving the reader to find out |
| A hook written in a language other than Python is proven to run | met | Demonstrated with PowerShell — `pwsh -NoProfile -File hooks/audit.ps1` — which shares no runtime with the tool. The test covers the same claim on whatever shell the machine has, choosing `bash` where it exists and `cmd` otherwise, so it proves the point on the platform it runs on rather than skipping. The mechanism is language-free because the declaration names a program: an interpreter plus a script, or an executable the project ships |
| A missing or unrunnable hook is reported when the config is read, not mid-command (R-17) | met | `broken-hook` is the committed fixture and it is reported identically by all four commands, `index` included, which is the form of the claim that matters — it is not `index`'s check, it is the config's. `index` wrote nothing before refusing. The message names the declared value rather than a resolved path, following `_check_tasks_dir`'s precedent: the declared value is what the reader can edit, and the resolved one is a machine path. The other half of "unrunnable" — a program neither in the project nor on `PATH` — is covered by a test, since it needs nothing on disk |
| The repository root resolves from the repository, not the working directory — proven by running from a subdirectory and from outside the repository | met | From `docs/method/` with no flag, `check` reported this project's 48 tasks; from an empty folder outside any project it exited 2 and named both marks it looked for. Review exercised a third case the criterion does not name and that the fixtures make urgent: a project **nested** inside another resolves to the nearer one, so running inside `tests/fixtures/` works on the fixture rather than on the host — the same rule `check` already used to skip nested projects, and now genuinely one rule rather than two that agree |

**Also checked, beyond the criteria**

- Suite 114/114, up from 92. `check` clean on 49 tasks. The pre-publish grep prints nothing with its
  exclusion and exactly five lines without it, all in `tests/fixtures/leak-check/samples.txt`.
- **The generated index is unchanged in shape**, and re-running `index` after the whole change
  produced no diff beyond the task edits of this session — the new key is config, not a column.
- `.gitattributes` already forces `eol=lf` on every text file, so `taskmd.sh` cannot reach a Linux
  machine with CRLF line endings and a broken `#!`. Checked rather than assumed, because it is the
  single most likely way criterion 1's untested half would fail.
- **A test written for one criterion found the defect belonging to another**: asserting that no
  message carries an absolute path failed on the *config-error* message, not on discovery's, which
  is what turned `Schema.source` into a display name. That latent form predates this task — a
  project with no config already printed the shipped default's absolute path — and nothing had ever
  read that message.

**Child fix tasks raised**
- [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) — the second platform for
  criterion 1.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Review worked. Five criteria met, one partly — the platform claim rests on Windows, and T-049 carries the second platform on the maintainer's routing to T-006. Review earned three things `implement` had not: the launcher no-logic claim became continuous rather than a one-off, a nested project was shown to resolve to the nearer root, and `.gitattributes` was checked to be already forcing LF, which is the likeliest way the untested platform would have failed. |
| 2026-08-07 | → review | Implemented in plan order, and the two decisions taken before any code both held. The unplanned change was forced: a resolved root is absolute, so `Schema.source` had to become a display name or every config error would print somebody's disk — found by a test written for a different criterion, and latent long before this task. One thing was found by the suite rather than by thinking: a launcher must check that its candidate interpreter *runs*, because on Windows `python3` is a Store stub that is on PATH and exits 49. 22 tests written first and failing; 92 → 114. |
| 2026-08-07 | → planned | Ten steps, with both load-bearing decisions taken before any code because each has an obvious answer that fails a criterion. The root marker cannot be the config folder — this repository has none, so the tree that must prove the feature is the one that would fail — and it cannot be `.git`, which R-9 forbids. The hook declaration cannot be a free shell string, because criterion 5 asks whether a hook is runnable *before* anything runs it, and that is undecidable for an arbitrary shell line. Two things surfaced rather than being absorbed: criterion 1's second platform is not reachable from this session's environment and the route is the maintainer's to pick (step 3), and T-025 §1's first mitigation claims something this task cannot deliver, because taskmd never writes a task file and so cannot hook the write that makes an index stale. |
| 2026-08-07 | → specified | Hook points answered by the maintainer: one, after a write. The rejected pre-write point is recorded with its real advantage rather than dismissed, so the argument for adding it later is on the record instead of being rediscovered. Nothing else was outstanding at `specify`. Worth noting why this sits first in the project's own ordering despite being `medium`: it is the cheap blocker that releases T-006. |
| 2026-08-04 | → proposed | Raised by T-007 to carry R-18/R-19 under assumption A1. |
