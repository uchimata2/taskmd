---
id: T-046
title: Reconcile the done-condition CLAUDE.md restates from the method
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-027, T-028]
work_package: v0.1
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - CLAUDE.md
  - plugin/skills/taskmd/docs/bindings/local-markdown.md
---

# T-046 — Reconcile the done-condition CLAUDE.md restates from the method

## 1. Specify

**Outcome**
`CLAUDE.md` states no closing condition of its own. Either it points at `docs/METHOD.md` §1 rule 5,
or it states only the part that is genuinely local — and its own sentence saying the method is not
restated there becomes true of the file.

**Why this one**
Raised by [T-027](T-027-give-the-design-rule-one-home.md)'s review, against its criterion 3: *"`CLAUDE.md`'s
own 'if you find it written out somewhere else, that copy is the defect' sentence is true of the file
that contains it."* Checked against the file rather than against the section T-027 edited, it is not:

| Document | The closing condition |
| :--- | :--- |
| `docs/METHOD.md` §1 rule 5 | outcome exists, record is current, **the `implement` evidence is written down** |
| `CLAUDE.md` §*Working method* | deliverables exist, log is current, **the validator passes** |

**It is not a copy, it is a copy that has already drifted** — which is the more expensive kind. Two
of the three slots are the local nouns for METHOD's, and that much is what a binding legitimately
does. The third is a different condition: METHOD requires recorded evidence that the outcome was
used, `CLAUDE.md` requires a tool run. A task can pass `python -m taskmd check` with `## 3. Implement`
left as the template placeholder, so the local version can be satisfied with none of what the method
asks for. The rule this project claims most loudly is the one it restated and lost a clause from.

**The framing around it is right for the other three bullets.** The list is introduced as *"What this
project adds on top, because the method is deliberately storage-agnostic"* — and the tasks folder,
the schema file and the generated index are genuine additions. This one is not an addition; it is
METHOD §1 rule 5 with local nouns and a substituted clause, sitting under a heading that says it is
not.

**Requirements served**
R-1, R-4 (`docs/SCOPE.md`).

**Scope**
- In: `CLAUDE.md` §*Working method*, the `done` bullet, and whatever replaces it.
- In: whether the local mapping belongs in `docs/bindings/local-markdown.md` instead — it is the
  document whose job is saying which artifact plays which role, and it does not currently carry this.
- Out: `docs/METHOD.md` §1 rule 5 itself, which is the one home and is correct as written.
- Out: the other three bullets in that list, which are additions and not restatements.
- Out: making `check` enforce the evidence clause. That is a tool change and a separate argument;
  this task is about a document saying something the method does not.

**Inputs**
`CLAUDE.md` §*Working method*, `docs/METHOD.md` §1 rule 5 and §2 *implement*,
`docs/bindings/local-markdown.md`, [T-027](T-027-give-the-design-rule-one-home.md) §4.

**Acceptance criteria**
- [ ] `CLAUDE.md` no longer states a closing condition that differs from `docs/METHOD.md` §1 rule 5
- [ ] The `implement`-evidence clause is reachable from `CLAUDE.md` in one link, or is stated there
      correctly — losing it silently is the defect, so a fix that drops the sentence without
      replacing the route to it does not count
- [ ] `CLAUDE.md`'s "it is not restated here; if you find it written out somewhere else, that copy is
      the defect" sentence is true of the whole file, checked by re-reading the file and not only the
      edited line
- [ ] If the local mapping moves to `docs/bindings/local-markdown.md`, that binding says it once and
      `CLAUDE.md` points there

**Open questions**
- None blocking `specify`. Which of the two homes takes the local mapping — `CLAUDE.md` as a pointer,
  or the local-markdown binding — is `plan`'s to choose against criterion 4.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Choose the home for the local mapping against criterion 4 — `CLAUDE.md` corrected in place, or `docs/bindings/local-markdown.md` — on what each document is *for* rather than on which edit is smaller. | A recorded decision, with what was rejected |
| 2 | **Demonstrate the defect rather than assert it.** Build a throwaway project outside this repository holding one task at `status: done` whose `## 3. Implement` is still the template placeholder, and run `check --root` on it. | The command output, and a verdict on the finding's central claim |
| 3 | Write the mapping into its chosen home, beside METHOD §6's homes assignment, and say what `check` does and does not see — the substitution being fixed is exactly the belief that it sees all three. | The edited document |
| 4 | Replace `CLAUDE.md`'s bullet with a route to the rule and to the mapping, **stating no closing condition of its own**. | The edited bullet |
| 5 | Re-read `CLAUDE.md` whole against criterion 3 — the sentence makes a claim about the file, and the last task to check it against only the section it had edited is the reason this task exists. | A verdict per section |

