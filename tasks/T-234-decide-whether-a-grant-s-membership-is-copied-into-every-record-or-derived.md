---
id: T-234
title: Decide whether a grant's membership is copied into every record or derived
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-106, T-087, T-136]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-234 — Decide whether a grant's membership is copied into every record or derived

## 1. Specify

**Outcome**
An answer, recorded, on whether a multi-task authorisation keeps naming its whole membership inside
every record it covers — and if not, what carries that membership instead.

**Why this one**
`CLAUDE.md` requires an authorisation covering more than one phase to be written into the task's own
record, *naming who gave it and what it covers*, because an authorisation kept anywhere else is one a
later session can miss or stretch. **In practice that means the membership list is written once per
covered record**, and every time the membership changes, all of those copies go stale at once. It is
the defect this project's own index removed from its release labels
([T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md)) and that
`.handoff/config.md` warns about in its own words, arriving in the mechanism meant to prevent
sessions overreaching.

**Three instances, all on 2026-08-22, and the first is the one that argues the case.**

| # | The grant | Members | What the extension cost |
| :-- | :--- | ---: | :--- |
| 1 | four tasks through the full lifecycle | 4 | Extended to cover tasks raised during the work. Two were raised and worked under it. **The four rows were not annotated and still read *any other task* is not covered** — found while raising this record, and annotated the same day |
| 2 | five records, unattended | 5 | Extended to a sixth when it became the release's blocker. Five annotations written |
| 3 | the six, unattended | 6 | Extended to cover whatever the work raises. A second row written into all six |

**Fifteen rows across three extensions, and one extension recorded in none of the records it
widened.** The two that were annotated were annotated by the session that widened them, minutes
later, with the change fresh. The one that was not is the one where the widening happened first and
the records were revisited hours afterwards — which is the ordinary case rather than the unlucky one.

**Why this is a decision and not a fix.** The copy is not an accident: it is the guard. A session
opening a covered record has to see the whole grant, or it can work a record that was never in it.
Removing the copy without replacing that property makes the mechanism weaker, not tidier. So the
question is what can carry membership such that one write serves every reader — and the candidates
differ in what they cost an adopter, not only this project.

**Scope**
- In: whether the per-record copy stays, and what replaces it if not
- In: the candidates and what each costs — a field the ordering tool can filter on, so membership is
  derived the way [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) made a release's
  membership derived; a row that names only *this* record's authority and points at one home for the
  rest; or nothing, keeping the copy with a stated rule about annotating on change
- In: **what an adopter pays.** A field is this project's `.taskmd/config.md` and not the shipped
  default, so [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s bar does not apply —
  but `CLAUDE.md`'s rule is text an adopter copies, and a rule naming a field they do not have is
  worse than the copy it replaced
- In: what happens to the fifteen rows already written, which record real instructions given on a
  real date and may not be rewritten
- Out: changing any grant already given. This decides the mechanism, not the authorisations
- Out: the wording of `CLAUDE.md`'s rule, unless the answer requires it — in which case that edit is
  tier 1 and is priced separately

**Inputs**
- `CLAUDE.md`, *Two rules that bind before there is any task* — the rule that produces the copy, and
  the reason it is written that way
- The fifteen rows themselves, in the records of the three grants above
- [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) — the same defect
  removed from release labels, and the shape of the fix that worked: name only the exceptions
- [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) — filtering on a field the schema
  names, which is how a release's membership stopped being written down

**Acceptance criteria**
- [ ] The answer is recorded with its reason, and every rejected candidate is named with its cost
- [ ] The property the copy currently guarantees — a session opening any covered record sees the whole
      grant — is either preserved by the answer or **explicitly given up**, with what that risks
- [ ] What happens to the rows already written is stated, and it does not involve rewriting a record of
      an instruction given
- [ ] If the answer needs a field, whether an adopter can follow the same rule without it is answered

**Open questions**
- ~~**Copy, point, or derive?** — the project owner. The recommendation is **derive**: a `grant` field
  naming the authorisation, so `list` answers membership the way it already answers a release's, and
  each record's row carries the **authority and its limits** — which do not drift — rather than the
  membership, which does. Against it: it is a second grouping field on every covered task, it needs
  the rule in `CLAUDE.md` reworded, and an adopter without the field falls back to the copy anyway.
  *Do nothing* is the honest alternative and it is cheap: three instances is a small corpus, and the
  one that went stale was caught within hours by the sweep that exists for it.~~ **Answered
  2026-08-22: derive, with a `grant` field.** See the Log row of that date, which carries why it
  guards better rather than only tidier, and names what the answer leaves for this record to do.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** added this record to the unattended grant of **2026-08-22** — the one that covers a batch worked through the full lifecycle, committed and pushed, **stopping before the audit**. **What it covers here:** this record, from `specify` through to closure, without stopping to ask for each phase. **What the grant covers in total, as extended three times:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md), [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), this record, and any task the work raises. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit**. **Specific to this task, and it is the whole of what was granted:** finish the **record** and nothing else. Answer §1's three remaining criteria from documents already to hand, close the decision, and **raise the build as its own task** with the field design settled. **Do not build it** — no key added to `.taskmd/config.md`, no `grant` value written to any record, and no edit to `CLAUDE.md`, whose rule is tier 1 and paid on every turn of every session. The owner priced that against finishing the job in one go and chose the record. **A further reason the split is right, and it is a limit of the tool rather than a preference:** a session cannot verify its own instruction-file edit, because `CLAUDE.md` is fixed before its first tool call — so the tier-1 half needs a later session or a subagent to confirm the rule loads, and bundling it here would have produced an unverifiable claim. **It authorises phases, not answers.** |
