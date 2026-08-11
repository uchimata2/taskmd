---
id_field: id
id_prefix: #
id_width: none
title_field: title
tasks_dir: issues
status_field: status
deliverables_field: none
value_field: none
effort_field: none
blocked_status: none
after_write: none
open_statuses: [open]
context_fields: [status]
index_columns: [status]
---

# A project whose backend allocates the ids

`id_width: none` — the value that says the ids are **handed out by the backend**, so this project
describes them rather than imposing a shape on them. Its ids are `#7`, `#41` and `#1024`: no single
width describes all three, which is the whole reason the value exists (T-082).

**This is not a way to switch the width check off.** On a backend that allocates, an id cannot be
mistyped because it is never composed — `create` returns it and the project reads it. A project that
writes its own ids has the opposite need, and `id_width: 3` catching a wrong-width file is what
`tests/fixtures/broken-id-width` exists to prove. Both fixtures have to keep passing, in opposite
directions.

`#` is a legal prefix and is the one the GitHub binding names. It survives the config parser because
a comment is whitespace-then-`#` and this value has no whitespace before it. It is deliberately
**unquoted**: this parser strips no quotes, so `'#'` would be a three-character prefix.

## Edges

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | open, closed |
