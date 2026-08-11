---
id: T-134
title: Check that every prose list of the commands names the commands there are
type: fix
status: done
phase: review
parent: T-117
blocked_by: []
related: [T-030, T-031, T-055, T-071, T-073, T-117, T-126]
work_package: v0.5
owner: maintainer
business_value: low
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [tests/test_publishing.py, README.md, plugin/skills/taskmd/taskmd/cli.py]
---

# T-134 — Check that every prose list of the commands names the commands there are

## 1. Specify

**Outcome**
A document listing taskmd's commands and getting the set wrong fails the suite, so
[T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md)'s answer — *distinct
registers, deliberately repeated* — is safe rather than only argued.

**Why this one**
T-117 decided that `README.md` and `cli.py`'s docstring may both list the four commands, because they
say different things about them: purposes against flags, for readers who need one or the other. That
answer holds exactly as long as the two agree about **which** commands exist, and nothing checks
that. `usage_line` is derived from `COMMANDS` ([T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md),
[T-071](T-071-let-the-usage-test-assert-every-command-there-is.md)), so the *usage string* cannot
drift; the two prose lists can.

**It has already happened once.**
[T-073](T-073-correct-the-command-surface-local-context-states.md) is this project carrying a
document that stated a three-command CLI for four days after it was four, and the correction outlived
it in two tracked files. That is the failure this guards, measured rather than imagined.

**Requirements served**
R-1, R-18 (`docs/SCOPE.md`); the design rule, from the other side — a fact allowed two homes needs
the two homes held together by something.

**Scope**
- In: the prose lists in `README.md` and in `plugin/skills/taskmd/taskmd/cli.py`'s module docstring,
  checked against `cli.COMMANDS`.
- In: what the check does about a document that mentions one command in passing, which is not a list.
- Out: reopening T-117. This exists because that answer was chosen, not instead of it.
- Out: the flags. `list`'s options are not a set anything else states, and checking them would be a
  second surface with its own drift.
- Out: `docs/SCOPE.md` non-goal 11 and `CLAUDE.md`, neither of which names a command — T-117 §3
  measured that, and a check aimed at them would be aimed at nothing.

**Inputs**
- [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md) §3, for which documents
  state the surface and which only appear to.
- `tests/test_publishing.py`, for the shape of a test that reads a rule out of a document rather than
  restating it.
- `plugin/skills/taskmd/taskmd/cli.py` — `COMMANDS`, the derived truth.

**Acceptance criteria**
- [ ] A command added to `COMMANDS` and not to `README.md` fails the suite, shown by doing it
- [ ] A command removed from a prose list fails too — the check is a set comparison, not a
      one-directional "everything listed exists"
- [ ] The check does not fire on a document mentioning a command in a sentence, shown on the real
      tree
- [ ] The test names, in its failure, which document is behind and which commands are missing

**Open questions**
- None. **Q1 — how does the check find "a list" in prose? — decided 2026-08-11 under the standing
  delegation: a marked region**, `<!-- taskmd:commands -->`, the idiom the generated index already
  uses. What is checked is declared rather than guessed, and a document that opts in is checked
  whether or not anyone remembered to add it to a list of documents. *Rejected: a heuristic* — "any
  document naming every current command is a list" needs no markup and stops checking a document the
  moment one name drops out of it, which is precisely the failure being guarded. *Also rejected: the
  test naming the two documents* — that list is a third statement of the surface's whereabouts, and
  it goes stale the day a third document starts listing them, which is
  [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md)'s own falsifier.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Mark the two regions | `README.md`, `plugin/skills/taskmd/taskmd/cli.py` |
| 2 | Read the names out of each region with one expression, and compare the **set** against `cli.COMMANDS` in both directions | `tests/test_publishing.py` |
| 3 | Assert the regions exist at all, so the comparison cannot pass on a tree where the markers were deleted | A test |
| 4 | Show it firing three ways: a command added to `COMMANDS`, a command dropped from a list, the markers removed | §3 |
| 5 | Show it staying quiet on a command named in a sentence, on the real tree | A test |
| 6 | Suite, `index`, `check` | §3 |

**Shape decisions.**

**D1 — One expression reads both documents.** README writes `` `taskmd context <id>` `` in a table of
purposes and `cli.py` writes `python -m taskmd context T-002` in a block of invocations; both contain
`taskmd <name>`, so `taskmd\s+([a-z][a-z0-9-]*)` reads either. Two parsers for two registers would
have been a second thing to keep in step, in a task about things not being kept in step.

**D2 — Step 3 is not ceremony.** Without it, deleting a marker makes the region unreadable, the
comparison finds nothing to compare, and every assertion passes. That is the vacuous pass this
project keeps meeting, and it costs one test.

