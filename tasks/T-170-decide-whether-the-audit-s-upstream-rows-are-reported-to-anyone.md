---
id: T-170
title: Decide whether the audit's upstream rows are reported to anyone
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-152]
work_package: M6
owner: maintainer
business_value: low
effort: xs
created: 2026-08-17
updated: 2026-08-19
deliverables: []
---

# T-170 — Decide whether the audit's upstream rows are reported to anyone

## 1. Specify

**Outcome**
A decision on what *handed over* means for the two upstream rows of the context-economy audit, U-01
and U-02 — either they are actually sent to whoever owns the harness, or being written in the
deliverable **is** the whole of the handover — and the disposition wording in
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 corrected to say
whichever it is.

**Why this one**
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) dispositions both rows as
*no task, and nothing implemented locally — they stay in the deliverable, which is the handover*. The
session of 2026-08-17 flagged that as a residual aimed at the maintainer: **it is a claim about where
the rows live, not about anyone having received them.** The audit's own scope says the reader should
be able to tell which costs belong to the harness, and a row nobody has sent is a cost still sitting
here. T-152 closed the same day, and **a question left inside a closed record leaves every view the
project has** — which is why it is a task rather than a sentence there.

**It may be a one-line close, and that is a fine outcome.** If the maintainer's position is that
publishing the observation is the handover this project intends, the decision is recorded, the wording
in T-152 §3 is corrected from *the handover* to what it actually is, and this closes. The cost of
raising it is one record; the cost of not raising it was losing it.

**Scope**
- In: the decision, and the correction to T-152 §3's disposition wording so the record says what was
  actually done
- In: naming the recipient, if the answer is that they are sent
- Out: re-opening the audit's findings or its bands. U-01 and U-02 are observations about the harness
  that assert no failure, and neither is a finding
- Out: writing anything into the two audit deliverables. They are a dated examination record, and
  correcting them would destroy what a dated record is for — the same reason
  [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md) left the step-11 table alone

