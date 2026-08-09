---
id: T-072
title: Give the plugin's description and version one home each
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-006, T-053]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-072 — Give the plugin's description and version one home each

## 1. Specify

**Outcome**
The plugin's description and its version are each written in one place, or — where the packaging
genuinely requires two — the requirement is recorded so the next release knows both must move.

**Why this one**
Raised as **F-12** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 2. Four homes for one sentence, two of them byte-identical:

| Where | Value |
| :--- | :--- |
| `.claude-plugin/marketplace.json` → `plugins[0].description` | the long form |
| `plugin/.claude-plugin/plugin.json` → `description` | **byte-identical** to the above |
| `.claude-plugin/marketplace.json` → `metadata.description` | a shorter variant of the same sentence |
| `plugin/taskmd/__init__.py` → module docstring | a shorter variant again |

And `version: 0.1.0` is written in both manifests, so a release moves two files or ships a
contradiction. The first release is [T-006](T-006-package-document-and-publish.md), which is the
moment this bites.

**Why it is a task rather than an observation.** The two byte-identical strings are the clearest
clause-2 case in the tree: no drift yet, and nothing whatever to keep them in step except someone
remembering. `docs/SCOPE.md` §1 *Invisibility* names exactly that shape — *"no correctness may depend
on someone remembering to intervene"*.

**Why `xs` and still worth checking rather than assuming.** Whether a marketplace entry may omit
`description` and `version` and inherit them from the plugin's own manifest is a **harness** question.
The answer decides whether this is a deletion or a documented obligation, and guessing it would be
the same mistake as
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) D1 avoided by reading the
shipped binary instead of inferring from behaviour.

**Requirements served**
R-1 (`docs/SCOPE.md`); §1 *Invisibility*; §2 principle 1.

**Scope**
- In: `description` and `version` across the two manifests.
- In: `metadata.description` in the marketplace file, which is the marketplace's own blurb and may
  legitimately differ — that is a question to answer, not an assumption either way.
- In: `plugin/taskmd/__init__.py`'s docstring, which is a package docstring and arguably owes nobody
  consistency; recorded so the decision covers it rather than leaving one copy unexamined.
- Out: the wording itself. Whatever survives keeps its current text.
- Out: the `source` field, which is [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md).
- Out: version *numbering* and when 0.1.0 becomes something else, which is T-006's.

**Inputs**
`.claude-plugin/marketplace.json`, `plugin/.claude-plugin/plugin.json`, `plugin/taskmd/__init__.py`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-12.

**Acceptance criteria**
- [ ] It is established — by reading what the harness accepts, not by inference — whether either
      field may be omitted from the marketplace entry
- [ ] Each field ends with one home, or the obligation to update two is written where a release will
      meet it
- [ ] The plugin still installs afterwards, demonstrated rather than assumed
- [ ] Every copy identified above is accounted for, including the two that may legitimately differ

**Open questions**
- **Is `metadata.description` a copy or a different fact?** It describes the *marketplace*, which
  today contains exactly one plugin, so the two are the same sentence by coincidence rather than by
  design — and would stop being so the moment a second plugin were added. If that reading is taken,
  three homes collapse to two and this row is not a finding at all. `plan` decides, and the answer
  determines whether the fix is a deletion or a rewording.

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
| 2026-08-09 | → proposed | Raised as F-12 from the T-059 audit, clause 2. Compared before write-up: the marketplace entry's `description` and `plugin.json`'s are byte-identical, and `version` is written twice. `low`/`xs`, and the one thing that must not be guessed is whether the harness permits omission — T-053 D1 is the precedent for reading that rather than inferring it. |
