---
id: T-065
title: Say what happens to a field the schema does not name
type: fix
status: done
phase: review
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
| 1 | Reproduce on a scratch project: a task carrying two fields the schema does not name, through all four commands | The failing evidence |
| 2 | Prove the replacement claim before writing it — name the same two fields in `context_fields` and `index_columns` and see whether they appear | The transcript that licenses the new sentence |
| 3 | Correct the sentence in the copied config, saying both what is true and what to do | `plugin/taskmd/defaults/config.md` |
| 4 | Re-check `BINDING.md` §1 *read* and the local binding's *read* against what `context` actually prints | Either a confirmation or a correction |
| 5 | Settle `Task.extra`: a reader, or its status recorded | `plugin/taskmd/schema.py` |
| 6 | Simulate T-030 — remove `schema.main()` — and confirm the new claim still holds | The transcript |

**Why step 2 precedes step 3.** The finding asserts the display route works *"with no code change"*.
That is the whole replacement claim, and writing it into the file every adopter copies on the
strength of reading `cmd_context` would repeat the mistake being fixed.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — `Task.extra` keeps no reader, and says so** — 2026-08-09. The display route reads
  `Task.fields` directly, so it needs nothing from `extra`; the only reader is `schema.main()`, which
  T-030 removes. Rather than inventing a use, its docstring now records that it has none and that it
  should leave with `main()`. *Rejected: deleting it now* — that is T-030's commit, and removing it
  here would take a decision out of the task that owns it.

- **D2 — the local binding's *read* was wrong about `context`, and is corrected here** — 2026-08-09.
  The criterion offered "still holds **or** is recorded as needing change". It does not hold:
  *"`taskmd context <id>` is this operation plus the derived edges"* is false, because `context`
  prints no body and no field the project did not name. Correcting it rather than only recording it,
  because the defect is the same class this task exists to fix — a document claiming behaviour the
  tool does not have — and it is one sentence in a file already open. `BINDING.md` §1 *read* itself
  needs no change: *read* for this backend is **opening the file**, which is exactly what it says.

  This is the finding underneath, and it is worth more than the sentence: the confusion was that
  `context` looks like the read operation. It is a *summary*, and calling it `read` is what made
  "carried and displayed" sound true.

### Step 1 — shown failing first

A task carrying `sprint: 2026-Q3` and `reviewer: someone`, on a project with the shipped default:

```
context      status proposed | phase specify | type deliverable | work_package - | owner -
list --json  blocked, blocked_by, blocks, children, id, open, parent, phase, related,
             status, title, work_package
```

Neither field, in either. **Carried** was true; **displayed** was false of every documented command.

### Step 2 — the replacement claim, proved before it was written

The same project, with the two fields named in the config and nothing else changed:

```
context_fields: [status, phase, sprint, reviewer]
index_columns:  [sprint, status]

taskmd context T-001
status proposed | phase specify | sprint 2026-Q3 | reviewer someone

taskmd index  ->  | ID | Title | Sprint | Status |
                  | [T-001](...) | Carries two fields ... | `2026-Q3` | `proposed` |
```

No code change, no schema entry. The corrected sentence tells an adopter this rather than only
telling them the truth about the default.

### Step 6 — the claim outlives T-030

`schema.main()` replaced by a stub that refuses to run, standing in for T-030's removal:

```
taskmd context T-001
status proposed | phase specify | sprint 2026-Q3 | reviewer someone
```

Unchanged. The old sentence was true only through `main()`; the new one does not touch it.

**Outputs produced**
- `plugin/taskmd/defaults/config.md` — the sentence the adoption argument rests on, in the file
  every adopter copies
- `plugin/docs/bindings/local-markdown.md` — *read*, corrected: `context` is a summary and is not
  that operation
- `plugin/taskmd/schema.py` — `Task.extra`'s docstring records that it has no reader and why

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The config states what the four commands actually do with an unnamed field, checked by running them | met | §3 step 1 for the old claim, step 2 for the new one. Both run, neither read off the source |
| The route that *does* display it is named, so the sentence tells an adopter what to do | met | `context_fields` / `index_columns`, named in the sentence itself and shown working on a project that had never named them |
| The claim survives T-030's removal of the schema entry point | met | §3 step 6 — simulated by stubbing `main()` to refuse. The new claim never depended on it, which is the difference from the old one |
| `BINDING.md` §1 *read* and the local binding's *read* are re-checked, and either still hold or are recorded as needing change | met | §1 *read* holds — reading is opening the file. The local binding did **not** hold and was corrected rather than only recorded; D2 says why that is inside this task rather than after it |
| Shown on a real case, per `CLAUDE.md` *Verifying*: a task with an unnamed field, before and after | met | One scratch project, carried through all six steps, before and after |

**Child fix tasks raised**
- none. `Task.extra`'s future is recorded in the code where T-030 will meet it, rather than raised as
  a task that would duplicate T-030's own decision.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met. The finding underneath is bigger than the sentence: `context` **is not the read operation**, though the local binding said it was, and that mis-naming is what made "carried and displayed" sound true — a summary reads like a read. `BINDING.md` itself needed nothing, because *read* for this backend is opening the file. The replacement claim was proved before being written into the file every adopter copies: naming two unknown fields in `context_fields` and `index_columns` displays them with no code change, and the claim was then re-run with `schema.main()` stubbed out to confirm it survives T-030, which the old claim did not. `Task.extra` keeps no reader and its docstring says so, rather than a use being invented for it or T-030's commit being taken here. |
| 2026-08-09 | → in_progress | Plan proves the replacement claim before writing it, because the claim is what goes into the copied config and reading `cmd_context` to check it would repeat the mistake being fixed. |
| 2026-08-09 | → specified | Criteria stand as raised; no open question, as recorded. |
| 2026-08-09 | → proposed | Raised as F-5 from the T-059 audit, clause 1. Run before write-up on a scratch project: a task carrying two unnamed fields showed them in none of the four commands. `medium`/`xs` — one sentence, but it is the sentence R-11's adoption argument rests on, it sits in the file every adopter copies, and T-030 turns it from misleading into false. |
