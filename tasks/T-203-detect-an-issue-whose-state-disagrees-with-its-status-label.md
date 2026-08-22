---
id: T-203
title: Detect an issue whose state disagrees with its status label
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-178, T-193, T-108]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-21
updated: 2026-08-22
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-203 — Detect an issue whose state disagrees with its status label

## 1. Specify

**Outcome**
The GitHub Issues binding's standing check can report an issue whose `state` contradicts its
`status:` label — so assumption 2 stops being a request nobody can enforce and becomes a condition
something notices.

**Why this one**
Raised by the owner on 2026-08-21, reading the binding's assumption 2: *Nobody on your project closes
or reopens an issue in the GitHub UI.* Their objection is the one the single-source-of-truth rule
makes: on this backend the answer to *is this task open?* is written in two places, and one of them
is a button.

**The hole is sharper than the assumption admits, and it is structural.** The binding says `state` is
*the one materialised derived view this binding has*, written from the `status:` label and only from
it. METHOD §4 allows a materialised derived view; what it does not allow is one that nothing
regenerates or reconciles. And **the standing check cannot see the divergence even in principle**:

- none of the nine rows of *Checking a backlog that is already here* compares `state` with the
  `status:` label;
- `enumerate` fetches `number,title,body,labels,parent,subIssues,blockedBy,blocking` and
  **deliberately does not fetch `state`** — assumption 2's own *no operation reads it*.

So the one procedure that could notice is looking away by design. The assumption is not merely
fragile; it is unenforceable by construction, and a click that breaks it leaves a task contradicting
itself with every view saying it is fine. **That is the same shape as
[T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md)'s duplicated index** —
a defect no validator could see because nothing read the place it lives.

**The interesting half is what *reading* `state` costs.** Assumption 2 exists to stop `state` being
read **as** the status — a rendering treated as the fact. Reading it **against** the fact is the
opposite move, and the binding's own text does not distinguish them. Whether that distinction
survives contact with the rest of the document is this task's question, not a detail.

**Requirements served**
R-9, R-16 (`docs/SCOPE.md`).

**Scope**
- In: whether `enumerate` fetches `state`, and what assumption 2 has to say once it does
- In: a row in *Checking a backlog that is already here* for the disagreement, if the answer is yes
- In: what the row tells a reader to do — the label is the fact, so the repair is to re-render
  `state`, and saying so is the difference between a check and a puzzle
- Out: **any change to how status is stored.** The `status:` label carries eight values and `state`
  carries two; making `state` the fact is not available and is not what this asks
- Out: reconciling automatically. Non-goal 10, and a check that silently repaired the thing it found
  would destroy the evidence that anybody clicked
- Out: the other bindings. `local-markdown` has no second place for this fact

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — assumption 2, *update*'s two-writes rule,
  *enumerate*, and the nine rows
- [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) §3 — the four runs, and
  which rows examined nothing
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the migration
  that established `state` as a rendering
- **A live backlog on GitHub — and it does not exist today.** Criteria 2 and 3 cannot be met by
  reading anything. [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) built
  `uchimata2/taskmd-standing-check-scratch` for its own run and left step 10 — deleting it — to the
  owner, because the token carries no `delete_repo` scope. That deletion has happened, measured on
  2026-08-22:

  ```text
  $ gh repo view uchimata2/taskmd-standing-check-scratch
  GraphQL: Could not resolve to a Repository with the name
  'uchimata2/taskmd-standing-check-scratch'. (repository)
  ```

  Credentials are present and sufficient — `gh auth status` reports account `uchimata2` with scopes
  `gist, project, read:org, repo, workflow`, so `repo` would create one. What is missing is not
  access but **permission**: creating a repository on the owner's account is an outward-facing act,
  and no grant here covers it. Recorded as an open question below rather than assumed, because
  specify treats an input nobody can reach as a dependency in disguise

**Acceptance criteria**
- [ ] The binding says whether `state` is fetched, and assumption 2 reads correctly beside that
      answer — a reader must not be able to conclude both *never read it* and *read it here*
- [ ] If a row is added, it is **run against a live backlog and made to fail** on an issue closed in
      the UI while its label says otherwise, with the output quoted — the standard
      [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) set
- [ ] It is shown **not** to fire on an issue whose `state` and label agree, in both directions —
      open with an open status, closed with a closed one
- [ ] The row says which side is the fact, so the repair is unambiguous
- [ ] Whether this makes assumption 2 removable is answered either way, and the answer is argued
      rather than asserted
