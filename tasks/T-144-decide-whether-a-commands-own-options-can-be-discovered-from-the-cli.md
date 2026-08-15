---
id: T-144
title: Decide whether a command's own options can be discovered from the CLI
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-022, T-029, T-087, T-113, T-149]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-144 — Decide whether a command's own options can be discovered from the CLI

## 1. Specify

**Outcome**
The project owner's 2026-08-07 rejection of per-command help is either confirmed against evidence it
did not have, or narrowed to the one command that carries options — and either way the record says
which, so the next report of this does not re-open a settled question.

**Why this one**
Raised from the htmldeck adopter report, row `O-T5`. **This is a decision that already exists**, and
the report was written without knowing that: `check --help`, `list --help` and `context --help` all
print the top-level usage line by design, ruled on by the project owner in
[T-029](T-029-reject-unknown-arguments-on-every-command.md) §1. Their reason goes past the wording —
the goal is a lightweight tool, and if it is difficult enough to use that detailed help is needed,
that is a reason to stop the project rather than to write the help. The alternative was named and
rejected: discoverability for someone who mistyped is real, and it is bought with a second surface
that drifts the first time a flag changes.

So this task exists to weigh new evidence against a recorded rejection, not to reverse it. Reproduced
2026-08-15, unchanged:

```
taskmd list --help      -> exit 0, usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd context --help   -> exit 0, usage: taskmd {check,context,index,list} [args] [--root PATH]
```

**What the report adds that 2026-08-07 did not have.** The rejection was argued about *someone who
mistyped*. The adopter's case is a different reader: an agent that has the command and not the skill
file. `--open`, `--closed`, `--limit`, `--json` and the `--<field> V` form exist only in `SKILL.md`
and in `cli.py`'s module docstring, so that caller reads a whole source file to learn what a flag is
called. That is a context-economy cost, which is the axis the tool is otherwise optimised on, and it
lands on the one command the report cares about.

**And one fact undercuts the *second surface* half of the rejection.** The surface already exists on
both sides. `usage_line(command)` derives a per-command line from the `ARGUMENTS` table and is
already printed on misuse; and `list`, which is absent from that table on purpose because its flags
are the project's vocabulary read at run time, **already computes and prints its accepted set** —
`taskmd list --wat x` answers with every filter this project accepts. So the material a per-command
help would show is derived, printed, and tested today. What is missing is not a surface; it is a
route to it that does not require getting something wrong first.

**What does not change.** The owner's stronger reason — that needing detailed help is evidence
against the tool's premise — is untouched by any of this, and it may still govern. Three of the four
commands take no options at all, so a per-command line for them would restate the top-level one,
which is `docs/SCOPE.md` §2 principle 3 and the reason the rejection was general.

**Requirements served**
R-17, R-18 (`docs/SCOPE.md`); §1 *Invisibility* — with the adopter's reading of it, that a surface an
agent can only learn by reading source is not invisible.

**Scope**
- In: whether `<command> --help` answers for the command named, and if so for which commands.
- In: whether `list` is a special case, since it is the only command with options and the only one
  whose options are configuration rather than code.
- Out: adding any flag or command. `docs/SCOPE.md` non-goal 11 stands.
- Out: the exit code and the unknown-command interaction, which is
  [T-145](T-145-stop-help-answering-for-a-command-that-does-not-exist.md).
- Out: reversing T-029 by preference. Evidence licenses re-opening a rejection; it does not reverse
  one, and if the owner confirms it the outcome is the confirmation written down.
- Out: what `check`, `index` and `context` print for any probe. The narrowing is to `list`, and the
  three that take no options keep the line they have.
- Out: extending [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md)'s
  prose-list check to cover the flags. That task ruled the flags out because they were "not a set
  anything else states"; if this one gives them a computed home, that ceases to be true and the check
  becomes cheap — which is a new task, raised when the home exists, not a widening of this one.

**Inputs**
- [T-029](T-029-reject-unknown-arguments-on-every-command.md) §1 open question, §3 decision 3, and the
  comment in `cli.py` that carries the ruling.
