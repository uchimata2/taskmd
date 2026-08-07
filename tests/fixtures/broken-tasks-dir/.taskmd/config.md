---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: taks
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

# A config whose tasks_dir names a folder that is not there

Every key is valid and every value is well-formed. The one defect is that `taks` is not a folder -
the task files are next door in `tasks/`, where the typo cannot reach them.

This is the second half of the config-error class. `broken-config` misspells a *key*, which was
always caught; misspelling a key's *value* was not, and the result was worse than a wrong answer:
`check` exited 0 on a project it had never read, `index` created `taks/` so the mistake acquired a
plausible artefact, and `context` blamed the task the user was trying to start.

Deliberately minimal rather than a copy of the shipped default, for the same reason `broken-config`
is - a fixture that duplicated the real schema would be a second home for it. No `## Edges`
section: edges are optional, and this fixture is about a path, not a graph.

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
