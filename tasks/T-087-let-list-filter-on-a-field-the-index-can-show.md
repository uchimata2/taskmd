---
id: T-087
title: Let list filter on a field the index can show
type: fix
status: specified
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
- [ ] A value that matches nothing exits 0 with no rows, and a field that does not exist exits 2
      naming what the project accepts — shown by running both
- [ ] `taskmd list --work_package v0.2 --open` returns the v0.2 tasks, which is the command
      [T-086](T-086-group-the-backlog-into-release-milestones.md)'s plan could not use
- [ ] The tests cover the unenumerated case, since every existing filter test uses a vocabulary

**Open questions**
- **What an unvalidatable value should do. Answered by the maintainer on 2026-08-09: nothing.** The
  filter matches literally, and an empty result at exit 0 is the answer. The field *name* stays
  validated, so an unknown field is still an error naming what the project accepts; only the value
  goes unchecked.

  **The behaviour that already ships settles it.** `--status blocked` is a vocabulary value that no
  task currently carries, and it prints nothing and exits 0; `--status v0.2` exits 2 naming the
  vocabulary. So "matched nothing" and "no such field" are *already* two different observable
  outcomes, and validating an unenumerated value would make the tool **stricter where it knows
  less** — with no list, it cannot tell a typo from an empty bucket, so any error it printed would
  be a guess.

  *Rejected: `list` reports that nothing carries the value.* Its accepted set could only be derived
  from what the tasks hold at that moment, which makes a command's validity depend on when it runs:
  `--work_package v0.1` would begin erroring once the last v0.1 task went, and `--work_package v0.4`
  would error until the first v0.4 task existed. A script written today would break tomorrow without
  being edited, and scripts are what `list` was argued for
  ([T-022](T-022-filtered-task-listing-for-scripts.md)).

  **The typo risk is accepted, not solved.** `--work_package v0.22` returns nothing and says nothing,
  and that is the price of this answer. It is bounded on both sides: the field name — the likelier
  typo — is still checked, and the unknown-filter error grows a `--work_package` entry the moment
  this lands, which is where a reader finds the spelling.

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
| 2026-08-09 | → specified | Open question answered: the filter matches literally, so an unenumerated value is not validated at all. Settled by behaviour that already ships rather than by preference — `--status blocked` is a valid value nothing carries and exits 0 silently, so erroring on an unenumerated value would make the tool stricter exactly where it has less to go on, and the error would be a guess at a typo it cannot detect. The rejected alternative is recorded in §1 with what breaks it: its accepted set could only come from current contents, so `--work_package v0.1` starts erroring when the last v0.1 task goes and `--work_package v0.4` errors until the first one arrives, which makes a script's validity depend on when it runs. Criterion 2 sharpened to name the exit codes, since the answer is precisely about that boundary. |
| 2026-08-09 | → proposed | Raised by [T-086](T-086-group-the-backlog-into-release-milestones.md), whose second acceptance criterion this is: the release plan was written against a command that does not exist, because `list` accepts only vocabulary fields and link names. The gap is not about `work_package` in particular. The schema promises that an unnamed field is carried and can be surfaced by naming it in a view, and that promise stops at the filter, which is where an adopter goes once the view is long. `high` because it contradicts a documented property rather than missing a feature, and `s` because `parse_filters` is where all of it lives. |
