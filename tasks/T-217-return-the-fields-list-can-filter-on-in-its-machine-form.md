---
id: T-217
title: Return the fields list can filter on in its machine form
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-087, T-022]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-217 — Return the fields `list` can filter on in its machine form

## 1. Specify

**Outcome**
A caller that can filter `list` on a field can also read that field back from `--json`, so a machine
consumer can verify, group or sort on the value it selected by — or the asymmetry is recorded as
deliberate, with the reason, where a caller meets it.

**Why this one**
Found on 2026-08-22 while answering a question about the open backlog, by running both halves rather
than reading the help text:

```text
$ taskmd list --open --effort xs
T-214   proposed  M6  specify  Decide whether the class-set subtraction that ...   -

$ taskmd list --open --effort xs --json
[ { "blocked": false, "blocked_by": [], "blocks": [], "children": [], "id": "T-214",
    "open": true, "parent": [], "phase": "specify", "related": [...],
    "status": "proposed", "title": "...", "work_package": "M6" } ]
```

`--effort` selects correctly and the object carries no `effort`. The same holds for
`business_value`. **So a machine caller must trust the filter blindly**: it cannot confirm what it
asked for, cannot group by the value, and cannot sort on it without opening every task file — which
is what this tool exists to stop people doing.

**It is a consequence of one key serving two masters, not an oversight.** `index_columns` decides
both what the generated human index shows *and* what the machine form returns. `effort` is named by
the schema — `effort_field: effort`, and ordering reads it — but it is not an `index_column` here, so
it is absent from the JSON. A project wanting it in the machine form must put it in the human index
too, and those are different questions.

**Scope**
- In: deciding whether the machine form should carry every schema-named field, the configured
  columns plus the fields filters accept, or stay as it is with the reason stated where a caller
  meets it
- In: implementing the decision, and whatever the answer costs a caller that already parses the
  current shape
- Out: the human view's columns. `list` omitting a column no task uses is a decided behaviour and is
  not what this is about
- Out: adding a config key. [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) records
  that a new key errors every adopter's config on upgrade, so a solution needing one is a different
  and much larger task

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_list`, `in_use`, and the *Views only* docstring that
  states the current rule
- [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) — which widened filtering, and
  whose own title names the coupling this task questions: *a field the index can show*
- `.taskmd/config.md` — `index_columns`, and the ordering keys that name `effort`

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternatives, including what each would cost a
      caller already parsing `--json` today
- [ ] If the shape changes, a test asserts that **every field `list` accepts as a filter** is present
      in the machine form — derived from the filter list rather than hand-typed, so the two cannot
      drift apart again
- [ ] If the shape does not change, the reason is stated where a caller meets it, not only in this
      record
- [ ] `check`, `index` and the suite are green, and the output is quoted

**Open questions**
- **None.** The options are named above; choosing between them is this task's work.

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
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it may honestly end with no code change.** §1 allows the answer *leave the machine form as it is*, provided the reason is stated where a caller meets it and not only in this record. Its scope also puts a new config key out by name, because [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) records that one errors every adopter's config on upgrade — no grant of phases licenses that. |
| 2026-08-22 | → proposed | Raised while answering an ordinary question about the backlog — the view the owner asked for needed `effort` and a gate column, and `--json` could supply neither, so it was built from the JSON and the front matter together. Recorded rather than worked around, because the workaround is exactly the file-reading this tool exists to remove. `low` and `s`: nothing is broken and the human view is unaffected, but it is `adopter_visible` because a machine consumer meets it. ~~**Not covered by the multi-phase grant of 2026-08-22**, which names six tasks by id and this is not one of them.~~ **Superseded later the same day** — the owner added this task to the grant; the row above is the authorisation, and this sentence records only what was true at the moment of raising it. |
