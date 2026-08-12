---
id: T-120
title: Echo an unknown flag as the caller typed it
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-113, T-022]
work_package: M2
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
- None. **Q1 — which spelling should the rejection quote? — answered by the maintainer on
  2026-08-11: echo what was typed.** The recommendation is taken, so the reason stands as it was
  argued: the accepted list printed beside the flag already teaches the canonical spelling, and the
  reader's problem is matching their own typing against it.

  This settles the type as well. The task was raised `decision` because the choice was genuinely
  two-sided; with the choice made, what remains is the one-line change and its test, and criteria 1
  and 4 collapse to their first branch. The `decision` type is left as it is — it records what this
  task was for when it was raised, and rewriting it would erase that the question was ever open.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the failing test: a hyphenated unknown flag is quoted back exactly as typed, pinned against the whole string rather than a substring. | A case in `tests/test_list.py`, failing on the normalised echo. |
| 2 | Interpolate `arg` instead of `--%s` in the unknown-filter message. | `plugin/skills/taskmd/taskmd/cli.py` `parse_filters`. |
| 3 | Check the missing-value message against the same rule — it already interpolates `arg`, so confirm rather than change, and pin it. | A case proving `list --blocked-by` echoes the hyphen. |
| 4 | Pin that normalisation itself is untouched: `--blocked-by <id>` still filters. | A case in `tests/test_list.py`. |
| 5 | Run the suite, `check` and `index`. | Recorded output in §3. |

**Output paths**

- `plugin/skills/taskmd/taskmd/cli.py`
- `tests/test_list.py`

## 3. Implement

**Decisions & assumptions**
- Only the unknown-name message changed — 2026-08-11. The missing-value message already interpolated
  the raw argument, so step 3 confirmed it rather than editing it. It is now pinned by a test, which
  is the actual product of that step: without one, nothing stops a later edit normalising both "for
  consistency" and undoing half of this decision silently.
- The test asserts the whole string, not a substring — 2026-08-11. `--wat` is a substring of both
  spellings, so the existing `test_an_unknown_filter_name_is_reported` passed throughout and would
  have kept passing. That test is why the defect survived being covered.

**Evidence**

```
$ taskmd list --not-a-flag
unknown filter: --not-a-flag. This project accepts: --blocked_by, --blocks, --business_value,
--children, --effort, --owner, --parent, --phase, --related, --status, --type, --work_package
```

Failing first, on the same call:

```
AssertionError: False is not true : unknown filter: --not_a_flag. This project accepts: ...
```

`check` exit 0 on 122 tasks, index regenerated. `test_list` 35, `test_cli` 89, `test_schema` 46,
`test_budget` 5 green; `test_runtime` unchanged at four `Launchers` failures, all environmental
([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)).

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — the unknown-filter message interpolates `arg`.
- `tests/test_list.py` — three cases: the typed echo, the missing-value echo, and the hyphen still
  accepted as a spelling.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its reason, whichever way it goes | met | §1 *Open questions*, and the comment at the change site carries the reason for the next reader of that line. |
| If the echo changes, a test pins a hyphenated unknown flag against the exact string printed | met | `test_an_unknown_flag_is_quoted_as_the_caller_typed_it`, asserting the whole prefix rather than a substring. |
| If it changes, `list --blocked-by <id>` still filters — the normalisation is untouched | met | `test_the_hyphen_is_still_accepted_as_a_spelling`, exit 0. |
| If it does not change, the reason is written where the next reader meets it | n/a | It changed. The branch is closed, not skipped. |

**Child fix tasks raised**
- none. [T-122](T-122-echo-the-typed-flag-in-the-rejected-value-message.md) is a sibling: a third
  message in the same function, outside the two this task's scope names, carrying a wording question
  this task deliberately did not open.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | Three criteria met and the fourth closed by its branch not being taken; evidence in §3. Run under the standing M2 full-lifecycle authorization, extended by the maintainer on 2026-08-11 to this task specifically after it was re-filed into the release. Raised [T-122](T-122-echo-the-typed-flag-in-the-rejected-value-message.md) for the third message in the same function, found by running the command rather than by reading the diff. |
| 2026-08-11 | → specified | Q1 answered by the maintainer: echo what was typed. **Moved `M3` → `M2` in the same pass, correcting the filing below rather than the answer.** The grouping rule is `tasks/README.md`'s — M2 takes all dependencies plus every minor-to-moderate correction, M3 the bigger work and the new capabilities — and this is an `xs` correction that blocks nothing. The M3 rationale recorded below imported a test the rule does not use, adopter-visibility, and it does not survive comparison with T-113: that task changed *which* message a given invocation receives, which is the larger visible change, and it is v0.2. Left standing below as what was argued at the time (METHOD rule 5). **Note for whoever picks this up: the move brings it inside the standing M2 full-lifecycle authorization, which is a consequence of the correction and not a grant — the agent that re-filed it did not also start it.** |
| 2026-08-11 | → proposed | Surfaced while closing T-113 by running the command rather than reading it: the message printed a flag nobody had typed. Raised rather than fixed there, because T-113's scope puts the wording of both messages out and a finding is not fixed where it is found (METHOD §5). `M3` rather than `M2`: it holds nothing up, and unlike the corrections in that package it changes a string a script could be matching on, so it belongs with work an adopter is told about. Sized `xs`/`low` — one interpolation, or one comment. |
