---
id: T-094
title: Make check answer the question a fresh clone would ask
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-013, T-034, T-092, T-095]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-094 — Make check answer the question a fresh clone would ask

## 1. Specify

**Outcome**
`check` states which question it is answering about a broken link — *"is this file here?"* or
*"would someone who cloned this repository find it?"* — and behaves consistently with the answer, so
a project that keeps machine-local documents is not given failures it cannot fix.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`), and reproduced here on a
throwaway project: a `.gitignore` containing `private/`, and a gitignored document holding a dead
link, produces

```
BROKEN LINK   private/notes.md -> ../nope.md

1 problem(s) over 1 task(s)
```

`markdown_files` walks everything except `SKIP_DIRS` — `.git`, `node_modules`, `__pycache__`,
`.venv` — and nested projects. `.gitignore` is not consulted on either side: not for the documents
scanned, and not for the targets a link points at.

**This repository is exposed to it and has not noticed.** `control/` is gitignored and holds
`LOCAL-CONTEXT.md`, which is prose full of references; a live `.handoff/HANDOFF.md` is resumption
state. Neither is in a clone. A dead link inside either is not a broken promise to any reader,
because no reader can reach the document making it.

**The inconsistency is inside this project's own tooling.** `CLAUDE.md`'s pre-publish check is built
on `git ls-files --cached --others --exclude-standard` **precisely** so it sees what a push would
send — that flag combination is argued for at length there, and
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) exists because getting it wrong
was silent. `check` answers a different question from the leak check standing next to it, and nothing
says which is intended.

**Requirements served**
R-16. R-23, since the quarantine of local-only material is the reason gitignored documents exist here
at all.

**Scope**
- In: whether `check` consults `.gitignore`, on the document side, the target side, or both.
- In: what it prints about what it skipped — a count at minimum, so the exclusion cannot quietly
  grow. That is [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)'s argument
  arriving here first.
- In: what a project with no git at all gets. One of the projects onboarded on 2026-08-09 has no
  version control, so "consult `.gitignore`" must degrade to something rather than fail.
- Out: the pre-publish leak check, which already answers this correctly and is not taskmd's code.
- Out: `SKIP_DIRS`, which is a different mechanism and is not at issue.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `markdown_files` and `check_links`.
- `CLAUDE.md` *The pre-publish check*, for the argument about what `git ls-files` with those three
  flags buys and why the shorter form was rejected.
- [T-013](T-013-quarantine-local-only-information-behind-gitignore.md), for why local-only material is
  quarantined rather than deleted.

**Acceptance criteria**
- [ ] The question `check` answers is written down in one place, and the behaviour matches it
- [ ] A fixture with a gitignored document holding a dead link behaves as decided, shown by running
      it both ways
- [ ] A project with no `.git` still works, shown on a fixture rather than reasoned about
- [ ] Whatever is skipped is counted in the output

**Open questions**
- **Which question is the right one.** "Would a clone find it?" matches the leak check and matches
  what a published repository promises. "Is it here?" is what a working session wants while the file
  is still local. They differ exactly on the material this project deliberately quarantines. The
  maintainer's.

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
| 2026-08-09 | → proposed | Raised from the deck-building sibling's migration report and reproduced here in a throwaway project. `high` and `s`: the fix is small and the argument is already written down in this repository for a different check — the pre-publish grep is built on `git ls-files --cached --others --exclude-standard` so that it sees exactly what a push would send, while `check` standing next to it walks everything. Two checks in one project answering different questions about the same tree, with neither saying which. |
