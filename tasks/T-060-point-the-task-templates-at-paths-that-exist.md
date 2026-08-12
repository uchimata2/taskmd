---
id: T-060
title: Point the task templates at paths that exist
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-032, T-051, T-076]
work_package: M1
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
- ~~**Do the references become Markdown links?**~~ **Decided at `plan` on 2026-08-09: yes.** The
  argument against them turned out to be false in this repository — see §2 step 2 and §3 D1.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Resolve each of the three named paths from its template's own location **and** from the repository root, so the failure is not an artefact of the base chosen | The failing evidence, before any edit |
| 2 | Settle the open question on evidence rather than on reading: does `check` reach a link inside a template at all, and does a task created from the template actually keep the comment block? | The decision recorded in §3 D1 |
| 3 | Rewrite the three references as Markdown links relative to each template's own location, which is what criterion 1 names | Both templates |
| 4 | Re-run the event that caused the finding — move `plugin/docs/METHOD.md` away — and confirm both templates are now reported | `check` transcript |
| 5 | Confirm the change is the three references and nothing else | `git diff tasks/_templates/` |
| 6 | Find out what the fix costs a file created from the template, by copying a template line into `tasks/` and checking it | The depth finding, and a task for it |

**Why step 2 comes before step 3.** The open question has an empirical answer on both sides — whether
`check` reads template links, and whether tasks keep the comment — and both were assumptions when the
question was written. Deciding first and testing afterwards would have made step 4 a formality.

**Why step 6 exists at all.** Making a reference a link changes what it is relative *to*, and a
template is copied. That is the one way this fix could introduce something, so it is checked rather
than hoped.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — the references become Markdown links** — 2026-08-09. Two measurements settled it, both
  taken before the edit:
  - `check_links` walks `markdown_files()`, which is every `.md` in the project — it is `load_tasks`
    that skips `_`-prefixed folders, and that only decides what is a *task*. A link planted inside
    the template's HTML comment was reported, so criterion 3 is reachable:

    ```
    BROKEN LINK   tasks/_templates/task-template.md -> ./no-such-file.md
    1 problem(s) over 75 task(s)
    ```
  - The argument recorded against linking — *"every task created from it would carry two live links
    to project documents"* — is **false here**. `grep -l` for the comment's own wording across
    `tasks/*.md` returns **0 of 75**: no task has ever kept the block. The cost was hypothetical and
    the benefit is not.

  *What was rejected:* correcting the paths and leaving them as prose. It meets criterion 1 and
  leaves criterion 3 answerable only by *"it cannot, and what would is making them links"* — which is
  the criterion telling you the answer.

- **D2 — one treatment for both templates, not one each** — 2026-08-09. The two are not alike: the
  task template's reference sits in a comment nobody keeps, the audit template's in a checklist line
  meant to survive. A split was available and was not taken, on
  [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)'s reasoning applied to a
  smaller case — a defensible exception is still a rule someone has to remember, which
  `docs/SCOPE.md` §1 *Invisibility* rejects. The consequence for the audit template is real and is
  **not absorbed**: it is [T-076](T-076-decide-what-a-template-s-links-resolve-against.md).

- **Assumption, recorded as one:** that 0-of-75 is evidence about the convention and not about the
  sample. If a future project keeps the comment block, its two links break and `check` says so —
  loudly, on the first run, which is the failure mode this fix is trying to create rather than avoid.

### Step 1 — shown failing first (R-16)

Neither base resolves, so the finding is not an argument about which base the templates meant:

```
resolved from tasks/_templates/ (each template's own location)
  docs/METHOD.md                -> does not exist
  taskmd/defaults/config.md     -> does not exist
resolved from the repository root
  docs/METHOD.md                -> does not exist
  taskmd/defaults/config.md     -> does not exist

docs/ actually holds:  BRIEF.md  SCOPE.md
the files are at:      plugin/docs/METHOD.md   plugin/taskmd/defaults/config.md
```

### Steps 3–4 — the fix, and the guard proved by making it fire

The three references became links relative to `tasks/_templates/`. Then the event that caused the
finding was re-run — `plugin/docs/METHOD.md` moved out of the way — and both templates are now
reported, which is the whole of criterion 3:

