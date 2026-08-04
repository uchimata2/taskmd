---
id_field: ref
id_prefix: ISSUE-
id_width: 4
title_field: name
tasks_dir: issues
status_field: state
deliverables_field: none
blocked_status: none
open_statuses: [todo, doing, waiting]
context_fields: [state, size, area]
index_columns: [size, state]
---

# Second schema — deliberately unlike the default

Every configurable dimension is changed: the id field, prefix and width; the title and status
field names; the folder; the status vocabulary and which of it is open; the edge field names and
what they derive; and an extra enumerated field the default does not have.

If taskmd works against this as well as against its own `tasks/`, the schema is configuration
rather than code. That is the whole of T-001's fourth acceptance criterion.

`area` appears in `context_fields` but in no vocabulary — it is a pass-through field, carried and
shown but never checked.

`deliverables_field` is `none`: this project does not declare outputs, which exercises the other
half of that key. The default config names a field; a schema that names nothing must work too, or
the key is not optional in practice.

`blocked_status` is `none`, and the reason is worth recording. It was first set to `waiting`, on
the assumption that "waiting" is this project's word for blocked. `check` immediately reported
ISSUE-0003 — an epic — as waiting with nothing blocking it, which is correct: it is waiting for its
stories, and that is **hierarchy, not dependency**. The two are different edges (`docs/METHOD.md`
§4), and one status value cannot stand for both. So this project declares no blocked status, and
the "a project may call it something else" case is proven by a purpose-built project in
`tests/test_cli.py` instead of by bending this one.

## Edges

| Field | Kind | Derives |
| :--- | :--- | :--- |
| epic | hierarchy | stories |
| depends_on | dependency | unblocks |
| see_also | soft | - |

## Vocabularies

| Field | Values |
| :--- | :--- |
| state | todo, doing, waiting, shipped, dropped |
| size | S, M, L |
