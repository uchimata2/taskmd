---
id: T-073
title: Correct the command surface local context still states
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-013, T-022]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-073 — Correct the command surface local context still states

## 1. Specify

**Outcome**
`control/LOCAL-CONTEXT.md` states the command surface taskmd actually has, and the gitignored file is
brought inside whatever sweep keeps the rest of the project's statements true.

**Why this one**
Raised as **F-13** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. The file closes with:

> Run the check in `CLAUDE.md` *Publishing constraints*. It is a grep, deliberately — `docs/SCOPE.md`
> non-goal 11 keeps the CLI to `context`, `index` and `check`, and says anything else is grep.

Non-goal 11 was **amended on 2026-08-05** by [T-022](T-022-filtered-task-listing-for-scripts.md):
`list` is the fourth command, and the non-goal now excludes a query language rather than everything
beyond three commands. The identical sentence was corrected in `CLAUDE.md` and `.handoff/config.md` at
the time; this copy was missed. It is the last place in the tree that still states the superseded
surface.

**Why the miss happened, which is the more useful half.** The file is gitignored, so it is outside
`git ls-files`, outside the pre-publish check by construction, and outside `.handoff/config.md`'s
`reconcile_targets` — which names `tasks/`, `docs/*.md`, `CLAUDE.md` and itself. Every mechanism this
project has for keeping statements true resolves against the tracked tree. A quarantined file is
quarantined from the sweeps too.

**Why it still costs something.** No publishing risk — that is what gitignoring it buys, and
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md) settled it. But the file's stated
job is resumption context, and it is read by a session that has not yet read anything else. A stale
claim there is read early and trusted.

**Requirements served**
R-1 (`docs/SCOPE.md`) — one home per fact, which a superseded copy defeats regardless of whether it is
tracked.

**Scope**
- In: the sentence quoted above.
- In: the rest of `control/LOCAL-CONTEXT.md`, checked once against the current tree rather than only
  this line — the same reasoning that made T-027's review find a second copy fifty lines from the one
  it was fixing.
- In: whether the file joins `reconcile_targets`, so this class stops recurring.
- Out: what the file records and why it is quarantined, settled in T-013.
- Out: the pre-publish check, which correctly does not read gitignored files.
- Out: the entry about the throwaway repository, which
  [T-037](T-037-delete-the-throwaway-proof-repository.md) removes at its own step 4.

**Inputs**
`control/LOCAL-CONTEXT.md`, `.handoff/config.md` (`reconcile_targets`),
[T-022](T-022-filtered-task-listing-for-scripts.md) for the amendment,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-13.

**Acceptance criteria**
- [ ] The file names the command surface taskmd has
- [ ] Every other statement in it is checked against the current tree, and the ones found true are
      recorded as checked
- [ ] Nothing recorded there moves into the tracked tree — the quarantine is the point
- [ ] Whether the file is swept in future is decided and written down, either way

**Open questions**
- **Does a gitignored file belong in `reconcile_targets`?** Adding it closes the class that produced
  this finding. Against it: `reconcile_targets` is resolved against the working tree at sweep time and
  its whole documented virtue is being a pattern rather than a list, so naming one specific
  gitignored file is the enumeration that entry warns against. A pattern that covers `control/`
  without naming the file may be the answer. `plan` decides.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the whole file against the current tree, not only the sentence the finding names | Every statement, judged |
| 2 | Correct the command surface, and say what the amendment did and did not carve out | `control/LOCAL-CONTEXT.md` |
| 3 | Decide the sweep question, and write the answer in **both** places a reader could look | `.handoff/config.md`, and the file itself |
| 4 | Confirm nothing recorded there has moved into the tracked tree | The pre-publish check, run last |

**Why step 1 reads the whole file.** The finding names one sentence. A file that has been outside
every sweep for its whole life is not likely to have exactly one stale statement in it, and this is
the only chance to find out cheaply.

## 3. Implement

**Decisions & assumptions**

