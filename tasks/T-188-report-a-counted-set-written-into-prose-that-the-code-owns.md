---
id: T-188
title: Report a counted set written into prose that the code owns
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-139, T-134, T-184]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: [tests/test_publishing.py, tests/test_cli.py]
---

# T-188 — Report a counted set written into prose that the code owns

## 1. Specify

**Outcome**
A ruling on whether a **count** of a set the code owns, written into prose, is worth a rule — and if
it is, the rule. The one instance is repaired either way.

**Why this one**
Found by [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) adding a seventeenth problem
prefix and going to check what the addition made false.
[`tests/test_publishing.py`](../tests/test_publishing.py) line 244 reads:

> **A marker is a claim of completeness, not a claim of importance.** It is why the fifteen problem
> prefixes are not marked

There were **sixteen** before T-184 and there are **seventeen** now, so the sentence was already
wrong when T-184 read it. The argument is sound and is not what is in question; the number inside it
is a derived value that was written down.

**A second instance, found the next day and in a worse place.**
[`plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
*What is gone* says `check` runs *seventeen checks* and that *five of them never take a task as
input*. `cmd_check` ran **sixteen** when that sentence was written, so it was wrong on the day it
shipped; [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) added the seventeenth and
made it accidentally true. Two things follow. It is an **adopter-facing** document rather than a test
docstring, so the reader who meets the wrong number is the one with least ability to check it. And a
count can be repaired by unrelated work without anybody noticing either the break or the repair,
which is the strongest argument available that the class is worth a rule.

**This is [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s
fault class one step sideways, and that is why it is a `decision` rather than a `fix`.** T-139
generalised T-134's guard from the command list to any **marked list of members**, and this is
neither: it names no member, so no pattern reading names can see it, and it sits inside the very
docstring explaining why that set carries no marker. A count is what a list of members degrades into
when somebody decides not to enumerate — which makes it the shape a completeness guard is least
likely to cover, and the shape most likely to be left alone by a reader, because a number in an
argument reads as background rather than as a claim.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`) — a statement the tooling silently accepts is one nobody learns is
wrong.

**Scope**
- In: the ruling — report such a count, or do not, with the rejected options named.
- In: both known instances, corrected whichever way the ruling goes — the test
  docstring and the shipped binding's *seventeen checks* / *five of them*.
- In: whether the honest repair is a rule at all, or removing the number from the sentence, which
  loses nothing the argument needs.
