---
id: T-157
title: B-2 — Settle what `taskmd context` claims to be enough for
type: decision
status: proposed
phase: specify
parent: T-152
blocked_by: []
related: []
work_package: M6
owner: maintainer
business_value: low
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-157 — B-2: settle what `taskmd context` claims to be enough for

## 1. Specify

**Outcome**
`SKILL.md` and the binding say the same thing about whether a session still has to open the task file,
so a reader of the first does not skip the second.

**Why this one**
Byproduct-register row `B-2` of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), recorded in
[its report](../docs/audits/2026-08-15-context-economy-taskmd.md#byproduct-register). `SKILL.md` says
`context` "returns everything needed to start that one task, and is the only read of it you need"; the
binding's `read` operation says the opposite in as many words — `context` "is **not** this operation",
it prints no body, and only one of the two satisfies the contract. Measured in the audit, `context`
returned a fraction of the file and no body at all.

**Recorded as an observation, not a defect claim.** The sentence is true for orientation and false for
specification, and which of those `SKILL.md` should promise is the owner's call. That is why this is a
`decision` and why it is `low`.

**Scope**
- In: the sentence in `plugin/skills/taskmd/SKILL.md`, and its agreement with the binding.
- Out: what `context` prints. The observation is about the claim, not the command.
- Out: the skill's front-matter description. It is tier 1 and this task must not grow it.

**Inputs**
- The register row, in
  [the project's audit report](../docs/audits/2026-08-15-context-economy-taskmd.md#byproduct-register)
- `plugin/skills/taskmd/SKILL.md` — the `Run first` block
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the `read` operation, and the paragraph
  that already states the distinction

**Acceptance criteria**
- [ ] `SKILL.md` and the binding make the same claim about whether the body must be opened
- [ ] The distinction is stated in one of them and pointed at from the other, never written twice
- [ ] The skill description is unchanged in length or shorter
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- none.

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
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s byproduct register, row B-2, whose disposition the maintainer agreed in advance: this row becomes a task and B-1 and B-3 do not. `low` because nothing is broken and no adopter is misled about what the tool does — only about how much of a task a session has read. |
