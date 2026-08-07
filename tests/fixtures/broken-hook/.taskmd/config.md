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
after_write: hooks/after-write.sh
open_statuses: [proposed]
context_fields: [status]
index_columns: [status]
---

# A config declaring a hook that is not there

Every key is valid and every value is well-formed. The one defect is that `hooks/after-write.sh`
does not exist, so the command this project declares could never run.

This is the third member of the config-error class, after `broken-config` (a misspelled key) and
`broken-tasks-dir` (a key whose value names a folder that is not there). All three share one
property: the defect is in the configuration rather than in a task, so reporting it from inside
whichever command first needed it would blame the wrong thing.

**What makes it catchable at all is the shape of the declaration.** A hook is written as a program
followed by its arguments, so taskmd can ask whether the program is there without running it. Had
the value been a free shell line, "is this runnable?" would have no answer short of running it, and
the report would necessarily arrive mid-command.

Deliberately minimal rather than a copy of the shipped default, for the same reason `broken-config`
and `broken-tasks-dir` are - a fixture that duplicated the real schema would be a second home for
it. No `## Edges` section: edges are optional, and this fixture is about a command, not a graph.

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
