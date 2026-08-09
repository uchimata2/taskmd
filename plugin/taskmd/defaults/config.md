---
# ---------------------------------------------------------------- identity
id_field: id               # front-matter field holding the task id
id_prefix: T-              # ids are <prefix><zero-padded number>
id_width: 3                # pad width, so T-007 rather than T-7
title_field: title         # one-line name, shown in every generated view
tasks_dir: tasks           # where task files live, relative to the project root; must exist

# ------------------------------------------------------------------ status
status_field: status       # which vocabulary below carries open/closed meaning
open_statuses: [proposed, specified, planned, in_progress, blocked, review]
blocked_status: blocked    # the value meaning "held up"; `none` if the project has no such value

# ------------------------------------------------------------- deliverables
deliverables_field: deliverables   # field listing the paths a task produces; `none` to not track them

# ---------------------------------------------------------------- ordering
value_field: business_value  # estimated worth; `none` to not order by it
effort_field: effort         # estimated cost; `none` to not order by it

# ------------------------------------------------------------------- hooks
after_write: none          # command taskmd runs after it writes a file; `none` for no hook

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

## The tasks folder

`tasks_dir` is the only value here that names a folder, and **the folder has to exist**. A value
pointing at nothing is an error when this file is read, naming the key and the value — not a
project that silently contains no tasks. Without that rule `tasks_dir: taks` made `check` exit 0 on
a project it had never opened, which is worse than no validator because a validator is believed.

The rule does not care whether you wrote the value or inherited it from this file: a project
adopting taskmd creates its tasks folder before the first command works. That is the whole of
setup, and there is no command to do it — no command creates a folder, and there is deliberately
no `init`. An **empty** tasks folder is entirely legal; the distinction is that
the folder is absent, not that it holds nothing yet.

## The blocked status

`blocked_status` names the one status value that asserts "this is held up by something". `check`
reports a task carrying it with no dependency recorded — a claim about the graph that the graph
does not support, which is invisible to every other check because the file is otherwise valid.

It must be a value in the status vocabulary. Set it to `none` if the project has no such value;
`check` then makes no such claim. Like every key here it is required to be written.

## Deliverables

`deliverables_field` names the front-matter field holding the paths a task produces, relative to
the project root. `check` reports a declared path that does not exist — the one thing the
retired `deliverables` command did that nothing else does, kept as a validation rather than as a
command of its own.

Set it to `none` if a project does not track outputs that way. It is still a **required** key:
every key must be written, because a config replaces the default rather than merging with it, and
a silently absent key would hand you a schema you did not write.

## The hook

`after_write` is a command **the project owns** and taskmd runs — a consistency check, a
formatter, whatever the project needs. taskmd ships none: a hook that arrived with the tool would
be the tool doing something the project never asked for.

**Written as a program followed by its arguments**, not as a shell line. That shape is what makes
the command checkable *before* it runs: a first token containing a slash is a file in the project,
anything else is looked up on PATH, and either way a hook that could never run is an error when
this file is read rather than a surprise inside a command someone was trying to finish. It is also
what makes the hook language-free — name an interpreter (`bash tools/audit.sh`,
`pwsh -File tools/audit.ps1`) or name an executable the project ships. Write paths with forward
slashes; they are translated for the platform.

**One invocation point, and it is after the write.** A pre-write point would catch a bad edit
before it landed rather than after, which is a genuine advantage and was deliberately not taken:
it is speculative, and every additional point is a key an adopting project pays to have
documented, validated and kept true. Adding a second later costs a schema change, which is cheaper
than carrying one nobody asked for.

**A hook that fails fails the command that ran it**, and its output is shown. A tool that ran your
consistency check and then reported success anyway would be worse than one that never ran it. The
write has already happened when the hook runs, so a failure reports a problem rather than undoing
one — the file is on disk either way, and the message says so.

**What it cannot do.** taskmd runs the hook after **its own** write, which today means after
`index` regenerates the index. It never sees an edit made to a task file by a person, an agent or
another tool, so it cannot be the thing that reacts to one. That job belongs to whatever runs the
editing — an agent harness, an editor, a commit hook — and it is the project's to arrange.

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
| business_value | critical, high, medium, low |
| effort | xs, s, m, l, xl |

## Ordering

`list` prints tasks in one order unless asked otherwise, and this is the only description of it.
The code implements what is written here; it does not restate it.

**The ranking is the vocabulary order — best value first.** The rows above are ordered
deliberately: `critical` outranks `high`, and `xs` is cheaper than `s`. There is no second table
mapping a value to a number, because that would be a second copy of a fact this row already
carries, and the two would disagree the first time someone added a value to one of them.

**A task sorts on four keys, in order:**

1. **Blocked last.** A task with an open dependency cannot be started, so it sorts after every task
   that can. It is still listed — hiding it would make `list` and `list --limit 1` describe
   different sets, and would conceal the graph from someone asking why nothing is moving.
2. **Effective value, best first.** A task's effective value is the best value among **itself and
   everything it transitively unblocks**. This is what "dependencies first" means: a cheap blocker
   is pulled ahead *by what it releases*, rather than sitting behind unrelated work while the
   valuable task waits on it. Effective value is derived per call and stored nowhere.
3. **Effort, cheapest first.**
4. **Id**, so the order is total and the same tree always gives the same answer. A tie broken by id
   is stated rather than arbitrary.

**A task with no estimate still sorts and is still listed**, after every task that has one. Nothing
in this tool requires a human to fill these in for the answer to be correct — the agent estimates
them, and a value someone edits by hand is honoured and never overwritten.

Set `value_field` or `effort_field` to `none` to drop that key from the sort. With both set to
`none` the order is blocked-last, then id.
