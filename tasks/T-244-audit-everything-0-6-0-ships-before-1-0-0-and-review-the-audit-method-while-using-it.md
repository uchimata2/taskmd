---
id: T-244
title: Audit everything 1.0.0 will ship, and review the audit method while using it
type: audit
status: planned
phase: plan
parent: null
blocked_by: [T-243, T-245, T-250, T-255]
related: [T-223, T-231, T-152, T-254]
work_package: M7
owner: the project owner
business_value: critical
effort: xl
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-244 — Audit everything 1.0.0 will ship, and review the audit method while using it

## 1. Specify

**Outcome**
Everything `1.0.0` will ship has been examined, every item in scope ends in exactly one
of the three states [`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md) §2
names, and the findings are ranked and raised. Second, a recorded judgement on **the audit method
itself**, which has never been run.

**The subject is the working tree, not the `v0.6.0` tag** — the owner's instruction of 2026-08-23,
recorded in the Log. The tag was §1's original subject and the tree has moved past it in files an
install copies, so the two are different sets. The plan pins which commit the first pass reads and
says how the subject moving under the audit is handled.

**Why this one**
The owner asked for it on 2026-08-23, immediately after `v0.6.0` was published, and set the frame:

- **`0.6.0` is a beta, or a release candidate.** It is published and it is the latest release on
  GitHub, which the owner chose on 2026-08-23 over flagging it a prerelease, because that would show
  `v0.5.0` as latest and point a visitor at older software. The beta framing lives here and in the
  backlog rather than on the release page.
- **`1.0.0` follows this audit and the application of its findings**, and is carried by
  [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md), which is blocked by this record.
- **The audit machinery is under review at the same time as the subject.** This is its first run.
  [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) shipped
  `pre-release-audit.md` to every adopter on the strength of one project's practice and no execution,
  so the document is currently a claim. This record is the case that tests it.

**Two things this repository already knows about auditing itself, and neither is optional here**

- **A finding is never fixed where it is found** ([`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md)
  §5). The temptation is highest in an audit whose findings are small.
- **Coverage is a partition, and it fails** (§2 of the method). An item in none of the three states is
  a gap in the audit, not a clean item. A summary that merges denominators re-creates the blindness
  it was built to show, so each cycle reports its own.

**Scope**
- In: everything inside `plugin/`, which is exactly what an install copies
  ([T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)), graded per §1 of the
  method rather than trimmed
- In: `README.md`, the repository description, both manifests and `LICENSE`, which are what a stranger
  reads before installing. `LICENSE` is named here because the plan had to assign every item to a
  cycle and this clause's own test — *what a stranger reads before installing* — answers for it; it is
  this bullet applied, not a widening of it
- In: **a judgement on the method document itself** — which of its six rules earned their place on a
  real run, which were dead weight, and which were missing. Recorded either way, including *it worked
  as written*
- In: the §6 grading pass, run **after** the remedies exist rather than at ranking time
- Out: applying the findings. Each becomes its own record, per METHOD §5
- Out: cutting `1.0.0`. That is [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md)
- Out: this repository's own tests, backlog and instruction files, except where a finding about the
  shipped product traces back into them

**Inputs**
- [`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md) — the six rules, and
  the subject of the second half of this record
- [`audit`](../plugin/skills/taskmd/docs/method/audit.md) — the ordinary procedure the above extends
- [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) — the last audit this
  project ran, for what its findings looked like and how they were raised

**Acceptance criteria**
- [ ] The scope is graded, the aspects are named in the plan, and every item in scope ends in exactly
      one of §2's three states
- [ ] Each cycle reports its own coverage, and no cycle's denominator is merged into another's
- [ ] Every actionable finding has a severity that obliges something, and a record of its own
- [ ] The §6 grading pass has been run after the remedies exist, and names at least one prediction
      that was wrong or says honestly that none was
- [ ] The record says which of the method's six rules earned their place, which did not, and what was
      missing — including *nothing was missing*, stated plainly
- [ ] Any change the method needs is a separate task, not an edit made here

**Open questions**
- ~~**How many cycles, and which subjects?**~~ — answered in §2 on 2026-08-23: eight cycles over 32
  items, under four aspects. The subject question §1 could not settle was answered by the owner the
  same day and is recorded in the Log.

## 2. Plan

### The subject, pinned

**32 items**: the 28 files `git ls-files plugin/` returns — which is exactly what an install copies
([T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)) — plus `README.md`,
`LICENSE`, `.claude-plugin/marketplace.json` and the GitHub repository description. `plugin.json` is
inside the 28 and is not counted twice. 31 of the 32 are files and carry bytes; the repository
description is the 32nd and does not.

**The first pass reads the tree at `ca25d87`.**

### Coverage grades

Per [`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md) §1. The grade is
the brief each item is examined under, and every item carries exactly one.

