---
id: T-249
title: Cut the handoff config back to a config, and rehome what only it records
type: fix
status: done
phase: review
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
deliverables:
  - .handoff/config.md
  - CLAUDE.md
  - docs/BRIEF.md
  - docs/PUBLISHING.md
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

**The test, set by the owner on 2026-08-23.** Prose in a config or instruction file **stays** when
it is a general guide — what something means, how to use or update it. It **goes** when it is update
history or a log entry. So this is not *prose versus no prose*, which is what this record assumed
before the answer; the keys section is in scope after all, because its notes are guidance wrapped
around three dated incident reports.

**Scope**
- In: `## Notes for whoever resumes`, block by block — classify each as *delete* or *move*, and act
- In: the keys section, where a note recites how a key reached its current value
- In: the two homeless blocks above, which get a home in this repository
- In: recording the general rule durably, so keeping the policy does not depend on an audit
  re-finding this. The owner's answer of 2026-08-23: `../CLAUDE.md`
- Out: **the handoff skill itself.** Its schema is right and this record does not change it
- Out: **`.taskmd/config.md` and other instruction files.** The owner scoped this to the handoff
  config for now; the rule recorded above is what reaches the rest
- Out: **the 249 records already written.** New writing only — METHOD rule 5 forbids rewriting what
  a record says about the past
- Out: **losing the provenance.** Where a task already holds it, the surviving text cites the id
  rather than restating the story

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
- ~~**Where do the two homeless blocks go?**~~ **Decided at implement, 2026-08-23**, on the standing
  delegation, since the owner's answers covered the rule and the scope but not this: the four
  adopter-report rules to [`docs/BRIEF.md`](../docs/BRIEF.md), the bump policy to
  [`docs/PUBLISHING.md`](../docs/PUBLISHING.md). *Rejected: `plugin/skills/taskmd/docs/`* — that
  subtree ships, and how this project reads its own adopters' reports is not something an adopter
  installs.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Classify every block in the file against the owner's guide-or-history test | The table in §3 |
| 2 | Move the two blocks that have no other home | `docs/BRIEF.md`, `docs/PUBLISHING.md` §8 |
| 3 | Rewrite the file to keys plus guide-only notes | `.handoff/config.md` |
| 4 | Record the general rule where it binds before anyone announces they are writing prose | `CLAUDE.md` |
| 5 | Prove `check` reads this file, rather than assume it | A recorded failing run, in §3 |

## 3. Implement

**Every block, and where it went.** Sixteen blocks: two moved, fourteen deleted because the fact
already had a home. Listed so a reader can check that none was dropped without a decision.

