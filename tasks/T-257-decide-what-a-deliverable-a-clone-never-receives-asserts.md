---
id: T-257
title: Decide what a deliverable a clone never receives asserts, and get CI green
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-103, T-089, T-090, T-250]
work_package: M7
owner: the project owner
business_value: critical
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/docs/bindings/local-markdown.md
  - tasks/T-250-give-the-context-registers-the-permitted-shape-for-history.md
---

# T-257 — Decide what a deliverable a clone never receives asserts, and get CI green

## 1. Specify

**Outcome**
A decision, written where a project reading this method will find it, on what `deliverables` asserts
when the artefact **exists and is deliberately never tracked**. Applied, so `check` exits 0 in a clone
and the `tests` workflow is green.

**Why this one**
**CI has been red on every push since 2026-08-23, 18 consecutive runs, and the whole value of that
job is that green means something.** Its own header states the position: *it is GREEN, and every
failure is now a regression*. A permanently-red job cannot show a regression, so the project has been
without its only Linux signal for a day — and every run since has been unreadable rather than merely
failing.

**One defect, reproduced rather than inferred.** The working tree passes and a clone does not:

```
git clone <this repo> /tmp/clone && /tmp/clone/plugin/bin/taskmd check --root /tmp/clone
MISSING OUTPUT T-250 declares 'control/LOCAL-CONTEXT.md', which does not exist
1 problem(s) - 256 task(s) ...
```

Working tree: exit 0. Clone: exit 1. `control/` is gitignored on purpose —
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md) put it there to quarantine
local-only information — so the file exists here, always will, and no clone will ever have it.
[T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) declared it on closing
today, and three test modules fail from that single `check` exit: `tests/test_cli.py`,
`tests/test_publishing.py`, `tests/test_runtime.py`.

**A survey, so the fix is not mistaken for the class.** All 374 declared paths across the 162 tasks
that declare any were tested against `git ls-files`. **Exactly one** is absent from a clone; eight
others flagged by a first pass were fixture *directories*, tracked through their contents, and are
false positives of that check rather than defects.

**This is a third case the recorded decisions do not cover.**
[T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) settled the **open**
task. [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) has the **cancelled**
one. [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) settled
**moved** — declared outputs follow the artefact — and said a deletion is not a move. **Not moved,
not deleted, and not missing: present, and permanently invisible to every reader but one.** T-103 was
itself raised as `R-5` by the first adopting project over this same path, so this is the second time
this exact file has exposed a gap in the same rule.

**Scope**
- In: what `deliverables` asserts for an artefact that exists but is never tracked, and where that is
  written — the method, the binding, or both, following T-103's split
- In: applying it, so a clone's `check` exits 0 and the workflow is green
- In: whether `check` should say *a clone would not receive this* rather than *does not exist*, since
  it already draws that distinction for documents and not for declared outputs
- Out: changing what `check` reports about a path that is genuinely gone. That is right under any
  answer
