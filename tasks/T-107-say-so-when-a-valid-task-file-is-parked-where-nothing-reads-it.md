---
id: T-107
title: Say so when a valid task file is parked where nothing reads it
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-062, T-069, T-075, T-101]
work_package: M2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [tests/fixtures/broken-parked-task/tasks/_drafts/T-002-parked-where-nothing-reads-it.md]
adopter_visible: yes
---

# T-107 — Say so when a valid task file is parked where nothing reads it

## 1. Specify

**Outcome**
A task file that is complete and correct, sitting in a folder `enumerate` skips, is either reported
or is documented as a supported way to park work — so its disappearance is a choice somebody made
rather than one the tool made for them.

**Why this one**
Found while implementing [T-101](T-101-report-a-template-the-create-path-cannot-see.md), and outside
it: T-101 reports a **template** in such a folder, and says nothing about a **task**. Measured on a
scratch project rather than reasoned about — a valid `T-002` in `tasks/_drafts/`, beside a valid
`T-001` in `tasks/`:

```text
OK - 1 task(s), 5 field value(s), ... , 2 document(s), 0 link(s), 0 template(s)
```

Two task files, one task, exit 0, and nothing anywhere says the second exists. It is counted as a
*document*, which is the only trace.

**This is the shape two other classes were raised for.** A near-miss id is reported rather than
skipped ([T-075](T-075-enforce-id-width-when-a-task-file-is-read.md)) and two files claiming one id
are reported rather than silently reduced
([T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md)) — both on the stated ground
that a file dropping out of the project with no signal is worse than a message. The binding says so
in as many words under *enumerate*. A valid task under a `_` folder is the same event with a
different cause, and it is the one case still silent.

**The honest counter.** The `_` skip is documented and deliberate: it is what lets a project keep
templates and its own material beside its tasks without an exclusion list to maintain. A project may
well be parking drafts there on purpose, and reporting them would break that. That is why this task
may legitimately end in *documented, not reported* — but it should not end where it is now, which is
neither.

**Requirements served**
R-16 (`docs/SCOPE.md`), and the *enumerate* rule in the local-Markdown binding that this is the
exception to.

**Scope**
- In: whether a schema-valid id in a skipped folder is reported, and if so how loudly — the near-miss
  class is a counted problem, and this may not warrant that.
- In: whether the binding's *enumerate* rule should instead state parking as supported, and say what
  the cost is.
- Out: templates in skipped folders —
  [T-101](T-101-report-a-template-the-create-path-cannot-see.md), already closed.
- Out: changing the `_` skip itself. It is what makes assumption 6 work without an exclusion list.
- Out: nested projects, which are skipped for a different reason and already tested
  ([T-069](T-069-skip-a-nested-project-at-any-depth.md)).

**Inputs**
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, *enumerate* and assumption 6.
- `plugin/skills/taskmd/taskmd/schema.py` — `load_tasks` and the folder skip.
- [T-101](T-101-report-a-template-the-create-path-cannot-see.md) §3, where this was measured.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, whichever way it goes
- [ ] If reported: a fixture holds a valid task in a skipped folder and it is reported, shown failing
      first
- [ ] If not reported: the binding's *enumerate* rule says parking is supported and what it costs,
      so the silence is documented rather than merely true
- [ ] Whichever way it goes, a project's own material in a `_` folder is still not reported

**Open questions**
- **Report, or document?** *Recommended: report it, as its own class.* The two adjacent classes were
  both raised on the argument that silent loss is the worst outcome, and a task file is a stronger
  claim to being work than a mistyped id is. *Alternative: document parking as supported* — cheaper,
  honest about the existing behaviour, and it leaves a project able to lose a finished task by
  moving it one folder.

## 2. Plan

**Authorisation.** The maintainer asked for the full lifecycle on this task on 2026-08-10. Recorded
per METHOD §3.1; it covers `plan`, `implement` and `review` of T-107 and nothing else.

**Q1 is answered: report it.** Taken on the recommendation already written above, under the standing
authority to settle a delegated question and record what it beat. The alternative — documenting
parking as supported — is rejected on the evidence of the two adjacent classes and on one argument
this task had not made: **a genuine draft does not carry a real id.** A task file before its id is
allocated carries a placeholder, which no test here matches, so it is never reported; a file carrying
a schema-valid id has already been allocated one, and parking it hides work the project believes it
has. Documenting it as supported would bless the one case where it costs something.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | A fixture holding a parked valid task **and** ordinary project material beside it, so the second half of the class is testable | `tests/fixtures/broken-parked-task/` |
| 2 | The failing test, run before any fix, so the class is shown unreported first | recorded run output in §3 |
| 3 | A third anomaly kind in `load_tasks`, found by reading the folders the walk prunes | `plugin/skills/taskmd/taskmd/schema.py` |
| 4 | The `check` line for it, in the shape the other two use | `plugin/skills/taskmd/taskmd/cli.py` |
| 5 | The binding's *enumerate* rule extended from two silent-loss cases to three | `plugin/skills/taskmd/docs/bindings/local-markdown.md` |
| 6 | Tests: the class fires, and a project's own material in the same folder does not | `tests/test_cli.py`, `tests/fixtures/README.md` |
| 7 | Full suite, `check` and `index` on this repository, leak check | run output in §4 |

## 3. Implement

**The vacuous pass, recorded before the fix.** The fixture holds `T-001` in `tasks/` and a complete
`T-002` in `tasks/_drafts/`:

```text
OK - 1 task(s), 5 field value(s), 0 reference(s), ... , 3 document(s), 0 link(s), 0 template(s)
exit=0
```

