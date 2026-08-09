"""Generate a taskmd project of a given size, so the scale ceiling can be measured (T-004).

    python tests/scale.py <count> <width> <destination>

Writes `<destination>/.taskmd/config.md` and `<destination>/tasks/` holding `<count>` tasks whose
ids are `<width>` digits wide. The destination must not already exist.

**Why a generator rather than a saved fixture.** A timing nobody can re-take is the unverified
claim this project exists to avoid, and five thousand task files in the tree would be read by every
run of `check`, of the link check and of the pre-publish grep. So the script is tracked and what it
writes is not.

**The shape is copied from this repository, because it is the only real taskmd project there is.**
Measured over its 81 tasks on 2026-08-09: 46% carry a parent, there are 0.41 `blocked_by` and 3.1
`related` entries per task, 7 Markdown links in a body, and the average file is 15.5 kB. A project of
tiny unlinked files would time the directory walk and skip `derive`, the sort and the link check,
which is most of what a command does — so it would measure something nobody runs.

Every edge points at a **lower** id. That is what keeps the graph acyclic and every reference
resolvable, so `check` on a generated project reports nothing and the timing is of the work rather
than of building an error list.
"""

import os
import sys

USAGE = "usage: python tests/scale.py <count> <width> <destination>"

DEFAULTS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        os.pardir, "plugin", "skills", "taskmd", "taskmd", "defaults", "config.md")

# The measured shape of this repository, in the order the docstring states it.
PARENT_IN = 2          # every 2nd task carries a parent, which is the 46%
BLOCKED_IN = 5         # every 5th, giving 0.4 per task
RELATED = 3            # 3 per task once there are 3 lower ids to point at
LINKS = 7              # Markdown links in a body
BODY_BYTES = 15500

STATUSES = ["proposed", "specified", "planned", "in_progress", "review", "done"]
PHASES = ["specify", "plan", "implement", "review"]
TYPES = ["analysis", "decision", "deliverable", "research", "fix", "admin"]
VALUES = ["critical", "high", "medium", "low"]
EFFORTS = ["xs", "s", "m", "l", "xl"]

PARAGRAPH = (
    "The step was worked in the planned order and the result recorded as it arrived, so the reason "
    "for each choice is written where the choice was made rather than reconstructed afterwards. "
    "What it rules out is stated beside it, because a decision without its rejected alternatives is "
    "re-litigated by the next reader. "
)


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def config(width):
    """The shipped defaults with one line changed, so the generated project has no second schema."""
    with open(DEFAULTS, encoding="utf-8") as handle:
        text = handle.read()
    out = []
    for line in text.split("\n"):
        if line.startswith("id_width:"):
            line = "id_width: %d" % width
        out.append(line)
    return "\n".join(out)


def body(task_id, number, links):
    """A body of about `BODY_BYTES`, carrying `LINKS` links that all resolve."""
    parts = ["# %s — Generated task %d\n" % (task_id, number),
             "\n## 1. Specify\n\n**Outcome**\nA generated task, so a command has something to read.\n"]
    for target in links:
        parts.append("\nSee [%s](%s) for the decision this one rests on.\n"
                     % (target, filename(target)))
    parts.append("\n## 3. Implement\n\n")
    while sum(len(p) for p in parts) < BODY_BYTES:
        parts.append(PARAGRAPH)
    parts.append("\n\n## Log\n\n| Date | Status change | Note |\n| :--- | :--- | :--- |\n"
                 "| 2026-08-09 | (no change) | Generated. |\n")
    return "".join(parts)


def task_id(number, width):
    return "T-%0*d" % (width, number)


def filename(an_id):
    return "%s-generated-task.md" % an_id


def task(number, width):
    an_id = task_id(number, width)
    lower = [task_id(n, width) for n in range(1, number)]
    parent = lower[number // 3] if lower and number % PARENT_IN == 0 else "null"
    blocked = [lower[0]] if lower and number % BLOCKED_IN == 0 else []
    related = lower[-RELATED:] if len(lower) >= RELATED else []
    front = [
        "---",
        "id: %s" % an_id,
        "title: Generated task %d" % number,
        "type: %s" % TYPES[number % len(TYPES)],
        "status: %s" % STATUSES[number % len(STATUSES)],
        "phase: %s" % PHASES[number % len(PHASES)],
        "parent: %s" % parent,
        "blocked_by: [%s]" % ", ".join(blocked),
        "related: [%s]" % ", ".join(related),
        "work_package: none",
        "owner: maintainer",
        "business_value: %s" % VALUES[number % len(VALUES)],
        "effort: %s" % EFFORTS[number % len(EFFORTS)],
        "created: 2026-08-09",
        "updated: 2026-08-09",
        "deliverables: []",
        "---",
        "",
    ]
    return "\n".join(front) + body(an_id, number, (lower * LINKS)[:LINKS])


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(argv) != 3:
        print(USAGE)
        return 2
    count, width, dest = int(argv[0]), int(argv[1]), argv[2]
    if 10 ** width - 1 < count:
        print("%d task(s) do not fit in %d digit(s) - the widest id is %s"
              % (count, width, task_id(10 ** width - 1, width)))
        return 2
    if os.path.exists(dest):
        print("%s already exists" % dest)
        return 2
    os.makedirs(os.path.join(dest, ".taskmd"))
    os.makedirs(os.path.join(dest, "tasks"))
    write(os.path.join(dest, ".taskmd", "config.md"), config(width))
    for number in range(1, count + 1):
        an_id = task_id(number, width)
        write(os.path.join(dest, "tasks", filename(an_id)), task(number, width))
    print("%d task(s), id width %d, in %s" % (count, width, dest))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