- [ ] **The mapping is untouched, shown by a diff**: `state` is still written from the `status:`
      label, *update*'s two-writes rule reads as it did, and no vocabulary moves. The owner's answer
      of 2026-08-22 rejected both revisiting the mapping and dropping `state`, so a task that
      quietly did either would have taken a decision it was told not to take

**Open questions**
- ~~**Is a detected divergence enough, or does the mapping itself need revisiting?** The owner's wider
  point on 2026-08-21 was that taskmd on this backend should be a guardrail over `gh` rather than
  anything holding its own copy — which the binding already is. This task takes the narrow reading: a
  fact stored twice, with nothing checking the two agree. If the answer is that a rendering nobody
  can be stopped from editing should not be materialised at all, that is a larger decision and the
  owner's.~~ **Answered by the owner on 2026-08-22: report the divergence; the mapping is not revisited** — see the Log row of that date.
- **Raised at `specify` on 2026-08-22, and it blocks `implement` rather than the outcome: may a
  scratch repository be created on the owner's GitHub account for the run criteria 2 and 3 require?**
  **The owner decides** — it is an outward-facing act on their account, and the previous one is gone
  (see *Inputs*). **Recommended: yes, one private scratch repository, deleted by the owner
  afterwards** — the same arrangement
  [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) ran under, which worked and
  whose cleanup step the owner has demonstrably performed. *The cost if that is wrong*: a private
  repository exists on their account until they remove it, and this token cannot remove it for them.
  *The alternative*: meet the criteria against a **fixture** rather than a live backlog — cheaper and
  needs no permission, but the thing under test is what GitHub's API returns for `state`, so a fixture
  would be this repository's own belief about that API rather than the API, and criterion 2 says *run
  against a live backlog* for exactly that reason. **This does not stop `specify`** — the criteria are
  written and agreed, and the method holds that a question blocking only a later phase is noted and
  left open. **Answered by the owner on 2026-08-22, the same day it was raised: yes — one private
  scratch repository, deleted by them afterwards.** See the Log row of that date. `implement` is
  therefore no longer blocked on permission; it is blocked only on being asked for.

## 2. Plan

**Sequencing.** Step 1 is first and is the whole risk: the binding says in three places that nothing
reads `state`, and a row that reads it either contradicts them or is placed somewhere they do not
reach. Deciding *where* the fetch happens settles what has to be rewritten, and everything after it
is downstream. Steps 4-6 need the scratch repository, so step 3 comes before them and step 9 hands
it back.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide **which fetch** gains `state` — *enumerate*, the standing check's own fetch, or both — against the criterion that a reader must not be able to conclude both *never read it* and *read it here*. | A decision in §3 with its rejected alternative, and the list of every sentence in the binding that has to change to stay true |
| 2 | Write the row, and make the sentences from step 1 true beside it. | The edits to `plugin/skills/taskmd/docs/bindings/github-issues.md` |
| 3 | Create the private scratch repository the owner authorised on 2026-08-22, enable issues, and seed a backlog carrying **both agreeing directions** and the disagreement. | The repository, and its seeded issues listed in §3 |
| 4 | **Make the row fail.** Close an issue from outside taskmd while its `status:` label still says open, and run the row. | The failing output quoted in §3, naming the issue |
| 5 | Show it **silent** on an open issue with an open status and on a closed issue with a closed status — both directions, per criterion 3. | The silent run quoted in §3, with what it examined rather than only its verdict |
| 6 | Answer whether assumption 2 becomes removable, **argued from what steps 4-5 measured** rather than asserted. | The answer in §3 and in the binding, wherever assumption 2 ends up |
| 7 | Show the mapping untouched by diff: `state` still written from the `status:` label, *update*'s two-writes rule unchanged, no vocabulary moved. | The diff quoted in §3, restricted to what did change |
| 8 | Run the gates. | `index`, `check` and the suite output quoted in §3 |
| 9 | **Hand the scratch repository back by name**, because this token carries `repo` and not `delete_repo`. | The request, in §3 and in the closing report — the repository named in full |

**Shape of the deliverable, decided — 2026-08-22.** A **row in the standing check**, not a new
section and not a taskmd command. *Rejected: a `check` class*, which cannot reach a network — the
four commands' inability to do so is a decision this binding already records, not a gap. *Rejected:
a scheduled job or action*, which is automatic reconciliation and non-goal 10, and would also destroy
the evidence that anybody clicked.

**Outputs** — plain paths:

