---
# ---------------------------------------------------------------- identity
id_field: id               # front-matter field holding the task id
id_prefix: T-              # ids are <prefix><zero-padded number>
id_width: 3                # pad width, so T-007 rather than T-7; `none` if a backend allocates them
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
context_fields: [status, phase, type, work_package, owner, adopter_visible, waiting_on]
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

Task files are the opposite: a front-matter field this schema does not name is **carried, never
interpreted**. Carried is literal — taskmd never writes a task file, so an unnamed field cannot
be altered or dropped by anything the tool does. It is not *shown* by default: name it in
`context_fields` or `index_columns` below and it appears, with no code change and no schema
entry, because both keys take any field name at all. That is what lets a project adopt taskmd
without first rewriting its task files.

## When this file moves ahead of yours

A config **replaces** this file rather than merging with it, which is the rule above and is not
changing. Its price is that a project which copied this file and then stopped looking cannot see a
value added here afterwards — and that is not hypothetical: a project copied it the day before
`audit` joined the `type` row, could not see the change, and raised work to fix a defect that had
already been fixed here.

So `check` says so. **One line per drifted row**, naming the row and the difference:

```
CONFIG DRIFT  type: shipped default adds 'audit'; this project's row does not carry it
```

**It is advisory and never a problem.** The exit status does not move and the count of problems does
not change, because pinning is legal — a validator that failed on a legal state is one a project
starts passing flags to.

**Only one shape is reported: a row you still keep, missing a value this file has since gained.**
Everything else a config does is a choice rather than a lag, and reporting choices would make every
configured project noisy from its first run — extra values, extra rows, renamed fields and every
front-matter setting are the whole point of writing a config. A row you deleted is *delete a row to
stop checking one*, above, and is left alone. A project using this file with no config of its own is
not compared at all: it cannot be behind what it is using.

**You still keep a row when it carries at least one of this file's values** — sharing the field name
is not enough. A row whose values you wholly replaced has left this vocabulary rather than fallen
behind it, and is not compared: an issue tracker's `status` is `open, closed`, which is the commonest
way to adopt and would otherwise be told, on every run, about eight values it has no use for.
The price is that a row you replaced *entirely* stops telling you about a value added here later —
paid because the line for such a row named the whole vocabulary anyway, so it never distinguished the
new value from the ones you dropped on purpose. Keep one value and the reporting comes back.

**There is no key to switch it off**, and that is a constraint rather than a preference — for the
reason the next section gives. A project that pinned deliberately reads one line that names exactly
what it decided not to have.

## A label that reads as a version

`check` prints one advisory line per front-matter value shaped like a two-part number — `v0.2`,
`2.1` — naming the field, the value and how many tasks carry it:

```
LABEL SHAPE  work_package: 'v0.2' on 47 task(s) reads as a version; a release of that number is a different thing
```

**Group your work under a label that cannot be parsed as something installable** — `M2`, `PH2`,
`hardening`. A grouping and a release are two sequences and they come apart the first time a version
is bumped for a reason other than finishing a group, which happens to every project that ships fixes
between milestones. The label then does not go stale, which would be visible. It **resolves**, to a
real tag holding something else. Two projects reached this independently before the line existed;
one of them ran 135 tasks under it and needed a hand-written table to stay legible.

**It reads the shape of a value and never the name of a field.** There is no key naming your
grouping field, and that is not an omission: `work_package` above is a field this schema *names* and
does not interpret, so a rule keyed on a field name would need a new key — and the next section says
what a new key costs everyone. Reading the shape also catches the defect under a field name nothing
here mentions, which is strictly more than a key could do.

**Three or more components is never reported.** `0.4.0` is a version recorded correctly, and a
project that keeps the version its work shipped in should keep writing it. **The fields named by
`value_field` and `effort_field` are exempt**, because a project estimating in days writes `1.5` and
means a number.

**It is advisory and never a problem**, and there is no key to switch it off — the same shape and
the same reasoning as the drift line above. Version-shaped labels are legal, and a project that
means them reads one line per distinct label.