- `plugin/skills/taskmd/taskmd/cli.py` — `ARGUMENTS`, `usage_line`, `parse_filters`.
- [T-022](T-022-filtered-task-listing-for-scripts.md) — why `list` validates its own arguments.
- [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) — the accepted set, derived from the
  project's config rather than written down.

**Acceptance criteria**
- [ ] The owner's 2026-08-07 ruling is put to them again **with the evidence it did not have**, once,
      and their answer is recorded where a reader of T-029 will find it
- [ ] T-029's record carries the narrowing and the evidence that moved it, so a reader who finds the
      2026-08-07 rejection there does not act on a ruling that no longer covers `list`
- [ ] **`list --help` prints no option name the code does not compute.** Shown both ways by a test
      that fails if either side gains a name the other lacks: every option the help prints is one
      `parse_filters` accepts, and every option `parse_filters` accepts is printed
- [ ] **No command's `--help` contradicts another's**: the top-level usage line is in all four
      outputs, and `list` adds to it rather than replacing it
- [ ] The four forms T-029's test covers — `--help`, `-h`, `check --help`, `context --help` — still
      pass that test **unchanged**, verified by running it rather than by reading it
- [ ] `list --help` exits 0 and writes nothing to disk

**Open questions**
- ~~**Is `list` separable from the other three?**~~ **Answered by the project owner on 2026-08-15:
  yes — narrow the 2026-08-07 ruling to `list` only.** The evidence put to them was the two counts in
  *Why this one*: the reader is an agent without the skill file rather than a person who mistyped, and
  the per-command surface the rejection priced already exists and is already printed on misuse.
  `list` answers `--help` from the same config `parse_filters` reads; `check`, `index` and `context`
  keep the top-level line.

  *Rejected: confirm the 2026-08-07 ruling unchanged.* It is the stronger-looking answer, because the
  owner's reason — that needing detailed help is evidence against the tool's premise — is untouched by
  anything in the adopter report, and because three of the four commands would restate the top-level
  line, which is `docs/SCOPE.md` §2 principle 3. What decided it against: `list` is the one command
  where help restates nothing. Its content is computed from the project's own config at run time and
  is already printed when a caller gets something wrong, so the *second surface that drifts* cost the
  rejection was bought with does not exist for this command.

- ~~**Is it acceptable that four commands answer one probe two different ways?**~~ **Answered
  2026-08-15: the question dissolves, because `list --help` is a superset rather than a different
  answer.** Every command's `--help` prints the top-level usage line, and `list` alone appends what
  that line's `[args]` hides for it. So nothing a caller learns from one command is contradicted by
  another, and the asymmetry that remains is in the commands themselves — three take no options, one
  does — rather than in how they answer.

  *Rejected: `list --help` replaces the top-level line with its own.* It is the conventional shape and
  reads better in isolation. What decided it against: it makes the probe genuinely inconsistent, so an
  agent that probed `check --help` first has been told something false about `list`. That is the
  adopter's own failure re-created one command over, and the superset costs one line to avoid.

  *Rejected: give all four commands their own line, from `usage_line(command)`, which already
  derives one.* It is the cheapest code and the most consistent surface. What decided it against:
  for `check`, `index` and `context` that line restates the top-level one with the alternatives
  removed, which is `docs/SCOPE.md` §2 principle 3, and it is most of what the project owner
  rejected on 2026-08-07. Nothing in the adopter report is evidence about those three.

- ~~**What does `list --help` print beyond the accepted set?**~~ **Answered 2026-08-15: every option
  `parse_filters` accepts, computed from `parse_filters`' own knowledge rather than written beside
  it.** The accepted set alone would under-answer the report: `--open`, `--closed`, `--limit` and
  `--json` are four of the five flags it names as reachable only by reading source, and they are
  *code* rather than configuration, so `filter_names` does not know them. They are also already
  discoverable the wrong way round — `list --wat x` names the filters — so a route that added only
  those would add a route and no content.

  *Rejected: print a hand-written usage line for `list`, as the module docstring already carries.*
  It is one string and no restructuring. What decided it against: that string is exactly the second
  home the 2026-08-07 rejection priced, and it is the one this task's §1 argued does not exist yet.
  Writing it would make the argument false in the act of using it.

  *Rejected: print the filters only, and leave the four code flags to the docstring.* Smallest change,
  and it keeps `list`'s help entirely derived from the config. What decided it against: it answers a
  question nobody asked. The report's reader is an agent that has the command and not the skill file;
  `--limit` is the flag that reader needs most and the one this answer withholds.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Capture what the five probes print and exit today — `--help`, `check --help`, `index --help`, `context --help`, `list --help` — before touching anything. | The five captures, pasted into §3 as the *before* |
