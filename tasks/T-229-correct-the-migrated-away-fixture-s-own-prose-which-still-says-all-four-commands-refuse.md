---
id: T-229
title: Correct the migrated-away fixture's own prose, which still says all four commands refuse
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-221, T-185, T-164, T-177]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-22
updated: 2026-08-22
adopter_visible: no
deliverables:
  - tests/fixtures/migrated-away/.taskmd/config.md
---

# T-229 — Correct the migrated-away fixture's own prose, which still says all four commands refuse

## 1. Specify

**Outcome**
`tests/fixtures/migrated-away/.taskmd/config.md` no longer tells a reader that all four commands
refuse on this fixture, because `check` does not, and this fixture is the project it is measured
against.

**Why this one**
The file says *"Refusing is right — all four read a folder, and there is no folder"*, written
2026-08-17 by [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md). On
2026-08-19 [T-185](T-185-run-the-document-checks-in-a-project-whose-tasks-moved.md) split `check` so
the checks that read documents run on exactly this shape, and the sentence was not revisited.
Measured 2026-08-22:

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md
1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), ...
exit 1
```

This is the same defect class as
[T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) in a second
document — a sentence about behaviour written once and never re-run — and it sits in the one file a
contributor opens to learn what the fixture is for.

**Scope**
- In: the two sentences under *The point of the fixture*, corrected against a run
- In: whether any other sentence in that file describes behaviour the 2026-08-19 split changed
- Out: the fixture's data. The config keys and the two documents are what they should be, and T-185
  proved it
- Out: the other fixtures' prose. If this class is wider than one file it is a sweep, and a sweep is
  its own task rather than a quiet widening of this one

**Inputs**
- `tests/fixtures/migrated-away/.taskmd/config.md` — the sentences, and the date they carry
- [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) §3 — the run
  that falsifies them, and the same defect corrected in the binding document

**Acceptance criteria**
- [ ] The corrected sentences are backed by a quoted command and its exit code, dated
- [ ] The fixture's stated purpose still distinguishes it from `broken-tasks-dir`, which is the
      distinction the file exists to hold
- [ ] Whether the 2026-08-17 date stays visible is decided and stated, not dropped by default

**Open questions**
- **None.** The direction of the correction is fixed by the run above.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run `check` on **both** fixtures — this one and `broken-tasks-dir` — and capture both outputs with their exit codes. The pair is the evidence, because the sentence being corrected is about the difference between them | the two runs, dated |
| 2 | Correct the opening sentence against that pair, keeping the 2026-08-17 date visible | the corrected paragraph |
| 3 | Read the rest of the file for any other sentence the 2026-08-19 split falsified | what was found |
| 4 | Re-run `check` on the fixture and the suite: the fixture's **data** must be untouched, and its reported counts unchanged | the before and after counts |

**Step 1 runs both fixtures, not this one.** The sentence under repair is a comparison, and a run of
one side cannot check a comparison. It also turns out to strengthen the paragraph rather than only
correct it: since 2026-08-19 the two fixtures differ in **behaviour**, not just in wording.

**Step 4 is not ceremony.** This file is both prose and configuration. An edit to the prose that
moved a heading or a table would change what `check` reads here, and the fixture's whole value is
that its output is stable and asserted elsewhere.

## 3. Implement

### Step 1 — the pair

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/migrated-away
BROKEN LINK   docs/guide.md -> plan.md
1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), ...
Scope  no task file was read, and the checks that open one did not run. ... Or nothing here is
       broken and these commands do not apply: id_width is 'none', ...
exit 1

$ ./plugin/bin/taskmd check --root tests/fixtures/broken-tasks-dir
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'taks', but the project root has no such folder.
              Create it, or correct tasks_dir.
exit 2
```

Run 2026-08-22. The genuine version still refuses outright, with the two old remedies and nothing
examined; the migrated one runs its document checks and says which half it did not reach.

### Steps 2 and 3 — what changed, and what did not