## Adding a key to this file is a breaking change

Three rules already stated here compose into a fourth that is easy to meet only by being bitten:

1. A config **replaces** this file rather than merging with it.
2. So every key must be **written**, including the ones set to `none`.
3. So a **missing** key is an error naming the key — not a silent fallback.

Therefore **the moment this file gains a key, every project that wrote its own config fails on the
next upgrade**, with an error naming a key nobody there has heard of, in a project that changed
nothing. Read the rules in the other order and it is obvious; read them in the order they arrive and
it is a surprise, which is what happened while designing the drift line above.

That is the price of the three, not a defect in any of them. Each does the job it was written for,
and without them a silently absent key hands you a schema you did not write.

**If it happens to you**, the error names the key. Add it, with the value and meaning documented
here — this file is the only description of what any key means, so the line to copy is in it. That
is the whole of the upgrade.

**It is deliberately not automated.** An optional key, a merge on upgrade, or a version marker in
every config would each be larger than the problem — no key has been added since this schema shipped
— and each would weaken rule 1, which is what makes a config say exactly what a project meant.

## What this rule has already refused

Two capabilities have been asked for under the rule above and declined, recorded here so the next
person to want one meets the answer instead of the gap. Both needed the tool to learn a fact about
*where a task has got to*. That is project vocabulary, and vocabulary is a key in this file.

- **`check` knowing a task's phase**, so that a placeholder left in a section the task has already
  passed is reportable, and not only one left in a closed record. Every route that works adds a key
  here. The routes that add none are worse than the cost: `context_fields` and `index_columns` name
  fields to **show**, so reading one of them as *this is the phase field* gives a display list a
  second meaning, and a project that stopped showing the field would silently stop being checked. A
  project that never names it would never be checked at all, and the check could not say so.
  Hardcoding the field name instead puts one project's vocabulary inside the tool, which is what
  `BINDING.md` exists to prevent.
- **A field required at a status, or two fields that must agree** — *this field is set when a task
  closes*, or *these two always move together*. Declined on the same ground, by the same routes
  failing the same way.

**What a project does instead.** Where the point is that a record should not look finished when it is
not, the record can say so itself: a section stating that the phase was never run reads correctly to
a person, needs no key, and cannot drift from a rule. Where the convention genuinely has to be
enforced rather than stated, enforce it outside taskmd and against the task files directly. They are
Markdown with front matter, in a folder this file names, and nothing about them is hidden from a
script a project writes for itself.

Neither refusal says the capability is worthless. Both are the arithmetic above: the cost falls on
every project that has written a config, it falls on the upgrade rather than at the moment of asking,
and it falls whether or not that project ever wanted the feature.

## Ids a backend allocates

`id_width` is a number, and `none` when the ids are **not yours to shape** — handed out by whatever
backend holds the tasks. Set that way, an id is the prefix plus any number of digits, so `#7`, `#41`
and `#1024` are all ids in one project, which no number can describe.

**It is not a way to switch the width check off**, and the difference is not a matter of taste.
Where you compose your own ids, the width is what makes a mistyped one reportable: a file carrying
`T-0001` under `id_width: 3` is not quietly a task, it is named and left out, and that is the only
thing standing between a typo and a task that silently exists in no view. Where the backend
allocates, an id **cannot** be mistyped, because it is never composed — `create` returns it and the
project reads it back. So `none` removes a rule that has nothing to catch, and a project that sets
it while still writing its own ids has removed one that has.

Two consequences follow, and neither needs configuring. Nothing can report a wrong-width id in such
a project, because there is no width to be wrong about. And composing an id pads to nothing —
`#7`, not `#007` — which keeps a composed id a legal one, though on a backend that allocates there
is no reason to compose one at all.

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

**Abandoning a task means clearing this field.** The list asserts production, so a task closed
without producing anything must stop claiming it did — the same act as writing why it was
abandoned, not an extra step. A path reported on such a task is a stale record rather than a
missing output, and `check` says the same thing either way: it can see that the path is gone, not
why it was declared. There is deliberately no key naming an abandoned status, because the only
thing one could buy is silence about a claim the task no longer makes.

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

