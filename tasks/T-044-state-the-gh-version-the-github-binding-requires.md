---
id: T-044
title: State the gh version the GitHub binding requires
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-010, T-042]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - plugin/docs/bindings/github-issues.md
---

# T-044 — State the gh version the GitHub binding requires

## 1. Specify

**Outcome**
An adopter can tell, before following the binding, whether the `gh` they have is new enough — and
the answer rests on something that was tried rather than on a number someone thought looked safe.

**Why this one**
`docs/bindings/github-issues.md` assumption 4 says what must be true of the *repository* — issues
enabled, sub-issues and dependencies available, a token with `repo` scope. It says nothing about the
CLI, and the binding leans on flags that are not old:

| Operation | Flag it depends on |
| :--- | :--- |
| create | `--parent`, `--blocked-by` |
| update | `--add-sub-issue`, `--add-blocked-by`, `--remove-parent` |
| update | `--template '{{.body}}'`, which T-042 made load-bearing for the byte-identical guarantee |
| read, enumerate | the `parent`, `subIssues`, `blockedBy`, `blocking` JSON fields |

Every one of those was exercised on exactly one version, `gh` 2.96.0, and the binding presents them
as simply available. An adopter on an older CLI does not get a clear refusal from the binding; they
get whatever `gh` says about an unrecognised flag, at the point where they are trying to follow a
document that told them this works. That is BINDING §4's "setup that is obvious to the binding's
author and invisible to everyone else", and it is R-17's failure shape too — a configuration problem
surfacing inside the work rather than before it.

**Scope**
- In: establishing a floor and writing it into the assumptions section, with what it was established
  against. Whether the floor is one version for the whole binding or differs per operation.
- Out: making anything work on older versions, and any fallback path for a CLI that lacks a flag.
  The binding states limits rather than working around them (BINDING §6.4); if an old CLI cannot do
  this, the honest answer is the floor.

**Inputs**
- `docs/bindings/github-issues.md` — assumption 4, and every command in *Operations*
- T-042 §3, which made `--template` load-bearing, and T-010 §3's capability table
- `gh`'s own release history, for when each flag landed

**Acceptance criteria**
- [ ] The binding states a `gh` version, in the assumptions section, phrased as something an adopter
      checks about their own machine
- [ ] The number is justified by evidence naming where each flag came from — not by the version that
      happened to be installed when the binding was written
- [ ] An adopter below the floor learns it from the binding rather than from a failed command,
      checked by reading the assumptions as someone on an old CLI would
- [ ] If the flags landed in different releases, the binding states the highest and says so, rather
      than listing a floor per operation that nobody will cross-reference mid-task

**Open questions**
- Is the floor discoverable without installing old versions? `gh`'s changelog should date each flag,
  which would settle it from evidence without a matrix of installs. If it will not, say so and state
  the floor as "verified at 2.96.0, earlier untested" — an honest bound beats a guessed one, and the
  criteria are written to accept that answer. — decide during the work.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Enumerate what the binding actually invokes — commands, flags, JSON fields — by reading the binding, not by recalling what was written. §1's table was assembled from memory and is the thing most likely to be wrong. | The real dependency list, in §3, with §1's errors named |
| 2 | Split it: the long-standing surface (`--json`, `--jq`, `--template`, `--state`, `--limit`, `--label`) against the recent one (sub-issues and dependencies). Dating all of it would be effort spent on flags that predate anything an adopter could plausibly have. | A short list of what actually needs dating |
| 3 | Date the recent ones against `gh`'s published release notes. | A release number per flag, each with its source |
| 4 | Decide the floor — the highest release found — or, if the notes will not settle it, the honest bound the open question already sanctions. | A decision in §3, with what it rests on |
| 5 | Write it into the assumptions section as a claim about the adopter's machine. | `docs/bindings/github-issues.md` |
| 6 | Check the new entry against the defect T-043 is open on: does it *ask the adopter something*, or describe the CLI? A seventh entry that fails the same way makes T-043 worse. | A verdict in §3 |

