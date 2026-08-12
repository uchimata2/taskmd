---
id: T-072
title: Give the plugin's description and version one home each
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-006, T-053]
work_package: M1
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
| 1 | Establish what the harness actually requires, by removing each field from the marketplace entry and validating - the criterion forbids inferring it | Three validation runs |
| 2 | Settle the open question about `metadata.description` | The decision in §3 D2 |
| 3 | Apply: drop from the marketplace entry whatever may be dropped | `.claude-plugin/marketplace.json` |
| 4 | Reinstall and confirm the harness resolves both fields from the surviving home | The transcript |

**Why step 1 is three runs and not one.** The two fields could differ - a marketplace that needs a
version to order its entries would plausibly still not need a description. Testing them together
would have answered a question nobody asked.

## 3. Implement

**Decisions & assumptions**

- **D1 - both fields are optional in the marketplace entry, so both leave it** - 2026-08-09.
  Established by running `claude plugin validate .` against four manifests:

  ```
  baseline                    Validation passed with warnings
  without description         Validation passed with warnings
  without version             Validation passed with warnings
  without both                Validation passed with warnings
  ```

  The only warning in every run is the pre-existing *no author information* note, unrelated. So
  `plugin/.claude-plugin/plugin.json` is now the single home of each, and the release obligation the
  finding described - *"must move together at every release"* - is gone rather than written down
  somewhere a release will meet it. One home beats a reminder.

- **D2 - `metadata.description` is a different fact and stays** - 2026-08-09. It describes the
  **marketplace**, which today holds exactly one plugin; that is why the two sentences resemble each
  other, and it would stop the moment a second plugin were added. So three homes were never three:
  they were two facts, one of which had two homes. Its wording is untouched, which §1 puts out of
  scope.

- **D3 - `plugin/taskmd/__init__.py` stays too** - 2026-08-09. One line:
  *"taskmd - Markdown files as a task tracker, with a generated index and real dependency links."*
  It is a **package docstring**, addressed to someone reading the source, and it is already worded
  differently from the manifest rather than byte-identical to it. Making a Python package import a
  string from a JSON manifest to avoid restating its own purpose would cost more than the sentence
  is worth. Recorded per criterion 4 rather than left unexamined.

### Step 4 - it still installs, and both fields still resolve

```
claude plugin marketplace update taskmd   Successfully updated marketplace: taskmd
claude plugin uninstall taskmd@taskmd     Successfully uninstalled
claude plugin install   taskmd@taskmd     Successfully installed (scope: user)

claude plugin list      taskmd@taskmd  Version: 0.1.0   enabled
claude plugin details   taskmd 0.1.0
                        Markdown files as a task tracker: one file per task, a generated index,
                        real dependency links, and a validator. For any kind of work, not only
                        software.
```

The version and the description the harness reports are `plugin.json`'s - the marketplace entry no
longer carries either.

**Outputs produced**
- `.claude-plugin/marketplace.json` - the plugin entry is now `name` and `source`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| It is established - by reading what the harness accepts, not by inference - whether either field may be omitted | met | Four validation runs, each field alone and both together. Run, not read |
| Each field ends with one home, or the obligation to update two is written where a release will meet it | met | The first branch. `plugin.json` is the one home of each; no reminder was needed because nothing is left to remind anyone of |
| The plugin still installs afterwards, demonstrated rather than assumed | met | Uninstalled and reinstalled; `list` and `details` both resolve version and description from the surviving home |
| Every copy identified above is accounted for, including the two that may legitimately differ | met | Four copies: two removed, `metadata.description` kept as a different fact (D2), the package docstring kept as a different audience (D3) |

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met. Both fields are **optional** in the marketplace entry — established by four `claude plugin validate` runs rather than inferred, which is what criterion 1 asked for — so both were dropped and `plugin/.claude-plugin/plugin.json` is the one home of each. That is better than the outcome the criterion allowed for: no release obligation had to be written down anywhere, because none is left. Reinstalled to prove it, and the harness reports the version and description from the surviving home. The open question resolved as *different fact*: `metadata.description` describes the marketplace, which holds one plugin today, which is why the two sentences resemble each other and would stop doing so on the second. So three homes were never three — two facts, one of which had two homes. |
| 2026-08-09 | → in_progress | Plan tests the two fields **separately** as well as together: a marketplace that needed a version to order its entries would plausibly still not need a description, and testing them as a pair would have answered a question nobody asked. |
| 2026-08-09 | → proposed | Raised as F-12 from the T-059 audit, clause 2. Compared before write-up: the marketplace entry's `description` and `plugin.json`'s are byte-identical, and `version` is written twice. `low`/`xs`, and the one thing that must not be guessed is whether the harness permits omission — T-053 D1 is the precedent for reading that rather than inferring it. |
