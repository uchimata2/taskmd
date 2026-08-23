---
id: T-247
title: Decide whether taskmd validates a finding field against a register
type: decision
status: done
phase: review
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
deliverables:
  - plugin/skills/taskmd/taskmd/defaults/config.md
  - .taskmd/config.md
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
- ~~**Does an adopter blocked on a real audit reopen a refusal taken twice on cost?**~~ **Answered by
  the owner on 2026-08-23: no. Record it as the third row.** Asked as a survey with the two
  alternatives priced — build it, or test the body-link route before deciding — and the recommendation
  below was taken as written. **What this settles and what it does not:** the refusal is settled, and
  the *Against* argument below stands unrefuted rather than defeated, so it is kept as written for
  whoever meets a fourth request. The body-link route stays in scope as something to test and record,
  because the third row is stronger if it says what a project can do instead. The argument the owner
  weighed, unchanged:
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

**The decision was already taken; this plans what it obliges.** The owner answered on 2026-08-23 —
*no, record it as the third row* — so no step below re-opens it. §1 keeps the *Against* argument
unrefuted rather than defeated, and that is deliberate: a fourth request meets the same page.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run the body-link route on a real register rather than reading the code, and record each half separately: the document, the section, and the finding row. | The measurement, in §3 |
| 2 | Write the third row into the **shipped** config's refused list, in the shape the two rows use, and put what step 1 measured into *What a project does instead*. | `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 3 | Carry the same text into this project's own config, which is a copy of that file. | `.taskmd/config.md` |
| 4 | Answer the adopter plainly: close their own gap, or wait. | §4 |

**Outputs this task will produce**

- `plugin/skills/taskmd/taskmd/defaults/config.md`
- `.taskmd/config.md`

## 3. Implement

**Decisions & assumptions**
- **The row goes in the shipped config first, and in this project's copy because it is a copy** —
  2026-08-23. §1 named `.taskmd/config.md` alone, and that is where a reader of *this* repository
  meets it — but the outcome says *the next person to want it*, and that person is an adopter, who
  reads the shipped file. Writing only the one §1 named would have left the answer invisible to
  everyone it is for.
- **The measurement is reported in three halves, not two** — 2026-08-23. §1 predicted the body link
  would buy the *document* half and not the *row* half. Running it splits the middle: the section
  half is **reported and does not gate**, which is a third state §1 did not have a word for.

**Evidence — the body-link route, run on a register**

A throwaway project: a two-row findings register at `docs/FINDINGS.md`, and one task carrying
`finding: PR-06` in front matter and four body references. `check` run against it:

```
BROKEN LINK   tasks/T-001-...md -> ../docs/MISSING-REGISTER.md
1 problem(s) - ... 11 front-matter value(s) ...            rc=1
```

```
OK - 1 task(s), ... 5 section reference(s)
SECTION REF  docs/FINDINGS.md has no section 9; 1 reference(s) name it     rc=0
```

Read per case rather than as a verdict:

| The reference | What `check` did | Gates? |
| :--- | :--- | :---: |
| `finding: PR-06` in front matter | counted among 11 front-matter values, **no vocabulary problem** | no |
| a link to a register that does not exist | `BROKEN LINK`, `rc=1` | **yes** |
| `[the register](...) §1`, a section that exists | silent | — |
| `[the register](...) §9`, a section that does not | `SECTION REF ... has no section 9`, **`rc=0`** | no |
| `PR-99`, an id the register does not hold | **nothing at all** | no |

**So the body link answers *is the register there* and not *is my finding in it*.** The last row is
the one that matters: a finding is a table row, and no reference kind resolves a row. The fourth row
is the surprise — the section check informs without moving the exit code, so a project relying on it
as a gate would be relying on a message.

**What taskmd does with `finding:` today, confirmed rather than assumed**: carried and never
interpreted. It is not in the schema, so it is neither validated nor complained about, which is
exactly what §1 states and what the 11 counted front-matter values show.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the third refused row, the count sentence
  corrected from two to three, and the measured register route added to *What a project does instead*
- `.taskmd/config.md` — the same text. The two files now differ in exactly one line, `context_fields`,
  as they did before

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is recorded, with what it rejected and why | met | The third row states the refusal and its ground — two project facts, not one. §1 keeps the *Against* argument as written, so a fourth request meets the counter-case rather than only the answer. |
| If declined, `.taskmd/config.md`'s refused list carries a third row, and it says what a project does instead | met | Carried in both that file and the shipped config it is a copy of. *What a project does instead* now names the body-link route with what it does and does not cover. |
| What the body-link route covers and does not cover is stated, from having run it rather than from reading the code | met | Run against a real register, five cases, table in §3. It refined the prediction rather than confirming it: the section half is reported and does not gate. |
| The adopter can tell from this record whether to close their own gap or wait | met | **Close their own gap.** See below. |

**The answer to the adopter, plainly.** Close your own gap; do not wait for taskmd. `finding:` will
not be validated, and the refusal is now recorded where you will meet it. The body link is worth
adopting anyway — it costs nothing and catches a register that has moved or gone — but it will not
catch a finding id that is absent from the register, and the section check that comes closest does
not move the exit code. Your `findings.py` is doing the half that no key-free route reaches.

**Adopter-visible?** yes — the shipped config is copied by every install, and the third row plus the
register route change what an adopter reads. `adopter_visible: yes` was set at `specify`, unchanged.

**Child fix tasks raised**
- [T-260](T-260-assert-that-a-project-s-config-and-the-shipped-default-still-agree.md) — writing this
  row twice exposed that nothing asserts the two files agree. They differ in exactly one line today
  and only because both were edited by hand in the same minute.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | specified → done | Full lifecycle in one session, under the grant recorded on the handoff resumed 2026-08-23. **No step re-opened the decision** — the owner had already answered it. The measurement refined §1's prediction: the section half is reported and does **not** gate, a third state the record had no word for. The row went into the shipped config as well as this project's, because the person it is written for is an adopter. |
| 2026-08-23 | proposed → specified | **The owner answered the open question on 2026-08-23: no, record the third refusal.** Put as a survey with all three readings priced both ways — decline and record it, test the body-link route first, or build it — and the recorded recommendation was taken unchanged. **Specify is complete; the work is not.** What remains is the third row in `.taskmd/config.md`'s *What this rule has already refused*, in the shape the two existing rows use, and the body-link test that says what a project can do instead. **The *Against* argument in §1 was not defeated and is kept verbatim**, because a fourth request should meet the strongest case for the other side rather than three refusals in a row. |
| 2026-08-23 | → proposed | **Raised on the owner's instruction of 2026-08-23**, after a check of taskmd's readiness for the adopter's audit found this scoped out of [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) with no successor record. **Raised as a `decision` rather than as tool work**, because `.taskmd/config.md` has already refused this exact shape twice on one ground, and the live question is whether a blocked adopter is evidence that moves it. **What taskmd does today was measured rather than assumed**: `finding:` is an unnamed field, so it is carried and never interpreted, and a `check` run over the adopter's 220 tasks raised nothing about it — the failing lint is theirs. **The body-link route is named but not claimed**, because it plausibly covers the document and not the row, and this record is not the place to guess which. |
