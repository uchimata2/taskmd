---
id: T-022
title: Filtered task listing for scripts
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-003, T-007]
work_package: none
owner: maintainer
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-022 — Filtered task listing for scripts

## 1. Specify

**Outcome**
A way to ask taskmd for *a subset* of the tasks, in a form a script or an agent can consume without
parsing the human index — for example "everything not yet specified", "everything that depends on
something open", "the children of T-002".

**Requested as** (maintainer, 2026-08-05):

```
/taskmd [list|table] [new|specified|planning|dependent|parents|children]
```

**Why this one**
`index` already computes the whole graph and renders it; what it cannot do is answer a narrower
question. Today the answer is grep over `tasks/`, which works for a person reading and badly for a
script: it re-parses front-matter that taskmd has already parsed, and it cannot see a derived edge
at all — `blocks` and the far end of a soft link exist nowhere on disk, so no grep will ever find
them. That is the gap this task is really about.

**This collides with a decided non-goal, and that has to be settled first.**
[`docs/SCOPE.md`](../docs/SCOPE.md) §4 non-goal 11 reads: *"A query language. `context`, `index` and
`check` are the surface. Anything else is grep."* Decided in
[T-007](T-007-define-the-project-scope-goals-and-requirements.md) and reaffirmed on 2026-08-05 in
[T-002](T-002-implement-the-core-cli-context-index-check.md), where it was the stated reason
`decisions` and `deliverables` were **not** built. Building a fourth command now would reverse a
decision two tasks have already been built on, so it is the owner's call, not this task's.

There is a shape that may not need the reversal. Non-goal 11 names `index` as part of the sanctioned
surface, and filtering is what `index` already does internally to split active from closed. Options,
in rough order of how much scope they cost:

1. **Options on `index`** — `index --status <v> --phase <v> --parent <id> --format list|table`. No
   fourth command, so non-goal 11 stands unamended. Least cost; least discoverable.
2. **A fourth command, `list`**, and non-goal 11 is amended to name four. Honest and explicit —
   but it reopens the boundary, and the next request after this one arrives at the same door.
3. **Nothing in the CLI; the skill composes it** — the agent runs `index` and filters. Cheapest of
   all, and worthless to the *script* case in the request, which is the case grep already fails.

**A trap in the requested vocabulary.** `new`, `specified` and `planning` are not taskmd's words —
the default vocabulary has `proposed`, `specified`, `planned`, and a project may rename all of them
(`tests/fixtures/alt-project` uses `todo`/`doing`/`waiting`). A filter that accepts a fixed alias
list would hardcode one project's vocabulary, which is exactly the defect
[T-002](T-002-implement-the-core-cli-context-index-check.md) criterion 7 forbids. Whatever the
filter accepts must come from the schema. Likewise `dependent`, `parents` and `children` are edge
**names**, and those are configurable too — `alt-project` calls them `depends_on`, `epic` and
`stories`.

**Requirements served**
R-15, R-18, R-20 (`docs/SCOPE.md`). Which further requirements apply depends on the shape chosen.

**Scope**
- In: selecting a subset of tasks by stored field value and by edge relationship; a machine-readable
  output form; the surface question above.
- Out: sorting, aggregation, counting, boolean expressions, saved queries — each is a step further
  into the thing non-goal 11 exists to prevent, and none is in the request.
- Out: how an agent is told to use it — [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md).

**Inputs**
`docs/SCOPE.md` §4 non-goal 11 and §1; `taskmd/schema.py` (`links`, `derived`, vocabularies);
`taskmd/cli.py` (`index_block` already filters and renders); T-002 §1 criterion 7.

**Acceptance criteria** — *provisional; they cannot be settled until the surface question is*
- [ ] Every filter value the tool accepts is drawn from the resolved schema, never from a built-in
      alias list — demonstrated against a project whose vocabulary shares no word with the default
- [ ] Filtering on a **derived** edge works (what blocks a task, the far end of a soft link), since
      that is the half grep cannot do and the reason the feature is not redundant
- [ ] The machine-readable form is stable enough to parse without knowing the terminal width
- [ ] An unknown filter value is an error naming what *is* accepted, reported before any output
- [ ] `docs/SCOPE.md` non-goal 11 and the chosen shape agree — whichever way that is resolved

**Open questions**
- **Which of the three shapes above, and does non-goal 11 change?** — maintainer. Everything else in
  this task depends on the answer, so `specify` cannot close without it.
- What does "machine-readable" mean here — one task per line with tab-separated fields, or JSON?
  JSON is stdlib and unambiguous; a line format is greppable and matches the tool's existing
  character. — maintainer, but only after the shape is decided.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Requested by the maintainer. Recorded with the non-goal 11 collision as its first open question rather than as a straightforward feature — two tasks have already been built on that non-goal, so reversing it is the owner's decision. The requested filter words were checked against the schema and are aliases, not vocabulary; noted so `specify` does not inherit them by default. |
