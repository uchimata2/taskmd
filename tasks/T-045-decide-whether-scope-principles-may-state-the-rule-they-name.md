---
id: T-045
title: Decide whether SCOPE §2 principles may state the rule they name
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-017, T-027]
work_package: M1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - docs/SCOPE.md
---

# T-045 — Decide whether SCOPE §2 principles may state the rule they name

## 1. Specify

**Outcome**
A decided, written answer to whether `docs/SCOPE.md` §2 *Principles* may state a method rule in full,
or must name it and point at `docs/METHOD.md` — applied to principle 1's closing qualification, which
is where the question was found.

**Why this one**
Raised by [T-027](T-027-give-the-design-rule-one-home.md), whose criterion 1 asked for the
qualification to survive in exactly one file and could not be met. After T-027 removed `CLAUDE.md`'s
copy, three remain:

| Hit | Role |
| :--- | :--- |
| `docs/METHOD.md` §4 | the one home, decided by the maintainer |
| `docs/method/rationale.md` | explains *why* the rule is phrased that way — a different job |
| `docs/SCOPE.md` §2, principle 1 | states the qualification in full, near-verbatim |

**The sanction that was invoked for the third does not reach it.** T-027's scope put the
SCOPE↔METHOD overlap out as "settled in T-017". But
[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) settled §3
**requirements** against the method — its three rows are R-6, R-7 and R-8 — and the rule it produced
is written into §3: *a requirement says what must be true, never what to do.* §2 **Principles** was
never in T-017's scope and is a different register: §2 says it holds "three rules", not three
properties, and a rule is exactly the thing §3's test excludes.

**§2's own header already claims what is at issue.** It reads *"Three rules that every requirement
below is an application of. They are listed once, here."* `docs/METHOD.md` §4 makes the second
sentence false, and it has been false since METHOD was written.

**Requirements served**
R-1 (`docs/SCOPE.md`); §2 principle 3, *point, don't restate*.

**Scope**
- In: whether §2 principles may state a rule in full; the general answer, and principle 1 as the case
  that raised it.
- In: principle 2, which is the design rule itself under another heading and stands or falls with the
  same answer.
- Out: §3's requirement-versus-rule division. T-017 decided it, T-027 re-checked it, and it is not in
  question here.
- Out: `docs/method/rationale.md`, whose hit is an explanation rather than a statement.
- Out: any change to the rule itself.

**Inputs**
`docs/SCOPE.md` §2 and §3, `docs/METHOD.md` §4,
[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md),
[T-027](T-027-give-the-design-rule-one-home.md) §3 and §4.

**Acceptance criteria**
- [ ] A written rule for whether a §2 principle may state what it names, in whichever document owns
      that convention — and it is the same document that owns §3's rule, or the two are explicitly
      distinguished
- [ ] Principles 1 and 2 resolved consistently with it
- [ ] §2's "They are listed once, here" is either true afterwards or gone
- [ ] If the answer is "leave it", the reasoning is recorded where the next reviewer meets it — this
      is the second task to arrive at these three lines, so an unrecorded acquittal will bring a third

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: §2 keeps stating its principles, and only the
  qualification sentence moves.**

  The reasoning, which is not the one the question anticipated. §2 principle 1 governs the **whole
  product** — the schema, the generated index, the config, the code — whereas `docs/METHOD.md` §4
  governs the inverse of a link between tasks. It is therefore a genuinely broader claim rather than
  a copy, and reducing it to a pointer would leave §2 unable to justify the requirements it says are
  applications of it. What *is* duplicated is one sentence: the "compels versus permits"
  qualification, which is the operative half and therefore the half that drifts. So the boundary
  falls inside principle 1 rather than around it.

  §2's *"They are listed once, here"* goes either way — it is false today and would still be false
  under the other answer, because `docs/METHOD.md` §4 states principle 2 by name.

  *Rejected: reduce §2 principles to names plus pointers, mirroring what T-027 did to `CLAUDE.md`.*
  The symmetry is tempting and wrong — `CLAUDE.md` was restating a rule at the same scope, and §2 is
  not. A principle that cannot be read without following a link stops being usable as the thing §3's
  requirements are checked against.
  *Rejected: leave §2 whole and record the acquittal.* It is the answer T-017 gave one register down
  and it is why this recurred: the near-verbatim sentence survives, and the next reader of those
  three lines raises the same finding a third time.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Split principle 1 sentence by sentence into what is product-wide and what is about the inverse of a link, and put principle 2 through the same test. | A classified list — stays, or moves |