**Sequencing.** Step 2 comes before any writing because it can change what the fix has to say: if
`check` *does* reject a placeholder `## 3.`, then `CLAUDE.md`'s bullet is imprecise rather than
wrong, the evidence clause is not actually losable, and a much smaller correction is the right one.
Asserting it and writing the fix around the assertion is the failure `CLAUDE.md` §*Verifying* names.
Step 5 is last because it judges the file after both edits, and it is deliberately a re-read of the
whole file rather than of the diff.

**Shape of the deliverable — decided: the mapping goes to the binding, and `CLAUDE.md` keeps a
route.** The decisive point is that the mapping is **not a project fact at all** — that the outcome
is the declared deliverables, the record is the log, and the evidence is `## 3. Implement` is true
for anyone using local Markdown files, not just for this repository. It reads as a project
convention only because `CLAUDE.md` is where it happened to be written. `docs/bindings/local-markdown.md`
already assigns METHOD §6's homes in exactly this form, so there is a place shaped for it.
*Rejected: correct the bullet in place, restoring the evidence clause.* It would be accurate today
and would still be a second copy — it drifts the moment METHOD §1 rule 5 is sharpened, which is
precisely how the present one came to differ. Fixing the content and keeping the structure fixes the
instance and not the defect.
*Rejected: delete the bullet with nothing in its place.* Cheapest for tier 1, and criterion 2 rules
it out: METHOD would be reachable only through the generic "the method has one home" link, so a
reader looking for when a task is done here has no reason to follow it. Losing the route silently is
the same failure as losing the clause.

**Output paths**
- `docs/bindings/local-markdown.md` — the homes assignment, extended with METHOD §1 rule 5's three conditions
- `CLAUDE.md` — §*Working method*, the `done` bullet
- This task's §3 — the demonstration and the per-section verdict

## 3. Implement

**Step 2 — the claim was demonstrated, and it holds.** A throwaway project was built outside this
repository — one task folder, one task, at `status: done` with an implement section holding nothing
but the template placeholder, no deliverables, no review table and no log — and the validator was
pointed at it with `--root`:

```text
OK - 1 task(s), vocabulary valid, references resolve, no broken links
exit=0
```

So a task that recorded **nothing** closes clean under the condition `CLAUDE.md` was stating. The
project lived outside the tree and is gone; it is not a fixture, because turning this into a test
would be the tool change the scope puts out. Run before either edit, since a rejection here would
have meant the bullet was imprecise rather than wrong and a much smaller correction was owed.

**Step 3 — the mapping now sits beside METHOD §6's, in the binding.** `docs/bindings/local-markdown.md`
assigns rule 5's three conditions — outcome, record, evidence — to the paths in `deliverables`, the
task file and its log, and the implement section. It states that only the first is mechanical and
that the validator returns OK on a `done` task whose implement section is untouched, which is the
belief that produced this defect rather than an aside.

**Step 4 — `CLAUDE.md` states no closing condition.** The bullet is now two links: the rule, and the
artifact mapping. It asserts nothing that could drift, and the section stays four bullets long.

**Step 5 — the whole file re-read, section by section.**

| Section | Verdict |
| :--- | :--- |
| *What this is*, *Status* | Project facts and a progress statement; no method content |
| *The one design rule* | A pointer since T-027; states the rule's name and this repository's application, not the rule |
| *Working method* — the spine size limit | About the *size* of `docs/METHOD.md`, not about anything it says |
| *Working method* — the four bullets | Three are genuine additions the method has no view on: the task folder, the schema file, the generated index. The fourth is now a route |
| *Publishing constraints*, *The pre-publish check* | Publishing and tooling; nothing from the method |
| *Verifying* | **Checked closely, judged not a restatement.** METHOD §2 makes verification `implement`'s exit criterion; this section says what counts as verification *in this repository* and adds a rule METHOD does not have — a validator is proven only by being made to fail (R-16). It constrains rather than repeats. It would become a restatement the moment it began listing METHOD's exit criteria, which is the thing to watch |