- plugin/skills/taskmd/docs/bindings/github-issues.md

## 3. Implement

### Step 1 — which fetch gains `state`

**Decided: the standing check's own fetch, and not *enumerate*.** The binding's rule is not that
`state` is untouchable; it is that nothing reads `state` **as** the status. *enumerate* answers
*which tasks exist and what are they*, so a `state` in its output sits within reach of every caller
who wants to know whether a task is open — which is the substitution the rule exists to prevent. The
standing check's fetch is a separate call made for one purpose, and row 10 reads `state` **against**
the label rather than instead of it.

*Rejected: fetch it in `enumerate` and let the row read from there*, one fetch instead of two and no
second command to keep in step — but it puts the rendering in the operation whose whole job is to
report what exists, and assumption 2's *no operation reads it* would have had to become *no operation
reads it except when it does*, which is the sentence criterion 1 forbids.

Three sentences had to change to stay true, and they are the whole of the edit besides the row:
assumption 2's *no view will flag it*, *enumerate*'s *no operation reads it*, and the standing
check's fetch command.

### Step 2 — the row and the three sentences

Row 10 added to *Checking a backlog that is already here*; the fetch above it gains `state` and says
it is the one field *enumerate* does not carry; *enumerate*'s paragraph now draws the read-as /
read-against distinction; assumption 2 keeps its warning and points at the row instead of saying
nothing will flag it.

### Step 3 — the live backlog

`uchimata2/taskmd-state-label-scratch`, private, issues enabled, created under the owner's answer of
2026-08-22. Four issues, chosen so that **both** agreeing directions and **both** disagreeing ones
are present — a fixture with only one disagreement would not have shown that the row reads in both
directions:

```text
1  OPEN    status:in_progress  Open issue with an open status
2  CLOSED  status:done         Closed issue with a closed status
3  CLOSED  status:specified    Closed in the UI while its label says open
4  OPEN    status:done         Reopened in the UI while its label says done
```

Issue 4 was closed and then reopened, so its state is the one a reopen actually produces rather than
one that was never closed.

### Step 4 — the row made to fail

```text
row 10 - state against the status: label, over 4 issue(s)
  STATE/LABEL  #4 state is OPEN while status:done is closed - the label is the fact; re-render
               state with gh issue close 4
  STATE/LABEL  #3 state is CLOSED while status:specified is open - the label is the fact; re-render
               state with gh issue reopen 3
examined 4 issue(s) carrying exactly one status: label; 2 disagreement(s)
```

Both directions named, each with the command that repairs it, and neither agreeing issue reported.

### Step 5 — silent when they agree

Repaired by the row's own instruction — `gh issue close 4`, `gh issue reopen 3` — and run again:

```text
  #1  state=OPEN   status:in_progress  agree
  #2  state=CLOSED status:done         agree
  #3  state=OPEN   status:specified    agree
  #4  state=CLOSED status:done         agree
examined 4 issue(s), both directions present; 0 disagreement(s)
```

**Both agreeing directions are present after the repair** — open with an open status at #1 and #3,
closed with a closed status at #2 and #4 — which is criterion 3, and the run says what it examined
rather than only that it passed.

### Step 6 — is assumption 2 removable?

**No, and the run is what says so rather than an opinion.** Row 10 answered only when it was run: the
backlog sat in the state of step 4 until a command was issued, and nothing on this backend would have
raised it. So the click still leaves a task contradicting itself; what has changed is that the
contradiction is now **findable** instead of invisible. The assumption changes kind rather than
disappearing — from a condition nobody can enforce into one that decays until somebody checks — and
assumption 2 is rewritten to say exactly that, with *or, if they do, you run the standing check
afterwards* in its first line.

**Removing it would have been the more attractive answer and is the wrong one**, because it would
leave a reader believing GitHub tells them, and nothing here is scheduled. The binding says so in the
same paragraph it says nothing here is automatic.

**A limit the run exposed, and the row now states it.** Row 10 compares against exactly one `status:`
label, so an issue with none or two is skipped — those are row 1's. A skip that said nothing would
make a badly-labelled backlog report the same *0 disagreements* as a healthy one, which is the exact
failure this document already names for rows 3 and 7. The row now requires the examined count to be
reported, and both runs above print it.

### Step 7 — the mapping untouched

```text
Mapping table identical: True
update section identical (update -> reference): True
find/read/create identical: True
enumerate's gh command line unchanged: True
status vocabulary lines changed: 0
```

