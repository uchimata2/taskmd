---
id: T-052
title: Decide what of .claude a published clone carries, and ignore the rest
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-050, T-006, T-003]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-08
deliverables: []
---

# T-052 — Decide what of `.claude` a published clone carries, and ignore the rest

## 1. Specify

**Outcome**
`.claude/` has a stated split — what a clone is meant to receive, and what is machine-local — and
`.gitignore` enforces it, so a harness writing local state into the repository cannot put a machine
path into what a push would send.

**Why this one**
Found while answering an install-scope question during
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md), and raised rather than fixed
there (METHOD §3.3): T-050 measures what a session is handed, and `.gitignore` is not that.

`.claude/settings.json` is tracked on purpose — [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)
**D3** made it the artifact that declares this repository's own plugin by **relative** path, so
nothing machine-specific is written down. Its sibling `.claude/settings.local.json` is the harness's
per-machine override file and is **not** ignored. It is not present today, so nothing is leaking
now; what makes this worth a task is that the file is created by an ordinary action, and what the
harness writes into it is resolved to an absolute path — read out of the parser in T-050 §3 step 5,
and then **confirmed at the destination** in step 6: an install taken at user scope wrote a
drive-letter path into the harness's own settings file. The only reason that path is not in this
repository is that the scope question was answered `user`, and the same install at project or local
scope writes the same value into `.claude/settings.json` or `.claude/settings.local.json`.

**A second, smaller thing found in the same look.** `.claude/skills/` exists and is empty — the
residue of T-003's throwaway-skill probe. Git does not track empty directories, so it reaches no
clone and no check will ever mention it; it is in scope here only because this task is the one
deciding what that folder is for.

So the current state is a repository whose publishing rule (R-23, and the pre-publish check in
`CLAUDE.md`) is upheld by nobody choosing the wrong menu item. The check would catch it — that is
what the check is for — but catching it at the push is the expensive place, and the fix is one line.

**The general shape is worth more than the one file.** `.gitignore` currently lists what this project
writes for itself. `.claude/` is written by something else, on a schedule this project does not
control, and a new file appearing there is a normal harness upgrade rather than an event anyone will
notice. So the decision to take is which way `.claude/` defaults, not whether to name one more file.

**Requirements served**
R-23 (`docs/SCOPE.md`), and `CLAUDE.md` *Publishing constraints* — free of machine data, and
out-of-the-box for someone who clones it.

**Scope**
- In: which paths under `.claude/` a clone is meant to receive, and the `.gitignore` rules that make
  the answer hold without anyone re-deciding per file.
- In: whether the rule is stated anywhere a reader will meet it, or is left to the ignore file.
- In: the empty `.claude/skills/`, which the decision either gives a purpose or removes.
- Out: the content of `.claude/settings.json`. T-003 D3 settled that, and T-050's measurement did not
  disturb it — the declaration is correct, it is merely not sufficient on its own.
- Out: how the plugin is installed, and the install instructions —
  [T-006](T-006-package-document-and-publish.md), which T-050 already put an install line on.
- Out: the pre-publish check itself. It behaves correctly here; this task removes an occasion for it
  to fire, not a defect in it.

**Inputs**
`.gitignore`; `CLAUDE.md` *Publishing constraints*; `docs/SCOPE.md` R-23;
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 5, which holds the
measurement of what the harness writes and why it is absolute.

**Acceptance criteria**
- [ ] A harness-written local settings file in `.claude/` is outside what a push would send —
      demonstrated by creating one and showing `git ls-files --cached --others --exclude-standard`
      does not list it
- [ ] `.claude/settings.json` is still sent, so a clone still receives the declaration T-003 D3 wrote
      — demonstrated by the same command listing it
- [ ] The rule says which way `.claude/` defaults, so a file the harness adds later is covered
      without an edit
- [ ] The pre-publish check still prints nothing, and still prints exactly the five fixture lines
      without its exclusion

**Open questions**
- ~~Does `.claude/` default to ignored-with-exceptions, or to tracked-with-exclusions?~~ **Answered
  by the maintainer on 2026-08-08, at the level of the goal rather than the mechanism:** this is to be
  a community-maintained plugin, so *user- and machine-specific material is excluded and project
  instructions and config are present in the repository*. Only one of the two options serves that
  under contribution — **ignored-with-exceptions** — and the reason is a finding, below, not a
  preference. *Rejected: tracked-with-exclusions*, the current arrangement: it is safe exactly while
  someone keeps naming new harness files, and the person who fails to is a contributor who has never
  read this task.

**The prior art the maintainer pointed at does not solve this, and that is the evidence.** A sibling
plugin of theirs — same shape, same publishing intent — has a `.claude/settings.local.json` on disk
that is neither tracked nor reported as untracked. It is excluded by the **user's global gitignore**
(`git check-ignore -v` names `~/.config/git/ignore`, rule `**/.claude/settings.local.json`), and by
nothing in that repository at all. So the protection is real on one machine and absent for every
contributor who clones it, and it is invisible from inside the repository: the tree looks clean, the
status is empty, and nothing anyone can read there says why. That is the sharpest possible argument
for the repository carrying its own rule — a per-machine exclusion is not a project decision, it is a
project decision that happens to be true where it was tested. The same reasoning applies to that
plugin and is the maintainer's to carry there; it is out of scope here (this task owns taskmd's
`.gitignore`).

- **None outstanding.** The mechanism follows from the goal, and criterion 3 was already written to be
  satisfiable either way.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `.gitignore`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | → specified | Maintainer answered at the level of the goal — community-maintained plugin, user- and machine-specific material out, project instructions and config in — and pointed at a sibling plugin of theirs as prior art with the same problem. **Checking it is what settled the mechanism, and the answer was the opposite of prior art.** That repository's `.claude/settings.local.json` is excluded by the maintainer's *global* gitignore and by nothing in the repository; `git check-ignore -v` names the global file and the rule. So its tree looks clean, its status is empty, and its protection does not survive being cloned by anyone else — which is precisely the failure a community plugin cannot afford and which no reader of that repository could detect. **ignored-with-exceptions**, therefore, because it is the only one of the two that does not depend on someone continuing to name files: a harness upgrade adding a file is out by default, and what a clone needs is stated once, positively, as an exception. The same finding applies to the sibling plugin and belongs to the maintainer there, not here. |
| 2026-08-08 | (no status change) | The premise moved from inferred to observed. T-050's install went ahead at **user** scope and the harness wrote the marketplace source as a resolved drive-letter path into its own settings file — so "the harness stores an absolute path" is now a fact about where it landed, not a reading of the parser. The repository was untouched: tracked `.claude/settings.json` byte-identical, nothing new under `.claude/`, pre-publish check silent. That is the counterfactual this task is about, and it held only because the scope question happened to be asked. Also noted while looking: `.claude/skills/` is an empty leftover from T-003's probe, invisible to git and to every check, and in scope here only because this task decides what that folder is for. |
| 2026-08-07 | → proposed | Raised from an install-scope question during T-050 and not fixed there, since `.gitignore` is not what that task measures. Nothing is leaking today: `.claude/settings.local.json` does not exist. What makes it a task rather than a note is that the file is created by picking one of three menu items during a plugin install, it is not ignored, and the harness resolves a relative directory source to an absolute path before storing it — so the ordinary action writes a machine path into a file a push would send. `medium` and `s`: the fix is one line, the pre-publish check already catches the consequence, and the part that needs a decision is which way `.claude/` should default rather than whether to name one more file. |
