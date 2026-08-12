---
id: T-067
title: Prove the install route an adopter actually takes
type: analysis
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-006, T-053, T-054, T-052, T-077]
work_package: M1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-067 — Prove the install route an adopter actually takes

## 1. Specify

**Outcome**
It is known, by running it, whether `.claude-plugin/marketplace.json` as written installs the plugin
for someone who is not the maintainer — and if it does not, what it has to say instead.

**Why this one**
Raised as **F-15** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 3. The manifest declares:

```json
"source": "./plugin"
```

[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) **D4** recorded the mechanism
that makes a subtree pay off:

> A marketplace entry may declare a `git-subdir` source: the harness clones with `--filter=tree:0
> --no-checkout` and then `sparse-checkout set --cone -- <path>`, materialising **only** that
> directory. So one subtree serves both installs — `./<subtree>` for the maintainer's local install
> and `git-subdir` at the same path for everyone else.

The manifest declares no such source, and **no install by any route other than a local directory has
ever been performed.** T-053's own log is explicit that its file list describes *"what the git route
would deliver"* — reasoned from reading the harness's code, not run. The one real install recorded
anywhere in this project is the maintainer's, from a directory, on this machine.

**Why this is `analysis` and not `fix`.** It may need no change at all: a relative source inside a
git-hosted marketplace may resolve exactly as intended, in which case the finding is that nobody
knew. Deciding to add a `git-subdir` entry before establishing that would be building against an
assumption, which is the failure mode this project keeps naming.

**Deduped, deliberately.** [T-006](T-006-package-document-and-publish.md) criterion 4 already says
*"installs from a clean clone on a machine that has never seen it"*, and owns the outcome. This task
exists because that criterion does not name **what** to run, and because discovering at publication
that the manifest needs a second source shape is exactly the release-day cost the audit's severity
scale is about. If the maintainer prefers, this folds into T-006 as a named step rather than standing
alone — recorded here so the choice is available rather than made by default.

**Requirements served**
R-20 (`docs/SCOPE.md`) — runs on a clone with no configuration; `docs/SCOPE.md` §1 *No install*, whose
whole content is that a clone works.

**Scope**
- In: whether the marketplace entry, as written, installs for a non-maintainer.
- In: what the resulting install contains, listed rather than predicted — T-053's 22-file expectation
  has never been checked against a git-sourced install, and its own log already found the
  local-directory route carries five files the prediction missed.
- In: whether `plugin/bin/` reaches `PATH` by that route, which is the whole of
  [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)'s mechanism.
- Out: publishing. This is a rehearsal against whatever remote is convenient, not a release.
- Out: the boundary and what ships, both settled in T-053.
- Out: the install *instructions*, which are T-006's.

**Inputs**
`.claude-plugin/marketplace.json`, `plugin/.claude-plugin/plugin.json`,
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) D1 and D4 and its closing log
entry, [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md),
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-15.

**Acceptance criteria**
- [ ] The plugin is installed by a route that is **not** a local directory, and the attempt's result
      is recorded either way — a failure is as much the outcome as a success
- [ ] The installed tree is **listed**, not predicted, and compared against T-053 §3 step 4's
      twenty-two files
- [ ] A command from the skill runs in that install, from a directory that is neither the plugin nor
      this repository — which is the claim T-054 established for the local route only
- [ ] If the manifest needs a different or additional source declaration, that is stated with what it
      would be; if it does not, that is stated too
- [ ] No absolute path from any machine reaches this record (R-23)

**Open questions**
- ~~**What stands in for "a machine that has never seen it"?**~~ **Answered by the maintainer on
  2026-08-09: a throwaway remote repository.**

  So the git route is tested as a git route — clone from a remote the harness has never seen, by the
  same mechanism an adopter would use — rather than by a path that happens to resolve. That is the
  only option that can answer the question the task was raised for: whether `"source": "./plugin"`
  needs to become `git-subdir`, which is a property of how the harness fetches a **remote**
  marketplace and is unobservable from any local arrangement.

  *Rejected: a second checkout on this machine.* It proves the source resolves outside the original
  working tree, which is worth something and is not the claim. A local clone is still a directory, so
  the fetch path — the part T-053 D4 reasoned about and nobody has run — is never exercised.

  *Rejected: a local bare repository as the remote.* It is a real `git clone`, costs nothing to
  delete, and is the tempting middle. It may also resolve by a code path that a hosted remote does
  not, and a result that might be an artefact of the transport answers nothing — which is the failure
  this task exists to avoid committing again.

  *Rejected: folding into [T-006](T-006-package-document-and-publish.md).* Offered in §1 and available;
  it moves the discovery to publication day, which is the release-day cost the audit's severity scale
  is about.

  **Cleanup is part of the work, not an afterthought.**
  [T-037](T-037-delete-the-throwaway-proof-repository.md) exists because the first scratch repository
  outlived its purpose and was awkward to remove. So this task's plan names the remote's deletion as
  a step with its own output, and `implement` records the deletion as evidence — not "will be removed
  later".

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish whether a **non-interactive** install route exists at all, before creating anything — T-053's evidence was reasoned rather than run precisely because the reinstall was thought to need a terminal | The answer, and what the run will be |
| 2 | Run the pre-publish check, then inspect what a push would actually send | The clean check, and the file inventory |
| 3 | Create the throwaway remote **private**, push once | The remote |
| 4 | Add the marketplace by the git route and install from it, capturing the pre-existing local-directory install first so the two can be compared | Both file lists |
| 5 | Compare against T-053 §3 step 4's twenty-two, and say where the difference comes from | The diff |
| 6 | Run a command from the install, in a directory that is neither the plugin nor this repository | The transcript |
| 7 | **Restore everything**: uninstall, remove the git marketplace, re-add the directory one, reinstall, and check this repository's own `.claude/settings.json` — the harness rewrites it when plugin scope changes | The restored state |
| 8 | Delete the remote | Its absence, or a task for it |

