---
id: T-061
title: Stop an inherited PYTHONPATH breaking the shell launcher
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-049, T-056, T-068]
work_package: v0.1
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-061 — Stop an inherited PYTHONPATH breaking the shell launcher

## 1. Specify

**Outcome**
`plugin/taskmd.sh` — and `plugin/bin/taskmd`, which delegates to it — finds its own package whatever
`PYTHONPATH` the caller's environment already holds.

**Why this one**
Raised as **F-3** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Reproduced across five environments, running the same `check` command
through `bash plugin/taskmd.sh`:

```
PYTHONPATH unset                  OK - 58 task(s), ...            exit 0
PYTHONPATH = a POSIX-absolute path  OK - 58 task(s), ...          exit 0
PYTHONPATH = a drive-lettered path  No module named taskmd        exit 1
PYTHONPATH = a relative path        No module named taskmd        exit 1
```

*(The two failing lines are transcribed with their leading path elided: the real output names the
interpreter's own location, and quoting it would put an absolute local path into this record.)*

**The mechanism.** The launcher builds `PYTHONPATH="$here${PYTHONPATH:+:$PYTHONPATH}"` where `$here`
is a POSIX path and `:` is hardcoded as the separator. On Windows the separator is `;` and a POSIX
path is not a path at all, so this only ever works because the shell layer rewrites the whole
variable on its way to a native process — and that rewrite is abandoned the moment one element of the
list is relative or drive-lettered. Python then receives the raw POSIX string and reports a missing
module. `plugin/taskmd.ps1` builds the same value with `[IO.Path]::PathSeparator` and native paths
and is unaffected.

**Who pays.** Anyone whose environment already sets `PYTHONPATH` — which is to say a Python developer,
the likeliest adopter. `plugin/bin/taskmd` is the command the skill names and it `exec`s this script,
so the adopter's documented entry point inherits the whole defect. The error names their interpreter
rather than taskmd, so it does not read as a taskmd problem.

**And this repository tells them to set it.** `CLAUDE.md` and `.handoff/config.md` both explain that a
bare `python -m taskmd` needs `PYTHONPATH` — advice which, followed and then left in place, breaks the
launcher the same documents recommend.

**Why the suite is green.** `tests/test_runtime.py::Launchers::test_the_shell_launcher_produces_what_
the_module_produces` runs the launcher under whatever environment the runner happens to have, and
compares it against a direct invocation given a *different*, correct environment. Under a plain run
both pass; the assertion cannot see the case it is closest to.

**Requirements served**
R-18, R-20 (`docs/SCOPE.md`) — one implementation whose launchers carry no logic, behaving identically
across platforms.

**Scope**
- In: how `plugin/taskmd.sh` composes `PYTHONPATH`, including whether it inherits an existing value
  at all.
- In: the same question asked of `plugin/taskmd.ps1`, which is believed correct and has not been
  tested against a hostile value.
- In: a regression test that fixes the environment rather than inheriting it.
- Out: `plugin/bin/*` coverage in general, which is [T-068](T-068-cover-the-entry-point-an-adopter-runs.md).
- Out: interpreter discovery, settled in [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)
  and its children.

**Inputs**
`plugin/taskmd.sh`, `plugin/taskmd.ps1`, `plugin/bin/taskmd`, `tests/test_runtime.py` (`Launchers`),
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-3.

**Acceptance criteria**
- [ ] The launcher works with `PYTHONPATH` unset, set to a relative path, set to a drive-lettered
      path, and set to a POSIX path — all four demonstrated
- [ ] Shown failing first on at least two of those, per R-16 — the current behaviour is reproduced
      before the change
- [ ] The PowerShell launcher is put through the same four values, and the result recorded either way
- [ ] A test asserts it, with the environment **set by the test** rather than inherited, so the case
      cannot go quiet again
- [ ] Whatever the launcher does with an existing `PYTHONPATH` is stated in its own comment — the
      current comment claims a property the code does not have
- [ ] No absolute path appears in this task's record (R-23)

**Open questions**
- ~~**Does the launcher keep inheriting `PYTHONPATH` at all?**~~ **Decided at `plan` on 2026-08-09:
  no — it replaces it, in both launchers.** The check the question asked for was run first; see §3 D1.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reproduce all four values against `taskmd.sh`, with a transport check first — confirm the fabricated relative and drive-lettered values reach the process intact before believing what they do there | The failing evidence, and proof it is not a quoting artefact |
| 2 | Put `taskmd.ps1` through the identical four, which criterion 3 asks for and which nobody has done | Its result, either way |
| 3 | Answer the open question's precondition: sweep the tree for anything that relies on the inherited value | The decision recorded in §3 D1 |
| 4 | Apply the decision to both launchers, and state in each comment what it now does with an existing value (criterion 5) | `plugin/taskmd.sh`, `plugin/taskmd.ps1` |
| 5 | Write the regression test with the environment **set by the test**, covering every launcher the machine can run | `tests/test_runtime.py` |
| 6 | Show the new test failing against the pre-fix launcher, then passing — a test that has only been watched passing proves nothing (R-16) | Both transcripts |
| 7 | Full suite under both documented runners, then the four values again against the fixed launchers | The §3 transcripts |

**Why step 1 leads with a transport check.** The two failing values are fabricated specimens with
backslashes and no leading slash, and both have to survive a shell that rewrites paths. A specimen
that arrived mangled would produce the same failure for the wrong reason, and the result would look
identical.

**Why step 6 is a step rather than a habit.** The defect exists *because* an assertion was only ever
watched passing. A regression test written for it and never seen red would repeat the mistake it is
there to close.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — the launcher replaces `PYTHONPATH` rather than extending it** — 2026-08-09. The question's
  own precondition was checked first: **nothing in the tree relies on the inherited value.** The only
  other `PYTHONPATH` writer is `tests/test_runtime.py`, which sets it explicitly for a *direct*
  `python -m taskmd` and never through a launcher; `plugin/bin/taskmd`'s own comment advertises "no
  `PYTHONPATH` to set"; and `taskmd` imports nothing but the standard library and itself, so there is
  no plugin surface for a caller to extend. The capability being given up has no user, today or in
  `docs/SCOPE.md`.

  *Rejected: converting `$here` to the platform's own form and keeping the inheritance.* It preserves
  something nobody uses, and it costs platform branching — a `cygpath` that exists only on Windows,
  plus separator detection — inside a file whose first comment is *"There is deliberately nothing
  here to read"*. That claim is R-18, and it is tested; spending it here would be the expensive way to
  keep a feature with no user.

  A second reason emerged while writing it down, and it is the stronger one: prepending an inherited
  path is one ordering mistake away from importing **somebody else's `taskmd`**. Replacing removes
  that class too.

- **D2 — the same change is made to `taskmd.ps1`, which was not broken** — 2026-08-09. It passed all
  four values (§3 step 2). R-20 says the two launchers behave identically, and after fixing only one
  they would have differed precisely in what they do with an inherited variable — the kind of
  difference that is invisible until it matters and then has no obvious owner. Changing it is a
  deletion of two lines, so the regression risk is close to the risk of leaving them.

- **Cost accepted, stated:** the suite goes from 1.4s to 4.0s. The new test starts a PowerShell
  process three times, and that is nearly all of it. It buys the only assertion in the suite that
  fixes its own environment, so it is worth the seconds — but it is a real change to how the suite
  feels and is recorded rather than discovered.

### Step 1 — shown failing first (R-16), with the specimens checked in transit

```
value as the shell sees it (transport check)
  drive-lettered arrives as: <a drive-lettered path, intact>
  relative arrives as:       relative/dir

sh plugin/taskmd.sh check
  PYTHONPATH unset                  OK - 76 task(s), ...        exit 0
  PYTHONPATH = POSIX absolute       OK - 76 task(s), ...        exit 0
  PYTHONPATH = relative             No module named taskmd      exit 1
  PYTHONPATH = drive-lettered       No module named taskmd      exit 1
```

The two failing lines are transcribed with the leading path elided — the real output names the
interpreter's own location under a home directory, and quoting it would put an absolute local path
into this record (R-23). This is the mistake T-013 and T-018 each made once.

### Step 2 — the PowerShell launcher, put through the same four

```
pwsh -NoProfile -File plugin/taskmd.ps1 check
  PYTHONPATH unset                  OK - 76 task(s), ...        exit 0
  PYTHONPATH = POSIX absolute       OK - 76 task(s), ...        exit 0
  PYTHONPATH = relative             OK - 76 task(s), ...        exit 0
  PYTHONPATH = drive-lettered       OK - 76 task(s), ...        exit 0
```

Four for four. F-3's reading of the two launchers was right, and it is now measured rather than
inferred from the source.

### Step 6 — the new test, shown red before green

Against the pre-fix launcher, restored for one run:

```
AssertionError: 0 != 1 : taskmd.sh with PYTHONPATH='relative/dir' exited 1: <interpreter>: No module named taskmd
1 failed, 23 deselected in 0.41s
```

Against the fixed launcher:

```
1 passed, 23 deselected in 2.51s
```

### Step 7 — validation

```
python -m pytest tests -q            117 passed in 4.04s
python -m unittest discover -s tests Ran 117 tests ... OK
taskmd check                         OK - 76 task(s), vocabulary valid, references resolve, no broken links

sh plugin/taskmd.sh check, all four values
  unset / POSIX absolute / relative / drive-lettered   OK - 76 task(s), ...   exit 0
```

**Nothing else needed changing.** `CLAUDE.md` and `.handoff/config.md` both tell a reader that a bare
`python -m taskmd` needs `PYTHONPATH` set — checked, and still true: that is advice about invoking the
module directly, and following it no longer breaks the launcher the same documents recommend, which
was the whole of the complaint.

**Outputs produced**
- `plugin/taskmd.sh` — replaces rather than extends, with the reason in its own comment
- `plugin/taskmd.ps1` — the same, for R-20 rather than for a defect
- `tests/test_runtime.py` — `test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has`,
  and `available_launchers()` beside it

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The launcher works with `PYTHONPATH` unset, relative, drive-lettered and POSIX — all four demonstrated | met | §3 step 7; and asserted by the new test on every launcher the machine can run |
| Shown failing first on at least two of those, per R-16 | met | §3 step 1 — the two that fail, with a transport check first so a mangled specimen could not be mistaken for the defect |
| The PowerShell launcher is put through the same four, result recorded either way | met | §3 step 2 — four for four, it was never broken. Changed anyway, for R-20, and that is recorded as D2 rather than folded in silently |
| A test asserts it, with the environment set by the test rather than inherited | met | §3 step 6, shown red against the pre-fix launcher before green. This is the criterion the old assertion could not meet |
| Whatever the launcher does with an existing `PYTHONPATH` is stated in its own comment | met | Both launchers say *replaced, not extended*, and `taskmd.sh` says why in the failure's own terms |
| No absolute path appears in this task's record (R-23) | met | The two places one would have appeared — step 1's failing output and step 6's assertion message — are elided. Verified by the pre-publish check, run last |

**Child fix tasks raised**
- none. All six criteria met, and the one discovery worth keeping is generic rather than actionable:
  F-3 is the environment-variable instance of a lesson already held in session memory about POSIX
  paths surviving as arguments but not inside quoted strings. It is written there, not here.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All six criteria met; 117 passing under both runners, up from 116. The launcher now **replaces** `PYTHONPATH` rather than extending it, which removes the class rather than the case — and the sweep the open question asked for found nothing in the tree relying on the inherited value, so nothing was given up that had a user. `taskmd.ps1` passed all four values and was changed anyway, for R-20: two launchers differing only in what they do with an inherited variable is a difference nobody finds until it matters. The regression test was **shown red against the pre-fix launcher before green**, which is the thing the assertion it replaces could never do — it inherited the runner's environment, so on a machine with no `PYTHONPATH` it passed while the launcher was broken for everyone who had one. Cost recorded rather than absorbed: the suite goes 1.4s → 4.0s, nearly all of it PowerShell startup. |
| 2026-08-09 | → in_progress | Plan front-loads two things the finding took on trust. First a **transport check**: both fabricated values are fabricated specimens with backslashes or no leading slash, and one that arrived mangled would fail for the wrong reason and look identical — both were confirmed intact before anything was concluded from them. Second the open question's own precondition, a sweep for anything relying on the inherited value, which is what turned a judgement call into a one-line answer. A second reason for replacing surfaced while writing it down and is the stronger one: prepending an inherited path is one ordering mistake away from importing somebody else's `taskmd`. |
| 2026-08-09 | → specified | Criteria stand as raised — six of them, and the fifth (*the launcher's comment states what it does with an existing value*) is the one that stops this being fixed without being explained. The open question is a `plan` question by its own terms and names the check that settles it, so nothing needed the owner beyond the authorisation to run the lifecycle. |
| 2026-08-09 | → proposed | Raised as F-3 from the T-059 audit, clauses 1 and 3. Reproduced across five environments before write-up; two of the five fail. `high` because it makes the adopter's own entry point fail outright for the reader most likely to have a `PYTHONPATH` set, and because this repository's own documents tell people to set one. `s` because the fix is a line or two, and the cost is deciding which line. Not fixed where it was found (METHOD §5). |
