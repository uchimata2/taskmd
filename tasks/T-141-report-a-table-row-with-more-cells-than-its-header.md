---
id: T-141
title: Report a table row with more cells than its header
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-025, T-095, T-107, T-121, T-140]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-15
updated: 2026-08-15
deliverables:
  - plugin/skills/taskmd/taskmd/cli.py
  - tests/test_cli.py
  - README.md
---

# T-141 — Report a table row with more cells than its header

## 1. Specify

**Outcome**
A Markdown table row carrying more cells than its header is reported by `check`, or this project
records that it will not be and says what a project relying on Markdown records is meant to do
instead.

**Why this one**
Raised from the htmldeck adopter report, row `O-T4`. The reporting project hit it twice in one
document, decided against building the equivalent gate for itself, and recorded the observation
anyway on the grounds that the trade may come out differently for a tool whose whole subject is
Markdown records. It does, and for a reason the report could not have known: **this repository has
the defect too**, and the instance destroyed part of a task record.

**Measured here before being argued.** A scan on 2026-08-15 read 270 Markdown files, 558 tables and
2,769 body rows, and found exactly one row wider than its header — in
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md), where a whole `→ proposed`
log entry was absorbed into the row above it during the commit that closed the task. It had rendered
as nothing on GitHub for five days short of a week. The repair is
[T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md); this task is the class.

**The failure mode is invisible by construction, and that is the argument.** Markdown drops the
excess cell silently, so the text is in the file and absent from the page. Nothing this project runs
had anything to say about it: `check` was clean on 105 tasks, the suite was green, and the
pre-publish gate printed its count and no lines. The instrument that finds it is counting cells
against the header, and there is no second one — which is what separates this from the classes
`check` already reports, where a reader could in principle have noticed.

**Why `check` is the only tool in the neighbourhood.** It already walks every Markdown document a
clone would receive and parses their links (`check_links`), so the file set, the read and the
gitignore reasoning all exist. The addition is a counting pass over the same text, not a new walk.

**The measured false-positive rate is what makes it worth deciding rather than assuming.** Zero over
2,769 rows here, which is a very different starting point from
[T-130](T-130-report-a-question-left-live-in-a-closed-task.md)'s 1-in-24 and from the precision
[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) rejected. What the scan does not
yet know is the rate on a project that is not this one — and a row *narrower* than its header, which
Markdown pads rather than truncates, is a different question this task should decide is in or out.

**Requirements served**
R-16, and the rule behind it: a validator is worth what you believe it would catch. The belief here
is measured rather than estimated, in both directions.

**Scope**
- In: whether `check` counts a body row's cells against its header row, on the documents it already
  reads.
- In: what a short row does, since Markdown pads it and no text is lost — a different fault, possibly
  not one.
- In: the escape and code-span cases. GitHub-flavoured Markdown requires `\|` inside a table cell
  even within backticks, so an unescaped pipe in inline code splits a cell and is one of the ways a
  row grows without its author intending it.
- In: whether the class is advisory or a problem, on the precedent of
  [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) and
  [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md).
- Out: the T-099 instance, which is [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md).
- Out: any other opinion about Markdown a document could carry. This is one countable property, not a
  linter.

**Inputs**
- [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md) — the one instance and its provenance.
- The scan itself, to be re-run and recorded in §3 rather than quoted from here.
- [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) and
  [T-025](T-025-let-check-notice-a-stale-generated-index.md) — the two precedents for reporting a loss
  that produces no other signal.
- [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) — what a new counted class owes
  the itemised line.

**Acceptance criteria**
- [ ] The decision rests on a rate measured over this repository's own documents and over the shipped
      fixtures, not on an estimate
- [ ] If a class is added, it is shown **failing** on a fixture carrying the fault and staying quiet
      on every existing fixture and on this repository — a clean pass proves nothing
- [ ] The fixture is a fixture, not an example in prose: a task file demonstrating this fault would
      itself be a hit, so nothing outside `tests/fixtures/` may carry a specimen
- [ ] Whatever is decided about short rows is stated, including if the answer is that they are ignored
- [ ] If no class is added, one document says what a Markdown-native tracker does about a cell past
      the header, and `check`'s own scope statement does not imply it is covered