**Decisions & assumptions**
- **The mapping is not a project fact, which is why the binding is its home.** — That the outcome is
  the declared deliverables, the record is the task file and the evidence is the implement section is
  true of anyone using local Markdown files. It read as a project convention only because
  `CLAUDE.md` was where it had been written, and that misfiling is what let it drift unnoticed.
  — 2026-08-07
- **The demonstration was not kept as a fixture.** — Every `broken-*` fixture in `tests/fixtures/`
  exists because `check` is supposed to catch that class. This one is the opposite: a case `check`
  correctly does not judge. Keeping it would imply a defect in the tool and pre-empt the argument the
  scope puts out. — 2026-08-07

**Outputs produced**
- [`docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) — METHOD §1 rule 5's
  conditions assigned, beside METHOD §6's homes
- [`CLAUDE.md`](../CLAUDE.md) — §*Working method*, the `done` bullet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `CLAUDE.md` no longer states a closing condition that differs from `docs/METHOD.md` §1 rule 5 | met | It states no closing condition at all, which is the stronger form: the bullet is two links and contains no condition that could differ from anything. |
| The `implement`-evidence clause is reachable from `CLAUDE.md` in one link, or is stated there correctly — a fix that drops the sentence without replacing the route does not count | met | One link to `docs/METHOD.md` §1 rule 5, where the clause is stated, and a second to the binding for what satisfies it here. The route is now more specific than the one it replaced, which named no rule at all. |
| `CLAUDE.md`'s "if you find it written out somewhere else, that copy is the defect" sentence is true of the whole file, checked by re-reading the file and not only the edited line | met | Re-read whole, seven sections judged in the table above. The one that needed real thought is *Verifying*, which is adjacent to METHOD §2 and turns out to add a rule rather than repeat one. Checked this way deliberately: T-027 met its version of this criterion against the section it had edited, and missed the line that became this task. |
| If the local mapping moves to `docs/bindings/local-markdown.md`, that binding says it once and `CLAUDE.md` points there | met | It moved, the binding says it once, in the paragraph that already assigns METHOD §6's homes, and `CLAUDE.md` points at it by name. |

Four met, none carried. The defect was demonstrated before it was fixed rather than argued from
reading — a `done` task that recorded nothing passed the validator, exit 0 — and what replaced it
asserts nothing, so there is no second copy left to drift.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Four criteria met, none carried. The defect was demonstrated before anything was written: a throwaway project outside the tree, one task at `done` with the implement section still the template placeholder and no log or review at all, and `check --root` returned **OK, exit 0**. Ordered that way on purpose — a rejection would have meant the bullet was imprecise rather than wrong and a smaller correction was owed. The mapping went to `docs/bindings/local-markdown.md` rather than being corrected in place, on the ground that decided the task: it is **not a project fact**. That the outcome is the declared deliverables, the record is the task file and the evidence is the implement section is true for anyone using local Markdown files, and it read as a local convention only because `CLAUDE.md` happened to be where it was written — which is why nobody noticed it losing a clause. Correcting it in place was rejected as fixing the instance and not the defect: an accurate copy still drifts the next time METHOD §1 rule 5 is sharpened, which is exactly how this one arrived. `CLAUDE.md` now states no closing condition at all, so there is nothing left that could differ. Criterion 3 was checked by re-reading all 140 lines rather than the diff — the reason this task exists is that T-027 checked its version against the section it had edited — and the section that needed real thought was *Verifying*, which sits next to METHOD §2 and turns out to add a rule (a validator is proven only by being made to fail) rather than repeat one. |
| 2026-08-07 | → planned | Five steps, with the demonstration second and both edits after it. `specify` was at `proposed`: its criteria were written when T-027's review raised this and never separately agreed, and the instruction to plan through fix is taken as that agreement, as for T-027, T-037 and T-042. The open question — which of the two homes takes the local mapping — was `plan`'s to answer and is answered in the shape decision. |
| 2026-08-07 | → proposed | Raised by T-027's review and not fixed there (METHOD §5), because T-027's scope was one section of `CLAUDE.md` and this is a different one. Found only because criterion 3 makes a claim about *the file*, so it was checked against the file. `business_value: high` and `effort: xs`: one bullet, and what it currently licenses is closing a task with `## 3. Implement` still holding the template placeholder, which is the failure R-4 exists to prevent. |
