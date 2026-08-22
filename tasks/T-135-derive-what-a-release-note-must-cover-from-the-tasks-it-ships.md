---
id: T-135
title: Derive what a release note must cover from the tasks it ships
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-086, T-125, T-127, T-128, T-129, T-133]
work_package: M6
owner: maintainer
business_value: medium
effort: m
created: 2026-08-11
updated: 2026-08-18
deliverables: [.taskmd/config.md, docs/PUBLISHING.md]
---

# T-135 — Derive what a release note must cover from the tasks it ships

## 1. Specify

**Outcome**
A release note has a rule for what it must mention, and the rule is checked against the set the
tracker already knows — so what reaches the note stops depending on who wrote it.

**Why this one**
Reported by an adopting project on 2026-08-11: *`v0.4.0`'s note omits T-112.* Verified, and it is
one instance rather than the finding.

`v0.4.0` shipped **47** closed tasks. Its note describes about eight changes and opens with
*"Everything grouped as the v0.2 milestone"*, which reads as a completeness claim. Neither the tag
message nor the release body names a single task id, so nothing connects the note to the set it
covers. Sampled against the closed set, these change what an adopter sees and appear nowhere in it:

| Task | What an adopter would have noticed |
| :--- | :--- |
| [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md) | `check` stops reporting link syntax shown inside a code span as a broken link |
| [T-025](T-025-let-check-notice-a-stale-generated-index.md) | `check` reports a stale generated index, which it never used to |
| [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) | `check` prints denominators and a `Scope` line on every run |
| [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) | `list` marks blocked rows |
| [T-111](T-111-stop-the-index-showing-a-closed-task-as-a-live-blocker.md) | the generated index stops showing a closed task as a live blocker |
| [T-101](T-101-report-a-template-the-create-path-cannot-see.md), [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) | two new `check` classes |

**This is the project's own design rule pointing at itself.** The membership of a release is
`work_package`, read with the tool and written down nowhere — that is
[T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md)'s whole point. The note is then
written by hand from memory of that set, which is the second copy arriving through the back door: not
a stale *list*, but a stale *selection*.

**What this is not.** Not a generated changelog. A note that prints 47 titles is worse than one that
describes eight changes well, and `docs/PUBLISHING.md` §1 makes the note covered prose that a stranger
reads. The question is what it must **not** omit, not what it must contain.

**Requirements served**
R-8 (`docs/SCOPE.md`) — everything found leaves a trace, applied to the one document an adopter reads
to find out what changed. R-21, since the note is covered text.

**Scope**
- In: a rule for what a note must mention, expressed against something the tracker already holds.
- In: whether anything checks it, and if so what it can honestly judge — the same proxy problem
  [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) met.
- In: whether the opening sentence should keep claiming completeness.
- Out: rewriting `v0.4.0`'s published note. Same answer as
  [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md), agreed by
  the maintainer on 2026-08-11: a dated public record is not rewritten after the rule changed.
- Out: generating the note. See *what this is not*.
- Out: the covered-text question. Settled in T-127.

**Inputs**
- The measurement above, reproducible with `list --work_package M2 --closed`.
- [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md), for why membership is derived.
- [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) §3, for a check that
  reads its rule out of the document that owns it, and for what a proxy may claim.
- `docs/PUBLISHING.md` §1 and §5.

**Acceptance criteria**
- [ ] `docs/PUBLISHING.md` states what a release note must not omit, in one place, as a test rather
      than a list
- [ ] The rule is applied to `v0.4.0`'s note as a worked example, and the result recorded either way
- [ ] If anything automated is added, it says what it cannot judge, in its output or its name
- [ ] The note for the next release is written to the rule, and the rule found something the writer
      had not already thought of — or the record says it did not

