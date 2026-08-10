---
id: T-031
title: Give the list rationale one home
type: fix
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-022, T-027]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-06
updated: 2026-08-10
deliverables: [docs/BRIEF.md, plugin/skills/taskmd/taskmd/cli.py]
---

# T-031 — Give the list rationale one home

## 1. Specify

**Outcome**
The reason `list` exists — that grep cannot answer these questions because a derived edge is stored
nowhere — is written once, and the other places point at it.

**Why this one**
Raised as **F-5** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clause 2. The same argument, in the same words, appears in four non-task homes:

| File | Line |
| :--- | ---: |
| `docs/SCOPE.md` — non-goal 11's amendment | 152 |
| `docs/BRIEF.md` — *Commands* | 89 |
| `taskmd/cli.py` — module docstring | 12 |
| `taskmd/cli.py` — `cmd_list` docstring | 477 |

Two of them are in the same file. The phrasing is close enough that all four would have to be
revised together if the argument were ever refined — which is clause 2 exactly, and which is what
makes this a finding rather than a matter of taste.

**Task records are not copies and are out of scope.**
[T-022](T-022-filtered-task-listing-for-scripts.md) states the argument because that task is where
it was made, and [T-002](T-002-implement-the-core-cli-context-index-check.md) states an earlier
version because that is the record of what was true then. A task record is a dated account of a
decision, not a live claim to keep in step; rewriting one to match a later document would destroy
the history the method exists to keep.

**Requirements served**
R-1 (`docs/SCOPE.md`); §2 principle 3, *point, don't restate*.

**Scope**
- In: the four live homes listed above.
- Out: `tasks/`, for the reason above.
- Out: the argument itself, which is settled and correct.
- Out: `CLAUDE.md`'s statement of the design rule — that is a different fact and is
  [T-027](T-027-give-the-design-rule-one-home.md)'s.

**Inputs**
`docs/SCOPE.md` non-goal 11, `docs/BRIEF.md` §*Commands*, `taskmd/cli.py`,
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-5.

**Acceptance criteria**
- [ ] The argument is written in full in one file; the others carry a pointer of a line or less
- [ ] A grep for its distinctive phrasing returns one hit outside `tasks/`
- [ ] Both `taskmd/cli.py` docstrings still say what their reader needs at that point — the module
      docstring's job is "what is this file", `cmd_list`'s is "what does this function do", and
      neither is served by silence
- [ ] Nothing in `docs/SCOPE.md` non-goal 11 that is *not* this argument is touched; the amendment's
      carve-out wording is load-bearing and was settled in T-022

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: `docs/SCOPE.md`**, non-goal 11's amendment.
  The argument exists to justify that amendment, so the non-goal is where a reader meets the
  question; `docs/BRIEF.md` and both `taskmd/cli.py` docstrings are downstream of it and become
  pointers. *Rejected: `taskmd/defaults/config.md` §Ordering*, which already owns the ordering rule
  and claims to be its only description — but it describes *what* the order is, where this argument
  is about *why the command exists at all*, and that is a scope question.

## 2. Plan

The home already holds the argument in full, so there is nothing to write there — the work is three
deletions that must each leave their own reader served, and one grep that decides whether it worked.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Choose the phrase the grep in criterion 2 will search for, before editing anything, so the measure cannot be fitted to the result. | The phrase, recorded in §3 with its hit count before the edits |
| 2 | Trim `docs/BRIEF.md` *Commands* to a pointer, keeping what is BRIEF's own — that the surface stood at three and `list` is the exception. | The edited `docs/BRIEF.md` |
| 3 | Trim `cli.py`'s module docstring to a pointer, keeping its job: what this file is and how many commands it has. | The edited `plugin/skills/taskmd/taskmd/cli.py` |
| 4 | Trim `cmd_list`'s docstring to a pointer, keeping its job: what the function does and that it writes nothing. | The same file |
| 5 | Re-run the step 1 grep and read `docs/SCOPE.md` non-goal 11 back, to show the argument survived where it was meant to and the carve-out wording was not touched. | The two outputs in §3 |
| 6 | Run the suite, `check` and `index` — `cli.py` is code, and two docstrings are not obviously harmless. | The literal output in §3 |

**What the pointers point at, and the one thing it costs.** `docs/SCOPE.md` is not shipped: T-053
put it on the *excluded* side of the plugin boundary, as this project's own requirements rather than
anything an adopter needs. So steps 3 and 4 leave shipped source naming a document the adopter does
not receive. That is tolerated here rather than solved — `cli.py`'s module docstring already cites
`T-022`, a task no adopter has, and it shipped that way deliberately — but "tolerated" is a judgement
someone should have made on purpose, so it is raised as its own task and linked, not settled here.

**Not in scope, and not touched:** `docs/SCOPE.md` non-goal 11 itself. The argument is already
written there in full, and criterion 4 makes the carve-out wording load-bearing.

**Outputs promised**

- docs/BRIEF.md
- plugin/skills/taskmd/taskmd/cli.py
- tasks/T-031-give-the-list-rationale-one-home.md
- tasks/README.md

## 3. Implement

**Decisions & assumptions**
- **The grep phrase was fixed before any edit** — 2026-08-10, `nowhere on disk`. Chosen from the
  argument's own wording rather than from a summary of it, and checked first: 4 hits outside
  `tasks/`, which are exactly the four homes §1 lists. A phrase that had returned 3 or 5 would have
  meant §1's table was wrong and the task needed re-specifying before it needed editing.
