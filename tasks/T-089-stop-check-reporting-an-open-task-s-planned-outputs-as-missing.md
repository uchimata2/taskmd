---
id: T-089
title: Stop check reporting an open task's planned outputs as missing
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-002, T-025, T-032]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-089 — Stop check reporting an open task's planned outputs as missing

## 1. Specify

**Outcome**
A project can declare a task's outputs when it plans them, and `check` stays quiet about them until
the task claims to have produced them.

**Why this one**
`check` reports every declared path that does not exist, whatever the task's status. So a project
that fills `deliverables` at `specify` or `plan` time gets a permanent complaint about work it has
not started:

```
MISSING OUTPUT T-006 declares 'deliverables/D6-executive-board-presentation.md', which does not exist
```

Three of the six problems the first adopting project (`control/LOCAL-CONTEXT.md`) reported on the
day it migrated are of exactly this kind, and its tasks are correct: the field says what the task
will produce, which is what makes the deliverable map derivable before the work happens.

**This repository is not the counter-example it looks like.** Its tasks carry `deliverables: []`
until `implement`, so it never sees the message. That is a habit this repository fell into, not a
rule anything states, and it is why the defect survived to publication: the validator was only ever
run against a project that avoided the case.

**The retiring standard had the distinction and taskmd dropped it.** `reference/TASK-WORKFLOW.md`'s
tool separated `check` from `check --closing`, and only the closing form required declared outputs
to exist. That separation is the thing to reconstruct, in whatever shape suits four commands rather
than five.

**Why `high`.** A validator that cries wolf gets ignored, which is the argument `../CLAUDE.md` makes
for keeping the leak check narrow. This one cries wolf at exactly the moment an adopter is deciding
whether to trust it: their first run, on their real backlog.

**Requirements served**
R-16 (`docs/SCOPE.md`) — the validator is proven by being made to fail on what it claims to catch,
and a false positive is the other half of that. R-4 in spirit: verification belongs at `implement`'s
exit, not before it.

**Scope**
- In: when a declared-but-missing output is a problem, and what `check` says when it is not.
- In: whether the rule keys on `status` being closed, on the phase reaching `implement`, or on
  something the project configures. Each is a different claim about what `deliverables` means.
- Out: `deliverables` becoming a command again. It is a validation, settled in T-002 under non-goal
  11.
- Out: [T-025](T-025-let-check-notice-a-stale-generated-index.md), the other thing `check` cannot
  see. They touch the same command and answer different questions.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, the deliverables check inside `cmd_check`.
- `reference/TASK-WORKFLOW.md` §0, for the `--closing` distinction as it was.
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, which assigns `deliverables` the role of
  METHOD §1 rule 5's *outcome* and already says only that one of the three closing conditions is
  mechanical.

**Acceptance criteria**
- [ ] A fixture with an **open** task declaring a path that does not exist passes `check`
- [ ] A fixture with a **closed** task declaring a path that does not exist fails it, with the
      message naming the task and the path
- [ ] Both fixtures are in `tests/fixtures/`, so the rule is proven by failing as well as by passing
- [ ] The binding says which condition it now checks, in one sentence, and nothing else restates it

**Open questions**
- **What "not yet" means, exactly. Answered by the maintainer on 2026-08-09: the task being closed.**
  `deliverables` asserts *production*, and the one place the method requires an outcome to exist is
  METHOD §1 rule 5 — a task closes when its outcome exists. Keying on closed makes `check` enforce
  exactly that sentence and invents no new claim.

  *Rejected: key on the phase reaching `implement`.* It is not merely more to explain, it is wrong in
  the same direction as the defect. A task that has just **entered** `implement` legitimately has no
  outputs yet — producing them is what the phase is — and `implement`'s own exit criterion places
  them at the exit, not the entry. That rule would reinstate the false positive in a narrower window
  and would be harder to argue with, because the window looks reasonable.

