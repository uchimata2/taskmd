---
id: T-149
title: Check that every prose list of list's options names the options there are
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-117, T-134, T-139, T-144]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-15
updated: 2026-08-16
adopter_visible: yes
deliverables: []
---

# T-149 — Check that every prose list of list's options names the options there are

## 1. Specify

**Outcome**
A document stating `list`'s flags and getting the set wrong fails the suite, the same way
[T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) already
makes that true of the command set.

**Why this one**
T-134 built exactly this check for the four command *names* and put the flags explicitly out of
scope, on a reason it stated: `list`'s options "are not a set anything else states, and checking them
would be a second surface with its own drift". That was true when it was written.

[T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) made it false.
`LIST_OPTIONS` is now the one home for those flags, read by `parse_filters` and by `list --help`, so
there **is** something else to check a document against and the second surface T-134 declined to
build already exists. The prose copies did not go away: `cli.py`'s module docstring and the skill's
own `SKILL.md` both spell the flags out, and nothing holds either to the table.

This is the same defect class T-073 measured — a document outliving its correction for four days —
one surface over.

**Requirements served**
R-1, R-18 (`docs/SCOPE.md`); the design rule from the other side, that a fact allowed two homes needs
the two homes held together by something.

**Scope**
- In: the flag lists in `plugin/skills/taskmd/taskmd/cli.py`'s module docstring and in the skill's
  `SKILL.md`, checked against `cli.LIST_OPTIONS`.
- In: whether a document mentioning one flag in passing is a list — the same question T-134 answered
  for commands, and its answer may not transfer, since a flag is named in prose far more often than a
  command is.
- Out: the filters. Those are the project's own vocabulary rather than taskmd's, so a shipped
  document naming this repository's fields would be the defect, not the check's subject.
- Out: reopening T-117 or T-134. This exists because both answers were chosen.
- Out: `--root`, which is `main`'s and not in `LIST_OPTIONS`.

**Corrected 2026-08-16, while working this phase.** The in-scope line above names two documents; the
corpus has **one**. `SKILL.md` names `--open --limit 1` in a single invocation and `--root` in a
sentence, and states no set — so under T-134's own rule it is a mention, not a list, and marking it
would assert a completeness the document does not mean. A sweep of every tracked document for the
four flags found no other statement of the set either: `README.md` names `--json` in passing beside
three *filters*, the bindings' hits are `gh`'s own flags, and the audit's are measurements. So the
one home to guard is `cli.py`'s module docstring. The outcome and the criteria below are unchanged —
this narrows where the check is armed, not what it must catch.

