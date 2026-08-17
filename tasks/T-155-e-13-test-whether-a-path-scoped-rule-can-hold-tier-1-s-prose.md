---
id: T-155
title: E-13 — Test whether a path-scoped rule can hold tier 1's prose about itself
type: decision
status: done
phase: review
parent: T-152
blocked_by: []
related: [T-118, T-153, T-159]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-17
deliverables: []
---

# T-155 — E-13: test whether a path-scoped rule can hold tier 1's prose about itself

## 1. Specify

**Outcome**
A measured answer to whether the block of `CLAUDE.md` that is prose about `CLAUDE.md` can be scoped to
that file — **reported, and not carried**. What survives is the boundary: which loads the mechanism
reached and which it did not.

**Why this one**
Finding [E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), whose portable half is
[E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03). Both are stated there.

**Tested, not carried — the maintainer's ruling, 2026-08-15.** The remedy re-opens
[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md), which settled that an unannounced
activity is the exception that keeps a rule in tier 1. **New evidence licenses re-opening a recorded
decision, never reversing it**, so this task measures and reports; whether anything moves is a
separate decision taken on what it finds.

**Blocked by [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md)**, which settles the policy
question this task cites. Specifying the two independently produces inconsistent answers.

**Scope**
- In: the settling test the finding names — write the rule, restart, and read the `InstructionsLoaded`
  hook's log rather than the harness's documentation.
- In: the compaction case, which is the risk that decides the answer: compact, edit the instruction
  file, and observe whether the rule fires a second time.
- In: the objection that `.claude/rules/` is harness-specific while this repository ships a plugin
  meant to work anywhere. A mechanism an adopter cannot receive is worth less here than the size says.
- In: re-measuring the carve-out — how much of the block is operative for the agent rather than
  addressed to the maintainer. The audit's estimate is an estimate and says so.
- Out: moving anything in `CLAUDE.md`. Nothing moves in this task.
- Out: the justification passages that can stay in the file at no per-turn cost. That is
  [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md), taken first, and it may
  leave less here to argue about.

**Inputs**
- [E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) — the measured block and its three
  risks
