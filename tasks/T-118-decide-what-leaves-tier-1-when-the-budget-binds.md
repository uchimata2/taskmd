---
id: T-118
title: Decide what leaves tier 1 when the budget binds
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-026, T-028, T-047, T-050, T-063, T-115, T-119]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [CLAUDE.md]
---

# T-118 — Decide what leaves tier 1 when the budget binds

## 1. Specify

**Outcome**
A decision, taken before the test goes red rather than during the edit that turns it red: what comes
out of tier 1 when it next exceeds its bound — or that the bound moves, with the reason it may.

**Why this one**
Carried out of [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md)'s review so that
closing the umbrella does not bury it. That review recorded a residual against its third criterion:
F-2, the audit's one clause-5 finding, named the cheaper **measure** — budget the whole always-loaded
set rather than one file — but not what to cut, and
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) put choosing the cut out of
scope. The residual was flagged for the owner and never answered.

**What has happened since, which changes the question rather than closing it.** The cheaper measure
was built and is now enforced: [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md)
made the budget a test, and it passes.

```
tier 1 7844 chars under by 2 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
```

So no cut was ever required — F-2's proposal was sufficient on its own, which is the answer to the
residual as it was posed. What is left is the next margin: **two characters**. The next ordinary
reconcile of `CLAUDE.md` turns the suite red, and at that moment somebody is mid-edit on something
else, which is the worst time to decide what a project's always-loaded context is for.

**This has been declined in passing twice.** T-028 scoped the cut out; T-047 moved two method rules
*into* `CLAUDE.md` and did not reopen it. Both were right to — a decision taken in passing while
doing something else is how the wrong thing gets cut. But twice declined and never raised leaves it
owned by nobody, which is the state this task exists to end.

**Requirements served**
R-15 (`docs/SCOPE.md`); `CLAUDE.md` *Three tiers, and only the first is budgeted*.

**Scope**
- In: what may leave tier 1, and by what rule — so the answer survives the next addition rather than
  naming one paragraph.
- In: whether the bound itself is right. It is `reference/TASK-WORKFLOW.md`'s size, chosen because it
  is the flat alternative the split must beat; a bound that is an artifact of another file's length
  is worth confirming deliberately rather than inheriting.
- Out: the two method rules `CLAUDE.md` carries verbatim (T-047). They bind before tier 2 loads, so
  tier 2 cannot be their home; moving them is not a cut, it is a regression.
- Out: changing how tier 1 is measured. That is settled and tested.

**Inputs**
`CLAUDE.md`, `plugin/skills/taskmd/SKILL.md`, `tests/test_budget.py`,
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md),
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md),
[T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) §4 criterion 3.

**Acceptance criteria**
- [ ] A rule is recorded for what belongs in tier 1, such that a reader with a candidate paragraph
      can tell whether it qualifies without asking — falsified by an answer that names what to cut
      today and gives the next session nothing
- [ ] The alternative is recorded with what it costs: moving the bound, and why the flat file is or
      is not the right thing to be measured against
- [ ] Whatever is decided, the test still passes and its margin is stated — a decision that leaves
      the margin at two characters has deferred the problem rather than taken it

**Open questions**
- ~~Is the answer a cut, or a different bound?~~ **Answered by the maintainer on 2026-08-11: state
  the rule first and let the cut fall out of it.** Tier 1's membership is already derived from the
  tree rather than listed, so a rule about what may be there is the same shape as everything else
  here, and it is what makes the *next* addition decidable rather than only this one. *Rejected:
  raising the bound.* It was defensible — the bound is another file's byte count, not a measured cost
  — but it converts a constraint into a number somebody chose, which is what the flat-file comparison
  exists to avoid, and it would have to be re-chosen every time the pressure returned.

  **What the answer settles, and what it deliberately does not.** It fixes the *order*: no paragraph
  is cut until the rule that would justify cutting it is written down. It does not pre-judge whether
  anything is cut at all — a rule may well find tier 1 already correct at 7,844 characters, in which
  case the finding is that the bound is the thing under pressure and criterion 2 is where that gets
  argued. Either outcome satisfies criterion 1; what it forbids is reaching for the largest paragraph
  under deadline, which is the failure this task was raised to prevent.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the rule: what qualifies a paragraph for tier 1, stated so that a reader holding a candidate can apply it without asking. Not a list of what is there today — that is membership, which this project derives rather than writes. | The rule, recorded in §3 |
