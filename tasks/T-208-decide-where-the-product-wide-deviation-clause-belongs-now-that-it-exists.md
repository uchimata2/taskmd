---
id: T-208
title: Decide where the product-wide deviation clause belongs now that it exists
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-187, T-045, T-027]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-21
updated: 2026-08-22
adopter_visible: no
deliverables: [docs/SCOPE.md]
---

# T-208 — Decide where the product-wide deviation clause belongs now that it exists

## 1. Specify

**Outcome**
A decided, written answer to whether the deviation clause
[T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) added belongs in
`plugin/skills/taskmd/docs/METHOD.md` §4, and `docs/SCOPE.md` §2 brought back into agreement with
whichever answer is given — including §2's own header, which currently describes a pointer this
repository no longer only has.

**Why this one**
**Found after T-187 closed, by applying that task's own criterion 6 one paragraph wider.** That
criterion asked that the rule's other statements not contradict the amended one, and it was judged
against `docs/SCOPE.md` §2 **principles 1 and 2**. It did not reach §2's **header**, which says:

> They govern the **whole product** … which is why they are stated here in full rather than pointed
> at. Where a principle *also* holds as a narrower rule about how work is tracked, `METHOD.md` states
> that version and this section points at it.

So §2 points at METHOD **only for a narrower, tracking-scoped version of a principle**. T-187's clause
is not narrower and is not about tracking: it is the product-wide rule's exception, and principle 1
now points at METHOD §4 for it. That is the header's condition unmet.

**[T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) said this in advance
and nobody re-read it.** Its §3 records the pointer being written to name *what case* METHOD §4
covers — the inverse of a link — "rather than implying METHOD states the qualification for facts in
general, **which it does not**". Since 2026-08-21 it does. The premise under a decided task expired,
and the only reason it was noticed is that T-187 edited the sentence resting on it.

**The deeper question is which document is the clause's home**, and T-187 did not ask it. METHOD.md's
own first line is *how work is tracked*, and §4 is *Edges*; `docs/SCOPE.md` §2 is where the
product-wide rule is stated in full, by that section's own explanation of itself. T-187 placed the
clause in METHOD on the strength of the owner's phrase *the rule's own home* and `CLAUDE.md`'s
pointer, both of which name §4 — and neither was written when a product-wide exception existed.

**It is a decision and not a fix**, which is why it is raised rather than repaired: every available
repair presumes the answer.

**Scope**
- In: where the clause lives — METHOD §4 as it stands, `docs/SCOPE.md` §2 principle 1, or both with
  one pointing
- In: `docs/SCOPE.md` §2's header, made true of whatever §2 then does
- In: whether `CLAUDE.md`'s pointer still says something true afterwards, judged against the tier-1
  figure rather than assumed
- Out: the **wording** of the clause, which T-187 settled and which this does not reopen. Its purpose,
  its condition and its refusal case stand wherever it ends up
- Out: T-045's decision that §2 **points** rather than states a narrower rule. That holds; what has
  changed is that a wider one now exists, which its wording did not anticipate

**Inputs**
- [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) §3 step 5 — the
  per-document read that reached principles 1 and 2 and stopped
- [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) §3 — the sentence-by-sentence
  boundary, and the premise that expired
- `docs/SCOPE.md` §2 — the header and principle 1
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the clause as written, and §1 rule 3 which defers to it

**Acceptance criteria**

Written on 2026-08-22, once the owner's answer fixed which repair they judge. The decision itself is
recorded and is not one of these: what remains is `docs/SCOPE.md` §2's header, and showing that
nothing else rested on the sentence it replaces.

- [ ] **§2's header is true of principle 1 as principle 1 now stands.** A reader who applies the
      header to that principle finds no pointer the header does not license. What failure looks like:
      the header still licenses only a *narrower rule about how work is tracked*, while principle 1
      points at METHOD §4 for a product-wide exception that is neither narrower nor about tracking
- [ ] **The header is checked against every principle in §2, and the check is shown** — not against
      the one that prompted this. A header is a claim about its section, and this task exists because
      [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md)'s criterion was
      judged against two named principles and never reached the header above them. Judging the repair
      the same narrow way would be the same mistake one turn later