| Grade | What it applies to here | Files | Bytes |
| :--- | :--- | ---: | ---: |
| **Wide** | everything an adopter reads or runs: the entry points, the landing surface, the adoption path, the three binding documents, the ten method documents, and the two small modules | 29 | 243,702 |
| **Narrow** | *no members.* Nothing in this subject is settled record — an install copies only what is current, so the grade that exists for closed and superseded material has nothing to apply to here | 0 | 0 |
| **Instrument only** | `cli.py` and `schema.py`, examined by being run against cases they are supposed to catch | 2 | 135,277 |
| | **read (Wide + Narrow)** | **29** | **243,702** |
| | **the subject** | **31** | **378,979** |

**The empty Narrow row is stated rather than omitted.** A grade with no members is a fact about the
subject — that this project ships nothing settled — and dropping the row would leave a reader unable
to tell that from an oversight.

**These figures are a dated snapshot for sizing sessions, taken 2026-08-23 at `ca25d87`, and they
decay.** The subject total is re-derived by one command and the cell is never the thing to cite:

```
git ls-files plugin/ README.md LICENSE .claude-plugin/marketplace.json | xargs wc -c | tail -1
```

**The per-cycle figures below cannot be re-derived that way, and no cycle runs until they can.** They
were computed once, by hand, from a membership list that lives nowhere in the repository — so a file
added to `plugin/` after today belongs to no cycle and nothing says so.
[T-255](T-255-derive-the-audit-cycle-membership-instead-of-typing-it.md) is the generator that fixes
it, and it is a **`blocked_by` on this record**, on the owner's instruction of 2026-08-23. htmldeck's
`PR-06` is the evidence that a hand-typed count fails: two tables that could not reconcile, four files
unread, and it looked like one. **Gating rather than warning is what stops this run repeating it** — a
caution printed beside a table is read once, by whoever wrote it.

### The finding threshold, stated before looking

A finding is one of these five, and nothing else:

1. **A claim about the product that the product refutes** — a count, a command, an exit code, a file
   list or a described behaviour that running it contradicts.
2. **An instruction an adopter cannot follow as written**, from a fresh clone, on a supported
   platform, with only what the document names.
3. **Two shipped statements that contradict each other**, where an adopter has no way to tell which
   is true.
4. **A breach of one of the five publishing constraints** ([`docs/SCOPE.md`](../docs/SCOPE.md) §5) —
   personal, client or machine data; a failure out of the box; a non-stdlib dependency; a platform
   assumption; or unhumanized text where a stranger reads it before installing.
5. **A pointer that does not resolve** for someone holding only what an install copies.

**Not findings**: taste, length, wording preference, and disagreement with a rule. The last has its
own route — [`rationale`](../plugin/skills/taskmd/docs/method/rationale.md) — and admitting it here
would turn the audit into a rewrite.

### The four aspects

Every cycle sits under exactly one, so no two cycles examine the same thing under different names.

| | Aspect | The question it asks | Cycles |
| :-- | :--- | :--- | :--- |
| **A** | It runs | Does the product do what it says when executed, from a fresh clone, on both this machine's shells? | 1, 7 |
| **B** | It is true about itself | Does every claim a shipped file makes about the product's own behaviour survive being run? | 2, 8 |
| **C** | A stranger can follow it | Can the path from landing page to a first working task be walked with only what is shipped? | 3 |
| **D** | It agrees with itself | Do any two shipped statements contradict, and does every pointer resolve? | 4, 5, 6 |

### The cycle program

**Eight examining cycles in five stages, then four synthesis steps.** Ordered by expected finding
density and by what would invalidate the rest, never by how the files are filed. **A cycle is a
session boundary**: it may be run alone, and it ends with its ledger rows written and committed.
Each row's Items figure is that cycle's own denominator and is never merged into another's.

