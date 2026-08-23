---
id: T-223
title: Ship the pre-release audit as a method document, so every adopter gets it
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-032, T-036]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/docs/method/pre-release-audit.md
---

# T-223 — Ship the pre-release audit as a method document, so every adopter gets it

## 1. Specify

**Where this came from**

An adopting project — `htmldeck`, public — was asked for a full pre-release audit of itself and found
it had no reusable statement of how to run one. It wrote one locally, then read
[`audit`](../plugin/skills/taskmd/docs/method/audit.md) and found that most of what it had written
either already lived here or contradicted a rule here. **The owner's decision was that the pre-release
audit should be a taskmd feature rather than one project's local document**, so every adopter gets it.

This branch carries a **draft** at the deliverable path. It is the input to `specify`, not a finished
deliverable, and the outcome is not agreed until this task says so.

*Reviewed 2026-08-22, after the branch merged.* **That is true of the draft's status and false of
its location.** The branch is `master` now, and the deliverable path is inside `plugin/`, which is
exactly what an install copies (T-053). Nothing in the tree says the document is a draft — only
this record does — and `METHOD.md` §5 and §7 and [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
already point at it by name. So the three open questions below are not held open at no cost: they
are held open on a document that the next tag publishes as method, and that the adopting project is
already waiting for — `htmldeck`'s `docs/AUDIT-METHOD.md` says *"`pre-release-audit.md` arrives
with a taskmd release; until it does, this file names what it will carry"*. **Both were done on 2026-08-22.** The owner answered all
three, and chose to move the draft out as well: it is now
`docs/pre-release-audit-draft.md`, outside `plugin/`, named
for what it is, and the three pointers were removed with it. `deliverables:` still names the
path the finished document goes to, which is now true rather than aspirational — and `check`
does not object to an open task declaring an output that does not exist yet.

*Superseded 2026-08-23 by this task's own `implement`, and left standing rather than rewritten.*
The document is at its declared path,
[`pre-release-audit.md`](../plugin/skills/taskmd/docs/method/pre-release-audit.md); the three pointers
are back; and there is no file at `docs/pre-release-audit-draft.md`. So the paragraph above is a dated
statement about where the draft sat, not a description of the tree. **Its three references to that path
were de-linked, not repointed and not reworded** — a Markdown link is a live pointer and a backticked
path is not (T-092), which is the distinction that lets a dated sentence keep its words while `check`
stops resolving it at a file that is gone. Two of the three sit in the Log below and had the same
treatment for the same reason.

**Outcome**

One tier-3 method document, loaded on demand, that a session can follow to run an audit whose subject
is everything a project is about to release — without that document telling anyone what to look for.

**Scope**

- In: the six things that only start to matter when an audit's subject is *everything* — coverage
  grades, coverage as a failing partition, cycles, severity that obliges something, remedy-as-hypothesis,
  and a grading pass after the remedies exist. Plus the scale exception that moves findings out of the
  umbrella, and the rule that this audit is requested and is never a step in a release procedure.
- In: one row in [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §7, one clause in its §5, and one
  pointer from [`audit`](../plugin/skills/taskmd/docs/method/audit.md). No rule in either is changed.
- Out: **anything that says what to look for.** See *The two constraints* below.
- Out: shipping a template. taskmd ships no task templates and that is a design decision (T-101, T-032);
  the audit umbrella stays project-owned. Raise it separately if it is wanted.
- Out: validating a `finding:` field against a findings register. That is schema and tool work, it is a
  real gap the adopting project has worked around, and it is a different task.

**The two constraints this was written against, and how the draft satisfies them**

1. **R-9** — nothing in the method may assume code, tests, compilers or version control; it must read
   sensibly for research, a deck, a training course or an ops runbook. The source document assumed all
   four. The draft names no artefact type, no tool and no command, and its worked example is a training
   course before its first cohort. **This is the criterion most likely to be violated by a later edit**,
   because the person editing will have a repository in mind.
2. **[`audit`](../plugin/skills/taskmd/docs/method/audit.md), *Procedure*** — *"How this one examines its
   subject is not fixed here … A standing checklist carried by every audit would examine each new subject
   for the last subject's problems."* The source document was largely such a checklist: four named
   aspects, a list of finding classes, and a forty-three cycle programme. **None of that came across.**
   What came across is the *shape* the plan must decide — grade the subject, choose aspects, order the
   cycles — with one project's aspects shown as an illustration and explicitly not a set to adopt.

**What was deliberately left behind**

The source document's aspects, its finding-class list, its cycle programme, its identifier space, its
register location, and everything reasoning from files, sizes, gates or renders. Those stay in the
adopting project's own audit plan, which is where [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
says a given audit's procedure belongs.

**Inputs**

- [`audit`](../plugin/skills/taskmd/docs/method/audit.md) — the procedure this extends and does not change.
- [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5, §7 — the type, and the load-on-demand table.
- [`SCOPE.md`](../docs/SCOPE.md) §3 R-9, R-21, R-22 — the constraints above, and the tier discipline.

**Acceptance criteria**

- [ ] The document tells a session how to *run* an audit of everything and never what to *find* in one.
- [ ] It reads sensibly for a non-software project, demonstrated by a worked example that is not software.
- [ ] It restates no rule that [`audit`](../plugin/skills/taskmd/docs/method/audit.md) or
      [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) already owns; where it deviates from one, it
      says so and says why.
- [ ] The three edits *Scope* names are present and resolve: the row in
      [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §7, the clause in its §5, and the
      pointer from [`audit`](../plugin/skills/taskmd/docs/method/audit.md). Each is checked by
      following it, not by seeing that the edit was made.
- [ ] No rule in [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) or
      [`audit`](../plugin/skills/taskmd/docs/method/audit.md) is changed by this work: the diff
      against each touches only the row, the clause and the pointer.
- [ ] Tier 1 is unchanged; `tests/test_budget.py` passes without editing the bound.
- [ ] `taskmd check` passes.
- [ ] The claim that the document is reachable is verified by running, not by reading the §7 table.

**Open questions**

- ~~**Is the scale exception acceptable?** The draft lets findings move out of the umbrella into their own
  record once the umbrella stops being a task record, under three conditions. It is a documented
  deviation from [`audit`](../plugin/skills/taskmd/docs/method/audit.md) step 3, and it is the one place
  the draft argues against an existing rule rather than extending it. Owner answers.~~ **Answered
  2026-08-22: accept as written.** See the Log row of that date.
- ~~**Is `pre-release audit` the right name?** The document is about audit *scale*, and the release is only
  the commonest reason to reach that scale. `audit at scale` would be more accurate and less findable.
  Owner answers.~~ **Answered 2026-08-22: keep `pre-release audit`.** See the Log row of that date.
- ~~**Does the Low-batching rule belong here or in `audit`?** The draft batches Low findings instead of
  raising a task each, and argues it as a scale rule. It may be a correction to
  [`audit`](../plugin/skills/taskmd/docs/method/audit.md) step 4 at every scale. Owner answers.~~
  **Answered 2026-08-22: it is a scale rule and stays here.** See the Log row of that date.
- ~~**Id collision.** `T-223` was the next free number when this branch was cut, and another session was
  committing to `master` at the time. Renumber at merge if it was taken.~~ **Settled 2026-08-22: it keeps
  `T-223`.** The other session had allocated the same number and neither could see the other. This branch
  was merged first and so was reachable by anybody else, which is the rule that decided it; the other
  record renumbered to
  [T-229](T-229-correct-the-migrated-away-fixture-s-own-prose-which-still-says-all-four-commands-refuse.md)
  and its references moved with it. Nothing here changed.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run the two checks that can still force a wording change, while the file is still a draft: a sweep of the whole document for software vocabulary (R-9), and a clause-by-clause comparison against [`audit`](../plugin/skills/taskmd/docs/method/audit.md) and [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) for a rule restated rather than extended | both results, dated, naming what was swept and what the comparison covered — plus any wording change they force, made at the draft's current path |
| 2 | Move the document to its declared path and make it read as method rather than as a draft: drop the draft banner, retitle, and rewrite every internal link for the new directory. Nothing stays behind at `docs/` | the file at `plugin/skills/taskmd/docs/method/pre-release-audit.md`, with no link routed through `../plugin/`, and no file at `docs/pre-release-audit-draft.md` |
| 3 | Restore the three pointers by reverting the hunks that removed them in `134e077`, rather than composing new text | the clause in `METHOD.md` §5, the row in its §7 table, and the paragraph in `audit.md` under *Procedure* |
| 4 | Follow each of the three pointers, and load the document the way the §7 row says a session does, from the tree as an install receives it | what each of the three resolved to, named one at a time |
| 5 | Run the gates: `taskmd index`, `taskmd check`, `python -m pytest tests/ -q`, and `git diff 134e077^` over the two edited documents | the four outputs, quoted |

**Step 1 runs before the move, and that ordering is this plan's one real choice.** Moving first
works and costs nothing to execute, but it produces a single diff in which a rename, a retitle, a
link rewrite and a wording change are indistinguishable — and the thing a reader most needs to see
is that *the content the owner agreed is the content that shipped*. Running the checks first keeps
step 2 a move, so that stays visible. *Rejected: move first and check at the new path*, which reaches
the same document and hides which half of the diff is content.

**Step 3 reverts rather than writes, and that is what makes a criterion checkable.** Fresh pointer
text would read the same and could not be **shown** to leave the two documents' rules alone: the
diff would be an addition somebody has to judge. A revert can be compared. That is also why step 5
diffs against `134e077^` rather than against `HEAD` — neither document has been touched by any commit
since, so an exact restoration makes that diff **empty**, which answers *no rule is changed* as a
command instead of as a reading. *Rejected: compose the three pointers afresh*, one less lookup and
no way to prove the constraint.

**Step 4 follows the pointers instead of confirming the edits were made**, which is the difference
the acceptance criteria name twice. Seeing a row in the §7 table is reading the table; the criterion
asks that the document be reached.

**Outputs**

- `plugin/skills/taskmd/docs/method/pre-release-audit.md` — new, the deliverable
- `plugin/skills/taskmd/docs/METHOD.md` — the §5 clause and the §7 row restored
- `plugin/skills/taskmd/docs/method/audit.md` — the *Procedure* paragraph restored
- `docs/pre-release-audit-draft.md` — gone


## 3. Implement

**Decisions & assumptions**

- **The deliverable was recovered from `134e077^`, not moved back from `docs/` and un-rewritten**
  — 2026-08-23. When the draft left `plugin/` its links were rewritten for the new directory and the
  lines holding them re-wrapped. Moving it back by hand would have meant undoing both, producing a
  diff in which a rename, a link rewrite and a re-wrap are indistinguishable from a content change.
  Taking the pre-move file out of git instead makes the deliverable **provably** the agreed content
  plus one deliberate paragraph: `git diff 134e077^` over it prints that paragraph and nothing else.
  *Rejected: `git mv` and hand-edit the links back* — the same file if done perfectly, and no way to
  show that it was. This changes step 2's method, not the plan's order or its output.
- **One wording change was forced by step 1, and only one** — 2026-08-23. *When one runs* opened
  **"Requested, never automatic, and never a step in the release procedure"**. The first half is
  [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5's rule about every audit, and
  [`audit`](../plugin/skills/taskmd/docs/method/audit.md)'s opening, stated in full and losing nothing
  — a second home. It now names that rule and points at it, and states only the half this size adds.
  **The test used, and worth keeping:** a compression that cannot be followed without the original is
  a pointer; one that can is a copy. *Rejected: leave it* — it reads well and is exactly what the
  criterion forbids.
- **The five-rule summary in the opening was judged a pointer and left** — 2026-08-23. *"Everything
  in `audit` holds — one umbrella, a finding threshold stated before looking, a child task per
  actionable finding, no finding fixed where it is found, and the umbrella closed only when every
  child is resolved"* names five rules by their content. It survives the test above: no clause is
  followable without `audit`, and the list is what makes the two later deviations locatable. It is
  also the shape [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §3 already sanctions — *a
  heading that says where a rule lives is not a copy of the rule*. Recorded because it is the closest
  call in the document, so `review` sees that it was made rather than missed.
- **The three stale references to the draft were de-linked, not repointed and not reworded**
  — 2026-08-23. See the annotation in §1. `deliverables:` was already correct and needed no edit.
- **`check`'s exit code is measured, not inferred from a pipeline** — 2026-08-23. Every exit code
  quoted below comes from running the command with its output redirected to a file. Piping `check`
  into `tail` and echoing `$?` reports **`tail`'s** status, which is always 0 — so a run that
  actually failed reads as a pass. That is how the three broken links below were nearly missed.

**Outputs produced**

- `plugin/skills/taskmd/docs/method/pre-release-audit.md` — the deliverable, 201 lines
- `plugin/skills/taskmd/docs/METHOD.md` — the §5 clause and the §7 row restored
- `plugin/skills/taskmd/docs/method/audit.md` — the *Procedure* paragraph restored
- `docs/pre-release-audit-draft.md` — removed

**Verification**

**Step 1, R-9.** Two sweeps over the whole draft. The first, for software and version-control
vocabulary (`code`, `compil*`, `test`, `repositor*`, `repo`, `commit`, `branch`, `git`, `software`,
`bug`, `function`, `api`, `script`, `command`, `deploy*`, `build`, `ci`, `install*`, `file`,
`directory`, `folder`, `path`, `program`, `developer`, `runtime`, `binary`, `server`, `database`),
returned **three** lines: `install` inside the draft banner, which step 2 deletes; `file` in *this
file adds the six things*; and `Test` as a column heading meaning the test for a severity level. The
second, for `source`, `version`, `merge`, `patch`, `render*`, `system`, `dataset`, `data`,
`artefact`, `module`, `package` and `release*`, returned `release` throughout — the document's
subject — and `dataset`, `live system` and `rendered artefact` as the worked examples of what the
instrument-only grade covers, which are things that cannot be read whole rather than assumptions
that the project is software. Nothing was changed for R-9. `file` was considered and kept:
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) says *this document* where this says *this
file*, which is an inconsistency of self-reference and not an assumption about code, and no
criterion asks for it.

**Step 1, restatement.** Read clause by clause against
[`audit`](../plugin/skills/taskmd/docs/method/audit.md) and
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5. One copy found and repaired; one near-miss
found and kept. Both are in *Decisions* above with the test that separated them. The two declared
deviations — Low-batching, and the findings moving out of the umbrella — each quote the step they
override and say why, which is what the criterion asks of a deviation.

**Steps 2 and 3, by diff.** `git diff --cached 134e077^` over the deliverable prints one hunk: the
*When one runs* paragraph, six lines replacing four. `git diff 134e077^` over
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) and
[`audit`](../plugin/skills/taskmd/docs/method/audit.md) prints **nothing at all**. No commit has
touched either since `134e077`, so an empty diff against its parent means the restoration is exact,
and the constraint *no rule in either is changed* holds mechanically rather than by inspection.

**Step 4, by following the pointers in an install-shaped copy.** `plugin/skills/taskmd/` was copied
alone into a scratch directory — what an adopter receives, per T-083 — and every link matching
`pre-release-audit.md` was resolved from its own file's directory and the target opened:

```text
docs/METHOD.md         link method/pre-release-audit.md  -> RESOLVES | opens: # pre-release audit
docs/METHOD.md         link method/pre-release-audit.md  -> RESOLVES | opens: # pre-release audit
docs/method/audit.md   link pre-release-audit.md         -> RESOLVES | opens: # pre-release audit
```

Two rows for `METHOD.md` because the §5 clause and the §7 row are separate links. The document is
reached, not merely listed, and it is reached from the subtree an install copies.

**Step 4, negative control.** The silence above proves nothing until the instrument is shown able to
speak, so the §7 row's target was changed to `pre-release-audit-XX.md` on purpose:

```text
check exit = 1
BROKEN LINK   plugin/skills/taskmd/docs/METHOD.md -> method/pre-release-audit-XX.md
```

Restored from a copy taken before the break — not with `git checkout --`, which restores to `HEAD`,
and `HEAD` is the version carrying no pointers at all. `git diff 134e077^` was empty again after.

**Step 5, and the finding it produced.** The first properly-measured `check` after the move exited
**1**, not 0, with three `BROKEN LINK` lines — all of them this record's own links to the draft it
had just deleted. Repaired as *Decisions* describes. After the repair:

```text
check exit = 0
OK - 234 task(s), ... 267 document(s), 3705 link(s), ...
python -m pytest tests/ -q                ->  337 passed, 8 subtests passed
python -m pytest tests/test_budget.py -q  ->  8 passed
git diff HEAD --stat -- CLAUDE.md plugin/skills/taskmd/SKILL.md  ->  (empty)
```

The suite's 337 is the figure taken before planning, so the work moved nothing. Tier 1 is untouched
by file, and `test_budget.py` passes with its bound unedited.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Tells a session how to *run* an audit of everything, and never what to *find* in one | met | The document decides shape and never subject: grade the subject, choose aspects, order the cycles, what each severity obliges. It names no finding class, and §1 sends the aspects to the audit's own plan rather than carrying a set. The illustration is labelled as shape, not as a list to adopt |
| Reads sensibly for a non-software project, shown by a worked example that is not software | met | The worked example is a training course before its first cohort, carried through five cycles including a grade for material that cannot be read. Both R-9 sweeps in §3 returned nothing that assumes code, tests, compilers or version control |
| Restates no rule [`audit`](../plugin/skills/taskmd/docs/method/audit.md) or [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) already owns; declared deviations say so and say why | met | One copy was found and repaired in `implement`, not here — *Requested, never automatic* was [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5's rule stated whole. The two deviations each quote the step they override and give the reason. The one near-miss that was kept is argued in §3 rather than left for a reader to notice |
| The three edits *Scope* names are present and resolve, each checked by following it | met | All three resolved and opened `# pre-release audit` — from a copy of `plugin/skills/taskmd/` alone, which is what an install receives. The table is in §3 |
| No rule in either document is changed: the diff touches only the row, the clause and the pointer | met | Stronger than the criterion asks: `git diff 134e077^` over both files is **empty**. No commit has touched either since, so the restoration is exact and nothing needs judging by eye |
| Tier 1 is unchanged; `tests/test_budget.py` passes without editing the bound | met | `git diff HEAD --stat` over `CLAUDE.md` and `SKILL.md` is empty; `test_budget.py` reports 8 passed, bound unedited. The deliverable is tier 3 and the two edits are tier 2 |
| `taskmd check` passes | met | `check exit = 0`, measured by redirect. The first properly-measured run exited **1** on three broken links this task's own record had created; §3 carries both the failure and the repair |
| Reachability is verified by running, not by reading the §7 table | met | Followed, not read — and the instrument was shown able to fail first: breaking the §7 target produced `check exit = 1` and a named `BROKEN LINK`, restored afterwards from a copy taken before the break |

**Child fix tasks raised**
- none — every criterion met, so nothing is carried and nothing holds this task open.

**Open questions, re-read before closing** ([`review`](../plugin/skills/taskmd/docs/method/review.md)
step 5). All four in §1 are struck through and answered by the owner on 2026-08-22; none was
re-opened by the work. One residual was considered and needs no task: `htmldeck`'s
`docs/AUDIT-METHOD.md` says the document *"arrives with a taskmd release"*, which is still true —
the deliverable exists here but is not released, and [T-231](T-231-cut-the-next-release.md) is the
release. That sentence describes its own trigger, so it neither goes stale nor waits on anybody
here, and a cross-repository item is not this project's task machinery to hold.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | review → done | **`review` closed the task: eight criteria, eight met, nothing carried and no child raised.** The two criteria added at `specify` both did work — the pointer one is what a review of the old list would have skipped, and the no-rule-changed one turned out to be answerable by an **empty** `git diff 134e077^`, which is a stronger result than the criterion asked for. **Nothing was repaired here.** The one restatement and the three broken links were both found and fixed in `implement`, and this phase reports them; `review` that repairs what it finds destroys the record of what was wrong. **Step 5 ran and found one residual that needs no task**: `htmldeck`'s `docs/AUDIT-METHOD.md` waits on a *release*, not on this record, so it describes its own trigger — written into §4 rather than left as a thing a later reader has to re-derive. |
| 2026-08-23 | planned → review | **`implement` ran the five planned steps and produced the deliverable at its declared path.** Two things are worth reading before the evidence. **The method of step 2 changed and its order did not**: the file was recovered from `134e077^` rather than moved back from `docs/` and un-rewritten, so the deliverable is provably the agreed content plus one deliberate paragraph. **And step 5 produced a finding rather than a green tick** — the first properly-measured `check` exited **1**, on three links this record itself pointed at the draft it had just deleted. They were **de-linked rather than repointed or reworded**, because a Markdown link is a live pointer and a backticked path is not (T-092), which keeps two dated Log rows saying exactly what they said. **The reason it was nearly missed is now a rule**: piping `check` into `tail` and echoing `$?` reports `tail`'s status, which is 0 whatever happened, so every exit code in §3 is taken from a redirect instead. |
| 2026-08-23 | specified → planned | **`plan` written under the unattended grant.** Five steps, each naming an output somebody else could go and look for. **The plan's one real decision is that the two content checks run before the move**, so step 2 stays a rename and a reader can see that the content the owner agreed on 2026-08-22 is the content that shipped; the rejected ordering is in §2 with its cost. **The second decision makes an acceptance criterion mechanical**: the three pointers are restored by reverting the hunks of `134e077`, not re-composed, and `git diff 134e077^` over the two documents is then expected to be **empty** — no commit has touched either since, which was checked with a path-filtered log before the plan relied on it. **Nothing here restates a criterion**; the criteria stay in §1 and are judged in `review`. The suite was run before planning around it rather than after: `python -m pytest tests/ -q` reports `337 passed, 8 subtests passed`, so step 5 has a baseline to be compared against rather than a first-ever run. |
| 2026-08-22 | proposed → specified | **`specify` closed under the unattended grant.** All four questions in §1 are struck through and answered by the owner the same day, so nothing here waits on an answer and the grant's *it authorises phases, not answers* does not bite. **Two acceptance criteria were added, and they are the only change to what this task must produce.** *Scope* already named three edits as in — the [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §7 row, its §5 clause, and the pointer from [`audit`](../plugin/skills/taskmd/docs/method/audit.md) — and the criteria judged none of them: the closest asked that reachability be verified by running, which reaches the §7 row and neither of the other two. The owner's decision of the same day is what made that a live gap rather than a pedantic one, because it **removed all three**, so `implement` restores them and a review reading the old list would have passed a document nothing points at. A criterion that makes an already-in-scope item judgeable is `specify` doing its job; **widening the scope would have needed the owner and was not done.** The second added criterion holds *Scope*'s own sentence — *no rule in either is changed* — to a diff, for the same reason: it was a constraint nothing would have checked. **Verified before writing this**, rather than read off the rows below: `docs/pre-release-audit-draft.md` is present, and a tree-wide search for `pre-release-audit` across `plugin/`, `docs/` and `CLAUDE.md` returns nothing outside the draft itself — so the three pointers are absent and `implement` has them to restore. |
| 2026-08-22 | (no change) | **The grant was extended a third time**, to [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md), scoped there to finishing that record and not to building what it decides. The rows below are what the grant covered when each was written and are left as written; **T-234's own row carries the membership as it now stands**. Nothing about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **`business_value` medium → high**, on the owner's statement of 2026-08-22 that a release is wanted soon and an audit precedes it. This record ships the method that audit is run by, so it now gates both. **Written as the field rather than as an instruction in a handoff**, because `list` orders on this field and prose orders nothing — with it at `medium` the tool sorted this record seventh of eight while it was in fact first, and the only place that fact could have lived was a sentence no view reads. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task:** all three of its questions were answered on 2026-08-22 and are struck through in §1 — the name, the scale exception and the Low-batching placement. The grant does not re-open them. The draft is at `docs/pre-release-audit-draft.md` and the three pointers that named it were removed, so `implement` is what puts the document at its declared deliverable path and restores those pointers. **This record is the one the audit waits on**, which is why its value moved to `high` the same day. |
| 2026-08-22 | (no change) | **All three questions answered by the owner, and a fourth thing decided that nobody had asked.** Put as a survey with each option priced both ways. **The name stays `pre-release audit`** — findability beats accuracy for a document nobody searches for by size, and three documents plus `htmldeck` already name that path. *Rejected: `audit at scale`*, accurate and describes when to load it, at the cost of a path four places follow and a word nobody preparing a release would search for. *Rejected: keep the name and widen the §7 row*, which changes no path but leaves the row and the file name saying different things. **The scale exception is accepted as written** — bounded by three conditions, declared as a deviation, and aimed at a real failure: an umbrella carrying sixty findings is not a task record. *Rejected: findings always stay in the umbrella*, one rule and no exception, obeyed and useless at that size. *Rejected: fold it into `audit`*, which ends the override at the cost of every ordinary audit reading a paragraph about a size it will not reach. **Low-batching is a scale rule and stays here** — one task per finding is right and cheap at ordinary size. *Rejected: move it to `audit` as a correction at every scale*, untested small, and batching three findings hides two from every view. *Rejected: leave it and add a pointer in `audit`*, which stops step 4 misleading anyone at the cost of a pointer every audit pays for. **Fourth, and it went against the recommendation:** the draft was moved out of `plugin/` rather than left there now that its content is agreed. It is `docs/pre-release-audit-draft.md`, its own links rewritten for that location, and the three pointers in `METHOD.md` §5, §7 and [`audit`](../plugin/skills/taskmd/docs/method/audit.md) removed with it — leaving them would have pointed shipped documents at a file no install receives, which `check` cannot see. *Recommended and rejected: leave it in place*, on the ground that agreed content is no longer a risk; the owner's choice separates **content agreed** from **deliverable produced**, which is what the lifecycle is for and what this record could not say while the file sat at its own output address. **`check` now reads the draft where it is**, proven by breaking one of its links and watching `BROKEN LINK docs/pre-release-audit-draft.md` fire, then restoring it. |
| 2026-08-22 | (no change) | **Reviewed at the owner's request, who was unsure the task had landed as it should.** Phase unchanged: this is an input to `specify`, not `specify` being done for them. **What verified clean.** The generic/local split is real and both sides state it rather than duplicate — `htmldeck`'s `docs/AUDIT-METHOD.md` opens *"The method is not here"* and points at the three taskmd documents, and its register defers §5's grading rule to this one by name. **R-9 holds**: a sweep for software vocabulary over the whole document returns `source` (as in *source of findings*), `file` (as in *this file*) and `Test` (a table heading), and the worked example is a training course. **§5's figures are sourced and were re-checked today** against the adopting project's own records — *two of thirteen held as written*, *every error was in the remedy and none in the observation*, *four rows were refused by a measurement taken while implementing them* — all three verbatim in `htmldeck`'s `docs/lessons/L-90.md` and `docs/CONTEXT-AUDIT.md`. `check` and the suite are green and tier 1 is unchanged. **What did not land: the draft is at the deliverable's address inside `plugin/`.** §1 above now carries that and what follows from it. **Two of the three open questions get more expensive after a release, not less** — the name is a path that `METHOD.md`, `audit.md` and a downstream document would all have to follow, and the scale exception is a published deviation from a published rule. **Nothing was raised from this review**: every finding is an input to this record's own `specify`, and routing them elsewhere would scatter one task's inputs. |
| 2026-08-22 | → proposed | Raised from an adopting project that needed the method and found it was not shipped. A draft is in this branch at the deliverable path, as the input to `specify`. |
