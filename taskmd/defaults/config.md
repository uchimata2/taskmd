---
# ---------------------------------------------------------------- identity
id_field: id               # front-matter field holding the task id
id_prefix: T-              # ids are <prefix><zero-padded number>
id_width: 3                # pad width, so T-007 rather than T-7
title_field: title         # one-line name, shown in every generated view
tasks_dir: tasks           # where task files live, relative to the project root

# ------------------------------------------------------------------ status
status_field: status       # which vocabulary below carries open/closed meaning
open_statuses: [proposed, specified, planned, in_progress, blocked, review]

# ------------------------------------------------------------------- views
context_fields: [status, phase, type, work_package, owner]
index_columns: [work_package, status, phase]
---

# taskmd — default schema

This is the schema taskmd uses when a project has no `.taskmd/config.md` of its own, so a
clone works with no configuration at all. It is also the **only** description of what a
config may contain: every key that exists is above or below, annotated. To adapt taskmd to a
project, copy this file to `.taskmd/config.md` and edit it.

There is no second copy of this schema in the code. `taskmd/schema.py` ships no defaults of
its own — it loads this file. A default written in both a Python literal and a doc is two
copies of one fact, which is the drift this plugin exists to remove.

## Format

Deliberately the same shape as a task file: a front-matter block for scalars and lists,
Markdown tables for anything with more than one column. taskmd already parses both shapes to
read task files, so the config costs no parser and no dependency.

- Lists take either `[a, b, c]` or a block of `  - a` lines.
- ` # ...` after a value is a comment and is stripped. A value may not contain ` #`.
- Only the keys documented here are accepted. **An unknown config key is an error**, not a
  silent no-op — a typo that was ignored would hand you a schema you did not write.

Task files are the opposite: a front-matter field this schema does not name is **carried and
displayed, never interpreted**. That is what lets a project adopt taskmd without first
rewriting its task files.

## Edges

The graph. `Field` is the front-matter field a task stores; `Derives` is the name of the
inverse, which is **computed and never written down** — that is the plugin's one design rule.
Record the edge on the task that is blocked, not on the blocker.

`Kind` is fixed vocabulary: taskmd implements exactly these three, because each is a
different traversal in code. Their *names* are yours; the set of kinds is not.

| Kind | Shape | Inverse |
| :--- | :--- | :--- |
| `hierarchy` | at most one value | derived, a list, under the name in `Derives` |
| `dependency` | a list | derived, a list, under the name in `Derives` |
| `soft` | a list | derived **symmetrically**, under its own name — write `-` |

A soft link has no separate inverse name because both ends mean the same thing, so it is derived
under the field's own name: write `related: [T-004]` on one task and **both** tasks show the link.
Writing it on both is allowed too — it collapses to one entry, so nobody needs to know which side
"owns" it. Whichever task you open, you see every link it has.

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

Enumerated fields. A value outside its list is a typo, and `check` says so. Add a row to
enumerate another field; delete a row to stop checking one.

`status_field` above names which of these carries open/closed meaning, and `open_statuses`
names the subset that counts as open — everything else in that row is closed. The vocabulary
itself is written once, here.

| Field | Values |
| :--- | :--- |
| status | proposed, specified, planned, in_progress, blocked, review, done, cancelled |
| phase | specify, plan, implement, review |
| type | analysis, decision, deliverable, research, fix, admin |
