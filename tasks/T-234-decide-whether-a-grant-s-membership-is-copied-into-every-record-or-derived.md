---
id: T-234
title: Decide whether a grant's membership is copied into every record or derived
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-106, T-087, T-136]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-23
adopter_visible: no
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
| 1 | Answer the second criterion: name the property the per-record copy guarantees today, and say whether the field keeps it or gives it up — and if it gives it up, what that risks | a recorded answer in §3, in the terms §1 states the property |
| 2 | Run the mechanism the answer depends on, rather than assuming it: whether `list` can filter on a field like `grant` as things stand | the command and its output |
| 3 | Answer the third criterion — what becomes of the rows already written — against METHOD rule 5, and against the fact that the corpus has grown since §1 counted it | a recorded answer, and a re-count of what exists today |
| 4 | Answer the fourth — whether an adopter with no such field can follow the same rule — and say what that requires of `CLAUDE.md`'s wording **without making the edit**, which the grant excludes | a recorded answer naming the principle, and the tier-1 cost left unpaid and visible |
| 5 | Dry-run the answer on a grant row written today, on paper, and check a session could still tell the record was covered | the before and after of one row, in §3, applied to nothing |

**Step 2 before steps 1 and 3 would be wrong, and before step 4 would be pointless** — but it must
happen before the answer is written up, because the whole case for *derive* is that membership becomes
a command. If no command can read the field today, the answer is still *derive* and its cost changes:
the build is not one field, it is a field plus a config entry.

**Step 5 is the verification and it is deliberately non-mutating.** The grant covers this record and
**not building what it decides**, so the answer may be tried on paper and not applied. A dry run can
still surprise: the test is whether a session opening the rewritten row can tell it is covered, which
is the property step 1 is about.

**Outputs**

- no file. The answer's home is §3 of this record; the field, the config entry and the `CLAUDE.md`
  wording are all outside this record's grant and belong to whatever builds them

## 3. Implement

**Decisions & assumptions**

- **The property is given up deliberately, and what replaces it guards the actual failure better**
  — 2026-08-23, answering the second criterion. Today's copy guarantees that *a session opening any
  covered record sees the whole grant*. Under a `grant` field it does **not**: the session sees that
  **this** record is covered, by which authority and with what limits, and learns the rest by running
  a command. **That is the property surrendered, stated plainly rather than argued away.** What it
  buys is that the failure the copy exists to prevent — a session **stretching** a grant to a task it
  never reached — becomes a per-record fact that cannot drift, because there is one write per task. A
  task never in the grant simply carries no value, which is checkable in the record already open.
  **What it risks:** a session that cannot run the tool, or does not think to, no longer sees *what
  else* is covered, so it cannot notice that a sibling record it was about to touch is outside the
  batch. That is a real loss and it is smaller than the one it replaces, because noticing a sibling
  is not how overreach happens — working the record in front of you is.
- **The answer needs a config entry as well as a field, and that was measured rather than assumed**
  — 2026-08-23. See *Verification*. `list` refuses a filter on any field the project has not named,
  so *membership becomes a command* is **not** true of a bare pass-through field. The build is a
  field **plus** an entry in this project's `.taskmd/config.md`. That does not change the answer, and
  it does change its price, which is the kind of thing a decision record exists to hand over.
- **The rows already written stay exactly as they are, and no migration happens** — 2026-08-23,
  answering the third criterion. Each records an instruction given on a date, which METHOD rule 5
  forbids rewriting. **They are also already handled**: the pattern this project reached for — a later
  row saying *the list below is what the grant covered when it was given, and it is left as written;
  T-NNN's own row carries the membership as it now stands* — is the annotation rule applied correctly,
  and it is why the third extension's omission was recoverable. So the answer for the existing rows is
  **nothing at all**, and the field applies to grants given from now on.
- **`CLAUDE.md`'s rule must state the requirement and not the mechanism, and the edit is not made
  here** — 2026-08-23, answering the fourth criterion. An adopter has no `grant` field and no config
  entry for one; a tier-1 rule naming a field they do not have is worse than the copy it replaces,
  which §1 says outright. **The wording principle: require that a session opening a record can tell
  whether it is covered and by what authority, and leave *how* to the project.** A copy satisfies it,
  a field satisfies it, and neither is named in the rule. That keeps tier 1 short — it is paid on
  every turn of every session — and keeps the rule true for a clone with no schema of its own.
  **The edit itself is out of this record's grant**, which covers the record and not what it decides,
  so the tier-1 cost is named and left unpaid rather than absorbed.

**Outputs produced**

- the four answers above. No file: the field, the config entry and the `CLAUDE.md` wording all belong
  to whatever builds them

