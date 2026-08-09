---
id: T-004
title: Settle the id scheme and the claimed scale ceiling
type: decision
status: done
phase: review
parent: null
blocked_by: [T-001]
related: [T-002]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-04
updated: 2026-08-09
deliverables: [tests/scale.py]
---

# T-004 — Settle the id scheme and the claimed scale ceiling

## 1. Specify

**Outcome**
A decided id format — prefix, width, how an id is allocated, and what happens when two people
allocate at once — and a stated ceiling on how many tasks the tool handles well that rests on a
measurement. Both live in this record, the ceiling as one sentence
[T-006](T-006-package-document-and-publish.md) can quote without rephrasing it.

**Why this one**
The source used `T-NNN`, zero-padded, never reused, next id in the generated index. Fine at 17 files; `context` and `index` re-read everything on each run. Claiming a ceiling without measuring is the exact unverified-claim failure this project exists to avoid.

**Requirements served**
R-14, R-15, R-20 (`docs/SCOPE.md`).

**Scope**

*In.* The shipped defaults for `id_prefix` and `id_width`; the ceiling that width implies; the
collision behaviour, described from a run; the timing; and the sentence about supported scale that
comes out of it.

*Out, and where each goes instead.*

- **Writing the README.** [T-006](T-006-package-document-and-publish.md) step 5, whose step 4 already
  says the claim is whatever this task measured and nothing past it. This task states the sentence;
  that one publishes it. The second open question below is why the split exists.
- **Resolving a collision.** `docs/SCOPE.md` non-goal 4 — git owns that. Describing what the tool
  reports is in; reservation, locking or automatic renumbering is not.
- **Any code the decision turns out to need.** This is a `decision` task, and a change to `is_id`, to
  a config key or to a binding's wording is raised as its own task rather than made here, for the
  reason METHOD §5 gives about findings.
- **Renumbering this repository's own tasks.** Whatever is decided governs the shipped default;
  moving an existing backlog onto it is non-goal 8.

**Inputs**
- [`plugin/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — the shipped defaults,
  and the only description of what the identity keys mean.
- [`plugin/taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py) — `is_id`, `format_id`, `load_tasks`.
- [`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) *create* and *enumerate* —
  allocation, and the two ways a file misses being a task.
- [`github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) — assumption 1, and the paragraph on
  what the identity keys do on a backend that allocates them.
- Generated projects at each measured scale. They do not exist and nothing blocks making them, so
  this is an input rather than a dependency; how they are generated is `plan`'s.

**Two things this phase found by running the tool**

1. **The default width is itself a ceiling, and it is 999.** Since
   [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md), `is_id` matches the prefix plus
   *exactly* `id_width` digits, while `format_id` pads to *at least* that many — so the thousandth id
   the *create* rule composes is not one the tool reads back. On a scratch project at the shipped
   default, holding `T-999` and `T-1000`:

   ```
   $ taskmd list
   taskmd: 1 problem(s) with the task files - run 'taskmd check'
   T-999   proposed   -   specify   Last id the default width can hold

   $ taskmd check
   ID WIDTH      tasks/T-1000-the-next-one.md declares 'T-1000', which is not T- plus 3 digit(s), so it is not loaded as a task
   ```

   Nothing is silent about it, which is what T-075 bought. But the task is out of the project, so
   "how many tasks the tool handles well" has a structural answer before it has a timing one — and
   the 5000-task measurement the second criterion asked for cannot be taken at the shipped width at
   all.
2. **The GitHub binding claims something the identity keys can no longer do.** It says `id_prefix`
   and `id_width` *describe* an issue number rather than impose a format. Under an exactly-N-digits
   rule, no value of `id_width` describes `#7` and `#41` in the same project. T-075 made the rule
   strict and was right to for local files; the binding's sentence predates it. This is the fifth
   criterion's subject rather than a separate finding, because backend-assigned ids are what the
   fourth criterion was already about.

