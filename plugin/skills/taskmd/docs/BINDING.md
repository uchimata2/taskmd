# The taskmd Backend Contract

**What a backend must provide for [`METHOD.md`](METHOD.md) to run on it.** The method names no
field, no file and no command; this document names the operations that make that possible, and each
*binding* — [`bindings/`](bindings/) — implements them for one backend. Changing backend changes the
binding, not the method.

**This document states guarantees, not mechanisms.** It never says how an operation is carried out,
because that differs by more than storage: for local Markdown the operations are implemented by
`taskmd`'s own code, while for a remote tracker they are instructions an agent follows using its own
tools. A contract that assumed either would exclude the other.

**Load this when writing or adopting a binding.** It is not loaded with the method — the method
governs the work, and it needs to know none of this.

---

## 1. The operations

Six. Five share their names and meanings with the handoff skill's tracker-binding contract, so a
project can carry one vocabulary across both; `enumerate` is taskmd's addition, and §3 is why.

| Operation | Must guarantee |
| :--- | :--- |
| **find** | Resolves a reference a person would naturally give — an id, a title, a link — to exactly one task, or says it resolved to none or to several. Never guesses between candidates. |
| **read** | Returns one task whole: every recorded property and all its content. Properties the backend does not understand are returned unchanged, not dropped. |
| **create** | Brings a new task into existence with its properties set, including its edges, in one operation. Returns the new task's identity. |
| **update** | Changes recorded properties and content on an existing task, leaving everything it was not asked to change **byte-identical**. |
| **reference** | Produces a stable identity for a task that any other task may point at, and that anyone who can reach the backend can resolve. |
| **enumerate** | Yields **every** task the project has, open and closed, with enough of each to evaluate the schema's fields and edges. |

### What the guarantees are protecting

- **`create` sets edges at creation, not afterwards.** An audit produces an umbrella task and its
  findings (METHOD §5); a two-step create-then-link leaves a window in which a finding exists with
  no parent, and a backend that crashes in that window has silently broken the rule that findings
  are traceable.
- **`update` preserves what it did not touch.** The schema deliberately carries fields it does not
  interpret, so a project can adopt taskmd without rewriting its tasks first. An update that
  normalises, reorders or drops those fields destroys data the tool was never told about.
- **`enumerate` includes closed tasks.** This is the one most easily got wrong, and the failure is
  silent — see §3.
- **Identity is assigned once and never changes.** Who assigns it is the binding's business: local
  Markdown picks the next number, a server-backed tracker is handed one. Nothing in the method
  depends on ids being chosen locally, being numeric, or being ordered.

### What no operation serves, deliberately

METHOD §3 — one phase per request, ask to the exit criterion, surface what you discover — asks
nothing of a backend. It governs how the agent works, not where tasks live. A binding that finds
itself implementing anything for §3 has misread the contract.

---

## 2. Fields, values and formats are not here

No operation above names a field, a status value, an id format or a file format. Those come from the
schema configuration, which is the project's, not the backend's. Two consequences:

- A binding **may not** define the vocabulary. If a binding says "status is one of backlog /
  doing / done", it has taken a decision that belongs to the adopting project.
- A binding **must** say how the schema's field names map onto whatever the backend calls its
  properties, when they are not the same thing. That mapping is the binding's own business and is
  exactly what it exists to absorb.

The test: a binding that can only be implemented one way has described a mechanism, and the contract
has failed. A second, differently-shaped backend implementing the same sentence is what proves it.

---

## 3. Derived views

The method's third core rule is that anything derivable is derived. Three things follow for a
backend, and they are the reason `enumerate` exists.

**Every derived view is computed from `enumerate`.** The inverse of each edge (children, what a task
blocks, the far end of a soft link), the index, any listing, any validation across the set — all of
them are one pass over every task. There is no operation for "give me a task's children", because
there is no way for a backend to answer it that is not either enumeration or a second stored copy of
the same fact.