**Open questions**
- None. Both answered by the maintainer on 2026-08-11.

  **Q1 — what is the trigger for "must mention"? — a field on the task.** The note's coverage is then
  derived from the same front-matter everything else is derived from, which is the design rule applied
  rather than worked around. It costs a config key, and
  [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) says a key is not free: the shipped
  config replaces rather than merges, so every project that has written one stops seeing the new row
  until it re-copies. **That cost is now `plan`'s first problem**, not a reason to reopen the answer.
  *Rejected: a type-and-status rule* — "every closed `fix` and `deliverable` must be mentioned or
  waived" adds no key and over-fires on internal work, and a rule that fires on work an adopter
  cannot see teaches the writer to waive by reflex.

  **Q2 — does the opening sentence keep claiming completeness? — no.** *"Everything grouped as the
  M2 milestone"* is true of the milestone and false of the note, and it is the sentence that turns
  an omission into a defect rather than an editorial choice. Dropping it makes the note honest about
  being a selection, which is what Q1's rule then bounds. *Rejected: keep it and make it true* — that
  is a note naming 47 tasks, which §1 already rules out as worse than eight described well.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Settle the key problem first**, by running the tool rather than reasoning about it: whether a field on the task can be made selectable without adding a key to the shipped config, which [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) shows would error every adopter's config on upgrade | A recorded decision in §3, quoting the commands that settled it and what each printed |
| 2 | Name the field and its values, and give **unjudged** a meaning distinct from *no* | The vocabulary, with the reason the third state exists, in §3 |
| 3 | Write this project's own `.taskmd/config.md` — the shipped default, with the field named where step 1 says it must be | .taskmd/config.md |
| 4 | Judge the 47 closed tasks of `M2`, the set `v0.4.0` shipped, one decision per task, and record the rule used on the borderline ones | The 47 edited task files, and the borderline rule, in §3 |
| 5 | Run the rule against `v0.4.0`'s published note: what it says must not have been omitted, against what the note did mention | The comparison in §3 — recorded whichever way it comes out |
| 6 | Write the rule into `docs/PUBLISHING.md` as a test with the command that answers it, and drop the completeness claim from the opening convention (Q2) | The edited docs/PUBLISHING.md |
| 7 | Say what the rule cannot judge, where a writer meets it rather than in a task record | A named limitation inside step 6's text |

**Step 1 is placed first because it can invalidate every step after it.** The owner's Q1 answer
costs a config key by its own account, and T-106's chain says a new key in the shipped default is a
hard error for every project that wrote a config — measured, not feared. If no route exists that
avoids that, the shape of this task changes and steps 3–7 are the wrong steps; finding that out at
step 6 means writing the document twice.

**Step 4 is the expensive one and it is not optional.** The worked example criterion 2 asks for is
the rule *run on the real corpus*, and the corpus cannot answer a filter it does not carry. A rule
argued against a sample would pass exactly as convincingly as one that works.

**Decisions taken at `plan`**

- **The rule's trigger is a field, per the owner's Q1, and the field is carried by this project's
  config rather than the shipped one.** — This is the answer to the cost the owner handed to `plan`.
  *Rejected: adding the key to `taskmd/defaults/config.md`*, which T-106 shows would raise on every
  adopter's next upgrade, naming a key they have never heard of — a release-note convention of ours
  is not worth an error in someone else's project. — 2026-08-18
- **Criterion 4 will not be met by this task, and that is planned for rather than discovered at
  review.** — It requires the *next* release to be written to the rule, and no release is in
  progress. Planning to carry it into a child task is honest; planning to satisfy it by writing a
  note for a release nobody is making would be the criterion describing the work instead of judging
  it. — 2026-08-18
- **`deliverables` stays empty until step 3 and step 6 land.** — 2026-08-18

**Outputs this task will produce**

- .taskmd/config.md — this project's schema, carrying the new field
- docs/PUBLISHING.md — the rule, its command, and what it cannot judge
- tasks/T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md — §3, the mechanism
  decision, the vocabulary, the borderline rule and the `v0.4.0` comparison
- 47 task files under tasks/ — the `M2` closed set, each carrying the new field

## 3. Implement

### Steps 1–2 — the key problem, settled by running the tool

The owner's Q1 answer costs a config key by its own account, and
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) makes a new key in the shipped
default a hard error for every project that wrote a config. **Two commands settled the route.**

A field the schema does not name is carried but not selectable:

```text
$ taskmd list --adopter_visible yes
unknown filter: --adopter_visible. This project accepts: --blocked_by, --blocks,
--business_value, --children, --effort, --owner, --parent, --phase, --related,
--status, --type, --work_package
```

