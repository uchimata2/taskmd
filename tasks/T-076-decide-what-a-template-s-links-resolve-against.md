---
id: T-076
title: Decide what a template's links resolve against
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-060, T-032, T-051]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-076 — Decide what a template's links resolve against

## 1. Specify

**Outcome**
A template's references are correct in the template **and** in the file the template becomes, or it
is written down which of the two is given up and why.

**Why this one**
Raised from [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) §3 under METHOD §3.3 —
actionable, and outside the task that found it. T-060 made the templates' three dead references into
Markdown links, which is what put them inside `check`'s reach. A relative link is resolved against
the file that holds it, and **a template lives one directory deeper than the file it becomes**:
`tasks/_templates/` against `tasks/`. So every link correct in a template is wrong by one level once
copied. Shown, by copying one template line verbatim into `tasks/`:

```
tasks/zz-probe.md holding only the audit template's Standard compliance line
taskmd check
BROKEN LINK   tasks/zz-probe.md -> ../../plugin/docs/METHOD.md
1 problem(s) over 75 task(s)
```

**Why it is not simply T-060's to fix.** T-060's criterion 1 is *"every path named in either template
resolves from that template's own location"*, which is the base it was given and which the fix meets.
Choosing a different base is a change to that criterion, not a way of satisfying it — and the choice
is about what a template *is*, which is the same question
[T-051](T-051-say-where-a-project-s-task-template-lives.md) asks from the other side.

**The two templates are not equally affected, and that is the interesting part.**

- `task-template.md`'s references sit in an **HTML comment that instructs the author** — and **0 of
  75** task files in this repository retain it. Nothing propagates in practice, and if someone did
  keep it, `check` reports it at once, which is a fair prompt to delete a block that says "after
  filling this in".
- `audit-umbrella-template.md`'s reference is a **checklist line meant to survive** into the audit
  task. That one is copied on purpose, so the depth shift reaches a real file every time.

**Requirements served**
R-1 (`docs/SCOPE.md`) — the pointer is how one home stays one home; R-16, since the value of making
these links is that a breakage is caught rather than read.

**Scope**
- In: what a template's links resolve against, for both templates.
- In: whether the two templates get one rule or two, and if two, what makes the split not a rule
  someone has to remember.
- Out: the three paths themselves, fixed in T-060.
- Out: the audit template's schema defects, [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s.
- Out: where an adopting project's template lives, [T-051](T-051-say-where-a-project-s-task-template-lives.md)'s.

**Inputs**
`tasks/_templates/task-template.md`, `tasks/_templates/audit-umbrella-template.md`,
[T-060](T-060-point-the-task-templates-at-paths-that-exist.md) §3,
`plugin/taskmd/cli.py` (`check_links`, `markdown_files`).

**Acceptance criteria**
- [ ] A line copied from either template into `tasks/` is shown to resolve, or the case is shown and
      stated as accepted with what it costs
- [ ] Shown failing first, per R-16 — the current templates are demonstrated producing the broken
      copy before anything changes
- [ ] `check` is still what reports the next breakage of a template reference; a fix that takes the
      references back out of its reach is a regression, not a fix
- [ ] Whatever is decided holds for both templates, or the reason they differ is stated in the
      template that differs
- [ ] **Every reference to the templates' old location is corrected, found by a sweep rather than by
      memory** — added 2026-08-09 with the answer, because the answer moves two files and the four
      criteria above all describe the destination rather than the move

**Open questions**
- ~~**Is the loud break the answer?**~~ **Answered by the maintainer on 2026-08-09: no — put the
  templates at the same depth as the files they become.**

  A template becomes a file in `tasks_dir`. Put it *in* `tasks_dir`, as an `_`-prefixed file
  (`tasks/_task-template.md`, `tasks/_audit-umbrella-template.md`), and every relative link is
  correct in the template **and** in the copy, because there is no longer a difference in depth
  between them. That dissolves the question rather than answering it: there is no break to be loud
  about.

  **Tested before being chosen**, on a scratch project holding a real task and a template beside it:

  ```
  taskmd check     OK - 1 task(s), vocabulary valid, references resolve, no broken links   exit 0
  taskmd list      T-001  proposed  -  specify  A real task        (the template is not a task)
  ID WIDTH class   0 hits                       ('T-NNN' is not the prefix plus digits, so it is
                                                 not a near miss either — T-075)
  ```

  So the template is link-checked at the right depth, is not loaded as a task, and does not trip the
  near-miss class T-075 added. Three properties, none of them assumed.

  **What the work now is**, which is more than the question implied: two files move, and every
  reference to their old location is corrected — `CLAUDE.md`, the binding's *create*, and anything
  else a sweep turns up. That is why criterion 5 is added below.

  *Rejected: accepting the loud break.* It is genuinely defensible — the failure announces itself,
  which is better than the silent one T-060 removed — and it was the cheapest answer available. It
  hands every future audit-umbrella author a puzzle before it costs them a keystroke, permanently,
  to avoid moving two files once.

  *Rejected: dropping the link from the audit template's checklist line and keeping it in the task
  template's comment.* It fixes the only line that survives a copy, and it costs the exception
  [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) D2 declined to make — a rule about
  which template may carry a link, which somebody has to remember.

  **Decide and write with [T-051](T-051-say-where-a-project-s-task-template-lives.md)**, whose
  answer is the same convention stated from the other end: the template is an `_`-prefixed Markdown
  file in `tasks_dir`.

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
| 2026-08-09 | → specified | Answered: **no — move the templates to `tasks_dir`, as `_`-prefixed files**, so a template sits at the same depth as the file it becomes and the question disappears instead of being answered. Tested before being chosen rather than after: on a scratch project the template is link-checked at task depth, is **not** loaded as a task, and does not trip the near-miss id class T-075 added — three properties, none assumed. The loud break was a real alternative and is recorded with what it costs: a permanent puzzle for every future audit-umbrella author, to avoid moving two files once. One criterion added with the answer, because the four already written all describe the destination and none of them covers the move. To be worked with T-051, which is the same convention from the other end. |
| 2026-08-09 | → proposed | Raised from T-060's `implement` under METHOD §3.3, not from the T-059 audit — so it carries no finding id and no parent. Verified before write-up by copying the audit template's checklist line into `tasks/` and running `check`, which reported the broken link. `low`/`xs`: one line in one template reaches a real file, the other sits in a comment block that 0 of 75 tasks kept. Deliberately not folded into T-060, whose criterion 1 names the template's own location as the base — changing that base is a change to the criterion rather than a way of meeting it. |
