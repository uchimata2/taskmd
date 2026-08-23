---
id: T-209
title: Report an open child as a blocker on the parent that cannot close
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-191, T-198]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-209 — Report an open child as a blocker on the parent that cannot close

## 1. Specify

**Outcome**
A task whose child is still open is reported as waiting on that child, rather than as having nothing
outstanding. The edge is already stored, so nothing new is written anywhere — the derivation is the
whole of the change.

**Why this one**
`audit.md` step 5 says it plainly: *Close the umbrella only when every child is resolved — done, or
dropped with a recorded reason.* Two umbrellas in the current backlog are in exactly that state, and
the tool says otherwise. Measured 2026-08-22:

| Task | Children | What `context` reports |
| :--- | :--- | :--- |
| [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) | T-197 done, **T-198 review** | `STATE  open, no blocker outstanding` |
| [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) | T-201 done, **T-202 proposed**, T-204 done | `STATE  open, no blocker outstanding` |

**Re-measured later on 2026-08-22, after this repository's own work moved one of the rows.** The
table above is left as it was taken. T-198 has since gained a fourth child and T-202 has moved
`proposed` → `specified`, so the row's detail is no longer current — and the defect it was taken to
show is unchanged, which is the point of re-running it rather than reasoning about it:

```text
$ taskmd context T-191
CHILDREN
  T-197        done        Derive the test harness's problem-class list from the code
  T-198        review      Show each quiet fixture is within its own check's reach
STATE  open, no blocker outstanding

$ taskmd context T-198
CHILDREN
  T-201        done        Give the fenced-table case a row that could be reported
  T-202        specified   Mark a fixture's quiet cases so a sweep can find them
  T-204        done        Count the short-row quiet case the wide-row audit left out
  T-210        done        Account for the two derived fixtures T-198's partition drops
STATE  open, no blocker outstanding
```

**Three of T-198's four children are now resolved and the fourth is further along than it was, and
the line has not moved** — because it never read them. `CHILDREN` prints the very thing `STATE`
claims is absent, four lines above it, which is the sharpest form the defect takes.

`check` is green over both, and `list --open` ranks them alongside tasks that really are free to
start. So a session choosing what to work on is told that two of the ten open tasks have nothing in
front of them, when each is behind a chain it cannot shorten.

**The shape is the one this project keeps finding.** The rule exists, the data supporting it exists,
and nothing reads the place it lives — the same class as
[T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md)'s second index, which
`check` passed twice in a row. It is worse than silence here: `no blocker outstanding` is an active
claim, so a reader has no reason to look further.

**What is not wrong.** `STATE` is accurate about `blocked_by`, which is empty on both. The defect is
that `blocked_by` is not the only thing that stops a task closing, and the line does not say which
question it answered.

**Scope**
- In: what `context` reports for a parent with at least one unresolved child, and whether the same
  belongs in `check`
- In: a case that must not fire — a parent whose children are all resolved keeps reporting no
  blocker outstanding
- Out: **any new front-matter field.** The parent edge is already stored and children are already
  derived; a field here would be the same fact written twice, which `CLAUDE.md`'s one design rule
  forbids
- Out: waits that are not tasks. **Settled by the owner on 2026-08-22**: they stay as prose, they are
  not folded in here, and no task is raised for them — so this scope is now closed rather than
  pending an answer

**Inputs**
- `plugin/skills/taskmd/docs/method/audit.md` step 5 — the rule being enforced
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the edge kinds, and what may be derived

**Acceptance criteria**
- [ ] The gap is demonstrated **failing first**: the command output above, re-run and recorded,
      before anything changes
- [ ] After the change, the same command on the same task names the unresolved child as the
      outstanding wait
- [ ] A parent whose children are all resolved still reports no blocker outstanding, proven by
      running it rather than by reading the code
- [ ] Whether `check` reports it too is decided, and the decision is recorded either way — including
      if the answer is that it does not

**Open questions**
- ~~**This question is why `specify` is worked but not agreed, and the status stays `proposed`.** It
  changes the outcome rather than only a later phase — the scope's last *Out* defers to it, and the
  effort estimate covers the child half alone — so `specify.md` step 5 says it must be answered before
  this phase can end. It was **not** part of the batched round the owner answered on 2026-08-22: this
  task was raised after that round went out. No grant of phases can answer it.~~ **Answered by the
  owner on 2026-08-22, later the same day** — see the Log row. `specify` is now agreed and the status
  is `specified`; the phase does not advance.
