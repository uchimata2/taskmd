---
id: T-029
title: Reject unknown arguments on every command
type: fix
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-002, T-022]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-029 — Reject unknown arguments on every command

## 1. Specify

**Outcome**
An argument taskmd does not understand is an error naming what *is* accepted, on all four commands,
before anything is printed or written — instead of being discarded in silence by three of them.

**Why this one**
Raised as **F-3** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clause 3. `cmd_check`, `cmd_index` and `cmd_context` each take an `args` parameter and never read it
past the first element. Observed:

```
python -m taskmd check nonsense
OK - 26 task(s), vocabulary valid, references resolve, no broken links
exit=0

python -m taskmd index nonsense --wat
Wrote tasks/README.md - 12 active, 14 closed
exit=0

python -m taskmd context T-026 extra junk
(normal output for T-026)
```

The `index` case is the sharp one: a mistyped invocation **performed a write** and reported success,
so the user's evidence that their flag did something is the same output they would get if it had.

**`list` already does this correctly**, and does it well — `parse_filters` returns a message rather
than printing, every rejection happens before a line reaches stdout, and an unknown value names the
project's own vocabulary. That was built deliberately in
[T-022](T-022-filtered-task-listing-for-scripts.md). So this is one command's behaviour that three
commands did not get, not a design nobody has settled.

**Why it is clause 3 and not tidiness.** R-17 puts configuration errors at setup rather than
mid-run, on the reasoning that a validator which is believed must not report success over something
it never examined — the same reasoning [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md)
acted on. An ignored argument is that failure at the command layer.

**Requirements served**
R-17, R-18 (`docs/SCOPE.md`); §1 *Invisibility* — the tool should not need the user to notice.

**Scope**
- In: argument handling for `check`, `index` and `context`, and the no-command and unknown-command
  paths in `main`.
- In: whether `--help` / `-h` is answered at all. `python -m taskmd --help` currently prints the
  usage line and exits **2**, so the conventional way to ask what a tool does is reported as misuse —
  which matters more here than usual, since the intended caller is an agent probing the surface.
- Out: adding any new flag or command. `docs/SCOPE.md` non-goal 11 stands; this is about rejecting
  what is not there, not accepting more.
- Out: `list`, which already behaves correctly and is the model to follow.

**Inputs**
`taskmd/cli.py` (`main`, `cmd_check`, `cmd_index`, `cmd_context`, and `parse_filters` as the
pattern), `docs/SCOPE.md` R-17, [T-022](T-022-filtered-task-listing-for-scripts.md) §3 *Rejections
arrive before output*, [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-3.

**Acceptance criteria**
- [ ] Each of the four commands rejects an argument it does not understand, naming what it does
      accept, and exits non-zero
- [ ] **Nothing is printed and nothing is written before the rejection** — asserted for `index`
      specifically, whose current failure mode is a silent successful write
- [ ] Shown failing first on the three commands, per R-16 — a check that has only ever passed proves
      nothing, and this one is being added to code that currently accepts everything
- [ ] `list`'s existing behaviour and messages are unchanged, verified by the T-022 tests still
      passing untouched
- [ ] The rejection message is the same bytes on every platform (R-20) and contains no path

**Open questions**
- Should `--help` print per-command usage, or only the top-level line? The top-level line already
  exists; per-command help is a second surface to keep true, and `docs/SCOPE.md` §2 principle 3
  argues against restating what the config already documents. — maintainer. Affects the wording
  only, so it does not block this phase.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Raised as F-3 from the T-026 audit, clause 3. Reproduced on all three commands before being written up; the `index` case writes the index and exits 0 on a mistyped invocation. Not fixed where it was found (METHOD §5). |
