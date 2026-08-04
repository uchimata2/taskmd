# Decisions register

Decisions **only the project owner can make**. They are the most common reason work stalls, so they get ids,
status and an owner like everything else.

This file is the source of truth. Tasks link to a decision with `decisions: [D-NNN]` in their
front-matter — **the forward edge only**. Which tasks a decision blocks is derived:

```
python tools/tasks/task.py context T-001      # shows the open decisions gating that task
python tools/tasks/task.py decisions          # shows every decision and what it blocks
```

`task.py check` fails on a reference to a decision that does not exist here.

**Format:** one row per decision. Keep `id`, `status` and `owner` machine-readable — the tool
parses this table. Everything else is prose.

| id | status | owner | question |
| :--- | :--- | :--- | :--- |
| D-001 | closed | owner | Example of a closed decision — the answer is written into this cell with the date. |
| D-002 | open | owner | Example of an open one. Tasks gated by it carry `decisions: [D-002]`; what it blocks is derived. |

## Closing one

1. Change `status` to `closed` and write the answer into the question cell, with the date.
2. Leave the row in place — closed decisions are the record of what was settled and why.
3. Re-run `task.py index`. Tasks it was gating stop reporting it.

Do **not** delete the `decisions:` reference from the task; it records what shaped the work.