**Why step 1 is a step.** T-053's file list is described in its own log as *"what the git route would
deliver"*, reasoned because *"the reinstall needed an interactive terminal"*. If that were still
true, this task's honest outcome would be a statement of what cannot be run. It is not true:
`claude plugin marketplace add` and `claude plugin install` both work non-interactively.

**Why step 7 is as large as the test.** The install being exercised is the maintainer's own, on their
own machine. Leaving it pointed at a remote about to be deleted would be worse than not running the
test.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — private, not public** — 2026-08-09. The maintainer authorised a throwaway remote; the
  visibility was not specified and private is the option that publishes nothing. It cost nothing: the
  harness cloned it over HTTPS using the existing credential helper, so a private remote exercises
  the same fetch path a public one would.

- **D2 — the pre-existing install was captured before it was disturbed** — 2026-08-09. The local
  directory install had been in place since 2026-08-08, and once overwritten it could not be
  inspected. Capturing it first is what turned "does the git route work" into a **comparison**, which
  is where this task's most useful finding came from.

- **Assumption, recorded:** that a marketplace's declared `name` is what the harness keys on. It is —
  and it means a marketplace named `taskmd` from a remote silently **replaced** the directory one of
  the same name. No warning, no prompt. Recorded because it is a real property of the mechanism and
  because it is what made step 7 necessary rather than tidy.

### Steps 3–4 — the install, by a route that is not a local directory

```
gh repo create <the rehearsal repository> --private
git push <it> master

claude plugin marketplace add <owner>/<the rehearsal repository>
  SSH not configured, cloning via HTTPS
  Clone complete, validating marketplace…
  Successfully added marketplace: taskmd (declared in user settings)

claude plugin uninstall taskmd@taskmd
claude plugin install  taskmd@taskmd
  Successfully installed plugin: taskmd@taskmd (scope: user)
```

**`"source": "./plugin"` resolves over the git route, as written.** No `git-subdir` entry was needed
and none was added. That is the question the task was raised for, and the answer is that the manifest
needs no change.

**What the marketplace clone carries, which is the half T-053 D4 was actually about.** The harness
clones the **whole repository** for the marketplace — 152 files, `tasks/` and `tests/` and
`reference/` included — and then materialises the plugin from `./plugin` into the install cache.
So `git-subdir` would be a clone-size optimisation, not a correctness requirement. D4 described a
mechanism that exists; it is not the mechanism this manifest triggers.

### Step 5 — the installed tree, listed rather than predicted

**24 files.** T-053 §3 step 4 predicted **22**, and the difference is exactly two:

```
bin/taskmd
bin/taskmd.cmd
```

Both added by [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md), *after* that
list was written. T-053's prediction was right for its date, and the git route delivers precisely
`plugin/`'s tracked contents today — no `tasks/`, no `tests/`, no `reference/`, no root documents.

**The comparison is the finding.** The local-directory install held **32** files against the git
route's 24, and the extra eight are all junk:

```
.in_use/11144, .in_use/21076, .in_use/25524, .in_use/35216.tmp.ea399020   lock files
taskmd/__pycache__/{__init__,__main__,cli,discovery,schema}.cpython-312.pyc
bin/taskmd-probe
```

The `.pyc` files are the five T-053's log already predicted a directory copy would carry. `.in_use`
is new. **`bin/taskmd-probe` is the interesting one: it exists nowhere in the tree.** It is a
leftover from an earlier session's probing that the directory install copied once and has never
pruned — so a directory install accumulates, and the route an adopter takes does not. Nobody would
have found that without installing by both routes and diffing them.

### Step 6 — a command from the install, in neither the plugin nor this repository

A project holding one task and nothing else, run through the installed entry point:

```
<install>/bin/taskmd check
OK - 1 task(s), vocabulary valid, references resolve, no broken links      exit 0

<install>/bin/taskmd list
T-001  proposed  -  specify  A task in a project that is neither the plugin nor taskmd's own repository
```

T-054 established this for the local route. It now holds for the route an adopter takes.

### Step 7 — restored, and one thing that had to be

```
claude plugin uninstall taskmd@taskmd        uninstalled
claude plugin marketplace remove taskmd      removed
claude plugin marketplace add ./             re-added as Directory
claude plugin install taskmd@taskmd          installed, enabled
```

