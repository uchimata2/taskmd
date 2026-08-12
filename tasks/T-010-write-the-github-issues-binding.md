---
id: T-010
title: Write the GitHub Issues binding
type: deliverable
status: done
phase: review
parent: null
blocked_by: [T-009]
related: [T-004]
work_package: M1
owner: maintainer
business_value: high
effort: m
created: 2026-08-04
updated: 2026-08-07
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-010 — Write the GitHub Issues binding

## 1. Specify

**Outcome**
A binding that maps every taskmd concept onto native GitHub features, so a project on GitHub
Issues follows the identical method with no local task files — and a project moving there changes
its binding, not how it works.

**Requirements served**
R-13, R-14 (`docs/SCOPE.md`). Bounded by assumption **A3**: a binding document, not code.

**Why this one**
This is the requirement that proves the method/technical split is real rather than claimed. It is
also more tractable than expected — GitHub gained native sub-issues and issue dependencies, so two
of the three edge kinds map directly, and both derive their inverse exactly as taskmd does.

**Scope**
- In: the concept mapping; the three structural mismatches below; the "assumptions this binding
  makes" section; how a project declares it uses this backend.
- Out: any taskmd code that calls GitHub, and any migration of existing tasks into issues — both
  excluded by A3 and non-goal 8. The agent drives `gh`; the tool does not.

**The three mismatches this task exists to solve**

1. **Ids are assigned by the server.** Locally the next id is picked before the file is written;
   GitHub assigns `#N` on create and the create response may not carry it. Any id rule must
   tolerate "id unknown until created" — this constrains T-004, which is currently written
   local-only.
2. **There is no soft-link field.** `parent` maps to sub-issues and `blocked_by` to issue
   dependencies, but `related` has no native carrier. It must map to a cross-reference or a label,
   and the choice must not fabricate a stored inverse.
3. **Status is binary.** GitHub has open/closed plus a state reason; a richer vocabulary must live
   in labels or a Projects field. Whichever is chosen, it stays **one** home — the label and the
   Projects field must not both be authoritative.

**Inputs**
- `docs/SCOPE.md` §3B, and T-007 §3 for the mapping evidence already gathered
- [`docs/BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) — the contract this binding implements; §5 is already one
  operation worked against this exact backend, and [`docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)
  is the worked precedent for the shape
- **Unreachable, so recorded here rather than consulted:** the Handoff project's `PROJECT_BOARD.md`
  is not in this repository and no copy of it is. What was taken from it is one sentence — issues
  are the source, the board is a derived view auto-synced from `status:` labels, and cards are never
  dragged by hand. That sentence is the evidence; the document cannot be re-read for more.
- GitHub documentation for sub-issues, issue dependencies, issue types and Projects — verify
  current limits rather than trusting this file (sub-issues were documented at 100 children and
  8 levels; dependencies at 50 per relationship). If a feature has changed or gone, criterion 1's
  "or a stated reason it has none" absorbs it and the outcome still stands.
- A GitHub account that can create, populate and delete a repository. Criterion 5 cannot be met
  without one; this repository has no remote, and the walk happens on a throwaway instead — see the
  answered open question. Creating and deleting it are actions on someone's account, so `implement`
  confirms before doing either.

**Acceptance criteria**
- [ ] Every concept the method and the contract name has a named GitHub carrier, or a stated reason
      it has none — the six operations of BINDING §1, the three edge kinds of METHOD §4, the homes
      of METHOD §6, and each field the schema config defines
- [ ] Each of the three mismatches above has a decided resolution with its rationale
- [ ] No taskmd concept maps to two authoritative carriers. Where a second carrier exists it is
      named as a derived view, with what regenerates it and the statement that no operation reads it
- [ ] The "assumptions this binding makes" section is present, states a position on all five of
      BINDING §4's minimum entries — including "none" where that is the answer — and is checkable in
      thirty seconds
- [ ] **Proven by being followed on a live repository** — not a transcript of what the API would
      return. One task is created and walked through all four phases as an issue, carrying a
      dependency and a sub-issue; the inverse of each is confirmed to appear at the far end without
      having been written; and **after that task is closed, the binding's `enumerate` still returns
      it and still shows the far end of its edges** (BINDING §3 — the default issue listing is open
      only, and that failure is silent)
