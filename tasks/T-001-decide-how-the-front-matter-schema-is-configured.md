---
id: T-001
title: Decide how the front-matter schema is configured
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: []
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - plugin/skills/taskmd/taskmd/defaults/config.md
  - plugin/skills/taskmd/taskmd/schema.py
  - tests/test_schema.py
  - tests/fixtures/alt-project/.taskmd/config.md
---

# T-001 — Decide how the front-matter schema is configured

## 1. Specify

**Outcome**
A written decision on whether the schema is declared in a config file, fixed in code with pass-through for unknown fields, or purely conventional — with the reason recorded.

**Requirements served**
R-1, R-2, R-11, R-17 (`docs/SCOPE.md`). Added after the fact: this task closed before the scope
document existed, and `SCOPE.md` §8 requires every implementing task to cite what it serves.

**Why this one**
**This blocks every other task.** `reference/task.py` hardcodes one project's fields (`status`, `phase`, `work_package`, `decisions`); a general plugin cannot. The brief recommends a config file with opinionated defaults, so zero config still works. Choosing late means rewriting whatever was built first.

**Acceptance criteria**
- [ ] One option chosen, with the reason written down
- [ ] A project with no config file still works, using the defaults
- [ ] The default schema is documented in one place the CLI can also read
- [ ] A second, deliberately different schema proven to work

**Open questions**
- ~~Does the config declare *which* fields are edges, or is that fixed?~~ — **answered**: the config
  declares the edge *field names*; the set of edge *kinds* is fixed at three. See §3.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Choose the option and the config format; record both with reasons | §3 of this file |
| 2 | Write the shipped default schema, annotated so it is its own documentation | `taskmd/defaults/config.md` |
| 3 | Implement resolution: project config if present, else the shipped default; validate and fail loudly | `taskmd/schema.py` |
| 4 | Read task front-matter through the resolved schema; derive the inverse edges | `taskmd/schema.py` |
| 5 | Write a second, deliberately different schema — every configurable dimension changed | `tests/fixtures/alt-project/` |
| 6 | Prove it by running: both schemas, plus each validation shown **failing** | `tests/test_schema.py` |

## 3. Implement

**The decision**

Option **(1) a config file**, with the defaults of (3) and the pass-through of (2). The brief
framed the three as alternatives; they are not. Pass-through is not a rival to a config file, it
is the fallback *inside* one — and it is what lets a project adopt taskmd without first rewriting
its task files.

**Decisions & assumptions**

- **D1 — Schema is configuration, with an opinionated default and pass-through for the rest.**
  Zero config gives the default schema; a config adapts it; any front-matter field the schema does
  not name is carried and displayed but never interpreted. — 2026-08-04
- **D2 — The config is Markdown: front-matter for scalars and lists, tables for anything with more
  than one column.** taskmd must already parse both shapes to read task files, so the config costs
  no new parser and no dependency; a config shaped like the thing it configures is one format to
  learn, not two; and comments let the shipped default double as its own documentation.
  *Rejected:* TOML — `tomllib` is stdlib but only from Python 3.11, a version floor bought for
  nothing, plus a second file format. JSON — no comments, so the default could not document
  itself and would force a separate prose copy, which is the exact drift this plugin removes.
  — 2026-08-04
- **D3 — The default schema is a file the CLI reads, not values in code.**
  [`taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) is loaded at run time;
  [`taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py) holds no default values to disagree with it. This is
  acceptance criterion 3, met by construction rather than by discipline. — 2026-08-04
- **D4 — A project config *replaces* the default; it is not merged with it.** So the config you
  are reading is your whole schema. Merged defaults would put the effective schema in two files
  and need a command to ask what it actually is. Cost: a project copies ~15 keys once. A missing
  key is an error naming the key, never a silent fallback. — 2026-08-04
