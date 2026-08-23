---
id: T-171
title: Test whether the InstructionsLoaded hook can see a path-scoped rule
type: research
status: done
phase: review
parent: T-169
blocked_by: []
related: [T-155]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-17
updated: 2026-08-18
adopter_visible: no
deliverables: []
---

# T-171 — Test whether the `InstructionsLoaded` hook can see a path-scoped rule

## 1. Specify

**Outcome**
An observation of whether the `InstructionsLoaded` hook writes a log line when a `.claude/rules/` file
is delivered — and, on the strength of it, either confirmation or correction of one sentence in
[T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) §3.

**Why this one**
T-169 closed naming `load_reason` as what would report the compaction case later. That is true of
**instruction files** and was asserted of **rules** without a reader. The rules directory has been
empty for the whole time the hook has been live, so **no rule delivery has ever had the chance to
appear in that log**. If the hook cannot see rules, T-169's line promises an annotation that can never
arrive — a premise inside a closed record, which is the way this project has watched claims expire
before.

It is raised as its own task rather than fixed inside T-169: the decision there stands either way,
because it assumed the worse branch. What is at stake is the accuracy of one sentence, not the ruling.

**Scope**
- In: writing one rule, reading `CLAUDE.md`, and reading the log
- In: correcting T-169 §3 if the observation says to
- Out: the compaction observation itself. Nobody can force a compaction; that is T-169's accepted risk
- Out: moving anything in `CLAUDE.md`. This task tests an instrument
- Out: any judgement on whether the rule mechanism should be used. T-169 declined that and is closed

**Inputs**
- [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) §3 — the
  sentence under test, and the decision that does not depend on it