```
taskmd check          (with plugin/docs/METHOD.md moved away)
BROKEN LINK   tasks/_templates/audit-umbrella-template.md -> ../../plugin/docs/METHOD.md
BROKEN LINK   tasks/_templates/task-template.md -> ../../plugin/docs/METHOD.md
67 problem(s) over 75 task(s)

file restored, working tree confirmed clean, then:
taskmd check          OK - 75 task(s), vocabulary valid, references resolve, no broken links
```

The 67 is the honest number and worth leaving in: moving that file breaks 65 other references too,
which is a measure of how much of this repository points at the method document — and of what the
next move of it would cost if none of those pointers were links.

### Step 5 — nothing else changed

```
tasks/_templates/audit-umbrella-template.md | 2 +-
tasks/_templates/task-template.md           | 7 ++++---
2 files changed, 5 insertions(+), 4 deletions(-)
```

Three reference lines. The task template's extra two lines are the comment paragraph re-wrapped to
stay inside the margin once the links made it longer; no sentence changed.

### Step 6 — what the fix costs a copy, escalated not absorbed

A template lives one directory deeper than the file it becomes, so a link correct in
`tasks/_templates/` is wrong by one level in `tasks/`. Confirmed rather than reasoned:

```
tasks/zz-probe.md holding only the audit template's Standard compliance line
taskmd check
BROKEN LINK   tasks/zz-probe.md -> ../../plugin/docs/METHOD.md
```

This reaches the audit template's checklist line, which is copied on purpose, and not the task
template's comment, which is not kept. It is **outside this task** — criterion 1 names the template's
own location as the base, so changing that base changes the criterion — and it is raised as
[T-076](T-076-decide-what-a-template-s-links-resolve-against.md) under METHOD §3.3. The probe file
was removed and the tree confirmed clean.

**Outputs produced**
- `tasks/_templates/task-template.md`, `tasks/_templates/audit-umbrella-template.md` — three
  references, now links that resolve
- [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) — the depth finding

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every path named in either template resolves from that template's own location | met | Both link targets resolved from `tasks/_templates/`; `check` reports no broken link over 75 tasks |
| Shown failing first, per R-16 | met | §3 step 1, before any edit, from both plausible bases so the failure is not a disagreement about which was meant |
| `check` reports the next such breakage, or it is stated why it cannot and what would | met | The first branch, not the second: §3 step 4 moved the referenced file and `check` named both templates. Reachability was established in D1 before the fix was written, not assumed from it |
| Nothing else in either template changes | met | §3 step 5 — three reference lines and a re-wrap; T-032's four schema defects in the audit template are untouched and still its |

**Child fix tasks raised**
- none. One task was raised, and it is **not** a child: [T-076](T-076-decide-what-a-template-s-links-resolve-against.md)
  comes from METHOD §3.3 — actionable, outside this task — rather than from a criterion this task
  failed. All four are met.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met; `check` OK on 76 tasks and the index regenerated. The guard is the result worth recording: moving `plugin/docs/METHOD.md` away now makes `check` name both templates, which is criterion 3's first branch rather than its escape clause. One thing was found and not absorbed — a template sits one directory deeper than the file it becomes, so the links this task created are wrong by one level in any copy of them. Shown with a probe file, and raised as T-076 rather than fixed here, because criterion 1 names the template's own location as the base and changing that base changes the criterion. |
| 2026-08-09 | → in_progress | Plan settled the open question **on measurement rather than on reading**, which is why step 2 precedes step 3: `check_links` walks every `.md` and reported a planted link inside the template's comment, and the argument against linking — that every task would carry the comment's links — is false at 0 of 75 task files. Both templates get the same treatment; the split that was available (comment vs. surviving checklist line) was rejected on T-064's reasoning that a defensible exception is still a rule someone has to remember. |
| 2026-08-09 | → specified | Criteria stand as raised. The one open question is a `plan` question by its own terms — it chooses the form of the fix, not what the fix has to achieve — so nothing here needed the owner beyond the authorisation to run the lifecycle. Premise re-verified before accepting it: all three paths fail to resolve from both the template's own location and the repository root. |
| 2026-08-09 | → proposed | Raised as F-2 from the T-059 audit, clause 1. Verified before write-up: `docs/` holds only `SCOPE.md` and `BRIEF.md`, so all three references are dead. `high`/`xs` because the cost is propagation — the template is copied into every new task — while the fix is three strings. Deliberately narrow against T-032, which owns the audit template's schema defects and predates the move that caused these. |
