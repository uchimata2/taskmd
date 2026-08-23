---
id: T-174
title: Carry the command that produced T-168's figures into a record that can re-run it
type: fix
status: done
phase: review
parent: T-168
blocked_by: []
related: [T-168]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-18
updated: 2026-08-19
adopter_visible: yes
deliverables: [tasks/T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md]
---

# T-174 — Carry the command that produced T-168's figures into a record that can re-run it

## 1. Specify

**Outcome**
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3's figures —
414 characters, 10 of 11 sessions, the three classes — can be produced again by someone who has only
the record. Today they cannot: the record describes the rule in prose and the scripts that ran it
were left in a scratchpad that does not survive the session.

**Why this one**
**Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s
review, where its criterion 2 failed.** That criterion asked for the cost "with the command that
produced it"; the record gives the figure, the unit and what was counted, and no command.

**The cause is a plan decision that changed at `implement` without being flagged**, which is the thing
[`implement`](../plugin/skills/taskmd/docs/method/implement.md) step 3 forbids. `plan` decided the
script would be "written to the scratchpad and **quoted in §3**, not committed"; §3 records it as
"described here rather than pasted". Quoted and described are not the same promise, and the narrower
one was substituted silently. Worth fixing as a record defect and worth noticing as a habit.

**Committing the script is not obviously the answer** and this task should not assume it is. T-168's
own reasoning still holds: the script reads a machine-private transcript store, and a test under
`tests/` reading it could never run for an adopter. Quoting it inside the record, which is what `plan`
actually decided, may be the whole fix.

**Scope**
- In: making T-168 §3's figures reproducible from the record alone
- In: whether the same gap exists in the other measurements this repository has taken against
  machine-private data, since the constraint that produced it is not unique to T-168
- Out: re-taking the measurement. The figures are not in doubt; their reproducibility is
- Out: changing what `tests/` may read. If the answer argues for that, it is its own task