- [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3 — the rule format
  that fired, `paths:` with one entry, and the **shape** of a delivery: a separate block appended to
  the read's result, naming the file it came from
- `~/.claude/instructions-loaded.log` — the instrument, and `~/.claude/settings.json`, which the
  maintainer confirmed on 2026-08-17 stays as it is

**The reading is fixed before the observation, because the observation can otherwise choose it.**
Two observables, and the pair is what discriminates — either alone does not.

| Delivered? (a block appended to the read) | Logged? (a new line naming the rule) | What it means |
| :--- | :--- | :--- |
| **yes** | **yes** | The hook sees rule loads. T-169 §3's sentence stands as written |
| **yes** | **no** | **Definitive negative.** The rule arrived and the hook did not report it, so T-169 §3 is wrong and is corrected here |
| **no** | either | **Inconclusive.** A rule written mid-session may simply not be delivered — precedent says a session does not see its own instruction-file change — so there was nothing for the hook to report. The log's silence says nothing, and a restart is needed |

**Contamination, and why the marker is not the observable.** Writing the rule puts its marker string in
this session's context by construction, so *the marker being in context* proves nothing. What T-155
observed, and what this task reads, is the **delivery shape**: a separate block appended to the read's
result, naming its source file. That cannot be produced by having written the file.

**Acceptance criteria**
- [ ] The three-way reading above is written **before** the observation, and the result is reported
      into it rather than argued about afterwards
- [ ] The log's line count is recorded before and after, with the command that produced each
- [ ] Whether the rule was delivered is recorded as an **observation of the delivery shape**, never
      inferred from the marker being in context
- [ ] Whichever cell is hit, T-169 §3's sentence is confirmed or corrected — and if corrected, the
      correction is made in this task, not left as advice
- [ ] If the cell is inconclusive, the rule stays in place and what the next session must do is written
      down
- [ ] The rule carries a marker and **no real content** — T-155's rule, re-applied
- [ ] Whatever is left machine-local at the end is said to be, since `.claude/*` reaches no clone

**Open questions**
- none. The maintainer asked for this test on 2026-08-17 and the reading is fixed above

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Fix the three-way reading, before touching anything | The table in §1 |
| 2 | Snapshot the log's line count | The figure below |
| 3 | Write one rule under `.claude/rules/`, `paths:` matching `CLAUDE.md`, carrying a marker and nothing else | The probe |
| 4 | Read `CLAUDE.md`. Record whether a delivery block arrived — the shape, not the string | Observation 1 |
| 5 | Re-read the log and diff the count | Observation 2 |
| 6 | Report into the table's cell; confirm or correct T-169 §3 | The finding |
| 7 | Decide the probe's fate, and say what stays machine-local | The closing note |

## 3. Implement

### First run — 2026-08-17, the session that wrote the probe

**The cell is row 3 — inconclusive — and the run was still worth making**, because
what stopped it is itself an observation nobody had made.

**Step 2, the baseline.** Taken immediately before writing the probe, and the *content* check is the
instrument rather than the count, for the reason recorded on
[T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md): this log
is noisy with other sessions.

```
BASELINE lines=22
rule-path lines so far: 0
```

**Step 3, the probe.** `.claude/rules/t-171-probe.md`, front matter `paths:` with one entry,
`CLAUDE.md`, body one marker sentence — `T171-PROBE-4B8E1D` — and no rule of any kind. T-155's format,
re-applied unchanged, because a second variable would make a null result unreadable.

**Step 4, observation 1 — not delivered, on either kind of read.**

| Read of `CLAUDE.md` | Delivery block appended? |
| :--- | :--- |
| partial (first 5 lines) | **no** |
| whole file | **no** |

The second read exists only to kill a confound: a null on a partial read has two explanations —
rules are fixed at session start, or the trigger needs a whole-file read — and one command removes
the second. Neither read produced the shape T-155 recorded: a separate block appended to the read's
result, naming its source file. **The marker being in this session's context is not evidence and was
not used**; it is there because this session wrote the file.

**Step 5, observation 2 — no rule line, and the one new line is somebody else.**

```
AFTER-FULL-READ lines=23
lines naming a rule: 0
lines naming THIS session 81338b48: 1
```

The log gained exactly one line during the test. It is session `30b32b93` starting in a different
working directory at 23:43 — an unrelated session, not this read. Had the count been the instrument,
that line would have read as a positive.

**The finding, reported into the table's cell.** Row 3: **delivered no, logged either → inconclusive.**
The hook's silence says nothing about whether it can see rules, because nothing was delivered for it
to report. **T-169 §3's sentence is therefore neither confirmed nor corrected**, and that is the one
thing this task was raised to do.

**What was learned instead, and it is not a consolation prize.** A rule written mid-session is **not
delivered to that session**, on a partial or a whole-file read of the file its `paths:` glob matches.
T-155 arranged its test around the assumption that this would be so and never tested it — its two
sessions were built to avoid the question. So `.claude/rules/` now sits observed, not assumed, in the
same class as instruction files and skills: **fixed at session start**. That is the wall this
repository has now hit four times, and it is the reason this test needs a restart like every one
before it.

**Decisions & assumptions**
- **The probe stays in place** — 2026-08-17. Deleting it would leave the next session with the same
  two-session setup cost T-155 paid, for a test that is now one read and one `Select-String`. It is
  machine-local: `.claude/*` is excluded, so `git status` never shows it and no clone receives it.
- **`review` does not run and the task stays at `implement`** — 2026-08-17. Three criteria judge an
  observation nobody has made yet. Phase and status are independent (METHOD §2): this task is
  waiting, and waiting is not a phase.
- **Criterion 4 is written slightly wrong, and it is recorded rather than reinterpreted** —
  2026-08-17. It says the sentence is confirmed or corrected *whichever cell is hit*, which assumes
  every cell resolves it; row 3 does not. Criterion 5 is the branch that actually covers this
  outcome. Rewriting 4 now would let the result choose its own criterion, so it stands as written and
  will be marked unmet at `review`.

**What the next session does.** One read and one command, in this order:

1. Read `CLAUDE.md`. **Note whether a block arrives appended to the read's result** naming
   `.claude/rules/t-171-probe.md` — that is observation 1, and it must be answered before step 2.
2. `Select-String` the user-scope `instructions-loaded.log` for `rules`. A line naming the probe is
   observation 2.
3. Report into §1's table. **Delivered yes + logged no is the definitive negative** and the case where
   T-169 §3 is corrected here.
4. Then delete the probe, and say so.

### Second run — 2026-08-17, 23:51, a later session

**The cell is row 1: delivered yes, logged yes.** The probe survived from the first run, so this run
cost one read and one `Select-String`, which is what leaving it in place bought.

**The order was kept, and it is the reason the observation counts.** `CLAUDE.md` was read **before
this session opened any task record**, including this one. A session that reads the record first can
no longer distinguish what the harness delivered from what it went and fetched.

**Observation 1 — delivered.** A separate block arrived appended to the `Read` result, naming
`C:\…\taskmd\.claude\rules\t-171-probe.md` and carrying its body. That is the shape
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3 recorded, and it is
the observable — not the marker string, which the first run had already put in context by writing the
file, and which this run did not use.

**Observation 2 — logged.** One line, written at the read:

```
2026-08-17T23:51:04 … "session_id":"36398769-…","prompt_id":"3bb59fd9-…",
"hook_event_name":"InstructionsLoaded",
"file_path":"…\.claude\rules\t-171-probe.md","memory_type":"Project",
"load_reason":"path_glob_match","globs":["CLAUDE.md"],
"trigger_file_path":"…\taskmd\CLAUDE.md"
```

**The finding, reported into the table's cell.** Row 1: **the hook sees rule loads, and
[T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) §3's
sentence stands as written.** It is **confirmed, not corrected** — `load_reason` does carry a value
other than `session_start`, so the compaction annotation T-169 deferred to it has a working reporter
rather than a hoped-for one. What is *not* shown is a compaction; this load is a `path_glob_match`.
T-169 §3 promised a field that could report, and that is the claim under test.

**Three things came out of it that the ask did not cover.**

1. **The payload is wider than T-169 enumerated.** Its §1 lists seven fields; a rule delivery adds
   **`prompt_id`, `globs`, and `trigger_file_path`**. The last is what makes a rule line self-identifying
   — it names the file whose read triggered it — so this line cannot be confused with another session's.
2. **The read of `CLAUDE.md` itself produced no line.** Only the rule it triggered did. So the two
   readings T-169's second open question kept apart are now separable: the hook does not fire on
   reading an instruction file *as a file*, and it does fire on the rule that read pulls in. T-169
   recorded that nothing there had ever made a `Read` due to produce a line; now something has, and it
   still produces none for the file read.
3. **The instrument was lossy again, in this very run.** This session started three instruction loads
   and the log holds **two** lines naming it — its project-`CLAUDE.md` record is the truncated
   fragment `"}` on line 31. Exactly the concurrency behaviour T-169 recorded, re-observed rather than
   assumed, and the reason the content check and not the count is the instrument.

**The counts, and an honest gap in how they were taken.** Criterion 2 asks for the line count before
and after with the command that produced each. This run has **32 before and 33 after**, but they were
**derived from the file's own line numbering afterwards, not snapshotted either side**:

```
TOTAL lines=33                                  # (Get-Content $log).Count
rule line is line number 33 of the file         # Select-String … -Pattern 'rules'
lines before it: 32
"load_reason":"path_glob_match"
```

No before-snapshot was taken, because the handoff's ordering put the read first and a snapshot
command would have been a task-adjacent step between the two. It costs nothing here: the line carries
this session's `session_id`, a `prompt_id`, and a `trigger_file_path` naming the file read, so it
identifies itself without reference to a count. Recorded as it happened rather than reconstructed into
a tidier shape — the count was corroboration in this run, never the instrument.

**Decisions & assumptions**
- **The probe is deleted** — 2026-08-17, step 4 of the first run's own instruction, which this run
  carried out. The task has its answer, so the instrument has no further job. It was machine-local
  throughout: `.claude/*` is excluded, `git status` never showed it, and no clone ever received it.
  The recipe survives in T-155 §3 and in this record, so rebuilding it is two lines.
- **Criterion 4's recorded defect stands as a judgement about row 3, and is not the branch taken** —
  2026-08-17. The first run recorded that criterion 4 assumes every cell resolves T-169's sentence,
  which row 3 does not, and predicted it would be marked unmet. Row 1 was hit, and row 1 *does*
  resolve it. The earlier note is left exactly as written: it was right about the cell it was facing,
  and rewriting it now would let this run's result choose its own criterion — the thing that note
  existed to prevent.
- **`review` is not run in this request.** The observation the three criteria were waiting for now
  exists, so review is runnable for the first time; one phase per request means it is a separate ask
  (METHOD §3.1, `CLAUDE.md`). The task stays at `implement`.

**Outputs produced**
- The four observations across the two runs, and the finding above. `.claude/rules/t-171-probe.md` was
  the instrument, machine-local, and is **deleted** as of the second run. Not a deliverable.
- One annotation on [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md),
  whose §1 said no record read anything but `session_start`. One now does.

## 4. Review

Run 2026-08-18, against the seven criteria as `specify` wrote them. **The date rolled between the
observation and this verdict** — the second run's log line reads 2026-08-17T23:51 and this review was
written twelve minutes later on the 18th. Recorded because a reader comparing the two dates would
otherwise infer a gap that did not happen.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The three-way reading is written **before** the observation, and the result reported into it rather than argued afterwards | met | Proven rather than asserted for the run that mattered: `git show 3e89743:tasks/T-171-…md` — the commit closing the *first* run — already contains the table, row 2's "**Definitive negative**" wording included. The second run therefore reported into a table it could not have written. For the first run the table and the run share one commit, so git cannot separate them there; the record's claim stands on its own account for that run and on evidence for this one |
| The log's line count is recorded before and after, with the command that produced each | met | **The contestable tick, and the note is longer than the others because of it.** Second run: **32 before, 33 after**, each from a named command (`(Get-Content $log).Count`; `Select-String … 'rules'` for the line's position). The "before" was **derived from the file's own line numbering afterwards, not snapshotted at the moment** — §3 says so plainly instead of presenting a snapshot it never took, which is why this reads as met rather than dressed up. The criterion asks for the counts and their commands, and does not ask that the before be taken before. Under a log this task re-observed to be **lossy under concurrency**, a derived figure is the sounder of the two. Against the tick: the *first* run recorded 22 and 23 with no command named at all. One line reverses this if the maintainer reads the criterion as requiring a snapshot |
| Delivery is recorded as an **observation of the delivery shape**, never inferred from the marker being in context | met | Both runs recorded the shape — a separate block appended to the read, naming its source file — and both state the marker was not used, the first run explaining why it could not be. The second run adds corroboration the marker is incapable of producing: a hook line naming the probe, carrying `trigger_file_path` |
| Whichever cell is hit, T-169 §3's sentence is confirmed or corrected — and if corrected, corrected here, not left as advice | met | Row 1 → **confirmed**. Written into [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) itself as an annotation, so a reader of that record meets it there rather than only here. The first run's recorded note — that this criterion assumes every cell resolves the sentence, which row 3 does not — **stands untouched**: it was right about the cell it faced, and that cell was not the final one |
| If the cell is inconclusive, the rule stays in place and what the next session must do is written down | met | Fired on the first run and was discharged there: the probe stayed and the four steps were written. The proof is what they cost — the second run was **one read and one `Select-String`**, where [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) had paid a two-session setup for the same question |
| The rule carries a marker and **no real content** — T-155's rule, re-applied | met | The body, as the harness itself delivered it: `T171-PROBE-4B8E1D — this file is a test instrument for T-171. It carries a marker and no rule.` Quoted here because the probe is now deleted and this is the last place it can be checked — the criterion would otherwise be judged from a description of a file nobody can open |
| Whatever is left machine-local at the end is said to be, since `.claude/*` reaches no clone | met, **vacuously** | Recorded as vacuous rather than as a clean pass. **Nothing is left**: the probe is deleted and `.claude/rules/` is empty, both verified by command. The hook and its log do survive and are machine-local — they are T-169's instruments, not this task's, and are said to be user-scope there |

