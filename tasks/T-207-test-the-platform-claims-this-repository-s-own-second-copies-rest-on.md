---
id: T-207
title: Test the platform claims this repository's own second copies rest on
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-187, T-072]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-22
deliverables: [docs/PUBLISHING.md, plugin/bin/taskmd.cmd]
---

# T-207 — Test the platform claims this repository's own second copies rest on

## 1. Specify

**Outcome**
Every place this repository writes one fact twice because a platform is believed to compel it has
either been shown the refusal — the single write attempted and rejected — or has lost the second copy.
Where the copy stays, what forces it is written where a reader meets it.

**Why this one**
Found by [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) while doing the
thing that phase asks for: **using** the clause it had just written, on cases it was not written from.
The clause turns away *a limitation you assumed rather than one you were refused*, and the first two
places it was pointed at in this repository both came back holding an assumption:

- **`.claude-plugin/marketplace.json` → `plugins[0].name`** is `taskmd`, and so is
  `plugin/.claude-plugin/plugin.json` → `name`. One fact, two homes.
  [T-072](T-072-give-the-description-and-version-one-home-each.md) is the precedent and it is a
  warning rather than a comfort: it ran `claude plugin validate` against four manifests and found
  **description and version both optional**, deleting two copies that everybody had assumed were
  required. It did not try `name`. So the surviving copy sits on exactly the untested claim its own
  task disproved twice.
- **`plugin/bin/taskmd.cmd`** states why the entry point exists twice: *no single name is typeable on
  both platforms — an extensionless POSIX script is not executable through a PATH lookup here, and
  `.cmd` is in the default PATHEXT where `.sh` and `.ps1` are not.* That is a claim about Windows,
  and `CLAUDE.md`'s *Verifying* section says a claim about behaviour is verified by running it. It
  reads as settled because it is stated well, which is the shape T-187's refusal case describes.

**It is a sweep, not these two.** They are what one application of the clause happened to reach, and
naming them as the membership would be the enumeration this project's own config warns against.
Derive the set: find where a fact is written twice and a platform is given as the reason.

**Scope**
- In: this repository's own second copies, whatever the sweep finds — the two above are found
  instances, not the list
- In: for each, the single write attempted against the real platform, and what it printed
- In: deleting the copy where the platform allows it, or recording the refusal beside it where it
  does not
- Out: the wording of the clause itself. That is T-187's, and this task tests the repository against
  it rather than the other way round
- Out: any second copy whose reason is not a platform — a different argument is a different task

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the clause, and the refusal case this applies
- [T-072](T-072-give-the-description-and-version-one-home-each.md) — the method that worked, and the
  field it did not reach
- `CLAUDE.md` — *Verifying*, which already binds on every claim about behaviour

**Acceptance criteria**

Written on 2026-08-22. The task's own hazard is that it is a **sweep whose two known members are
already named in §1** — so a derivation that finds only those two would look like a result, and a
verdict reached by reading a manifest would look like a test. Four of the criteria below exist to
stop each of those.

- [ ] **The set is derived, the derivation is shown, and what it is known to miss is stated** rather
      than left as an implied completeness. What failure looks like: a sweep that reports a set and
      cannot say what it read
- [ ] **The two instances named in §1 are found *by* the derivation, not added to it.** They are how
      the derivation is checked, so a derivation that misses either is itself the finding — widening
      it until it happens to catch them fits the answer to the known cases and says nothing about the
      unknown one
- [ ] **Every member of the derived set ends with one of two verdicts** — the copy is gone, or the
      refusal is recorded beside it. None is left described, considered, or deferred without a task
- [ ] **Each *the platform compels it* claim is settled by running something, with the command and its
      output quoted.** A verdict reached from documentation, from a manifest schema, or from how the
      code reads fails this: an untested claim about a platform is the exact case METHOD §4's clause
      refuses, and this task is the clause applied to its own repository