| 2 | Apply the rule to tier 1 as it stands — `CLAUDE.md` section by section, and the served skill's `description` — and record a verdict per member with the rule's own reason. **This step can invalidate steps 3–5:** if nothing fails, there is no cut, and criterion 3 falls entirely to step 4. | A pass over today's members, each kept or cut with its reason, recorded in §3 |
| 3 | Take whatever cut step 2 produced, and put the rule itself into tier 1 — it costs characters, so it is paid for out of the same pass rather than exempted from its own test. Anything cut that is still needed moves to its home; nothing is deleted for being long. | Edited CLAUDE.md, and plugin/skills/taskmd/SKILL.md only if step 2 finds the description is what fails |
| 4 | Argue the bound: whether `reference/TASK-WORKFLOW.md` is the right thing to be measured against, and what moving it would cost. This is where the rejected answer from `specify` keeps its say, and where the answer lands if step 2 finds no cut. | The decision and its rejected alternative, recorded in §3 |
| 5 | Re-run the budget test and state the margin the decision leaves. A margin that the next ordinary edit still turns red is a finding to record, not a pass to report. | `python tests/test_budget.py` output, recorded in §3 |
| 6 | Run `check` and `index`, then the full suite per module, stating the result against the four `Launchers` failures this tree is already known to carry locally (T-114). | The commands' output, recorded in §3 |

**Deliverable shape** — the rule's home is `CLAUDE.md`, in the *Three tiers* section, and its argument
stays here. Rejected: **a page under `docs/`**, which is free of the budget but reaches the reader too
late — a rule about what may enter tier 1 binds at the moment somebody is editing tier 1, and at that
moment tier 1 is the only thing loaded. That is T-047's argument for carrying METHOD §3.1 and §3.3
verbatim, and it applies unchanged here. Also rejected: **this task alone, reached from the rationale
list `CLAUDE.md` already carries** — about seven characters, the cheapest option by far, and wrong for
the same reason: that list points at *why*, and this is a rule that binds. The split this project
already runs is rules in tier 1, arguments in tasks; the rule paying its own way into the thing it
governs is the honest form of it.

**Promised outputs**
- CLAUDE.md
- tasks/T-118-decide-what-leaves-tier-1-when-the-budget-binds.md
- plugin/skills/taskmd/SKILL.md (conditional on step 2)

## 3. Implement

### Step 1 — the rule

**A line belongs in tier 1 only if it changes what a session does before that session has chosen what
to work on.** Everything scoped to an activity the session *knows* it has started — a phase,
publishing, adopting, writing a binding — is reachable from a pointer at the moment it starts, so
tier 1 carries the pointer and never the thing. Its text is in `CLAUDE.md` *Working method*; what
follows is the argument, which is why it is here and not there.

The rule is about **when** a fact is needed, not how important it is. Importance was the trap: every
line in a project's conventions is important, which is why "is this important?" has never cut
anything and why this has been declined twice in passing. *When* discriminates, because tier 1 is
paid by every session and most of what it carries is used by one session in fifty.

**An activity nobody announces is the exception, and it is what admits this rule into the thing it
governs.** Editing `CLAUDE.md` is never the task; it happens while reconciling, while handing off,
while tidying. There is no moment at which a session says "I am editing tier 1 now" and goes to fetch
the rule, so a rule kept one tier down would be read only by someone who already knew it. That is the
same argument T-047 used to carry METHOD §3.1 and §3.3 here verbatim, arrived at independently —
which is the first evidence the rule is the project's own and not a new preference.