**Closed tasks are part of the set.** A binding that enumerates only open tasks makes every edge
pointing at finished work disappear from the other end: a task blocked by a task that has since
closed shows nothing, and the graph quietly says the work was never connected. The failure looks
exactly like a task with no dependencies, which is why it is worth stating rather than assuming.

**A backend may satisfy a derived view natively instead.** Some trackers store one relation and
present both directions themselves. Where that is true, the binding says so and the guarantee is met
without enumeration — the contract asks for the *result*, never the traversal.

**A materialised derived view is a rendering, never an input.** Where a binding writes a derived view
down, two rules hold without exception: it is reproducible from the tasks alone, and **no operation
may read it**. The moment an operation takes it as input it has become a second home for a fact, and
it will be stale exactly when it matters — and nothing warns you, because a second home
looks exactly like a first one.

**Size is not the test.** A materialised view may be a whole artefact — a generated index file, a
saved board — or **a single property on a single task**. The second kind is the one that gets
missed, because it does not look like a view: it looks like an ordinary field, it is written by the
same operation that writes everything else, and there is no separate file whose staleness anyone
would think to check. §5 missed exactly this and drew the wrong conclusion from an earlier draft of
this paragraph that offered only the two large examples. If a backend stores something your schema
*derives*, that is a materialised view whatever its size, and both rules above apply to it.

---

## 4. What every binding must state

A binding is not only a set of instructions; it is a set of **premises about the adopting project**,
and those are what go wrong. Every binding carries an **"Assumptions this binding makes"** section,
near the top, that an adopter can check in about thirty seconds. Each entry is a claim about *their*
project that they can confirm or deny — not a description of the backend.

**What the thirty seconds measures: the claim lines, not the section.** Every entry opens with one
bold sentence that is the whole claim, and those sentences alone are what an adopter reads to decide
whether anything here is false for them; the prose under each is for when the answer is "no" or "not
sure", and is not part of the budget. State it this way because the alternative was tested and
failed — measured against whole sections, neither existing binding came close (498 and 401 words,
around two minutes and ninety seconds), and the figure had been carried for as long as it existed
without anyone measuring it. Against the claim lines, both come in at 65 and 44 words, under twenty
seconds. To check a binding: read its bold leads, in order, and stop at the first one you cannot
answer for your project.

This section exists because of a failure that had already happened elsewhere: a binding stated "the
folder is the index" as a premise. For a project whose index is a *generated file*, that premise is
false, and a project following the binding exactly would leave its index stale while appearing to
comply. Nothing in that binding was wrong about the backend; the assumption about the project was
never surfaced to be checked.

Minimum entries — a binding states its position on each, even when the answer is "none". Each is an
entry **in that section**, except the last, which gets a section of its own for the reason under
*Where the declaration goes*, below.

| Must state | Why it bites |
| :--- | :--- |
| What plays each **home** in METHOD §6 for this backend | The homes are roles; a binding that leaves one unassigned leaves facts homeless |
| Whether anything **derived** is materialised, and what regenerates it | The folder-is-the-index failure described above |
| What the backend **cannot** represent, and what the binding does instead | A limit belongs in the binding; unstated, it becomes the method's problem |
| What must already be true before the first operation works | Setup that is obvious to the binding's author and invisible to everyone else |
| Whether identity is chosen locally or assigned by the backend | Decides whether ids can be predicted, referenced before creation, or reused |
| Which of the validator's checks **cannot occur under this binding's mapping** | An adopter who moves here loses some of what `check` gave them, and needs to know which part rather than discovering it |

### The coverage a binding declares, and why it is stated the short way

**Name what cannot occur; say the rest either applies or still runs locally.** Some of the
validator's classes describe a state that is impossible once this binding's mapping is in place —
`STALE INDEX` where the listing *is* the index, `DUPLICATE ID` where the service allocates the id
*and this binding uses it as the task id* — and an adopter needs those named, because that is the
part of `check` they stop getting. Everything else falls under *the rest* and needs no entry.