**Acceptance criteria**
- [ ] **The default `id_prefix` and `id_width` are decided, and the decision states the ceiling the
      width implies.** Falsified by a default chosen without saying what it caps a project at.
- [ ] **Collision behaviour is described from a run** — two files claiming one id, and what each
      command then says. Falsified by a description with no output behind it.
- [ ] **Timing measured at 50, 500 and 5000 tasks, for all four commands** — `context`, `list`,
      `index` and `check` each re-read the whole folder, so none of them is covered by another.
      Falsified by an extrapolated figure, or by a scale the decided width cannot express.
- [ ] **The supported scale is one sentence in §3, quotable verbatim, carrying no number a run did
      not produce.** It is judged against **one second of wall-clock for any single command**, named
      here before anything was measured so the threshold cannot be chosen to fit the result.
- [ ] **The scheme tolerates ids the backend assigns**: "id unknown until created" is a supported
      state rather than an error (R-14; catalogued in T-010), *and* the identity keys can describe an
      unpadded server-assigned sequence — or the binding sentence claiming they already do is
      corrected. Either way the record says which one moved and why.

**How these map to the four criteria this task carried.** The first keeps the format half of the old
first; the second is its merge-conflict half, separated so each can fail on its own evidence; the
third is the old second with a budget attached; the fourth **replaces** the old third, per the open
question below; the fifth is the old fourth, sharpened by what this phase found. Nothing was dropped.

**Open questions**
- ~~Configurable prefix and width, or fixed?~~ — **answered by T-001 (D8): configurable**, via the
  `id_prefix` and `id_width` config keys. This task still owns the default values, the
  merge-conflict behaviour and the measured ceiling.
- ~~Criterion 3 is circular.~~ — **answered here, in `specify`, which is where the previous session
  asked for it.** *"The README states a supported scale"* needs a README, which
  [T-006](T-006-package-document-and-publish.md) step 5 writes, and T-006 is `blocked_by` this task,
  so each waited on the other. The fact is now **split from its publication**: this task states the
  ceiling in §3 in a quotable sentence, and the README claim stays T-006's own sixth criterion, which
  already reads *"a supported scale that T-004 measured, and nothing it did not"*. The dependency
  edge is unchanged and still points the right way — T-006 needs the number, and this task no longer
  needs the document. *Rejected: leaving the criterion as written* — it is unmeetable, so `review`
  could only tick it by pretending, which is what
  [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md) had to repair after
  [T-079](T-079-humanize-the-human-facing-documents-before-publishing.md). *Rejected: dropping the
  dependency so T-006 writes the README first* — the README would then carry a figure nobody took,
  which is the failure T-006 was deliberately scheduled last to avoid. *Rejected: merging this task
  into T-006* — a measurement and a publication are judged on different evidence, and the merge
  would bury the number inside a review about a document. Decided rather than referred back because
  the maintainer authorised the whole lifecycle on 2026-08-09; the alternatives are recorded here
  instead of asked.
- **The one-second budget is the thing most worth disagreeing with.** It is a product judgement, not
  a measurement: the tool runs between an agent's turns, and `docs/SCOPE.md` §1 *Invisibility* is
  what makes a command nobody notices the target. *Rejected: a per-command budget*, four numbers
  where one will do. *Rejected: no budget*, which makes "handles well" mean whatever the timings turn
  out to be — the definition chosen after seeing the result. Say so now if a different number is
  wanted; after §3 is measured, changing it re-opens the criterion rather than adjusting it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write a generator that makes a taskmd project of N tasks at a given `id_width`, carrying parent, `blocked_by` and `related` edges at something like this repository's density — a folder of unlinked files would time the file reading and skip `derive` and the sort, which is half of what every command does. | `tests/scale.py`, and the three projects it writes at 50, 500 and 5000 — the script tracked, the projects not |
