---
id: T-239
title: Give both shipped declarations the content the repaired clause now requires
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-232, T-238, T-222]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
deliverables:
  - plugin/skills/taskmd/docs/BINDING.md
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-239 — Give both shipped declarations the content the repaired clause now requires

## 1. Specify

**Outcome**

Every shipped binding's coverage declaration carries what
[`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 requires of it after the 2026-08-23
repair — or is exempt by a rule that says so, rather than by nobody having checked.

**Where this came from**

[T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) added **six**
requirements to §4 and its sixth criterion measured **three** of them: heading, level and position.
Found hours later while doing [T-238](T-238-bring-the-github-binding-s-coverage-declaration-into-line-with-the-repaired-clause.md).
Re-measured across all six, **neither shipped binding** carried the per-class reasoning, the
*hygiene, not truth* sentence, or the mapping-not-service line — three requirements the repair made
mandatory and nothing checked.

**That is the same failure the repair was about, one level up.** T-232 exists because a clause
naming two classes read as an inventory; its own review then read a three-of-six check as a
six-of-six one. T-232's row is annotated and its verdict left as written.

**Scope**

- In: the three content requirements, measured against both shipped bindings, and supplied where they
  are owed
- In: **whether they are owed at all by a declaration that names no class impossible** — the question
  applying them raised, and the reason this is not simply an edit
- Out: heading, level and position, which are [T-238](T-238-bring-the-github-binding-s-coverage-declaration-into-line-with-the-repaired-clause.md)
- Out: re-opening what either declaration **classifies**. The four classes `github-issues.md` names
  are unchanged; only their reasoning is added
- Out: the marked-region machinery, which T-232 settled

**Inputs**

- [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 as repaired on 2026-08-23
- both files in `plugin/skills/taskmd/docs/bindings/`

**Acceptance criteria**

- [x] All six requirements are measured against both bindings, and the measurement is shown rather
      than asserted
- [x] Every requirement a binding owes is supplied, and every one it does not owe is exempted **by a
      rule written into §4**, not by a judgement made here
- [x] `github-issues.md` classifies exactly the four classes it classified before
- [x] `taskmd check` passes and `tests/test_publishing.py` still reads every class each region names

**Open questions**
- **None.** The requirements are the contract's and the measurement decides the rest.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure all six requirements against both bindings by reading the regions programmatically, not by eye | the per-binding result |
| 2 | Apply the two content rules to `local-markdown.md` **first**, because it is the case most likely to show the rule is wrong | either the edit, or a defect in the rule |
| 3 | Fix whatever step 2 finds in §4 before writing anything into a binding against it | the qualified rule |
| 4 | Supply what `github-issues.md` owes, changing no classification | the filled-out declaration |
| 5 | Re-run the region tests, which are what read the declarations | the output |

**Step 2 takes the awkward binding first on purpose.** `local-markdown.md` declares that *nothing*
cannot occur, so it is the one case where a rule about naming classes might demand something
incoherent — and applying a new rule to its easiest subject first is how a rule ships broken.

## 3. Implement

**Decisions & assumptions**

- **Both new content rules were wrong as written, and step 2 found it** — 2026-08-23. They demanded a
  per-class reason and a *hygiene, not truth* sentence from **every** declaration.
  `local-markdown.md` names no class as impossible, so the first is vacuous there — and the second is
  worse than vacuous, it is **false**: *nothing cannot occur here* is a claim about the validator and
  the mapping, both of which anyone who installed them can read, so it is checkable locally and a
  caveat saying otherwise would mislead. Both rules are now qualified in §4 to bind only where a
  declaration names at least one class impossible, with the exemption stated as a rule.
  *Rejected: write the caveat into `local-markdown.md` anyway* — it would satisfy the rule and say
  something untrue, which is how a contract teaches a bad habit.
- **`github-issues.md` gains reasoning and loses no classification** — 2026-08-23. The same four
  classes, each with its own paragraph, plus one line saying all four rest on the mapping rather than
  on the service, plus the hygiene sentence. The closing line is unchanged and still carries both
  halves, which is right: a migrated project keeps a working tree.
- **T-232 was annotated, not re-opened** — 2026-08-23. Its sixth criterion keeps its **met** verdict
  and its original note; the cell now also records that the check covered three of six and names this
  record. METHOD rule 5: correct the present, annotate the past.

**Outputs produced**

- `plugin/skills/taskmd/docs/BINDING.md` — both content rules qualified
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the declaration filled out

**Verification**

**Step 1, measured by reading each region rather than by eye.** A short script extracted the text
between the markers in each binding and tested for each requirement:

```text
local-markdown.md   region 731 chars   hygiene: False   mapping-not-service: False   per-class: none
github-issues.md    region 432 chars   hygiene: False   mapping-not-service: False   per-class: none
```

Three of six missing from both, against the three T-232 measured. **Six requirements, two bindings,
twelve cells** — and the earlier check filled six of them.

**Step 2 is the step that paid.** Applying the rules to `local-markdown.md` produced an edit that
would have been false, which is the whole reason for taking that binding first. The rule was fixed
instead of the binding.

**Step 5, the gates.**

```text
python -m pytest tests/test_publishing.py -q  ->  21 passed
taskmd check                                   ->  exit 0
```

`test_publishing.py` is the reader here: it finds the region in every binding and requires each
capitalised token inside it to be a class the validator reports. `github-issues.md`'s region grew
from 432 to roughly four times that and still names exactly `DUPLICATE ID`, `ID WIDTH`,
`PARKED TASK` and `STALE INDEX`, all four read and all four real.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| All six requirements are measured against both bindings, and the measurement is shown | met | §3 step 1, one line per binding, produced by reading the regions rather than by eye. Twelve cells, and the earlier check had filled six |
| Every requirement a binding owes is supplied, and every one it does not owe is exempted **by a rule in §4** | met | `github-issues.md` gained all three. `local-markdown.md` owes none, and §4 now says why in two places — a declaration naming no class is exempt, and the hygiene sentence would be false there |
| `github-issues.md` classifies exactly the four classes it classified before | met | `DUPLICATE ID`, `ID WIDTH`, `PARKED TASK`, `STALE INDEX` — the same four, now with a paragraph each. The region test reads all four and each is a class the validator reports |
| `taskmd check` passes and the region tests still read every class each region names | met | `check` exit 0; `21 passed` |

**Child fix tasks raised**
- none.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds none. **One thing is
recorded rather than left implicit**: this record corrected a rule that
[T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) wrote hours earlier, and
that is not a reversal of anything the owner agreed — the owner agreed the four findings were worth
repairing, not the wording of a clause that had not been written yet.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **Raised and closed the same day, under the owner's unattended grant of 2026-08-22 as extended to what the work raises.** **What the grant covers here:** this record to closure. **What it does not:** [T-231](T-231-cut-the-next-release.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), and any audit. No open question, so it did not stop at `specify`. **Found by doing [T-238](T-238-bring-the-github-binding-s-coverage-declaration-into-line-with-the-repaired-clause.md)**: T-232 added six requirements and its own sixth criterion measured three, which is the failure T-232 was repairing arriving one level up in its own review. That row is annotated and its verdict left as written. **The plan took `local-markdown.md` first because it was the awkward case, and that is what paid** — both new rules were wrong as written, demanding a per-class reason from a declaration that names no class and a *hygiene, not truth* caveat that would have been **false** there, since *nothing cannot occur here* is checkable by anyone who installed the validator. **The rule was fixed rather than the binding**, and §4 now carries the exemption as a rule so the next binding is not left to judge it. `github-issues.md` gained a paragraph per class, the mapping-not-service line and the hygiene sentence, and classifies exactly the four classes it did before. |
