---
id: T-231
title: Cut the next release
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-182, T-085, T-135, T-223]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/.claude-plugin/plugin.json
---

# T-231 — Cut the next release

## 1. Specify

**Outcome**
A tagged, published release of taskmd whose manifest, tag and release note agree, cut by
`docs/PUBLISHING.md`, and a record of what the cut had to be stopped for.

**Why this one**
The owner wants a release soon, and until now it had no record. Every other release this project has
made left one: the act itself is a handful of commands, and everything that has gone wrong went wrong
around it rather than in it. Three things this project already knows and that a release with no task
would have to remember unaided:

- **A bump exists because `claude plugin update` compares version strings.** A directory install whose
  manifest never changes reports *already at the latest version* and keeps serving its snapshot.
- **A release is not the last step of a release.** `0.4.0` shipped with nothing checking it from
  outside; [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) is why
  `0.5.0` did not, and it closed with half proven and half unreachable from any machine here.
- **The gate at `docs/PUBLISHING.md` §5 was red for two releases and nobody had disobeyed it** —
  nobody had run it. The suite runs it now, which is a reason to trust it and not a reason to skip
  reading its count.

**Scope**
- In: the version bump, `docs/PUBLISHING.md`'s procedure end to end, the tag, and the published release
- In: which milestone this release ships, and therefore what
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) runs §7 against
- In: **what the cut was stopped for.** A release that reports nothing had a gate that examined nothing
- Out: writing the release note to the rule and recording whether the rule caught anything. That is
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), which the owner
  scheduled after this one
- Out: **the pre-release audit.** It is not a step in the release procedure and never becomes one, which
  the method document says in its own words; the owner's instruction of 2026-08-22 keeps the two apart
- Out: anything a session may do unattended. **This record is deliberately outside the unattended grant
  of 2026-08-22** — tagging and publishing are outward-facing acts and the owner's to make

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) — the procedure, §5's gate, §6's pre-publish check, and
  §7's release-note rule
- `plugin/.claude-plugin/plugin.json` — the manifest, and the only place the version is written
- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) — what verifying a
  release from outside proved last time, and which half of it could not be run from any machine here

**Acceptance criteria**
- [ ] The manifest version, the tag and the published release all name the same version
- [ ] `docs/PUBLISHING.md` §5's gate and §6's pre-publish check were both **run**, and their output is
      recorded — including §5's file count, not only its silence
- [ ] Which milestone the release ships is stated, so §7 has a set to run against
- [ ] What the cut was stopped for is recorded, and if the answer is *nothing*, how that was checked
- [ ] Whether this release is verified from outside is decided and recorded either way

**Open questions**
- **Does a verification-from-outside task follow this one?** — the project owner. The recommendation is
  **yes, and blocked by this**: `0.5.0` had one and `0.4.0` did not, and the difference is the whole of
  what [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) records.
  Against it: T-085 also found half of that verification unreachable from any machine here, so a repeat
  buys less than the first one did and the reachable half is the cheaper half.
- **Which version number?** — the project owner. Not derivable: the standing policy spends one bump on
  a batch rather than on a single fix, and whether this batch is a minor or a patch is a judgement about
  what adopters meet.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, when they said a release was wanted soon and a survey of the open backlog found **no task carried it**. **Raised rather than left as an act** for the reason this project's own records give twice over: `0.4.0` shipped with nothing checking it from outside, and the dash gate was red for two releases because it lived in a document read only at publication. An act with no record repeats both. **Deliberately outside the unattended grant of the same date** — tagging and publishing are outward-facing and the owner's to make, and the grant's own boundary says the release is not in it. **It gives [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) a blocker it never had**, which is worth more than it looks: that record was gated on *there being a release to make*, an event no field could carry, and it sorted as startable in every view. The gate is now an edge. |