| 2 | Give `list`'s **code** options one home in `cli.py` that `parse_filters` reads for its literals, rather than a second table beside them. This is the step that can invalidate the rest: the four are not one shape — `--json` is a bare switch, `--open`/`--closed` are two spellings of one option, `--limit` takes a validated value. | A table in `cli.py`, and a `parse_filters` that carries no option literal of its own |
| 3 | Render `list`'s help from that table plus `filter_names(schema)`, top-level usage line first so the output is a superset. | A function in `cli.py` returning the help text |
| 4 | Route the probe: `main` sends `--help` to that function when the command is `list`, and leaves the other three on the line they print now. | `list --help` exits 0 with the new text; the other three byte-identical to step 1's capture |
| 5 | Test both directions of the derivation, and re-run T-029's own test unchanged. | Tests in `tests/test_cli.py`, and the T-029 test's result pasted into §3 |
| 6 | Record the narrowing where a reader of the 2026-08-07 rejection meets it. | An annotation in `tasks/T-029-reject-unknown-arguments-on-every-command.md` |
| 7 | Raise the follow-on T-134 declined: its prose-list check can now cover the flags, because step 2 gives them the computed home it said they lacked. | A new task file in `tasks/` |

**Shape of the one home — decided, and step 2's to confirm.** A module-level table keyed by flag,
carrying each option's placeholder and how it is consumed; `parse_filters` tests membership against
it and the help renders it.

*Rejected: keep the literals in `parse_filters` and share only a tuple of names with the help.* Least
disruptive. What decided it against: the placeholder — `N` for `--limit` — is the half a caller needs
and the half a name-only tuple cannot carry, so the help would still hand-write `[--limit N]`.

*Rejected: derive the help by calling `parse_filters` in a describe mode.* Perfectly single-homed, no
new table. What decided it against: it makes the parser's control flow the documentation format, so
every later change to either has to be made without disturbing the other.

**Promised outputs**

- plugin/skills/taskmd/taskmd/cli.py
- tests/test_cli.py
- tasks/T-029-reject-unknown-arguments-on-every-command.md
- one new task file in tasks/, for step 7

## 3. Implement

**Reproduced first, per R-16.** Before any change, at `72b9dc6`:

```
taskmd --help          -> exit 0, usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd check --help    -> exit 0, the same line
taskmd index --help    -> exit 0, the same line
taskmd context --help  -> exit 0, the same line
taskmd list --help     -> exit 0, the same line
```

Five probes, one answer. The last line is the defect: `list` has four options and a project's worth
of filters, and the line a caller is given states none of them.

**Decisions & assumptions**
- **The one home is a four-column table, `LIST_OPTIONS`** — 2026-08-15. Flag, value placeholder,
  the option it sets, and the value a switch sets. `parse_filters` recognises a flag by looking it up
  there and carries no option literal of its own; `list_options_line` renders the same rows. The two
  alternatives are priced in §2 and both leave the placeholder — `--limit`'s `N` — written where the
  parser cannot see it.
- **`--limit`'s numeric check stays written as `--limit`'s** — 2026-08-15. It is the only valued
  option. Describing validation in the table too would be the small configuration language §2
  rejected, bought for a second option nobody has asked for.
- **`list --help` prints the top-level line first** — 2026-08-15, and this is what dissolved §1's
  first question rather than answering it. The output is a superset, so no command contradicts
  another and an agent that probed `check --help` first has been told nothing false.
- **It exits 0 with no project too** — 2026-08-15. The filters need a config, so where none loads the
  two usage lines still print and the line about filters says so. *Asking a tool what it does is not
  misuse* is T-029's own finding, and making it conditional on the working directory would have
  reintroduced it one condition over. Reached by `--root` at a folder that is not a project; the
  degraded branch is proven, not assumed.