**Inputs**
- [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  shape of the check, and the out-of-scope line this task exists to revisit.
- [T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) §3 — what
  `LIST_OPTIONS` is and what already reads it.
- `tests/test_publishing.py` — how a test reads a rule out of a document rather than restating it.

**Acceptance criteria**
- [ ] A document listing `list`'s flags and missing one, or naming one that does not exist, fails the
      suite — shown by making it fail, not by reading the test
- [ ] The check derives the true set from `cli.LIST_OPTIONS` and writes no flag name of its own
- [ ] T-134's out-of-scope line carries a note saying what changed, so a reader does not conclude the
      flags were considered and excluded on grounds that still hold

**Open questions**
- **Is `SKILL.md` in reach of a test that runs here?** T-134's check reads `README.md` and `cli.py`;
  `SKILL.md` is inside the plugin subtree and is what an adopter is actually served. If the existing
  test's mechanism does not reach it, that is a finding worth more than this check — the project
  owner decides whether to widen it or to record the gap.

  **Answered 2026-08-16, by running it rather than by reading the test.** T-139 replaced the two
  named documents with a sweep of `git ls-files --cached --others --exclude-standard`, and that
  listing contains `plugin/skills/taskmd/SKILL.md`:

  ```
  $ git ls-files --cached --others --exclude-standard | Select-String SKILL.md
  plugin/skills/taskmd/SKILL.md
  ```

  So there is no gap to record and nothing for the owner to widen: any document in the plugin subtree
  that opts in by marker is already checked wherever it sits. The question was raised on 2026-08-15
  against T-134's mechanism, and T-139 had generalised it the same day.

## 2. Plan

T-139 built the general mechanism, so the shape of this work is *use it*, not *build a second one*.
Its comment claims adding a kind is one row and a pair of markers; step 3 exists because that claim
is false today, in a way only a second kind can expose.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give the docstring's four switches a line of their own, wrapped in a `taskmd:list-options` region. They are mid-line today, beside `--<field>` and `--root`, and a region is line-scoped | `plugin/skills/taskmd/taskmd/cli.py` module docstring, two blocks where there was one |
| 2 | Add one `Kind` row: marker `list-options`, pattern reading `--flag` tokens out of the region, `owned` derived from `cli.LIST_OPTIONS`, `required` naming `cli.py` alone | one row in `KINDS`, `tests/test_publishing.py`; no flag name written anywhere in the test |
| 3 | Make `test_a_name_mentioned_in_a_sentence_is_not_a_list` tolerate a kind `README.md` carries no region of — it calls `next()` with no default, so a second kind raises `StopIteration` — and read the whole file as *outside* when there is no region | `tests/test_publishing.py`, that test only |
| 4 | Make it fail three ways on the real tree: a flag dropped from the region, a flag named that does not exist, the markers deleted | three recorded failures in §3, each with the message |
| 5 | Note on T-134's out-of-scope line what changed, so its reason is not read as still holding | `tasks/T-134-…md` |
| 6 | Run the suite, then `check` and `index` | green output quoted in §3 |

## 3. Implement

**Decisions & assumptions**
- **The docstring's `list` line is split in two, and the switches get a line of their own** —
  2026-08-16. A region is line-scoped, and the four switches sat mid-line between `[--<field> V]` and
  `[--root PATH]`, neither of which is in `LIST_OPTIONS`. The alternative was a pattern that skips
  them, which means writing `root` into the test — the exact thing criterion 2 forbids, and the thing
  that makes such a check rot. The invocation line keeps `[OPTIONS]` in their place, so the commands
  region still reads as four invocations.
- **`required` names `cli.py` alone, and `README.md` is deliberately not marked** — 2026-08-16.
  `README.md` names `--json` in the paragraph about filters, and `--open --limit` in two invocations;
  it never claims to state the set. T-134's class docstring already settled what a marker means — *a
  claim of completeness, not of importance* — and marking that paragraph would make the document
  assert something it does not mean.
- **`SKILL.md` is not marked either, for the same reason**, and the §1 correction records why it was
  expected to need marking and does not.
- **The third test was changed, which the plan said would happen and the mechanism said would not** —
  2026-08-16. T-139's comment claims a kind is one row plus a pair of markers.
  `test_a_name_mentioned_in_a_sentence_is_not_a_list` falsified it: it located `README.md`'s region
  with `next()` and no default, so the first kind that document does not carry raised
  `StopIteration` rather than failing an assertion. It now treats *no region* as *the whole file is
  outside*, which is what the test means anyway, and the claim is true again. Fixed here rather than
  raised as a child task because it is not a defect found in passing — it is the mechanism this task
  had to use, and using it is what exposed it.

**Evidence — the check was made to fail, three ways, on the real tree**

Dropping `[--json]` from the region:

```
AssertionError: plugin/skills/taskmd/taskmd/cli.py's list-options list is behind: it does not name
['--json'], and it names nothing extra which do not exist
```

Adding a `[--sort FIELD]` that does not exist:

```
AssertionError: plugin/skills/taskmd/taskmd/cli.py's list-options list is behind: it does not name
nothing missing, and it names ['--sort'] which do not exist
```

Deleting the two markers — caught twice, by the floor and by the sweep:

```
AssertionError: [] is not true : no document carries a taskmd:list-options region, so this kind is
declared and checked against nothing
```

The test writes no flag name of its own, which is checked rather than asserted — exit 1 is *no match*:

```
$ git grep -nE '\-\-(open|closed|limit|json)' -- tests/test_publishing.py
$ echo $?
1
```

Restored, then the suite, `check` and `index`:

```
264 passed, 3 skipped, 6 subtests passed in 21.50s
OK - 162 task(s), ... 192 document(s), 1810 link(s), ...
Wrote tasks/README.md - 17 active, 145 closed
```

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — module docstring: `[OPTIONS]` in the commands region, and a
  `taskmd:list-options` region carrying the four switches
- `tests/test_publishing.py` — one `Kind` row, and the mention-versus-list test made kind-agnostic
- `tasks/T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md` — the
  note on its out-of-scope line and on the matching decision

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A document listing `list`'s flags and missing one, or naming one that does not exist, fails the suite — shown by making it fail, not by reading the test | met | Both directions run and quoted in §3, plus a third case the criterion did not ask for: deleting the markers, which is how a guard is disarmed rather than broken |
| The check derives the true set from `cli.LIST_OPTIONS` and writes no flag name of its own | met | The row is `lambda cli: set(flag for flag, _, _, _ in cli.LIST_OPTIONS)`, and a `git grep` of the four flag spellings across `tests/test_publishing.py` exits 1 — the command and its empty result are in §3 |
| T-134's out-of-scope line carries a note saying what changed | met | Its §1 line and its matching §3 decision both carry it, because the decision would otherwise still read as standing |

**Child fix tasks raised**
- none. The one thing found in passing — the third test's `next()` — is the mechanism this task was
  built on rather than an unrelated defect, so it is fixed here and recorded in §3.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | Full lifecycle in one session under the authorisation below. `specify` corrected its own in-scope line: the corpus is one document, not two, and the parked question about `SKILL.md` was answered by running `git ls-files` rather than by reading the test. `implement` used T-139's mechanism and, in using it, falsified its *adding a kind is one row* claim — one kind is one row **and** a test that no longer assumes `README.md` carries every kind. `review` judged all three criteria met, no child task. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, unattended**, given 2026-08-16 as the subject of a handoff — *a vast amount of task alone, unattended*, the maintainer having selected the batch from a list put to them and answered two questions about it. It covers [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md), [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) and [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) and **nothing else** — not the six `decision` tasks beside them, not the three parked on the `InstructionsLoaded` hook, and **not anything these four raise**, which are filed and left. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. |
| 2026-08-15 | → proposed | Raised from T-144's `implement`, under METHOD §3.3: actionable, outside that task, so it costs one record rather than a silent widening. T-144 §1 named it as out of scope while `specify` was being written, before the home existed that makes it possible. `low` because the prose is correct today and the risk is drift rather than a live defect — but it is the drift class T-073 measured at four days, and the flags now have exactly the computed home whose absence was T-134's reason for declining. |
