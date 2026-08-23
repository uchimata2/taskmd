---
id: T-242
title: Judge adopter_visible on the closed M6 tasks the release note must cover
type: fix
status: done
phase: review
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

*Annotated 2026-08-23, after the owner answered: the proposal above was accepted and applied. It ran
over 80 tasks rather than 78 — the owner's second answer added `T-006` and `T-085`, which sit outside
M6 — so the figures it produced were 62 `yes` and 18 `no`. The paragraph above is left as written
because it records what was proposed before the answer; §3 records what happened.*

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
| 1 | Put the derivation and the backfill question to the owner as a survey, with both alternatives priced. | Two recorded answers, with what each was chosen over |
| 2 | Compute each task's value from the union of two sources — the files its commits touched, and its declared `deliverables`. | A value per task, and the counts behind it |
| 3 | Write the value into each task's front matter, in the position the already-marked tasks use. | 80 task files carrying `adopter_visible` |
| 4 | Re-run §7's three counts and check the two filtered ones sum to the whole set. | The counts, and whether they sum |

## 3. Implement

**Decisions & assumptions**

- **The owner accepts the computed rule — 2026-08-23.** Asked as a survey with all three options
  priced both ways. *Rejected: judge all 78 by hand* — it gives the best marks and is what the field
  was designed for, but it is 78 judgements and §7 itself says a mark made now is a weaker fact than
  one made when the work was understood, so hand-judging buys less than it looks. *Rejected: do not
  backfill, and say in the note that the rule could not be run* — honest and free, but it leaves the
  note bounding nothing, which is the state `v0.4.0` shipped in and the reason the rule exists.
- **The rule, stated so a wrong mark is findable.** A task is marked `no` when its work touched no
  file under `plugin/`, and `yes` otherwise. The `no` half is **proved rather than judged**: since
  [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) an install copies exactly the `plugin/` subtree, so a
  task that changed nothing inside it cannot have changed anything an adopter receives. The `yes`
  half is deliberately over-inclusive, because §7 lets a required task be consciously waived with the
  waiver named — over-inclusion costs a line in the note, under-inclusion costs a permanent omission
  from a record [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md)
  forbids rewriting.
- **The evidence is the union of two sources, because each misses what the other catches — 2026-08-23.**
  The files a task's commits touched (`git log --all --name-only --grep=<id>`) and its own declared
  `deliverables`. [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)
  is why the union is needed and not either half: it declares `plugin/skills/taskmd/docs/BINDING.md`
  and no commit message names it, so the git source alone would have marked it `no` and dropped a
  shipped change out of the note.
- **Two tasks outside M6 were marked as well — 2026-08-23.** The owner's second answer. `T-006`
  *"Package, document and publish"* and `T-085` *"Install the published plugin on a machine that has
  never seen it"* both closed after the `v0.5.0` tag and sit in M1 and M5, so §7's milestone query
  cannot see them. They are marked here and added to this release's set by hand; the durable fix is
  [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md).

**Outputs produced**
- 80 task files gained an `adopter_visible` value — the 78 unmarked in M6, plus `T-006` and `T-085`.
- 62 `yes` and 18 `no` among them.

**What the counts say now**

```text
$ taskmd list --work_package M6 --closed                        | wc -l   → 108
$ taskmd list --work_package M6 --closed --adopter_visible yes  | wc -l   →  72
$ taskmd list --work_package M6 --closed --adopter_visible no   | wc -l   →  36
                                                                  72 + 36 = 108
```

They sum, which is the whole mechanism: a filter cannot report what it failed to see, so the sum is
the only thing that shows nothing was skipped.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every closed M6 task carries an `adopter_visible` value | met | 108 of 108, verified by the counts rather than by the edit succeeding |
| §7's three counts sum | met | 72 + 36 = 108, run after `index` and `check` were both clean |
| The derivation used is recorded, per task or as a stated rule with its exceptions named | met | §3 above states the rule, its two sources, and why the `yes` half is deliberately loose |
| Any task where the derivation was overridden by hand says so, and why | met | None was. Every one of the 80 came from the rule, with no manual override |

**Child fix tasks raised**
- [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md) — as
  a soft edge. It is not part of this record's outcome, which was the marks; it is the reason the
  marks had to reach outside M6 at all.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **The owner answered both questions as a survey, and the derivation was applied.** 80 tasks marked — the 78 unmarked in M6 plus `T-006` and `T-085`, which closed after the `v0.5.0` tag and sit outside the milestone §7 queries. 62 `yes`, 18 `no`, no manual override anywhere. **§7's counts now sum: 108 = 72 + 36**, checked after `index` and `check` were both clean rather than assumed from the edits landing. Closes on all four criteria. **What it does not fix is why the field went unfilled**, which is not in this record's scope and is not solved by clearing the backlog — nothing asks for the value at the moment §7 wants it judged, and the next release meets the same wall. |
| 2026-08-23 | → proposed | **Raised by the session cutting `0.6.0`, at the moment §7's commands were run for the first time on a real release.** The counts did not sum: 108 closed in M6, 30 marked, **78 unmarked**. Raised rather than absorbed, because clearing 78 marks silently would have made the release note a permanent public record resting on judgements nobody could see, and because the fix is not the backfill — it is that nothing asks for the value when §7 says it should be judged. **The cut is stopped here**, which is the outcome [T-231](T-231-cut-the-next-release.md) §1 asks to be recorded rather than a failure of it. The derivation in §1 was computed and deliberately **not applied**. |
