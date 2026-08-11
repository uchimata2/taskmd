---
id: T-122
title: Echo the typed flag in the rejected-value message too
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-120, T-113]
work_package: v0.2
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_list.py]
---

# T-122 — Echo the typed flag in the rejected-value message too

## 1. Specify

**Outcome**
The third rejection `parse_filters` can emit quotes the flag as the caller typed it, on the same rule
[T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md) settled for the other two.

**Why this one**
T-120's scope named two messages — the unknown-name one and the missing-value one — and both now
echo the raw argument. There is a third, for a value outside an enumerated vocabulary, and it still
interpolates the normalised name:

```
$ taskmd list --business-value nonsense
--business_value does not take 'nonsense'. This project's business_value values are: critical, high, medium, low
```

Found by running the command after closing T-120, not by reading the diff. Raised rather than fixed
there because T-120's scope is explicit about which two messages it covers, and a finding is not
fixed where it is found (METHOD §5).

**It is not simply T-120 applied again.** That message names the field *twice*, and the two
occurrences want different spellings: the first is the flag the caller typed, the second is the
project's field, whose values are being listed. `--business-value does not take 'nonsense'. This
project's business_value values are: ...` is the likely shape, and it reads as a mismatch until you
see that one is a flag and the other is a field. Deciding whether that is acceptable is the whole of
this task.

**Scope**
- In: the vocabulary-value rejection in `parse_filters`, and whether its two references to the field
  take the same spelling.
- Out: the two messages T-120 covered, which are done.
- Out: accepting both spellings, and the normalisation itself. Unchanged and not in question.
- Out: `--limit`'s "whole number" message, which names a flag that has only one spelling.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `parse_filters`, the vocabulary branch.
- [T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md) — the rule and the reason behind it.

**Acceptance criteria**
- [ ] The flag in that message is quoted as typed, or a recorded decision says why it is not
- [ ] The listed values still name the project's field in the schema's own spelling
- [ ] A test pins the whole string for a hyphenated call, not a substring — the defect T-120 fixed
      survived a substring assertion
- [ ] `list --business-value high` still filters; the normalisation is untouched

**Open questions**
- **Should the message name the field once instead of twice?** "`--business-value` does not take
  'nonsense'. Accepted: critical, high, medium, low" avoids the mismatch entirely by dropping the
  second reference. It is a wording change, which T-120 held out of scope for itself — maintainer to
  decide whether it is in scope here.

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
| 2026-08-11 | → proposed | Third of the three rejections in one function to be looked at, after T-113 fixed the order of two of them and T-120 fixed what two of them quote. `v0.2` under `tasks/README.md`'s grouping rule — an `xs` correction blocking nothing — which is also the correction applied to T-120's own filing on the same day. Sized `low` rather than `medium`: unlike T-120's case, the flag here is one the project *has*, so a reader comparing it against their own typing is checking a value, not hunting a misspelling. |