*Those two are named here, in the names the validator uses, since 2026-08-22.* The clause used to
describe both states in prose and name neither, which left a writer describing a state correctly and
then guessing what it is called.

**It is the mapping that decides, not the service**, and that wording is the result of testing this
clause rather than of writing it. Two bindings over comparable services answer differently on
`DUPLICATE ID`: where §3's mapping makes the service's own identifier the task id, the class is
impossible; where the binding keeps a human id in a property the service does not police, the same
service leaves the class fully live. A binding that reads this row as *what can my backend do* will
get that one wrong in the direction that loses an adopter a check they still needed.

**It asks for the exceptions rather than for a coverage table on purpose.** A table with a row per
check is a hand-written copy of a set the code owns, so **one new check falsifies every binding's
table at once**, in every binding anybody ever writes. The short form is stable under a new check by
construction: a class nobody has classified falls under *the rest*, and nothing needs editing. A
binding may still carry a fuller table if its author finds it useful — `github-issues.md` does — but
that is the binding's own detail and not what this contract asks for.

#### Where the class names come from

**No document holds the list, and that is this clause's own argument applied to itself.** A list of
every class, written here, is the table above with its second column removed: it would be falsified
by exactly the same event, and one was added to this validator on 2026-08-22 while this paragraph was
being written. So the names have one home and it is the validator's own source — the literal at each
`problems.append` site in `taskmd/cli.py`, together with the `ADVISORY_PREFIXES` constant beside
them. Nothing outside those two places is the list, and anything that looked like it would be a copy.

**To read the set rather than guess at it**, run `check` on any project and read the prefixes it
prints, or read those two places. Both are in what an adopter installs.

**Do not guess a name from the state this clause describes.** The prose here is not the name, and a
guess costs more than it looks: it will pass any human reader and fail the marked-region check, which
is the one thing that half of this clause exists to support. Where the name cannot be found, leave
the class out and say so in the declaration — an honest gap is reviewable and a wrong name is not.

#### Where the declaration goes, and what shape it takes

**A section of its own, not an entry in *Assumptions this binding makes*.** The minimum-entries table
says a binding must state a position on this; it does not put the position in that section, and both
shipped bindings give it a section. Three things follow, and each was a question a writer had to
settle by guessing until 2026-08-22:

- **The thirty-second budget does not reach it.** That budget is over the Assumptions section's bold
  leads, and this declaration is not one of them. There is no per-lead word figure to divide out.
- **It opens with a bold lead that states the answer**, and that lead is a fact about the **mapping**,
  not a claim about the adopter's project. This is the one place in a binding exempt from the
  claim-about-your-project rule, because an adopter cannot confirm or deny what their tracker makes
  impossible — they can only be told, and then check the reasoning.
- **The markers wrap the whole declaration**, bold lead included, so no class name can sit outside
  what the machine reads.

**When nothing is local, the closing line has a second form.** *The rest either applies or still runs
locally* presumes the adopter kept a working copy of documents on disk. A binding whose backend is
remote-only writes *the rest applies as written* and stops; a binding for a project that still has
files writes both halves, as `github-issues.md` does.

**Put the class names in a marked region**, so the one thing a machine *can* check is checked:

```text
<!-- taskmd:cannot-occur -->
... the whole declaration, with each class named in `BACKTICKS` ...
<!-- taskmd:end-cannot-occur -->
```

**What that check reads.** Inside the region and nowhere else, it takes every backticked run of three
or more capitals — `WORD`, or `WORD WORD` — and requires each to be a class the validator reports.
Measured 2026-08-22 against a specimen holding all four kinds: `STALE INDEX` and `DUPLICATE ID` were
accepted, `JQL` and `API` were reported as classes the validator does not report, and `check` and
`gh` were never looked at, being lowercase. So a backticked command inside the region is safe — as
`local-markdown.md`'s declaration has always shown — and a backticked acronym is not. Write an
acronym without backticks, or keep it outside the markers.

