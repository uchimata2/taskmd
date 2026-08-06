---
id: T-032
title: Repair the audit template, and validate templates at all
type: fix
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-003, T-022]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-032 — Repair the audit template, and validate templates at all

## 1. Specify

**Outcome**
A task created from `tasks/_templates/audit-umbrella-template.md` passes `check`, follows the
mandatory lifecycle, and carries the fields every other task carries — and a template that stops
being valid is noticed by something other than a person reading it.

**Why this one**
Raised as **F-6** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 1 and 3. Shown, not asserted — a task built from the template, with only the placeholders
filled in, run against `check`:

```
VOCABULARY    T-001.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
STORED DERIVED T-001 stores 'children:', which is computed from 'parent'; remove it

2 problem(s) over 1 task(s)
exit=1
```

Four defects, of which `check` can see the first two:

1. **`type: audit`** is not in the `type` vocabulary. There is no audit type — audit is a task
   *type* in the method's sense (METHOD §5) but the schema never gained the value, so the template
   names one the config does not have.
2. **`children: []`** is a stored derived name — the precise thing `check`'s STORED DERIVED class
   exists to catch, and the thing `tasks/_templates/task-template.md` warns against by name.
3. **No `related`, `business_value` or `effort`.** T-022's backfill updated the other template and
   left this one, so a task made from it sorts after everything estimated and shows no soft links.
4. **The body is `1. Specify / 2. Findings / 3. Resolution`** — not the four mandatory phases (R-3),
   and its fixed *Review dimensions* checklist predates
   [`docs/method/audit.md`](../docs/method/audit.md) step 2, which requires a finding threshold
   stated per audit instead.

**Why nobody saw it.** `load_tasks` skips folders whose name begins with `_`, so `_templates/` is
never enumerated and never validated — correctly, since a template is not a task, but the
consequence is that both templates can rot silently. `check_links` walks the whole tree, so a broken
*link* in a template is caught; nothing checks its front-matter.

**Why it is High.** This is the template for the audit task type, and audit is the one task type
whose whole product is traceability. [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)
will teach an agent to create tasks from these templates, and
[T-006](T-006-package-document-and-publish.md) ships them.

**Requirements served**
R-3, R-5, R-16 (`docs/SCOPE.md`).

**Scope**
- In: `tasks/_templates/audit-umbrella-template.md` — its front-matter and its body structure.
- In: a way for a template's front-matter to be checked, which is what stops this recurring.
- In: whether the `type` vocabulary gains an `audit` value, or the template uses an existing one.
  [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) itself used `analysis`, which
  is evidence that it works but not a decision that it is right.
- Out: `reference/templates/audit-umbrella-template.md`, which is prior art from another project and
  is not this repository's to correct (T-026's scope).
- Out: any new command. Non-goal 11 stands; if templates are to be validated it is by `check`, which
  already walks the tree.

**Inputs**
`tasks/_templates/audit-umbrella-template.md`, `tasks/_templates/task-template.md`,
`taskmd/defaults/config.md` §*Vocabularies*, `taskmd/schema.py` (`load_tasks`),
`docs/method/audit.md`, [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-6.

**Acceptance criteria**
- [ ] A task created from the template, with placeholders filled in and nothing else changed, passes
      `check` — demonstrated by running it, per `CLAUDE.md` *Verifying*
- [ ] The template's body carries the four mandatory phases, and the findings table lives inside
      that structure rather than replacing it
- [ ] It carries every front-matter field `task-template.md` carries, or states why one is absent
- [ ] **The failure is caught mechanically from now on** — shown by breaking a template on purpose
      and watching the check report it, per R-16. A fix that leaves templates unvalidated has fixed
      today's instance and not the class
- [ ] Whatever the audit-type decision is, it is recorded with the alternative that was rejected —
      the template and the vocabulary must not disagree again

**Open questions**
- Does the `type` vocabulary gain `audit`, or does an audit use `analysis`? Adding a value is
  config, so it is cheap; but METHOD §5 calls audit a task type in a sense the schema's `type` field
  may not be meant to carry, and T-026 ran fine as `analysis`. — maintainer; it decides what the
  template says, so it blocks `specify`.

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
| 2026-08-05 | → proposed | Raised as F-6 from the T-026 audit, clauses 1 and 3. Proven by building a task from the template and running `check`, which reported two classes; the other two defects are structural and invisible to it. The audit that found this is the one that would have been created from the template. |