- [ ] **The header names the kind of thing METHOD may hold on a principle's behalf, and that kind
      covers a product-wide exception.** A header widened only far enough to admit T-187's clause by
      name leaves the next widening to re-open this silently, which is the failure mode
      [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md)'s wording
      already demonstrated once
- [ ] **Principle 1's own wording is unchanged**, shown by a diff — the owner's answer confines the
      repair to the header, and a principle edited to fit its header would be the decision reversed
      without being re-asked
- [ ] **The clause in `plugin/skills/taskmd/docs/METHOD.md` §4 is byte-identical afterwards**, shown
      by a diff. Its wording is out of scope and this task must be able to prove it did not drift
- [ ] **T-045's decision is left standing and the record says so.** §2 still *points* rather than
      stating a narrower rule; what changed is that a wider one now exists, which T-045's wording did
      not anticipate. What failure looks like: a header that reads as reversing T-045, so the next
      reader cannot tell which of the two decisions is live
- [ ] **`CLAUDE.md`'s pointer is shown still true, not assumed true** — §4 is read and confirmed to
      state what the pointer promises about the word *requires*. If `CLAUDE.md` is edited at all, the
      tier-1 figure is re-measured by running the suite and the number is stated
- [ ] `check` is clean and the suite passes

**Open questions**
- ~~**Where does a product-wide qualification belong — `METHOD.md` §4, or `docs/SCOPE.md` §2
  principle 1?** **The owner decides**, because it is the placement of the rule every design decision
  here is checked against and the two documents have different audiences: METHOD ships to adopters and
  says it is about *how work is tracked*; SCOPE is this project's own and says its principles govern
  the *whole product*. **Recommended: leave the clause in METHOD §4 and widen §2's header**, on the
  ground that an adopter reading METHOD is the reader who most needs it and is the one reader SCOPE
  never reaches — `CLAUDE.md`'s pointer already promises §4 states what the word *requires* does and
  does not forbid, so moving it would falsify tier 1 as well. *The cost if that is wrong*: METHOD
  carries a product-wide rule under a heading about edges, and §2's explanation of why it states
  things in full gets a second clause. *The alternative*: state the clause in §2 principle 1 and have
  METHOD §4 point up at it — truer to each document's stated scope, and it moves the clause out of
  everything an adopter receives, which is the half that made T-187 write the case generically in the
  first place.~~ **Answered by the owner on 2026-08-22: the clause stays in `METHOD.md` §4, and `docs/SCOPE.md` §2's header is widened** — see the Log row of that date.
- **None outstanding.** The acceptance criteria above were written after the answer, so they judge the
  repair the owner chose rather than the choice.

## 2. Plan

**Sequencing.** Step 1 is first because it decides whether the repair is the one the criteria
assume. The header is a claim about §2, so what §2's principles actually delegate has to be read
before anything is written — and this task exists because a criterion was judged against two named
principles and never reached the sentence above them.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read **each** of §2's three principles and record what it delegates to `METHOD.md`, if anything, and at what scope. Not principle 1 alone. | A table in §3, one row per principle: what it delegates, at what scope, and whether the header as it stands licenses that |
| 2 | Write the header so it names the **kind** of fact `METHOD.md` may hold on a principle's behalf, with the scope left open rather than widened to fit the one qualification that prompted this. | The edited header in `docs/SCOPE.md` §2 |
| 3 | Re-run step 1's table against the **new** header, so the check that found the defect is the check that judges the repair. | The same table, second column of verdicts, in §3 |
| 4 | Show the two things the owner's answer confines this task away from are untouched: principle 1's wording, and the clause in `plugin/skills/taskmd/docs/METHOD.md` §4. | Two diffs quoted in §3, both empty |
| 5 | Read `METHOD.md` §4 and judge `CLAUDE.md`'s pointer against it — does §4 state what that pointer promises about the word *requires*? Edit `CLAUDE.md` only if the answer is no. | A recorded finding in §3; if `CLAUDE.md` is edited, the re-measured tier-1 figure from the suite |
| 6 | Run the gates and sweep what the change made stale. | `index`, `check` and the suite output quoted in §3 |

