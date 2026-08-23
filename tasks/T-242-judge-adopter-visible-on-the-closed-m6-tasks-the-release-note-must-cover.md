---
id: T-242
title: Judge adopter_visible on the closed M6 tasks the release note must cover
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-231, T-182, T-135]
work_package: M6
owner: the project owner
business_value: critical
effort: m
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-242 — Judge adopter_visible on the closed M6 tasks the release note must cover

## 1. Specify

**Outcome**
Every closed task in M6 carries an `adopter_visible` value, so that
[`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7's three counts sum and the release note for `0.6.0`
can be written to the rule. Today they do not sum, and §7 says an unmarked task **blocks the note**.

**Why this one**
Measured on 2026-08-23, running §7's own commands before writing the note:

```text
$ taskmd list --work_package M6 --closed                        | wc -l   → 108
$ taskmd list --work_package M6 --closed --adopter_visible yes  | wc -l   →  11
$ taskmd list --work_package M6 --closed --adopter_visible no   | wc -l   →  19
```

11 + 19 = 30 against 108. **78 closed tasks carry no value at all**, and §7 is explicit that absent
does not pass as `no`: *"Absent means nobody judged it, which is a different fact from judged and not
visible."* The sum is the whole mechanism — a filter cannot report what it failed to see — so the
release note cannot be written until this closes.

**This is the rule catching something, not the rule being wrong.**
[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) exists to record
whether §7 surfaces anything the writer had not already listed. It did, on its first real use, and
what it surfaced is larger than the note: the field's own design says *judgement happens once, on the
task, at the time the work is understood — not months later while writing prose about a release*, and
for 78 tasks that did not happen. So this record is also the evidence that the practice, not only the
backlog, needs a fix.

**Scope**
- In: a value for `adopter_visible` on each of the 78 closed M6 tasks that lack one
- In: the **derivation** used to reach each value, written down, so a wrong mark is findable rather
  than a guess nobody can re-check
- Out: writing the release note. That is
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)
- Out: changing §7 or the field. If either is wrong, that is a finding here and a separate task
- Out: **stopping the field going unmarked again.** The 78 exist because nothing asks for the value
  at the moment §7 wants it judged; that is a second task and is not solved by clearing the backlog

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 — the rule, its test, and why an absent value blocks
- [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) — the task that
  derived the rule and added the field
- The 30 tasks already judged (T-183 to T-220), which are the only calibration for what this
  project has meant by the value

**The derivation this session proposes, and why it is sound in one direction only**

§7's test is *would someone who installed the plugin see different output, receive a different file,
or have to act differently?* Since T-053 an install copies exactly the `plugin/` subtree, so:

- a task whose work touched **no** file under `plugin/` cannot have changed anything an adopter
  receives. `no` is then **provable**, not judged;
- a task that did touch one **may** be visible. `yes` is then the safe mark, because §7 permits a
  required task to be *consciously waived with the waiver named*, and over-inclusion costs a line in
  the note where under-inclusion costs a permanent omission from a record
  [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) forbids
  rewriting.

Evidence for each task is the **union of two sources**, because each misses cases the other catches:
the files its commits touched (`git log --all --name-only --grep=<id>`), and its own declared
`deliverables`. T-222 is why the union is needed: it declares
`plugin/skills/taskmd/docs/BINDING.md` and its commits name no plugin file, so the git source alone
would have marked it `no` and dropped a shipped change from the note.

Applying it gives **60 `yes` and 18 `no`**. That is a proposal, not a result: it was not applied,
because the marks feed a public record this project does not rewrite.

**Acceptance criteria**
- [ ] Every closed M6 task carries an `adopter_visible` value
- [ ] §7's three counts sum: the two filtered ones equal the whole set
- [ ] The derivation used is recorded, per task or as a stated rule with its exceptions named
- [ ] Any task where the derivation was overridden by hand says so, and why

**Open questions**
- **Is the derivation above accepted, or is each of the 78 judged by hand?** — the project owner. The
  recommendation is **accept it**, because its `no` half is provable rather than judged and its `yes`
  half fails safe into §7's waiver mechanism. *Against: 60 `yes` marks make the note's required set
  six times the eleven already judged, and every waiver then has to be named — the rule's cost lands
  on the note rather than on this record.*
- **Does the value get backfilled at all, or does `0.6.0` ship a note that says the rule could not be
  run over most of its milestone?** — the project owner. The recommendation is **backfill**: a stated
  rule nobody can run is the state §5 was in for two releases. *Against: §7 says the judgement is
  worth having because it is made when the work is understood, and a mark made months later by
  someone who did not do the work is a different and weaker fact wearing the same field name.*

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised by the session cutting `0.6.0`, at the moment §7's commands were run for the first time on a real release.** The counts did not sum: 108 closed in M6, 30 marked, **78 unmarked**. Raised rather than absorbed, because clearing 78 marks silently would have made the release note a permanent public record resting on judgements nobody could see, and because the fix is not the backfill — it is that nothing asks for the value when §7 says it should be judged. **The cut is stopped here**, which is the outcome [T-231](T-231-cut-the-next-release.md) §1 asks to be recorded rather than a failure of it. The derivation in §1 was computed and deliberately **not applied**. |