- **The two `cli.py` copies point at T-022, not at the chosen home** — 2026-08-10, and this is a
  departure from the answer of 2026-08-07, taken because that answer cannot be carried out as
  written. `tests/test_runtime.py::ThePluginShipsWhatItCites` (T-064) forbids any file under
  `plugin/` from citing `SCOPE.md`, `BRIEF.md`, `CLAUDE.md`, an `R-NN` or a `non-goal`, because an
  adopter receives none of them. Both `cli.py` docstrings are inside `plugin/`. So "the others carry
  a pointer" is unimplementable for two of the four: the pointer they are told to carry is the one
  citation they may not make. The first draft made it anyway and the test caught it — 5 failures
  where the machine's own count is 4.
  *Rejected: moving the home into the plugin*, which reverses a maintainer decision to solve a
  wording problem. *Rejected: leaving the argument in `cli.py`*, which is the duplication this task
  exists to remove and would have passed every check, since T-064 forbids the pointer and not the
  copy. What the docstrings now say is that the argument is T-022's and lives in a paper the plugin
  does not ship — no name, so no escape, and a reader inside the repository has the task id.
- **`docs/BRIEF.md` keeps what is its own** — 2026-08-10. It still records *that* the surface stood
  at three and that `list` is the exception argued for; only the *why* left, which is what makes it
  a pointer rather than a deletion.
- **`docs/SCOPE.md` was not opened for editing** — 2026-08-10. The argument was already written
  there in full, so the home needed nothing; criterion 4 is met by the diff, which does not contain
  the file.

**Outputs produced**
- docs/BRIEF.md — *Commands*, amendment trimmed to a pointer
- plugin/skills/taskmd/taskmd/cli.py — module and `cmd_list` docstrings
- tasks/T-031-give-the-list-rationale-one-home.md — this record
- tasks/README.md — regenerated

**Evidence — the grep, before and after.** Same phrase, same scope, `tasks/` excluded as §1 requires:

```
before:  docs/BRIEF.md:89  docs/SCOPE.md:175  cli.py:12  cli.py:912
after:   docs/SCOPE.md:175
```

**Evidence — what was and was not touched.**

```
 docs/BRIEF.md                                   |  7 +++----
 plugin/skills/taskmd/taskmd/cli.py              | 13 ++++++------
 tasks/T-031-give-the-list-rationale-one-home.md | 27 ++++++++++++++++++++++++-
```

`docs/SCOPE.md` is absent from it, which is criterion 4 stated as a fact rather than as a promise.

**Evidence — the suite, `index` and `check`.**

```
=== test_budget.py (exit 0)
=== test_cli.py (exit 0)
=== test_list.py (exit 0)
=== test_runtime.py (exit 1) FAILED (failures=4)
=== test_schema.py (exit 0)
```

Four is this machine's standing count, all in `Launchers` ([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)) and absent on the Linux
runner. The fifth, which appeared and then went, is the finding recorded above.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The argument is written in full in one file; the others carry a pointer of a line or less | met, with the departure recorded | One file, `docs/SCOPE.md` non-goal 11, untouched. Three pointers, each a line or less. Two of them point at **T-022** rather than at that home — §3 records why the chosen home cannot be named from inside the plugin, and what was rejected instead. Judged met because the criterion's purpose is that the argument have one home and no copies, and it does; the pointer's target was the maintainer's choice and the departure is on the record for reversal rather than buried. |
| A grep for its distinctive phrasing returns one hit outside `tasks/` | met | `nowhere on disk`: four hits before, one after, and the phrase was fixed before the first edit so it could not be chosen to fit the outcome. The one survivor is the home. |
| Both `cli.py` docstrings still say what their reader needs | met | The module docstring still answers "what is this file": four commands, their invocations, the fourth argued for rather than added, and the module's no-hardcoded-vocabulary rule. `cmd_list` still answers "what does this function do": a subset in priority order, rendered ready to use, writes nothing. Neither is silent about the fourth command being unusual — they say it was argued for and where, which is the part a reader of the *source* needs. |
| Nothing in `docs/SCOPE.md` non-goal 11 that is not this argument is touched | met | Stronger than asked: nothing in `docs/SCOPE.md` was touched at all, shown by the file's absence from the diff rather than by inspection of the amendment. |

**Child fix tasks raised**
- none. The one thing that would have been raised — that the plugin may not cite this repository's
  own papers — turned out to be already decided and already enforced by a test (T-064), which is why
  it appears here as a departure with its reasoning rather than as a new question.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | (no change) | **Departure confirmed by the maintainer**, put to them with its alternative and answered the same day: the two `cli.py` docstrings keep pointing at T-022. *Rejected: moving the argument into a document the plugin ships*, which would make every pointer resolve for an adopter at the cost of relocating a home the maintainer had already chosen and putting this project's own scope reasoning into what adopters install. So §3's departure is now an agreed position rather than a reversible one, and the answer of 2026-08-07 stands amended rather than overridden. |
| 2026-08-10 | → done | Plan through review in one session, under the maintainer's `v0.2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1). The answer of 2026-08-07 could not be carried out for two of the four homes: T-064 forbids anything under `plugin/` from naming this repository's own papers, and it post-dates the answer. Those two now point at T-022 instead — a departure, recorded in §3 with what it rejected, and reversible if the maintainer would rather move the home. Nothing raised; the question that would have been raised was already settled and already had a test. |
| 2026-08-07 | → specified | Answered: `docs/SCOPE.md` non-goal 11. The rejection is on register rather than convenience — the config's §Ordering owns what the order *is*, and the rationale being relocated is about why `list` exists at all, which is what a non-goal amendment settles. The same distinction T-045 drew the same day between a principle and the rule it names. |
| 2026-08-06 | → proposed | Raised as F-5 from the T-026 audit, clause 2. Four live homes located by grep, two of them in one file. Task records deliberately excluded — a dated record of a decision is not a copy to keep in step. |
