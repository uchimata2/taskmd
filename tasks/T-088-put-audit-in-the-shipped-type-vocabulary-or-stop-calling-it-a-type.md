---
id: T-088
title: Put audit in the shipped type vocabulary, or stop calling it a type
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-001, T-026, T-032]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-088 — Put audit in the shipped type vocabulary, or stop calling it a type

## 1. Specify

**Outcome**
The method and the shipped schema agree about what an audit is, so a project that follows METHOD §5
literally does not fail `check`.

**Why this one**
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5 opens: *"An audit is a **task type**, not a
phase."* The shipped schema's `type` vocabulary is `analysis, decision, deliverable, research, fix,
admin`. There is no `audit` in it, so writing the thing the method names produces:

```
VOCABULARY    T-NNN.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
```

**Two projects have now hit this, and neither noticed on its own.** This repository types its audit
umbrellas `analysis` (T-026, T-059) and never remarked on it. The first adopting project
(`control/LOCAL-CONTEXT.md`) carried two tasks typed `audit` for five days: its own standard had no
such value either, and nothing said so until taskmd's validator read them on 2026-08-09. A rule that
two independent projects work around by inventing the same substitute is a rule whose vocabulary is
wrong, not two projects making the same mistake.

**Requirements served**
R-5 (`docs/SCOPE.md`) — audit is a task type and findings become child tasks. R-11, since the answer
is a schema question rather than a code one.

**Scope**
- In: the `type` row of `plugin/skills/taskmd/taskmd/defaults/config.md`, or METHOD §5's wording.
- In: whether `decision` and `audit` are the same kind of addition, since `decision` is in the
  shipped list and is not named by the method at all.
- Out: any behaviour. Nothing branches on `type` today; it is vocabulary and display.
- Out: the audit *procedure*, which is `docs/method/audit.md` and is not at issue.

**Inputs**
- METHOD §5 and [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md).
- The `type` row in `plugin/skills/taskmd/taskmd/defaults/config.md`.
- T-026 and T-059 in this repository, both audit umbrellas typed `analysis`.

**Acceptance criteria**
- [ ] A task following METHOD §5 word for word passes `check` on a project with no config, shown by
      creating one in a fixture rather than by reading the vocabulary
- [ ] Whichever way it is settled, the method and the schema say the same thing afterwards, checked
      by reading both
- [ ] The existing umbrellas in this repository are either retyped or explicitly left, with the
      reason

**Open questions**
- **Which of the two moves. Answered by the maintainer on 2026-08-09: add `audit` to the
  vocabulary.** The method's wording stays as it is.

  **The objection to adding it does not survive the scope's own second question.** "It adds a value
  that changes nothing the tool does" is true of *every* value in that row — nothing branches on
  `type`, by this task's own out-list. And `decision` is already shipped while the method never names
  it, which settles what the row is: a **useful default vocabulary, not a projection of the method's
  nouns**. So `audit` and `decision` are the same kind of addition, and adding `audit` sets no
  precedent that the vocabulary must track METHOD's wording.

  *Rejected: reword §5 to say an audit is a "kind of task".* §5's sentence is built on the contrast
  *type, not a phase*, and that contrast is the whole point of the line — nothing passes through an
  audit. "Kind" is also already spoken for: §4 uses it for the three edge kinds. Rewording would
  trade a one-word vocabulary gap for a term-of-art collision in the document that defines both
  terms.

  **The evidence is that two projects invented the same substitute.** This repository typed its
  umbrellas `analysis` and never remarked on it; the first adopting project used `audit` and could
  not validate. A word two independent projects reach for is missing from the list, not misused.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Add `audit` to the `type` row, and say in the *Vocabularies* prose what that row is — a default worth having, not the set of nouns METHOD uses — so the next reader does not treat the two as needing to match. | `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 2 | Prove it on a project with no config: build a task typed the way METHOD §5 words it and run `check` against it. | A test beside `test_a_bare_folder_of_tasks_works`, and its output in §3 |
| 3 | Retype this repository's two audit umbrellas, one of which is closed, and record the reason either way. | T-026, T-059 |
| 4 | Read METHOD §5 and the vocabulary against each other, then the suite and the index. | The reading and the runs, in §3 |

**Criterion 1 says "in a fixture", and step 2 builds one in the test rather than adding a directory
under `tests/fixtures/`.** Those directories earn their place by being reproductions worth keeping —
the `broken-*` set is one defect each, runnable by hand on the day a class regresses. A positive
vocabulary case has no such day: if it regresses, every project fails at once. `RunsOnACloneWithNoConfiguration`
is already the home for "a project with no config", which is the condition the criterion actually
names. Flagged in §4 so the reading can be rejected cheaply.