- [ ] **The single write is attempted against every consumer that reads the fact, and the consumers
      are named.** [T-072](T-072-give-the-description-and-version-one-home-each.md) settled two fields
      with `claude plugin validate`; a validator accepting an absent field is not the same claim as
      every reader tolerating it, and `name` is the field an install resolves by
- [ ] **Where a copy is deleted, the artefact is shown still to work afterwards** — the manifest still
      validates, the entry point still starts — quoted, and **on the platform the claim was about**.
      A green run names the operating system it was green on, because the `taskmd.cmd` claim is a
      claim about Windows and answers differently elsewhere
- [ ] **Where a copy stays, what forces it is written where a reader meets the second copy** — not
      only in this task's record. That is the clause's own condition: the rule is exchanged for the
      obligation to keep the constraint visible, so that whoever finds it the day the platform stops
      compelling it can delete it
- [ ] `check` is clean and the suite passes; if a manifest changes, the plugin is shown to still
      install from it

**Open questions**
- **None.** Two candidates were considered and neither survives. *Whether a shipped manifest may be
  edited outside a release* is already settled by
  [T-072](T-072-give-the-description-and-version-one-home-each.md), which deleted two fields from
  these same manifests. *Whether deleting a field could break an already-installed snapshot* is not a
  question for the owner but a thing to measure, and the criteria above require exactly that
  measurement — it is the difference between a consumer that was tested and one that was assumed.

## 2. Plan

**Sequencing.** Step 1 before anything else, because the two instances §1 names are how the
derivation is *checked* rather than what it is for — a sweep that starts from them can only confirm
them. Steps 3-4 are the tests, and step 5 is the only step that edits an artefact.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the set: scan the tracked tree for a place where a duplication is described **and** a platform is given as the reason. Partition every hit so the rows sum, rather than filtering until the answer looks right. | The scan, its reach, and a partition whose counts sum, in §3 |
| 2 | Check the derivation against §1's two known instances. A miss is the finding, not an invitation to widen until it hits. | Which of the two the derivation found, and for any it missed, **why** — a property of the method, not of the instance |
| 3 | Attempt the single write for each member, against the real platform, and quote what it printed. | The command and its output, per member, in §3 |
| 4 | Name the consumers that read each fact, and say which of them the attempt was made against. | The list in §3 |
| 5 | Per member: delete the copy, or record what forces it **where a reader meets it**. | The edits, and for each, why that location and not a closer one |
| 6 | Show the artefact still works afterwards, on the platform the claim was about, and run the gates. | The quoted runs, naming the operating system |

**Shape of the deliverable, decided — 2026-08-22.** Where a copy stays, the refusal goes **beside the
copy** in whatever the format allows, and into the document that governs the artefact where the
format allows nothing. *Rejected: recording every refusal in this task's record only*, which is what
METHOD §4's clause explicitly refuses — the rule is exchanged for keeping the constraint visible, and
a task record is not where anybody meets the second copy.

**Outputs** — plain paths:

- docs/PUBLISHING.md
- plugin/bin/taskmd.cmd

## 3. Implement

### Step 1 — the derivation, and its reach

Two vocabularies, and a hit is a paragraph where they meet: words a second copy is described with,
and words a system is named with. It reads the **tracked** tree — every text file a clone receives.

```text
read 345 tracked text file(s); 172 paragraph hit(s) where a duplication word meets a platform word
```

**Partitioned rather than filtered**, because a filter cannot report what it dropped:

```text
138  task records: a record describes a past decision; it is not itself a second copy
 11  source: the words are identifiers and check-class names, not claims about a platform
 23  LIVE ARTEFACTS AND SHIPPED DOCUMENTS - the set to read
172  total, against 172 hits reported above
```

Reading the 23 gives **one** in-scope member: `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd`, the
entry point written twice. The rest are the rule itself (`METHOD.md`, `BINDING.md`), guidance to an
adopter's backend (`github-issues.md`, the config files), or a coincidence inside one paragraph —
`docs/SCOPE.md:273` is a table whose rows happen to contain *duplicate* and *PowerShell*.

