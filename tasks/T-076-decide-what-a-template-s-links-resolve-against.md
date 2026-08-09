---
id: T-076
title: Decide what a template's links resolve against
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-060, T-032, T-051]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables:
  - tasks/_task-template.md
  - tasks/_audit-umbrella-template.md
  - tests/test_schema.py
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

**This is half a plan, and the other half is [T-051](T-051-say-where-a-project-s-task-template-lives.md)'s.**
The two tasks are one convention seen from two ends, so the steps are split by *outcome* rather than
duplicated: everything that moves a file or repairs a reference is below; everything that states the
convention for a project that is not this one is T-051 §2. Neither table restates the other. Run this
one first — T-051's step 3 checks the rule against a project other than this one, and there is no
point checking a rule this repository does not yet obey.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reproduce the break against the templates **as they stand**, by copying the audit template's checklist line into `tasks/` and running `check` — criterion 2, and R-16's "shown failing first". | The `BROKEN LINK` line, recorded in §3 with the probe file that produced it |
| 2 | Move both templates into `tasks_dir` as `_`-prefixed files, re-basing their three links one level up. | `tasks/_task-template.md`, `tasks/_audit-umbrella-template.md`; `tasks/_templates/` gone |
| 3 | Repeat step 1's probe against the moved templates, then delete the probe. | The same copied line resolving, and `check` clean — recorded in §3 beside step 1's failure |
| 4 | Sweep every reference to the old location **by text, not by link check** — one reference is a Markdown link and the rest are backticked prose, which `check` cannot see. Correct the live ones; leave a closed task's record of what it did at the time. | A table in §3: every hit, each marked corrected or left, with the reason for leaving it |
| 5 | Repoint the test that asserts a template is not loaded as a task. Its current form matches on `_templates`, which the move makes **vacuous** rather than false. Record the vacuous pass before replacing it. | `tests/test_schema.py` — the vacuous pass captured in §3, then an assertion against the mechanism that actually excludes the file now |
| 6 | Run `check`, `index` and the suite; confirm the whole diff is the move plus step 4's corrections. | Command output and `git diff --stat` in §3 |

**Step 5 is where the risk is, and it is why it is not last.** The move changes *which mechanism*
keeps a template out of the task set — from the enumerate walk skipping a `_`-prefixed **folder** to
the id rule rejecting a file it now reads. If that swap does not hold, step 2 is wrong and steps 4
and 6 are wasted; the scratch-project evidence in §1 says it holds, and step 5 is where this
repository proves it on itself.

**Outputs**

```
tasks/_task-template.md
tasks/_audit-umbrella-template.md
tests/test_schema.py
CLAUDE.md
.handoff/config.md
tasks/T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md
tasks/README.md
```

## 3. Implement

**Step 1 — the break, against the templates as they stood.** The audit template's *Standard
compliance* line, copied verbatim into `tasks/` as `zz-probe.md`:

```
BROKEN LINK   tasks/zz-probe.md -> ../../plugin/docs/METHOD.md
1 problem(s) over 78 task(s)
exit 1
```

**Step 3 — the same line, after the move.** Probe regenerated from the moved template, so its link
now carries one `../` instead of two:

```
OK - 78 task(s), vocabulary valid, references resolve, no broken links
```

Criterion 1 met: the copy resolves, and it resolves because the template and the copy are now at one
depth rather than because anything was special-cased.

> **Neither block quotes the template line itself, and that is not tidiness.** The first draft of
> this section pasted it verbatim — Markdown link syntax and all — which put a live `../../` link
> inside a file two levels *shallower* than the template, and `check` immediately reported this task
> as the broken one. **It then happened a second time**, in
> [T-051](T-051-say-where-a-project-s-task-template-lives.md) §3, where the pasted evidence was a
> line from a scratch project whose link target does not exist in this repository at all. Neither
> was a near miss: a Markdown link in a task record *is* a link, and the file it sits in is the base
> it resolves against, so evidence about a link's depth re-creates the very thing it documents.
> Quote the validator's **output**, which is inert, and describe the source line. `check` caught
> both, immediately, which is the arrangement working rather than a reason to be careful.

**Step 3 also produced the finding that step 4's sweep had under-classified.** The same `check` run
reported four problems, and three of them were not links at all:

```
MISSING OUTPUT T-008 declares 'tasks/_templates/task-template.md', which does not exist
MISSING OUTPUT T-008 declares 'tasks/_templates/audit-umbrella-template.md', which does not exist
MISSING OUTPUT T-022 declares 'tasks/_templates/task-template.md', which does not exist
BROKEN LINK   tasks/T-003-...md -> _templates/task-template.md
```

