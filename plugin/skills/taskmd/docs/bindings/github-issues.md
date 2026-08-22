# Binding: GitHub Issues

One task per issue, in a repository. The contract this implements is
[`../BINDING.md`](../BINDING.md); the method it serves is [`../METHOD.md`](../METHOD.md). Neither is
restated here.

**Who runs this.** An agent, using the `gh` CLI. No taskmd code touches the network, and none is
planned to — so unlike [`local-markdown.md`](local-markdown.md), whose operations are commands, the
operations below are instructions someone follows. That difference is the point of the contract:
both are conforming backends, and the method cannot tell them apart.

---

## Assumptions this binding makes

Claims about **your project**, not about GitHub. Check them before adopting; each is something that
has to be true for the instructions below to be safe.

1. **Nothing in your project needs a task's id before that task exists.** Ids are assigned by
   GitHub: the issue number *is* the task id, and you cannot know it in advance, reserve one, or
   renumber. So a task may carry the edges it owns from birth, but an edge pointing **at** a new
   task is written afterwards, on the task that owns it. If you have a habit of writing an id into
   a document, a branch name or a commit message before the task is real, that habit does not
   survive the move.
2. **Nobody on your project closes or reopens an issue in the GitHub UI** — or, if they do, you run
   the standing check afterwards. They will want to: it is one click and it looks like finishing the
   task. Here `state` is a rendering of the `status:` label, written from it and only from it (see
   *update*), and it is the one materialised derived view this binding has. A click that changes the
   rendering without changing the fact leaves the task contradicting itself.
   **Row 10 of *Checking a backlog that is already here* is what notices**, so the assumption is no
   longer a request nobody can enforce — but it is still an assumption, because nothing here is
   scheduled and the row only answers when somebody runs it. If your team works in the web UI as
   much as the CLI, answer this one honestly and run the check more often.
3. **Every label the vocabulary needs already exists in the repository.** Labels are created per
   repository, `gh` will not invent one, and a mistyped label name fails the write rather than
   silently mislabelling. Creating them is your one setup action — see *Setup*.
4. **Your `gh` is 2.94.0 or newer, your repository has issues enabled with sub-issues and issue
   dependencies available, and your token has `repo` scope.** One question, three ways to fail it.
   2.94.0 is where `gh` gained the sub-issue and dependency flags — `--parent`, `--blocked-by`,
   `--add-blocked-by`, `--remove-parent` — and every other flag used below is older, so that release
   is the floor for the whole binding. Below it you get an unrecognised-flag error partway through an
   operation instead of an answer here. Nothing needs `project` scope, a Projects board, or an
   organisation. Verified on 2.96.0 against GitHub.com; **Enterprise Server is untested** — the
   features are server-side as well as CLI-side, which is what the middle clause is asking you.
5. **Your project does not treat a GitHub cross-reference as a recorded link.** Soft links live in
   one designated section of the issue body and only there. GitHub raises a cross-reference on the
   far issue for **any** `#N` mention — in a comment, in a commit message, in passing prose — and
   none of those is a soft edge. If "GitHub showed a link between them" counts as the record where
   you work, that reading is false here and will manufacture edges nobody wrote.
6. **Your project records nothing about a task in a pull request, commit message or branch.** The
   task is the issue, whole. This binding never reads anything attached to an issue, so a decision
   whose only home is a PR description has no home at all (METHOD §6). Projects that do their
   thinking in review comments fail this one, and it is worth knowing before adopting rather than
   after.

METHOD §6's homes, assigned: **the task** is the issue; **its recorded properties** are its labels,
its native relations and the property block at the top of its body; **which tasks exist and their
state** is derived by enumeration; **the method** and **project conventions** are documents in the
repository, outside the issue tracker.

**Backend limits that reach the method: one.** GitHub has no field whose shape is a symmetric link,
so `related` is absorbed by this binding into a body section (*Mapping*, below) rather than by a
native carrier. Everything else in METHOD is represented directly. Contrast
[`local-markdown.md`](local-markdown.md), where nothing is absorbed at all — which is why that one
is the wrong binding to generalise from ([`../BINDING.md`](../BINDING.md) §2).

---

## Configuration this binding reads

