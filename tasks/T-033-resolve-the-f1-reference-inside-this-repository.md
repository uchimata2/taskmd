---
id: T-033
title: Resolve the F1 reference inside this repository
type: fix
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-005, T-013]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-06
updated: 2026-08-06
deliverables: []
---

# T-033 — Resolve the F1 reference inside this repository

## 1. Specify

**Outcome**
Every tracked document that depends on "F1" states what it is, so a reader who has only this
repository can follow the argument — or the label is replaced by the fact it stands for.

**Why this one**
Raised as **F-7** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 1 and 3. Three tracked files lean on a label that is defined nowhere a reader can reach:

| File | How it is used |
| :--- | :--- |
| `docs/BRIEF.md` §*Interop* | *"see that repository's improvement brief, F1"* — an unnamed external document |
| `docs/BINDING.md` §4 | *"The F1 failure above"*, in a table row — the paragraph above describes the failure but never labels it F1 |
| `tasks/T-005` | Twice, including **acceptance criterion 1**: *"The handoff F1 outcome is known before this is designed"* |

**It is not the label discipline working.** `CLAUDE.md` allows a tracked file to refer to something
by a label that `control/LOCAL-CONTEXT.md` defines. That file exists and does **not** define F1, so
the reference resolves nowhere — not for someone who clones the repository, and not on the
maintainer's own machine.

**Why it matters more than a loose citation.** T-005 makes it a gating criterion, so a task's
closure currently depends on an outcome the repository cannot describe. `docs/BINDING.md` §4 is
worse in a quiet way: the whole *"Assumptions this binding makes"* requirement is justified by that
failure, so the strongest rule in the backend contract rests on evidence a reader cannot check.

**Requirements served**
R-20 — a clone works with nothing else; R-23 in spirit, via `CLAUDE.md`'s label discipline.

**Scope**
- In: the three files above.
- In: whether F1's substance belongs in the tracked tree or in `control/LOCAL-CONTEXT.md` with a
  defined label. `docs/BINDING.md` already states the substance in prose — *a binding claimed "the
  folder is the index", which is false for a project with a generated one* — so the cheapest fix may
  be to drop the label and keep the fact.
- Out: doing the work T-005 describes. This is about the reference being resolvable, not about
  aligning with the handoff binding.
- Out: any other external citation. If the audit had found more they would be here; it did not.

**Inputs**
`docs/BRIEF.md` §*Interop*, `docs/BINDING.md` §4, `tasks/T-005`, `CLAUDE.md` *Publishing
constraints*, [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-7.

**Acceptance criteria**
- [ ] No tracked file uses "F1" without the reader being able to learn what it is from this
      repository, or from a label `control/LOCAL-CONTEXT.md` defines
- [ ] T-005's acceptance criterion 1 states a condition someone can tell has been met
- [ ] `docs/BINDING.md` §4's justification stands on evidence stated in the tracked tree — that
      section's rule is the contract's strongest and must not rest on an unreachable citation
- [ ] Nothing personal, client-specific or machine-specific is added in the process (R-23); the
      pre-publish check in `CLAUDE.md` still prints nothing

**Open questions**
- None. What "F1" refers to is already stated in prose in `docs/BINDING.md` §4; the question is only
  whether to keep the label, and that does not change the outcome.

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
| 2026-08-06 | → proposed | Raised as F-7 from the T-026 audit, clauses 1 and 3. Checked `control/LOCAL-CONTEXT.md` before writing this up — it exists and does not define F1, so this is a dangling reference rather than the label discipline working as intended. |