- **The `cancelled` case is real, and this task does not solve it.** A cancelled task is closed, so
  the rule above reports its declared outputs — but rule 5 does not apply to a task that was
  abandoned rather than completed, so that is the same false positive wearing a different status.
  It is not hypothetical: two of the projects onboarded on 2026-08-09 carry a cancelled task, and one
  of them declares two outputs. It fires today in neither, because those two paths happen to exist.

  Not solved here because the only clean fix is a config key naming the abandoned status — the
  `blocked_status` precedent shows the shape — and every key in that file is **required**, so it is a
  line every adopting project pays for to settle a case none of them is currently hitting. Carried as
  a child task instead, with the evidence, so the next reader meets a decision rather than a gap.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Make the deliverables check skip open tasks, then run the suite **before** touching any fixture. | `plugin/skills/taskmd/taskmd/cli.py`, and the suite's reaction recorded in §3 |
| 2 | Close `broken-deliverable`'s task. Its status is `proposed` today, so it has been proving this class with an **open** task — the fixture was miscategorised from the start and step 1 is what exposes it. | `tests/fixtures/broken-deliverable/tasks/T-001-x.md` |
| 3 | Add the positive fixture: an open task declaring a path that does not exist, which must pass. | `tests/fixtures/planned-deliverable/`, and its row in the fixtures table |
| 4 | Assert both directions, and re-run the first adopting project to show which of its six problems were noise and which were real. | `tests/test_cli.py`, and the before/after in §3 |
| 5 | One sentence in the binding saying which of rule 5's conditions is now checked. Nothing else restates it. | `plugin/skills/taskmd/docs/bindings/local-markdown.md` |
| 6 | Raise the `cancelled` case as a child task, with the evidence from §1. | A new task |

**Step 1 runs before step 2 deliberately.** The existing negative test will break, and that break is
the finding: it says `broken-deliverable` has been asserting this class through a task whose status
made the assertion vacuous under the new rule. Fixing the fixture first would hide that the fixture
was ever wrong — the same reason T-025 captured its vacuous pass before repairing it.

## 3. Implement

**Decisions & assumptions**
- **`broken-deliverable` was miscategorised, not merely in need of an update — 2026-08-09.** Its task
  was `proposed`. So the fixture that has been proving this class since T-002 was proving it with an
  **open** task, which is the case that was never supposed to fail. Changed to `done`, and the test's
  docstring now says the status is load-bearing so the next person cannot flip it back innocently.
- **The reason `check` returns 0 on the positive fixture is asserted, not just the exit code —
  2026-08-09.** `assertNotIn("MISSING OUTPUT", out)` alongside the code, because a fixture that
  passes for an unrelated reason is the failure mode this whole task is about.
- **The cancelled case was carried, not solved — 2026-08-09.** See §1 and
  [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md).

**Verification**

Step 1 ran before any fixture was touched, and the suite's reaction is the finding:

```
FAIL: test_declared_deliverable_that_is_gone
AssertionError: 0 != 1 : OK - 1 task(s), vocabulary valid, references resolve, no broken links
```

That is the eight-day-old negative fixture announcing that its task was open. Nothing about the new
rule is wrong there — the fixture was.

**The real case.** The first adopting project (`control/LOCAL-CONTEXT.md`), unchanged on its side:

```
before   6 problem(s) over 41 task(s)
after    MISSING OUTPUT T-011 declares '.claude/skills/session-start/SKILL.md', which does not exist
         MISSING OUTPUT T-011 declares '.claude/skills/session-close/SKILL.md', which does not exist
         MISSING OUTPUT T-014 declares 'tools/tasks/check-index.py', which does not exist
         3 problem(s) over 41 task(s)
```

Six became three, and **the three that remain are on `done` tasks** — real findings about that
project rather than noise. §1 predicted exactly this split before the fix, which is the strongest
thing that can be said for the diagnosis.

