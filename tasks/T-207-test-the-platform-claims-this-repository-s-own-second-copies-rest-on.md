---
id: T-207
title: Test the platform claims this repository's own second copies rest on
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-187, T-072]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-22
deliverables: []
---

# T-207 — Test the platform claims this repository's own second copies rest on

## 1. Specify

**Outcome**
Every place this repository writes one fact twice because a platform is believed to compel it has
either been shown the refusal — the single write attempted and rejected — or has lost the second copy.
Where the copy stays, what forces it is written where a reader meets it.

**Why this one**
Found by [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) while doing the
thing that phase asks for: **using** the clause it had just written, on cases it was not written from.
The clause turns away *a limitation you assumed rather than one you were refused*, and the first two
places it was pointed at in this repository both came back holding an assumption:

- **`.claude-plugin/marketplace.json` → `plugins[0].name`** is `taskmd`, and so is
  `plugin/.claude-plugin/plugin.json` → `name`. One fact, two homes.
  [T-072](T-072-give-the-description-and-version-one-home-each.md) is the precedent and it is a
  warning rather than a comfort: it ran `claude plugin validate` against four manifests and found
  **description and version both optional**, deleting two copies that everybody had assumed were
  required. It did not try `name`. So the surviving copy sits on exactly the untested claim its own
  task disproved twice.
- **`plugin/bin/taskmd.cmd`** states why the entry point exists twice: *no single name is typeable on
  both platforms — an extensionless POSIX script is not executable through a PATH lookup here, and
  `.cmd` is in the default PATHEXT where `.sh` and `.ps1` are not.* That is a claim about Windows,
  and `CLAUDE.md`'s *Verifying* section says a claim about behaviour is verified by running it. It
  reads as settled because it is stated well, which is the shape T-187's refusal case describes.

**It is a sweep, not these two.** They are what one application of the clause happened to reach, and
naming them as the membership would be the enumeration this project's own config warns against.
Derive the set: find where a fact is written twice and a platform is given as the reason.

**Scope**
- In: this repository's own second copies, whatever the sweep finds — the two above are found
  instances, not the list
- In: for each, the single write attempted against the real platform, and what it printed
- In: deleting the copy where the platform allows it, or recording the refusal beside it where it
  does not
- Out: the wording of the clause itself. That is T-187's, and this task tests the repository against
  it rather than the other way round
- Out: any second copy whose reason is not a platform — a different argument is a different task

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the clause, and the refusal case this applies
- [T-072](T-072-give-the-description-and-version-one-home-each.md) — the method that worked, and the
  field it did not reach
- `CLAUDE.md` — *Verifying*, which already binds on every claim about behaviour

**Acceptance criteria**

Written on 2026-08-22. The task's own hazard is that it is a **sweep whose two known members are
already named in §1** — so a derivation that finds only those two would look like a result, and a
verdict reached by reading a manifest would look like a test. Four of the criteria below exist to
stop each of those.

- [ ] **The set is derived, the derivation is shown, and what it is known to miss is stated** rather
      than left as an implied completeness. What failure looks like: a sweep that reports a set and
      cannot say what it read
- [ ] **The two instances named in §1 are found *by* the derivation, not added to it.** They are how
      the derivation is checked, so a derivation that misses either is itself the finding — widening
      it until it happens to catch them fits the answer to the known cases and says nothing about the
      unknown one
- [ ] **Every member of the derived set ends with one of two verdicts** — the copy is gone, or the
      refusal is recorded beside it. None is left described, considered, or deferred without a task
- [ ] **Each *the platform compels it* claim is settled by running something, with the command and its
      output quoted.** A verdict reached from documentation, from a manifest schema, or from how the
      code reads fails this: an untested claim about a platform is the exact case METHOD §4's clause
      refuses, and this task is the clause applied to its own repository
- [ ] **The single write is attempted against every consumer that reads the fact, and the consumers
      are named.** [T-072](T-072-give-the-description-and-version-one-home-each.md) settled two fields
      with `claude plugin validate`; a validator accepting an absent field is not the same claim as
      every reader tolerating it, and `name` is the field an install resolves by
- [ ] **Where a copy is deleted, the artefact is shown still to work afterwards** — the manifest still
      validates, the entry point still starts — quoted, and **on the platform the claim was about**.
      A green run names the operating system it was green on, because the `taskmd.cmd` claim is a
      claim about Windows and answers differently elsewhere
- [ ] **Where a copy stays, what forces it is written where a reader meets the second copy** — not
      only in this task's record. That is the clause's own condition: the rule is exchanged for the
      obligation to keep the constraint visible, so that whoever finds it the day the platform stops
      compelling it can delete it
- [ ] `check` is clean and the suite passes; if a manifest changes, the plugin is shown to still
      install from it

**Open questions**
- **None.** Two candidates were considered and neither survives. *Whether a shipped manifest may be
  edited outside a release* is already settled by
  [T-072](T-072-give-the-description-and-version-one-home-each.md), which deleted two fields from
  these same manifests. *Whether deleting a field could break an already-installed snapshot* is not a
  question for the owner but a thing to measure, and the criteria above require exactly that
  measurement — it is the difference between a consumer that was tested and one that was assumed.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* by [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), whose `implement` step 7 used the new clause on cases it was not written from. `medium` and `s`: nothing is broken, and what it buys is that the clause's own repository is not the first place it is ignored. **Not covered by the grant T-187 runs under**, which reaches three named tasks and nothing any of them raises. |
| 2026-08-22 | → specified | **Specify agreed: eight criteria written, where §1 had carried a placeholder, and the open-questions slot resolved to none with the reasons.** The criteria are shaped by this task's two ways of looking finished without being it. **First, the sweep**: §1 names two instances, so a derivation returning exactly those two would read as a result — a criterion therefore requires the two be found *by* the derivation rather than added to it, making them the test of the instrument instead of its output. **Second, the verdict**: this task is METHOD §4's refusal case applied to its own repository, so a claim settled by reading a schema is the failure and not the evidence, and one criterion requires a command and its output for every claim. One criterion carries [T-072](T-072-give-the-description-and-version-one-home-each.md)'s unfinished half: that task settled two fields with `claude plugin validate`, and a validator tolerating an absent field is not every reader tolerating it — `name` is what an install resolves by, so the consumers have to be named and each one tried. Another requires a green run to name the operating system it was green on, because the `taskmd.cmd` claim is about Windows. Phase stays at `specify`; `plan` is not authorised (METHOD §3.1). |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it may not be finishable in one run, and stopping is correct if so.** Its criteria require the single write to be *attempted and refused* against every consumer that reads the fact — an attempt that cannot be made is a finding to record, not a claim to reason out. |
