---
id: T-251
title: Give the open records the adopter_visible prompt they predate
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-245, T-248, T-242]
work_package: M7
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-251 — Give the open records the adopter_visible prompt they predate

## 1. Specify

**Outcome**
Every open record carries the `## 4. Review` prompt for `adopter_visible`, so none of them can close
without the judgement `docs/PUBLISHING.md` §7 reads.

**Why this one**
[T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) put the prompt in
the templates on 2026-08-23 and measured what that does to the **closed** backlog: nothing, because
those records contain no line to match. It did not measure the **open** backlog, and that is the gap.

Measured 2026-08-23, while writing a handoff: **all six open records predate the template change and
carry no prompt.** Two carry no `adopter_visible` field either.

| Record | Has the prompt | Has the field |
| :--- | :---: | :---: |
| [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md) | no | yes |
| [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) | no | **no** |
| [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md) | no | yes |
| [T-247](T-247-decide-whether-taskmd-validates-a-finding-field-against-a-register.md) | no | yes |
| [T-240](T-240-the-competition-rig-does-not-reproduce-the-silence-it-was-built-to-explain.md) | no | **no** |
| [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md) | no | yes |

`check` is silent on all six and correctly so — an open record has not reached `## 4. Review`, which
is the gate that keeps the rule from being 77% noise. The consequence is only visible later: each
closes with nothing having asked, and §7 blocks on it. That is the wall `0.6.0` met, arriving through
the open backlog rather than the closed one.

**Scope**
- In: the six open records above, and any opened before this lands
- In: the two missing `adopter_visible` fields
- Out: **closed records.** They contain no line to match and METHOD rule 5 forbids rewriting them.
  The three the rule already reports are
  [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md)
- Out: judging the value on the six. Adding the prompt is not answering it — the judgement is made
  when the work is understood, which is what §7 says and what the prompt exists to ask for

**Inputs**
- [`tasks/_task-template.md`](_task-template.md) — the prompt's wording, which is what must match
- [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) §3 — why the
  prompt is a body slot and not a front-matter field, and why it carries no code spans

**Acceptance criteria**
- [ ] Every open record carries the prompt, byte-identical to the template's line — a near-miss is a
      slot `check` cannot match
- [ ] The two records missing `adopter_visible` have the field, unjudged is not an option once closed
- [ ] Closing one of them without answering the prompt is reported, shown by making `check` fail on
      a real case rather than by a clean tree
- [ ] `taskmd check` still exits 0 on the tree, since all six remain open

**Open questions**
- None. The set is measured and the wording is the template's.

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
| 2026-08-23 | → proposed | **Found by the reconcile sweep while writing a handoff**, 2026-08-23. [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) stated what its fix does to the closed backlog and was not asked about the open one; the sweep asked. **The owner's full-lifecycle grant of 2026-08-23 does not reach this record** — it covers T-250, T-241 and anything raised *by their work*, and this was raised by the handoff, not by either of them. |
