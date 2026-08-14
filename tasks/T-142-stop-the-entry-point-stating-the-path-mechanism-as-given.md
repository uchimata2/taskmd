---
id: T-142
title: Stop the entry point stating the PATH mechanism as given
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-054, T-085, T-099]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-142 — Stop the entry point stating the PATH mechanism as given

## 1. Specify

**Outcome**
`plugin/bin/taskmd` describes how it is reached in terms that are true on the machines where it is
not reached, so the file an adopter opens when the command is missing does not tell them the command
cannot be missing.

**Why this one**
Raised from the htmldeck adopter report, row `O-T2` — the corrected row, whose remaining clause is
this and nothing larger. The comment at the top of the launcher reads, in substance, that the file is
on `PATH` because the harness appends every enabled plugin's `bin/` to the `PATH` it hands the
agent's shell, so there is no install step, no `PYTHONPATH` to set and no path to a cache directory
anyone has to know.

Every clause of that is true of the design and false on at least one real machine, including the one
this project is written on. [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3
step 2 measured why: the harness does write the directory into the shell snapshot, and the snapshot's
`export PATH=` line is truncated mid-value, so sourcing fails and the inherited `PATH` survives. The
defect is the harness's and is filed against the harness. What is left here is that a shipped file
states the mechanism as a guarantee.

**Why the comment rather than the behaviour.** [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md)
already gave the adopter the second way in, and it ships: `SKILL.md` names the condition and the
launcher beside it, and `adopt.md` points at that rather than carrying a copy. So the documentation an
adopter reads is correct, and the file they open when it fails is the one that is not. The two are a
few directories apart and disagree.

**The cost is a real one and it has been paid.** The reporting project wrote its own locator rather
than using the shipped fallback, and that locator globs the version directory and **sorts it as
text** — which selects `0.5.0` over `0.10.0` at the next minor bump. That specific bug is theirs, and
the general point is not: an adopter who believes the mechanism is unconditional, then finds it
failing, re-derives a locator instead of looking for a documented fallback.

**Requirements served**
R-18 (`docs/SCOPE.md`) — auto-discovery so a clone runs unedited — in the sense T-099 left it: the
promise holds, and the file explaining it does not say what happens when the machine breaks it.

**Scope**
- In: the comment at the top of `plugin/bin/taskmd`, and whether `plugin/bin/taskmd.cmd` says
  anything with the same problem.
- In: whether the file points at the fallback, given that the fallback's one home is `SKILL.md` and
  this project does not keep two copies of a fact.
- Out: the fallback itself, which T-099 settled and shipped.
- Out: fixing the harness, which T-054 settled is not taskmd's.
- Out: adding any detection or automatic re-route. T-099 decided the reader switches, not the tool.

**Inputs**
- `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd`.
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 2 — the mechanism
  and the truncation.
- [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) — the fallback, and D1 on
  why it names the launcher beside `SKILL.md` rather than this file.

**Acceptance criteria**
- [ ] The comment no longer states as unconditional a mechanism known to fail, and says what the
      reader does when it has
- [ ] It does not become a second copy of the fallback — the one home stays `SKILL.md`
- [ ] Both entry points are checked, not only the one the report named
- [ ] The launcher still runs unchanged from both shells, shown rather than assumed
- [ ] `check` and the suite are green, and no path from any machine appears in the file

**Open questions**
- **Can a shipped file point at `SKILL.md` at all?** [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)
  and [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) bound what a file inside
  the plugin may cite, and `bin/` sits outside the copyable skill folder that
  [T-083](T-083-make-the-skill-directory-self-contained.md) made self-contained — so a relative
  pointer from here resolves in one shipped shape and not the other. The answer may be that the
  comment states the condition and names no path at all. Decide at `specify`.

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
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T2`, which is the row the reporter corrected: it originally pointed at T-085 and would have sent this project hunting a packaging defect that does not exist. The correction is right — the launcher runs, the harness does emit the directory, and the truncation is upstream — and what survives it is small and real. `medium` because the fallback already ships, so nobody is blocked; the file is simply wrong where a reader meets it at the worst moment. `xs` because it is a comment. Two facts recorded here rather than left for `specify`: the report's version-sorting locator bug is the reporting project's, not a defect to copy, and the open question below may end with the comment naming no path. |