**The harness emptied this repository's `.claude/settings.json` during the swap** — both
`extraKnownMarketplaces` and `enabledPlugins` came back `{}` — which is the behaviour
[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md) tracks the file for. It showed up
in `git status` rather than silently, which is the whole point of tracking it, and was restored from
the index. Final state matches the state before this task started.

### Step 8 — the remote, which could not be deleted

```
gh repo delete <the rehearsal repository>
HTTP 403: Must have admin rights to Repository.
This API operation needs the "delete_repo" scope.
```

The same 403 that produced [T-037](T-037-delete-the-throwaway-proof-repository.md) two days earlier:
the token carries `repo` and not `delete_repo`, and adding it is an interactive re-authentication
that is the owner's action. The `rehearsal` git remote this task added **was** removed, so no local
clone points at it. The repository itself is carried as
[T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) rather than left unsaid.

**Outputs produced**
- This record — the file lists, the diff between routes, and what the manifest does not need
- [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) — the deletion that could
  not complete
- `control/LOCAL-CONTEXT.md` — the repository's qualified name, which the tracked tree may not hold

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The plugin is installed by a route that is **not** a local directory, and the attempt's result is recorded either way | met | §3 step 4 — a private remote, cloned over HTTPS by the harness, installed from. It succeeded, so the "failure is as much the outcome" branch was not needed |
| The installed tree is **listed**, not predicted, and compared against T-053 §3 step 4's twenty-two files | met | §3 step 5 — 24, and the two extra are T-054's entry point, added after that list. The unplanned finding is the comparison with the directory route: 32 files, eight of them junk including one that exists nowhere in the tree |
| A command from the skill runs in that install, from a directory that is neither the plugin nor this repository | met | §3 step 6 — `check` and `list`, on a project holding one task |
| If the manifest needs a different or additional source declaration, that is stated with what it would be; if it does not, that is stated too | met | **It does not.** `"source": "./plugin"` resolves as written. `git-subdir` would reduce what the *marketplace* clone carries — 152 files — which is a size question, not a correctness one, and T-053 D4 described the mechanism rather than a defect |
| No absolute path from any machine reaches this record (R-23) | met | Every path is written as a placeholder or repo-relative; the repository's qualified name is in `control/LOCAL-CONTEXT.md` on T-037's precedent. Pre-publish check run last |

**Child fix tasks raised**
- **[T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md)** — the remote still
  exists. Raised rather than folded into T-037, which is the same 403 on a repository that is alive
  *on purpose* until T-006 publishes; merging would inherit a block this one does not have.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met. **The manifest needs no change**: `"source": "./plugin"` resolves over the git route exactly as written, so the `git-subdir` shape T-053 D4 described is a clone-size option rather than a correctness requirement — the harness clones the whole repository for the *marketplace* (152 files) and materialises the plugin from the relative path. The installed tree is 24 files against T-053's predicted 22, and the two extra are T-054's `bin/`, added after that list was written; the prediction was right for its date. The finding nobody asked for came from capturing the pre-existing install **before** disturbing it: the local-directory route holds 32 files, eight of them junk — five `.pyc`, four `.in_use` locks, and `bin/taskmd-probe`, which exists nowhere in the tree and is a leftover the directory install copied once and never pruned. A directory install accumulates; the route an adopter takes does not. Two things were escalated rather than absorbed: a remote marketplace **silently replaced** the same-named directory one, and the harness emptied this repository's `.claude/settings.json` during the swap — visible in `git status`, which is why T-052 tracks it, and restored from the index. Cleanup completed except the deletion, which hit the same missing `delete_repo` scope that produced T-037; carried as T-077. |
| 2026-08-09 | → in_progress | Plan opens by asking whether a non-interactive install route exists at all, because T-053's file list is reasoned rather than run on the stated grounds that *the reinstall needed an interactive terminal* — if that still held, this task's honest outcome would have been a statement of what cannot be run. It does not hold: `claude plugin marketplace add` and `claude plugin install` both work without one. |
| 2026-08-09 | → specified | Answered: **a throwaway remote repository**, which is the only option that exercises the thing the task was raised about — how the harness fetches a *remote* marketplace, and therefore whether `"source": "./plugin"` has to become `git-subdir`. A second local checkout and a local bare remote were both rejected and why is written down: the first never leaves a directory, and the second may resolve by a transport-specific path, so a pass would not be evidence. Folding into T-006 was rejected because it moves the discovery to publication day. The answer adds an obligation the specify section now carries explicitly: **deletion of the remote is a plan step with its own output**, because T-037 exists for a scratch repository that outlived its purpose. Criteria unchanged. |
| 2026-08-09 | → proposed | Raised as F-15 from the T-059 audit, clause 3. `medium`/`s`, and typed `analysis` because the honest first move is to find out rather than to add a source declaration on the strength of a design note. Deduped against T-006 criterion 4, which owns the outcome and names no command; recorded separately so the specific unproven thing — a relative subtree source, never installed by any route but a local directory — is visible before publication rather than at it. |