**This was found by using the rule, not by writing it.** As first drafted the rule listed "editing
this budget" among the chosen activities, and so cut itself: by its own words it belonged one tier
down behind a pointer. The announced/unannounced distinction is the repair, and it is load-bearing
rather than a saving throw — without it the rule is an argument for emptying tier 1 entirely.

### Step 2 — the rule applied to tier 1 as it stood

Measured first, judged second; per-section character counts of `CLAUDE.md` plus the served
`description`, totalling the 7,844 that `specify` records.

| Member | Chars | Verdict |
| :--- | ---: | :--- |
| `# taskmd — working conventions` + preamble | 81 | **Keep** — it is what makes the rest arrive |
| *What this is*, para 1–2 (what this is, read-in-this-order) | ~700 | **Keep** — the index that makes tier 2 reachable at all |
| *What this is*, "Status: published … front door … four commands" | ~165 | **Cut** — status, and duplicated by *Publishing constraints* saying the repository goes to GitHub |
| *What this is*, the invocation `./plugin/bin/taskmd` (T-054) | ~250 | **Keep** — a session cannot run the tool without it, and running the tool is how work is chosen |
| *What this is*, `after_write` | ~90 | **Keep**, on unproven reachability rather than on the rule — it was not confirmed to have another home, and keeping is the safe way to be wrong |
| *What this is*, para 4 (`check` shown failing, fixtures, `BINDING.md`, both bindings written) | ~370 | **Cut** — where the project has got to. It ends by naming its own home; `BINDING.md` stays reachable from `README.md`'s load-when table and from both bindings |
| *The one design rule* | 556 | **Keep** — binds on every design decision, including ones taken with no task open |
| *Working method*, the method's one home | ~330 | **Keep** — the tier-2 pointer |
| *Working method*, three tiers and the bound | ~830 | **Keep** — unannounced activity, per the rule |
| *Working method*, "Why membership is derived … T-028, T-050, T-063 and T-115" | ~250 | **Cut** — rationale, reachable when the rule is challenged. A list of ids that grows each time the rule is argued is membership in disguise; it collapses to the one task holding the current rule, which points onward |
| METHOD §3.1 and §3.3 verbatim, and their preamble | 2,731 | **Keep** — 35% of tier 1 and the rule admits them outright, without needing `specify`'s out-line |
| *Working method*, "What this project adds on top" (4 bullets) | ~470 | **Cut** — every one has a home a session is told to load before touching a task; see below |
| *Working method*, `reference/TASK-WORKFLOW.md` is not the standard | ~270 | **Keep** — its home was not established, so the rule does not reach it yet |
| *Publishing constraints*, the five constraints | ~510 | **Keep** — they bind on everything written, before anything is chosen |
| *Publishing constraints*, what the pre-publish check is and why it is short | ~230 | **Cut** — publishing announces itself; the pointer survives, the description does not |
| *Verifying* | 347 | **Keep** — binds on every claim, including claims made with no task open |
| `SKILL.md` `description` | 397 | **Keep** — it *is* the pointer; a trigger qualifies at the length that makes it fire |

**The four bullets were checked, not assumed.** `plugin/skills/taskmd/docs/bindings/local-markdown.md`
carries the generated index (§ lines 19, 25), `tasks_dir` and the identity keys (83, 89), copying the
template (106), and — in its own words — T-076's reason for the template sitting *in* `tasks_dir`
rather than under it (110–116). `SKILL.md` carries the schema pointer and "never maintain a list".
So the block was a second copy of facts already at home, and `SKILL.md` tells a session to load the
binding *before creating or changing any task* — which is the pointer the rule requires.

### Step 3 — the cut

Four cuts, all of them status, rationale or duplication; nothing was removed for being long. The rule
itself was added to `CLAUDE.md` and paid for out of the same pass rather than exempted from its own
test.

### Step 4 — the bound

