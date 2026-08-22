---
id: T-236
title: Build check --classes, and give the class derivation one home in the package
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-226, T-197, T-191, T-222]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
deliverables: []
---

# T-236 — Build check --classes, and give the class derivation one home in the package

## 1. Specify

**Outcome**

`check --classes` prints the set of classes `check` can report, from an installed copy, and the
derivation that produces that set exists **once** — in the package, with `tests/classes.py` importing
it rather than repeating it.

**Where this came from**

[T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md) put the
whether-and-what-shape question to the owner and it was answered on 2026-08-22: **yes, as
`check --classes`** rather than a fifth command, because it adds no verb to a surface this project has
held at four and it sits on the command that owns the classes. T-226 §3 answers its third criterion —
the derivation moves into the package — with the placements it rules out. **This record is the build,
which T-226's scope puts out of its own.**

**Why it matters rather than being tidiness.**
[`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 requires a binding to name the classes its
mapping makes impossible **in the validator's own names**, and tells the author to go and read
`cli.py`. That is honest and it asks somebody to read Python in order to write Markdown. T-225
measured the cost: both uninvolved readers found the answer and both reported they could not reach it
from the text.

**Scope**

- In: the flag, the move of the derivation into the package, and `tests/classes.py` reduced to an
  import so that the set has one home
- In: the four questions below, which T-226's answer does not reach and which were found by writing
  this record from it
- In: [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 *Where the class names come from*
  updated to name the command, since its current instruction is *read the source* and the whole point
  is to replace it
- Out: changing what the classes are, or adding one
- Out: a list of the classes in any document. That is the per-check coverage table §4 refuses, one
  column narrower, and it is falsified by the same event
- Out: `tests/classes.py`'s own guard readers in `tests/test_publishing.py` losing coverage — they
  must still run against the derivation wherever it ends up

**Inputs**

- [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md) §3 — the
  answer, the rejected placements, and the four gaps this record's questions come from
- `tests/classes.py` — the derivation as it exists, its guard on `CONFIG ERROR`, and the `source=`
  override that keeps the guarded line inside the run
- `plugin/skills/taskmd/taskmd/cli.py` — the 20 `problems.append` sites and `ADVISORY_PREFIXES`
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) — the defect a second
  derivation would re-create

**Acceptance criteria**

- [ ] `check --classes` prints the set, and is shown to do so **from an installed copy** rather than
      from this working tree
- [ ] Exactly one derivation exists: a search for the prefix pattern finds it in one place, and
      `tests/classes.py` imports rather than repeats it
- [ ] The set the flag prints is the same set the tests compare against, shown by running both
- [ ] `CONFIG ERROR` is absent from the printed set, and the guard that removes it is still exercised
      by its reader in `tests/test_publishing.py`
- [ ] [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 names the command where it currently
      says to read the source, and no list of classes is added to any document
- [ ] `taskmd check` passes and the suite passes with no bound edited

**Open questions**

*All four came out of writing this `specify` from T-226 alone, which was T-226's own verification
step. None is the owner's; each is answerable by measurement during `plan`.*

- **Does the shipped derivation keep reading `cli.py`'s source text, or do the 20 append sites gain a
  constant?** `tests/classes.py` says a constant *"would change `cli.py` at every append site, which
  is a plugin change with adopter reach and is out of T-197's scope"* — but this record **is** a
  plugin change, so the reason has expired and the question is live again. **Recommendation: keep the
  regex.** 20 sites is a large diff for robustness the guard reader already supplies, and the padding
  those literals carry is what aligns `check`'s output. *Against:* a prefix that stops matching leaves
  the set silently, and a shrunken set makes every assertion built on it **weaker** rather than
  louder — which the module's own docstring names as its cost.
- **Does a runtime source-read work from an installed copy?** The derivation opens `cli.__file__`.
  That is fine for a directory install, which is what this plugin ships as, and it is **not** fine if
  the module is ever loaded from an archive or a frozen build. Nothing anywhere has considered this,
  because until now the derivation only ever ran from a checkout. It is the first acceptance criterion
  for that reason. **Recommendation: measure it before choosing the shape above** — if it fails from
  an install, the constant stops being optional and the first question is answered for us.
- **What exactly does the flag print?** One class per line, sorted, nothing else — so the output can
  be piped and diffed — or grouped into problems and advisories, which is a distinction a binding
  author does care about, since only the problem classes move an exit code. **Recommendation: one per
  line, sorted, no grouping**, and let `check`'s own output teach the distinction. *Against:* the
  author then cannot tell from this command which names are advisory.
- **Does `check --classes` still run the checks?** **Recommendation: no — print and exit 0**, because
  a binding author running it has no project in mind and `check` would fail on whatever directory they
  happen to be in. *Against:* every other flag on `check` modifies a run rather than replacing it.

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
| 2026-08-23 | → proposed | Raised from [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md)'s `implement`, whose scope puts building it out by name, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure, without stopping to ask for each phase. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit** — unchanged. **None of the four open questions above is the owner's**, so unlike [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md) this record does not stop at `specify`; each is answerable by measurement in `plan`. **This record was written from T-226 alone, deliberately and as that task's verification step** — a decision is verified when the people bound by it can state what it commits them to, so the smallest real use of the answer was to write the build's `specify` from it and keep what had to be invented. The four questions **are** that list, and the second is the one worth having: nothing had considered that a derivation reading its own module's source has only ever run from a checkout. |
