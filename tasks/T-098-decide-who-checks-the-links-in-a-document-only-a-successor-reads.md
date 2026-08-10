---
id: T-098
title: Decide who checks the links in a document only a successor reads
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-002, T-034, T-080, T-094, T-095]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-098 — Decide who checks the links in a document only a successor reads

## 1. Specify

**Outcome**
A project is told what validates the pointers in its machine-local working state — resumption notes,
scratch plans, anything gitignored that a *later session* reads — or is told plainly that nothing
does, so the gap is a decision rather than an accident.

**Why this one**
[T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) excluded gitignored
documents from `check` on the argument that a dead link inside something no reader can reach is a
promise to nobody. **That argument has a hole, and this repository walked straight into it within the
hour.** The live handoff is gitignored, so writing one on 2026-08-10 moved the skipped count from 31
to 32 and its ten links went unvalidated. They had to be resolved by hand.

**The walk that is now bypassed exists precisely for this document.** `markdown_files` walks
dot-directories rather than globbing, and both its docstring and `tests/fixtures/README.md` give the
same reason: `glob`'s `**` skips dot-directories, *"which is how a broken link in a live handoff
pointer stayed invisible"*. The fixture `broken-link` puts its defect in `.notes/` to pin that. So the
project paid for a deliberate walk to reach this exact case, and T-094 has now put the case back out
of reach for a different and individually sound reason.

**Two decisions, each defensible, that contradict on one document.** T-094's population is "whoever
clones the repository", and for a handoff that population is empty. The population that actually reads
a handoff is the next session, for whom the pointer is the whole artefact — a dead one there is not a
cosmetic defect, it is the resumption failing. Neither decision is wrong; nothing reconciles them.

**Requirements served**
R-16.

**Scope**
- In: whether `check` gains a way to validate documents it currently excludes, and what selects them
  — a flag, a config key naming paths to read regardless, or nothing.
- In: whether the answer is instead that this is not `check`'s job, in which case say whose it is.
  The handoff skill writes the document and could resolve its own pointers; that is a real answer and
  should be rejected explicitly rather than by omission.
- In: what happens to `broken-link` and the dot-directory rationale, which currently justify a walk
  by a case the tool no longer reaches. If the answer is "nothing does", that fixture's stated reason
  is stale and must be rewritten rather than left to read as coverage.
- Out: the document-side rule itself. T-094 decided it on evidence and this task does not reopen it;
  the question is what covers what it excluded.
- Out: the target side, which is [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md).

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `markdown_files` and `check_links` — the docstring of the
  first states the reason the second now bypasses.
- `tests/fixtures/README.md`, the `broken-link` paragraph.
- [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) §3, for the argument this
  finds the boundary of.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, whichever way it goes
- [ ] If something covers the excluded documents: a fixture holds a dead link in a gitignored
      document and it is reported, shown failing first
- [ ] If nothing does: `broken-link`'s stated reason and `markdown_files`' docstring no longer claim
      a case the tool does not reach, and the adopter-facing text says what is unvalidated
- [ ] Whichever way it goes, a run still reports what it did **not** examine

**Open questions**
- **Whose job it is.** The maintainer's. Note the shape of the trap before answering: the cheap
  reading is "add `--all` and move on", but a flag nobody remembers to pass is the same silence with
  a feature attached — which is the failure mode T-095 and T-080 were both raised for.

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
| 2026-08-10 | → proposed | Found by writing a handoff an hour after closing T-094: the skipped count went 31 to 32 and the document that disappeared was the one whose invisibility had justified walking dot-directories in the first place. Not found by review, and not findable by one — `check` exits 0 either way, which is the whole point. `high` because the project has now twice paid for a check that read fewer files than anyone believed (T-034, T-080) and this is the same shape arriving through a change made deliberately; `s` because the mechanism is a line, and only the rule is hard. |
