---
id: T-055
title: Settle what the tool calls itself when it prints its own usage
type: fix
status: done
phase: review
parent: T-054
blocked_by: []
related: [T-054, T-029]
work_package: v0.1
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-08
updated: 2026-08-09
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-055 — Settle what the tool calls itself when it prints its own usage

## 1. Specify

**Outcome**
Someone who mistypes a command is told how to retype it in a form they can actually run.

**Why this one**
Raised from [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3, which fixed
every place the *documentation* names a command and deliberately left this one, because it is not a
substitution.

`plugin/taskmd/cli.py` prints `usage: python -m taskmd {check,context,index}` on a bad argument,
and names the same form in its module docstring. That is the form T-054 established **nobody can
type**: an adopter has the package in an install cache and no `PYTHONPATH`, and a contributor in a
clone needs `PYTHONPATH` set. So the tool's own error message is the last place still naming it.

**Why it is not simply a substitution.** T-054 **D2** decided the two audiences type different
things on purpose — an adopter types `taskmd`, which the harness puts on `PATH`; a contributor types
`./plugin/taskmd.sh`, which works in a clone with nothing installed. A usage line is printed by one
process to whoever happened to run it, and **it cannot know which of the two it is talking to**.
Every answer therefore gives up something, which is why this needs deciding rather than editing.

**Requirements served**
**R-18** (`docs/SCOPE.md`) — the same one T-054 serves, at the one surface T-054 left: a message
telling you to run something unrunnable is the "clone runs unedited" promise failing at the moment
the user is already stuck. Also `docs/SCOPE.md` §1 *Invisibility*.

**Scope**
- In: what `usage:` names, and the same question for the module docstring in `plugin/taskmd/cli.py`
  and `plugin/taskmd/__main__.py`.
- In: whether the answer is one fixed string, or derived from how the process was actually invoked.
- Out: adding, renaming or removing a command — the surface is settled.
- Out: `python -m taskmd.schema` in `plugin/taskmd/schema.py`, which is
  [T-030](T-030-settle-the-schema-module-s-own-entry-point.md)'s question, not this one.

**Inputs**
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §2 **D2** — why the two
  audiences differ, and why that was chosen rather than unified.
- `plugin/taskmd/cli.py` — the usage string and the module docstring.
- [T-029](T-029-reject-unknown-arguments-on-every-command.md) — which made the usage line something
  users actually reach, by rejecting unknown arguments instead of ignoring them.

**Acceptance criteria**
- [ ] A bad argument, run through the shipped `bin/` entry point from a directory that is not this
      repository, prints a command line that **can be copied and run as printed** — demonstrated by
      copying it and running it, not by reading it
- [ ] The record says which audience was chosen over the other and why, the tool having been shown
      unable to tell them apart
- [ ] The module docstrings are **decided rather than left** — either changed with the usage line, or
      recorded as deliberately unchanged with the reason
- [ ] The usage line and the command the skill names cannot drift apart unnoticed, and the guard is
      shown **failing** on the text as it stands today
- [ ] The suite still passes and `check` is still clean on this repository

**Open questions**
- None. **The question this task was raised on is answered, and the answer is no.** `sys.argv[0]`
  does not distinguish the audiences, so there is nothing to derive and the choice is forced.
  Measured rather than reasoned: a probe printing `argv[0]` was run through all three routes — the
  shipped `bin/taskmd`, `./plugin/taskmd.sh`, and `python -m taskmd` directly — and every one
  reported `-m` at package-import time and `__main__.py` by the time the CLI runs. They are
  **identical**, and the reason is structural: T-054 **D3** made `bin/taskmd` a delegate rather than
  a second implementation, so every route funnels into the same `python -m taskmd`. The decision that
  kept interpreter discovery in one place is the same one that erased the information a derivation
  would have needed. *Rejected: an environment variable set by each entry point* — it would put the
  command's name into `bin/taskmd`, `bin/taskmd.cmd` and both launchers, which is four copies of the
  string this task exists to have one of, and it would make deleting a launcher change the tool's
  output. *Rejected: inferring the audience from where the package sits* (a git work tree versus an
  install cache) — that is a guess about the user dressed as a fact.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish how many strings are actually user-facing, by finding what the tool prints as against what only a source reader sees | The answer in §3, and with it whether the docstrings are part of the change or part of the record |
| 2 | Write the guard tying the usage line to the command the skill names, and run it against the text as it stands | The guard **failing**, output in §3 |
| 3 | Change the usage line | the string in `plugin/taskmd/cli.py` |
| 4 | Demonstrate the result by **copying the printed line and running it**, from a directory that is not this repository | The transcript in §3 — the mistake, the advice, and the advice taken |
| 5 | Re-run the suite and `check` | Recorded output in §3 |

Step 1 is first because it sizes the change: `specify` decided the docstrings are in scope as a
question, and the answer turns on whether anything prints them. Step 2 is before step 3 for the same
reason it was in T-056 — a guard written after the change passes on its first run and proves nothing.

**Shape decisions.**

**D1 — The usage line names `taskmd`, the adopter's form.** Forced, `specify` having shown the tool
cannot tell the two apart. The argument for choosing this side is that the two audiences are not
comparable in size: **one repository** has contributors who type `./plugin/taskmd.sh`, and every
other user of this tool for the rest of its life is an adopter who types `taskmd`. A usage line is
read at the moment someone has already made a mistake, and the person who needs telling is the one
without the source tree — a contributor who just typed `./plugin/taskmd.sh` knows what they typed.
*Rejected: naming `python -m taskmd`* — the status quo, and correct for nobody: it needs `PYTHONPATH`
in a clone and is unreachable from an install. *Rejected: naming no program at all*
(`usage: {check,context,…}`) — honest about the ambiguity, but it answers the question the reader
actually has with silence. *Rejected: printing both forms* — two lines of error message to serve a
handful of people who already know the answer.

**D2 — The docstrings keep `python -m taskmd`, and that is a decision rather than an omission.**
They describe the **module**, to someone who is reading the module, and `python -m taskmd` is
literally how this module is entered; `taskmd` is how a wrapper is entered that then enters it.
Changing them would make them less accurate about the thing they document, not more. The usage line
goes the other way because it addresses a **user**, not a reader of the source. *Rejected: changing
them for consistency* — consistency between two texts with different subjects is not a virtue.

**D3 — The guard derives the expected name from `SKILL.md` rather than hard-coding it.** What is
worth pinning is not the literal string `taskmd` but the property T-054 found broken: the tool and
the skill naming different things. Hard-coding would put a third copy of the name in the tests;
deriving leaves two and asserts they agree. *Rejected: asserting the literal* — cheaper to write and
it guards the weaker claim.

**Planned outputs**
- `plugin/taskmd/cli.py` — the usage string
- `tests/test_cli.py` — the guard

## 3. Implement

### Step 1 — two user-facing strings, not one, and no docstring among them

**The docstrings are never printed.** Nothing in the package refers to `__doc__` at all; the only
matches are the compiled constants inside `__pycache__`. So **D2** is confirmed by measurement
rather than assumed: they are read from the source or not at all, which is the whole of the reason
they keep `python -m taskmd`.

**`--help` is not a third string.** It falls through the same branch as an unknown command and
prints the same line, so there was one top-level message to change, not two.

**But there were two usage strings, not one** — and the second is the reason this step exists:

```text
cli.py:578   usage: python -m taskmd {check,context,index,list} [args] [--root PATH]
cli.py:129   usage: context <id>
```

The second is printed when `context` is given no id. It names **no program at all**, so it was
un-runnable for exactly the same reason as the first and by the opposite mistake — one named a form
nobody could type, the other named nothing to type. The plan's step 3 said "the string" in the
singular; step 1's job was to size the change, and it sized it at two. Both are inside the agreed
outcome — *someone who mistypes a command is told how to retype it in a form they can actually run*
— so this is the step doing its work rather than the scope moving.

### Step 2 — the guard, failing before the change

```text
FAILED tests/test_cli.py::Usage::test_every_usage_line_names_the_command_the_skill_names
AssertionError: 'taskmd' != 'python'
 : no command: 'usage: python -m taskmd {check,context,index,list} [args] [--root PATH]\n'
```

`'taskmd'` there is not written in the test: it was read out of `SKILL.md`'s first `bash` block,
which is **D3** working — the assertion is that the tool and the skill name the same command, not
that either names a particular word.

### Step 3 — the change

Both strings now open with `taskmd`. The top-level one carries a comment saying why it is not
derived, because "why is this hard-coded" is the first question a later reader will have and the
answer — every route ends in `python -m taskmd`, so `argv[0]` is identical — is not visible from
where they will be standing.

### Step 4 — the advice, taken literally

In the adopter project, with the plugin installed outside this repository and reached only through
`PATH`. The printed line is not read and retyped; it is extracted mechanically from the output and
executed, because a line a human retypes charitably is not a line that has been shown to work:

```text
$ taskmd lst
usage: taskmd {check,context,index,list} [args] [--root PATH]
$ taskmd check
OK - 1 task(s), vocabulary valid, references resolve, no broken links          exit 0

$ taskmd context
usage: taskmd context <id>
$ taskmd context T-001
T-001  Write the quarterly summary
status proposed | phase specify | type deliverable | ...
```

Both messages are now advice that can be followed, which is criterion 1 by use rather than by
inspection.

### Step 5 — the suite and this repository

```text
116 passed
OK - 56 task(s), vocabulary valid, references resolve, no broken links
```

115 before, 116 after: the guard is the one addition.

**Decisions & assumptions**

- **The `context` sub-usage is changed too, and the plan's singular wording is not a reason to leave
  it.** — It fails the task's stated outcome in the same way as the top-level line, and `specify`
  put "what `usage:` names" in scope without qualifying which one. Raising it as a separate task
  would have split one string's worth of work across two records for the sake of a word in a plan
  written before step 1 had counted them. — 2026-08-09
- **The docstrings stay, now on evidence rather than on argument.** — **D2** reasoned they were
  source-facing; step 1 confirmed nothing prints them. Had that come out the other way, D2 would
  have been wrong and the change larger, which is why the step was first. — 2026-08-09
- **The guard reads `SKILL.md` and will break if that file stops opening with a `bash` block.** —
  Accepted deliberately: it fails with "SKILL.md no longer opens its first command in a bash block",
  which names the cause. A test that silently stopped checking would be worse than one that
  complains about a reformat. *Rejected: asserting the literal `taskmd`* — a third copy of the
  name, and it would guard the weaker claim. — 2026-08-09

**Outputs produced**
- `plugin/taskmd/cli.py` — both usage strings
- `tests/test_cli.py` — `test_every_usage_line_names_the_command_the_skill_names`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A bad argument, run through the shipped `bin/` entry point from a directory that is not this repository, prints a command line that **can be copied and run as printed** — demonstrated by copying it and running it, not by reading it | met | §3 step 4, in the adopter project with the plugin outside this repository and reached only through `PATH`. The printed line was extracted mechanically from the output and executed rather than retyped, so no charity was applied on the way. Both messages were put through it: `taskmd lst` → `taskmd check` → `OK`, and `taskmd context` → `taskmd context T-001` → the task. |
| The record says which audience was chosen over the other and why, the tool having been shown unable to tell them apart | met | **D1** chooses the adopter and gives the asymmetry as the reason — one repository has contributors who type `./plugin/taskmd.sh`; everyone else who ever uses this tool is an adopter. That the tool cannot tell them apart is measured, not argued: §1's answered question records `argv[0]` identical across all three routes, and why — T-054 **D3** made `bin/taskmd` a delegate, so every route funnels into the same `python -m taskmd`. |
| The module docstrings are **decided rather than left** — either changed with the usage line, or recorded as deliberately unchanged with the reason | met | Unchanged, and **D2** says why: they describe the module to someone reading the module, and `python -m taskmd` is literally how it is entered. Step 1 turned that from an argument into a finding — nothing in the package refers to `__doc__`, so no docstring reaches a user. |
| The usage line and the command the skill names cannot drift apart unnoticed, and the guard is shown **failing** on the text as it stands today | met | §3 step 2, run before the change: `AssertionError: 'taskmd' != 'python'`. The expected name is read out of `SKILL.md`'s first `bash` block, so what is pinned is that the tool and the skill agree — the property T-054 found broken — rather than a particular word. Both usage strings are covered. |
| The suite still passes and `check` is still clean on this repository | met | `116 passed` — 115 before, the guard being the one addition — and `OK - 56 task(s), vocabulary valid, references resolve, no broken links`. |

**One thing this leaves standing, deliberately.** A contributor in a clone who mistypes is now shown
`usage: taskmd …`, which is not what they should type — `./plugin/taskmd.sh` is. That is **D1
accepted rather than overlooked**: the tool cannot distinguish them, so one audience had to be
chosen, and this is the cost of choosing the larger one. No task is raised for it, because there is
nothing anyone could do about it without re-opening D1 — and the day this repository stops being the
only clone in the world is the day the choice stops costing anything.

**Child fix tasks raised**
- none

**Verdict.** All five criteria met, none carried. The task closes, and with it the last open child
of [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md).

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met, none carried; the last open child of T-054 closes. Both usage strings now open with `taskmd`, and the demonstration took the printed advice **literally** — extracted from the output and executed rather than retyped — in the adopter project with the plugin outside this repository and only `PATH` joining them. The guard reads the expected name out of `SKILL.md`'s first `bash` block, so what is pinned is that the tool and the skill agree rather than that either says a particular word; it was shown failing first, `'taskmd' != 'python'`. Suite 116 (115 before), `check` OK on 56. The residual is named and accepted rather than carried: a contributor in a clone who mistypes is shown `usage: taskmd …`, which is not what they should type — that is **D1**'s cost, there is nothing to do about it without re-opening D1, and no task is raised for it. |
| 2026-08-09 | → specified → planned → in_progress | Whole lifecycle in one request. **`specify` answered the question this task was raised on, and the answer is no**: `argv[0]` does not distinguish the audiences. Measured, not reasoned — a probe run through all three routes reported `-m` at import time and `__main__.py` by the time the CLI runs, identically every time, because T-054 D3 made `bin/taskmd` a delegate so every route funnels into the same `python -m taskmd`. The decision that kept interpreter discovery in one place is the one that erased the information a derivation needed. With derivation gone the choice was forced, and **D1** takes the adopter's side on asymmetry: one repository has contributors, everyone else who ever uses this tool is an adopter, and a usage line is read by someone who has already made a mistake. `implement` step 1 then found **two** user-facing usage strings rather than one — `context` with no id printed `usage: context <id>`, naming no program at all, un-runnable by the opposite mistake — and confirmed by measurement that no docstring is ever printed, which turned D2 from an argument into a finding. |
| 2026-08-08 | → proposed | Raised from T-054 §3 under METHOD §3.3, as the one naming site that is a decision rather than a substitution. T-054 changed every document that names a command to `taskmd`, the form the harness puts on `PATH`; the tool's own `usage:` line still says `python -m taskmd`, which T-054 established nobody can type. It was left because **D2** deliberately gives the two audiences different commands, and a usage line cannot tell which one it is printing to — so the choice costs something either way. `medium`/`xs` because it is one string in one file, reached only on a mistyped command, but reached exactly when the user is already stuck. The open question is whether `sys.argv[0]` makes "it cannot know" false, which decides whether this is a one-line edit or nothing at all. |
