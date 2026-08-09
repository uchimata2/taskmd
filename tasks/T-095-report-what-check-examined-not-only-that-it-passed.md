---
id: T-095
title: Report what check examined, not only that it passed
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-025, T-034, T-080, T-092, T-094]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-095 — Report what check examined, not only that it passed

## 1. Specify

**Outcome**
`check`'s summary carries the denominators — how many of each thing it looked at — so a count that
silently shrinks is visible. Today the line says what passed and not what was examined.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`), which had already been bitten:
its own checker's summary *"used to read 0 broken links while two documents the tool itself points at
were missing"*, and a later scoping change dropped six pointers out of validation while the summary
still read `0 broken`. It now prints what it did rather than what passed.

taskmd prints one line:

```
OK - 61 task(s), vocabulary valid, references resolve, no broken links
```

The task count is a denominator; nothing else is. "No broken links" over zero links examined reads
identically to "no broken links" over a thousand.

**This is the project's own most-repeated lesson, applied to the tool instead of the process.**
`CLAUDE.md` says of the pre-publish check that the omission *"was silent for as long as it existed —
a check that reads none of the files it was aimed at prints nothing, which is also what success looks
like"*, and [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md) added *"judge a run
by the file count, not by its silence."* That instruction is unfollowable against `check`, because
`check` does not print a file count.

**It also affects two tasks raised the same day.**
[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) and
[T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) both change *what* is
examined. Whichever way each is decided, the change is invisible in the current summary — which is
an argument for doing this one first.

**Requirements served**
R-16. `docs/SCOPE.md` §1 *Invisibility* in the negative sense: a number nobody has to maintain but
everybody can see.

**Scope**
- In: which denominators the summary carries — documents scanned, links checked, tasks read, and
  whatever [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) and
  [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) add.
- In: whether the summary also names what the check **cannot** decide. The reporting project's line
  is *"structure and references only — it cannot tell you a spec or a deliverable is any good"*, and
  its argument is that a validator that passes silently is read as an endorsement.
- In: keeping the line usable from a script. `check`'s output is read by people and by hooks.
- Out: the problem lines themselves, which are fine.
- Out: a verbosity flag. One summary that is honest beats two that differ.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `cmd_check`'s final two branches.
- `CLAUDE.md` *The pre-publish check*, for the silence argument in its original form.
- [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) and
  [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md), the two occasions this
  project paid for it.

**Acceptance criteria**
- [ ] The summary carries a denominator for every class `check` examines, shown by running it on this
      repository and on a fixture
- [ ] A deliberately narrowed scan produces a visibly smaller number — proven by narrowing one on
      purpose, since that is the failure the task exists to make visible
- [ ] The line remains parseable by whatever a hook would reasonably do with it
- [ ] What the check cannot decide is stated, or the decision not to state it is recorded

**Open questions**
- **How much the summary may grow.** The reporting project's runs to four lines. One line is
  scriptable and scannable; four say more and start being skipped. The maintainer's, since it is the
  output every user sees on every run.

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
| 2026-08-09 | → proposed | Raised from the deck-building sibling's migration report, which arrived with the incident that produced it: a summary reading `0 broken` while two documents the tool pointed at were missing, and later while six pointers had dropped out of scope. `high` because this repository has already paid for the same class twice in a different check (T-034, T-080) and wrote the rule — judge a run by the file count, not by its silence — against a command that prints no count. Worth doing before T-092 and T-094, since both change what is examined and neither would be visible in today's line. |
