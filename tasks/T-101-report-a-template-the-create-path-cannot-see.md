---
id: T-101
title: Report a template the create path cannot see
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-032, T-051, T-076, T-091]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-101 — Report a template the create path cannot see

## 1. Specify

**Outcome**
A project that keeps its task templates one level down is told that nothing will find them, instead
of being read as a project that has no template — which is a legal state and looks identical.

**Why this one**
Raised as **R-3** by the first adopting project (`control/LOCAL-CONTEXT.md`), and it is the half of
R-3 that [T-032](T-032-repair-the-audit-template-and-validate-templates.md) does not already carry.

The binding defines a template as a `_`-prefixed Markdown file **directly in** `tasks_dir`, and says
listing them is how you find one. That project kept both of its templates in `tasks/_templates/` — a
folder `enumerate` skips because its name begins with `_`. The listing returned nothing, and the
binding's documented reading of nothing is that *a project with no template is a normal project*. The
silence runs both ways: nothing reports a missing template, and nothing reports one that is present
and unreachable.

**`_templates/` is not a mistake an adopter has to be careless to make** — it is the obvious place to
put templates, and this repository put them there too until
[T-076](T-076-decide-what-a-template-s-links-resolve-against.md) moved them out. So this repository
can no longer reach the case by accident, and the adopter is the evidence for it.

**What it cost there.** A decision task open for two days, and a project running with two task
templates at once without a single document mentioning the second — the shipped
`_task-template.md` had arrived at the compliant location during migration, referenced by nothing and
declared by no task. An agent following the create procedure finds *that* one. Discovery was not
broken any more; it was wrong in a way that looks correct. The stray-copy half is
[T-091](T-091-make-the-shipped-task-template-survive-being-copied.md)'s; the unreachable half is this.

**Requirements served**
R-16 (`docs/SCOPE.md`) — a class the validator does not catch. R-17, since it is a setup fact that
currently surfaces, if at all, inside whatever task the agent was trying to create.

**Scope**
- In: one line from `check` — R-3 suggests `TEMPLATE UNREACHABLE` — for a `_`-prefixed folder under
  `tasks_dir` holding Markdown whose id is a placeholder rather than a valid id.
- In: what makes a file in such a folder a *template* rather than somebody's notes, since the folder
  is skipped precisely so a project can keep things there.
- Out: validating a template's front-matter. That is
  [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s second in-scope item and this
  task must not duplicate it.
- Out: a config key naming a template folder. The binding argues the location rule down to *there is
  no path to be told and none to go stale*, and a key would undo that rather than fix this.
- Out: reporting that a project has **no** template. The binding states that as a legal, deliberate
  silence, and it stays one.

**Inputs**
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, *create* → *Which template*, and
  *enumerate*.
- `plugin/skills/taskmd/taskmd/schema.py` — `load_tasks` and the `_`/`.` folder skip.
- [T-076](T-076-decide-what-a-template-s-links-resolve-against.md), for why the location rule is what
  it is, so a fix does not weaken it.

**Acceptance criteria**
- [ ] Shown failing first, per R-16: a fixture with a template under `tasks/_templates/` is reported
- [ ] A project with a compliant `_`-prefixed template in `tasks_dir` stays silent
- [ ] A project with no template at all stays silent — the legal case above
- [ ] Something the project keeps in a `_`-prefixed folder that is *not* a template does not produce
      the line, or the rule says plainly why it does
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- **What identifies a template inside a skipped folder?** *Recommended: a Markdown file whose id
  field is present and is neither a valid id nor a near miss* — that is the test `load_tasks` already
  applies to `tasks/_task-template.md`, so it names no new rule and no new configuration.
  *Alternative: any Markdown in a `_`-prefixed folder*, which is simpler and reports a project's
  scratch notes as a broken template. The maintainer decides.

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
| 2026-08-10 | → proposed | Raised as R-3 from the first adopting project's recommendations — the half T-032 does not carry. T-032 already wants a template's front-matter validated; this is the case where the file is never opened at all, because it sits in a `_`-prefixed folder that `enumerate` skips, and the resulting silence reads as the legal "this project has no template". `medium` rather than high because the cost is a slow discovery rather than a wrong answer, and because T-076 has already moved this repository's own templates out of that folder; the adopter is the only evidence, which is exactly why it is worth having. `s` because the information is in hand during the walk `check` already does. |
