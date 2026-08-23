---
id: T-254
title: Sweep for history prose living outside Markdown, which T-250's corpus could not see
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-250, T-249]
work_package: M7
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-254 — Sweep for history prose living outside Markdown, which T-250's corpus could not see

## 1. Specify

**Outcome**
The rule in [`../CLAUDE.md`](../CLAUDE.md) *Write the fact, not its history* has been applied to the
prose this project keeps **outside** `.md` files — module docstrings and comments in shipped code
first — or the project has recorded that it deliberately does not reach there.

**Why this one**
Found while working [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md)
on 2026-08-23, by reading `plugin/skills/taskmd/taskmd/cli.py` for an unrelated reason. Its module
docstring carries:

```text
Four, and the fourth was argued for rather than added — the command surface stood at three until
2026-08-05 (T-022).
```

That is a shipped file telling an adopter what the command surface **used to be**. Whether it is a
defect is the question this record exists to answer; that it was never examined is not in question.

**How it was missed, which is the part worth keeping.**
[T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) swept this project for
exactly this rule and derived its corpus as *every Markdown file the project keeps*. That derivation
is stated in its §3 and it is honest, but it is keyed on **file extension**, and prose does not live
only in `.md`. So the sweep reported 25 candidates, five edited and twenty read, with a denominator
that never contained this file. **A corpus derived by extension cannot report the prose it excluded
by construction** — the same failure T-250's own findings are about, one level up.

**Scope**
- In: prose in files the project keeps that are not `.md` — module docstrings, comment blocks in
  shipped code, and anything else a derivation by extension skipped
- In: deciding whether the rule reaches a **docstring in shipped code** at all, which is the
  question, not a formality — a comment explaining why a design is what it is may be the one place
  that reasoning can live
- Out: re-doing T-250's Markdown sweep. That corpus was derived, classified and recorded
- Out: code comments that explain *what the code does*. The rule is about history, not about
  commenting style

**Inputs**
- [`../CLAUDE.md`](../CLAUDE.md) *Write the fact, not its history* — the rule
- [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) §3 — the corpus
  derivation, its stated blind spot, and the five edits it made, so this one does not repeat them
- `plugin/skills/taskmd/taskmd/cli.py` — the instance that raised this

**Acceptance criteria**
- [ ] The corpus is derived from something other than a file extension, and the derivation states
      what it reaches and what it does not — the failure this record is about must not recur in the
      record that fixes it
- [ ] Every candidate carries a verdict, not only the ones edited
- [ ] Where the rule is decided **not** to reach a docstring, that decision is recorded with what it
      rules out, so the next sweep does not re-open it
- [ ] Nothing an adopter runs changes behaviour; if a shipped file is edited, that is stated and the
      suite is re-run

**Open questions**
- **Does the rule reach a docstring in shipped code?** — the project owner. **Recommendation: yes,
  but with the same exemption Markdown gets** — guide prose of any length stays, and only the account
  of *what a thing used to be* goes. On the instance above that means keeping *"the fourth was argued
  for rather than added"* and the pointer to T-022, and dropping *"stood at three until 2026-08-05"*.
  *Against:* code comments are where a maintainer expects to find why a decision was made, and the
  line is short, load-bearing and read by far fewer people than a binding is — the rule was written
  for documents paid for on every read, which a docstring is not.

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

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised while working [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md)**, 2026-08-23, and **outside its scope** — T-248 judges three marks and touches nothing else. Raised rather than fixed for that reason. **It is not covered by the grant given for T-248**, which named that record and did not extend to what its work turned up, so nothing here has been worked past `specify`. **[T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) is not re-opened**: its corpus, its classification and its five edits stand, and this record is the class its derivation could not see rather than a correction of what it did. |
