---
id: T-207
title: Test the platform claims this repository's own second copies rest on
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-187, T-072]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-21
deliverables: []
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
- [ ] <written at `specify`>

**Open questions**
- <none yet>

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* by [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), whose `implement` step 7 used the new clause on cases it was not written from. `medium` and `s`: nothing is broken, and what it buys is that the clause's own repository is not the first place it is ignored. **Not covered by the grant T-187 runs under**, which reaches three named tasks and nothing any of them raises. |
