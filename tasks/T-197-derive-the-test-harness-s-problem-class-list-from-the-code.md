---
id: T-197
title: Derive the test harness's problem-class list from the code
type: fix
status: proposed
phase: specify
parent: T-191
blocked_by: []
related: [T-151, T-139]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-197 — Derive the test harness's problem-class list from the code

## 1. Specify

**Outcome**
`CheckFailsOnEveryClassItClaims.LABELS` is read from `plugin/skills/taskmd/taskmd/cli.py` rather than
transcribed into `tests/test_cli.py`, so a class added to the code is asserted silent in every
fixture but its own with nothing edited in the test file — and a class the derivation cannot see
fails a test rather than passing unnoticed.

**Why this one**
Finding **F-1** of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md).
That audit derived the class set from the code and got **21**; `LABELS` names **14**, one of which
(`CONFIG ERROR`) is not a `check` class at all. So thirteen classes get a cross-fixture silence
assertion and eight do not, and nothing anywhere compares the two lists.

**The repository already does this correctly one file over.** `tests/test_publishing.py` reads
`cli.ADVISORY_PREFIXES` from the module, which is why the advisory half of the set cannot drift.
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) built that home precisely so a prose list could
be checked against it. The problem half has the same need and none of the mechanism.

**The derivation this needs already exists.**
[T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) added `check_classes()` to
`tests/test_publishing.py` on 2026-08-21 — it reads the problem prefixes out of `cli.py`'s source and
unions them with `ADVISORY_PREFIXES`, and it is the first derivation of the problem half in the
suite. **Reuse it rather than writing a second**: two derivations of one set is the defect this task
exists to remove, arriving by the door it was watching.

**What the risk actually is.** No present assertion is wrong. The failure is in the future and is
silent: a class added to `cli.py` is never asserted absent from the other fixtures, so a check that
starts firing spuriously on an unrelated fixture is not reported by anything. That is the shape
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s rule exists to prevent.

**Scope**
- In: deriving the problem-class set in the test harness, the same way `ADVISORY_PREFIXES` is derived
- In: whether the advisory classes belong in the same cross-fixture assertion, or have their own
- Out: adding fixtures. A class with no fixture of its own is a different question, and T-191 found
  none
- Out: `CONFIG ERROR`, which is the config loader's class and not one `check` owns

**Inputs**
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) §3 — the derivation,
  the 21, and the two counts side by side
- `tests/test_cli.py` — `CheckFailsOnEveryClassItClaims`
- `tests/test_publishing.py` — `check_classes()`, the derivation to reuse, and the `ADVISORY_PREFIXES` read that is its precedent

**Acceptance criteria**
- [ ] The harness's class list is read from the code, and the derivation is the one thing a reader
      has to trust
- [ ] **The derivation is shown to fail when it should**: a class present in the code and unreachable
      by the derivation makes a test fail, demonstrated by breaking it on purpose and quoting what
      the run printed
- [ ] The count the harness uses and the count T-191 derived are stated together, and agree
- [ ] Whether the four advisory classes join the same assertion is decided, with the rejected option
      named

**Open questions**
- **Should the cross-fixture assertion cover the advisory classes too?** The owner answered the
  parent question this way for T-191 — every class the validator prints is audited, advisory or not
  — so the same reasoning may carry. It is asked rather than assumed because the assertion has a
  cost the audit did not: an advisory that legitimately fires on several fixtures would make the
  loop wrong rather than the fixture.

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
| 2026-08-21 | → proposed | Raised as finding F-1 of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md). `medium` and `s`: the repair is small and the mechanism already exists in `tests/test_publishing.py`, but the failure it prevents is a silently absent assertion, which is the class of defect the audit was run to find. A child of T-191 rather than a soft link, because that audit does not close until this resolves (`audit.md` step 5). |