- [ ] Every existing fixture still reports exactly the classes it reported before

**Open questions**
- ~~**Is this a problem or an advisory?**~~ **Decided at `specify` on 2026-08-15: a problem.** Settled
  by the test [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) set
  and [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) restated — *legal states
  do not fail*. Every advisory this project prints is a state a project may mean: a config behind the
  default, a label named after a version, a second index during a migration. **A cell past the header
  is not a state anyone can mean.** The author wrote text, the renderer drops it, and no project
  intends that; it is the same kind of fact as a link that does not resolve, which is a problem.

  *Rejected: an advisory, on the adopting project's reasoning.* Their argument is good and is the
  reason this was a question — a cell past the header is not a broken pointer, and a new problem
  class can turn an adopter's passing tree red on an upgrade. What decided it against: the exit code
  is the only part of `check` a script reads, and a fault that loses text while the command reports
  success is the shape this project has twice called critical
  ([T-029](T-029-reject-unknown-arguments-on-every-command.md),
  [T-025](T-025-let-check-notice-a-stale-generated-index.md)). The upgrade cost is real and is paid
  once, by a project that has text nobody can read.

  **The measured rate is what makes it affordable**, and it is in §3: zero over 2,812 body rows here
  and 46 in the fixtures, after the one instance was repaired.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Prove the measuring instrument fires before trusting any zero it reports, on a specimen file outside the repository | The self-test transcript, §3 |
| 2 | Measure the rate on both corpora and settle the three shape questions from what the corpus says, not from the spec | §3, and D1 to D4 |
| 3 | The check and its wiring into `cmd_check`, appending to `problems` | `cli.py` |
| 4 | A fixture carrying the fault, since every existing one is silent | `tests/fixtures/wide-table-row/` |
| 5 | Tests: it fires, it is a problem, blank excess is exempt, an escaped pipe is not a cell, a fence is not a table, short rows are silent, every other fixture and this repository stay quiet | `tests/test_cli.py` |
| 6 | Document the class where an adopter meets it | the shipped default config, `README.md` |
| 7 | Prove both directions and the tree | Recorded output, §4 |

**Why step 1 comes first.** Every number this task rests on is a zero, and a zero is what a scanner
reports when it is reading nothing. The corpus cannot distinguish *no faults* from *no rows*, so the
instrument is shown firing on a fabricated specimen before its silence on the real tree is allowed to
mean anything.

**Why step 2 measures before deciding.** Three questions look like matters of taste — code spans,
short rows, blank excess — and at least one of them is settled by what this repository's own authors
had to write. Choosing first would have produced a defensible answer and missed it.