`check` had already accepted the same field without complaint — front-matter values rose by one and
the exit stayed 0 — so the field was being *carried*, exactly as the schema's *Format* section says.
Naming it in `context_fields`, an **existing** key, made it selectable with no code change:

```text
$ taskmd list --adopter_visible yes
(no rows — nothing marked yet)
```

**Decision: the field is carried by this project's own `.taskmd/config.md`, not by the shipped
default.** This repository had no config at all and now has one — a copy of the shipped file with
one line changed. *Rejected: adding a key to `taskmd/defaults/config.md`*, which T-106's chain shows
would raise on every adopter's next upgrade, naming a key they have never heard of. A release-note
convention of ours does not justify an error in someone else's project. — 2026-08-18

**Cost accepted, and named so it is not discovered later**: this repository stops demonstrating the
zero-config path, and its config can now fall behind the shipped one. That is what the `CONFIG DRIFT`
advisory exists for, so the cost is carried by a mechanism that already reports it. — 2026-08-18

**Decision: three states, not two.** `adopter_visible: yes` / `no`, and **absent means nobody
judged it** — which is a defect at release time rather than a synonym for `no`. Two states would let
an unexamined task pass as *not visible* by default, which is the failure this task exists to stop:
the note's coverage would once again depend on who looked. — 2026-08-18

### Step 4 — the 47 judged

**The test used, stated so the borderline calls can be argued with**: *would someone who installed
the plugin see different output, receive a different file, or have to act differently?* Internal
work — this repository's own tests, backlog grouping, CI decisions and instruction files — is `no`.

```text
$ taskmd list --work_package M2 --closed                       47
$ taskmd list --work_package M2 --closed --adopter_visible yes 31
$ taskmd list --work_package M2 --closed --adopter_visible no  16
```

**The counts sum to the whole set**, which is the point of checking them this way: a filter cannot
report what it failed to see, so the partition is what shows nothing was skipped. Nothing in `M2` is
unjudged.

### Step 5 — the rule run against `v0.4.0`'s published note

The note names **zero task ids** — confirmed with `git for-each-ref refs/tags/v0.4.0`. So the
mapping from its prose to the 31 required rows had to be made by hand, and the result is a floor
rather than a count:

| | |
| :--- | ---: |
| Required by the rule | **31** |
| Identifiable in the note by description | 10 |
| **Not identifiable** | **21** |

The ten are `tasks_dir` rejections (T-024, T-078), the `CONFIG DRIFT` narrowing (T-123), cancelled
outputs (T-090), the third rejection message (T-122), `IGNORED LINK` (T-097), `id_width: none`
(T-082), and three named in the `v0.3.0` catch-up paragraph — template validation (T-032), filtering
on any field a view names (T-087), unknown-argument rejection (T-029).

**The result, recorded as criterion 2 asks, either way: the rule fires, and hard.** §1 found six
omissions by sampling. The rule finds at least twenty-one, from the same release, without anyone
choosing what to look at — which is the difference between a selection and a set.

**One paragraph of the note resists the rule and is worth naming**: *"the first adopter's seven
recommendations"* covers seven tasks as a group without naming any. Whether that counts as
mentioning them is a judgement the rule cannot make, and it is the concrete form of the proxy
problem §1 anticipated. It is why step 6 makes the command produce a **checklist for the writer**
rather than a gate.

### Steps 6–7 — the rule, and what it cannot judge

Written into `docs/PUBLISHING.md` as a new §2, with the command that answers it, the unjudged-state
rule, and an explicit statement of the two things it cannot do: decide whether a sentence describes a
given task, and see a task nobody marked. Q2 applied in the same edit — the completeness claim is
dropped from the opening convention, so the note is honest about being a selection.

