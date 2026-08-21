---
id: T-206
title: Test whether the description's Markdown-files clause turns a session away
type: fix
status: proposed
phase: specify
parent: T-205
blocked_by: []
related: [T-175, T-050]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-21
updated: 2026-08-21
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

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**How is a description change verified, given that no clean venue exists?** A description is loaded
  by a harness at session start, so the only honest test is a session — and
  [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) refused a
  synthetic project as *evidence about adopters*. Whether a synthetic project is acceptable as a **test
  rig** for a before-and-after comparison, where both runs share the same confounds and only the
  wording differs, is a different question and has not been put. **The maintainer's**, at `specify`,
  because it decides whether this task can be finished at all.~~ **Answered by the owner on 2026-08-22: a synthetic project is acceptable as a **test rig** — two runs differing only in the wording** — see the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised as [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) §3 step 4, which is what the owner's *act on the negative* decision of the same day produces. `high` because the description is the only thing that can route an adopter's request to this skill, and an adopter is by definition someone who has not written the tool's name into their own conventions; `m` because the test is a session and the honest way to run one is still an open question. **Its scope was shaped by T-205 §3 step 3 rather than by the decision alone**: the venue's config declares a GitHub-issues backend, so the candidate defect is a specific clause pulling against another and not a general failure to trigger. Typed `fix` rather than `research` so that it ends in a description that either changed or was shown not to need to, instead of in a recommendation that needs a third task to act on it. |
| 2026-08-22 | (no change) | **The open question is answered by the owner: a synthetic project is acceptable as a test rig, run twice with only the wording changed.** Asked in the batched round of 2026-08-22. [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) refused a synthetic project as *evidence about adopters*; a differenced before-and-after needs its confounds constant rather than absent, and only the wording varies between the runs, so the refusal does not reach this use. *Rejected: wait for a real adopter venue*, which would make the evidence about adopters directly, but no such venue exists, so the task could not be finished at all. *Rejected: change the wording on reasoning alone*, cheap and the clash between the two clauses is plain in the text, but this task exists to produce evidence either way. **The known cost is recorded with the answer**: a confound surviving the differencing would make the result look controlled when it is not. This row is the answer, not authorisation to start. |
