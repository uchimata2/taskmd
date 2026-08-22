---
id: T-217
title: Return the fields list can filter on in its machine form
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-087, T-022]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-217 — Return the fields `list` can filter on in its machine form

## 1. Specify

**Outcome**
A caller that can filter `list` on a field can also read that field back from `--json`, so a machine
consumer can verify, group or sort on the value it selected by — or the asymmetry is recorded as
deliberate, with the reason, where a caller meets it.

**Why this one**
Found on 2026-08-22 while answering a question about the open backlog, by running both halves rather
than reading the help text:

```text
$ taskmd list --open --effort xs
T-214   proposed  M6  specify  Decide whether the class-set subtraction that ...   -

$ taskmd list --open --effort xs --json
[ { "blocked": false, "blocked_by": [], "blocks": [], "children": [], "id": "T-214",
    "open": true, "parent": [], "phase": "specify", "related": [...],
    "status": "proposed", "title": "...", "work_package": "M6" } ]
```

`--effort` selects correctly and the object carries no `effort`. The same holds for
`business_value`. **So a machine caller must trust the filter blindly**: it cannot confirm what it
asked for, cannot group by the value, and cannot sort on it without opening every task file — which
is what this tool exists to stop people doing.

**It is a consequence of one key serving two masters, not an oversight.** `index_columns` decides
both what the generated human index shows *and* what the machine form returns. `effort` is named by
the schema — `effort_field: effort`, and ordering reads it — but it is not an `index_column` here, so
it is absent from the JSON. A project wanting it in the machine form must put it in the human index
too, and those are different questions.

**Scope**
- In: deciding whether the machine form should carry every schema-named field, the configured
  columns plus the fields filters accept, or stay as it is with the reason stated where a caller
  meets it
- In: implementing the decision, and whatever the answer costs a caller that already parses the
  current shape
- Out: the human view's columns. `list` omitting a column no task uses is a decided behaviour and is
  not what this is about
- Out: adding a config key. [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) records
  that a new key errors every adopter's config on upgrade, so a solution needing one is a different
  and much larger task

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_list`, `in_use`, and the *Views only* docstring that
  states the current rule
- [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) — which widened filtering, and
  whose own title names the coupling this task questions: *a field the index can show*
- `.taskmd/config.md` — `index_columns`, and the ordering keys that name `effort`

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternatives, including what each would cost a
      caller already parsing `--json` today
- [ ] If the shape changes, a test asserts that **every field `list` accepts as a filter** is present
      in the machine form — derived from the filter list rather than hand-typed, so the two cannot
      drift apart again
- [ ] If the shape does not change, the reason is stated where a caller meets it, not only in this
      record
- [ ] `check`, `index` and the suite are green, and the output is quoted

**Open questions**
- **None.** The options are named above; choosing between them is this task's work.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised while answering an ordinary question about the backlog — the view the owner asked for needed `effort` and a gate column, and `--json` could supply neither, so it was built from the JSON and the front matter together. Recorded rather than worked around, because the workaround is exactly the file-reading this tool exists to remove. `low` and `s`: nothing is broken and the human view is unaffected, but it is `adopter_visible` because a machine consumer meets it. **Not covered by the multi-phase grant of 2026-08-22**, which names six tasks by id and this is not one of them. |
