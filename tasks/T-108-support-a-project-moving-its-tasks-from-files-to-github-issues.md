---
id: T-108
title: Support a project moving its tasks from local files to GitHub Issues
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-004, T-009, T-010, T-041, T-082, T-163]
work_package: M6
owner: maintainer
business_value: high
effort: l
created: 2026-08-10
updated: 2026-08-17
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
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

**The migration is not finished when the issues exist, and that half is now
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md).** The maintainer added it here
on 2026-08-10 — once a move succeeds the project is told what taskmd still gives it, and can drop
whichever of the two overlapping tools it does not want. It left this task on 2026-08-17 by Q4, with
its full statement and its criteria, because it is a second outcome and not a clause of this one. It
is soft-linked and not a blocker: what taskmd still provides once the folder is gone is a fact about
today's CLI.

**Requirements served**
R-13 and R-14 (`docs/SCOPE.md`) — changing backend changes the binding and not the method, which is
the claim a migration would exercise end to end rather than one binding at a time. R-10 and R-15 are
what the source side rests on.

**Scope**
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
- Out: **what taskmd still provides after the move, and the removal path** —
  [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md), split out on 2026-08-17.

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
- **Q3 — who inspects the device for other task-management skills, and how is the answer honest?
  Answered 2026-08-17, and the work it governs is now
  [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md).** Kept here because it was
  raised, argued and settled in this record, and because it is what removed three of this task's
  criteria. taskmd's code must not scan a machine — the
  agent can see what its harness serves, and that is the same division Q2 just drew. The harder half
  is bias: a tool assessing whether it still earns its place has an obvious interest in the answer.

  **Answered by the maintainer, 2026-08-17: taskmd states facts and names no side.** The division is
  the one Q2 drew.
  The agent enumerates what its harness serves, because it can see that and taskmd's code must not
  scan a machine. taskmd supplies the half only it knows: which of its own commands stop applying —
  all four read a task folder that no longer exists — and what survives, which is the method, the
  binding, and the skill that routes an agent through them. The person reads both halves and decides.

  **It falsified this task's ninth acceptance criterion**, which required the offer to *say plainly
  which of the two it is proposing to drop*. Naming a side **is** the verdict this question's own
  sketch says to withhold, and it is the single judgement the tool is least able to make honestly.
  That criterion did not survive the answer: it is replaced, in
  [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md), by *names neither side, shows
  the facts each half rests on*. The *demonstrated, not described* criterion beside it was unaffected
  and moved intact.

  *Rejected: taskmd names a side and justifies it.* It reads as decisive and is the same
  self-interested judgement at greater length — a tool concluding *keep me* is unfalsifiable to the
  reader, and one concluding *drop me* is not more trustworthy for being self-denying.
  *Rejected: the agent issues the verdict instead.* The same bias one step removed; the agent reaches
  the question by running taskmd's own skill.