- **`ARGUMENTS` is untouched** — 2026-08-15. `list` is absent from it deliberately, and it drives
  `main`'s arity gate: adding a row would reject every real `list` call. So `list`'s usage line is
  rendered separately rather than by `usage_line(command)`, which is why the two look alike and are
  not the same code.

**Verified by use.** After the change:

```
taskmd --help / -h / check --help / index --help / context --help
                       -> exit 0, usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd list --help     -> exit 0
   usage: taskmd {check,context,index,list} [args] [--root PATH]
   usage: taskmd list [--open] [--closed] [--limit N] [--json] [--<field> <value>] [--root PATH]
   filters: --blocked_by, --blocks, --business_value, --children, --effort, --owner, --parent,
            --phase, --related, --status, --type, --work_package
taskmd list --help --root <a folder that is not a project>
                       -> exit 0, the two usage lines, and "filters: --<field> <value>, named by
                          the project's own config; run this inside a project to have them listed"
```

**Shown failing, per R-16.** Three tests, each broken on purpose and the failure read:

```
LIST_OPTIONS[:3] in the renderer   -> test_every_option_the_parser_takes_is_printed
                                      AssertionError: '--json' not found in '...'
a hand-written [--verbose] in the
  rendered line                    -> test_every_option_it_prints_is_one_the_parser_takes
                                      AssertionError: 'unknown filter' unexpectedly found in
                                      'unknown filter: --verbose. This project accepts: ...'
if arg == "--verbose": continue
  added to parse_filters           -> test_the_parser_carries_no_option_name_of_its_own
```

The third test was added because the first two are only as good as the claim that `LIST_OPTIONS` *is*
the parser's accepted set — a branch added by hand would be accepted, unprinted, and invisible to
both. It reads the parser's source for a standalone option literal and finds none.

```
261 passed, 8 subtests passed
OK - 149 task(s), ... (taskmd check, exit 0)
```

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `LIST_OPTIONS`, `accepted_filters`, `list_options_line`,
  `list_help`, a `parse_filters` with no option literal, and the `main` help branch.
