---
id: T-109
title: Decide whether a task that settles a question must be typed decision
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-088, T-090, T-093, T-097, T-098, T-104]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-109 — Decide whether a task that settles a question must be typed decision

## 1. Specify

**Outcome**
`list --type decision` either answers *what is waiting on a decision* or is known not to, so nobody
reads a short answer as a complete one.

**Why this one**
Found in the project status review of 2026-08-10 and raised so it is not lost with the session. Six
open tasks have question-shaped titles; two carry `type: decision` and four carry `type: fix`:

```text
T-021  decision  Settle what the context closing line may say
T-030  decision  Settle the schema module's own entry point
T-090  fix       Decide what a cancelled task's declared outputs assert
T-093  fix       Decide whether check resolves a section reference
T-097  fix       Decide whether a published document may point at a file no clone receives
T-098  fix       Decide who checks the links in a document only a successor reads
```

So the filter returns a third of them, and the third it returns is not distinguishable by anything a
reader can see. **It was raised in the review and the maintainer did not act on it** — recorded here
as a parked question rather than pressed, because a question nobody wrote down is one the next review
finds again from scratch.

**Neither typing is obviously wrong, which is why this is a decision and not a fix.** A task whose
*outcome* is an answer is a decision; a task that will also change a file once the answer is known is
plausibly a fix. All four of the mistyped set are both. The value has no stated test.

**It matters more since [T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md).**
That task settled that a decision lives in the task it belongs to, and that a register of taken
decisions is a view of those tasks. A view nobody can build — because the tasks holding decisions are
not identifiable — is a weaker answer than it reads as.

**Requirements served**
R-1 (`docs/SCOPE.md`) — a fact with one home is only useful if the home can be found. R-11, since
whatever is decided is a statement about what a vocabulary value means, which is configuration.

**Scope**
- In: whether the `decision` value carries a test, and what it is.
- In: retyping the four, or leaving them, as the decision requires.
- In: whether the shipped schema's `type` row gains a word about it — the vocabulary is documented
  there and currently says nothing about what any value means.
- Out: adding a field. A task that is both a decision and a fix does not need two type values; if the
  vocabulary cannot express it, that is the answer, not a schema change.
- Out: the vocabulary itself. `decision` stays; this is about when it applies.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Vocabularies*, and the pointer T-104 added.
- The six tasks above.
- [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md), the last time
  a `type` value's meaning was settled — the argument there was drift between the method's word and
  the schema's field.

**Acceptance criteria**
- [ ] The test for `type: decision` is written down, or it is recorded that there is none and why
- [ ] The four tasks above are consistent with whatever is decided
- [ ] `list --type decision` is run afterwards and its answer stated, so the claim is measured rather
      than asserted
- [ ] `check` is clean on this repository

**Open questions**
- **Does `decision` mean "the outcome is an answer"?** *Recommended: yes, and it wins over `fix` when
  a task is both* — the answer is what the task exists to produce, and the file change follows from
  it. That makes the filter complete and costs four field edits. *Alternative: leave the value
  untested and say so* — honest, cheap, and it means the vocabulary carries a value that cannot be
  used to find anything, which is what T-088 was raised to remove.

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
| 2026-08-10 | → proposed | Found in the project status review of 2026-08-10, surfaced to the maintainer, and **not acted on** — raised as a parked task rather than pressed, because an observation with no record is one the next review re-derives from nothing. `medium` because nothing is broken and the cost is a filter that quietly under-answers; `xs` because the work is a sentence and four field edits. Sized against the wrong reading deliberately: it looks like a typo to fix, and it is not — all four of the mistyped tasks are genuinely both a decision and a fix, and the vocabulary has never stated a test for which wins. Worth settling in the same pass as any re-grouping of `work_package`, since that touches every task's front-matter anyway. |
