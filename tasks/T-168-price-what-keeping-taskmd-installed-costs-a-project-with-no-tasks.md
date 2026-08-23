---
id: T-168
title: Price what keeping taskmd installed costs a project that has no tasks folder
type: research
status: done
phase: review
parent: null
blocked_by: []
related: [T-166, T-167]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-17
updated: 2026-08-18
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-168 — Price what keeping taskmd installed costs a project that has no tasks folder

## 1. Specify

**Outcome**
A measured answer to two questions about a project that has migrated its backlog away and has no task
folder left: **does the skill still fire**, and **what does having it installed cost per session** —
in the same units the rest of this repository measures context in, taken by running something rather
than by reasoning about the harness.

**Why this one**
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 put the edited migration
listing in front of an uninvolved reader. Asked what missing fact would most change their
recommendation, they named this one, and their argument for why it is decisive is the part worth
keeping: the document quotes `gh` versions, task counts, byte deltas and exit codes, and **the single
claim carrying the whole installation decision is the only sentence in it with no source** — *the
skill that routes an agent through them*. Three of the four survivors are documents, which need
nothing installed. The fourth is the only thing installation buys, and nobody has measured it.

**What this task is for, since the reason it was raised is gone.** It was raised to feed a sentence
pricing the overlap against taskmd itself, in
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md) — which the maintainer cancelled on
2026-08-17, accepting the listing's remaining lean as a decision. **This survives that, and the
maintainer confirmed it should, because it is a different defect wearing the same clothes.** The
five accepted mechanisms are *framing*: what is selected, placed and worded. This one is *factual*:
one claim in the listing is neither a measured output nor a pointer, which is the standard
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) set, that
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) held itself to at `review`, and
that the rest of the document meets. Sourcing a claim is the move
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) already made once and it is not
the move that was stopped.

**It is probably already half-answered, and that is the first move.** `tests/test_budget.py` measures
tier 1 in characters and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) measured
what a session is handed unasked. Whether either covers a project with **no task folder** is the
open part. Read the shipped artefact before building anything — a gap this repository has already
shipped an answer to has cost a round trip before.

**Scope**
- In: whether the skill is served, and whether it triggers, in a project with no task folder and no
  local task config
- In: what the install costs a session there, measured, with the command that produced the number
- In: whether the existing budget test and
  [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) already answer either half
- In: sourcing the one unevidenced survivor claim once the number exists — the same move
  [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) made for the migration run
- Out: **the five accepted framing mechanisms.** They were judged and accepted in
  [T-167](T-167-stop-the-listing-pricing-only-the-rival.md); attaching a number to the listing is not
  a licence to re-balance it, and doing so here would reverse a decision the maintainer took
- Out: changing what the skill does in that situation. If the measurement argues for a change, it is
  its own task

**Inputs**
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 — the reader's argument
  for why this gap is decisive
- `tests/test_budget.py` and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) —
  what is already measured, and in what units
- `tests/fixtures/migrated-away/` — a project shaped the way this question is about
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *What survives*, the bullet this answer
  is for, and the three beside it that already carry evidence a reader can check
- `~/.claude/projects/` — the harness's own session transcripts, one folder per project. The
  instrument `specify` found; what it reaches and what it does not is under *Open questions*

**Acceptance criteria**
Drafted by the working session, not agreed by the owner — see the `specified` row in the log for why,
and note that five of the six are settled by running something rather than by judging prose.
- [ ] For a project carrying a `.taskmd` config whose task folder does not resolve, the answer states
      **whether the harness serves the skill**, resting on a session that was *handed* the listing
      rather than on the install's scope — which is an argument about the mechanism, and this
      project does not accept those
- [ ] The per-session cost is given **in characters**, the unit `tests/test_budget.py` measures in,
      with the command that produced it and a statement of what was counted: **the listing entry as
      served**, which is not the same figure as the `description:` line in `SKILL.md`
- [ ] The answer says whether a request for task work in such a project **reaches** the skill, or
      records it as unobserved and names what would show it. An observation from a session that
      never asked for task work is reported as confounded, never as a direction
- [ ] Whether `tests/test_budget.py` and
      [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) already answer either half
      is stated as a finding, naming for each what it covers and what it does not
