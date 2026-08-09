---
id: T-087
title: Let list filter on a field the index can show
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-022, T-086, T-029]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-087 — Let list filter on a field the index can show

## 1. Specify

**Outcome**
A project that stores a field taskmd does not enumerate can select on it with `list`, or is told at
setup that it cannot. Either way the tool stops being able to *display* a field it refuses to
*filter* on.

**Why this one**
Found by [T-086](T-086-group-the-backlog-into-release-milestones.md) while grouping this backlog
into releases. `work_package` is a shipped schema key, `index_columns` names it, `--json` emits it,
and the generated index grew a column for it the moment tasks had values. The filter refuses it:

```
taskmd list --work_package v0.2
unknown filter: --work_package. This project accepts: --blocked_by, --blocks, --business_value,
--children, --effort, --parent, --phase, --related, --status, --type
```

`parse_filters` builds its accepted set from the vocabularies plus the link names, so a stored field
that is not enumerated is unfilterable by construction. The error is at least honest and lists what
works, which is [T-029](T-029-reject-unknown-arguments-on-every-command.md)'s standard arriving
early.

**Why it matters beyond one field.** The schema's own promise is that a field it does not name is
*carried, never interpreted*, and that naming such a field in `context_fields` or `index_columns`
makes it appear "with no code change and no schema entry". That promise holds for the two views and
breaks at the filter, which is the one place an adopter reaches when the view gets long. The first
project to hit it was this one, on the day it published.

**Requirements served**
R-15 in the sense `docs/SCOPE.md` non-goal 11 was amended on: selecting a subset by a stored value is
inside the carve-out, and a query language is still outside it. R-11, since which fields exist is
configuration.

**Scope**
- In: which fields `list` accepts as filters, and what it says about a value it cannot check.
- In: whether a filter on a non-enumerated field validates its value at all, since there is no list
  to validate against. A typo would silently return nothing, which is worse than an error.
- Out: boolean expressions, ranges, sorting flags, saved queries. Non-goal 11 stands.
- Out: `context_fields`, which already shows anything.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `parse_filters` and `matches`.
- `plugin/skills/taskmd/taskmd/defaults/config.md` — *Vocabularies*, *Views*, and the paragraph
  promising that an unnamed field is carried and can be shown.
- [T-022](T-022-filtered-task-listing-for-scripts.md) — why `list` exists and what it was allowed to
  do.

**Acceptance criteria**
- [ ] `list` filters on a stored field that no vocabulary enumerates, shown on this repository's
      `work_package`
- [ ] A value that matches nothing is distinguishable from a field that does not exist, and the
      difference is shown by running both
- [ ] `taskmd list --work_package v0.2 --open` returns the v0.2 tasks, which is the command
      [T-086](T-086-group-the-backlog-into-release-milestones.md)'s plan could not use
- [ ] The tests cover the unenumerated case, since every existing filter test uses a vocabulary

**Open questions**
- **What an unvalidatable value should do.** A vocabulary filter rejects a value that is not in the
  list, and there is no list here. Either the filter matches literally and an empty result is the
  answer, or `list` reports that nothing carries that value, which is friendlier and is one step
  towards a query language nobody asked for. The maintainer's, since it is a behaviour an adopter
  sees.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised by [T-086](T-086-group-the-backlog-into-release-milestones.md), whose second acceptance criterion this is: the release plan was written against a command that does not exist, because `list` accepts only vocabulary fields and link names. The gap is not about `work_package` in particular. The schema promises that an unnamed field is carried and can be surfaced by naming it in a view, and that promise stops at the filter, which is where an adopter goes once the view is long. `high` because it contradicts a documented property rather than missing a feature, and `s` because `parse_filters` is where all of it lives. |
