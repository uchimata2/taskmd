---
id: T-189
title: Say whether the audit's method finding reached the repository that owns it
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-170, T-152]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: []
---

# T-189 — Say whether the audit's method finding reached the repository that owns it

## 1. Specify

**Outcome**
A decision on whether finding **E-08** of the context-economy audit was delivered to the repository
that owns the audit method, and [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)
§3's disposition of it corrected to say whichever it is. Second: a statement of whether *published,
therefore handed over* is a class worth checking for, now that two members of it are known.

**Why this one**
Found by [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) widening
its own sweep. T-170 corrected the U-01/U-02 disposition, whose false clause was *they stay in the
deliverable, which is the handover*. Its first sweep filtered on the ids it was about and found nine
hits; dropping the filter found a tenth, four rows above the one it had just fixed:

> **E-08** — Screen a figure on its source and on where the effect concentrates. A rule for the
> audit **method**, which is another repository's. Carried in the portable deliverable, which is the
> handover.

Same sentence, different recipient, and no evidence that anybody received it either.

**This one has a recipient, which is what makes it a different question from T-170's.** T-170 was
answered *no route exists* because the harness is not something this project can reach. The audit
method belongs to a sibling repository, and that sibling is **cloned beside this one on the owner's
machine** — so a route not only exists, the owner's own standing rule says what it is: a defect one
of these repositories finds in another arrives as a branch with a failing test, not as a report.
A finding about the method is not a defect in code, so whether that rule reaches it is exactly the
question.

**Scope**
- In: the decision, and the correction to T-152 §3's E-08 disposition
- In: naming the recipient and the route, if the answer is that it should be sent
- In: whether *published, therefore handed over* is worth a rule, or whether two instances is two
  instances
- Out: re-opening E-08 itself, its severity or its band. It is a finding about another repository's
  method and this task does not judge it
- Out: writing anything into the dated audit deliverables, for the reason
  [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) §1 gives