**Planned outputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_wide_rows` and its wiring
- `tests/fixtures/wide-table-row/` — the reproduction case
- `tests/test_cli.py` — the class
- `plugin/skills/taskmd/taskmd/defaults/config.md`, `README.md` — what the line means

## 3. Implement

### Step 1 — the instrument, shown firing before its zeros are believed

A specimen file was written outside this repository carrying one of each property, and scanned:

```text
1 file(s), 5 table(s), 7 body row(s)
over-wide rows      : 2      the deliberate one, and the code-span row
short rows          : 1
rows w/ code-span pipe : 1   (of which the excess is code-only: 1)
rows w/ escaped pipe   : 1
```

Five tables, not six: the pseudo-table inside a fence is not read, and the table immediately after
the fence is. The escaped-pipe row is **not** counted over-wide, which is the escape working. Only
now is a zero on the real tree worth anything.

### Step 2 — the rate, on both corpora

```text
whole tree            277 file(s), 579 table(s), 2812 body row(s)   over-wide 0   short 0
tests/fixtures only    57 file(s),  16 table(s),   46 body row(s)   over-wide 0   short 0
```

Zero and zero, after [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md) repaired the one
instance the tree had. Before that repair the same scan reported 1 in 2,797.

### The corpus settled the code-span question, and the spec did not have to

The natural implementation blanks inline code spans before counting, because `cli.py` already has
`without_code` for exactly that and every other text check uses it. **That would be wrong**, and this
repository proves it without appeal to any specification:

- `tasks/T-016-...md:96` writes a `grep` pattern inside a code span inside a table cell, with every
  pipe escaped as `\|`.
- `tasks/T-091-...md:141` writes a menu inside a code span inside a table cell, both pipes escaped.

Neither author would have escaped a pipe already protected by backticks. GitHub-flavoured Markdown
splits cells before it parses inline spans, so a pipe in a code span **is** a cell boundary and the
code span is broken too. A check that blanked code spans would be silent on a row that is doubly
wrong.

**Decisions & assumptions**

- **D1 — a problem, not an advisory** — 2026-08-15. §1's open question, with the rejected alternative
  and the adopting project's reasoning recorded there.
- **D2 — an excess cell that is entirely blank is not reported** — 2026-08-15. The rule is *text that
  renders nowhere*, and a trailing `|` with nothing after it loses nothing. This corpus has no such
  row, so it is the one false-positive class the measurement could not price; exempting it costs
  nothing and removes the likeliest first alarm an adopter meets. *Rejected: report every excess
  cell*, which is simpler and would make the first thing a new adopter sees a complaint about
  whitespace.
- **D3 — code spans are read, not blanked; only `\|` is honoured** — 2026-08-15. Argued above from
  the corpus rather than from the specification. Recorded as a decision because reaching for
  `without_code` is the obvious move and it is the wrong one here.
- **D4 — a short row is not reported** — 2026-08-15. Markdown pads it, so nothing is lost and there
  is nothing to tell anyone. Zero in 2,812 rows here in any case. The fourth acceptance criterion
  asked for this to be stated whichever way it went.
- **D5 — fenced blocks are not tables** — 2026-08-15. This project quotes taskmd's own table output
  constantly, and `index` emits a Markdown table; reading a fence would make the output the tool
  produces the output a project cannot quote. The same reasoning as
  [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md) for links.
- **D6 — it counts `table row` as its own noun** — 2026-08-15. T-096: a narrower walk does not merge
  into a wider one, and this walk reads rows where `check_links` reads documents.
- **D7 — the README documents it and the shipped default does not. Plan step 6 revised.** —
  2026-08-15. The plan named both, copying T-138, and that was wrong about which document owns what.
  The shipped config describes the **schema** and what a project may set; this rule has no key, no
  vocabulary, no threshold and touches no field, so a section there would be documentation by habit
  and a second home for a fact with one. The README carries it, where a stranger meets `check`
  before installing. Recorded as a revision rather than done quietly, per
  [T-036](T-036-say-where-a-plan-is-revised-and-that-it-is-not-an-audit.md).

### What this task found and did not fix

The README's quoted sample run was **already stale before this task touched it** — missing
`front-matter value(s)` since [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md)
on 2026-08-12. This task corrected the one line it owed and raised
[T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) for the class,
because the cause is structural: `examined()` derives that line from the checks that ran, so every
new check changes it and two of the last three did.

**Outputs produced**
- [`../plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py) — `table_cells`, `is_delimiter_row`, `check_wide_rows` and its wiring
- `tests/fixtures/wide-table-row/` — the reproduction case, two tasks and a config
- [`../tests/test_cli.py`](../tests/test_cli.py) — nine tests in a new class
- [`../README.md`](../README.md) — the `WIDE ROW` paragraph, and the sample run corrected

**Evidence — both directions**

```text
fixture       3 problem(s), exit 1, three WIDE ROW lines, all in the first task
              second task absent from the output entirely
this tree     OK - ... 2793 table row(s) ...                        exit 0, no WIDE ROW
fixtures      every other fixture with a .taskmd: silent
suite         254 passed, 3 skipped, 6 subtests passed              (245 before)
dash gate     4 file(s) covered, no lines                           exit 1, clean
```

