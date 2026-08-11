---
id: T-048
title: Say what "always-loaded" means in R-21, before the skill is built against it
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-003, T-028]
work_package: v0.1
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-11
deliverables:
  - docs/SCOPE.md
---

# T-048 — Say what "always-loaded" means in R-21, before the skill is built against it

## 1. Specify

**Outcome**
R-21 says what it means by "always-loaded", so that [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)
is built against a testable property rather than the phrase this project has just shown to be
relative.

**Why this one**
R-21 reads: *"The skill is a small always-loaded spine plus files loaded only when their moment
arrives — never the whole method up front."*

[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) established, by observation
rather than argument, that **"always-loaded" is relative to something and the something is never
stated.** `docs/METHOD.md` called itself always-loaded and was not: it is reached through a link and
read on demand, which is why a budget built on the phrase measured a claim instead of a load. The
sibling `handoff` skill has the same shape one level up — its core describes itself as *"the
always-loaded spine"* at 282 lines, while the artifact a session actually always has is a 31-line
stub.

R-21 uses the phrase in exactly that unqualified sense, and **T-003 is the next task to be built**.
A skill has at least two tiers of its own — the description the harness always has, and the body it
loads on activation — so a skill built to satisfy R-21 as written will reproduce the defect T-028
was raised to fix, one level up, in the deliverable this project exists to ship.

**This is not an argument against R-21.** Progressive disclosure is right and the requirement is the
right requirement; what is missing is the referent, which was invisible until T-028 went and looked.

**Requirements served**
R-21, R-22 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: R-21's wording, and any other requirement that leans on the same phrase.
- In: what the referent is for a skill — what a session has before the skill activates, versus after.
- In, **added at `specify` 2026-08-07**: the acceptance criteria of **open** tasks that will be judged
  against the phrase — today, [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)'s
  first and fourth. Correcting a criterion that contradicts the requirement it cites is not designing
  anything; leaving it would mean T-003 is judged against its own copy of the phrase rather than
  against R-21, which is precisely what criterion 4 below forbids. *Rejected: raising a separate task
  for it* — that is the right shape for a **finding**, which is why R-21 itself got this task rather
  than being fixed inside T-028, but a statement that this task's own answer makes false is reconcile
  debt, and T-022's precedent is that the task making it false pays it.
- Out: `CLAUDE.md`'s tier model. T-028 settled it for this repository; this is about the requirement
  a shipped skill is judged against, which is a different reader.
- Out: designing the skill's tiers. That is T-003's work; this task gives it a testable target.
- Out: `docs/METHOD.md` and `docs/BINDING.md`, both already reconciled to the tier model.
- Out: the records of **closed** tasks, which use the phrase throughout and are evidence of what was
  believed when they ran. Editing them would destroy the audit trail that made this task findable.

**Inputs**
`docs/SCOPE.md` R-21 and R-22,
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) §1 Q1 and §3 step 1,
[T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md).

**Acceptance criteria**
- [ ] R-21 states what "always-loaded" is relative to, in terms someone can check against a real
      session rather than against a document's description of itself
- [ ] The requirement stays a **property**, not an instruction — `docs/SCOPE.md` §3's division, which
      T-017 settled and T-045 re-checked, is not disturbed
- [ ] Every other requirement using the phrase is found by search and resolved the same way, or
      confirmed not to use it
- [ ] T-003 can be judged against the result: someone holding the finished skill can say whether it
      passes, without re-litigating what the phrase meant
- [ ] Every **live** statement that would be judged against the phrase is resolved — the requirement,
      and the acceptance criteria of open tasks that cite it. Closed tasks' records are evidence of
      what was believed at the time and are left alone
      <br>*Added 2026-08-07 at `specify`, with the scope amendment above. The four original criteria
      stand unchanged.*