- **Q4 — is this one task or two? Two. Answered by the maintainer, 2026-08-17, and carried out**:
  [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md). The evidence was inside this
  record: the **Outcome** paragraph above described only the migration, while criteria 7, 8 and 9
  judged a second deliverable — what taskmd still provides after the move, and the removal offer. A
  `specify` whose stated outcome does not cover a third of its own criteria cannot be agreed as one
  thing, and the criteria partitioned cleanly: 2–6 the migration, 7–9 the listing and the offer, none
  of the nine spanning both. Effort **xl → l**, reversing the 2026-08-10 raise that the second
  deliverable caused.

  The two are also not blocked on each other. What taskmd still provides once the folder is gone is
  knowable today — *the four commands are local-Markdown only* is a fact about the current CLI, not
  about a completed migration. So the second task takes a **soft** edge and not a dependency
  ([`../plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4).

  *Rejected: keep one task and widen the Outcome to cover both.* It leaves an `xl` task whose
  `review` judges nine criteria across two deliverables, and the 2026-08-10 log row already flagged
  the split as likely; deferring it to `plan` moves the same decision later, after a plan has been
  written against the wrong boundary.
  *Rejected: drop the second deliverable and leave it unraised.* The 2026-08-10 row requires it not
  be softened into a summary line, and an unraised deliverable is softer than a summary line.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Test whether the export already exists.** Run `list --json` over this repository's own tasks and check it against what a migration needs: every task, every field the schema names, and both directions of every edge. It decides whether steps 3–4 write code or nothing, so it goes first | A recorded decision in §3 — export sufficient / insufficient — with the command run and what was missing |
| 2 | **Name where each issue body comes from.** `list --json` does not emit bodies and the local binding's *read* is *open the file*, so the agent already holds both halves or it does not | A recorded decision naming the source of each half |
| 3 | **Write the two-pass procedure** into the GitHub binding: pass 1 creates in an order that lets `--parent` and `--blocked-by` be set at creation, pass 2 rewrites every `T-NNN` and every relative task link to the issue that replaced it | A new section in `plugin/skills/taskmd/docs/bindings/github-issues.md` |
| 4 | **Write what stops a one-pass attempt** — the id mapping exists only between the passes, and a body written in pass 1 cannot name an issue that does not exist yet | A paragraph in that section, naming the failure rather than the rule |
| 5 | **Write the verification**: what "the move worked" means as a comparison between source and destination — task count, both directions of every edge, bodies intact, every reference resolving | The verification, in the same section |
| 6 | **Answer the reverse direction**, yes or no, with the reason. Non-goal 8's amendment scopes one direction in; this step states plainly whether the other is refused or merely unbuilt | A stated answer in the binding and in §3 |
| 7 | **Prove the procedure end to end on a scratch repository**, then run the verification against it. **This creates real issues on a real account and is asked for separately** — see the decision below | A transcript in §3, and the verification's output |
| 8 | **Make the verification fail first**, on two classes it must catch: an edge dropped between the passes, and a reference left pointing at a task id that no longer exists | Two failing runs recorded in §3, before the passing one |
| 9 | **Check that no taskmd code touched the network**, by naming what ran in each pass and which side ran it | A statement in §3 |

**Decisions taken at `plan`**

- **The procedure's home is the GitHub binding, not a new document** — 2026-08-17. Q2 already put the
  judgement there, and the binding is what a project on this backend reads. *Rejected: a migration
  document of its own*, which adds a file to find and splits the backend's instructions across two
  homes. *Rejected: `README.md`*, which is read before adopting rather than while moving.
- **The proof runs on a scratch repository, never on this project's backlog or on
  `github.com/uchimata2/taskmd`** — 2026-08-17. Criterion 2 asks for a real backlog moved, not for
  this one: 163 issues on the published repository is irreversible, public, and would bury the
  repository's real issues. *Rejected: migrate this repository's tasks*, which is the reading that
  makes the criterion destructive rather than demanding. *Rejected: a mocked `gh`*, which proves the
  script and not the migration — `CLAUDE.md` *Verifying* asks for the thing run on a real case.
- **Creating that repository and its issues is asked for at the point of running it** — 2026-08-17.
  The lifecycle authorisation of the same day covers the phases of this task; it is not permission to
  create public artefacts on the maintainer's GitHub account, and `gh` being authenticated is a fact
  about the machine rather than a grant.

**Outputs this task will produce**

- plugin/skills/taskmd/docs/bindings/github-issues.md — the migration section, its verification, and
  the reverse-direction answer
- the transcripts and decisions in §3 of this record

## 3. Implement

**Steps 1–6 are done. Steps 7–9 are stopped at an approval, not at a difficulty** — see the boundary
below.

**Step 1 — the export does not already exist, and it cannot be made to without damage.** Measured
2026-08-17 against this repository's own tasks:

```
taskmd list --json --limit 1
  → id, title, work_package, status, phase,
    parent, children, blocked_by, blocks, related, blocked, open
```

`list --json` emits `id`, `title`, **the columns `index_columns` names**, and both directions of every
edge. Running the shipped default (`index_columns: [work_package, status, phase]`), five schema-named
fields never reach it — `type`, `owner`, `business_value`, `effort`, `deliverables` — and neither does
any body. On the destination side those five are not optional: three are enumerated and become labels,
two become property-block lines.

**So Q2's hope is half right and the half that fails is the useful half.** The export the agent needs
is not a taskmd output at all: it is
[`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)'s *read*, which is
*open the file* and returns front-matter and body together. The agent already holds it. **No new code,
no fifth command, and non-goal 11 is untouched rather than argued with** — which was the outcome Q2
wanted, reached by a different route than it expected.

*Rejected: widen `index_columns` until the export is complete.* It works, and it changes what every
reader's index shows in order to feed a migration that runs once. A view bent to serve a contract is
the wrong artefact carrying the requirement.

**Step 1 also found `list --json` a job it is better at.** Being derived by the tool rather than by
whatever read the files, it is an independent second opinion for *Verify* — the inverse edges in
particular, which the file side does not store at all. Comparing a file-derived reconstruction against
a tool-derived one is a real check; comparing either against itself is not.

**Step 2 — each half named.** Front-matter and body both come from the files, in one read. Nothing
else is needed and nothing else is used.

**Steps 3–6 — written into the binding, not here.**
[`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md),
section *Moving a project here from local Markdown*: why one pass is impossible, what to read, the two
passes, the verification table, and the reverse-direction answer.

**The suite caught the section citing something the plugin does not ship.**
`test_no_file_in_the_plugin_cites_something_it_does_not_ship` failed on one sentence of the
reverse-direction answer, which justified the refusal by pointing at a non-goal — and the document
holding the non-goals is outside `plugin/`, so an adopter receives the citation and not its referent.
Rewritten to stand on its own. Worth recording rather than quietly fixing: **the reasoning that
produced the sentence was sound and the sentence was still unshippable**, because the boundary of what
an adopter receives is not visible from inside the argument. The gate is, which is what it is for.

**Step 6's answer is no, and it is a refusal rather than a gap.** Non-goal 8 as amended scoped one
direction in. The technical half is recorded with it: coming back means *composing* ids rather than
receiving them, so every `#N` in every body is rewritten to an id somebody must allocate — the same
two-pass problem plus a numbering policy that belongs to the project. What is not refused is leaving,
and the binding says so: the issues are the project's, and `gh issue list --state all` returns them
whole.

**Decisions & assumptions**

- **The migration reads the files, not `list --json`** — 2026-08-17, on the measurement above. The
  rejected alternative and why it is worse are recorded with step 1.
- **Pass 1 creates in an order where every task's `parent` and `blocked_by` targets already exist** —
  2026-08-17. Hierarchy is a tree and dependencies are acyclic, so such an order exists, and it lets
  the binding's own *create* be used unchanged with the edges native at creation. *Rejected: create
  everything edgeless, then add edges in pass 2* — simpler to write, and it invents a second creation
  path for the one case where the whole backlog is in flux, which is when a dropped edge is hardest to
  notice.
- **Pass 1 leaves every `T-NNN` in the body untouched** — 2026-08-17. A body rewritten against a
  partial mapping is worse than one not rewritten, because it looks done. The mapping exists only
  between the passes, which is the reason there are two.

**Steps 7–8 — the procedure was run end to end, on 2026-08-17.** The maintainer approved a **private
scratch repository** that day, after being asked; `gh` had been authenticated here throughout and was
deliberately not read as permission. Destination `uchimata2/taskmd-migration-proof`, private, created
for this and disposable. Source: this repository's own 165 tasks — a real backlog with real hierarchy,
dependencies, soft links and cross-references, which is what criterion 2 asks for.

The migration script is **outside the repository** and is not shipped. taskmd ships the procedure, not
code: the script imports nothing from taskmd and calls no taskmd command, which is criterion 4 held
structurally rather than promised.

Sequence, with what each run said:

| Run | Result |
| :--- | :--- |
| labels | 28 created, one per vocabulary value |
| pass 1 | 165 issues, dependency order, `--parent` and `--blocked-by` native at creation |
| **verify, mid-migration** | **FAIL (324)** — count and native edges already correct, every `Related` line and every body reference still unrewritten |
| pass 2 | 165 bodies rewritten |
| verify | FAIL (8) — **all eight spurious**; see the finding below |
| verify, rule corrected | **PASS** — count, parent, blocked_by, related, bodies, no dangling reference |
| break-edge + break-ref | `blocked_by [1] != []`, and `T-004 did not become #3` / `was left unrewritten` ×4 — **FAIL (13)** |
| repair, then verify | **PASS** |

**The mid-migration failure was not planned and is the more convincing of the two.** Running the
verification between the passes shows it rejecting a state that is half-correct — every issue created,
every native edge right, every reference dead — which is exactly the state a one-pass attempt leaves
behind and calls finished.

**The finding: the verification rule I had written into the binding was wrong, and only running it
showed that.** It checked references by **shape** — *no `T-NNN` survives*, *every `#N` names an
issue*. Both are the obvious rule and both are false. Task bodies carry illustrative ids that never
named a task (`T-404`, `T-999`) and bare numbers that were never references (`#1024` as an example
id, an external tracker's `#13057`). Eight failures, all eight spurious, and the state they invite is
worse than the false alarm: the next move is to "repair" prose that was correct. **A reference is an
id that named a real task in the source**, so the check is computed from the source's id set and
everything else in the destination is text. The binding now says so, and says why the obvious rule is
the wrong one.

**A second correction the run forced.** `blockedBy`, `blocking` and `subIssues` return
`{"nodes": [...], "totalCount": N}` rather than lists. The binding named the fields and not their
shape; reading them as lists raises a type error, which is the harmless way for it to fail. Recorded
in the binding beside the verification that reads them.

**One fidelity loss, stated rather than hidden.** A relative link carrying a section anchor loses the
anchor: a task file has headings, an issue body does not. The binding says to accept it rather than
invent a target.

**Step 9 — no taskmd code touched the network.** What ran: `gh` (agent side) and a scratch Python
script that reads files and shells out to `gh`. What did not run: any taskmd command, at any point in
either pass. The four commands cannot reach a network and were not asked to.

**The destination is gone, and the evidence is not.** `uchimata2/taskmd-migration-proof` was created
for this task and **deleted by the maintainer on 2026-08-17**, the same day, which is what a scratch
destination is for. What the runs proved is in the table above and in §4; **it cannot be re-checked
by inspecting the repository, and never could be** — a migration is verified while it runs, by the
comparison the procedure ends with, and a destination left standing would have been a second copy of
an answer this record already holds. Anyone doubting the result runs the procedure again rather than
reading the artefact.

**Outputs produced**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — section *Moving a project here from local
  Markdown*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Non-goal 8 amended or the task cancelled, recorded either way | met | Met at `specify` 2026-08-10; **re-checked against `docs/SCOPE.md` on 2026-08-17** rather than trusted, and the amendment is there with the original beside it |
| A real backlog moved and checked against the source — count, edges both ways, bodies, every reference resolving | met | 165 tasks → 165 issues, `PASS` on all five checks. §3 carries every run, including the ones that failed |
| Shown failing first on at least one class it must catch | met | **Three** failing states recorded, not one: mid-migration (324), the spurious-rule state (8), and the deliberate breaks (13). The dropped edge exited 0, as the binding warns |
| taskmd makes no network call; the division is visible in what ships | met | The script is outside the repository and imports nothing from taskmd. What ships is the procedure. §3 step 9 names what ran |
| The procedure is written where an adopter meets it, not only in this record | met | The binding, *Moving a project here from local Markdown* |
| Whether the reverse direction is supported is stated, yes or no | met | **No**, with the reason, in the binding and in §3 |

**The second criterion was met by a rule that had to be corrected mid-review**, and that is worth
more than the tick. The verification shipped in this task's own deliverable was wrong when first
written — it checked references by shape and produced eight false failures on a real corpus. A clean
first run would have hidden it, because the wrong rule passes on any body whose prose happens to
carry no illustrative id. `CLAUDE.md`'s *Verifying* rule is what caught it: the validator was only
proven once it had been made to fail, and the first failure it produced was its own.

**Child fix tasks raised**
- none. The two corrections the run forced were to this task's own deliverable, inside its boundary,
  and are recorded in §3 rather than deferred.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **§3's statement of the `list --json` contract is superseded, and annotated rather than edited** (METHOD rule 5). It reads *`list --json` emits `id`, `title`, **the columns `index_columns` names**, and both directions of every edge* — true when written and measured on 2026-08-17. Since [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) on **2026-08-22** it emits every field `list` accepts as a **filter**, so `type`, `owner`, `business_value` and `effort` now reach it; `deliverables` still does not, because nothing filters on it. **The conclusion this record drew is unchanged and its reason is sharper**: `list --json` is still not the export, because it carries no **body**, and no schema change reaches that. The rejection of *widen `index_columns`* also stands — T-217 widened the machine form and left the human index alone, which is what that rejection asked for. The shipped sentence in `github-issues.md` §*What to read* was corrected there. |
| 2026-08-17 | (no change) | **The scratch destination was deleted by the maintainer**, hours after this task closed. §3's claim that it still existed was true when written and false by the end of the day, so it is corrected in place — METHOD rule 5 applied to the present, while the row below keeps what was true then. **Nothing was lost with it**: the proof is the comparison the procedure ran, recorded here, and the repository was never the evidence. Worth stating outright because a closed task naming a destination that no longer resolves invites a later reader to conclude the run was undone. |
| 2026-08-17 | → done | `implement` finished and `review` run, closing the lifecycle the maintainer authorised the same day. **The migration was proved on a real backlog**: this repository's 165 tasks into a private, disposable `uchimata2/taskmd-migration-proof`, approved separately after being asked, because `gh` being authenticated here is a fact about the machine and not a grant. All six criteria met. **The result worth keeping is not the passing run.** The verification this task shipped was **wrong when first written** — it checked references by lexical shape, and a real corpus produced eight false failures on prose carrying illustrative ids (`T-404`, `T-999`) and bare numbers that were never references (`#1024`, `#13057`). The rule now computes from the source's own id set, and the binding says why the obvious rule is the wrong one. A clean first run would have shipped the defect, which is the whole of `CLAUDE.md` *Verifying* in one instance: the validator was proven only once made to fail, and its first failure was its own. Three failing states are on record, not one — mid-migration (324), the spurious rule (8), the deliberate edge and reference breaks (13, with `gh` exiting 0 on the destructive edit exactly as the binding warns). Two corrections were forced back into the shipped procedure: the `{"nodes": […]}` shape of `blockedBy`/`blocking`/`subIssues`, and the anchor a rewritten link cannot keep. The scratch repository still exists; deleting it is the maintainer's. |
| 2026-08-17 | → in_progress | `implement` steps 1–6 done, **stopped at step 7's approval and not at a difficulty**. Step 1 paid for its position at the front: `list --json` is **not** the export — it is a view contract driven by `index_columns`, so `type`, `owner`, `business_value`, `effort` and `deliverables` never reach it, and neither do bodies. Q2 hoped the export already existed; it does, but it is [`local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)'s *read* — *open the file* — which the agent already has. **The result Q2 wanted holds by a different route: no code, no fifth command, non-goal 11 untouched.** *Rejected: widening `index_columns` until the export is complete*, which bends every reader's index to feed a migration that runs once. Step 1 also gave `list --json` a better job — as a tool-derived second opinion in *Verify*, since the file side stores no inverse edges at all, so the check compares two independent reconstructions rather than one against itself. The procedure, its verification and the reverse-direction refusal are in the binding. **Steps 7–9 create real issues on a real account**; `gh` is authenticated here and that is deliberately not read as permission, so they wait on a request made separately. |
| 2026-08-17 | → planned | `plan` written, nine steps. **Step 1 is placed first because it can invalidate steps 3 and 4**: if `list --json` already emits every task with both directions of every edge, this task writes no code and non-goal 11 is untouched rather than argued with, which is the outcome Q2 hoped for. Three decisions recorded with their rejections: the procedure's home is the **GitHub binding**; the proof runs on a **scratch repository**, never on this backlog or on the published one, because 163 public issues is the reading that makes criterion 2 destructive rather than demanding; and **creating that repository is asked for at the point of running it**, since the day's lifecycle authorisation covers this task's phases and is not a grant to create public artefacts on the maintainer's account. `gh` is installed and authenticated here — recorded as a fact about the machine, and deliberately not read as permission. |
| 2026-08-17 | → specified | **The six remaining criteria were agreed by the maintainer**, which is what `specify` closes on, so the phase is complete. **The maintainer authorised the whole lifecycle in the same request** — `specify` → `plan` → `implement` → `review` — covering **T-108 and [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) and nothing else**: no other task, and nothing either of these two raises, which takes one phase per request unless separately authorised (METHOD §3.1). Recorded in both records rather than in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a task it never reached. **One thing `plan` must not discover late**: criterion 2 requires a real backlog moved into real GitHub Issues, which is an outward-facing action on a public account and is not covered by this authorisation — `gh` being installed and authenticated is not permission to create issues. It is asked for separately, at the point of running it. |
| 2026-08-17 | (no change) | **Q3 and Q4 both answered by the maintainer the same day, and both carried out.** **Q3 — taskmd states facts and names no side**: the agent enumerates what its harness serves, taskmd supplies the half only it knows, and the person decides. *Rejected: taskmd names a side and justifies it*, and *the agent issues the verdict instead* — both recorded on Q3 with why. **Q4 — two tasks**, joined by a **soft** edge: [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) now holds what taskmd still provides after the move and the removal path. Criteria 7 and 8 moved intact; **criterion 9 did not survive Q3** and is replaced there by *names neither side, shows the facts each half rests on*, plus a reader test. The 2026-08-10 requirement paragraph went with it, leaving a pointer rather than a summary — it is a second outcome, not a clause of this one. Effort **xl → l**, reversing the raise the second deliverable caused. **Status still `proposed`**: the two blockers are gone, and the six remaining criteria have never been agreed by the owner, which is the only thing `specify` closes on. |
| 2026-08-17 | (no change) | `specify` resumed at the maintainer's request, one phase. **Criterion 1 was re-checked against its source rather than trusted**: `docs/SCOPE.md` non-goal 8 does carry the narrow amendment with the original wording preserved beside it, so the tick is earned. Two things were found that stop this phase closing, and both are questions rather than edits because each changes what the task produces. **Q3 now carries a recommendation** — taskmd states facts and names no side — and recording it exposed a contradiction that was already in the record: **acceptance criterion 9 requires the offer to name which of the two to drop**, which is exactly the verdict Q3's own sketch says to withhold. One of the two has to give, and which is the owner's. **Q4 is new**: the **Outcome** paragraph describes only the migration while criteria 7–9 judge a second deliverable, so a third of the criteria sit outside the stated outcome. Recommended split into two tasks joined by a **soft** edge, since what taskmd still provides after the move is knowable today and is not blocked on a migration having happened. **Status unchanged and no criteria rewritten** — `specify` closes on the owner's agreement, and rewriting criterion 9 before Q3 is answered would settle the question by editing it. |
| 2026-08-10 | (no change) | **Both open questions answered by the maintainer, and one carried out.** **Q1 — non-goal 8 amended, narrowly**: `docs/SCOPE.md` now scopes local Markdown → GitHub Issues **in** and keeps everything else out, with the original wording preserved beside it in the style non-goal 11's 2026-08-05 amendment set. Importing a foreign backlog stays v1, continuous two-way sync stays out, and non-goals 5 and 11 are explicitly left untouched by the carve-out. The first acceptance criterion is therefore met at `specify`, which is unusual and is marked as such. **Q2 — an export the agent drives, plus a documented two-pass procedure in the GitHub binding.** Recorded with it, for `plan` to test before writing code: the export may already exist, since `list --json` emits every task with its edges in both directions and the binding's *read* is *open the file* — so the agent may hold both halves already, and this may cost no new command at all, which is how non-goal 11 stays untouched rather than argued with. **A requirement was also added**, and it is the unusual half: once a migration succeeds the project is told what taskmd still gives it over GitHub's own issue management, and if that is not enough — or if it collides with another task-management skill installed on the device — taskmd **offers to remove one or the other**, so the tracking is left efficient rather than doubled. Two facts recorded so `specify` does not meet them late: the four commands are **local-Markdown only**, so after the move what remains is the method, the binding and the skill; and a tool assessing whether it still earns its place has an obvious interest in the answer, which is now **Q3** — unanswered, with the shape of an honest answer sketched as *state the facts, leave the verdict*. Effort **l → xl**: a two-pass migration with verification was already `l`, and a post-migration capability listing plus a removal offer is a second deliverable with its own criteria. Worth splitting at `plan` if it does not shrink. **Status unchanged** — the questions are answered but the criteria are not agreed, and `specify` closes on agreement rather than on activity. |
| 2026-08-10 | → proposed | Raised at the maintainer's request after they asked whether taskmd is prepared for this move. It is not, and not by accident: `docs/SCOPE.md` non-goal 8 defers migration tooling to v1. **The task is raised anyway, with the conflict as Q1 rather than resolved inside it**, because a task that quietly implements against a written boundary makes the boundary meaningless. The argument for amending is in the clause itself — it defers the work *until the method and both bindings are proven*, and both now are, T-010 having walked the GitHub binding on a live repository and T-041 having proven its body-rewrite rule by making it fail. `high` because the maintainer asked and because it is the first capability the project has deliberately withheld from adopters; `l` because assumption 1 of the GitHub binding makes this inherently two-pass — ids are assigned by GitHub, so every reference in every edge, body, deliverable path and project document must be rewritten to a number that does not exist until the issue is created. Two other non-goals were checked and neither is in the way: 5 keeps the network out of the core, which the request already respects by asking for a script that *supports* an agent, and 11 keeps the CLI at four commands, so this is not a fifth. |
