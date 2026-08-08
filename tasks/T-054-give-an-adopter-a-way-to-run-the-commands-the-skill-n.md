---
id: T-054
title: Give an adopter a way to run the commands the skill names
type: fix
status: in_progress
phase: implement
parent: null
blocked_by: []
related: [T-053, T-006, T-003]
work_package: none
owner: maintainer
business_value: critical
effort: s
created: 2026-08-08
updated: 2026-08-08
deliverables: []
---

# T-054 — Give an adopter a way to run the commands the skill names

## 1. Specify

**Outcome**
Someone who installs this plugin and asks their agent what to work on next gets an answer, because
the command the skill tells it to run is one their machine can actually execute.

**Why this one**
Found during [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)'s restructure,
and **it is not caused by it** — the same hole was there before, hidden by this repository being the
only place the plugin had ever run.

`plugin/skills/taskmd/SKILL.md` opens with `python -m taskmd list --open --limit 1`, and
[`../plugin/skills/taskmd/adopt.md`](../plugin/skills/taskmd/adopt.md) ends with
`python -m taskmd check`. For an adopter, neither can work: the package sits in the plugin's
install cache, their working directory is their own project, and nothing puts the two together.
`python -m taskmd` raises `No module named taskmd`. The launchers solve it only for someone standing
in the plugin directory, which an adopter never is. So **every command the skill names fails for the
only audience the skill exists for**, and it has never been noticed because in this repository the
package happens to be in the tree.

That makes it critical rather than merely important: it is not a rough edge in the adoption path, it
is the adoption path not working at all, and [T-006](T-006-package-document-and-publish.md) would
publish it as-is.

**The mechanism to fix it is already established.** Read out of the shipped binary during T-053: the
harness collects `<plugin-root>/bin` for every enabled non-builtin plugin and puts those directories
on `PATH` (dropping any containing shell metacharacters). So a `bin/` entry point in the plugin
subtree becomes a command an adopter can type from anywhere, with no install step, no `PYTHONPATH`,
and no path editing — which is what `CLAUDE.md` *Publishing constraints* means by out-of-the-box.

**Requirements served**
**R-18** (`docs/SCOPE.md`) most directly — *"the repository root are auto-discovered so a clone runs
unedited"*. That requirement is currently **unmet for anyone who is not standing in this repository**,
which is the whole of this task. Also `docs/SCOPE.md` §1 *Invisibility* — a tool the agent cannot
invoke is not invisible, it is absent — and R-19 with the dependency-free constraint in `CLAUDE.md`,
which bind the shape of the answer.

**Scope**
- In: how an adopter invokes the four commands, and what the skill and `adopt.md` tell them to type.
- In: whether the `bin/` mechanism is the answer, or whether the skill should name something else.
- In: what this repository itself types, so the instruction has one form rather than two.
- Out: what the plugin contains — [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md).
- Out: install instructions and published shapes — [T-006](T-006-package-document-and-publish.md).
- Out: adding a command. The four exist; this is about reaching them.

**Inputs**
`plugin/skills/taskmd/SKILL.md`, `plugin/skills/taskmd/adopt.md`, `plugin/taskmd.sh` and
`plugin/taskmd.ps1` for how the path is set today, and
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) §2 D1 for what was read out
of the harness.

**Acceptance criteria**
- [ ] The command the skill names runs from a directory that is **not** this repository and not the
      plugin folder — demonstrated by running it in a scratch project and showing the output
- [ ] The failure is demonstrated first, on the current arrangement, so the fix is shown to fix
      something rather than to coincide with something working
- [ ] `SKILL.md` and `adopt.md` name one form of the command, not one each
- [ ] The suite still passes and `check` is still clean on this repository

