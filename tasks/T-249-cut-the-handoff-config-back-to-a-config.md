---
id: T-249
title: Cut the handoff config back to a config, and rehome what only it records
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-073, T-135, T-190, T-047]
work_package: M7
owner: the project owner
business_value: high
effort: m
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-249 — Cut the handoff config back to a config, and rehome what only it records

## 1. Specify

**Outcome**
[`.handoff/config.md`](../.handoff/config.md) carries the handoff skill's keys and the guidance that
explains them, and nothing else. Every fact now sitting in its `## Notes for whoever resumes` section
is either **deleted** because it already has a home, or **moved** to the home it should have had. What
stays is rephrased as configuration rather than as narrative.

**Why this one**

**Measured 2026-08-23.** The file is 16,159 bytes. The keys and their guidance are **3,128** of them;
`## Notes for whoever resumes` is the other **13,031 — 81% of a config file**.

**It is not the skill asking for this.** The handoff skill's schema is its own `config.example.md`: core keys, tracker keys,
and the instruction *keep the `key: value` shape simple*. Grepping the whole skill for a notes or narrative
section returns nothing — no flow, no binding and no core section invites one. The section is this
project's own accretion, so it is this project's to remove.

**Three things are wrong with it, and only the first is size.**

1. **It is a second home for facts that have one.** The tier structure, *read `docs/SCOPE.md` first*,
   `reference/` being prior art, the publishing constraints, and the cross-repository *send a branch,
   not a report* policy are all stated in `../CLAUDE.md` or in the owner's global instructions, which
   are loaded on **every turn**. The config's copies are read only by a handoff run, so a session can
   act on the stale copy while the authoritative one sits in its context.
2. **It goes stale silently, and already has.** Line 74 states *what is left is grouped into `M6`
   alone*. Four open tasks carry `M7`, and the word `M7` does not appear in the file. Nothing reads
   the file between handoff runs, so nothing could have caught it — this is the failure the file's own
   `reconcile_targets` note warns about, occurring inside the file that carries the warning.
3. **It carries derived values as values.** Counts of adopters, release numbers and dates are written
   as prose, in a file whose own text says *do not carry either number around in prose*.

**Two blocks have no other home, and must be moved rather than deleted.** Both were checked by
grepping `tasks/`, `docs/`, `CLAUDE.md` and `control/` for their distinctive phrasing, and neither
appears anywhere else:

| Block | What it is |
| :--- | :--- |
| The four rules for reading an adopter report | Verify against this repository first; resolve every id cited; ask whether a defect in the reporter's own code is still there; test the reasons, not only the asks |
| The version-bump policy | Why a bump exists at all, and the owner's 2026-08-10 confirmation that one bump covers a batch rather than a single fix |

**Scope**
- In: `## Notes for whoever resumes`, block by block — classify each as *delete* or *move*, and act
- In: rephrasing whatever stays so it reads as configuration, and correcting the `M6` line
- In: the two homeless blocks above, which get a home in this repository
- Out: **the handoff skill itself.** Its schema is right and this record does not change it
- Out: the keys section (lines 1 to 49). Its inline notes explain *why a key is shaped as it is*,
  which is what config guidance is for, and they are not the defect
- Out: **losing the provenance deliberately.** The owner has already accepted that a shorter record
  may not name where each fact came from; where a task record already holds the provenance, the
  moved text points at it rather than restating it

**Inputs**
- [`.handoff/config.md`](../.handoff/config.md) — the file, and its own `reconcile_targets` note,
  which is the argument this record extends
- the handoff skill's own `config.example.md` — the schema this file should match. It is
  installed per machine and lives outside this repository, so it is named and not linked
- [`../CLAUDE.md`](../CLAUDE.md) and [`docs/BRIEF.md`](../docs/BRIEF.md) §*Carried lessons* — the two
  homes most of the notes duplicate or belong in
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) — the natural home for a release policy

**Acceptance criteria**
- [ ] `## Notes for whoever resumes` is gone, and every block in it was either deleted or moved —
      shown as a block-by-block table in `implement`, so a reader can check that none was dropped
- [ ] Each of the two homeless blocks resolves to a named file and section, and the text there is
      reachable without the config
- [ ] No statement in the file is false. In particular the `M6` line is corrected or removed, and no
      count, release number or roster size is written as prose
- [ ] The file matches the skill's schema: keys, tracker keys, and guidance about keys
- [ ] `taskmd check` passes and every link in the moved text resolves — this file is **tracked**, so
      `check` does read it, unlike the live handoff

**Open questions**
- **Where do the two homeless blocks go?** — the project owner. The recommendation is
  **[`docs/BRIEF.md`](../docs/BRIEF.md) §*Carried lessons*** for the four adopter-report rules, since
  that section exists for exactly this and the rules are lessons rather than procedure; and
  **[`docs/PUBLISHING.md`](../docs/PUBLISHING.md)** for the bump policy, since it is a release rule and
  that document is where release rules live. *Against: the report rules are arguably method rather
  than lesson, which would put them in `plugin/skills/taskmd/docs/` — rejected in the recommendation
  because that subtree ships, and how this project reads its own adopters' reports is not something an
  adopter installs.*

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** no — `.handoff/config.md` is this repository's own handoff configuration. An
adopter installs `plugin/` and never receives it.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised on the owner's observation of 2026-08-23**, in these words: *"The Handoff config should be specific with the historical information, only the important information should be added. This is neither a log file, nor a task file, but a config."* They asked first whether the fault lies with the handoff skill or with this project, and it is this project's: grepping the whole skill for a notes or narrative section returns nothing, and its schema says to keep the shape simple. The owner also accepted in advance that a shorter record may lose the source of some information, which is why *Out* names that rather than treating it as a cost to avoid. |
