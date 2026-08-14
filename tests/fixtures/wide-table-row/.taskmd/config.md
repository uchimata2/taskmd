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
context_fields: [status]
index_columns: [status]
---

# A project with a table row wider than its header

The reproduction case for `WIDE ROW`. Markdown drops a cell past the header count, so the text is in
the file and renders nowhere, and nothing else a validator does can see it.

It carries all six behaviours in one project, because they are one decision and a fixture proving
five would let the sixth regress in silence. The first task holds the three the check must
**report**; the second holds the three it must **ignore**.

The two tasks are named here by position rather than by id on purpose: naming both would be a
majority of this project's known ids sitting outside the generated markers, and `DUPLICATE INDEX`
would fire on the file explaining the fixture.

The specimens live only here. A row demonstrating this fault in a task file or a document would be
an instance of the fault, so there is nowhere else in this repository it can be written (T-141).

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
