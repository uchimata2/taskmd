---
id: T-144
title: Decide whether a command's own options can be discovered from the CLI
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-022, T-029, T-087, T-113]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: []
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
- [ ] If the answer is no, T-029's record carries the new evidence and why it did not move the ruling,
      so this is not re-raised by the next adopter
- [ ] If the answer is yes for `list` only, the line is derived from the same config `parse_filters`
      reads, so it cannot drift from what the filter accepts
- [ ] Nothing restates a flag name in prose that the code does not compute
- [ ] The four `--help` forms T-029 covered still behave as its test asserts, or that test is changed
      deliberately and the change is stated

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

  **What `specify` still owns.** The ruling is narrowed, not implemented: whether four commands
  answering one probe two different ways is acceptable, and what `list --help` prints beyond the
  accepted set, are this task's to settle.

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
| 2026-08-15 | (no change) | **The 2026-08-07 ruling is narrowed to `list` only**, by the project owner on 2026-08-15, answering §1's open question with the evidence T-029 did not have. That is the first acceptance criterion discharged before `specify` starts, which is unusual and is recorded here so review does not go looking for a conversation that has already happened. It authorises no phase of this task. What it settles is the *whether*; the *what* is still `specify`'s, and the rejected alternative is kept in §1 rather than in this row. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T5`, which is real and reproduced and which the reporter could not know was already ruled on — the row is stamped *implementation*, meaning no backlog was read for it. Filed as a `decision` and deliberately **not** as a fix: T-029 §1 carries the owner's answer and its reasoning, so the honest shape is to bring the new evidence back once rather than to build past it. Two things are new since 2026-08-07 and both are recorded in §1: the reader in question is an agent without the skill file rather than a person who mistyped, and the per-command surface the rejection priced already exists and is already printed on misuse, including `list`'s config-derived accepted set. `medium` because the workaround is reading one file and the adopter is not blocked. The adjacent defect the same probe turned up is T-145, kept separate on METHOD §5. |