| # | Subject | Asp | Files | Bytes | Items | Brief | Status |
| :-- | :--- | :-: | ---: | ---: | ---: | :--- | :--- |
| | *Stage 1 — does it start at all.* First because an out-of-the-box failure is High and changes what every later cycle is examining. It is also the only stage no amount of reading can answer. | | | | | | |
| 1 | The entry points | A | 6 | 8,487 | 6 | `bin/taskmd`, `bin/taskmd.cmd`, `taskmd.sh`, `taskmd.ps1`, `taskmd/__main__.py`, `taskmd/__init__.py`, run from a fresh clone on Git Bash and PowerShell 7 before anything is read. Exit codes captured to a file, never through a pipe or after `&&`. | pending |
| | *Stage 2 — what a stranger meets, and the path they walk.* Highest audience cost: the method's §4 makes a one-character error in the first instruction a newcomer follows a High. | | | | | | |
| 2 | The landing surface | B | 4 | 23,514 | 5 | `README.md`, `LICENSE`, `.claude-plugin/marketplace.json`, `plugin/.claude-plugin/plugin.json`, and the GitHub repository description. Every self-claim executed rather than read — [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md) was one such count and there is no reason to think it was the only one. The two manifests agree with each other. | pending |
| 3 | The adoption path | C | 4 | 42,047 | 4 | `SKILL.md`, `adopt.md`, `docs/HANDOFF.md`, `taskmd/defaults/config.md`, walked as one sequence by a reader holding only what an install copies. The output names where the walk first stopped resolving, or states that it did not. | pending |
| | *Stage 3 — the shipped guidance, densest first.* 149,693 bytes, 61% of the reading. Cycle 4 leads it: two of its three documents were rewritten by [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) after the tag. | | | | | | |
| 4 | The binding documents | D | 3 | 94,850 | 3 | `docs/BINDING.md`, `docs/bindings/github-issues.md`, `docs/bindings/local-markdown.md`. The heaviest readable cycle in the run. | pending |
| 5 | The method spine and its phases | D | 5 | 34,737 | 5 | `docs/METHOD.md`, `method/specify.md`, `method/plan.md`, `method/implement.md`, `method/review.md`, against each other and against §7's load-on-demand table. | pending |
| 6 | The method's supporting documents | D | 4 | 20,106 | 4 | `method/audit.md`, `method/rationale.md`, `method/uninvolved-reader.md`, `method/where-facts-live.md`. A rule stated twice and differing. | pending |
| | *Stage 4 — the engine.* Placed after the documents because cycle 1 already proved it starts, so nothing here can invalidate a document cycle — only contradict one, which is the finding. | | | | | | |
| 7 | `cli.py`, `schema.py`, and the two small modules | A | 4 | 143,867 | 4 | **Instrument only** for `cli.py` (93 KB) and `schema.py` (42 KB): run against cases they are supposed to catch, and a validator is proven only by being made to **fail**. `classes.py` and `discovery.py` are 8.6 KB and are read. [T-254](T-254-sweep-for-history-prose-living-outside-markdown.md) is already raised against a docstring here — record it examined and carried, do not raise it again. | pending |
| | *Stage 5 — the instrument on trial.* Last of the examining cycles because it can only be judged against a run that has happened. | | | | | | |
| 8 | `method/pre-release-audit.md` | B | 1 | 11,371 | 1 | Read against what this run actually did, under the same threshold as any other shipped document. Its own six rules are judged separately, in step 11. | pending |
| | **Examining total** | | **31** | **378,979** | **32** | | |
| | *Stage 6 — synthesis.* No items of their own; they consume what the cycles produced. | | | | | | |
| 9 | Re-examine what the remedies changed | — | — | — | — | Every cycle whose subject a remedy touched, plus the densest cycle a second time. **This is where an audit's own damage shows.** | pending |
| 10 | Triage, rank, raise | — | — | — | — | A severity per the method's §4 table and the record it obliges. High and Medium get a child task; Low is batched or accepted with a reason and a date. | pending |
| 11 | Judge the six rules | — | — | — | — | Which earned their place on this run, which were dead weight, which were missing — including *nothing was missing*, said plainly. Any change the method needs is a separate task. | pending |
| 12 | Grade the ranking | — | — | — | — | Predicted against actual, per finding. It must name a prediction the measurement refused, or say how it was checked that none did. | pending |

