---
id: T-113
title: Name an unknown filter before complaining it has no value
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-022, T-029]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_list.py]
---

# T-113 — Name an unknown filter before complaining it has no value

## 1. Specify

**Outcome**
`list` tells a caller that a flag is not one it accepts, whether or not that flag was given a value.
The message that names the project's own vocabulary is reached by the misspelling that actually
happens, not only by the one that happens to be well-formed.

**Why this one**
Found by [T-029](T-029-reject-unknown-arguments-on-every-command.md) while building a probe that
every command had to refuse. `list` checks the *shape* of an argument before its *name*:

```
taskmd list --definitely-not-a-flag value
unknown filter: --definitely-not-a-flag. This project accepts: --blocked_by, --blocks, ...

taskmd list --definitely-not-a-flag
--definitely-not-a-flag needs a value
```

The second is the more likely typing — a flag remembered wrongly and typed alone, or a boolean flag
that is not one — and it is the one told nothing useful. "Needs a value" invites the reader to
supply one, which produces the *other* error; the message actively points away from the answer.

**Not what T-029 fixed.** That task made three commands reject what they had been discarding, and
recorded `list` as the model to follow because it refuses before printing and names the project's own
values. Both remain true. This is one branch inside that refusal taken in the wrong order, and it is
raised rather than fixed there because a finding is not fixed where it is found (METHOD §5).

**Scope**
- In: the order of the two tests in `parse_filters` — an unrecognised name is unrecognised whether or
  not a value follows it.
- Out: the wording of either message, and which filters exist. Both are settled.
- Out: `--help` and the three commands' arity, which are T-029's and are done.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `parse_filters`.
- [T-022](T-022-filtered-task-listing-for-scripts.md) — where the rejection behaviour was built, and
  the rule that a rejection arrives before any output.

**Acceptance criteria**
- [ ] `list --<unknown>` with no value names the flag as unknown and lists what the project accepts
- [ ] `list --<unknown> value` is unchanged
- [ ] A *known* filter given no value still says it needs one — the missing-value message is not
      removed, only reached second
- [ ] Shown failing first, since the second criterion passes today

**Open questions**
- None.

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
| 2026-08-10 | → proposed | Surfaced by T-029's derived probe: a test written to prove all four commands refuse an unknown argument found that one of them refuses it for the wrong reason. Sized `xs`/`medium` — a two-line reordering, on the command whose whole purpose is being scripted against. `v0.2` by T-110's rule (a minor correction, holding nothing up). |
