---
id: T-237
title: The softening clause T-228 repaired has a second instance, and an idiom behind it
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-228, T-176, T-193, T-196]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-237 — The softening clause T-228 repaired has a second instance, and an idiom behind it

## 1. Specify

**Outcome**

`github-issues.md` carries no unexamined instance of *it was never the evidence*, and the project has
decided whether the phrase is a defect wherever it appears or only where the document refutes it.

**Where this came from**

Found on 2026-08-23 while [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md)
was reading the standing-check section, hours after
[T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md) closed
having judged that exact clause softening and repaired it.

**T-228 repaired one instance and there are two.** The reader quoted *"The destination is gone and was
never the evidence"*, which sits under *Verify*; that one is now three sentences that do not overclaim.
The second is under *The standing check* and was untouched:

> The scratch repository was created for this run and is the owner's to delete; the credential a
> session can reach carries `repo` and not `delete_repo`, measured on the day. **It was never the
> evidence** — the counts above are, and anyone doubting them runs the procedure again rather than
> looking for an artefact.

**T-228's own reasoning reaches it.** The refutation was that a kept artefact *could* have been
re-checked, because *Verify* compares a destination against the source's own id set. The standing
check is stronger on that point, not weaker: its nine rows run against a **live** repository, so a
kept scratch repository is exactly the thing they could be re-run against.

**The half of that sentence that is honest is also current**, and was re-measured today rather than
taken from the page: `gh auth status` reports scopes `gist`, `project`, `read:org`, `repo`,
`workflow` — no `delete_repo`. So *the session cannot delete it* holds; it is only *it was never the
evidence* that overclaims.

**And it is an idiom, not a slip, which is why this is a record and not an edit.** The phrase is
written into the **acceptance criteria of two closed tasks** —
[T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) (*"the record says the
destination was never the evidence"*, criterion and plan step 10) and
[T-196](T-196-delete-the-scratch-repository-the-standing-check-ran-against.md) — and appears in
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)'s Log. A project that
made a phrase an acceptance criterion twice was not being careless with it, so whether it is wrong
everywhere or only where the document contradicts it is a real question rather than a tidy-up.

**Scope**

- In: the second instance in the shipped binding, judged on T-228's own test and repaired or defended
- In: whether the idiom is a defect wherever it appears, or only where the same document elsewhere
  shows the artefact could have been re-checked — the distinction T-228's reasoning actually turns on
- Out: rewriting the closed criteria in T-193 and T-196. They are dated statements of what was agreed
  at the time and METHOD rule 5 permits annotating them, never rewriting them. Whether they are
  annotated at all is in scope; changing what they say is not
- Out: re-opening T-228. Its verdict on the arrangement stands and nothing here touches it
- Out: the measurements in the standing-check section, which are
  [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md)'s

**Inputs**

- `plugin/skills/taskmd/docs/bindings/github-issues.md` — both instances, and the *Verify* section
  that refutes the claim
- [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md) §3 — the
  test applied, and the repair made to the first instance
- [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md),
  [T-196](T-196-delete-the-scratch-repository-the-standing-check-ran-against.md) — the phrase as an
  acceptance criterion, twice

**Acceptance criteria**

- [ ] The second instance is repaired, or defended in the record with the reason it differs from the
      first
- [ ] A sweep for the phrase is run over the whole tree and its result recorded, so *two* is a
      measured count and not the number that happened to be noticed
- [ ] Whether the idiom is wrong everywhere is answered, and the answer says what a future use of it
      would have to satisfy
- [ ] Nothing in T-193 or T-196 has its recorded text changed

**Open questions**

- ~~**Was T-228's repair meant to reach both, or only the sentence the reader quoted?**~~ **Answered
  2026-08-23 by the owner: yes, it reaches both.** Original question and recommendation follow.
  — the **project owner**, who answered T-228's question. **Recommendation: treat it as reaching both.** The owner's
  *yes* was about a claim the document makes that its own contents refute, and that is true of the
  second instance for the same reason. *Against:* the reader named one sentence, and extending a
  ruling past what was put to them is how an accepted decision drifts — which is the failure T-167 and
  T-228 both exist to prevent, arriving from the other side.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Sweep the whole tree for the phrase **with whitespace normalised**, not line by line | a per-file count, and the total |
| 2 | Repair the shipped instance on T-228's own test — could the artefact have been re-examined if kept? | the edited binding |
| 3 | State what a future use of the idiom must satisfy, so the answer is a rule and not a verdict on two sentences | the rule, in this record |
| 4 | Confirm nothing in T-193 or T-196 changed | a diff |

**Step 1 normalises whitespace because a line-based sweep already failed at this once.** The phrase
wraps, and a `grep` for it found the copies that happen to sit on one line while missing the one in
the shipped document — the instance this record exists for.

## 3. Implement

**Decisions & assumptions**

