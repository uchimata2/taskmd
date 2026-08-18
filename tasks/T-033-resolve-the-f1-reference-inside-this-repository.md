---
id: T-033
title: Resolve the F1 reference inside this repository
type: fix
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-005, T-013]
work_package: M2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-06
updated: 2026-08-11
deliverables: [docs/BRIEF.md, plugin/skills/taskmd/docs/BINDING.md]
adopter_visible: no
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

**Premises re-verified on 2026-08-10, before accepting the criteria.** Two things had moved since
this was raised on 2026-08-06, neither of them changing what the task has to achieve:

- **The contract's path.** §1's table says `docs/BINDING.md`; since T-083 the file is
  `plugin/skills/taskmd/docs/BINDING.md`. The table is right about the content and stale about the
  location, and is left as written — it is a dated account of what the audit found.
- **The use set is wider than the three files named.** `F1` also appears as explanatory prose in
  T-007, T-009, T-010, T-026 and T-040. Criterion 1 already reaches them — it says *no tracked file*,
  not *these three* — and they need no edit if the label is defined somewhere a reader reaches, which
  is the difference between defining a label once and rewriting every use of it. §1's *Scope* names
  the three because they are the ones that must be **written to**; that is the same distinction, and
  it is recorded here rather than by editing the scope.
- **`control/LOCAL-CONTEXT.md` still does not define F1**, re-checked rather than assumed from the
  2026-08-06 log. The finding stands.

## 2. Plan

**One definition, one deletion, one rewrite** — and the order matters, because the definition is
what makes the other tracked uses legal without touching them.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give `F1` a definition in `docs/BRIEF.md` §*Interop*, the one place that already cites the brief it comes from: say what document the label belongs to, that it is the upstream project's and not in this repository, and what it found. | The edited `docs/BRIEF.md` |
| 2 | Drop the label from `plugin/skills/taskmd/docs/BINDING.md` §4 and keep the fact — the paragraph two rows above already states the failure in full, so the row can name it without a citation. | The edited `plugin/skills/taskmd/docs/BINDING.md` |
| 3 | Rewrite T-005's acceptance criterion 1 so it states a condition someone can tell has been met, preserving the scoping the maintainer added on 2026-08-07 — the recipe half does not wait, the contribution half does. Keep the original beside it. | The edited `tasks/T-005-align-with-the-handoff-tracker-binding-contract.md` |
| 4 | Grep the whole tree for `F1` again and check every remaining use resolves through step 1. | The hit list in §3 |
| 5 | Run the suite, `check`, `index`, and the pre-publish leak check — step 1 adds prose about an external project, which is exactly what R-23 governs. | The literal output in §3 |

**Why the definition goes in `docs/BRIEF.md` and not in the contract — decided.** The contract is
inside `plugin/`, and T-064 forbids anything there from sending a reader to what an adopter does not
receive; a label defined in this repository's own papers is exactly that. So the two live sites are
fixed in opposite directions on purpose: `BRIEF.md` gains the definition because it is this
repository's paper, and `BINDING.md` loses the label because it is shipped. *Rejected: defining F1 in
`control/LOCAL-CONTEXT.md`*, which is where a private label would go — but F1 is not private, it is
an upstream project's public-facing finding, and putting it there would make every tracked use
depend on a gitignored file.

**Not in scope, and not touched:** the task records that mention F1 in passing. They are dated
accounts, and step 1 makes them resolvable without an edit.

**Outputs promised**

- docs/BRIEF.md
- plugin/skills/taskmd/docs/BINDING.md
- tasks/T-005-align-with-the-handoff-tracker-binding-contract.md
- tasks/T-033-resolve-the-f1-reference-inside-this-repository.md
- tasks/README.md

## 3. Implement

**Decisions & assumptions**
- **The label is defined once, in `docs/BRIEF.md` §*Interop*** — 2026-08-10, as planned. It says
  what document F1 belongs to, that the document is the upstream project's and not in this
  repository, and what the finding is. That is what makes the other tracked uses legal without
  touching any of them: the label now resolves inside the clone, which is what criterion 1 asks for.
- **`BINDING.md` lost the label instead of gaining a pointer** — 2026-08-10. It is inside `plugin/`,
  and T-064 forbids anything there from sending a reader to what an adopter does not receive, which
  is what a pointer to `BRIEF.md` would be. The row now reads *the folder-is-the-index failure
  described above* — the paragraph it refers to is in the same section and states the failure in
  full, so the citation was carrying no information the reader could not already see.
  *Rejected: an unqualified positional phrase like "two paragraphs above"*, which is a fact about
  the current layout and goes stale on the next edit that adds a paragraph.
- **T-005's criterion 1 was unfalsifiable, not merely unresolvable** — 2026-08-10. "The handoff F1
  outcome is known" gives no way to tell whether it has happened; the replacement names what has to
  be recorded, against what, and where, and keeps the maintainer's 2026-08-07 scoping verbatim — the
  recipe half does not wait, the contribution half does. The original is struck through beside it,
  not deleted, and the open-question note that referred to it is annotated rather than rewritten.