**Keep `reference/TASK-WORKFLOW.md` as the bound.** *Rejected: any chosen number.* The objection to
the flat file is real and is the one `specify` recorded — 7,846 is an artifact of another document's
length, and nothing says the right size for tier 1 is exactly that. But it is the same property that
makes it the right bound: it encodes a falsifiable claim about the design rather than a preference —
*a split whose always-loaded first tier costs more than the flat document it replaced has inverted
the point of splitting it* — and a claim cannot be quietly raised by the session that is failing it,
whereas a number can. That failure is not hypothetical here; it is the one this task was raised to
prevent, and moving the bound is exactly what it would look like.

**What that costs, recorded rather than glossed:** the bound moves if `reference/` is ever edited or
dropped, for reasons having nothing to do with tier 1, and it measures a length rather than what is
actually paid, which is tokens per turn. Both are accepted. The first is bounded — `reference/` is
frozen prior art by construction — and the second is a unit problem the project already decided
(characters, T-115) rather than a bound problem.

### Step 5 — verification, and the margin

The rule is a decision, so it is verified by being *used*: applied to all seventeen members above
before anything was edited. It surprised its author three times, which is the test of a use rather
than a re-reading — it cut itself (step 1), it reproduced T-047's independently-taken trim of the
pre-publish check, and it admitted METHOD §3.1/§3.3 without needing the exemption `specify` wrote for
them.

```
tier 1 6968 chars under by 878 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
```

**The margin is 878 characters, from 2.** That is roughly eleven per cent of the bound, and on this
project's own history — `CLAUDE.md` grew by about 400 characters over the run that produced T-115 —
it is several ordinary reconciles rather than one edit. Stated as required by criterion 3: the
problem is taken, not deferred.

### Escalated (METHOD §3.3)

- **Raised as [T-119](T-119-put-the-stranded-paragraph-under-a-heading-that-owns-it.md).**
  Removing the bullet block exposed that the `reference/TASK-WORKFLOW.md` paragraph sits under
  `#### Surface what you discover — never absorb it, never drop it`, a heading that has nothing to do
  with it. Pre-existing, not caused here, and out of scope: this task decides what *leaves* tier 1,
  not where what stays sits.

**Outputs produced**
- CLAUDE.md
- tasks/T-118-decide-what-leaves-tier-1-when-the-budget-binds.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A rule is recorded for what belongs in tier 1, such that a reader with a candidate paragraph can tell whether it qualifies without asking — falsified by an answer that names what to cut today and gives the next session nothing | met | The rule is in `CLAUDE.md` *Working method* and takes a candidate as its input, not a list of today's contents. What settles it is that it was **shown deciding**: seventeen members in §3 step 2, four of them cut, and it reached the two decisions this project had already taken independently (T-047's trim of the pre-publish check; derive-don't-list). It also decided *against itself* on first drafting and had to be repaired — a rule that could not lose an argument would not have. The falsifier is not triggered: it named no paragraph until after the rule existed |
| A rule is recorded … without asking (second reading: what the rule still requires of its reader) | met, with a limit stated | Applying it can require a **lookup, not a question** — two keeps (`after_write`, `reference/TASK-WORKFLOW.md`) rest on reachability that was not established rather than on the rule deciding for them, and §3 step 2 says so in their rows instead of dressing them as rule outcomes. A reader can settle both by reading the tree; neither needs the owner |
| The alternative is recorded with what it costs: moving the bound, and why the flat file is or is not the right thing to be measured against | met | §3 step 4. The flat file is kept and *any chosen number* is the recorded rejection; the argument is that the bound encodes a falsifiable claim about the design, which the session failing it cannot quietly raise. Its two costs are written down rather than glossed — the bound moves if `reference/` is ever edited or dropped, and it measures a length, not the tokens actually paid |
| Whatever is decided, the test still passes and its margin is stated — a decision that leaves the margin at two characters has deferred the problem rather than taken it | met | `tier 1 6968 chars under by 878 (bound 7846, reference/TASK-WORKFLOW.md)`. 878 from 2; against this project's own growth — about 400 characters over the run that produced T-115 — that is several ordinary reconciles, not one edit. The rule paid its own way in rather than being exempted from the count it governs |

