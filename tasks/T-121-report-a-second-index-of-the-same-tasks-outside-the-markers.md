---
id: T-121
title: Report a second index of the same tasks sitting outside the generated markers
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-025, T-096, T-100, T-101, T-107]
work_package: M5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-121 — Report a second index of the same tasks sitting outside the generated markers

## 1. Specify

**Where this came from.** The first adopting project's second written report, 2026-08-11 — its R-8,
and the only item in that report. Copied to `control/` beside the first one. Every earlier
recommendation from that project is closed (T-099 to T-105, plus T-106 and T-107 which they raised
indirectly), so this is the whole of the outstanding adopter feedback.

**What happened there.** The project migrated onto taskmd and kept its own pre-migration index
generator running for a while. Both wrote to the same file. The result was `tasks/README.md` holding
taskmd's generated block between taskmd's markers **and a second complete table of the same 56 task
ids outside them**.

`check` was silent. It ran twice over that state and reported `OK` both times, because it owns the
text between its own markers and reads everything else in the file as prose. The only number that
moved was a link count two screens up in the output, which nobody reads as a signal. The duplicate
was found by a person noticing the file had grown, not by any tool.

**Why it is taskmd's to report and not only theirs to avoid.** Two tools that can write one file are
invisible to *both*: neither validator can see a block it does not own, and a second generated copy
of the same facts therefore passes every check either tool runs. Nothing warns an adopter that this
is the shape of the risk, and migrating onto taskmd is exactly the moment it arises — an adopting
project has an old generator by definition. The information needed to spot it is already parsed:
`check` knows every task id, and it knows where its own markers are.

**Outcome.** `check` emits one advisory line when a file carries a table of ids taskmd already knows,
outside taskmd's markers — naming the file and the count, so the adopter can decide whether it is a
duplicate index or a legitimate quotation of their own backlog.

```
DUPLICATE INDEX  tasks/README.md: a second table of 56 known task ids sits outside the taskmd markers
```

**Scope**

- In: the advisory line, its threshold, and a fixture proving it fires and proving it stays quiet.
- Out: doing anything about the duplicate. Deleting one of the two writers is the project's call —
  in the reporting project it was the old generator, and removing it was their own task.
- Out: any change to exit status or to the problem count. See the criterion below.

**Inputs**
- `control/adopter-report-2026-08-11.md` — R-8, the source, with the evidence as they recorded it.
- The `CONFIG DRIFT` line shipped for T-100, which is the precedent this follows in every respect.

**Acceptance criteria**
- [ ] `check` prints one line per affected file, naming the file and how many known ids sit outside
      the markers.
- [ ] **It is advisory: the exit status does not move and the count of problems does not change.** A
      project may legitimately quote its own task table in a document, and a validator that failed on
      a legal state is one a project starts passing flags to — the reasoning `CONFIG DRIFT` already
      settled.
- [ ] It rests only on what `check` already parses — the known id set and its own marker positions.
      No new file format is read and no configuration key is added.
- [ ] A fixture with a duplicate block **fails to be silent**, and a fixture without one stays
      silent. A clean-tree pass proves nothing on its own.

**Open questions**
- None. Both answered by the maintainer on 2026-08-11.

  **Q1 — what counts as "a table of known ids"? — *most of the known set*.** The advisory fires when
  the known ids outside the markers are a majority of what taskmd knows. Chosen over *more than N*
  because N cannot be justified at two project sizes at once: a number that is quiet in a 500-task
  project fires on ordinary cross-linking in a 20-task one, and there is no basis for picking
  between them. A majority scales by construction and cannot be reached by a task file linking to
  its neighbours. The observed case was 56 of 56.

  **Q2 — which files are examined? — everything `check` already reads.** It costs nothing extra: the
  known id set and the marker positions are both already parsed, so the scan is over material the
  command has in hand. Narrowing to `tasks_dir` would be quieter and would miss a copy pasted into a
  document, which is the case an adopter is least likely to notice — the opposite of what the
  advisory is for.

  Neither answer changes the acceptance criteria; both were fork-free choices inside them. The
  fixture required by criterion 4 must now carry a *majority* duplicate to fire, and a file quoting a
  handful of ids is the case it must stay quiet on.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write `check_duplicate_index` exactly as Q1 and Q2 answer it — majority of the known id set, over every document `check` already reads — printed on its own prefix beside `CONFIG DRIFT` | `plugin/skills/taskmd/taskmd/cli.py` |
