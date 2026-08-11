---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: tasks
status_field: status
deliverables_field: none
blocked_status: none
value_field: none
effort_field: none
after_write: none
open_statuses: [proposed]
context_fields: [status]
index_columns: [status]
---

# A config whose tasks_dir names something that is not a folder

Every key is valid and every value is well-formed, and `tasks` is *there* - as a file. The one
defect is that a folder was expected and a file was found.

This is the third of the `tasks_dir` cases and the only one where the name resolves. Its neighbour
`broken-tasks-dir` misspells the value so nothing is there at all, and the two must be told apart
in the message: denying the existence of a name the reader can see, and then advising them to
create it, gives a remedy that cannot be followed (T-024).

Deliberately minimal rather than a copy of the shipped default, for the same reason `broken-config`
and `broken-tasks-dir` are - a fixture that duplicated the real schema would be a second home for
it. No `## Edges` section: edges are optional, and this fixture is about a path, not a graph.

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
