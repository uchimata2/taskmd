---
id: T-169
title: Decide whether tier 1's prose about itself moves into a path-scoped rule
type: decision
status: proposed
phase: specify
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
- **Unknown.** The compaction case. T-155's criterion 2 closed as *not answered, and why* — the
  `InstructionsLoaded` hook was never enabled and no session can force a compaction. **The instrument
  still exists**: `.claude/rules/t-155-probe.md` was kept against T-155's own instruction to delete
  it, precisely so this question stays answerable.

**Scope**
- In: the decision, with its reasons, recorded where a later reader finds it
- In: the move itself, if the decision is to carry — including whatever `.gitignore` amendment it
  needs, which is part of the cost rather than a detail after it
- In: the compaction observation, if the decision turns on it. The probe is in place
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
- [ ] <written at `specify`>

**Open questions**
- **Is the compaction case a precondition for deciding, or a risk the decision can accept?** It is
  the one thing T-155 could not observe. **The instrument is gone**: the maintainer had
  `.claude/rules/t-155-probe.md` deleted on 2026-08-17, so answering *precondition* now means
  rebuilding it first. That is two lines and not a loss — T-155 §3 records the format that fired,
  `paths:` with one entry, and the marker sentence — but it is no longer in place. **The maintainer
  answers, at `specify`.**
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

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | — | **Both of this task's open questions moved the same day, on the maintainer's instruction, and neither is answered.** The probe was **deleted**, so the compaction observation now starts by rebuilding the rule rather than by compacting — the recipe survives in [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3, which is why this is a cost and not a loss. The `InstructionsLoaded` hook was **installed at user scope**, which moves step 4's ask from *outstanding* to *unverified*: the event is real (it is in the settings schema's hook-event enum) and the logging command is pipe-tested, but nothing has been seen to fire. Recorded with **both** readings of that silence intact — a mid-session `hooks` key that is not live yet, versus an event that fires on instruction *loading* and not on a file read — because the discriminating test was declined by the permission classifier and a record that picked one would be guessing. A restart settles it. |
| 2026-08-17 | → proposed | Raised from [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) at `review`, step 9 of its plan, which said to raise this **only if** the mechanism holds. It held. `decision` and not `fix` because the size and the reach both moved against the remedy while the mechanism moved for it, so what happens next is a judgement rather than an edit somebody already agreed to. Child of T-155 rather than of [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md): the audit's job was to find and report, and this is the consequence of testing one finding, not a further finding. **Raised on the maintainer's explicit request of 2026-08-17**, which covered reviewing T-155 and raising this task and **nothing else** — this task takes one phase per request from here. |
