---
id: T-259
title: Give CI the history its tag-range tests need, and make a blind instrument say so
type: fix
status: done
phase: review
parent: T-257
blocked_by: []
related: [T-243, T-116]
work_package: M7
owner: the project owner
business_value: critical
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables:
  - tests/test_publishing.py
  - .github/workflows/tests.yml
---

# T-259 - Give CI the history its tag-range tests need, and make a blind instrument say so

## 1. Specify

**Outcome**
The `tests` workflow can resolve a tag range, so the release-note assertions in
`tests/test_publishing.py` measure what they were written to measure. And where a test's input is
missing rather than wrong, it says so as a missing input rather than as a failed assertion.

**Why this one**
**This is the second defect behind the red gate, and the first one was hiding it.**
[T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md) removed a `MISSING OUTPUT`
that took `check` to exit 1 and failed three modules at once. With that gone, two modules went green
and `tests/test_publishing.py` stayed red on its own cause - which had been there the whole time and
was unreadable underneath the other.

**Diagnosed by reproducing it, not by reading the log.** `actions/checkout@v4` is used with no
`fetch-depth`, so the runner gets a shallow checkout. Measured on 2026-08-23:

```
git clone --depth 1 <this repo> <tmp>
git tag            -> 0 tags
git rev-list v0.5.0..v0.6.0
fatal: ambiguous argument 'v0.5.0..v0.6.0': unknown revision or path not in the working tree
```

`TheReleaseNoteSetIsKeyedOnWhatShips` runs its rule over `v0.5.0..v0.6.0`, gets an empty list, and
both assertions fail - one reporting that the release shipped nothing an adopter notices, which is a
statement about the checkout and not about the release.

**The failure message is about the project and the cause is about the runner, and that is the real
finding.** A reader of that CI log is told the release note dropped `T-006` and that no task is
`adopter_visible`. Both are false. A test whose input never arrived reported a verdict on the
subject instead of on itself - and a full local suite passes, because a normal clone has tags. That
is why this survived: **the gate you run is not the gate that gates.**

**Scope**
- In: giving the workflow the history and tags the range needs
- In: making the class say *the range did not resolve* rather than assert about the project, so the
  next blind instrument is legible at a glance rather than after a reproduction
- Out: changing what the release-note rule itself selects. [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md)
  settled that and the assertions are correct - they were never reached
- Out: the `deliverables` asymmetry. That is T-257 and its follow-up T-258

**Inputs**
- `.github/workflows/tests.yml` - the checkout step, and the header stating the job is green and
  every failure is a regression
- `tests/test_publishing.py` - `TheReleaseNoteSetIsKeyedOnWhatShips`, and the `skipUnless` it
  already carries for `git` and `sh`
- CI run 32665552639 - the first run where this was the only cause

**Acceptance criteria**
- [ ] The `tests` workflow is green on a real push, read from the run rather than predicted
- [ ] The class is shown **failing** when the rule is genuinely wrong, so the repair did not buy green
      by making it blind. A check that has only ever succeeded has not been tested
- [ ] A checkout with no tags produces a message naming the missing range, not an assertion about the
      release - shown by running it against a shallow clone
- [ ] The local suite and CI agree on this module, checked on the same commit

**Open questions**
- **Whether an absent range should skip or fail.** Skipping keeps the gate green and silently stops
  measuring; failing keeps the signal and is noisy anywhere without tags. A third reading is to fail
  with a message about the input. Whoever plans this - and the project's own rule that a blocked
  instrument is not a negative result argues against a plain skip.

## 2. Plan

**Two halves, and the second is the one that matters longer.** Giving the runner its history fixes
today. Making the class say *my input did not arrive* is what stops the next blind instrument
reporting a verdict on the project - and it must be written first, because once the range resolves
there is no longer a case to test it on.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Make the class detect that the range does not resolve, and fail naming the range and the likely cause instead of asserting about the release. Decide skip-versus-fail and record the rejected reading. | An edit to `tests/test_publishing.py`, and the decision in §3 |
| 2 | Show step 1 firing: run the module against a shallow clone with no tags and read the message. This is the only moment the case exists. | The message, captured in §3 |
| 3 | Give the workflow the history the range needs, at the checkout step. | An edit to `.github/workflows/tests.yml` |
| 4 | Show the class still fails when the rule is genuinely wrong - break the documented rule on a scratch copy and confirm the assertion fires. A repair that bought green by going blind would pass every other step here. | The failing run, captured in §3 |
| 5 | Run the module in a full clone, then push and **read** the run. | The run's own verdict, in §3 |

**Outputs this task will produce**

- `tests/test_publishing.py`
- `.github/workflows/tests.yml`

## 3. Implement

**Decisions & assumptions**
- **An unresolvable range fails; it does not skip** — 2026-08-23. The open question's three
  readings, decided: *fail with a message about the input* was taken. **Skip was rejected** because it
  keeps the gate green while silently ending the measurement, which is the one outcome nobody can
  notice — and this project has already met that shape. **A plain fail was rejected** too: it keeps
  the signal but says nothing about the cause, which is exactly the state that cost a day here.
- **The guard is a method on the class, called by each test that runs the command** — not
  `setUp` — 2026-08-23. `test_the_document_still_yields_a_command` reads the document and never
  runs `git`, so it is correct in a tagless checkout and must keep passing there. A `setUp` guard
  would have failed it too, and reported a git problem about a test that does not use git.
