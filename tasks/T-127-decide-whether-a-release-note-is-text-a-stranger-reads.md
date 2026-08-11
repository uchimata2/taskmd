---
id: T-127
title: Decide whether a release note is text a stranger reads
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-079, T-081, T-125, T-126, T-129, T-133]
work_package: v0.5
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [docs/PUBLISHING.md]
---

# T-127 — Decide whether a release note is text a stranger reads

## 1. Specify

**Outcome**
`docs/PUBLISHING.md` §1 says whether a tag message and its GitHub release are covered by the
humanization rule, so the next person writing one is not deciding it again by themselves.

**Why this one**
Met while writing `v0.4.0`'s notes in
[T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md). §1's test is *text a stranger reads before
they have installed anything*, and a release page is exactly that: it is the second thing someone
evaluating the plugin opens after the README. But §1's worked list does not name it, §1 explicitly
excludes commit messages on the grounds that they are read *after* arriving, and the §5 gate's
pathspec covers four files, none of them a tag.

So the question was answered in the moment, by writing the notes without em dashes anyway, and that
answer is recorded nowhere the next release can find it. **This is the residue §5 names out loud** —
*what it cannot do is notice a covered document of a new kind* — arriving for the first time.

**Why `low`.** Nothing is wrong today: the three published release notes carry no em dashes, and the
one written under this uncertainty was written to the stricter reading. The cost is that the next
person re-derives it, and may derive it the other way.

**Requirements served**
R-21 (`docs/SCOPE.md`).

**Scope**
- In: whether a tag message and a GitHub release are covered by §1's test, and one sentence in §1
  saying which.
- In: if covered, whether the §5 gate can reach them at all, given it reads files and a tag message
  is not one.
- Out: when the gate runs, which is [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md).
- Out: the humanizer patterns and the three exceptions. Settled in T-079 and T-081.

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §1 and §5, in particular the commit-message exclusion
  and the *what it covers, and the one thing it cannot derive* paragraph.
- The three existing tag messages, as evidence of what has been done in practice.

**Acceptance criteria**
- [ ] `docs/PUBLISHING.md` §1 answers the question for a release note, either way, in one place
- [ ] If they are covered, the answer says what enforces it, or states plainly that nothing does
- [ ] The existing three release notes are checked against whichever answer is given, so the rule
      starts from a known state rather than from an assumption

**Open questions**
- ~~**Covered or excluded.**~~ **Answered by the maintainer on 2026-08-11: covered, and §1 says
  plainly that nothing enforces it.** That is the literal reading of §1's own test, and a stated
  unenforced rule beats an unwritten one.

  *Rejected: excluded, on the commit-message grounds.* A release note is an audit trail entry too,
  and excluding it would keep the covered set to files the gate can read. It loses the more
  important half: a release page is the second thing an evaluator opens, and §1's test is about the
  reader rather than about what a script can reach.

  **This makes the residue explicit rather than removing it.** §5 already says the gate cannot notice
  a covered document of a new kind. After this, one covered document is known to be unreachable by
  it, which is the honest state and is why criterion 2 asks for it to be said out loud.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the answer into `docs/PUBLISHING.md` §1 — covered, and what enforces it | `docs/PUBLISHING.md` §1 |
| 2 | Answer the second scope question: whether the §5 gate can reach a tag message or a release body at all | The same paragraph, and a pointer from §5 |
| 3 | Measure the existing notes against the answer, **both texts**, before claiming a known state | Figures in §3, and any task the figures raise |

Step 3 says *both texts* because §1 as raised assumed there was one. A tag message and a GitHub
release body are separate objects, and a check of the reachable one is not a check of the page a
stranger opens.

**Shape decision.**

**D1 — The substance goes in §1, and §5 gets a pointer of one sentence.** §5's residue paragraph
already says the gate cannot notice a covered document of a new kind; naming this case there as well
as in §1 would be two homes for the answer, so §5 names it and points. Criterion 1 asks for one place
and this is it.

## 3. Implement

### Steps 1 and 2 — the answer, and what it can reach

`docs/PUBLISHING.md` §1 now says a tag message and its GitHub release are **covered**, records the
rejected reading, and says plainly that **nothing enforces it**. It also answers the second scope
question, which turned out to have two halves rather than one:

- a tag message can at least be listed, with `git for-each-ref`;
- a release body lives on GitHub and needs the network, which the dependency-free and offline
  constraints keep out of the suite;
- the §5 gate reaches **neither**, because its pathspec lists files and neither of these is one.

