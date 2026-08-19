---
id: T-188
title: Report a counted set written into prose that the code owns
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-139, T-134, T-184]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: []
---

# T-188 — Report a counted set written into prose that the code owns

## 1. Specify

**Outcome**
A ruling on whether a **count** of a set the code owns, written into prose, is worth a rule — and if
it is, the rule. The one instance is repaired either way.

**Why this one**
Found by [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) adding a seventeenth problem
prefix and going to check what the addition made false.
[`tests/test_publishing.py`](../tests/test_publishing.py) line 244 reads:

> **A marker is a claim of completeness, not a claim of importance.** It is why the fifteen problem
> prefixes are not marked

There were **sixteen** before T-184 and there are **seventeen** now, so the sentence was already
wrong when T-184 read it. The argument is sound and is not what is in question; the number inside it
is a derived value that was written down.

**This is [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s
fault class one step sideways, and that is why it is a `decision` rather than a `fix`.** T-139
generalised T-134's guard from the command list to any **marked list of members**, and this is
neither: it names no member, so no pattern reading names can see it, and it sits inside the very
docstring explaining why that set carries no marker. A count is what a list of members degrades into
when somebody decides not to enumerate — which makes it the shape a completeness guard is least
likely to cover, and the shape most likely to be left alone by a reader, because a number in an
argument reads as background rather than as a claim.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`) — a statement the tooling silently accepts is one nobody learns is
wrong.

**Scope**
- In: the ruling — report such a count, or do not, with the rejected options named.
- In: the one known instance, corrected whichever way the ruling goes.
- In: whether the honest repair is a rule at all, or removing the number from the sentence, which
  loses nothing the argument needs.
- Out: re-opening [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s
  marked-region mechanism. That is closed and this does not touch it.
- Out: counts of things the code does **not** own. A sentence counting task files or adopters is a
  different question and probably a worse one.

**Inputs**
- [`tests/test_publishing.py`](../tests/test_publishing.py) — the instance, and the guard that could
  not see it
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and
  [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  existing mechanism and its stated boundary
- `plugin/skills/taskmd/taskmd/cli.py` — the seventeen prefixes, which is the set in question

**Acceptance criteria**
- [ ] The ruling is stated as *report it*, *do not report it*, or *remove the counts instead*, with
      the rejected options named
- [ ] The corpus is swept for other written-down counts of code-owned sets before ruling, and the
      number found is stated — a rule justified by one instance is a rule justified by an anecdote
- [ ] If a rule is adopted, it is shown **failing** on the known instance before it is fixed
- [ ] The instance at `tests/test_publishing.py:244` is correct at close, whichever way the ruling
      goes
- [ ] The ruling says why this is or is not the same decision as
      [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s, in
      the terms that record uses

**Open questions**
- **Is a spelled-out number worth a rule, or is the answer to stop writing them?** The instance
  spells it in words, inside an argument that does not need the figure at all: *the problem prefixes
  are not marked* carries the whole point. If the corpus sweep finds one instance, removing it is
  the cheaper and more honest repair, and a rule guards a class with no members. Decide at
  `specify`, after the sweep — **the sweep is what settles it, not a preference**, and the criterion
  above orders them that way for that reason.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19, when resuming the handoff that carried it: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. Every grant before it excluded what its tasks raised, by name, so this is a change of boundary and not a reading of the old one. It reaches this task because [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) raised it. **It does not answer the open question above** — the grant is permission to run the lifecycle, and §1's question is settled by the sweep the criteria require, not by anyone's authority. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md)'s review, from adding the seventeenth problem prefix and checking what that made false. Not fixed there: a review that repairs what it finds destroys the record of what was wrong (METHOD §5), and the one-word repair is the least interesting half. Typed `decision` because the answer may be that nothing is added — one instance, spelled in words, inside a sentence that does not need the number. |
