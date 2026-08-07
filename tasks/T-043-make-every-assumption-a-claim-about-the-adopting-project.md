---
id: T-043
title: Make every assumption a claim about the adopting project
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-009, T-010, T-040]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables: []
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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → proposed | Found by T-040's last plan step, which deliberately looked past that task's own question at whether the entries could be answered at all. Kept out of T-040 by its scope, which put the content of the assumptions with their bindings — and the separation is worth keeping, since T-040 fixed how the section is measured and this fixes what it says. |
