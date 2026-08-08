---
id: T-058
title: Say that a four-part version number trips the leak check
type: fix
status: done
phase: review
parent: T-049
blocked_by: []
related: [T-049, T-018, T-034, T-035]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: [CLAUDE.md]
---

# T-058 — Say that a four-part version number trips the leak check

## 1. Specify

**Outcome**
Someone who records a version number in a task and watches the pre-publish check go off knows within
one line whether they have leaked something or hit a known limit of the pattern.

**Why this one**
Found by [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md), which recorded the
second platform's kernel as reported by `uname`. That string carries a **four-component version
number**, and the check's IP branch — `[0-9]{1,3}(\.[0-9]{1,3}){3}` — cannot tell one from an
address. The check fired on the task's own record, twice.

Nothing had leaked. But the failure mode is the expensive one: `CLAUDE.md` says the check must print
nothing and that **every hit is either a leak or a label that needs adding**, so a reader who trusts
that sentence spends their time hunting for a leak that is not there. T-049 worked around it by
eliding the patch component, which is a fix for one record rather than for the next person.

**This is the third limit, and the other two are already written down.** `CLAUDE.md` explains at
length why a single-segment drive path is deliberately let through — "a check that cries wolf gets
ignored, which is worse than a narrow one" — and why a real name is not mechanically detectable at
all. Both are honest statements of what the pattern cannot do. This one is the same kind of fact and
is simply missing, which is why the task is about **saying it**, not necessarily about changing the
pattern.

**Requirements served**
No numbered requirement — this serves `CLAUDE.md` *Publishing constraints* and the *Verifying*
discipline directly. A check whose false positives are undocumented gets its output disbelieved,
and then it is not a check.

**Scope**
- In: whether the limit is documented, narrowed, or both.
- In: what a version number should look like in a record, if the answer is "document it".
- Out: the other two limits and the fixture. They are correct and
  [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) and
  [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) settled them.
- Out: any change to what the check *scans*. T-034 settled that.

**Inputs**
- `CLAUDE.md` *The pre-publish check* — the pattern, and the two limits already stated.
- `tests/fixtures/leak-check/samples.txt` — nine lines, five that must be caught and four that must
  not. A fifth safe form belongs there if the answer is "narrow it".
- [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) §1, for the case that found it.

**Acceptance criteria**
- [ ] A reader who hits this is told, in `CLAUDE.md`, what it is and what to do — without having to
      find this task
- [ ] If the pattern is narrowed, the fixture gains a line for the new safe form **and** keeps
      catching all five it caught before — shown by running both halves of the documented check
- [ ] If the pattern is not narrowed, the record says why the false positive is cheaper than the
      alternative, in the same terms the other two limits use
- [ ] **Tier 1 still fits under the flat alternative** — `CLAUDE.md` shorter than
      `reference/TASK-WORKFLOW.md`, counted from the tree rather than asserted
      <br>*Added 2026-08-09 at `specify`, on measuring the headroom: **16 lines**. The rule in
      `CLAUDE.md` *Working method* is the binding constraint on any addition to that file, and a
      task that adds a paragraph to it without checking is how the rule gets broken silently.*

