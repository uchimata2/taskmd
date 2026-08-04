---
id: T-001
title: Decide how the front-matter schema is configured
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: []
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-001 — Decide how the front-matter schema is configured

## 1. Specify

**Outcome**
A written decision on whether the schema is declared in a config file, fixed in code with pass-through for unknown fields, or purely conventional — with the reason recorded.

**Why this one**
**This blocks every other task.** `reference/task.py` hardcodes one project's fields (`status`, `phase`, `work_package`, `decisions`); a general plugin cannot. The brief recommends a config file with opinionated defaults, so zero config still works. Choosing late means rewriting whatever was built first.

**Acceptance criteria**
- [ ] One option chosen, with the reason written down
- [ ] A project with no config file still works, using the defaults
- [ ] The default schema is documented in one place the CLI can also read
- [ ] A second, deliberately different schema proven to work

**Open questions**
- Does the config declare *which* fields are edges, or is that fixed? — decide with the schema

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
