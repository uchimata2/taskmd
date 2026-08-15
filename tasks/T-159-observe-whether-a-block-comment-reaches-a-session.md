---
id: T-159
title: Observe whether a block comment in CLAUDE.md reaches a session
type: analysis
status: done
phase: review
parent: T-153
blocked_by: []
related: [T-050, T-155]
work_package: M6
owner: maintainer
business_value: high
effort: xs
created: 2026-08-15
updated: 2026-08-16
deliverables: []
---

# T-159 — Observe whether a block comment in `CLAUDE.md` reaches a session

## 1. Specify

**Outcome**
An observation, from a session that started after the change, of whether the five block comments now
in `CLAUDE.md` are in what it was handed. Either the 663-character saving
[T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) recorded is real, or it is
not and the file grew instead.

**Why this one**
[T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) rests on a documented
harness behaviour that **no session in this repository has ever observed**, and it changed
`tests/test_budget.py` to follow that documentation. If the documentation is wrong, tier 1 is larger
than before and the one check that would have noticed is now looking past it.

**`high` for an `xs` task, deliberately.** The work is reading one thing once. What hangs on it is a
gate this project relies on, and [the project's own rule](../CLAUDE.md) is that a claim about
behaviour is verified by running the thing, never by reading its documentation.

**Scope**
- In: whether the commented text is present in what a fresh session receives unasked.
- In: the counted figure at that moment, so the observation and the check are compared rather than
  assumed to agree.
- Out: the path-scoped rule mechanism. That is
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md), a different
  mechanism needing a different test, and folding them would make one failure look like two.
- Out: reverting anything. If the comments do reach a session, what to do about it is a decision, and
  this task supplies the evidence for it.

**Inputs**
- `CLAUDE.md` — the five comment blocks, listed in T-153's `implement`
- [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) — the documented behaviour
- [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) — how this repository
  established tier 1 by observation before, which is the method to repeat

**Acceptance criteria**
- [x] The observation is made in a session that started **after** the change, and the record says so
- [x] It reports what was found, not what was expected — including if the comments arrived
- [x] The counted figure is taken in the same session and compared with the observation
- [x] If the comments arrive, `tests/test_budget.py`'s strip is reported as unsound, and the task
      that decides what to do about it is named
- [x] The result is written into this record on the day it is known

**Open questions**
- none.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish that this session qualifies: find the commit that introduced the comment markers and show it predates the session | The commit and the two dates below |
| 2 | Choose a marker the observation cannot fake — a string present in `CLAUDE.md` **only** inside a comment, so its absence is not a judgement about wording | The two task ids below |
| 3 | Read what this session was handed unasked, and check each of the five blocks against it | Observation |
| 4 | Take the counted figure in the same session and reconcile it with the observation, rather than assume the two agree | The command output below |
| 5 | Report what was found. Name where the consequence lands — whichever way it fell | This record, and the note to T-153 |

## 3. Implement

**This session started 2026-08-16 and the change is `557a7ec`, 2026-08-15** — the only commit that
has ever changed a comment marker in `CLAUDE.md`:

```
git log --format="%h %ad %s" --date=short -S "<!--" -- CLAUDE.md
557a7ec 2026-08-15 Take four audit repairs as far as this session can take them
```

So the file this session was handed at its first turn is the file as `557a7ec` left it. That is the
condition [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) established the method
for, and the one T-153 could not meet from inside itself.

**The comments did not arrive. All five were stripped.**

The marker matters more than the count, so it is stated first. Two task ids appear in `CLAUDE.md`
**only** inside comment blocks — nowhere else in the file:

```
grep -n "T-047\|T-118" CLAUDE.md
76:why the bound is another file's length: T-118.
83:carried here in full for that reason (T-047); §3.2 presupposes a phase and stays with the method.
```

Line 76 is inside block 4, line 83 inside block 5. **Neither string is in what this session was
handed**, while `T-054` — the one task id in the file's uncommented prose — is. A marker beats a
judgement about missing paragraphs here: absence of a whole passage invites the reading *I summarised
it*, whereas a five-character id is either present or it is not.

Each of the five blocks is absent, checked by what stands next to it in the handed copy:

| # | Lines on disk | What it justifies | In the handed copy, the paragraph before is followed by |
| :-- | :--- | :--- | :--- |
| 1 | 34–36 | the method having one home | `**The method has one home:` — directly under the heading |
| 2 | 51–55 | the bound being another file's length | `` `reference/TASK-WORKFLOW.md` is the pre-split standard `` |
| 3 | 60–63 | what the pre-split standard left behind | `**What earns a place here.**` |
| 4 | 74–77 | why the unannounced-activity exception is tier 1 | `### Two rules that bind before there is any task` |
| 5 | 81–84 | why METHOD §3.1 and §3.3 are carried in full | `#### One phase per request — never auto-advance` |

