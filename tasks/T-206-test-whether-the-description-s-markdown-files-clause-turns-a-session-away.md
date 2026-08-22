---
id: T-206
title: Test whether the description's Markdown-files clause turns a session away
type: fix
status: done
phase: review
parent: T-205
blocked_by: []
related: [T-175, T-050]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-21
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-206 — Test whether the description's Markdown-files clause turns a session away

## 1. Specify

**Outcome**
The skill's shipped `description` either changes, or is shown not to need to, with the evidence either
way. The specific thing under test is whether its opening clause — *Work with tasks kept as Markdown
files* — gives a session a reason to stop in a project whose `.taskmd` config declares that its tasks
are **not** files.

**Why this one**
The owner decided on 2026-08-21 to act on
[T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md)'s negative, and
[T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) §3 step 3
turned that decision into something testable rather than a general suspicion.

**The observation, in one paragraph.** A session in a project with no instruction file of its own was
served this skill among 68 and asked *"What should I do next?"* — almost the description's own words.
It ran seven shell commands, one of which opened that project's `.taskmd` config, then listed the
project's GitHub issues and answered well from their labels. It never invoked this skill or any other.

**The hypothesis this task exists to test.** The description says two things that pull apart:

> Work with tasks kept as Markdown files … Use in a project that tracks tasks this way (a folder of
> Markdown task files, **or a .taskmd config**) when asked what to work on next…

The trigger clause admits a `.taskmd` config on its own. The opening clause promises files. The config
that session read says the opposite of files — `tasks_dir: tasks  # unused on this backend`,
`after_write: none  # taskmd writes nothing here - there are no task files` — so a session weighing the
two may take the opening clause as a reason the skill does not apply.

**The skill does apply there, which is why this matters.**
`plugin/skills/taskmd/SKILL.md:42` states it outright: *"These commands are the local-Markdown backend.
If this project keeps its tasks somewhere else, its binding supplies the operations instead — and
everything below is unchanged, which is the point."* The plugin ships that binding, and
[T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) verified taskmd's
own recipe on that same project on 2026-08-19. So a session turned away by the first clause is turned
away from a project the tool serves.

**Scope**
- In: whether the opening clause turns a session away from a non-file backend, tested rather than
  argued
- In: a change to the shipped `description` where the test supports one, and the same description left
  alone where it does not
- In: whether the change, if any, costs the cases the description currently gets right — the local
  Markdown project is the majority case and must not regress
- Out: the venue question.
  [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) settled that
  no third real venue is sought, and its step 2 records why a synthetic one is refused as *evidence*.
  A synthetic project may still be used as a **test rig** here, which is a different use and needs
  saying so in the plan
- Out: `SKILL.md`'s body and the method. Only the front-matter `description` is loaded unasked, and
  only that is under test

**Inputs**
- [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) §3 step 3 —
  the two readings, and the evidence separating them
