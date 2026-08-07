---
id: T-043
title: Make every assumption a claim about the adopting project
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-009, T-010, T-040, T-004]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - docs/bindings/github-issues.md
  - docs/bindings/local-markdown.md
---

# T-043 — Make every assumption a claim about the adopting project

## 1. Specify

**Outcome**
Every numbered entry in both bindings' assumptions sections opens with something an adopter can
answer yes or no about **their own project**, so the check §4 describes is one a reader can actually
perform on every line rather than on most of them.

**Why this one**
`docs/BINDING.md` §4 requires it already: *"Each entry is a claim about their project that they can
confirm or deny — not a description of the backend."* T-040 defined the thirty-second check as
reading the bold claim opening each entry, then read them as an adopter would, and three across the
two bindings are descriptions rather than claims:

| Binding | Entry | Opens with |
| :--- | :--- | :--- |
| `github-issues.md` | 1 | "Ids are assigned by GitHub and cannot be chosen" — about the backend |
| `github-issues.md` | 2 | "The issue's open/closed `state` is a rendering of the status label" — about the binding |
| `local-markdown.md` | 3 | "Identity is chosen locally" — about the backend |

The failure is quiet: each of the three is **true**, and each is genuinely important, so nothing
looks wrong. What an adopter cannot do is answer it — there is no state of their project under
which "ids are assigned by GitHub" is false, so reading it confirms nothing and the entry costs
attention without spending it on a risk. §4's phrasing rule is not a style preference; it is what
makes the section a check instead of a summary.

**Scope**
- In: the opening claim of each entry in both bindings, and whether the underlying premise is
  reachable as a question about the adopting project at all.
- Out: the substance. Every one of these assumptions stays — this is about what each entry asks the
  reader, not about which assumptions the bindings make. Also out: §4's rule itself, which is right
  and is what caught this.

**Inputs**
- `docs/BINDING.md` §4, both the phrasing rule and T-040's *What the thirty seconds measures*
- Both bindings under `docs/bindings/`
- T-040 §3 step 5, which lists the three and why each fails

**Acceptance criteria**
- [ ] Every entry in both bindings opens with a sentence an adopter can answer about their project,
      checked by reading each one and stating the answer for a project that would fail it
- [ ] For each of the three rewritten, the backend fact it currently states is still present in the
      entry — moved into the explanation, not deleted
- [ ] At least one entry is shown to be answerable **"no"** by some plausible project, since a claim
      no project could deny is the same defect wearing better grammar
- [ ] The claim lines still fit the thirty-second budget after rewriting, measured the way T-040
      measured them

**Open questions**
- Entry 2 of `github-issues.md` may not have a project-facing form at all: the `state` rendering is
  a fact about the binding, and the thing an adopter can get wrong is a *habit* — closing issues in
  the UI. If it cannot be phrased as a claim about their project, that is a finding about §4's rule
  rather than a licence to leave it, and it should be raised as one. — decide during the work.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Test **all twelve** entries across both bindings against one question — can an adopter answer this about their own project? — rather than the three §1 names. §1's list came from a spot check while closing T-040, and T-044 has just shown what a specify-section table assembled that way is worth. | A verdict per entry, in §3 |
| 2 | For each failure, find its project-facing form by asking **what the adopter can do that breaks it**, not by restating the fact in the second person. A backend fact turned into "your project uses a backend where…" is the same defect with a pronoun. | A proposed lead per failing entry |
| 3 | Rewrite the leads, keeping each backend fact in the entry's explanation. | Both files under `docs/bindings/` |
| 4 | Find an entry a plausible project would answer **no** to, and name the project. A set of claims everyone confirms is a description that has learned to look like a check. | The example, in §3 |
| 5 | Re-measure the claim lines in both bindings against T-040's thirty-second budget, which the rewrite can break. | Word counts and read times |

**Sequencing.** Step 1 is widened deliberately and comes before any rewriting, because the cost of
discovering a fourth or fifth failure *after* editing three is a second pass over the same prose.
Step 4 is placed after the rewrite rather than before: it tests the new text, and an example found
against the old text would prove nothing about what replaced it.