**Inputs**
- [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 — the disposition
  table, rows E-08 and U-01/U-02
- [`docs/audits/2026-08-15-context-economy-portable.md`](../docs/audits/2026-08-15-context-economy-portable.md) — E-08 in full
- [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) §3 — the sweep,
  and what its filter cost

**Acceptance criteria**
- [ ] The decision is recorded, with the rejected option named
- [ ] T-152 §3's E-08 disposition says what was actually done, and what it said before stays legible
- [ ] **The tree is swept for the claim as a phrase, not as an id**, and the count is stated. Two
      instances are known; the sweep says whether there are more
- [ ] The ruling says whether the class is worth a check, and if it says no, why two instances is
      not evidence of one
- [ ] The dated audit deliverables are unchanged, shown rather than asserted

**Open questions**
- ~~**Should the finding be sent, given that a route exists?**~~ **Answered 2026-08-19: nothing is
  sent, because the rule is already in the repository that owns the method.** The owner made the
  branch **conditional** on there being no evidence of arrival, and asked for that repository to be
  read before anything was written. It was, and the evidence is there: its `references/measure.md`
  carries the rule under a heading of its own — *Screen on the source of every figure* — closing
  with *where an effect concentrates decides more screenings than its size*, which is E-08's second
  half in the method's own words, and it carries the same independently-benchmarked example E-08 was
  drawn from.

  **What the evidence does not show is the route.** Every commit in that repository carries this
  audit's own date, so a content match cannot say which way the rule travelled, or whether anything
  travelled at all. **So the disposition is corrected on its outcome and not on its reasoning**:
  *carried in the portable deliverable, which is the handover* stays false as a reason — it was
  false for U-01/U-02 for exactly this reason — while the thing it was used to excuse turns out to
  have happened anyway. A row can be right in outcome and wrong as a justification, and only the
  justification generalises.

  **The second half of §1's outcome is untouched by this**, and is now the more interesting question
  rather than the less: whether *published, therefore handed over* is a class worth checking for,
  given that this member of it came out right without anybody being able to show why.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the repository that owns the audit method for the rule itself, before writing anything — the owner made the branch conditional on finding no evidence of arrival | the finding, in §3 |
| 2 | Sweep every document a clone receives for the claim **as a phrase**, not as an id, and say what was read and with which pattern | the count and its scope, in §3 |
| 3 | Extend the sweep to the homes `git ls-files` cannot see, since one of them is where the adopter roster lives | in §3 |
| 4 | Correct T-152 §3's E-08 disposition, leaving the old wording legible, in the form T-170 used four rows below | `tasks/T-152-audit-what-this-repository-costs-a-session-on-every-turn.md` |
| 5 | Rule on whether *published, therefore handed over* is worth a check, from what step 2 counted rather than from the two instances already known | the ruling, in §3 |
| 6 | Show the dated audit deliverables unchanged rather than assert it | `git status` output, in §3 |

## 3. Implement

**Decisions & assumptions**
- **Nothing is sent** — 2026-08-19, the owner's answer made conditional and the condition read.
  *Rejected: opening a branch on the owning repository*, which was the owner's first preference and
  is the standing cross-repository rule; it is refused here only because the rule is already there,
  not because a method finding falls outside that rule. That question is left unanswered because
  this case no longer poses it.
- **The evidence is content, and the route is not shown** — 2026-08-19. That repository's
  `references/measure.md` carries the rule under a heading of its own, closing on the clause that is
  E-08's second half, and it carries the same independently-benchmarked example the finding was
  drawn from. **Every commit in that repository carries this audit's own date**, so a content match
  cannot say which way the rule travelled, or whether it travelled. Recorded as *the rule is there*
  rather than as *the finding arrived*, because only the first is observed.
- **No check** — 2026-08-19, ruled from the sweep below rather than from the two instances already
  known. Three reasons, in the order they bind. **Two instances are one event**: both sit in one
  table, in one task, written by one session on one day, in one sentence pattern — independent
  recurrence is what makes a class, and this is a habit applied twice in a sitting. **No checker
  here can see the property**: whether a person received something is not structure or a reference,
  which is all `check` reads, and a phrase lint would be a checker testing shape where it means
  identity. **And it would be noisy in the ratio that gets a check switched off**: of the sweep's
  11 hits, 2 make the claim and 9 describe it, so a rule keyed on the phrase would be wrong 9 times
  out of 11 on the corpus that motivated it — [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s
  argument, arriving before the check exists rather than after.
- **What generalises is the sweep, not a rule** — 2026-08-19. T-170's lesson already carries it: a
  disposition that asks for nothing still makes a claim, and it is found by sweeping for the phrase
  rather than for the ids the task is about. That is recorded where it was learned and is not
  restated as a second rule here.

**The sweep, and what it read**

Scope: **300 tracked Markdown files** — everything a clone receives — enumerated with `git ls-files`
rather than by a glob, so the membership is derived. Then, separately, the homes `git ls-files`
cannot see by construction: `control/` and `.taskmd/`, which are gitignored and are where the
adopter roster lives.

| Pattern | Hits before the correction | Hits after | Of which **make** the claim, after |
| :--- | :--: | :--: | :--- |
| `(is\|are\|as\|was\|were) the handover` over tracked documents | 11 | 12 | **0.** The 2 in T-152 are now the old wording quoted inside its two corrections; the other 10 are T-170's record and this one, describing the claim in order to correct it |
| the same pattern over `control/` and `.taskmd/` | 0 | 0 | 0 |
| `handed over`, as a wider net | 19 | 20 | 0. The nearest miss is the portable deliverable's own *written to be handed over*, which defines the band and disposes of nothing |

**Both columns are stated because the sweep's own subject moved while it ran.** Correcting a cell
replaces a live claim with a quotation of it, and writing this record adds more quotations — so a
single number would have been true of a tree that no longer exists by the time anyone read it. The
figure that answers the criterion is the **claim** column: two members before, none live after.

**So the class has exactly two members and both are now corrected** — U-01/U-02 by T-170 on
2026-08-19, E-08 here the same day. The sweep says there is no third, and it says so over a scope it
can name.

**The dated audit deliverables are unchanged, shown rather than asserted:**

```text
$ git status --porcelain docs/audits/
$ git log --oneline -1 -- docs/audits/
7da0802 Answer the audit umbrella's open questions where they were asked
```

Empty output from the first, and the last commit to touch them is not this one.

**Outputs produced**
- `tasks/T-152-audit-what-this-repository-costs-a-session-on-every-turn.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded, with the rejected option named | met | §3, first decision. The rejected option is the branch, and why it is refused **here** without being refused in general |
| T-152 §3's E-08 disposition says what was actually done, and what it said before stays legible | met | The cell now says the rule is in the owning repository and that nothing was sent, and carries *Until 2026-08-19 this cell ended …* with the old sentence quoted — the form T-170 used four rows below, so the two corrections read alike |
| **The tree is swept for the claim as a phrase, not as an id**, and the count is stated. Two instances are known; the sweep says whether there are more | met | §3's table. 300 tracked documents plus the two gitignored homes, three patterns, and the claim-versus-description split stated rather than collapsed into a total |
| The ruling says whether the class is worth a check, and if it says no, why two instances is not evidence of one | met | No check, and the three reasons are in §3. The first is the one the criterion asks for: the two instances are one event, not two occurrences |
| The dated audit deliverables are unchanged, shown rather than asserted | met | Empty `git status --porcelain docs/audits/`, and the last commit touching them is another task's. Quoted in §3 |

Five criteria, five met, no child raised.

**One thing worth carrying past this task.** The outcome was right and the reason was wrong, and only
the reason generalises — *carried in the deliverable, which is the handover* was false in both places
it was written, and in this one the thing it excused had happened anyway. A disposition that turns out
lucky is the hardest kind to catch, because nothing downstream ever fails.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | All five criteria met, no child raised. **Authorisation (METHOD §3.1):** the owner's grant of 2026-08-19 to work T-194, T-189, T-148, T-131 and T-181 through their full lifecycle. `specify` needed no new agreement — its question was answered by the owner the same day, conditionally, and reading the condition changed the answer. **Nothing is sent**: the rule is already in the repository that owns the method. The sweep the criteria asked for found **no third instance** across 300 tracked documents and the two gitignored homes, and the 11 hits split 2 making the claim to 9 describing it — which is also the argument against a check keyed on the phrase. Ruled **no check**, for three reasons in §3, the first being that two instances written in one table on one day are one event. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round, conditionally — and the condition changed the answer.** The owner asked for the owning repository to be read for evidence of arrival before any branch was opened. It was read, and the rule is in its `references/measure.md`, with the example E-08 came from. So **no branch is sent.** The route is still unproven, since every commit there carries this audit's own date, so the disposition's *the deliverable is the handover* is corrected as an outcome and left refuted as a reason. **No phase was started** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)); correcting [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3's row is this task's own work, not this round's. |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) raised it. **It does not answer §1's question** — that one asks whether to send something to another repository, which is the owner's to decide and not a phase to run. Under the grant's own instruction, this task therefore ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md)'s review, from widening a sweep that had been filtered by the ids the task was about. `xs` and `low`, like T-170, and for the same reason: the likeliest outcome is a recorded answer and a corrected clause. |
