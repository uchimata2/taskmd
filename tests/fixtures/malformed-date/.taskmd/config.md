---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: tasks
status_field: status
open_statuses: [proposed, in_progress]
blocked_status: none
deliverables_field: none
value_field: none
effort_field: none
after_write: none
context_fields: [status, reviewed_on]
index_columns: [status]
---

# A project whose date fields hold values that are not dates

The reproduction case for `MALFORMED DATE`. **Nothing in this config names a date**, and nothing
can: taskmd has no date field and gaining a key to name one would error every project that wrote a
config (T-106). So the check has to work from the shape of the value, which is what T-162 ruled.

`reviewed_on` is a field name no schema mentions, here for the reason `label-shaped-value` carries
`milestone`: a rule keyed on a field name could not have seen it at all.

`windows` is a **list**, because a field the schema does not name arrives as one when a task writes
one, and a check that had only ever met scalars crashed on the first real tree it was pointed at.

## Edges

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, in_progress, done |