Compared against `git show HEAD:` rather than read. **The first attempt at this said `False`** — the
slice ran from *update* to *After any write* and so contained *enumerate* and *order* as well, which
is the section that legitimately changed. A block comparison is only as good as its boundaries, and
the fix was to bound it at the next operation.

### Step 8 — the gates

```text
OK - 211 task(s), ... 243 document(s), 2901 link(s), ... 3479 section reference(s)
317 passed, 8 subtests passed
```

### Step 9 — the scratch repository, handed back

**`uchimata2/taskmd-state-label-scratch` still exists and this session cannot delete it.** `gh auth
status` reports scopes `gist, project, read:org, repo, workflow` — `repo` created it, and
`delete_repo` is absent, which is the same arrangement
[T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) ended on. **Deleting it is
the owner's**, and it is asked for by name here and in the session's closing report rather than left
as a note somebody might not read.

**Decisions & assumptions**

- **`state` is fetched in the standing check and not in *enumerate*** — the rule is that nothing
  reads `state` as the status, and the operation reporting what exists is exactly where a caller
  would substitute it. Rejected: one fetch in *enumerate*, cheaper, but it would have forced
  assumption 2 into *no operation reads it except when it does* — 2026-08-22.
- **Both disagreeing directions are seeded, not one** — a backlog with only the closed-but-labelled-
  open case would have passed a row that only ever compares one way — 2026-08-22.
- **The row requires the examined count** — a silent skip makes a mislabelled backlog score like a
  healthy one, which is this document's own lesson about rows 3 and 7 — 2026-08-22.
- **Assumption 2 stays, rewritten.** Rejected: removing it, which reads as *GitHub tells you* and
  nothing here is scheduled — 2026-08-22.
- **The repair is by hand.** Rejected: a row that re-renders `state` itself, which is non-goal 10 and
  destroys the only evidence that somebody clicked — 2026-08-22.

**Outputs produced**

- plugin/skills/taskmd/docs/bindings/github-issues.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The binding says whether `state` is fetched, and assumption 2 reads correctly beside that answer | met | The standing check's fetch carries `state` and says it is the one field *enumerate* does not; *enumerate*'s paragraph draws the read-**as** / read-**against** distinction; assumption 2 points at row 10. A reader can conclude *no operation reads it as the status* and *row 10 reads it against the status*, which are not the same sentence |
| The row is **run against a live backlog and made to fail**, with the output quoted | met | §3 step 4, on `uchimata2/taskmd-state-label-scratch`. Two named issues, in opposite directions, each with the command that repairs it |
| It is shown **not** to fire when `state` and label agree, in both directions | met | §3 step 5. After the repair all four agree — open/open at #1 and #3, closed/closed at #2 and #4 — and the run reports what it examined, not only its verdict |
| The row says which side is the fact | met | *The label is the fact*, in the row itself, with the repair being `gh issue close` / `gh issue reopen` and never a relabel |
| Whether assumption 2 becomes removable is answered either way, **argued** | met | §3 step 6: **no**, and the run is the argument — the backlog sat divergent until a command was issued, so the contradiction became findable rather than raised. The assumption is rewritten to say it decays until somebody checks |
| **The mapping is untouched, shown by a diff** | met | §3 step 7: the mapping table, the `update` section and `find`/`read`/`create` are all byte-identical against `git show HEAD:`, no status vocabulary line moved, and *enumerate*'s `gh` command is unchanged |

**What this does not settle.** Row 10 answers when somebody runs it, and nothing here schedules
anything — that is the binding's standing position for all ten rows, not a gap this task opened. And
the run is against GitHub.com; Enterprise Server is untested, as assumption 4 already says of the
whole binding.

