---
id: T-165
title: Have an uninvolved reader test the post-migration listing
type: fix
status: done
phase: review
parent: T-163
blocked_by: []
related: [T-166]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-165 — Have an uninvolved reader test the post-migration listing

## 1. Specify

**Outcome**
The seventh acceptance criterion of
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) is judged by the test it names —
a reader who was not involved reads the listing and says what would change their decision — rather
than by the structural substitute that ran in its place.

**Why this one**
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) closed with that criterion met
by a weaker test, and the substitution is recorded in its §3 and §4. The weaker test asks whether
every claim in the listing is a measured output or a pointer; the specified test asks whether a
reader can *act* on them. **The second can fail while the first passes** — a document can be entirely
factual and still leave someone unable to say what would move them, which is the failure the criterion
was written to catch.

The reason it was not run is recorded and is not a judgement about the test: no uninvolved reader was
available in the session, and spawning an agent to be one had not been asked for.

**Scope**
- In: the reader test, on the listing as it stands.
- In: what the test finds, recorded whether or not it agrees with the structural check.
- Out: rewriting the listing. If the test fails, that is a finding and its repair is its own task —
  a fix made in the same breath as the measurement leaves no evidence the measurement happened.

**Inputs**
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — *What taskmd still gives you here*, the document under test
- [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 step 6 — what ran instead,
  and why it is weaker

**Acceptance criteria**
- [ ] The reader was given **the listing and nothing else** — no task records, no repository, no
      knowledge that neutrality is what is being tested
- [ ] The reader was asked both halves the criterion contains: **what would change their decision**,
      and **whether the document argues for an answer**
- [ ] The answer is recorded **whether or not it agrees** with the structural check
      [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) ran in its place
- [ ] The listing is **not edited** by this task
- [ ] Where the reader disagrees, the disagreement leaves this task as its own item rather than as a
      note

**Open questions**
- **Who is the uninvolved reader? A subagent, given the document and nothing else. Answered by the
  maintainer, 2026-08-17**, when asked — the agent could not be spawned otherwise. Recorded as a
  **proxy for a person and not the thing itself**: it reads without the session's context, which is
  the property the criterion needs, and it is not a member of the team whose decision this is.
  *Rejected: the maintainer reads it* — they authorised and reviewed the work, so *uninvolved* is
  the one thing they are not. *Rejected: skip it* — that leaves
  [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md)'s criterion carried forever.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Extract the listing to a standalone file, so the reader cannot reach the task records or the repository around it | The document under test |
| 2 | Put the reader in the position the listing is written for — a team that has just migrated, deciding whether to keep the tool — and ask both halves plus an invitation to call it a pitch | The four questions |
| 3 | Record the answer verbatim enough to be re-read, including the parts that disagree with us | The finding, in §3 |
| 4 | Judge [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md)'s seventh criterion on it, and route any disagreement to its own task | The judgement, and one task or none |

**Decisions taken at `plan`**

- **The reader is asked to be blunt and offered "sales pitch" as an available answer** — 2026-08-17.
  A neutrality test that only asks *can you decide?* gets a polite yes. Naming the failure mode in
  the question is what makes a negative answer cheap to give. *Rejected: asking only the criterion's
  own wording*, which tests the half that was never in doubt.
- **The reader is not told the document is under test for neutrality** — 2026-08-17. It is put in the
  position of someone making the decision, because that is the reader the listing claims to serve.

**Outputs this task will produce**

- the finding, in §3 of this record

## 3. Implement

**Run 2026-08-17.** The listing was extracted to a standalone file — 3,771 characters, the section
whole and nothing around it — and a reader was given that path, told to read nothing else, and put in
the position of advising a team that had just migrated. Four questions: what pushes toward keeping,
what pushes toward uninstalling, what missing fact would most change the recommendation, and whether
the document argues for an answer.

**The first half of the criterion passes cleanly.** The reader named what would change their
decision, specifically and without prompting: whether the binding's six operations have ever been
**run** against a real repository, with dated output. Runner-up, and they said to check it first
because it is binary: whether the harness already serves another task-management skill.

**The second half does not.** Asked whether the document argues for an answer, the reader said **yes,
mildly, toward keep** — and gave three mechanisms rather than an impression:

1. **The *What is gone* section argues against the migration, in a document about the tool.** All
   three losses — no validator, no ordering rule, no offline copy — are things that **keeping taskmd
   cannot restore**, because the commands exit 2 either way. Their placement leaves the reader
   feeling a loss the surviving product is adjacent to.
2. **The heading *What survives, and it is the part that was never local*** reframes losing the whole
   executable surface as incidental — "as though the commands were never the point. They were enough
   of the point to have their own table."
3. **The disclaimer buys trust.** Naming the conflict of interest is "the cheapest way to be
   believed", and here it is doing persuasive work. The reader called it partly performative modesty.

They also observed that the closing paragraph converts *should taskmd go?* into *which of the two
should go?* and then legitimises keeping both — "a menu where two of three outcomes leave taskmd
installed."

**The structural check was wrong, and it was wrong in the way a structural check is always wrong.**
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 verified that every claim is
a measured output or a pointer, and every claim is. **Framing is not a claim.** Selection, ordering,
headings and what a true sentence is placed next to are all invisible to a test that walks assertions
one at a time — so the substitute passed a document the specified test marks down, which is exactly
the gap the criterion existed to cover.

**What the reader got wrong, and it does not soften the finding.** Their central missing fact — has
the binding actually been run — had been answered the same day by
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md), which drove
`create` 165 times, `update` 165 times, `enumerate`, `read` and the edge operations against a real
repository. The reader could not know that, because **the listing does not say so**. That is not a
defect in the reader; it is the finding restated from the other side: the document proves its
failures with dated output and asserts its survivors.