**Shape of the deliverable — decided.** Rewrite the lead sentence in place, keeping each entry's
number and its explanation. Two alternatives rejected. Adding a separate "what you can get wrong"
line under each entry was rejected because it doubles the section and re-creates the problem T-040
solved — the claim line is what gets read, so the answerable sentence has to *be* the claim line,
not sit beside it. Dropping entries that resist rephrasing was rejected outright: every one of them
is a true and load-bearing premise, and this task is about what each entry asks, not which
assumptions the bindings hold.

**Output paths**
- `docs/bindings/github-issues.md` — the assumptions section
- `docs/bindings/local-markdown.md` — the assumptions section
- This task's §3 — the twelve verdicts, the rewrites, and the measurements

## 3. Implement

**Step 1 — nine of twelve failed, not the three §1 named.**

| Binding | # | Opened with | Answerable? |
| :--- | :-- | :--- | :--- |
| github-issues | 1 | "Ids are assigned by GitHub…" | no — about the backend |
| github-issues | 2 | "The issue's `state` is a rendering…" | no — about the binding |
| github-issues | 3 | "Every label the vocabulary needs already exists…" | **yes** |
| github-issues | 4 | "Your `gh` is 2.94.0 or newer…" | **yes** — rewritten by T-044 |
| github-issues | 5 | "Soft links live in one designated section…" | no — about the binding |
| github-issues | 6 | "The task is the issue, whole." | no — about the binding |
| local-markdown | 1 | "The folder listing is *not* the index." | no — about the binding |
| local-markdown | 2 | "Nothing else derived is materialised." | no — about the binding |
| local-markdown | 3 | "Identity is chosen locally" | no — about the backend |
| local-markdown | 4 | "Done tasks stay in the folder." | no — about the binding |
| local-markdown | 5 | "The task folder already exists." | **yes** |
| local-markdown | 6 | "A file… whose id does not match the schema is not a task." | no — about the binding |

§1 had it at three. It is nine. The spot check that produced §1's table caught the two most obvious
backend descriptions and missed the whole class of *binding* descriptions — sentences that state
what this document does, which read as authoritative precisely because they are true. Widening step
1 was the difference between fixing a third of the section and fixing it.

**Step 2 — the method that made the rewrites tractable.** Asking "how do I say this fact in the
second person?" produces "your project uses a backend where ids are assigned" — the same defect with
a pronoun. Asking **"what can the adopter do that breaks this?"** produces a claim with a real
answer, because it starts from their behaviour rather than from the fact. Applied to entry 2 of
`github-issues.md`, the answer is a click: closing an issue in the web UI. That resolves the open
question — the entry *does* have a project-facing form, and it needed the behaviour to be found
first. No finding against §4's rule is raised; the rule was right and the entries were lazy.

**Step 3 — nine leads rewritten**, each keeping its backend fact in the explanation. The two that
changed most:

- `github-issues.md` 2 → **"Nobody on your project closes or reopens an issue in the GitHub UI."**
  The old lead described the `state` rendering, which no project can deny. The new one asks about a
  habit that a mixed CLI-and-web team almost certainly has.
- `local-markdown.md` 3 → **"Only one person or agent creates tasks at a time."**

**Step 4 — the entry a plausible project answers "no" to, and it is the interesting one.**
`local-markdown.md` 3. Any team using feature branches fails it: identity is the next number after
the highest present, so two people creating tasks on separate branches both pick the same number and
collide at merge.

That limit was **not visible before this rewrite**. "Identity is chosen locally" is true, important,
and unanswerable — it describes a mechanism, and the consequence for a branching team is left as an
exercise. Rephrasing it as a claim about the project is what turned a mechanism into a risk with a
name. This is the argument for §4's rule stated better than §4 states it: the phrasing is not a
style preference, it is what makes a limit findable. Soft edge added to **T-004**, which owns the
merge-conflict behaviour and is still open; no new task, because the work already has a home.

A second, cheaper example for the same criterion: `github-issues.md` 6 — a project that does its
design thinking in pull-request review comments answers no.

**Step 5 — both sections still fit T-040's budget**, which the rewrite could easily have broken
since every lead got longer:

| Binding | Before | After | Budget |
| :--- | ---: | ---: | ---: |
| `github-issues.md` | 77 words, ~18s | **85 words, ~20s** | 30s |
| `local-markdown.md` | 44 words, ~11s | **56 words, ~13s** | 30s |

