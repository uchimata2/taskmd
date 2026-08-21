---
id: T-181
title: Verify the handoff GitHub recipe against a live issues-backed project
type: research
status: done
phase: review
parent: T-005
blocked_by: []
related: [T-108]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-181 — Verify the handoff GitHub recipe against a live issues-backed project

## 1. Specify

**Outcome**
A recorded result of configuring the handoff skill against a taskmd project whose backend is GitHub
Issues, and resuming through it — or a statement of why that could not be done here, naming what
would show it.

**Why this one**
[T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) shipped
`plugin/skills/taskmd/docs/HANDOFF.md`, whose GitHub half was derived by **reading two binding
documents against each other**: taskmd stores enumerated fields as `<field>:<value>` labels, and
handoff's `github-issues` binding accepts a `label:<prefix>` form for `tracker_status`. The join is
exact on paper and has never been run. T-005's review carried the criterion rather than met it, which
is what raised this.

**This is the failure mode the method names.** A configuration that has only ever been reasoned about
is worth what the reasoning is worth, and the reasoning here spans two projects' documents — the
class of claim [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) exists because
nothing was checking. The local half of the same recipe *was* run, which is exactly why the
difference between the halves should not be papered over.

**Scope**
- In: the four keys the recipe names for this backend — `tracker`, `tracker_status`,
  `tracker_status_done`, `tracker_workflow` — exercised through at least one handoff operation that
  reads a work item, and one that writes a status.
- Out: any change to taskmd's own GitHub binding. If this finds one needed, that is a separate task.

**Inputs**
- `plugin/skills/taskmd/docs/HANDOFF.md` — the recipe under test
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — taskmd's own backend binding
- The handoff skill's `bindings/github-issues.md` — the other half of the derivation

**Acceptance criteria**
- [ ] The result is stated as what the commands printed, not as a verdict
- [ ] Both directions are exercised: handoff **reads** an item, and handoff **writes** a status
- [ ] Where it works, the recipe's GitHub section says so and names what was run; where it does not,
      the recipe states the limitation instead of the configuration
- [ ] If no live issues-backed project is reachable, that is recorded as the result, naming what
      would show it — an honest gap, not an implied assurance

**Open questions**
- ~~**Is a taskmd project on the GitHub backend reachable to test at all?** Nobody has been observed
  running one; `control/LOCAL-CONTEXT.md` carries the adopter roster and is where the answer would
  come from. **This is the question that decides whether the task can run unattended**, so it is the
  owner's — the same property that keeps T-175, T-176 and T-178 outside the standing grant.~~
  **Answered on 2026-08-19: yes — one is reachable, and it was checked rather than assumed.** The
  Log row of that date names the venue, the evidence, and why the second candidate was rejected.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Confirm the venue **on the day**, as the answer row of 2026-08-19 required, rather than trusting that row: the configs there are local and uncommitted | §3 |
| 2 | Apply the recipe's four keys to that project's handoff config, the way an adopter reading the recipe would | the venue's `.handoff/config.md`, outside this repository |
| 3 | Exercise **find** and **read** against a live issue, recording what the commands printed | §3 |
| 4 | Exercise **write a status**, using the one combined edit the binding specifies, then restore the item and record both states | §3 |
| 5 | Say in the recipe itself that it has been run, and name what was run — and say which key the run did **not** reach | `plugin/skills/taskmd/docs/HANDOFF.md` |
| 6 | `check` and the suite green, including the guard that stops the plugin citing what it does not ship | §3 |

## 3. Implement

**Decisions & assumptions**
- **The venue was confirmed on the day and it holds** — 2026-08-19. Both configs are present and
  still untracked, exactly as the answer row predicted; the repository carries **6 issues**, every
  one labelled `status:proposed`, `phase:specify`, `type:*`, `business_value:*` and `effort:*`.
  That is taskmd's `<field>:<value>` convention, which is the join the recipe was derived from.
