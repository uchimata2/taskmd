---
id: T-121
title: Report a second index of the same tasks sitting outside the generated markers
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-025, T-101, T-107]
work_package: v0.5
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
- None. Both answered by the maintainer on 2026-08-11.

  **Q1 — what counts as "a table of known ids"? — *most of the known set*.** The advisory fires when
  the known ids outside the markers are a majority of what taskmd knows. Chosen over *more than N*
  because N cannot be justified at two project sizes at once: a number that is quiet in a 500-task
  project fires on ordinary cross-linking in a 20-task one, and there is no basis for picking
  between them. A majority scales by construction and cannot be reached by a task file linking to
  its neighbours. The observed case was 56 of 56.

  **Q2 — which files are examined? — everything `check` already reads.** It costs nothing extra: the
  known id set and the marker positions are both already parsed, so the scan is over material the
  command has in hand. Narrowing to `tasks_dir` would be quieter and would miss a copy pasted into a
  document, which is the case an adopter is least likely to notice — the opposite of what the
  advisory is for.

  Neither answer changes the acceptance criteria; both were fork-free choices inside them. The
  fixture required by criterion 4 must now carry a *majority* duplicate to fire, and a file quoting a
  handful of ids is the case it must stay quiet on.

## 2. Plan

_Not planned._

## 3. Implement

_Not started._

## 4. Review

_Not started._

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → specified | Both open questions answered by the maintainer: a majority of the known set is the threshold, and the scan covers everything `check` already reads. No criterion amended — both were choices inside the criteria rather than forks between them. **Stays `v0.3` and is not started**: the standing authorization covers the current release only, and being fully specified is not a reason to reach past it. |
| 2026-08-11 | → proposed | Raised from the first adopting project's second report, delivered 2026-08-11 and carrying one item. **Checked against this repository before filing**: `DUPLICATE INDEX` appears nowhere in the tree, and no existing task covers it — so unlike two items in their first report, this one does not arrive already answered. The reporting project has already deleted its own second writer, so nothing here is holding them up; what they are asking for is that the next adopter not have to notice it by eye. |