Two closed tasks declare the templates in `deliverables`, which `check` enforces as paths that must
exist. Planning had them filed as historical prose. They are not prose — they are the one class of
reference to a template that the tool refuses to let rot, and the move would have left `check`
failing indefinitely.

**Step 4 — the sweep.** By text, over the tree, not by link check.

| Reference | Kind | Action |
| :--- | :--- | :--- |
| `CLAUDE.md` *Working method* | live prose, tier 1 | corrected, and kept to one added clause |
| `.handoff/config.md` `tracker_template` | live key | corrected |
| `tasks/T-008` and `tasks/T-022` `deliverables:` | **machine-checked** | corrected — 3 paths |
| `tasks/T-003` Inputs | the tree's **only** Markdown link to a template | corrected |
| `tasks/T-032` Outcome, defect 2, Scope, Inputs | **open** task, says what it will act on | corrected — 4 paths |
| `tasks/T-032` *Why nobody saw it* | open task, premise this move invalidates | annotated, not rewritten — see below |
| `tests/test_schema.py` | live assertion | step 5 |
| T-002, T-008 §1/§2/§3, T-022 §3, T-026, T-054, T-059, T-060 | closed records of what was true then | left |
| T-051 §1, T-076 §1 and Inputs | this pair's own problem statements | left; §3 is where the new state is |
| `reference/` and `docs/BRIEF.md` | prior art's own `reference/templates/`, a different tree | untouched |

**Step 5 — the test, and the vacuous pass first.** `test_schema.py` asserted that no loaded task had
`_templates` in its path. The move does not falsify that; it makes it unfalsifiable. Measured by
giving a `_`-prefixed file in `tasks/` a **real** id, so it was genuinely loaded as a task:

```
T-999 loaded as a task: True
old assertion  assertFalse([])                        -> PASSES
new assertion  assertFalse(['_zz-vacuity-probe.md'])  -> fails
```

The old form passes on the exact state it exists to forbid. Replaced with an assertion on the file's
name, plus a check that two templates are actually present — without which deleting both templates
would make the test greener.

**Decisions & assumptions**
- **The `_` prefix is now a signal to people, not a mechanism** — 2026-08-09. In `tasks/_templates/`
  the prefix was load-bearing: `load_tasks` skips `_`-prefixed **folders**, so the templates were
  never opened. A `_`-prefixed **file** is opened, and what keeps it out of the task set is the
  binding's assumption 6 — its `id: T-NNN` is not the prefix plus three digits, and is not even a
  near miss, so it is neither loaded nor reported. *What this costs:* protection moved from
  structural to content-based, so a template that acquired a real id would become a task. That is
  not a new hazard — assumption 6 already states it as the corollary of having no exclusion list —
  and it is now the thing `tests/test_schema.py` checks rather than something nothing checked.
- **A closed task's `deliverables` is repointed; its prose is not** — 2026-08-09. The distinction the
  sweep ran on: a reference a reader would use to *find the file now* is corrected, a sentence
  recording *what was true then* is left. `deliverables` is the first kind however old the task, and
  `check` says so.
- **T-032's premise is annotated in place rather than rewritten** — 2026-08-09. Its *Why nobody saw
  it* explains that templates rot silently because `_templates/` is never enumerated. That mechanism
  no longer exists, and the conclusion still holds by a different route. Rewriting it would delete
  the reason F-6 survived to be found; a dated note under it keeps both facts. *Rejected: raising a
  new task* — nothing is actionable, T-032 is open and unstarted, and this is reconcile debt this
  work created rather than a finding, which is METHOD §5's distinction.

**Step 6 — final state.**

```
OK - 78 task(s), vocabulary valid, references resolve, no broken links
Wrote tasks/README.md - 20 active, 58 closed
129 passed, 4 subtests passed in 6.05s
```

`git diff --stat`: 12 files, `tasks/_templates/{task,audit-umbrella}-template.md` shown as renames
into `tasks/_{task,audit-umbrella}-template.md` with 2 and 4 changed lines — the three re-based
links; every other file is a swept reference or this pair's own records.