**The listing was not edited.** `specify` put that out of scope, and the repair is
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md).

**Decisions & assumptions**
- **The reader's verdict is recorded as the result, not weighed against ours** — 2026-08-17. We
  built the test to be able to fail and it failed; re-arguing it here would make the measurement
  decorative. Where they were factually wrong, that is recorded as evidence *for* the finding.

**Outputs produced**
- the finding above

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The reader got the listing and nothing else | met | 3,771 characters extracted to a standalone file, told to read nothing else, given no repository path and no task record |
| Both halves asked, with the failure mode named as an available answer | met | Four questions; the fourth invited "sales pitch" and "false modesty" explicitly, which is what made the negative answer cheap to give |
| The answer recorded whether or not it agrees with us | met | It does not agree, and §3 carries it including the parts that are unflattering |
| The listing not edited by this task | met | Untouched. The repair is [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) |
| Disagreement leaves as its own item | met | [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md), raised with the three mechanisms |

**And the verdict on the criterion this task exists to serve.**
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md)'s seventh criterion — *an
uninvolved reader can say what would change their decision, which is the test that it states facts
rather than issuing a verdict* — **splits**. The reader could say what would change their decision,
precisely. The document does not state facts rather than issuing a verdict: it argues mildly toward
keep, by arrangement rather than by assertion. T-163's §4 already recorded the criterion as
**carried** rather than met, so nothing there needs correcting — the carry is now discharged into a
judgement, and the judgement is *not met*, held by
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md).

**The cost of the substitute is now measurable, which is the point of having run this at all.** The
structural check passed a document the specified test marks down. It was not a weaker version of the
same test; it was a different test that cannot see the defect, because framing is not a claim.

**Child fix tasks raised**
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) — the listing leans toward
  keeping taskmd, and its survivors are asserted where its failures are proven.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → done | Full lifecycle in one request, under the maintainer's authorisation of the same day covering this task and [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) **and nothing else** — recorded here as well as there because an authorisation kept in one place is one a later session reading the other can miss (METHOD §3.1). The instrument was a subagent, approved when asked, and is recorded as a **proxy for a person** rather than the thing the criterion means. **The test did what it was built to do: it failed.** The reader named what would change their decision — whether the binding's operations have ever been run — but answered *yes, mildly toward keep* on whether the document argues a case, with three mechanisms: the *what is gone* section arguing against the migration rather than about the tool, a heading that reframes losing the whole executable surface as incidental, and a conflict-of-interest disclaimer doing persuasive work. **The structural substitute [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) ran was not a weaker version of this test but a different one**, and it cannot see the defect: every claim really is measured or a pointer, and framing is not a claim. Their decisive missing fact had in fact been answered by [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) hours earlier — which is the finding from the other side, since the listing never says so. Repair is [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md); the listing was deliberately not touched here. |
| 2026-08-17 | → proposed | Raised as the child of [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) that carries its seventh criterion, under METHOD §2 — a criterion is met, or it carries a child task that will meet it. T-163 met it with a structural check of the same property from the other side and **recorded the substitution rather than claiming the criterion**, which is why this task exists and is small. `xs`: one reading and one recorded answer. **Not covered by the lifecycle authorisation of 2026-08-17**, which named T-108 and T-163 and excluded whatever they raise. |
