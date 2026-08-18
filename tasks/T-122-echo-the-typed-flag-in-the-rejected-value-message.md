---
id: T-122
title: Echo the typed flag in the rejected-value message too
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-120, T-113]
work_package: M2
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_list.py]
adopter_visible: yes
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
- ~~**Should the message name the field once instead of twice?**~~ **Answered 2026-08-11: no**, and
  the reason is in this section rather than in taste — see D2 in §2. Dropping the second reference
  would falsify **criterion 2**, which is unconditional and was agreed with the rest of this spec;
  answering the question "yes" is therefore not a wording choice but an amendment to the outcome,
  which is the owner's to make and not something to slip in beside the answer.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reproduce the message by running the command, hyphenated, before changing anything. | Recorded output |
| 2 | Interpolate the raw argument in the first of the message's two references to the field, leaving the second in the schema's spelling. | `parse_filters` in `plugin/skills/taskmd/taskmd/cli.py` |
| 3 | Pin the **whole** string for a hyphenated call, and keep the underscored call answered too — the two spellings are one filter. | `tests/test_list.py` |
| 4 | Show `list --business-value high` still filters, so the normalisation is untouched. | Recorded output |
| 5 | `check`, `index`, the suite. | Recorded output |

**Shape decisions.**

**D1 — One character of behaviour, `--%s` on `name` becoming `%s` on `arg`.** The scope allows exactly
this: the first reference is the flag the caller typed, and everything else about the sentence stays.

**D2 — The field is still named twice, in two spellings.** This is the open question, answered here
because the specify already answered it in criterion 2 — *the listed values still name the project's
field in the schema's own spelling* — which the one-reference form does not satisfy. It is also the
rule T-120 recorded and the reason the trio ends consistent: the echo teaches nothing and exists to be
recognised, the canonical name teaches the spelling and exists to be copied. *Rejected: "Accepted:
critical, high, medium, low".* It is the better-reading sentence and that is a real cost of this
answer; what it drops is the one place the message states the field's own spelling, and it would have
to arrive as an amendment to criterion 2 rather than under it.

**Planned outputs**
- plugin/skills/taskmd/taskmd/cli.py
- tests/test_list.py

## 3. Implement

### Step 1 — before

```text
$ taskmd list --business-value nonsense
--business_value does not take 'nonsense'. This project's business_value values are: critical, high, medium, low
exit 2
```

### Steps 2–3 — after, both spellings

```text
$ taskmd list --business-value nonsense
--business-value does not take 'nonsense'. This project's business_value values are: critical, high, medium, low

$ taskmd list --business_value nonsense
--business_value does not take 'nonsense'. This project's business_value values are: critical, high, medium, low
```

**Two tests, not one.** The first pins the hyphenated call whole. The second exists because *echoed
as typed* and *always hyphenated* are different rules that agree on the first case: a fix that
hard-coded the hyphen would pass the whole-string test and be the same defect mirrored. Step 1 is
what makes the first test non-vacuous — the old message is on record answering a hyphenated call
with underscores, so no revert was needed to show it would have failed.

### Step 4 — the normalisation is untouched

```text
$ taskmd list --business-value high --limit 3
T-001  done  M1  review  Decide how the front-matter schema is configured
T-010  done  M1  review  Write the GitHub Issues binding
T-079  done  M1  review  Humanize the human-facing documents before publishing
exit 0
```

### Step 5 — the rest

Suite: `test_cli` 98 OK, `test_list` **37** OK (35 before, plus these two), `test_schema` 53 OK,
`test_budget` 5 OK, `test_runtime` 27 `OK (skipped=3)`.

**Decisions & assumptions**
- **D1 — the echo is `arg`, one interpolation** — 2026-08-11, §2.
- **D2 — the field stays named twice, in two spellings** — 2026-08-11, §2; this answers the open
  question, and the rejected wording is recorded there with what it costs.
- **Assumption: the two-spelling sentence is legible enough.** It is the shape T-120 settled and now
  the shape all three rejections share, so a reader meets one convention rather than three. If it
  turns out to read as a disagreement in practice, that is a wording task against criterion 2, not a
  re-run of this one.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py)
- [`tests/test_list.py`](../tests/test_list.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The flag in that message is quoted as typed, or a recorded decision says why it is not | met | §3 step 2, both spellings, from runs |
| The listed values still name the project's field in the schema's own spelling | met | `This project's business_value values are: …` is unchanged — and it is the clause the open question proposed dropping, which is why the answer to that question is *no* rather than a preference |
| A test pins the whole string for a hyphenated call, not a substring — the defect T-120 fixed survived a substring assertion | met | `assertEqual` on the full line, plus a second test for the underscored call, since the whole-string test alone cannot tell *as typed* from *always hyphenated* |
| `list --business-value high` still filters; the normalisation is untouched | met | §3 step 4: three rows, exit 0 |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met, no child raised. **Authorisation (METHOD §3.1):** the maintainer's standing grant to work every open `M2` task through its full lifecycle, given 2026-08-10 and widened on 2026-08-11 to *the remaining tasks, full lifecycle, continuously*. **The open question was decided by the specify rather than by taste**: dropping the second reference to the field would falsify criterion 2, which is unconditional and already agreed — so answering it *yes* is an amendment to the outcome and not a wording choice, and it is recorded as rejected with what it costs (the better-reading sentence) rather than as a bad idea. Two things worth carrying. **Two tests, because one cannot separate the rules**: *echoed as typed* and *always hyphenated* agree on the hyphenated call, so a fix hard-coding the hyphen would pass a whole-string test and be the same defect mirrored. And **the pre-fix run is what makes the whole-string test non-vacuous** — the old message is on record answering `--business-value` with `--business_value`, so nothing had to be reverted to show what the test catches. All three rejections in `parse_filters` now share one convention. |
| 2026-08-11 | → proposed | Third of the three rejections in one function to be looked at, after T-113 fixed the order of two of them and T-120 fixed what two of them quote. `M2` under `tasks/README.md`'s grouping rule — an `xs` correction blocking nothing — which is also the correction applied to T-120's own filing on the same day. Sized `low` rather than `medium`: unlike T-120's case, the flag here is one the project *has*, so a reader comparing it against their own typing is checking a value, not hunting a misspelling. |