- **D5 — The set of edge *kinds* is fixed at three (`hierarchy`, `dependency`, `soft`); the edge
  *field names* are configuration.** This answers the specify-phase open question. Each kind is a
  distinct traversal in the derivation code, so a fourth kind is new code, not new config. What
  genuinely differs between projects is naming — `blocked_by` vs `depends_on` — and that is
  declared. — 2026-08-04
- **D6 — Unknown *config* keys are an error; unknown *task* fields are pass-through.**
  Deliberately opposite. A typo'd config key that was silently ignored hands you a schema you did
  not write; an unrecognised task field is just someone's data. — 2026-08-04
- **D7 — A derived name may not also be a stored field, and no two edges may derive the same
  name.** Enforced by the loader. A computed value overwriting a written one is the drift the
  design rule exists to prevent, so it is rejected at load rather than checked later. — 2026-08-04
- **D5/D7 amended by [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) (2026-08-04).**
  D5 described the `soft` kind as having *no inverse*. That is superseded: a soft edge is
  **symmetric** — derived under its own name, so a link written on one task is visible from the
  other. D7's collision rule is unaffected (a symmetric edge names no separate inverse, so there is
  nothing to collide with) and the config still requires `-` in the `Derives` column.
- **D8 — `id_prefix` and `id_width` are config keys.** This settles T-004's open question
  ("configurable prefix and width, or fixed?") as *configurable*; T-004 still owns the default
  values and the measured scale ceiling. — 2026-08-04
- **Assumption — package layout.** The plugin source sits in `taskmd/` at the repository root,
  separate from `tools/tasks/task.py` (the self-hosting copy, which is not the deliverable).
  T-006 may move it when it settles the published package layout; nothing above depends on the
  location.
- **Scope boundary.** T-001 delivers the schema, its loader and the derivation of inverse edges.
  The `context`, `index` and `check` commands are T-002 and build on this.

**Outputs produced**
- [`taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — the default schema, and the only
  documentation of what a config may contain
- [`taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py) — resolution, validation, task reading, edge derivation
- [`tests/fixtures/alt-project/`](../tests/fixtures/alt-project) — the second, deliberately
  different schema and three task files written to it
- [`tests/test_schema.py`](../tests/test_schema.py) — 25 tests; 15 of them are rejections

## 4. Review

Verified by running, on the real case — not by reading the code (`CLAUDE.md`).

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One option chosen, with the reason written down | pass | D1–D8 above, each with its rationale and what was rejected. |
| A project with no config file still works, using the defaults | pass | `python -m taskmd.schema .` resolves to the shipped default and loads this repository's own 6 tasks; `test_no_config_file_falls_back_to_the_shipped_default` proves it on a directory with no `.taskmd/` at all. |
| The default schema is documented in one place the CLI can also read | pass | `taskmd/defaults/config.md` is the only copy — `schema.py` carries no default values (D3). `test_the_shipped_default_passes_its_own_validator` runs the shipped file through the same validator a user's config gets. |
| A second, deliberately different schema proven to work | pass | `python -m taskmd.schema tests/fixtures/alt-project` resolves `ISSUE-` ids at width 4 out of `issues/`, with `epic → stories` and `depends_on → unblocks` computed under the new names. Every configurable dimension differs from the default. |

**Proof that the validator fails when it should**

A clean pass proves nothing on its own, so each rule the loader claims to enforce has a test that
makes it fire: unknown key, missing key, non-numeric and zero `id_width`, a list key given a
scalar, an unimplemented edge kind, a soft edge claiming an inverse, a dependency edge deriving
nothing, a derived name colliding with a stored field, two edges deriving one name, an open status
outside its vocabulary, a `status_field` no vocabulary declares, a mis-shaped table header, a short
table row, and a config with no front-matter.

```
python tests/test_schema.py
Ran 25 tests in 0.036s
OK
```

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
| 2026-08-04 | → in_progress | Specify closed: option (1) confirmed, config format chosen with the maintainer, edge-kind question answered (D5). |
| 2026-08-04 | → done | Both schemas proven by running; 25 tests pass, 15 of them rejections. Unblocks T-002 and T-004. |