**One near-member is excluded by scope and is worth naming**: `.taskmd/config.md` and
`plugin/skills/taskmd/taskmd/defaults/config.md` are near-copies of each other, decided in T-135 —
but the reason is a schema-key decision and not a platform, and §1 puts a second copy with a
non-platform reason out.

**What this derivation cannot see, stated rather than implied:** a second copy nobody wrote a
sentence about. It keys on the *explanation*, so a duplication in a format with no comments is
invisible to it — which is not a hypothetical.

### Step 2 — checked against the two known instances

**One found, one missed.**

| §1's instance | Found by the derivation? |
| :--- | :--- |
| `plugin/bin/taskmd` / `taskmd.cmd` | **Yes** — `plugin/bin/taskmd.cmd:1`, on *two files rather than one* meeting *cmd* |
| `marketplace.json` / `plugin.json` `name` | **No** |

**The miss is a property of the method and it is the useful half.** Neither manifest is prose and
JSON carries no comment, so there is no sentence to key on — and widening the word list would never
have helped, because the text does not exist. So the derivation gained a **second arm** for formats
that cannot carry an explanation: compare the values structurally.

```text
arm 2 - structural: every scalar value appearing in more than one tracked JSON manifest
read 3 tracked .json file(s): .claude-plugin/marketplace.json, .claude/settings.json,
                              plugin/.claude-plugin/plugin.json

  'taskmd'     in 2 file(s):
      .claude-plugin/marketplace.json            name
      .claude-plugin/marketplace.json            plugins[0].name
      plugin/.claude-plugin/plugin.json          name
```

It finds the member, and **finds one more copy than §1 named**: three places, not two. The
marketplace's own top-level `name` is a different fact — what the *marketplace* is called — that
happens to share the value, which is why it is not treated as a fourth thing to delete.

### Step 3 — the single write, attempted and refused

**Member 1 — the manifests.** Both directions, on 2026-08-22:

```text
$ claude plugin validate .          # with plugins[0].name deleted
  ❯ plugins.0.name: Invalid input: expected string, received undefined
✘ Validation failed                                                    exit 1

$ claude plugin validate .          # with plugin.json's name deleted
  ❯ plugins[0] plugin.json → name: Invalid input: expected string, received undefined
✘ Validation failed                                                    exit 1

$ claude plugin validate .          # both restored
✔ Validation passed with warnings                                      exit 0
```

**Member 2 — the entry point**, with only the extensionless file on `PATH`, on Windows 11:

```text
PATHEXT = .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL
  .sh in PATHEXT: False   .ps1 in PATHEXT: False   .cmd in PATHEXT: True

cmd.exe   'taskmd' is not recognized as an internal or external command      exit 1
pwsh 7    resolves the file, then produces no output and no exit code
```

**The claim held and got sharper.** It said *not executable through a PATH lookup*; cmd.exe refuses
it by name, and PowerShell 7 **resolves** it and runs nothing — which is the worse of the two,
because it looks like a command that ran. That distinction was found by insisting on a command with
known non-empty output: an earlier probe ran `taskmd --help`, got an empty result, and could not tell
success from silence.

### Step 4 — the consumers, named

| Fact | Consumers that read it | Attempted against |
| :--- | :--- | :--- |
| `plugins[0].name`, `plugin.json` `name` | `claude plugin validate`; the install path, which resolves a plugin **by** that name | The validator. It refuses at exit 1 before an install is reachable, so the install path is named and not separately tested — there is nothing to install from a manifest that will not validate |
| the entry-point file name | a `PATH` lookup in `cmd.exe`, in PowerShell, and in a POSIX shell | All three: cmd.exe and pwsh above; the POSIX side is `plugin/bin/taskmd` itself, which is what every command in this record ran through |

### Step 5 — the verdict per member: both copies stay, both refusals recorded

