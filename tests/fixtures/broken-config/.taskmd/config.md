---
id_field: id
id_prefix: T-
id_witdh: 3
title_field: title
tasks_dir: tasks
status_field: status
deliverables_field: none
open_statuses: [proposed]
context_fields: [status]
index_columns: [status]
---

# A config with a typo in a key name

`id_witdh` is not a key taskmd knows. The point of this fixture is *when* that is reported: at
config-read time, naming the key, rather than inside whichever command first needed the width.

Deliberately minimal rather than a copy of the shipped default - a fixture that duplicated the
real schema would be a second home for it, and would go stale the next time a key is added.