- **The task records that mention F1 were not touched** — 2026-08-10. Six of them use it as
  explanatory prose in dated accounts. Rewriting a record to match a later document destroys the
  history the method exists to keep, and step 1 makes every one of them resolvable anyway.

**Outputs produced**
- docs/BRIEF.md — §*Interop* gains the definition
- plugin/skills/taskmd/docs/BINDING.md — §4's table row names the failure instead of citing it
- tasks/T-005-align-with-the-handoff-tracker-binding-contract.md — criterion 1 replaced, original
  kept, the open-question note annotated
- tasks/T-033-resolve-the-f1-reference-inside-this-repository.md — this record
- tasks/README.md — regenerated

**Evidence — where `F1` survives.** Whole tree, `reference/` and `.handoff/` excluded, after the
edits:

```
docs/BRIEF.md:105  docs/BRIEF.md:106     <- the definition
tasks/…                                   <- 40 uses across 8 task records and the index
plugin/…                                  <- none
```

Nothing under `plugin/` uses the label at all, so the shipped tree carries no reference to a
document adopters do not receive. Every remaining use is in a tracked file, and resolves through
`docs/BRIEF.md`.

**Evidence — the suite, the tool, and the leak check.**

```
=== test_budget.py (exit 0) tier 1 7844 chars under by 2 (bound 7846, reference/TASK-WORKFLOW.md)
=== test_cli.py (exit 0) OK
=== test_list.py (exit 0) OK
=== test_runtime.py (exit 1) FAILED (failures=4)
=== test_schema.py (exit 0) OK
Wrote tasks/README.md - 18 active, 98 closed
OK - 116 task(s), 580 field value(s), 367 reference(s), 22 dependency edge(s), 183 declared output(s), 1 index file(s), 144 document(s), 1146 link(s), 2 template(s), 10 template field value(s), 0 vocabulary row(s)
```

The four are the standing `Launchers` failures ([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)), unchanged by this task and absent
on the Linux runner. The pre-publish check printed nothing — run because step 1 adds prose about an
external project, which is the case R-23 governs.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| No tracked file uses "F1" without the reader being able to learn what it is from this repository | met | `docs/BRIEF.md` §*Interop* defines it, and `BRIEF.md` is tracked, so all 40 remaining uses resolve from inside a clone. Checked by grepping the whole tree rather than the three files §1 named — the criterion says *no tracked file*, and the wider set was found at `specify` and recorded there. The second half of the criterion, *or from a label `control/LOCAL-CONTEXT.md` defines*, was deliberately not used: F1 is an upstream project's finding, not local-only material, and putting it there would make tracked documents depend on a gitignored file. |
| T-005's acceptance criterion 1 states a condition someone can tell has been met | met | It now names what must be recorded (whether the handoff binding still states "the folder is the index"), against what (the binding as it then stands), and that the check must say where it was made. Falsifiable in the way the original was not: a T-005 that closes without that record fails it. The 2026-08-07 scoping survives word for word. |
| `docs/BINDING.md` §4's justification stands on evidence stated in the tracked tree | met | Stronger than asked. The section already stated the failure in full two paragraphs above the row; the row cited a label instead of the paragraph, so the strongest rule in the contract pointed outside the repository for evidence that was already inside it. It now names the failure, and the contract cites nothing external at all. |
| Nothing personal, client-specific or machine-specific is added (R-23); the pre-publish check still prints nothing | met | Run over every file a push would send — cached and untracked, the fixture excluded — and it printed nothing. Worth running rather than reasoning about: this task's one substantive addition is a paragraph describing another project's document, which is exactly the shape R-23 exists for. |

**On what this task did not do.** It did not remove the label, and removing it was the obvious
reading of "resolve the F1 reference". Six task records use it as shorthand in dated accounts of
decisions that were taken in those words; rewriting them would have destroyed the history the method
exists to keep, to save a definition of three sentences. The label now costs one paragraph and buys
the readability of every one of those records.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | Specify through review in one session — the work and its decisions are dated 2026-08-10, which is when they were taken; the session ran past midnight and this row is dated when it closed rather than back-dated to make the two agree. Under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1), re-confirmed by them for this task. Criteria stood as raised; two premises had moved since 2026-08-06 and are recorded in §1 rather than by editing the audit's account. Nothing raised. The shape that made it cheap: **define the label once, rewrite nothing that uses it** — the alternative, removing F1 from six dated task records, would have cost the history those records exist to keep. |
| 2026-08-06 | → proposed | Raised as F-7 from the T-026 audit, clauses 1 and 3. Checked `control/LOCAL-CONTEXT.md` before writing this up — it exists and does not define F1, so this is a dangling reference rather than the label discipline working as intended. |