**Open questions**
- **Does this repository use the same entry point it ships?** Using it proves it on every turn, which
  is this project's usual argument. Against: `bin/` is only on `PATH` when the plugin is *installed
  and enabled*, so a contributor who has merely cloned would find the documented command missing —
  the same class of defect as T-052's global-ignore finding, where the thing worked only where it had
  been tested. `specify` cannot settle this alone; it needs the `bin/` shape to be known.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Demonstrate the failure on the current arrangement, from a directory that is neither this repository nor the plugin folder | A recorded transcript in §3 of the command `SKILL.md` names and what it actually does |
| 2 | Settle whether `<plugin-root>/bin` on `PATH` is a mechanism that *runs*, rather than one that is merely present in the binary — everything after this step assumes its answer | **D1**, below — a recorded verdict, and it needs a session this one cannot start |
| 3 | *(shape assumes step 2 says yes)* Write the entry point and reach the four commands through it | `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd` |
| 4 | Make the skill and the adoption note name that one form | the command named in `plugin/skills/taskmd/SKILL.md` and `plugin/skills/taskmd/adopt.md` |
| 5 | Re-run the suite and `check` on this repository | recorded output in §3 |

Step 1 is first because §1's second acceptance criterion asks for the failure before the fix, and it costs
one command. **Step 2 is where this plan can be invalidated**, which is
[`../plugin/docs/method/plan.md`](../plugin/docs/method/plan.md)'s *reduces uncertainty soonest* rule —
it is second rather than first only because step 1 does not depend on it. Steps 3–5 are written at the
detail step 2 allows and no further: if step 2 answers no, the plan stops there rather than
substituting D4's shape silently.

**Shape decisions.**

**D1 — The `bin/` mechanism is read-from-source and *not demonstrated*, so step 2 exists to settle
it.** §1 calls it "already established"; that overstates what was read. What is confirmed: the shipped
binary exports `getEnabledPluginBinPaths`, whose body is exactly what
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) D1 described — the enabled,
non-builtin plugins that have a path, mapped to `<path>/bin`, with entries containing shell
metacharacters dropped when the path separator is not a backslash. What is **not** confirmed is that
anything calls it: in a live session with this plugin installed and enabled, `PATH` carries no plugin
`bin` directory at all, and creating one inside the install cache mid-session did not add it. Two
readings survive that — the consumer keeps only directories that existed when plugins were loaded, or
the export is unreached in this build — and they differ in whether step 3 is the right step.

The probe for it is already planted: an executable named `taskmd-probe` now sits in a `bin/` directory
inside this plugin's install cache. A session started after it was written settles D1 with one
command, `command -v taskmd-probe`, and no reinstall. **This session cannot run that command
meaningfully**, because `PATH` is fixed before the first turn — which is why step 2 is a step rather
than something this plan already answers.

**D2 — This repository keeps typing its launcher, and the skill names the `bin/` command. They differ
on purpose.** This settles §1's open question. The two audiences hold different things: a contributor
has the tree and no install, an adopter has an install and no tree. `./plugin/taskmd.sh` works from a
fresh clone with no setup at all; a `bin/` command works from an install with no path knowledge and no
`PYTHONPATH`. Making this repository type the shipped command would make its own documented command
missing for anyone who had merely cloned — which is
[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md)'s finding re-created rather than
avoided, and it would make `CLAUDE.md`'s *out-of-the-box* constraint false for the contributor it is
written for.

The cost is a real one and is stated rather than waved away: this repository stops proving the shipped
entry point on every turn. It is **bounded** by D3 — the `bin/` entry is a delegate to the launcher, so
the body is still exercised continuously and only the delegation is not, and exercising that
delegation from a directory that is not this repository is exactly what criterion 1 asks for.
*Rejected: this repository types the shipped command* — unavailable in a clone, per the above.
*Rejected: the skill names the launcher* — an adopter cannot write a relative path into a cache
directory they never see, which is the whole of §1.

