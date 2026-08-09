---
id: T-051
title: Say where a project's task template lives
type: fix
status: specified
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

[`docs/bindings/local-markdown.md`](../plugin/docs/bindings/local-markdown.md) *create* says **"Copy the
template"**. Nothing says where the template is. The schema
([`taskmd/defaults/config.md`](../plugin/taskmd/defaults/config.md)) names every key that exists and none of
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
[`docs/bindings/local-markdown.md`](../plugin/docs/bindings/local-markdown.md) *create* and *enumerate*,
[`taskmd/defaults/config.md`](../plugin/taskmd/defaults/config.md),
[`docs/BINDING.md`](../plugin/docs/BINDING.md) §2 and §4,
[T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) — the schema-is-configuration
decision this would extend.

**Acceptance criteria**
- [ ] An agent that has read only the binding and the schema can locate a project's template, or
      knows there is none — checked by doing it on a project other than this one
- [ ] A project with no template is a supported state, and nothing reports it as a problem
- [ ] Whatever carries the answer does not become a second copy of a path this repository already
      writes down in `../CLAUDE.md`
- [ ] ~~If the answer is a new config key, it is a required key like every other one, and
      `taskmd/defaults/config.md` documents it — the schema has no optional keys, by T-001~~
      — **moot, and kept to say so.** The answer is a convention, so there is no key. The criterion
      was a conditional and its condition is now false; deleting it would hide that the key was
      considered and declined

**Open questions**
- ~~**Is a config key the right shape, or a convention the binding states?**~~ **Answered by the
  maintainer on 2026-08-09: a convention, stated in the binding.**

  The question asked what `check` could report in each case, and the answer is **nothing useful**.
  No code reads the template path: there is no `create` command and non-goal 11 keeps it that way,
  so the binding's *create* step — *"Copy the template"* — is performed by an agent following prose,
  not by the tool. A key would therefore be a required line in every adopting project's config,
  naming a file no command opens, which §1 *Invisibility* is exactly the property that rejects.

  **The convention is a rule, not a path**, which is what keeps criterion 3 satisfiable: *the
  template is an `_`-prefixed Markdown file in `tasks_dir`*. Nothing enumerates it, nothing can go
  stale, and a project with none is legal by construction because the rule describes where to look
  rather than what must exist. It also reuses a mechanism the binding already relies on —
  *enumerate* skips `_`-prefixed names — rather than introducing a second one.

  **Decide the shape with [T-076](T-076-decide-what-a-template-s-links-resolve-against.md).** That
  task's answer puts templates at the same depth as the tasks they become, as `_`-prefixed **files**
  in `tasks_dir`. The two answers are the same convention seen from opposite ends, and stating them
  independently would give one fact two homes.

  *Rejected: a config key.* It is checkable in principle, and that is its whole case. There is
  nothing to check until [T-032](T-032-repair-the-audit-template-and-validate-templates.md) makes
  templates validatable, and a key added now buys a line in every project's config against a
  validation that does not exist. If T-032 gives `check` something real to say about a template, the
  key can be argued for then, on evidence.

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
| 2026-08-09 | → specified | Answered: **a convention, not a config key**. The open question asked what `check` could report in each case and the answer settled it — nothing useful, because no code reads the template path: there is no `create` command, so the binding's *create* step is followed by an agent rather than executed. A required key naming a file no command opens is what §1 *Invisibility* rejects. The convention is stated as a **rule** — an `_`-prefixed Markdown file in `tasks_dir` — which is what keeps criterion 3 satisfiable, since a rule cannot become a second copy of a path. Criterion 4 is conditional on the answer being a key and is now moot; kept and marked rather than deleted. To be decided and written with T-076, whose answer is the same convention from the other end. |
| 2026-08-07 | → proposed | Raised from T-003, which needed to tell an agent how to create a task and found that the binding's *create* names a template the project has no way to locate. Not fixed there: T-003's scope puts the CLI and the schema out, and this is a premise about the adopting project rather than something T-003 made false — so METHOD §5's distinction applies and it is a finding, not reconcile debt. `medium`/`s` because nothing is broken until someone adopts taskmd, and T-006 is the task that makes that possible. |
