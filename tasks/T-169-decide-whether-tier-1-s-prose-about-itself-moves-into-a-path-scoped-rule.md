---
id: T-169
title: Decide whether tier 1's prose about itself moves into a path-scoped rule
type: decision
status: done
phase: review
parent: T-155
blocked_by: []
related: [T-118, T-153]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-169 — Decide whether tier 1's prose about itself moves into a path-scoped rule

## 1. Specify

**Outcome**
A decision, taken by whoever owns `CLAUDE.md`, on whether the block of it that is **prose about
`CLAUDE.md`** moves into a path-scoped rule under `.claude/rules/` — and, if the answer is yes, the
move itself. [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) measured
the mechanism and deliberately carried nothing; this is the task that carries, or declines to.

**Why this one**
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3 observed the middle
row of its own table on 2026-08-17: the marker was **absent** from the context a session was handed
and **present** the moment `CLAUDE.md` was read. So the mechanism does what
[E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) hoped, and the carry decision it was
holding open becomes real. T-155's recorded decision of 2026-08-15 sends that decision **here** rather
than into a re-opened [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md): new evidence
licenses re-opening a recorded decision, never reversing it, and T-118's account of why the prose
stayed is the only one there is.

**The evidence does not all point one way, and that is why this is a decision and not a fix.**

- **For.** The mechanism is confirmed by observation rather than by documentation, and the format that
  fired is known — `paths:` with one entry.
- **Against, on size.** What a successful relocation would now extract is roughly **1,000 to 1,180
  characters**, about half what phase 1 priced, because
  [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) already took 806 of them
  into block comments at no relocation risk.
- **Against, on reach.** `.gitignore` excludes `.claude/*`, so a rule placed there is **machine-local
  and reaches no clone**. The remedy would move prose out of a file every clone gets and into one no
  clone gets, unless the ignore rule is amended to re-include part of a directory excluded wholesale
  for a stated reason. This is the fourth risk, and E-13 never weighed it.
- **Unknown.** The compaction case. T-155's criterion 2 closed as *not answered, and why* — no session
  can force a compaction, and when that was written the `InstructionsLoaded` hook had never been
  enabled. **Corrected 2026-08-17: both states this bullet was written against are gone.** It said the
  hook was never enabled, and that `.claude/rules/t-155-probe.md` was retained against T-155's own
  instruction so the question stayed answerable. The probe was **deleted** the same day on the
  maintainer's instruction, and the hook was **installed and has since been observed to fire**. The
  question is no less open; what would answer it is now the hook's log plus a rule somebody rebuilds,
  rather than an instrument already in place.

**Scope**
- In: the decision, with its reasons, recorded where a later reader finds it
- In: the move itself, if the decision is to carry — including whatever `.gitignore` amendment it
  needs, which is part of the cost rather than a detail after it
- In: the compaction observation, if the decision turns on it. ~~The probe is in place~~ — **it is
  not**, corrected 2026-08-17; the line was true for a few hours of the day this task was raised
- In: re-measuring the block at decision time. T-155's figure was taken 2026-08-15 and is only good
  while `CLAUDE.md` is unchanged
- Out: rewriting [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md)'s decision. It was
  right on what it knew; cite it, annotate it, never edit it
- Out: advising adopters to use `.claude/rules/`. Since T-053 the plugin is the `plugin/` subtree, so
  neither `CLAUDE.md` nor a rule beside it reaches anybody