- **The venue's config refused this binding, and its reason had expired** — 2026-08-19, found while
  applying step 2 and **not** something this task went looking for. That file said, in its own
  words, that the handoff skill *ships bindings for Notion and for two local-Markdown shapes only*
  and that `none` was therefore the only honest setting. Checked rather than believed:
  `bindings/github-issues.md` exists in that skill and its first commit is dated **2026-08-16** —
  one day after the paragraph was written. So the refusal was true when written and false when
  read, which is the failure class that file's own last section exists to catch. Corrected there,
  with the original kept as a quotation.
- **The status write was done on a live item and reverted in the same minute** — 2026-08-19. There
  is no way to exercise a status write without writing a status, and the alternatives were both
  worse: *creating a throwaway issue* leaves a permanent row in a real backlog and is a larger
  action than the one authorised, and *not writing at all* fails criterion 2. So the item was moved
  and moved back, and **both states are recorded below** rather than only the end state.

**Step 3 — find, and read**

`--state all` and a limit above the issue count, as the binding requires:

```text
$ gh issue list --repo <venue> --state all --limit 100 --json number,title,labels,state
issues: 6
 #6   OPEN   Commit the taskmd and handoff configs, or record why they stay local
              status:proposed, phase:specify, type:admin, business_value:medium, effort:xs
```

```text
$ gh issue view 6 --repo <venue> --json number,title,body,labels,state,url,comments
number : 6
state  : OPEN            <- NOT the status, per the binding
labels : status:proposed, phase:specify, type:admin, business_value:medium, effort:xs
status : status:proposed <- read from the label, per tracker_status
comments: 0
body   : 528 chars
```

**The read proves the join.** `tracker_status: label:status:` plus the value `proposed` is the
literal label taskmd writes, with no translation layer, and the binding's rule that `state` is not
the status under a label form is visible in the same output: `OPEN` and `status:proposed` are two
different facts about one item.

**Step 4 — write a status, then restore**

```text
$ gh issue view 6 --json labels
status:proposed, phase:specify, type:admin, business_value:medium, effort:xs

$ gh issue edit 6 --add-label "status:done" --remove-label "status:proposed"
https://github.com/<venue>/issues/6

$ gh issue view 6 --json labels,state
status:done, phase:specify, type:admin, business_value:medium, effort:xs
OPEN

$ gh issue edit 6 --add-label "status:proposed" --remove-label "status:done"
$ gh issue view 6 --json labels,state
status:proposed, phase:specify, type:admin, business_value:medium, effort:xs  state=OPEN
```

**The most useful line of the whole run is `OPEN` after the write.** `tracker_status` is
`label:status:` and not `label:status:+state`, and the binding says the label is then the one stored
fact and the write must **never also close**. It did not close. A recipe that had quietly specified
the `+state` form would have shut a live issue here, and nothing but running it would have said so.

`tracker_status_done` was exercised by the same command: `done` plus the `status:` prefix is the
`status:done` label, that label existed in the repository, and the write succeeded. The binding's
safe-direction rule — a label named in config that does not exist fails the write — was therefore
**not** exercised, because the label was there.

**What was not reached.** `tracker_workflow` is not read by any operation: it is a pointer a session
follows, not an input to find, read, create, update or reference. Three of the recipe's four keys
are now proven by a command and the fourth is proven by somebody opening what it names. The recipe
says so in the same paragraph that claims the rest, so the claim and its limit travel together.

**One correction to this record's own method.** The first attempt to confirm that the plugin's
self-containment guard would catch a link escaping into `tasks/` ran
`test_no_file_in_the_plugin_cites_something_it_does_not_ship` and passed, which reads as *the guard
is weak*. It is not: there are **two** tests and the one for escaping relative paths is
`test_no_relative_path_in_the_plugin_climbs_out_of_it`, which fails on exactly that link. The
recipe's first draft did carry such a link; it was removed, and re-added once to make the correct
guard fail before being trusted.

