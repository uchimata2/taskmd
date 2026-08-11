---
id: T-113
title: Name an unknown filter before complaining it has no value
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-022, T-029]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-10
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_list.py]
---

# T-113 — Name an unknown filter before complaining it has no value

## 1. Specify

**Outcome**
`list` tells a caller that a flag is not one it accepts, whether or not that flag was given a value.
The message that names the project's own vocabulary is reached by the misspelling that actually
happens, not only by the one that happens to be well-formed.

**Why this one**
Found by [T-029](T-029-reject-unknown-arguments-on-every-command.md) while building a probe that
every command had to refuse. `list` checks the *shape* of an argument before its *name*:

```
taskmd list --definitely-not-a-flag value
unknown filter: --definitely-not-a-flag. This project accepts: --blocked_by, --blocks, ...

taskmd list --definitely-not-a-flag
--definitely-not-a-flag needs a value
```

The second is the more likely typing — a flag remembered wrongly and typed alone, or a boolean flag
that is not one — and it is the one told nothing useful. "Needs a value" invites the reader to
supply one, which produces the *other* error; the message actively points away from the answer.

**Not what T-029 fixed.** That task made three commands reject what they had been discarding, and
recorded `list` as the model to follow because it refuses before printing and names the project's own
values. Both remain true. This is one branch inside that refusal taken in the wrong order, and it is
raised rather than fixed there because a finding is not fixed where it is found (METHOD §5).

**Scope**
- In: the order of the two tests in `parse_filters` — an unrecognised name is unrecognised whether or
  not a value follows it.
- Out: the wording of either message, and which filters exist. Both are settled.
- Out: `--help` and the three commands' arity, which are T-029's and are done.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `parse_filters`.
- [T-022](T-022-filtered-task-listing-for-scripts.md) — where the rejection behaviour was built, and
  the rule that a rejection arrives before any output.

**Acceptance criteria**
- [ ] `list --<unknown>` with no value names the flag as unknown and lists what the project accepts
- [ ] `list --<unknown> value` is unchanged
- [ ] A *known* filter given no value still says it needs one — the missing-value message is not
      removed, only reached second
- [ ] Shown failing first, since the second criterion passes today

**Open questions**
- None.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the failing test: `list --<unknown>` with no value must name the flag as unknown and print what the project accepts. | A new case in `tests/test_list.py`'s `RejectsWhatItCannotAnswer`, failing on the current order with the "needs a value" message. |
| 2 | Recognise the name before demanding a value in `parse_filters` — `limit` included, since it is accepted but is not in `filter_names`. | `plugin/skills/taskmd/taskmd/cli.py` `parse_filters`, with the unknown-name test lifted above the missing-value test. |
| 3 | Pin the branch the reorder must not break: a *known* filter with no value, and `--limit` with no value, both still say they need one. | Two more cases in the same class, passing before and after. |
| 4 | Correct T-029's probe docstring, which records the old ordering as the reason it passes a value. | `tests/test_cli.py` `test_every_command_rejects_an_argument_it_does_not_understand`. |
| 5 | Run the four affected modules and `check`/`index`. | Recorded output in §3. |

## 3. Implement

**Decisions & assumptions**
- `limit` is recognised by the new name check as well as by the branch below it — 2026-08-11. The
  reorder is two lines only if `known` is the whole accepted set, and it is not: `filter_names`
  builds from vocabularies, links and the two view keys, so `--limit` is absent from it and was
  reaching its own branch *after* the name check it would now fail. Hoisting the name test without
  `name != "limit"` would have made `list --limit 1` an unknown filter — invisible to both of the
  criteria above, since each uses a real filter. `test_limit_with_no_value_still_says_so` is what
  holds it, and it is the reason step 3 exists.
- The messages are unchanged, both wording and code — 2026-08-11. Scope puts wording out, so the
  edit moves a block and widens one condition; no string was touched.

**Evidence**

