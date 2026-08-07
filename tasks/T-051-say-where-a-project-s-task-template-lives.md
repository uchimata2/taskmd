---
id: T-051
title: Say where a project's task template lives
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-003, T-001]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-051 — Say where a project's task template lives

## 1. Specify

**Outcome**
An agent creating a task in a project it has not seen before can find that project's template, or is
told plainly that there is none and what to do instead.

**Why this one**
Found while writing the skill ([T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md))
and raised rather than absorbed, per `docs/METHOD.md` §3.3.

[`docs/bindings/local-markdown.md`](../docs/bindings/local-markdown.md) *create* says **"Copy the
template"**. Nothing says where the template is. The schema
([`taskmd/defaults/config.md`](../taskmd/defaults/config.md)) names every key that exists and none of
them names a template, and `check` therefore cannot report a missing one. This repository keeps its
template at `tasks/_templates/task-template.md` and that path appears in `../CLAUDE.md` — so the
convention exists here and is invisible to an adopting project, which is exactly the shape of defect
`docs/BINDING.md` §4 was written to catch: a premise about the adopting project that was never
surfaced to be checked.

**Not urgent, and worth saying why.** Nothing is broken today: creating a task without a template
still produces a file `check` accepts, because the schema is what `check` validates and the template
is only a convenience. The cost is a worse first task in every project that adopts taskmd, and one
more thing an adopter has to be told rather than shown.

**Requirements served**
R-11, R-13, R-17 (`docs/SCOPE.md`).

**Scope**
- In: where the answer belongs — the schema, the binding, or the convention the binding already
  relies on when it skips `_`-prefixed folders while enumerating.
- In: what happens when a project has no template at all, which must be a supported state rather
  than an error.
- Out: changing the template's content, and validating templates — [T-032](T-032-repair-the-audit-template-and-validate-templates.md) holds both.
- Out: adding a command. `docs/SCOPE.md` non-goal 11 still stands after its 2026-08-05 amendment.

**Inputs**
[`docs/bindings/local-markdown.md`](../docs/bindings/local-markdown.md) *create* and *enumerate*,
[`taskmd/defaults/config.md`](../taskmd/defaults/config.md),
[`docs/BINDING.md`](../docs/BINDING.md) §2 and §4,
[T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) — the schema-is-configuration
decision this would extend.

**Acceptance criteria**
- [ ] An agent that has read only the binding and the schema can locate a project's template, or
      knows there is none — checked by doing it on a project other than this one
- [ ] A project with no template is a supported state, and nothing reports it as a problem
- [ ] Whatever carries the answer does not become a second copy of a path this repository already
      writes down in `../CLAUDE.md`
- [ ] If the answer is a new config key, it is a required key like every other one, and
      `taskmd/defaults/config.md` documents it — the schema has no optional keys, by T-001

**Open questions**
- **Is a config key the right shape, or a convention the binding states?** A key is checkable and
  costs every adopting project a line they must write; a convention costs nothing and cannot be
  validated. `plan` decides, after looking at what `check` could actually report in each case.

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
| 2026-08-07 | → proposed | Raised from T-003, which needed to tell an agent how to create a task and found that the binding's *create* names a template the project has no way to locate. Not fixed there: T-003's scope puts the CLI and the schema out, and this is a premise about the adopting project rather than something T-003 made false — so METHOD §5's distinction applies and it is a finding, not reconcile debt. `medium`/`s` because nothing is broken until someone adopts taskmd, and T-006 is the task that makes that possible. |