- **The shipped instance is repaired, on the owner's answer of 2026-08-23** — the ruling reaches both.
  The half that is true is kept: the comparison needs a source and a destination at the same moment,
  and the session's credential genuinely cannot delete the repository. What goes is *it was never the
  evidence*, because the nine rows run against a **live** repository, so a kept scratch repository is
  precisely what they could have been re-run against. The sentence now says the artefact is gone, what
  the record is instead, and **what the deletion costs** — an independent re-check.
- **The rule for any future use, which is what makes this more than two edits** — 2026-08-23. *X was
  never the evidence* is legitimate **only where the artefact could not have been re-examined even if
  kept.** Where it could have been — a repository, a dataset, a rendered output, anything a second
  party could run a comparison against — say the artefact is gone, say what the record is instead, and
  say what keeping it would have allowed. The failure is not the phrase; it is converting a loss into
  a principle so that nothing is owed for it.
- **Nothing in T-193 or T-196 is edited** — 2026-08-23. Their acceptance criteria asked, in those
  words, that the record say the destination was never the evidence. Under the rule above that was the
  wrong thing to ask for, and it is also a dated statement of what was agreed on the day; METHOD rule
  5 forbids rewriting it. The rule binds from now on, and those two records are why it is written down
  rather than applied twice and forgotten.

**Outputs produced**

- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the second instance

**Verification**

**Step 1, and it corrected the count this record was raised with.** §1 says *two*; a whitespace-
normalised sweep of every Markdown file in the tree, excluding `.git` and the handoff archives,
returns **18 occurrences across 7 files**:

```text
  1  ./plugin/skills/taskmd/docs/bindings/github-issues.md
  1  ./tasks/T-108-…   1  ./tasks/T-176-…   4  ./tasks/T-193-…
  3  ./tasks/T-196-…   4  ./tasks/T-228-…   4  ./tasks/T-237-…
files: 7   occurrences: 18
```

**Exactly one of them is in a document an adopter receives**, and that is the one repaired. The other
seventeen are task records — this one, the two that made the phrase a criterion, the reader's own
quotation of it, and T-228's reasoning about it.

**A line-based sweep of the same tree returns 15 across 6 files, and the file it misses is the
binding.** The phrase wraps as *It was never the / evidence*, so `grep` sees neither half. That is the
finding worth keeping from this step: the sweep that would naturally be run to check this rule is
blind to the only instance that ships.

**Step 4, nothing changed in the two closed records.**

```text
git diff --stat -- tasks/T-193-*.md tasks/T-196-*.md   ->   (empty)
```

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The second instance is repaired, or defended with the reason it differs from the first | met | Repaired. It does not differ: the nine rows take a live repository, so a kept artefact was re-runnable, which is the same refutation T-228 applied to the first |
| A sweep for the phrase is run over the whole tree and its result recorded, so *two* is a measured count | met | 18 occurrences, 7 files, whitespace normalised — and the count in §1 was wrong. **One is in a shipped document**; the rest are records. The naive line-based sweep returns 15 and misses the shipped one, which is recorded because it is the sweep anyone would run |
| Whether the idiom is wrong everywhere is answered, and the answer says what a future use must satisfy | met | Not everywhere. It is legitimate only where the artefact could not have been re-examined even if kept; otherwise say it is gone, what the record is instead, and what keeping it would have allowed. §3 carries it as a rule |
| Nothing in T-193 or T-196 has its recorded text changed | met | `git diff` over both is empty. Their criteria asked for the wrong thing and are left as the dated record of what was agreed |

**Child fix tasks raised**
- none.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 held one, the owner's, answered
2026-08-23 and struck through above.


## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed on the owner's answer: the ruling reaches both instances.** The shipped one is repaired the way T-228 repaired the first — the true half kept, the overclaim replaced by what the loss actually costs, which here is an independent re-check, since the nine rows take a live repository. **The sweep corrected this record's own count**: §1 said two and the tree holds **18 across 7 files**, exactly one of them in a document an adopter receives. **And the sweep anyone would run cannot see that one** — the phrase wraps as *It was never the / evidence*, so a line-based `grep` returns 15 and misses the shipped instance, which is why the criterion asked for the sweep to be recorded rather than performed. **The answer is a rule rather than a verdict on two sentences**: the idiom is legitimate only where the artefact could not have been re-examined even if kept. **T-193 and T-196 are untouched**, `git diff` empty — their criteria asked for the wrong thing and are the dated record of what was agreed, which is why the rule is written down instead. |
| 2026-08-23 | → proposed | Raised while working [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), whose scope puts the document's framing out by name, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit** — unchanged. **The open question is the owner's, so this record stops at `specify`**, exactly as [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md) does: extending a ruling past what was put to the person who gave it is the drift both [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) and T-228 exist to prevent, so it may not be done by the session that found the second instance. **Raised rather than fixed in passing**, which is the point: the edit is one sentence and the question behind it is whether a phrase this project made an acceptance criterion **twice** is wrong everywhere. **T-228 is not re-opened and was not edited** — it repaired the instance it was given and said so accurately; that its scope was one sentence is a fact about the reader's report, not an error in the record. |