The fixture's twelve counted rows are the fenced pseudo-table's absence made visible: four tables in
the two tasks and two in the config, and the fence contributes none.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision rests on a rate measured over this repository's documents and the shipped fixtures | met | §3 step 2: 0 in 2,812 and 0 in 46, and 1 in 2,797 before T-140. Measured **after** the instrument was shown firing, which is step 1 and is the only reason the zeros mean anything |
| Shown failing on a fixture and quiet on every existing fixture and this repository | met | Three lines and exit 1 on `wide-table-row`; silent on every other fixture with a `.taskmd`, and on this tree, both asserted in the suite rather than run by hand |
| The fixture is a fixture: no specimen outside `tests/fixtures/` | met | The reproduction rows exist in one directory. The tests assert on counts and filenames and never quote a row; this record describes the fault and quotes none. The criterion was written because writing the checker up re-creates what it catches |
| Whatever is decided about short rows is stated | met | D4 — not reported, because Markdown pads them and nothing is lost. Measured 0 in 2,812 in any case. The fixture holds one so the silence is asserted rather than assumed |
| If no class is added, one document says what a tracker does about a cell past the header | n/a | A class was added. The conditional is recorded as not reached rather than ticked |
| Every existing fixture still reports exactly the classes it reported before | met | The full suite is green, and every `broken-*` fixture's own assertion is that it produces its class and nothing else |

**Beyond the written criteria**
- **D2 and D3 were not in the criteria and are the two that decide the false-positive rate.** Blank
  excess is exempt, and code spans are read rather than blanked. The second was settled by this
  repository's own authors rather than by the specification: two of them escaped a pipe inside a code
  span inside a table cell, which nobody does unless the backticks failed to protect it.
- **The obvious implementation is wrong here.** `without_code` is what every other text check uses
  and it would have made this one silent on a row that is doubly broken. Recorded in the code, since
  the next person to touch that function will reach for it.

**Child fix tasks raised**
- [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) — the README's
  sample `check` run was already stale before this task edited it, and the cause is structural.
- Noted for [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)
  rather than raised: the README now carries a **problem**-class paragraph beside its three advisory
  ones, so that task's open framing — guard the advisories, or guard any marked list of a set the
  code owns — has one more data point than when it was written. No edit made to it; its `specify`
  reads the README as it then stands.

**Verdict.** Five criteria met, one not reached. The task closes.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → done | Five criteria met, one not reached because a class was added. **The instrument was proved before any of its zeros were believed**, which is the step that makes this record worth anything: a scan reports zero when it is reading nothing, so a specimen file carrying one of each property was scanned first and shown to fire on all five. Only then does 0 in 2,812 mean the tree is clean. **The corpus settled the question the specification would have**: two authors here escaped a pipe inside a code span inside a table cell, which nobody does unless the backticks failed to protect it, so cells are split before inline spans are parsed and `without_code` — the helper every other text check reaches for — would have made this one silent on a row that is doubly broken. Two exemptions keep the rate at zero and neither was in the criteria: blank excess, and short rows. Filed as a **problem** rather than an advisory on T-100's test, legal states do not fail: a config behind the default is a state a project may mean, and a cell that renders nowhere is not. One child raised, T-147, for a stale sample run this task found and did not cause. |
| 2026-08-15 | → in_progress | Plan taken in seven steps, and step 1 is the one that is not obvious: prove the measuring instrument before trusting a zero. Step 6 was revised during implement — D7 — because the plan copied T-138 and named the shipped default as a home for the wording. It is not one: that document describes the schema and what a project may set, and this rule has no key, no vocabulary and no field. The README carries it alone. |
| 2026-08-15 | (no change) | **Authorisation (METHOD §3.1):** the project owner asked *take T-141, full lifecycle* on 2026-08-15. It covers this task through all four phases and reaches no other — T-147, raised by it today, waits to be asked for. |
| 2026-08-15 | → specified | Open question answered: a **problem**, not an advisory, on the test T-100 set and T-138 restated. The reasoning is not that the fault is serious but that it is not a *state*: every advisory this project prints reports something a project may mean, and no project means to write a cell that does not render. The adopting project's own reasoning is recorded in §1 as the rejected alternative, because it is a good argument that lost to a specific counter rather than a weak one dismissed: the exit code is the only part of `check` a script reads, and losing text while reporting success is the shape this project has twice called critical. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T4`. The report was written as an observation the reporter expected to be marginal, and it is not marginal here: the scan it prompted found this repository carrying the same fault, and the instance had silently destroyed a log row in a closed task. `high` because the loss is invisible to every instrument this project owns and the record it damaged is the kind this project exists to keep honest. `m` rather than `s` because the decision needs a rate on more than one corpus, a fixture that cannot live in a task file, and an answer about short rows. The third criterion is unusual and load-bearing: writing this checker up re-creates what it catches, so a specimen may not be quoted anywhere a scan would read it. |
