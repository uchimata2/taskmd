# taskmd — `index` can drop a task written during its run, and `check` then reports OK

| Field | Value |
| :--- | :--- |
| **Target** | `taskmd` — the maintainer's own repository, cloned beside the reporting project |
| **Kind** | Defect |
| **Status** | `open` |
| **Found while** | Two sessions working the same `tasks/` folder, on 2026-08-24 |
| **Version seen** | `0.6.0` |

## Observation 1 — a task file present on disk was left out of the index, and nothing said so

Sequence, as observed:

| Step | What happened |
| :--- | :--- |
| 1 | Another session created `tasks/E28-make-the-d7-annex-claims-traceable.md` |
| 2 | `index` in this session printed `Wrote tasks/README.md - 7 active, 20 closed` |
| 3 | `check`, run immediately after, printed `OK - 27 task(s)` |
| 4 | `grep -c E28 tasks/README.md` returned **0**, while the file existed with `status: proposed` |
| 5 | A second `index` printed `7 active, 21 closed`, and `check` printed `OK - 28 task(s)` |

So the index was written without a task that existed, and the validator that ran next called it OK.

**What is established:** the index omitted E28 while the file was on disk, and `check` did not
report it. **What is not:** whether E28's file was complete at the moment `index` read the
directory. The run that produced the bad index and the run that fixed it differ only in time.

**The cheap guard, whatever the cause.** `check` already reads every document. Comparing the number
of task files against the number of index rows, and failing when they differ, catches this class
without needing to know which side was late. Today the two numbers can disagree and the exit is
clean.

## Observation 2 — nothing allocates ids, so two sessions can pick the same one

Choosing the next id means reading the folder and adding one. With two sessions that is a race. It
was avoided here only because the id was re-derived immediately before the write:

```
ls E*.md | sed -n 's/^E\([0-9][0-9]\).*/\1/p' | sort -n | tail -1
```

The first reading said the next free id was E29; by the time the file was written another session
had taken E29 and the correct answer was E30. An id picked from an earlier reading in the same
session would have collided silently, since two files can carry the same `id:` and only `check`
would notice.

Same root cause as observation 1: the folder is treated as a snapshot that does not move.

## Proposed fix

Not settled, and the two observations may not want the same answer. The count comparison in `check`
is small, self-contained and useful on its own — worth doing regardless of what is decided about
concurrent writers.