- [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 — the observation,
  its four confounds, and what each does to the result
- [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9 — the one positive this
  question has, and the confound on it
- `plugin/skills/taskmd/SKILL.md` — the description under test, and line 42
- **A session that did not start with the wording it is testing.** A harness fixes its skill list at
  session start, so the session that edits a `description` is the one session that cannot observe the
  edit. Whatever instrument runs an arm has to be shown to have *loaded* the wording under test —
  which is a criterion below rather than a plan step, because a rig that silently ran the old text
  would produce two arms that differ in nothing and a null result that looks like an answer

**Acceptance criteria**

Written on 2026-08-22, after the owner's answer fixed the venue. They are written to make *cannot be
determined* a legitimate passing outcome: this task ends in a description that changed or was shown
not to need to, and "the rig could not tell" is one of the ways it can be shown not to have been.

- [ ] **The result names a direction and does not hedge** — the clause turns a session away, does not,
      or cannot be determined by this rig. A conclusion that reports both readings and picks neither
      fails this
- [ ] **The two arms are shown to differ only in the wording**, by diffing the rigs rather than by
      asserting it. What failure looks like: any second difference between the arms — a file, an
      instruction, a project name — which makes the comparison measure something nobody chose
- [ ] **Each arm's instrument is shown to have loaded the wording it is testing**, quoted from the run
      rather than inferred from the file on disk. A harness fixes its skill list at session start, so
      an arm that ran the old text is the failure this rig is most exposed to, and it is invisible in
      the result
- [ ] **The rig is shown able to produce a positive before any negative is believed** — at least one
      run in which the skill *is* invoked. Without that, *the session did not use the skill* measures
      the rig, and a silent instrument and a working one score alike
- [ ] **The number of runs per arm is fixed and stated before the results are read.** Adding a run
      after seeing an unwelcome one turns an experiment into iteration, and nothing in the record
      afterwards can distinguish the two
- [ ] **The local-Markdown case is shown not to regress**, under the same rig — a project that is a
      folder of Markdown task files still routes to the skill under whichever wording ends up shipped.
      It is the majority case and the scope names it
- [ ] **If the description changes, the new text is quoted beside the old and the tier-1 figure is
      re-measured by running the suite**, with the number stated. The `description` is paid on every
      turn of every session, so a wording that fixed the routing and broke the budget would be a
      regression this task caused
- [ ] **The confounds that survive the differencing are named**, and the answer says what each does to
      the result. The owner's answer of 2026-08-22 records this as the known cost of a synthetic rig:
      a surviving confound makes the result look controlled when it is not, and an unnamed one cannot
      be weighed by whoever reads the conclusion
- [ ] `check` is clean and the suite passes

**Open questions**
- ~~**How is a description change verified, given that no clean venue exists?** A description is loaded
  by a harness at session start, so the only honest test is a session — and
  [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) refused a
  synthetic project as *evidence about adopters*. Whether a synthetic project is acceptable as a **test
  rig** for a before-and-after comparison, where both runs share the same confounds and only the
  wording differs, is a different question and has not been put. **The maintainer's**, at `specify`,
  because it decides whether this task can be finished at all.~~ **Answered by the owner on 2026-08-22: a synthetic project is acceptable as a **test rig** — two runs differing only in the wording** — see the Log row of that date.
- **None outstanding.** The criteria above were written after the answer and judge the rig it
  licenses.

## 2. Plan

**Sequencing.** Steps 1-3 build the rig and prove it is a rig; step 4 is the first that could produce
a result, and it is deliberately after the instrument has been shown to load the wording under test.
A run before that would produce a number nobody could interpret.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Draft the candidate wording, and price it: the `description` is paid on every turn of every session, so a rewording that fixed routing and broke the budget is a regression this task caused. | The candidate quoted beside the current text in §3, with the character delta against the tier-1 margin |
| 2 | Build four synthetic projects — two arms on a **non-file** backend, two controls that are a folder of Markdown task files — each carrying the wording under test as a project-local skill, because a plugin's served text is a snapshot of what was installed and not of this working tree. | The rig directories, and the `diff -r` between each pair in §3 |
| 3 | **Show each arm's instrument loaded the wording it is testing**, by asking a fresh session to quote the description back. A harness fixes its skill list at session start, so an arm that ran the old text yields two identical arms and a null result indistinguishable from a real one. | The quoted description from each arm's own run, in §3 |
| 4 | **Fix the run count per arm before reading any result**, then run the routing prompt — *What should I do next?*, near the description's own words, as in the observation this task comes from. | The stated count, then the runs and whether the skill was invoked in each |
| 5 | Run the controls under both wordings, so the majority case is shown not to regress. | The control runs in §3 |
| 6 | Name the confounds that survive the differencing, and say what each does to the result. | The list in §3, one line per confound |
| 7 | Ship the change if the result supports one, leave the description alone if it does not, and re-measure tier 1 by running the suite either way. | `plugin/skills/taskmd/SKILL.md` if it changes, and the suite figure |

**Shape of the deliverable, decided — 2026-08-22.** The rig is **four project directories carrying a
project-local skill**, not a reinstall of the plugin between arms. *Rejected: editing
`plugin/skills/taskmd/SKILL.md` and re-installing for each arm*, which tests the real artifact — but
a served skill is a snapshot of the installed subtree, so each arm would need an install and an
uninstall on the owner's machine, and a failed cleanup leaves their harness serving a rig's wording.
*Rejected: a subagent as the instrument*, which does not start a session in the rig's directory and
so would not load the rig's skill at all.

## 3. Implement

### Step 1 — the candidate, and what it costs

```text
current   Work with tasks kept as Markdown files — one per task, plus a generated index, real
          dependency links and a validator — for any kind of work, not only software. Use in a
          project that tracks tasks this way (a folder of Markdown task files, or a .taskmd config)
          when asked what to work on next, or to start, specify, plan, implement, review, audit or
          close a task. Also whenever the user says taskmd.

candidate Work with tasks tracked by taskmd — one task per record, plus a generated index, real
          dependency links and a validator — for any kind of work, not only software. Use in a
          project that tracks tasks this way (a .taskmd config, whatever backend it names — a
          folder of Markdown task files, an issue tracker, anything else) when asked what to work
          on next, or to start, specify, plan, implement, review, audit or close a task. Also
          whenever the user says taskmd.

current   397 chars
candidate 457 chars
delta      +60 chars against a tier-1 margin of 1403
```

The margin is read from the suite rather than assumed: `tier 1 6451 chars under by 1403 (bound 7854,
reference/TASK-WORKFLOW.md)`. So the candidate is affordable. **It is not shipped**, because nothing
below produced the evidence that it is needed, and criterion 1 forbids a direction the rig did not
support.

### Step 2 — the rig, and the proof it is one

Four projects, none of them this repository: `arm-old` and `arm-new` on a backend whose config says
*there are no task files*, and `ctl-old` / `ctl-new` which are a folder of Markdown task files. Each
carries the wording as a **project-local** skill, because a plugin's served text is a snapshot of what
was installed rather than of this working tree.

```text
diff -r arm-old arm-new
  3c3  < description: Work with tasks kept as Markdown files - ...
       > description: Work with tasks tracked by rigtask - ...
```

**One line differs, and it is the description.** Same for the control pair. That is criterion 2, shown
by differencing rather than declared.

### Step 3 — the instrument, and what each arm loaded

**The first attempt could not start.** On 2026-08-22 the headless CLI answered
*401 OAuth access token has expired* from the rig and from this repository alike, so no arm ran and
nothing was claimed. The owner re-authenticated the same day and the run below is the resumption;
the rig was not rebuilt, because nothing about it had changed.

**Each arm quoted the wording it was actually given**, from its own session rather than from the
file on disk:

```text
arm-old  Work with tasks kept as Markdown files - one per task, plus a generated index, real
         dependency links and a validator - ... (a folder of Markdown task files, or a .taskmd
         config) ...

arm-new  Work with tasks tracked by rigtask - one task per record, plus a generated index, real
         dependency links and a validator - ... (a .taskmd config, whatever backend it names - a
         folder of Markdown task files, an issue tracker, anything else) ...
```

That is the failure this rig was most exposed to, closed: neither arm ran the other's text.

### Step 4 — the run count, then the runs

**Fixed before any routing result was read: three runs per arm, one per control.** Nothing but this
record's own ordering attests that, which is the limit of the criterion rather than of the run —
stated because the criterion exists to stop a count moving after a result, and a reader should know
what is and is not evidence of that.

**Detection is from the event stream, not the prose.** Each run was taken with
`--output-format stream-json`, and a run counts as routing to the skill only if a `Skill` tool call
naming `rigtask` appears. The raw streams are kept beside the rig so a run can be re-read without
being re-run.

The prompt is `What should I do next?` — near the description's own words, as in the observation
[T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) recorded.

```text
ctl-old    Skill invocations: ['rigtask']    RIGTASK INVOKED: True
ctl-new    Skill invocations: ['rigtask']    RIGTASK INVOKED: True

arm-old-1  Skill invocations: ['rigtask']    RIGTASK INVOKED: True
arm-old-2  Skill invocations: ['rigtask']    RIGTASK INVOKED: True
arm-old-3  Skill invocations: ['rigtask']    RIGTASK INVOKED: True

arm-new-1  Skill invocations: ['rigtask']    RIGTASK INVOKED: True
arm-new-2  Skill invocations: ['rigtask']    RIGTASK INVOKED: True
arm-new-3  Skill invocations: ['rigtask']    RIGTASK INVOKED: True
```

**Eight of eight.** The controls answer criterion 4 before any negative is read: the rig *can*
produce a positive, so a null from it is a null rather than a silent instrument.

### Step 5 — the controls, and the majority case

`ctl-old` and `ctl-new` are a folder of Markdown task files — the case the description already gets
right and the one the scope says must not regress. Both routed to the skill. **Under the candidate
wording as well as the current one**, so the change, if it had been made, would not have cost the
majority case.

### Step 6 — the confounds that survive the differencing

Each is present in **both** arms, so none biases the comparison. What they do is bound what the
comparison could have detected, which is the half worth writing down.

| Confound | What it does to the result |
| :--- | :--- |
| **One skill in the field, not 68** | The big one. The observed session weighed this description against 67 others; a rig session has nothing to lose to, so a positive is close to forced in both arms. **This rig can detect a description that turns a session away, and cannot detect one that comes second** |
| A project-local skill, not a plugin skill | A different serving mechanism, which may carry different weight. Unavoidable: a plugin skill is a snapshot of what was installed, so an arm could not have carried its own wording |
| The skill is named `rigtask`, not `taskmd` | Necessary — under the real name the installed plugin would be served too and both arms would be contaminated. The cost is that the description's last clause, *whenever the user says taskmd*, is unexercised in either arm |
| No instruction file in the arm | A fidelity choice rather than a defect: the observed venue had none either |
| The arms hold no actual backlog | The session had nothing to route *to* and routed anyway, which makes the null slightly stronger rather than weaker |
| One model, one day | Routing is a model behaviour, not a fixed function. A null today is not a null forever |

### Step 7 — the direction, and what ships

**The clause does not turn a session away.** Three runs under the current wording, in a project whose
config says *there are no task files*, and all three invoked the skill. That is the hypothesis §1
stated, answered in the direction that requires no change.

**So the description ships unchanged**, and the candidate drafted in step 1 is not applied. Nothing
else moves: the `description` is byte-identical, so the tier-1 figure is untouched — re-measured
anyway rather than assumed, `tier 1 6451 chars under by 1403 (bound 7854)`.

**The confound that could not be removed is a task, not a caveat.** *Does not apply* and *does not
win* are different hypotheses, and only the first was tested — the observation this task came from is
consistent with both. Raised as
[T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md)
rather than tested here, because the run count was fixed before these results were read and adding a
condition after seeing a clean null is exactly the iteration criterion 5 exists to stop.

**Decisions & assumptions**

- **The rig is four project-local skills, not four plugin installs** — a served skill is a snapshot of
  the installed subtree, so an install-per-arm would put a rig's wording into the owner's harness and
  leave it there if cleanup failed - 2026-08-22.
- **A subagent is not the instrument** — it does not start a session in the rig's directory, so it
  would never load the rig's skill, and the arms would differ in nothing - 2026-08-22.
- **The candidate wording is drafted and priced but not shipped** — the evidence that it is needed is
  exactly what this run failed to produce, and shipping it would be the change criterion 1 refuses -
  2026-08-22.
- **The run count was fixed at three per arm and one per control before any result was read** - and
  the record says that only this record's ordering attests it, which is the criterion's limit rather
  than the run's - 2026-08-22.
- **A run counts as routing only on a `Skill` tool call naming the rig's skill**, read from the event
  stream. Rejected: reading the session's prose, which describes what it did and is not what it did -
  2026-08-22.
- **The description ships unchanged.** The hypothesis was tested in the direction that requires no
  change, and applying the candidate anyway would be a rewording the rig did not support -
  2026-08-22.
- **The competition hypothesis is a task, not a second condition here** - the run count was fixed
  before these results were read, so adding an arm pair after seeing a clean null is the iteration
  criterion 5 exists to stop - 2026-08-22.

**Outputs produced**

- no change to any shipped file: `plugin/skills/taskmd/SKILL.md` is byte-identical, which is this
  task's outcome in the *shown not to need to* direction
- [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md)
- the rig itself is not committed. It lives in the session scratch directory and is rebuilt by its
  own `build.py` — an instrument, not a deliverable

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| **The result names a direction and does not hedge** | met | *The clause does not turn a session away* — §3 step 7. Three runs under the current wording on a non-file backend, all three routing to the skill. The competition question is named as a **different** hypothesis and given its own task, not offered as a second reading of this one |
| **The two arms are shown to differ only in the wording**, by diffing | met | §3 step 2: `diff -r` gives one changed line, the `description`, for the arm pair and for the control pair |
| **Each arm's instrument is shown to have loaded the wording it is testing**, quoted from the run | met | §3 step 3, both arms quoted from their own sessions. Neither ran the other's text |
| **The rig is shown able to produce a positive before any negative is believed** | met | Both controls routed to the skill, §3 step 4. As it turned out no negative arrived at all, so the null is a null and not a silent instrument |
| **The run count per arm is fixed and stated before the results are read** | met, with its limit stated | Three per arm, one per control. §3 step 4 says plainly that only this record's ordering attests it |
| **The local-Markdown case is shown not to regress**, under the same rig | met | §3 step 5: both controls routed, under the candidate wording as well as the current one |
| **If the description changes, the new text is quoted beside the old and tier 1 is re-measured** | n/a, and measured anyway | It does not change. The candidate is quoted beside the current text in §3 step 1 with its +60-char cost, and the suite was re-run: `tier 1 6451 chars under by 1403 (bound 7854)` |
| **The confounds that survive the differencing are named**, with what each does to the result | met | §3 step 6, six of them, one row each. The first is the one that bounds the answer, and it is why [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md) exists |
| `check` is clean and the suite passes | met | `OK - 213 task(s), ...` and the suite below |

**What this does not settle, stated plainly.** The rig serves **one** skill. It can show that a
description does not turn a session away, and it cannot show whether one comes second in a field of
sixty-eight — which is the condition
[T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) actually observed. So
this task answers the hypothesis it stated and leaves the observation it came from unexplained.
That is [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and until it runs nobody should read this null as *the observation was noise*.

**Open questions, re-read before closing.** §1 recorded one and it was answered by the owner on
2026-08-22. Nothing in §3 raised a question for the owner: the competition hypothesis is a task.

**Child fix tasks raised**
- [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md) — whether the description loses a competition, which this rig cannot see

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised as [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) §3 step 4, which is what the owner's *act on the negative* decision of the same day produces. `high` because the description is the only thing that can route an adopter's request to this skill, and an adopter is by definition someone who has not written the tool's name into their own conventions; `m` because the test is a session and the honest way to run one is still an open question. **Its scope was shaped by T-205 §3 step 3 rather than by the decision alone**: the venue's config declares a GitHub-issues backend, so the candidate defect is a specific clause pulling against another and not a general failure to trigger. Typed `fix` rather than `research` so that it ends in a description that either changed or was shown not to need to, instead of in a recommendation that needs a third task to act on it. |
| 2026-08-22 | (no change) | **The open question is answered by the owner: a synthetic project is acceptable as a test rig, run twice with only the wording changed.** Asked in the batched round of 2026-08-22. [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) refused a synthetic project as *evidence about adopters*; a differenced before-and-after needs its confounds constant rather than absent, and only the wording varies between the runs, so the refusal does not reach this use. *Rejected: wait for a real adopter venue*, which would make the evidence about adopters directly, but no such venue exists, so the task could not be finished at all. *Rejected: change the wording on reasoning alone*, cheap and the clash between the two clauses is plain in the text, but this task exists to produce evidence either way. **The known cost is recorded with the answer**: a confound surviving the differencing would make the result look controlled when it is not. This row is the answer, not authorisation to start. |
| 2026-08-22 | → specified | **Specify agreed: nine criteria written, where §1 had carried a placeholder.** They are built around the one thing a synthetic rig is bad at — looking controlled — so four of the nine are about the instrument rather than the answer: the arms must be diffed rather than declared identical, each arm must **quote** the wording it actually loaded, the rig must produce a positive before a negative is believed, and the run count per arm is fixed before any result is read. **The third of those is the one this project has been bitten by**: a harness fixes its skill list at session start, so the session that edits a `description` cannot observe the edit, and an arm that silently ran the old text yields two identical arms and a null result indistinguishable from a real one. **`cannot be determined` is written in as a passing outcome**, because the task's stated end is a description that changed *or was shown not to need to*, and a criterion that forced a direction would steer the rig toward a usable answer. One criterion carries the tier-1 cost: the `description` is paid on every turn of every session, so a rewording is re-measured by running the suite rather than assumed cheap. Phase stays at `specify`; `plan` is not authorised (METHOD §3.1). |
| 2026-08-22 | → done | **Resumed after the owner re-authenticated, and the answer is that the clause does not turn a session away — so the description ships unchanged.** Eight runs, **eight positives**: three per arm and one per control, detected from the `Skill` tool call in the event stream rather than from the session's prose. Both arms quoted back the wording they were actually given, which closes the failure this rig was most exposed to. Both controls routed under both wordings, so the majority case is shown not to regress and the rig is shown able to fire before any null was read. **The run count was fixed at three per arm before any result was read, and the record says only its own ordering attests that** — the criterion's limit, stated rather than papered over. **The confound that bounds the answer is the field size**: the arms serve one skill and the observation this task came from happened among sixty-eight, so *does not apply* is answered and *does not win* is not. Raised as [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md) rather than tested by adding a condition here, because that is the iteration criterion 5 exists to stop. Tier 1 unchanged and re-measured anyway: 6451 chars, under by 1403. |
| 2026-08-22 | → in_progress | **Plan written and the rig built; the lifecycle stops at step 3 because the instrument cannot start.** Four synthetic projects exist — two arms on a backend whose config says there are no task files, two controls that are a folder of Markdown task files — each carrying the wording as a **project-local** skill, because a served skill is a snapshot of the installed subtree and editing this working tree would not reach any session. `diff -r` shows each pair differing on **one line**, which is criterion 2 met by differencing rather than by assertion. The candidate wording is drafted and priced: **+60 chars against a tier-1 margin of 1403**, read from the suite. **Then `claude -p` returned *401 OAuth access token has expired* — from the rig and from this repository alike**, so no arm ran. **This is deliberately not recorded as *cannot be determined by this rig***: that verdict is available under criterion 1 and has not been earned, because what is missing is one authentication the owner can restore, not a limit of the experiment — and a record saying otherwise would leave the next reader believing the description was tested. **Status is `in_progress` and not `blocked`**: nothing in the task graph holds this up, and `blocked` with no dependency is a claim the graph does not support. Phase stays at `implement`; it resumes at step 3 with the rig already built. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: the lifecycle may honestly end at *cannot be determined*, and that is not a failure to finish it.** A harness fixes its skill list at session start, so each arm needs an instrument that did not start with the wording it is testing — recorded in *Inputs*. If no such instrument can be shown to have loaded the text, the criteria say to report that rather than to force a direction. |
