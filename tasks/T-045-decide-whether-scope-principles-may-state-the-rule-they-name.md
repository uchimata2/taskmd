---
id: T-045
title: Decide whether SCOPE §2 principles may state the rule they name
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-017, T-027]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-045 — Decide whether SCOPE §2 principles may state the rule they name

## 1. Specify

**Outcome**
A decided, written answer to whether `docs/SCOPE.md` §2 *Principles* may state a method rule in full,
or must name it and point at `docs/METHOD.md` — applied to principle 1's closing qualification, which
is where the question was found.

**Why this one**
Raised by [T-027](T-027-give-the-design-rule-one-home.md), whose criterion 1 asked for the
qualification to survive in exactly one file and could not be met. After T-027 removed `CLAUDE.md`'s
copy, three remain:

| Hit | Role |
| :--- | :--- |
| `docs/METHOD.md` §4 | the one home, decided by the maintainer |
| `docs/method/rationale.md` | explains *why* the rule is phrased that way — a different job |
| `docs/SCOPE.md` §2, principle 1 | states the qualification in full, near-verbatim |

**The sanction that was invoked for the third does not reach it.** T-027's scope put the
SCOPE↔METHOD overlap out as "settled in T-017". But
[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) settled §3
**requirements** against the method — its three rows are R-6, R-7 and R-8 — and the rule it produced
is written into §3: *a requirement says what must be true, never what to do.* §2 **Principles** was
never in T-017's scope and is a different register: §2 says it holds "three rules", not three
properties, and a rule is exactly the thing §3's test excludes.

**§2's own header already claims what is at issue.** It reads *"Three rules that every requirement
below is an application of. They are listed once, here."* `docs/METHOD.md` §4 makes the second
sentence false, and it has been false since METHOD was written.

**Requirements served**
R-1 (`docs/SCOPE.md`); §2 principle 3, *point, don't restate*.

**Scope**
- In: whether §2 principles may state a rule in full; the general answer, and principle 1 as the case
  that raised it.
- In: principle 2, which is the design rule itself under another heading and stands or falls with the
  same answer.
- Out: §3's requirement-versus-rule division. T-017 decided it, T-027 re-checked it, and it is not in
  question here.
- Out: `docs/method/rationale.md`, whose hit is an explanation rather than a statement.
- Out: any change to the rule itself.

**Inputs**
`docs/SCOPE.md` §2 and §3, `docs/METHOD.md` §4,
[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md),
[T-027](T-027-give-the-design-rule-one-home.md) §3 and §4.

**Acceptance criteria**
- [ ] A written rule for whether a §2 principle may state what it names, in whichever document owns
      that convention — and it is the same document that owns §3's rule, or the two are explicitly
      distinguished
- [ ] Principles 1 and 2 resolved consistently with it
- [ ] §2's "They are listed once, here" is either true afterwards or gone
- [ ] If the answer is "leave it", the reasoning is recorded where the next reviewer meets it — this
      is the second task to arrive at these three lines, so an unrecorded acquittal will bring a third

**Open questions**
- Whose call, and which way — the maintainer's. Both readings are live, and the honest summary is
  that this is T-017 one register up: SCOPE §2 is either the place the principles are *stated* (and
  METHOD applies them) or the place they are *named* (and METHOD states them). Deciding which is
  cheap; leaving it undecided has now cost two tasks. — maintainer.

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
| 2026-08-07 | → proposed | Raised by T-027's review, which could not meet its criterion 1 because two of the three surviving copies are protected by that task's own scope. Not fixed there (METHOD §5). The finding is narrow and checkable: T-017's settlement is written into §3 and is about requirements, so §2's principles are unsettled rather than sanctioned — and §2's own "listed once, here" has been false since `docs/METHOD.md` §4 was written. |