**Shape of the deliverable, decided — 2026-08-22.** The header is **one edit to `docs/SCOPE.md` §2's
opening paragraph**, and nothing else moves. *Rejected: a fourth principle stating the delegation
rule*, which promotes a note about where facts live to the status of the three rules every
requirement is an application of. *Rejected: a footnote under principle 1*, which puts a claim about
the whole section under one of its members — the exact shape that let the current defect through,
since a reader checking principle 1 would find the note and a reader checking the section would not.

**Outputs** — plain paths:

- docs/SCOPE.md

## 3. Implement

### Step 1 — what each principle actually delegates

Read per principle, from the section rather than from the one that prompted this. The pointers are
counted out of §2's numbered list rather than by eye:

```text
One home per fact.                       METHOD pointers: 1  ['METHOD.md']
Store the forward edge, derive the rest. METHOD pointers: 0  []
Point, don't restate.                    METHOD pointers: 0  []
```

| Principle | What it delegates | At what scope | Old header licensed it? |
| :--- | :--- | :--- | :--- |
| 1. One home per fact | What the word *requires* does and does not forbid: the inverse-of-a-link case, and the grounds on which the rule yields to a system limitation | **product-wide** | **No.** It licensed only *a narrower rule about how work is tracked* |
| 2. Store the forward edge | nothing — stated in full, with GitHub and Notion cited as evidence | — | n/a |
| 3. Point, don't restate | nothing — stated in full | — | n/a |

**The old sentence described a pattern no principle follows, which is worth more than the defect it
was raised for.** It said *where a principle also holds as a narrower rule about how work is tracked,
`METHOD.md` states that version and this section points at it*. Principle 2 is exactly that case —
its narrower version is `METHOD.md` §4's own heading — and principle 2 **states it in full and points
at nothing**. So the sentence licensed a delegation nobody makes, and failed to license the only one
anybody does. Repairing it to fit principle 1 alone would have left the same shape.

### Step 2 — the header

One edit, to §2's opening paragraph. It names the **kind** of fact `METHOD.md` holds on a
principle's behalf — *a principle's boundary cases, and the grounds on which it yields* — and leaves
the **scope open** rather than widening it to admit the clause that prompted this. It says in its
own words why: a header widened just far enough is one the next qualification re-opens in silence.

### Step 3 — the same check against the new header

| Principle | Delegates | New header licenses it? |
| :--- | :--- | :--- |
| 1. One home per fact | a product-wide boundary case and a product-wide grounds to yield | **Yes** — both are *boundary cases* and *grounds on which it yields*, at a scope the header does not fix |
| 2. Store the forward edge | nothing | **Yes**, vacuously — and the first sentence still says why the rules themselves are stated in full, which is what principle 2 does |
| 3. Point, don't restate | nothing | **Yes**, vacuously, on the same sentence |

**The header is now true of a principle that delegates nothing and of one that delegates a
product-wide qualification, and it fixes no scope in between.** That is what stops the third case —
whatever it turns out to be — arriving as a defect.

### Steps 4 — the two diffs, both empty

```text
git diff -- plugin/skills/taskmd/docs/METHOD.md      (no output)
principle 1 identical: True
```

The clause T-187 wrote is byte-identical, and principle 1's wording is byte-identical — compared
against `git show HEAD:docs/SCOPE.md` rather than by reading it, because the point of the criterion
is that reading is what let the header through in the first place. `docs/SCOPE.md`'s whole diff is
one hunk, and it is the header.

### Step 5 — `CLAUDE.md`'s pointer, read rather than assumed

```text
CLAUDE.md:25  **Store the forward edge; derive the rest.** Stated in full - including what the word
CLAUDE.md:26  *requires* below does and does not forbid - in `.../METHOD.md` §4.
```

§4 states the rule in full, then *what the rule forbids is a design that compels the second write*,
then the purpose, then the limitation clause and the case it turns away. So the pointer promises what
§4 delivers and is **still true**. `CLAUDE.md` is not edited, so no tier-1 figure moves — and
`tests/test_budget.py` runs in the suite below either way rather than being reasoned about.

