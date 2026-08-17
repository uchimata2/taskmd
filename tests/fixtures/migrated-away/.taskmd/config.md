---
id_field: id
id_prefix: '#'
id_width: none
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

# A project that moved its tasks to a backend and kept no folder

Nothing here is misconfigured. `id_width: none` says the ids are handed out by a backend, and
`tasks_dir` names a folder that is deliberately absent because the tasks are not files any more.

**The point of the fixture is what the commands *say*, not that they refuse.** Refusing is right —
all four read a folder, and there is no folder. What was wrong before T-164 is that both remedies
offered assumed the absence was a mistake: *create it, or correct tasks_dir*. A project that has
migrated cannot follow either, and was given no third possibility, so the message read as a defect
in the project rather than as a command that does not apply to it.

Distinguished from `broken-tasks-dir`, which is the genuine version of the same shape — a typo, a
folder that should be there. That one must keep the old message exactly, or this fix has traded one
misleading sentence for another.

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
