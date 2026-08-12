---
id: T-101
title: Report a template the create path cannot see
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-032, T-051, T-076, T-091, T-095]
work_package: M2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/schema.py, plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, tests/fixtures/README.md, tests/fixtures/broken-unreachable-template/tasks/_templates/task-template.md]
---

# T-101 — Report a template the create path cannot see

## 1. Specify

**Outcome**
A project that keeps its task templates one level down is told that nothing will find them, instead
of being read as a project that has no template — which is a legal state and looks identical.

**Why this one**
Raised as **R-3** by the first adopting project (`control/LOCAL-CONTEXT.md`), and it is the half of
R-3 that [T-032](T-032-repair-the-audit-template-and-validate-templates.md) does not already carry.

The binding defines a template as a `_`-prefixed Markdown file **directly in** `tasks_dir`, and says
listing them is how you find one. That project kept both of its templates in `tasks/_templates/` — a
folder `enumerate` skips because its name begins with `_`. The listing returned nothing, and the
binding's documented reading of nothing is that *a project with no template is a normal project*. The
silence runs both ways: nothing reports a missing template, and nothing reports one that is present
and unreachable.

**`_templates/` is not a mistake an adopter has to be careless to make** — it is the obvious place to
put templates, and this repository put them there too until
[T-076](T-076-decide-what-a-template-s-links-resolve-against.md) moved them out. So this repository
can no longer reach the case by accident, and the adopter is the evidence for it.

**What it cost there.** A decision task open for two days, and a project running with two task
templates at once without a single document mentioning the second — the shipped
`_task-template.md` had arrived at the compliant location during migration, referenced by nothing and
declared by no task. An agent following the create procedure finds *that* one. Discovery was not
broken any more; it was wrong in a way that looks correct. The stray-copy half is
[T-091](T-091-make-the-shipped-task-template-survive-being-copied.md)'s; the unreachable half is this.

**Requirements served**
R-16 (`docs/SCOPE.md`) — a class the validator does not catch. R-17, since it is a setup fact that
currently surfaces, if at all, inside whatever task the agent was trying to create.

**Scope**
- In: one line from `check` — R-3 suggests `TEMPLATE UNREACHABLE` — for a `_`-prefixed folder under
  `tasks_dir` holding Markdown whose id is a placeholder rather than a valid id.
- In: what makes a file in such a folder a *template* rather than somebody's notes, since the folder
  is skipped precisely so a project can keep things there.