**Verification**

**Step 2, run rather than reasoned about.** The case for *derive* rests on membership becoming a
command, so the command was tried. `list` accepts a filter only on fields the project has named:

```text
$ ./plugin/bin/taskmd list --waiting_on "the project owner" --open
unknown filter: --waiting_on. This project accepts: --adopter_visible, --blocked_by, --blocks,
--business_value, --children, --effort, --owner, --parent, --phase, --related, --status, --type,
--work_package
exit 2
```

`adopter_visible` is in that list and is **not** in the shipped schema — it is in this project's own
`context_fields`. So the mechanism exists and a bare pass-through field is not enough on its own.

**Step 3, re-counted rather than carried forward.** §1's table counts **fifteen** rows across three
grants, measured 2026-08-22. **Three more were written on 2026-08-23** — in
[T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md),
[T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md) and
[T-237](T-237-the-softening-clause-t-228-repaired-has-a-second-instance-and-an-idiom-behind-it.md),
each carrying the authority and its exclusions, by the extension that requires a raised task to carry
the grant in its own Log. **So the corpus is eighteen and growing at three a day under one grant**,
which is the argument for the answer arriving as evidence rather than as a prediction. §1's fifteen is
left as written: it was right on its date.

**Step 5, the dry run — on paper, applied to nothing.** Take T-236's row as written today. It carries
the authority, the exclusions, and *what the grant covers here*. Under the answer it would lose
nothing except the exclusion list, and gain `grant:` in the front matter:

```text
grant: unattended-2026-08-22

| 2026-08-23 | → proposed | Raised from T-226's implement … under the project owner's unattended
grant of 2026-08-22 as extended the same day. What it covers here: this record, through the
lifecycle to closure. Its limits are the grant's: it authorises phases, not answers. |
```

**A session opening that record can still tell it is covered, by which authority, and to what extent
— which is the property that had to survive.** What it cannot tell without a command is that
[T-231](T-231-cut-the-next-release.md) and the audit are outside the same grant. **The dry run
surprised in one way**: the exclusion list is the part that drifts *and* the part a session reads to
avoid overreaching, so removing it moves a safety net behind a command. That is the risk named in
*Decisions* above, and it is why the answer says the property is given up rather than preserved.

**Nothing was applied.** No `grant` field was added to any record, no config was edited, and
`CLAUDE.md` is untouched — the grant covers this record and not what it decides.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is recorded with its reason, and every rejected candidate is named with its cost | met | The owner's answer and its two rejected candidates — *keep the copy and annotate on every change*, and *name only this record's authority and point at one home* — are in the Log row of 2026-08-22, each with what it costs. §3 adds the price the answer turned out to carry: a config entry as well as a field |
| The property the copy guarantees is preserved or **explicitly given up**, with what that risks | met | **Given up**, said in those words in §3, with the risk named: a session no longer sees what *else* is covered without running a command, so the exclusion list moves behind the tool. The dry run in §3 is what turned that from a prediction into a stated cost |
| What happens to the rows already written is stated, and does not involve rewriting a record of an instruction given | met | Nothing happens to them. They are already handled by the annotation pattern this project reached for, and METHOD rule 5 forbids more. Re-counted while answering: §1's fifteen was right on 2026-08-22 and the corpus is **eighteen** today, three having been written on 2026-08-23 by the extension that requires it |
| If the answer needs a field, whether an adopter can follow the same rule without it is answered | met | Yes, and the wording principle is given: `CLAUDE.md` states the requirement — a session opening a record can tell whether it is covered and by what authority — and never the mechanism, so a copy and a field both satisfy it. **The edit is not made**, being outside this record's grant, and the tier-1 cost is named rather than absorbed |

**Child fix tasks raised**
- none. The field, its config entry and the `CLAUDE.md` wording are what this decision commits
  someone to, and the grant on this record covers **the record and not building what it decides** —
  so raising the build here would be the widening that grant excludes. It is the owner's to schedule.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds one, struck through and