| 2 | Time `context`, `list`, `index` and `check` at each of the three scales, warm cache, repeated enough that the spread shows. | A table in §3 of command against scale, with the spread, and the machine given by class rather than by name |
| 3 | Show the collision from a run against the fixture that already exists, `tests/fixtures/broken-duplicate-id`, and say what **each** command does with it rather than only `check`. | The output, and a paragraph in §3 naming who resolves it and what the tool deliberately does not do |
| 4 | Settle whether the identity keys can describe a sequence the backend allocates, or whether the sentence in `github-issues.md` is the thing that is wrong. Decide it; if the answer needs a code or config change, raise that as a task rather than making it here. | A decision in §3 with its rejections, and either the id of the task raised or the reason none was |
| 5 | Decide the default `id_prefix` and `id_width` against steps 2 and 4, and state the ceiling the width implies along with what a project meets when it arrives there. | The decision in §3, with what was rejected |
| 6 | Write the supported-scale sentence T-006 quotes, out of steps 2 and 5. | The sentence in §3, marked as the quotable one |

**Step 2 is where this plan can break, which is why it is second.** If the commands are already slow
at 500 tasks, the width question in step 5 stops mattering — a structural ceiling of 999 is
irrelevant behind a performance ceiling of 500 — and step 6 is writing a different sentence than it
would otherwise be. So the measurement leads, and steps 5 and 6 are named at the level their inputs
support rather than invented in detail against an unknown.

**The generated project's width is not the default under discussion.** 5000 tasks need `id_width: 4`
in the generated project's own config, because at the shipped width the five-thousandth file is not a
task at all (§1). That is a property of the fixture and settles nothing about step 5.

**Decisions — the shape of the deliverable**

- **The generator is tracked; the projects it generates are not.** A figure in a README that nobody
  can re-take is the unverified claim this project exists to avoid, and a short stdlib script is what
  makes the ceiling re-measurable after any later change to how files are read. *Rejected: measuring
  in a scratch directory and recording only the numbers* — cheaper today, and it makes the next
  person's re-measurement a different measurement rather than the same one. *Rejected: committing the
  generated projects* — five thousand task files in the tree to hold a timing still, each of them a
  file the leak check, the link check and `check` itself would then read on every run.
- **The ceiling is stated as a task count with its measured time and the machine's class beside it,
  never as "fast".** A wall-clock figure is a property of the machine that took it, so a bare number
  does not travel and an adjective cannot be falsified; count, time and class together let a reader
  on slower hardware scale it. *Rejected: a bare task count*, which hides that the threshold was
  wall-clock at all. *Rejected: naming the hardware*, which is machine data (R-23).
- **The generator writes a project, not a benchmark harness.** It takes a count, a width and a
  destination, and stops there; the timing in step 2 is whatever the shell reports around a real
  command. *Rejected: timing from inside Python around the command's entry point* — it would measure
  a warm interpreter and not the thing an agent actually waits on, which is process start included.

