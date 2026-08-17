---
id: T-171
title: Test whether the InstructionsLoaded hook can see a path-scoped rule
type: research
status: in_progress
phase: implement
parent: T-169
blocked_by: []
related: [T-155]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-17
updated: 2026-08-17
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

**Run 2026-08-17. The cell is row 3 — inconclusive — and the run was still worth making**, because
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

**Outputs produced**
- `.claude/rules/t-171-probe.md` — the instrument, machine-local, deleted once this task records its
  answer. Not a deliverable.
- The two observations above, and the session-start finding, are the outputs of steps 4 and 5.

## 4. Review

**Not run.** Three criteria judge an observation that needs a session this one cannot be. See §3.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → in_progress | `specify` and `plan` complete, `implement` run and **stopped at the same wall as [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md)**. The probe was written and the matching file read twice — partial and whole — and **no delivery arrived either time**, so the hook had nothing to report and its silence is not an answer. That is §1's row 3, reported into a table fixed before the run rather than argued afterwards. The log gained one line during the test and it belonged to **another session**, which is why the content check and not the count was the instrument. What the run did settle was never the question: **a rule written mid-session is not delivered to that session** — observed, where T-155 built its two-session design around assuming it. `review` must not run: three criteria judge an observation nobody has made. The probe stays in place so the next session pays one read instead of a setup. |
| 2026-08-17 | — | **The maintainer asked for this test in one request on 2026-08-17**, together with the ruling that the hook stays installed. It covers **T-171 and nothing it raises**. Recorded here because an authorisation kept anywhere else is one a later session can miss (METHOD §3.1). |
| 2026-08-17 | → proposed | Raised while answering a question about the hook, not from an audit: [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) closed asserting that `load_reason` would report a rule's load, and that half was never observed — the rules directory has been empty the whole time the hook has been live. Child of T-169 because it checks a claim in T-169's record; `research` and not `fix`, because nobody yet knows whether there is anything to fix. |