**Outputs produced**
- .taskmd/config.md
- docs/PUBLISHING.md
- 47 task files under tasks/ — the `M2` closed set

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `docs/PUBLISHING.md` states what a note must not omit, in one place, as a test rather than a list | **met** | §7, one section. Stated as a test — *every task the release closed that an adopter would notice is described or waived* — with the command that produces the set. No list of files or tasks anywhere in it |
| The rule applied to `v0.4.0`'s note as a worked example, result recorded either way | **met** | §3 step 5. 31 required, 10 identifiable in the note, **at least 21 omitted** against the 6 a hand-sample had found. The note names no task ids, which is why 21 is a floor and is recorded as one |
| If anything automated is added, it says what it cannot judge | **met** | Nothing was added to the tool — the rule runs on `list` as it already is. Its two limits are stated in §7 *What this rule cannot judge*: it cannot tell whether a sentence describes a task, and it cannot see a task nobody marked. The second is why the counts must sum |
| The next release's note is written to the rule, and the rule found something the writer had not thought of — or the record says it did not | **carried** | No release is in progress, so this cannot be met by the task that wrote the rule without the criterion describing the work instead of judging it. Planned for at `plan`, not discovered here. → **[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)** |

**Open questions, re-read before closing** (procedure step 5)

Both were answered by the maintainer on 2026-08-11 and both were **used** rather than merely
recorded: Q1's field is `adopter_visible`, and Q2's dropped completeness claim is §7's closing
subsection. The cost Q1 handed to `plan` — the config key — was the plan's first step and is
resolved without one. Nothing here is addressed to anyone else; T-182 carries the only open thread
and states its own gating question.

**A caveat the criteria do not cover, recorded because it bounds the result**

The 47 judgements in step 4 are one person's, made from titles and records rather than from running
each change as an adopter. The test used is written down in §3 and in §7 so a disagreement has
something to argue with, but the set is only as good as that pass. The rule's value does not rest on
it — a wrong `yes` costs a sentence in a note, a wrong `no` is the failure the rule exists to catch,
and the counts summing is what makes a re-judgement cheap.

**Child fix tasks raised**
- [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) — apply the rule
  to a real release and say whether it caught anything

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) no longer records this task as its parent** — re-edged to a soft edge by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), so that this record's closure does not contradict the rule the owner settled on 2026-08-22 that a child holds every parent open. **§4 is unchanged and is still the account of what happened**: criterion 4 was *carried*, T-182 was raised for it, and this row does not rewrite that. What changed is only the edge, and only on T-182's record where it is stored. The judgement and its rejected alternative are in T-216 §3. |
| 2026-08-18 | → done | `plan`, `implement` and `review` all run in one session under the extended grant below. Three criteria met, one carried to [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md). **The cost the owner handed to `plan` is paid without a shipped config key**: a field named in `context_fields` — an existing key — is selectable by `list`, so `.taskmd/config.md` carries `adopter_visible` here and no adopter's config gains a key it would raise on. This repository now has a config where it had none, which is the price and is named in §3. The rule was run on the real corpus rather than argued: 31 of `M2`'s 47 required, at least 21 missing from `v0.4.0`'s note against the 6 a sample had found. Suite green afterwards — 276 passed — which was the live risk, since this repo had been exercising the zero-config path. |
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `plan` → `implement` → `review` (this task's `specify` is already closed and owner-agreed, so the authorisation starts where the work does) — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-11 | → specified | Both questions answered by the maintainer, with the rejections recorded in §1. **Q1: a field on the task**, so coverage derives from the same front-matter as everything else. That buys a config key, and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s constraint makes the key the first thing `plan` has to solve rather than a detail: the shipped config replaces rather than merges, so a project that already wrote one stops seeing the new row. **Q2: the opening sentence stops claiming completeness**, because it is the clause that turns an omission into a defect. Criteria unchanged; both answers are choices inside them. Still `M6` and still not started. |
| 2026-08-11 | → proposed | Reported by an adopting project as *"`v0.4.0`'s note omits T-112"* and **verified before filing**, which changed what it is: the note omits T-112 and it omits at least five other adopter-visible changes, out of 47 tasks shipped, while opening with a sentence that reads as a completeness claim. So the report is a specimen and the finding is that a note has no rule. Filed `M6` by the maintainer's release rule of 2026-08-10 — this is a new capability and a config decision rather than a minor correction, and nothing about it holds up `0.5.0`, whose note is written by hand to the same standard in the meantime. Not started: both open questions are the maintainer's, and Q1 turns on whether the schema gains a key. |
