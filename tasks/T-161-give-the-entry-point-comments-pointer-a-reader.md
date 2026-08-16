---
id: T-161
title: Give the entry-point comments' pointer a reader
type: fix
status: proposed
phase: specify
parent: T-142
blocked_by: []
related: [T-064, T-099, T-139, T-160]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-16
updated: 2026-08-16
deliverables: []
---

# T-161 — Give the entry-point comments' pointer a reader

## 1. Specify

**Outcome**
The two entry-point shims' pointer to `SKILL.md` cannot be deleted, moved or left dangling without
something failing.

**Why this one**
Raised from [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md)'s `implement`,
which found the gap while establishing what its own green suite proved. `tests/test_runtime.py` reads
both shims twice and neither reading can see this:

- `test_every_entry_point_produces_what_the_module_produces` **executes** them, so it covers
  behaviour and nothing about the prose;
- `test_no_entry_point_names_a_command_a_flag_or_a_field` strips every comment line first, by an
  explicit decision stated in its own docstring — *a launcher's body is what carries logic; its prose
  is allowed to say anything, and does.*

So T-142 replaced a comment that had been false for weeks with a comment that could go false again
the same way, and the suite would stay green through both.

**This is T-160's shape, one file over.** That task found a printed line whose provenance clause no
test had ever read, and its answer was not to trust the new wording but to add the reader — proved by
failing against the old text. The same argument applies here and the same remedy is available.

**What the pointer is worth guarding.** It is the only thing in either shim that reaches the fallback
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) shipped. If `SKILL.md`
moves inside the skill folder, or the paragraph it names is renamed away, the shims keep saying
*it is stated once, in ../skills/taskmd/SKILL.md* and the stranded adopter follows it to nothing —
which is the failure mode T-142 was raised to remove, restored by a different route.

**Scope**
- In: `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd`, and whether the path each names resolves.
- In: whether the target still contains the fallback, or only that a file is there. A path that
  resolves to a `SKILL.md` with no fallback paragraph in it is the more likely failure.
- In: whether this is written as its own test or falls out of whatever
  [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) settles —
  that task is generalising the guard for marked lists, and a bespoke fifth guard written beside it
  is the duplication it exists to stop. **Read T-139's outcome before writing anything here.**
- Out: the wording of either comment, which T-142 settled and verified.
- Out: the fallback itself, which is T-099's and unchanged.
- Out: guarding prose in general. The claim worth a reader is the **pointer**; the rest of the
  comment is argument, and `test_no_entry_point_names_a_command_a_flag_or_a_field`'s ruling that
  prose may say anything is not reopened here.

**Inputs**
- `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd` — the two pointers.
- `tests/test_runtime.py` — `entry_points`, and the two tests named above.
- [T-160](T-160-retire-the-budget-check-s-unobserved-premise-warning.md) — a citation given a reader,
  and the way it was proved.
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) — the
  general guard, whose answer may supply this one.

**Acceptance criteria**
- [ ] <written at `specify`, after T-139's outcome is known>

**Open questions**
- **Is this its own test, or an instance of T-139's mechanism?** Decide at `specify`, and not before
  T-139 closes. Recorded as a soft link rather than a dependency edge: this task can be specified
  either way and nothing here is blocked, but someone working it without knowing T-139's answer would
  make the worse choice — which is exactly what `related` is for (METHOD §4).

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
| 2026-08-16 | → proposed | Raised from [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md)'s `implement`, which established what its own green suite covered and found the answer was *not this*. Filed rather than fixed there: the standing authorisation of 2026-08-16 covers four named tasks and explicitly not what they raise, and the guard is the class [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) is generalising — so a bespoke test written the day before that ruling is the duplication T-139 exists to stop. `medium` because the pointer is the stranded adopter's only route to the fallback; `xs` because it is one assertion once the mechanism is chosen. |