- [ ] The method document required no change to support this backend — if it did, that is a defect
      in T-008 and a child task

**Open questions**
- ~~Labels or a Projects single-select for `phase` and `status`?~~ — **not a `specify` question, and
  closed here as one.** It is mismatch 3's resolution, which criterion 2 already requires the
  binding to decide and criterion 3 already constrains to a single authoritative carrier. A sentence
  naming labels would be false had a different carrier been chosen, so by
  [`specify`](../plugin/skills/taskmd/docs/method/specify.md)'s own test it is a later phase's decision, not part of what
  the outcome is judged against. Carried forward rather than dropped: the trade is adoptability
  against tidiness — labels need nothing beyond issues being enabled, a Projects field needs a board
  and a token scope — and criterion 4 is what turns whichever cost is chosen into a stated
  assumption instead of a surprise for the adopter.
- ~~What "a live repository" means for criterion 5.~~ — **answered by the owner, 2026-08-07: a
  throwaway repository, created for the walk and deleted after.** Nothing in the proof needs the
  repository to be this project's; the binding is about GitHub Issues, and migrating these tasks
  into issues is already out of scope. Two alternatives rejected: giving this project its remote now
  would be the stronger proof but publishes ahead of T-006, which owns publishing; and weakening the
  criterion to a paper walk was rejected against `CLAUDE.md` *Verifying* and BINDING §6.5 — the
  after-close `enumerate` trap is precisely the failure a walk on paper cannot catch. Criterion 5 is
  unchanged by this: it already said "live", and which repository is an input, not a measure.

Not an open question, and recorded so it is not re-raised: mismatch 1 constrains T-004, and T-004
already carries that constraint as its own fourth criterion, citing this task. Restating it here
would be the second home the design rule forbids.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Probe the **live** API for every carrier the mapping needs — hierarchy, dependency, soft link, status, phase, type — and for what the listing returns by default. Documentation is not evidence here; the limits in §1's inputs are second-hand and one of them is what the whole binding rests on. | A capability table in §3: what exists, what does not, and the tool version it was checked against |
| 2 | Decide the two carrier questions the mismatches leave open — what carries `related` (mismatch 2) and what carries `phase`/`status` (mismatch 3) — against step 1's table rather than against the documentation. | Two decisions in §3, each with its rationale and its rejected alternative |
| 3 | Write the **assumptions** section, from BINDING §4's five entries, before a single operation is written. BINDING §6.2 is explicit that doing this last yields a description of what was built rather than a premise anyone can check. | `docs/bindings/github-issues.md` — its assumptions section |
| 4 | Map the six contract operations, the three edge kinds and the schema's fields onto the carriers step 1 confirmed. | The same file — its configuration, mapping and operations sections |
| 5 | Walk the binding on a throwaway repository: create one task as an issue, carry it through all four phases, give it a dependency and a sub-issue, confirm each inverse appears without being written — then close it and confirm `enumerate` still returns it and its far ends. | Recorded evidence in §3: the commands run, and what each actually returned |
| 6 | Delete the throwaway repository. | Confirmation in §3 that nothing remains of it |

**Sequencing.** Step 1 is first because it can invalidate steps 2–4 outright: the binding's whole
premise is that GitHub carries two of the three edge kinds natively, and if it does not, the mapping
is a different document. Step 5 is placed after the binding is written rather than alongside it,
because a walk performed while drafting proves the author's intent, not the text — BINDING §6.5
wants the binding followed, which requires something to follow.

**Step 5 needs an input from outside this task:** a GitHub account able to create and delete a
repository. Creating and deleting are actions on someone's account, so `implement` asks before doing
either — agreed in §1.

