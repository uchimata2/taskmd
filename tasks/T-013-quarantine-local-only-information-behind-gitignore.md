---
id: T-013
title: Quarantine local-only information behind .gitignore
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-006, T-008, T-011]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - CLAUDE.md
  - tasks/T-007-define-the-project-scope-goals-and-requirements.md
  - tasks/T-008-write-the-backend-neutral-method-document.md
---

# T-013 — Quarantine local-only information behind .gitignore

## 1. Specify

**Outcome**
Every identifiable, personal or machine-specific fact this project relies on lives in **one
gitignored local file**, and every tracked file that needed such a fact points at it generically.
Sessions keep the information they need; publishing cannot leak it, because it is not in the tree
that gets pushed.

**Requirements served**
R-23 (`docs/SCOPE.md`).

**Why this one**
R-23 is a publishing gate, and the current tree does not pass it. Tracked task files name a real
project and its internal paths as a prior-art source — evidence the project genuinely needs, in a
place that gets published. The existing `.gitignore` already reserves `control/` as "local scratch
— never published", so the mechanism exists and is simply unused. Deciding this per-mention, file
by file, is what let it accumulate; one quarantine file makes the rule checkable.

**Scope**
- In: choosing the quarantine file and ignoring it; moving the identifiable references there;
  rewriting the tracked mentions to a generic form that keeps the evidentiary point; deleting
  local-only facts nothing still needs; a repeatable check that says whether the tree is clean.
- Out: `reference/` — already verified clean (2026-08-04: no project name, tool name or client
  trace). Notion, GitHub and Unity as **product** names are not covered: they are public tools
  cited as prior art, not client data.

**Known occurrences** (verified 2026-08-04, `reference/` scanned and clean)

| File | Line | What |
| :--- | :--- | :--- |
| `tasks/T-007-...md` | 41 | Project name + its internal `.agents/` paths, as a studied source |
| `tasks/T-007-...md` | 61 | Project name in the plan's step 1 |
| `tasks/T-007-...md` | 131 | Project name in the log |
| `tasks/T-008-...md` | 62 | Project name + internal paths, as an input |

**Inputs**
- `docs/SCOPE.md` R-23; `CLAUDE.md` *Publishing constraints*
- `.gitignore` — already ignores `control/`, `dist/`, `.handoff/HANDOFF.md`, `.handoff/processed_*`

**Acceptance criteria**
- [ ] One gitignored file holds every local-only fact, and `git check-ignore` confirms it is ignored
- [ ] No tracked file names a real project, person, client, hostname, drive letter or absolute
      local path — proven by running the check below and getting no hits
- [ ] Each rewritten mention still carries its evidentiary point (that a real non-file backend ran
      the same lifecycle), so no argument in `SCOPE.md` or the tasks weakens
- [ ] Local-only facts nothing still needs are deleted rather than quarantined
- [ ] The check is written down somewhere a future session will run it before publishing

**Open questions**
- ~~Which file?~~ **`control/LOCAL-CONTEXT.md`** — see *Decisions*.
- ~~Subcommand, grep or hook?~~ **A grep**, settled by non-goal 11 — see *Decisions*.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Choose the quarantine file and confirm git actually ignores it. | `control/LOCAL-CONTEXT.md`, `git check-ignore` output |
| 2 | Move the identities there behind a label, with why each is kept rather than deleted. | the quarantine file |
| 3 | Rewrite the four tracked occurrences to use the label. | T-007 ×3, T-008 ×1 |
| 4 | Write the pre-publish check where a publisher will meet it. | `CLAUDE.md` |
| 5 | **Prove the check by making it fail** on one planted line per class. | the run, in §4 |

## 3. Implement

**Decisions & assumptions**
- **`control/LOCAL-CONTEXT.md`, not a new root file** (2026-08-04). `.gitignore` already excludes
  `control/` and describes it as "Local scratch — never published", so reusing it needs no new
  ignore rule — and a new rule is a thing that can be written wrong. The filename carries the meaning
  that the directory name does not.