**D3 — Two entry-point files, because one cannot be typed on both platforms.** An extensionless
`bin/taskmd` is a POSIX script; a `PATH` lookup from PowerShell or `cmd` will not execute it, and
`.cmd` is in the default `PATHEXT` where `.sh` and `.ps1` are not. So `bin/taskmd` and
`bin/taskmd.cmd`, each a delegate to the launcher one directory up rather than a second
implementation of interpreter discovery — the launchers already solve that, and a second copy is the
one thing this project's design rule forbids.
*Rejected: a Python file in `bin/`* — it has the same extension problem and needs an interpreter
located before it can run, which is the job the launchers exist to do.

**D4 — If step 2 answers no, the fallback has a different shape and is not this plan's to adopt.**
Named here so step 2 has somewhere to point rather than stalling: `${CLAUDE_PLUGIN_ROOT}` does
substitute into **command and hook arguments** (T-053 D1), so a plugin *command* could carry the
invocation even where a Markdown pointer and a `PATH` entry cannot. That changes what the plugin
ships and what the skill is, so it needs agreement at `specify` rather than a quiet swap here.

**Planned outputs**
- `plugin/bin/taskmd`
- `plugin/bin/taskmd.cmd`
- `plugin/skills/taskmd/SKILL.md` — the command it names
- `plugin/skills/taskmd/adopt.md` — the command it names

## 3. Implement

### Step 2 — D1 settled: the mechanism exists and is wired; one machine's shell is broken

**The probe answered no, and the reason is neither of the two readings D1 offered.** A session started
after the probe was planted reported that no plugin `bin` directory was on `PATH` — 37 entries, none
matching `plugin`, and `command -v taskmd-probe` not found. Taken alone that reads as "the mechanism
does not work". Reading further changes the verdict.

**The chain is complete in the shipped binary.** `getEnabledPluginBinPaths` is not an unreached
export: it is called from the **shell-snapshot builder**, which composes the login shell's `PATH`,
appends every enabled plugin's `bin` directory (converted to POSIX form on Windows), and writes the
result into the snapshot as a single `export PATH=…` line inside a heredoc. The snapshot is what the
agent's shell sources. So a `bin/` entry point is the right shape, and D1's two candidate
explanations — *kept only directories present at plugin load*, and *the export is unreached* — are
**both false**.

**What is actually broken is the snapshot file.** Its `export PATH=` line is **truncated mid-value**:
it opens a single quote, runs to a fixed 5551 characters, and ends part-way through a path with no
closing quote. Sourcing it fails —