**Sequencing.** Step 1 leads because §1's dependency table is second-hand: it was written while
closing T-042, from what that task had just used, and a floor derived from the wrong flag list would
be a measured-looking number that measures nothing. Step 2 is a deliberate narrowing — the floor is
set by the newest dependency and nothing else, so dating the rest is waste. Step 6 is last and
checks this task's own output against another open task's finding, because the cheapest moment to
not add to a known pile is before the entry is written.

**Shape of the deliverable — decided.** The version goes into the existing assumption 4, which
already carries the repository-side prerequisites, rather than becoming a seventh numbered entry.
Two reasons: the adopter is answering one question — "can my setup run this?" — and splitting its
halves across two entries makes them checkable separately and forgettable together; and T-043 is
already open on the assumptions being too many things at once, so adding a seventh entry to fix a
gap would trade one defect for another. Rejected: a *Requirements* section above the assumptions,
which would be the second place an adopter has to look before starting.

**Output paths**
- `docs/bindings/github-issues.md` — assumption 4
- This task's §3 — the real dependency list, the dated flags, and the verdict on the new wording

## 3. Implement

**Step 1 — the real dependency list, and §1 was wrong.** Read out of the binding rather than
recalled:

| Surface | What the binding actually uses |
| :--- | :--- |
| commands | `gh issue view`, `list`, `create`, `edit`, `close`; `gh label create` in *Setup* |
| edge flags | `--parent`, `--remove-parent`, `--blocked-by`, `--add-blocked-by`, `--remove-blocked-by` |
| other flags | `--json`, `--jq`, `--template`, `--state`, `--limit`, `--search`, `--label`, `--add-label`, `--remove-label`, `--title`, `--body-file` |
| JSON fields | `parent`, `subIssues`, `blockedBy`, `blocking`, plus the ordinary ones |

**§1's table listed `--add-sub-issue`, which the binding does not use.** It sets hierarchy from the
child with `--parent`, never from the parent — which is the design rule showing up in the command
choice, since the child is the constrained end. The error came from assembling that table while
closing T-042, from flags that task had in view rather than from the document. Step 1 existed for
exactly this and it earned its place: a floor derived from a flag the binding never invokes would
have been a measured-looking number measuring nothing.

**Step 2 — only the edge flags and the four JSON fields need dating.** Everything in the third row
is long-standing `gh` surface, and no plausible adopter has a CLI old enough for `--json` or
`--label` to be the binding constraint. The floor is set by the newest dependency and nothing else.

