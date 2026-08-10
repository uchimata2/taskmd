---
id: T-099
title: Give an adopter a command that runs when the plugin's bin is not on PATH
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-054, T-055, T-067, T-085]
work_package: v0.2
owner: maintainer
business_value: critical
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-099 — Give an adopter a command that runs when the plugin's bin is not on PATH

## 1. Specify

**Outcome**
An adopter whose harness does not put the plugin's `bin/` on `PATH` is told one invocation that
works, in the documents they already read — so they run taskmd instead of writing a launcher of
their own.

**Why this one**
Raised as **R-1** by the first adopting project (`control/LOCAL-CONTEXT.md`), which ranked it the
largest of seven divergences it hit. Every command in taskmd's documentation is `taskmd <verb>`. On
that project's machine the bare name resolves in neither shell, so the project wrote its own 60-line
launcher that finds the newest installed version and runs it. Every command in every task file, every
skill, every project document and every handoff there now reads that shim rather than the documented
command — across roughly forty task files, and **permanently**, because a task record is not rewritten
after the fact.

**This repository already knows the cause and shipped nothing for it.**
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 2 found it: the
harness does append every enabled plugin's `bin` to `PATH`, but it does so by writing one `export
PATH=` line into a shell snapshot, and on a machine with a long `PATH` that line is truncated
mid-value. Sourcing fails, the shell keeps its inherited `PATH`, and the directory is written
correctly and never loaded. T-054 recorded that as an upstream defect and deliberately raised no task
— correctly, since taskmd cannot fix the harness. **What it did not do is give the adopter a second
way in**, and the failure is not rare: it is the same machine class the maintainer develops on.

**The recommended fallback does not run as written.** R-1 proposes
`python <plugin>/skills/taskmd/taskmd/__main__.py <verb>` on the grounds that `__main__.py` already
exists and already walks up to find the project. Run:

```text
python <plugin>/skills/taskmd/taskmd/__main__.py check
ImportError: attempted relative import with no known parent package        exit 1
```

`__main__.py` is `from .cli import main` — a module inside a package, which is why `python -m taskmd`
works and naming the file does not. So this task cannot adopt the recommendation as stated; it has to
choose between making that form work and documenting a different one.

**Requirements served**
R-18 (`docs/SCOPE.md`) — *"the interpreter and the repository root are auto-discovered so a clone runs
unedited"*, which is unmet for anyone whose harness does not deliver the `PATH` entry. Also §1
*Invisibility*: a tool the agent cannot invoke is not invisible, it is absent.

**Scope**
- In: what `plugin/skills/taskmd/SKILL.md` and `plugin/skills/taskmd/adopt.md` say when the bare name
  is not found, and whether the shipped binding says it too.
- In: which fallback form is documented — the launchers by path
  (`plugin/skills/taskmd/taskmd.sh`, `.ps1`), `plugin/bin/taskmd` by path, or `python -m taskmd` with
  the package directory named — and whether one form covers both platforms.
- In: whether `__main__.py` gains a `sys.path` bootstrap so the obvious command works. It is one
  block, and the recommendation shows an adopter reaching for exactly that file.
- Out: fixing the harness. Not taskmd's, and T-054 settled that.
- Out: adding a command. The four exist; this is about reaching them.

**Inputs**
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 steps 2–4, for the
  mechanism, the truncation and the two-audience decision (**D2**) that any answer here must not undo.
- `plugin/skills/taskmd/SKILL.md`, `plugin/skills/taskmd/adopt.md`.
- `plugin/skills/taskmd/taskmd/__main__.py`, `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd`.

**Acceptance criteria**
- [ ] The failure is reproduced first, from a project that is neither this repository nor the plugin
      folder, with no plugin directory on `PATH` — per `CLAUDE.md` *Verifying*
- [ ] The documented fallback is then **run** from that same place, on both platforms, and its output
      recorded
- [ ] `SKILL.md` and `adopt.md` name the same fallback as each other, and say plainly which condition
      it is for
- [ ] The short form stays the primary instruction — an adopter whose `PATH` works types `taskmd`
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- **Can an adopter discover the plugin path at all?** A fallback naming `<plugin>` is not a fallback
  if the person reading it cannot fill the blank. `${CLAUDE_PLUGIN_ROOT}` substitutes into command and
  hook arguments ([T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) D1) but not
  into a Markdown pointer, so the document has to tell them how to find it. Whoever answers this
  should say how, not only that.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Raised as R-1 from the first adopting project's recommendations, which ranked it the largest of its seven divergences. `critical` because the documented command failing is the adoption path not working, which is the same reason T-054 carried that value, and because the cost is permanent — a shim written into forty task records is not retracted later. `s` because nothing new is built; the entry points exist and this is what the documents say when the harness does not deliver the `PATH` entry. Two facts recorded here rather than left for `specify` to rediscover: the cause is known and is upstream (T-054 §3 step 2, a truncated shell-snapshot `PATH` line), and **the recommended command does not run** — `__main__.py` is a package module, so naming the file raises `ImportError: attempted relative import with no known parent package`. Verified by running it. |
