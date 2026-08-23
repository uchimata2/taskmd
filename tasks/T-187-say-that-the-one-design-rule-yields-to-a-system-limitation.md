---
id: T-187
title: Say that the one design rule yields to a system limitation
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-179, T-012]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-19
updated: 2026-08-21
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/METHOD.md, docs/SCOPE.md]
---

# T-187 — Say that the one design rule yields to a system limitation

## 1. Specify

**Outcome**
The one design rule — *store the forward edge; derive the rest* — states its own purpose and the
condition under which a project may deviate from it, so that a decision to write a fact twice can be
judged against a written test instead of argued from first principles each time.

**Why this one**
**The owner ruled it on 2026-08-19**, while answering
[T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md)'s open question in the backlog-wide
round of that date. The words were that single source of truth is the *ultimate goal* rather than an
absolute, that its purpose is to minimise inconsistency and unnecessary administration, and that a
system configuration or comparable limitation is grounds to deviate.

**It is raised here rather than folded into T-179 for the reason that task's answer gives.** T-179
changes one binding document; this changes the rule every design decision in the repository is
checked against, and it lives at a different tier — `CLAUDE.md` carries the pointer, and the rule is
stated in full in `plugin/skills/taskmd/docs/METHOD.md` §4. A ruling of that reach recorded inside a
binding task is one a later session reads as being about bindings.

**The rule already admits one exception and does not say why.** METHOD §4 draws a line around what
the word *requires* does and does not forbid, and
[T-012](T-012-decide-whether-soft-edges-are-symmetric.md) settled that a derived inverse may be
written twice. So the amendment is expected to make an existing tolerance explicit rather than to
open a new one — which is also the risk: a deviation clause loose enough to cover any inconvenience
retires the rule.

**Scope**
- In: the amended wording of the rule in its own home, carrying its purpose and the deviation
  condition
- In: whether `CLAUDE.md`'s pointer needs any change, judged against the tier-1 budget rather than
  assumed
- In: whether the existing tolerances — T-012's derived inverse, and the two rules `CLAUDE.md`
  restates verbatim — are instances of the new clause or remain separately stated
- In: whether the rule's **other statements** still hold once it is amended — `docs/SCOPE.md` §2
  principles 1 and 2 state it as well. **Added at `specify` on 2026-08-21**, having been missed when
  this was raised: an amendment that leaves a second statement asserting the unamended rule is a
  contradiction the project would then carry, which METHOD rule 5 already forbids. It widens the
  reading, not the writing — the finding may well be that both already point at §4 for exactly this
- Out: re-opening any decision the rule has already been used to settle. A clause that arrives with
  a list of decisions it reverses is a rewrite, not an amendment
- Out: T-179's own answer, which stands on the binding's precedent and does not wait on this

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the rule in full, and the text this amends
- `CLAUDE.md` — the pointer, and the two-rule exception it already carries
- [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md) — the answer this ruling arrived
  with, and the case that prompted it
- [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) — the one deviation already settled

**Acceptance criteria**
- [ ] **The rule states what it is for** — minimising inconsistency and unnecessary administration —
      so it reads as a means to that end rather than as an end in itself. *Falsified* if the amended
      §4 can be read start to finish without learning why the rule exists.
- [ ] **It states the deviation condition in terms a reader can apply**: a system configuration or a
      comparable limitation that puts the single write out of reach. *Falsified* if settling a real
      case still needs an argument from first principles rather than a reading of the sentence.
- [ ] **It names at least one case that does not qualify**, concrete enough that a reader can point
      at the words that refuse it. *Falsified* if every deviation somebody could propose passes —
      the failure §1 names as retiring the rule, and the owner's condition of 2026-08-21.
- [ ] **Each tolerance that already exists is classified** — [T-012](T-012-decide-whether-soft-edges-are-symmetric.md)'s
      permitted second write of a derived inverse, and the two METHOD rules `CLAUDE.md` restates
      verbatim ([T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)) —
      as an instance of the new clause, or as standing separately with the reason. *Falsified* if a
      reader cannot tell which, for either.
- [ ] **Whether `CLAUDE.md`'s pointer changes is decided against a measured figure**: the decision
      cites the headroom `python tests/test_budget.py` reports, and that suite still passes after the
      change. *Falsified* by a decision recorded without the number, which §1's scope refuses by name.
