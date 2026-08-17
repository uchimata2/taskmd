---
id: T-172
title: Catch a template placeholder left in a finished record
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-171]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-172 — Catch a template placeholder left in a finished record

## 1. Specify

**Outcome**
Finished task records that no longer carry unfilled scaffolding from
[`_task-template.md`](_task-template.md) — and a ruling, settled by running something rather than by
argument, on whether `check` is the thing that should have caught them.

**Why this one**
Found on 2026-08-18 while reviewing
[T-171](T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md), in a record T-171 had just
annotated. It is raised separately rather than fixed there because it fails none of T-171's criteria
and has nothing to do with what T-171 tested — `review` §*What review is not* sends a problem found
outside the criteria to its own task.

Measured on the tree the same day, not estimated:

```
task files with a DUPLICATED 'Child fix tasks raised' heading: 5
  T-037-delete-the-throwaway-proof-repository.md
  T-059-audit-the-whole-project-after-the-plugin-restructure.md
  T-140-restore-the-log-row-a-table-cell-swallowed.md
  T-141-report-a-table-row-with-more-cells-than-its-header.md
  T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md

files still holding the unfilled placeholder line: 6
```

The shape in [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md)
is the clearest: the heading appears **twice**, once answered `none` and once still reading
`<T-NNN or "none">`. A reader cannot tell whether the placeholder is an oversight or an open item.

**What makes it worth a record rather than a tidy-up.** `check` returns `exit=0` on every one of these
files. So this is not five typos; it is a class the validator does not see, in the one artifact this
project uses to argue that its records stay honest. Two of the five affected records are themselves
about defects in table and log structure, which is the kind of coincidence worth not laughing off.

**Scope**
- In: the five records above, and any the sweep finds when it is re-run at `implement` — resolve the
  set against the tree, never against the list quoted here
- In: the ruling on whether `check` gains a rule for it, taken by **building the rule and reading its
  alarms on this corpus**, which is how this project has settled in-or-out questions before
- Out: changing [`_task-template.md`](_task-template.md) itself. The placeholder is correct *in* the
  template — that is what a template is — and a fix that mangles the source to protect the copies is
  the wrong end
- Out: any other placeholder class nobody has measured. If the sweep turns one up, it is a finding and
  gets its own row, not a silent widening of this one

**Inputs**
- [`_task-template.md`](_task-template.md) — where the placeholder legitimately lives
- The five records named above
- `tasks/T-032-repair-the-audit-template-and-validate-templates.md` — **a lead, not a citation.** Its
  title says it validated templates, which would make it either the prior art or the task that should
  have caught this. Nobody has read it for this purpose; resolve it at `specify` before relying on a
  word of that sentence

**Acceptance criteria**
- To be written at `specify`, by whoever owns the outcome. They are not drafted here: this record is
  a raise, and criteria invented by the finder are criteria the fix will pass by construction.

**Open questions**
- **Does `check` own this class at all?** A validator that reports unfilled scaffolding is also a
  validator that fires on any record legitimately quoting the template — this very file quotes it
  twice. **The owner answers, at `specify`**, and the honest way to put the question is to build the
  rule first and show what it flags here.
- **Does the publishing constraint raise the value above `low`?** The records are in a public
  repository, so a stranger reading T-169 meets an unresolved placeholder. Set `low` because no
  behaviour is affected; the owner may disagree.

## 2. Plan

Not run — the task is at `proposed`.

## 3. Implement

Not run — the task is at `proposed`.

## 4. Review

Not run — the task is at `proposed`.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → proposed | Raised from [T-171](T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md)'s `review`, and deliberately **not** as its child: it fails none of T-171's criteria and shares no subject with it, so a parent edge would say something false about why it exists. `fix` and not `decision` because the five records are wrong by inspection and cleaning them needs nobody's ruling; the one thing that does need a ruling — whether `check` grows a rule — is an open question inside it rather than the task's purpose. The count was **measured on the tree, not estimated**, and the scope says to re-resolve it at `implement` rather than trust the list quoted in this record. Acceptance criteria are left for `specify` on purpose: written now, by the session that found the defect, they would be criteria the fix passes by construction. |
