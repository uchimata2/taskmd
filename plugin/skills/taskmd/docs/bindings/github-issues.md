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
2. **Nobody on your project closes or reopens an issue in the GitHub UI.** They will want to — it
   is one click and it looks like finishing the task. Here `state` is a rendering of the `status:`
   label, written from it and only from it (see *update*), and it is the one materialised derived
   view this binding has. A click that changes the rendering without changing the fact leaves the
   task contradicting itself, and no view will flag it. If your team works in the web UI as much as
   the CLI, answer this one honestly.
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
  backend has ids like `#41`; `id_prefix` and `id_width` describe that, they do not impose it.
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

Nothing filters on `state` — that is assumption 2's "no operation reads it", and passing
`--state all` is how this operation obeys it rather than merely agreeing with it.

### After any write

Nothing. There is no index to regenerate: the issue list *is* the index, computed on demand, and
this binding materialises only the `state` rendering that *update* already wrote. This is the
sentence that would be false for [`local-markdown.md`](local-markdown.md), whose assumption 1 says
the opposite — and it is why [`../BINDING.md`](../BINDING.md) §4 asks every binding to state its
position rather than inherit one.