- Out: the audit. [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
  would have met this in cycle 7, and a gate red today cannot wait for it

**Inputs**
- [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) — the closest
  recorded decision, and the one that names this same file as `R-5`
- [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) — the record carrying
  the declaration
- `.github/workflows/tests.yml` — what the job asserts about itself

**Acceptance criteria**
- [ ] The decision is written in the method or the binding, and says which of the three readings was
      taken and what the other two cost
- [ ] A **fresh clone** exits 0 on `check`. A green working tree proves nothing — it is the tree that
      has been passing throughout
- [ ] The `tests` workflow is green on a real push, verified by reading the run rather than by
      predicting it
- [ ] The survey above is recorded, so a later reader knows the class was one and not one-of-many

**Open questions**
- ~~**Which reading?**~~ **Answered by the owner on 2026-08-23: unblock now, fix properly after** —
  reading 1 today so the gate recovers, then reading 2 as a follow-up. Asked as a survey with all
  three priced both ways. **Both halves are the answer, and the second half is the one that gets
  lost**: the plan must raise the checker change as its own record before the one-line edit lands, so
  it does not depend on anyone remembering a red job that is no longer red. The owner named that risk
  in the option they chose. The three readings, unchanged:
  1. **A deliverable names something a reader can obtain** — so an untracked artefact is not declared,
     and T-250's line is removed with a Log row saying it was produced and is quarantined. *Cheapest,
     loses the record that T-250 produced the file.*
  2. **`check` learns the distinction** — it already reports *83 document(s) not read: a clone would
     not receive them*, and applies no such awareness to `deliverables`. Reporting the same way here
     makes the asymmetry go away. *Truest to what happened, and it is a product change that ships.*
  3. **Track the file.** *Rejected on sight and named only so the record shows it was considered — it
     is quarantined deliberately and the publishing constraints forbid machine-local data.*

  **Recommendation: 2, with 1 as the immediate unblock if the decision needs longer than the gate can
  wait.** The asymmetry in `check` is a real defect an adopter meets the first time they gitignore
  anything a task produced, and this project has now met it twice.

## 2. Plan

**Ordered by the owner's answer, not by convenience.** The follow-up is step 1 because the answer
names its own failure mode: a fix that only the pain argues for loses its constituency the moment the
pain stops. Once step 3 lands, the gate is green and nothing is left pushing for step 1.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Raise reading 2 as its own record: `check` learns the distinction it already draws for documents, and reports *a clone would not receive this* rather than *does not exist* for a declared output. Raised **before** step 3's edit lands. | A new task file at `proposed`, carrying a soft edge to this one |
| 2 | Write the decision in the binding, beside T-103's *moved* and *deleted* paragraphs — the block that assigns METHOD rule 5's closing conditions, where `deliverables` is defined and where a reader chasing a `MISSING OUTPUT` lands. It says which reading was taken and what the other two cost. | A paragraph in `plugin/skills/taskmd/docs/bindings/local-markdown.md` |
| 3 | Apply reading 1: drop `control/LOCAL-CONTEXT.md` from T-250's `deliverables`, with a Log row on that record saying the file was produced and is quarantined — so removing the declaration does not also remove the fact. | `tasks/T-250-give-the-context-registers-the-permitted-shape-for-history.md`, edited |
| 4 | Record the survey in §3 — 374 declared paths across the 162 tasks that declare any, one absent from a clone, eight fixture *directories* that a first pass flagged and that are tracked through their contents. | The survey, in §3 |
| 5 | Verify in a **fresh clone**, not in this tree: clone the repository, run `check --root` against the clone, capture the exit code separately from any pipe. | The command and its exit code, in §3 |
| 6 | Push, then **read** the workflow run. A prediction is not the criterion. | The run's own verdict, in §3 |

**Outputs this task will produce**

- `plugin/skills/taskmd/docs/bindings/local-markdown.md`
- `tasks/T-250-give-the-context-registers-the-permitted-shape-for-history.md`

The step 1 record is a task rather than an output, so it is not listed here.

## 3. Implement

**Decisions & assumptions**
- **The decision goes in the binding and not in METHOD** — T-103's split, followed deliberately.
  METHOD names no field, and this answer is about `deliverables`; METHOD rule 5 already carries the
  principle it rests on. Change either and the other stays true, which is the test for whether a
  second statement is a copy — 2026-08-23.
- **The paragraph names its own successor.** It says it is superseded when T-258 ships, because a
  reading taken to recover a gate should not read as the settled answer once the gate is fine —
  2026-08-23.
- **The survey was re-derived, not copied from §1.** A figure quoted in a spec may never have been
  run, and it is the baseline the whole *one, not one-of-many* claim rests on — 2026-08-23.

**Evidence — what was actually run**

**The survey, re-derived on 2026-08-23.** Every `deliverables:` value in `tasks/` tested against
`git ls-files`, counting a path tracked through its contents as present:

```
tasks declaring any deliverable: 162
declared paths total: 373
absent from a clone entirely: 0
directories, tracked through contents: 8   (all T-002, tests/fixtures/broken-*)
```

This reproduces §1's survey exactly — 374 paths and one absent before the edit, 373 and none after —
and the eight are the same fixture directories. **The class was one and it is now zero.**

**The clone, and the delta rather than the exit code.** A clean clone of this repository, the same
command run twice, one commit apart:

```
clone @ HEAD~1 : check --root <clone>  ->  rc=1
                 MISSING OUTPUT T-250 declares 'control/LOCAL-CONTEXT.md', which does not exist
                 1 problem(s) - 257 task(s) ...
clone @ HEAD   : check --root <clone>  ->  rc=0
                 OK - 258 task(s) ...
```

The failing run is what makes the passing one worth anything: the instrument was shown able to fire
on the case it exists to catch, in the same clone, before it was shown quiet. A working tree exits 0
at both commits, which is why it went unseen for a day.

**The suite in the clone**: `350 passed, 8 subtests passed`.

**CI, read rather than predicted — and still red.** Run `32665552639` on commit `acec56b` failed.
Two of the three modules went green; `tests/test_publishing.py` stayed red on **a different and
independent cause**, which the `check` exit had been masking. Reproduced rather than inferred: the
workflow checks out shallow, a shallow clone has 0 tags, and the range `v0.5.0..v0.6.0` cannot
resolve, so `TheReleaseNoteSetIsKeyedOnWhatShips` asserts about an empty list. **Raised as
[T-259](T-259-give-ci-the-history-its-tag-range-tests-need.md), a child of this task**, because this
task's outcome includes a green workflow and it cannot deliver that alone.

**Outputs produced**
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — two paragraphs: the reading, and what it
  cost with both rejected alternatives priced
- `tasks/T-250-give-the-context-registers-the-permitted-shape-for-history.md` — one path removed from
  `deliverables`, one Log row keeping the fact the declaration carried

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is written in the method or the binding, and says which of the three readings was taken and what the other two cost | met | In the binding, beside T-103's *moved* and *deleted* paragraphs — the block a reader chasing a `MISSING OUTPUT` lands in. Reading 1 taken; reading 2 priced and raised as T-258; reading 3 recorded as rejected on sight with its ground. |
| A **fresh clone** exits 0 on `check` | met | Shown as a delta in one clone, not as an exit code: `rc=1` at `HEAD~1` naming the defect, `rc=0` at `HEAD`. §3. |
| The `tests` workflow is green on a real push, verified by reading the run rather than by predicting it | met | **Run `32666064211`: `completed success`** — the first green run after 19 consecutive failures. It took two commits, not one: run `32665552639` on this task's own fix still failed. Not this task's defect: two of three modules recovered, and the third was the shallow-checkout cause, fixed under **[T-259](T-259-give-ci-the-history-its-tag-range-tests-need.md)**, this task's child, now closed. Reading the run rather than predicting it is what found it — the local suite passed 350 tests on the same failing commit. |
| The survey above is recorded, so a later reader knows the class was one and not one-of-many | met | Re-derived rather than copied, and it reproduces §1 exactly. 373 paths, 162 tasks, 0 absent, 8 fixture directories. §3. |

**This task was held open by its child and is now released.**
[T-259](T-259-give-ci-the-history-its-tag-range-tests-need.md) closed on 2026-08-23 and
METHOD §4's rule is satisfied. The record above is left as it was written — the criterion
genuinely was unmet when this task's own fix had landed, and that is the fact worth keeping:
**one red gate had two independent causes, and the first one masked the second.**

**Adopter-visible?** yes — the binding paragraph ships, and it changes what an adopter is told to
put in `deliverables`. `adopter_visible: yes` was already set at `specify` and is unchanged.

**Child fix tasks raised**
- [T-258](T-258-report-a-declared-output-a-clone-never-receives-as-excluded-not-missing.md) — reading 2,
  raised as step 1 of the plan and **before** the unblock landed. A soft edge: this task's outcome is
  complete without it.
- [T-259](T-259-give-ci-the-history-its-tag-range-tests-need.md) — the second cause behind the red
  gate. A child, because a green workflow is part of this task's stated outcome.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | review → done | Closed once [T-259](T-259-give-ci-the-history-its-tag-range-tests-need.md), the child holding it open, was done. **CI green on run `32666064211`.** All four criteria met. |
| 2026-08-23 | planned → review | Steps 1—6 run. The decision is in the binding, the unblock is applied, and a clone exits 0 where it exited 1 one commit earlier. **CI is still red, on a second and independent cause the first was masking** — raised as [T-259](T-259-give-ci-the-history-its-tag-range-tests-need.md) and not fixed here, per the rule that a finding is not repaired where it is found. This task stays open over that child. |
| 2026-08-23 | specified → planned | Six steps, ordered so the follow-up record is raised **before** the one-line edit lands — the owner's answer names that as its own failure mode. **The owner granted `specify`, `plan`, `implement` and `review` on every task named in the handoff of 2026-08-23, in the invocation that resumed it** (*resume, all mentioned tasks with full lifecycle*). For this record that grant covers all four phases through to close. It does not reach the pre-release audit, which is gated on its own dependency and on the standing rule that a session starts no audit. |
| 2026-08-23 | proposed → specified | **The owner chose *unblock now, fix properly after* on 2026-08-23**, from a survey of all three readings priced both ways. So: drop `control/LOCAL-CONTEXT.md` from T-250's declared outputs to recover the gate today, then teach `check` the distinction it already draws for documents. **The second half is a separate record and must be raised before the one-line edit lands** — the option the owner picked names its own failure mode, which is that a follow-up loses its constituency the moment the pain stops. **The owner also ordered this ahead of T-247 and T-255**, both of which they had chosen before the red gate was found. |
| 2026-08-23 | → proposed | **Raised from the owner's report of failing CI notifications since 15:42 on 2026-08-23.** The session had run the suite green four times and pushed three commits against a red job without noticing, because `pytest` on the working tree and the workflow's per-module run in a clone are different instruments and only the second sees the defect. **Diagnosed by cloning rather than by reading**: the clone exits 1 and names one problem, the working tree exits 0. **Not fixed here.** The one-line unblock is available and the reading behind it is a policy question this project has already answered three times for three neighbouring cases, so choosing silently would set the fourth precedent without anyone deciding it. |
