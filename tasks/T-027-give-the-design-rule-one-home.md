---
id: T-027
title: Give the design rule one home
type: fix
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-017]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-06
deliverables: []
---

# T-027 — Give the design rule one home

## 1. Specify

**Outcome**
"Store the forward edge; derive the rest" — and in particular its *compels the second write*
qualification — is written out in full in exactly one place, and the other documents point at it.

**Why this one**
Raised as **F-1** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 2 and 4. The rule is currently stated in full, with its own worked qualification, in three
documents:

- `CLAUDE.md` §*The one design rule*
- `docs/SCOPE.md` §2, principles 1 and 2
- `docs/METHOD.md` §4 and its *Store the forward edge; derive the rest* subsection

with a fourth treatment in `docs/method/rationale.md` §*Why the inverse of a link is never written
down*. The near-verbatim part is the qualification: all three say that the rule forbids a design
that **compels** a second write rather than a user who makes one, and all three reach for the same
"collapses to a single entry" phrasing.

**Two of those copies are already sanctioned; the third is not.** `docs/SCOPE.md` §3 settles the
SCOPE↔METHOD overlap deliberately — a requirement states a property, the method states the rule that
gives it that property, and their agreeing is what conformance *is*
([T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md)). Nothing settles
`CLAUDE.md` carrying a third full statement, and `CLAUDE.md` itself rules it out: *"The method has
one home: `docs/METHOD.md` — ... it is not restated here; if you find it written out somewhere else,
that copy is the defect."*

**Why it costs more than an ordinary duplicate.** `CLAUDE.md` is loaded on every turn, so this copy
is paid for on every turn (clause 4), and it is the project's own thesis — delete duplication rather
than policing it — violated in the document that states the thesis.

**Requirements served**
R-1, R-21 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: `CLAUDE.md` §*The one design rule*, and whatever pointer replaces it.
- Out: the SCOPE↔METHOD overlap, which is settled in T-017 and is not a defect.
- Out: `docs/method/rationale.md`, which explains *why* the rule holds rather than restating it —
  that is the division METHOD §7 is built on.
- Out: any change to the rule itself. This is about where it lives, not what it says.

**Inputs**
`CLAUDE.md`, `docs/SCOPE.md` §2 and §3, `docs/METHOD.md` §4,
[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-1.

**Acceptance criteria**
- [ ] The qualification is written in full in exactly one file; a grep for its distinctive phrasing
      returns one hit outside task records
- [ ] `CLAUDE.md` still tells a new session that the rule exists and where to read it — the fix is a
      pointer, not a deletion, since a spine that omits the rule entirely fails a different job
- [ ] `CLAUDE.md`'s own "if you find it written out somewhere else, that copy is the defect"
      sentence is true of the file that contains it
- [ ] `docs/SCOPE.md` §3's sanctioned overlap is left intact and is explicitly re-checked, so this
      fix does not quietly reopen T-017

**Open questions**
- Which file is the one home — `docs/METHOD.md` §4 is the obvious candidate, since METHOD is already
  declared the method's one home. Confirm rather than assume, because `docs/SCOPE.md` §2 principle 2
  states it as a *principle* the requirements apply, which is a different role. — maintainer.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-06 | → proposed | Raised as F-1 from the T-026 audit, clauses 2 and 4. Not fixed where it was found (METHOD §5). The finding is narrow on purpose: two of the three copies are settled by T-017 and are not in scope here. |
