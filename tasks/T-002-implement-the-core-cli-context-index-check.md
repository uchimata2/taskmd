---
id: T-002
title: Implement the core CLI: context, index, check
type: deliverable
status: specified
phase: specify
parent: null
blocked_by: [T-001]
related: [T-008, T-004]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-05
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

**Inputs**
`taskmd/schema.py` and `taskmd/defaults/config.md` (the schema, settled in T-001);
`docs/METHOD.md` §2 and §4 (phase/status independence, the three edge kinds);
`reference/task.py` and `tools/tasks/task.py` as evidence of behaviour that already works.

**Acceptance criteria**
- [ ] Runs on a clone with no configuration and no dependencies
- [ ] `index` regenerates without touching hand-written regions
- [ ] `check` proven **failing** on every class in *What `check` claims to catch*, below
- [ ] Output byte-identical across Windows, macOS and Linux (`newline` set explicitly)
- [ ] Console output survives a cp1252 terminal
- [ ] **Configuration problems are reported when the config is read, not mid-command** (R-17) — a
      bad key, a missing file or an unresolvable reference fails at setup, never inside a task the
      user is trying to finish
- [ ] Reads the schema through `taskmd/schema.py`, holding no field name or status value of its own
- [ ] **The id format comes from config** (`id_prefix`, `id_width`) and is never hardcoded, so the
      defaults and the scale ceiling remain T-004's to settle without reopening this task
- [ ] **`context`'s `NEXT:` hint reads phase *and* status** (R-3) — proven on a task whose status has
      moved past its phase, where the current tool tells you to redo the phase you just finished
- [ ] **The `context` saving is measured on a real case** and the before/after byte counts recorded
      in `## 3. Implement` (R-15). Stating the number in the README is T-006's.

**What `check` claims to catch**

Enumerated here so the criterion above is falsifiable before implementation starts: an
implementation cannot quietly shrink the claim to whatever proved easy. Each must be demonstrated
failing on a fixture that contains it.

| # | Class | The case that must fail |
| :-- | :--- | :--- |
| 1 | Bad enumerated value | A field carries a value outside its vocabulary row |
| 2 | Dangling reference | An edge points at an id that does not exist |
| 3 | Missing blocker | A task is `blocked` with an empty dependency list |
| 4 | Dependency cycle | A depends on B depends on A |
| 5 | Broken link | A Markdown link resolves to no file, including inside dot-directories |
| 6 | Stale stored-derived field | A task stores a field the tool derives (e.g. `children`) |
| 7 | Missing deliverable | A task declares a deliverable path that no longer exists |
| 8 | Config error at setup | An unknown key, a missing file, an unresolvable reference (R-17) |

Class 5's dot-directory case is not hypothetical: `glob`'s `**` skips them, which hid the live
handoff pointer — the one file where a broken link costs most.

**Consequence of class 7, carried into implementation.** `check` must not learn the field name
`deliverables`, which the criteria above forbid. So the schema needs a key naming which field holds
deliverable paths — the field is currently carried and displayed but not interpreted
(`taskmd/defaults/config.md`). That is one added config key, within T-001's settled design rather
than a change to it; it is recorded here so it is not discovered mid-implementation.

**Not in this task**
- Interpreter and repository-root discovery, and project hook commands — **T-011**.
- The default id prefix and width, merge-conflict behaviour, and the measured scale ceiling —
  **T-004**. This task consumes whatever config says.
- Stating the measured saving in the README — **T-006**.
- `decisions` and `deliverables` as commands — **not built**; see *Resolved*, below.

**Resolved**
- ~~Are `decisions` and `deliverables` core commands or config-declared derived views?~~ —
  **neither.** `docs/SCOPE.md` non-goal 11 (decided later, in T-007) keeps the surface at three
  commands. The one behaviour worth keeping from them — `deliverables` caught a declared file that
  had been deleted (`docs/BRIEF.md`) — becomes class 7 above rather than being dropped.

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
| 2026-08-05 | → specified | Specify agreed by the owner. The open question is closed by `docs/SCOPE.md` non-goal 11 — three commands, and the deliverable-existence behaviour survives as a `check` class rather than being dropped. `check`'s eight failure classes enumerated so R-16's criterion is falsifiable before implementation. R-15 gained a criterion (measure here, state in README in T-006). Id format pinned to config, which makes T-004 independent rather than a prerequisite; `related` gained T-004. |
