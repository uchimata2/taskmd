---
id: T-082
title: Let id_width say that the backend allocates the ids
type: fix
status: done
phase: review
parent: T-004
blocked_by: []
related: [T-075, T-010]
work_package: M2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/schema.py, plugin/skills/taskmd/taskmd/defaults/config.md, plugin/skills/taskmd/docs/bindings/github-issues.md, plugin/skills/taskmd/docs/bindings/local-markdown.md, tests/test_schema.py, tests/fixtures/backend-allocated-ids/.taskmd/config.md, tests/fixtures/README.md]
---

# T-082 — Let id_width say that the backend allocates the ids

## 1. Specify

**Outcome**
A project whose ids are allocated by its backend can write a config that describes them, and
[`github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) stops claiming the identity keys
already do.

**Why this one**
Raised by [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) §3 D3, which decided
the shape and left the change here because T-004 is a `decision` task and this is code and a
document. The binding says:

> the identity keys describe the issue number rather than a chosen format. A project on this
> backend has ids like `#41`; `id_prefix` and `id_width` describe that, they do not impose it.

Since [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md), `is_id` matches the prefix plus
**exactly** `id_width` digits. No value of `id_width` describes `#7` and `#41` in one repository, so
the second half of that sentence is false and the first half is unreachable. T-075 was right for
local files — the width is what makes a mistyped id reportable there — and the two backends want
opposite things from the same key, which is why a value meaning "not applicable" is the fix rather
than a relaxation.

**Why the width check protects nothing on that backend.** An id you cannot invent cannot be
mistyped: on GitHub the number comes back from `create` and is read, never composed. So the rule
that earns its keep locally has nothing to catch there, and enforcing it costs a project the ability
to describe its own ids.

**Scope**
- In: `id_width: none` meaning "the backend allocates these; impose no width", its effect on
  `is_id`, `looks_like_id` and `format_id`, whatever `check` should say about a project configured
  that way, and the binding sentence above.
- Out: the default, which stays `T-` and 3 — decided in T-004 §3 D1 and not re-opened here. Out
  also: anything that would let a local project turn the width check off as a convenience; the value
  is for a backend that allocates, and the record should say so plainly enough that it is not read
  as an escape hatch.

**Inputs**
- [`defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — `none` is already this config's word
  for a key that does not apply, in `blocked_status`, `deliverables_field`, `value_field`,
  `effort_field` and `after_write`. The idiom exists; this is one more use of it.
- [`schema.py`](../plugin/skills/taskmd/taskmd/schema.py) — `is_id`, `looks_like_id`, `format_id`, and the
  `id_width < 1` rejection that a non-numeric value has to pass through.
- [`github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) — the sentence, and assumption 1
  around it.

**Acceptance criteria**
- [x] A config with `id_width: none` loads, and a project whose ids are the prefix plus digits of
      **mixed** widths enumerates every one of them
- [x] The default config still rejects a wrong-width id, shown by the existing
      `tests/fixtures/broken-id-width` continuing to fail
- [x] `format_id` under `none` returns the prefix plus the number unpadded, and `is_id` accepts
      what it returns — a padder with no width to pad to is the obvious way this breaks
- [x] A project configured this way can raise no `ID WIDTH` anomaly, so `check` gains no new output
      and the message that reads `id_width` as a number is unreachable rather than crashing
- [x] The binding sentence says what is true of the keys as they then are
- [x] The default config and the local-markdown binding say `none` is for a backend that allocates
      ids, in terms that do not read as a way to switch the width check off

**Open questions**
- None. **Q1 — does `looks_like_id` still mean anything when width is off? — answered here on
  2026-08-11 under the standing authorisation below: the two collapse, and that is the outcome
  rather than a casualty of it.** `looks_like_id` exists to make a *near-miss* reportable, and a
  near-miss is defined by the width; with no width, prefix-plus-digits is either an id or not a
  task, and there is no third case left to report. So under `none` the two predicates match the
  same set, `load_tasks` never reaches its `elif`, and the `ID_WIDTH` anomaly class is unreachable.

  **Both functions stay.** The alternative — fold `looks_like_id` into `is_id` and delete it — was
  rejected: it is not dead on the default config, where it carries the entire T-075 near-miss
  report, so deleting it would trade a real signal for the tidiness of one project's configuration.
  Keeping both also means no call site changes, so nothing outside `schema.py` has to learn that
  the width can be off.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the positive fixture the criteria are judged against: a project whose config sets `id_width: none` and whose tasks carry the prefix plus **1, 2 and 4** digits, so a single width could not describe them. Written first, before anything accepts the value, so the failure is watched. | `tests/fixtures/backend-allocated-ids/` — `.taskmd/config.md` plus three task files; `check --root` on it failing at config load. |
| 2 | Accept `none` in `_require`, leaving every other non-numeric value rejected by the message it has now, and decide what `self.id_width` then holds. | `plugin/skills/taskmd/taskmd/schema.py` `_require`; the decision recorded in §3. |
| 3 | Make `is_id` accept prefix-plus-any-digits when the width is off, and `format_id` compose without padding. `looks_like_id` is untouched — §1 Q1 says the two collapse by matching, not by editing either one. | `plugin/skills/taskmd/taskmd/schema.py` `Schema.__init__`, `is_id`, `format_id`. |
| 4 | Prove the collapse rather than assume it: assert on the fixture that all three ids load, that no anomaly is raised, and that `is_id(format_id(n))` holds — the property that would break if `format_id` padded to nothing. | Cases in `tests/test_schema.py`; `check --root` on the fixture exiting 0. |
| 5 | Pin the negative half in the same pass: `tests/fixtures/broken-id-width` still fails, and `id_width: 0` and `id_width: nonce` are still rejected. A value meaning "off" that also switched off the typo check would be the escape hatch §1 rules out. | Cases in `tests/test_schema.py`; recorded output in §3. |
| 6 | Correct the binding sentence to say what the keys then do, and say in the two places an adopter reads that `none` is for a backend that allocates ids. | `plugin/skills/taskmd/docs/bindings/github-issues.md`, `plugin/skills/taskmd/taskmd/defaults/config.md`, `plugin/skills/taskmd/docs/bindings/local-markdown.md`, and the fixture table in `tests/fixtures/README.md`. |
| 7 | Run the affected modules and `check`/`index`. | Recorded output in §3. |

**Outputs promised** — `tests/fixtures/backend-allocated-ids/` (config and three task files),
`plugin/skills/taskmd/taskmd/schema.py`, `plugin/skills/taskmd/taskmd/defaults/config.md`,
`plugin/skills/taskmd/docs/bindings/github-issues.md`,
`plugin/skills/taskmd/docs/bindings/local-markdown.md`, `tests/test_schema.py`,
`tests/fixtures/README.md`.

## 3. Implement

**Decisions & assumptions**
- **`none` needed no parsing at all — it was already arriving as `""`, and being rejected there.**
  2026-08-11. The plan expected the work to be in the integer conversion; the fixture failed one
  step earlier, at `CONFIG ERROR .taskmd/config.md: 'id_width' must be a non-empty scalar`, because
  `parse_fields` maps `none`, `null`, `~` and empty to `""` for **every** key before any key-specific
  rule runs. So the change is that `id_width` is the one member of `SCALAR_KEYS` permitted to be
  empty, and empty is what means "no width". This is why step 1 was step 1.
- **`self.id_width` holds `None`, not `0`.** 2026-08-11. Zero would be a width, and `\d{0}` matches
  the empty string, so every prefix would become an id. `None` also makes the two states impossible
  to confuse at a call site, which matters because `cli.py` formats the value with `%d`.
- **`is_id` becomes the same compiled object as `looks_like_id`, rather than a second loose regex.**
  2026-08-11. §1 Q1 decided the two collapse; sharing the object is that decision expressed where
  it cannot drift. The alternative — building a second identical pattern — would leave two places
  to change if the loose form ever moves.
- **`format_id` pads to zero rather than raising.** 2026-08-11. Rejected: raising on a backend that
  allocates, on the grounds that composing an id there is a mistake. It is a mistake, but the caller
  has already decided to compose by the time this runs, and raising breaks
  `is_id(format_id(n))` — a property the test now pins and that a padder returning `#7` keeps.
- **Both rejection messages now name `none` as the way out.** 2026-08-11. Not in the plan; added
  because the two existing errors tell a reader their value is wrong without saying that a legal
  non-numeric value now exists, which sends them to the config doc to discover it.
- **Assumption 1 of `github-issues.md` was read and left alone.** 2026-08-11. It says nothing in
  your project needs a task's id before the task exists, which is the *premise* of this change and
  is still true; editing it would put the same fact in two places.
- **Accepted cost: `id_width:` written with no value now means `none` rather than erroring.**
  2026-08-11. That is how every nullable key in this config already behaves, and the config's own
  rule is that every key must be written — so the alternative would be one key with a private
  spelling of "absent". A misspelling is still caught: `id_width: nonce` is a number that is not
  one, and the test pins it.

**Evidence — the fixture failing before the change, which is why it was built first:**

```
CONFIG ERROR  .taskmd/config.md: 'id_width' must be a non-empty scalar
exit=2
```

**After, on the same fixture:**

```
OK - 3 task(s), 3 field value(s), 3 reference(s), 1 dependency edge(s), 0 declared output(s),
0 index file(s), 4 document(s), 0 link(s), 0 template(s), 0 template field value(s),
1 vocabulary row(s)
#1024   open    Shed refresh
#41     open    Paint the shed
#7      closed  Pick a colour
```

**Suite, per module, one process each, as the runner runs it:** `test_cli` 89, `test_list` 35,
`test_schema` 53, `test_budget` 5 — all OK. `test_runtime` 27, with the four known `Launchers`
failures and no fifth: `test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has`,
`test_the_shell_launcher_produces_what_the_module_produces`, and
`test_every_entry_point_produces_what_the_module_produces` twice, for `skills/taskmd/taskmd.sh` and
`bin/taskmd` — environmental, [T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md).
`test_schema` was 46 before this task and `test_list` was 35, not the 32 the resumption note
recorded — that number was already stale in the commit it was written at.

Repository `check` exit 0 on 123 tasks after `index`; tier 1 unchanged at 6968 characters, 878 under
the bound.

**Outputs produced**
- `tests/fixtures/backend-allocated-ids/.taskmd/config.md` and three task files under `issues/`
- `plugin/skills/taskmd/taskmd/schema.py` — `_require`, `Schema.__init__`, `is_id`,
  `looks_like_id`, `format_id`
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the `id_width` comment and *Ids a backend
  allocates*
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the identity-keys bullet
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — *Configuration this binding reads*
- `tests/test_schema.py` — `BackendAllocatedIds`, and two cases in `RejectsBadConfig`
- `tests/fixtures/README.md` — the fourth positive case

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A config with `id_width: none` loads, and a project whose ids are the prefix plus digits of **mixed** widths enumerates every one of them | met | `check --root tests/fixtures/backend-allocated-ids` exit 0 on `#7`, `#41`, `#1024`; `test_mixed_widths_all_load`. `test_the_derived_edges_still_work_across_the_widths` is the sharper half — a dropped task would show as a parent with one child, which enumeration alone would not reveal. |
| The default config still rejects a wrong-width id, shown by `tests/fixtures/broken-id-width` continuing to fail | met | `test_a_project_that_chose_a_width_still_catches_a_file_that_breaks_it`, asserting the anomaly is `("id-width", "T-0001")` and that only `T-002` loads. Put in the same class as the positive case deliberately: neither can be relaxed without the other being read. |
| `format_id` under `none` returns the prefix plus the number unpadded, and `is_id` accepts what it returns | met | `test_format_id_pads_to_nothing_and_stays_a_valid_id`, round-tripping through `number_of` as well. |
| A project configured this way can raise no `ID WIDTH` anomaly, so `check` gains no new output and the message that reads `id_width` as a number is unreachable rather than crashing | met | `test_is_id_and_looks_like_id_accept_the_same_set` proves the collapse that makes `load_tasks`'s `elif` unreachable; `test_mixed_widths_all_load` asserts `anomalies == []`. The fixture's `check` run prints no `ID WIDTH` line. |
| The binding sentence says what is true of the keys as they then are | met | `github-issues.md` now names both values and says why `none` must be written rather than inherited. |
| The default config and the local-markdown binding say `none` is for a backend that allocates ids, in terms that do not read as a way to switch the width check off | met | *Ids a backend allocates* in `defaults/config.md`, and a paragraph under *Configuration this binding reads* in `local-markdown.md` saying what setting it there would buy: the loss of the check, in return for nothing that binding offers. |

**Child fix tasks raised**
- [T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md) — not a child of this change
  but a finding this task's fixture exposed: `check` reports a **replaced** vocabulary row as
  `CONFIG DRIFT`, which the shipped config says it does not do. Raised rather than fixed here
  (METHOD rule 4), and recorded in `tests/fixtures/README.md` so the fixture's advisory line is not
  read as a defect.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | Six criteria met, evidence in §3 and §4. Run under the standing M2 full-lifecycle authorization recorded below. Raised [T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md) — found by running `check` on the new fixture, not by reading the diff, which is the second time in three tasks that the finding was in the output rather than the change. **The `plugin/` subtree moved**, so this joins the batch waiting on a manifest bump; the version line already reads `0.3.0` from the 2026-08-10 raise, so there is nothing to do here beyond knowing the batch now contains a config-key addition an adopter can write. |
| 2026-08-11 | → planned | Test-first, and the fixture is step 1 rather than step 4: this is a config value nothing accepts yet, so the cheapest thing that could invalidate the rest is `none` failing to reach `Schema.__init__` at all — `id_width` sits in `SCALAR_KEYS`, which is checked before the integer conversion the change is aimed at. Watching the fixture fail at config load puts that in front of the design rather than behind it. Step 5 pins the negative half in the same pass, because the risk this change carries is not that `none` fails to work but that it works too broadly. |
| 2026-08-11 | → specified | Full-lifecycle authorization, given by the maintainer on 2026-08-10, re-confirmed on 2026-08-11 and widened the same day to *multiple tasks, full lifecycle, until you need to stop*: run every open `M2` task through specify → plan → implement → review automatically, one at a time. It covers that set and nothing outside it (METHOD §3.1). Q1 answered under it rather than by an owner turn; the criteria were already written and were sharpened rather than replaced. **The spec's premises were re-checked before agreeing them, not just its target** — `is_id`'s exact-width rule is live at `schema.py:242`, `looks_like_id` at `:253`, the `id_width < 1` rejection at `:293`, and the binding sentence is still at `github-issues.md:76`. Two criteria added: one pinning that `check`'s `ID WIDTH` message, which formats `id_width` with `%d`, becomes unreachable rather than a crash waiting for a project that sets `none`; one pinning the scope's *out*-list — "not an escape hatch" — to text a reader actually meets, since a boundary recorded only in this file is invisible to the adopter it is for. |
| 2026-08-09 | → proposed | Raised by T-004 §3 D3, which found the contradiction while settling its own fourth criterion and decided the shape rather than the change: T-004 is a `decision` task, and a config key plus a binding sentence is neither. Not a blocker on publication — the CLI is local-markdown only, so nothing today reads a config for a GitHub-backed project; what ships broken is the instruction to write one. |