**Open questions**
- None. The referent is discoverable the way T-028 discovered it — observe what a session is handed
  before anything is asked of it — so this needs measurement rather than a decision.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Measure, before writing a word of the requirement.** Observe what a session is handed for a skill it has not invoked, versus after invoking it, on the sibling skill this repository already cites. The whole defect is a phrase asserted rather than checked, so a step that reasoned about the referent instead of looking at it would reproduce it. | The observation recorded in §3: which artifact arrives at which moment, with its size |
| 2 | Search the tracked tree for the phrase and split the hits three ways — the requirement, the acceptance criteria of open tasks, and the records of closed ones. The third group is evidence and is not touched. | A classified list in §3, so criteria 3 and 5 are answered from a search rather than from memory |
| 3 | Rewrite R-21 so it names the referent and says how it is falsified. | The edited row in `docs/SCOPE.md` §3D |
| 4 | Correct the live statements step 2 turned up outside `docs/SCOPE.md`. | The edited criteria in `tasks/T-003-…md` |
| 5 | Run `check`, `index` and the pre-publish check, and confirm the requirement still reads as a property rather than an instruction by the test `docs/SCOPE.md` §3 already states. | The transcript in §3, and the §3 test applied in §4 |

**Deliverable shape — decided here.**

**R-21 names the referent and stops there; it does not name a number of tiers.** The referent is what
makes the phrase checkable, and it is one clause. A count is a design, and designing the skill's
tiers is T-003's — a requirement that fixed the count would be judging T-003 against a decision this
task took on its behalf. *Rejected: writing the three tiers into R-21*, which is tempting because the
sibling has them and `CLAUDE.md` records three for this repository, and which fails `docs/SCOPE.md`
§3's own test: a row that survives someone rewriting the method is a property, and a row that fixes
an architecture does not.

**The falsification clause names the *measurement*, not a limit.** R-21 becomes falsifiable by going
and looking at a session, in the same move T-028 used. *Rejected: a line budget for the skill*, on
two grounds — `CLAUDE.md` already owns the budget question for this repository and T-048's scope puts
it out, and a number in a requirement is the pair T-028 spent a whole task removing.

**Output paths**

- `docs/SCOPE.md` — the R-21 row
- `tasks/T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md` — two acceptance criteria

## 3. Implement

### Step 1 — measured, and the sibling has four tiers where its own documents claim three

Observed in this session, which invoked the sibling skill and so carries both halves of the
measurement. Before invocation, the only thing present is the skill's **`description` field**,
supplied by the harness in a listing of available skills. The body arrived only when the skill was
invoked by name, and the core only when the body pointed at it.

| Arrives | Artifact | Size |
| :--- | :--- | ---: |
| every session, unasked | the `description` field of the skill's front-matter | 1 field, ~65 words |
| on invocation | the skill body | 29 lines |
| when the body points at it | the portable core | 282 lines |
| when a mode is chosen | one flow file | 71 or 92 lines |

**This overturns the figure T-048 was raised with, in the same direction and one tier further.** §1
says the artifact a session always has is the 31-line stub. It is not: the stub is the *body*, and it
loads on invocation like everything else. What a session that never mentions the skill pays for is
the description alone. So the sibling's core calling itself *"the always-loaded spine"* at 282 lines
is wrong by **two** tiers, not one — and the stub repeats the same phrase about the core, which is
how the claim survived being copied.

**Why this is the answer rather than an observation about one harness.** The tiers differ in kind,
not just in size: the description is paid by every session in the project including every session
that never does task work, while everything below it is paid only by a session that has already
decided to do the thing. That is the distinction R-21 exists to protect, and it is the one the
unqualified phrase cannot express.

### Step 2 — the phrase, classified

