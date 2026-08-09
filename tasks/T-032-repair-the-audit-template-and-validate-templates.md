---
id: T-032
title: Repair the audit template, and validate templates at all
type: fix
status: specified
phase: specify
parent: T-026
blocked_by: []
related: [T-003, T-022, T-036]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-06
deliverables: []
---

# T-032 — Repair the audit template, and validate templates at all

## 1. Specify

**Outcome**
A task created from `tasks/_audit-umbrella-template.md` passes `check`, follows the
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
   exists to catch, and the thing `tasks/_task-template.md` warns against by name.
3. **No `related`, `business_value` or `effort`.** T-022's backfill updated the other template and
   left this one, so a task made from it sorts after everything estimated and shows no soft links.
4. **The body is `1. Specify / 2. Findings / 3. Resolution`** — not the four mandatory phases (R-3),
   and its fixed *Review dimensions* checklist predates
   [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 2, which requires a finding threshold
   stated per audit instead.

**Why nobody saw it.** `load_tasks` skips folders whose name begins with `_`, so `_templates/` was
never enumerated and never validated — correctly, since a template is not a task, but the
consequence is that both templates can rot silently. `check_links` walks the whole tree, so a broken
*link* in a template is caught; nothing checks its front-matter.

> **The mechanism above changed under this task on 2026-08-09, and the conclusion did not** —
> [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) moved both templates out of
> `_templates/` and into `tasks/` as `_`-prefixed files. There is no skipped folder any more:
> `load_tasks` now **reads** each template and discards it because `id: T-NNN` is neither a valid id
> nor a near miss. Still unvalidated, still silent — but by a rule about the file's *content* rather
> than about where it sits, which is a much shorter distance to travel for this task's second
> in-scope item below. Recorded rather than rewritten, because the paragraph is why F-6 went
> unnoticed for as long as it did, and that is a fact about the past.

**Why it is High.** This is the template for the audit task type, and audit is the one task type
whose whole product is traceability. [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)
will teach an agent to create tasks from these templates, and
[T-006](T-006-package-document-and-publish.md) ships them.

**Requirements served**
R-3, R-5, R-16 (`docs/SCOPE.md`).

**Scope**
- In: `tasks/_audit-umbrella-template.md` — its front-matter and its body structure.
- In: a way for a template's front-matter to be checked, which is what stops this recurring.
- In: whether the `type` vocabulary gains an `audit` value, or the template uses an existing one.
  [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) itself used `analysis`, which
  is evidence that it works but not a decision that it is right.
- Out: `reference/templates/audit-umbrella-template.md`, which is prior art from another project and
  is not this repository's to correct (T-026's scope).
- Out: any new command. Non-goal 11 stands; if templates are to be validated it is by `check`, which
  already walks the tree.

**Inputs**
`tasks/_audit-umbrella-template.md`, `tasks/_task-template.md`,
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
- None. **Q1 — does `type` gain `audit`? — answered by the maintainer on 2026-08-06: yes.**

  The answer given was that an audit task runs the same pipeline as any other task. That settles the
  doubt the question was raised on rather than sidestepping it: `type` and `phase` are **orthogonal**
  fields, and every value already in the vocabulary goes through all four phases. So "it has a full
  lifecycle" is an argument *for* the value, not the reason to withhold it — `type` records what kind
  of work a task is, and audit is a kind of work.

  The deciding argument is drift. METHOD §5's first line is *"An audit is a task type, not a
  phase"*; if the schema's `type` field has no such value, the method's word and the schema's field
  name different things, which is what this plugin exists to remove. T-026 running as `analysis` is
  evidence the field tolerates the substitution, not that the substitution is right — and it makes
  audits unfindable as a class, since `list` filters on the value that is stored.

  *Rejected: keep using `analysis`.* It costs nothing today and leaves the template naming a value
  the config does not have — which is this finding, unfixed.

**Deliberately not answered here — the audit *workflow*, which is a different subject**

The answer to Q1 arrived with a fuller account of how an audit should run: `specify` carries goals
and requirements, `plan` researches and produces the audit procedure for that particular audit,
`implement` performs it and records findings; plus a separate case — a user asking for a **task's
plan** to be audited.

Most of it is already written, and where it is not, **it does not belong in this task**:

- Scope-first, threshold-before-looking, findings-in-the-umbrella and close-only-when-children-resolve
  are [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) steps 1–5. The mandatory lifecycle is METHOD
  rule 2.
- **Genuinely new:** that the audit *procedure* is designed in `plan`, per audit. That is an addition
  to `audit.md`.
- Writing any of it into the template is the defect this task exists to fix. F-6 is a template that
  had rotted into a stale second copy of the method; repairing it by copying more method into it
  reproduces the fault at a larger size.

Split out as [T-036](T-036-say-where-a-plan-is-revised-and-that-it-is-not-an-audit.md), which also
carries the plan-audit case — where the answer given is argued **against**; see that task.

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
| 2026-08-09 | (no change) | Reconciled by [T-076](T-076-decide-what-a-template-s-links-resolve-against.md), which moved both templates from `tasks/_templates/` to `tasks/` as `_`-prefixed files. Four path references updated — Outcome, defect 2, Scope *In*, Inputs — and *Why nobody saw it* annotated rather than rewritten: its mechanism is now historical, its conclusion still holds, and it is the record of why F-6 survived. **Not a status change**: nothing about this task's four defects or its criteria moved, and the second in-scope item — a way for a template's front-matter to be checked — got closer rather than different, since `load_tasks` now reads the file and rejects it on its id instead of never opening it. |
| 2026-08-06 | → specified | Q1 answered by the maintainer: `type` gains `audit`. The answer's own reasoning — that an audit runs the same pipeline as any other task — is what settles it, since `type` and `phase` are orthogonal and every existing value already runs all four phases; the deciding argument is that METHOD §5 calls audit a task type while the schema has no such value, which is the drift this plugin exists to remove. No criterion amended; criterion 5 already required the rejected alternative to be recorded and it now is. The answer also carried an account of the audit *workflow* — two method changes that would have widened this task into the thing it was raised to fix, so they are split to T-036, one agreed and one argued against there rather than here. |
| 2026-08-06 | → proposed | Raised as F-6 from the T-026 audit, clauses 1 and 3. Proven by building a task from the template and running `check`, which reported two classes; the other two defects are structural and invisible to it. The audit that found this is the one that would have been created from the template. |
