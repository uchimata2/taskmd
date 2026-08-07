---
id: T-039
title: Let a plan name a deliverable that does not exist yet
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-010, T-025]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - docs/method/plan.md
---

# T-039 — Let a plan name a deliverable that does not exist yet

## 1. Specify

**Outcome**
Writing a plan that names its outputs no longer puts the project into a state `check` calls broken,
and whichever of the method or the validator was wrong about that says so.

**Why this one**
`plan`'s procedure step 6 asks for the output paths collected in one place, and step 2 asks that
each be named "precisely enough that someone else could look for it". Doing that with a Markdown
link — the ordinary way this project writes a path — makes `check` fail:

```
BROKEN LINK   tasks/T-010-...md -> ../docs/bindings/github-issues.md
```

Which is correct, and also unavoidable: at `plan` the deliverable does not exist yet, by
definition. The workaround is to write the path as a code span and convert it to a link later, and
**nothing anywhere says so** — it was rediscovered by tripping over it in T-010, and the next person
planning a new file will rediscover it the same way. A convention that exists only in the memory of
whoever hit it last is the drift this plugin was built to remove.

**Scope**
- In: deciding where the rule belongs and writing it in exactly one place. The candidates are the
  validator (exempt a path a task declares in `deliverables`), the method (`plan` says to name
  outputs as paths, not links), or the schema doc.
- Out: any other class of broken link. `check`'s link rule is right and stays; this is about one
  case it cannot distinguish, not about relaxing it.

**Inputs**
- `docs/method/plan.md` steps 2 and 6
- Whatever in `taskmd/` implements the broken-link check
- T-010 §2, where the collision was hit and worked around in the plan itself

**Acceptance criteria**
- [ ] A plan can name a not-yet-existing deliverable in the documented way and `check` passes
- [ ] The rule has exactly one home, and the other candidate documents point at it rather than
      repeat it
- [ ] `check` still fails on a genuinely broken link — shown by making it fail, not by it passing
- [ ] If the answer is that the validator should exempt declared deliverables, the exemption is
      shown not to hide a real broken link once the task closes and the file still is not there

**Open questions**
- ~~Fix it in the validator or in the method?~~ — **the owner delegated the whole lifecycle, so it
  is decided here: the method.** What settled it was a fact neither option anticipated, measured
  before choosing (§3, step 1): `check` refuses a **declared** deliverable that does not exist, not
  only a linked one. So `deliverables` already means *produced*, and the validator is right twice
  over. Exempting declared paths would have forced that field to mean "produced, or promised, we
  cannot tell" — one field carrying two facts, which is the drift this plugin exists to remove, and
  a far worse outcome than the friction it was meant to relieve. Rejected on that basis rather than
  on the "weakens a check with no exceptions" argument the question was framed around, which was
  real but not the deciding one.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what `check` actually refuses, by declaring a non-existent deliverable on a real task and running it. The question assumed only *links* were rejected; that assumption decides the answer, so it is tested before anything is chosen. | The command output, recorded in §3 |
| 2 | Choose the home on step 1's evidence, and record what was rejected. | A decision in §3 |
| 3 | Write the rule in the one place chosen. | The edited document |
| 4 | Prove `check` still catches a genuinely broken link — by making it fail, not by watching it pass. | The failing output, and the clean run after |

**Sequencing.** Step 1 is first because it can invert the answer, and it did: the validator turned
out to reject more than the question supposed, which converted "should the validator relax?" into
"what does `deliverables` mean?" — a different question with a different answer.

**Shape of the deliverable — decided.** One sentence appended to `plan.md` step 6, where the
temptation arises, rather than a new paragraph or a note in the schema config. Rejected: putting it
in `taskmd/defaults/config.md` beside `deliverables_field`, which is where the *field* is defined
but not where anyone is standing when they make this mistake.

**Output paths**
- `docs/method/plan.md` — step 6

## 3. Implement

**Step 1 — the measurement that inverted the question.** Declared `docs/NOT-YET-WRITTEN.md` as a
deliverable on this task, at `phase: specify`, and ran `check`:

