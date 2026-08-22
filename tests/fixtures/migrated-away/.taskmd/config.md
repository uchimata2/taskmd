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

**The point of the fixture is what the commands *say*.** What was wrong before T-164 is that both
remedies offered assumed the absence was a mistake: *create it, or correct tasks_dir*. A project that
has migrated cannot follow either, and was given no third possibility, so the message read as a
defect in the project rather than as a command that does not apply to it.

*This paragraph opened with "Refusing is right — all four read a folder, and there is no folder",
written 2026-08-17. The date is kept because the sentence stopped being true on 2026-08-19, when
T-185 split `check`, and nothing brought it forward.* **Three refuse and `check` does not.** Measured
2026-08-22, from the project root:

```text
$ taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md
1 problem(s) - 3 document(s), 2 link(s), ...
Scope  no task file was read, and the checks that open one did not run. ...
exit 1

$ taskmd context T-1 --root tests/fixtures/migrated-away
CONFIG ERROR  ... Or nothing here is broken and these commands do not apply: ...
exit 2        and `index` and `list` are the same message and the same code
```

Distinguished from `broken-tasks-dir`, which is the genuine version of the same shape — a typo, a
folder that should be there. That one must keep the old message exactly, or this fix has traded one
misleading sentence for another. **Since 2026-08-19 the two differ in behaviour and not only in
wording**, which is a stronger distinction than the one this paragraph was written to hold. Measured
the same day: `check` on `broken-tasks-dir` prints `tasks_dir is 'taks'` with the two old remedies
and exits 2, having run nothing; here it runs the document checks and exits 1.

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
