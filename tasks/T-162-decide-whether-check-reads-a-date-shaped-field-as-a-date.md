---
id: T-162
title: Decide whether check reads a date-shaped field as a date
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-095, T-113, T-138, T-141]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-16
updated: 2026-08-18
adopter_visible: yes
deliverables: []
---

# T-162 — Decide whether check reads a date-shaped field as a date

## 1. Specify

**Outcome**
A ruling on whether `check` says anything about a value in a date field that is not a date, and — if
it does — what the class is and which fields it covers.

**Why this one**
Found on 2026-08-16 by writing one, not by looking for one. A script inserting the day's
authorisation rows also tried to refresh `updated:` and had an off-by-one in its match, producing:

```
updated: 2026-08-165        in two task files
updated: 2026-08-161        in a third
```

`check` reported `OK` over all three, and `index` regenerated without complaint. The damage was
caught by reading the script's own output, which is the accident this project usually calls a defect
in the instrument.

**Confirmed deliberately afterwards**, because an accident is not a specimen:

```
updated: 2026-13-99   ->   OK - 161 task(s), ... 2370 front-matter value(s)      exit 0
```

Month 13, day 99, exit 0.

**Why it is a `decision` and not a `fix`.** Three things are genuinely open and the answer to the
first may be *nothing*:

- **Dates are not a vocabulary.** Every field `check` validates today has an enumerated set in the
  config, and a date has none — so this is a new *kind* of field rule, not a new row. Whether taskmd
  wants typed fields at all is the question, and [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)
  is the same shape from a different direction. They may want one answer between them.
- **A wrong-but-well-formed date is the commoner fault and is not detectable.** `2026-08-15` where
  the author meant `2026-08-16` passes any check that could be written. So the class catches
  malformed values only, and the honest question is whether that is worth a rule — the
  [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) precision argument.
- **Which fields.** `created` and `updated` are the shipped template's, but a project's own config
  names its fields, and taskmd has no way to know which of them are dates unless the config says so —
  which is a config key, and therefore a cost paid by every adopter.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`) — a value the tool silently accepts is one nobody learns is wrong.

**Scope**
- In: whether malformed values in date-shaped fields are reported at all, and as `problem` or
  advisory.
- In: how such a field is *identified*, given that only a project's config could say.
- In: whether this and [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) are one
  decision about typed fields rather than two.
- Out: dates being *wrong* rather than malformed. Undetectable, and saying so is part of the answer.
- Out: any change to the shipped template's fields.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_vocabularies`, and how a field rule is expressed.
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the schema keys an adopter writes.
- [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) — the neighbouring question.
- The two specimens above; both reproduce in one command.

**Acceptance criteria**
- [ ] The ruling is stated as one of *report as a problem*, *report as an advisory*, or *do not
      report*, with the rejected options named
- [ ] The ruling says how a date field is identified, and whether that costs a config key —
      answered against [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md), not around it