- Out: re-opening [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s
  marked-region mechanism. That is closed and this does not touch it.
- Out: counts of things the code does **not** own. A sentence counting task files or adopters is a
  different question and probably a worse one.

**Inputs**
- [`tests/test_publishing.py`](../tests/test_publishing.py) — the instance, and the guard that could
  not see it
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and
  [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  existing mechanism and its stated boundary
- `plugin/skills/taskmd/taskmd/cli.py` — the seventeen prefixes, which is the set in question

**Acceptance criteria**
- [ ] The ruling is stated as *report it*, *do not report it*, or *remove the counts instead*, with
      the rejected options named
- [ ] The corpus is swept for other written-down counts of code-owned sets before ruling, and the
      number found is stated — a rule justified by one instance is a rule justified by an anecdote
- [ ] If a rule is adopted, it is shown **failing** on the known instance before it is fixed
- [ ] Both known instances are correct at close, whichever way the ruling goes
- [ ] The ruling says why this is or is not the same decision as
      [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s, in
      the terms that record uses

**Open questions**
- ~~**Is a spelled-out number worth a rule, or is the answer to stop writing them?**~~ **Answered at
  `specify` by the sweep, on 2026-08-19, which is what §1 said would settle it.** The sweep found
  **six live counts and three exempt ones**, and the exemptions are the answer: a number a recorded
  decision *fixes* is not a count of a mutable set, and a number written as *measured on a date* is a
  record of that day. Strip those and every survivor is decoration. See the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Sweep every tracked file for a number-word or digit beside a noun naming a set the code owns | The hits, in §3 |
| 2 | Check each against the code and mark it right or wrong **today**, not when it was written | The scored table |
| 3 | Rule, from that table rather than from the two instances §1 opens with | The ruling, in §3 |
| 4 | Repair every live instance the ruling condemns | The edited files |
| 5 | Write the rule where the next person adding a marked list reads | `tests/test_publishing.py` |
| 6 | Run the suite | The output, in §3 |

**Decisions taken at `plan`**

- **The sweep is over `git ls-files`, and task records are excluded from the repair set.** A record
  saying *seventeen checks* on a date is a statement about that date, and correcting it is the thing
  METHOD §5 forbids. They are still read, because a wrong count in one would tell us the class is
  wider than the tooling. *Rejected: sweeping only the plugin*, which would have missed both known
  instances, since both are in `tests/`. — 2026-08-19
- **Each hit is scored against the code as it stands today.** A count that was right when written and
  is wrong now is the whole failure mode; a count that was wrong when written is a second, easier
  one. — 2026-08-19

**Outputs this task will produce**

- tests/test_publishing.py
- tests/test_cli.py
- plugin/skills/taskmd/taskmd/cli.py
- plugin/skills/taskmd/taskmd/schema.py

## 3. Implement

### Step 1–2 — the sweep, scored against the code today

```text
git ls-files -z | xargs -0 grep -nIE "\b(two|three|...|twenty|[0-9]+) (advisor|check|command|
problem|prefix|class|option|flag|vocabular|edge kind|phase)"
```

| Where | Says | Truth today | Verdict |
| :--- | :--- | :--- | :--- |
| `tests/test_publishing.py` | *the fifteen problem prefixes* | 17 | **wrong**, and wrong when written — 16 then |
| `tests/test_cli.py` | *the three advisory lines beside it* | 4 | **wrong**, and it went wrong **four commits ago in this session**, when [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) added `SECTION REF` |
| `tests/test_cli.py` | *the twelve checks that need a task file* | 12 | right, and fragile |
| `tests/test_cli.py` | *the four options that are code* | 4 | right, and fragile |
| `cli.py` | *three checks walk the task set* | 3 | right, and fragile |
| `schema.py` | *the five checks that never open a task file* | 5 | right, and fragile |
| `github-issues.md` | *seventeen checks and five of them never take a task as input* | 17 and 5 | **dated** — the sentence opens *measured 2026-08-18* |
| `docs/SCOPE.md`, `cli.py`, `local-markdown.md`, `github-issues.md` | *four commands*, *four phases*, *three edge kinds* | 4, 4, 3 | **fixed by a recorded decision** |

**The second row is this task's strongest evidence and nobody planned it.** T-188 was raised at
09:00-ish from one instance; by the time its own sweep ran, this session had created a second one in
the same file as the first, with 304 tests green and `check` clean. The class does not take days to
recur. It recurs inside one session, in the file whose job is to catch this shape.

### Step 3 — the ruling

**A count of a set the code owns is either dated as a measurement or not written at all. No
mechanical rule is added.**

Two exemptions, and they are one exemption seen twice:

- **A number a recorded decision fixes is not a count of a mutable set.** *Four commands* is
  `docs/SCOPE.md` non-goal 11 holding the CLI at four; *four phases* is the lifecycle; *three edge
  kinds* is METHOD §4 saying the set is not the project's to choose. None of these moves when
  somebody adds code — moving one takes a decision, and the decision is where it would be caught.
- **A number written as measured on a date is a record of that day**, true then and true forever.
  The binding's *seventeen checks* opens with *measured 2026-08-18*, and METHOD §5 forbids rewriting
  it. It is not a live claim and needs no guard.

Everything else drops the number. Six did.

*Rejected: a mechanical rule.* It needs a mapping from prose nouns — *advisory lines*, *problem
prefixes*, *checks* — to the code sets they name, and **that mapping is a hand-kept list of a
code-owned set**, which is this class one level up. The alternative shape,
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s marked
region with the count inside it, does work and was designed here before being set aside: a `Kind`
row whose `owned` returns `{str(len(the set))}` compares by set equality with no new test. It is
rejected on what it would guard rather than on cost — after the repair there is no live count left
for a region to sit in, and minting a mechanism for an empty class is the failure
[*ask whether the remedy's target class is empty*] names.
*Rejected: leaving them and correcting on sight.* That is what happened, and the sweep is what
noticed; nobody was going to.

### Step 4–5 — the repairs, and where the rule lives

Six edits, each removing a number and nothing else — the sentences all carried their point without
it, which is itself part of the evidence. The rule is written into
`tests/test_publishing.py`'s `EveryMarkedListNamesTheSetTheCodeOwns`, in the paragraph that already
argues why the problem prefixes carry no marker: that is where the next person adding a marked list
reads, and it is the paragraph that was wrong.

### Step 6 — verification

```text
Ran 304 tests in 46.636s
OK
```

The sweep re-run finds no live count outside the two exemptions.

**Decisions & assumptions**

- Both `plan` decisions held. — 2026-08-19
- **The ruling has no detector, and that is stated rather than implied.** A writing convention with
  no test is exactly the kind of guard this project distrusts. What makes it acceptable here is that
  the rule's *shape* is checkable by a sweep anybody can re-run — the grep in step 1 is in the
  record — and that the alternative detector is the same fault class. A future count that is
  genuinely load-bearing and undated should carry T-139's region, and the design for it is above
  rather than lost. — 2026-08-19

**Outputs produced**
- tests/test_publishing.py — the rule, and one repair
- tests/test_cli.py — three repairs
- plugin/skills/taskmd/taskmd/cli.py — one repair
- plugin/skills/taskmd/taskmd/schema.py — one repair

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The ruling is one of the three, with the rejected options named | **met** | §3 step 3: *remove the counts, with two exemptions, and no rule*. Rejected: a mechanical rule, T-139's region, and correcting on sight |
| The corpus is swept before ruling, and the number found is stated | **met** | §3 steps 1–2. Six live, three exempt, one dated. §1 opened with one instance and the sweep found six |
| If a rule is adopted, it is shown failing on the known instance first | **n/a** | No rule is adopted, and §3 says what would have to be true for one to be worth it |
| Both known instances are correct at close | **met** | And four more the sweep found. `git grep` for the sweep pattern returns only the exempt rows |
| Why this is or is not the same decision as T-139's | **met** | §3 step 3, in T-139's own terms: a marked list is a claim of completeness that a pattern reading *names* can check; a count names no member, so the same mechanism needs a prose-noun-to-set mapping, which is the fault class again |

**Open questions, re-read before closing** (procedure step 5)

§1's only question is answered above by the sweep, as §1 said it would be, and struck through there.
Nothing here is addressed to anyone else.

**One thing worth carrying out of this task.** The instance that mattered was not the one it was
raised for. It was the one created **during** the task, by unrelated work, in the file whose purpose
is to catch this shape — which is a stronger argument for the rule than the original finding was, and
it exists only because the sweep was run after the day's other work rather than before it.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **§3's catalogue missed one occurrence, and the shape of the miss is the interesting part.** Its table carries **one row per file**, and `github-issues.md` held **two** counts of this set: the dated blockquote the row names — *measured 2026-08-18* — and, separately, an **undated** *Seventeen checks run on the local backend. Nine land here as rows above, and four cannot occur at all.* The verdict column read **dated — needs no guard**, which is right about the sentence the row names and licensed leaving the other. So *Everything else drops the number. Six did* was short by one. Found on **2026-08-22** by [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), which added a check, falsified the undated sentence, and **applied this task's own ruling to it** — deleted rather than bumped, with the deletion said out loud. The ruling is unchanged and was not the thing at fault; classifying a **file** where the unit is an **occurrence** was. Whether any other undated count survived the same way is [T-220](T-220-re-run-t-188-s-sweep-one-occurrence-at-a-time.md). |
| 2026-08-19 | → done | `specify` through `review` in one session, under the owner's extension of the eight-task grant to what those eight raise. **Ruled: a count of a set the code owns is either dated as a measurement or not written, and no mechanical rule is added.** The sweep settled it, as §1 said it would: six live counts, three fixed by a recorded decision — four commands, four phases, three edge kinds — and one written as a dated measurement, which METHOD §5 protects. Strip those and every survivor was decoration, so six numbers came out and every sentence still carried its point. **The decisive instance was created during this task**, four commits earlier, when [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) added a fourth advisory and left `tests/test_cli.py` saying *the three advisory lines beside it* — in the file whose job is to catch this shape, with the suite green. A detector was designed and rejected on what it would guard rather than on cost: it needs a prose-noun-to-code-set mapping, which is this class one level up. |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19, when resuming the handoff that carried it: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. Every grant before it excluded what its tasks raised, by name, so this is a change of boundary and not a reading of the old one. It reaches this task because [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) raised it. **It does not answer the open question above** — the grant is permission to run the lifecycle, and §1's question is settled by the sweep the criteria require, not by anyone's authority. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md)'s review, from adding the seventeenth problem prefix and checking what that made false. Not fixed there: a review that repairs what it finds destroys the record of what was wrong (METHOD §5), and the one-word repair is the least interesting half. Typed `decision` because the answer may be that nothing is added — one instance, spelled in words, inside a sentence that does not need the number. |