- ~~**Do waits that are not tasks belong in the model at all?** Every one of the ten open tasks is
  waiting on something, and only two of those waits are task-to-task. The rest are an owner's
  answer, a person who has not been named ([T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md),
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)) and an event that
  cannot be scheduled ([T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)).
  **The owner decides**, because it is a change to what the schema means rather than to what the tool
  derives from it. **Recommended: leave them as prose and close this task on the child half alone**,
  on the ground that a wait on a person or an event has no second party to store the edge against, so
  any field for it is a hand-kept status — the class this project removes rather than adds. *The cost
  if that is wrong*: `list --open` keeps ranking a task nobody can start beside one anybody can, and
  the only thing that says so is a sentence somebody has to read. *The alternative*: a `waiting_on`
  free-text field, which makes the wait visible in every generated view at the price of a value
  nothing can validate and nothing clears when the wait ends.~~ **Answered: the child half alone,
  and the `s` estimate stands.**

## 2. Plan

**Sequencing.** Step 1 before the change, because the criterion says *failing first* and the state
of this repository's own backlog moves while the work runs — the same reason §1's first table was
re-taken rather than reasoned from.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-run `context` on both umbrellas and record what it says **now**, before anything changes. | The two runs quoted in §3 |
| 2 | Find where the closing line is derived, and decide which edge side holds a task open. | The decision in §3, naming the asymmetry it rests on |
| 3 | Change the derivation. Nothing is written to any task — the edge is already stored. | The edit to `plugin/skills/taskmd/taskmd/cli.py` |
| 4 | Tests: the positive, and **both** cases that must not fire — a parent whose children are all resolved, and a child whose parent is open. | The tests, and their run |
| 5 | Show the new tests **failing** against the code before the change. | The failures quoted in §3 |
| 6 | Decide whether `check` reports it too, by building the case and running it rather than by reasoning. | The decision in §3, with the run that settled it |
| 7 | Run the gates on this repository, whose own backlog is the live case. | `index`, `check`, the suite, and the two umbrellas re-read |

**Shape of the deliverable, decided — 2026-08-22.** The closing line **names which kind of wait it
found** — a blocker and an open child are different reasons, so they get different words rather than
one merged list of ids. *Rejected: appending children to the existing blocker list*, one clause and
no new vocabulary, but a reader would then have to open each id to learn why it was named, and the
defect this task fixes is precisely a line that did not say which question it answered.

**Outputs** — plain paths:

- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py

## 3. Implement

### Step 1 — failing first, re-measured

```text
$ taskmd context T-191
CHILDREN
  T-197        done        Derive the test harness's problem-class list from the code
  T-198        review      Show each quiet fixture is within its own check's reach
STATE  open, no blocker outstanding

$ taskmd context T-198
CHILDREN
  T-201        done        Give the fenced-table case a row that could be reported
  T-202        done        Mark a fixture's quiet cases so a sweep can find them
  T-204        done        Count the short-row quiet case the wide-row audit left out
  T-210        done        Account for the two derived fixtures T-198's partition drops
STATE  open, no blocker outstanding
```

**The backlog moved again while this session ran, and it made the case sharper rather than weaker.**
T-202 closed earlier today, so T-198's four children are now **all resolved** — and it prints the
same line as T-191, which has an open child. Two opposite states, one sentence. That is the defect
without any argument attached, and it also handed this task its negative case for free.

### Step 2 — which side of an edge holds a task open

**Only the derived side of a hierarchy edge.** A parent is held open by its children; a child is not
held open by its parent — work on a child proceeds while its umbrella waits, which is the whole
arrangement `audit.md` describes. That is the same asymmetry the existing code already applies one
edge over: `blocked_by` is flagged and its inverse `blocks` is not, because a task you are blocking
does not block you.

So the test is not *is this a hierarchy edge* but *is this name the edge's `derives` side*, which is
what `holds_open` asks.

### Step 3 — the change

`context` collects open children beside open blockers, flags them in the `CHILDREN` block with the
same `<-- still open` marker the dependency side uses, and the closing line names them as a distinct
kind of wait. **No task file is touched and no field is added**: the parent edge was already stored
and children were already derived, so this reads data that was there all along.

