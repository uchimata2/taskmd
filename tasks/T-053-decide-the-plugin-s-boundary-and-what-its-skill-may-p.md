---
id: T-053
title: Decide the plugin's boundary, and what its skill may point at
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-050, T-006, T-003, T-052, T-054]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-08
updated: 2026-08-08
deliverables: [plugin/skills/taskmd/SKILL.md, .claude-plugin/marketplace.json]
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
[`../plugin/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4 read in the direction the project usually reads it: the
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
[`../plugin/docs/BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 is not involved — this is not a binding question.

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
| 1 | Establish what the harness actually supports for excluding files at install, read out of the shipped binary rather than assumed — this is the deferred open question and it determines whether the rest of the plan is the right plan at all | **D1**, below |
| 2 | Put the consequence to the maintainer: the answer chosen in `specify` has a cost nobody had priced, and paying it is not this task's to decide | **D2**, below — *this plan stops here* |
| 3 | *(shape depends on step 2)* Either restructure so the plugin is a subtree, or record the whole-tree copy as accepted and state the rule that governs it | `.claude-plugin/marketplace.json`, and whatever step 2 chooses |
| 4 | Demonstrate the criteria against the result: which copy a session gets and why, and what an install contains | §3, and the §4 table |

Step 1 is first because it could invalidate everything after it, which is
[`../plugin/docs/method/plan.md`](../plugin/skills/taskmd/docs/method/plan.md)'s *reduces uncertainty soonest* rule. It did.

**Shape decisions.**

**D1 — There is no exclusion mechanism. The only lever is what is in the source.** Read out of the
shipped binary, not inferred from the cache's contents:

- A **local directory** source is copied whole. The install function checks the path exists, calls
  `copyDir`, and then removes exactly one thing afterwards: `.git`. There is no ignore file, no
  manifest field, and `.gitignore` is not consulted — which is why `control/` and `.pytest_cache/`
  are in the cache and why the tracked/untracked distinction that governs a push has no bearing here.
- `copyDir` itself filters nothing. Its only skip is the destination directory when the destination
  is nested inside the source, which exists to stop it recursing into its own output.
- The marketplace entry's component fields — `commands`, `agents`, `skills`, `hooks`, `outputStyles`,
  `themes`, `mcpServers`, `lspServers`, `experimental` — looked like the mechanism and **are not**.
  They are consumed only on the `archive` source, and there they are *validated*, not applied: the
  code checks the declared paths **exist** in the archive and errors if they do not, then moves the
  whole thing. So declaring `skills` narrows nothing.
- `${CLAUDE_PLUGIN_ROOT}` exists but substitutes into hook and command arguments. It is not available
  to a Markdown link inside `SKILL.md`, so it cannot make a pointer resolve to one file.

**This settles the deferred open question, and settles it as "not a defect, and not fixable either".**
A local-directory install is a snapshot by construction — there is no dev-mode or linked install to
choose instead. The one arrangement that serves a skill without a snapshot is a project-level
`.claude/skills/`, which [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) **D2**
and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 5 both refused, for
creating a second home for the skill. So drift between the cache and the tree is a property of
installing, not a bug to remove.

**D2 — The chosen answer costs a repository restructure, and that is the maintainer's call, so this
plan stops at step 2 rather than starting step 3.** `specify` chose *ship what the skill points at,
minus this repository's working material*. Given D1, the only way to deliver it is to make the
plugin a **subtree** — a directory holding `skills/`, `docs/`, `taskmd/` and the launchers and
nothing else — and point `marketplace.json`'s `source` at that instead of `./`. That is not a
packaging tweak: it moves `docs/` and `taskmd/` and rewrites every path that names them, in a
repository whose documents cite each other constantly. *Rejected: doing it anyway* — METHOD §3.3
forbids quietly widening the outcome, and "fix it" was asked before this cost was known to anyone,
including the person who asked. *Rejected: silently downgrading to accept the whole-tree copy* — that
reverses a decision the maintainer took two turns ago, on evidence they have not seen.

**D3 — Two things §1 got wrong, corrected here rather than left standing.** Both were written before
step 1 read the install paths, and both overstate the problem:

- **`control/` does not reach an adopter.** §1 says an install ships "its local-context file", and
  that is true only of a **local directory** source — the maintainer's own install. The `github`
  source runs `git clone --depth 1`, and `git-subdir` runs a filtered clone plus a sparse checkout,
  so both deliver **tracked files only**. A gitignored path cannot reach an adopter by that route.
  What an adopter actually receives that they have no use for is `tasks/`, `tests/`, `reference/` and
  `.handoff/config.md` — noise, not exposure.
- **Criterion 2 is already met for an adopter, and cannot be met here.** An adopter's working tree is
  their own project, which has no `docs/METHOD.md`, so the skill's pointer resolves in exactly one
  place: the cache. The two-resolutions problem is an artefact of **self-hosting** — this repository's
  tree holds the same files its cache does — and no restructure removes it, because a subtree's
  contents are still copied into the cache. So the criterion needs rewording at `review` under
  [`../plugin/docs/method/review.md`](../plugin/skills/taskmd/docs/method/review.md) *Changing a criterion*, with the original
  recorded; it is not satisfiable as written by any option.

**D4 — `git-subdir` is what makes a subtree pay off, and it exists.** A marketplace entry may declare
a `git-subdir` source: the harness clones with `--filter=tree:0 --no-checkout` and then
`sparse-checkout set --cone -- <path>`, materialising **only** that directory. So one subtree serves
both installs — `./<subtree>` for the maintainer's local install and `git-subdir` at the same path
for everyone else — instead of the two divergent mechanisms a build-an-archive approach needs.

**Measured cost of the subtree, so the choice is not made on a feeling.** Moving `docs/` and
`taskmd/` under a plugin directory touches: **~70 Markdown links** in `tasks/` (59 to `../docs/`, ~10
to `../plugin/taskmd/`) which `check` validates and would report broken, **~98 references** in live
documents outside `tasks/`, and **4 Python imports**. Separately, ~646 backticked *prose* mentions of
`docs/…` and `taskmd/…` sit inside closed task records; those break nothing and are historical
statements about where a file was, so they are not rewritten — consistent with this project's rule
against editing closed evidence.

**Planned outputs**
- `.claude-plugin/marketplace.json` — the `source`, if step 2 goes that way.
- A stated packaging rule, in whichever document step 2 settles on.

## 3. Implement

**Authorized as one pass.** `plan`, `implement`, `review` and the fix were asked for together, and
the restructure was authorized after D2's cost was put to the maintainer and priced. Recorded here
rather than inferred, per METHOD §3.1.

### Step 3 — the subtree

`plugin/` now holds the whole of what ships, and nothing else moved into it:

| In `plugin/` | Left at the repository root |
| :--- | :--- |
| `skills/taskmd/`, `taskmd/` (the package), `taskmd.sh`, `taskmd.ps1`, `.claude-plugin/plugin.json` | `tasks/`, `tests/`, `reference/`, `.handoff/`, `control/`, `CLAUDE.md` |
| `docs/METHOD.md`, `docs/BINDING.md`, `docs/method/`, `docs/bindings/` — the method, which is what the skill points at | `docs/SCOPE.md`, `docs/BRIEF.md` — this project's own requirements and evidence, which an adopter has no use for |

`.claude-plugin/marketplace.json` stays at the repository root, because it is the *marketplace*
manifest rather than the plugin's; its `source` is now `./plugin`.

**Two things fell out that were not designed and are worth recording.** `SKILL.md`'s pointers needed
**no edit at all** — `../../docs/METHOD.md` from `plugin/skills/taskmd/` resolves to
`plugin/docs/METHOD.md` in the tree and to `docs/METHOD.md` in an install, which is the same file
either way. And the launchers already did the right thing: each sets `PYTHONPATH` to *its own
folder*, so moving them into the subtree moved the package path with them, unedited.

### Step 4 — verification

**What an install now receives**, listed from what a git-sourced install would clone:

```text
.claude-plugin/plugin.json   docs/BINDING.md   docs/METHOD.md
docs/bindings/{github-issues,local-markdown}.md
docs/method/{audit,implement,plan,rationale,review,specify,where-facts-live}.md
skills/taskmd/{SKILL.md,adopt.md}   taskmd.ps1   taskmd.sh
taskmd/{__init__,__main__,cli,discovery,schema}.py   taskmd/defaults/config.md
```

Twenty-two files, and a grep for `tasks/`, `.handoff/`, `control/`, `tests/` or `reference/` under
`plugin/` returns nothing.

**The tool, run on itself, through the launcher an adopter would use:**

```text
Wrote tasks/README.md - 21 active, 32 closed
OK - 53 task(s), vocabulary valid, references resolve, no broken links
114 passed in 1.05s
```

**`check` did the work the restructure needed, and it is the evidence for D1's claim that this was
verifiable.** It failed four times on the way, each time naming the class and the file: 26
`MISSING OUTPUT` lines from `deliverables:` front-matter still declaring pre-move paths — **a
category the plan had not counted at all** — then `BROKEN LINK` runs across archived handoffs, then
across `docs/SCOPE.md` and `docs/BRIEF.md`, then the single one that mattered.

**That last one is a finding, not a chore.** `plugin/skills/taskmd/adopt.md` pointed at
`../../docs/SCOPE.md` — this project's requirements document, which is **not** part of the plugin and
which an adopter will never have. Before the restructure that link resolved, so nothing could
distinguish "a pointer inside the plugin" from "a pointer into the project that happens to sit
alongside". Making the boundary structural is what made the escape visible, on the first run. The
sentence was rewritten to state the measurement instead of citing R-21, and a sweep for any remaining
pointer out of `plugin/` returns none.

**Decisions & assumptions**

- **The subtree is `plugin/`, and `docs/` splits rather than moving whole.** — `METHOD.md`,
  `BINDING.md`, `method/` and `bindings/` are what the skill points at and what an adopter needs;
  `SCOPE.md` and `BRIEF.md` are about *building* taskmd. Two `docs/` folders is the honest shape:
  one is the shipped method, the other this project's own papers. *Rejected: moving `docs/` whole* —
  it would ship an adopter the requirements list for a tool they are merely using. — 2026-08-08
- **~646 backticked prose mentions of the old paths inside closed task records are left alone.** —
  They break nothing, `check` does not read them, and they are statements about where a file was at
  the time. Rewriting them would edit closed evidence at scale, which this project refuses for a
  reason. Only *links* were rewritten, and `check` proves every one resolves. — 2026-08-08
- **Archived handoffs under `.handoff/processed_*` had their links rewritten.** — They are gitignored
  local working files rather than a record anyone audits, and `check` reads them, so leaving them
  broken would have left the validator permanently red. — 2026-08-08
- **The tests now separate `PKG` from `ROOT`, and one assertion was found resting on their being the
  same.** — `test_schema` resolved `schema.source` against the working directory and passed only
  because the package's parent *was* the repository root. `_display` is correct and unchanged: it
  returns a path relative to the plugin root, which is what keeps a machine's disk out of an error
  message. The test was fixed, not the code. — 2026-08-08

**Outputs produced**
- The `plugin/` subtree, and `.claude-plugin/marketplace.json` pointing at it.
- `CLAUDE.md`, `.handoff/config.md`, `docs/SCOPE.md`, `docs/BRIEF.md` — paths and the new way in.
- `plugin/skills/taskmd/adopt.md` — the escaping pointer removed.
- `tests/test_{cli,list,runtime,schema}.py` — `PKG` separated from `ROOT`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The set of paths the plugin ships is stated somewhere a reader meets it, and is derived from a rule rather than enumerated file by file | met | The rule is a **directory**: what is in `plugin/` ships, what is not does not. Nothing enumerates it, nothing can go stale, and a file added later is in or out by where it is put. Stated in `CLAUDE.md` *Status* and `.handoff/config.md`, both of which a reader meets before working here |
| A pointer followed from a served `SKILL.md` resolves to one file | **reworded, then met** — see below | Original text, kept: *"demonstrated by making the tree and the install disagree on a file the skill points at, and showing which one a session gets and why"* |
| An adopter's install does not contain this project's task files, handoff archive or `control/` | met | The 22 files listed in §3 step 4 are the whole of `plugin/`; a grep for `tasks/`, `.handoff/`, `control/`, `tests/` or `reference/` under it returns nothing. `control/` was never at risk by this route anyway — D3 |
| The pre-publish check still prints nothing, and still prints exactly the five fixture lines without its exclusion | met | Run after the restructure: nothing with the exclusion, five without. Suite 114/114, `check` clean on 53 tasks |

**The reworded criterion, under [`../plugin/docs/method/review.md`](../plugin/skills/taskmd/docs/method/review.md)
*Changing a criterion*.** It measured something no acceptable outcome could deliver, and D3 says why:
a pointer has two resolutions **only when the working tree is itself a copy of the plugin**, which is
true here and false for every adopter. No restructure removes it, because a subtree's contents are
still copied into the cache. So the original demanded a demonstration that could only ever fail.

> **Replacement:** *No pointer inside the plugin resolves outside it — demonstrated by sweeping
> `plugin/` for links that escape the subtree.*

**Met**, and it caught something on the first run: `adopt.md` pointed at `docs/SCOPE.md`, a project
document the plugin does not ship (§3 step 4). The sweep now returns none. This replacement measures
what the task can actually control — the plugin's own referential closure — rather than a property of
whoever happens to be reading it. **Agreed with the maintainer** as part of authorizing the
restructure, which is where the D3 correction was put to them.

**Child fix tasks raised**
- **[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)** — raised, not carried,
  and **not caused by this task**. Every command `SKILL.md` and `adopt.md` name fails for an adopter:
  the package is in the install cache and their working directory is their own project, so
  `python -m taskmd` finds no module. The hole predates the restructure and was hidden by this
  repository being the only place the plugin had ever run. `critical` — it is the adoption path not
  working at all, and [T-006](T-006-package-document-and-publish.md) would publish it as-is. The
  mechanism was found in the same read of the binary that produced D1: the harness puts
  `<plugin-root>/bin` on `PATH` for every enabled plugin.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | (no status change, task stays `done`) | **Confirmed against a real install, which §3 step 4 could not do** — that evidence was the file list a git-sourced clone would carry, because the reinstall needed an interactive terminal. Reinstalled by the maintainer at the restructured HEAD, the cache holds `docs/`, `skills/`, `taskmd/`, the two launchers and nothing else: `tasks/`, `tests/`, `reference/`, `control/`, `.handoff/` and `.git` are all absent, where before the restructure every one of them was present. **One correction to step 4's count, appended rather than edited in place**: the cache holds **30** files, not 22, because a *local-directory* install copies `taskmd/__pycache__/` — five `.pyc` files that `.gitignore` excludes from a push but which no ignore rule can keep out of a directory copy (§2 D1: the harness consults none). So step 4's list describes what the **git** route delivers, which is the route an adopter takes; the local-directory route additionally carries build artifacts of whoever ran the tool last. Recorded as a note at the maintainer's decision rather than raised as a task: no adopter receives them, they are inert, and the only mechanism that could exclude them does not exist. |
| 2026-08-08 | → done | Restructured, verified and reviewed in the authorized single pass. `plugin/` is now the whole of what ships — skills, the package, the launchers, and the method half of `docs/`; `SCOPE.md` and `BRIEF.md` stay at the root because they are about *building* taskmd. **Two things fell out unplanned and both were free**: `SKILL.md`'s pointers needed no edit, since `../../docs/METHOD.md` resolves correctly inside the subtree *and* inside an install; and the launchers already set `PYTHONPATH` to their own folder, so the package path moved with them. **`check` is the reason this was safe, and it failed four times on the way** — 26 `MISSING OUTPUT` lines from `deliverables:` front-matter, a category the plan never counted, then broken links in archived handoffs, then in `docs/`, then the one that mattered: `adopt.md` pointed at `docs/SCOPE.md`, a project document the plugin does not ship. Before the restructure that link resolved, so nothing could tell a plugin-internal pointer from an escape; making the boundary structural made it visible on the first run. Criterion 2 was **reworded** under *Changing a criterion* with the original kept — it demanded a demonstration no outcome could give, because two resolutions exist only when the working tree is itself a copy of the plugin, which is this repository and no adopter. The replacement measures referential closure instead, and it is what caught the escape. Left alone: ~646 backticked prose mentions of old paths inside closed records, which break nothing and would be a mass edit of closed evidence. Raised: T-054, `critical`, and not caused by this task — every command the skill names fails for an adopter, and the `bin`-on-`PATH` mechanism to fix it came out of the same binary read as D1. |
| 2026-08-08 | → planned | `plan`, `implement`, `review` and a fix were asked for together — authorized, so not an auto-advance under METHOD §3.1 — but **step 1 invalidated the rest before it ran**, which is why the plan is ordered to find that out first. Read out of the shipped binary: **the harness has no exclusion mechanism.** A local-directory install copies the tree whole and then deletes exactly one thing, `.git`; `copyDir` filters nothing; `.gitignore` is never consulted, which is why `control/` is in the cache. The marketplace entry's component fields looked like the lever and are not — they apply only to the `archive` source and are *validated* rather than applied, so declaring `skills` narrows nothing. `${CLAUDE_PLUGIN_ROOT}` is for hook arguments, not Markdown links. That settles the deferred question as **not a defect and not fixable**: a local-directory install is a snapshot by construction, the only snapshot-free arrangement is the project-level skills folder that D2 and T-050 both refused, so cache/tree drift is a property of installing. It also prices the `specify` answer for the first time: delivering it needs the plugin to become a **subtree**, moving `docs/` and `taskmd/` and rewriting every path that cites them. That is a repository restructure, it was asked for before anyone knew it was one, and METHOD §3.3 says raise it rather than widen quietly — so the plan stops at step 2 and the question goes back. |
| 2026-08-08 | → specified | Maintainer answered the boundary question: **ship what the skill points at, minus this repository's working material** — `skills/`, `docs/`, `taskmd/` and the launchers in; `tasks/`, `.handoff/`, `tests/`, `reference/`, `control/` out. That keeps `docs/METHOD.md` with one authored home and the relative pointers resolving, which is why the self-contained alternative was rejected — it would have bought a guaranteed single resolution by giving the method a second home, trading the plugin's own design rule for the symptom. The drift question is **deferred to `plan`**: whether a versioned snapshot going stale is a defect at all depends on what the harness supports for a local-directory install, which is a thing to check rather than to reason about. Criterion 2 is the one that now needs care — it asks for a demonstration that a pointer resolves once, and under this answer the honest demonstration is about which copy a session in *this* repository reads, since an adopter has only one. |
| 2026-08-08 | → proposed | Raised from T-050 §3 step 7 and not fixed there (METHOD §3.3): T-050 measures what a session is handed, and it now has the answer; what the plugin should ship is a packaging decision. The harness serves the skill from an install-time snapshot of the **whole repository**, so every relative pointer in `SKILL.md` has two resolutions, and `CLAUDE.md` already differed between them within hours of the install — duplication nobody wrote, created by installing. `high` because it lands on the tier model R-21 names and on what an adopter receives, and because the two halves pull opposite ways: shipping less breaks the pointers, shipping everything hands an adopter this project's 52 tasks and its gitignored local-context file. `s` because the work is a decision and a packaging rule, not code. Held as `decision` rather than `fix` — nothing is known to be broken for an adopter yet, since nobody has installed it but the maintainer. |