**These are defaults worth having, not the set of nouns METHOD uses.** `research` is here and the
method never mentions it; `audit` is here *and* METHOD §5 names it, which is a coincidence of
usefulness rather than a rule that the two must agree. Do not treat this table as derived from the
method — replace any row that does not suit your project. `audit` was added on 2026-08-09 after two
independent projects reached for it and neither could validate (T-088).

**`decision` is the one value here with a stated test, because it is the one people filter on to ask
what is waiting on an answer.** Read the task's stated **outcome**: if that outcome is an answer
someone else could act on, the type is `decision`, whatever else the task changes on the way there.
A task that already knows what it will change is not a decision however much detail it has left to
work out, and a task that cannot name the change until it has answered something is one even if the
answer turns out to be a single line. Where a task is honestly both, `decision` wins — the answer is
what somebody is waiting on, and the change follows from it. Note that this reads the outcome and not
the title: *settle whether…* in a title with a behaviour underneath it is a `fix`, and a filter built
on titles finds the wrong set (T-109).

**If you keep a decisions register beside your tasks, read where the method puts a decision before
deciding which of the two holds what** — METHOD §6, *where facts live*. A project that adopts
`decision` here and keeps a register as well has two homes for one fact and no rule choosing between
them, which is the failure this schema exists to avoid (T-104).

*Named rather than linked, like every other pointer in this file: it is copied into your project as
`.taskmd/config.md`, and a relative link would resolve from there and not from here.*

| Field | Values |
| :--- | :--- |
| status | proposed, specified, planned, in_progress, blocked, review, done, cancelled |
| phase | specify, plan, implement, review |
| type | analysis, decision, deliverable, research, fix, admin, audit |
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

1. **Blocked last, and marked.** A task with an open dependency cannot be started, so it sorts after
   every task that can. It is still listed — hiding it would make `list` and `list --limit 1`
   describe different sets, and would conceal the graph from someone asking why nothing is moving.
   Order alone is not the answer, though: it says a boundary exists without saying where it falls, so
   `list` appends a trailing column carrying `blocked`. That column is **absent from a project that
   has no blocked task**, which is the omit-when-unused rule under *Views*, and present on every row
   otherwise — the test is project-wide, so every call has the same shape. `list --json` carries
   `blocked` on every task unconditionally, because a caller should not have to know what the project
   looks like today.
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

## Views

`context_fields` and `index_columns` name what the two **views** show — the `context` header, and
the generated index's columns. Both take any field name, including one this schema does not
interpret.

**A view omits a column no task has a value for; a contract does not.** So a field named here but
unused by every task in the project is simply absent from `context` and from the index — a column
of dashes costs a reader, and an agent, and tells them nothing. The moment one task carries a
value, the column is there, with nothing to switch on and no config to edit. The test is
project-wide rather than per-task, so every task's `context` header has the same shape.

The contract surfaces are the other half of that sentence. `taskmd list --json` and its
tab-separated form emit **every** configured column whether it is used or not, because a key that
disappeared when a field fell out of use would be a breaking change to a script that did nothing
wrong.

**A field named here can also be selected on.** `taskmd list --<field> <value>` accepts any field
either key names, not only the ones a vocabulary below enumerates — otherwise a field could be
*shown* and not *filtered*, which is where a reader goes the moment a view gets long. A value that
no vocabulary enumerates is matched literally and is not validated: with no list to check it
against, an empty result is the honest answer and an error would be a guess at a typo the tool
cannot detect. The field **name** is still checked, and an unknown one is reported with everything
the project does accept.

The same rule has always governed **edge** columns — parent, children, blocked_by and the rest —
which are not configured here at all: they are derived from the `## Edges` table and appear when
some task uses them. For a **dependency** edge, *uses* means an edge that is still outstanding: a
cell shows only the blockers and blocked tasks that are still open, and the column goes when none
are, because a cell that cannot show the far end's status has to resolve it.
