---
id: T-121
title: Report a second index of the same tasks sitting outside the generated markers
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-025, T-101, T-107]
work_package: v0.3
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-121 — Report a second index of the same tasks sitting outside the generated markers

## 1. Specify

**Where this came from.** The first adopting project's second written report, 2026-08-11 — its R-8,
and the only item in that report. Copied to `control/` beside the first one. Every earlier
recommendation from that project is closed (T-099 to T-105, plus T-106 and T-107 which they raised
indirectly), so this is the whole of the outstanding adopter feedback.

**What happened there.** The project migrated onto taskmd and kept its own pre-migration index
generator running for a while. Both wrote to the same file. The result was `tasks/README.md` holding
taskmd's generated block between taskmd's markers **and a second complete table of the same 56 task
ids outside them**.

`check` was silent. It ran twice over that state and reported `OK` both times, because it owns the
text between its own markers and reads everything else in the file as prose. The only number that
moved was a link count two screens up in the output, which nobody reads as a signal. The duplicate
was found by a person noticing the file had grown, not by any tool.

**Why it is taskmd's to report and not only theirs to avoid.** Two tools that can write one file are
invisible to *both*: neither validator can see a block it does not own, and a second generated copy
of the same facts therefore passes every check either tool runs. Nothing warns an adopter that this
is the shape of the risk, and migrating onto taskmd is exactly the moment it arises — an adopting
project has an old generator by definition. The information needed to spot it is already parsed:
`check` knows every task id, and it knows where its own markers are.

**Outcome.** `check` emits one advisory line when a file carries a table of ids taskmd already knows,
outside taskmd's markers — naming the file and the count, so the adopter can decide whether it is a
duplicate index or a legitimate quotation of their own backlog.

```
DUPLICATE INDEX  tasks/README.md: a second table of 56 known task ids sits outside the taskmd markers
```

**Scope**

- In: the advisory line, its threshold, and a fixture proving it fires and proving it stays quiet.
- Out: doing anything about the duplicate. Deleting one of the two writers is the project's call —
  in the reporting project it was the old generator, and removing it was their own task.
- Out: any change to exit status or to the problem count. See the criterion below.

**Inputs**
- `control/adopter-report-2026-08-11.md` — R-8, the source, with the evidence as they recorded it.
- The `CONFIG DRIFT` line shipped for T-100, which is the precedent this follows in every respect.

**Acceptance criteria**
- [ ] `check` prints one line per affected file, naming the file and how many known ids sit outside
      the markers.
- [ ] **It is advisory: the exit status does not move and the count of problems does not change.** A
      project may legitimately quote its own task table in a document, and a validator that failed on
      a legal state is one a project starts passing flags to — the reasoning `CONFIG DRIFT` already
      settled.
- [ ] It rests only on what `check` already parses — the known id set and its own marker positions.
      No new file format is read and no configuration key is added.
- [ ] A fixture with a duplicate block **fails to be silent**, and a fixture without one stays
      silent. A clean-tree pass proves nothing on its own.

**Open questions**
- **What counts as "a table of known ids"?** A threshold of one id would fire on any task file that
  links to another. The reporting project's case had 56. A count-based rule needs a number and a
  rationale, and the honest options are *most of the known set* or *more than N* — maintainer to
  decide, and it is the only real design question here.
- **Which files are examined?** Everything `check` already reads, or only files inside `tasks_dir`?
  The observed case was `tasks/README.md`, which is the file most likely to carry a copy and least
  likely to be read closely.

## 2. Plan

_Not planned._

## 3. Implement

_Not started._

## 4. Review

_Not started._

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → proposed | Raised from the first adopting project's second report, delivered 2026-08-11 and carrying one item. **Checked against this repository before filing**: `DUPLICATE INDEX` appears nowhere in the tree, and no existing task covers it — so unlike two items in their first report, this one does not arrive already answered. The reporting project has already deleted its own second writer, so nothing here is holding them up; what they are asking for is that the next adopter not have to notice it by eye. |