| 2 | Build the fixture that must **fire**: a document carrying a table of every known id outside the markers | `tests/test_cli.py` |
| 3 | Build the fixture that must stay **quiet**: a document quoting a handful of ids | `tests/test_cli.py` |
| 4 | Run the finished rule against this repository, against `tests/fixtures/alt-project`, and against a deliberately **small** project, and record where the threshold turns noisy | Measured figures in §3 |
| 5 | Confirm the exit status and the problem count do not move, by asserting both on a firing fixture | §3 — criterion 2 |
| 6 | `index`, `check`, suite | §3 |

**Step 4 is the one that can invalidate this plan, and it is deliberately placed after the rule
exists.** Q1 chose *majority* over *more than N* on the ground that a majority "cannot be reached by
a task file linking to its neighbours". That is true at 132 tasks and it is arithmetic at 6: a task
whose `related:` names four of five siblings is a majority. Task files are inside Q2's scan, and
every task file already contains its own id. So the threshold has a small-project regime the answer
did not consider, and criterion 4's *stays quiet* half is what will show it. **The rule is built as
answered and the result measured** — a recorded decision is re-opened by evidence, not by a builder
who thinks he sees further ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) is
the standing-authorization precedent, not a licence to redecide). If the measurement refutes the
threshold it goes back to the maintainer as one question with the numbers attached.

**Shape decisions.**

**D1 — Its own prefix, `DUPLICATE INDEX`, not a second `CONFIG DRIFT` line.** The two are both
advisories and they are not the same finding, and the outcome in §1 already writes the line that way.
Sharing a prefix would mean a project grepping for config drift gets index duplicates as well.

**D2 — The scan is one regex over the text outside the markers, intersected with the known id set.**
Deriving the pattern from `schema.id_prefix` and matching loosely on digits, then keeping only ids
taskmd actually knows, means the width rule stays in one place and a project with `id_width: none`
needs no special case. *Rejected: searching for each known id in turn* — the same answer at
132 × 160 string searches.

**D3 — Distinct ids, counted once per file.** A document that names `T-001` eleven times is one id,
not eleven. Counting occurrences would make a chatty prose document look like an index.

**Planned outputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_duplicate_index`, and its line in `cmd_check`
- `tests/test_cli.py` — the firing fixture and the quiet one

## 3. Implement

### Step 1, and what the first cut did

Built exactly as Q1 and Q2 answer it — a majority of the known id set, over every document `check`
already reads. Run against the two real projects:

```text
this repository        OK, silent
tests/fixtures/alt-project
  DUPLICATE INDEX  issues/ISSUE-0001-pick-a-colour.md: a second table of 3 known task ids ...
  DUPLICATE INDEX  issues/ISSUE-0002-paint-the-shed.md: a second table of 3 known task ids ...