### Step 4 — after

```text
$ taskmd context T-191
CHILDREN
  T-197        done        Derive the test harness's problem-class list from the code
  T-198        review      Show each quiet fixture is within its own check's reach  <-- still open

STATE  open, waiting on child T-198

$ taskmd context T-198
STATE  open, no blocker outstanding
```

Five tests: one open child, two open children, a parent whose children are all resolved, a child
whose parent is open, and a task carrying both a blocker and an open child —
`STATE  open, waiting on T-001 and on child T-003`.

### Step 5 — the tests shown failing first

Against `git show HEAD:` of `cli.py`, the five new tests give **3 failed, 2 passed**:

```text
'STATE  open, waiting on child T-002' not found in '... CHILDREN
  T-002        proposed    The child

STATE  open, no blocker outstanding'

'STATE  open, waiting on children T-002, T-003' not found in '... STATE  open, no blocker outstanding'

'STATE  open, waiting on T-001 and on child T-003' not found in '... STATE  open, waiting on T-001'
```

**The two that passed before are the two that must not fire**, and that is the correct result rather
than a gap: they are guards against the change over-firing, so a guard that failed beforehand would
mean the old code was already wrong about them. Stated because *3 of 5 failed* reads like partial
coverage and is not.

### Step 6 — does `check` report it too? No, and the run says why

**Decided: no.** An open parent with an open child is the ordinary state of every umbrella
mid-flight, so a `check` class for it would report a healthy backlog as a problem — both of this
repository's audit umbrellas, every day they are correctly in progress. `check` reports defects;
this is not one.

**Building the case to answer that turned up one that is.** A **closed** parent with an open child is
exactly the state `audit.md` step 5 forbids, and:

```text
$ taskmd check --root <T-001 done, child T-002 proposed>
OK - 2 task(s), 10 field value(s), 11 front-matter value(s), 1 reference(s), ...
```

Raised as [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) rather than folded in:
it is a new validator class with a fixture and coverage rows, not a change to what a derived line
says.

### Step 7 — the gates

```text
Wrote tasks/README.md
OK - 212 task(s), ...
322 passed, 8 subtests passed
```

**Decisions & assumptions**

- **Only the derived side of a hierarchy edge holds a task open** — a parent does not hold its child,
  which is the same asymmetry `blocked_by` / `blocks` already has. Rejected: treating any hierarchy
  link as a wait, which would report every child as held up by its own umbrella - 2026-08-22.
- **The line names the kind of wait.** Rejected: merging children into the existing blocker list,
  which is one clause fewer and leaves the reader opening ids to find out why each was named — the
  defect being fixed - 2026-08-22.
- **`check` does not report the open case** — it is the ordinary state of an umbrella mid-flight, and
  a class for it would report a healthy backlog - 2026-08-22.
- **The closed-parent case is a task, not a widening** — a new validator class carries a fixture and
  coverage rows, which is a different size from a derived line - 2026-08-22.

**Outputs produced**

- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The gap is demonstrated **failing first**, re-run and recorded before anything changes | met | §3 step 1. Re-running it mattered: T-202 closed earlier the same day, so T-198's children are now all resolved and it printed the **same** line as T-191, which has an open child — two opposite states, one sentence |
| After the change, the same command names the unresolved child as the outstanding wait | met | `STATE  open, waiting on child T-198`, with `<-- still open` beside T-198 in the `CHILDREN` block |
| A parent whose children are all resolved still reports no blocker outstanding, **proven by running it** | met | T-198 itself, §3 step 4, and `test_a_parent_whose_children_are_all_resolved_reports_no_blocker_outstanding`. A second must-not-fire case was added that the criterion did not ask for — a child whose parent is open — because the asymmetry is where this could have over-fired |
| Whether `check` reports it too is decided, and recorded either way | met | §3 step 6: **no**, because an open umbrella with an open child is the ordinary mid-flight state and a class for it would report a healthy backlog. Building the case to answer it found the state that *is* a defect — a **closed** parent with an open child, over which `check` returns `OK` — now [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) |

**What this does not settle.** `list` and the generated index still rank a parent with an open child
beside a task that is genuinely free; only `context` reads the new state. That is the scope §1 drew
and not an oversight, but it is the half a session choosing what to work on meets first.