- `tests/test_cli.py` — `ListSaysWhatItAccepts`, six tests.
- `tasks/T-029-reject-unknown-arguments-on-every-command.md` — two annotations and a log row.
- `tasks/T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The 2026-08-07 ruling put to the owner once, with the evidence it did not have, and the answer recorded where a reader of T-029 finds it | met | Answered 2026-08-15 and recorded in §1; T-029 §1 carries the annotation pointing here. |
| T-029 carries the narrowing and the evidence that moved it | met | Two annotations, at §1's answer and §3's third decision, because both read as present tense. Neither original was edited (METHOD §1 rule 5). |
| `list --help` prints no option name the code does not compute, shown both ways | met | `test_every_option_the_parser_takes_is_printed` and `test_every_option_it_prints_is_one_the_parser_takes`, each shown failing. `test_the_parser_carries_no_option_name_of_its_own` is what makes the pair valid. |
| No command's `--help` contradicts another's | met | `test_it_adds_to_the_top_level_line_rather_than_replacing_it` asserts the top-level line is inside `list`'s output and is the whole of the other three's. |
| T-029's four forms still pass that test unchanged | met | `1 passed` — run on its own, and the test file's assertion is untouched. |
| `list --help` exits 0 and writes nothing to disk | met | `test_it_writes_nothing` compares the tree of a project with no index before and after; `test_it_answers_outside_a_project_too` pins the exit code where no config loads. |

**Beyond the written criteria**
- The rejection message and the help now render the accepted filters through one function,
  `accepted_filters`, so the caller who mistyped and the caller who asked are answered in the same
  words. That was not a criterion and is the change's one incidental improvement.
- `--limit`'s two rejection messages are now built from the flag as typed rather than from a literal
  `--limit`. Byte-identical for the only flag that reaches them; it stops being a literal, which is
  what the third test polices.

**Child fix tasks raised**
- [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md) — the
  prose copies of these flags in `cli.py`'s docstring and in `SKILL.md` are now checkable against
  `LIST_OPTIONS`, which is the reason T-134 gave for leaving them out.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → done | **`review` closed.** Six criteria, six met, each against a run rather than a reading; the table is in §4. Nothing was deferred and no criterion needed a child task. The two things worth a later reader's time are in §4 *Beyond the written criteria*, and neither was asked for: the rejection message and the help now share one rendering of the accepted filters, and `--limit`'s messages stopped carrying a literal flag name. |
| 2026-08-15 | → in_progress | **`implement` done, all seven steps.** Step 2 held — the four options do share a home, with one exception recorded as a decision rather than smuggled: `--limit`'s numeric check stays written as its own, because generalising it is the configuration language §2 rejected. Two things the plan did not foresee. `ARGUMENTS` cannot take a `list` row, since it drives `main`'s arity gate and would reject every real call, so `list`'s usage line is rendered separately — which is why it resembles `usage_line(command)` and is not it. And the help needs the project's config, which `--help` was otherwise answered without, so a folder that is not a project would have turned exit 0 into exit 2 — the finding T-029 exists for, one condition over; the degraded branch is proven by `--root`, not assumed. Step 7 raised [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md). A sixth test was added beyond the plan, because the two bidirectional ones are only as good as the claim that `LIST_OPTIONS` is the parser's accepted set. |
| 2026-08-15 | → planned | **`plan` written**, seven steps. Step 2 is placed second rather than first because it is the one that can invalidate the rest — the four code options are not one shape, and if they cannot share a home without becoming a small config language, steps 3–5 are the wrong steps and the honest outcome is a narrower one. Step 1 is a capture rather than preparation: three of the four commands must print in step 4 exactly what they print now, and "unchanged" cannot be judged against a remembered baseline. The shape of the one home is decided in §2 with two alternatives priced, both rejected on the same ground — they leave the caller-facing half of an option (`--limit`'s `N`) written somewhere the parser does not read. |
| 2026-08-15 | → specified | **`specify` closed.** Both questions §1 held open are answered there with their rejected alternatives, under the standing delegation for decisions of this size; neither needed the owner, because the *whether* was already theirs and settled and these two are the *what*. The first dissolved rather than resolving: making `list --help` a **superset** of the top-level line means no command answers the probe differently, so the acceptability question had no subject left. The second is the one with teeth — `list --help` must name the four code flags, not only the config-derived filters, and naming them in a printed string is the second home the 2026-08-07 rejection priced. So the criterion is bidirectional and the burden lands on `implement`: give the options one home that both `parse_filters` and the help read. Two criteria were dropped as unjudgeable branches (*if the answer is no* / *if yes*), the ruling having already been made. |
| 2026-08-15 | (no change) | **Authorisation (METHOD §3.1): the maintainer asked for this task to be taken through its full lifecycle**, given on 2026-08-15 as the subject of a handoff. It covers T-144 and reaches no other task. Written here on 2026-08-15 because the handoff was until now its only home, which is the thing §3.1 says not to do — an authorisation kept anywhere but the task's own record is one a later session can miss or stretch. Nothing has been started under it: the task is still at `proposed`, and this row records the permission, not any phase of the work. |
| 2026-08-15 | (no change) | **The 2026-08-07 ruling is narrowed to `list` only**, by the project owner on 2026-08-15, answering §1's open question with the evidence T-029 did not have. That is the first acceptance criterion discharged before `specify` starts, which is unusual and is recorded here so review does not go looking for a conversation that has already happened. It authorises no phase of this task. What it settles is the *whether*; the *what* is still `specify`'s, and the rejected alternative is kept in §1 rather than in this row. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T5`, which is real and reproduced and which the reporter could not know was already ruled on — the row is stamped *implementation*, meaning no backlog was read for it. Filed as a `decision` and deliberately **not** as a fix: T-029 §1 carries the owner's answer and its reasoning, so the honest shape is to bring the new evidence back once rather than to build past it. Two things are new since 2026-08-07 and both are recorded in §1: the reader in question is an agent without the skill file rather than a person who mistyped, and the per-command surface the rejection priced already exists and is already printed on misuse, including `list`'s config-derived accepted set. `medium` because the workaround is reading one file and the adopter is not blocked. The adjacent defect the same probe turned up is T-145, kept separate on METHOD §5. |