| 2026-08-22 | (no change) | **This record's own extension is instance 4, and it is left in as evidence rather than tidied away.** Adding this task to the grant cost **seven more rows**: the authorisation above, and a one-line annotation in each of the six records the grant already covered. That is the pattern §1 measures, happening inside the task raised to decide what to do about it, hours after the decision was taken — because the answer is *derive*, the field does not exist yet, and the old mechanism is the only one available until it does. **Twenty-two rows across four extensions now**, and §1's table is left at three instances because it records what the case rested on when it was made; this row is the fourth and it changes nothing about the answer. **What it does change is the interim question**, which belongs in this record's own work: whether to keep growing the copy until the field lands, or to stop annotating and let each record guard only itself. |
| 2026-08-22 | (no change) | **The owner answers: derive it, with a `grant` field.** Answered 2026-08-22, the day the third instance was recorded. **Why it is the stronger guard and not merely the tidier one** — which matters, because §1 says the copy *is* the guard and nothing may replace it that guards less. A list answers *what else is covered* and is the half that drifts. A field answers *am I covered*, in the record a session has already opened, and it cannot drift because there is one write per task; *what else* is then a command, which cannot go stale either. The failure the copy exists to prevent is a session **stretching** a grant to a task never in it, and under a field that task simply carries no grant value — checkable per record rather than remembered from a list. *Rejected: keep the copy and annotate on every change* — no schema change and no tier-1 edit, at the price this record measured: fifteen rows across three extensions and one extension annotated nowhere. *Rejected: name only this record's authority and point at one home for membership* — one write per change, but the home has to be somewhere a session actually opens; a handoff is ephemeral and a task record naming the membership is the same copy with one fewer instance. **What the answer does not settle, and what still stands in §1's criteria:** the field is almost certainly a **pass-through** rather than an enumerated one, since a vocabulary would need a config edit per grant, and this project's own fixture already carries such a field; `list` then filters on it because [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) made filtering work on any field the schema names. Whether the fifteen rows already written are migrated or left as records of instructions given, and whether an adopter who has not added the field can still follow `CLAUDE.md`'s rule, are both open and both are criteria here. **The `CLAUDE.md` edit is tier 1 and is paid on every turn of every session**, so it is priced rather than assumed. |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, after the same pattern appeared three times in one day and the third was reported to them with the first two. **Held back until there were three instances**, deliberately: this project has been caught building a rule for a class of one, and one drifted enumeration is an accident. **The first instance is the evidence and it was captured before being repaired** — the four records of that grant still read *any other task* is not covered, hours after two raised tasks had been worked under its extension, and they are annotated the same day this record was raised. Repairing it first would have left the case resting on two instances that were both caught immediately. **A decision rather than a fix**, by the schema's own test: the copy is the guard, not the defect, so nothing changes until it is known what preserves the property the copy buys. **Not in the unattended grant of 2026-08-22** — the owner confirmed that grant covers six records plus what a session's own work raises, and this was raised by their request rather than by that work. |
