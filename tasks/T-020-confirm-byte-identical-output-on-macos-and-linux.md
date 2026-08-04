---
id: T-020
title: Confirm byte-identical output on macOS and Linux
type: analysis
status: proposed
phase: specify
parent: T-002
blocked_by: []
related: [T-006]
work_package: none
owner: maintainer
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-020 — Confirm byte-identical output on macOS and Linux

## 1. Specify

**Outcome**
The same commands run on macOS and on Linux against the same tree, with the output compared byte
for byte against the Windows run — turning T-002's mechanism argument into a measurement.

**Why this one**
T-002's criterion reads *"output byte-identical across Windows, macOS and Linux"*. Only Windows was
available, so `implement` verified the **mechanism** instead: explicit `newline="\n"` on every
write, no `os.linesep`, separators normalised to `/` in printed output, asserted in
`tests/test_cli.py::WritesTheSameBytesEverywhere`. That is a good argument and it is not the
criterion. The plan recorded the gap as an assumption rather than letting the review tick a box the
evidence does not support.

This matters more than it looks. R-20 puts cross-platform identical behaviour in the goal, and
`docs/SCOPE.md` §9 puts it in the definition of done — so an untested claim here is a claim the
README will eventually make.

**Requirements served**
R-20 (`docs/SCOPE.md`).

**Scope**
- In: `context`, `index` and `check` on this repository and on `tests/fixtures/alt-project`.
- Out: making anything pass. If a difference appears, it is a finding and its own fix task — this
  task measures.

**Inputs**
A macOS or Linux machine with a Python 3 interpreter; this repository at a known commit.

**Acceptance criteria**
- [ ] The three commands run on at least one non-Windows platform, at a named commit
- [ ] `index` output compared byte for byte with the Windows run; any difference reported rather
      than normalised away
- [ ] Console output of `context` and `check` compared as bytes, not read and judged equivalent
- [ ] The result recorded either way — a confirmation is as much the outcome as a difference is
- [ ] T-002's recorded assumption is marked closed, or replaced by what was actually found

**Open questions**
- Which non-Windows platform is reachable, and is it both, or one? — maintainer. One closes most of
  the risk; the criterion names two.

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
| 2026-08-05 | → proposed | Raised by T-002's review. The criterion was not met as written and is carried here rather than reinterpreted as "the mechanism is right". |
