---
id: T-075
title: Enforce id width when a task file is read
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-062, T-004]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-075 — Enforce id width when a task file is read

## 1. Specify

**Outcome**
`id_width` means something when tasks are read, so the binding's *enumerate* rule — keep the files
whose id matches the configured prefix **and width** — is true of the tool.

**Why this one**
Raised as **F-16** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. `Schema.is_id` compiles `^<prefix>\d+$` — prefix plus any run of digits, with
`id_width` used only by `format_id` when a new id is composed. Shown alongside T-062, on a project
using the default `id_width: 3`:

```
taskmd list --root <a scratch project>
T-0001  proposed  -  specify  over-wide id, width is 3
T-001   proposed  -  specify  SECOND file alphabetically
```

`T-0001` is accepted as a task. [`local-markdown.md`](../plugin/docs/bindings/local-markdown.md)
*enumerate* says the opposite:

> read every `.md` file; keep the ones whose `id` field matches the configured prefix **and width**.

**Consequence, stated honestly: mild.** The task loads, sorts and links; nothing is lost. What it
costs is that an id no `create` would ever produce is silently a task, so a typo in an id — the most
likely way to reach this — is indistinguishable from a deliberate one, and the file sorts by string
rather than where its number belongs. It is `low` for that reason and not because the binding's
sentence matters less than the others.

**Why it is a separate task from [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md).**
Same function, same likely commit, different evidence and different severity — T-062 loses a task,
this one accepts an odd one. Splitting them keeps each judgeable on what it actually costs, and the
soft edge records that they are one piece of work in practice. Whoever plans T-062 should plan this
with it.

**Requirements served**
R-13 (`docs/SCOPE.md`) — a binding's stated behaviour is what an adopter builds on; R-11, since
`id_width` is a config key that currently does less than the config implies.

**Scope**
- In: whether `is_id` honours `id_width`, and what happens to a file whose id does not — ignored as
  not-a-task, or reported.
- In: the third possibility, that the **binding** is what should change: a project migrating from
  another scheme may hold historical ids of mixed width, and rejecting them is not obviously right.
- Out: id format, the merge-conflict policy and the scale ceiling, all
  [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md)'s.
- Out: duplicate ids, which is T-062.

**Inputs**
`plugin/taskmd/schema.py` (`Schema.is_id`, `format_id`, `number_of`, `load_tasks`),
[`local-markdown.md`](../plugin/docs/bindings/local-markdown.md) *enumerate*,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-16.

**Acceptance criteria**
- [ ] The code and the binding agree about what `id_width` does when a task is read — whichever way
      the disagreement is resolved
- [ ] Shown failing first on a fixture, per R-16
- [ ] `tests/fixtures/alt-project`, which uses a different prefix and width, still loads unchanged
- [ ] If an out-of-width id stops being a task, that is **reported** rather than silently ignored —
      a file dropping out of the project with no signal is the failure T-062 exists to remove

**Open questions**
- **Does the code change, or the binding?** Enforcing the width makes `id_width` mean what the config
  says and turns a typo into a diagnosable error. Relaxing the binding's sentence costs nothing and
  admits mixed-width ids, which a project migrating an existing backlog would have — and non-goal 8
  puts migration tooling out of v1 while saying nothing about tolerating what a migration produces.
  `plan` decides; the maintainer's view on migrated backlogs would settle it faster.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised as F-16 from the T-059 audit, clause 1. Reproduced alongside T-062 on a scratch project: an over-wide id is accepted under `id_width: 3`. `low`/`xs` — nothing is lost, only a rule the config implies and the binding states is not applied. Split from T-062 deliberately: same function and probably the same commit, but different evidence and a different cost, and merging them would hide one behind the other. |
