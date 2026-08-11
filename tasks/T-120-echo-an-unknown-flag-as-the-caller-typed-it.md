---
id: T-120
title: Echo an unknown flag as the caller typed it
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-113, T-022]
work_package: v0.3
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py]
---

# T-120 — Echo an unknown flag as the caller typed it

## 1. Specify

**Outcome**
A decision, and the one-line change if it goes that way: when `list` rejects a flag it does not
recognise, the message either quotes the flag as it arrived or keeps quoting the normalised form,
with the reason recorded either way.

**Why this one**
`parse_filters` normalises before it complains — `name = arg[2:].replace("-", "_")` — and every
message downstream interpolates `name`. So the flag the caller typed and the flag the error names
are not the same string:

```
$ taskmd list --definitely-not-a-flag
unknown filter: --definitely_not_a_flag. This project accepts: --blocked_by, ...
```

Found while closing [T-113](T-113-name-an-unknown-filter-before-complaining-it-has-no-value.md),
which reordered the two checks around this line without touching it. Pre-existing, not introduced
there: the old order printed the same normalised name from the same expression. It surfaced because
T-113's spec quoted the message with hyphens, and the quote turned out to be idealised rather than
copied — so the spec of a task about this message had itself misread it, which is the evidence that
a reader can.

**It is genuinely two-sided, which is why this is a `decision` and not a `fix`.** The normalised
form matches the accepted list printed beside it, all of which uses underscores, so echoing what was
typed puts two spellings of the same vocabulary in one message. Against that: the message quotes
something the caller can search their own history for and not find, and the one case where the two
differ is the case where they most need to compare character by character — a misspelling.

**Scope**
- In: which spelling the rejection echoes, for the unknown-name message and the missing-value one.
- Out: accepting both spellings. That is settled and stays — `--blocked-by` and `--blocked_by` are
  the same filter, and this task does not touch the normalisation itself, only what is quoted back.
- Out: the accepted list's spelling. It is the schema's own, and a field is named with underscores.
- Out: the ordering of the two checks, which is T-113's and is done.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `parse_filters`, and the two `return None, ...` messages.
- [T-022](T-022-filtered-task-listing-for-scripts.md) — where the rejection behaviour and its rule
  that nothing prints before an error were built.

**Acceptance criteria**
- [ ] The decision is recorded with its reason, whichever way it goes
- [ ] If the echo changes, a test pins a hyphenated unknown flag against the exact string printed
- [ ] If it changes, `list --blocked-by <id>` still filters — the normalisation is untouched
- [ ] If it does not change, the reason is written where the next reader of that line meets it

**Open questions**
- Which spelling should the rejection quote — the maintainer decides. Recommended: echo what was
  typed, since the accepted list beside it already teaches the canonical spelling and the reader's
  problem is matching their own typing against it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → proposed | Surfaced while closing T-113 by running the command rather than reading it: the message printed a flag nobody had typed. Raised rather than fixed there, because T-113's scope puts the wording of both messages out and a finding is not fixed where it is found (METHOD §5). `v0.3` rather than `v0.2`: it holds nothing up, and unlike the corrections in that package it changes a string a script could be matching on, so it belongs with work an adopter is told about. Sized `xs`/`low` — one interpolation, or one comment. |