| Member | Verdict | Where the constraint now lives |
| :--- | :--- | :--- |
| `marketplace.json` / `plugin.json` `name` | copy stays — **refused** | `docs/PUBLISHING.md` §4a |
| `plugin/bin/taskmd` / `taskmd.cmd` | copy stays — **refused** | `plugin/bin/taskmd.cmd`'s own header comment |

**Member 2's constraint sits beside the copy**, in the file's comment, with both shells' output and
the `PATHEXT` value, and a line saying to delete the file the day that changes.

**Member 1's could not, and the attempt to put it there is itself measured.** JSON carries no
comment, so the only candidate was a key in the manifest — and the validator answers:

```text
  ❯ plugins[0]._why_name_is_here: Unknown field '_why_name_is_here'. Claude Code ignores it at
    load time.
```

An explanation that makes every future run of the gate print a warning is worse than one a directory
away, so it went into the document that governs the manifests. **That is a weaker placement than the
clause asks for, and §4a says so** rather than presenting the compromise as the intent.

### Step 6 — still working, on the platform the claim was about

```text
Windows 11, cmd.exe:  plugin\bin\taskmd.cmd list --open --limit 1
  T-206  in_progress  M6  implement  Test whether the description's Markdown-files clause ...

claude plugin validate .     ✔ Validation passed with warnings
taskmd check                 OK - 211 task(s), ...
```

Both manifests are byte-identical to where they started — `git diff` on the two was empty after each
probe, checked rather than assumed, because every test in step 3 edited them.

**Decisions & assumptions**

- **The derivation is partitioned, not filtered** — 138 + 11 + 23 = 172, so what was set aside is
  counted and named. Rejected: scanning only the live artefacts, which is the same set by a route
  that could not say what it skipped - 2026-08-22.
- **The missed member widened the method, not the word list** — a manifest has no sentence to key on,
  so a structural arm was added for formats that cannot carry an explanation. Rejected: adding
  *marketplace* and *manifest* to the vocabulary until the known case appeared, which fits the answer
  to what is already known and says nothing about the next one - 2026-08-22.
- **The install path is named but not separately tested** — the validator refuses at exit 1, and
  there is nothing to install from a manifest that will not validate - 2026-08-22.
- **Member 1's constraint lives a directory away, and the record says it is weaker than the clause
  asks.** Rejected: an explanatory key in the manifest, which validates but makes the gate warn on
  every run from then on - 2026-08-22.
- **A claim is only tested by a command with known non-empty output** — the first PowerShell probe
  returned nothing and could not distinguish a script that ran from one that did not - 2026-08-22.

**Outputs produced**

- docs/PUBLISHING.md
- plugin/bin/taskmd.cmd

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| **The set is derived, the derivation is shown, and what it is known to miss is stated** | met | §3 step 1: 345 files read, 172 hits, partitioned 138 + 11 + 23 so the rows sum. The stated miss — a second copy nobody wrote a sentence about — was not hypothetical, and step 2 is it happening |
| **The two instances in §1 are found *by* the derivation, not added to it** | met | §3 step 2: the entry point was found; the manifests were **missed**, and the miss is recorded as the finding. The method gained a second arm for formats that carry no comment, rather than the word list gaining the words that would have caught the known case |
| **Every member ends with one of two verdicts** | met | §3 step 5: both copies stay, both refusals recorded. Neither is left described or deferred |
| **Each claim is settled by running something, command and output quoted** | met | §3 step 3: three `claude plugin validate` runs with exit codes, and the `PATH` lookup in cmd.exe and pwsh 7 with `PATHEXT` quoted |
| **The single write is attempted against every consumer, and the consumers are named** | met | §3 step 4, one row per fact. The install path is named and not separately tested, with the reason: the validator refuses at exit 1, so there is nothing to install |
| **Where a copy is deleted, the artefact is shown still to work** | n/a | No copy was deleted — both were refused. The artefacts are shown still to work anyway (§3 step 6), on **Windows 11**, which is the platform member 2's claim was about |
| **Where a copy stays, what forces it is written where a reader meets it** | met, one weakly | Member 2's is in `plugin/bin/taskmd.cmd`'s own header. Member 1's is a directory away in `docs/PUBLISHING.md` §4a, because the manifest answers an explanatory key with a standing validator warning — measured, and §4a states the compromise rather than presenting it as the intent |
| `check` is clean, the suite passes, and the plugin still installs from the manifest | met | `OK - 211 task(s), ...`, the suite below, and `claude plugin validate .` → *Validation passed with warnings*, exit 0, with both manifests byte-identical to where they started |