**Inputs**
- [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 — the upstream
  disposition table and the residual flagged against it
- [`docs/audits/2026-08-15-context-economy-portable.md`](../docs/audits/2026-08-15-context-economy-portable.md) — where U-01 and U-02 are stated in full

**Acceptance criteria**
- [ ] The decision is recorded here, with the rejected option named
- [ ] The disposition in [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)
      §3 no longer asserts a handover that did not happen
- [ ] **What that cell said before is still legible**, rather than replaced silently. METHOD §5
      forbids rewriting what a record says about the past, and a disposition is a record of a
      decision taken on a date
- [ ] The two dated audit deliverables are unchanged, and that is shown rather than asserted
- [ ] **Nothing else in the tree still claims the two rows were handed to anyone.** Checked by
      searching, with what was searched and what it returned stated — a correction applied to the
      one place somebody remembered is the shape this task exists to catch

**Open questions**
- ~~**Is there a recipient at all?** Both rows are about the harness, which this project does not
  own and has no channel to. If the answer is that no route exists, that is the decision and the
  wording changes to say so. **The maintainer answers, at `specify`.**~~ **Answered by the owner on
  2026-08-19: no route exists, so the wording changes** — see the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Sweep the tree for every statement that the two rows were handed over, so the correction reaches the set rather than the remembered one | The search, its command and its hits, in §3 |
| 2 | Separate the hits into claims about the **present** and records of the **past**, because METHOD §5 treats them oppositely | The split, in §3 |
| 3 | Correct the present-tense claim, carrying what it said before | The edited cell in T-152 §3 |
| 4 | Show the two audit deliverables unchanged | `git status` over `docs/audits/`, in §3 |
| 5 | Re-run the sweep and `check` | The output, in §3 |

**Decisions taken at `plan`**

- **The correction carries the superseded sentence inside the cell, rather than replacing it.** The
  owner's answer says *corrected*, and METHOD §5 says never rewrite what a record says about the
  past. A disposition is both: it states what the audit decided about U-01 and U-02, which stands,
  and it claimed that decision amounted to a handover, which was never true. Keeping the old clause
  quoted and dated satisfies both readings and costs one sentence. *Rejected: replacing the clause
  outright*, which is what the answer literally licenses and would leave every later reader unable to
  tell that the row had ever said anything else — and this task exists because a claim nobody could
  see was wrong survived four days. — 2026-08-19
- **Only the present-tense claim is touched.** T-152's §4 residual paragraph and its two 2026-08-17
  log rows describe the residual *as it stood then*, and are correct as history. — 2026-08-19

**Outputs this task will produce**

- tasks/T-152-audit-what-this-repository-costs-a-session-on-every-turn.md

## 3. Implement

### Step 1 — the sweep, as it was actually run

```text
grep -rn "handed over|handover|hand over" --include=*.md tasks/ docs/ control/ CLAUDE.md README.md plugin/
  | grep -i "u-01|u-02|upstream"
```

Nine hits, in three files. `control/LOCAL-CONTEXT.md`'s is about an adopter report and not about
these rows at all; T-170's four are this task describing the problem.

### Step 2 — present against past

| Hit | Kind | Action |
| :--- | :--- | :--- |
| T-152 §3, the U-01/U-02 disposition cell | a claim about **now** | corrected |
| T-152 §4, *U-01 and U-02 are dispositioned as handed over by being in the deliverable* | a record of the residual as it stood on 2026-08-17, and the sentence that raised this task | left exactly as written |
| T-152 Log, two rows of 2026-08-17 | records of what was known that day | left exactly as written |
| T-170 §1, four mentions | this task stating the problem | left as written |
| `control/LOCAL-CONTEXT.md` | an adopter report handed over by a maintainer, a different sense of the word | not a hit for this |

**One claim about the present, four records of the past, one false positive.** That split is the
whole of the work, and it is why step 1 came before step 3: a find-and-replace over the same nine
lines would have destroyed the paragraph that raised this task.

**The table above is complete for the sweep that produced it and not for the tree** — step 5 says
what the filter cost.

### Step 3 — the correction

The cell now reads *they are published in the deliverable and were sent to nobody, because this
project has no route to whoever owns the harness*, and carries the superseded clause in place, dated,
with this task named as what established it.

### Step 4 — the deliverables

```text
git status --short docs/audits/
(no output)
```

Nothing under `docs/audits/` is modified, which is what §1's second *Out* required.

### Step 5 — re-run, and the thing the first sweep could not see

The re-run dropped the id filter, and that is what found the sibling:

```text
grep -rn "is the handover|are the handover|as the handover" --include=*.md .
./tasks/T-152-...md:132: ... which is the handover. |
```

**Step 1's sweep was narrowed by `grep -i "u-01|u-02|upstream"`, and the narrowing hid a second live
instance of the same claim in the same table.** T-152 §3 row **E-08** disposes of an audit-method
finding as *carried in the portable deliverable, which is the handover* — the identical sentence,
about a different recipient, and no more sent than U-01 and U-02 were. A sweep filtered by the ids
this task names could not have seen it, because the defect is a **phrase**, not an id.

It is **out of scope here** and raised rather than fixed: §1's second *Out* excludes the audit's
findings, and E-08 is one. Raised as
[T-189](T-189-say-whether-the-audit-s-method-finding-reached-the-repository-that-owns-it.md), which
also carries the wider question this row makes visible — a claim of the form *published, therefore
handed over* is a class, and this task met two members of it while looking for one.

Nothing else in the tree claims that **U-01 and U-02** were sent to anyone, which is what this
task's criterion asks.

**Decisions & assumptions**

- **Recorded: the two upstream rows were never sent to anyone, and this project has no route to
  send them.** The audit's handover consisted of publishing them. *Rejected: naming a recipient and
  delivering the two rows*, which the owner rejected on 2026-08-19: it would make the original
  sentence literally true at the price of committing this project to a reporting channel it has never
  used and would then have to keep. — 2026-08-19
- Both `plan` decisions held. — 2026-08-19

**Outputs produced**
- tasks/T-152-audit-what-this-repository-costs-a-session-on-every-turn.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded here, with the rejected option named | **met** | §3 *Decisions*: no route exists, so nothing was sent. Rejected: naming a recipient and delivering the rows |
| T-152 §3 no longer asserts a handover that did not happen | **met** | §3 step 3. The cell now says what was done, which is that the rows were published and sent to nobody |
| What the cell said before is still legible | **met** | The superseded clause is quoted inside the cell, dated, and attributed to this task. §2 records why the literal reading of the owner's answer was not taken |
| The two dated audit deliverables are unchanged, shown rather than asserted | **met** | §3 step 4: `git status --short docs/audits/` returns nothing |
| Nothing else in the tree still claims the rows were handed to anyone | **met** | §3 steps 1, 2 and 5, and met on the second sweep rather than the first. The id-filtered sweep found nine hits; the unfiltered one found a tenth, which is not about these rows and is [T-189](T-189-say-whether-the-audit-s-method-finding-reached-the-repository-that-owns-it.md) |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner on 2026-08-19 and is struck through there. Nothing
remains addressed to anyone else. **The residual this task was raised to carry is now spent**, which
is the outcome §1 called a fine one.

**One finding, outside this task's criteria and raised rather than fixed.** The criterion above
is about U-01 and U-02 and is met. What the widened sweep exposed is that the *claim* is a class
rather than an instance: T-152 §3 disposes of finding **E-08** with the same sentence, about a
different recipient. Not corrected here, because §1 puts the audit's findings out of scope and
because the interesting half is the class.

**Child fix tasks raised**
- [T-189](T-189-say-whether-the-audit-s-method-finding-reached-the-repository-that-owns-it.md) — the same claim, about the audit method's own repository

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 2 of the eight. **Recorded: the two upstream rows were sent to nobody, and no route exists to send them** — the audit's handover was publishing them. The work was almost entirely the sweep rather than the edit: nine statements mention the handover, and exactly **one** is a claim about the present. The other four in T-152 are records of what was known on 2026-08-17, including the paragraph that raised this task, and a find-and-replace would have destroyed it — which is why the plan put the sweep before the correction. The corrected cell carries its superseded clause quoted and dated rather than replacing it, because METHOD §5 forbids rewriting what a record says about the past and a disposition says both things at once. `docs/audits/` is untouched, shown with `git status` rather than asserted. **The sweep found a tenth hit only once its id filter came off**: T-152 §3 disposes of finding E-08 with the same sentence about a different recipient, so *published, therefore handed over* is a class this task met twice while looking for one instance. Out of scope here and raised as [T-189](T-189-say-whether-the-audit-s-method-finding-reached-the-repository-that-owns-it.md). |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 2 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered by the owner: there is no route, so the wording is what changes.** Asked in the backlog-wide round of 2026-08-19. §1 anticipated this outcome and called it a fine one: the decision is recorded, and [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3's disposition is corrected from *they stay in the deliverable, which is the handover* to what was actually done — an observation published, with no recipient and nothing sent. *Rejected: naming a recipient and delivering the two rows*, which would make the disposition literally true and commits this project to a reporting channel it has never used and would then have to keep. The correction lands in T-152 §3 and nowhere else; the two dated audit deliverables are not touched, for the reason §1 already gives. This row is the answer, not authorisation to start. |
| 2026-08-17 | → proposed | Raised at [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s close, routing a residual that task's own log had flagged the same day as *live and would die silently at close*. **Soft edge, not a child**, and deliberately: a child would re-open the closure rule this task exists because of, and the residual is not a finding needing repair — it is a question about whether a disposition already taken describes what happened. `xs` and `low`, because the likeliest outcome is a recorded answer and a two-word correction. |
