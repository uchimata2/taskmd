---
id: T-226
title: Decide whether taskmd should print the class list a binding author needs
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-222, T-197, T-191]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-226 — Decide whether taskmd should print the class list a binding author needs

## 1. Specify

**Outcome**
An answer, recorded, on whether taskmd gains a way to print the set of classes `check` can report —
and if so, what shape it takes.

**Why this one**
`BINDING.md` §4 requires a binding to name the classes its mapping makes impossible, in the
validator's own names. **Nothing an adopter installs tells them what those names are.** The set has
one home and it is source code — the literal at each `problems.append` site and the
`ADVISORY_PREFIXES` constant, both in `taskmd/cli.py`. On 2026-08-22
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) repaired the
clause to say so, which is honest and is not the same as reachable: it asks a binding author to read
Python to write Markdown.

**The alternative is not a document.** A list written into any document is the per-check coverage
table §4 refuses, with its second column removed — falsified by the same event, and one class was
added to this validator on 2026-08-22. So the only shapes that do not re-create the defect are ones
that **derive** the set: a command that prints it, or nothing.

**Scope**
- In: whether to add it, and if yes its shape — a subcommand, a flag on `check`, or something else
- In: what it costs. A fifth command is adopter-visible surface and this project has kept to four
- In: whether `tests/classes.py`'s derivation moves into the package or stays in `tests/`. It is the
  derivation that exists; a command would need one, and two would be the defect T-191 found
- Out: building it. This task answers whether and what shape; the build is its own task if the answer
  is yes
- Out: changing what the classes are

**Inputs**
- `tests/classes.py` — the derivation that exists today, and its recorded reasons
- `plugin/skills/taskmd/taskmd/cli.py` — the two places the names live
- `plugin/skills/taskmd/docs/BINDING.md` §4 *Where the class names come from* — the clause that
  currently sends a reader to the source

**Acceptance criteria**
- [ ] The answer is recorded with its reason, and the rejected shapes are named
- [ ] If the answer is yes, the shape is specific enough that a build task could start from it
- [ ] Whether the derivation gets one home or two is answered either way — a yes that leaves two
      derivations has re-created T-191

**Open questions**
- ~~**Is a fifth command worth it, against reading two places in `cli.py`?** — the project owner. The
  recommendation is **yes, as `check --classes` rather than a fifth command**: it adds no verb to the
  surface, it sits on the command that owns the classes, and it makes the clause's instruction
  runnable. The cost is one flag and moving the derivation into the package.~~ **Answered by the
  owner on 2026-08-22: yes, as `check --classes`.** See the Log row of that date — this record's
  outcome is that answer, so what is left here is the lifecycle and not the decision.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task:** the decision exists, so what remains is the lifecycle and a build task, not the choice. **Its third criterion is not answered by the decision and is the part with teeth** — a shipped flag needs a derivation in the package, `tests/classes.py` already has one, and two derivations is the defect T-191 found. |
| 2026-08-22 | (no change) | **The owner answers the question this record exists to ask: yes, as `check --classes`.** Answered 2026-08-22. It adds no verb to a surface this project has held at four commands, it sits on the command that owns the classes, and it makes runnable an instruction `BINDING.md` §4 currently gives in the form *go and read `cli.py`*. *Rejected: a fifth command* — adopter-visible surface for something only a binding author needs. *Rejected: nothing, and leave the clause pointing at source* — honest, and it asks somebody to read Python in order to write Markdown. *Rejected: a list in a document* — the per-check coverage table §4 refuses, one column narrower. **The third criterion is not answered by this and is the part with teeth**: the derivation lives in `tests/classes.py`, a shipped flag needs one in the package, and two derivations is the defect T-191 found. **The outcome of this record now exists**, so what remains here is the lifecycle and a build task, not the decision. |
| 2026-08-22 | → proposed | Raised from [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md), whose §1 puts changing the validator out of scope. The repaired clause tells a binding author where the class names live and that place is source code, which is the honest answer and is not a usable one — so the gap is recorded as a decision rather than left as a shrug in a shipped document. `decision` by the schema's own test: the outcome is an answer somebody else could act on, and the change follows from it. |