**Both directions, on fixtures:** `planned-deliverable` (open, missing path) passes and prints no
`MISSING OUTPUT`; `broken-deliverable` (closed, same missing path) still fails naming `out/report.md`.

**Suite:**

```
test_cli.py  44 tests OK   test_list.py  18 OK   test_runtime.py  27 OK   test_schema.py  44 OK
```

**What the work turned up, recorded rather than absorbed:** the decision this task's sibling T-088
was re-deciding had already been made in T-032 on 2026-08-06. Found while looking for the right home
for the cancelled case. T-088's record now points at T-032, and T-032's finding 1 carries a dated
resolution note beside the original text.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py) — `check_deliverables` skips open tasks
- [`tests/fixtures/planned-deliverable/`](../tests/fixtures/planned-deliverable/tasks/T-001-x.md), [`tests/fixtures/broken-deliverable/`](../tests/fixtures/broken-deliverable/tasks/T-001-x.md) — the pair
- [`tests/test_cli.py`](../tests/test_cli.py), [`tests/fixtures/README.md`](../tests/fixtures/README.md)
- [`plugin/skills/taskmd/docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) — the one sentence
- [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) — the carried case

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| An **open** task declaring a path that does not exist passes `check` | met | `planned-deliverable`, exit 0, and asserted to print no `MISSING OUTPUT` so it cannot pass for an unrelated reason |
| A **closed** task declaring a path that does not exist fails, naming task and path | met | `broken-deliverable`, still `MISSING OUTPUT T-001 declares 'out/report.md'`. Its task had to be closed first — it was `proposed`, which §3 records as a defect in the fixture rather than a consequence of the fix |
| Both fixtures are in `tests/fixtures/`, so the rule is proven by failing as well as by passing | met | The two are a deliberate pair — same missing path, opposite statuses — and the fixtures README says so, since a reader finding them separately would not see the point |
| The binding says which condition it now checks, in one sentence, and nothing else restates it | met | One clause added to the rule-5 paragraph that already owned this. Grepped for other homes: `CLAUDE.md` and the config's *Deliverables* section describe the field, not the timing, so neither needed touching |

Four met, one case carried.

**The carried case is not a criterion failure.** No criterion mentions `cancelled`, and the rule as
specified was implemented exactly. The gap is that `cancelled` is closed while METHOD §1 rule 5 does
not apply to it, so the fixed rule reproduces the original fault under a different status —
[T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md), raised with the evidence
that two of the four projects onboarded today carry a cancelled task and that neither fires yet.

**The criteria could not have caught the fixture defect, and that is worth noting.** All four are
about behaviour; none asks whether the existing fixtures were testing what they claimed. It surfaced
only because the plan ran the suite *before* repairing anything — the same ordering T-025 used, for
the same reason, and the second time in two tasks that the ordering paid.

**Child fix tasks raised**
- [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) — what a cancelled task's declared outputs assert

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | -> done | Settled on the task being closed, which is METHOD rule 5 stated mechanically and invents no new claim. Keying on the phase reaching implement was rejected as wrong rather than merely wordy: a task that has just entered implement legitimately has no outputs, since producing them is what the phase is for. Running the suite before repairing any fixture exposed that broken-deliverable had been proving this class with an open task since T-002 -- the fixture was miscategorised, and the fix is what revealed it. Six problems became three on the first adopting project, and the three that remain are on done tasks, which is the split section 1 predicted. The cancelled case is carried by T-090: it is closed but rule 5 does not cover it, so the same false positive survives under a different status. |
| 2026-08-09 | → proposed | Raised on the day the first project outside this repository adopted taskmd. Half of what its validator reported was noise of this one kind: tasks that declare their outputs when they plan them, which is what makes a deliverable map derivable in advance. This repository never saw it because its own habit is to leave `deliverables` empty until `implement`, so the case existed and was untested at publication. The retiring standard had the distinction as `check --closing`; taskmd dropped it without deciding to. `high` because a validator that cries wolf on an adopter's first real run is worse than one that says less. |
