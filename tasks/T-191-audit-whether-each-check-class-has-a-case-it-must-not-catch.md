---
id: T-191
title: Audit whether each check class has a case it must not catch
type: audit
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-151, T-150, T-100]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: []
---

# T-191 — Audit whether each check class has a case it must not catch

## 1. Specify

**Outcome**
For every class `check` reports, a statement of whether its fixtures include a case it must **not**
catch, and whether that case has been shown able to fire. Each gap becomes its own child task; none
is filled here.

**Why this one**
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) ruled that a check needs
such a case and that the case counts only once it has been shown it could have spoken. It wrote the
rule and deliberately did not apply it: its own §1 *Out* said auditing the existing checks is a real
piece of work and would be raised from it.

**The rule's condition is what makes this an audit rather than a checklist.** Confirming that a
fixture *has* a quiet case is a grep. Confirming the quiet case *can* fire means breaking it on
purpose, one class at a time, and watching the alarm arrive — which is the only step that separates a
guard from evidence. This project has two measured instances of the difference:
[T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) §3's four tests
that pass by asserting silence, called guards rather than evidence in that record, and
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) §3's negative fixture
that could not fire at all because the check consumed the line under its header as a delimiter.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`).

**Scope**
- In: every class `check` reports — the problem prefixes and the advisories. The set is read from the
  code, never from a list in a document
- In: for each, whether a must-not-fire case exists, and whether it has been shown able to fire
- Out: **filling any gap.** A finding is never fixed where it is found (METHOD §5); each gap is a
  child task
- Out: re-opening [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s rule or
  its condition
- Out: classes reported by something other than `check` — the launchers' errors and the config
  loader's, which are not check classes

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — the classes, read from the code
- `tests/fixtures/` and `tests/test_cli.py` — the fixtures and what asserts about them
- [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) — the rule and its
  condition
- [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) — a worked instance
  of the condition failing

**Acceptance criteria**
- [ ] The class set is **derived from the code** and the derivation is shown, so a class added since
      cannot be missing from the audit
- [ ] Every class has a row, and the rows sum to the derived set — a class with nothing to say still
      has a row saying that
- [ ] Each *has a quiet case* claim names the fixture and the assertion, not the intention
- [ ] Each *can fire* claim quotes what happened when it was made to fire; a class whose quiet case
      was not exercised is recorded as unproven rather than as passing
- [ ] Every gap is a child task, and the audit closes only when each is resolved (`audit.md` step 5)

**Open questions**
- **Do the advisories carry the same rule?** T-151's argument turns on noise getting a check switched
  off, and it names *a check that moves an exit status* as the case with no tolerance for it. An
  advisory moves nothing, so the rule may bind more weakly there or not at all. **Decide at
  `specify`** — the answer changes the size of the audit and should be taken before the rows are
  written, not discovered while writing them.

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
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) raised it. **It does not answer §1's question**, which sizes the audit and is the owner's. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s review, as that task's §1 said it would be. Typed `audit` rather than `fix` because it examines a body of work for a problem nobody has alleged of any particular class, and its findings become children rather than repairs (METHOD §5). `m` rather than `s`: the condition means exercising each quiet case, not grepping for one. |
