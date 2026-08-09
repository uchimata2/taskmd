---
id: T-084
title: Correct the generated index preamble after the directory move
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-083, T-006, T-025]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: [tasks/README.md]
---

# T-084 — Correct the generated index preamble after the directory move

## 1. Specify

**Outcome**
`tasks/README.md`'s hand-written preamble names commands that exist, so the first thing a reader of
this repository's backlog is told to run is not a path that was deleted on 2026-08-09.

**Why this one**
Three lines, in the only part of the index that is not generated:

```
./plugin/taskmd.sh index          # regenerate this file
./plugin/taskmd.sh context T-001  # everything needed to start a task
./plugin/taskmd.sh check          # validate
```

[T-083](T-083-make-the-skill-directory-self-contained.md) moved that launcher to
`plugin/skills/taskmd/taskmd.sh` and made `./plugin/bin/taskmd` the command this repository types.
`cmd_index` replaces only the text between its markers and leaves every byte outside them in place,
so regenerating the index does not touch these lines and never will.

**Why T-083 missed it, which is the part worth keeping.** Its step 6 reconciled the residue and
reported `of those, outside tasks/ 0`. The instrument treated everything under `tasks/` as a closed
record, on the rule that a closed task says what was true when it was written. `tasks/README.md` is
not a task record at all: it is a living document that happens to live in that folder, and it is the
one file in there that describes the tree as it is now. So the exemption that protects the audit
trail also hid the one file in `tasks/` the maintainer's rule was meant to correct.

Found on 2026-08-09 while working [T-006](T-006-package-document-and-publish.md) step 5, by grepping
the tree for pre-move paths outside closed task records. One file, three lines, and nothing else in
the tree still names the old paths.

**Requirements served**
R-23 is not the one at issue: no path here is personal or machine-specific. This serves
`docs/SCOPE.md` §1 *No install* as it reaches a reader, and R-12 in its neighbourhood: the generated
half of that file cannot drift, and this task is about the half that can.

**Scope**
- In: the preamble of `tasks/README.md`, above the generated marker.
- In: whether the same class exists anywhere else, answered by a grep rather than by assertion.
- Out: what the tool writes between the markers, which is generated and correct.
- Out: [T-025](T-025-let-check-notice-a-stale-generated-index.md), which is about the generated
  region going stale. This is the opposite half of the same file and does not wait on it.
- Out: making `check` notice a stale preamble. A hand-written region is prose, and no validator here
  reads prose for truth.

**Inputs**
- `tasks/README.md` lines 5 to 9.
- [T-083](T-083-make-the-skill-directory-self-contained.md) §3 steps 5 and 6, for the rule that was
  applied and the arithmetic that reported zero.
- `plugin/skills/taskmd/taskmd/cli.py`, `cmd_index`, for why regeneration will not fix it.

**Acceptance criteria**
- [ ] Every command in the preamble runs, shown by running it rather than by reading the path
- [ ] A grep for pre-move paths returns nothing but closed task records and this file's own quotation
      of them, with the file count it read printed. **The quotation above is why the criterion reads
      that way**: writing up a stale path re-creates the string the sweep looks for, so a criterion
      demanding silence would be one this task can never meet
- [ ] `check` and `index` are clean afterwards, and the generated region is unchanged by the edit

**Open questions**
- **Whether the preamble should name commands at all.** It is a second home for what `SKILL.md` and
  the README already say, and this is the second time it has gone stale independently of them. The
  alternative is a pointer, which costs a reader one hop and cannot rot. The maintainer's, because
  it changes what the backlog's front page is for rather than repairing it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `tasks/README.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised from [T-006](T-006-package-document-and-publish.md) step 5, which found it by grepping for pre-move paths in living documents. Not folded into that task: T-006 owns the root README and its plan says reconciling other documents is closing work rather than a step, and not fixed in passing either, because T-083's residue arithmetic reported zero for this class and a silent correction would leave that number looking right. `xs` and `medium`: three lines, and they are the first commands a reader of the backlog is told to run. |
