---
id: T-238
title: Bring the GitHub binding's coverage declaration into line with the repaired clause
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-232, T-222]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-238 — Bring the GitHub binding's coverage declaration into line with the repaired clause

## 1. Specify

**Outcome**

`github-issues.md`'s coverage declaration carries the heading, the level and the position that
[`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 now fixes — so the contract's own example
of a binding is not the one that breaks its newest rule.

**Where this came from**

[T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) fixed the heading, level
and position on 2026-08-23, because two uninvolved readers had to guess all three. It measured both
shipped bindings against the result and **reported rather than repaired**, for
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s reason: a
binding edited inside the task that changed the contract makes it impossible to see which of the two
moved. This is the repair, in its own record, so the diff shows only the binding.

| | Required | `github-issues.md` today |
| :--- | :--- | :--- |
| Heading | `What the validator cannot check here` | *What this does not cover, and why* |
| Level | `###` | `####` |
| Position | after the mapping section, before the write step | after its own *After any write*, inside the migration-verification material |

**`local-markdown.md` already matches all three**, which is how those values were chosen — they were
measured, not invented. So this record has a working example to move toward and nothing to design.

**Scope**

- In: the heading, the level and the position of that one section, and any pointer to it that moves
- Out: what the declaration **says**. Its content was judged by two readers and is not re-opened here
- Out: the marked-region markers and what they wrap, which T-232 settled
- Out: `local-markdown.md`, which complies

**Inputs**

- [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 *Where the declaration goes* — the three
  values, and the measurement behind them
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the compliant example
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the section to move

**Acceptance criteria**

- [ ] The section carries the required heading at `###`, positioned after the mapping section and
      before *After any write*
- [ ] Every pointer to that section still resolves, checked by running rather than by reading
- [ ] The declaration's text is unchanged apart from the heading line
- [ ] `taskmd check` passes and `tests/test_publishing.py` still finds the region and reads every
      class it names

**Open questions**
- **None.** The three values are fixed by the contract and a compliant example exists.

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
| 2026-08-23 | → proposed | Raised from [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s `review`, whose scope reports a non-compliant binding and does not fix it, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), and **any audit** — unchanged. **No open question**, so unlike [T-237](T-237-the-softening-clause-t-228-repaired-has-a-second-instance-and-an-idiom-behind-it.md) this record does not stop at `specify`: the contract fixes all three values and `local-markdown.md` is a working example of them. **A soft edge from T-232 and not a child**, because T-232's outcome is the contract and the contract is complete; a binding that has not caught up does not make it incomplete, and a hierarchy edge would have held the release's blocker open for an edit to something else. |