answered by the owner on 2026-08-22. **One thing is flagged for the owner rather than left in a closing
record**: the build this decision commits to has no task, deliberately, because raising one would cross
this record's stated boundary. It is named here so that *no follow-on task* is visibly a choice and not
an omission.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed: four criteria, four met, no child raised — and the absent child is a decision, not an omission.** The owner answered *derive, with a `grant` field* on 2026-08-22; this record answered the three things that answer left open. **The property the copy guarantees is given up, in those words**, and the reason it is still the stronger guard is that overreach happens by working the record in front of you, not by failing to notice a sibling. **The answer cost more than it looked**: `list` refuses a filter on any field the project has not named, measured, so *membership becomes a command* needs a config entry as well as a field. **Nothing happens to the rows already written** — METHOD rule 5, and the annotation pattern already applied handles them. **The corpus was re-counted rather than carried forward**: §1's fifteen was right on its date and today it is eighteen, three rows having been written on 2026-08-23 by the extension that requires them, which is the argument arriving as evidence. **Nothing was applied** — no field, no config edit, `CLAUDE.md` untouched — because the grant covers this record and not what it decides, and the tier-1 wording is priced and left unpaid. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** added this record to the unattended grant of **2026-08-22** — the one that covers a batch worked through the full lifecycle, committed and pushed, **stopping before the audit**. **What it covers here:** this record, from `specify` through to closure, without stopping to ask for each phase. **What the grant covers in total, as extended three times:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md), [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), this record, and any task the work raises. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit**. **Specific to this task, and it is the whole of what was granted:** finish the **record** and nothing else. Answer §1's three remaining criteria from documents already to hand, close the decision, and **raise the build as its own task** with the field design settled. **Do not build it** — no key added to `.taskmd/config.md`, no `grant` value written to any record, and no edit to `CLAUDE.md`, whose rule is tier 1 and paid on every turn of every session. The owner priced that against finishing the job in one go and chose the record. **A further reason the split is right, and it is a limit of the tool rather than a preference:** a session cannot verify its own instruction-file edit, because `CLAUDE.md` is fixed before its first tool call — so the tier-1 half needs a later session or a subagent to confirm the rule loads, and bundling it here would have produced an unverifiable claim. **It authorises phases, not answers.** |
| 2026-08-22 | (no change) | **This record's own extension is instance 4, and it is left in as evidence rather than tidied away.** Adding this task to the grant cost **seven more rows**: the authorisation above, and a one-line annotation in each of the six records the grant already covered. That is the pattern §1 measures, happening inside the task raised to decide what to do about it, hours after the decision was taken — because the answer is *derive*, the field does not exist yet, and the old mechanism is the only one available until it does. **Twenty-two rows across four extensions now**, and §1's table is left at three instances because it records what the case rested on when it was made; this row is the fourth and it changes nothing about the answer. **What it does change is the interim question**, which belongs in this record's own work: whether to keep growing the copy until the field lands, or to stop annotating and let each record guard only itself. |
| 2026-08-22 | (no change) | **The owner answers: derive it, with a `grant` field.** Answered 2026-08-22, the day the third instance was recorded. **Why it is the stronger guard and not merely the tidier one** — which matters, because §1 says the copy *is* the guard and nothing may replace it that guards less. A list answers *what else is covered* and is the half that drifts. A field answers *am I covered*, in the record a session has already opened, and it cannot drift because there is one write per task; *what else* is then a command, which cannot go stale either. The failure the copy exists to prevent is a session **stretching** a grant to a task never in it, and under a field that task simply carries no grant value — checkable per record rather than remembered from a list. *Rejected: keep the copy and annotate on every change* — no schema change and no tier-1 edit, at the price this record measured: fifteen rows across three extensions and one extension annotated nowhere. *Rejected: name only this record's authority and point at one home for membership* — one write per change, but the home has to be somewhere a session actually opens; a handoff is ephemeral and a task record naming the membership is the same copy with one fewer instance. **What the answer does not settle, and what still stands in §1's criteria:** the field is almost certainly a **pass-through** rather than an enumerated one, since a vocabulary would need a config edit per grant, and this project's own fixture already carries such a field; `list` then filters on it because [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) made filtering work on any field the schema names. Whether the fifteen rows already written are migrated or left as records of instructions given, and whether an adopter who has not added the field can still follow `CLAUDE.md`'s rule, are both open and both are criteria here. **The `CLAUDE.md` edit is tier 1 and is paid on every turn of every session**, so it is priced rather than assumed. |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, after the same pattern appeared three times in one day and the third was reported to them with the first two. **Held back until there were three instances**, deliberately: this project has been caught building a rule for a class of one, and one drifted enumeration is an accident. **The first instance is the evidence and it was captured before being repaired** — the four records of that grant still read *any other task* is not covered, hours after two raised tasks had been worked under its extension, and they are annotated the same day this record was raised. Repairing it first would have left the case resting on two instances that were both caught immediately. **A decision rather than a fix**, by the schema's own test: the copy is the guard, not the defect, so nothing changes until it is known what preserves the property the copy buys. **Not in the unattended grant of 2026-08-22** — the owner confirmed that grant covers six records plus what a session's own work raises, and this was raised by their request rather than by that work. |
