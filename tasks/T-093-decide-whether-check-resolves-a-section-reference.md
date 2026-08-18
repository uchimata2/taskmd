---
id: T-093
title: Decide whether check resolves a section reference
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-092, T-095]
work_package: M6
owner: maintainer
business_value: medium
effort: l
created: 2026-08-09
updated: 2026-08-11
deliverables: []
---

# T-093 — Decide whether check resolves a section reference

## 1. Specify

**Outcome**
A decision, recorded with its alternative, on whether a citation of the form *document §n* is a
reference `check` resolves — and if so, what binds a mark to a document and what happens to a mark
nothing binds.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`) from the same migration that
produced [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md). Its observation is
sharp and checkable: **taskmd uses the convention throughout its own documentation and cannot check
it.** This repository's prose cites `METHOD §4`, `METHOD §1 rule 5`, `docs/SCOPE.md §9`, `T-011 §1`
and `BINDING.md §4` — including in the source comments of the tool itself. Renumber a section and
every citation of it lies, silently, exactly like a moved file.

That project cites 497 of them and had 1394 unresolved before it built a rule.

**Why it is more than a link check.** A `§n` is a pointer whose target is a number *printed inside
the document it points at*, so it is mechanically resolvable — but only once you know **which**
document a bare `§n` belongs to. The reporting project measured two bindings and recorded the result:
*adjacency* — the document named next to the mark — against *nearest document mentioned in the
paragraph*, and the second picked the wrong target for a third of the misses it reported. That
measurement is the most valuable thing in the report and is the reason this task is `l` rather than
`m`.

**Requirements served**
R-16. R-13 in the same sense as T-092.

**Scope**
- In: whether this belongs in taskmd at all, given the convention is the method's rather than the
  tool's.
- In: if yes — the binding rule, what `§n.m` may resolve against, and the treatment of marks the
  form does not bind. The reporting project **counts and reports those as skipped** rather than
  dropping them, which is the same argument as [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md).
- In: that a `§` inside a code span or fence is literal text — which is what lets a document quote a
  reference that is wrong, and this repository's task records do exactly that.
- Out: renumbering anything, or any opinion on how sections should be numbered.
- Out: bare paths in prose, which is [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md).

**Inputs**
- The reporting project's `tools/docs/refcheck.py`, MIT, with a self-test that rejects `§9.4` and
  `§0.9` while accepting `§5.1` and `§0.8`. Offered as a reference implementation, not a patch.
- This repository's own `§` citations, as the corpus to try any rule against.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative
- [ ] If in: a fixture cites a document at a section it does not have, and `check` reports it, shown
      failing first
- [ ] If in: a mark the rule cannot bind is reported as skipped and counted, never dropped
- [ ] If in: a `§` inside a fence is not resolved, proven by a fixture that quotes a wrong reference
      on purpose
- [ ] If out: the reason is written where an adopter reads it, since taskmd's own documents use the
      convention and a reader will assume it is checked

**Open questions**
- ~~**Whether this is taskmd's job.** It is a documentation-integrity check, not a task-graph check,
  and everything else `check` does is about tasks and their edges. Adding it widens what the tool is
  for. Against that: the method's own documents are the thing most cited by section, and the tool
  already validates Markdown links across the whole tree rather than only in task files. The
  maintainer's.~~ **Answered by the owner on 2026-08-19: yes, it is taskmd's job** — see the Log row
  of that date for the rejected option and its cost.

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
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 8 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). It is last in the order and the only `l` in the eight, so it is the one most likely to end in a recorded question rather than a close — which the instruction above makes an acceptable outcome. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: yes, this is taskmd's job.** Asked in the backlog-wide round of 2026-08-19. The reason given is the one §1 already carried — `check` validates Markdown links across the whole tree rather than only in task files, so resolving the section a reference names is the same job one level deeper, not a widening. *Rejected: ruling it out of scope as a documentation check*, which keeps a clean task-graph boundary at the price of section references breaking in silence whenever a document is reorganised, in a project that cites its own method by section throughout. The binding rule and the reporting shape are still open and belong to `specify`. This row is the answer, not authorisation to start. |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-09 | → proposed | Raised from the deck-building sibling's migration report. The observation that carries it is that taskmd uses `§n` citations throughout its own documentation, including in the tool's source comments, and has no way to check one. `M3` rather than `M2` because it widens what the tool is for and that question should not be answered in a milestone about holding up in another project. `l` because the binding rule is the hard part and the reporting project has already measured that adjacency beats proximity — proximity picked the wrong target a third of the time. |