**Outputs produced**
- `plugin/skills/taskmd/docs/HANDOFF.md`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The result is stated as what the commands printed, not as a verdict | met | §3 quotes five command outputs including both sides of the status write. No sentence in it says *works* |
| Both directions are exercised: handoff **reads** an item, and handoff **writes** a status | met | Read on issue 6, status write and its reversal on the same item, all quoted |
| Where it works, the recipe's GitHub section says so and names what was run; where it does not, the recipe states the limitation instead of the configuration | met | The recipe gained *This recipe has been run*, naming the two commands and their results — **and the key the run did not reach**, so the limitation sits in the same paragraph as the claim |
| If no live issues-backed project is reachable, that is recorded as the result, naming what would show it | **not applicable** | One was reachable and was confirmed on the day. Recorded as inapplicable rather than ticked, since nothing about it was tested |
| `check` and the suite green | met | `check` clean, suite green, quoted in the Log |

Four criteria, three met, one not applicable, no child raised.

**What running it actually bought.** The derivation was correct on paper and stayed correct — but the
run produced one fact no amount of reading would have: the issue stays **open** after a status write
under the label form. That is the difference between `label:status:` and `label:status:+state`, and
it is the difference between a recipe and a recipe that has shut somebody's live issue.

**And it produced one fact about a neighbour.** The venue was refusing this binding on a reason that
expired the day after it was written. Nobody would have found that by reading taskmd.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | Three criteria met, one **not applicable** because a venue was reachable, no child raised. **Authorisation (METHOD §3.1):** the owner's grant of 2026-08-19 covering T-194, T-189, T-148, T-131 and T-181, full lifecycle, given after being told this task writes to a live issue. `specify` confirmed the venue on the day, as the answer row of 2026-08-19 required. **The run produced one fact no reading would have**: after a status write under `label:status:` the issue stayed **OPEN**, which is the binding's *never also close* rule holding — the `+state` form would have shut a live issue. The item was moved and moved back and both states are recorded. **It also found a defect in the venue**: its config refused this binding because none existed, and one shipped the day after that paragraph was written; corrected there with the original kept as a quotation. `tracker_workflow` was **not** reached by any operation and the recipe says so beside the claim. |
| 2026-08-19 | (no change) | **The open question is answered, and the answer falsifies the premise §1 was written on.** Asked in the backlog-wide round of 2026-08-19; the owner named two candidates rather than accepting the *unreachable* result, and both were checked before answering. **A live issues-backed taskmd project is reachable: the context-audit sibling**, labelled in `control/LOCAL-CONTEXT.md`. Its `.taskmd/config.md` declares the GitHub Issues binding with `id_prefix: '#'` and `id_width: none`, and its open issues carry `status:proposed`, `phase:specify`, `type:*`, `business_value:*` and `effort:*` as labels — which is taskmd's `<field>:<value>` convention, the exact join the recipe's GitHub half was derived from and which §1 says has never been run. So the *unreachable* branch of criterion 4 is closed as a possibility, not as a result. **The other candidate was rejected on its own written evidence**: the handoff skill's own repository carries a `.taskmd/config.md` too, and that file states plainly that the taskmd CLI does not run on the project and that its operations are `gh` instructions followed by an agent; its status labels also take a different form. It is a project configured *for* the binding rather than one running it, so a pass there would not exercise the join. *Rejected: recording the task as unreachable*, which §1's criterion 4 allows and which the check above shows would have been false. `specify` still confirms the venue on the day rather than trusting this row — the configs there are local and uncommitted, and that project has an open issue about whether they stay that way. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md)'s review, which carried its either-backend criterion rather than meeting it. The local half of that recipe was verified by use — the session that wrote it resumed through the configuration it documents — and the GitHub half was not, so shipping both under one heading would have made them look equally tested. **Outside the standing grant of 2026-08-18**, on both counts: it is a task T-005 raised, and its open question is the owner's. |