**What this does not settle.** Arm 1 sees only what somebody explained, arm 2 only tracked JSON. A
second copy in a format that carries no comment **and** is not JSON — a `.ini`, a lockfile, two shell
scripts sharing a literal — is outside both, and nothing here would report it. Named because the
whole task is about untested claims, and *the sweep was complete* would be one.

**Open questions, re-read before closing.** §1 recorded none, and none arose.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* by [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), whose `implement` step 7 used the new clause on cases it was not written from. `medium` and `s`: nothing is broken, and what it buys is that the clause's own repository is not the first place it is ignored. **Not covered by the grant T-187 runs under**, which reaches three named tasks and nothing any of them raises. |
| 2026-08-22 | → specified | **Specify agreed: eight criteria written, where §1 had carried a placeholder, and the open-questions slot resolved to none with the reasons.** The criteria are shaped by this task's two ways of looking finished without being it. **First, the sweep**: §1 names two instances, so a derivation returning exactly those two would read as a result — a criterion therefore requires the two be found *by* the derivation rather than added to it, making them the test of the instrument instead of its output. **Second, the verdict**: this task is METHOD §4's refusal case applied to its own repository, so a claim settled by reading a schema is the failure and not the evidence, and one criterion requires a command and its output for every claim. One criterion carries [T-072](T-072-give-the-description-and-version-one-home-each.md)'s unfinished half: that task settled two fields with `claude plugin validate`, and a validator tolerating an absent field is not every reader tolerating it — `name` is what an install resolves by, so the consumers have to be named and each one tried. Another requires a green run to name the operating system it was green on, because the `taskmd.cmd` claim is about Windows. Phase stays at `specify`; `plan` is not authorised (METHOD §3.1). |
| 2026-08-22 | → done | **Both platform claims were tested by running something, and both held — so both copies stay and both refusals are now recorded where a reader meets them.** `plugins[0].name` and `plugin.json`'s `name` each make `claude plugin validate` exit 1 when deleted; an extensionless script on `PATH` is refused by name in cmd.exe and, worse, **resolves and runs nothing in PowerShell 7**, which looks like a command that ran. **The derivation found one of the two known instances and missed the other, and the miss is the result**: a manifest is not prose, so there was no sentence to key on — the method gained a structural arm for formats that carry no comment rather than the word list gaining the words that would have caught the known case, and that arm found *three* copies where §1 named two. **One constraint is placed more weakly than METHOD §4 asks** — a directory away in `docs/PUBLISHING.md` §4a rather than in the manifest, because an explanatory key validates but makes the gate warn on every run from then on; §4a says so rather than presenting the compromise as the intent. Both manifests are byte-identical to where they started, checked after every probe. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that the six remaining tasks be scheduled to the next session with the **full lifecycle**. **What it covers:** this task, one of the six — [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md), [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md), [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md), [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) and [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase. **What it does not cover:** any other task. The owner was asked on the same date whether the grant reached [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), whose closure these six unblock, and answered **the six only** — so that boundary is a decision taken rather than a silence. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it may not be finishable in one run, and stopping is correct if so.** Its criteria require the single write to be *attempted and refused* against every consumer that reads the fact — an attempt that cannot be made is a finding to record, not a claim to reason out. |
