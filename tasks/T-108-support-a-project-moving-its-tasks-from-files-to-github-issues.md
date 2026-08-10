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
effort: xl
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

**And the migration is not finished when the issues exist.** Added by the maintainer, 2026-08-10:
once a move succeeds, the project is **told what taskmd still gives it** on top of GitHub's own issue
management — and if that is not enough, or if it collides with another task-management skill already
installed on the device, taskmd **offers to remove one or the other** so the issue tracking is left
efficient rather than doubled.

This is the unusual half of the task and it should not be softened into a summary line. It commits
taskmd to naming the point at which it stops earning its place, which is the honest version of a
storage-neutral method: if the method is what matters and the backend is now GitHub, a project should
not also be running a second tracker's habits out of momentum. Note the shape of the answer before
specifying it — **the four commands are local-Markdown only**. `context`, `index`, `check` and `list`
read a folder of task files; after the move there is no folder, so what remains is the method, the
binding, and the skill that routes an agent through them. Whether that is worth keeping is the
question the listing has to let someone answer, and it is a real question rather than a rhetorical
one.

**Requirements served**
R-13 and R-14 (`docs/SCOPE.md`) — changing backend changes the binding and not the method, which is
the claim a migration would exercise end to end rather than one binding at a time. R-10 and R-15 are
what the source side rests on.

**Scope**
- In: **what taskmd still provides once the tasks live in GitHub**, listed for the migrated project
  rather than left to be inferred — which parts keep working, which stop applying, and what the
  method is still worth when the folder is gone.
- In: **the offer to remove one or the other**, when what remains is not enough or collides with
  another task-management skill on the device. Its trigger, its wording, and what it must never do —
  removal is the person's action, never taskmd's.
- In: whether non-goal 8 is amended, and how narrowly — Q1, **answered**.
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
- [x] Non-goal 8 is amended or the task is cancelled — recorded either way, with the alternative.
      **Met at `specify`, 2026-08-10**: amended narrowly, original text kept beside it
- [ ] A real project's backlog is moved and the result **checked against the source**: same task
      count, same edges in both directions, bodies intact, and every `T-NNN` reference resolving to
      the issue that replaced it
- [ ] Shown failing first on at least one class it must catch — a dropped edge, or a reference left
      pointing at a task id that no longer exists — per `CLAUDE.md` *Verifying*
- [ ] taskmd makes no network call; the agent does, and the division is visible in what ships
- [ ] The procedure is written where an adopter meets it, not only in this task record
- [ ] Whether the reverse direction is supported is stated, yes or no
- [ ] **The migrated project is told what taskmd still provides** — as a list of what keeps working
      and what stops applying, checked against the four commands actually being local-Markdown only,
      rather than as a claim about value
- [ ] **The removal offer is made when it should be**, shown on a case: what remains is not enough,
      or another task-management skill on the device overlaps it. Demonstrated, not described
- [ ] The offer never removes anything itself, and says plainly which of the two it is proposing to
      drop and why — a tool judging its own worth must show the facts it judged on

**Open questions**
- **Q1 — is non-goal 8 amended? — yes, narrowly. Answered by the maintainer, 2026-08-10**, and
  carried out: `docs/SCOPE.md` non-goal 8 now scopes **local Markdown → GitHub Issues in, everything
  else out**, with the original text kept beside it. Importing a foreign backlog stays v1, continuous
  two-way sync stays out, and non-goals 5 and 11 are untouched. *Rejected: leave it and cancel this
  task until v1* — defensible while nothing was blocked on it, and overtaken by the clause's own
  condition being met.
- **Q2 — what does taskmd ship, given it cannot make the calls? — an export the agent drives, plus a
  documented two-pass procedure in the GitHub binding. Answered by the maintainer, 2026-08-10.** It
  keeps the network boundary intact and puts the judgement in the binding, where every other backend
  instruction already lives. *Rejected: procedure only, no code* — it leaves the two-pass id rewrite
  to be done by hand on every reference, which a hundred-task backlog makes unreasonable.

  **The export may already exist, which `plan` should test before writing anything.** `list --json`
  emits every task with its configured columns and every edge in both directions; what it does not
  emit is bodies, and the local-Markdown binding's *read* is *open the file*. So the agent may have
  both halves already, and this may cost no code and no fifth command — which is the outcome that
  leaves non-goal 11 untouched rather than argued with.
- **Q3 — who inspects the device for other task-management skills, and how is the answer honest?**
  Raised by the requirement below, and not answered here. taskmd's code must not scan a machine — the
  agent can see what its harness serves, and that is the same division Q2 just drew. The harder half
  is bias: a tool assessing whether it still earns its place has an obvious interest in the answer.
  *No recommendation yet.* Whoever specifies this should consider stating **facts** — which commands
  still work, which stop applying, what overlaps what — and leaving the verdict to the person, rather
  than issuing one.

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
| 2026-08-10 | (no change) | **Both open questions answered by the maintainer, and one carried out.** **Q1 — non-goal 8 amended, narrowly**: `docs/SCOPE.md` now scopes local Markdown → GitHub Issues **in** and keeps everything else out, with the original wording preserved beside it in the style non-goal 11's 2026-08-05 amendment set. Importing a foreign backlog stays v1, continuous two-way sync stays out, and non-goals 5 and 11 are explicitly left untouched by the carve-out. The first acceptance criterion is therefore met at `specify`, which is unusual and is marked as such. **Q2 — an export the agent drives, plus a documented two-pass procedure in the GitHub binding.** Recorded with it, for `plan` to test before writing code: the export may already exist, since `list --json` emits every task with its edges in both directions and the binding's *read* is *open the file* — so the agent may hold both halves already, and this may cost no new command at all, which is how non-goal 11 stays untouched rather than argued with. **A requirement was also added**, and it is the unusual half: once a migration succeeds the project is told what taskmd still gives it over GitHub's own issue management, and if that is not enough — or if it collides with another task-management skill installed on the device — taskmd **offers to remove one or the other**, so the tracking is left efficient rather than doubled. Two facts recorded so `specify` does not meet them late: the four commands are **local-Markdown only**, so after the move what remains is the method, the binding and the skill; and a tool assessing whether it still earns its place has an obvious interest in the answer, which is now **Q3** — unanswered, with the shape of an honest answer sketched as *state the facts, leave the verdict*. Effort **l → xl**: a two-pass migration with verification was already `l`, and a post-migration capability listing plus a removal offer is a second deliverable with its own criteria. Worth splitting at `plan` if it does not shrink. **Status unchanged** — the questions are answered but the criteria are not agreed, and `specify` closes on agreement rather than on activity. |
| 2026-08-10 | → proposed | Raised at the maintainer's request after they asked whether taskmd is prepared for this move. It is not, and not by accident: `docs/SCOPE.md` non-goal 8 defers migration tooling to v1. **The task is raised anyway, with the conflict as Q1 rather than resolved inside it**, because a task that quietly implements against a written boundary makes the boundary meaningless. The argument for amending is in the clause itself — it defers the work *until the method and both bindings are proven*, and both now are, T-010 having walked the GitHub binding on a live repository and T-041 having proven its body-rewrite rule by making it fail. `high` because the maintainer asked and because it is the first capability the project has deliberately withheld from adopters; `l` because assumption 1 of the GitHub binding makes this inherently two-pass — ids are assigned by GitHub, so every reference in every edge, body, deliverable path and project document must be rewritten to a number that does not exist until the issue is created. Two other non-goals were checked and neither is in the way: 5 keeps the network out of the core, which the request already respects by asking for a script that *supports* an agent, and 11 keeps the CLI at four commands, so this is not a fifth. |
