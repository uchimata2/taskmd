---
id: T-084
title: Correct the generated index preamble after the directory move
type: fix
status: done
phase: review
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
- ~~Whether the preamble should name commands at all.~~ — **answered here, 2026-08-09**, under the
  standing authorization to decide at this level, and flagged to the maintainer rather than buried:
  **it keeps exactly one command, the one that regenerates this file, and points at
  [`README.md`](../README.md) for the rest.** Three commands here were a second home for what the
  root README and `SKILL.md` both say, and that copy is what went stale; one command is not a copy of
  anything, because it is the instruction the *"do not hand-edit"* sentence directly implies and it is
  about this file rather than about the tool.

  *Rejected: keeping all three*, which restores the duplication that caused this task. *Rejected:
  naming none and pointing only*, which reads well against the design rule and takes away the one
  thing a reader of a generated file needs to be told, and which would also make criterion 1 vacuous
  by leaving nothing to run.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Rewrite the preamble to the answer above: one command, a pointer to the README, the *do not hand-edit* sentence and the existing document links unchanged. | The new preamble |
| 2 | Run the command it names, and diff the file against its previous state. | The transcript, and a diff whose only changes are in the preamble |
| 3 | Sweep the tree for pre-move paths, reporting the number of files read as well as the hits. | The count and the residue, in §3 |
| 4 | `check`, `index` and the suite. | The outputs |

**Step 2 is a diff rather than an eyeball.** The claim in criterion 3 is that regeneration leaves the
generated region alone while the preamble changes, and the only way to see both halves at once is to
look at what actually changed in the file.

**Not in this plan, deliberately:** teaching `check` to notice a stale preamble. Prose is not
validated here, and [T-025](T-025-let-check-notice-a-stale-generated-index.md) is about the other
half of this file.

## 3. Implement

Worked in plan order.

### Step 1 — the preamble

Before, the three lines that named a launcher deleted on 2026-08-09; after, one command and a
pointer:

```
./plugin/bin/taskmd index          # regenerate this file
```

`context` and `check` are no longer named here. They are in [`README.md`](../README.md), which is
where someone learning the tool is, and in `SKILL.md`, which is where the agent is.

### Step 2 — the command runs, and the generated region is untouched

```
./plugin/bin/taskmd index     Wrote tasks/README.md - 19 active, 65 closed     exit 0

git diff --stat tasks/README.md     1 file changed, 4 insertions(+), 5 deletions(-)
```

Every changed line is above the marker. The generated region came back byte-identical, which is what
`cmd_index` promises by replacing only what lies between the markers, and is the half of criterion 3
that could only be seen by regenerating after the edit rather than before it.

### Step 3 — the residue, and an instrument that lied first

```
files read                                          166
files naming a pre-move path                         28
of those, not a task record                           0
of those, an open task                       T-084 only
```

T-084 is this file, quoting the three lines it removed, which is the case criterion 2 was written to
allow. The other 27 are the closed records T-083 left as written.

**The first run of this sweep reported zero open tasks, and it was wrong.** It reduced a filename to
its id with `s#-.*##`, which cuts at the *first* hyphen and turns every `T-084-correct-…` into `T`,
so the comparison against the open list had nothing to compare and printed the clean answer. Recorded
because it is the same failure this task exists for: an instrument narrower than the thing it
measures, silent about the difference, and indistinguishable from success.

### Step 4 — nothing else moved

```
./plugin/bin/taskmd check     OK - 84 task(s), vocabulary valid, references resolve, no broken links
./plugin/bin/taskmd index     Wrote tasks/README.md - 19 active, 65 closed
python -m pytest tests/ -q    129 passed, 4 subtests passed
```

**Decisions & assumptions**

- **One command, not three and not none** — the §1 answer, with its rejections. Taken here rather
  than referred up because it repairs a duplication rather than changing what the backlog's front
  page is for, and it is reported to the maintainer in the same turn so reversing it costs one
  sentence. — 2026-08-09
- **The pointer goes to the root README rather than to `SKILL.md`** — a human opening the backlog is
  the reader being served, and `SKILL.md` is written for the agent and ships inside the plugin.
  — 2026-08-09

**Outputs produced**
- [`tasks/README.md`](README.md) — the preamble

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every command in the preamble runs, shown by running it rather than by reading the path | met | §3 step 2. One command now, and it is the one this repository types since T-083 |
| A grep for pre-move paths returns nothing but closed task records and this file's own quotation of them, with the file count it read printed | met | §3 step 3: 166 files read, 28 files hit, and the only open one is this task. The count is the evidence that the sweep read the tree rather than a corner of it, and the first run of that sweep was silently broken, which is written up rather than quietly re-run |
| `check` and `index` are clean afterwards, and the generated region is unchanged by the edit | met | §3 steps 2 and 4. The diff is four insertions and six deletions, all above the marker |

**What this task does not fix.** Nothing stops the preamble going stale again: it is prose in a file
the tool only half-writes, and no validator here reads prose for truth. What changed is the size of
the target, from three copied facts to one instruction about the file itself.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Three criteria met, on the maintainer's instruction to deliver the whole lifecycle. The preamble now names one command instead of three: the one that regenerates the file it sits in, which is what the *do not hand-edit* sentence implies and is not a copy of anything, with the rest pointed at the root README. That answered the specify question at this level rather than referring it up, with both rejections written down and the answer reported in the same turn. The edit is four insertions and five deletions, all above the marker, and regenerating afterwards returned the generated region byte-identical, which is the only way to see both halves of criterion 3 at once. One thing is recorded rather than quietly re-run: the residue sweep's first pass reported no open task still naming the old paths, because it cut filenames at the first hyphen and compared `T` against the open list. The corrected sweep reads 166 files, finds 28, and the only open one is this task quoting what it removed. |
| 2026-08-09 | → planned | Four steps, and the specify question answered first because steps 1 and 2 both depend on it. The diff in step 2 is deliberate: the claim is that the preamble changed while the generated region did not, and only a diff shows both. Teaching `check` to notice a stale preamble is out, because no validator here reads prose for truth. |
| 2026-08-09 | → proposed | Raised from [T-006](T-006-package-document-and-publish.md) step 5, which found it by grepping for pre-move paths in living documents. Not folded into that task: T-006 owns the root README and its plan says reconciling other documents is closing work rather than a step, and not fixed in passing either, because T-083's residue arithmetic reported zero for this class and a silent correction would leave that number looking right. `xs` and `medium`: three lines, and they are the first commands a reader of the backlog is told to run. |