The opening clause *"Refusing is right — all four read a folder, and there is no folder"* is quoted
in place with its 2026-08-17 date and replaced by **three refuse and `check` does not**, with the run
above beneath it. **Nothing else in the file describes behaviour**: the remaining paragraphs are about
the message's wording and about the contrast with `broken-tasks-dir`, and the contrast is now true
twice over rather than false.

### Step 4 — the fixture's data is untouched

`check` on the fixture reports the same `1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), 0
template(s), 0 template field value(s), 1 vocabulary row(s), 0 section reference(s)` before and
after, and the suite is green. The prose grew and the counted units did not, which is what tells you
the edit stayed on the prose side of a file that is both.

**Decisions & assumptions**
- **The old sentence is quoted rather than deleted, and its date kept** — 2026-08-22. §1's third
  criterion asked for this to be decided rather than defaulted. Kept, for the reason
  [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) established
  hours earlier in the shipped document: the interesting fact is not what the file says now but that
  the tool moved on a known date and the file did not, and deleting the date hides it.
- **The comparison with `broken-tasks-dir` is strengthened rather than left alone** — 2026-08-22. It
  was written when the two differed only in wording. They now differ in exit code and in what runs,
  which is a better guarantee that a future change cannot collapse the two fixtures into one.
- **`context` is shown with an id** — 2026-08-22. Run bare it exits 2 on a usage error, which is the
  same code for a different reason; a fixture document that a contributor copies from should not
  teach the ambiguity.

**Outputs produced**
- `tests/fixtures/migrated-away/.taskmd/config.md` — the corrected paragraph, the run beneath it, and
  the strengthened contrast with `broken-tasks-dir`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The corrected sentences are backed by a quoted command and its exit code, dated | met | Both fixtures, both exit codes, 2026-08-22, in the file itself and not only in this record |
| The fixture's stated purpose still distinguishes it from `broken-tasks-dir` | met | And distinguishes it better than before: the two differ in behaviour now, not only in the wording of one message, and the file says so with the run |
| Whether the 2026-08-17 date stays visible is decided and stated, not dropped by default | met | Kept, and the old sentence quoted in place. Decided rather than defaulted, with the reason recorded above |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | proposed → done | `specify` through `review` in one session. **Authorisation:** the **project owner**, on **2026-08-22**, extended the same day's four-task full-lifecycle grant to cover a task **raised during** that work. Six were raised; this is one of the two with no open question of the owner's, and the other four stop where they stand because they have one. **The extension authorises phases, not answers**, exactly as the grant it extends. **Both fixtures were run, not this one**, because the sentence under repair is a comparison and one side cannot check a comparison — and running both turned the repair into a strengthening: since 2026-08-19 `migrated-away` and `broken-tasks-dir` differ in **exit code and in what runs**, where the paragraph was written when they differed only in the wording of one message. **The 2026-08-17 date is kept and the old sentence quoted in place**, which §1's third criterion required be decided rather than defaulted; the reason is [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s, hours earlier in the shipped document — the fact worth having is that the tool moved on a known date and the file did not. **The fixture's data is untouched**, shown by `check` reporting the same counted units before and after: this file is prose and configuration at once, and its value is that its output is stable. |
| 2026-08-22 | (no change) | **Renumbered from T-223 on the day it was raised**, before it was pushed. A concurrent branch had already taken that id and merged it as pull request #2, so two files claimed `T-223` the moment the two lines met. The one that had been published keeps the id and this one moves — the ordering rule is which was reachable by anybody else, not which was written first. `check` reports the state as `DUPLICATE ID`, which is what would have caught it had the merge been pushed unread. Recorded because a record whose id changed is a record whose old id may still be written somewhere: [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) carried two references and both were rewritten in the same commit. |
| 2026-08-22 | → proposed | Raised from [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md)'s step-4 sweep, which was reading the binding document and found the same defect in the fixture that document's evidence is measured against. **Raised rather than absorbed**: T-221 declares one deliverable and this is a second, so folding it in would have made that record false about what it changed. `medium` rather than `high` because it misleads a contributor rather than an adopter — no clone of the plugin receives `tests/`. **The sweep bound is deliberate**: this file was found by opening it, not by a sweep of the fixture tree, and a second instance would make the sweep the task instead of the fix. |
