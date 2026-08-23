---
id: T-156
title: E-16 — Decide whether a read-only phase can skip the binding
type: decision
status: done
phase: review
parent: T-152
blocked_by: []
related: []
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
adopter_visible: yes
deliverables: []
---

# T-156 — E-16: decide whether a read-only phase can skip the binding

## 1. Specify

**Outcome**
Either `SKILL.md`'s scoping of the binding becomes load-bearing — a phase that only reads does not load
it — or the reason it stays unconditional is recorded where the next person looking at the read path
will find it.

**Why this one**
Finding [E-16](../docs/audits/2026-08-15-context-economy-taskmd.md#e-16) of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), stated there: on a measured
unit of work the binding was the largest item on the read path apart from the task file itself, and
`SKILL.md` already scopes it to *before creating or changing any task* without that scoping doing
anything.

**The finding stands regardless of the remedy's fate.** The measurement is a fact about the read path;
the change is a hypothesis with a named risk, and deciding against it is a legitimate outcome of this
task rather than a failure of it.

**Scope**
- In: `SKILL.md`'s load table and the sentence scoping the binding.
- In: which phases read only, and what a session does when one of them turns out to write after all —
  the risk the finding names, that a rule firing mid-phase is the kind that gets missed.
- In: what share of phases only read. A remedy that fires rarely is worth less than its size suggests.
- Out: cutting the binding's content. The finding is about **when** it loads, not how long it is.
- Out: the second binding. Only one is ever loaded, which the audit records as already working.

**Inputs**
- [E-16](../docs/audits/2026-08-15-context-economy-taskmd.md#e-16) — the measured read path and the risk
- `plugin/skills/taskmd/SKILL.md` — the load table
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the document in question, and its
  *After any write* step, which is what a read-only phase would not need

**Acceptance criteria**
- [ ] The decision names which phases are read-only, and what a session does when one is not
- [ ] The read path is re-measured at decision time on a named unit of work, not carried from the audit
- [ ] If the scoping is made load-bearing, the instruction to load the binding late is stated in one
      place, not repeated per phase
- [ ] Whatever is decided, the finding is recorded as standing
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Is the expected saving worth the mid-phase rule?** Most phases write, so the gain is `M` in
  expectation against `L` on the occasions it fires. Whether to measure the share of read-only phases
  before deciding, or to decide on the risk alone, is the first thing to settle. **The maintainer
  answers, at `specify`.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-measure the read path in characters at decision time, on a named unit of work | The table below |
| 2 | Ask the question the remedy assumes an answer to: **which phases only read?** Test each of the four against its own exit criterion | The finding below — none of them |
| 3 | Decide, and say what the finding is worth once the remedy is refused | The decision below |
| 4 | Stop `SKILL.md` implying a read-only phase exists, since that sentence is what invites the change | `plugin/skills/taskmd/SKILL.md`, the load table |

## 3. Implement

**Re-measured 2026-08-15**, unit of work: the `specify` phase of
[T-157](T-157-b-2-settle-what-context-claims-to-be-enough-for.md), closed this session. Characters,
not bytes:

| Item | Characters |
| :--- | ---: |
| `SKILL.md` | 3,155 |
| `METHOD.md` | 7,443 |
| phase file (`specify`) | 3,340 |
| **binding** | **14,346** |
| **non-task read path** | **28,284** |

**The binding is 50.7% of it** — the audit measured 49.4% eight hours earlier, and the share moved
while the subject was still being ranked. The finding is stronger than when it was written.

**The remedy has no target, and that is the answer.** E-16's change asks that a phase which only reads
should not load the binding. Tested against
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §2, **all four phases end in a write to the
task's record**, and each one's exit criterion is that write: `specify` has acceptance criteria
written and agreed; `plan` has every step naming an output; `implement` has the evidence recorded;
`review` has every criterion met or carrying a child task. METHOD §1.5 says the same thing from the
other side — undocumented progress did not happen. **There is no read-only phase to exempt.** What is
read-only is orientation — asking what to work on next — and orientation loads neither the binding nor
the method.

**Decisions & assumptions**

- **The scoping does not become load-bearing** — 2026-08-15. Not because the risk is too high, which
  is what the finding expected, but because the class it would exempt is empty. The finding's own risk
  field — a rule that fires mid-phase gets missed — never had to be weighed. *Rejected:* a rule
  deferring the binding for `review`, which writes its criteria table like every other phase.
- **`SKILL.md` stops implying otherwise** — 2026-08-15. Its load table said *before creating or
  changing any task*, which reads as though some phases neither create nor change one. That sentence
  is what makes this optimisation look available, so leaving it would leave the question open for the
  next reader to re-open. It now says all four phases end in a write. Costs about 90 characters on a
  tier-2 file and settles a question that cost more than that to ask.
- **The finding stands** — 2026-08-15, and this is why the task said so before knowing the answer. The
  binding is half the non-task read path and grew as a share since it was measured. What is refused is
  one remedy, not the measurement.

**Outputs produced**

`plugin/skills/taskmd/SKILL.md` — the binding's row in the load table. Nothing else changed; the
binding itself is untouched, which was out of scope.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision names which phases are read-only, and what a session does when one is not | met | **None are.** The second half of the criterion cannot arise, and the record says why rather than leaving it blank. |
| The read path is re-measured at decision time on a named unit of work | met | T-157's `specify`, 2026-08-15, in characters: 28,284 non-task, binding 50.7%. |
| If the scoping is made load-bearing, the late-load instruction is stated in one place | n/a | It was not made load-bearing. |
| Whatever is decided, the finding is recorded as standing | met | In `implement`, with the share that grew since the audit took it. |
| The measured outcome is written into this record on the day it is known | met | Above, 2026-08-15. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), finding E-16. `decision` because the finding's own risk field says the change may not be worth making, so the work is the judgement and not the edit. `s`, `medium`: independent of the other children and takeable in any order. |
| 2026-08-15 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review` — in a request covering T-153, T-154, T-155, T-156 and T-157 and **nothing else**. Any task raised from here takes one phase per request unless separately authorised (METHOD §3.1). Recorded in each of the five records because an authorisation kept anywhere else is one a later session can miss or stretch. |
| 2026-08-15 | → done | All four phases run, four criteria met and one `n/a` by the decision itself. **The remedy was refused for a reason the finding did not anticipate**: it exempts read-only phases and the lifecycle has none. The finding's stated risk — a mid-phase rule gets missed — never had to be weighed, and the measured share had grown from 49.4% to 50.7% in the hours between ranking and deciding. Both are material for [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md), which grades this band. |
