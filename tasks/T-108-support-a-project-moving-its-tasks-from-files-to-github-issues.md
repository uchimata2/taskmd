---
id: T-108
title: Support a project moving its tasks from local files to GitHub Issues
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-004, T-009, T-010, T-041, T-082]
work_package: v0.3
owner: maintainer
business_value: high
effort: l
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-108 — Support a project moving its tasks from local files to GitHub Issues

## 1. Specify

**Outcome**
A project running taskmd on local Markdown files can move to GitHub Issues without hand-transcribing
its backlog, and without the move silently dropping edges, bodies or history — with taskmd supplying
whatever an agent needs to do it and the agent supplying the network access.

**Why this one**
Requested by the maintainer, 2026-08-10. Today the answer is nothing: both bindings exist and each is
proven on its own, and there is no route from one to the other. An adopter's only option is to open
issues by hand and rewrite every reference, on a backlog that may be a hundred tasks.

**This contradicts a written non-goal, and that has to be settled before anything is built.**
`docs/SCOPE.md` non-goal 8 reads: *"Migration tooling (v1). Moving an existing backlog into taskmd,
or local files into GitHub Issues, is out until the method and both bindings are proven."* The
argument for amending it is inside its own wording — **that condition is now met**. Both bindings are
written; the GitHub one was walked on a live repository under
[T-010](T-010-write-the-github-issues-binding.md) and its body-rewrite rule proven by being made to
fail under [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md); and the method needed no
change to carry either. The clause deferred the work *until* a bar was cleared, not forever. It is
still an amendment, and it is the maintainer's, which is why it is Q1 below rather than an assumption
this task makes quietly.

**Two other non-goals bear on the shape and neither is in the way.** Non-goal 5 keeps network access
out of the core — the GitHub binding already says *"No taskmd code touches the network, and none is
planned to"* — so whatever this produces must leave the `gh` calls to the agent. Non-goal 11 keeps
the CLI to four commands, so this is not a fifth. The request is a **script supporting Claude Code**,
which fits both: taskmd prepares, the agent acts.

**The hard part is named now so `specify` does not discover it late.** The GitHub binding's
assumption 1: *ids are assigned by GitHub — the issue number is the task id, and you cannot know it
in advance, reserve one, or renumber.* So migration is inherently two-pass. Every `T-NNN` in an edge
field, in a body, in a deliverable path and in a project document has to be rewritten to an issue
number that does not exist until the issue is created, and the mapping only exists in between. A
one-pass script produces a backlog whose links all point at nothing.

**Requirements served**
R-13 and R-14 (`docs/SCOPE.md`) — changing backend changes the binding and not the method, which is
the claim a migration would exercise end to end rather than one binding at a time. R-10 and R-15 are
what the source side rests on.

**Scope**
- In: whether non-goal 8 is amended, and how narrowly — see Q1.
- In: what taskmd supplies. Candidates, to be chosen and not assumed: a read-only export of the task
  graph in a form an agent can drive `gh` from; a documented two-pass procedure in the GitHub
  binding; an id-mapping file the second pass consumes; a verification step that the destination
  matches the source.
- In: what "the move worked" means, and how it is checked. A migration nobody can verify is worse
  than none, because it looks finished.
- In: the reverse direction, at least as a stated yes or no. Non-goal 8 names *"an existing backlog
  into taskmd"* as well, and an adopter who cannot come back is being asked for more trust than the
  method's storage-neutrality claim implies.
- Out: taskmd making network calls. Non-goal 5, and the GitHub binding's opening paragraph.
- Out: a fifth CLI command, unless Q1's amendment explicitly buys one. Non-goal 11.
- Out: continuous two-way sync between a folder and a repository. That is a different product and
  nothing here asks for it.
- Out: migrating anything that is not a taskmd project — importing a foreign backlog is the other
  half of non-goal 8 and is not this task.

**Inputs**
- `docs/SCOPE.md` non-goals 5, 8 and 11, and R-13/R-14.
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — *Assumptions* 1–6, *Mapping*, and every operation; assumption 1 is the one that shapes the work.
- [`../plugin/skills/taskmd/docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)
  — the source side.
- [`../plugin/skills/taskmd/docs/BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §1, the six
  operations both ends must satisfy.
- [T-010](T-010-write-the-github-issues-binding.md) §3 and
  [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md) §3 — the only transcripts of these
  operations running against a real repository.

**Acceptance criteria**
- [ ] Non-goal 8 is amended or the task is cancelled — recorded either way, with the alternative
- [ ] A real project's backlog is moved and the result **checked against the source**: same task
      count, same edges in both directions, bodies intact, and every `T-NNN` reference resolving to
      the issue that replaced it
- [ ] Shown failing first on at least one class it must catch — a dropped edge, or a reference left
      pointing at a task id that no longer exists — per `CLAUDE.md` *Verifying*
- [ ] taskmd makes no network call; the agent does, and the division is visible in what ships
- [ ] The procedure is written where an adopter meets it, not only in this task record
- [ ] Whether the reverse direction is supported is stated, yes or no

**Open questions**
- **Q1 — is non-goal 8 amended?** *Recommended: yes, narrowly — local Markdown to GitHub Issues
  only, leaving "an existing foreign backlog into taskmd" out.* The clause's own condition is met,
  and the narrow half is the one with two proven bindings behind it. *Alternative: leave it and
  cancel this task until v1* — defensible, since nothing is blocked on it today and the amendment
  spends scope on a route no adopter has yet asked to take. The maintainer decides; **nothing else
  in this task can be agreed first**, because a cancelled task needs no criteria.
- **Q2 — what does taskmd ship, given it cannot make the calls?** *Recommended: an export the agent
  drives, plus a documented two-pass procedure in the GitHub binding.* It keeps the network boundary
  intact and puts the judgement in the binding, where every other backend instruction already lives.
  *Alternative: procedure only, no code* — cheaper and consistent with the GitHub binding being
  instructions rather than commands, and it leaves the two-pass id rewrite to be done by hand on
  every reference, which is the part a hundred-task backlog makes unreasonable.

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
| 2026-08-10 | → proposed | Raised at the maintainer's request after they asked whether taskmd is prepared for this move. It is not, and not by accident: `docs/SCOPE.md` non-goal 8 defers migration tooling to v1. **The task is raised anyway, with the conflict as Q1 rather than resolved inside it**, because a task that quietly implements against a written boundary makes the boundary meaningless. The argument for amending is in the clause itself — it defers the work *until the method and both bindings are proven*, and both now are, T-010 having walked the GitHub binding on a live repository and T-041 having proven its body-rewrite rule by making it fail. `high` because the maintainer asked and because it is the first capability the project has deliberately withheld from adopters; `l` because assumption 1 of the GitHub binding makes this inherently two-pass — ids are assigned by GitHub, so every reference in every edge, body, deliverable path and project document must be rewritten to a number that does not exist until the issue is created. Two other non-goals were checked and neither is in the way: 5 keeps the network out of the core, which the request already respects by asking for a script that *supports* an agent, and 11 keeps the CLI at four commands, so this is not a fifth. |