Three documents, one task, no problem, exit 0 — the same shape T-101 measured, reproduced here as a
fixture so it cannot come back silently.

**After**, on the same fixture:

```text
PARKED TASK   tasks/_drafts/T-002-parked-where-nothing-reads-it.md declares 'T-002', a valid id,
but it sits under a folder beginning with '_' or '.', which enumerate skips - so it is loaded by
nothing, is in no view and is on no edge

1 problem(s) - 1 task(s), ...
exit=1
```

And `list` on the same project, which is the half that matters to somebody not running `check`:

```text
taskmd: 1 problem(s) with the task files - run 'taskmd check'
T-001	proposed	-	specify	The task in the folder that is read
```

**Decisions & assumptions**

- **D1 — reported, as a third anomaly kind, not a fourth mechanism.** `load_tasks` already carries
  two silent-loss classes on `tasks.anomalies`, `check` already prints them and every other command
  already warns that they exist. Parking is the same event with a different cause, so it joins them
  and inherits all three behaviours at once. *Rejected: a standalone check beside the unreachable-
  template one* — that check exists because a template is not a task and cannot ride the task
  anomalies; a parked task is a task, and giving it its own path would mean `list` did not warn.
- **D2 — only a schema-valid id is reported; a near miss under a skipped folder is not.** Two
  reasons to skip it and one message would name neither clearly, and the near-miss class exists to
  catch a file someone meant to be a task in the folder tasks live in. *Rejected: report both*,
  which would fire on any scratch file whose front-matter happens to carry an id-shaped string.
- **D3 — the skip is untouched, and descending into a skipped folder is not a change of mind about
  it.** `_parked_under` reads front-matter and nothing else; nothing it finds is loaded, linked,
  derived from or counted as a task. `.`-prefixed folders are read on the same terms as `_`-prefixed
  ones because the binding's *enumerate* rule names both in one breath, and a class that fired on
  one and not the other would be a rule nobody could state.
- **D4 — no new counted noun.** T-095's counts say what was examined; a parked file is already
  examined as a *document* and counted there, and the anomaly itself is counted as a problem. A
  `parked file(s)` number would count the same file twice under two nouns, which is what T-096
  settled against.
- **D5 — unreadable files under a skipped folder are passed over, not raised on.** That walk is over
  material the project never offered as tasks, so a corrupt notes file must not be able to fail a
  command. The main walk keeps its existing behaviour, deliberately: a bad file *in* `tasks_dir` is
  a different claim.
- **Assumption — "park it" is not a supported workflow, and the binding now says so plainly rather
  than by omission.** A project that wants a task out of the way closes or cancels it. This is the
  half of the answer that would have been lost if the task had ended at "report it".

**Outputs produced**
- `plugin/skills/taskmd/taskmd/schema.py` — `PARKED`, `_parked_under`, and the walk that collects it.
- `plugin/skills/taskmd/taskmd/cli.py` — the `PARKED TASK` line in `check_anomalies`.
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — *enumerate*, two silent-loss cases to three, plus what
  parking now costs and what it still does not.
- `tests/fixtures/broken-parked-task/`, `tests/fixtures/README.md`, `tests/test_cli.py`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative, whichever way it goes | met | §2 records why *report* beat *document parking as supported*, on an argument the specify had not made: a genuine draft carries a placeholder id, so the rule only ever reaches an id already allocated |
| If reported: a fixture holds a valid task in a skipped folder and it is reported, shown failing first | met | `tests/fixtures/broken-parked-task/`; the `OK - 1 task(s) … exit=0` run is in §3, taken before the fix existed |
| If not reported: the binding says parking is supported and what it costs | n/a | It is reported. The binding says the opposite instead — parking is not a way to shelve work, and closing or cancelling is |
| A project's own material in a `_` folder is still not reported | met | `notes.md` sits in the same fixture folder and has its own test asserting it is absent from the output and that exactly one `PARKED TASK` line is printed |
| *(added at review)* Every other class still reports only itself | met | `PARKED TASK` joined `LABELS`, so all twelve sibling fixtures now assert it is **not** in their output |

Suite **169 passed**, up from 167. `check` and `index` clean on this repository at exit 0.

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Full lifecycle in one session on the maintainer's authorisation, recorded in §2. Q1 answered *report it*, and the argument that settled it was not in the specify: **a genuine draft does not carry a real id**, so the rule can only ever reach an id already allocated, and blessing parking would bless exactly the case that costs something. Implemented as a third kind on the anomaly machinery the other two silent-loss classes already use, which is what makes `list` warn as well as `check` report — a standalone check would have got the report and lost the warning. The half most likely to regress has its own test rather than a sentence: `notes.md` sits in the fixture beside the parked task and must stay unreported, because a check that fires on it has stopped being about lost work and become one about where a project files its notes. The binding gained the other half of the answer too: parking is not a supported way to shelve work, and closing or cancelling is. Suite 167 → 169. |
| 2026-08-10 | → proposed | Found while implementing [T-101](T-101-report-a-template-the-create-path-cannot-see.md) and raised rather than absorbed, per METHOD §3.3: T-101 reports a *template* the create path cannot see, and this is a *task* nothing reads at all. Measured, not argued — a valid `T-002` in `tasks/_drafts/` beside a valid `T-001` in `tasks/` gives `OK - 1 task(s)` at exit 0, with the second file's only trace being the document count. `medium` because the failure needs somebody to move a file into a `_` folder, which is rarer than the two adjacent classes; `s` because the mechanism is a walk that already happens, and the hard half is whether to report at all. The counter is recorded with it: the `_` skip is deliberate and is what lets a project keep its own material beside its tasks, so *documented, not reported* is a legitimate ending — but the present state is neither. |
