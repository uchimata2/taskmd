---
id: T-100
title: Report a project config that has drifted from the shipped default
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-001, T-023, T-088, T-095]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/schema.py, plugin/skills/taskmd/taskmd/cli.py, plugin/skills/taskmd/taskmd/defaults/config.md, tests/test_cli.py, README.md]
adopter_visible: yes
---

# T-100 — Report a project config that has drifted from the shipped default

## 1. Specify

**Outcome**
A project that copied the shipped schema and then fell behind it is told so, by a command it already
runs — so a schema improvement reaches the projects that pinned before it existed.

**Why this one**
Raised as **R-2** by the first adopting project (`control/LOCAL-CONTEXT.md`). It copied the shipped
default to `.taskmd/config.md` on 2026-08-09 — correctly, since a config *replaces* the default
rather than merging with it. taskmd added `audit` to the `type` vocabulary the same day
([T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md)). The project
could not see that, and raised a task to "fix" a template for naming a type the schema lacked — **a
defect that had stopped existing.** It was caught a day later only because somebody opened the
plugin's shipped default by hand and compared the two.

So the cost is not a stale value. It is a task specified against a false premise, whose planned fix
would have edited a valid field to satisfy a constraint that no longer existed.

**The replace-not-merge rule is right and this does not reopen it.**
`plugin/skills/taskmd/taskmd/defaults/config.md` argues it twice — every key must be written, because
a silently absent key would hand you a schema you did not write. Drift is the accepted price of that
rule. What is being asked for is a **report**, not a merge: a project that pinned deliberately reads
the line and ignores it; a project that pinned and forgot gets told.

**Both files are already parsed**, so the comparison costs a walk of two dictionaries and no new
input.

**Requirements served**
R-11 (`docs/SCOPE.md`) — the schema is configuration, which is what makes a shipped default something
a project can fall behind. R-17, since this is a fact about the config that surfaces once rather than
inside a task somebody is trying to finish.

**Scope**
- In: whether `check` gains a drift line, and what counts as drift — a missing key, an extra
  vocabulary value, a row the default has since changed.
- In: whether a project that pinned on purpose can say so, and where. A line nobody can silence is a
  line everybody learns to skip.
- In: what the line says. R-2's suggested shape names the row and the difference:
  `CONFIG DRIFT  type: shipped default adds 'audit'; this project's row does not carry it`.
- Out: merging a project config with the default, at read time or at any other time. That is the rule
  above, and it is not this task's to change.
- Out: a `config` command. `docs/SCOPE.md` non-goal 11 keeps the CLI to four, so if this is reported
  it is reported by `check` — the same constraint T-032 works under.
- Out: telling a project its config is *wrong*. Drift is not an error; the default is a default.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the shipped default, and its own argument for
  replace-not-merge.
- `plugin/skills/taskmd/taskmd/schema.py` — where both files are already read.
- [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md), the change
  that went unseen, and its note that two independent projects reached for `audit`.

**Acceptance criteria**
- [ ] Shown failing first, per R-16: a project config missing a value the shipped default carries
      produces the line, demonstrated on a fixture
- [ ] A project whose config matches the default produces nothing, and a project with no config of
      its own produces nothing
- [ ] The line names the key and the difference, not merely that a difference exists — a report that
      sends the reader to diff two files by hand is the thing that already happened
- [ ] Whether a drift line changes the exit status is decided and recorded with its alternative
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- None. **Q1 — is drift a problem or an advisory? — answered by the maintainer, 2026-08-10:
  advisory, reported with the exit status unchanged.** A pinned config is legal, and a validator that
  fails on a legal state is one a project starts passing flags to. *Rejected: a counted problem* — it
  guarantees the line is seen, and guarantees a project that pinned deliberately can never have a
  clean run again.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what a new config key would cost, since the silencing question in §1 assumes one is available | **D2**, below — settled by reading `_require` |
| 2 | Write the comparison and the advisory line | `plugin/skills/taskmd/taskmd/schema.py`, `plugin/skills/taskmd/taskmd/cli.py` |
| 3 | **Run it on the real corpus** — the reporting project's own config, and the same file reconstructed as it stood the day the failure happened | A recorded transcript, and the rule's shape either confirmed or narrowed by what it says |
| 4 | Write the rule where a config's own rules live, and trim the code to point at it | `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 5 | Tests, including the silent cases, shown against unmodified `HEAD` | `tests/test_cli.py` |
| 6 | Update anything that quotes `check`'s output literally | `README.md` |
| 7 | Suite, `index`, `check`, pre-publish check | Recorded output |

Step 3 is the step that decides the design rather than confirming it, which is why it is third and
not last: a rule that fires on a config someone wrote on purpose is noise, and the only way to find
out is to run it on one. Step 1 is first because §1's *In* scope asks whether a project can silence
the line, and the answer changes shape entirely depending on whether a key can be added at all.

**Shape decisions.**