```
MISSING OUTPUT T-039 declares 'docs/NOT-YET-WRITTEN.md', which does not exist
1 problem(s) over 42 task(s)
```

So a plan can neither **link** a future output nor **declare** one. The question was framed as
"should the validator relax its link rule"; the answer is that the validator is consistent and the
field already has a settled meaning — `deliverables` is what a task **produced**, and `check`
enforces exactly that in both places it can.

**Step 2 — the decision, and why the framing was wrong.** The rule goes in `docs/method/plan.md`.
Rejected: exempting declared `deliverables` from the link rule. The original argument against it was
that it weakens a check whose value is having no exceptions — true, but not decisive. Step 1 supplied
the decisive one: the exemption only makes sense if `deliverables` may hold paths that do not exist
yet, which would make one field mean *produced* on a closed task and *promised* on an open one, with
nothing distinguishing them. That is one field carrying two facts. The friction this task was raised
to remove is worth less than that.

The two lists are genuinely different facts that look alike: `plan`'s output list is what is
**promised**, the front-matter field is what was **produced**. The method already keeps them in
separate places; what was missing was any statement that they are separate, which is why the
collision read as a defect.

**Step 4 — `check` still catches a real broken link**, proven by making it fail. With a link to a
non-existent file added to `plan.md`:

```
BROKEN LINK   docs/method/plan.md -> ../does-not-exist.md
1 problem(s) over 42 task(s)   (exit 1)
```

and after removing it, `OK - 42 task(s)` at exit 0. The rule is untouched and still absolute, which
is the property the rejected option would have spent.

**Decisions & assumptions**
- **The rule lives in `plan.md` step 6, not in the validator and not in the schema config.** — Step
  2. Step 6 is where the temptation arises; `config.md` defines the field but is not where anyone is
  standing when they make this mistake. — 2026-08-07
- **`check` is not changed at all.** — It was correct in both behaviours, and this task's premise
  that one of them was a defect did not survive step 1. — 2026-08-07

**Outputs produced**
- [`docs/method/plan.md`](../docs/method/plan.md) — step 6 gains the paths-not-links rule and the
  promised-versus-produced distinction

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A plan can name a not-yet-existing deliverable in the documented way and `check` passes | met | The documented way is now written down: plain paths in the plan, front-matter left empty until the output exists. This task's own §2 follows it, and `check` reports `OK - 42 task(s)`. |
| The rule has exactly one home, and other candidates point at it rather than repeat it | met | One sentence, in `plan.md` step 6. Nothing was added to `config.md` or to `check`'s output, so there is nothing to point at it — the second clause is satisfied by there being no second copy rather than by cross-references. |
| `check` still fails on a genuinely broken link, shown by making it fail | met | `BROKEN LINK docs/method/plan.md -> ../does-not-exist.md`, exit 1; clean at exit 0 once removed. Step 4 in §3. |
| If the validator exempts declared deliverables, the exemption is shown not to hide a real broken link | n/a | The validator was not changed. Step 1 showed the exemption would require `deliverables` to mean *promised* and *produced* at once, so it was rejected — and this criterion, which existed to police that option, has nothing to police. Recorded rather than deleted: it is the criterion that would have caught the choice going wrong. |

Three met, one made moot by the decision. The task was raised believing `check` had a gap; measuring
it first showed the gap was in the method's silence about two similar-looking facts.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Three criteria met, one made moot. The open question was decided here rather than referred back, since the whole lifecycle was delegated — and the measurement taken before deciding inverted it: `check` refuses a *declared* deliverable that does not exist, not only a linked one. That converted "should the validator relax?" into "what does `deliverables` mean?", and the answer — *produced*, never *promised* — rules out the exemption on stronger grounds than the ones the question was framed around. `check` is unchanged and was proven still to catch a real broken link by being made to fail. |
| 2026-08-07 | → proposed | Raised from T-010's plan phase, where `check` rejected the plan for linking the file that plan existed to produce. Worked around there with a code span and a note; raised here because a workaround discovered by tripping over it is not a convention. Soft edge to T-025, the other open task about what `check` does and does not notice. |
