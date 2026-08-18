---
id: T-162
title: Decide whether check reads a date-shaped field as a date
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-095, T-113, T-138, T-141]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-16
updated: 2026-08-18
deliverables: []
---

# T-162 — Decide whether check reads a date-shaped field as a date

## 1. Specify

**Outcome**
A ruling on whether `check` says anything about a value in a date field that is not a date, and — if
it does — what the class is and which fields it covers.

**Why this one**
Found on 2026-08-16 by writing one, not by looking for one. A script inserting the day's
authorisation rows also tried to refresh `updated:` and had an off-by-one in its match, producing:

```
updated: 2026-08-165        in two task files
updated: 2026-08-161        in a third
```

`check` reported `OK` over all three, and `index` regenerated without complaint. The damage was
caught by reading the script's own output, which is the accident this project usually calls a defect
in the instrument.

**Confirmed deliberately afterwards**, because an accident is not a specimen:

```
updated: 2026-13-99   ->   OK - 161 task(s), ... 2370 front-matter value(s)      exit 0
```

Month 13, day 99, exit 0.

**Why it is a `decision` and not a `fix`.** Three things are genuinely open and the answer to the
first may be *nothing*:

- **Dates are not a vocabulary.** Every field `check` validates today has an enumerated set in the
  config, and a date has none — so this is a new *kind* of field rule, not a new row. Whether taskmd
  wants typed fields at all is the question, and [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)
  is the same shape from a different direction. They may want one answer between them.
- **A wrong-but-well-formed date is the commoner fault and is not detectable.** `2026-08-15` where
  the author meant `2026-08-16` passes any check that could be written. So the class catches
  malformed values only, and the honest question is whether that is worth a rule — the
  [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) precision argument.
- **Which fields.** `created` and `updated` are the shipped template's, but a project's own config
  names its fields, and taskmd has no way to know which of them are dates unless the config says so —
  which is a config key, and therefore a cost paid by every adopter.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`) — a value the tool silently accepts is one nobody learns is wrong.

**Scope**
- In: whether malformed values in date-shaped fields are reported at all, and as `problem` or
  advisory.
- In: how such a field is *identified*, given that only a project's config could say.
- In: whether this and [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) are one
  decision about typed fields rather than two.
- Out: dates being *wrong* rather than malformed. Undetectable, and saying so is part of the answer.
- Out: any change to the shipped template's fields.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_vocabularies`, and how a field rule is expressed.
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the schema keys an adopter writes.
- [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) — the neighbouring question.
- The two specimens above; both reproduce in one command.

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Is this one decision with T-146 or two?** Decide at `specify`. Both ask whether taskmd's schema
  describes fields beyond an enumerated vocabulary, and answering them apart risks two mechanisms for
  one idea — which is the fault [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)
  had to repair in the marked-list guard four days after T-134 shipped it.

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
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-16 | → proposed | Raised while writing the unattended batch's authorisation rows, from a real accident rather than a review: a script produced `2026-08-165` in two files and `2026-08-161` in a third, and `check` and `index` both passed over them. Confirmed with a deliberate specimen (`2026-13-99`, exit 0) because an accident is not evidence. **Explicitly outside that batch's authorisation**, which names four tasks and excludes what they raise; this is filed and left for the maintainer. `medium` and `s`, and typed `decision` because the answer may be that nothing is added — the detectable half is malformed values only, and a date that is merely wrong passes anything. |
