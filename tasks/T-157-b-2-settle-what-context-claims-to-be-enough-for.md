---
id: T-157
title: B-2 — Settle what `taskmd context` claims to be enough for
type: decision
status: done
phase: review
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
| 1 | Re-measure the row rather than carry it: what `context` returns against the file it names | The figures below |
| 2 | Replace the claim with what is true for orientation, and say plainly that it is a summary | `plugin/skills/taskmd/SKILL.md` |
| 3 | Point at the binding's `read` for what is left out, rather than restating it | The same sentence, one clause |
| 4 | Confirm the description is untouched, since that is the half tier 1 pays for | The budget figure, unchanged |

## 3. Implement

**Re-measured 2026-08-15**, on the same task the register row used:

```
context T-145: 753 chars
file:         7554 chars
body in context: False
```

Ten times smaller, and the body is absent — not abridged. The register row's observation holds at
figures slightly different from its own, which is why it was re-run.

**Decisions & assumptions**

- **The sentence changes; the command does not** — 2026-08-15. `context` returning a pointer is the
  design, and the audit records the tool *already declining* to pay for the body. What was wrong was
  a sentence promising more than the tool intends to give. *Rejected:* changing what `context` prints.
- **The binding keeps the full statement, and `SKILL.md` points at it** — 2026-08-15. The binding's
  `read` operation already says `context` is not `read` and why; writing that again in `SKILL.md`
  would be the second copy this project's one design rule forbids. The new sentence names the
  binding's own `read` rather than describing it, so it stays true for a project on any backend.
- **`your binding's read`, not this repository's** — 2026-08-15. `SKILL.md` ships to adopters and must
  not name the local-Markdown binding; `read` is in the backend contract, so every binding has one.

**Outputs produced**

`plugin/skills/taskmd/SKILL.md` — the *Run first* block. Tier 1 is unchanged: the edit is in the body,
and the counted figure stayed at 6,305 characters.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `SKILL.md` and the binding make the same claim about whether the body must be opened | met | Both now say `context` is a summary, not the file. The contradiction the register row found is gone. |
| The distinction is stated in one of them and pointed at from the other, never written twice | met | The binding's `read` states it; `SKILL.md` names that operation in one clause and describes nothing. |
| The skill description is unchanged in length or shorter | met | Untouched — the budget reports the same 6,305 characters as before this task. |
| The measured outcome is written into this record on the day it is known | met | Above, 2026-08-15. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s byproduct register, row B-2, whose disposition the maintainer agreed in advance: this row becomes a task and B-1 and B-3 do not. `low` because nothing is broken and no adopter is misled about what the tool does — only about how much of a task a session has read. |
| 2026-08-15 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review` — in a request covering T-153, T-154, T-155, T-156 and T-157 and **nothing else**. Any task raised from here takes one phase per request unless separately authorised (METHOD §3.1). Recorded in each of the five records because an authorisation kept anywhere else is one a later session can miss or stretch. |
| 2026-08-15 | → done | All four phases run, all four criteria met. The byproduct register was right about the sentence and the figures had already moved — 753 and 7,554 against the 740 and 7,590 it recorded, on the same day. That is the register doing its job and the re-measurement doing its own. |
