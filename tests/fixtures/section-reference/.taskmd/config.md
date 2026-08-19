---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: tasks
status_field: status
open_statuses: [proposed]
blocked_status: none
deliverables_field: none
value_field: none
effort_field: none
after_write: none
context_fields: [status]
index_columns: [status]
---

# A project that cites its own documents by section

The reproduction case for `SECTION REF`. It carries a citation that resolves, one that does not, one
bound to nothing, and one quoted inside a fence on purpose.

## Edges

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
