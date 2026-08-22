---
id: T-217
title: Return the fields list can filter on in its machine form
type: fix
status: done
phase: review
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
| 1 | Read both sides from the tool rather than from the code: the accepted filter names from `list`'s own rejection line, and the key set from its own `--json`. | Both quoted in §3, and the difference named |
| 2 | Decide between the three options in §1, and price each against a caller already parsing `--json`. | A decision in §3 |
| 3 | Write the test **before** the change, deriving both sides from the tool, and run it on the unchanged code. | The failing run quoted in §3 |
| 4 | Implement the decision. | Edited `cli.py` |
| 5 | Re-read the key set, and confirm **no key was lost** — an additive change is what makes the cost to existing callers what §3 claims it is. | The new key set in §3, compared with step 1's |
| 6 | Correct every shipped statement the change falsifies. **`github-issues.md` §*What to read* states this contract in present tense**, and it is the one place that does. | The edited region |
| 7 | Run `check`, `index` and the suite. | Their output in §3 |

**Shape decision — the machine form is widened to `filter_names`, and the line form is untouched.**
That is §1's second option. The change is **one loop**, and it makes the two halves read from the
same function `parse_filters` already validates against, so a field added to a project's config
becomes filterable and readable in the same edit. **Rejected: every schema-named field**, §1's first
option — it would emit fields nobody can select on, which is a wider contract answering a need
nobody has stated, and it would tie the machine form to schema internals rather than to the
command's own accepted set. **Rejected: leaving it and stating the reason**, §1's third — the reason
would have been *`index_columns` serves two masters*, which is a description of the cause rather
than a defence of the behaviour.

**Step 3 is placed before step 4 deliberately**, and step 5 exists because step 3 cannot see a
removal: a test that asserts a set of keys is present passes just as well on a shape that dropped
one it does not name.

**Outputs**
- plugin/skills/taskmd/taskmd/cli.py
- plugin/skills/taskmd/docs/bindings/github-issues.md
- tests/test_list.py

## 3. Implement

**Step 1 — both sides, from the tool**

```text
$ ./plugin/bin/taskmd list --nope x
unknown filter: --nope. This project accepts: --adopter_visible, --blocked_by, --blocks,
--business_value, --children, --effort, --owner, --parent, --phase, --related, --status, --type,
--work_package

$ ./plugin/bin/taskmd list --open --limit 1 --json   # keys
['blocked', 'blocked_by', 'blocks', 'children', 'id', 'open', 'parent', 'phase', 'related',
 'status', 'title', 'work_package']
```

**Thirteen accepted, and five of them unreadable**: `adopter_visible`, `business_value`, `effort`,
`owner`, `type`.

**Decisions & assumptions**

1. **The machine form carries every field `list` accepts as a filter** — 2026-08-22 — read from
   `filter_names(schema)`, the same function `parse_filters` validates a flag against and
   `list --help` renders. Both rejected alternatives are priced in §2's shape decision, with what
   each costs.
2. **The cost to a caller already parsing `--json` is additive and nothing else** — 2026-08-22.
   Five keys arrive; none is removed or renamed, confirmed in step 5 by comparing the two key sets
   rather than by reasoning about the code. A consumer reading the keys it wants is unaffected; one
   asserting an **exact** key set breaks, and that is the whole of the cost. No test in this
   repository asserted an exact set — checked before the change, not after.
3. **`index_columns` still decides the line form, and that is the point rather than a leftover** —
   2026-08-22. §1 named the cause as one key serving two masters; the repair separates the two
   masters instead of renaming the key. What a person's index shows and what a script can read back
   are different questions, and §1 puts the human view out of scope.
4. **`deliverables` is still absent, and that is consistent rather than an omission** — 2026-08-22.
   Nothing filters on it, so under this contract it is not carried. A project that wants it in the
   machine form names it in a view, which makes it filterable and readable together — which is the
   promise T-087 half-kept and this completes.
5. **The test derives both sides from the tool, not from `cli`'s internals** — 2026-08-22. The
   accepted names are parsed from the command's **own rejection line**, which is the string
   `list --help` prints, so the test is written against the caller-visible contract. **Rejected:
   importing `filter_names` into the test** — it would compare the implementation with itself, and
   would stay green on a `--json` that had stopped agreeing with the message a caller actually reads.
6. **It is asserted on two projects** — 2026-08-22 — this repository and
   `tests/fixtures/alt-project`, which names different fields. One project passing could be its
   config happening to line up; two with different schemas is about the rule.

**Step 3 — the test, failing on the unchanged code**

```text
$ python -m pytest tests/test_list.py -q -k "MachineForm"
E   AssertionError: Lists differ: [] != ['adopter_visible', 'business_value', 'effort', 'owner', 'type']
    : list accepts --adopter_visible, --business_value, --effort, --owner, --type as a filter and
    the machine form carries no such key, so a caller cannot read back what it selected on.
    Keys: ['blocked', 'blocked_by', 'blocks', 'children', 'id', 'open', 'parent', 'phase',
    'related', 'status', 'title', 'work_package']
FAILED tests/test_list.py::TheMachineFormCarriesWhatItCanFilterOn::test_on_a_project_with_a_different_schema
FAILED tests/test_list.py::TheMachineFormCarriesWhatItCanFilterOn::test_on_this_project
2 failed, 37 deselected in 0.18s
```