**Open questions, re-read before closing.** §1 recorded two and both were answered by the owner on
2026-08-22 — the second, on waits that are not tasks, was answered *the child half alone*, and this
task is that half and nothing more. Nothing in §3 raised a question for the owner: the closed-parent
finding is a task, not a question.

**Child fix tasks raised**
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) — a closed parent with an open child, which `check` returns `OK` over

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* while answering a request for the open list with a blocks column. Building that column meant reading `blocked_by` on all ten open tasks, finding it empty on every one, and then checking `context` against the two parents that visibly cannot close — which is where the disagreement with `audit.md` step 5 turned up. `medium` rather than `high`: nothing is corrupted and no gate passes work it should stop, so the damage is a misread rather than a bad state — but the rival was argued, on the ground that the method states a rule nothing enforces and `no blocker outstanding` is an assertion rather than a silence. `s` because both the parent edge and the derived children already exist, so nothing is stored and only the report changes; that estimate covers the child half only, and the open question could widen it. It carries an open question that is the owner's, so nothing starts on it. |
| 2026-08-22 | (no change) | **`specify` worked and deliberately not agreed; the status stays `proposed`.** The evidence was re-run rather than re-read, and it needed to be: this session's own work gave T-198 a fourth child and moved T-202 to `specified`, so §1's table was stale within hours of being written. The table is **left as it was taken** and the re-measurement sits below it (METHOD rule 5). **The defect is unchanged and now shows more sharply** — three of T-198's four children are resolved, the fourth has advanced a phase, and `STATE` still prints `open, no blocker outstanding` four lines under a `CHILDREN` block that lists them. **What does not move is the phase.** The open question — whether waits that are not task-to-task belong in the model — changes this task's outcome and not merely a later phase: the scope's last *Out* defers to it and the `s` estimate covers the child half alone. So `specify.md` step 5 forbids ending the phase, and the multi-phase grant this session ran under authorises **phases, not answers**. The question was never in the batched round of 2026-08-22 — this task was raised after it went out — and it is carried to the owner with the recommendation and both costs §1 already records. |
| 2026-08-22 | → specified | **The open question is answered by the owner: leave waits that are not task-to-task as prose, and close this task on the child half alone.** Put to them in a two-question round the same day, after the phase had been worked and stopped at exactly this point. It is the recommendation §1 carried: a wait on a person or an unschedulable event has no second party to store the edge against, so any field for it is a hand-kept status — the class this project removes rather than adds — while the child half stores nothing at all, because `parent` is already recorded and `children` is already derived. *Rejected: a `waiting_on` free-text field*, which makes every wait visible in every generated view, at the price of a value nothing can validate and nothing clears when the wait ends, and which would widen this task past its `s` estimate. **The known cost of the answer, recorded with it**: `list --open` keeps ranking a task nobody can start beside one anybody can, and the only thing that says so is a sentence somebody has to read. The scope's last *Out* is now closed rather than pending, the four criteria are unchanged, and the estimate stands. **The phase does not advance** — this row ends `specify`; `plan` is not authorised (METHOD §3.1). |
| 2026-08-22 | → done | **All four criteria met. `context` now reads the children it was already printing**: `STATE  open, waiting on child T-198`, with the same `<-- still open` marker the dependency side uses. Nothing is written to any task — the parent edge was stored and children were derived, so this is a reader for data that was there all along. **Re-running the failing case first mattered**: T-202 closed earlier the same day, so T-198's four children are now all resolved and it printed the *same* line as T-191, which has an open child — two opposite states, one sentence, and the negative case handed over for free. **Only the derived side of a hierarchy edge holds a task open**, which is the asymmetry `blocked_by`/`blocks` already has, and a second must-not-fire test was added for it that the criteria did not ask for. Five new tests: **3 fail against the code before the change and 2 pass**, the two being the guards, which is the correct result rather than partial coverage. **`check` does not report the open case** — an umbrella with an open child is the ordinary mid-flight state — and building the case to decide that found the one that *is* a defect: a **closed** parent with an open child, over which `check` returns `OK`, now [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md). |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: nothing new is stored by its outcome.** `parent` is already recorded and `children` already derived, so `implement` changes what is reported and not what is written — a plan that adds a front-matter field has left the scope. |
