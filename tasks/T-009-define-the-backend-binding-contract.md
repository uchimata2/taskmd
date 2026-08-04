---
id: T-009
title: Define the backend binding contract and write the local-Markdown binding
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-008]
related: [T-005, T-010]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-009 — Define the backend binding contract and write the local-Markdown binding

## 1. Specify

**Outcome**
A named set of operations every backend must provide, plus the first implementation of it — local
Markdown files — written as a binding document rather than assumed by the method.

**Requirements served**
R-13, R-14 (`docs/SCOPE.md`).

**Why this one**
Without a contract, "backend-neutral" is an aspiration. Handoff proves the shape works: five
operations (`find` / `read` / `create` / `update` / `reference`) let one core drive Notion or a
folder of files unchanged. taskmd needs its own contract because it does more than handoff does —
it derives edges and generates an index, and neither is expressible in those five.

**Scope**
- In: the operation set; what each must guarantee; how derived views are expressed for a backend
  that has no files; the local-Markdown binding; the mandatory "assumptions this binding makes"
  section.
- Out: GitHub (T-010). The method itself (T-008).

**Inputs**
- `docs/SCOPE.md` §3B
- Handoff `bindings/README.md` + `handoff.core.md` §8 — the contract shape that works
- Handoff `control/IMPROVEMENT-BRIEF.md` **F1** — a binding stated "the folder is the index" as a
  premise; an adopting project with a generated index could follow it exactly and still break its
  own single source of truth. The failure was silent and looked like compliance.

**Acceptance criteria**
- [ ] Every operation the method needs is named, with what it must guarantee — and nothing the
      method does not need
- [ ] Each binding carries an **"assumptions this binding makes"** section an adopter can check in
      thirty seconds (the F1 fix)
- [ ] The contract expresses derived views without assuming a filesystem, proven by writing one
      operation against a backend that has no files
- [ ] The local-Markdown binding is proven by the existing tooling running unchanged against it
- [ ] Nothing in the contract names a field, a status value or a file format — those come from the
      schema config (T-001)

**Open questions**
- Does taskmd's contract extend handoff's five operations or replace them? Sharing the vocabulary
  helps T-005; diverging may be unavoidable given derivation and index generation. — decide here,
  T-005 depends on the answer.

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
| 2026-08-04 | → proposed | Raised by T-007 to carry R-13/R-14. |