## 3. Implement

**Decisions & assumptions**
- **Both umbrellas retyped, including the closed one — 2026-08-09.** Criterion 3 allows either.
  `type` says what a task *is*, nothing branches on it, and the alternative was for the repository
  that removed the workaround to keep demonstrating it. The Log row on each carries the history, so
  nothing is lost by the front-matter being correct. *Rejected: leave T-059 as `analysis` because it
  is `done`.* Defensible — a closed record is a dated account — but it would leave a reader of the
  audit umbrellas with no way to tell a deliberate choice from an omission.
- **The vocabulary prose now says what the row is — 2026-08-09.** Not just the word. The scope's
  second question was whether `decision` and `audit` are the same kind of addition; the answer is
  written into the config so the next person does not re-derive it from the table's contents.

**Verification**

The new test against the pre-fix vocabulary, produced by stashing the one-line config change:

```
AssertionError: 1 != 0 : VOCABULARY    T-001.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
1 problem(s) over 1 task(s)
FAILED (failures=1)
```

The same test with the row restored: `Ran 1 test  OK`.

**The real case, which is the one that matters.** The deck-building sibling
(`control/LOCAL-CONTEXT.md`) is where this defect was found. Before and after, with **no change to
any of its sixty files**:

```
before   VOCABULARY    T-042.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
after    OK - 60 task(s), vocabulary valid, references resolve, no broken links
```

**Method and schema read against each other.** METHOD §5 opens *"An audit is a task type, not a
phase"*; the shipped `type` row now contains `audit`. No wording changed in METHOD.

**Suite and host**, after the change:

```
OK - 89 task(s), vocabulary valid, references resolve, no broken links
test_cli.py  42 tests OK   test_list.py  18 OK   test_runtime.py  27 OK   test_schema.py  44 OK
```

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — the row, and the prose saying what the row is
- [`tests/test_cli.py`](../tests/test_cli.py) — the no-config proof
- [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) — retyped, each with its reason in the Log

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A task worded as METHOD §5 words it passes `check` on a project with no config, shown by creating one | met | Built in a temp project with no `.taskmd/`, asserted to pass and to print no `VOCABULARY` line; shown failing first by stashing the config change. See the note below on where it was built |
| Method and schema say the same thing afterwards, checked by reading both | met | METHOD §5 unchanged and still reads "a task type, not a phase"; the `type` row now carries `audit`. The config's prose additionally records *why* the two need not track each other, which the reading exposed as the thing that would otherwise be re-derived |
| The existing umbrellas are retyped or explicitly left, with the reason | met | Both retyped, including the closed T-059; the reason and the rejected alternative are in each task's Log and in §3 |

Three met, none carried.

**Where the proof was built, flagged because criterion 1 said "in a fixture".** It is a temp project
constructed inside `RunsOnACloneWithNoConfiguration`, not a directory under `tests/fixtures/`. The
reasoning is in §2: those directories earn their place as hand-runnable reproductions for the day a
class regresses, and a positive vocabulary case has no such day. The criterion's substantive demand —
created rather than read, on a project with no config — is met either way. Cheap to reject: it is one
directory and three lines.

**The strongest evidence is not in the criteria.** None of them asked for the adopting project to be
re-run, and that is what actually settles it: sixty task files that could not validate now do, with
nothing changed on their side. A criterion set written before the fix could not name that, which is
worth remembering the next time one looks complete.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | -> done | Settled by adding the word rather than rewording the method. The objection to adding it -- a value that changes nothing the tool does -- turned out to be true of every value in that row, and `decision` being shipped while the method never names it settles what the row is: a useful default, not a projection of METHOD's nouns. That answer is now written into the config's prose, because it is the thing the next reader would otherwise re-derive from the table's contents. Both of this repository's audit umbrellas were retyped, the closed one included. Proven where it was found: the deck-building sibling's sixty task files went from one VOCABULARY failure to OK with nothing changed on their side. |
| 2026-08-09 | → proposed | Raised the day the first project outside this repository adopted taskmd, whose validator immediately reported two of its tasks as having an invalid `type: audit`. The value is absent from the shipped vocabulary and present in the method's own sentence about what an audit is. This repository has been working around it since T-026 without noticing, which is the part that makes it worth a task rather than a note: the workaround was invisible because everyone reached for the same substitute. |