- [ ] **The rule's other statements do not contradict the amended one** — `docs/SCOPE.md` §2
      principles 1 and 2, and `CLAUDE.md`'s *one design rule* section — each checked and the result
      recorded **per document**, not as one assurance covering all three. *Falsified* if any of them
      still states the rule as admitting no deviation.
- [ ] **Nothing the rule has already settled is reversed.** *Falsified* if the same change writes any
      fact to a second home, or if its text tells anyone to revisit a past decision — which §1's
      out-list calls a rewrite rather than an amendment.

**Open questions**
- ~~**What stops the clause swallowing the rule?**~~ **Answered 2026-08-21: the amendment must name
  what does *not* qualify.** The owner required it. The argument given is this project's own
  [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) rule applied to prose: a
  check is trusted only once it has been seen to refuse something, and a deviation clause with no
  refusal case retires the rule it is attached to. Stating the condition alone was the alternative
  and was rejected. **No phase was started on this answer**
  ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)): it settles what `specify`
  owes, and the work is done when it is asked for.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Collect the cases the rule has actually decided, from the tasks that cite it — both the second writes it **refused** and the ones it **allowed**. Drafting a refusal case out of imagination is how a clause ends up refusing only what nobody wanted. | A short list recorded in §3, each case naming the task and what the rule said there |
| 2 | From that list, pick the **refusal case** the clause must name, and check it is one somebody would genuinely propose. A refusal nobody could have asked for is a description, not a limit. | The chosen case, recorded in §3 with the ones passed over and why |
| 3 | Draft the amendment in `plugin/skills/taskmd/docs/METHOD.md` §4 — purpose, deviation condition, refusal case — in place, in the subsection that already states the rule. | The amended §4 |
| 4 | Classify the two tolerances that already exist: T-012's permitted second write of a derived inverse, and the two METHOD rules `CLAUDE.md` restates verbatim (T-047). Say of each whether it is an instance of the new clause or stands on its own ground. | A classification per tolerance, recorded in §3, and whatever §4 must say for a reader to reach the same answer |
| 5 | Read the rule's **other statements** against the amended text, one document at a time — `CLAUDE.md`'s *one design rule*, `docs/SCOPE.md` §2 principle 1, `docs/SCOPE.md` §2 principle 2. Correct what now contradicts; record the finding for each even where it is *no change needed*. | A per-document finding in §3, plus any edits those findings require |
| 6 | Decide whether `CLAUDE.md`'s pointer changes, against the headroom `python tests/test_budget.py` reports rather than against a guess, and re-run the suite after any edit. | The decision recorded in §3 with the measured figure, and the suite's output |
| 7 | **Use the amended rule on a case it was not written from** — settle one real design question by reading the sentence alone, and one the sentence must refuse. This is the phase's exit criterion, and the two-direction shape is T-151's. | Both applications written out in §3, each naming the case, the words that decided it, and the answer |
| 8 | Run the project's gates and quote them. | `taskmd index`, `taskmd check` and `python tests/test_budget.py` output, in §3 |

**Deliverable shape — decided at `plan`, 2026-08-21.** The amendment is written **into §4's
*Store the forward edge; derive the rest* subsection, in place**. *Rejected: a new subsection beside
it*, because a reader who reaches the rule and stops reading would then have the unamended rule —
splitting a rule from the condition under which it yields is the second-home shape the rule itself
refuses. *Rejected: stating it in `plugin/skills/taskmd/docs/method/rationale.md` and pointing*,
because rationale is loaded when a rule **looks wrong** (METHOD §7) while a deviation condition is
applied while a design is being **chosen**; putting it there costs a tier-3 load at the moment it is
needed, and hides it from everyone who never doubts the rule.

**Outputs this task will produce** (plain paths — at `plan` none of them is written yet):
- plugin/skills/taskmd/docs/METHOD.md
- CLAUDE.md — only if step 6 decides so
- docs/SCOPE.md — only if step 5 finds a contradiction

## 3. Implement

### Steps 1-2 — the cases the rule really decided, and the refusal case chosen from them