**Decisions & assumptions**
- **The lead is the claim; no "what you can get wrong" line is added beside it.** — Decided at
  `plan` and held. T-040 established that the lead is what gets read, so an answerable sentence
  sitting *under* an unanswerable one would leave the thirty-second check exactly as broken. — 2026-08-07
- **Nine rewrites, not three.** — Step 1. Stopping at §1's list would have left the section a mix of
  answerable and unanswerable entries, which is worse than uniformly bad: a reader who hits two
  descriptions in a row stops treating any of them as questions. — 2026-08-07
- **No finding raised against BINDING §4.** — The open question anticipated that entry 2 might have
  no project-facing form and that this would indict the rule. It had one. The rule is right; what
  was missing was a way to find the form, which is now recorded as step 2's method. — 2026-08-07

**Outputs produced**
- [`docs/bindings/github-issues.md`](../docs/bindings/github-issues.md) — assumptions 1, 2, 5, 6
- [`docs/bindings/local-markdown.md`](../docs/bindings/local-markdown.md) — assumptions 1, 2, 3, 4, 6

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every entry in both bindings opens with a sentence an adopter can answer about their project, checked by reading each one and stating the answer for a project that would fail it | met | All twelve read back individually, tabulated in §3 step 1. Nine were rewritten; the three that already passed were left alone rather than edited for consistency, since the criterion is about what the entry asks, not how it is worded. |
| For each rewritten entry, the backend fact is still present, moved into the explanation not deleted | met | Checked entry by entry: "ids are assigned by GitHub", "`state` is a rendering of the `status:` label", "identity is chosen locally… the next number after the highest already present", "the folder listing is *not* the index" and the rest all survive in the body of their own entries. Nothing was traded away for the phrasing. |
| At least one entry is shown answerable "no" by a plausible project | met | `local-markdown.md` 3 — any team using feature branches, since two people on separate branches pick the same next number and collide at merge. Worth more than the criterion asked for: that limit was invisible while the entry read "Identity is chosen locally", so the rewrite found a risk rather than just rephrasing one. → soft edge to T-004, which owns it. |
| The claim lines still fit the thirty-second budget | met | 85 words / ~20s and 56 words / ~13s against 30. Both grew — every lead got longer — and both still fit, which is the measurement the criterion existed to force rather than assume. |

Four met, none carried. The open question resolved against its own premise: entry 2 *did* have a
project-facing form, so BINDING §4's rule stands unamended and the entries were simply lazy.

**Child fix tasks raised**
- none. The one substantive limit surfaced — id collision on concurrent creation — belongs to T-004,
  which is open and now carries a soft edge from here rather than a duplicate task.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | All four criteria met. Step 1's widening was the task: §1 named three unanswerable entries, and testing all twelve found **nine** — the spot check had caught the backend descriptions and missed the whole class of *binding* descriptions, sentences stating what the document does, which read as authoritative because they are true. Step 2's method is the reusable part: ask what the adopter can *do* that breaks the assumption, not how to say the fact in the second person. That resolved the open question — entry 2's project-facing form is a click in the web UI — so BINDING §4 stands unamended. The rewrite of `local-markdown.md` 3 surfaced a limit that was invisible while it read "Identity is chosen locally": any team on feature branches collides on the next id. Soft edge to T-004, which owns merge-conflict behaviour. Both sections re-measured against T-040's budget: 85 and 56 words, ~20s and ~13s of 30. |
| 2026-08-07 | → planned | Five steps. `specify` was at `proposed` — criteria written when T-040 raised this and never separately agreed; the instruction to plan is taken as that agreement, as for T-042 and T-044. Step 1 is widened from §1's three entries to all twelve, because §1's list came from a spot check and T-044 had just found a table assembled the same way to be wrong. Step 2 names the method rather than leaving it to taste: find what the adopter can *do* that breaks the assumption, since a backend fact rewritten in the second person is the same defect with a pronoun. |
| 2026-08-07 | → proposed | Found by T-040's last plan step, which deliberately looked past that task's own question at whether the entries could be answered at all. Kept out of T-040 by its scope, which put the content of the assumptions with their bindings — and the separation is worth keeping, since T-040 fixed how the section is measured and this fixes what it says. |