```

**Two false positives, on this project's own shipped fixture, which has no duplicate anywhere.**
`ISSUE-0001` carries its own ref, its `epic`, and one sibling named in a sentence: three of three
known ids, which is a majority. Q1 chose *majority* over *more than N* partly because a majority
"cannot be reached by a task file linking to its neighbours". That is true at 132 tasks and it is
arithmetic at three, and the fixture is the proof rather than the worry.

### The amendment, and why it is this one

**A task file is not counted for the ids it is *entitled* to carry** — its own, and the ones in its
own edge fields. Everything else it names still counts.

This keeps every part of the maintainer's two answers. The threshold is still a majority, so it still
scales by construction and no number was invented. The scan is still everything `check` reads, so a
copy pasted into a document is still caught — Q2's reason for refusing to narrow to `tasks_dir` is
untouched, because nothing was narrowed. What changed is which ids in a task file are evidence, and
the discount is exactly the class Q1's argument had assumed away.

*Rejected: a floor as well as a majority* — "fires at a majority and at least ten" would have silenced
the fixture too, and it reintroduces the arbitrary N that Q1 refused, at two project sizes at once.
*Rejected: leaving it firing and asking first* — the rule would have shipped nothing testable, and
criterion 4's *stays quiet* half cannot be met by a rule that does not.

**This amends an answer the maintainer gave, and it is flagged as such** rather than absorbed. It is
taken under the standing delegation, on measured evidence, and the alternative is live: if the
maintainer prefers a majority with no discount, the fixture is what has to change instead.

### Step 4 — the headroom, measured on real corpora

How close does an honest document come to the threshold?

```text
this repository: 132 known ids, advisory fires at 67 distinct ids in one document
     38   28.8%   tasks/T-059-audit-the-whole-project-after-the-plugin-restructure.md
     29   22.0%   tasks/T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md
     22   16.7%   tasks/T-026-audit-the-whole-project-before-the-remaining-build.md
     20   15.2%   tests/fixtures/README.md
     18   13.6%   docs/SCOPE.md
   headroom: the loudest document is 29 ids short of firing

alt-project fixture: 3 known ids, advisory fires at 2 distinct ids in one document
      1   33.3%   issues/ISSUE-0001-pick-a-colour.md
   headroom: the loudest document is 1 id short of firing
```

The loudest documents here are audit umbrellas naming their own findings, and at 132 tasks they sit
at less than a third of the threshold. **At three tasks the margin is one id.** So the discount makes
the fixture quiet; it does not make a very small project comfortable, and a three-task project whose
one task names both siblings in prose would still fire. That residual is real, it is bounded by the
project being tiny enough to read by eye, and it is the thing to put to the maintainer rather than
engineer around.

### Steps 2, 3 and 5 — the fixtures

Seven tests, paired so that neither side is assumed:

```text
a second table of every id is reported                              fires
the reported case exactly - generated block plus a second table     fires
the discount does not blind it to a table inside a task file        fires
it is advisory: exit status and problem count do not move           fires, exit 0, "OK - ", no "problem(s)"
a document quoting a handful of ids stays quiet                     quiet
a small project of tasks linking to neighbours stays quiet          quiet
the generated block itself is not a duplicate of itself             quiet
```

*The reported case exactly* is the shape the adopting project actually had — `index` run, then a
second table appended below the end marker of the same file — because a rule for a reported defect
should be tested on the report. *A small project of tasks linking to neighbours* is the fixture case
above, locked in: it **fails on the first cut**, which is the evidence that the discount does
something.

### Step 6

```text
test_cli 108  test_list 37  test_schema 53  test_budget 5  test_runtime 27 (skipped=3)
```

`check` clean on this repository and on the fixture, with `index` run first.

**Decisions & assumptions**

- **The denominator merges into `document` rather than getting a noun of its own.** T-096 requires a
  narrower walk to be counted separately; this walk is the *same* set `check_links` reports, so a
  second noun would report a coverage that is not additional. — 2026-08-11
- **The marked region is skipped, not scanned and forgiven.** taskmd's own generated block names
  every id there is, so a rule that read it would fire on its own output in every project that has
  run `index` once. There is a test for it. — 2026-08-11
- **One regex over the text, intersected with the known set.** The width rule stays in
  `schema`, and `id_width: none` needs no special case. **D2.** — 2026-08-11

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_duplicate_index`, and its line in `cmd_check`
- `tests/test_cli.py` — `ReportsASecondIndexOutsideTheMarkers`, seven tests

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `check` prints one line per affected file, naming the file and how many known ids sit outside the markers | met | `DUPLICATE INDEX  <file>: a second table of N known task ids sits outside the taskmd markers`, one per file, on its own prefix (**D1**). |
| **It is advisory: the exit status does not move and the count of problems does not change** | met | Asserted directly: the same project checked clean and then with a duplicate returns the same exit code, `0`, prints `OK - ` and never `problem(s)`. |
| It rests only on what `check` already parses — no new file format, no configuration key | met | The known id set, the edge fields already loaded, and the two marker constants. Nothing added to the schema or the config. |
| A fixture with a duplicate block **fails to be silent**, and a fixture without one stays silent | met | Four firing and three quiet, listed in §3. One quiet test is the case that **failed on the first cut** — so the pair is genuine rather than two clean runs. |

