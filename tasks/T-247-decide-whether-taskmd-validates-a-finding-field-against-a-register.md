---
id: T-247
title: Decide whether taskmd validates a finding field against a register
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-223, T-146, T-173, T-244]
work_package: M7
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables: []
---

# T-247 — Decide whether taskmd validates a finding field against a register

## 1. Specify

**Outcome**
A recorded answer to whether `check` validates a task's `finding:` value against a findings register,
and — if the answer is no — a **third row** in `.taskmd/config.md`'s *What this rule has already
refused*, so the next person to want it meets the answer rather than the gap.

**Why this one**
[T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) §1 scoped it out in these words:

> Out: validating a `finding:` field against a findings register. That is schema and tool work, it is
> a real gap the adopting project has worked around, and it is a different task.

**It named no task, and none was raised.** Found on 2026-08-23 by searching for one. That is the
shape `check`'s own `PARKED TASK` class exists to catch, arriving in a scope line rather than in an
open question, where nothing looks for it.

**The adopter is about to walk into it.** The deck project's `docs/AUDIT-METHOD.md` §3 calls it *the
one tool gap*: their `tools/docs/findings.py` hardcodes one register and one id pattern, their own
lint runs it, and a task carrying a different register's id fails that lint. Their pre-release audit
is at `implement`, and its cycle 0 still owns closing the gap.

**What taskmd does today, stated so nobody re-derives it.** `finding:` is a field this schema does not
name, so it is **carried and never interpreted** — taskmd neither validates it nor complains about it.
Confirmed on 2026-08-23 by running `check` over that project's 220 tasks: 3,952 front-matter values
read, no vocabulary problem raised about `finding`. The failing lint is theirs, not ours.

**This is the same shape refused twice already, and that is the heart of the decision.**
`.taskmd/config.md`'s *What this rule has already refused* names two capabilities, both declined on
one ground: each needed the tool to learn **project vocabulary** — which field carries the fact — and
every route to that adds a key to the config, which breaks every project that has written one. A
finding register is the same, twice over: the tool would have to learn which field holds the finding
id *and* where the register lives.

**So the question is not whether it would be useful.** Both refusals say plainly that neither
capability is worthless. The question is whether a real adopter, blocked on a real audit, is the
evidence that changes the arithmetic — and evidence licenses re-opening a rejection, not reversing it.

**One route that adds no key, and is probably only half an answer**

A project could carry the pointer as an ordinary Markdown **link in the task body** rather than as a
front-matter field. `check` already resolves every link in every task it reads and reports a broken
one, with no key and no vocabulary. What it cannot do is confirm that a particular finding *id*
exists inside the register: `SECTION REF` resolves *document §n*, and a finding is usually a table
row rather than a section. So this route probably buys the *document* half and not the *row* half.
It is written here as something to test rather than as an answer.

**Scope**
- In: the decision, and the argument that supports it either way
- In: if declined, the third row in `.taskmd/config.md`'s refused list, in the shape the two existing
  rows use
- In: testing the body-link route far enough to say what it does and does not cover
- Out: **closing the adopter's gap.** Their `findings.py` is theirs, their document says so, and this
  record does not take it on
- Out: re-opening [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) or
  [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md). Both stand;
  this record only asks whether new evidence changes the same arithmetic

**Inputs**
- `.taskmd/config.md`, *What this rule has already refused* — the two declines, and the ground both
  rest on
- `.taskmd/config.md`, *Adding a key to this file is a breaking change* — the cost that ground is
  made of, and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) for why an
  unknown key errors rather than passing
- [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) §1 — the scope line that raised
  this and named no successor
- The deck project's `docs/AUDIT-METHOD.md` §3 — the gap as its owner states it, and what it blocks

**Acceptance criteria**
- [ ] The answer is recorded, with what it rejected and why
- [ ] If declined, `.taskmd/config.md`'s refused list carries a third row, and it says what a project
      does instead
- [ ] What the body-link route covers and does not cover is stated, from having run it rather than
      from reading the code
- [ ] The adopter can tell from this record whether to close their own gap or wait

**Open questions**
- **Does an adopter blocked on a real audit reopen a refusal taken twice on cost?** — the project
  owner. The recommendation is **no: record it as the third row**. The two existing refusals were not
  about whether anyone wanted the capability; they were about the cost falling on every configured
  project, at upgrade, whether or not that project ever wanted it — and one adopter's need does not
  move that arithmetic. They already own a script that does the job for their register, and the
  config's own *What a project does instead* points exactly there. *Against: two refusals and a third
  request is a pattern rather than a coincidence, and a rule that has now turned away three real asks
  may be protecting an upgrade cost that is smaller than the sum of what it refuses. The honest way
  to find out is to price the key once, rather than to decline a third time on the same sentence.*

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
| 2026-08-23 | → proposed | **Raised on the owner's instruction of 2026-08-23**, after a check of taskmd's readiness for the adopter's audit found this scoped out of [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) with no successor record. **Raised as a `decision` rather than as tool work**, because `.taskmd/config.md` has already refused this exact shape twice on one ground, and the live question is whether a blocked adopter is evidence that moves it. **What taskmd does today was measured rather than assumed**: `finding:` is an unnamed field, so it is carried and never interpreted, and a `check` run over the adopter's 220 tasks raised nothing about it — the failing lint is theirs. **The body-link route is named but not claimed**, because it plausibly covers the document and not the row, and this record is not the place to guess which. |