- **D1 - `reconcile_targets` gains `control/`, the directory** - 2026-08-09. The open question set
  closing the class against the enumeration that entry explicitly warns about. Naming the folder is
  the resolution: it is a pattern, resolved against the working tree at sweep time like every other
  entry, so a second file appearing in `control/` is swept the day it lands and nobody edits a list.
  *Rejected: naming `control/LOCAL-CONTEXT.md`* - one specific gitignored file is precisely the
  hand-maintained membership the config's own note was written against.

  Recorded in both places on purpose, and it is not a second home: the config declares the sweep,
  and the file records that it *is* swept - which is the fact a reader of the file needs and cannot
  derive from inside it.

- **D2 - being swept does not make it publishable** - 2026-08-09. Stated in both edits, because the
  two properties are easy to conflate and the quarantine is the whole reason the file exists.
  Reconciling reads it; nothing about what may leave it changes.

### Step 1 - the whole file, judged against today's tree

| Statement | Verdict |
| :--- | :--- |
| `control/` is gitignored and the tracked tree names nothing in it | **checked, true** - `git check-ignore` confirms, and the pre-publish check is silent |
| The Notion-backed project row | **checked, unchanged** - a dated record of prior art read for T-007 and T-008 |
| The throwaway proof repository still exists | **checked, true** - and correctly still points at T-037 |
| The install-rehearsal repository | **added this session** by T-067, already current |
| The sibling plugin's negative finding | **checked, unchanged** - a dated observation from T-052 |
| *Why it is quarantined* and *Facts deliberately not recorded here* | **checked, true** - neither describes the tool |
| *Before publishing*: non-goal 11 keeps the CLI to `context`, `index` and `check` | **stale** - the finding's sentence, and the only one |

One stale statement in the file, which is the finding. Everything else survived, and is recorded as
checked rather than left ambiguous between *true* and *not looked at*.

### Step 2 - what the correction says

The sentence now names four commands and says what the 2026-08-05 amendment did: it carved out a
task listing, and the exclusion of everything else - **including a leak check** - survived it. That
second half is why the sentence is there at all; correcting only the count would have left a reader
wondering whether the grep is still the right instrument.

**Outputs produced**
- `control/LOCAL-CONTEXT.md` - the corrected sentence, and a new *Is this file swept?* section
- `.handoff/config.md` - `control/` in `reconcile_targets`, with the reason beside the existing note

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The file names the command surface taskmd has | met | Four commands, and what the amendment did not carve out |
| Every other statement in it is checked against the current tree, and the ones found true are recorded as checked | met | §3 step 1 - seven statements, one stale. The table is the record, so a later reader can tell *checked and true* from *not looked at* |
| Nothing recorded there moves into the tracked tree - the quarantine is the point | met | The pre-publish check run last over tracked and untracked-not-ignored files: silent. The two repository names stay behind their labels |
| Whether the file is swept in future is decided and written down, either way | met | Decided yes, by folder rather than by filename, and written in the config that declares the sweep **and** in the file itself - which is where a reader of the file will look |

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met. The whole file was read against today's tree, not just the sentence the finding named — seven statements, exactly one stale, and the six that survived are recorded **as checked**, so a later reader can tell *checked and true* from *not looked at*. The sweep question resolved by naming `control/` the **directory** in `reconcile_targets`: naming the file would have been the hand-maintained enumeration that entry was written to warn against, while the folder keeps the membership derived and picks up whatever lands there. Written in both the config that declares the sweep and the file itself, which is not a second home — the config declares it, the file records that it is subject to it, and a reader inside the file cannot derive that. |
| 2026-08-09 | → in_progress | Plan reads the whole file rather than the one sentence: a file that has been outside every sweep for its entire life is unlikely to hold exactly one stale statement, and this was the cheap moment to find out. |
| 2026-08-09 | → specified | Criteria stand as raised. |
| 2026-08-09 | → proposed | Raised as F-13 from the T-059 audit, clause 1. `low`/`xs` — no publishing risk, and the file is read early by a resuming session, which is what keeps it worth correcting. The transferable half is why it was missed: every mechanism this project has for keeping statements true resolves against the tracked tree, so a quarantined file is outside all of them. |