**Child fix tasks raised**
- none. The false positives §3 records are this task's own rule mid-construction, not a separate
  defect: they were found by the plan's own step 4 and repaired before the rule existed anywhere
  outside this branch.

**Verdict.** All four criteria met. One thing leaves this task unresolved and is deliberately not
buried: the rule now discounts a task file's structural ids, which **amends the maintainer's Q1
answer** on measured evidence. It is recorded here, and it is the question that goes back.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **The Q1 amendment is confirmed by the maintainer, 2026-08-11.** The rule keeps discounting the ids a task file is entitled to carry — its own and its declared edges — with the threshold and the scan unchanged from the original answer. The rival was put with it and rejected: restoring a strict majority and editing `tests/fixtures/alt-project` so it stops firing would have silenced the specimen rather than handled the regime it exposed. So the amendment is now the answer rather than a builder's deviation from one, and §3's headroom figures are what it rests on. |
| 2026-08-11 | → done | All four criteria met, and the interesting result is that the plan's own step 4 refuted a maintainer answer before the rule left the branch. Built exactly as Q1 specified, `DUPLICATE INDEX` fired **twice on this project's shipped `alt-project` fixture**, which has three tasks and no duplicate anywhere: `ISSUE-0001` names its own ref, its epic and one sibling, which is three of three. Q1's ground for choosing a majority — that one "cannot be reached by a task file linking to its neighbours" — is true at 132 tasks and arithmetic at three. **The amendment discounts the ids a task file is entitled to carry** and keeps everything else the maintainer decided: still a majority, still every document `check` reads. Measured headroom afterwards: at 132 tasks the loudest honest document is 38 ids against a threshold of 67; at three tasks the margin is **one**, so a tiny project is quiet but not comfortable, and that residual is what goes back rather than being engineered around. Seven tests, four firing and three quiet, one of which fails on the first cut. |
| 2026-08-11 | → in_progress | Six steps. Two shape notes worth keeping: the marked region is **skipped** rather than scanned and forgiven, because taskmd's own generated block names every id there is and a rule that read it would fire on its own output everywhere; and the denominator merges into `document` rather than taking a noun of its own, since the walk is the same set `check_links` already reports and [T-096](T-096-decide-whether-a-narrower-walk-of-a-counted-class-needs-its-own-number.md)'s rule is about *narrower* walks. A floor alongside the majority was considered and rejected — it would silence the fixture and reintroduce exactly the arbitrary N that Q1 refused. |
| 2026-08-11 | → planned | Six steps, and step 4 is placed after the rule exists on purpose: the threshold has a small-project regime Q1's answer did not consider, since task files are inside Q2's scan and every task file already carries its own id. Built as answered, then measured — a recorded decision is re-opened by evidence rather than by a builder who thinks he sees further. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: M5`, through all four phases — including a task raised into M5 *by* that work, which is a M5 task and not a fresh grant. It **does not generalise** to `M6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a M5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → specified | Both open questions answered by the maintainer: a majority of the known set is the threshold, and the scan covers everything `check` already reads. No criterion amended — both were choices inside the criteria rather than forks between them. **Stays `M3` and is not started**: the standing authorization covers the current release only, and being fully specified is not a reason to reach past it. |
| 2026-08-11 | → proposed | Raised from the first adopting project's second report, delivered 2026-08-11 and carrying one item. **Checked against this repository before filing**: `DUPLICATE INDEX` appears nowhere in the tree, and no existing task covers it — so unlike two items in their first report, this one does not arrive already answered. The reporting project has already deleted its own second writer, so nothing here is holding them up; what they are asking for is that the next adopter not have to notice it by eye. |
