---
id: T-002
title: Implement the core CLI: context, index, check
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-001]
related: [T-008]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-002 — Implement the core CLI: context, index, check

## 1. Specify

**Outcome**
A dependency-free CLI providing `context`, `index` and `check`, driven by the schema decision from T-001.

**Why this one**
These three carry the plugin's whole thesis: `context` is the token saving, `index` is the derived view that removes drift, `check` validates what is left hand-made. `reference/task.py` proves the behaviour — it is evidence, not code to lift.

**Requirements served**
R-12, R-15, R-16, R-17, R-20 (`docs/SCOPE.md`).

**Acceptance criteria**
- [ ] Runs on a clone with no configuration and no dependencies
- [ ] `index` regenerates without touching hand-written regions
- [ ] `check` proven **failing** on every class of problem it claims to catch
- [ ] Output byte-identical across Windows, macOS and Linux (`newline` set explicitly)
- [ ] Console output survives a cp1252 terminal
- [ ] **Configuration problems are reported when the config is read, not mid-command** (R-17) — a
      bad key, a missing file or an unresolvable reference fails at setup, never inside a task the
      user is trying to finish
- [ ] Reads the schema through `taskmd/schema.py`, holding no field name or status value of its own
- [ ] **`context`'s `NEXT:` hint reads phase *and* status** (R-3) — proven on a task whose status has
      moved past its phase, where the current tool tells you to redo the phase you just finished

**Open questions**
- Are `decisions` and `deliverables` core commands or config-declared derived views? — see brief

**Not in this task**
Interpreter and repository-root discovery, and project hook commands, are T-011.

**What this replaces**
`tools/tasks/task.py` is the interim self-hosting copy, kept so the project could use its own
method from the first session. It predates `taskmd/schema.py` and carries its own hardcoded schema,
so it **does not** implement symmetric soft links (T-012) — its `context` shows only the `related`
values a task literally stores, missing the ones derived from the other end. That is a known
limitation of the interim tool, not a defect to chase; this task removes it by building on
`taskmd/schema.py`. Delete `tools/tasks/task.py` when this lands, or it becomes a second
implementation with its own idea of the schema.

**Second known limitation — the `NEXT:` hint collapses phase and status.** The interim tool derives
its closing hint from `phase` alone:

```
NEXT: read the file above, then work the '%s' phase." % t.phase
```

`docs/METHOD.md` §2 makes phase and status independent — phase says where the work got to, status
says whether it can move. So a task that has *finished* a phase and is waiting for the next one to
be requested (status `review`, phase `implement`) is told to work the phase it just completed.
Observed 2026-08-04 on T-008 at exactly that state. The hint should read both, and say what the task
is waiting for rather than naming its phase back at the reader — which is the only part of `context`
that gives an instruction rather than a fact, so getting it wrong actively misleads.

Note the interaction with R-6: a hint that names the next phase is the kind of "next step pointer"
the method explicitly says is context, not authorization. Whatever it prints should not read as
permission to proceed.

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
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
| 2026-08-04 | (no change) | Second interim-tool limitation recorded: the `NEXT:` hint derives from `phase` alone and contradicts R-3. Found while working T-008, which also gave the CLI its new footer target. `related` gained T-008. |
