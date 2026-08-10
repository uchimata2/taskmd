---
id: T-107
title: Say so when a valid task file is parked where nothing reads it
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-062, T-069, T-075, T-101]
work_package: v0.3
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Found while implementing [T-101](T-101-report-a-template-the-create-path-cannot-see.md) and raised rather than absorbed, per METHOD §3.3: T-101 reports a *template* the create path cannot see, and this is a *task* nothing reads at all. Measured, not argued — a valid `T-002` in `tasks/_drafts/` beside a valid `T-001` in `tasks/` gives `OK - 1 task(s)` at exit 0, with the second file's only trace being the document count. `medium` because the failure needs somebody to move a file into a `_` folder, which is rarer than the two adjacent classes; `s` because the mechanism is a walk that already happens, and the hard half is whether to report at all. The counter is recorded with it: the `_` skip is deliberate and is what lets a project keep its own material beside its tasks, so *documented, not reported* is a legitimate ending — but the present state is neither. |