| Where | Kind | Action |
| :--- | :--- | :--- |
| `docs/SCOPE.md` R-21 | the requirement | rewritten, step 3 |
| `T-003` criteria 1 and 4 | **open**, and would be judged against it | corrected, step 4 |
| `T-036` criterion 4 | **open**, and uses the phrase | none — it reads "unchanged, or the change is agreed against T-028's decision", so the referent is named in the same sentence. Qualified already, and about this repository's tier 1 rather than the skill's |
| `T-047` | **open** | none — cites T-028's tiering by name and never uses the bare phrase |
| `docs/METHOD.md` 10 and 49, `CLAUDE.md` 58 | live, written by T-028 | none — they state *this repository's* tier boundary, which is the fix, not the defect. `CLAUDE.md` 58 cites R-21 for tiers 2 and 3, and that citation is neither strengthened nor weakened here |
| `T-008`, `T-014`, `T-015`, `T-028` closed, `T-026` at review | records of what was believed while they ran | none — evidence, and editing it would delete the trail that made this task findable |
| `docs/BRIEF.md` 20 | about token cost, not the phrase | none |

`docs/BINDING.md` and `.handoff/config.md`, the other two hits from T-028's sweep, were reconciled in
that sweep and carry no unqualified use now.

**Two open tasks other than T-003 use the phrase and neither needed changing**, which is worth
recording rather than leaving as a silent absence: a criterion naming its referent in the same
sentence is already doing what this task asks R-21 to do.

### Decisions & assumptions

- **The referent is "before the skill is invoked", not "before the body is read"** — 2026-08-07,
  step 1. The measurement forces it: there is a tier below the body, and it is the one every session
  pays for. Naming the body would have reproduced the sibling's error at the exact place this task
  was raised to prevent it.
- **R-21 states the referent and the falsification, and no count** — 2026-08-07, step 3. Decided in
  `plan` and confirmed against `docs/SCOPE.md` §3's test: the row survives someone rewriting the
  skill completely, which is what makes it a property rather than an instruction.
- **T-003's criterion 1 is replaced rather than reworded** — 2026-08-07, step 4. "Short enough to
  load on every turn without cost" is not imprecise, it is false: the body does not load on every
  turn. What it was reaching for — that the always-paid tier is small — is now R-21's, so the
  criterion points at R-21 instead of carrying a second copy of it, which is R-22 applied to this
  project's own backlog.

### Outputs produced

- `docs/SCOPE.md` — the R-21 row
- `tasks/T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md` — criteria 1 and 4

### Verification

`check` clean on 49 tasks, index regenerated, suite 114/114 untouched by a documentation change, and
the pre-publish check prints nothing with its exclusion. The substantive verification is step 1's
measurement, which is the only kind this task admits: a requirement about what a session loads is
checked by looking at a session, not by reading the requirement.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| R-21 states what "always-loaded" is relative to, in terms someone can check against a real session rather than against a document's description of itself | met | It names the moment — *before the skill is invoked* — and the artifact that occupies it, and it says what falsifies the row: measuring a session. The referent was not chosen by argument; step 1 went and looked, and the answer contradicted this task's own §1, which is the strongest available evidence that the phrase needed a referent |
| The requirement stays a **property**, not an instruction — `docs/SCOPE.md` §3's division, which T-017 settled and T-045 re-checked, is not disturbed | met | Applied §3's own test: *does the row survive someone rewriting the method completely?* It does — any skill, of any shape, can be measured against what a session receives before invoking it. The row deliberately stops short of naming a number of tiers, because a count is an architecture and would have failed that test; the rejection is recorded in `plan` rather than left implicit |
| Every other requirement using the phrase is found by search and resolved the same way, or confirmed not to use it | met | Searched rather than recalled, and the classification is in §3 step 2. R-21 is the only **requirement** that used it. R-22 is adjacent and does not. The other live hits — `docs/METHOD.md` and `CLAUDE.md` — state a tier rather than the unqualified phrase, which is T-028's and T-047's work already done |
| T-003 can be judged against the result: someone holding the finished skill can say whether it passes, without re-litigating what the phrase meant | met | And it required more than editing R-21, which is what the `specify` scope amendment was for: T-003 carried its own copy of the phrase in criterion 1, so it would have been judged against that rather than against the requirement. Corrected to point at R-21, which is R-22 turned on this project's own backlog |
| Every **live** statement that would be judged against the phrase is resolved; closed tasks' records are left alone | met | Two live statements, both corrected. Five closed tasks use the phrase and none was touched — they record what was believed while they ran, and rewriting them would delete the trail that made this task findable in the first place |

