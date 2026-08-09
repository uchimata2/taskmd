---
id: T-065
title: Say what happens to a field the schema does not name
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-030, T-001]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-065 — Say what happens to a field the schema does not name

## 1. Specify

**Outcome**
The schema config describes what taskmd actually does with a front-matter field it does not
interpret, so the sentence the adoption story rests on is one an adopter can check.

**Why this one**
Raised as **F-5** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. `plugin/taskmd/defaults/config.md` says:

> Task files are the opposite: a front-matter field this schema does not name is **carried and
> displayed, never interpreted**. That is what lets a project adopt taskmd without first rewriting
> its task files.

Shown, not asserted — a task carrying two fields the schema does not name, run through all four
commands:

```
context     status ... | phase ... | type - | work_package - | owner x     (neither field)
index       | ID | Title | Work Package | Status | Phase |                 (neither field)
list        tab-separated: id, status, work_package, phase, title          (neither field)
list --json keys: blocked, blocked_by, blocks, children, id, open,
            parent, phase, related, status, title, work_package            (neither field)
```

**Carried** is true — taskmd never writes a task file, so nothing is dropped from disk. **Displayed**
is false of every documented command. The only code that prints such fields is `taskmd.schema`'s
`main()`, which is undocumented and which
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md) has already decided to **remove** — so
the claim is true today only through a doorway nobody is told about, and false outright once T-030
lands.

**The accurate statement is cheap and already works.** Naming the field in `context_fields` or
`index_columns` displays it, with no code change: those keys take any field name and the commands
read `task.fields` directly. So the honest sentence is *carried, and displayable by naming it* — which
is a better adoption story than the current one, because it tells the adopter what to do.

**Why it is worth a task rather than a note.** The sentence is the whole argument for R-11's
pass-through design, it is in the file every adopter is told to copy, and it becomes plainly false
the moment T-030 is implemented — at which point `Task.extra` is dead code with nothing reading it.

**Requirements served**
R-11 (`docs/SCOPE.md`), and R-13 in spirit — the config is the only description of what a config may
contain, so a false statement there is unresolvable from anywhere else.

**Scope**
- In: the sentence quoted above, and any other place stating the same thing.
- In: what happens to `Task.extra` once nothing prints it — either something does, or its status as
  an unused accessor is recorded.
- In: whether `BINDING.md` §1 *read* — *"Properties the backend does not understand are returned
  unchanged, not dropped"* — is still satisfied by `context`, which
  [`local-markdown.md`](../plugin/docs/bindings/local-markdown.md) declares to be that operation.
- Out: adding a command or a flag to display them. `docs/SCOPE.md` non-goal 11 stands.
- Out: removing the `taskmd.schema` entry point, which is T-030's and is the reason this is worth
  settling now rather than after.

**Inputs**
`plugin/taskmd/defaults/config.md` §*Format*, `plugin/taskmd/schema.py` (`Task.extra`, `known_fields`,
`main`), `plugin/taskmd/cli.py` (`cmd_context`, `cmd_list`, `index_block`),
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md),
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-5.

**Acceptance criteria**
- [ ] The config states what the four commands actually do with an unnamed field, checked by running
      them on a task that carries one
- [ ] The route that *does* display it is named, so the sentence tells an adopter what to do rather
      than only what is true
- [ ] The claim survives T-030's removal of the schema entry point — it does not depend on it
- [ ] `BINDING.md` §1 *read* and the local binding's *read* are re-checked against the answer, and
      either still hold or are recorded as needing change
- [ ] Shown on a real case, per `CLAUDE.md` *Verifying*: a task with an unnamed field, before and
      after

**Open questions**
- None. The correction follows from what the commands do; whether `Task.extra` keeps a reader is a
  `plan` question with no owner decision in it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised as F-5 from the T-059 audit, clause 1. Run before write-up on a scratch project: a task carrying two unnamed fields showed them in none of the four commands. `medium`/`xs` — one sentence, but it is the sentence R-11's adoption argument rests on, it sits in the file every adopter copies, and T-030 turns it from misleading into false. |
