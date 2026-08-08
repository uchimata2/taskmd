---
id: T-053
title: Decide the plugin's boundary, and what its skill may point at
type: decision
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-050, T-006, T-003, T-052]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-08
updated: 2026-08-08
deliverables: []
---

# T-053 — Decide the plugin's boundary, and what its skill may point at

## 1. Specify

**Outcome**
It is written down what the installed plugin contains and what `skills/taskmd/SKILL.md` is allowed to
reference, such that a pointer in the skill has exactly **one** resolution for a session that follows
it — whichever tree that session is working in.

**Why this one**
Found in [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 7, by reading the
base directory the harness reported when it served the skill. It is on the far side of a claim this
project has already made carefully, so it is worth stating plainly what was seen:

The harness serves the skill from an **install-time snapshot** under `~/.claude/plugins/cache/`, keyed
by marketplace, plugin and version. That snapshot is a copy of the **whole repository** — `docs/`,
`taskmd/`, `tasks/` (all 52 of this project's task files), `tests/`, `reference/`, `.handoff/`,
`.pytest_cache/`, and the gitignored `control/`. The skill's own pointers are relative and reach
*outside* its folder — `../../docs/METHOD.md`, `../../taskmd/defaults/config.md` — so each of them
names a real file in the snapshot **and** a real file in the working tree.

Those two are not the same file. Hashed against each other on the day of the install,
`docs/METHOD.md`, `docs/method/implement.md` and `SKILL.md` matched, and **`CLAUDE.md` did not** —
drift inside a few hours, from one ordinary commit. Nothing decides which copy a session reads except
where it happens to be working. That is a second home for every fact the skill points at, which is
[`../docs/METHOD.md`](../docs/METHOD.md) §4 read in the direction the project usually reads it: the
duplication was not written by anyone, it was created by installing.

**Two consequences, and they pull in different directions.** For *this* repository, the snapshot is a
stale mirror that a session may silently prefer. For an *adopter*, it is worse and more concrete: an
install ships them this project's 52 tasks, its handoff archive and its local-context file, none of
which is theirs, and `docs/METHOD.md` is genuinely something they need. So the answer is not simply
"ship less".

**Requirements served**
R-21 (`docs/SCOPE.md`) and §1 *Invisibility* — the tier model is a claim about what a session is
handed, and it is not settled while a pointer has two ends. R-23 and `CLAUDE.md` *Publishing
constraints* for the half about what an adopter receives.

**Scope**
- In: what the packaged plugin contains — which paths are part of it and which are this repository's
  own working material that happens to sit alongside.
- In: whether `SKILL.md` may reference paths outside its own folder at all, and if so how those are
  written so they resolve once.
- In: the drift itself — whether a served snapshot going stale against the tree is accepted, detected
  or prevented.
- In: `control/` reaching an install. It is gitignored, so no push sends it; the install copies from
  the working directory, which is a different route and the pre-publish check cannot see it.
- Out: how the plugin is installed, and the install instructions —
  [T-006](T-006-package-document-and-publish.md), which already owes an install line.
- Out: `.gitignore` and what a **clone** receives under `.claude/` —
  [T-052](T-052-decide-what-of-claude-a-published-clone-carries.md). Related, and deliberately not
  merged: that one is about a push, this one about an install, and the two mechanisms read different
  files.
- Out: the content of the method documents and the skill. Nothing here says any of them is wrong.

**Inputs**
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 7, which holds the
observation and the hash comparison; `skills/taskmd/SKILL.md`, for the pointers;
`.claude-plugin/`, for what the packaging currently declares;
[`../docs/BINDING.md`](../docs/BINDING.md) §4 is not involved — this is not a binding question.

**Acceptance criteria**
- [ ] The set of paths the plugin ships is stated somewhere a reader meets it, and is derived from a
      rule rather than enumerated file by file
- [ ] A pointer followed from a served `SKILL.md` resolves to one file — demonstrated by making the
      tree and the install disagree on a file the skill points at, and showing which one a session
      gets and why
- [ ] An adopter's install does not contain this project's task files, handoff archive or `control/`
      — demonstrated by listing the installed snapshot
- [ ] The pre-publish check still prints nothing, and still prints exactly the five fixture lines
      without its exclusion

**Open questions**
- ~~Does the skill stop pointing outside its folder, or does the plugin keep shipping what it points
  at?~~ **Answered by the maintainer on 2026-08-08: the plugin keeps shipping what it points at,
  minus this repository's working material.** So `skills/`, `docs/`, `taskmd/` and the launchers are
  the plugin; `tasks/`, `.handoff/`, `tests/`, `reference/` and `control/` are not. The pointers in
  `SKILL.md` stay relative and keep resolving, and `docs/METHOD.md` keeps its single authored home.
  *Rejected: making the skill self-contained* by moving the method under `skills/taskmd/` — it buys
  one guaranteed resolution by giving the method a second home or a new one, which is the rule this
  plugin exists to enforce, and it would leave `docs/` a pointer to its own contents. *Rejected:
  shipping the whole tree* — cheapest to package and it is what an adopter gets today: this project's
  53 task files, its handoff archive, and `control/` by a route no push-oriented check can see.
- **Is a stale install acceptable if it is *versioned*?** A snapshot pinned to `0.1.0` is arguably
  correct behaviour rather than drift — the tree is `0.1.0`+work, and an adopter wants the released
  method, not the in-flight one. If that reading is taken, the defect is only that *this* repository
  reads its own installed copy, and the fix is much smaller. **Deferred to `plan` by the maintainer
  on 2026-08-08**, to be settled after checking what the harness actually supports for a
  local-directory install — the two readings differ in cost only once that is known.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <not yet decided — depends on the open questions>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | → specified | Maintainer answered the boundary question: **ship what the skill points at, minus this repository's working material** — `skills/`, `docs/`, `taskmd/` and the launchers in; `tasks/`, `.handoff/`, `tests/`, `reference/`, `control/` out. That keeps `docs/METHOD.md` with one authored home and the relative pointers resolving, which is why the self-contained alternative was rejected — it would have bought a guaranteed single resolution by giving the method a second home, trading the plugin's own design rule for the symptom. The drift question is **deferred to `plan`**: whether a versioned snapshot going stale is a defect at all depends on what the harness supports for a local-directory install, which is a thing to check rather than to reason about. Criterion 2 is the one that now needs care — it asks for a demonstration that a pointer resolves once, and under this answer the honest demonstration is about which copy a session in *this* repository reads, since an adopter has only one. |
| 2026-08-08 | → proposed | Raised from T-050 §3 step 7 and not fixed there (METHOD §3.3): T-050 measures what a session is handed, and it now has the answer; what the plugin should ship is a packaging decision. The harness serves the skill from an install-time snapshot of the **whole repository**, so every relative pointer in `SKILL.md` has two resolutions, and `CLAUDE.md` already differed between them within hours of the install — duplication nobody wrote, created by installing. `high` because it lands on the tier model R-21 names and on what an adopter receives, and because the two halves pull opposite ways: shipping less breaks the pointers, shipping everything hands an adopter this project's 52 tasks and its gitignored local-context file. `s` because the work is a decision and a packaging rule, not code. Held as `decision` rather than `fix` — nothing is known to be broken for an adopter yet, since nobody has installed it but the maintainer. |