**Seven met, none carried, and one of them worth a second opinion.** The task closes. The only tick a
later reader should re-examine is the second: it turns on reading "recorded before and after" as a
statement about the figures rather than about when they were taken.

**On the phase this review did not re-do.** The first run's `implement` verdict — row 3, inconclusive —
is not overturned here and was never wrong. It reported the cell it observed. The second run hit a
different cell because it was a different session, which is precisely what the first run predicted it
would take.

**Open questions swept before closing** (`review` step 5). §1 records none, and none arose: the maintainer's
authorisation of 2026-08-17 fixed the reading in advance, which is what left nothing for a verdict to
refer upward. The compaction case stays unobserved and is **not** a residue of this task — T-169
accepted it as a risk against its worse branch and kept it off its own reversal list, so nothing here
is waiting on it.

**Child fix tasks raised**
- none. Every criterion is met, so there is no gap to carry. One defect **outside** this task's
  criteria was found while reviewing and is raised separately, per
  [`review`](../plugin/skills/taskmd/docs/method/review.md) *What review is not*:
  [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md)

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | **Seven criteria, seven met, none carried.** The verdict ran twelve minutes after the observation, across midnight, which is why the dates differ by a day and the record says so. Two ticks were made deliberately awkward rather than clean: the line-count criterion is **met on a reading**, because the second run derived its "before" figure from the file's own numbering instead of snapshotting it, and the note says so and invites reversal — the alternative was to quietly grade the criterion against what the run happened to do well. The machine-local criterion is met **vacuously** and is labelled vacuous, because nothing survives the task to be said machine-local. The first run's inconclusive verdict is **not overturned**: it reported the cell it saw, and predicted exactly what a second session would cost. The probe's body is quoted into §4 because the file is deleted and a criterion about its contents would otherwise be judged from a description of something nobody can open. One defect found while reviewing sits **outside** these criteria — a template placeholder left in five finished records that `check` does not catch — so it is raised as [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md) and not fixed here. |
| 2026-08-17 | — | **Row 1: delivered and logged. The hook sees rule loads, and [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) §3's sentence is confirmed rather than corrected** — which is what this task was raised to settle. A later session read `CLAUDE.md` **before opening any task record**, the delivery block arrived naming the probe, and the log gained one line reading `load_reason: path_glob_match`. The probe surviving the first run is what made the whole test one read and one command. Three things fell out that nobody asked for: the payload carries **`prompt_id`, `globs` and `trigger_file_path`**, which T-169's enumeration does not have and which make a rule line self-identifying; **the read of `CLAUDE.md` produced no line of its own**, only the rule it triggered, which separates the two readings T-169's second open question deliberately kept apart; and the log **lost this session's project-`CLAUDE.md` record to concurrency**, re-observing the limit rather than assuming it. The probe is **deleted** — step 4 of the first run's own instruction. Criterion 4's recorded defect is left standing as a judgement about row 3, because rewriting it now would let this result pick its own criterion. `review` is runnable for the first time and is **not** run here: one phase per request. |
| 2026-08-17 | → in_progress | `specify` and `plan` complete, `implement` run and **stopped at the same wall as [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md)**. The probe was written and the matching file read twice — partial and whole — and **no delivery arrived either time**, so the hook had nothing to report and its silence is not an answer. That is §1's row 3, reported into a table fixed before the run rather than argued afterwards. The log gained one line during the test and it belonged to **another session**, which is why the content check and not the count was the instrument. What the run did settle was never the question: **a rule written mid-session is not delivered to that session** — observed, where T-155 built its two-session design around assuming it. `review` must not run: three criteria judge an observation nobody has made. The probe stays in place so the next session pays one read instead of a setup. |
| 2026-08-17 | — | **The maintainer asked for this test in one request on 2026-08-17**, together with the ruling that the hook stays installed. It covers **T-171 and nothing it raises**. Recorded here because an authorisation kept anywhere else is one a later session can miss (METHOD §3.1). |
| 2026-08-17 | → proposed | Raised while answering a question about the hook, not from an audit: [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) closed asserting that `load_reason` would report a rule's load, and that half was never observed — the rules directory has been empty the whole time the hook has been live. Child of T-169 because it checks a claim in T-169's record; `research` and not `fix`, because nobody yet knows whether there is anything to fix. |