- [ ] It is reconciled with [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s
      refusal: either the same answer for the same reason, or a stated reason the refusal does not
      reach this case
- [ ] The rule is run over a real corpus before it is ruled on, in both directions — what it fires on,
      and what it stays silent on — with the counts as of the run
- [ ] A known positive is used. A rule measured only on clean data has not been measured
- [ ] `check`'s present silence is reproduced rather than quoted from §1

**Open questions**
- **Is this one decision with T-146 or two?** Decide at `specify`. Both ask whether taskmd's schema
  describes fields beyond an enumerated vocabulary, and answering them apart risks two mechanisms for
  one idea — which is the fault [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)
  had to repair in the marked-list guard four days after T-134 shipped it.

  **Answered 2026-08-18: two, and the question is settled by a fact rather than a preference —
  [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) is closed.** It ruled **no** on
  a field-keyed rule and recorded the refusal in the shipped schema's *What this rule has already
  refused*. So the risk this question names is real and now has a shape: the danger is not that the
  two are decided apart, it is that this one re-opens what that one closed.

  **It does not, and the line is precise.** T-146's refusal turns on one sentence: both refused
  capabilities *"needed the tool to learn a fact about where a task has got to. That is project
  vocabulary, and vocabulary is a key in this file."* A rule keyed on the **value's shape** learns no
  such fact. It never asks which field is a date; it asks whether *this value* is a date-shaped string
  that is not a date, and that question is the same in every project without anything being declared.
  So the refusal does not reach it — not as an exception to T-146, but because T-146 was about naming
  **fields** and this names **none**.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s outcome and the refusal it wrote into the schema, and say whether it reaches this case | The answered question in §1 |
| 2 | Reproduce `check`'s present silence rather than quoting §1's specimen | The command and its output, in §3 |
| 3 | Write the rule as a probe and run it on this repository — both directions: what fires, and what stays silent, with the fields date-shaped values actually occupy | The counts, in §3 |
| 4 | **Seed known positives** and re-run, because a rule measured only on clean data has not been measured | The three seeded values and what the probe said, in §3 |
| 5 | Run the same probe on the sibling corpora, to test the false-positive claim somewhere this project did not write the data | Per-corpus counts, in §3 |
| 6 | Rule, and name the rejected options | The ruling, in §3 |

**Step 4 is the one that makes step 3 mean anything.** This repository's dates were repaired on
2026-08-16, so the corpus is clean by construction and a silent probe and a broken one score alike.

**Decisions taken at `plan`**

- **The rule is keyed on the value, not the field.** — This is the whole design, and it is what lets
  the task have an answer other than *no*. *Rejected: a `date_fields` config key*, which is
  T-146's refused shape exactly and costs every adopter an error on upgrade. — 2026-08-18
- **Implementing it is a child task, not this one.** — This is typed `decision` and §1 argues for
  that type. A ruling that also ships the code makes the ruling unreviewable — the reader cannot tell
  whether the rule was adopted because it was right or because it was already written. — 2026-08-18

**Outputs this task will produce**

- tasks/T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md — §3, the ruling and its
  measurements

## 3. Implement

### Step 2 — the silence, reproduced

Seeded `updated: 2026-13-99` into a real task file in this tree and ran the shipped command:

```text
OK - 183 task(s), 915 field value(s), ... 2710 front-matter value(s)
EXIT=0
```

Month 13, day 99, exit 0 — and `check`'s entire output mentions the string *date* zero times. Reverted
immediately afterwards. §1's specimen was from 2026-08-16 and a different corpus size; this one is
today's.

### Steps 3–5 — the rule run in both directions, on three corpora

The probe reports a front-matter value matching `^\d{4}-\d{1,3}-\d{1,3}$` that `date.fromisoformat`
refuses. It reads no config and names no field.

| Corpus | Files | Front-matter values | Date-shaped | Malformed | Fields holding a date-shaped value |
| :--- | ---: | ---: | ---: | ---: | :--- |
| this repository | 185 | 2,792 | 366 | **0** | `created`, `updated` |
| the deck-building sibling | 181 | 2,662 | 358 | **0** | `created`, `updated` |
| the diagram sibling | 8 | 106 | 14 | **0** | `created`, `updated` |

**The last column is the false-positive answer, and it is the column that was not predictable.** The
worry about a value-keyed rule is that some other field somewhere holds a date-shaped string it does
not mean as a date. Across 374 files and 5,560 front-matter values in three independently written
corpora, **no field other than `created` and `updated` carries one**. So the rule needs no field list
because the data does not have one to give.

**Step 4 — the known positives.** With §1's own two shapes plus the deliberate one seeded into a copy:

```text
MALFORMED DATE  T-001-...md: updated: 2026-08-165 is not a date
MALFORMED DATE  T-002-...md: updated: 2026-08-161 is not a date
MALFORMED DATE  T-003-...md: updated: 2026-13-99 is not a date
--- read 185 files, 2792 front-matter values; 366 date-shaped, 3 malformed
```

Three seeded, three caught, and the two that were the original accident are among them. Without this
step the table above is a rule that has only ever succeeded.

### Step 6 — the ruling

**`check` reports a date-shaped value that is not a date, as a `problem`, keyed on the value and never
on the field name.**

**Why a problem and not an advisory.** The nearest existing class is `VOCABULARY`, which reports a
value outside its allowed set and is a problem. A malformed date is the same shape — the set is
*real dates* rather than an enumerated row — and unlike `CONFIG DRIFT`, which is advisory because
pinning is a legal choice, there is no reading on which `2026-13-99` is something the author meant.
The measured incidence of 0 in 374 files is what makes this safe to make a problem: no corpus
observed is broken by it.

*Rejected: an advisory.* It would match `CONFIG DRIFT`'s form, but that class is advisory because it
reports a **choice**; this reports an **error**, and an advisory teaches a reader to skim it.
*Rejected: reporting nothing.* That is T-146's answer, and it was right there for a reason that does
not hold here — no key is needed, so the arithmetic that justified the refusal never runs.
*Rejected: keying on a `date_fields` config key.* T-146's refused shape, at T-106's price.

**What the ruling explicitly does not claim.** A date that is well-formed and wrong — `2026-08-15`
where the author meant `2026-08-16` — is undetectable by this or any rule, and it is the commoner
fault. §1 said so and the ruling does not pretend otherwise: this catches values that are not dates,
which is a smaller class than values that are not *the* date.

**Decisions & assumptions**
- Both `plan` decisions held. — 2026-08-18
- **Assumption, recorded as one**: the three corpora are all maintained by the same person, so the
  false-positive evidence is weaker than 374 files suggests. It is the widest sample reachable, and
  the child task can widen it if an adopter's corpus disagrees. — 2026-08-18

**Outputs produced**
- tasks/T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md — §3

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The ruling is one of the three, with the rejected options named | **met** | §3 step 6: report as a **problem**. Three rejections named — advisory, nothing, and a `date_fields` key |
| Says how a date field is identified, and whether that costs a key, answered against T-106 | **met** | It identifies none. The rule reads values, so T-106's arithmetic never runs — which is the finding rather than a way around it |
| Reconciled with T-146's refusal — same answer, or a stated reason it does not reach | **met** | §1's answered question. T-146 refused rules needing the tool to learn *project vocabulary*; a value-shaped rule learns none. The distinction is quoted from the refusal itself, not asserted |
| Run over a real corpus in both directions, counts as of the run | **met** | §3, three corpora, 374 files, 5,560 values. Both directions: 0 fired, and date-shaped values occupy no field beyond `created`/`updated` |
| A known positive is used | **met** | Three seeded, three caught, including both shapes from the original accident. This is the step that makes the zeros mean something |
| `check`'s present silence reproduced, not quoted | **met** | §3 step 2, run today on this tree and reverted |

**Open questions, re-read before closing** (procedure step 5)

§1's only question is answered above and its answer turned on a fact — T-146 is closed — rather than
on a preference. Nothing here is addressed to anyone else. **The ruling is not self-executing**, and
that is carried to a child task rather than left implied.

**Child fix tasks raised**
- [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) — implement the ruling

## Log


| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | `specify` through `review` in one session under the standing grant. **Ruled: `check` reports it, as a problem, keyed on the value and never on the field name.** That keying is the whole answer — it is what clears [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s refusal, which turned on a rule needing to learn *project vocabulary*, and it means [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s arithmetic never runs because no config key is asked for. Measured in both directions on three corpora — 374 files, 5,560 front-matter values, 0 malformed — and the column that decided it was the last one: no field other than `created` and `updated` holds a date-shaped value anywhere, so the rule needs no field list. Three known positives seeded and all three caught, without which the zeros would have measured nothing. Implementation is [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md), kept separate so the ruling stays reviewable. |
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-16 | → proposed | Raised while writing the unattended batch's authorisation rows, from a real accident rather than a review: a script produced `2026-08-165` in two files and `2026-08-161` in a third, and `check` and `index` both passed over them. Confirmed with a deliberate specimen (`2026-13-99`, exit 0) because an accident is not evidence. **Explicitly outside that batch's authorisation**, which names four tasks and excludes what they raise; this is filed and left for the maintainer. `medium` and `s`, and typed `decision` because the answer may be that nothing is added — the detectable half is malformed values only, and a date that is merely wrong passes anything. |
