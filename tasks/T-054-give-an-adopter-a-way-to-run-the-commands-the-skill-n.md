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

### Step 1 — the failure, taken after step 2 rather than before it

Step 2 had to run in a session started after its probe was planted, so it was taken first and this
step second. Nothing in step 1 depends on step 2's answer, which is why the plan already allowed
either order.

A scratch project was made outside this repository — a folder containing only `tasks/` with one
task in it, which is what an adopter has after `adopt.md` §1. The commands are the ones `SKILL.md`
and `adopt.md` named at the time:

```text
python -m taskmd list --open --limit 1   <python>: No module named taskmd        exit 1
python -m taskmd check                   <python>: No module named taskmd        exit 1
./taskmd.sh list --open --limit 1        ./taskmd.sh: No such file or directory  exit 127
command -v taskmd                        (not found)
```

The interpreter's own path is redacted above and nowhere in this record: it is under a home
directory, which is the class the pre-publish check in `CLAUDE.md` exists to catch.

All four lines are the same fact from four sides. The package is not importable because it is in the
plugin's install cache and the adopter is not; the launcher is not reachable because a relative path
to it only exists for someone standing in the plugin folder; and there was no third way in. This is
§1's claim reproduced rather than asserted, and it is the *before* that step 3 is measured against.

### Step 3 — the entry point, and a second defect that had to be fixed for it to work

**Built.** `plugin/bin/taskmd` (POSIX `sh`) and `plugin/bin/taskmd.cmd` (`cmd`/PowerShell), each a
delegate to the launcher one directory up, per **D3**. Neither repeats interpreter discovery. The
POSIX one invokes its target through `sh` rather than executing it, so the delegation does not also
depend on the target's mode bit; `bin/taskmd` itself is recorded in the index as `100755`, which a
`PATH` lookup on a Unix checkout requires.

**Demonstrated, on both platforms.** The plugin subtree was copied to a scratch location outside
this repository, the adopter project of step 1 is somewhere else again, and the *only* thing joining
them is that the copy's `bin/` is on `PATH`. Command typed by bare name, working directory the
adopter project:

```text
taskmd list --open --limit 1    T-001  proposed  -  specify  Write the quarterly summary   exit 0
taskmd check                    OK - 1 task(s), vocabulary valid, references resolve, ...  exit 0
```

Identical output through `bin/taskmd` from `sh` and through `bin/taskmd.cmd` from PowerShell, each
resolved by name from `PATH` — confirmed by asking the shell which file it had found.

**What that does and does not settle.** It is the whole of acceptance criterion 1: the command ran
from a directory that is neither this repository nor the plugin folder, and the output is above. The
one link still not exercised **on this machine** is narrower than step 2's finding suggested — not
the `bin/` mechanism, which is what ran, but the harness's own `PATH` append, which the truncated
shell snapshot recorded in step 2 prevents from arriving. That link is upstream of this plugin and
its shape was read out of the shipped binary in step 2.

**The second defect: `plugin/taskmd.ps1` reports no Python on a machine with three.** The `.cmd`
delegate failed on its first run with the launcher's own `taskmd: no Python found` message. The
cause is not the delegate. `taskmd.ps1` probes each candidate with `-c ""`, and **Windows PowerShell
5.1 drops an empty-string argument on its way to a native command**, so Python receives a bare `-c`:

```text
Windows PowerShell 5.1.26100.8972    py -c ""      exit 2   Argument expected for the -c option
                                     py -c "pass"  exit 0
PowerShell 7.6.4                     py -c ""      exit 0
                                     py -c "pass"  exit 0
```

The probe's verdict is "did it run", so exit 2 reads as "not a working interpreter" and every
candidate is rejected. It survived because this project drives the launcher from PowerShell 7 and
5.1 is what a stock Windows machine has — the same shape as
[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md)'s finding, a thing that worked
only where it had been tested. It breaks the contributor path too: `.\plugin\taskmd.ps1` from
`powershell.exe` in a fresh clone reports the same.

`-c "pass"` still executes nothing and still exits 49 on the Store stub, so the probe's original
purpose is intact. With it, the `.cmd` entry point produces the output shown above.

### Step 4 — one form, and where it had to be named

`taskmd` for the adopter and `./plugin/taskmd.sh` for this repository, which is **D2** unchanged.
The plan's step 4 named two files; four more turned out to name a command, and each was decided
rather than swept up:

| File | Now names | Why |
| :--- | :--- | :--- |
| `plugin/skills/taskmd/SKILL.md` | `taskmd` | planned output |
| `plugin/skills/taskmd/adopt.md` | `taskmd` | planned output |
| `plugin/docs/bindings/local-markdown.md` | `taskmd` | ships in the plugin and `SKILL.md` routes the agent to it before any write, so it is a command the skill names — one step removed |
| `tasks/README.md` preamble | `./plugin/taskmd.sh` | this repository's own, and since T-053 the form it carried does not run without `PYTHONPATH` |
| `tasks/_templates/task-template.md` | `./plugin/taskmd.sh` | same, and it is copied into every new task |
| `plugin/taskmd/cli.py` — `usage:` | unchanged | **not a substitution**; raised as [T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) |

`SKILL.md`'s line about running the launcher from a subdirectory went with it: `taskmd` is on `PATH`
everywhere, and the project is already found by walking up (T-011), so the sentence now says that
rather than naming a second command form.

**The binding's own instruction was then run, not just edited.** In the scratch adopter project, the
default config was copied to `.taskmd/config.md` per `adopt.md` §2 and `after_write` set to the form
the binding now documents:

```text
taskmd index    Wrote tasks/README.md - 1 active, 0 closed
                Hook   taskmd check
                  OK - 1 task(s), vocabulary valid, references resolve, no broken links
```

So the hook resolves `taskmd` through `PATH` the same way a person does, and the binding does not
need a different form from the one the skill names.

### Step 5 — the suite and this repository

```text
114 passed
OK - 54 task(s), vocabulary valid, references resolve, no broken links
Wrote tasks/README.md - 21 active, 33 closed
```

**Run the suite with no `PYTHONPATH` set.** The tests put the package on `sys.path` themselves, and
a *relative* `PYTHONPATH` in the environment makes `test_the_shell_launcher_produces_what_the_module
_produces` fail spuriously — the launcher prepends its own absolute directory and the resulting list
does not survive the trip to a native Python. It looks exactly like a regression in the launcher.

**Decisions & assumptions**

- **The 5.1 launcher defect is fixed inside this task rather than deferred.** — It is pre-existing
  and strictly speaking outside the plan, but without it this task's own planned output does not
  work on Windows at all, so under METHOD §3.3 it changes what this task must produce rather than
  being a separate concern. *Rejected: a child task plus an honest gap at `review`* — it would ship
  a `.cmd` entry point known not to work. *Rejected: making the `.cmd` prefer `pwsh`* — it leaves
  stock Windows broken and does not help the contributor path. **Decided by the maintainer,
  2026-08-08**, with the diagnosis and the one-token fix put to them. — 2026-08-08
- **`plugin/taskmd.sh` keeps `-c ""`.** — No POSIX shell drops an empty argument, so there is
  nothing to fix there, and changing it for symmetry would make two files differ from what each
  actually needs. The asymmetry is explained in `taskmd.ps1` where a reader meets it. — 2026-08-08
- **The binding document is in scope; the `usage:` string is not.** — The binding ships in the
  plugin and the skill routes to it, so it names commands for the same audience and the same fix
  applies. The `usage:` line is printed by one process to whoever ran it and cannot tell an adopter
  from a contributor, which **D2** made two different people on purpose — a choice, not a
  substitution. *Rejected: deciding it here* — it would settle a D2-adjacent question inside
  `implement`. **Decided by the maintainer, 2026-08-08.** — 2026-08-08
- **Assumption, recorded as one: an adopter's `PATH` stays under the snapshot cap.** — Step 2 found
  this machine's `PATH` too long for the shell snapshot to survive, which is why the harness's
  append cannot be watched here. Nothing in this task depends on the threshold, and the work
  survives being wrong about it: the entry point is unchanged either way, only the demonstration
  route differs. — 2026-08-08

**Outputs produced**
- `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd` — the entry point, mode `100755` on the first
- `plugin/taskmd.ps1` — the interpreter probe, fixed for Windows PowerShell 5.1
- `plugin/skills/taskmd/SKILL.md`, `plugin/skills/taskmd/adopt.md`,
  `plugin/docs/bindings/local-markdown.md` — the command they name