**Step 3 — they all landed together, in `gh` 2.94.0.** That release added Issues 2.0 support to
`gh issue`: sub-issues (`--parent`, `--add-sub-issue`), dependencies (`--blocked-by`,
`--add-blocking`) and issue types. Sources: the [2.94.0 release
notes](https://github.com/cli/cli/releases/tag/v2.94.0) and the PR that implemented it,
[cli/cli#13057](https://github.com/cli/cli/pull/13057).

**Step 4 — the floor is 2.94.0, not the 2.96.0 that happened to be installed.** This is the
distinction the criteria were written around: 2.96.0 is where the binding was *exercised*, 2.94.0 is
where the capability *arrived*, and stating the former would have excluded adopters for no reason
while looking equally authoritative.

**Not asserted: Enterprise Server version numbers.** The release-notes fetch also reported that
sub-issues need GHES 3.17+ and relationships GHES 3.19+. That would have been worth having, and it
is not in the binding, because the same fetch dated 2.94.0 to 2024 — impossible, since the installed
2.96.0 is dated 2026-07-02 — and the GitHub Docs page on issue dependencies carries no version note
to corroborate it. One source that is demonstrably wrong about a neighbouring fact is not evidence.
The binding says Enterprise Server is untested instead, which is true and checkable; no task is
raised, because assumption 4's middle clause already asks the adopter whether the features are
available to them, and that question is server-agnostic and correct as it stands.

**Step 6 — the new entry passes the test T-043 is open on.** "Your `gh` is 2.94.0 or newer…" is
answerable by running one command and looking; contrast assumptions 1 and 2, which state facts about
GitHub and about this binding that no project could deny. Re-measured against T-040's budget after
the edit: **six claim lines, 77 words, ~18s** against 30 — the entry grew by 12 words and the section
still fits, which is why it went into assumption 4 rather than becoming a seventh.

**Decisions & assumptions**
- **The floor is one number for the whole binding.** — All the recent flags shipped in one release,
  so a per-operation table would have had one distinct value in it and given a reader something to
  cross-reference mid-task for no gain. — 2026-08-07
- **The version folds into assumption 4 rather than adding an entry.** — Decided at `plan` and it
  held under measurement: the adopter is answering one question, "can my setup run this?", and its
  three failure modes belong together. T-043 is already open on this section; fixing a gap by
  lengthening the list would have traded one defect for another. — 2026-08-07
- **What happens below the floor is stated, not just the floor.** — Criterion 3 asks that an adopter
  *learn* it from the binding. A bare version number is a fact you can skim past; "below it you get
  an unrecognised-flag error partway through an operation" is the reason to check. — 2026-08-07

**Outputs produced**
- [`docs/bindings/github-issues.md`](../plugin/docs/bindings/github-issues.md) — assumption 4

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The binding states a `gh` version, in the assumptions section, phrased as something an adopter checks about their own machine | met | Assumption 4 opens "Your `gh` is 2.94.0 or newer…" — answerable by running one command. Step 6 checked it against the defect T-043 is open on and it does not repeat it. |
| The number is justified by evidence naming where each flag came from, not by the version that happened to be installed | met | 2.94.0, from the cli/cli release notes and the implementing PR, both linked in §3. The installed version was 2.96.0, and §3 states the distinction explicitly so the next reader does not re-derive it. |
| An adopter below the floor learns it from the binding rather than from a failed command | met | The entry says what going below it costs — an unrecognised-flag error partway through an operation — rather than only naming the number. Read back as someone on an old CLI: the first bold clause is the answer, before any command is run. |
| If the flags landed in different releases, the binding states the highest and says so | met | The condition did not arise — all of them shipped in 2.94.0 together. The substance behind the criterion is honoured anyway: the entry says that release is the floor for the whole binding and that every other flag used is older, so nothing is left for a reader to cross-reference. |

Four met, none carried. The task's own §1 turned out to contain the error step 1 was written to
catch, which is the useful part of having put verification before the work rather than after.

**Child fix tasks raised**
- none. The Enterprise Server question is answered in the binding — untested, and assumption 4
  already asks the adopter whether the features are available to them — rather than deferred.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | All four criteria met. The floor is `gh` **2.94.0** — where the sub-issue and dependency flags arrived — not the 2.96.0 that happened to be installed, which is the distinction the criteria were built around. Step 1 caught this task's own §1 claiming a dependency on `--add-sub-issue`, which the binding never uses: it sets hierarchy from the child with `--parent`, the constrained end, so the design rule shows up in the command choice. GHES version numbers surfaced but are not asserted — the source that gave them dated 2.94.0 to 2024, which the installed 2.96.0 disproves, and GitHub Docs did not corroborate; the binding says Enterprise Server is untested instead. Folded into assumption 4 rather than adding a seventh entry, and re-measured at 77 words / ~18s against T-040's 30-second budget. |
| 2026-08-07 | → planned | Six steps. `specify` was at `proposed` — the criteria were written when T-042 raised this and never separately agreed; the instruction to plan is taken as that agreement, as it was for T-042, and recorded rather than skipped. Step 1 exists because §1's dependency table was assembled from memory while closing T-042 and already has at least one error, and a floor derived from the wrong flags would look measured while measuring nothing. Step 6 checks the output against T-043's open finding, so this task does not add a seventh unanswerable assumption while fixing a gap. |
| 2026-08-07 | → proposed | Raised by T-042's last plan step, which asked only whether the fix added a tool. It did not — but answering that exposed that the binding has never named a version for the tool it already required. Kept out of T-042, whose scope is the `update` operation, while this concerns every operation and the assumptions section. |