**It reads every class name, and that is newer than this document.** Until 2026-08-22 the pattern
required three capitals **first**, so a class whose opening word was shorter was read as nothing at
all — neither passed nor failed, which looks exactly like a pass. Two of the validator's classes were
invisible to it and `github-issues.md` declared one, so that region carried four names of which three
were guarded, and nothing anywhere said which three. The pattern now also accepts a multi-word run
whose every word is two or more capitals, and a second check counts from the other side: anything a
region backticks in capitals throughout must be a name the scan reads, so the next narrowing fails
instead of going quiet. A single two-letter word is still not a class name and still does not match.

**What that check is, and what it is not.** It confirms every binding carries the statement and that
each class it names is a class the validator actually reports — which is the staleness a hand-kept
list dies of. It cannot confirm the classification is **true**: whether a class really cannot occur
on some hosting service is a fact about that service, and nothing running locally knows it. So the
substance of this clause is reviewed by a person, and only its hygiene is mechanical. A binding that
says so plainly is easier to trust than one that implies the check settles more than it does.

---

## 5. Worked operation on a backend with no files

To show the contract does not assume a filesystem, one operation against **GitHub Issues** — a
backend with no files, no folders and no local ordering. The full binding is a separate piece of
work; this is one operation, written to test the contract's wording rather than to be complete.

> **enumerate** — every issue in the repository, open and closed, with the fields the schema names.
> Issues carry no arbitrary properties, so the binding maps the schema's fields onto what GitHub
> does have: labels for enumerated vocabularies, the issue body for content, and the native
> blocked-by relation for dependency edges. The whole set is one paginated listing filtered to no
> state; **the default listing is open issues only, and a binding that accepts that default breaks
> §3 in exactly the way described there.**
>
> Two derived views need no traversal here: GitHub presents blocked-by and blocking as two views of
> one relation, and its issue list *is* the index — so this binding materialises **no aggregate**,
> which is the sentence that would be false for local Markdown.
>
> It does materialise one thing, and this paragraph originally denied it. An issue's open/closed
> `state` is stored, where the schema *derives* open versus closed from the status value; so the
> binding writes `state` from the status label and, per §3, never reads it back. That is also the
> reason its enumeration must ask for every state explicitly rather than merely to avoid missing
> closed work — filtering on `state` would turn a rendering into an input.

**What this changed in the contract: §3, twice.** Every operation in §1 was already written as a
guarantee about a result, and none of them moved. §3 gained the "may satisfy a derived view
natively" paragraph — GitHub meets the both-ends guarantee without enumerating, and an earlier draft
that said derived views *are computed from* `enumerate` would have made a conforming backend
non-conforming for being better at it. That correction is the value of having written this before
the bindings rather than after.

The second change came the other way round, and is worth more. Writing the real binding
([`bindings/github-issues.md`](bindings/github-issues.md)) found the `state` property above, which
this example had confidently said did not exist — so §3 gained *Size is not the test*. **A worked
example written from documentation mispredicted the binding written from the tool**, and the
mispredicted part was the one thing on this backend that a project could get wrong without ever
seeing a symptom. Read that as the limit of exercises like this one: §5 is good evidence that the
contract's *wording* does not assume a filesystem, and no evidence at all about what a backend
actually stores.

---

## 6. Writing a binding

1. Copy the closest existing binding in [`bindings/`](bindings/).
2. Write the **assumptions** section first, from §4. Doing it last produces a description of what
   you built; doing it first is what catches a premise you were about to leave implicit.
3. Implement each of the six operations by whatever the backend exposes — code, a CLI, an API, an
   agent following prose. Say which, because it determines who can run it.
4. State the backend's limits rather than working around them silently.
5. **Prove it by following it.** A binding that has only been read has not been tested: perform a
   real operation using nothing but the binding's text, and check the project is still consistent
   afterwards. A binding that has never been made to fail is worth what your confidence in it is
   worth, and no more.