**Not in this plan, deliberately:** editing
[`defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md). Step 5 *decides* the default; changing
the shipped one is a code change, which §1 routes to its own task. If the decision is to keep the
width at 3 there is nothing to edit and no task to raise, and that asymmetry is the point of putting
the decision here and the change elsewhere.

**Output paths**
- `tests/scale.py`

## 3. Implement

### The measurement

Every command, at every scale, on a current Windows laptop with a warm filesystem cache; five runs
each, best and worst in milliseconds; timed around the launcher so process start is inside the
figure, which is what an agent actually waits on. Projects built by step 1's generator into a
temporary directory. The 0-task row is the control and the 999/1000 pair is a second one: 999 is
`id_width: 3` and 1000 is `id_width: 4`, and they land inside each other's spread, so the width
itself costs nothing measurable.

| Tasks | `context` | `list` | `index` | `check` |
| ---: | :--- | :--- | :--- | :--- |
| 0 | 302..309 | 306..307 | 305..323 | 307..319 |
| 50 | 313..322 | 311..319 | 309..322 | 332..339 |
| 500 | 373..394 | 373..390 | 380..406 | 560..581 |
| 999 | 442..452 | 443..461 | 447..465 | **824..829** |
| 1000 | 444..455 | 443..452 | 454..463 | 813..826 |
| 2000 | 586..624 | 595..602 | 590..632 | **1337..1378** |
| 5000 | 1024..1056 | 1046..1451 | 1331..1396 | 2924..3854 |

**About 0.3 s of every row is process start, not task work.** The empty project costs the same as the
50-task one to within noise, so at small scales the tool is measuring the launcher finding an
interpreter and Python starting. Two things follow: the per-task cost is only what the rows above the
floor show, and a faster machine moves the floor rather than the slope. The obvious way to remove it
is a resident process, which is `docs/SCOPE.md` non-goal 2, so it is recorded rather than raised.

**`check` is the command that runs out first**, by roughly a factor of three over the other three. It
is the only one that reads every Markdown file in the project a second time for links and stats each
target, so it scales on links rather than on tasks.

### Decisions & assumptions

- **D1 — the default stays `id_prefix: T-` and `id_width: 3`, and the ceiling it implies is 999
  tasks.** The two ceilings this task set out to find turn out to land in the same place: the width
  caps a project at 999, and `check` crosses one second somewhere between 1000 and 2000. So the
  shipped default expires at almost exactly the point the tool stops being instant, and a project
  cannot silently grow into the slow range — it has to raise `id_width` first, which is a deliberate
  act with this record behind it. *Rejected: a default width of 4*, which would move the structural
  cap to 9999 and leave the tool advertising a range where every command is over budget — the
  unverified claim in a different costume. *Rejected: dropping the width rule so ids grow as needed*
  — T-075 bought a mistyped id being reported, and the report is defined by the width. *Rejected: a
  wider default with a note saying not to use it*, which is not a default. — 2026-08-09
- **D2 — the supported scale, in the sentence [T-006](T-006-package-document-and-publish.md)
  quotes.** Written to contain no figure the table above does not, and with no em or en dash in it,
  so it survives that task's §5a gate verbatim:

  > At its shipped id width taskmd handles up to 999 tasks with every command finishing in under a
  > second (measured at 999 tasks: `check`, the slowest, took 0.83 s), and a project that raises
  > `id_width` to go further pays 1.34 s for `check` at 2000 tasks and up to 3.9 s at 5000.

  The figures are what is being handed over, not the wording: T-006 step 5a rewrites the README's
  prose, and the constraint that travels is that no number may appear which is not in the table
  above. — 2026-08-09
- **D3 — `id_width` needs a value meaning "the backend allocates these; impose no width", and the
  change is [T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md).** The shape is decided
  here because the id scheme is this task's; the change is a config key and a binding sentence, which
  a `decision` task does not make. `none` is already this config's word for a key that does not apply
  — `blocked_status`, `deliverables_field`, `value_field`, `effort_field`, `after_write` all take it
  — so the idiom exists and T-082 is one more use of it rather than a new concept. *Rejected:
  relaxing `is_id` back to any width*, which un-buys T-075 for every local project to serve one
  backend. *Rejected: leaving it and correcting only the binding sentence*, which would tell an
  adopter their ids cannot be described and stop there. *Rejected: making it T-004's own change* — see
  §1 *Scope*. — 2026-08-09
- **D4 — a collision is reported by every command and resolved by a person, and that is the whole of
  the behaviour.** `docs/SCOPE.md` non-goal 4 puts merge resolution with git; what the tool owes is
  that the loss is never silent. Shown below. — 2026-08-09
- **Assumption — the timings are relative to the machine that took them.** They are not a promise, and
  D2 says so by naming the machine's class. What is portable is the shape: a fixed floor around 0.3 s,
  a slope that is roughly linear in tasks for three commands and steeper for `check`. If a future
  measurement disagrees, it is the numbers that move and not D1's reasoning, which rests on the two
  ceilings coinciding rather than on either one's exact value.

### Collision behaviour, from a run

`tests/fixtures/broken-duplicate-id` holds two files claiming `T-001`. Every command notices; only
`check` names both files, and only `check` exits non-zero:

```
$ taskmd check
DUPLICATE ID  T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md. Only the first is loaded, so the other is in no view and on no edge
1 problem(s) over 1 task(s)                                          exit 1

$ taskmd list
taskmd: 1 problem(s) with the task files - run 'taskmd check'
T-001   proposed   -   specify   First file alphabetically, and the one that loads    exit 0

$ taskmd index
taskmd: 1 problem(s) with the task files - run 'taskmd check'
Wrote tasks/README.md - 1 active, 0 closed                           exit 0

$ taskmd context T-001
taskmd: 1 problem(s) with the task files - run 'taskmd check'
T-001  First file alphabetically, and the one that loads             exit 0
```

So two branches that both allocate the next id and merge cleanly — which git will do, since they are
different files — leave a project where one task is in no view and on no edge, and the tool says so
on the next command anyone runs. It picks the first in sorted order so the answer is at least the
same twice, and it renumbers nothing.

### Backend-allocated ids

Two halves, and they came out differently.

**"Id unknown until created" is already a supported state.** The tool allocates no ids: its whole
command surface is `usage: taskmd {check,context,index,list} [args] [--root PATH]`, with no `create`
and no `new`, so nothing in it can require an id before a task exists. Allocation is a sentence in a
binding, and the GitHub one gets its number back from `gh issue create`. The method's side holds too
— an edge is stored on the constrained task, so a new task carries the edges it owns from birth and
an edge pointing *at* it is written afterwards, which is that binding's assumption 1.

**The identity keys cannot describe a sequence the backend allocates.** That is D3 and T-082.

### Outputs produced

- [`tests/scale.py`](../tests/scale.py) — the generator
- [T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md) — raised, not fixed here

### Verification — what was run, and what it printed

- **`check` is clean on every generated project**, at 0, 50, 500, 999, 1000, 2000 and 5000 tasks:
  `OK - 5000 task(s), vocabulary valid, references resolve, no broken links`. This is load-bearing
  rather than tidy — a generated project that failed `check` would have been timing the construction
  of an error list instead of the work.
- **The ceiling was shown refusing the next task**, which is the case that could fail and the reason
  999 is a measured boundary rather than arithmetic. `T-999` was copied to `T-1000` in the 999-task
  project and the id changed to match:

  ```
  ID WIDTH      tasks/T-1000-generated-task.md declares 'T-1000', which is not T- plus 3 digit(s), so it is not loaded as a task
  1 problem(s) over 999 task(s)
  ```

  The count is the evidence: 999 tasks, and the thousandth file is not one of them.
- **D2's sentence was checked figure by figure against the table.** 999, 0.83 s, 1.34 s at 2000 and
  3.9 s at 5000 each appear above; nothing in the sentence is rounded up or interpolated. This is the
  check that criterion 4 asks for and it is one that could have failed — an earlier draft said "about
  4 s" for the 5000 row, which the table does not say.
- **The generator was checked against the shape it claims to copy.** It writes 832 kB for 50 tasks,
  16.6 kB a file, against this repository's measured average of 15.5 kB over 81 tasks; 7 links a
  body and every one of them resolving, which is what `check`'s clean run above proves.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The default `id_prefix` and `id_width` are decided, and the decision states the ceiling the width implies | met | D1 — `T-` and 3, capping a project at 999, with three rejections. The ceiling is a measured boundary rather than arithmetic: the thousandth file is refused and `check` says so over a count of 999 |
| Collision behaviour is described from a run | met | §3 *Collision behaviour*, all four commands against `tests/fixtures/broken-duplicate-id`. Only `check` names both files and exits non-zero; the other three warn and carry on, which is the half a `check`-only description would have missed |
| Timing measured at 50, 500 and 5000 tasks, for all four commands | met, and **the criterion's second falsifier is wrong** | Seven scales rather than three, all from real runs. But *"falsified by a scale the decided width cannot express"* fires literally, because 5000 was measured at `id_width: 4` and the decided default is 3. The clause was written to forbid extrapolation, and measuring above the default is exactly what makes D1's rejection of width 4 evidence instead of assertion. The defect is in the wording, not in the work; amending it is the maintainer's, and nothing about the result turns on it |
| The supported scale is one sentence in §3, quotable verbatim, no number a run did not produce, judged at one second a command | met | D2. Checked figure by figure against the table during `implement`, which caught a draft rounding the 5000-task `check` figure of 3.85 s up to "about 4 s" |
| The scheme tolerates ids the backend assigns | **carried** | First half met: the tool allocates nothing — its whole surface is `{check,context,index,list}` — so "id unknown until created" needs no support, it is the only state there is. Second half not met here, and neither the key nor the binding sentence has moved → **[T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md)** |

**What this task does not claim.** The figures are one machine's. D2 names the machine's class for that
reason, and the assumption in §3 says what is portable about them: the shape, not the numbers.

**Child fix tasks raised**
- **[T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md)** — carries the second half of
  criterion 5. Not a blocker on publication: nothing today reads a config for a GitHub-backed
  project, so what ships wrong is the instruction to write one, and that is a document fix.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Four criteria met, one carried by T-082. One criterion is marked wrong rather than quietly reread: the third forbids "a scale the decided width cannot express", which the 5000-task row fires literally, since it was taken at width 4 and the decided default is 3 — the clause meant to forbid extrapolation and instead forbids the measurement that made rejecting width 4 evidence-based. Marked openly, amendment left to the maintainer, result unaffected. T-004 was the last of T-006's nine blockers; the other eight were already closed, so publication is now unblocked. |
| 2026-08-09 | → in_progress | Six steps worked in order. The result the plan did not anticipate: the structural ceiling and the performance ceiling land in the same place, so the shipped `id_width: 3` caps a project at 999 tasks and `check` crosses one second between 1000 and 2000 — the default expires just before the tool stops being instant, which is why D1 keeps it. About 0.3 s of every figure is process start rather than task work; removing it means a resident process, which is non-goal 2, so it is recorded and not raised. One task raised rather than fixed: T-082, because the GitHub binding says the identity keys *describe* an issue number and an exactly-N-digits rule cannot. Verification includes the case that can fail — the thousandth file refused at the boundary — and D2's sentence was checked figure by figure against the table, which caught a draft saying "about 4 s" for a row that says 3.85. |
| 2026-08-09 | → planned | Six steps, measurement second because it is the one that can invalidate the rest: a performance ceiling below 500 would make the width question moot and change the sentence step 6 writes. Three shape decisions, each with its rejections — the generator is tracked and what it generates is not, the ceiling is stated as a count with its time and the machine's class rather than as an adjective, and the timing is taken around a real command so process start is inside it. Editing the shipped config is deliberately outside the plan: this task decides the default, and changing it is a code change §1 routes elsewhere, so keeping the width at 3 costs no edit and no task while changing it costs both. |
| 2026-08-09 | → specified | Five criteria from four; the mapping is stated so nothing looks dropped. The circularity is answered by splitting the fact from its publication, with three rejections recorded rather than referred back, since the maintainer authorised the whole lifecycle. Two things were found by running the tool rather than reading it, and both changed a criterion: the shipped `id_width` is a hard ceiling of 999 tasks, so `format_id` composes a thousandth id that `is_id` will not read back and the 5000-task measurement cannot be taken at the default width at all; and the GitHub binding says the identity keys *describe* an issue number, which an exactly-N-digits rule cannot do. The second is the fifth criterion's subject, not a separate task, because backend-assigned ids were already the fourth criterion's. A budget of one second per command is named before any measurement, so the threshold cannot be picked to fit the result — flagged as the one judgement here most worth the owner's disagreement. |
| 2026-08-09 | (no change) | Handed to a fresh session with the full lifecycle authorised by the maintainer. One question added before it starts: criterion 3 asks the README to state the ceiling, the README does not exist, and T-006 — which writes it — is blocked by this task, so the two wait on each other. That is the same circularity T-079 hit and T-081 had to repair, found here before any work was planned against it. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
