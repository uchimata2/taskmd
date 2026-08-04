---
id: T-002
title: Implement the core CLI: context, index, check
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-001]
related: []
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