**Also checked, beyond the criteria**

- **The measurement overturned this task's own §1, and §1 was left as written.** §1 says the artifact
  a session always has is the sibling's 31-line stub. It is not — the stub is the *body* and loads on
  invocation, so what a session actually always has is one front-matter field. The correction lives
  in §3 and in this log, following T-028's own precedent: refreshing §1 would delete the evidence the
  task was raised on, and the movement is the record's to carry.
- **The error being fixed is two tiers deep in the sibling, not one.** Its core calls itself the
  always-loaded spine at 282 lines, and its body repeats that claim about the core — so the phrase
  was copied along with the mistake. That is the mechanism this requirement now blocks: not a wrong
  number, but a claim that nobody was in a position to check.
- `check` clean on 49 tasks; index regenerated; suite 114/114, unaffected as expected by a
  documentation change; pre-publish check prints nothing with its exclusion and exactly five lines
  without it, all in its own fixture.

**Child fix tasks raised**
- none — every criterion is met.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-07 | → done | Five criteria met, none carried. The load-bearing move was refusing to answer the question by argument: step 1 observed a session that had *not* invoked a skill and one that had, and the answer contradicted this task's own §1 by a whole tier. What a session always has is a skill's `description`; the body loads on invocation, so the 31-line stub §1 called always-present is not. R-21 now names the moment rather than the artifact, states what falsifies it, and deliberately fixes no number of tiers — a count would be an architecture and would fail §3's own property test, which the review applied rather than assumed. |
| 2026-08-07 | → review | Five steps, worked in order. The measurement came first on purpose: the defect being fixed is a phrase asserted rather than checked, so reasoning about the referent would have reproduced it. Two things fell out. The sibling skill is wrong by two tiers, not one — its core claims to be the always-loaded spine and its body repeats the claim, which is how it propagated. And the phrase was live in a second place: T-003's criterion 1 said the skill body loads on every turn, which is false rather than vague, so T-003 would have been judged against its own copy instead of against R-21. Corrected there under the `specify` scope amendment. |
| 2026-08-07 | → specified | Nothing was outstanding — the question had already been answered as *measure it* — so `specify` did the one thing left: check the criteria were sufficient, and they were not. Criterion 4 asks that T-003 be judgeable against the result, and T-003 carries its own unqualified copy of the phrase, so editing `docs/SCOPE.md` alone could not deliver it. Scope amended to cover the acceptance criteria of **open** tasks, with closed records explicitly excluded, and a fifth criterion added. The alternative — a separate task — is recorded as rejected: that is the right shape for a finding, which is why R-21 got this task rather than being fixed inside T-028, but a statement this task's own answer makes false is reconcile debt, and T-022's precedent is that the task making it false pays it. |
| 2026-08-07 | → proposed | Found during the reconcile sweep after T-028 closed, and deliberately **not** fixed there: T-028's scope put `docs/SCOPE.md` out, and R-21 was not made false by that task — it carried the same unqualified phrase before it and would have carried it after. So this is a finding rather than a stale line, and METHOD §5 keeps the two apart. `high`/`xs` because the cost is one sentence and the exposure is T-003, which is `critical`, next in the ordering, and would otherwise reproduce T-028's defect inside the deliverable. Two lines *were* reconciled in the same sweep and are not part of this task: `docs/BINDING.md` said the method governs every turn, and `.handoff/config.md` called METHOD an always-loaded spine — both made false by T-028's edit rather than merely imprecise. |
