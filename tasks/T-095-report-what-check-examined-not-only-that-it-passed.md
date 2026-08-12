---
id: T-095
title: Report what check examined, not only that it passed
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-025, T-034, T-080, T-092, T-094]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, README.md]
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
- [ ] Every class `check` examines carries a denominator, with the classes taken from what `cmd_check`
      actually runs rather than from any list written down — shown by running it on this repository
      and on a fixture
- [ ] A deliberately narrowed scan produces a visibly smaller number — proven by narrowing one on
      purpose, since that is the failure the task exists to make visible
- [ ] The **failing** summary carries the same denominators as the passing one
- [ ] The counts stay on the first line, that line still opens with the pass/fail word, and the exit
      codes are unchanged — so `head -1` remains the whole parse a hook needs
- [ ] A second line states what `check` cannot decide, on the passing path

**Open questions**
- None. **Answered on 2026-08-10: the counts stay one line, and what the check cannot decide is a
  second, fixed line.** The two are different kinds of text and should not compete — the counts vary
  per run and are the thing that must be seen, the caveat is invariant and is skimmed past by the
  second run. Putting both on one line pushes the numbers rightward until a terminal wraps and hides
  its own tail. Two lines is also not four: the maintainer's worry about a summary being skipped
  starts when the output becomes a block. *Rejected: one line carrying both* — cheapest to parse, but
  it makes the invariant half crowd out the variable half, which inverts the task. *Rejected: the
  reporting project's four lines* — it says more, and three of the four would be invariant here.
- Also decided, and cheap to reverse: **the failing summary carries the denominators too.** A
  narrowed scan is exactly as invisible behind an unrelated problem as behind a pass, and today's
  `%d problem(s) over %d task(s)` has the same single denominator the OK line does. Read as a
  clarification of the stated outcome — "`check`'s summary" — rather than a widening of it.
- Also decided: **the caveat prints on the passing path only.** Its argument is that a silent pass is
  read as an endorsement; a failing run is not being read as one.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give every `check_*` a return value naming what it examined, as `(noun, count)` pairs. | Nine functions in `cli.py` returning their own denominators |
| 2 | Collect the returns at `cmd_check`'s call sites and merge them by noun. | A merged, call-ordered count list in `cmd_check` |
| 3 | Render both summary branches from that list, `OK` and the problem line alike. | The two branches of `cmd_check` |
| 4 | Make an absent generated index count as zero rather than return silently. | `check_stale_index` reporting `0 index file(s)` |
| 5 | Add the second line stating what `check` cannot decide, on the passing path. | The caveat line |
| 6 | Narrow one scan on purpose and capture the number before and after. | Before/after output recorded in §3 |
| 7 | Run on this repository and on a fixture; run the suite. | Command output recorded in §3 |
| 8 | Update whatever asserted on the old summary text. | `tests/` passing |

**Shape of the deliverable.** Each check *returns* what it examined and `cmd_check` assembles the
line from what it collected. *Rejected: `cmd_check` counting the classes itself* — it would re-derive
what the checks walked, so the number and the scan could drift apart, which is the exact failure this
task exists to remove. *Rejected: a shared mutable tally passed in beside `problems`* — it mirrors the
existing style, but a check that forgets to record anything stays silent, whereas a missing `return`
is visible at the call site.

Nouns are merged rather than summed, keeping the largest count seen for a noun: several checks walk
the same class over different subsets (`check_cycles` sees the dependency edges, `check_references`
all of them), and the reader's denominator is the wider one. A count whose noun is already shown adds
no line noise, which is what keeps seven checks from producing ten numbers.

**Outputs**
- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py

## 3. Implement

**Decisions & assumptions**
- **Each check returns what it examined; `cmd_check` assembles the line from what it collected —
  2026-08-10.** The alternative rejected at `plan` was `cmd_check` counting the classes itself, which
  would let the number and the scan drift apart. The property this buys was verified rather than
  assumed: `check_vocabularies` was stripped of its `return` and the run died at the call site —
  `TypeError: 'NoneType' object is not iterable`, naming the check — instead of printing a summary
  with one denominator quietly missing.
- **Nouns merge by largest, never by sum — 2026-08-10.** `check_cycles` walks the dependency edges
  and `check_references` walks all of them; summing would report 285 + 140 references over a project
  that has 285. Merging also collapses the three checks that walk the task set into one number, which
  is what keeps nine checks from printing ten numbers.
- **An absent generated index counts as `0 index file(s)` — 2026-08-10.** `check_stale_index`
  returning early is correct (T-025 §1) and was also invisible: "nothing was stale" and "nothing was
  compared" were the same output. This is the task's own thesis applied to the check that inspired it.
- **The README sample was updated, not just the code — 2026-08-10.** It showed the old line as the
  output of a fresh install, so leaving it would have published a claim the tool no longer makes.
  The empty-project run turned out to be the best illustration available and is quoted verbatim.

**What was checked by using it**

`check` on this repository, both branches, and on every `broken-*` fixture:

```
OK - 95 task(s), 475 field value(s), 285 reference(s), 119 declared output(s), 1 index file(s), 153 document(s), 1147 link(s)
structure and references only - it cannot tell you whether a spec or an outcome is good
```

```
BROKEN LINK   .notes/scratch.md -> gone.md

1 problem(s) - 1 task(s), 5 field value(s), 0 reference(s), 0 declared output(s), 0 index file(s), 2 document(s), 1 link(s)
```

**The narrowing, which is the criterion this task exists for.** `markdown_files` was given a
`d.startswith(".")` skip — one plausible line of scoping change — and the run compared against the
same tree before and after:

```
before   ... 1 index file(s), 153 document(s), 1147 link(s)
after    ... 1 index file(s), 123 document(s), 942 link(s)
```

**Both runs printed `OK` and exited 0.** Before this task the two lines were byte-identical, so 30
documents and 205 links left the scan with every available signal saying the project was fine — which
is the sibling project's incident reproduced here on purpose. The edit was reverted and the counts
returned to 153 and 1147.

A fresh project shows the same property from the other end — every denominator zero, where the old
line read as though four things had been verified:

```
OK - 0 task(s), 0 field value(s), 0 reference(s), 0 declared output(s), 0 index file(s), 0 document(s), 0 link(s)
```

Suite: `139 passed, 4 subtests passed` — six tests added, 133 before. One of them failed on its first
run for the right reason: it narrowed `nested-at-root`, which scans exactly one document, so halving
it produced the same number. Recorded in the test rather than quietly repointed.

**Outputs produced**
- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py
- README.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every class carries a denominator, classes taken from what `cmd_check` runs rather than a list | **partly met** | Seven nouns, each returned by the check that walked it; the derived-not-listed half was proven by deleting a `return` and watching the run die at the call site rather than under-report. What it does **not** cover is a check walking a *subset* of an already-counted class — `check_cycles` over the dependency edges, `check_blocked_without_blocker` over blocked tasks — which merge into the wider number by the decision recorded in §2. → **child task [T-096](T-096-decide-whether-a-narrower-walk-of-a-counted-class-needs-its-own-number.md)** |
| A deliberately narrowed scan produces a visibly smaller number | met | 153 → 123 documents, 1147 → 942 links, from one plausible line of scoping change; both runs still `OK` at exit 0, which is the whole finding. Held by a test rather than by this note. |
| The failing summary carries the same denominators as the passing one | met | Every `broken-*` fixture now prints `N problem(s) - ` followed by the same seven nouns. |
| Counts on the first line, pass/fail word first, exit codes unchanged | met | `OK - ` and `N problem(s) - `; `head -1` is still the whole parse. Exit codes are covered by the pre-existing suite, which asserts them per fixture and passes unchanged. |
| A second line states what `check` cannot decide, on the passing path | met | Present on a pass, absent on a failure, and both directions are asserted — the second is the half that would rot silently. |

**Child fix tasks raised**
- [T-096](T-096-decide-whether-a-narrower-walk-of-a-counted-class-needs-its-own-number.md) — whether
  a narrower walk of an already-counted class needs its own number. **Closed the same day, and it
  split the noun**: the merge was defended here on the argument that the wider count would witness a
  narrowing, and that argument is false — reclassifying an edge from `dependency` to `soft` leaves it
  counted as a reference while cycle-checking drops to nothing. The verdict above stands as written;
  `dependency edge` is now the fourth noun on the line, so the summary this task produced was wrong
  about its own coverage for exactly as long as it took to test it.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Four criteria met, one carried by T-096. The narrowing was reproduced rather than argued: the same tree lost 30 documents and 205 links to one plausible scoping line, and both runs printed `OK` at exit 0 — before this the two lines were byte-identical. The README sample was stale the moment the code changed and was updated from a real run, which turned out to be the clearest demonstration available: every denominator zero on a fresh project, where the old line read as though four things had been verified. |
| 2026-08-10 | → specified | Answered: counts on one line, the caveat on a second. The reasoning that decided it is not the one the question offered — the question weighed one line against four on length, and what actually separates them is that a per-run measurement and an invariant disclaimer are different kinds of text, so the constant is what gets skimmed and it takes the numbers with it. Two criteria added that the original set missed: the *failing* summary needs the same denominators, since a narrowed scan hides behind an unrelated problem just as well as behind a pass; and `head -1` is named as the parse a hook gets, because "parseable by whatever a hook would reasonably do" cannot be failed against. |
| 2026-08-09 | → proposed | Raised from the deck-building sibling's migration report, which arrived with the incident that produced it: a summary reading `0 broken` while two documents the tool pointed at were missing, and later while six pointers had dropped out of scope. `high` because this repository has already paid for the same class twice in a different check (T-034, T-080) and wrote the rule — judge a run by the file count, not by its silence — against a command that prints no count. Worth doing before T-092 and T-094, since both change what is examined and neither would be visible in today's line. |
