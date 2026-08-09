---
id: T-067
title: Prove the install route an adopter actually takes
type: analysis
status: specified
phase: specify
parent: T-059
blocked_by: []
related: [T-006, T-053]
work_package: none
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
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → specified | Answered: **a throwaway remote repository**, which is the only option that exercises the thing the task was raised about — how the harness fetches a *remote* marketplace, and therefore whether `"source": "./plugin"` has to become `git-subdir`. A second local checkout and a local bare remote were both rejected and why is written down: the first never leaves a directory, and the second may resolve by a transport-specific path, so a pass would not be evidence. Folding into T-006 was rejected because it moves the discovery to publication day. The answer adds an obligation the specify section now carries explicitly: **deletion of the remote is a plan step with its own output**, because T-037 exists for a scratch repository that outlived its purpose. Criteria unchanged. |
| 2026-08-09 | → proposed | Raised as F-15 from the T-059 audit, clause 3. `medium`/`s`, and typed `analysis` because the honest first move is to find out rather than to add a source declaration on the strength of a design note. Deduped against T-006 criterion 4, which owns the outcome and names no command; recorded separately so the specific unproven thing — a relative subtree source, never installed by any route but a local directory — is visible before publication rather than at it. |
