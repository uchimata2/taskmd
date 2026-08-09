---
id: T-025
title: Let check notice a stale generated index
type: fix
status: planned
phase: plan
parent: null
blocked_by: []
related: [T-002, T-009, T-011, T-019]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-05
updated: 2026-08-07
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
- None. **Answered by the maintainer on 2026-08-07: an error.** Consistent with T-019 — a validator
  that reports OK over something it did not check is worse than none — and the generated index is
  the one written derived artifact, so a stale one is exactly the drift this plugin exists to
  remove. *Rejected: a warning.* Its only argument is that the fix is cheap, which is equally an
  argument that the fix will be run.

**Long-term mitigations, recorded 2026-08-07 at the maintainer's request**

Written here rather than left in a conversation. **Corrected 2026-08-07 after T-011 was built**: the
first of these was recorded as a way the condition stops arising, and it is not one. The error is
therefore the mechanism, not a backstop — confirmed by the maintainer on 2026-08-07, who kept it.

1. ~~**The after-write hook removes the condition instead of reporting it.**~~ **It cannot, and the
   original wording said otherwise.** T-011 was answered with a single invocation point — after a
   write — and what it built runs a project's command after **taskmd's own** write, which is `index`
   regenerating the file. The claim was that this leaves the error "for edits made outside the hook
   — by hand, by another tool, or arriving in a merge". But taskmd never writes a task file, so
   *every* task-file edit is outside the hook and the carve-out is the whole set. The hook is still
   worth declaring — `after_write: python -m taskmd check` collapses the binding's *After any write*
   step from two commands to one — it simply cannot make a stale index unreachable. What would is a
   **harness** hook running `index` after an edit, which is the adopting project's to configure and
   was explicitly outside T-011's scope. The soft edge stands; neither task blocks the other.
2. **Compare by regenerating, never by storing a fingerprint.** The check renders the index in
   memory and compares it with the file. A stored hash or timestamp would be a written derived
   value, which the design rule forbids, and a field somebody has to keep true, which §1
   *Invisibility* forbids. That is a constraint on the fix, not a preference.
3. **One renderer, used by both commands.** `check` must not carry its own idea of what the index
   looks like. Two independent renderers eventually disagree, and the failure mode is a validator
   reporting staleness on a file that is current — which trains people to ignore it.

*Rejected: drop the file and derive the index on read.* It would make the whole class impossible,
and it costs R-12 and the artifact people browse in the repository without cloning it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build `broken-stale-index` — otherwise-valid tasks plus a `tasks/README.md` whose generated region disagrees with them in one field, every link inside it resolving — and run `check` on it **before** touching the code. | The fixture, and the `OK` at exit 0 recorded in §3 |
| 2 | Compare by rendering: `check` calls the existing `index_block` and matches its output byte-for-byte against what sits between the markers on disk. | `check_stale_index` in `plugin/skills/taskmd/taskmd/cli.py`, called from `cmd_check` |
| 3 | Re-run the fixture, then this repository twice — once with a task edited and the index left alone, once regenerated. | The failing output and both host runs, in §3 |
| 4 | Digest the fixture tree either side of a run that reports staleness. | The two digests, in §3 |
| 5 | Add the class to the suite: `STALE INDEX` in `LABELS`, a test asserting its own class and nothing else, and the fixture's row in the fixtures table. | `tests/test_cli.py`, `tests/fixtures/README.md` |
| 6 | Reconcile the documents that currently say `check` does not notice this, found by grep rather than from memory. | `CLAUDE.md`, `plugin/skills/taskmd/docs/bindings/local-markdown.md`, and whatever else the grep returns |

**Step 1 is first because its evidence expires.** `check` printing `OK` over a stale index *is* the
defect, and once step 2 lands that run can never be produced again — a fixture added afterwards is
only ever seen passing, which proves the assertion runs and not that it was ever false.

**Two decisions taken here, because both change what an adopter sees.**

*Nothing generated is not stale.* Where `tasks_dir/README.md` is absent, or present without the
markers, `check` says nothing. Otherwise a fresh project is reported on its first run, before
`index` has ever been asked for, and a project keeping a hand-written index deliberately is reported
forever. It also follows §1's out-list: the prose outside the markers is nobody's to police, and a
file with no markers is entirely prose. *Rejected: make "would `index` change this file?" the test.*
It is the simpler predicate and it is exactly what `cmd_index` already computes, but it turns "you
have not generated one yet" into a problem.

*It is an ordinary `check` problem at exit 1, not a code of its own.* Criterion 5 asks the exit code
to separate this from a config error, and 1 against 2 already does: a config error is a project that
could not be read, and everything `check` reports is a project the user can fix. *Rejected: a third
exit code for staleness.* Nothing would consume it, and minting one for the newest class implies the
nine older ones each deserve theirs.

**Outputs this task will produce**

- `tests/fixtures/broken-stale-index/` — a `tasks/` directory and a deliberately stale `tasks/README.md`
- `plugin/skills/taskmd/taskmd/cli.py`
- `tests/test_cli.py`
- `tests/fixtures/README.md`

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
| 2026-08-09 | → planned | Six steps, and the fixture is step 1 rather than step 5: `check` printing OK over a stale index is the defect itself, so that run is unobtainable the moment the comparison lands, and a fixture written afterwards can only ever be watched passing. §1's mitigations 2 and 3 are met by construction — the comparison renders through the existing `index_block` and stores nothing. Two behaviours decided at plan time and recorded with their rejections in §2: a file with no generated markers is not stale, so a fresh project is not reported before `index` has ever been run; and staleness is an ordinary problem at exit 1 rather than a code of its own, which is what criterion 5 asks for since a config error is already 2. |
| 2026-08-07 | (no status change) | Mitigation 1 corrected after T-011 was built and showed it false: the hook runs after taskmd's *own* write, and taskmd never writes a task file, so it cannot catch the edit that makes an index stale. The maintainer confirmed the error stands, which makes it the mechanism rather than the backstop the mitigation described — so this task's value went up, not down. The mitigation is struck through rather than deleted: it was recorded at the maintainer's request, and an argument that turned out to be wrong is worth more on the record than absent, since the next reader will otherwise propose it again. |
| 2026-08-07 | → specified | Answered: an error, not a warning. The maintainer also asked for long-term mitigations to be recorded rather than offered and forgotten, so three are written into §1 with one rejected. The first is the substantive one and it arrived from T-011 being answered the same day: a single after-write hook point makes a stale index unreachable in ordinary use, which turns this task's error into the backstop for edits made outside it. Soft edge to T-011 added. The other two are constraints on the fix rather than alternatives to it — no stored fingerprint, and one renderer shared by both commands. |
| 2026-08-05 | → proposed | Raised from T-009's `implement`, where the local-Markdown binding was being proven by following it. The binding's *after any write* step was missed, the index went stale, and `check` reported OK — an unstaged reproduction of the thing the binding's first assumption warns about. Raised rather than fixed in place (METHOD §3.3); T-009's own criteria do not cover the validator. |
