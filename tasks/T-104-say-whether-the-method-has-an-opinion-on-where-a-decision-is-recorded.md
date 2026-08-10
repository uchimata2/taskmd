---
id: T-104
title: Say whether the method has an opinion on where a decision is recorded
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-008, T-088, T-103]
work_package: v0.3
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-104 — Say whether the method has an opinion on where a decision is recorded

## 1. Specify

**Outcome**
A project that keeps a decisions register is told whether taskmd considers `type: decision` the home
for a decision and the register a view of it, or whether taskmd has no opinion — so the project is
choosing rather than guessing it has missed something.

**Why this one**
Raised as **R-6** by the first adopting project (`control/LOCAL-CONTEXT.md`). The shipped `type`
vocabulary carries `decision`; `METHOD.md` never mentions decisions. That project already kept a
`tasks/DECISIONS.md` with its own generated view, and after migrating it had both — `type: decision`
tasks *and* a register — with no rule saying which holds what. `context <id>` shows the task and not
the register, so the register is read by hand.

**What it cost.** A standing exception in the project's own configuration, documenting that one
question the tool cannot answer must be looked up elsewhere. That is a second procedure to remember,
which is the thing *one home per fact* exists to prevent.

**The honest counter, which `specify` must weigh rather than skip.** The shipped schema's
*Vocabularies* section already addresses this, and names this exact value: *"These are defaults worth
having, not the set of nouns METHOD uses. `decision` is here and the method never mentions it."* So
the silence is deliberate and it is written down — **one level away from where an adopter meets the
question**, in the schema they copied on day one and are unlikely to reread. The question is not
whether taskmd has thought about it. It is whether a note in the config discharges the duty, or
whether the method owes a sentence at the place a project decides how to record decisions.

**Requirements served**
R-1 (`docs/SCOPE.md`) — one home per fact, applied to a kind of fact the method does not currently
place. R-9, since decision registers are commonest in exactly the non-software work the method claims
to serve.

**Scope**
- In: one paragraph, in METHOD §6 or `method/where-facts-live.md`, saying where a decision lives — or
  saying explicitly that taskmd has no opinion and why.
- In: if the answer is `type: decision`, whether a register is then a **view** of those tasks, and
  what that implies for a project that maintains one by hand.
- Out: a `decision` **edge kind**. The three kinds are fixed and each is a different traversal; this
  is about where a fact is recorded, not about a fourth relationship.
- Out: a command that generates a register. Non-goal 11, and a project's own view is its own to
  generate.
- Out: changing the `type` vocabulary. `decision` stays whatever the answer is.

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §6 and `docs/method/where-facts-live.md`.
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Vocabularies*, the paragraph that already names
  `decision` as the deliberate mismatch.
- The first adopting project's register and the standing exception it wrote, per
  `control/LOCAL-CONTEXT.md`.

**Acceptance criteria**
- [ ] The answer is written once, and an explicit silence counts as an answer if that is what it is
- [ ] It is placed where a project deciding how to record decisions will actually meet it, which the
      config note is not
- [ ] A decision recorded inside a task's `implement` section — which is how this repository does it,
      and which the template prompts for — is reconciled with the answer rather than contradicted
- [ ] Nothing else in the tree ends up stating a second version of it
- [ ] `check` is clean on this repository

**Open questions**
- **Does taskmd have an opinion at all?** *Recommended: yes, and it is `type: decision` plus a
  register-as-view.* A project that has both stores the same fact twice, which is the one thing this
  method forbids, and refusing to say so leaves every adopter to invent the rule.
  *Alternative: an explicit no.* The method is deliberately storage-agnostic and decision records are
  a governance convention rather than a lifecycle fact; saying so plainly still tells an adopter they
  are choosing. Note that this repository records decisions **inside the task that took them**, in
  §3, and that is a third answer already in use here — whichever way this goes, it has to account for
  that rather than leave it as a fourth practice.

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
| 2026-08-10 | → proposed | Raised as R-6 from the first adopting project's recommendations, which ended up running two systems — `type: decision` tasks and its own register — and wrote a standing exception into its configuration saying so. `medium` because the cost is a remembered second procedure rather than a wrong answer, and because a partial answer already exists; `s` because it is a paragraph. The partial answer is recorded here so `specify` does not present itself with a blank page: the shipped schema's *Vocabularies* section already names `decision` as a value the method never mentions and calls that deliberate. The live question is narrower than R-6 states — not *does taskmd have an opinion*, but *does a note in the config file discharge it*, given that a third practice, recording decisions inside the task that took them, is what this repository itself does. |