Read out of the tasks that cite the rule, so the clause is drafted against decisions rather than
against imagination. **Second writes the rule refused:**
[T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) (four exit criteria stated verbatim in
two places), [T-027](T-027-give-the-design-rule-one-home.md) (this rule itself, in three documents),
[T-072](T-072-give-the-description-and-version-one-home-each.md) (plugin description and version, in
two manifests), [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) (a
label-to-version mapping table, deleted rather than extended). **Second writes it allowed:**
[T-012](T-012-decide-whether-soft-edges-are-symmetric.md) (a derived inverse, at both ends),
[T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) (a shared heading over
different content is not a restatement),
[T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md) (the ordering rule described in a
binding, the owner's call),
[T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md) (one wider
rule and one narrower one, so not one fact twice).

**D1 — the refusal case is T-072's shape, generalised: a limitation assumed rather than demonstrated
— 2026-08-21.** T-072's own finding *granted* the deviation in advance, in the words "where the
packaging genuinely requires two". Then it ran `claude plugin validate .` against four manifests and
found both fields optional, so both copies went. That is the strongest refusal case available here,
because the exception was believed by the person best placed to know and was still wrong. *Passed
over: convenience, and "it reads better in both places"* — real, but nobody has ever mistaken either
for a system limitation, so refusing them would be the clause refusing what nobody would ask for,
which is the failure §1 names.

**D2 — the qualifying case is stated generically, and its instance stays in the tasks — 2026-08-21.**
`METHOD.md` names no file, no field and no command (its own opening line), and it ships to adopters.
So §4 says *a configuration that replaces a default instead of extending it*; the instance behind
that phrase is this project's own, in [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
and [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), and it is not
carried into the method.

### Step 3 — the amendment

Three paragraphs added to `plugin/skills/taskmd/docs/METHOD.md` §4's *Store the forward edge; derive
the rest*, after the sentence that already states the general rule: **what the rule is for**, **a
limitation of the system is grounds to deviate**, and **a limitation you assumed does not qualify**.

**D3 — the purpose paragraph was rewritten mid-step because the first draft was a second licence —
2026-08-21.** It ended "the question to put to a proposed second write is what it costs and what it
buys", which reads as permission to deviate whenever the trade looks worthwhile — the clause
swallowing the rule by the other door, while the door §1 was watching stayed shut. It now says
outright that knowing the purpose is not a second way to deviate, and that there is exactly one
grounds. Recorded because the first draft passed a reading of §1's open question and still failed it.

### Step 4 — the two existing tolerances, classified

| Tolerance | Instance of the new clause? | Why |
| :--- | :--- | :--- |
| [T-012](T-012-decide-whether-soft-edges-are-symmetric.md)'s second write of a derived inverse | **No** | Nothing compels it. The clause covers writes a system *forces*; this one is merely permitted and collapses to one link. §4's new first paragraph says so in a clause, so the two adjacent paragraphs cannot be read as one |
| The two METHOD rules `CLAUDE.md` restates verbatim ([T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)) | **No, and not a tolerance at all** | METHOD §3 deliberately does **not** state them, saying a copy there "would be a second home for a rule that must have one". Tier 1 is their only home, so there is no second write to excuse |

### Step 5 — the rule's other statements, one document at a time

| Statement | Finding |
| :--- | :--- |
| `CLAUDE.md` *The one design rule* | **No change needed.** Its pointer already promises §4 states "what the word *requires* below does and does not forbid" — a deviation condition is exactly that, so the sentence covers the amendment without being touched |
| `docs/SCOPE.md` §2 principle 1 | **Corrected.** It said the case where the distinction bites "is the inverse of a link … what the rule does and does not forbid **there** is stated once, in METHOD.md §4". True when T-045 wrote it; false the moment §4 gained a clause about facts in general. The pointer now names both, and T-045's decision — that §2 points and does not state — is untouched |
| `docs/SCOPE.md` §2 principle 2 | **No change needed.** T-045 already established its body is prior-art evidence about GitHub and Notion, not a restatement of the rule; the amendment does not reach it |
| `METHOD.md` §1 rule 3 | **No change needed.** It states the rule and defers with "(§4)". That is the same shape it had before, when §4 already permitted a second write |
| `docs/SCOPE.md` §3, R-1 | **No change needed.** R-1 is narrower than the principle — "every fact **about a task**" — and §3's own note says so. The tool derives; nothing in the amendment touches what R-1 asserts |

### Step 6 — `CLAUDE.md`, decided against the measured figure

```
tier 1 6451 chars under by 1403 (bound 7854, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
```

**D4 — `CLAUDE.md`'s pointer does not change — 2026-08-21.** The figure is unchanged from before this
task because the file is unchanged, and **1403 characters of headroom mean the budget did not force
the decision** — which is the half worth saying, since a "no change" that was really a budget refusal
would read identically. It stands on step 5's first row: the pointer's existing wording already
promises what §4 now delivers.

### Step 7 — using the amended rule on cases it was not written from

**Case A — it must refuse, and does.** [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md):
the local ordering rule lives in `plugin/skills/taskmd/taskmd/cli.py` and is now also described in
the GitHub-issues binding. Read the clause: no system offers no way to record this once — pointing at
the code was available, and T-179's own record names it as the rejected alternative. **So the clause
refuses this second write.** T-179 stands anyway, because the owner allowed it on a different ground
entirely — that reading Python to learn the one behaviour deciding what people work on costs the
reader too much. **The clause is silent on it rather than reversing it**, and that is the result
worth having: the ruling that *prompted* this amendment is not covered by it, so the clause did not
quietly grow to fit the case beside it.

**Case B — it permits, and finds the obligation already discharged.** `plugin/bin/taskmd` and
`plugin/bin/taskmd.cmd` exist as two files for one entry point. The clause permits it, and its second
sentence — *say, where a reader meets the second copy, what forces it* — is already satisfied:
`taskmd.cmd` opens by saying no single name is typeable on both platforms. Written well before the
clause existed, and it is the clause's obligation in the clause's own shape.

**Case C — it fires on something nobody had noticed.** `.claude-plugin/marketplace.json` →
`plugins[0].name` is `taskmd`, and so is `plugin/.claude-plugin/plugin.json` → `name`. One fact, two
homes, the second resting on the belief that the entry needs it. T-072 tested description and version
against `claude plugin validate` and deleted both; **it did not test `name`.** By the refusal case
this is an assumed limitation and does not qualify. Raised as
[T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md) rather than
fixed here (`CLAUDE.md`, *surface what you discover*) — and its firing on the first repository it was
pointed at is what the exit criterion asks for, since a clause that had only ever agreed with us
would have been worth nothing.

### Step 8 — the gates

Run after T-207 and this record were written, not before:

```
taskmd index    Wrote tasks/README.md - 12 active, 195 closed
taskmd check    OK - 207 task(s), 1035 field value(s), 3478 front-matter value(s), 688 reference(s),
                24 dependency edge(s), 306 declared output(s), 1 index file(s), 195 closed record(s),
                239 document(s), 2755 link(s), 4391 table row(s), 2 template(s), ...     exit 0
test_budget.py  Ran 8 tests in 0.027s  OK
                tier 1 6451 chars under by 1403 (bound 7854, reference/TASK-WORKFLOW.md)
```

**Outputs produced**
- `plugin/skills/taskmd/docs/METHOD.md` — §4, three paragraphs
- `docs/SCOPE.md` — §2 principle 1's pointer

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The rule states what it is for | met | §4's *What the rule is for* names both costs the rule holds down — inconsistency and administration — in the owner's own terms. Falsification test applied: the subsection cannot now be read through without meeting them |
| It states the deviation condition in terms a reader can apply | met | Applied three times in step 7 without an argument from first principles: refused Case A, permitted Case B, fired on Case C. The falsification test is that settling a case still needs first principles, and none of the three did |
| It names at least one case that does not qualify | met | *A limitation you assumed does not qualify — only one you were refused.* Case C is a live member of that class in this repository, so the class is demonstrably non-empty — which is the half a refusal clause usually cannot show |
| Each tolerance that already exists is classified | met | Step 4's table. T-012's is **not** an instance (nothing compels it); T-047's pair is **not a tolerance at all**, because METHOD §3 declines to state those rules and tier 1 is their only home. A reader can tell which from §4's first new paragraph and METHOD §3 respectively |
| Whether `CLAUDE.md`'s pointer changes is decided against a measured figure | met | D4 cites `tier 1 6451 chars under by 1403`, and says the headroom means the budget did **not** force the answer — so a "no change" cannot be misread as a budget refusal. Suite green after the change |
| The rule's other statements do not contradict the amended one | met | Step 5, five rows, one document at a time. One correction (`docs/SCOPE.md` §2 principle 1), four reasoned no-changes. Two of the five — METHOD §1 rule 3 and SCOPE §3 R-1 — were outside the criterion's own list and were read anyway |
| Nothing the rule has already settled is reversed | met | The sharpest evidence is Case A: the clause **refuses** T-179, the ruling that prompted it, and T-179 stands on the ground its own record gives. Nothing in the amendment tells anyone to revisit a decision, and the change writes no fact to a second home — the SCOPE edit removed a narrowing, it did not add a statement |

**Child fix tasks raised**
- none. [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md) came
  out of `implement` step 7 and is **not** a child of this task: every criterion here is met, and
  what it carries is the repository's conformance to the new clause rather than a gap in the clause.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | (no change) | **Criterion 6 was judged against `docs/SCOPE.md` §2's principles and did not reach §2's own header, which is a statement about the rule too.** The header says §2 points at `METHOD.md` only where a principle *also* holds as a **narrower** rule about how work is tracked; the clause §3 added is neither narrower nor about tracking, so principle 1's new pointer does not meet the condition the header sets for having one. Found after this task closed, by re-reading §2 whole. **The verdict rows are left as written** — they say what this task judged and against what — and the residue is [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md), which is a **decision** rather than a repair: every available fix presumes an answer about which document the clause belongs in, and that is the owner's. [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) predicted this in as many words and nobody re-read it. |
| 2026-08-21 | → done | `review`: **seven criteria, seven met, no child fix task.** The one that carries the others is the last — the clause refuses [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md), which is the ruling it came from, so it did not grow to fit the case beside it. **The refusal class is not empty**, which is the thing a deviation clause usually cannot show: `plugins[0].name` is a live member and is now [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md). T-207 is **not** a child of this task — nothing here is unmet — it is the repository's conformance to a rule this task wrote. `specify` → `review` in one session under the grant below. |
| 2026-08-21 | (no change) | `implement` done under the grant below. §4 gains three paragraphs; `docs/SCOPE.md` §2 principle 1's pointer is corrected because the amendment made its narrowing false. **The verification is step 7 and it produced three different answers** — the clause refused [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md), the very ruling that prompted it; permitted the two launcher shims and found their obligation already discharged; and fired on `plugins[0].name`, a second copy nobody had tested, now [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md). One decision was reversed mid-step and is recorded as D3: the first draft of the purpose paragraph was itself a second licence to deviate. |
| 2026-08-21 | (no change) | `plan` done under the grant below. Eight steps. **The riskiest thing is first**: the refusal case is collected from decisions the rule really made (steps 1–2) rather than invented at the point of drafting, because a clause that refuses only what nobody would ask for is the failure `specify` names. Step 7 is the phase's exit criterion made concrete — the rule is *used*, in both directions, on a case it was not written from. The deliverable's shape is recorded above with two rejected alternatives. |
| 2026-08-21 | (no change) | `specify` done under the grant below. Seven acceptance criteria, each with what would falsify it. **One scope item was added rather than assumed**: `docs/SCOPE.md` §2 principles 1 and 2 state this rule as well, and §1's in-list named only `CLAUDE.md`'s pointer — an amendment leaving a second statement asserting the unamended rule is a contradiction METHOD rule 5 already forbids, so the third home is read at `implement` and the finding recorded per document. **It widens what is read, not what is written**, and the likely finding is that SCOPE §2 already delegates this exact boundary to METHOD §4 in as many words. Surfaced here rather than fixed silently (`CLAUDE.md`, *surface what you discover*). |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** the next steps by the project's own ordering rule, each through its **full lifecycle**. Resolved against `taskmd list --open` on 2026-08-21, the grant is [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), then [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md), then [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) — **these three and no others.** Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **What the grant skips, and why, so nobody reads the order as arbitrary**: T-182, T-199, T-202, T-203 and T-206 each carry a live open question that is the owner's, and T-176 needs an uninvolved reader, who is a person and not a session. T-191 and T-198 are audit umbrellas that close when their children do, so neither is work to start. **This one is first** because it is first by that ordering and its own open question was answered on 2026-08-21, with the record saying in as many words that the work is done when it is asked for. It is now asked for. |
| 2026-08-21 | (no change) | **Answered by the owner: the amendment must name a case that does not qualify.** Stating the deviation condition alone was offered and rejected, on [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s ground - a rule trusted without having refused anything is a licence. §1's question is struck through with both. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised from the owner's answer to [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md), given in the backlog-wide question round of 2026-08-19. `high` because the rule is the one every design decision here is checked against, and an unwritten deviation condition is currently settled by argument each time. **Not covered by any standing authorisation** — the round of 2026-08-19 answered questions and authorised [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) alone. |