- [ ] The survivor bullet — *The skill that routes an agent through them* — carries its evidence in
      the form the three bullets beside it use: checkable by whoever reads it. **Restated, not
      cited** — [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 established
      that this document cannot point at a task record, since a link outside `plugin/` fails a
      shipped test and a bare id resolves to nothing an adopter holds
- [ ] **Nothing else in that listing changes.** The five framing mechanisms accepted in
      [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) are out of scope, and this criterion
      is what makes that checkable rather than merely asserted

**Open questions**

- **Can a session measure this about itself? — answered on 2026-08-18 by trying three instruments,
  not by reasoning about the harness.** Yes for *is it served*; not yet for *does it fire*. The
  question is kept word for word in the heading, so what was asked stays legible beside what came
  back; the run itself is in the log.
  - **Headless `claude -p` in another directory — dead.** `401 OAuth access token has expired`, the
    same failure [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 5
    recorded on 2026-08-07. That record said this route would answer the task in one command if the
    token were live; re-verified today, it is not.
  - **A spawned subagent — cannot reach.** It runs in this project, and worktree isolation is still
    this repository. It is the right instrument for the question memory says it answers, and the
    wrong one for a question about a different project.
  - **The harness's own session transcripts — this works, and it is the one nobody had tried.** Each
    session is written under a per-project folder, and the skill listing it was handed is stored
    there as an attachment of type `skill_listing`, carrying `isInitial`, a count and the served
    text. So *what a session was handed unasked* is readable after the fact, for projects this
    repository cannot start a session in. That is what makes the two halves separable.
- **What the instrument does not settle, and it is the one thing this phase carries out.** For a
  project of this shape the store holds a single session; it asked for no task work and invoked no
  skill of any kind, so it cannot test a trigger and its zero is noise rather than a negative.
  Whether the trigger half is taken by widening the sweep to the sessions that **did** ask for task
  work, or needs a probe arranged out-of-band the way
  [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 8 arranged its own, is
  **the maintainer's to decide**. It is the only question `specify` puts.
- **One row in that store is this session's own litter, and it looks like evidence.** The failed
  headless probe wrote a transcript for an empty scratchpad directory, which is now a project folder
  carrying a served listing and no task config at all. Whoever sweeps the store must exclude it by
  name or label it; read as a data point it would be this session measuring itself.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Define the subset **by rule and not by hand** — which projects in the transcript store carry a `.taskmd` config whose `tasks_dir` does not resolve — and apply it. Exclude this session's scratchpad row by name, per §1 *Open questions* | The rule, the folders it selects, the folders it rejects and why, and the exclusion, in §3 |
| 2 | Sweep the store for the **served** half across the selected subset: whether the initial listing carried the skill, and the entry's length in characters as served | One row per selected project, with the script that produced it, in §3 |
| 3 | **Before writing any direction**, establish whether the selected subset holds a session that asked for task work at all, and state what the detector reads and what it cannot tell apart | A recorded decision: the trigger half is observable here, or it is not and this names what would show it |
| 4 | Take the trigger half as far as step 3 allows, reporting each observation's confound beside it rather than after it | The finding, or the unobserved result with its probe named, in §3 |
| 5 | Read `tests/test_budget.py` and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) against both halves and say what each covers and does not | The already-answered finding, in §3 |
| 6 | Write the evidence into the survivor bullet of the shipped listing — restated, not cited — and touch nothing else in that document | The edited `plugin/skills/taskmd/docs/bindings/github-issues.md` |
| 7 | Run `check`, `index` and the suite, and read the document's own diff to confirm the change is the bullet and only the bullet | The command output and the diff verdict, in §3 |

**Step 3 is a stopping point, not a formality.** It is placed before anything is written because
*unobserved* is a legitimate result here and it is only legitimate while it is still available — a
step that writes the answer first will find a way to fill it.

**Decisions taken at `plan`**

- **The measurement lives in this record, not in a new document.** — The answer is one figure and one
  direction, and its consumer is a single bullet in a shipped file. *Rejected: a document under
  `docs/audits/`*, which would be a second home for a fact that already has one and would need its
  own reconcile every time the figure moved. — 2026-08-18
- **The sweep script is written to the scratchpad and quoted in §3, not committed.** — It reads the
  maintainer's own transcript store, which is machine-private and outside what a clone may carry, and
  a test committed under `tests/` that reads it could never run for an adopter. Quoting it keeps the
  figure reproducible without shipping a path nobody else has. **The quote names the store in its
  generic form only** — no absolute local path reaches a tracked file. — 2026-08-18
- **`deliverables` stays empty until step 6 lands.** — A plan lists what is promised; the field
  records what exists. — 2026-08-18

**Outputs this task will produce**

- tasks/T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md — §3, the
  measurement and the four findings
- plugin/skills/taskmd/docs/bindings/github-issues.md — the survivor bullet, sourced

## 3. Implement

### Step 1 — the subset, by rule, and the defect the rule caught

**The rule.** A project is in scope when the transcript store holds sessions for it, its `cwd` still
exists and carries `.taskmd/config.md`, and the `tasks_dir` that config names **does not resolve**.
Nothing is named by hand: the two specimens this task was raised with are selected by the rule or
they are not in it.

**The first version of the rule was wrong, and the corpus said so before any figure was quoted.** It
read the value as everything after `tasks_dir:`, and these configs carry a trailing inline comment,
so the path it tested was `tasks` followed by that comment, which resolves nowhere. Every
config-carrying project came back as migrated-away, **including the deck-building sibling, which has
60 task files**. That contradiction is what exposed it. Corrected to strip the comment and then the
quotes; a `tasks_dir` whose own value contained a hash preceded by a space would still be cut, and no
such config exists here.

This is the phase's strongest piece of evidence and it is worth naming as such: the rule was **seen
to fail on a case it must catch** before it was trusted, which is the only thing that makes its later
silence mean anything.

**What it selects, from 12 project folders and 193 sessions:**

| Class | Definition | Projects | Sessions |
| :--- | :--- | :---: | :---: |
| **A** | config present, `tasks_dir` does not resolve — *migrated away* | 2 | 11 |
| **B** | no config **and** no task folder — nothing to configure | 4 | 7 |
| **C** | everything else — a resolvable task folder | 5 | 174 |

**Both A and B are reported because §1 asks for two different things.** *Outcome* says a project that
"has migrated its backlog away", which is A; *Scope* says "no task folder **and no local task
config**", which is B. They are not the same class, and the criteria are written about A. Class C is
the control: it is where the deck-building sibling belongs, and its presence there is what shows the
rule discriminates rather than merely partitions.

**One folder is excluded by name**: the scratchpad directory this session's failed headless probe
created. It is class B by the rule, and counting it would be this session measuring itself.

### Step 2 — the served half: yes, and the figure is 414

Of the 11 class-A sessions, **10 were served** the skill. The one that was not is dated
**2026-07-16**, before the user-scope install of 2026-08-11 — so **every class-A session started since
the plugin was installed was served it**, and the exception dates the install rather than qualifying
the result.

The entry is **414 characters**, identical in every session in every class that saw it:

| Part | Characters | Where it comes from |
| :--- | ---: | :--- |
| the `description:` line in `plugin/skills/taskmd/SKILL.md` | 397 | the file |
| the prefix the harness writes before it | 17 | the harness, at serve time |
| **the line a session is handed** | **414** | measured |

**That 17 is the whole reason for insisting on the entry as served.** It is in no file this
repository owns, so nothing that counts files can see it.

### Step 3 — the stopping point: the trigger half is unobserved, and stays that way

The plan put this before anything was written, because *unobserved* is a legitimate result only while
it is still available. It is the result.

| Probe over the 11 class-A sessions | Result |
| :--- | :--- |
| Sessions asking for task work in ordinary words — the description's own phrasing: *work on next*, *next task*, *start / specify / plan / implement / review / close a task* | **0** |
| Turns containing the literal token `taskmd` | 7, in 3 sessions, split 6 and 1 across the two projects |
| Of those, turns opening their session | **0** |
| Skills actually invoked anywhere in class A | `handoff` twice, `code-review` once |
| taskmd invocations | **0** |

**The zero does not mean the trigger failed.** Nothing asked. A description cannot be matched against
a request that was never made, and the 7 literal mentions all arrive mid-session, in projects whose
work is *about* this repository and its siblings rather than a request for task work — so they are
confounded in the direction that matters, and are reported as confounded per criterion 3. Treating
this corpus as a negative would score a silent trigger and a working one alike.

**What would show it**, stated so the next attempt does not have to re-derive it: one session in
either class-A project whose **first** substantive request is task work in ordinary words, with the
skill unnamed and no handoff or command supplying it. That is the arrangement
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 8 had to make by hand, and
what has changed since is that a venue now exists: step 9 of that record says a clean measurement
"would need a project that uses taskmd and does not describe it in its always-loaded conventions",
and calls that outside what the task could reach. Class A is two such projects.

### Step 4 — folded into step 3

Step 4 was to take the trigger half as far as step 3 allowed. Step 3 allowed nothing further, and the
plan is not re-cut around that — it is the outcome the step was placed there to make available.

### Step 5 — what was already answered, and what was not

- **`tests/test_budget.py` answers neither half, and its arithmetic differs from a session's.** It
  measures **this repository's** tier 1 — `CLAUDE.md` plus each served skill's `description` **as it
  appears in the file** — against `reference/TASK-WORKFLOW.md`. It never reads another project, so it
  cannot speak about one; and it counts **397** where a class-A session pays **414**, because the
  17-character prefix is added at serve time. Its own `SCOPE` line already says a pass is not a clean
  load path. This is that caveat with a number on it, and it is a limit of scope rather than a defect
  in the test.
- **[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) answers the served half for
  this repository only, and says so itself.** It confirmed the tier table on a session that was
  handed the skill, in this repository, where `CLAUDE.md` names the skill in tier 1 — the confound its
  §3 step 9 records and calls unremovable *here*. Neither half transfers to a project with no task
  folder, and step 9 names the missing venue that step 3 above has now found.

So *already half-answered* was the right instinct and the wrong split: what existed was the **unit and
the method**, not either answer.

### Step 6 — the bullet

[`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md),
*What survives*. The claim now carries what was measured, when, against what, and — in the same
sentence — that the trigger half was not observed. Restated rather than cited, per criterion 5.

### Step 7 — verification

Run, not asserted:

```text
OK - 173 task(s), 865 field value(s), 585 reference(s), 24 dependency edge(s), 269 declared output(s)
276 passed, 8 subtests passed in 22.06s
```

`index` was regenerated and `check` was clean afterwards. The document's own diff is **one hunk, six
lines in and one out**, and the line out is the bullet the lines in replace — criterion 6, checked by
reading the diff rather than by intending not to touch anything else.

**The check that earned its silence.** Step 1's rule was observed failing on the deck-building
sibling before it was fixed. The 414 figure is corroborated the same way: it is identical across all
three classes and 87 served sessions, so a per-project accident would have shown as a spread.

**The honest gap, recorded rather than implied.** The bullet has **not** been put in front of an
uninvolved reader. Every other claim in that listing reached its present form through one — it is the
method [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) used twice, and its
second run is what raised this task. A reader is the only check that can catch what the mechanical
ones cannot: whether a sourced cost sentence tilts a document whose lean
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed as accepted. Not run here, because it
needs a fresh agent and this session was not asked to spawn one. `review` judges the gap; it is not
papered over.

### The sweep script, added 2026-08-19 by T-174

**This section was added after the fact and is not a record of what this task did.** `plan` decided
the script would be *quoted in §3*; `implement` recorded it as *described here rather than pasted*
and the scratchpad it lived in did not survive the session, so §4's criterion 2 failed and
[T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md) was raised to carry it. The script
below was **reconstructed from this record's own prose**, then run, and it reproduces every figure
above. The reconstruction is therefore also the test of whether the prose was sufficient, and
T-174 §3 records where it was not.

It names no project, no path and no person: the classes come out of the rule, so it is quotable here
and runs for anybody who has such a store.

```python
"""T-168's sweep. Selects the subset by rule, then measures the served and trigger halves.

Reads the agent's own transcript store, which is machine-private: one folder per project, one
JSONL file per session. It names no project and no path of its own - the classes come out of the
rule below - so it is quotable in a published record and runs for anybody who has such a store.
"""
import json
import os
import pathlib
import re

STORE = pathlib.Path.home() / ".claude" / "projects"
ASKED = re.compile(r"work on next|next task|(start|specify|plan|implement|review|close)\s+"
                   r"(the\s+|a\s+|this\s+)?task", re.I)


def first(path, key):
    for rec in records(path):
        if rec.get(key):
            return rec[key]
    return None


def records(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                yield json.loads(line)
            except ValueError:
                continue


def tasks_dir(config):
    """The configured value, with an inline comment and quotes stripped.

    The comment strip is load-bearing: without it the path tested is `tasks` plus the trailing
    comment, which resolves nowhere, and every config-carrying project reads as migrated away.
    """
    for line in open(config, encoding="utf-8", errors="replace"):
        if line.startswith("tasks_dir:"):
            return line.split(":", 1)[1].split(" #")[0].strip().strip("'\"")
    return None


def classify(cwd):
    if not cwd or not os.path.isdir(cwd):
        return "?"
    config = os.path.join(cwd, ".taskmd", "config.md")
    if not os.path.isfile(config):
        return "B" if not os.path.isdir(os.path.join(cwd, "tasks")) else "C"
    named = tasks_dir(config)
    return "C" if named and os.path.isdir(os.path.join(cwd, named)) else "A"


def turns(path):
    """What a person actually typed, in order.

    `isMeta` records are typed `user` and nobody typed them - a skill stub, a slash-command body,
    a hook message. Counting them answers a different question: every one of this sweep's own
    false positives was one string, the handoff skill's stub, matched in seven sessions.
    """
    out = []
    for rec in records(path):
        if rec.get("type") != "user" or rec.get("isMeta"):
            continue
        content = rec.get("message", {}).get("content", "")
        if isinstance(content, list):
            content = " ".join(c.get("text", "") for c in content
                               if isinstance(c, dict) and c.get("type") == "text")
        if isinstance(content, str) and content.strip():
            out.append(content)
    return out


def served(path):
    """The taskmd entry of this session's skill listing, '' if listed without it, None if absent."""
    for rec in records(path):
        if rec.get("attachment", {}).get("type") != "skill_listing":
            continue
        for entry in rec["attachment"].get("content", "").split("\n"):
            if entry.startswith("- taskmd:"):
                return entry
        return ""
    return None


# ------------------------------------------------------------------ step 1: the subset, by rule
projects = {}
for folder in sorted(STORE.iterdir()):
    files = sorted(folder.glob("*.jsonl")) if folder.is_dir() else []
    if files:
        projects[folder] = (classify(first(files[0], "cwd")), files)

# This session's own scratchpad folder is excluded by name: it is class B by the rule, and
# counting it would be the session measuring itself.
EXCLUDE = "scratchpad"
for klass in "ABC?":
    chosen = [(f, v) for f, v in projects.items()
              if v[0] == klass and EXCLUDE not in f.name]
    print("class %s: %d project(s), %d session(s)"
          % (klass, len(chosen), sum(len(v[1]) for _, v in chosen)))

a_projects = [v[1] for f, v in projects.items() if v[0] == "A"]
a_files = [p for group in a_projects for p in group]

# ------------------------------------------------------------------ step 2: the served half
lines = [served(p) for p in a_files]
sizes = sorted(set(len(x) for x in lines if x))
print("served: %d of %d class-A session(s); line length as served: %s"
      % (sum(1 for x in lines if x), len(a_files), sizes))

# ------------------------------------------------------------------ step 3: the trigger half
asking = sum(1 for p in a_files if any(ASKED.search(t) for t in turns(p)))
hits = [(p, [t for t in turns(p) if "taskmd" in t]) for p in a_files]
hits = [(p, h) for p, h in hits if h]
opening = sum(1 for p, _ in hits if "taskmd" in turns(p)[0])
skills = []
for p in a_files:
    for line in open(p, encoding="utf-8", errors="replace"):
        if '"Skill"' in line:
            skills += re.findall(r'"name"\s*:\s*"Skill".{0,200}?"skill"\s*:\s*"([a-z0-9:_-]+)"',
                                 line)
print("asked for task work in ordinary words: %d session(s)" % asking)
by_project = sorted((sum(len(h) for p, h in hits if p in group) for group in a_projects),
                    reverse=True)
print("turns holding the literal token: %d in %d session(s), split %s across the projects"
      % (sum(len(h) for _, h in hits), len(hits), by_project))
print("of those, turns opening their session: %d" % opening)
print("skills invoked anywhere in class A: %s"
      % sorted((s, skills.count(s)) for s in set(skills)))
```

Run on 2026-08-19:

```text
class A: 2 project(s), 11 session(s)
class B: 4 project(s), 7 session(s)
class C: 5 project(s), 179 session(s)
class ?: 0 project(s), 0 session(s)
served: 10 of 11 class-A session(s); line length as served: [414]
asked for task work in ordinary words: 0 session(s)
turns holding the literal token: 7 in 3 session(s), split [6, 1] across the projects
of those, turns opening their session: 0
skills invoked anywhere in class A: [('code-review', 1), ('handoff', 2)]
```

**Every figure this section reports reproduces, except class C's session count**, which is 179 today
against the 174 recorded above: this repository's own transcript folder is class C and has gained
sessions since 2026-08-18. Class A, the class every criterion here is written about, is unchanged at
2 and 11, and so are 10 of 11, 414, and all four trigger rows.

**Decisions & assumptions**

- **Class B is measured and reported alongside A rather than folded into it.** — §1's *Outcome* and its
  *Scope* describe different populations, and quoting one figure for both is the failure where a
  task's measured class is not the class it names. — 2026-08-18
- **The 7 literal `taskmd` mentions are reported as confounded, not as a negative observation.** —
  None opens a session, and all sit in work about this repository, so the description was never the
  thing being matched. Recording them as a failed trigger would put a direction into the listing that
  the corpus cannot support. — 2026-08-18
- **The bullet states the cost and the unobserved trigger, and nothing else.** — *Rejected: calling it
  the only survivor with a running cost*, which is true and is a ranking against the other three
  bullets. §1 puts the five accepted framing mechanisms out of scope, and a number is not a licence to
  re-balance the document. — 2026-08-18
- **The sweep scripts stay in the scratchpad and are described here rather than pasted.** — Taken at
  `plan` and carried out unchanged. *Annotated 2026-08-19 by [T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md): the second half of that sentence is false, and it is the whole reason T-174 exists. `plan` decided **quoted in §3**, not described, so this was a change carried out silently, which [`implement`](../plugin/skills/taskmd/docs/method/implement.md) step 3 forbids. The bullet is left as written because it records what was believed on 2026-08-18; the script it should have carried is above.* They read a machine-private store, and a test under `tests/`
  reading it could never run for an adopter. — 2026-08-18

**Outputs produced**
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — the sourced survivor bullet
- This record, §3 — the measurement and the four findings

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Whether the harness serves the skill, from a session that was *handed* the listing | met | 10 of 11 class-A sessions served; the twelfth is dated 2026-07-16, before the install. Read from each session's own `skill_listing` attachment, so the evidence is what arrived and not what the install scope implies |
| The cost in characters, **with the command that produced it**, counting the entry as served | **not met** | The figure, the unit and what was counted are all there and correct — 414, decomposed as 397 plus a 17-character prefix. The command is not. → **[T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md)** |
| Whether a request for task work reaches the skill, or an unobserved result naming what would show it | met | §3 step 3 records it unobserved, names the probe, and reports the 7 literal mentions as confounded rather than as a direction — 0 of 11 sessions asked for task work, so there was nothing to match |
| What `tests/test_budget.py` and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) cover and do not | met | §3 step 5. Each is named with its limit, and the budget test's 397-against-414 gap is stated as a limit of scope rather than as a defect |
| The survivor bullet carries its evidence in the neighbours' form — restated, not cited | met | The bullet states what was measured, against what, and when, and links to nothing. Read against the three beside it, which use the same *this was run on that* shape |
| Nothing else in the listing changes | met | One hunk, six lines in and one out, and the line out is the bullet the lines in replace. Settled by reading the diff |

**Five met, one carried.** The one that failed is a record defect rather than a wrong answer: the
figures are right and nobody can re-produce them from the record alone.

**What review found beyond the table, and did not fix.** Criterion 2 failed because a `plan` decision
changed at `implement` without being flagged — planned as *quoted in §3*, carried out as *described
here*. That is the substitution
[`implement`](../plugin/skills/taskmd/docs/method/implement.md) step 3 exists to prevent, and it is
the more useful half of the finding, so it is written into
[T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md) rather than repaired here.

**The open questions, read before closing** ([`review`](../plugin/skills/taskmd/docs/method/review.md)
step 5). §1's *can a session measure this about itself* is answered in place. Two residues were live
and neither fails a criterion, so nothing in the table would have carried them and both would have
left every view the moment this task closed:

- the trigger probe, which needs a session nobody here can arrange →
  [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md);
- the uninvolved reader the new bullet has not had →
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md).

**Child fix tasks raised**
- [T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md) — the command behind the figures
- [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) — the trigger half,
  observed rather than argued
- [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) — the reader the bullet
  has not had

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **[T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) no longer records this task as its parent** — re-edged to a soft edge by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), under the rule the owner settled on 2026-08-22 that a child holds every parent open. T-176 came out of `review` step 5 rather than from a failed criterion, and waits on an uninvolved reader nobody here can supply. **§4 is unchanged**, including its list of the three tasks this review raised. The judgement and its rejected alternative are in T-216 §3. |
| 2026-08-18 | → done | Five criteria met, one carried, three children raised. **The failure is criterion 2 and it is a record defect, not a wrong answer** — the 414 figure is right and nobody can re-produce it from the record, because a `plan` decision to *quote* the script became *describe* at `implement` with nothing flagging the change. That silent narrowing is the more useful half of the finding and it travels with [T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md) rather than being repaired here, since a review that fixes what it finds destroys the record of what was wrong. **Two residues failed no criterion and would have gone invisible at close**, which is the class [`review`](../plugin/skills/taskmd/docs/method/review.md) step 5 exists for: the trigger probe nobody in a session can arrange, and the uninvolved reader every other claim in that listing passed through. Both now have owners. **What this task actually bought the listing** is one sourced sentence where there was an assertion, and the honest shape of it is that half the claim is measured and half is declared unobserved in the same breath — which is stronger than the confident version it replaced. |
| 2026-08-18 | → review | `implement` run under the same authorisation, seven steps in the planned order. **The served half is answered: 414 characters, every class-A session since the install.** **The trigger half is unobserved, and step 3 is why that is a result rather than a gap** — nothing in 11 sessions asked for task work, so the corpus scores a silent trigger and a working one alike. **The load-bearing event is that the subset rule was caught being wrong**: its first version read the configs' trailing inline comment as part of the path and classified the 60-task deck-building sibling as migrated-away. It was the contradiction that surfaced it, not a review, and a rule seen failing on a case it must catch is the only kind whose later silence means anything. Two things came out that §1 did not have. *Already half-answered* was the right instinct and the wrong split — what existed was the unit and the method, not either answer, and `tests/test_budget.py` counts **397** where a session pays **414**, because the harness's own prefix is in no file. And [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9's confound, recorded there as unremovable from inside this repository, now has the venue it said it lacked: class A is two projects that use taskmd and do not name it in their always-loaded conventions. **One gap is declared rather than closed** — no uninvolved reader has seen the new bullet, which is the check every other claim in that listing passed, and `review` is left to judge it. |
| 2026-08-18 | → planned | Seven steps under the same authorisation. **Ordered so the step that can invalidate the rest comes third rather than last**: whether the selected subset holds a session that asked for task work decides whether steps 4 onward write an observed direction or an *unobserved* one, and §1's criterion 3 already says both are passes. Placing it after the writing would have made the honest result the expensive one. **The subset is defined by a rule rather than by naming the sibling** — the context-audit checkout is the specimen this task was raised with, and hand-listing it would rebuild the enumeration `.handoff/config.md` has now recorded three separate failures of. Three decisions are recorded with what they reject; the load-bearing one is that the sweep script is quoted rather than committed, since it reads a machine-private store no adopter has and a test under `tests/` reading it could never run for them. |
| 2026-08-18 | — | **The one question `specify` put is answered: sweep the store first.** The trigger half is taken from the transcripts across every project folder, and where the migrated-away subset holds no session that asked for task work, criterion 3 is met by recording it **unobserved with what would show it** rather than by manufacturing a direction — the probe then leaves as its own task. *Rejected: the maintainer running the probe out-of-band first*, the [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 8 shape. It would give a clean observation instead of a possible *unobserved*, and would close the `CLAUDE.md` confound that record's step 9 called unfixable from inside this repository — but it blocks the phase on a person for a half the corpus may already answer, and the corpus is free. *Rejected: sweeping and then stopping to ask again* — criterion 3 already says what an empty subset produces, so the second ask would be re-deciding something written down. **A second question was answered in the same turn and is not this task's**: the transcript instrument generalises to any session on this machine, which is the context-audit sibling's subject and not taskmd's, so nothing is raised here and the cross-repo rule sends it there rather than describing it to it. |
| 2026-08-18 | → specified | `specify` run under the whole-lifecycle authorisation in the row below. **The six criteria were drafted by this session and not agreed by the owner** — the authorisation covers running the phases and cannot pre-agree criteria that did not exist when it was given, so the draft says so in §1 and carries a guard instead: five of the six are settled by running something, and the sixth exists only to make [T-167](T-167-stop-the-listing-pricing-only-the-rival.md)'s out-of-scope decision checkable rather than merely asserted. **The open question is answered, by an instrument this project had not used.** Three were tried. Headless `claude -p` in another directory returns `401 OAuth access token has expired` — the same failure [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 5 recorded on 2026-08-07, and that record named it as the one command that would answer this task; re-verified today, it still does not run. A spawned subagent cannot leave this project. **The harness's own session transcripts can**: each session's initial skill listing is stored under a per-project folder as an attachment of type `skill_listing`, so what a session was handed unasked is readable after the fact for projects this repository cannot start a session in. **Measured on the context-audit sibling** — a project carrying a `.taskmd` config whose `tasks_dir` does not resolve, labelled in `control/LOCAL-CONTEXT.md` — the skill **is** served: `isInitial` true, `taskmd:taskmd` present among 66 entries, and its line **414 characters**, being the 397-character `description:` line plus the 17 the harness's own `- taskmd:taskmd: ` prefix adds. That 17 is precisely what `tests/test_budget.py` does not count, which is why a criterion asks for the entry **as served** rather than for the file, and why the two halves of *already half-answered* had to be separated instead of assumed. **The trigger half is not answered and the corpus must not be read as answering it**: that project has one session, it asked for no task work, and it invoked no skill of any kind, so its zero is noise and not a negative. That is the single question this phase puts to the maintainer. |
| 2026-08-18 | — | **The maintainer authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. It covers **this task and nothing it raises**. Recorded here as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). **Two specimens arrived the same day and are not this row's opinion about them.** Closing T-173 required running `check --root` against four sibling checkouts, and **two returned `CONFIG ERROR` on `tasks_dir`** — a project carrying a `.taskmd/config.md` with no task folder the command can resolve, which is this task's subject standing in the open. One of the two also declares `id_width: none`, so the error names a second cause: a backend allocates its ids and its tasks are not local files. Both are labelled in `control/LOCAL-CONTEXT.md`, and the run is in [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) §3 step 6. Routed here rather than into §1 deliberately: `specify` decides what counts as evidence, and a session that pre-filled its inputs would have chosen for it. |
| 2026-08-17 | — | **Rescoped when [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) was cancelled**, on the maintainer's decision the same day. The consumer of the measurement is now the unsourced survivor claim rather than the pricing sentence, and the five framing mechanisms are explicitly out — a number arriving is not an occasion to re-open a judgement somebody made. Recorded because a task whose stated reason has been cancelled and whose scope still reads as if it had not is the shape that gets quietly re-widened by whoever picks it up. |
| 2026-08-17 | → proposed | Raised from [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3, where an uninvolved reader named it as the fact that would most change their recommendation. Raised separately from [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) because it is a **measurement**, not an edit: the listing cannot price keeping taskmd alone until somebody knows the price, and writing the sentence first would put an unevidenced claim into the one place this repository has just finished removing them from. `high` — it is the load-bearing claim of the whole listing and currently the only unsourced one. **Not covered by the authorisation of 2026-08-17**, which named [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) and excluded what it raises. |