**6 + 4 + 4 + 3 + 5 + 4 + 4 + 1 = 31 files, and 32 items with the repository description.** The sum
is written out because a partition that does not sum is the failure this record's own criteria name,
and a double-counted member is invisible in a total. Verified per item on 2026-08-23 by diffing the
assignment against `git ls-files plugin/` in both directions — neither direction returned a row.

**Every finding carries the command that proves it.** That is [`../CLAUDE.md`](../CLAUDE.md)
*Verifying* applied to this run rather than a new criterion, and it is written here because a cycle's
output is the plan's to name: a finding stated without the command that produced it is a reading, and
readings are what the threshold above exists to exclude.

### How to run one cycle in a fresh session

1. Read [`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md), this section,
   and §3's register.
2. Ask [T-255](T-255-derive-the-audit-cycle-membership-instead-of-typing-it.md)'s command for the
   cycle's file list. **It reports the whole partition's verdict before it answers**, so a tracked
   path that has fallen outside every cycle stops the reading rather than surviving it. Read what it
   names, not the Brief above — the Brief is prose and the command is the membership.
3. Examine under the cycle's grade. Append a register row per finding, and one coverage row per item
   — including *examined, clean*, with what was checked.
4. Set the cycle's Status above, commit, stop. **Never leave a cycle half-read and unwritten.**

### Decisions

**The subject is what `1.0.0` will ship, and the first pass is pinned to `ca25d87`.** The owner
settled the first half on 2026-08-23; the pin is this plan's. Without it the denominator moves under
the audit and no cycle's coverage means anything, because an item added at cycle 7 was never in
cycle 2's 5. Step 9 is what handles the movement, per the method's §3 rules on re-examining a changed
subject. *Rejected: audit the `v0.6.0` tag*, which is a fixed set and therefore easier to count — and
which audits software that `1.0.0` will not ship, while
[T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md) gates on this record.

**Cycle 1 runs before anything is read, and that ordering is this plan's other real choice.** An
out-of-the-box failure is a High finding that changes what every later cycle is examining, and
plan's sequencing rule puts what could invalidate the rest at the front. It is also the only cycle
whose result cannot be obtained by reading, so leaving it late is how it gets skipped.
*Rejected: read the documents first and execute last*, which reaches the same findings and discovers
the expensive one after seven cycles have been written against an assumption.

**`cli.py` and `schema.py` are graded instrument only, and the plan says so rather than quietly
skipping them.** 135 KB cannot be read and still judged inside one session — the limit the method
names is attention, not volume. *Rejected: read them across three cycles*, which produces three
denominators over one artifact and a reader who cannot say whether the file was covered.

**Findings stay in the umbrella unless there are more than 20** — proposed by the session and
accepted by the owner, 2026-08-23. Below that line §3 is still a task record; above it the lifecycle
sections disappear under the ledger and the method's umbrella exception applies. The line is stated
now because deciding it after seeing the count is deciding it to suit the count. *Rejected: separate
finding records from the start*, which is the method's scale exception adopted before the scale
exists — htmldeck moved its register out because it holds 56 findings, and this subject is a
twenty-third of that tree.

**Eight cycles, not fewer** — proposed by the session and accepted by the owner, 2026-08-23, against a
measurement that argued the other way. htmldeck sizes a cycle at about 300 KB of source; this whole
subject is 378,979 bytes, so **all eight of these cycles fit inside one of that project's**, and on
volume alone this is one or two cycles. Three reasons the yardstick does not transfer:

- **The grade mix is not comparable.** Nearly half of htmldeck's byte mass is Grade-B closed record,
  read against one question and read fast. This subject has **no Narrow members at all** — 243,702 of
  its bytes are Wide, examined against the full threshold.
- **A cycle is a session boundary, and boundaries are the point.** Eight give eight places to stop
  with the ledger written; two give one, and the method's own rule is that a cycle ends with its
  record written including one that ran out of time half way.
- **Merging collapses the aspects.** Cycles 4, 5 and 6 are one stage but three lenses would become
  one, and the method asks for a set no cycle shares.

*Rejected: fold cycles 1, 6 and 8 into their neighbours*, which are the three under 21 KB and the
strongest case for merging. Refused because cycle 1 must run before anything is read and cycle 8
cannot run until everything else has — their size is not what places them, so folding them by size
would break the ordering that justifies the program.

**[T-254](T-254-sweep-for-history-prose-living-outside-markdown.md) is already raised and cycle 7 must
not raise it again.** It is history prose in a shipped `.py` docstring, which is inside this audit's
subject. Cycle 7 records it as examined and already carried, pointing at that record. Made a `related`
edge rather than a sentence, because a sentence is invisible to every view.

**Findings get the id space `TM-nn`, reserved now and never reused.** The method requires a stable
identifier only once findings leave the umbrella, but a child task raised at step 10 and the grading
pass at step 12 have to name the same thing, and an id invented at the moment findings move is an id
that has to be retro-fitted to everything already raised. `TM-` rather than `PR-`, which reads as
*pull request* in a repository published to GitHub. *Rejected: number findings only if they move out
of the umbrella*, which is the method read literally and costs a renumber exactly when the record is
at its largest.

**The display of this plan is taken from htmldeck's `T-219`, 2026-08-23** — named without a link,
because a path into a sibling clone resolves on the machine that wrote it and 404s for every other
reader. `check` refuses it, which is the gate working. What was borrowed: the
grade table with its totals row, the stage separators carrying why a stage sits where it does, the
per-cycle Files, Bytes and Status columns, and the *how to run one cycle* steps. That run is 12
cycles into the same method and is the only execution of it anywhere, so its shape is evidence rather
than preference. **What was not taken: its stages as aspects.** Stages order the work; the four
aspects above are lenses, and the method asks for the second. *Rejected: keep the items-only table*,
which cannot answer how long a cycle will take and gave no way to see that stage 3 is 61% of the
reading.

### Outputs

- `tasks/T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md` §3 — the coverage ledger, 32 rows, and the findings with their severities
- `tasks/T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md` §4 — the judgement on the method's six rules, and the §6 grading pass
- child task records under `tasks/`, one per actionable finding with Low batched into one — paths not knowable until the findings exist

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Findings raised**

Counts only. The statements live in the register below, and nothing restates them.

| Severity | Raised | Tasked | Accepted | Open |
| :--- | ---: | ---: | ---: | ---: |
| High | 0 | 0 | 0 | 0 |
| Medium | 0 | 0 | 0 | 0 |
| Low | 0 | 0 | 0 | 0 |

**Register — `TM-nn`**

One row per finding, id never reused and never renumbered. It moves to a document of its own if the
count passes 20, per §2's decision; below that line this is the register.

| Id | Cycle | Severity | Finding | Command that proves it | Task | Status |
| :-- | :-: | :--- | :--- | :--- | :--- | :--- |
| | | | *no findings yet — the run has not started* | | | |

**Coverage ledger**

One row per item, 32 rows when the run is complete. Every row ends in exactly one of §2's three
states: a finding, examined-and-clean with what was checked, or not examined with the reason. **An
item in none of the three is a gap in the audit, not a clean item.**

| Cycle | Item | State | What was checked, or why not |
| :-: | :--- | :--- | :--- |
| | | | *empty — the run has not started* |

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **Blocked by [T-255](T-255-derive-the-audit-cycle-membership-instead-of-typing-it.md), on the owner's instruction of 2026-08-23.** The session had recommended only that the generator *should probably* land first and left it a soft link; the owner made it a gate, so no cycle now runs against a membership no command has verified. **`status` stays `planned` and is deliberately not set to `blocked`** — `list` already derives that column from the graph and prints it for this record, so writing the value would be the same fact in two homes, which is the one design rule. `check` guards only the opposite error, a `blocked` status with no edge behind it. **Three statements the edge falsified were corrected, not left standing:** §2 no longer says the defect is shipped knowingly, *how to run one cycle* step 2 no longer describes a manual check that will never run, and T-255's own criterion and Log row were updated. Its `related` edge back to here was dropped as duplication of the dependency. |
| 2026-08-23 | (no change) | **The plan was compared against htmldeck's `T-219` on the owner's instruction, and the better of the two shapes taken.** That project is 12 cycles into the first and only execution of this method anywhere, so its display is evidence rather than preference. **Adopted:** the coverage-grade table with a totals row, stage separators that argue their own placement, per-cycle Files, Bytes and Status columns, a reserved `TM-nn` register id space, the Severity × Raised/Tasked/Accepted/Open summary, *how to run one cycle in a fresh session*, and the requirement that every finding carry the command that proves it. **Not adopted:** its stages in place of aspects — stages order work, aspects are lenses, and the method asks for the second. **What the comparison returned that was not a preference:** its Files and Bytes are printed by a command that fails when a tracked path belongs to no cycle, and this plan's are typed. Raised as [T-255](T-255-derive-the-audit-cycle-membership-instead-of-typing-it.md) rather than fixed here. **Two decisions the owner then accepted, both recorded in §2 with what was rejected:** eight cycles rather than fewer, and the register stays in the umbrella below 20 findings. |
| 2026-08-23 | proposed → planned | **The owner settled the subject and the record was planned.** The instruction, 2026-08-23: *"audit what 1.0.0 will ship, not the tag"* — which answers the question the row below flagged as the plan's, and it is recorded here because it changed §1 rather than only §2. **What moved in §1:** the Outcome and the title now name `1.0.0` instead of `v0.6.0`, and `LICENSE` is named in the Scope's stranger-reads clause, which is that clause applied rather than widened. **What the plan added:** the subject pinned at `ca25d87` and re-derived rather than copied, a finding threshold of five items stated before looking, four aspects, and eight examining cycles over **32 items** whose per-cycle counts sum to the pinned total. **The filename still says `0-6-0` and was deliberately not changed** — 13 references across 9 files point at it, three of them archived handoffs, which are records and are not edited. The id is what resolves. |
| 2026-08-23 | (no change) | **The owner is beginning this record in the next session**, stated 2026-08-23: *"isn't this the right moment to start the T-244 (audit)? … let me start the new session with that."* Recorded here because the standing rule is that a session starts no audit, so **this is the owner beginning it and not a session deciding to** — and a pointer in a handoff is context rather than authorisation. **What this row is:** the owner opening the record. **What it is not:** a grant of phases. No lifecycle beyond what that session asks for is authorised by it, and anything wider belongs in a row of its own. **All three `blocked_by` are closed** — T-243, T-245 and T-250 — so nothing mechanical holds it. |
| 2026-08-23 | (no change) | **The subject moved after this record was written, and the plan has to settle it before grading anything.** §1 scopes the audit to *everything an adopter receives at `v0.6.0`*, and the working tree is now **27 commits ahead of that tag**, four of them in files an install copies: `README.md`, `docs/BINDING.md`, `docs/bindings/github-issues.md` and `docs/method/uninvolved-reader.md` — the first from [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md), the rest from [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md). So *audit the tag* and *audit what `1.0.0` will ship* are now different sets, and this record's purpose — gating [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md) — argues for the second while its §1 says the first. Not decided here: it is the plan's, and it changes what every coverage denominator counts. |
| 2026-08-23 | (no change) | **Ordered behind [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md)** on the owner's instruction, 2026-08-23. T-250 rewrites three shipped binding documents, which are inside `plugin/` and therefore inside this record's subject. Auditing text already scheduled to change costs a child task per finding that T-250 would have removed anyway, and METHOD §5 forbids fixing them here. The edge is the ordering; nothing is written down to keep in step. |
| 2026-08-23 | (no change) | **Blocked by [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md) and [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md), on the owner's instruction of 2026-08-23 that both land before the audit.** **Recorded as edges rather than as a sentence**, which is this project's own lesson twice over: the ordering that put the release before its note lived in prose and was invisible to every view until somebody ran the rule. Both change something this record would audit — §7's release-note rule and the task template — so auditing first would judge a shape about to change and re-find what is already known. **This is a sequencing edge, not a scope change**: §1 is untouched, and the record is still `proposed` for the owner to start. |
| 2026-08-23 | → proposed | **Raised on the owner's instruction of 2026-08-23**, given as a survey answer minutes after `v0.6.0` was published: raise the task, do not start it. The standing rule that a session starts no audit is unchanged, and this record is deliberately left at `proposed` for the owner to start. **Three things came with the instruction and are recorded in §1 rather than here**: `0.6.0` is to be read as a beta, `1.0.0` follows the audit and its fixes, and **the audit feature itself is under review** because it has never been run. The last is the reason this is not an ordinary audit umbrella: [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) shipped the method to every adopter without it having been executed once, so the subject and the instrument are both on trial. **The owner also chose not to flag the published release as a prerelease** on the same exchange, because GitHub would then show `v0.5.0` as latest and point a visitor at older software. |
