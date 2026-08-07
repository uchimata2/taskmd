---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: tasks
status_field: status
after_write: none
open_statuses: [proposed, blocked]
blocked_status: none
deliverables_field: none
value_field: business_value
effort_field: effort
context_fields: [status]
index_columns: [status]
---

# Ordering fixture

Four tasks, built so the two readings of "dependencies first" give different answers. Nothing here
is broken; the project is valid and `check` passes. What it exercises is the sort.

T-001 is the least valuable and cheapest task, and it blocks T-002, which is the most valuable.
Under the rule taskmd implements, T-001 leads because its **effective** value is T-002's. Under the
plain reading -- each task ranked on its own value -- T-003 would lead. The tests assert the first.

T-004 carries no estimates at all, which must not remove it from the listing.

## Edges

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, blocked, done |
| business_value | critical, high, medium, low |
| effort | xs, s, m, l, xl |