- `tasks/README.md` preamble, `tasks/_templates/task-template.md` — this repository's own form
- [T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) — raised under METHOD §3.3

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | (implement complete) | Steps 1 and 3–5 taken; `implement` is finished and `review` is **not** started (METHOD §3.1 — the handoff's "then review" is a pointer, not a request). Step 1 reproduced §1's claim from four sides in a scratch project outside this repository: the module is not importable, the launcher is not reachable by a relative path, and there was no third way in. Step 3 built `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd` as delegates to the launchers per D3, and **acceptance criterion 1 is met on both platforms** — plugin copied outside the repository, adopter project elsewhere again, nothing joining them but `PATH`, command typed by bare name. The gap step 2 predicted turns out narrower than expected: what cannot be watched here is not the `bin/` mechanism, which ran, but the harness's own `PATH` append, which this machine's truncated snapshot prevents. Step 3 also uncovered a **second, pre-existing defect**: `plugin/taskmd.ps1` probes interpreters with `-c ""`, and Windows PowerShell 5.1 drops empty-string arguments to native commands, so Python gets a bare `-c`, exits 2, and every interpreter on the machine is reported missing. It broke the new `.cmd` entry point and breaks `.\plugin\taskmd.ps1` for any contributor on stock Windows; it survived because this project drives the launcher from PowerShell 7. Maintainer decided to fix it here rather than defer, since without it this task's own output does not work on Windows. Step 4 found four naming sites beyond the plan's two: the shipped binding document moved to `taskmd` (the skill routes to it, so it is one step removed from a command the skill names), this repository's index preamble and task template moved to `./plugin/taskmd.sh` (they carried a form that stopped running at T-053), and the CLI's own `usage:` string was left alone and raised as **T-055**, because D2 made the two audiences different on purpose and a usage line cannot tell which one it is printing to. The binding's instruction was then run rather than only edited — `after_write: taskmd check` resolves through `PATH` in the scratch project. Suite 114 passed, `check` OK on 54 tasks, index regenerated. |
| 2026-08-08 | → in_progress | Step 2 taken, and **D1 is answered yes** — the opposite of what the probe alone said. The probe was a clean negative (no plugin `bin` on `PATH`, `taskmd-probe` not found), but reading further inverted it: `getEnabledPluginBinPaths` **is** called, from the shell-snapshot builder, which appends every enabled plugin's `bin` to the login `PATH` and writes it as one `export PATH=` line for the agent's shell to source. So D1's two candidate explanations were both false. What is broken is the snapshot **file**: its `PATH` line is truncated mid-value at a fixed 5551 characters, leaving an unmatched quote, so sourcing dies on `unexpected EOF` and the shell silently keeps its inherited `PATH` — the plugin `bin` is written correctly and never loaded. Confirmed by sourcing the newest snapshot in a subshell and watching the entry count not move. The cap is a property of **this machine's long `PATH`**, not of the mechanism: the oldest snapshot here is 2064 characters with matched quotes and sources fine, while every later one is the same 5551 across differing contents. Stated as a hypothesis, unbisected, because it needs a second machine and changes nothing this task builds. Maintainer decided to proceed rather than fall back to D4, which would have swapped what the plugin ships on the strength of a defect that is not in the plugin. Accepted consequence, named: this repository cannot dogfood the shipped entry point. The truncation is an upstream harness bug and is deliberately **not** a task here — taskmd cannot fix it and such a task would never close. No `PATH` listing is quoted anywhere in the record; it is the home-directory class the pre-publish check exists to catch. |
| 2026-08-08 | → planned | Plan written; §1's open question settled as **D2** — this repository keeps typing `./plugin/taskmd.sh` and the skill names the `bin/` command, because a contributor has the tree and no install while an adopter has an install and no tree, and typing the shipped command here would make it missing for anyone who merely cloned. The plan's own finding is **D1**: §1 calls the `bin/` mechanism "already established" and that overstates the read. `getEnabledPluginBinPaths` is in the shipped binary with exactly the described body, but no plugin `bin` directory is on a live session's `PATH` with this plugin installed and enabled, and creating one mid-session did not add it — so whether anything *calls* it is open, and steps 3–5 assume an answer this session cannot obtain, `PATH` being fixed before the first turn. A probe was planted in the install cache so a later session settles it with one command. |
| 2026-08-08 | → proposed | Raised from T-053's restructure and **not caused by it**: the same hole predates the move and was hidden by this repository being the only place the plugin had ever run. Every command `SKILL.md` and `adopt.md` name — `python -m taskmd …` — fails for an adopter, because the package is in the install cache and their working directory is their own project. `critical` because it is not a rough edge in the adoption path but the adoption path not working at all, and T-006 would publish it as-is; `s` because the mechanism is already known. Read out of the shipped binary during T-053: the harness puts `<plugin-root>/bin` on `PATH` for every enabled plugin, so a `bin/` entry point is a command an adopter can type from anywhere with no install step and no `PYTHONPATH`. The open question is whether this repository should then type that same command, which proves it continuously but is only on `PATH` when the plugin is installed — the T-052 shape, where a thing works only where it was tested. |
