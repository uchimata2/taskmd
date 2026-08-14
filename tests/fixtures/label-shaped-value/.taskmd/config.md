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
effort_field: days
after_write: none
context_fields: [status, work_package, milestone]
index_columns: [work_package, status]
---

# A project whose labels read as versions

The reproduction case for `LABEL SHAPE`. It carries all four behaviours the check has to get right,
in one project, because they are one decision and a fixture that proved three of them would let the
fourth regress silently.

`days` is the effort field and holds a number, so `T-002` estimates `1.5` — a dotted value that is a
**quantity, not a label**, and the exemption for the effort and value fields is the only thing that
stops it being reported. It is a real shape: a project that estimates in days writes it on the first
task it files, which is why the exemption exists at all (T-137).

No vocabulary enumerates `days`, or anything else. Every check here has to work from shape.

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