| # | Block | Verdict | Its home |
| :-- | :--- | :---: | :--- |
| 1 | Published at GitHub; current release is `v0.6.0` | delete | `git tag` and the manifest; T-182, T-242 |
| 2 | Version bumps versus milestone labels | **move** | [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §8 |
| 3 | Milestone labels `M1`…`M6`, and what is left | delete | Each task's `work_package`; T-136. This is the block that had gone false |
| 4 | A release is not the last step of a release | delete | [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) |
| 5 | Start with `SCOPE.md`, then `BRIEF.md` | delete | `../CLAUDE.md` *Read in this order*; the `project_docs` key still names `SCOPE.md` |
| 6 | Adopters outside this repository, and the roster counts | delete | `control/LOCAL-CONTEXT.md`, which the block itself named as the home |
| 7 | The four rules for reading an adopter report | **move** | [`docs/BRIEF.md`](../docs/BRIEF.md) *Reading a report from outside* |
| 8 | Siblings send a branch, not a report | delete | The owner's global instructions, loaded every turn |
| 9 | The three tiers; T-053's boundary; T-083's self-containment | delete | `../CLAUDE.md` *Three tiers*; T-053, T-083 |
| 10 | The third overlap and T-190's ruling | delete | [T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md) |
| 11 | This project has its own `.taskmd/config.md` | delete | T-135, and the file itself |
| 12 | The schema question is answered; how to run the CLI | delete | `../CLAUDE.md` *Run the commands here as* |
| 13 | Walking up to find the project; the launchers; `after_write` | delete | `plugin/skills/taskmd/SKILL.md` |
| 14 | `BINDING.md` is the backend contract | delete | `SKILL.md`'s load-on-demand table |
| 15 | `reference/` is prior art, not the plugin | delete | `../CLAUDE.md` *What this is* |
| 16 | This repository will be published | delete | `../CLAUDE.md` *Publishing constraints* |

**The two keys notes were compressed, not kept and not cut.** Each was a rule wrapped around dated
incident reports. The rule is guidance and stays; the incidents are log entries and go, with the task
id and date left as the pointer — `reconcile_targets` keeps *patterns, never an enumeration, no depth
limit* and cites T-073; `tracker_lint` keeps *a lint that cannot start reads as a pass* and cites
T-005 and T-054.

**Decisions & assumptions**

- **The rule went to `CLAUDE.md`, not to `docs/`** — 2026-08-23, the owner's answer. It binds while
  editing any document, and nobody announces that they are about to write prose, which is the one
  exception `CLAUDE.md` itself names as earning always-loaded space. It cost **551 characters**:
  tier 1 was 6,451 and is 7,002 against a 7,854 bound, so headroom fell from 1,403 to 852.
- **This record is written to the rule it establishes.** The block table is a table rather than
  sixteen paragraphs, and each row cites a home rather than restating what is there.
- **A session cannot verify its own `CLAUDE.md` edit**, since the file is fixed before the first tool
  call. `tests/test_budget.py` measures its size, and nothing here measures whether a later session
  obeys it. Stated rather than claimed.

**Outputs produced**

- [`.handoff/config.md`](../.handoff/config.md) — **16,159 bytes to 1,845**, an 89% cut.
- [`CLAUDE.md`](../CLAUDE.md) — *Write the fact, not its history*.
- [`docs/BRIEF.md`](../docs/BRIEF.md) — *Reading a report from outside*, four rules as four rows.
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §8 — *When to spend a version bump*.

**Checked by using it.** `check` reads this file, shown by breaking it rather than by a clean pass:

```text
check with broken link exit=1
BROKEN LINK   .handoff/config.md -> ../docs/NO-SUCH-FILE.md
restored, check exit=0
```

`taskmd check` exits 0 and the suite is 350 passed, `tests/test_budget.py` included.

**One self-inflicted failure, kept because the blast radius is the lesson.** A `T-190` link in this
record was composed from a remembered title rather than resolved, and the file did not exist. That
one bad link took `check` to exit 1, and with it **eight tests**: the whole `ChecksThisRepository`
class, `CheckReportsWhatItExamined`, and a launcher test in `test_runtime.py` that runs `check` and
asserts exit 0. It read as unrelated flakiness until the launcher test was opened. Resolving the
filename with `ls` fixed all eight.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `## Notes for whoever resumes` is gone, and every block was deleted or moved, shown block by block | met | §3's table: 16 blocks, 2 moved, 14 deleted, each with the home that made deleting it safe |
| Each homeless block resolves to a named file and section, reachable without the config | met | `docs/BRIEF.md` *Reading a report from outside*; `docs/PUBLISHING.md` §8 |
| No statement in the file is false; no count or release number as prose | met | The `M6` block is gone rather than corrected — it was derived from `work_package` and had no business being written down. No count, roster size or release number survives |
| The file matches the skill's schema: keys, tracker keys, guidance about keys | met | Two key blocks and two guide notes. Nothing else |
| `taskmd check` passes and the moved text's links resolve | met | Exit 0, and `check` was shown to fail on a planted broken link in this exact file |

**Adopter-visible?** no — `.handoff/config.md` is this repository's own handoff configuration. An
adopter installs `plugin/` and never receives it.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | Landed. 16,159 bytes to 1,845. The one thing the survey did not settle — where the two homeless blocks go — was decided on the standing delegation and the rejection recorded in §1. |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record**, given 2026-08-23: *"Update T-249 accordingly, the you can work the full lifecycle, commit and push."* **Covers:** this record's `specify` through `review`, and committing and pushing. **Does not cover:** any other file or task, including `.taskmd/config.md`, which the same answer scoped out. |
| 2026-08-23 | (no change) | **Answered by the owner on 2026-08-23**, four questions in one survey. The test is *guide or changelog*, not *prose or none* — so the keys section came into scope and this record's original *Out* line for it was wrong. Scope stays the handoff config alone, with the general rule recorded in `CLAUDE.md` so the policy does not depend on an audit re-finding it. Existing records are untouched: new writing only. |
| 2026-08-23 | → proposed | **Raised on the owner's observation of 2026-08-23**, in these words: *"The Handoff config should be specific with the historical information, only the important information should be added. This is neither a log file, nor a task file, but a config."* They asked first whether the fault lies with the handoff skill or with this project, and it is this project's: grepping the whole skill for a notes or narrative section returns nothing, and its schema says to keep the shape simple. The owner also accepted in advance that a shorter record may lose the source of some information, which is why *Out* names that rather than treating it as a cost to avoid. |