**Outputs produced**
- `tasks/_task-template.md`, `tasks/_audit-umbrella-template.md` — moved, links re-based
- `tests/test_schema.py` — assertion repointed at the mechanism that now does the excluding
- `CLAUDE.md`, `.handoff/config.md`, `tasks/T-003`, `tasks/T-008`, `tasks/T-022`, `tasks/T-032`,
  `tasks/README.md` — swept references

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A line copied from either template into `tasks/` resolves, or the case is stated as accepted with its cost | met | The audit template's *Standard compliance* line, copied into `tasks/`, resolved after the move; the same probe reported `BROKEN LINK` before it. Nothing was accepted, because nothing had to be — the answer removed the case rather than tolerating it |
| Shown failing first, per R-16 | met | §3 step 1, run against the templates as they stood and before any file moved. Not inherited from §1's earlier demonstration: re-run in this session, over 78 tasks |
| `check` is still what reports the next breakage of a template reference | met | Both templates are still walked by `check_links` — they moved within the tree, not out of it — and it proved it twice unprompted, catching a `../../` link this very record introduced and then a second one in [T-051](T-051-say-where-a-project-s-task-template-lives.md) §3 |
| Holds for both templates, or the difference is stated in the template that differs | met | One rule, two files, no difference to state. The asymmetry §1 identified — a comment block 0 of 75 tasks kept, versus a checklist line copied on purpose — stopped being a reason to treat them differently once depth was equalised |
| Every reference to the old location corrected, found by a sweep rather than by memory | met | §3 step 4's table: 10 references corrected across 6 files, and the classes left are named with the reason. The sweep was by **text**, which is what found the three `deliverables:` declarations `check` enforces — a link-only sweep would have found one of the ten |

**Child fix tasks raised**
- none. One open task was **reconciled** rather than made a child:
  [T-032](T-032-repair-the-audit-template-and-validate-templates.md), whose *Why nobody saw it*
  premise this move invalidated. Reconcile debt this work created, not a finding — METHOD §5.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met; no child raised. The move landed as planned and the two surprises both came from the plan's own blind spots rather than from the answer. First, three of the ten references were `deliverables:` declarations in closed tasks, which `check` enforces as paths that must exist — filed at plan time as historical prose, and the move would have left `check` failing until someone noticed. That produced the sweep's operating rule: a reference used to *find the file now* is corrected however old the task; a sentence recording *what was true then* is left. Second, `check` twice reported this pair's own records as the defect, because a Markdown link pasted as evidence is a live link resolved against the record's directory — once here and once in T-051 §3. Both caught immediately, which is the third criterion demonstrating itself unasked. [T-032](T-032-repair-the-audit-template-and-validate-templates.md) was reconciled rather than made a child: its *Why nobody saw it* premise is now historical, and is annotated in place because it is the record of why F-6 survived. |
| 2026-08-09 | → planned | Planned **with [T-051](T-051-say-where-a-project-s-task-template-lives.md), as one plan split by outcome across two tables** — this one moves files and repairs references, T-051's states the convention; neither restates the other, and this one runs first because a rule is not worth checking against another project while this repository still disobeys it. Two things the plan had to account for that §1 did not. The reference sweep is a **text** sweep, not a link check: of the hits, exactly one is a Markdown link and every other is backticked prose, so `check` certifies nothing here and criterion 5 would be met vacuously by a clean link run. And `tests/test_schema.py` asserts on the string `_templates`, which the move makes **vacuous** rather than false — so the step captures the vacuous pass before replacing the assertion, and the replacement targets the mechanism that will actually be doing the excluding. That mechanism swap is the plan's real risk and is sequenced early: today a template is never read, because *enumerate* skips `_`-prefixed folders; afterwards it is read at task depth and rejected by the id rule. |
| 2026-08-09 | → specified | Answered: **no — move the templates to `tasks_dir`, as `_`-prefixed files**, so a template sits at the same depth as the file it becomes and the question disappears instead of being answered. Tested before being chosen rather than after: on a scratch project the template is link-checked at task depth, is **not** loaded as a task, and does not trip the near-miss id class T-075 added — three properties, none assumed. The loud break was a real alternative and is recorded with what it costs: a permanent puzzle for every future audit-umbrella author, to avoid moving two files once. One criterion added with the answer, because the four already written all describe the destination and none of them covers the move. To be worked with T-051, which is the same convention from the other end. |
| 2026-08-09 | → proposed | Raised from T-060's `implement` under METHOD §3.3, not from the T-059 audit — so it carries no finding id and no parent. Verified before write-up by copying the audit template's checklist line into `tasks/` and running `check`, which reported the broken link. `low`/`xs`: one line in one template reaches a real file, the other sits in a comment block that 0 of 75 tasks kept. Deliberately not folded into T-060, whose criterion 1 names the template's own location as the base — changing that base is a change to the criterion rather than a way of meeting it. |