**Inputs**
- [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3 — the observation,
  the re-measured block, the four risks, and the retained probe
- [E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) and
  [E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03) — the finding and the mechanism
- [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) — the decision this cites
- `CLAUDE.md` — the block itself

**Acceptance criteria**

Written 2026-08-17. They judge a **decision**, so they must be answerable whichever way it goes — a
criterion that only fits *carry* would make declining look like a failure to finish.

- [ ] The decision is recorded with its reasons, and names which evidence moved it
- [ ] The block is **re-measured at decision time**, with the command that produced the figure — not
      carried from [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md)
- [ ] The **budget's current margin** is measured. A size argument with no margin beside it says
      nothing about whether the saving is needed
- [ ] The reach question is settled by **running something**: what a clone receives is measured, not
      argued from the ignore file's text
- [ ] [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) is cited and **not edited**
- [ ] The compaction case is either observed, or **named as an accepted risk** — with the branch the
      decision assumed, and what would report it later
- [ ] If the decision is **carry**: the move is done, `.gitignore` amended, and the budget re-run
      afterwards
- [ ] If the decision is **decline**: what would reverse it is written down in terms a later session
      could check, rather than as a mood
- [ ] Nothing here advises adopters to use `.claude/rules/` (scope, Out)

**Open questions**
- **Is the compaction case a precondition for deciding, or a risk the decision can accept?** It is
  the one thing T-155 could not observe. **The instrument is gone**: the maintainer had
  `.claude/rules/t-155-probe.md` deleted on 2026-08-17, so answering *precondition* now means
  rebuilding it first. That is two lines and not a loss — T-155 §3 records the format that fired,
  `paths:` with one entry, and the marker sentence — but it is no longer in place. **The maintainer
  answers, at `specify`.**
  **Answered at `specify` on 2026-08-17, under the whole-lifecycle authorisation recorded in the log:
  a risk the decision can accept, not a precondition.** Three reasons, and the third is the one that
  decides it. Nobody can force a compaction, so a precondition parks this task on an event that
  arrives by chance — the same wall T-155 hit, made permanent. The hook is now a **standing**
  instrument: `load_reason` will carry a value other than `session_start` the first time a non-start
  load happens, so the observation can arrive later and annotate the decision instead of gating it.
  And the decision can be taken against the **worse** branch — assume the rule does *not* re-fire
  after a compaction — because if the remedy fails to pay under that assumption, an observation
  confirming the better branch cannot change the answer. *Rejected:* rebuild the probe and wait. It
  buys the better branch of a question the decision does not turn on, at the cost of leaving a
  machine-local rule in place indefinitely.
- **The `InstructionsLoaded` hook is installed and unverified, which is a different state from
  outstanding.** T-155's step 4 asked for it and closed without it; the maintainer authorised it on
  2026-08-17 and it is now written at user scope. Two things are settled and one is not. **The event
  exists** — it is in the settings schema's own hook-event enum, so the ask was never void, which is
  more than the record could say before. **The command works** — pipe-tested against a synthetic
  payload, exit 0, one line written. **Whether the hook fires is unobserved**, and the two readings
  must not collapse: a `hooks` key added mid-session may not be live until a restart, or the event
  may fire only when instruction files load *as instructions* and not when one is read as a file — it
  did not fire on a `Read` of `CLAUDE.md`. The test that separates those needs a second hook on an
  event triggerable in-turn, and the permission classifier declined it. **A restart settles it**, and
  that is the same wall T-155 hit: no session observes its own instruction- or config-file change.
  **The instrument is `.claude/instructions-loaded.log` in the user directory**, written by the hook,
  one line per event carrying that event's whole payload — the field naming *which* load happened is
  the one this task needs and nobody knows yet what the payload holds. A line there after a restart
  is the first reading; no line is the second.
  **Answered on 2026-08-17, by reading the log after the restart: the hook fires.** The file holds
  **14 complete records written by real session starts**, the earliest at 23:00, alongside the
  synthetic pipe-test line from before the restart. So of the two readings this task kept apart, the
  file shows **the first** — a `hooks` key added mid-session is not live until a restart. That is
  what the file shows and not an argument about why; the second reading is neither confirmed nor
  refuted, because nothing here ever made a `Read` of an instruction file due to produce a line.
  **The payload is `session_id`, `transcript_path`, `cwd`, `hook_event_name`, `file_path`,
  `memory_type`, `load_reason`.** The field naming *which* load happened is `file_path`, qualified by
  `memory_type` (`User` / `Project`) — both this repository's `CLAUDE.md` and the user-scope one
  appear, on separate lines. **`load_reason` is the field the compaction question needs**: every
  record so far reads `session_start` and none reads anything else, so the compaction case is still
  unobserved — but it now has a named discriminator instead of a hope.
  **Two properties of the instrument bear on how any later reading is taken.** It is **lossy under
  concurrency**: 3 of the log's 18 lines are truncated JSON tails (`"}`, `rt"}`) written while several
  sessions started at once, and this session's own record for the project `CLAUDE.md` is missing with
  a fragment in its place. And it is **not one line per session**: one session start produced four
  records, two `User` and two `Project`. So the log proves what is present in it, and an absence in it
  proves nothing — least of all that a load did not happen.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Rule on `specify`'s first open question **before** measuring anything. A precondition ruling taken after the figures are in would be chosen by them | The ruling, in §1's open questions |
| 2 | Re-measure the block and — the part [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) never had — the budget's current margin | The figures below |
| 3 | Measure what a clone receives by **running** `git check-ignore`, not by reading `.gitignore`'s text | The reach finding below |
| 4 | Test the remedy against [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md)'s **stated reason**, which is why the prose stayed. Size was never that reason | The finding below |
| 5 | Take the decision, with the rejected alternatives recorded beside it | The decision below |
| 6 | Decline → write what would reverse it, checkably. Carry → move the block, amend `.gitignore`, re-run the budget | §3's closing block |
| 7 | Judge the nine criteria | §4 |

## 3. Implement

**Re-measured 2026-08-17, at decision time, which the scope asked for.** `git log -1 -- CLAUDE.md` is
`557a7ec`, 2026-08-15 — [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s
block-comment work — so this is the same file T-155 tested against, and the block agrees with its
1,578 characters to within where the boundary lines are drawn.

```
tier 1 6305 chars under by 1541 (bound 7846, reference/TASK-WORKFLOW.md)
       from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       836 chars of block comment are not counted (T-159)

paid CLAUDE.md                    5908 chars   (raw 6744)
  three tiers                      715
  TASK-WORKFLOW bound              143
  what earns a place here          717
  META-BLOCK TOTAL                1575 chars   26.7% of the paid file, 25.0% of tier 1

headroom 1541 chars (19.6% of the bound)
```

**The margin is the figure the size argument never had beside it.** E-13 priced the prize and nothing
priced the need. Tier 1 is **under its bound by 1,541 characters**, and the entire meta-block is
**1,575** — so a perfect relocation would roughly double a headroom that is already a fifth of the
bound. The realistic prize is smaller still: T-155's carve-out leaves 400 to 600 characters that are
operative before a session has chosen its work, so what would actually leave is **≈1,000 to 1,180**.
The budget does not bind, and this remedy exists to make it bind less.

**What a clone receives, measured rather than read off the ignore file:**

```
$ git check-ignore -v .claude/rules/example.md
.gitignore:23:.claude/*	.claude/rules/example.md
$ git ls-files .claude
.claude/settings.json
```

**The strongest argument for the remedy is not size, and it is set aside only after being stated.**
[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) kept this block in tier 1 for one
stated reason: editing `CLAUDE.md` is an activity nobody announces, so a rule governing it cannot sit
one tier down where a session must already know to load it. T-155 then observed that the mechanism
fires **on the read of a matching file** — and an edit is preceded by a read of the file being
edited. The rule would arrive at precisely the moment the unannounced activity begins. That does not
weaken T-118's objection; it **answers** it, and this task would be dishonest to record the decision
without saying so.

**It still does not carry, because answering the objection is not a reason to move.** The mechanism
removes the blocker. What a move needs is a positive case, and the positive case was always the
characters — which the margin above says are not needed. Three further costs point the same way, and
the third is one nobody has named before:

1. **Reach.** A rule under `.claude/rules/` reaches no clone, measured above. The amendment is one
   `.gitignore` line, but its cost is not one line: `.claude/*` is excluded **because the harness
   writes into that folder on its own schedule, including machine paths resolved absolutely**.
   Re-including part of it puts a harness-written directory inside a repository whose first
   publishing constraint is no machine data. That is a standing exposure traded for a saving nobody
   needs.
2. **Compaction, assumed at its worse branch** per `specify`'s ruling: the rule does not re-fire.
   Tier 1 is re-injected every turn by definition; a path-scoped rule is delivered once, on a read.
   So the remedy trades a guarantee for a delivery.
3. **The block's audience would split into two opposite invisibilities.**
   [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) already sent 836
   characters of this same material into block comments — **visible to a human, stripped for the
   agent**. A path-scoped rule is the mirror: **delivered to the agent, invisible to a human** reading
   `CLAUDE.md` on GitHub or in an editor. Take both and one short rule about what earns a place in
   this file exists in three fragments, no two of which any single reader sees. Nothing in E-13 or
   T-155 weighed this, because T-153 was still in progress when they were written.

**Decisions & assumptions**

- **Decline. The block stays in `CLAUDE.md`** — 2026-08-17. The mechanism works and the reason for
  the block being where it is has been answered; neither of those is a reason to move it while the
  budget has 1,541 characters of headroom and the move costs reach, a delivery guarantee, and a third
  fragment of one rule. *Rejected:* **carry now** — it spends a standing publishing exposure on a
  saving of ≈1,000–1,180 characters against a margin of 1,541, which is buying room in a room that is
  already empty. *Rejected:* **carry only the operative half** — it produces the three-fragment
  outcome of cost 3 at half the prize, which is the worst cell in the table.
- **Assumed: the rule does not survive a compaction** — 2026-08-17, per `specify`'s ruling to decide
  against the worse branch. The work survives being wrong: the better branch would only strengthen a
  case already declined on other grounds, so an observation later cannot flip this decision by
  itself. That is what makes it an assumption and not a question (METHOD §3.2).
- **[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) is cited and untouched** —
  2026-08-17. Its account of why the prose stayed is the only one there is, and it was right on what
  it knew. This record supersedes nothing there; it adds what T-155 measured afterwards.

**What would reverse this, in terms a later session can check.** A decline with no trigger is a mood,
so here are the three that would make it wrong. Any **one** of the first two, together with the third:

1. **The margin stops covering the block.** `python tests/test_budget.py` prints `under by N`; when
   *N* is smaller than the block, the saving stops being optional. It is 1,541 against 1,575 today.
2. **Tier 1 grows for a reason that cannot be refused** — a served skill's `description`, which is
   derived from the tree and not this file's to cut.
3. **`.claude/rules/` becomes shippable without re-including a harness-written directory** — the
   harness gaining a location outside `.claude/`, or the folder ceasing to be machine-written. Without
   this, moving the block only relocates it out of everyone's reach but one machine's.

The compaction observation is deliberately **not** on this list. It can annotate the record whenever
`load_reason` first reports a non-`session_start` load; it cannot reverse a decision that assumed its
worse branch.

**Outputs produced**

- This record. **Nothing moved**: `CLAUDE.md`, `.gitignore` and `.claude/` are untouched by this task,
  which is what a decline means and is checked as a criterion rather than asserted.

## 4. Review

Run 2026-08-17, against the nine criteria as `specify` wrote them.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its reasons, and names which evidence moved it | met | §3 names it: the **margin**, which nothing before this task had measured. The mechanism working and T-118's objection being answered are both recorded as pointing the other way, so the record shows a decision taken against its strongest counter-argument rather than one that never met it |
| The block is re-measured at decision time, with the command that produced the figure | met | 1,575 characters, 26.7% of the paid file, from the run quoted in §3. `git log -1 -- CLAUDE.md` is 2026-08-15, so the file is the one T-155 tested — the figures were re-run anyway, because "unchanged" is a claim that needs a reader |
| The budget's current margin is measured | met | `under by 1541` (bound 7,846; tier 1 6,305). This is the criterion that changed the answer, and it exists because a size with no margin beside it is not evidence |
| The reach question is settled by running something | met | `git check-ignore -v` returns `.gitignore:23:.claude/*`, and `git ls-files .claude` returns one path. Read, not argued from the ignore file's prose |
| [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) is cited and not edited | met | Cited in §3 twice and unmodified. `git log -1 -- tasks/T-118-*.md` predates this task and this task wrote nothing to it |
| The compaction case is either observed, or named as an accepted risk with the branch assumed and what would report it later | met | By the second branch. Named as accepted, the **worse** branch assumed, and the reporter named: `load_reason` in the hook's log. Not observed — no session forces a compaction |
| If carry: the move is done, `.gitignore` amended, budget re-run | n/a | The decision was decline. Recorded as not applicable rather than met, because a criterion whose branch was never taken passes for a different reason than one that held |
| If decline: what would reverse it is written down checkably | met | Three triggers in §3, two of them a command's output and the third an observable change in where the harness writes |
| Nothing here advises adopters to use `.claude/rules/` | met | The mechanism is discussed only as it applies to this repository's own `CLAUDE.md`, which since T-053 no adopter receives. No binding, skill or doc was touched |

**Eight met, one not applicable, none carried.** No child fix task: a decline produces no follow-up
work by construction, and the three reversal triggers are conditions to notice rather than work to
schedule.

**Child fix tasks raised**
- none

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → done | **Declined: the block stays in `CLAUDE.md`.** The whole lifecycle ran in one session. What decided it was a figure nobody had taken: tier 1 is **under its bound by 1,541 characters** and the block is **1,575**, so the remedy would double a headroom that is already a fifth of the bound. The decision is recorded against its strongest counter-argument rather than around it — the mechanism works, and it **answers** [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md)'s stated reason, because a path-scoped rule fires on the read that precedes an edit, which is exactly when the unannounced activity starts. Answering the objection removes the blocker; it is not itself a reason to move. Three costs point the other way, and the third is new to this task: reach (measured with `git check-ignore`, not read off `.gitignore`), a delivery in place of tier 1's per-turn guarantee, and — unweighed by E-13 or T-155 because [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) was still running — the block splitting into **two opposite invisibilities**, comments a human sees and an agent does not, a rule an agent sees and a human does not. Three reversal triggers are written down, two of them a command's output. **T-118 was cited and not edited**, which the raise required. |
| 2026-08-17 | — | **The maintainer authorised this task's whole lifecycle in one request on 2026-08-17** — `specify` → `plan` → `implement` → `review` — covering **T-169 and nothing it raises**. Recorded here rather than only in the exchange that gave it, because an authorisation kept anywhere else is one a later session can miss or stretch to a task it never reached (METHOD §3.1). It also settled who decides: the outcome names the owner of `CLAUDE.md`, and a request to run the lifecycle is the delegation of that call — so the decision is taken here with its rejected alternatives beside it, and it is one line to overturn. |
| 2026-08-17 | — | **The hook fires, and the log says which load it was.** Read at the maintainer's instruction, which covered that observation and nothing else — no `specify`, and nothing this task goes on to decide. The second open question carries what the file shows: **the first of its two readings**, a mid-session `hooks` key that is not live until a restart, recorded because that is what the file shows and not because an argument picked it. What this buys the decision is `load_reason`: the compaction case stays unobserved, but it is now a field to read rather than a thing to hope for. Two limits of the instrument are recorded with it — concurrent session starts truncate lines, and one session start can write four records — so **an absence in this log is not evidence**, which is exactly how a compaction reading could go wrong. |
| 2026-08-17 | — | **Both of this task's open questions moved the same day, on the maintainer's instruction, and neither is answered.** The probe was **deleted**, so the compaction observation now starts by rebuilding the rule rather than by compacting — the recipe survives in [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3, which is why this is a cost and not a loss. The `InstructionsLoaded` hook was **installed at user scope**, which moves step 4's ask from *outstanding* to *unverified*: the event is real (it is in the settings schema's hook-event enum) and the logging command is pipe-tested, but nothing has been seen to fire. Recorded with **both** readings of that silence intact — a mid-session `hooks` key that is not live yet, versus an event that fires on instruction *loading* and not on a file read — because the discriminating test was declined by the permission classifier and a record that picked one would be guessing. A restart settles it. |
| 2026-08-17 | → proposed | Raised from [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) at `review`, step 9 of its plan, which said to raise this **only if** the mechanism holds. It held. `decision` and not `fix` because the size and the reach both moved against the remedy while the mechanism moved for it, so what happens next is a judgement rather than an edit somebody already agreed to. Child of T-155 rather than of [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md): the audit's job was to find and report, and this is the consequence of testing one finding, not a further finding. **Raised on the maintainer's explicit request of 2026-08-17**, which covered reviewing T-155 and raising this task and **nothing else** — this task takes one phase per request from here. |