- **The check is a grep, and that was already decided** (2026-08-04). Non-goal 11 keeps the CLI to
  `context`, `index` and `check` and says anything else is grep, so a `task.py` subcommand was never
  available. A project hook (T-011) is the better long-term home; the grep is written so it can move
  there unchanged.
- **Label, not deletion** (2026-08-04). The identity is load-bearing evidence: it is the only prior
  art running this lifecycle against a **non-file backend**, which is what makes R-13/R-14 testable
  rather than aspirational. Deleting the reference would weaken `docs/SCOPE.md`'s argument; naming
  the project would publish a client engagement. The label keeps the argument and drops the identity.
- **"Handoff" stays named** (2026-08-04). It is a sibling plugin of this one, cited by R-24, and
  published in its own right — not client data. Only the client project was quarantined.
- **`git ls-files` rather than a directory walk** (2026-08-04). The check must answer "what would a
  push send", not "what is on disk"; anything gitignored is then out of scope by construction, and
  the quarantine file cannot trip its own check.

**Outputs produced**
- `control/LOCAL-CONTEXT.md` — gitignored; the label map, why the evidence is kept, and the facts
  deliberately not recorded
- `tasks/T-007-…md` (3 occurrences), `tasks/T-008-…md` (1) — now use the label
- `CLAUDE.md` — the quarantine rule and the pre-publish check, with its two limits stated

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One gitignored file holds the local-only facts; `git check-ignore` confirms | met | `.gitignore:2:control/  control/LOCAL-CONTEXT.md`, exit 0. `git status --untracked-files=all` does not list it. |
| No tracked file names a real project, person, client, hostname, drive letter or absolute path | met | The check below is clean across `git ls-files`; a separate grep for the client name over the tracked tree returns nothing. |
| Each rewritten mention still carries its evidentiary point | met | All four now say *the Notion-backed project* and state what it evidences — T-007's entry gained an explicit "the only prior art here that is not file-based, which is what makes R-13/R-14 testable", which the original left implicit. |
| Local-only facts nothing needs are deleted rather than quarantined | met | The quarantine file records what was **not** kept and why: absolute checkout paths, the studied project's Notion workspace/database ids and board URLs, and any person or company name. |
| The check is written where a future session will run it before publishing | met | `CLAUDE.md` *Publishing constraints*, as the first bullet's consequence rather than a separate appendix. |

**The check, proven by failing** (plan step 5). A fixture with one line per class, plus four lines
that must **not** trip it:

```
1:drive C:\Work\AgentPlugins\taskmd          <- caught
2:home /home/someone/project                 <- caught
3:users /Users/someone/project               <- caught
4:unc \\fileserver\share\docs                <- caught
5:ip 192.168.1.42                            <- caught
  safe https://example.com/a                 <- correctly ignored
  safe a python d:\n escape inside a string  <- correctly ignored
  safe the words drive letters and hostnames <- correctly ignored
  safe version 1.2.3 and a range 1-3         <- correctly ignored
```

Two earlier drafts were wrong, and **only the failure test found them**. The first matched `http://`
and a `d:\n` escape — noise that would have trained a reader to ignore the check. The second ended a
branch in `\\`, which grep parses as an escaped `|`, silently gluing the IP branch onto the UNC one
so that **neither** fired. Both drafts pass cleanly on a clean tree, which is precisely why
`CLAUDE.md` *Verifying* says a clean-tree pass proves nothing.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → done | Identities moved to the gitignored `control/LOCAL-CONTEXT.md` behind a label; four tracked occurrences rewritten; pre-publish grep added to `CLAUDE.md` and proven by being made to fail on all five leak classes. `.gitignore` needed no change — `control/` was already excluded, so it left the deliverables list. |
| 2026-08-04 | → proposed | Raised while planning T-008: the R-23 risk is repo-wide (T-007 and T-008 both carry it), so it is its own fix rather than a step inside T-008. |