Run against this repository, not a fixture. The unknown flag, typed alone, now reaches the message
that names the vocabulary:

```
$ taskmd list --definitely-not-a-flag
exit 2
unknown filter: --definitely_not_a_flag. This project accepts: --blocked_by, --blocks,
--business_value, --children, --effort, --owner, --parent, --phase, --related, --status, --type,
--work_package

$ taskmd list --status
exit 2
--status needs a value

$ taskmd list --limit
exit 2
--limit needs a value
```

Shown failing first, as the fourth criterion requires — before the edit, on the same command:

```
AssertionError: 'unknown filter' not found in '--wat needs a value\n'
```

`check` exit 0 on 119 tasks; index regenerated (16 active, 103 closed). Suite per module, one
process each: `test_list` 32, `test_cli` 89, `test_schema` 46, `test_budget` 5 green; `test_runtime`
25 plus 2 subtests, with four failures, all in `Launchers` and all environmental
([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)) —
`test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has`,
`test_the_shell_launcher_produces_what_the_module_produces`, and
`test_every_entry_point_produces_what_the_module_produces` twice, for `skills/taskmd/taskmd.sh` and
`bin/taskmd`. Named rather than counted, and there is no fifth.

Six `test_cli` failures appeared mid-run and were **not** a regression: editing this file left the
index stale, which T-025 made `check` report and every repository-level test then failed on. One
`index` cleared all six. The tool caught it on the project using it, which is what it is for.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `list --<unknown>` with no value names the flag as unknown and lists what the project accepts | met | `test_an_unknown_filter_name_is_reported_without_a_value`, and the run above. |
| `list --<unknown> value` is unchanged | met | `test_an_unknown_filter_name_is_reported`, untouched and still passing. Byte-identical output to the old order — see the note below on what the spec's quote got wrong. |
| A *known* filter given no value still says it needs one | met | `test_a_known_filter_with_no_value_still_says_so`, plus `test_limit_with_no_value_still_says_so` for the accepted-but-not-a-filter case the criterion does not mention. |
| Shown failing first, since the second criterion passes today | met | The assertion error is quoted in §3. The two guard cases passed before the edit as well, which is what makes them guards. |

**One thing the spec had wrong.** Its quoted output shows `unknown filter: --definitely-not-a-flag`,
with hyphens. The tool prints `--definitely_not_a_flag`: `parse_filters` normalises the name before
any message uses it, and did so under the old order too. So the quote was idealised rather than
copied, and the second criterion is met against what the command actually printed, not against the
illustration. Left as written per METHOD rule 5 — the record's account of the past is annotated, not
rewritten. Whether echoing a flag the caller did not type is itself worth fixing is
[T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md), raised rather than settled here
because this task's scope puts the wording of both messages out.

**Child fix tasks raised**
- none. [T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md) is a sibling, not a child: no
  criterion here is unmet, and it is a pre-existing behaviour this task only made visible.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met, evidence in §3. Raised [T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md) for the one thing found outside scope — the rejection quotes a normalised flag rather than the typed one, which is how the spec's own quote came to be wrong. |
| 2026-08-11 | → planned | Full-lifecycle authorization, given by the maintainer on 2026-08-11 when resuming: run every open `v0.2` task through specify → plan → implement → review automatically, one at a time. It covers that set and nothing outside it (METHOD §3.1). `specify` needed no owner turn: the criteria were already written and the open-questions list was empty. The spec's target was re-checked before planning against it — `parse_filters` is live at `cli.py:859` and still tests shape before name, so this task did not sleep through a move the way T-035 had. |
| 2026-08-10 | → proposed | Surfaced by T-029's derived probe: a test written to prove all four commands refuse an unknown argument found that one of them refuses it for the wrong reason. Sized `xs`/`medium` — a two-line reordering, on the command whose whole purpose is being scripted against. `v0.2` by T-110's rule (a minor correction, holding nothing up). |