### Step 6 — the gates, and the sweep

```text
Wrote tasks/README.md - 11 active, 200 closed
OK - 211 task(s), ... 243 document(s), 2901 link(s), ... 3448 section reference(s)
317 passed, 8 subtests passed in 51.43s
```

**The sweep found one live pointer at the sentence that was replaced, and it is inside this task's
own §1**, which quotes the old header as evidence for why the task exists. That is a statement about
the past and METHOD rule 5 says to leave it. Nothing else in the tree quotes or paraphrases the
sentence: `check` resolves every link and every section reference in `docs/`, and the only other
documents naming §2's delegation are closed task records describing what they decided at the time.

**Decisions & assumptions**

- **The header names a kind and leaves the scope open** — *a principle's boundary cases, and the
  grounds on which it yields*, at whatever scope they hold. Rejected: widening it to *narrower or
  product-wide*, which is an enumeration of the two scopes that exist today and expires the same way
  the sentence it replaces did — 2026-08-22.
- **One edit, to §2's opening paragraph.** Rejected: a fourth principle stating the delegation rule,
  which promotes a note about where facts live to the rank of the three rules every requirement is an
  application of; rejected: a footnote under principle 1, which puts a claim about the section under
  one of its members — the shape that let this defect through, since a reader checking principle 1
  would find it and a reader checking the section would not — 2026-08-22.
- **T-045's decision is restated as standing, in the header itself** rather than only in this record,
  because the next reader of §2 is the one who has to know which of the two decisions is live —
  2026-08-22.
- **`CLAUDE.md` is not edited**, so no tier-1 measurement moves. Its pointer was judged by reading
  §4 against what the pointer promises, not by assuming the clause's placement kept it true —
  2026-08-22.

**Outputs produced**

- docs/SCOPE.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| **§2's header is true of principle 1 as principle 1 now stands** | met | §3 step 3, row 1. Principle 1 delegates a product-wide boundary case and a product-wide grounds to yield; the header licenses *a principle's boundary cases, and the grounds on which it yields*, at a scope it does not fix |
| **The header is checked against every principle in §2, and the check is shown** | met | §3 steps 1 and 3, three rows each, and the METHOD-pointer count is computed out of the section rather than read by eye. The check against the old header is what found that the sentence described a pattern **no** principle follows — principle 2 is its stated case and points at nothing |
| **The header names the kind of thing METHOD may hold, and that kind covers a product-wide exception** | met | It names *a principle's boundary cases, and the grounds on which it yields*, and says the scope is left open on purpose with the reason. T-187's clause is not named in it |
| **Principle 1's own wording is unchanged**, shown by a diff | met | `principle 1 identical: True`, compared against `git show HEAD:docs/SCOPE.md`. The whole `docs/SCOPE.md` diff is one hunk and it is the header |
| **The clause in METHOD §4 is byte-identical afterwards**, shown by a diff | met | `git diff -- plugin/skills/taskmd/docs/METHOD.md` produced no output |
| **T-045's decision is left standing and the record says so** | met | The header itself says it: *whose decision stands: this section points and does not state*, with what its wording did not anticipate stated beside it — so the next reader of §2 can tell which decision is live without opening a task |
| **`CLAUDE.md`'s pointer is shown still true, not assumed true** | met | §3 step 5 quotes the pointer and names what §4 actually states against it. `CLAUDE.md` is not edited, so no tier-1 figure moves; `tests/test_budget.py` ran in the suite regardless |
| `check` is clean and the suite passes | met | `OK - 211 task(s), ...` and `317 passed, 8 subtests passed` |

**What this does not settle.** The header is judged against the three principles §2 has today. A
fourth would be judged against it by whoever writes it, and nothing mechanical reads the header — the
per-principle table above is a person's check, run twice, and this record is the only place it exists.