- Out: validating a template's front-matter. That is
  [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s second in-scope item and this
  task must not duplicate it.
- Out: a config key naming a template folder. The binding argues the location rule down to *there is
  no path to be told and none to go stale*, and a key would undo that rather than fix this.
- Out: reporting that a project has **no** template. The binding states that as a legal, deliberate
  silence, and it stays one.

**Inputs**
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, *create* → *Which template*, and
  *enumerate*.
- `plugin/skills/taskmd/taskmd/schema.py` — `load_tasks` and the `_`/`.` folder skip.
- [T-076](T-076-decide-what-a-template-s-links-resolve-against.md), for why the location rule is what
  it is, so a fix does not weaken it.

**Acceptance criteria**
- [ ] Shown failing first, per R-16: a fixture with a template under `tasks/_templates/` is reported
- [ ] A project with a compliant `_`-prefixed template in `tasks_dir` stays silent
- [ ] A project with no template at all stays silent — the legal case above
- [ ] Something the project keeps in a `_`-prefixed folder that is *not* a template does not produce
      the line, or the rule says plainly why it does
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- None. **Q1 — what identifies a template inside a skipped folder? — decided 2026-08-10 under the
  standing authorization to settle delegated questions: a Markdown file carrying the id field with a
  placeholder in it**, a value that is neither an id nor a near miss. That is the test `load_tasks`
  already applies when it declines to read `tasks/_task-template.md` as work, so it names no new rule
  and adds no configuration. *Rejected: any Markdown in a `_`-prefixed folder* — simpler, and it
  reports a project's own notes as a broken template, which makes the class the noise it was raised
  to remove.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the fixture where an adopter would actually put it — `tasks/_templates/` — and watch `check` pass on it | The *before*, per `CLAUDE.md` *Verifying* |
| 2 | Write what a template is, once, in the schema module, keyed on the placeholder id and not on the folder | `plugin/skills/taskmd/taskmd/schema.py` |
| 3 | Report the unreachable ones, and **count all of them** | `plugin/skills/taskmd/taskmd/cli.py` |
| 4 | Join the class to the fixture set and its documentation | `tests/test_cli.py`, `tests/fixtures/README.md` |
| 5 | Suite, `index`, `check`, pre-publish check | Recorded output |

**Shape decisions.**

**D1 — The rule is the placeholder id; the folder decides only *reachability*.** Two separate
questions, deliberately kept apart: *is this a template* is a fact about the file's content, and
*can create find it* is a fact about where it sits. Keeping them apart is what lets the report say
which of the two a project got wrong, and what keeps a project's own material in a `_` folder out of
the class entirely. It also means the compliant case is recognised by the same test, which is what
makes the count below possible.

**D2 — Templates are counted whether reachable or not, and this closes R-3's other half at no
cost.** R-3 says the silence runs both ways: *"nothing reports a missing template, and nothing
reports one that is present but unreachable."* The second is the problem class. The first is **not a
defect** — the binding states plainly that a project with no template is a normal project — so it
cannot become a failure. A count can say it without saying it is wrong: `0 template(s)` in the
summary tells a project it has none, where before it could only *find* that it had none by running
the listing and reading nothing. This is T-095's rule applied to a class whose normal case is finding
nothing. *Rejected: reporting the absence* — it would make a documented, legal state fail.

**D3 — It is a counted problem, not an advisory.** Unlike a pinned config (T-100), which is a legal
state, an unreachable template is a file the project's own binding says will never be found. The
whole finding is that its silence is indistinguishable from absence; an advisory a reader may skip
reproduces that at lower volume. *Rejected: advisory* — for that reason.

**Planned outputs**
- `plugin/skills/taskmd/taskmd/schema.py` — `templates`
- `plugin/skills/taskmd/taskmd/cli.py` — `check_unreachable_templates`
- `tests/fixtures/broken-unreachable-template/`, `tests/fixtures/README.md`, `tests/test_cli.py`

## 3. Implement

### Steps 1–3 — the class

The fixture puts a template in `tasks/_templates/`, beside a valid task so the run fails on one
thing only. Before the change `check` returned `OK - 1 task(s)` at exit 0 — the silence R-3
described, reproduced rather than asserted. After:

```text
TEMPLATE UNREACHABLE tasks/_templates/task-template.md carries a placeholder id, so it is a
template - but create lists '_'-prefixed files directly in tasks/, so nothing will find it

1 problem(s) - 1 task(s), 5 field value(s), ... , 2 document(s), 0 link(s), 1 template(s)
                                                                                    exit 1
```

The message names the rule and the fix rather than the violation alone, because the project reading
it has just been told that something it believed was set up is not.

**The count is the half that is not a failure.** On this repository:

```text
OK - 107 task(s), ... , 2 template(s), 0 vocabulary row(s)
```

Two, both reachable, both directly in `tasks/` since
[T-076](T-076-decide-what-a-template-s-links-resolve-against.md) — so the live case exercises the
compliant branch on every run, and a rule that had keyed on the folder rather than the id would have
broken here immediately.

### Step 4 — and one thing found on the way, raised rather than fixed

A file with a **valid** id inside a `_` folder is not a template, correctly, and it is also not a
task — `enumerate` never opens the folder. Measured on a scratch project: two task files, `OK - 1
task(s)`, exit 0, and the second file's only trace is the document count. That is the shape
[T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) and
[T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) were both raised for, still silent in one
place. Outside this task, which is about templates. Raised as
[T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md).

### Step 5 — the suite and this repository

```text
Ran 166 tests in 6.590s                                                                      OK
OK - 107 task(s), 535 field value(s), 331 reference(s), 22 dependency edge(s), 144 declared
     output(s), 1 index file(s), 135 document(s), 1027 link(s), 2 template(s),
     0 vocabulary row(s)
```

Figures from the run taken **after** this record and T-107 were written, so a later reader can
reproduce them.

**One guard fired, and it was right to.** The first draft of the new docstring cited the reported
gap by its number in the adopter's report, and `ThePluginShipsWhatItCites` failed: the plugin may not
cite a document it does not ship, and an `R-n` in shipped code reads as a `docs/SCOPE.md`
requirement, which an adopter never receives (T-064). Rephrased to state the rule instead of citing
it. Worth recording because the failure looked like a false positive for about a minute and was not.

**Decisions & assumptions**

- **The walk is `check`'s, not `enumerate`'s.** — `load_tasks` still skips `_` folders exactly as
  before; nothing that reads tasks changed. A second, narrower walk was cheaper than teaching the
  first one to return things it must not return, and it keeps the binding's *enumerate* rule true as
  written. — 2026-08-10
- **A file that cannot be read is skipped rather than reported.** — Unreadable bytes under a task
  folder are not this class's finding, and guessing would produce a message about templates for a
  file that is not one. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/taskmd/schema.py` — `templates`
- `plugin/skills/taskmd/taskmd/cli.py` — `check_unreachable_templates`
- `tests/fixtures/broken-unreachable-template/` — the fixture
- `tests/test_cli.py` — the class test plus `ATemplateIsCountedRatherThanInferred`
- `tests/fixtures/README.md` — the fixture set's own documentation
- [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Shown failing first, per R-16: a fixture with a template under `tasks/_templates/` is reported | met | §3 steps 1–3. `OK - 1 task(s)` at exit 0 before, `TEMPLATE UNREACHABLE` at exit 1 after, on a fixture placed where an adopter would actually put it. |
| A project with a compliant `_`-prefixed template in `tasks_dir` stays silent | met | Tested on a scratch project and true of this repository on every run — two templates, counted, not reported. |
| A project with no template at all stays silent — the legal case above | met | Tested. And **improved beyond the criterion**: it now reads `0 template(s)` in the summary, so a project is told it has none rather than having to infer it from silence. That is R-3's other half, closed without making a legal state fail (**D2**). |
| Something the project keeps in a `_`-prefixed folder that is *not* a template does not produce the line, or the rule says plainly why it does | met | Tested with a note carrying no front-matter at all. **D1** is why: the rule keys on a placeholder id, never on the folder. |
| The suite still passes and `check` is clean on this repository | met | `Ran 166 tests … OK`, `check` OK. |

**Child fix tasks raised**
- [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) — a **valid** task
  file in a skipped folder is silently not a task. Found during `implement`, raised rather than
  fixed.

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Reviewed against the five criteria as written; **all five met, none carried**, so the task closes. Criterion 3 is met beyond what it asked: a project with no template now reads `0 template(s)` in the summary, so R-3's *other* silent direction — nothing reports a missing template — is closed by a count rather than by a failure, which keeps a documented legal state legal (**D2**). One child raised and not fixed: [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md), a **valid** task file in a skipped folder being silently not a task, measured rather than argued. `deliverables` names the five files. Pre-publish check run last, after this record was written: **193 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All five steps taken. Shown failing first on a fixture placed where an adopter would actually put it — `tasks/_templates/`, the folder this repository itself used until T-076 — which returned `OK - 1 task(s)` at exit 0 before the change. **D1 is what the implementation turns on**: the rule keys on a *placeholder id*, never on the folder, so *is this a template* and *can create find it* stay separate questions and a project's own notes in a `_` folder are untouched. That also made **D2** possible at no cost, since the compliant case is recognised by the same test. `check` gained a narrower second walk rather than teaching `load_tasks` to return things it must not return, which keeps the binding's *enumerate* rule true as written. Found on the way and raised as T-107: a file with a valid id inside a `_` folder is not a template and is also not a task — two task files, `OK - 1 task(s)`, exit 0, the second traceable only in the document count. Suite `Ran 166 tests … OK`. |
| 2026-08-10 | → planned | Plan written; §1's Q1 settled as **D1** under the standing authorization to decide delegated questions — a template is a file carrying the id field with a placeholder in it, which is the test `load_tasks` already applies, with *any Markdown in a `_` folder* rejected because it would report a project's notes as a broken template. Two further decisions the specify did not anticipate: **D2**, that templates are counted whether reachable or not, which closes R-3's other silent direction without making a legal state fail; and **D3**, that this is a counted problem rather than an advisory — unlike T-100's config drift, an unreachable template is not a legal state but a file the project's own binding says will never be found. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"keep going with T-101, full lifecycle"*. It covers this task alone and **does not generalise**; it is the third such waiver in this session. Recorded here for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) exists. |
| 2026-08-10 | → proposed | Raised as R-3 from the first adopting project's recommendations — the half T-032 does not carry. T-032 already wants a template's front-matter validated; this is the case where the file is never opened at all, because it sits in a `_`-prefixed folder that `enumerate` skips, and the resulting silence reads as the legal "this project has no template". `medium` rather than high because the cost is a slow discovery rather than a wrong answer, and because T-076 has already moved this repository's own templates out of that folder; the adopter is the only evidence, which is exactly why it is worth having. `s` because the information is in hand during the walk `check` already does. |
