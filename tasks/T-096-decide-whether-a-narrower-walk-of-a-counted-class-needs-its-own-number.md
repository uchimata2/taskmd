---
id: T-096
title: Decide whether a narrower walk of a counted class needs its own number
type: decision
status: done
phase: review
parent: T-095
blocked_by: []
related: [T-025]
work_package: M2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-10
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-096 — Decide whether a narrower walk of a counted class needs its own number

## 1. Specify

**Outcome**
A decision, recorded, on whether a check that walks a **subset** of an already-counted class gets a
denominator of its own — and the summary matching that decision.

**Why this one**
Raised at [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)'s review as the one
criterion it did not fully meet. T-095 merges denominators by noun, keeping the largest count, so
several checks that walk one class contribute one number. Two of them walk a genuinely narrower set:

- `check_cycles` walks only the **dependency** edges; `check_references` walks all of them and its
  larger count is what shows.
- `check_blocked_without_blocker` walks only tasks carrying the blocked status; the task total shows.

So the failure T-095 exists to make visible survives in miniature: if a schema change left no edge
classed as a dependency, cycle-checking would cover nothing while the summary still read `285
reference(s)` and the run still passed. Nobody has seen this happen — it is the shape of the hole,
not a report.

**Requirements served**
R-16, as T-095's.

**Scope**
- In: whether a subset walk earns its own noun, or whether the merge is right and the criterion was
  written too strictly.
- In: if it earns one, what the noun is called, since `285 reference(s), 140 reference(s)` says
  nothing to a reader.
- Out: the merge mechanism itself, which is working as designed — this is about what feeds it.
- Out: any other class. Two checks have this shape today; a rule covering ones that do not exist yet
  is speculation.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `examined`, and the two checks named above.
- [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) §2, which recorded the
  merge-by-largest decision and its reason.

**Acceptance criteria**
- [ ] The decision is recorded with what was rejected, whichever way it goes
- [ ] If subsets get their own number, narrowing the cycle walk on purpose shrinks a visible count —
      the same proof T-095 used, since a decision to add a number that nothing tests is not the fix
- [ ] If they do not, T-095's first criterion is amended openly rather than left reading as met

**Open questions**
- None. **Answered on 2026-08-10: a narrower walk gets its own noun.** The answer was decided by
  measurement rather than argument — see §3, where the argument for the other side was falsified.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Test the claim the merge rests on: that a narrowed dependency walk moves the wider reference count. | A before/after pair of summaries on a two-task project |
| 2 | Decide from what that shows, not from the shape of the argument. | The decision recorded in §3 |
| 3 | Give the cycle walk its own noun if the claim fails. | `check_cycles` in `cli.py` |
| 4 | Settle the other subset walk, which is a different shape. | `check_blocked_without_blocker` in `cli.py` |
| 5 | Hold it with a test that reproduces the reclassification. | `tests/test_cli.py` |
| 6 | Record the outcome against T-095's criterion, without rewriting the verdict it was given. | T-095 §4 |

**Outputs**
- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py

## 3. Implement

**Decisions & assumptions**
- **A narrower walk gets its own noun — 2026-08-10.** The case for merging was that a subset walk is
  complete over its own domain, so the wider count already witnesses any narrowing. **That is false,
  and the run is what showed it.** Reclassify one edge field from `dependency` to `soft` and the edge
  stays in `task.edges`: `check_references` still counts it, `check_cycles` no longer walks it, and
  the summary does not move by a character.

```
blocked_by: dependency   OK - 2 task(s), 10 field value(s), 1 reference(s), 0 declared output(s), ...
blocked_by: soft         OK - 2 task(s), 10 field value(s), 1 reference(s), 0 declared output(s), ...
```

  With the noun split out, the same pair reads `1 dependency edge(s)` and `0 dependency edge(s)`. On
  this repository the number is **22 dependency edges against 287 references** — the cycle check
  covers under a thirteenth of the graph, which nothing said before today.

- **`check_blocked_without_blocker` is a different shape and needed a different answer —
  2026-08-10.** It is not a subset walk: it iterates every task and filters, so the task count is its
  honest denominator. The dishonest branch was the disabled one, where `blocked_status: none` made it
  return early while still claiming `("task", len(tasks))` — a walk it had not done. It now returns
  nothing, which the merge accepts. *Rejected: a `blocked task` noun* — nearly always zero, and it
  would cost a place on the line to say what the config already says.
- **One noun added, not two — 2026-08-10.** The line is the output of every run, and the maintainer's
  standing concern is that a summary becomes a block and gets skipped. Splitting only where a hole
  was demonstrated keeps that cost proportionate to the evidence.

**What was checked by using it**

The reclassification above, run both ways, before and after the fix — the before pair being the
falsification and the after pair the proof. Then this repository, and the suite:

```
OK - 96 task(s), 480 field value(s), 287 reference(s), 22 dependency edge(s), 122 declared output(s), 1 index file(s), 154 document(s), 1152 link(s)
```

```
140 passed, 4 subtests passed
```

**Outputs produced**
- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with what was rejected, whichever way it goes | met | §3 records both the split and the rejected `blocked task` noun. The rejected *position* — merge is fine, criterion too strict — is recorded as falsified rather than as a preference, which is the more useful form. |
| If subsets get their own number, narrowing the cycle walk on purpose shrinks a visible count | met | `1 dependency edge(s)` → `0 dependency edge(s)` from one edge reclassified, held by a test that asserts the reference count *does not* move in the same run — the half that makes it a proof rather than a coincidence. |
| If they do not, T-095's first criterion is amended openly | n/a | They do, so there is nothing to amend. T-095's `partly met` verdict stands as written and now carries the outcome beneath it. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-10 | → done | Decided the opposite way to the argument that opened it. The specify said "nobody has seen this happen — it is the shape of the hole, not a report"; step 1 went looking and the hole was there, so the case for merging died on its first test rather than in discussion. Worth keeping as an instance of the project's own rule: the merge was defended by reasoning about what the wider count must witness, and one two-task project settled it in a minute. |
| 2026-08-10 | → proposed | Raised at T-095's review, from its own first criterion — "every class `check` examines carries a denominator" — which the merge-by-largest decision meets for six nouns and not for the two subset walks. `medium`/`xs` because the hole is real but narrow and nothing has been reported against it; the alternative is deciding the criterion was written too strictly, which is a legitimate answer and is why this is a decision rather than a repair. Not fixed where it was found (METHOD §5). |
