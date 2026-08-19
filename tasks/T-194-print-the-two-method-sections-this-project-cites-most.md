---
id: T-194
title: Print the two method sections this project cites most
type: fix
status: proposed
phase: specify
parent: T-093
blocked_by: []
related: [T-047, T-028]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-19
updated: 2026-08-19
adopter_visible: yes
deliverables: []
---

# T-194 — Print the two method sections this project cites most

## 1. Specify

**Outcome**
`check` reports no `SECTION REF` line on this repository, because every section this project cites
is a section the target document prints.

**Why this one**
[T-093](T-093-decide-whether-check-resolves-a-section-reference.md) shipped the class and it reports
seven lines here, all real:

```text
plugin/skills/taskmd/docs/METHOD.md has no section 3.1; 136 reference(s) name it
plugin/skills/taskmd/docs/METHOD.md has no section 3.3; 74 reference(s) name it
plugin/skills/taskmd/docs/method/review.md has no section 1, 2, 4, 5; 1 reference each
tasks/T-047-...md has no section 3.2; 1 reference(s) name it
```

**The first two are the interesting ones and they are not a typo.** `METHOD.md` numbers its §3
subsections and prints only §3.2, because §3.1 and §3.3 are the two rules carried in tier 1
instead ([T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)), and
METHOD.md says so in prose. So the document explains the absence and still leaves 210 citations
pointing at nothing a reader can find. **A pointer is not a copy**, which is what makes this
repairable without re-opening T-047: a heading numbered 3.1 whose body says *this rule binds before
this document loads, so it lives in your project's always-loaded conventions* states where the rule
is, not what it is.

**The other five are ordinary.** `review.md`'s procedure is a numbered list under an unnumbered
heading, so the citations of *procedure step n* have no section to resolve against; and one task
record is cited at a §3.2 it does not have.

**Requirements served**
R-16, and `CLAUDE.md`'s standing requirement that `check` is clean on this tree.

**Scope**
- In: the seven, each resolved either by the document gaining the section or by the citation being
  corrected
- In: which of the two repairs each case gets, decided per case and not by a blanket rule
- Out: re-opening [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md).
  The two rules stay where they are; this is about whether `METHOD.md` prints a numbered heading
  saying so
- Out: promoting `SECTION REF` from advisory to problem. That becomes available once this closes and
  is its own decision, named in
  [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3
- Out: the 1,885 marks the rule binds to nothing. They are reported as skipped by design, and
  reducing that number is a different task with T-093's measurements to beat

**Inputs**
- [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3 — the class, the seven, and
  the rule that produced them
- `plugin/skills/taskmd/docs/METHOD.md` §3 — the section that prints 3.2 and not 3.1 or 3.3
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) — why those two
  rules are not in that document
- `tests/test_budget.py` — tier 1, in case a repair is proposed that touches `CLAUDE.md`

**Acceptance criteria**
- [ ] `taskmd check` on this repository prints no `SECTION REF` line, shown as output
- [ ] **No rule is copied.** If `METHOD.md` gains headings, their bodies point at where the rule
      lives and do not restate it — checked by reading them against `CLAUDE.md`'s text, not by
      intending it
- [ ] Tier 1's character count is unchanged, from `tests/test_budget.py`
- [ ] Each of the seven says which repair it got and why, so a reader can tell a corrected citation
      from a corrected document
- [ ] A test holds the result, so the seven cannot come back unnoticed

**Open questions**
- **Does `METHOD.md` gaining headings for 3.1 and 3.3 weaken what T-047 achieved?** The claim is
  that it does not, because a heading with a pointer is not a copy of a rule — but T-047's whole
  point is that those two rules must not have a second home, and *pointer* is what every second home
  calls itself at the start. **The owner decides**; the alternative is to correct 210 citations
  instead, which is more work and moves the convention rather than the document.

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
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) raised it. **It does not answer §1's question**, which asks whether a numbered heading in `METHOD.md` weakens what [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) achieved — a judgement about the project's most carefully guarded rule, and the owner's. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-093](T-093-decide-whether-check-resolves-a-section-reference.md)'s review, from what the new class reports on this repository. Not fixed there: §1 of that task puts renumbering out of scope, and a finding is never repaired where it is found (METHOD §5). `s` in effort and `medium` in value — the work is small, and what it unblocks is promoting the class to a problem, which is where its worth actually is. |
