---
id_field: ref
id_prefix: ISSUE-
id_width: 4
title_field: name
tasks_dir: issues
status_field: state
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