**Open questions, re-read before closing.** §1 recorded none outstanding: the one it had was answered
by the owner on 2026-08-22 and the criteria were written after that answer. Nothing in §3 raised a
question for the owner — the finding about principle 2 widened the *reason* for the repair, not the
repair.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* immediately after [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) closed, by re-reading `docs/SCOPE.md` §2 whole rather than the two principles that task's criterion named. `high` because it is the placement of the one rule every design decision here is checked against, and `s` because the argument is written and only the choice is missing. **Not covered by the grant T-187 ran under**, which reached three named tasks and nothing any of them raised. It carries an open question that is the owner's, so nothing starts on it. |
| 2026-08-22 | (no change) | **The open question is answered by the owner: leave the clause in `METHOD.md` §4 and widen `docs/SCOPE.md` §2's header.** Asked in the batched round of 2026-08-22, and it is the recommendation §1 carried. An adopter receives METHOD and never receives SCOPE, so they are the reader who most needs the clause; `CLAUDE.md` already promises §4 states what *requires* does and does not forbid, so moving it would falsify tier 1 as well. *Rejected: state it in §2 principle 1 and have METHOD §4 point up*, truer to each document's stated scope, but it moves the clause out of everything an adopter receives — the half that made [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) write the case generically — and falsifies `CLAUDE.md`'s pointer too. The known inconsistency in §2's header is now repairable, but repairing it is this task's work and is not authorised by this row. |
| 2026-08-22 | → done | **All eight criteria met. `docs/SCOPE.md` §2's header now names a kind — *a principle's boundary cases, and the grounds on which it yields* — and leaves the scope open, saying in its own words why a header widened just far enough is one the next qualification re-opens.** **Checking it against every principle found more than the defect it was raised for**: the old sentence licensed *a narrower rule about how work is tracked*, and principle 2 is exactly that case and points at nothing, so the sentence licensed a delegation nobody makes while failing to license the only one anybody does. Repairing it to fit principle 1 alone would have left the same shape. **Both confinement criteria are shown by comparison rather than by reading**: `git diff` on METHOD.md is empty and principle 1 is byte-identical against `git show HEAD`, which matters because reading is what let the header through in the first place. `CLAUDE.md`'s pointer was judged by reading §4 against what it promises and is still true, so tier 1 does not move. `check` OK over 211 tasks, 317 tests passed. |
| 2026-08-22 | → planned | **Plan written under the multi-phase grant recorded above.** Six steps, and **step 1 is a per-principle read rather than a repair**, because the header is a claim about §2 and this task exists precisely because a criterion was judged against two named principles and never reached the sentence above them. Step 3 re-runs that same table against the new header, so the instrument that found the defect is the one that judges the repair. Two steps are diffs that must come out empty — principle 1's wording and METHOD §4's clause — because the owner's answer confines the repair to the header. **The deliverable's shape is decided with its rejections**: one edit to §2's opening paragraph; a fourth principle was rejected as promoting a note about where facts live to the rank of the three rules, and a footnote under principle 1 was rejected because putting a claim about the section under one of its members is the shape that let this defect through. Phase stays at `plan` until `implement` runs. |
| 2026-08-22 | → specified | **Specify agreed: eight criteria written, where §1 had carried a placeholder.** They judge only what the owner's answer leaves to do — `docs/SCOPE.md` §2's header — and they say twice, in different words, that the header must not be repaired the narrow way. **That is deliberate and is this task's own lesson turned on itself**: T-208 exists because [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md)'s criterion was judged against two named principles and never reached the header above them, so a criterion here requires the header be checked against **every** principle in §2, and another requires it name a *kind* of thing rather than admit T-187's clause by name — a header widened to fit one clause re-opens this the next time the clause widens, which is exactly how [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md)'s wording expired. Two criteria are diffs — principle 1 and METHOD §4's clause must both come out byte-identical — because the answer confines the repair to the header and a task that widened anything else would have reversed a decision without re-asking. Phase stays at `specify`; `plan` is not authorised (METHOD §3.1). |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its outcome edits `docs/SCOPE.md` §2's header, which the live handoff names as not to be tidied by a reconcile sweep.** That instruction is aimed at a sweeping session; this grant is what makes the repair this task's own authorised work. |
