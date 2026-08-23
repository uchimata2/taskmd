---
id: T-148
title: Decide whether a caller outside a served skill can find the launcher
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-054, T-099, T-142]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-19
adopter_visible: yes
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
- ~~Is a release gate — a plain script, no session, no `PATH` entry — an adopter case this plugin
  means to support at all?~~ **Answered 2026-08-19: no, and the silence is what gets repaired.**
  taskmd offers no route to the launcher for a process that was never served the skill, and
  `SKILL.md` says so where the fallback is stated, so a gate author can tell at once that the
  sentence is not addressed to them. Committing to such a route was the alternative and was rejected
  for the reason [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) already
  establishes: any route is a promise about the harness's own directory layout, which this project
  does not control, so it would break silently and this project would own the breakage for every
  adopter. The reporter offered *no* as acceptable and it is the answer — what was never acceptable
  is the current silence.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what a route would have to be, from what this project has already observed of the harness's layout, so the *no* rests on a measurement rather than on caution | §3, the rejected answer |
| 2 | The fallback paragraph in `SKILL.md` names the caller it is for, so it stops reading as unconditional | `plugin/skills/taskmd/SKILL.md` |
| 3 | The same answer where a **stranger** with a gate script looks. `SKILL.md` is read by a session, which is precisely not this caller, so the record cannot end there | `README.md` |
| 4 | The *no* becomes a non-goal, so it is answered where "is this supported?" is answered | `docs/SCOPE.md` §4 |
| 5 | Check that nothing written names a path under the harness, since that is the thing this task must not promise | §3 |
| 6 | `check`, `index`, the suite and the publishing gate run | §3 |

## 3. Implement

**Decisions & assumptions**
- **No, and the answer is written in three places** — 2026-08-19, the owner's, in a question round.
  A caller the harness never served is not offered a route to the launcher.
- **The rejected answer is *yes, offer a route*, and the evidence against it is the layout this
  project has already recorded.** [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)
  §3 and [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) §1 both observed
  the same thing: the harness serves the skill from an install-time snapshot under a cache directory
  keyed by **marketplace, then plugin, then version**. A route that named it would therefore break
  on every plugin update, and a route that globbed it is what the adopter had already written and
  came here to replace. So the rejected option is not merely expensive, it does not work — which is
  a stronger reason than the caution [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)
  gives, and it is why the *no* is recorded as a non-goal rather than as a deferral.
- **The answer is not flat, and saying so is the useful half.** There are two install shapes and
  only one has the problem. In the plugin shape the harness owns the directory and no caller can be
  told it. In the copied-skill shape **the adopter chose the directory**, so the launcher has a
  stable path a gate can name — which makes the reporter's case answerable rather than merely
  refused. `README.md` now says which shape to use when something other than an agent runs taskmd.
- **`SKILL.md` alone would have failed criterion 2** — 2026-08-19. That file is read by a session
  the harness served, which is exactly the caller that does not have this problem. Writing the
  answer only there would have put it where the affected reader never looks, so `README.md` and
  `docs/SCOPE.md` §4 carry it too.

**The route that does exist, run rather than described.** From a plain shell with nothing of this
plugin on `PATH` — which is the gate author's situation minus the session:

```text
$ command -v taskmd
not on PATH
$ sh plugin/skills/taskmd/taskmd.sh check --root .
OK - 195 task(s), 975 field value(s), 3287 front-matter value(s), ...
$ echo $?
0
```

That is the copied-skill shape's command, and it is the one `README.md` now points a gate author at.

**Nothing written here names a path the harness owns**, checked rather than intended. A sweep of
every tracked document for a plugin cache path returns **two** files, both task records
([T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md),
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)), and both **observe** the
layout rather than promise it. None of the three documents changed by this task names one.

**`README.md` carries no em or en dash**, and the publishing gate covers it — the paragraph added
there was written to that constraint rather than corrected into it afterwards. `test_publishing.py`
passes, 14 tests.

**Outputs produced**
- `plugin/skills/taskmd/SKILL.md`
- `README.md`
- `docs/SCOPE.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision says whether a caller outside a served skill is supported, in one sentence a stranger can act on | met | `README.md`: *If something other than an agent runs taskmd, use this shape.* It tells the reader what to do, not only what is refused |
| It is written where such a caller looks, not only in this task record | met | Three places, and the reasoning for each is in §3. `SKILL.md` alone would have missed the reader entirely |
| If the answer is no, the fallback paragraph names the caller it is for, so nobody reads it as unconditional again | met | `SKILL.md`'s fallback now opens *That paragraph is addressed to you — a session the harness told where this skill lives — and to nobody else* |
| If the answer is yes, the route is demonstrated from a process with no `bin/` on `PATH` and no served skill directory | **not applicable** | The answer is no. Recorded as inapplicable rather than ticked: nothing was demonstrated because nothing was promised. The route that *does* exist, for the other install shape, is run in §3 anyway |
| Nothing written prescribes a cache layout the harness owns | met | Swept rather than asserted: two tracked documents name such a path, both task records, both observing. None of this task's three outputs does |
| The rejected answer is recorded with the evidence for it, not summarised away | met | §3's second decision. The evidence is this project's own observation that the cache path is version-keyed, which makes the rejected route break on every update rather than merely cost something |
| `check` and the suite are green | met | `check` clean, 307 passed with no skips, publishing gate 14 passed. Quoted in §3 and in the Log |

Six criteria met, one recorded as not applicable, no child raised.

**One thing worth carrying.** The task was framed as *is this caller supported?* and the answerable
question turned out to be *which of the two install shapes is this caller using?* — the plugin shape
cannot help them and the copied-skill shape always could. A flat *no* would have satisfied every
criterion above and left the reporter exactly where they started.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | Six criteria met, one recorded **not applicable** because the answer is no, no child raised. **Authorisation (METHOD §3.1):** the owner's grant of 2026-08-19 covering T-194, T-189, T-148, T-131 and T-181, full lifecycle. `specify` needed no new agreement — the owner answered its question the same day. **The *no* is recorded as a non-goal rather than a deferral**, because the rejected route does not merely cost something: the cache path this project has twice observed is keyed by version, so a named route breaks on every update and a globbed one is what the adopter already had. **The framing moved during the work**: there are two install shapes, and the copied-skill one always had a nameable path, so the reporter has an answer rather than only a refusal. `SKILL.md` alone would have failed criterion 2 — it is read by a session, which is the one caller without this problem. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round: no.** A session-less caller is out of scope, and the deliverable is the sentence in `SKILL.md` that says so; offering such a caller a route was rejected on [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)'s grounds. This is the question the backlog-wide round of 2026-08-19 skipped and the handoff of that date recorded as still owed; it is no longer owed. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-15 | → proposed | Raised from the htmldeck reporter's follow-up of 2026-08-15, which recorded it as an unranked observation and not a request. Raised rather than absorbed because it is actionable and outside every open task: T-099 shipped the fallback and is closed, T-142 owns the launcher comment one level down, and neither covers who the fallback is addressed to. `medium` because nobody is blocked — their cache glob works and is now correct — and because what is wrong is a silence a reader fills in wrongly. `s` because the outcome is one sentence in a shipped file plus, if the answer is no, a non-goal; deciding which sentence is the work. The likely answer is that a gate script is out of scope, and that is a result, not a dismissal: it is what stops the next adopter re-deriving a locator against a directory layout this project does not own. |
