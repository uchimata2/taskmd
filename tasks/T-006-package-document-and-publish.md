---
id: T-006
title: Package, document and publish
type: deliverable
status: planned
phase: plan
parent: null
blocked_by: [T-002, T-003, T-008, T-009, T-010, T-011, T-018]
related: [T-004]
work_package: none
owner: maintainer
business_value: critical
effort: l
created: 2026-08-04
updated: 2026-08-09
deliverables: []
---

# T-006 — Package, document and publish

## 1. Specify

**Outcome**
An installable plugin with a README that only claims what has been demonstrated.

**Why this one**
A README written before the thing works becomes the unverified claim the whole project warns about. Written last, on purpose.

**Requirements served**
R-15, R-20, R-23 (`docs/SCOPE.md`). This task closes the definition of done, `SCOPE.md` §9.

**Acceptance criteria**
- [ ] Install instructions end with a command that proves it runs
- [ ] The measured `context` saving reproduced on a sample project and quoted
- [ ] No personal, client or machine data anywhere in the repository
- [ ] Installs from a clean clone on a machine that has never seen it
- [ ] The package ships the method document and **both** bindings, and the README states that
      changing backend changes the binding, not the method (R-13, R-14)
- [ ] The README claims a supported scale that T-004 measured, and nothing it did not
- [ ] Every non-goal in `SCOPE.md` §4 still holds at publish — checked, not assumed
- [ ] **Both** distribution shapes install from a clean clone and are each proven by a command that
      runs — the marketplace plugin and the plain skill package
      <br>*Added 2026-08-07 with the answer to the distribution question. The seven above predate it and
      are unchanged.*

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: both, with the marketplace plugin primary.**
  The tree is already a plugin and the marketplace is how it is found; the plain skill package is a
  subset of the same tree and is what someone not using the marketplace needs. *Rejected: the plugin
  alone.* Two shapes are two sets of install instructions and paths to keep true — which is the cost
  this answer accepts, and which the criterion added with it exists to hold.

**Why the new blockers**
`blocked_by` gained T-008, T-009, T-010 and T-011. The definition of done requires the method
document, both bindings implementing the same lifecycle, and a clone that runs with nothing
installed — publishing before those exist would ship a product that fails its own stated scope.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the **plain skill package** and run a command the skill names from it. The marketplace shape is proven (T-067); this one has never existed, and `bin/` reaching `PATH` is a plugin mechanism (T-054), not a skill one. | The list of files the shape consists of, and the transcript of the command running from it — or, if the entry point does not resolve by that route, the statement of what it offers instead |
| 2 | Reproduce the `context` saving: the bytes a session reads to start one task without the tool, against the bytes `context <id>` returns, on this repository. | Both byte counts, the id they were taken on, and the commands that produced them, in §3 |
| 3 | Check each of `SCOPE.md` §4's eleven non-goals against the tree as it stands. | An eleven-row verdict table in §3, each row naming what was looked at rather than asserting the non-goal |
| 4 | Settle what the README says about scale and about platforms — T-004 has measured no ceiling, and T-020's amended outcome states macOS untested rather than claimed. | The two sentences as they will appear in the README, with what was rejected, in §3 |
| 5 | Write the README from steps 1–4: what the tool is, both shapes' install instructions each ending in a command that proves it runs, and the backend sentence criterion 5 asks for. | `README.md` |
| 6 | Run the pre-publish check both ways, after this record and the README are written and before anything is pushed. | The silent run with the exclusion, and the five-line run without it |
| 7 | Publish to a public remote. The maintainer's action: it is outward-facing and not undoable, and the token this project has already failed twice to delete a repository with (T-037, T-077). | The public repository |
| 8 | Install **both** shapes from a clean clone of what was published, run each shape's proving command, and list what the install carries. | Two transcripts, and the installed file list — which is also how criterion 5's "ships the method document and both bindings" is read rather than assumed |

**Step 1 is first because it can invalidate the rest.** Criterion 8 asks both shapes to be proven by
a command that runs, and the second shape is a name in an answer rather than anything that exists.
If a skill-only install cannot put `taskmd` on `PATH`, then steps 5 and 8 are writing and proving a
different document than they would otherwise be — so the horizon this plan can honestly see ends at
step 1, and steps 5 and 8 are named at the level their inputs support.

**Steps 2–4 come before step 5 on purpose.** Each produces a number or a sentence the README then
quotes. Writing the README first and measuring afterwards is exactly how a document ends up carrying
a figure nobody took, which is the failure this task was scheduled last to avoid.

**Decisions — the shape of the deliverable**

- **One README, at the repository root.** It is the front door for both shapes and for anyone
  browsing the repository, and nothing inside `plugin/` cites it, so T-064's constraint is untouched.
  *Rejected: a second README inside `plugin/`* — a second copy of the install instructions, shipped
  into every install cache, read by nobody who has not already installed it. *Rejected: one README
  per shape* — two homes for one fact, when the shapes differ in about a dozen lines.
- **The README points at the method; it carries none of it.** Criterion 5's sentence — changing
  backend changes the binding, not the method — is a claim about the *package*, so it belongs there;
  `plugin/docs/METHOD.md` and `plugin/docs/bindings/` stay the only homes for the thing itself.
- **This repository is the sample project of step 2.** It is the only real taskmd project that
  exists, and its tasks are real work. *Rejected: a project built for the measurement*, which would
  produce a ratio chosen rather than found. *Rejected: quoting `reference/`'s 37,909 → 992*, which is
  the prior art's number and is already in `docs/BRIEF.md`; criterion 2 asks for it reproduced.
- **Nothing this task writes is added to `CLAUDE.md`.** Tier 1 is over its bound already
  ([T-063](T-063-measure-the-tier-1-member-the-rule-declares.md)), and every character there is paid
  on every turn of every session; a README is read once. Whatever `CLAUDE.md` owes at close is a
  pointer, not a summary.

**Not in this plan, deliberately:** the remote's identity, which is `control/LOCAL-CONTEXT.md`'s;
and reconciling `CLAUDE.md`'s status paragraph and `docs/SCOPE.md` §9, which is closing work rather
than a step that produces the outcome.

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
| 2026-08-09 | → planned | Eight steps. The plain skill package leads because it is the one shape that has never existed — the marketplace route was installed and listed by T-067, while `bin/` reaching `PATH` is a plugin mechanism T-054 proved for plugins, so a skill-only install may not be able to end its instructions in the command criterion 1 asks for. The plan says so rather than inventing steps 5 and 8 in detail against an unknown. Four shape decisions, each with its rejection: one root README; the README points at the method and carries none of it; this repository is the sample project the `context` saving is re-measured on, because a project built for the measurement chooses its own ratio; and nothing lands in `CLAUDE.md`, which is over its tier-1 bound already. **One thing is raised rather than absorbed**: criterion 6 asks the README to claim a scale that T-004 measured, and T-004 has measured nothing, so on the plan as written that criterion is met by claiming no ceiling at all — vacuously. Whether publication waits for T-004 is a dependency edge, and the maintainer's to add. |
| 2026-08-07 | → specified | Answered: both shapes, plugin primary. One acceptance criterion added with the answer — both shapes install from a clean clone and are proven by a command — because shipping two distributions and testing one is how the second becomes stale, and the criteria named no shape at all. The seven that predate this are unchanged. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
| 2026-08-05 | (no change) | `blocked_by` gained T-018: a tracked file carries a real absolute local path, which R-23 and §9 put inside this task's definition of done. |