- **`fetch-depth: 0` rather than `fetch-tags`** — 2026-08-23. The range needs the commits
  *between* the two tags, not only the tag objects, so fetching tags onto a depth-1 checkout would
  leave the range still unresolvable. Rejected for being the smaller-looking change that does not
  work.

**Evidence — the two causes now give two different messages**

Step 2, the window that closes once the checkout is fixed. A **shallow** clone (`git clone --depth 1`,
`git tag` — 0 tags), running the edited module:

```
FAIL: test_the_set_contains_the_task_the_milestone_query_missed
FAIL: test_the_three_marks_partition_the_set
AssertionError: the range v0.5.0..v0.6.0 does not resolve in this checkout, so section 7's rule
was never run and nothing below is a statement about the release. This is almost always a shallow
clone: `actions/checkout` fetches depth 1 by default and a shallow checkout carries no tags.
git said: fatal: bad revision 'v0.5.0..v0.6.0'
Ran 29 tests ... FAILED (failures=2)
```

Step 4, and it is the one that matters. **The repair must not have bought green by going blind**, so
the documented rule was broken on purpose in a **full** clone — tags present, range resolving,
`rc=0` — by making section 7's `/^plugin\//` ship test unmatchable:

```
tags present: 6; range resolves rc=0
FAIL: test_the_set_contains_the_task_the_milestone_query_missed
AssertionError: [] is not true : section 7's rule run over v0.5.0..v0.6.0 does not return T-006 ...
FAIL: test_the_three_marks_partition_the_set
AssertionError: 0 is not true : no task in v0.5.0..v0.6.0 is marked adopter_visible: yes ...
Ran 29 tests ... FAILED (failures=2)
```

**The original assertions still fire on a genuinely wrong rule**, and the guard did not swallow them.
Same module, same two tests, two causes, two messages that name the right subject.

**A first attempt at step 4 proved nothing and is recorded rather than discarded.** The sabotage
substituted `git rev-list`, which does not occur in section 7's command — 0 sites — so the
document was unchanged and the run returned `OK`. A clean result from an experiment that never
started reads exactly like a passing check.

The unmodified module in a full clone: `Ran 29 tests ... OK`.

**Outputs produced**
- `tests/test_publishing.py` — a `range_resolves` helper and an `assert_range_is_available`
  guard, called by the two tests that run the command
- `.github/workflows/tests.yml` — `fetch-depth: 0` on the checkout, with a note saying what it
  is for

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The `tests` workflow is green on a real push, read from the run rather than predicted | met | Run `32666064211` on commit `abfe8b4`: `completed success`, 57s. Read with `gh run watch --exit-status`, `rc=0`. **The first green run after 19 consecutive failures.** |
| The class is shown **failing** when the rule is genuinely wrong, so the repair did not buy green by making it blind | met | §3 step 4: in a full clone with the range resolving, section 7's `/^plugin\//` ship test was made unmatchable and both original assertions fired with their own messages. **The first attempt at this proved nothing and is recorded** — it substituted a string absent from the document, so the run returned `OK` with the specimen never applied. |
| A checkout with no tags produces a message naming the missing range, not an assertion about the release | met | §3 step 2, run against a shallow clone carrying 0 tags, before the checkout was fixed. The message names the range, says the rule was never run, and points at `actions/checkout`'s depth-1 default. |
| The local suite and CI agree on this module, checked on the same commit | met | Commit `abfe8b4`, both. Local: `350 passed, 8 subtests passed`. CI: `success`. **This is the criterion the whole task exists for** — they disagreed for a day, and the local half was the one that looked trustworthy. |

**Adopter-visible?** no — `.github/workflows/tests.yml` is outside the plugin boundary and
`tests/` is not copied by an install, so nothing here reaches an adopter. `adopter_visible: no` set
at `specify` and unchanged.

**Child fix tasks raised**
- none. The guard covers the general case — any test in the class that runs the command calls it
  — so there is no residual.

**One thing worth knowing, and it is not this task's to fix.** The pipeline in section 7 exits 0 even
when its `git log` fails, which is why an unresolvable range reached an assertion at all rather than
raising in `run_shipped_set`. The guard makes that harmless here by testing the range first. Whether
the documented command should itself fail loudly is a question about
[`../docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 rather than about this test, and nothing
currently depends on it.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | in_progress → done | **CI green on run `32666064211`, the first success after 19 consecutive failures.** All four criteria met. The two causes now report separately: a wrong rule fails on the original assertions, a tagless checkout fails naming the range. Local suite and CI agree on `abfe8b4`, which is the disagreement this task existed to end. |
| 2026-08-23 | planned → in_progress | Guard written and shown firing against a shallow clone first, because that case stops existing the moment the checkout is fixed. |
| 2026-08-23 | specified → planned | Five steps, ordered so the no-tags case is exercised **before** the checkout is fixed - it is the only window in which that case exists. Step 4 exists because a repair that made the class blind would pass every other step. |
| 2026-08-23 | → specified | **Found by pushing T-257's fix and reading the run rather than predicting it.** The clone check exited 0 and the full local suite passed 350 tests, and CI was still red - on a module whose cause is the runner's shallow checkout. Raised as a child of T-257 because that task's stated outcome includes a green workflow, which it cannot now deliver alone. |