**Shape of the deliverable — decided.** One Markdown document, `docs/bindings/github-issues.md`,
structured as [`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) is: assumptions, then
configuration, then the six operations. Two alternatives rejected. Splitting mapping from operations
into two documents was rejected because it lets an adopter read the operations without the premises
that make them safe, which is exactly the F1 failure BINDING §4 exists to prevent. Shipping a `gh`
wrapper script was rejected as out of scope by A3 and non-goal 8 — and because a script would make
"runs on a clone with nothing installed" false.

**Output paths**
- `docs/bindings/github-issues.md` — the binding (written as a path, not a link: it does not exist
  until step 4, and `check` correctly refuses a link that does not resolve)
- This task's §3 — the capability table, the two carrier decisions, and the walk evidence

## 3. Implement

**Step 1 — the capability table.** Probed against the live tool, `gh` 2.96.0, on 2026-08-07. The
documented limits quoted in §1 were not the risk; what mattered was which carriers exist at all.

| What the mapping needs | Exists? | Carrier found |
| :--- | :--- | :--- |
| hierarchy, both directions | yes | `--parent` / `--add-sub-issue` on create and edit; `parent` **and** `subIssues` both readable |
| dependency, both directions | yes | `--blocked-by` / `--blocking`; `blockedBy` **and** `blocking` both readable |
| soft link | **no** | nothing — no flag, no field, no JSON key. Mismatch 2 confirmed rather than assumed |
| enumerated vocabularies | yes | labels, readable via `labels` |
| a single-select alternative | yes | issue types (`--type`) and Projects fields — both rejected, below |
| the whole set, open and closed | yes | `gh issue list --state all`, **default `open`** |
| the whole set, untruncated | yes | `--limit`, **default 30** |

Two findings here that §1 did not anticipate. `gh issue create` takes `--parent` and `--blocked-by`
directly, so the contract's "edges set in one operation" is met natively and mismatch 1 costs less
than expected. Against that, `--limit` defaulting to 30 is a **second** silent truncation sitting
beside the `--state` default that BINDING §3 warns about — same failure class, not mentioned
anywhere, and the more convincing of the two because thirty results look like an answer.

**Step 2 — the carrier decisions.**

- **D1 — every enumerated vocabulary is a label, `<field>:<value>`; no exceptions.** — Uniform, so
  there is no per-field reasoning to get wrong, and it needs nothing beyond issues being enabled.
  Three alternatives rejected: a **Projects single-select** (needs a board, a second token scope, and
  makes `read` a two-lookup operation for a cosmetic gain); **issue types** for `type` (defined at
  organisation level, so a personal repository cannot have them — a binding whose `type` field only
  works for organisations excludes most adopters); **assignees** for `owner` (an assignee is a login,
  the schema's `owner` values are roles, and mapping one to the other would have this binding decide
  the project's vocabulary, which BINDING §2 forbids). — 2026-08-07
- **D2 — `related` is a line in a property block at the top of the issue body.** — There is no
  native carrier, confirmed in step 1. Rejected: a label per pair (quadratic label explosion, and a
  label cannot point at an issue); a dedicated comment (a second place to look, in a stream anyone
  can append to). The binding states the trap this creates: GitHub raises a cross-reference for
  **any** `#N` mention anywhere, so those cross-references are explicitly *not* soft edges. — 2026-08-07
- **D3 — the issue's open/closed `state` is a materialised rendering of the status label, written
  by the same update and never read.** — This is the sharpest problem in the binding. taskmd derives
  open/closed from `status` via `open_statuses`; GitHub stores it. Something has to give, and making
  `state` a rendering under BINDING §3's materialised-view rule ("reproducible from the tasks alone,
  and no operation may read it") is what keeps a single home. It also supplies the *reason*
  `enumerate` must pass `--state all` — not merely to avoid missing closed tasks, but because
  filtering on `state` would make a rendering into an input. Rejected: **never closing an issue at
  all**, which would materialise nothing and is cleaner by the design rule, but leaves every issue
  permanently open — and GitHub's entire surface reads `state`, so the result is unusable as a
  GitHub project, which is the opposite of this task's outcome. — 2026-08-07
- **D4 — everything with no native and no label carrier goes in the property block, verbatim,
  including fields the schema does not name.** — BINDING §1's `read` requires uninterpreted
  properties to come back unchanged; a fenced block at the top of the body is the only place that
  survives a round trip. — 2026-08-07

**Step 5 — the walk.** On a throwaway private repository, created for this and nothing else. Three
issues: a blocker, the task under test blocked by it, and a child created with `--parent` in the
same command. Every claim below is what the tool returned, not what the binding says it would.

- **Setup worked as written.** Eighteen vocabulary labels created; nothing else configured — no
  board, no organisation, no template.
- **Inverse edges appear without being written.** Only two edges were ever written: `--blocked-by`
  on the task, `--parent` on the child. Reading the *other* ends returned `blocking: [#2]` on the
  blocker and `subIssues: [#3]` on the task. Neither was written by anything.
- **All four phases walked** by the `update` operation, one `phase:` and one `status:` label at
  every point, `state` correctly still open at `status:review`.
- **Edges survive closure.** With the blocker closed, the still-open task returned
  `blockedBy: [#1, state CLOSED]`, and the closed blocker still returned `blocking: [#2]`. The far
  end of a link to finished work is intact.
- **`enumerate` proven by being made to fail**, which is the only proof that counts here. As the
  binding specifies (`--state all`), the listing returned all three with the graph whole. With the
  default state it returned **one** issue: the two closed tasks vanished, and the survivor's
  `parent: 2` was left pointing at a task the enumeration says does not exist. No error, no warning.
  The limit trap has the same shape — asking for 2 of 3 returned 2 and **exit code 0**.
- **Assumption 2's hazard is real, not theoretical.** Closing an issue without touching its label
  left `state: CLOSED` alongside `status:proposed` — a task contradicting itself, with nothing
  raised. That is the muscle-memory error the assumption is written to catch, and it is silent.

**Step 6 — cleanup: not completed, and the repository still exists.** `gh repo delete` returned
HTTP 403: the authenticated token carries `repo` but not `delete_repo`. Refreshing the scope is an
interactive re-authentication, which is the owner's to perform, not the agent's. The repository is
private, so nothing is exposed while it stands. Carried to **T-037** rather than left in this record.

**Findings raised, not fixed here** (METHOD §3.3, rule 4)
- **T-038** — BINDING §5 predicts this binding "materialises nothing". It materialises one thing,
  by D3. A worked example in the contract now contradicts the binding derived from it.
- **T-039** — `plan`'s own instruction to name output paths collides with `check`, which reads a
  Markdown link to a not-yet-created deliverable as a broken link. Hit while writing §2 above.

**Outputs produced**
- [`docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every concept the method and the contract name has a carrier, or a stated reason it has none | met | All six BINDING §1 operations have a section. All three METHOD §4 edge kinds are carried — two natively, and `related` by the stated absence of any carrier, which the criterion admits as an answer. METHOD §6's homes are assigned in one paragraph. The schema's fields are covered by three ordered rules rather than a row each; that is deliberately stronger, since rule 3 also catches fields the schema does not name, which a field-by-field table could not. |
| Each of the three mismatches has a decided resolution with its rationale | met | Mismatch 1 → assumption 1 and the `create` command that carries edges from birth. Mismatch 2 → D2, with the cross-reference trap stated as assumption 5 because the obvious reading of GitHub's UI is the wrong one. Mismatch 3 → D1 and D3. Each carries its rejected alternative. |
| No concept maps to two authoritative carriers | met | One second carrier exists and is the interesting case: the issue's `state`. It is named as a rendering (assumption 2), what regenerates it is written into `update`, and `enumerate` says nothing filters on it. Judged against the criterion's own escape clause, which permits a second carrier only on those three conditions — all three are present. |
| Assumptions section present, all five BINDING §4 entries, checkable in thirty seconds | **not met** | The five entries are all there. The thirty seconds are not: measured at **498 words, ~120s at 250 wpm** — four times the bar. Measuring the older binding for comparison put it at 401 words, ~96s, so the figure has never been met by anything and was never tested. Not narrowed to this section, because a fix confined here would leave §4's claim false and the precedent standing → **T-040**. |
| Proven by being followed on a live repository | met | Every clause of it. Four phases walked; a dependency and a sub-issue carried; both inverses (`blocking`, `subIssues`) returned without ever being written; edges intact across closure; and after closing, `enumerate` returned the task and its far ends. The two failure demonstrations are what make this a proof rather than a pass — the default state returned **one of three** issues and left a dangling `parent`, and `--limit 2` of 3 truncated silently at **exit 0**. Closing an issue without its label produced a task contradicting itself, unflagged. Gap the criterion did not ask about: no issue body was ever edited, so `update`'s body-rewrite rule is unexecuted → **T-041**. |
| The method document required no change | met | `docs/METHOD.md` is untouched and no change was wanted. Every absorption happened in the binding, which is what R-14 asks for. The contract, by contrast, did not come through clean — BINDING §5 now contradicts the binding it predicted → **T-038**, which is not this criterion's subject and is raised rather than folded into it. |

Five met, one carried. The failed criterion is the one the task could most easily have passed by
declaring it: "checkable in thirty seconds" invites a glance and a tick, and it survived T-009
unmeasured for exactly that reason.

**Child fix tasks raised**
- **T-040** — the thirty-second claim, measured and failed, across both bindings and BINDING §4.
- **T-041** — `update`'s body-rewrite rule, never executed, to be proven by being made to fail.
- **T-038** — BINDING §5's worked example contradicts the binding derived from it.
- **T-039** — `plan` cannot link a deliverable it has not produced yet without failing `check`.
- **T-037** — the throwaway repository still exists; deleting it needs a token scope only the owner
  can grant.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Five criteria met, one carried to T-040. The binding is `docs/bindings/github-issues.md`, proven by being walked on a live throwaway repository rather than by being read. Three things the plan did not anticipate, all recorded in §3: `gh issue create` takes `--parent` and `--blocked-by`, so mismatch 1 costs less than feared and the contract's edges-at-creation guarantee is native; `--limit` defaults to 30, a second silent truncation beside the `--state` default BINDING §3 warns about; and open/closed `state` is a stored property where taskmd derives it, which forced D3 — `state` is a materialised rendering of the status label, never read, which is also the *reason* `enumerate` must pass `--state all`. Both truncations and the label/state desync were demonstrated by being made to fail, per `CLAUDE.md` *Verifying*. Five tasks raised rather than absorbed: T-037 (cleanup blocked on a token scope), T-038 (BINDING §5 contradicts this binding), T-039 (`plan` versus `check` on unbuilt deliverables), T-040 (the thirty-second claim, measured and failed by both bindings), T-041 (the one operation rule left unexecuted). |
| 2026-08-07 | → planned | Six steps. The capability probe is step 1 because it can invalidate steps 2–4 entirely — the binding's premise is that GitHub carries two of three edge kinds natively, and the limits quoted in §1's inputs are second-hand. The walk is placed after the binding is written, not alongside it, since BINDING §6.5 asks for the binding to be *followed* and a walk done while drafting proves the author's intent instead. Deliverable shape decided as one document mirroring `local-markdown.md`; splitting mapping from operations was rejected as re-creating the F1 failure, and a `gh` wrapper was rejected under A3 and non-goal 8. No new dependency edge — T-009 is done and nothing else gates this. |
| 2026-08-07 | → specified | Criteria agreed as written; six kept, four sharpened. Q1 (labels or a Projects field) was closed as *not a specify question* rather than answered — a sentence naming a carrier is false under a different approach, so by `specify`'s own test it belongs to a later phase, and criteria 2 and 3 already compel the binding to decide it and to decide only one. The trade is carried forward so it is not re-derived. Q2 answered by the owner: the walk happens on a throwaway repository, since this one has no remote; two alternatives recorded as rejected, and criterion 5 needed no amendment because "which repository" is an input, not a measure. Criterion 5 gained the one check the task was missing — that `enumerate` still returns the task and its far-end edges *after* it closes, which BINDING §3 names as the silent failure of this backend. Criterion 1's "every concept" was made enumerable, criterion 3 now permits a second carrier only as a named derived view nothing reads, and criterion 4 is pinned to BINDING §4's five entries. Two things recorded so they are not re-raised: mismatch 1's constraint on T-004 already lives on T-004 and is not copied here, and the `PROJECT_BOARD.md` input is unreachable — the one sentence taken from it is now the evidence. |
| 2026-08-04 | → proposed | Raised by T-007 to carry R-14, the seamless local↔GitHub transition. |
