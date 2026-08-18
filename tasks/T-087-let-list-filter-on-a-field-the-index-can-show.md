---
id: T-087
title: Let list filter on a field the index can show
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-022, T-086, T-029]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_list.py]
adopter_visible: yes
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
taskmd list --work_package M2
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
- [ ] `taskmd list --work_package M2 --open` returns the M2 tasks, which is the command
      [T-086](T-086-group-the-backlog-into-release-milestones.md)'s plan could not use
- [ ] The tests cover the unenumerated case, since every existing filter test uses a vocabulary

**Open questions**
- **What an unvalidatable value should do. Answered by the maintainer on 2026-08-09: nothing.** The
  filter matches literally, and an empty result at exit 0 is the answer. The field *name* stays
  validated, so an unknown field is still an error naming what the project accepts; only the value
  goes unchecked.

  **The behaviour that already ships settles it.** `--status blocked` is a vocabulary value that no
  task currently carries, and it prints nothing and exits 0; `--status M2` exits 2 naming the
  vocabulary. So "matched nothing" and "no such field" are *already* two different observable
  outcomes, and validating an unenumerated value would make the tool **stricter where it knows
  less** — with no list, it cannot tell a typo from an empty bucket, so any error it printed would
  be a guess.

  *Rejected: `list` reports that nothing carries the value.* Its accepted set could only be derived
  from what the tasks hold at that moment, which makes a command's validity depend on when it runs:
  `--work_package M1` would begin erroring once the last M1 task went, and `--work_package M4`
  would error until the first M4 task existed. A script written today would break tomorrow without
  being edited, and scripts are what `list` was argued for
  ([T-022](T-022-filtered-task-listing-for-scripts.md)).

  **The typo risk is accepted, not solved.** `--work_package v0.22` returns nothing and says nothing,
  and that is the price of this answer. It is bounded on both sides: the field name — the likelier
  typo — is still checked, and the unknown-filter error grows a `--work_package` entry the moment
  this lands, which is where a reader finds the spelling.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide which fields the filter accepts, and derive the set from configuration | `filter_names` in `cli.py` |
| 2 | Match an unenumerated value literally; leave the name check alone | `matches` in `cli.py` |
| 3 | Cover the unenumerated case, which no existing filter test had a shape for | `tests/test_list.py` |
| 4 | Complete the promise where it is written, rather than beside the code | `defaults/config.md` §Views |

## 3. Implement

**Decisions & assumptions**
- **The accepted set is "any field a view names"** — 2026-08-10. `context_fields` and
  `index_columns` are exactly where the schema already promises that an uninterpreted field can be
  surfaced, so extending the filter to that same set keeps both halves of one promise in one place
  and needs **no new config key** — which matters, because T-106 established that the shipped config
  cannot gain one without breaking every project that has written its own. In this repository that
  admits `work_package` and `owner`, both of which are wanted. Rejected: a new key naming the
  filterable fields, which is a second copy of "which fields this project uses" and the key the
  schema cannot afford.
- **Rejected: every field any task happens to carry** — 2026-08-10. It would have accepted more, and
  it is the same defect the open question's rejected alternative was rejected for, one level up: an
  accepted set read off current contents makes a command's validity depend on when it runs. The
  answer that governs values governs names.
- **`vocabulary` and `field` differ at parse time, not at match time** — 2026-08-10. The kinds exist
  to say whether the *value* was validated; both then compare literally against the stored value. So
  `matches` was reorganised around `link` being the exception rather than `vocabulary` being the
  rule, which is what the two non-link kinds actually have in common.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `filter_names`, `matches`.
- `tests/test_list.py` — four tests in a new class.
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Views* — the promise, completed where it is
  made. The same edit reconciled the edge-column sentence with
  [T-111](T-111-stop-the-index-showing-a-closed-task-as-a-live-blocker.md), which changed what
  *uses* means for a dependency column earlier the same day.

**Evidence**

The command [T-086](T-086-group-the-backlog-into-release-milestones.md)'s plan could not use, run:

```
taskmd list --work_package M2 --open      -> 20 rows, exit 0
taskmd list --work_package v0.22            -> no rows, exit 0
taskmd list --owner maintainer --open       -> rows, exit 0
taskmd list --wat x                         -> exit 2, unknown filter: --wat. This project
   accepts: --blocked_by, --blocks, --business_value, --children, --effort, --owner, --parent,
   --phase, --related, --status, --type, --work_package
```

The last line is the third criterion's other half: the accepted list now names `--work_package` and
`--owner`, which is where a reader finds the spelling of the values nothing validates.

Suite **185 passed** (181 before), `check` clean on 113 tasks.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `list` filters on a stored field no vocabulary enumerates, shown on this repository's `work_package` | met | 20 open M2 rows, above. |
| A value matching nothing exits 0 with no rows; a field that does not exist exits 2 naming what the project accepts — both run | met | `--work_package v0.22` → exit 0, silent. `--wat x` → exit 2 with the full accepted list. |
| `taskmd list --work_package M2 --open` returns the M2 tasks | met | It is now the way the release's membership is read, which is what T-110 left with no command. |
| The tests cover the unenumerated case, since every existing filter test uses a vocabulary | met | A class of four, including one asserting the accepted set is derived from `alt-project`'s **config** rather than from its contents — the property the rejected alternative would have broken, and the one a test on this repository alone could not see. |

**Child fix tasks raised**
- none. [T-113](T-113-name-an-unknown-filter-before-complaining-it-has-no-value.md), raised earlier
  today by T-029, is in this same code and stays separate: it is about the order of two rejections,
  not about which fields are accepted.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Plan through review in one session, under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1). The set of filterable fields is now the set a view may name, so the schema's promise about an uninterpreted field holds at all three surfaces instead of two. |
| 2026-08-09 | → specified | Open question answered: the filter matches literally, so an unenumerated value is not validated at all. Settled by behaviour that already ships rather than by preference — `--status blocked` is a valid value nothing carries and exits 0 silently, so erroring on an unenumerated value would make the tool stricter exactly where it has less to go on, and the error would be a guess at a typo it cannot detect. The rejected alternative is recorded in §1 with what breaks it: its accepted set could only come from current contents, so `--work_package M1` starts erroring when the last M1 task goes and `--work_package M4` errors until the first one arrives, which makes a script's validity depend on when it runs. Criterion 2 sharpened to name the exit codes, since the answer is precisely about that boundary. |
| 2026-08-09 | → proposed | Raised by [T-086](T-086-group-the-backlog-into-release-milestones.md), whose second acceptance criterion this is: the release plan was written against a command that does not exist, because `list` accepts only vocabulary fields and link names. The gap is not about `work_package` in particular. The schema promises that an unnamed field is carried and can be surfaced by naming it in a view, and that promise stops at the filter, which is where an adopter goes once the view is long. `high` because it contradicts a documented property rather than missing a feature, and `s` because `parse_filters` is where all of it lives. |
