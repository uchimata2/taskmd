---
id: T-252
title: Correct the README's file count for the copied skill, and decide whether a number belongs there
type: fix
status: proposed
phase: specify
parent: T-241
blocked_by: []
related: [T-083, T-085]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
deliverables: []
---

# T-252 — Correct the README's file count for the copied skill, and decide whether a number belongs there

## 1. Specify

**Outcome**
An adopter following [`README.md`](../README.md) *As a plain skill* can check their copy is complete
against a number that is true of the release they copied — or against no number at all, if the
project decides a hand-kept count is not worth keeping.

**Where this came from**
Finding 1 of [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md),
the audit of the published `0.6.0`. Measured against a fresh clone of the tag `v0.6.0` (`cb0702c`),
2026-08-23:

```text
README claims                                21 files
git ls-files plugin/skills/taskmd/ | wc -l   25
```

**It was right when it was written**, which is the part that decides what this task is about.
[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) followed the
section on a second operating system for `0.5.0` and recorded that *"the file count matches the
number the README claims"*, calling it a claim nobody had checked from outside. The folder then grew
past it. Nothing reported the drift, because nothing reads it: `check` validates references and
links, not prose arithmetic.

**A second number is in play and must not be confused with it.** A filesystem count of that folder
returns **31** once the tool has been run, because `taskmd/__pycache__/` appears and is gitignored.
T-085 predicted that figure and this audit reproduced it by accident. So a reader checking by `ls`
gets 31, a reader checking by `git ls-files` gets 25, and the README says 21 — three numbers, and the
README does not say which kind it means.

**Scope**
- In: `README.md`'s *As a plain skill* section, and any other place a count of that folder is stated
- In: deciding **whether** a number belongs there at all, since a hand-kept count of a growing folder
  is the thing that just drifted
- Out: changing what the folder contains
- Out: the `__pycache__` behaviour itself, which is Python's and is correct

**Inputs**
- [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) §3 —
  the measurement, the three numbers and how each was taken
- [T-083](T-083-make-the-skill-directory-self-contained.md) — why the folder is self-contained, which
  is the claim the count exists to support
- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) — the count
  verified from outside at `0.5.0`, and its note that a filesystem count says 31 and is wrong

**Acceptance criteria**
- [ ] The section states something true of the published artifact, checked against a clone of the
      tag rather than against the working tree
- [ ] If a number stays, it says which count it is — what a copy receives, not what `ls` shows after
      the tool has run once — and the decision records why a hand-kept number was kept over dropping
      it or deriving it
- [ ] If a number goes, the section still gives an adopter a way to tell their copy is complete
- [ ] Whatever is written cannot drift silently again, or the record says plainly that it can and
      that this is accepted

**Open questions**
- **Does a count belong in the README at all?** — the project owner. **Recommendation: replace it
  with a check the adopter can run**, because the value of the number is *"my copy is complete"* and
  a number cannot answer that — it can only fail to. *Against:* a count is readable at a glance and
  needs no tooling, and the section is written for someone who has not installed anything yet.
  A middle option is to keep a number and say which count it is, accepting that it drifts and saying
  so.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised as finding 1 of [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md)**, the audit of the published `0.6.0`, 2026-08-23. Raised rather than fixed because [`audit`](../plugin/skills/taskmd/docs/method/audit.md)'s no-inline-fix rule applies and the repair is one word — which that document names as the case where the rule is most often waived. **`parent: T-241`**, so the umbrella stays open until this closes, per METHOD §4. **The owner's grant of 2026-08-23 reaches this record**, in its words *"including anything raised during the work of these tasks"* — it covers this record's `specify` through `review`, committing and pushing. |