**The one form of verification not available before close**, recorded rather than implied: the
method's check for a decision is that *the people bound by it can state what it commits them to*, and
the maintainer has not yet read the rule back. What was done instead is the strongest use available
from inside the session — applying it to every current member before editing anything, which
surprised its author three times. The close report is the read-back moment; a criterion is not being
claimed on it.

**Child fix tasks raised**
- none. [T-119](T-119-put-the-stranded-paragraph-under-a-heading-that-owns-it.md) came out of
  `implement`, not out of a criterion, and carries no part of this task's outcome.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All three criteria met, none carried, and the second row is criterion 1 read a second way rather than a fourth criterion — it exists because the honest answer to "without asking" is *without asking the owner, but not without reading the tree*, and burying that in a tick would have made the tick worth less than the note. Nothing was repaired during review; T-119 was already open before it started. The one verification the method asks for and the session could not perform — the people bound stating back what the rule commits them to — is recorded as a gap rather than claimed, because the maintainer reads this at close and that is the moment it happens. Suite as the runner would see it: `test_cli` 89, `test_list` 29, `test_schema` 46, `test_budget` 5 all green; `test_runtime` 27 with the four `Launchers` failures this machine already carries (T-114), named individually rather than counted, so a fifth could not hide in the number. |
| 2026-08-11 | → in_progress → review | Four cuts, all status, rationale or duplication; the margin went from 2 characters to 878. The result the plan did not expect: **the rule cut itself** on first drafting, because editing tier 1 looked like any other chosen activity — the announced/unannounced distinction that repairs it is the phase's real yield, and it came from applying the rule rather than from writing it. Step 2's verdict table is where the answer actually lives: it is the rule shown deciding seventeen cases, including the four it kept for reasons that are not the rule (`after_write` and `reference/` on unproven reachability, said so rather than dressed up). Two of the cuts reproduce decisions taken independently — T-047's trim of the pre-publish check, and the design rule's derive-don't-list — which is the closest thing available to a second opinion. Bullet block cut only after checking every one of its four facts is carried by `bindings/local-markdown.md` or `SKILL.md`, cited by line; nothing was removed on the assumption that it must be written somewhere else. T-119 raised for the paragraph the cut left stranded under the wrong heading. |
| 2026-08-11 | → planned | Steps 1–2 carry the maintainer's answer as their order: the rule is written before anything is judged against it, and step 2 is allowed to conclude that nothing fails. Shape decided rather than deferred, because where the rule lives changes what step 3 has to pay for — see *Deliverable shape*. **Authorization, recorded here rather than in the handoff that carried it (METHOD §3.1):** the maintainer gave a standing instruction on 2026-08-10, re-confirmed since and most recently per task by name, to work each open `v0.2` task through its full lifecycle — specify, plan, implement, review, fix, commit and push — one task at a time, stopping before the next task when the remaining work will not fit the context. It covers the whole lifecycle of this task and nothing outside the `v0.2` set. |
| 2026-08-11 | → specified | Answered by the maintainer the day it was raised: state the rule first, let the cut follow. Criteria stand as written — they were drafted to survive either answer, and criterion 2 is where the rejected option keeps its say, since "why the flat file is or is not the right thing to be measured against" is exactly the argument raising the bound would have made. Nothing here needed the owner beyond that: the remaining questions are `plan`'s. Handed to a clean session at the maintainer's request with `specify` complete and no work started. |
| 2026-08-11 | → proposed | Raised at T-026's close, so the umbrella's one unanswered residual gets an open home instead of expiring inside a closed task. The residual as posed is answered by events — F-2's cheaper measure was built, is enforced, and passes with no cut — so this is not that question re-asked; it is the two-character margin that answer left behind, and the fact that two tasks have now declined the cut in passing without anyone raising it. |