```text
line 44: unexpected EOF while looking for matching `''
```

— and the shell silently keeps its inherited `PATH`. That is why the plugin's `bin` directory is
present *in the file* and absent from every live `PATH`: it is written correctly and then never
loaded. Verified by sourcing the newest snapshot in a subshell, which left the entry count unchanged.

**And the truncation is a property of this machine, not of the mechanism.** The oldest snapshot on
disk has a 2064-character `PATH` line, a matched pair of quotes, and sources cleanly. Every snapshot
since carries exactly 5551 characters and exactly one quote — the *same* length across files whose
contents differ, which is the signature of a fixed cap rather than of the value itself. This machine
carries an unusually long `PATH`; a shorter one stays under the cap. **Stated as the strong
hypothesis it is**: the threshold lies between those two figures and has not been bisected, because
doing so needs a second machine and does not change what this task builds.

**No evidence is quoted here.** The material is a `PATH` listing, which is the home-directory class
the pre-publish check in `CLAUDE.md` exists to catch; the counts and the shell's own error message
carry the finding without reproducing it.

**Decisions & assumptions**

- **D1 answers *yes*: `bin/` is the mechanism, and step 3 proceeds.** — The plan's stop condition was
  written for "the mechanism does not exist", and the mechanism does. What fails is one machine's
  shell snapshot, which no change to this plugin can repair and which an adopter with an ordinary
  `PATH` never meets. *Rejected: stopping and adopting D4's shape* — it would swap what the plugin
  ships on the strength of a defect that is not in the plugin. **Decided by the maintainer,
  2026-08-08**, after the root cause was put to them. — 2026-08-08
- **The consequence is accepted and named: this repository cannot dogfood the shipped entry point.** —
  It would not resolve here even once built. D2 had already decided this repository types
  `./plugin/taskmd.sh` and the skill names the `bin/` command, so the loss is bounded to what D2
  already accepted; but "we run what we ship" is not available for this one artifact, and saying so
  is cheaper than a later reader assuming it was checked. — 2026-08-08
- **The truncation is an upstream defect and is not tracked here.** — It is a harness bug: a snapshot
  that fails to parse should not silently drop every plugin's `bin`. taskmd cannot fix it, no
  acceptance criterion depends on it, and a task in this backlog for someone else's code would never
  close. Recorded in this step so the next reader is not re-deriving it, and in agent memory as the
  reusable half. — 2026-08-08

**Outputs produced**
- This step's verdict. Steps 1 and 3–5 remain.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | → in_progress | Step 2 taken, and **D1 is answered yes** — the opposite of what the probe alone said. The probe was a clean negative (no plugin `bin` on `PATH`, `taskmd-probe` not found), but reading further inverted it: `getEnabledPluginBinPaths` **is** called, from the shell-snapshot builder, which appends every enabled plugin's `bin` to the login `PATH` and writes it as one `export PATH=` line for the agent's shell to source. So D1's two candidate explanations were both false. What is broken is the snapshot **file**: its `PATH` line is truncated mid-value at a fixed 5551 characters, leaving an unmatched quote, so sourcing dies on `unexpected EOF` and the shell silently keeps its inherited `PATH` — the plugin `bin` is written correctly and never loaded. Confirmed by sourcing the newest snapshot in a subshell and watching the entry count not move. The cap is a property of **this machine's long `PATH`**, not of the mechanism: the oldest snapshot here is 2064 characters with matched quotes and sources fine, while every later one is the same 5551 across differing contents. Stated as a hypothesis, unbisected, because it needs a second machine and changes nothing this task builds. Maintainer decided to proceed rather than fall back to D4, which would have swapped what the plugin ships on the strength of a defect that is not in the plugin. Accepted consequence, named: this repository cannot dogfood the shipped entry point. The truncation is an upstream harness bug and is deliberately **not** a task here — taskmd cannot fix it and such a task would never close. No `PATH` listing is quoted anywhere in the record; it is the home-directory class the pre-publish check exists to catch. |
| 2026-08-08 | → planned | Plan written; §1's open question settled as **D2** — this repository keeps typing `./plugin/taskmd.sh` and the skill names the `bin/` command, because a contributor has the tree and no install while an adopter has an install and no tree, and typing the shipped command here would make it missing for anyone who merely cloned. The plan's own finding is **D1**: §1 calls the `bin/` mechanism "already established" and that overstates the read. `getEnabledPluginBinPaths` is in the shipped binary with exactly the described body, but no plugin `bin` directory is on a live session's `PATH` with this plugin installed and enabled, and creating one mid-session did not add it — so whether anything *calls* it is open, and steps 3–5 assume an answer this session cannot obtain, `PATH` being fixed before the first turn. A probe was planted in the install cache so a later session settles it with one command. |
| 2026-08-08 | → proposed | Raised from T-053's restructure and **not caused by it**: the same hole predates the move and was hidden by this repository being the only place the plugin had ever run. Every command `SKILL.md` and `adopt.md` name — `python -m taskmd …` — fails for an adopter, because the package is in the install cache and their working directory is their own project. `critical` because it is not a rough edge in the adoption path but the adoption path not working at all, and T-006 would publish it as-is; `s` because the mechanism is already known. Read out of the shipped binary during T-053: the harness puts `<plugin-root>/bin` on `PATH` for every enabled plugin, so a `bin/` entry point is a command an adopter can type from anywhere with no install step and no `PYTHONPATH`. The open question is whether this repository should then type that same command, which proves it continuously but is only on `PATH` when the plugin is installed — the T-052 shape, where a thing works only where it was tested. |
