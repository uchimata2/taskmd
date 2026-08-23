---
id: T-260
title: Assert that this project's config and the shipped default still agree
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-247, T-106]
work_package: M7
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-260 — Assert that this project's config and the shipped default still agree

## 1. Specify

**Outcome**
Something fails when `.taskmd/config.md` and `plugin/skills/taskmd/taskmd/defaults/config.md` come
apart in any way this project did not choose, naming the lines that differ. The one line this project
deliberately overrides stays overridden and does not have to be argued about again.

**Why this one**
**Found by having to write the same paragraph into both files by hand**, while closing
[T-247](T-247-decide-whether-taskmd-validates-a-finding-field-against-a-register.md) on 2026-08-23.
Measured that day, before the edit:

```
diff .taskmd/config.md plugin/skills/taskmd/taskmd/defaults/config.md
25c25
< context_fields: [status, phase, type, work_package, owner, adopter_visible, waiting_on]
---
> context_fields: [status, phase, type, work_package, owner]
```

**One line of 25,047 bytes.** Everything else — including roughly 3,500 bytes of prose about what the
config refuses and why — is byte-identical, and **nothing asserts that.** The two agree today because
whoever last edited one remembered the other.

**The prose is the part that matters, and it is the part with no owner.** The keys differ on purpose
and a reader can see that. The explanatory sections cannot be told apart from a copy that has drifted:
if the shipped file gains a paragraph, this project's copy silently keeps the old one, and the next
person reads whichever they opened. T-247 nearly did exactly this — its own §1 named only
`.taskmd/config.md`, and writing the row there alone would have left the shipped file, which is what
every adopter reads, still saying two capabilities had been refused.

**This is not the duplication rule being broken.** A config is copied by design — that is how a
project adopts one — so the second copy is forced by the mechanism, which METHOD §4 permits on exactly
that ground. What the rule then obliges is that the constraint be visible, and it is not: nothing says
these two files are the same document, and nothing notices when they stop being.

**Scope**
- In: a check that fails on an unintended difference and names the lines
- In: how the deliberate override is expressed, so it is data rather than a remembered exception
- In: whether the check belongs in `tests/` — it runs unasked there, and this defect is one nobody
  would go looking for
- Out: removing the duplication by generating one file from the other. The copy is the adoption
  mechanism and this project must be able to override a key
- Out: any change to what either file says. T-247 settled the current text

**Inputs**
- `.taskmd/config.md` and `plugin/skills/taskmd/taskmd/defaults/config.md` — the two files
- [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) — why an unknown key errors, which
  is what makes a silently-drifted copy expensive rather than untidy
- [T-247](T-247-decide-whether-taskmd-validates-a-finding-field-against-a-register.md) §3 — the run
  that exposed this

**Acceptance criteria**
- [ ] Changing one file and not the other **fails**, naming the differing lines. Shown by doing it,
      not by reading the check
- [ ] The deliberate `context_fields` override does **not** fail, and that case is shown able to fire
      — a permitted difference that could never have been reported proves nothing
- [ ] Adding a permitted override is one edit in one place, and the record says where
- [ ] The check runs without being asked for

**Open questions**
- **Whether the override list is per-key or per-line.** Per-key survives reformatting and needs the
  file parsed; per-line is trivial and breaks when a comment is rewrapped. Whoever plans this.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised while closing [T-247](T-247-decide-whether-taskmd-validates-a-finding-field-against-a-register.md)**, which required the same paragraph in both files. Raised rather than fixed there: T-247's outcome is a decision about a `finding:` field, and a check over two config files is not part of it. The measurement is in that record's §3. |