| 2 | Rewrite §2's header so its claim about itself is true, and so a reader can tell the §2 convention from the §3 one without conflating them. | The edited header |
| 3 | Rewrite principle 1: keep the product-wide statement, replace the link-specific sentences with a pointer that **names what it narrows to** — METHOD §4 states the qualification for links, not for facts in general, and a pointer that hid that would be lossy. | The edited principle |
| 4 | Re-run T-027's grep unchanged and account for every remaining hit by role. | Before and after counts, and a verdict per hit |
| 5 | Confirm R-2 still carries the permitted-second-write property, so that removing §2's sentence loses nothing T-017 sanctioned. | A stated verdict against R-2's text |

**Sequencing.** Step 1 leads because the decision names a boundary *inside* a paragraph and nothing
yet says where it falls; getting that wrong in either direction is the failure — too much moved and
§2 can no longer justify its requirements, too little and the near-verbatim sentence survives, which
is what brought this back twice. Step 5 is last and negative, like T-027's step 5: it proves the edit
did not quietly take something T-017 decided to keep.

**Shape of the deliverable — decided: §2 states its own convention, in §2.** This mirrors §3, which
states the convention governing §3 in its own opening paragraph, so a reader meets each rule where it
applies and the two are visibly different rules rather than one rule stated twice.
*Rejected: one convention section covering §2 and §3 together.* It would have to be written as the
generalisation of two rules that are not the same, and the merge would itself be the restatement
this task is about.
*Rejected: putting the convention in `CLAUDE.md`.* It is a rule about how `docs/SCOPE.md` is
written, `CLAUDE.md` is tier 1 under T-028, and T-027 has just finished taking content the other way.

**Output paths**
- `docs/SCOPE.md` — §2 *Principles*: the header and principle 1
- This task's §3 — the classification and the two grep runs

## 3. Implement

Run on 2026-08-07, using T-027's grep unchanged so the two tasks' before-and-after are comparable:

```bash
grep -rnIE --exclude-dir=.git --exclude-dir=tasks --exclude-dir=.handoff --exclude-dir=.pytest_cache 'compels?\W+(a|the) second write' .
```

**Step 1 — the boundary falls after the third sentence.** Principle 1 taken sentence by sentence:

| Sentence | Scope | Verdict |
| :--- | :--- | :--- |
| Every fact is written in exactly one place | whole product | stays |
| Anything derivable is computed at read time, never stored | whole product | stays |
| A feature that *requires* writing the same fact twice is the wrong feature — emphasis on "requires" | whole product | stays |
| Where the inverse is derived, one write is sufficient … a two-way reference living at both ends (R-2) | the inverse of a link | moves — METHOD §4 and R-2 both hold it already |
| This rule forbids designs that **compel** a second write, not users who make one | the inverse of a link | moves — the near-verbatim sentence |

**Principle 2 was put through the same test and stays.** Only its *name* is shared with METHOD §4's
subsection heading; its body is the prior-art evidence — GitHub's `--blocked-by` / `--blocking`,
Notion's `Parent item` — which exists nowhere else in the repository and is what makes the principle
a claim about trackers rather than a preference. A shared heading over different content is not a
restatement.

**Steps 2 and 3 — the header now says something true, and the pointer names its own narrowing.**
§2 states why it holds its principles in full (they govern the product, not just the tracking of
work), and points at `docs/METHOD.md` for the narrower version where one exists. Principle 1 keeps
its three product-wide sentences and replaces the other two with a pointer that says *what case*
METHOD §4 covers — the inverse of a link — rather than implying METHOD states the qualification for
facts in general, which it does not.

**Step 4 — three hits before, two after.** `docs/SCOPE.md` has dropped out. What remains:

| Hit | Role |
| :--- | :--- |
| `docs/METHOD.md:113` | the one home |
| `docs/method/rationale.md:16` | explains why the rule is phrased this way — it cannot make that argument without naming the phrasing |

`grep 'listed once, here'` now returns nothing.

**Step 5 — nothing T-017 sanctioned was lost.** R-2 still reads *"Storing it on one task is
sufficient; storing it on both is permitted and collapses to a single entry"*, so the property a
requirement is supposed to state is still stated, in the register T-017 settled. The sentence removed
from §2 was the *rule*, which is the half that was never §2's to hold twice.

**Decisions & assumptions**
- **The pointer names the case it narrows to, rather than reading as a general redirect.** — METHOD
  §4 qualifies the rule for link inverses; principle 1 is about any fact. "Stated once in METHOD §4"
  on its own would have been lossy in a way nobody would notice, since the only case that currently
  exercises the distinction *is* links. — 2026-08-07
- **The §2 header points at §3's convention instead of summarising it.** — The first draft read "a
  requirement states a property and never the rule (§3)", which is §3's rule compressed into §2 — this
  task's own defect, re-created inside its fix, and caught before review. — 2026-08-07

**Outputs produced**
- [`docs/SCOPE.md`](../docs/SCOPE.md) — §2 *Principles*: the header, and principle 1

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A written rule for whether a §2 principle may state what it names, in whichever document owns that convention — and it is the same document that owns §3's rule, or the two are explicitly distinguished | met | Both conventions live in `docs/SCOPE.md`, each stated in the section it governs, which is the same arrangement §3 already had. Distinguished explicitly and by pointer: §2's header says it is *not* the convention in §3 and sends the reader there rather than paraphrasing it. |
| Principles 1 and 2 resolved consistently with it | met | Principle 1 keeps three product-wide sentences and loses two that were about link inverses. Principle 2 was tested rather than assumed and stays: the shared item is its heading, and its body is prior-art evidence held nowhere else. |
| §2's "They are listed once, here" is either true afterwards or gone | met | Gone; `grep 'listed once, here'` returns nothing. Replaced by a claim the tree supports — that the principles govern the whole product, which is *why* they are stated rather than pointed at. |
| If the answer is "leave it", the reasoning is recorded where the next reviewer meets it | met | Vacuous as written — the answer was not "leave it" — but what it was protecting against is served anyway: the decision and its link to this task are in §2 itself, so the next reader of those three lines meets the answer before raising the finding a third time. |

Four met, none carried. **T-027's criterion 1 is now two hits rather than one, and that is the
correct end state**: the residue is `rationale.md`, whose job is explaining why the rule is worded as
it is, and which both tasks put out of scope deliberately rather than by omission. An explanation
that may not name what it explains would be the rule applied past the point where it helps.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Four criteria met, none carried, on the same day it was raised. The maintainer answered and the answer moved the boundary rather than choosing between the two readings the question offered: §2 keeps stating its principles because they govern the **whole product** where METHOD §4 governs the inverse of a link between tasks — a broader claim, not a copy — and only the "compels versus permits" sentence moves, being the operative half and therefore the half that drifts. Both alternatives recorded as rejected, including the symmetrical one: doing to §2 what T-027 did to `CLAUDE.md` would have left a principle that cannot be read without following a link, and §3's requirements are checked against it. Boundary established sentence by sentence rather than by paragraph, three of principle 1's five sentences staying; principle 2 tested against the same rule and kept, because only its heading is shared and its body is the GitHub/Notion prior art held nowhere else. The grep is down from three hits to two and `listed once, here` is gone. One thing caught inside the fix: the first draft of the new header summarised §3's rule into §2, which is this task's own defect re-created — replaced by a pointer before review. |
| 2026-08-07 | → proposed | Raised by T-027's review, which could not meet its criterion 1 because two of the three surviving copies are protected by that task's own scope. Not fixed there (METHOD §5). The finding is narrow and checkable: T-017's settlement is written into §3 and is about requirements, so §2's principles are unsettled rather than sanctioned — and §2's own "listed once, here" has been false since `docs/METHOD.md` §4 was written. |