**D1 — Drift is one shape only: a vocabulary row the project still keeps, missing a value the shipped
default has since gained.** Everything else a config does is a choice rather than a lag — extra
values, extra rows, renamed fields, and every front-matter setting, which is what a config exists to
change. *Rejected: report any difference* — the corpus says why in §3.

**D2 — There is no key to switch it off, and this is a constraint rather than a preference.**
`schema._require` raises on a *missing* config key, because a config replaces the default rather than
merging with it. So adding any key to the shipped default invalidates every existing project's config
on upgrade. The silencing question in §1 therefore has no cheap answer, and the one taken is that a
project which pinned deliberately reads one line naming exactly what it decided not to have.
*Rejected: an optional key with a default* — "optional" is precisely what `_require` exists to forbid,
and carving out an exception would hand a project a schema it did not write.

**D3 — The comparison reports its own reach, as a counted noun.** `check` prints `N vocabulary
row(s)`, which is 0 for a project with no config of its own. That case is vacuous — a project using
the default cannot be behind it — but a comparison that reads nothing must not be indistinguishable
from one that read everything and found nothing, which is the failure T-034, T-080 and T-095 were
each raised for. The number is what tells the two apart.

**Planned outputs**
- `plugin/skills/taskmd/taskmd/schema.py` — `drift_from_default`
- `plugin/skills/taskmd/taskmd/cli.py` — `check_config_drift` and the advisory register
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the rule
- `tests/test_cli.py`, `README.md`

## 3. Implement

### Step 3 — the corpus, which is what settled D1

The reporting project's own `.taskmd/config.md` was copied into a scratch project and run against,
in two states. **As it stands today:**

```text
OK - 5 vocabulary row(s), 0 task(s), ... , 1 document(s), 0 link(s)
```

Silent. Five rows compared and nothing to say — because that project has since added `audit` itself.
**The same file with `audit` removed from the `type` row**, which is the state it was in on
2026-08-09 when the failure happened:

```text
CONFIG DRIFT  type: shipped default adds 'audit'; this project's row does not carry it
```

One line, and it is R-2's suggested wording almost to the word.

**The corpus is what rejected the wider rule.** That config also carries a `work_package` vocabulary
row the shipped default has never had, and its front-matter is identical to the default's. A rule
reporting *any* difference would therefore have printed a line about `work_package` on every run,
from the first — a deliberate addition reported as a lag. So the one-directional, values-only rule in
**D1** is not a matter of taste: it is the only shape that is silent on a config someone maintained
and loud on one they forgot.

### Steps 1–2, 4 — the change

`drift_from_default` compares; `check_config_drift` appends to an advisory register that prints on
both the passing and the failing branch, for the same reason `Scope` does — a legal-but-stale config
hides behind a run that found real problems exactly as well as behind a clean one.

The rule itself is written **once**, in the shipped config under *When this file moves ahead of
yours*, beside the replace-not-merge rule it is the consequence of. Both functions carry a pointer
and no restatement, which is the arrangement `## Ordering` already uses.

### Step 5 — the tests, and an honest note about which of them prove anything

Seven tests. On unmodified `HEAD`:

```text
Ran 7 tests                                                        FAILED (failures=3)
```

**Only three fail, and the four that pass do so vacuously** — they assert *silence* (a current copy,
an extra value, an extra row, a deleted row), and `HEAD` is silent about everything. They are guards
against a future rule that grows teeth, not evidence for this one. Said plainly because a 7-test
class reported as "shown failing first" would otherwise claim four times the proof it has.

The three that fail are the three that matter: the named line, the reach count, and the zero count
for a project with no config.

### Steps 6–7 — the output that changed, and the suite

`README.md` quotes `check`'s output literally, and that sample gained `0 vocabulary row(s)`; the
README also now says the line exists and points at the config for the rule. It was the only literal
sample in the tracked tree outside task records, which was checked rather than assumed.

```text
Ran 161 tests in 6.270s                                                                      OK
OK - 106 task(s), 530 field value(s), 326 reference(s), 22 dependency edge(s), 139 declared
     output(s), 1 index file(s), 134 document(s), 1011 link(s), 0 vocabulary row(s)
```

The `check` line is the run taken **after** this record and its child task were written, so the
figures are ones a later reader can reproduce.

This repository's own count is **0** and correctly so: it has no `.taskmd/config.md` and runs on the
shipped default.

**Decisions & assumptions**

- **The advisory prints on a failing run too.** — Same argument as the `Scope` line, which T-095
  settled: a fact that only appears on clean runs is missing from every run where somebody is already
  looking at output. — 2026-08-10
- **Front-matter values are never compared, not even the ones that look like defaults.** — `id_width`
  or `tasks_dir` differing is the config doing its job. There is no way to tell a stale value from a
  chosen one there, and D1's shape works only because a *missing member of a list the project still
  maintains* is a signature that a chosen value is not. — 2026-08-10
