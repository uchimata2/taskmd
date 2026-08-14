---
id: T-139
title: Check that the advisory lines the README lists are the advisory lines there are
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-100, T-121, T-134, T-138]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-12
updated: 2026-08-12
deliverables: []
---

# T-139 — Check that the advisory lines the README lists are the advisory lines there are

## 1. Specify

**Outcome**
A prose list of `check`'s advisory lines cannot name a set different from the one the code emits.
Adding a third advisory fails the suite until the document that enumerates them is updated, the same
way [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) made a
prose list of the commands fail.

**Why this one**
[`../README.md`](../README.md) devotes a paragraph each to `CONFIG DRIFT` and `DUPLICATE INDEX`.
[T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) added `LABEL SHAPE` and did not
add the paragraph — its scope named the task template and the shipped default, which are where an
*adopter* meets the wording, and missed the document a *stranger* reads before installing. It was
caught by the handoff reconcile sweep on 2026-08-12, by a person's grep rather than by anything in
the suite, which is the same way the command lists were caught before T-134 guarded them.

**This is T-134's class, one set over.** That task guarded the command lists and stopped there,
correctly — it was scoped to commands. Nothing generalised the guard, so the next enumerated set to
drift was the next one nobody was watching. The question worth settling here is whether the guard is
written a third time for advisories or written once for *any* marked list of a set the code owns.

**Scope**
- In: the advisory lines `check` can print, and every tracked document that enumerates them.
- In: whether the existing marker mechanism T-134 built is reused, extended, or copied.
- Out: what any advisory says or when it fires. Those belong to the tasks that added them.
- Out: the `Scope` and problem-class lines, unless the answer generalises to them for free — which is
  worth asking, since they are enumerated in prose too.

**Inputs**
- [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  marker mechanism and the reason a list is guarded rather than a sentence.
- `tests/test_publishing.py` — where the command-list assertions live.
- [`../README.md`](../README.md) — the three paragraphs as they now stand.

**Acceptance criteria**
- [ ] <written at specify>

**Open questions**
- <specify has not run>

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | → proposed | Raised by the handoff reconcile sweep after [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) shipped a third advisory line and left `README.md` naming two. **The missing paragraph was written during the sweep and this task is the guard, not the paragraph** — fixing the instance silently would have left the class exactly as unguarded as T-138 found it. Not folded back into T-138: that task is closed and its scope was honest about where it looked, so the gap is in what nobody had generalised rather than in what it did. |
