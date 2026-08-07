# Binding: local Markdown files

One task per file, in a folder, with front-matter for facts and the body for content. The contract
this implements is [`../BINDING.md`](../BINDING.md); the method it serves is
[`../METHOD.md`](../METHOD.md). Neither is restated here.

This is the backend `taskmd`'s own code implements, so its six operations are the commands plus
ordinary file edits — no agent judgement is needed to perform them, and no dependency beyond a
Python interpreter.

---

## Assumptions this binding makes

Claims about **your project**, not about the backend. Check them before adopting; each one is
something that has to be true for the instructions below to be safe.

1. **Your process regenerates the index after every write.** The folder listing is *not* the index:
   the index is a generated file inside the task folder, and it goes stale the moment a task's
   properties change — see *update*. If you are coming from a binding that told you the folder is
   the index and there is no central list to keep in sync, that sentence is false here, and
   forgetting this step is the single most likely way to leave your project inconsistent.
2. **Your project keeps no other derived view of its tasks.** Nothing else here is materialised:
   inverse edges, the open/closed split and every listing are computed per read and stored nowhere,
   and the generated index is the only written derived artefact. If you also maintain a board, a
   spreadsheet or a status page fed from these tasks, this binding does not know about it and will
   not keep it current.
3. **Only one person or agent creates tasks at a time.** Identity is chosen locally, before the task
   exists: the next number after the highest already present. That is what lets an id be written
   into another task's edges in the same edit that creates it — and it is also why two people
   creating tasks on separate branches will pick the same number and collide at merge.
4. **Your project is content for finished tasks to stay in the task folder.** Status alone carries
   open versus closed. Moving them to an archive folder is a common variant and this binding does
   not do it, because every link pointing at a finished task would then have to be rewritten — and
   `enumerate` would have to know about two places to keep the far end of those links visible.
5. **The task folder already exists.** Creating it is the adopting project's one setup action; no
   command creates it, and every command refuses to run until it is there.
6. **Nothing you keep alongside your tasks carries a schema-matching id.** A file in the task folder
   whose id does not match the schema is not a task, which is what keeps the generated index,
   templates and your own notes from being read as work — and why there is no exclusion list to
   maintain. The corollary is the checkable half: a stray file that *does* match becomes a task
   silently.

METHOD §6's homes, assigned: **the task** is the file; **its recorded properties** are the
front-matter; **which tasks exist and their state** is derived by enumeration; **the method** and
**project conventions** are repository documents outside the task folder.

METHOD §1 rule 5's closing conditions, assigned: **the outcome** is the paths in `deliverables`;
**the record** is the task file, and its log in particular; **the `implement` evidence** is what the
task's implement section says was checked by using the outcome. **Only the first of the three is
mechanical.** `check` reports a declared path that is missing and can see neither of the others, so
it returns OK on a `done` task whose implement section is still the untouched template. Passing the
validator is necessary for closing and is never the condition — reading it as the condition is how a
project ends up closing tasks that recorded nothing.

**Backend limits: none that reach the method.** A file holds any field, any edge and any content,
so nothing in METHOD is absorbed or approximated here. That is what makes this binding the wrong
one to generalise from — see [`../BINDING.md`](../BINDING.md) §2.

---

## Configuration this binding reads

All of it from the schema config (`taskmd/defaults/config.md`, or the project's `.taskmd/config.md`)
— this binding introduces no settings of its own, and defines no field names or status values.
It needs `tasks_dir`, the identity keys (`id_field`, `id_prefix`, `id_width`), and the edge table.

---

## Operations

**find** — a task id resolves to the one file in `tasks_dir` whose `id` field is that id. Filenames
are `<id>-<slug>.md` by convention and the slug may drift from the title; **the front-matter is
what is matched, never the filename**, so a renamed file is still found and two files claiming one
id are a conflict rather than a coin toss. For a reference that is not an id, match against titles
and report every candidate rather than choosing.

**read** — the file, whole: front-matter and body. Fields the schema does not name are returned
with the rest and are never interpreted. `python -m taskmd context <id>` is this operation plus the
derived edges, which is what makes it enough to start a task.

**create** — take the next id: the highest existing id across the whole folder, plus one, padded to
`id_width`. Copy the template, fill identity, title, initial status and phase, and **write the
task's edges in the same write** — the parent of an audit finding belongs in the file that is being
created, not in a follow-up edit. Then regenerate the index.

**update** — edit the file in place. Change only the front-matter fields and body sections you mean
to change; everything else stays byte-identical, including unknown fields, blank lines and the order
of anything you did not touch. Append to the task's log rather than rewriting it. **Then regenerate
the index** — this is assumption 1, and it is the step that gets forgotten.

**reference** — the id, plus a repository-relative link to the file, so anyone who pulls the
repository can open it. Since done tasks do not move (assumption 4), a reference stays valid for the
life of the project.

**enumerate** — walk `tasks_dir` recursively; skip folders whose name begins with `_` or `.`; read
every `.md` file; keep the ones whose `id` field matches the configured prefix and width. Everything
else in the folder — the generated index, templates — is not a task by assumption 6. The result
includes finished tasks, which is what keeps the far end of a link to finished work visible
([`../BINDING.md`](../BINDING.md) §3).

### After any write

```bash
python -m taskmd index
```

```bash
python -m taskmd check
```

`index` regenerates the derived file; `check` confirms the write left the project consistent —
vocabulary valid, references resolving, declared deliverables present. A write is not finished until
both have run, and `check` is the reason a mistake here surfaces immediately instead of at the next
person's turn.

**A project may have the second one run for it, and still owes the first.** Setting `after_write` in
the config makes taskmd run a command of the project's choosing after **its own** write, so
`after_write: python -m taskmd check` turns the two steps above into one — a supplement to this
step, not a replacement for it. The half that cannot be automated this way is `index` itself: taskmd
never writes a task file, so the edit that made the index stale is one it never saw. Whatever
performs the edit is what has to run `index` — which is why this step is written as an instruction
to the agent rather than delegated to the tool.