§5's residue paragraph gains one sentence naming this as the first known instance of the gap it
already described (**D1**).

### Step 3 — the measurement, and what it refuted

```text
tag messages      v0.1.0  em 0   v0.2.0  em 0   v0.3.0  em 0   v0.4.0  em 0
release bodies    v0.1.0  em 0   v0.2.0  em 4   v0.4.0  em 0        (v0.3.0 has no release)
```

**Two assumptions failed here, and the criterion exists to catch exactly this.** §1 of this task said
*"the three published release notes carry no em dashes"*. That is true of the tag messages and false
of the release pages. It was written before anyone had noticed the second fact: the tag message and
the release body are **different texts** — `v0.2.0`'s tag message is 936 characters and its body
2591, and they do not say the same thing. The earlier check had read the reachable one.

So the rule does **not** start from a clean state, and saying so is the criterion's point. Raised as
[T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md).

**Decisions & assumptions**

- **The `v0.2.0` body is not edited here, and not by this session at all.** Modifying published
  content is outside what a standing multi-phase authorization grants — that waiver is about phases,
  not about acting on a public page. The question is recorded in T-133 with a recommendation and its
  rival. — 2026-08-11
- **§1 says "nothing enforces it" although a tag message is technically reachable.** Building the
  half that can be automated would enforce the text nobody opens while leaving the page they do open
  unchecked, which is worse than an honest none: it would read as coverage. Stated as reachable, and
  deliberately not built. — 2026-08-11

**Outputs produced**
- `docs/PUBLISHING.md` — §1, the answer; §5, one sentence pointing at it

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `docs/PUBLISHING.md` §1 answers the question for a release note, either way, in one place | met | Covered, with the rejected reading recorded. **D1** keeps it to one place: §5 points rather than repeats. |
| If they are covered, the answer says what enforces it, or states plainly that nothing does | met | Nothing does, said in those words — and the paragraph goes further than the criterion asked, distinguishing the tag message (listable) from the release body (not, without the network) so that "nothing" is a conclusion rather than an assertion. |
| The existing three release notes are checked against whichever answer is given, so the rule starts from a known state rather than from an assumption | met | Checked, and it **refuted** the assumption: `v0.2.0`'s release body carries 4 em dashes, and the tag message and the body are not the same text. The known state is therefore *one page in breach*, recorded in [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md). |

**Child fix tasks raised**
- [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) — the
  `v0.2.0` release body. Raised rather than fixed, on two grounds: it is a published page, and
  whether a dated record may be rewritten after the rule changed is the maintainer's call.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All three criteria met, and the third one earned its place. It asked for the existing notes to be **checked** rather than assumed, and the check refuted two things: this task's own §1 claim that the published notes carry no em dashes, and the unstated assumption that a tag message and a GitHub release body are one text. They are not — `v0.2.0`'s tag message is 936 characters, its release body 2591 — and the body carries **4 em dashes**, so the rule starts from a known breach rather than a clean slate. Raised as [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) and deliberately not fixed here: editing a published page is outside what a phase waiver grants, and whether a dated record may be rewritten after the rule changed is the maintainer's. §1 also answers the second scope question more precisely than "no": a tag message is listable with `git for-each-ref`, a release body is not without the network, and the §5 gate reaches neither because both are not files. Building only the reachable half was considered and rejected — it would enforce the text nobody opens and read as coverage of the page they do. |
| 2026-08-11 | → planned | Three steps, and step 3 is the one with content: it says *both texts*, because §1 as raised assumed there was one, and a check of the reachable half is not a check of the page a stranger opens. **D1** keeps the answer in §1 and gives §5 a pointer, since §5's residue paragraph already describes the gap in general and naming this case in both places would be two homes for one answer. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → specified | Answered by the maintainer: **covered, and §1 says plainly that nothing enforces it.** The rival was excluding it on the commit-message grounds, which is defensible and is recorded in §1 with what it loses. The answer makes the residue explicit rather than removing it: one covered document is now known to be beyond the gate's reach, because the gate reads files and a tag message is not one. That is the state criterion 2 asks to be written down. |
| 2026-08-11 | → proposed | Raised from T-125 at the moment the question had to be answered to ship, and not fixed there: T-125's job was to publish this tree, and deciding what the publishing rule covers is a different outcome that changes a document T-125 only reads. The notes for `v0.4.0` were written to the stricter reading so nothing shipped under an unresolved rule, and that choice is recorded here rather than left as the reason a later reader finds no em dashes and assumes a rule exists. Filed `v0.3`, outside the standing `v0.2` authorization, and not started. |