**Open questions**
- **Narrow it, or only document it?** Requiring each component to be ≤ 255 would let a version whose
  third component exceeds it through, while still catching every real address — but a version *can*
  be all-low-numbered, so it narrows the false positives without removing them, and it makes the
  pattern harder to read for a gain that may be smaller than the cost. `CLAUDE.md`'s own argument
  cuts both ways here and the maintainer owns the trade-off, as they did for the drive-path limit.

  *No four-part number is written anywhere in this task, deliberately.* Quoting the specimen into the
  record of a task about the checker re-creates exactly what the checker catches — which happened in
  T-013 and again in T-018, and which `CLAUDE.md` warns about in those words. The specimen belongs in
  `tests/fixtures/leak-check/samples.txt` if the answer is "narrow it", and nowhere else.

  **Answered 2026-08-09: document only, and the narrowing is refuted rather than declined.** The
  proposed change was to require each component to be a valid octet. Measured against the string
  that started this, built from parts so it appears nowhere as a literal:

  ```text
  current IP branch  matches a four-part kernel version : True
  narrowed branch    matches it                         : True
  narrowed branch    still catches a real address       : True
  branch length, current -> narrowed                    : 27 -> 83 characters
  ```

  **It does not help at all.** Every component of an ordinary version string is already under 256,
  so a valid-octet pattern matches it identically — while tripling the length of a line whose
  readability `CLAUDE.md` explicitly buys ("the point of the line is that a reader can see what it
  covers"). So this is not a trade-off that was declined on taste; the candidate fix was tested and
  does nothing.

  That leaves documenting it, which is what the other two limits already are. And criterion 2 falls
  away with it: the fixture must not gain a line, because its contract is five forms that **must**
  be caught and four that must **not**, and a version number is neither — it is caught, correctly by
  the pattern's own terms and wrongly by the reader's expectation. Adding it either breaks the
  documented count of five or asserts a safe form that is not safe.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the third limit into `CLAUDE.md`, alongside the two already there and in the same terms | the paragraph |
| 2 | Re-measure tier 1 against the flat alternative, from the tree | the two counts in §3 |
| 3 | Run both halves of the documented check — silent with the exclusion, exactly five without | the output in §3 |
| 4 | Confirm the suite and `check` are untouched | the output in §3 |

Step 3 carries a trap this task is uniquely exposed to and step 1 must be written for: **the check
reads `CLAUDE.md`**, so a paragraph describing the false positive can create one. That is the same
mistake T-013 and T-018 made, and it is why the existing drive-path limit tells the reader not to
illustrate itself. The new paragraph is written under the same constraint, and step 3 is what proves
it held.

**Shape decisions.**

**D1 — The paragraph names no example, and says so.** The neighbouring limit already does this for
drive paths, in a parenthesis explaining why. Repeating the discipline is cheaper than repeating the
incident. *Rejected: an illustrative version string* — indistinguishable from a leak to the check
that reads this file, which is the whole subject.

**D2 — It says what to do, not only what is happening.** "Elide a component" is one clause and turns
a reader's hunt into an edit. A limit that tells you a hit may be spurious, without telling you how
to make it go away, leaves the file in a state where the check cannot pass — and the check's
contract is that it prints nothing. *Rejected: describing the cause alone* — it is the diagnosis
without the treatment.

**D3 — The heading changes from "Two limits" to "Three".** It is a count of what follows, so leaving
it would make the document wrong about itself in the one section whose subject is being precise
about what a pattern does and does not do.

**Planned outputs**
- `CLAUDE.md` — the third limit

## 3. Implement

### Step 1 — the third limit

`CLAUDE.md`'s *Two limits, both deliberate* becomes *Three limits, all deliberate*, with the new one
placed second so the mechanical two sit together and the un-mechanical one stays last where it was.
It states the class, says nothing has leaked, gives the one-clause remedy, and records that the
obvious fix was tried and does not work — the last part so the next reader does not re-derive the
narrowing and re-propose it.

Written under the constraint it describes, which is the same one the neighbouring limit warns about:
**no four-part number appears in it**, because the check reads `CLAUDE.md`.

### Step 2 — tier 1 still fits

```text
CLAUDE.md               : 160
reference/TASK-WORKFLOW : 173
passes (a < b)          : True | headroom now 13 lines
```

Three lines spent of the sixteen that were there. Counted from the tree, per the rule in
`CLAUDE.md` *Working method*, rather than asserted.

### Step 3 — both halves of the documented check

```text
with the exclusion    : (nothing)
without it            : 5 lines, all in tests/fixtures/leak-check/samples.txt
```

**The first line is the one that matters here**, and it is a stronger result than it looks. The
check reads `CLAUDE.md`, so a paragraph about a false positive is exactly the kind of text that
creates one — that is what T-013 and T-018 did, and what this task's own §1 nearly did before it was
caught. Silence means the paragraph describes the class without instantiating it. The second line
confirms the fixture is untouched and still catches all five, so nothing was bought by weakening the
pattern.

### Step 4 — nothing else moved

```text
116 passed
OK - 58 task(s), vocabulary valid, references resolve, no broken links
```

**Decisions & assumptions**

- **Documenting rather than narrowing is a refutation, not a preference.** — The candidate fix was
  run before being judged: a valid-octet pattern matches an ordinary version string just as the
  current one does, because every component is under 256, and it triples the branch length. So there
  was no trade-off to weigh. Recording it in `CLAUDE.md` rather than only here, because the next
  person to hit this will be reading that file and not this task. — 2026-08-09
- **The fixture is deliberately unchanged, and criterion 2 falls away with the narrowing.** — Its
  contract is five forms that must be caught and four that must not. A version number is neither: it
  *is* caught, correctly by the pattern and wrongly by the reader's expectation. Adding it would
  either break the documented count of five or assert a safe form that is not safe. — 2026-08-09
- **The paragraph is three lines, and the budget was checked rather than assumed.** — Tier 1 is paid
  on every turn of every session and had 16 lines of headroom, which is not much. A task that adds
  prose to `CLAUDE.md` without measuring is how that rule gets broken silently, so it became a
  criterion at `specify` rather than a note here. — 2026-08-09

**Outputs produced**
- `CLAUDE.md` — the third limit, in *The pre-publish check*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A reader who hits this is told, in `CLAUDE.md`, what it is and what to do — without having to find this task | met | §3 step 1. It sits with the other two limits, states the class, says nothing has leaked, and gives the remedy in one clause. The task id is cited only as the source of the refutation, so nothing needed to read the verdict lives outside the file. |
| If the pattern is narrowed, the fixture gains a line for the new safe form **and** keeps catching all five it caught before | n/a — **not narrowed** | The condition did not arise, and it was tested rather than waved off: §1 shows a valid-octet pattern matching an ordinary version string exactly as the current one does. The fixture is unchanged and step 3 confirms it still catches five. |
| If the pattern is not narrowed, the record says why the false positive is cheaper than the alternative, in the same terms the other two limits use | met | Both in the task (§1, with the measurements) and in `CLAUDE.md` (one clause: octets do not help, and it triples the branch). "Cheaper" is the wrong frame in the end and the record says so — the alternative was not more expensive, it was **ineffective**. |
| **Tier 1 still fits under the flat alternative** — `CLAUDE.md` shorter than `reference/TASK-WORKFLOW.md`, counted from the tree rather than asserted | met | §3 step 2: 160 against 173, passing with 13 lines of headroom where there were 16. *Added 2026-08-09 at `specify`; the three above predate it.* |

**The trap this task was most exposed to did not close on it.** The check reads `CLAUDE.md`, so a
paragraph about a spurious match is precisely the text that can create one — the mistake made in
T-013 and again in T-018. Step 3's first line is silent, which is the proof that the paragraph
describes the class without instantiating it. §1 of this task nearly made the same mistake and was
caught by running the check rather than by care.

**Child fix tasks raised**
- none

**Verdict.** Three criteria met, one not applicable because the branch it was conditional on was
refuted rather than declined. The task closes, and with it the last finding from the Linux run.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Three criteria met; the fourth was not applicable because the branch it depended on was **refuted rather than declined**. The proposed narrowing — require each component to be a valid octet — was run before being judged, and it matches an ordinary version string exactly as the current branch does, every component being under 256, while tripling the branch from 27 to 83 characters in a line whose readability `CLAUDE.md` explicitly buys. So there was no trade-off to weigh and the answer is to document, which is what the other two limits already are. `CLAUDE.md` *Two limits* is now *Three*, the new one placed second so the mechanical pair sit together. It cost **three lines** of the sixteen tier 1 had spare — measured, because a task adding prose to the always-loaded file without checking is how that rule breaks silently, which is why it became a criterion at `specify`. The fixture is deliberately unchanged: its contract is five forms that must be caught and four that must not, and a version number is neither. **The trap did not close on this task**: the check reads `CLAUDE.md`, so a paragraph about a spurious match is exactly the text that can create one — the T-013 and T-018 mistake — and the run with the exclusion is silent, which is the proof it describes the class without instantiating one. §1 of this task nearly made that mistake and was caught by running the check rather than by care. |
| 2026-08-09 | → proposed | Raised by T-049 under METHOD §3.3. Recording the second platform's kernel string put a four-component version into a task record, and the check's IP branch matched it twice — nothing leaked, but `CLAUDE.md` promises every hit is a leak or a missing label, so the reader is sent hunting. T-049 elided the patch component, which fixes one record and not the next one. This is the **third** limit of a pattern whose other two are already written down at length, so the task is about saying it; narrowing is an option rather than the goal. `medium`/`xs` — one paragraph in `CLAUDE.md`, possibly one fixture line, but it protects the credibility of the only mechanical guard before publication. |