**The counted figure agrees, measured 2026-08-16 in this same session.** It is unchanged from the
figure T-153 recorded on 2026-08-15, which is itself the point — nothing has drifted between the day
the strip was written and the day it was observed:

```
python -m unittest discover -s tests -p "test_*.py"
tier 1 6305 chars under by 1541 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       836 chars of block comment are not counted: the harness is documented to strip them before injecting and this check follows it - not yet observed here (T-153)
```

Counted independently of the check, so the two are compared rather than one quoting the other:

```
raw chars       6744
comment blocks  5
comment chars   831
stripped chars  5913
```

The five-character disagreement with the check is expected and is not a defect in either: the check
strips whole lines and so takes the newline after each `-->`, five blocks and five newlines. Its
figures are therefore 836 and 5,908 where a `<!--.*?-->` regex sees 831 and 5,913. **The check's
`5908` is what a session pays for `CLAUDE.md`, and this session's reading of its own input agrees
with it** — the comment text is not there.

**Decisions & assumptions**

- **A marker string, not a missing-paragraph judgement** — 2026-08-16. The observation is a session
  reporting on its own input, which is the weakest kind of evidence this repository accepts, so it
  was made falsifiable: an id that exists on disk only inside a comment either arrived or did not.
  *Rejected:* listing the five passages as absent and leaving it there, which cannot distinguish
  *stripped* from *present but not worth mentioning*.
- **The figure was re-derived, not carried from T-153** — 2026-08-16. `specify` asks for the count
  *at that moment* precisely so the observation is not compared against a number from another day.
  It came out identical, which is a result rather than a formality.
- **Nothing was reverted or edited outside this record** — 2026-08-16, per `specify`'s second Out.

**Outputs produced**

Nothing outside this record. The observation, the marker and the two figure sets above are the
outputs of steps 1 to 4.

**What follows, and where it lands.** The strip in `tests/test_budget.py` is **sound**, so the
saving T-153 recorded is real and its acceptance criterion 5 is now answerable. One consequence is
outside this task's scope and is not taken here: the second line of `report`'s output still says
`not yet observed here (T-153)`, and that sentence is now false. It was T-153's plan step 5 —
keeping an unobserved premise visible — and it has done its job. **Correcting it is T-153's
`review`, not this task's**, which is also where the criterion it serves is judged.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Observation made in a session that started after the change, and the record says so | met | Session 2026-08-16; change `557a7ec`, 2026-08-15, shown by the only commit ever to touch a comment marker in the file |
| Reports what was found, not what was expected — including if the comments arrived | met | The expected result and the found result coincide, so the marker test carries the honesty here rather than the wording: `T-047` and `T-118` were checked either way |
| The counted figure is taken in the same session and compared with the observation | met | 6,305 counted with 836 stripped, plus an independent count of 6,744/831/5,913; the five-character gap is explained rather than rounded away |
| If the comments arrive, the strip is reported as unsound and the deciding task named | **n/a** | **Recorded as vacuous, not as met.** The antecedent did not occur, so nothing exercised this clause. The mirror consequence was reported instead, and T-153 named for it |
| The result is written into this record on the day it is known | met | Written 2026-08-16, the day of the observation |

**Child fix tasks raised**
- none. The one consequence found belongs to
  [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s open `review`, which is
  a task that already exists rather than one to raise.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Raised from [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s review, which met four of five criteria and could not meet the fifth: a session cannot observe a change to the instruction file it was handed before its first tool call. The maintainer chose to leave the observation to a later session rather than spend a subagent on it. T-153 is `blocked_by` this task and does not close until it answers. |
| 2026-08-16 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review` — asked at the start of the resuming session, covering **T-159 and nothing else**; T-155 was left untouched in the same answer. Recorded here rather than only in the request, because an authorisation kept anywhere else is one a later session can miss (METHOD §3.1). The `specify` written on 2026-08-15 was agreed as it stood, which is its exit criterion. |
| 2026-08-16 | → done | **Observed: the five block comments do not reach a session.** `tests/test_budget.py`'s strip is sound and T-153's 663-character saving is real. The evidence is a marker rather than a judgement — `T-047` and `T-118` are in `CLAUDE.md` only inside comments and reached nothing. Four criteria met; the fifth is recorded **vacuous**, its antecedent never having occurred. Unblocks T-153, whose `review` also inherits the one consequence found: `report`'s `not yet observed here` line is now false. |
