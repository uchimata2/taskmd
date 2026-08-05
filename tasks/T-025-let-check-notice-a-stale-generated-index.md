---
id: T-025
title: Let check notice a stale generated index
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-002, T-009, T-019]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-025 — Let check notice a stale generated index

## 1. Specify

**Outcome**
`check` reports a `tasks/README.md` that no longer matches the tasks it was generated from, instead
of exiting 0 beside it. The index stays generated and `check` stays read-only — what changes is that
a project whose index disagrees with its tasks can no longer be reported as consistent.

**Why this one**
Found in [T-009](T-009-define-the-backend-binding-contract.md)'s `implement`, and not by testing for
it: the session updated a task's front-matter, did not regenerate the index, and `check` said the
project was fine.

```
--- file says ---
status: planned
phase: plan
--- index says ---
`specified` | `specify`
--- check says ---
OK - 24 task(s), vocabulary valid, references resolve, no broken links
exit=0
```

This is the same failure shape as [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md):
`check` returning success over a discrepancy it never looked at. It is milder — nothing is lost, and
`index` fixes it — but the file is committed, so a reader of the repository sees the stale version
and has no signal that it is stale.

**It also weakens a stated claim.** `docs/SCOPE.md` R-12 says the index is generated "so drift is
structurally impossible rather than policed". That is true of the *content* — nothing is
hand-maintained — but not of the *timing*: between a write and the next `index`, the generated file
is a stale second copy of facts that live in the task files. `docs/SCOPE.md` §1 *Invisibility* is
the sharper test, and this fails it: staying correct currently depends on someone remembering a
step.

**Requirements served**
R-12, R-16, R-17 (`docs/SCOPE.md`); §1 *Invisibility*.

**Scope**
- In: `check` detecting that the generated block in the index does not match what the tasks would
  produce now.
- Out: `check` rewriting it. That is `index`'s job, and an automatic fixer is `docs/SCOPE.md`
  non-goal 6.
- Out: any fourth command, and any cache or timestamp file. Comparing regenerated output against
  the file on disk needs neither.
- Out: the hand-written prose outside the generated markers, which is nobody's to police.

**Inputs**
`taskmd/cli.py` (`index_block`, `check`), `docs/SCOPE.md` R-12 and §1, T-009 §3 verification,
`docs/bindings/local-markdown.md` *After any write*.

**Acceptance criteria**
- [ ] A project whose index is stale is reported by `check`, naming the file and what to run
- [ ] `check` writes nothing — the working tree is byte-identical after a run that reports staleness
- [ ] A project whose index is current is unaffected, and an index file that does not exist yet is
      not reported as stale by mistake
- [ ] Shown failing on a fixture first, per R-16
- [ ] The exit code distinguishes this from a config error, since a stale index is a project the
      user can fix with one command rather than a project that could not be read

**Open questions**
- Is a stale index an error or a warning? An error is consistent with T-019 (a validator that says
  OK over something it did not check is worse than none); a warning avoids failing a run for a
  condition one command fixes. — maintainer. *Recommendation: an error*, because the only argument
  for a warning is that the fix is cheap, which is equally an argument that it will be run.

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
| 2026-08-05 | → proposed | Raised from T-009's `implement`, where the local-Markdown binding was being proven by following it. The binding's *after any write* step was missed, the index went stale, and `check` reported OK — an unstaged reproduction of the thing the binding's first assumption warns about. Raised rather than fixed in place (METHOD §3.3); T-009's own criteria do not cover the validator. |
