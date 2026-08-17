---
id: T-164
title: Say something truthful when a migrated project runs one of the four commands
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-163, T-108]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-164 — Say something truthful when a migrated project runs one of the four commands

## 1. Specify

**Outcome**
A project whose tasks now live in GitHub Issues gets an accurate answer when it runs `context`,
`index`, `check` or `list`, instead of being told to create a folder it deliberately does not have.

**Why this one**
Found on 2026-08-17 while measuring for
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md), and recorded rather than fixed
there — it is outside that task's boundary and a silent fix would have made its record false. All
four commands exit 2 with:

```
CONFIG ERROR  <shipped default>: tasks_dir is 'tasks', but the project root has no such folder.
This project has no .taskmd/config.md, so taskmd is using its shipped default; create the folder,
or write a config naming a different one.
```

That is correct advice for a misconfigured project and wrong for a migrated one, where the absence of
the folder is the intended state. The message names the two repairs that do not apply and none of the
one that does.

**The shape of the fix is not obvious, which is why this is `specify` and not a one-line edit.**
taskmd has no way to know a project moved: there is nothing left behind to read, which is exactly what
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md)'s listing says. So the candidates
differ in what they ask a project to keep — a config naming a non-local backend, a marker file, or
nothing at all and a wider message. Each buys accuracy with a different cost, and one of them is
*leave it alone*: a message that lists a third possibility no reader can act on is worse than one that
is merely incomplete.

**Scope**
- In: what the four commands say when `tasks_dir` is absent.
- Out: making any command work against GitHub Issues. The commands are local-Markdown only, and that
  is the fact [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) documents rather
  than a defect to repair.
- Out: a fifth command. Non-goal 11.

**Inputs**
- [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 — the measured output
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — *What taskmd still gives you here*

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Does a migrated project keep anything taskmd can read?** It decides whether the fix can be
  accurate or only less wrong. **The maintainer answers, at `specify`.**

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → proposed | Raised from [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 step 1, where the four commands were run against a project with no task folder to establish what stops applying after a migration. The measurement was the deliverable; **the misleading advice in the error was a by-product**, and it is recorded there and raised here rather than fixed in place. `s` because the message is one string, and `specify` rather than `fix`-and-done because the honest message depends on whether a migrated project keeps anything taskmd can read — which nothing currently requires it to. **Not covered by the lifecycle authorisation of 2026-08-17**, which named T-108 and T-163 and explicitly excluded whatever they raise. |