**D3 — The marker goes in `cli.py`'s docstring as an HTML comment, which looks foreign in Python.**
Accepted deliberately: one marker token across both files is worth more than a docstring that reads
slightly better, and the alternative was a second convention for the second file. The cost is two odd
lines in a module docstring.

## 3. Implement

### Steps 1–3, 5 — the check

`<!-- taskmd:commands -->` … `<!-- taskmd:end-commands -->` around the README table and around the
invocation block in `cli.py`'s docstring. Four tests in `tests/test_publishing.py`:

- the regions exist (**D2**);
- each region's set equals `cli.COMMANDS`, compared **both ways**, and the failure names the document,
  what it is missing and what it names that does not exist;
- a command named in a sentence is not a list — checked on the real tree, against the text of
  `README.md` *outside* the region, which mentions commands in an FAQ row and in a paragraph about
  filters. That test asserts its own premise first: if the README ever stops mentioning a command
  outside the region, it says so rather than passing vacuously.

An unclosed region raises rather than being ignored.

### Step 4 — firing, three ways

```text
1. a fifth command added to COMMANDS, listed nowhere
   AssertionError: Items in the first set but not the second:            FAILED

2. a command dropped from the README list
   AssertionError: Items in the first set but not the second:            FAILED

3. markers deleted
   AssertionError: unexpectedly None : README.md carries no taskmd:commands region,
   so nothing checks the list in it                                      FAILED
```

Each mutation was reverted and the suite re-run green. Two directions and the meta-case, which is
criteria 1, 2 and **D2**.

### Step 6

```text
python -m unittest discover -s tests -q     Ran 237 tests     OK (skipped=3)
```

**Decisions & assumptions**

- **`docs/SCOPE.md` and `CLAUDE.md` are not marked**, because T-117 §3 measured that neither names a
  command: one states a bound, the other an invocation route. Marking them would aim a check at
  nothing and imply they are lists. — 2026-08-11
- **The flags are out.** `list`'s options are a second surface with its own drift, and nothing else
  states them. — 2026-08-11

**Outputs produced**
- `tests/test_publishing.py` — `EveryMarkedListNamesTheCommandsThereAre`, four tests
- `README.md`, `plugin/skills/taskmd/taskmd/cli.py` — the marked regions

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A command added to `COMMANDS` and not to `README.md` fails the suite, shown by doing it | met | §3 step 4, case 1. A fifth entry added to the dict and reverted. |
| A command removed from a prose list fails too — a set comparison, not a one-directional check | met | §3 step 4, case 2. The failure message names both directions, and the assertion compares sets rather than testing membership. |
| The check does not fire on a document mentioning a command in a sentence, shown on the real tree | met | The README names commands outside the region in two places and none of it is checked. The test asserts that premise before relying on it, so it cannot become vacuous in silence. |
| The test names, in its failure, which document is behind and which commands are missing | met | *"%s is behind: it does not name %s, and it names %s which do not exist."* |

**Child fix tasks raised**
- none.

**Verdict.** All four criteria met. T-117's answer — two registers, deliberately repeated — is now
held together by something, which is what it was missing.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met, and the check was shown firing **three** ways rather than the two asked for: a fifth command added to `COMMANDS`, a command dropped from the README list, and the markers deleted. The third is **D2** and it is the one worth keeping — without an assertion that the regions exist, deleting a marker leaves nothing to compare and every other assertion passes. Q1 was decided under the standing delegation: a marked region, because a heuristic stops checking a document the moment one name drops out of it, which is the failure being guarded, and a list of documents inside the test is a third statement of the surface's whereabouts. The quiet case is checked on the real tree and asserts its own premise first, so it cannot go vacuous in silence. |
| 2026-08-11 | → in_progress | One expression reads both registers (**D1**), since README's table of purposes and `cli.py`'s block of invocations both write `taskmd <name>`; two parsers would have been a second thing to keep in step inside a task about things not being kept in step. **D3** accepts an HTML comment inside a Python docstring, which reads foreign, in exchange for one marker convention across both files. 237 tests. |
| 2026-08-11 | → specified | Q1 answered under the standing delegation. Criteria unchanged. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised by [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md)'s criterion 3, which asked what would have to be true for its answer to change. One of the two falsifiers has already happened in this project ([T-073](T-073-correct-the-command-surface-local-context-states.md), four days of a document naming a three-command CLI), so it is raised rather than left as a sentence. `low` and `s`: the failure is a wrong front door rather than a broken tool, and the work is one test plus a decision about how a list is recognised. Q1 is left open deliberately — it is a real fork with a cost either way, and answering it inside the task that raised it would be the absorption METHOD §3.3 forbids. |
