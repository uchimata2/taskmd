---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: .
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

# A config whose tasks_dir is the project root

Every key is valid, every value is well-formed, and the folder named certainly exists - it is the
root. The one defect is that naming it makes `discovery.is_project` true of **every directory in
existence**, because that test asks whether `<folder>/<tasks_dir>` is a directory. So every
subdirectory looks like a nested project, is skipped, and `check` reports success over a tree it
never read (T-078).

That is why this fixture has files below the root: the defect is not what the run *says*, it is what
the run silently declines to look at. A fixture whose whole content sat at the top would have passed
while the bug was fully present.

Deliberately minimal rather than a copy of the shipped default, for the same reason its `tasks_dir`
neighbours are. No `## Edges` section: edges are optional, and this fixture is about a path.

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
