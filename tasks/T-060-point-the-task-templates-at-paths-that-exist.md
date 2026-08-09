---
id: T-060
title: Point the task templates at paths that exist
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-032, T-051]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-060 — Point the task templates at paths that exist

## 1. Specify

**Outcome**
Every path either template names resolves, and a later move of the same files is caught by something
other than a person reading them.

**Why this one**
Raised as **F-2** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. Three references, all dead since
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) moved the files on
2026-08-08:

```
tasks/_templates/task-template.md:20          docs/METHOD.md
tasks/_templates/task-template.md:21          taskmd/defaults/config.md
tasks/_templates/audit-umbrella-template.md:28  docs/METHOD.md
```

`docs/` now holds `SCOPE.md` and `BRIEF.md` and nothing else; the method is at
`plugin/docs/METHOD.md` and the schema at `plugin/taskmd/defaults/config.md`.

**Why it survived a restructure that `check` guarded.** Two independent blind spots stack here. The
references are **prose inside an HTML comment**, not Markdown links, so `check_links` never reads
them — and `load_tasks` skips `_`-prefixed folders, so the templates are not tasks and nothing else
looks at them either. T-053's own criterion swept the plugin subtree for *links* that escape it and
correctly returned none.

**Why it is High for an `xs` fix.** The task template is copied into every new task. A dead pointer in
it is the first thing a new task's author is told to read, and it propagates once per task until it is
corrected — which is why it outranks larger findings in the audit's triage.

**Requirements served**
R-1 (`docs/SCOPE.md`) — the pointer is how one home stays one home; §2 principle 3.

**Scope**
- In: the three path references above, in both templates.
- In: whether anything can mechanically catch the next one — a template is a file `check` already
  walks for links, so the cheapest answer may be to make the references links.
- Out: the audit template's schema defects — `type: audit`, `children: []`, the missing estimate
  fields, the non-lifecycle body. All four are
  [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s and predate this.
- Out: validating templates as tasks, also T-032's.
- Out: where an adopting project's template lives, which is
  [T-051](T-051-say-where-a-project-s-task-template-lives.md).

**Inputs**
`tasks/_templates/task-template.md`, `tasks/_templates/audit-umbrella-template.md`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-2,
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) §3 for what moved where.

**Acceptance criteria**
- [ ] Every path named in either template resolves from that template's own location
- [ ] Shown failing first — the current templates are demonstrated to name a file that does not
      exist, before the correction, per R-16
- [ ] `check` reports the next such breakage, or it is stated why it cannot and what would
- [ ] Nothing else in either template changes — this is a path fix, and a template edited on the way
      past cannot be compared against T-032's separate work on the same file

**Open questions**
- **Do the references become Markdown links?** Making them links puts them inside `check`'s reach and
  gives criterion 3 for free. Against it: the task template's comment block is stripped by nobody, so
  every task created from it would carry two live links to project documents, which is arguably a
  pointer the task does not need. `plan` decides.

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
| 2026-08-09 | → proposed | Raised as F-2 from the T-059 audit, clause 1. Verified before write-up: `docs/` holds only `SCOPE.md` and `BRIEF.md`, so all three references are dead. `high`/`xs` because the cost is propagation — the template is copied into every new task — while the fix is three strings. Deliberately narrow against T-032, which owns the audit template's schema defects and predates the move that caused these. |