- [E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03) — the mechanism and the named test
- [E-20](../docs/audits/2026-08-15-context-economy-portable.md#e-20) — why this remedy is measured
  rather than obeyed
- [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) — the decision this re-opens, and
  the reason it was taken

**Acceptance criteria**
- [ ] The test was run: a rule written, a session restarted, and the load **observed** — a document's
      claim about its own loading is not evidence
- [ ] The compaction case is answered by observation, or recorded as not answered and why
- [ ] The report names which loads the mechanism reached and which it did not, rather than a verdict
- [ ] Two failed attempts stop the task, with what survives recorded
- [ ] Nothing in `CLAUDE.md` moved as part of this task
- [ ] The carve-out is re-measured at the time of the test, not carried from the audit
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Where does the carry decision go if the test succeeds?** A follow-up task, or
  [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) re-opened in place. Re-opening a
  closed record has a cost this project has not paid before. **The maintainer answers, at `specify`.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Answer `specify`'s open question first — it decides what a **success** produces, and answering it afterwards would let the result choose the answer | The decision below |
| 2 | Re-measure the block at test time. [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) has already taken part of it at no risk, so the audit's figure is stale by construction | The figure below |
| 3 | Weigh the portability objection, which can be settled by reading what an adopter receives | The finding below |
| 4 | **Ask the maintainer to enable the `InstructionsLoaded` hook.** It is user-scope configuration, not this repository's to write | A hook that logs when an instruction file enters context |
| 5 | Write one rule under `.claude/rules/` with a `paths:` glob matching `CLAUDE.md`, carrying a **marker sentence and not the real block** — the block moving is the change this task must not carry | The candidate rule |
| 6 | Restart. Read the log: did the rule load at session start, and did it load when `CLAUDE.md` was read? | Observation 1 |
| 7 | Compact, edit `CLAUDE.md`, read the log again: did it fire a second time? | Observation 2 — the risk that decides the answer |
| 8 | Report the boundary — which loads the mechanism reached and which it did not. **Two failed attempts stop the task** | The report |
| 9 | Raise the carry decision as its own task **only if** the mechanism holds | one task, or none |

## 3. Implement

**Steps 1–3 are done. Steps 4–9 need a session that has not started yet** — see the boundary below.

**The block is smaller than the audit measured.** Re-measured 2026-08-15, after
[T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md):

```
paid meta-block: 1578 chars
paid tier-1 file: 5908
share: 26.7%
```

E-13 measured 2,384 characters, 36.3% of a 6,571-character file. **806 of them have already gone**,
into block comments, at no relocation risk and with no decision re-opened. Against the finding's own
carve-out estimate — 400 to 600 characters of the block operative for the agent — what a successful
relocation would now extract is roughly **1,000 to 1,180 characters**, about half what phase 1
priced. The remedy has to be worth its three risks at that size, not at the original one.

**The portability objection is weaker than it looks.** Risk 3 said `.claude/rules/` is
harness-specific while this repository ships a plugin meant to work anywhere. But the rule would
govern `CLAUDE.md`, and **`CLAUDE.md` is not shipped either** — since T-053 the plugin is the
`plugin/` subtree, so neither the instruction file nor a rule beside it reaches an adopter. The
objection applies to advising adopters to use the mechanism, which nothing here proposes. Risks 1 and
2 — compaction, and a recorded decision re-opened — are untouched and are what the test is for.

**Decisions & assumptions**

- **A success produces a new task, not a re-opened [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md)** — 2026-08-15, answering
  `specify`'s open question. METHOD rule 5 keeps binding after a task closes: correct what a record
  says about the **present**, never rewrite what it says about the **past**. T-118's decision is a
  dated statement about what was known then, and it was right on what it knew. A new task cites it,
  carries the new evidence, and leaves the record intact. *Rejected:* editing T-118's decision in
  place, which would destroy the only account of why the prose stayed.
- **The candidate rule carries a marker, not the block** — 2026-08-15. The task tests a *mechanism*.
  Putting the real prose in the rule would carry the change under cover of testing it, which is the
  thing the maintainer's ruling forbids.
- **The hook is the maintainer's to enable** — 2026-08-15. It is persistent user-scope configuration
  outside this repository, so this task asks rather than writes.

**Step 4 — the instrument is not installed, and that is measured rather than assumed.** Read on
2026-08-17: the user-scope settings file has no `hooks` key at all, and there is no `.claude/rules/`
directory at either scope. So the `InstructionsLoaded` hook has never been enabled, and step 4's ask
is still outstanding rather than done-and-forgotten. It stays the maintainer's: it is persistent
user-scope configuration outside this repository.

**Step 5 — the probe is written, which is the half that has to happen in the session *before* the
observing one.** `.claude/rules/t-155-probe.md`, `paths:` matching `CLAUDE.md`, carrying the marker
`T155-PROBE-9F3A2C` and **no part of the real block** — the decision above forbids carrying the change
under cover of testing it. The next session to start can be asked one question: can it see that
string.

**The format is taken from the finding and is itself unverified — recorded so a null result stays
readable.** [E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03)'s source is harness
documentation and it says *hypothesis, unverified*. If the next session cannot see the marker, there
are three explanations and this record must not let them collapse into one: the mechanism does not
exist, the mechanism exists and is evaluated only at session start, or the front matter is written
wrong. The catalogue's row 46 is the precedent for keeping that distinction — a lever was rejected
there because its only source was a feature request, not because it was shown not to work.

**A fourth risk the finding did not name, and it was found by writing the file.** `.gitignore`
excludes `.claude/*` and re-includes exactly one file, `settings.json` — the exclusion exists because
the harness writes into that folder on its own schedule, including machine paths. **So a rule placed
there is machine-local: no clone receives it.** The remedy E-13 proposes would therefore move prose
out of a file every clone gets and into one no clone gets, unless the ignore rule is amended to
re-include `.claude/rules/` — which means re-including part of a directory that was excluded
wholesale for a stated reason. Surmountable, and it was not among the three risks the finding
weighed. It points the same way as the other two things this task has established: the prize is
smaller than phase 1 priced it, and the cost is larger.

**Outputs produced**

- `.claude/rules/t-155-probe.md` — the candidate rule, machine-local, to be deleted once this task
  records its answer. Not a deliverable: it is the instrument.
- The two figures above are the outputs of steps 2 and 3; the three findings above are steps 4 and 5.

**The boundary, and why it is here.** Steps 4 to 9 need an instruction file to be **loaded** after it
changes, and a session's copy is fixed before its first tool call — so no session can observe its own
change. The maintainer chose on 2026-08-15 to leave that to a later session rather than spend a
subagent as the instrument. This task therefore stops at `implement` with its phase intact: it is
waiting, and waiting is not a phase.

**The boundary moved on 2026-08-17 and did not dissolve.** Steps 4 and 5 are now done, so what
remains is one restart rather than two sessions of work: the probe is in place and the next session
to start either sees the marker or does not. What still cannot happen here is criterion 1, which asks
for a rule written, **a session restarted**, and the load observed — this session wrote the rule, so
it is the one session that structurally cannot be the observer. **The marker is a second instrument
and may make the hook optional**: it observes the content arriving rather than a hook's report that
it did, which is closer to what the criterion actually asks for. The hook is still worth enabling,
because it separates *loaded at session start* from *loaded when the file was read*, and that
distinction is the whole claim under test.

**What the probe can actually distinguish — and it is not a yes/no.** `CLAUDE.md` is tier 1: it is
loaded on every turn of every session, by definition. So a rule scoped to `paths: CLAUDE.md` fires at
session start **if** the harness matches paths against the files it auto-loads as instructions.
E-13's remedy needs the opposite — the rule must fire only when `CLAUDE.md` is opened as a file
somebody is editing. That is the entire question, and it makes the reading a three-way table:

| Observation | What it means |
| :--- | :--- |
| **A** — the marker is in context at session start, before any tool call | **The remedy saves nothing.** A rule scoped to an always-loaded file is itself always loaded, and the prose has moved without leaving the load path. E-13 closes negative and the carry decision never arises |
| **A** no, **B** yes — absent at start, present after `CLAUDE.md` is explicitly read | The mechanism does what the finding hoped, and the carry decision becomes real |
| **A** no, **B** no | The mechanism did not reach. **Three readings**, named above, and this record must not let them collapse into one |

**The observation contaminates itself, so the order is part of the test.** The marker string is
written into this record and into the rule file. A session that opens either one has the string in
context and can no longer say where it came from. So the next session must answer **A before its
first tool call**, then read `CLAUDE.md` and nothing else for **B**, and only then open this record.
The handoff carries that instruction and deliberately does **not** carry the string.

**Observed 2026-08-17 — it is the middle row: A no, B yes.** Run by a session that started after the
probe was written, which is what criterion 1 asks for.

| | Observation | What was looked at |
| :--- | :--- | :--- |
| **A** | **No** — the marker was not in context at session start | The context handed over unasked named exactly three sources: the user-scope instruction file, this repository's `CLAUDE.md`, and the memory index. No `.claude/rules/` block anywhere in it, and no `T155-PROBE-9F3A2C` |
| **B** | **Yes** — it arrived when `CLAUDE.md` was read | The probe's body came back as a separate message appended to that read's result, naming the file it came from and carrying the marker |

**The trigger is isolated to the read, not merely to the session.** Answering A took four reads first
— the handoff skill's own files, this project's handoff config, and the handoff itself — and the
marker was absent through all four. It appeared on the next call, which was `CLAUDE.md` and nothing
else. So *before any tool call* is not the condition that was actually met; *before reading any file
the rule's glob matches* is, and it is the stronger of the two, because it names the trigger instead
of only timing it.

**One of the null result's three readings is now closed, and the format is no longer a hypothesis.**
The front matter under test was `paths:` with a single entry, `CLAUDE.md`. It fired, so
[E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03)'s *unverified* qualifier can be
dropped for this one shape. The harness delivers the **body only** — the front matter is consumed on
the way in, not passed through.

**What this does not settle, and criterion 2 is the whole of it.** Observation 2 asks whether the rule
fires again after a compaction. A session can neither force a compaction nor read a hook that was
never enabled, so step 4 is still outstanding and **criterion 2 is unanswered rather than met**. What
was seen is one delivery tied to one read; nothing here says how long it survives, or whether a second
read in the same session delivers it twice.

**The carve-out figure holds at test time.** `CLAUDE.md` has not changed since it was re-measured —
`git log -1 -- CLAUDE.md` is 2026-08-15, the same day — so the 1,578 characters and 26.7% above are
what the test ran against rather than a figure carried forward.

**Step 9 is live and is not this session's to take.** The middle row makes the carry decision real,
and the decision above sends it to a new task rather than to a re-opened
[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md). The handoff that authorised this
observation covered T-155 and **nothing T-155 raises**, so the task is named here and not created.

**The instrument is retained, and that is a departure from what this record says to do.** Both this
record and the handoff say to delete `.claude/rules/t-155-probe.md` once the answer is recorded.
Deleting it now forecloses observation 2 permanently — it is the only thing a later session could
compact against — so it stays until the maintainer rules on criterion 2. It is machine-local and
reaches no clone; what it costs is one injection per read of `CLAUDE.md`.

## 4. Review

Run 2026-08-17, against the criteria as `specify` wrote them.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The test was run: a rule written, a session restarted, and the load **observed** | met | The rule was written by the session of 2026-08-17; the observing session started after it, which is the separation the criterion is built around. The load was observed **directly** — the probe's body arriving in context — rather than through a hook's report of it, which is closer to what "a document's claim about its own loading is not evidence" asks for |
| The compaction case is answered by observation, or recorded as not answered and why | met | By the criterion's **second** branch, and it is worth saying plainly: the compaction case is **not answered**. §3 records why — no session can force a compaction, and step 4's hook was never enabled. The gap and the instrument that would close it are carried by [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) |
| The report names which loads the mechanism reached and which it did not, rather than a verdict | met | §3 names both sides: reached — a read of a file the `paths:` glob matches; not reached — the session-start load of that same always-loaded file, and any second firing after a compaction. It stops short of saying whether the prose should move, which is the point of the maintainer's ruling |
| Two failed attempts stop the task, with what survives recorded | met | **Not exercised.** The first attempt answered, so the stopping rule never fired. Recorded rather than ticked in silence, because a rule that was never tested passes for a different reason than one that held |
| Nothing in `CLAUDE.md` moved as part of this task | met | `git log -1 -- CLAUDE.md` is `557a7ec`, 2026-08-15, +30/−11 — [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s block-comment work, and no change since. The probe carries a marker and no part of the block |
| The carve-out is re-measured at the time of the test, not carried from the audit | met | Re-measured 2026-08-15 at 1,578 characters / 26.7%, and `CLAUDE.md` is unchanged since — so what the test ran against **is** the measured figure, not one carried from the audit. The audit's 2,384 was never used |
| The measured outcome is written into this record on the day it is known, not reconstructed later | met | §3's observation and the log row are dated 2026-08-17, the day the probe was read |

**Seven met, none carried, and one open question discharged.** `specify` asked where the carry
decision goes if the test succeeds; the decision of 2026-08-15 answered it — a new task, never a
re-opened [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) — and step 9 has now
acted on it. **Two residues aimed at the maintainer were live at closing and are routed rather than
left here**: step 4's request to enable the `InstructionsLoaded` hook, which this repository cannot
write, and whether `.claude/rules/t-155-probe.md` should be deleted or kept. Both are open questions
on [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md), because
a question left in a closed record leaves every view the project has.

**Child fix tasks raised**
- [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) — not a
  fix but the plan's step 9: the carry decision this task was forbidden to take. Raised because the
  mechanism held

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | — | **§3's last paragraph is now false in the present, and is annotated rather than rewritten** (METHOD rule 5). It says `.claude/rules/t-155-probe.md` is **kept** against this record's own instruction, pending the maintainer's ruling on criterion 2. The maintainer ruled the same day: the probe was **deleted**. That was right on what it knew and the reasoning stands; what changed is the world. A different probe now sits in that directory for [T-171](T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md), which is a separate instrument for a separate question and not this one restored. Also worth carrying back: this task's two-session design assumed a rule written mid-session is not delivered to that session, and T-171 **observed** it — the assumption was sound and is no longer an assumption. |
| 2026-08-17 | → done | `review` run against the seven criteria as written: **seven met, none carried**. Criterion 2 is met by its own second branch and the compaction case is genuinely unanswered — the criterion anticipated that, and the gap travels with the instrument to [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) rather than being buried in a tick. Criterion 4 was **never exercised**, which is recorded in its row for the same reason. Step 9 raised T-169, the carry decision, because the mechanism held. Two residues addressed to the maintainer — the hook, and whether to delete the probe — were live at closing and are now open questions on T-169; a closing record is where a question aimed at somebody else goes invisible, so they were looked for rather than waited for. **The maintainer authorised `review` and the raise in one request on 2026-08-17**, covering T-155 and T-169's creation and **nothing else** — not [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), which T-155 was the last open child of. |
| 2026-08-17 | — | **The probe was run and it answered: A no, B yes** — the marker was absent from the context this session was handed and present the moment `CLAUDE.md` was read. That is the middle row of the table above, so the mechanism does what E-13 hoped and **the carry decision becomes real**. Three things came with it. The trigger is the *read*, not the session: four unrelated reads preceded A and none of them delivered the marker. The format is verified rather than assumed — `paths:` with one entry — so a null result's three readings never had to be separated, and the harness passes the body while consuming the front matter. And **criterion 2 is unanswered, not met**: observation 2 needs a compaction a session cannot force and a hook step 4 never installed. The instrument is therefore **kept** against both instructions to delete it, because deleting it forecloses observation 2 for good; that is the maintainer's to rule on. Step 9's task is named and not raised — the authorising handoff covered T-155 and nothing T-155 raises. |
| 2026-08-17 | — | **The maintainer asked to finish and close this. It did not close, and steps 4 and 5 are now done.** Step 4's precondition was read rather than assumed: no `hooks` key exists in user-scope settings and no `.claude/rules/` existed at either scope, so the instrument had never been installed. Step 5's probe is now written, machine-local, carrying a marker and none of the block. **What blocks closure is criterion 1 and nothing else** — it asks for a restart, and the session that writes the rule is structurally the one session that cannot observe it. Three things were found on the way, and all three weaken the remedy rather than the test: the front-matter format is itself unverified, so a null result has three readings and this record names them instead of letting them collapse; `.gitignore` excludes `.claude/*`, so a rule placed there reaches no clone — **a fourth risk the finding never weighed**; and the marker may make the hook optional by observing the content arrive rather than a hook's report of it. |
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), finding E-13. `decision` and not `fix`, on the maintainer's explicit ruling the same day: the remedy re-opens a decision recorded with a reason, so this task measures and reports and carries nothing. `s` — the work is one write, one restart and one observation, twice. |
| 2026-08-15 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review` — in a request covering T-153, T-154, T-155, T-156 and T-157 and **nothing else**. Any task raised from here takes one phase per request unless separately authorised (METHOD §3.1). Recorded in each of the five records because an authorisation kept anywhere else is one a later session can miss or stretch. |
| 2026-08-15 | → in_progress | `specify` and `plan` complete, `implement` begun and **stopped at its boundary**: steps 4 to 9 need a session that starts after a rule file is written, and no session can observe a change to the instruction file it was handed. `blocked_by` was cleared when [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md) closed. `review` has not run and must not — three of its criteria judge observations nobody has made. |
| 2026-08-15 | — | **The maintainer authorised this task's whole lifecycle again, for the session after this one**, given as the subject of a handoff (`create - work T-155 full lifecycle`). It covers finishing `implement` and running `review` on T-155 and **nothing else** — no other task, and nothing this task raises. Recorded here and not only in the handoff, which is consumed once and archived (METHOD §3.1). |
| 2026-08-15 | — | **Finishing `implement` takes two sessions, not one**, and whoever picks it up should plan for that rather than find it. Step 5 writes the rule; steps 6 and 7 observe whether it loaded — and a session cannot observe an instruction-file change it made itself. So one session writes the hook and the rule, and the next one reads the log. [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) has no such gap: its change is already committed, so the very next session can answer it. |
| 2026-08-15 | — | Two findings from the part that could be done, and both weaken the case for the change rather than strengthen it: the block is **1,578 characters, not 2,384**, because T-153 took 806 of it at no risk; and the portability objection largely dissolves, because `CLAUDE.md` is no more shipped to an adopter than a rule beside it would be. What survives as a reason to test is compaction and the re-opened decision. |
