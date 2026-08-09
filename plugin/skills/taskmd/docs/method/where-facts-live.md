# Where each kind of fact lives

> Referenced from [`../METHOD.md`](../METHOD.md) §6. Load it when you are about to write something
> down and are not certain where it belongs.

Core rule 3 applied. Every fact has exactly one home; everything else **points** at that home.

These are **roles**, not locations. The binding says which artifact plays each role for a given
tracker — "that task" is a file in one project and an issue in another, and the method does not
care which.

| Fact | Home |
| :--- | :--- |
| What a task is for, needs, and produces | that task |
| A task's phase, status and edges | that task's recorded properties |
| Which tasks exist and what state they are in | derived from the tasks — never maintained by hand |
| A decision made while doing a task, and why | that task |
| A decision someone else must make before the work can proceed | wherever the project registers open decisions, referenced from the task it blocks |
| The working method | [`../METHOD.md`](../METHOD.md) and the files it points at |
| Why a rule in the method is the way it is | [rationale](rationale.md) |
| How the method maps onto this tracker | the binding |
| Conventions, standards and environment rules for the project | the project's own conventions document |
| A lesson that outlives the task that taught it | the project's conventions document, not the task |
| Where to resume next session | the resumption note — pointers only, never content |

## When it seems to belong in two places

The tie-break is in [`../METHOD.md`](../METHOD.md) §6. What follows is why it is worth obeying when
it feels pedantic.

The instinct to write it in both is almost always the desire to save the reader a click, and it is
almost always wrong: the two copies are identical on the day they are written and are the only
places anyone will look afterwards, so when one is updated the other becomes a confident, plausible
lie. A pointer cannot do that.

Two consequences worth stating, because they are the cases people talk themselves out of:

- **A summary is a copy.** "Just the gist, for convenience" drifts exactly like a full duplicate,
  and is harder to spot because it never looked authoritative.
- **A fact learned in a task rarely stays a task fact.** If it will matter to the next task too, its
  home is the project's conventions, and the task points there. Leaving it in the task means the
  next person re-learns it.