**Open questions, re-read before closing.** §1 recorded two and both are answered — the mapping
question by the owner on 2026-08-22, and the scratch-repository permission by the owner the same day.
Neither is left live. **One obligation leaves this task open in the world rather than in the record**:
the scratch repository is the owner's to delete, asked for by name in §3 step 9.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised by the owner on 2026-08-21, from reading assumption 2 of the GitHub binding. `high` and `s`: the row is small and what it guards is the only fact this backend stores twice, in a place one click changes and nothing reads. The evidence that it is unenforceable rather than merely fragile came out of [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s run - `enumerate` does not fetch `state`, so no row could compare it even if one wanted to. |
| 2026-08-22 | (no change) | **The open question is answered by the owner: detecting the divergence is enough, and the mapping stands.** Asked in the batched round of 2026-08-22. METHOD §4 allows a materialised derived view but not one nothing reconciles, and a comparison of `state` against the `status:` label is that reconcile — reading `state` *against* the fact rather than *as* it. *Rejected: revisit the mapping first*, which avoids building a guard for something that might be removed, but leaves the hole open while it is decided and a click still leaves a task contradicting itself with every view reporting it fine. *Rejected: stop writing `state` at all*, which removes the second copy outright, but GitHub's own search, filters and UI read it, so the backlog gets harder to use in the tool people already have open. This row is the answer, not authorisation to start. |
| 2026-08-22 | → specified | **Specify agreed. The owner's answer is folded in, one criterion is added, and one new question is opened.** The added criterion pins the mapping by diff: the answer rejected both revisiting it and dropping `state`, and neither rejection was written anywhere a review would read, so a task that quietly did either would have passed. **The new question is a precondition, found by checking that this task's own criteria can be met.** Criteria 2 and 3 require a run against a live backlog, and [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s scratch repository is gone — `gh repo view` returns *Could not resolve to a Repository*, quoted in *Inputs*, which is the owner performing that task's step 10 rather than anything going wrong. Credentials are present and carry `repo`; what is absent is permission to create a repository on the owner's account. **It blocks `implement`, not the outcome**, so `specify` ends with it noted rather than waiting on it (`specify.md` step 5) — and it is the *phases, not answers* limit in advance: no grant of phases could answer it. Phase stays at `specify`; `plan` is not authorised. |
| 2026-08-22 | (no change) | **The question raised at `specify` earlier the same day is answered by the owner: a private scratch repository may be created for the run, and they delete it afterwards.** It is the arrangement [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) ran under, which worked, and whose step 10 the owner has demonstrably performed — that deletion is why the question had to be asked again. *Rejected: meet criteria 2 and 3 against a fixture*, which needs no permission and no cleanup, but the thing under test is what GitHub's API returns for `state`, so a fixture would test this repository's belief about that API rather than the API — which is why criterion 2 says *run against a live backlog* in the first place. **The known cost, recorded with the answer**: the repository sits on the owner's account until they remove it, because this token carries `repo` and not `delete_repo`, so `implement` owes them the same explicit hand-back T-193 made. **No phase moves.** This task is `specified` and `plan` has not been asked for. |
| 2026-08-22 | → done | **All six criteria met. Row 10 compares `state` against the `status:` label, and it was made to fail on a live backlog in both directions before being believed.** `state` is fetched in the standing check and **not** in *enumerate*: the rule is that nothing reads `state` *as* the status, and the operation reporting what exists is precisely where a caller would substitute it — so the field is fetched where it is compared and nowhere else. **Assumption 2 is not removable and the run is the argument**: the backlog stayed divergent until a command was issued, so the contradiction is now findable rather than raised, and the assumption is rewritten to say it decays until somebody checks. **The run exposed a limit the plan did not anticipate** — row 10 skips an issue with no `status:` label or two, which are row 1's, and a silent skip would make a mislabelled backlog score like a healthy one, so the row now requires the examined count. **The mapping is proved untouched by byte comparison against `git show HEAD:`**, after a first attempt whose slice ran past *update* into *enumerate* and reported a difference that was the intended edit. **`uchimata2/taskmd-state-label-scratch` is the owner's to delete** — this token carries `repo` and not `delete_repo`, and the hand-back is §3 step 9. |
| 2026-08-22 | → planned | **Plan written under the multi-phase grant recorded above.** Nine steps. **Step 1 is the whole risk and is first**: the binding says in three places that nothing reads `state`, so a row that reads it either contradicts them or sits where they do not reach — which fetch gains the field decides what has to be rewritten, and everything else is downstream of that. **The deliverable's shape is decided with its rejections**: a row in the standing check, because a `check` class cannot reach a network — a decision this binding already records rather than a gap — and a scheduled job would be automatic reconciliation, non-goal 10, and would destroy the evidence that anybody clicked. **Step 9 is the hand-back**, written as a step rather than left to the closing note, because the token carries `repo` and not `delete_repo` and a lifecycle that ended without it would close on an obligation nobody was told about. Phase stays at `plan` until `implement` runs. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: `implement` owes the owner an explicit hand-back.** Two criteria need a run against a live backlog, the owner authorised one private scratch repository on 2026-08-22, and the token here carries `repo` and not `delete_repo` — so deleting it is theirs to do and has to be asked for by name, as [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) did. A lifecycle that ended without that request would have closed on an obligation nobody was told about. |