- **Assumption, recorded as one: the shipped default only ever gains vocabulary values.** — If a
  value were ever *removed* from the default, a project carrying it would be told nothing, which is
  right under D1 and would matter if the default ever narrowed. It never has, and the work survives
  being wrong: the omission is a silence, not a false report. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/taskmd/schema.py` — `drift_from_default`
- `plugin/skills/taskmd/taskmd/cli.py` — `check_config_drift`, the advisory register
- `plugin/skills/taskmd/taskmd/defaults/config.md` — *When this file moves ahead of yours*
- `tests/test_cli.py` — `APinnedConfigIsToldWhenTheDefaultMovesOn`, seven tests
- `README.md` — the sample output, and one paragraph naming the line

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Shown failing first, per R-16: a project config missing a value the shipped default carries produces the line, demonstrated on a fixture | met | §3 step 5 on a scratch project, and §3 step 3 on something better than a fixture — the actual config that reported this, reconstructed into the state it was in on the day. |
| A project whose config matches the default produces nothing, and a project with no config of its own produces nothing | met | Both tested, and the second is also this repository on every run. §3 step 5 states plainly that these two pass on `HEAD` as well, so they are guards rather than evidence. |
| The line names the key and the difference, not merely that a difference exists — a report that sends the reader to diff two files by hand is the thing that already happened | met | `type: shipped default adds 'audit'; this project's row does not carry it`. |
| Whether a drift line changes the exit status is decided and recorded with its alternative | met | Q1, answered by the maintainer: advisory. Recorded with the rejected alternative in §1, asserted by `test_it_is_advisory_and_does_not_move_the_exit_status`, and written into the shipped config so an adopter meets it too. |
| The suite still passes and `check` is clean on this repository | met | `Ran 161 tests … OK` — seven more than before — and `check` OK on 105 tasks. |

**What was found and not fixed.** **D2**: no key can be added to the shipped config without
invalidating every existing project's config, because a missing key is an error by design. That is a
real constraint on every future schema change, not just this one, and it is currently written down
only as a consequence of two rules stated separately. Raised as
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) rather than fixed here, per METHOD
§3.3 and §5's rule against fixing a finding where it is found.

**Child fix tasks raised**
- [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) — the shipped config cannot gain a
  key without breaking every project that wrote one.

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Reviewed against the five criteria as written; **all five met, none carried**, so the task closes. One child raised and not fixed here: [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md), for **D2** — the shipped config cannot gain a key without invalidating every project that wrote one, which is a constraint on every future schema change and not this task's to absorb. Criterion 2's note says plainly that its two tests pass on `HEAD` as well, so a reader is not told the class was "shown failing first" seven times when it was three. `deliverables` names the five files. Pre-publish check run last, after this record was written: **190 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All seven steps taken. **Step 3 is the one that earned its place in the plan**: the rule was run against the reporting project's real config before its shape was fixed, and the corpus rejected the wider design — that config carries a `work_package` vocabulary row the shipped default has never had, so a rule reporting *any* difference would have printed a line about a deliberate addition on every run since the day it was written. What ships is silent on that file today and prints exactly one line on the same file reconstructed as it stood on 2026-08-09, which is R-2's wording almost to the word. **D2** was settled first, by reading `_require`: no key can be added to silence the line, so a project that pinned deliberately reads one line naming what it decided not to have. **D3** gives the comparison a counted noun, so a walk that read nothing is distinguishable from one that read everything and found nothing — the failure T-034, T-080 and T-095 were each raised for. Tests seven, of which only three fail on `HEAD`; the four that pass assert silence and are guards rather than evidence, and the record says so. `README.md` was the only literal sample of `check` output in the tracked tree outside task records, checked rather than assumed. Suite `Ran 161 tests … OK`. |
| 2026-08-10 | → planned | Plan written; Q1 answered by the maintainer — **advisory, exit status unchanged** — with the rejected alternative recorded, and the whole of that argument is that a validator which fails on a legal state is one a project starts passing flags to. The plan's own finding is **D2**, put first as a step because §1's scope asked whether a project could silence the line and the answer changes the shape of everything after it. Step 3 is placed third rather than last on purpose: running the candidate rule on a config someone actually maintains is what *decides* the design, not what confirms it. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"keep going with T-100, advisory as you recommend, full lifecycle"*, which also answered Q1. It covers this task alone and **does not generalise**; it is the second such waiver in this session, after the one covering T-099 and T-102. Recorded here for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) exists. |
| 2026-08-10 | → proposed | Raised as R-2 from the first adopting project's recommendations. `high` because the failure is not a stale value but a task specified against a false premise — the project raised work to fix a defect that had already been fixed upstream, and would have edited a valid field to satisfy a constraint that no longer existed; it was caught by accident. `s` because both files are already parsed and the comparison is a walk of two dictionaries. Recorded here so `specify` does not relitigate it: the replace-not-merge rule is deliberate and argued twice in the shipped default, drift is its accepted price, and what is asked for is a report rather than a merge. Non-goal 11 rules out the `config --diff` verb R-2 offered as an alternative, so `check` is the only surface. |