The schema config (`taskmd/defaults/config.md`, or the project's `.taskmd/config.md`), exactly as
the local binding does: this binding introduces no settings of its own and **defines no field names
or vocabulary values** ([`../BINDING.md`](../BINDING.md) §2). It needs the identity keys, the edge
table and the vocabularies.

Two keys mean something different here, and neither is this binding's to change:

- **the identity keys** describe the issue number rather than a chosen format. A project on this
  backend has ids like `#7`, `#41` and `#1024`: set `id_prefix: #` and **`id_width: none`**, which
  is the value that says the ids are allocated rather than composed. It has to be said rather than
  left to the default, because `id_width` is otherwise enforced when a file is read — no number
  describes those three ids, so a project inheriting `3` would find two of them were not tasks.
- **`tasks_dir` is unused.** There is no folder. A project running only on this backend has nothing
  for it to name.

## Setup

One action, once per repository: create a label for every value in every vocabulary the config
enumerates, named `<field>:<value>` — `status:proposed`, `phase:specify`, `type:deliverable`, and so
on for each row of the config's vocabulary table. Assumption 3 is why this cannot be skipped and
why it is safe that it fails loudly.

Nothing else is set up. There is no board to configure, no organisation to belong to, and no
template to install.

---

## Mapping

Three rules cover every field, in this order.

1. **A field GitHub carries natively uses the native carrier** — the table below.
2. **A field the config enumerates is a label**, `<field>:<value>`. One label per field per issue.
3. **Everything else is a line in the property block**, a fenced block at the very top of the issue
   body. This includes fields the schema does not name, which the contract requires be carried
   unchanged rather than dropped ([`../BINDING.md`](../BINDING.md) §1, *read*).

| Field | Carrier | Note |
| :--- | :--- | :--- |
| id | the issue number | Assigned by GitHub — assumption 1 |
| title | the issue title | |
| parent | the sub-issue relation | Native both ways: `parent` and `subIssues` |
| blocked_by | the issue dependency relation | Native both ways: `blockedBy` and `blocking` |
| related | the `Related` line of the property block | No native carrier — assumption 5 |
| created, updated | `createdAt`, `updatedAt` | Maintained by GitHub; never written, always derived |
| status, phase, type, and every other enumerated field | a `<field>:<value>` label | Rule 2 |
| work_package, owner, deliverables, and any field the schema does not name | the property block | Rule 3 |

**Why labels and not the tidier options.** Two alternatives were rejected, and both would have been
defensible:

- **A Projects single-select field** for `status` and `phase` is what a Projects board is for, and
  it renders better. Rejected because it needs a board, an extra token scope and an organisation in
  practice, and because *read* would then need a second lookup to return a task whole — the
  contract's `read` guarantee gets materially harder for a cosmetic gain. Labels need nothing beyond
  assumption 4.
- **Issue types** for `type` map almost exactly — one per issue, a closed vocabulary. Rejected
  because they are defined at the organisation level, so a personal repository cannot have them at
  all, and a binding whose `type` field only works for organisations excludes most adopters. The
  same argument rejects **assignees** for `owner`: an assignee is a GitHub login, while the schema's
  `owner` values are roles like `maintainer`. Mapping a role onto a login would make this binding
  decide the project's vocabulary, which [`../BINDING.md`](../BINDING.md) §2 forbids.

**Why the property block and not a comment.** The block is at the top of the body, so `read` returns
it in the same fetch as everything else, and *update* edits one field. A comment would be a second
place to look and would put a task's facts into a stream that anyone can append to.

---

## Operations

**find** — `gh issue view <number>` for an id. For anything else, `gh issue list --state all
--search "<text>"` and report every candidate rather than choosing. The issue number is the only
identity; a title may be edited freely and is never matched as if it were an id.

**read** — one issue whole:

```bash
gh issue view <number> --json number,title,body,labels,parent,subIssues,blockedBy,blocking,createdAt,updatedAt
```

The body carries the property block verbatim, so fields this binding does not interpret come back
with the rest. `parent`/`subIssues` and `blockedBy`/`blocking` arrive as pairs: GitHub presents both
directions of one relation, so the inverse is available without traversal
([`../BINDING.md`](../BINDING.md) §3). **Do not report `state` as the status** — assumption 2.

**create** — one command, carrying the edges the new task owns:

```bash
gh issue create --title "<title>" --body-file <file> --label "status:proposed" --label "phase:specify" --parent <number> --blocked-by <numbers>
```

`--parent` and `--blocked-by` at creation are what satisfy the contract's "edges set in one
operation": an audit finding is never briefly parentless, which is the window
[`../BINDING.md`](../BINDING.md) §1 exists to close. The id is in the returned URL; it did not exist
before this command, which is assumption 1 in practice.

**update** — `gh issue edit <number>`, changing only what you mean to change. Three rules:

- **Editing the body replaces all of it.** There is no patch. Fetch the body, change your one field
  in what you fetched, and send the whole thing back:

  ```bash
  gh issue view <number> --json body --template '{{.body}}' > body.md
  # edit body.md
  gh issue edit <number> --body-file body.md
  ```

  **Fetch it with `--template`, not with `--jq .body` or `-q .body`.** Both jq forms append a
  newline that is not in the body, and writing that back stores a body one byte longer — every time,
  compounding, invisible in rendered Markdown. Measured: five `--template` round trips held at 204
  bytes; the jq form grew 230 → 231 → 232 over three. The `read` operation above is unaffected,
  because it consumes JSON rather than writing it back; this rule is only for the round trip.

- **What a partial rewrite destroys.** Sending a body containing only the fields you meant to change
  deletes, silently and unrecoverably:
  - **soft edges** — `related` lives in the property block and nowhere else on this backend, so
    there is no far end holding a copy and no derived view that can notice one has gone;
  - **fields the schema does not name**, which the contract requires be carried unchanged;
  - **the prose**, and anything else below the block.

  **`gh` exits 0 for the destructive edit exactly as it does for the correct one.** Nothing in the
  output distinguishes them, and the resulting issue is well-formed — it simply has one fewer edge
  than it had a moment earlier. Assume no error means nothing.

- **A status change is two writes and one fact.** Set the label, then render `state` from it: if the
  new status is in `open_statuses` the issue is open, otherwise closed.

```bash
gh issue edit <number> --remove-label "status:planned" --add-label "status:done"
gh issue close <number>
```

Never the second without the first, and never `gh issue close` on its own — that changes the
rendering while the fact stays put (assumption 2). Edges are moved with `--add-blocked-by`,
`--remove-blocked-by`, `--parent` and `--remove-parent`, none of which touch the body.

**reference** — the issue number and its URL. An issue number is never reused within a repository,
so a reference stays valid for the life of the project. `#41` resolves inside the repository;
the full URL is what to use anywhere else.

**enumerate** — every issue, open and closed:

```bash
gh issue list --state all --limit 1000 --json number,title,body,labels,parent,subIssues,blockedBy,blocking
```

**Both flags are load-bearing, and both defaults are wrong for this operation.** `--state` defaults
to `open`, which drops every finished task and makes each link pointing at one vanish from the far
end — the failure [`../BINDING.md`](../BINDING.md) §3 describes, and it looks exactly like a task
with no dependencies. `--limit` defaults to **30**, which silently truncates any project larger than
that; set it above the issue count and check the result against it. Neither failure raises an error,
and a listing that is quietly 30 items long is the more convincing of the two because it looks like
a complete answer.

Nothing filters on `state`, and this fetch does not carry it — that is assumption 2's "no operation
reads it", and passing `--state all` is how this operation obeys it rather than merely agreeing with
it. **The standing check fetches `state` on purpose and that is not a contradiction**: the rule is
that nothing reads `state` **as** the status, and row 10 reads it **against** the status. One
substitutes the rendering for the fact; the other asks whether the two still agree. An operation that
carried `state` here would put it within reach of every caller that wants to know whether a task is
open, which is the substitution the rule exists to prevent — so the field is fetched where it is
compared and nowhere else.

**order** — *what should I work on next*, by the local backend's stated rule rather than by issue
number. Every input the rule needs is already in *enumerate*'s output, so this is a sort over
something you have, not a query you cannot make. Run *enumerate*, then sort the open issues on four
keys, in this order:

1. **Blocked last.** An issue is blocked when its `blockedBy` names an issue that is still open.
   Closed blockers do not count, and a blocked issue is still listed rather than hidden, so that
   `order` and `order --limit 1` describe the same set.
2. **Effective value, best first** — the best value among the issue **and everything it transitively
   unblocks**, following `blocking`. A cheap blocker is pulled ahead by what it releases rather than
   sitting behind unrelated work. Best is the earliest value in your config's own row, so
   `critical` outranks `high` because it is written first, not because of any number here.
3. **Effort, cheapest first**, by the same rule: earliest in the row wins. An issue with no estimate
   sorts after every issue that has one.
4. **Issue number**, so the order is total and the same repository always gives the same answer.

The value and effort of an issue are its `<field>:<value>` labels. Read the label, not the body: the
property block in the body is a rendering, and rule 2 makes the label the fact.

**What this cannot reproduce, stated rather than glossed:**

- **A dependency cycle.** The local command tolerates one because its validator reports it
  separately; here nothing reports it, so a cycle in `blockedBy` will not terminate a naive walk.
  Stop at an issue already on the current path and take its own value.
- **A stale `blockedBy`.** The local backend derives the inverse edge; here both directions are
  GitHub's and nothing checks that they agree.
- **Absent labels.** An issue whose value or effort label was never applied has no key to sort on.
  Treat it as unestimated, and note that the local backend has a validator that would have told you.

**This is a description of the local backend's behaviour, and that is deliberate.** Every other
operation in this document describes local behaviour too; the rule's one home is the `## Ordering`
section of the schema config, and this restates it because whoever implements this backend should
not have to read Python to learn the one behaviour that decides what people work on.

### After any write

Nothing. There is no index to regenerate: the issue list *is* the index, computed on demand, and
this binding materialises only the `state` rendering that *update* already wrote. This is the
sentence that would be false for [`local-markdown.md`](local-markdown.md), whose assumption 1 says
the opposite — and it is why [`../BINDING.md`](../BINDING.md) §4 asks every binding to state its
position rather than inherit one.

---

## Moving a project here from local Markdown

For a project that already runs taskmd on [`local-markdown.md`](local-markdown.md) and wants its
backlog to live in issues. It is the one migration direction in scope; the reverse is answered at the
end of this section.

**No taskmd code performs any of this.** The agent reads the files and runs `gh`, exactly as it does
for every operation above. Nothing here is a command.

### Why it cannot be one pass

Assumption 1. The issue number *is* the id and it does not exist until the issue does, so every
`T-NNN` written anywhere — in an edge, in a body, in a Markdown link to another task's file — names
something that has no number yet. Write the bodies as you create the issues and you get a backlog
whose references all point at nothing, and it looks finished: `gh` exits 0 on every one of those
creates, and each issue is well-formed on its own.

The mapping from old id to issue number exists only **between** the two passes. It is the whole
reason there are two.

### What to read, and why `list --json` is not the source

Read the **files**, which is [`local-markdown.md`](local-markdown.md)'s *read* — front-matter and
body together, whole.

`taskmd list --json` looks like the export for this job and is not. It is a **view** contract: it
emits `id`, `title`, and every field this project can **filter** on — its vocabularies, the fields it
names in a view, and both directions of every edge. It does not emit the **body**, and it does not
emit a field the project has named nowhere.

*Measured on 2026-08-17, against a 163-task project running the shipped default
(`index_columns: [work_package, status, phase]`), it carried no `type`, `owner`, `business_value`,
`effort` or `deliverables` — five schema-named fields this binding must carry as labels or as
property-block lines, and it carried no body. **Four of those five arrived on 2026-08-22**, when the
machine form was widened to every field `list` accepts as a filter; `deliverables` did not, because
nothing filters on it. The measurement is left as the record of that day.*

**The body is the half that still makes this the wrong source**, and it is the half no schema change
reaches. Widening `index_columns` to add the missing fields was considered in 2026-08-17 and rejected
as the wrong repair — it changes what every reader's index shows in order to feed a migration that
runs once — and that reasoning held: the repair went to the machine form and left the human index
alone.

It does have a job here, in *Verify* below. Because it is derived by the tool rather than by whatever
read the files, comparing against it is a genuine second opinion rather than the same reconstruction
checked twice.

### Pass 1 — create, and keep the mapping

Create in an order where a task's `parent` and its `blocked_by` targets already exist: hierarchy is a
tree and dependencies are acyclic, so such an order exists. That lets *create* above be used
unchanged, with `--parent` and `--blocked-by` set natively at creation, and nothing is briefly
parentless.

Give each issue its labels and its property block. **Leave every `T-NNN` in the body exactly as it
is** — pass 1 is not the moment to rewrite them, and a body half-rewritten against a partial mapping
is worse than one not rewritten at all.

Record `T-NNN → #N` for every task as you go. That record is the only thing pass 2 has.

### Pass 2 — rewrite every reference

For each issue: fetch the body with `--template` (never `--jq`; see *update*), rewrite, send it back
whole. Three kinds of reference, and missing any one leaves a dead link:

- **the `Related` line** of the property block — soft edges have no native carrier here, so this is
  their only home;
- **every `T-NNN` in the prose**, to `#N`;
- **every relative Markdown link to a task file** — `T-042-some-slug.md` — to the issue's URL. These
  are the ones a search for `T-` finds and a search for the id alone does not.

**A link carrying a section anchor loses the anchor**, and there is nowhere for it to go: a task file
has headings to point at and an issue body has none that survive. Rewrite to the issue and accept the
loss rather than inventing a target — a link that resolves to the right issue and the wrong place is
worse than one that resolves to the issue.

### Verify — and make it fail first

A migration nobody can check is worse than none, because it looks finished. Check the destination
against the source on four things:

| Check | Source | Destination |
| :--- | :--- | :--- |
| Every task arrived | file count | `gh issue list --state all --limit <above the count>` |
| Edges, both directions | `parent`, `blocked_by`, `related`, and `list --json`'s `children` and `blocks` | `parent`/`subIssues`, `blockedBy`/`blocking`, the `Related` line |
| Bodies intact | the file body below its property block | the issue body below its property block |
| Every reference arrived | the ids in the source body **that name a real task** | each one present as its `#N` |
| Nothing was skipped | — | no id that named a real task survives in `T-NNN` form |

**`blockedBy`, `blocking` and `subIssues` come back as `{"nodes": [...], "totalCount": N}`, not as
lists.** `parent` is a plain object, or absent. Measured on `gh` 2.96.0; reading them as lists raises
a type error rather than a wrong answer, which is the harmless way for this to go wrong.

**Do not check references by shape, which is the obvious rule and is wrong.** "No `T-NNN` survives
anywhere" and "every `#N` names an issue" both look right and both produce false failures on ordinary
prose: task bodies carry illustrative ids that never named anything (`T-999`), and they carry bare
numbers that were never references (`#1024` as an example id, an external tracker's `#13057`).
Measured on a 165-task migration: eight failures, all eight spurious, and the temptation at that point
is to "repair" prose that was correct. **A reference is an id that named a real task in the source** —
so both rows above are computed from the source's own id set, and anything else in the destination
body is text.

**Run the check against a deliberately broken migration before trusting a clean one.** Two classes it
must catch: an edge dropped between the passes — which *update*'s partial-rewrite warning shows is
silent and exits 0 — and a reference left pointing at an id that no longer exists. A verification that
has only ever passed has not been tested.

### What this procedure has been run against

**This register covers both verifications in this document** — the migration *Verify* above, and the
standing *Checking a backlog that is already here* below. It stays here, under this name, because a
closed record cites it by both (T-166); the standing half being defined further down is the price of
not falsifying that.

#### The migration verification

The two sections above are not a design. On 2026-08-17 the whole of it was run end to end, into a
private repository created for the run and deleted the same day: 28 labels, one per vocabulary value;
then 165 tasks — a real backlog with hierarchy, dependencies, soft links and cross-references —
created in dependency order with `parent` and `blocked_by` native at creation; then 165 bodies
rewritten.

**The verification failed three times before it passed, and two of those failures are the reason to
trust it.**

| Run | Result |
| :--- | :--- |
| Between the passes | **FAIL, 324** — every issue created, every native edge already right, every reference still dead. That is the state a one-pass attempt reaches and calls finished |
| After pass 2 | **FAIL, 8** — and all eight spurious. The shape rule was wrong, which is the paragraph above, written from this |
| With the rule corrected | **PASS** — count, parent, blocked_by, related, bodies, no dangling reference |
| Against a deliberately broken migration | **FAIL, 13** — the dropped edge as `blocked_by [1] != []`, and the unrewritten reference in each place it appeared |
| After repairing those | **PASS** |

No taskmd command ran at any point in either pass: the four cannot reach a network and were not asked
to. The destination is gone and was never the evidence — a migration is checked while it runs, by the
comparison the procedure ends with, so anyone doubting this runs it again rather than inspecting an
artefact.

#### The standing check

On 2026-08-21 the nine rows below were run four times against a private scratch repository created
for the run: 28 labels, one per vocabulary value; then 24 tasks from this project's own backlog —
20 closed and 4 open, with hierarchy, dependencies, soft links and cross-references — migrated by the
two passes above, then broken on purpose and repaired.

| Run | Result |
| :--- | :--- |
| Healthy backlog, first run | **FAIL, 14** — and all fourteen spurious. Row 7 had been read as *any angle-bracket span*, so it reported `<field>`, `<value>`, `<prefix>`, `<backend>` and `<pattern>` wherever prose used them. The paragraph warning against this is written from this run |
| With row 7 read as the template's own slot lines | **PASS** — 120 labels, 37 references, 15 `Related` lines, 7 dependency edges, 24 property blocks, 20 closed issues against 9 slot lines |
| Against a backlog broken in two ways | **FAIL, 3** — row 2 named the reference repointed at an issue nothing holds, and row 3 named the issue whose `Related` line was deleted. Each row named its own defect, which is the criterion |
| After repairing both | **PASS** |

**Three of the nine rows examined nothing on this corpus**, and that is a property of the project's
config rather than of the backlog: row 4 needs an issue labelled with the blocked status, row 8 needs
a date-shaped value in a property block — `created` and `updated` have native carriers, so none
reaches one — and row 9 needs the grouping field to be *enumerated*, which makes it a label; where it
is not, as here, it is a property-block line and row 9 has nothing to read. A row that examined
nothing scores like a row that found nothing, so a run is worth reporting per row with its count,
not as a verdict.

The scratch repository was created for this run and is the owner's to delete; the credential a
session can reach carries `repo` and not `delete_repo`, measured on the day. It was never the
evidence — the counts above are, and anyone doubting them runs the procedure again rather than
looking for an artefact.

### Checking a backlog that is already here

*Verify* above compares a source against a destination, so it runs on the one day a source exists.
The day after, nothing checks anything again. This section is the standing counterpart, and it exists
because the gap it leaves is **silent data loss** rather than lost convenience: `related` lives in the
property block and nowhere else on this backend, no far end holds a copy, no derived view can notice
one has gone, a partial body rewrite deletes it, and `gh` exits 0 on the destructive edit exactly as
on the correct one.

Run it after any bulk edit, after anything that rewrote bodies, and whenever you want the answer.
Nothing here is scheduled or automatic, and nothing here is a taskmd command: every call is `gh`.
The four commands cannot reach a network at all, which is a decision rather than a gap — the
same one the migration passes above obeyed.

**Fetch once**, with both flags *enumerate* explains, and work from the result:

```bash
gh issue list --state all --limit 1000 --json number,title,body,labels,parent,subIssues,blockedBy,blocking,state
```

**`state` is the one field here that *enumerate* does not fetch**, and it is added for row 10 alone.
The paragraph under *enumerate* says why that is not a contradiction of assumption 2.

Then answer these, each of which is one of the validator's classes as it lands here:

| # | What to check | How, on this backend |
| :-- | :--- | :--- |
| 1 | **Every enumerated field's value is in its row** | Each issue's `<field>:<value>` labels against your config's vocabularies. A label the config does not list, or two labels of one field on one issue, is the defect |
| 2 | **Every reference resolves** | Every id in a body's property block, and every `blockedBy` and `parent`, names an issue in the fetch. **This is the one the migration got wrong twice**, and the one nothing else can see |
| 3 | **`related` still exists** | Every issue whose property block should carry it still does. There is no far end to compare against, so compare against your own last known copy — a fetch kept before a bulk edit is the cheapest one. **This row needs two fetches, so a first run cannot answer it**; say so rather than passing it |
| 4 | **A blocked issue has an open blocker** | An issue labelled with your blocked status whose `blockedBy` is empty, or whose blockers are all closed |
| 5 | **No dependency cycle** | Walk `blockedBy`. A loop is a defect here and nothing else reports it |
| 6 | **No body stores a derived edge** | A property block writing `children:` or `blocks:`. Both are GitHub's to compute, from `subIssues` and `blocking` |
| 7 | **No closed issue carries a template slot** | A closed issue whose body holds a whole line that is one of your task template's own slot lines, with fenced and inline code blanked first. **Not any angle-bracket span** — see below |
| 8 | **No date-shaped value that is not a date** | Any property-block value shaped like a date that is not one |
| 9 | **No label reads as a version** | A grouping label whose value is a two-part number. A release of that number is a different thing |
| 10 | **`state` agrees with the `status:` label** | An issue whose `state` is `CLOSED` while its `status:` label is one of your open statuses, or `OPEN` while the label is a closed one. **The label is the fact**; `state` is its rendering, so the repair is to re-render `state` from the label with `gh issue close` / `gh issue reopen` — never to relabel the issue to match the button somebody pressed |

**Row 10 is the only row that reads a materialised derived view, and it is the only one this backend
needs.** `state` is written from the `status:` label and from nothing else (*update*), so the two can
only disagree when something outside taskmd moved one of them — which on GitHub is one click, and is
assumption 2. Every other derived thing here is computed by GitHub on demand and cannot drift.

**Repair it by hand, not automatically.** A run that closed the gap it found would destroy the only
evidence that anybody clicked, and the click is worth knowing about: it usually means somebody
believes the button finishes the task, which is a thing to correct in a person rather than in a
backlog.

**Say how many issues this row examined, not only what it found.** An issue carrying no `status:`
label, or two, has no single label to compare `state` against, so row 10 has nothing to say about it
— row 1 is what reports those. Skipping them silently makes a backlog where half the issues are
mislabelled produce the same *no disagreements* as a healthy one, which is the failure the paragraph
below names for rows 3 and 7.

**Two of the nine other rows need something the fetch does not carry, and neither says so by its length.**
Row 3 needs a *fetch kept from before*, so the section heading above — *fetch once* — is true of the
other eight and not of it. Row 7 needs your task template's **slot lines**, which are not issue data
at all; the coverage table below says the two template checks do not come across, and row 7 is the
one place a template is still read. A run that has neither should report those rows as unanswered
rather than as passed, because a row that examined nothing scores exactly like a row that found
nothing.

**Do not check template slots by shape, for the same reason references are not checked by shape.**
`<field>`, `<value>`, `<prefix>`, `<backend>` are ordinary notation in ordinary prose, and matching
any `<...>` span reports every one of them. Measured on a healthy 24-issue backlog: **14 failures,
all 14 spurious**, in the first run this procedure ever had. A slot is a **whole line the template
offers**, compared after code is blanked — which is what the local backend's own check does, and why
adding a slot to a template starts it being reported with no rule edited anywhere.

**And make it fail first.** A pass on a healthy backlog proves nothing about the procedure — it is
the same run a procedure that checks nothing produces. Before trusting it, break one issue on
purpose in a scratch repository: delete a `related` line from one body, and point one property-block
reference at an issue number that does not exist. Row 2 and row 3 must both name the issue. Repair
them and run it again. That is the standard the migration *Verify* is held to, and the reason its
three recorded failures are what make it trustworthy.

**This has been done, and the runs are in *What this procedure has been run against* above.** The
instruction stays because it is what to do after *your* next bulk edit — the recorded runs prove the
rows can fire, not that your backlog is sound. One of the two things it caught was in the procedure
itself, which is why the run is worth more than its verdict.

#### What this does not cover, and why

<!-- taskmd:cannot-occur -->
**Four classes cannot occur here**, because GitHub makes the state they describe impossible:
`DUPLICATE ID`, `ID WIDTH` and `PARKED TASK` — the service allocates issue numbers, never reuses one,
and has no folders for a task to be parked in — and `STALE INDEX`, because the issue list *is* the
index and is computed on demand. **The rest either apply here or still run locally**, against the
working tree a migrated project keeps.
<!-- taskmd:end-cannot-occur -->

That is what [`../BINDING.md`](../BINDING.md) §4 asks every binding for. The table below is this
binding's own detail rather than the contract's requirement — it says where each remaining check
went, which is worth having and is the half that goes stale:

The checks that run on the local backend split three ways here: some land above as rows, four
cannot occur at all, and the rest do not come across. The reasons are worth reading rather than
trusting. **The totals that used to open this paragraph are gone rather than corrected** - a count of
a set the code owns is either dated as a measurement or not written at all, and adding one check on
2026-08-22 falsified them. The four that cannot occur is a *stated list*, not a count of a mutable
set, so it stays.

The four that cannot occur are above and are not repeated here. What follows is where each of
the **remaining** ones went:

| Check | Here |
| :--- | :--- |
| unreachable template, template field | **Not applicable as written.** They read a task template in a folder. If your project keeps an issue template, nothing here checks it. They do still *run* on a migrated project and find nothing to read, which is why they are not in the row below |
| declared output that is gone | **Still local.** It compares declared paths against a working tree, which you still have. Run it there |
| broken link, ignored link, wide table row, config drift, section reference | **Still local, and still run.** None of these takes a task as input: they walk the documents from your project root, which a migrated project keeps. Re-run 2026-08-22 against this repository's own `tests/fixtures/migrated-away`, they reported one dead link and a config advisory, and `check` exited 1. This is the measurement under *No validator* below |
| duplicate index | **Can occur, and nothing here reports it — `check` included.** *Corrected 2026-08-22.* This row used to sit above, and it was wrong on the day it was written rather than drifted into being wrong: the check recognises a second table by the task ids it already knows, so a project with no task folder gives it nothing, and it is not reached at all. Measured 2026-08-22 — one document firing `DUPLICATE INDEX  BACKLOG.md: a second table of 3 known task ids sits outside the taskmd markers` went silent, unedited, once the task folder was taken away |
| closed parent with an open child | **Can occur, and nothing here reports it.** GitHub lets you close a parent issue while a sub-issue is still open, so the state is reachable — which is why it is not in the *cannot occur* list above. No row in the procedure looks for it. A row would have to be run against a real backlog before it could be trusted, which is the standard every row above is held to |

**Two limits of this list itself.** It is a hand-kept description of a set the code owns, so it goes
stale the way any such list does — the local backend has a guard for that class and this document has
none. And the coverage is **this** backend's: a project on a different service has a different table,
which belongs to that binding rather than to a copy of this one.

### The reverse direction: no

Moving a backlog **out** of issues and back into local files is **not supported**, and that is a
decision rather than a gap nobody got to. Only one direction was taken on, and the reason is not only
policy: coming back means *composing* ids rather than receiving them, so every `#N` in every body
would be rewritten to an id somebody has to allocate — the two-pass problem again, plus a numbering
policy that belongs to the project rather than to this binding.

What is not refused is leaving. The issues are yours, `gh issue list --state all` returns every one of
them whole, and nothing here is a format only taskmd can read.

---

## What taskmd still gives you here

Read this after a move, or before one. It is a list of facts and it stops short of a recommendation,
because the facts that would decide it are about your project and this document holds none of them.

### Three of the four commands do not come with you, and `check` half does

`context`, `index` and `list` read a folder of task files. After the move there is no folder, so they
stop — they do not degrade, warn, or fall back. Re-run 2026-08-22 against this repository's own
`tests/fixtures/migrated-away`, a project of exactly this shape:

```
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but the project root has no such folder. …
exit=2
```

**`check` is the exception, and it used to be counted in the sentence above.** *Corrected
2026-08-22.* This paragraph said **each of the four** stops, measured on 2026-08-17 — true on that
date and false from 2026-08-19, when `check` was split so that the checks reading documents run on a
project whose tasks have moved. The tool moved and this paragraph did not, which is worth more to you
than a quiet repair would be, and is why the old date is still here. On the same project, the same
day:

```
BROKEN LINK   docs/guide.md -> plan.md
1 problem(s) - 3 document(s), 2 link(s), 2 table row(s), …
CONFIG DRIFT  status: shipped default adds 'specified', 'planned', …
Scope  no task file was read, and the checks that open one did not run. …
exit=1
```

The `Scope` line is the half to read. It names what went unexamined, so a document-only run cannot be
taken for a clean bill of health on a backlog it never opened.

| Command | Replaced by | What that costs you |
| :--- | :--- | :--- |
| `context` | *read* above — `gh issue view <n> --json …` | Nothing material. One fetch, one issue, whole |
| `index` | nothing to replace — *After any write* says why | Nothing. The issue list is the index, computed on demand |
| `list` | *enumerate* above, then *order* | The enumeration survives, and so does the ordering — as a procedure you run rather than a command that runs it |
| `check` | **partly itself** | The checks that open a task file: references, vocabularies, dates, cycles, the index. The ones that walk your documents still run — *What this does not cover* above says which |

### What survives

- **The method** — the lifecycle and its exit criteria, the three edge kinds, the audit rule, one
  home per fact. It names no field, no file and no command, which is a property you can check by
  opening it rather than a claim to take from here.
- **This binding** — the mapping and the six operations. Not a proposal: the procedure above and all
  six operations were run end to end against a real repository at 165 tasks, and the verification
  caught a deliberately broken run before it passed a clean one — *What this procedure has been run
  against*, above.
- **The skill** that routes an agent through them. Measured on 2026-08-18 against two migrated
  projects of this shape, read from those sessions' own records rather than from the install: it is
  served to every session started after it was installed, at **414 characters** in the skill
  listing, and that is its standing cost until something invokes it. **Whether it still triggers
  there is unobserved** — across those 11 sessions none asked for task work in ordinary words, so
  nothing put the description to the test, and a zero drawn from that is not a negative.
- **Your schema config** — still the vocabulary, and now the source of the label names.

### What is gone and has no replacement here

Three things, stated plainly because they are the ones that would otherwise be found later. **None of
them is a reason to keep taskmd installed**: `context`, `index` and `list` exit 2 on a project with no
task folder, so those costs are already paid whatever you decide here.

**`check` is not covered by that sentence, and this is the correction rather than the conclusion.**
*Corrected 2026-08-22.* The sentence used to read *the commands exit 2 either way*, which was the
whole of the argument; `check` exits 1 and reports real problems, so one of the four does work an
uninstalled taskmd cannot. **What follows from that is stated here and not acted on.** The balance of
this section — what it lists, and that it stops short of a recommendation — was settled as a decision
on a wider set of facts than one exit code, and re-weighing it on the back of a correction of fact
would be reversing that decision as a side effect. So: the *either way* argument is now weaker for one
command out of four, item 1 below says what that command still does, and the reader weighs it.

1. **No validator.** `check` verified that every reference resolved, that every field value was in
   its vocabulary, and that the index matched the tasks it came from. Nothing on this backend does
   any of that. A `Related` line naming an issue that was never created is not reported by anything.

   > **True as behaviour, overstated as necessity — measured 2026-08-18, corrected 2026-08-22.**
   > `check` **splits** on a project with no task folder: the checks that open a task file do not
   > run, and the ones that walk the documents from your project root do — which is exactly what a
   > migrated project still keeps. *The 2026-08-18 sentence here said you lose all of them, because
   > the config error was raised while the schema loaded, before any check was reached. That was true
   > when it was written, and stopped being true on 2026-08-19; the date stays so you can see that
   > the tool moved and the document did not.* Re-run 2026-08-22 against this repository's own
   > `tests/fixtures/migrated-away`: one dead link, a config advisory, exit 1, and a `Scope` line
   > naming the half that went unexamined. So the sentence above describes where one guard sits, not
   > what this backend makes impossible.


2. **No ordering *command*.** `list --open --limit 1` answered "what to work on next" by a stated
   rule — blocked last, then effective value, then effort, then id. GitHub sorts by number, recency
   or whatever a saved filter says.

   > **The rule is not gone, only the command — corrected 2026-08-19.** This item used to say the
   > question goes back to a person. It does not have to: every input the rule needs is in
   > *enumerate*'s output, so the rule is written out under *order* in *Operations* above and an
   > agent runs it. What is genuinely lost is that nothing computes it for you and nothing checks
   > the inputs, which *order* states as three named limits rather than as a caveat.
3. **No offline copy.** The local backend's tasks are readable and editable with no tool installed.
   Here you need network access and `gh`.

### If this is not enough, or if it is doubled

Two situations, one response.

You may decide what remains does not earn its place — the method is a document you could follow
without the skill installed. Or the harness may already serve **another task-management skill**, in
which case two things are offering to track the same work, and the overlap is a cost paid on every
session rather than a tidiness problem.

**taskmd does not resolve either one, and does not say which side should go.** What it has is:

- which of its commands still run here — the table above, which is exit codes rather than argument;
- what it still supplies that nothing else does — the method, the binding, the schema, each of them a
  document you can open and disagree with;
- what the other tool covers, which **the agent can see and taskmd cannot**: taskmd's code does not
  inspect the machine, and the agent already knows what its harness serves.

The first two bullets are taskmd's account of itself, so read them as claims with their sources
attached and check one at random rather than taking the paragraph's word.

Removal is your action, and it has three ends: uninstall taskmd, uninstall the other, or keep both.
Keeping both is a real answer and it is not the free one — the overlap above is what it costs, for as
long as it stands.