**Inputs**
- [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §2 and §3 —
  the decision as planned and as carried out, which are the two texts that disagree
- `plugin/skills/taskmd/docs/method/implement.md` step 3 — the rule the substitution broke

**Acceptance criteria**
- [ ] [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3 carries
      the script, quoted, which is what its `plan` decided
- [ ] **The quoted script has been run, and what it printed is recorded beside it.** A script quoted
      and never executed is the same defect one step along: it reads as evidence, so nobody re-checks
      it
- [ ] Every figure §1 names — 414, 10 of 11, the three classes — is produced by that run, or the
      divergence is stated with its cause
- [ ] The script names **no project, no path and no person**. This repository is published, and a
      transcript-store path is machine-identifying
- [ ] The false sentence in T-168 §3 is annotated rather than rewritten, per METHOD §5
- [ ] The other measurements this repository has taken against machine-private data are checked for
      the same gap, and what was found is stated — including the ones that do not have it

**Open questions**
- ~~**Does quoting the script in the record satisfy the criterion, or does reproducibility require
  something runnable?** A quoted script is copy-and-run for anyone with the store, and unrunnable for
  everyone else — which is also true of the measurement itself. **The maintainer decides**; the
  publishing constraint is the part nobody here can weigh alone.~~ **Answered by the owner on
  2026-08-19: quoting it satisfies the criterion** — see the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reconstruct the sweep from T-168 §3's prose alone, without inventing anything the record does not say | A script, in the scratchpad |
| 2 | Run it and compare every figure against the record, treating a divergence as information about the prose rather than as something to tune away | The comparison, in §3 |
| 3 | Strip anything machine-identifying: derive the subset from the rule instead of naming the projects the rule selects | The script, quotable |
| 4 | Quote it and its output into T-168 §3, marked as added and by whom | The edited T-168 §3 |
| 5 | Annotate, not rewrite, the sentence in T-168 §3 that says the plan was carried out unchanged | The annotated bullet |
| 6 | Check the repository's other machine-private measurements for the same gap | The sweep result, in §3 |

**Step 2 is the phase's real content, and step 1 is what makes it possible.** Reconstructing from the
prose *is* the test of whether the prose was sufficient — a script copied from a surviving original
would prove nothing about the record, which is the thing under repair.

**Decisions taken at `plan`**

- **One script, not three.** The three probes were reconstructed separately and merged, because the
  merged form is the one that needs no hand-maintained list: steps 2 and 3 take their subset from
  step 1's rule instead of naming the two projects it selects. *Rejected: three scripts as
  originally run*, which is closer to history and puts local folder slugs — drive letter and all —
  into a published file. — 2026-08-19
- **A divergence is reported, never tuned out.** If a reconstructed probe disagrees with the record,
  the first hypothesis is that the reconstruction is wrong and the second is that the record is;
  neither is settled by adjusting the probe until the number matches. — 2026-08-19

**Outputs this task will produce**

- tasks/T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md

## 3. Implement

### Steps 1–2 — the reconstruction, and the one figure it could not reproduce

Reconstructed from §3's prose. On the first run **eight of the nine figures matched and one did
not**: the record says **0** sessions asked for task work in ordinary words, and the reconstruction
said **7**.

Per the `plan` decision, the probe was not adjusted until it agreed. The seven matches were printed
and read, and **all seven were the same string** — the handoff skill's own stub, which the harness
injects as a record typed `user` and which contains the words *it does not start the task*. Nobody
typed any of them.

```text
17066a | '... it does **not** start the task. Writing the handoff is the task ...'
1b727e | '... it does **not** start the task. Writing the handoff is the task ...'
   (five more, the same sentence)
```

The store marks these `isMeta: true`. With that one filter the figure is **0**, and the record is
right.

**This is the finding, and it is worth more than the repair.** T-168's prose described the detector
as *the description's own phrasing*, which is enough to rebuild the pattern and not enough to rebuild
the corpus it ran over. A reader reconstructing it would have got 7, would have had no way to know
the record was right, and would most likely have concluded the trigger half was observable after
all — the opposite of what §3 step 3 established. **A quoted script carries the corpus definition;
prose about a pattern does not.**

### Step 3 — what had to come out

The three probes as run named their subset by folder slug, and a slug in this store is a local path
with its separators rewritten — drive letter, user folder and all. Merged into one script, the
subset comes from step 1's rule, so the quotable version contains no project name, no path and no
person. Checked rather than intended: the tracked file matches neither the machine's user name nor a
drive-letter path.

### Steps 4–5 — where it landed

T-168 §3 now carries the script, its run of 2026-08-19, and a heading saying it was added after the
fact and by which task. The bullet claiming the `plan` decision was *carried out unchanged* is
annotated in place and not rewritten: it records what was believed on 2026-08-18, and METHOD §5
keeps that.

### The run, against the record

| Figure | T-168, 2026-08-18 | Re-run, 2026-08-19 |
| :--- | :--- | :--- |
| class A | 2 projects, 11 sessions | **same** |
| class B | 4 projects, 7 sessions | **same** |
| class C | 5 projects, 174 sessions | 5 projects, **179** sessions |
| served | 10 of 11 | **same** |
| the entry, as served | 414 characters, one distinct length | **same** |
| asked in ordinary words | 0 | **same**, after the `isMeta` filter |
| literal token | 7 turns, 3 sessions, split 6 and 1 | **same** |
| opening their session | 0 | **same** |
| skills invoked | handoff twice, code-review once | **same** |

**Class C moved and nothing else did.** This repository's own transcript folder is class C, and it
has gained five sessions since. Class A — the class every criterion in T-168 is written about — is
unchanged, which is the corroboration the re-run can offer that a one-off measurement cannot.

### Step 6 — the same gap elsewhere

Four records measure against the agent's transcript store or against a session as served:

| Record | Has the gap? | What it quotes |
| :--- | :--- | :--- |
| [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) | **it did** | figures with the method in prose. Closed by this task |
| [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) | no | three runnable commands with their output, including the `git log -S` that dates the change |
| [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) | no, and not by having a script | its observations are of a live session's own behaviour, quoted as the harness's replies. There is nothing to script, and the record says so |
| [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) | no | it cites the two dated deliverables, which carry the method |

**One neighbouring instance, deliberately not raised as a task.**
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) §3 quotes
`paid meta-block: 1578 chars / paid tier-1 file: 5908 / share: 26.7%` with no command beside it. It
is the same shape one notch weaker: the data is `CLAUDE.md`, which every clone has, so the figures
are re-derivable by anyone rather than by one machine. §1 scopes this sweep to measurements against
**machine-private** data and that is not one, and the class of a quoted output nothing re-runs already
has a home in [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md)'s
mechanism. Recorded here so it is not lost, and not raised, because opting a closed record into that
mechanism would be editing a record about the past to satisfy a rule written after it.

**Decisions & assumptions**

- **The reconstruction is quoted, not the originals.** The originals are gone, and a reconstruction
  that reproduces every figure is better evidence than a recovered file would have been: it proves
  the record is sufficient, which is the actual outcome §1 asks for. — 2026-08-19
- Both `plan` decisions held; the second one is what produced the `isMeta` finding. — 2026-08-19
- **Assumption, recorded as one**: the reconstruction matching on nine figures does not prove it is
  the same code, only that it answers the same questions on the same corpus. For the outcome §1
  states — reproducible from the record alone — that is the thing being claimed, and the stronger
  claim is not made. — 2026-08-19

**Outputs produced**
- tasks/T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md — §3, the script,
  its run and the annotated bullet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| T-168 §3 carries the script, quoted | **met** | §3 steps 4–5. Under a heading naming the date and the task that added it |
| The quoted script has been run and its output recorded beside it | **met** | The run of 2026-08-19 is quoted under the script, and the comparison table in §3 sets it against the record line by line |
| Every figure §1 names is produced, or the divergence is stated | **met** | All three reproduce. One figure outside that set moved — class C, 174 to 179 — and §3 states it and its cause rather than omitting it |
| The script names no project, no path and no person | **met** | §3 step 3. The subset comes from the rule; checked against the file rather than intended |
| The false sentence is annotated, not rewritten | **met** | The `carried out unchanged` bullet keeps its original text and gains a dated annotation naming this task |
| Other machine-private measurements checked for the same gap | **met** | §3 step 6: four records, one had it, three did not and the table says what each quotes instead. One weaker neighbouring instance recorded with the reason it is not a task |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner on 2026-08-19 and is struck through there. Nothing
remains addressed to anyone else.

**The habit §1 asked to notice is worth stating at close.** The defect was not that a script was
lost. It was that `plan` promised *quoted* and `implement` wrote *described*, and both words are the
same author's, one day apart, with nothing between them that could disagree. What caught it was
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s own review
reading its criterion against the artifact instead of against the intention.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 3 of the eight. T-168 §3 now carries the sweep **quoted and run**, which is what its own `plan` decided before the wording drifted. The script was **reconstructed from that record's prose rather than recovered**, deliberately: that makes the reconstruction a test of whether the prose was sufficient, and it was not. Eight of nine figures matched on the first run and one did not — the record says 0 sessions asked for task work and the reconstruction said 7, and all seven turned out to be one injected skill stub the store marks `isMeta`. **A quoted script carries the corpus definition; prose about a pattern does not**, which is this task's finding and is worth more than the repair. With that filter every figure reproduces except class C's session count, which grew because this repository's own sessions are in it. The false sentence in T-168 is annotated rather than rewritten (METHOD §5), and the quoted script names no project, no path and no person. Three other machine-private measurements were checked and none has the gap. |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 3 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered by the owner: quoting the script in the record satisfies the criterion.** Asked in the backlog-wide round of 2026-08-19. It is copy-and-run for anyone holding the store and unrunnable for everyone else — which is equally true of the measurement itself, so a runnable file would not close the gap it appears to. It is also what [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §2 decided before the wording drifted to *described* at `implement`, and restoring the planned form is the repair this task exists for rather than a new choice. *Rejected: committing a runnable script* — it reads a machine-private transcript store no adopter has, so it could never run for them, and it would put machine-specific code in a repository whose publishing constraints forbid it. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review as the one criterion it did not meet. Raised rather than fixed in place, per [`review`](../plugin/skills/taskmd/docs/method/review.md) step 4 — repairing a criterion during its own review destroys the record of what was wrong. **Not covered by the authorisation of 2026-08-18**, which named T-168 and excluded everything it raises. |