Both projects, and the message names the five.

**Step 5 — the key set after, compared with step 1's**

```text
['adopter_visible', 'blocked', 'blocked_by', 'blocks', 'business_value', 'children', 'effort',
 'id', 'open', 'owner', 'parent', 'phase', 'related', 'status', 'title', 'type', 'work_package']
```

Seventeen against twelve, and **every one of the twelve is still there** — which is decision 2's
claim, checked rather than argued.

**Step 6 — the shipped statement that had to change**

[`github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
§*What to read, and why `list --json` is not the source* stated the contract in the present tense:
*it emits `id`, `title`, the columns `index_columns` names, and both directions of every edge*. That
is now false. It reads *every field this project can filter on*, and:

- **the 2026-08-17 measurement beside it is kept and annotated**, not rewritten — four of the five
  fields it names have since arrived and `deliverables` has not, with the reason. It is a record of
  that day (METHOD rule 5);
- **the section's conclusion survives, and its reason is now sharper.** `list --json` is still not
  the source for a migration, because it carries no **body** — and no schema change reaches that.
  The 2026-08-17 rejection of *widen `index_columns`* is restated as what it was: right, and the
  reason the repair went to the machine form instead.

**Step 7 — the gates**

```text
$ python -m pytest tests -q
336 passed, 8 subtests passed in 42.90s

$ ./plugin/bin/taskmd check
OK - 219 task(s), 1095 field value(s), 3690 front-matter value(s), 725 reference(s), 25 dependency edge(s), 331 declared output(s), 1 index file(s), 214 closed record(s), 251 document(s), 3336 link(s), 4773 table row(s), 2 template(s), 10 template field value(s), 5 vocabulary row(s), 3751 section reference(s)
EXIT=0
```

334 before, 336 after: the two tests of decision 6.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py)
- [`plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
- [`tests/test_list.py`](../tests/test_list.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternatives, including what each would cost a caller already parsing `--json` today | met | §2's shape decision names both rejections with their costs, and §3 decision 2 prices the chosen one: five keys added, none removed or renamed, so only a consumer asserting an **exact** key set breaks. Checked against this repository's own tests before the change |
| If the shape changes, a test asserts that **every field `list` accepts as a filter** is present in the machine form — derived from the filter list rather than hand-typed, so the two cannot drift apart again | met | `TheMachineFormCarriesWhatItCanFilterOn` in `tests/test_list.py`. Both sides come from the tool: the flags from its own rejection line, the keys from its own `--json`. §3 decision 5 records why importing `filter_names` into the test was rejected, and decision 6 why it runs on two projects |
| If the shape does not change, the reason is stated where a caller meets it, not only in this record | n/a | The shape changed, so this arm does not apply. The clause it protects against — a decision recorded only in a task record — is met anyway: the contract is written in `cmd_list` beside the loop, and in the shipped binding §*What to read*, both quoted in §3 |
| `check`, `index` and the suite are green, and the output is quoted | met | §3 step 7. `check` exit 0 after `index`, `336 passed, 8 subtests passed` |

**§1's closing line said this task may honestly end with no code change. It did not**, and the reason
is worth one sentence: the third option was a defence of the current behaviour, and the only defence
available was a description of its cause.

**What review found beyond the table.** The shipped statement in §3 step 6 was found by grepping for
every place that describes the machine form — three hits, all in one binding, two of them still true.
It is the class of thing that goes stale silently, and it was **one document away from the code**: a
sweep confined to the plugin's own module would have missed it.

**Open questions, re-read before closing** (`review` step 5). §1 recorded none and none arose.
Nothing is addressed to anyone else.

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | Four criteria, three met and one **not applicable** — the *if the shape does not change* arm, since it did. `--json` now carries every field `list` accepts as a filter, read from `filter_names`, so the five that were selectable and unreadable — `adopter_visible`, `business_value`, `effort`, `owner`, `type` — come back. Additive: the twelve old keys are all still there, compared rather than assumed. The test derives both sides from the command's own output and runs on two schemas. One shipped statement in `github-issues.md` was corrected and its dated measurement annotated. 334 → 336 tests. **Worked under the multi-phase grant recorded at the top of this Log.** |
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it may honestly end with no code change.** §1 allows the answer *leave the machine form as it is*, provided the reason is stated where a caller meets it and not only in this record. Its scope also puts a new config key out by name, because [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) records that one errors every adopter's config on upgrade — no grant of phases licenses that. |
| 2026-08-22 | → proposed | Raised while answering an ordinary question about the backlog — the view the owner asked for needed `effort` and a gate column, and `--json` could supply neither, so it was built from the JSON and the front matter together. Recorded rather than worked around, because the workaround is exactly the file-reading this tool exists to remove. `low` and `s`: nothing is broken and the human view is unaffected, but it is `adopter_visible` because a machine consumer meets it. ~~**Not covered by the multi-phase grant of 2026-08-22**, which names six tasks by id and this is not one of them.~~ **Superseded later the same day** — the owner added this task to the grant; the row above is the authorisation, and this sentence records only what was true at the moment of raising it. |
