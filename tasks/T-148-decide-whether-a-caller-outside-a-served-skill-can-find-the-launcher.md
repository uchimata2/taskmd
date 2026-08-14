---
id: T-148
title: Decide whether a caller outside a served skill can find the launcher
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-054, T-099, T-142]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-148 — Decide whether a caller outside a served skill can find the launcher

## 1. Specify

**Outcome**
It is settled whether taskmd offers any route to the launcher for a process that was never served the
skill — a release gate, a hook, a plain script — or whether it does not and says so where the
fallback is stated, so an adopter reading *the launcher sits in the skill directory the harness
named* can tell at once whether that sentence is addressed to them.

**Why this one**
Raised from the htmldeck reporter's follow-up of 2026-08-15, recorded there as an observation and
unranked, as everything in that register is. They tried to take the advice this project gave them —
delete the wrappers, use the shipped fallback — and could not. The caller that runs their locator is:

```
python tools/tasks/lint.py
```

a plain script, run by their release gate from any working directory, in a process that was never
served the skill and has no channel to ask for a directory. So their glob over the plugin cache is
not them ignoring the documented route; from outside a served skill it is the only route there is.

**This is not T-099 failing.** [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md)
gave the adopter a second way in and it works, for the caller it was written for: an agent in a
session, told by the harness where the skill directory is. For a process with no session the
mechanism does not degrade — it is absent. Nothing in `SKILL.md` says so, because the paragraph was
written from inside the case it serves.

**The shape is [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md)'s, one
level up.** There, `bin/taskmd` states the `PATH` mechanism as a guarantee on a file that is read
because the guarantee failed. Here, `SKILL.md` states the fallback as the answer to a broken `PATH`,
and the caller with the least claim on `PATH` — a script with no session, no shell profile and no
harness — is the one caller the fallback cannot reach. Both are a mechanism stated as available to a
reader who has just discovered they cannot use it. They are separate tasks because the fix is in a
different file and may go a different way; that they are the same fault twice is the argument for
deciding this one rather than leaving it.

**We told them to do something that cannot be done, which is how this surfaced.** The disposition
comment listed *delete both wrappers* as theirs to act on. One of them is a release-gate locator and
has no route to the fallback; and neither is only a locator — one chains `index`, `check` and a
reference checker and stops at the first failure, so the fallback would have replaced a part of it
rather than all of it. The advice was given from inside the session case too.

**A "no" is a real result here.** The reporter says plainly that a gate script may be outside what
this plugin means to support, and that it is a fine answer. It probably is: a route that survives
harness versions is a promise about someone else's directory layout, which
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) already establishes this
project does not control. What is not an answer is the current silence, which reads as an
unconditional fallback and sends a gate author looking for a directory nobody will hand them.

**Requirements served**
R-18 (`docs/SCOPE.md`) — auto-discovery so a clone runs unedited — in the reading T-099 and T-142
left it: the launcher discovers the interpreter and the project root, and the one thing it cannot
discover is itself.

**Scope**
- In: whether taskmd names any route to the launcher for a caller with no `bin/` on `PATH` and no
  served skill directory, and what such a route would cost to hold.
- In: what the fallback paragraph in `SKILL.md` says about who it is for, whichever way this goes.
- In: whether a *no* belongs in `docs/SCOPE.md` §4 as a non-goal rather than only in this record.
- Out: prescribing a plugin cache layout. That is the harness's and not this project's to promise.
- Out: the harness `PATH` truncation, settled as not taskmd's by T-054.
- Out: the launcher comment, which is T-142 and must not be pre-empted here.
- Out: adding a command, a flag, an environment variable or an install step before the shape is
  decided.

**Inputs**
- The reporter's follow-up on the adopter thread, §3 — the gate invocation, and their statement that
  a gate script may be outside what the plugin supports.
- `plugin/skills/taskmd/SKILL.md`, the fallback paragraph, for what it promises and to whom.
- [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) — what the fallback was
  for, and the caller it was written for.
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 2 — why `PATH`
  cannot be relied on, and what this project decided it does not own.
- `docs/SCOPE.md` R-18 and §4.

**Acceptance criteria**
- [ ] The decision says whether a caller outside a served skill is supported, in one sentence a
      stranger can act on
- [ ] It is written where such a caller looks, not only in this task record
- [ ] If the answer is no, the fallback paragraph names the caller it is for, so nobody reads it as
      unconditional again
- [ ] If the answer is yes, the route is demonstrated from a process with no `bin/` on `PATH` and no
      served skill directory — run, with its output recorded, not described
- [ ] Nothing written prescribes a cache layout the harness owns
- [ ] The rejected answer is recorded with the evidence for it, not summarised away
- [ ] `check` and the suite are green

**Open questions**
- Is a release gate — a plain script, no session, no `PATH` entry — an adopter case this plugin means
  to support at all? — the project owner. The reporter offers *no* as acceptable and it may well be
  right; the answer this task cannot end with is silence.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Raised from the htmldeck reporter's follow-up of 2026-08-15, which recorded it as an unranked observation and not a request. Raised rather than absorbed because it is actionable and outside every open task: T-099 shipped the fallback and is closed, T-142 owns the launcher comment one level down, and neither covers who the fallback is addressed to. `medium` because nobody is blocked — their cache glob works and is now correct — and because what is wrong is a silence a reader fills in wrongly. `s` because the outcome is one sentence in a shipped file plus, if the answer is no, a non-goal; deciding which sentence is the work. The likely answer is that a gate script is out of scope, and that is a result, not a dismissal: it is what stops the next adopter re-deriving a locator against a directory layout this project does not own. |
