---
id: T-252
title: Correct the README's file count for the copied skill, and decide whether a number belongs there
type: fix
status: done
phase: review
parent: T-241
blocked_by: []
related: [T-083, T-085]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - README.md
---

# T-252 — Correct the README's file count for the copied skill, and decide whether a number belongs there

## 1. Specify

**Outcome**
An adopter following [`README.md`](../README.md) *As a plain skill* can check their copy is complete
against a number that is true of the release they copied — or against no number at all, if the
project decides a hand-kept count is not worth keeping.

**Where this came from**
Finding 1 of [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md),
the audit of the published `0.6.0`. Measured against a fresh clone of the tag `v0.6.0` (`cb0702c`),
2026-08-23:

```text
README claims                                21 files
git ls-files plugin/skills/taskmd/ | wc -l   25
```

**It was right when it was written**, which is the part that decides what this task is about.
[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) followed the
section on a second operating system for `0.5.0` and recorded that *"the file count matches the
number the README claims"*, calling it a claim nobody had checked from outside. The folder then grew
past it. Nothing reported the drift, because nothing reads it: `check` validates references and
links, not prose arithmetic.

**A second number is in play and must not be confused with it.** A filesystem count of that folder
returns **31** once the tool has been run, because `taskmd/__pycache__/` appears and is gitignored.
T-085 predicted that figure and this audit reproduced it by accident. So a reader checking by `ls`
gets 31, a reader checking by `git ls-files` gets 25, and the README says 21 — three numbers, and the
README does not say which kind it means.

**Scope**
- In: `README.md`'s *As a plain skill* section, and any other place a count of that folder is stated
- In: deciding **whether** a number belongs there at all, since a hand-kept count of a growing folder
  is the thing that just drifted
- Out: changing what the folder contains
- Out: the `__pycache__` behaviour itself, which is Python's and is correct

**Inputs**
- [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) §3 —
  the measurement, the three numbers and how each was taken
- [T-083](T-083-make-the-skill-directory-self-contained.md) — why the folder is self-contained, which
  is the claim the count exists to support
- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) — the count
  verified from outside at `0.5.0`, and its note that a filesystem count says 31 and is wrong

**Acceptance criteria**
- [ ] The section states something true of the published artifact, checked against a clone of the
      tag rather than against the working tree
- [ ] If a number stays, it says which count it is — what a copy receives, not what `ls` shows after
      the tool has run once — and the decision records why a hand-kept number was kept over dropping
      it or deriving it
- [ ] If a number goes, the section still gives an adopter a way to tell their copy is complete
- [ ] Whatever is written cannot drift silently again, or the record says plainly that it can and
      that this is accepted

**Open questions**
- ~~**Does a count belong in the README at all?**~~ **Answered by the owner on 2026-08-23: no —
  replace it with a check the adopter can run.** *The question as it stood, with what was rejected:
  the recommendation was* **replace it**, *because the value of the number is "my copy is complete"
  and a number cannot answer that — it can only fail to. Against: a count is readable at a glance and
  needs no tooling, and the section is written for someone who has not installed anything yet.*
  **Rejected with it:** fixing the number to 25 and saying which count it is, which drifts again the
  next time the folder grows; and fixing it plus a test asserting the README's figure equals
  `git ls-files plugin/skills/taskmd/ | wc -l`, which is the only option where drift cannot recur
  silently but couples the suite to README wording for one sentence of prose.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Find whether a runnable completeness check exists at all, before promising one. Point `check --root` at a copy of the skill folder and see what it reads. | A yes or no, with the command and its output |
| 2 | **Make it fail on both kinds of incomplete copy** — a missing document and a missing code file — since a check that has only passed has not been tested. | Two captured failures |
| 3 | Rewrite the README section: drop the number, add the check, and place it after the launcher is introduced rather than before. | The edited section |
| 4 | Run the block **verbatim on a fresh copy**, as a reader would, rather than the shape it was developed with. | Its exit code and first line |
| 5 | Re-run the project's own gates. | `check`, `index`, the suite |

**Decisions taken here**

- **Step 4 is a separate step from step 1 on purpose** — 2026-08-23. Step 1's command is run in
  whatever state the experiment left the folder; step 4 is the text as published, on a copy that has
  never been touched. Those differ, and the difference is what a reader hits.

## 3. Implement

**Decisions & assumptions**

- **The check is `check --root <the copied folder>`** — 2026-08-23. Pointed at the skill folder, the
  validator treats it as the project root and reads the skill's own 17 documents and 119 links, which
  is exactly the claim the number was standing in for: *nothing cited that it does not carry*.
  *Rejected: `ls | wc -l`*, which is the count that returns 31 after the tool has run once and is the
  trap [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) named.

- **Step 4 caught the instruction failing, and this is the decision worth reading** — 2026-08-23.
  The first draft of the block was written from the shape the experiment used, where a `tasks` folder
  already existed. Run verbatim on a fresh copy it **exits 2**:

  ```text
  CONFIG ERROR  <shipped default>: tasks_dir is 'tasks', but the project root has no such folder.
  ```

  A documented route that does not run when followed as written is the third item on
  [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md)'s own
  finding threshold, so publishing it would have shipped the class of defect the audit that raised
  this record exists to catch. The block now carries the `mkdir`, and says the folder can be deleted.

- **The section moved after the launcher paragraph rather than before it** — 2026-08-23. The first
  draft opened with a `mkdir` and a launcher path, three paragraphs before the text that explains why
  a copied skill runs its launcher by path at all, and it repeated the `mkdir tasks` line already
  there. *Rejected: leaving it where the number was*, which read as a second, unexplained setup.

**Outputs produced**

- [`README.md`](../README.md) *As a plain skill* — the count removed from the self-contained
  sentence, and a two-shell block added after the launcher paragraph with what its output means and
  how each kind of short copy fails.

**Checked by using it.**

*A complete copy passes, and the count it reports is the thing to look at:*

```text
exit=0
OK - 0 task(s), ... 17 document(s), 119 link(s), ... 73 section reference(s)
```

*A copy missing a document fails, and names what points at the hole* — `docs/method/plan.md` deleted:

```text
exit=1
BROKEN LINK   docs/METHOD.md -> method/plan.md
BROKEN LINK   docs/method/audit.md -> plan.md
BROKEN LINK   docs/method/specify.md -> plan.md
4 problem(s) - ... 16 document(s), 111 link(s), ...
```

*A copy missing a code file fails earlier still* — `taskmd/schema.py` deleted:

```text
exit=1
Traceback (most recent call last):
  File "...\taskmd\__main__.py", line 11, in <module>
    from .cli import main
```

*And the published block was run verbatim on a copy that had never been touched:*

```text
exit=0
OK - 0 task(s), ... 17 document(s), 119 link(s), ...
```

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The section states something true of the published artifact, checked against a clone of the tag rather than against the working tree | met | The check was developed and run against a copy taken from the `v0.6.0` clone (`cb0702c`), not from this tree. It reports 17 documents and 119 links there |
| If a number stays, it says which count it is, and the decision records why a hand-kept number was kept | met, vacuously — **and the vacuity is recorded rather than ticked** | No number stayed, so the clause has nothing to bind on. It was written to catch the *keep-a-number* outcome the owner did not choose, and the two rejected options are in §1 beside the answer |
| If a number goes, the section still gives an adopter a way to tell their copy is complete | met | One command per shell, run verbatim on an untouched copy: `exit=0`, 17 documents. Its failure on both kinds of short copy is in §3, produced rather than predicted |
| Whatever is written cannot drift silently again, or the record says plainly that it can and that this is accepted | met | It cannot drift: the section names no derived quantity. The one figure it does mention — *a document count in the teens* — is a range, and a range that goes wrong means the skill folder has doubled, which is not silent |

**Adopter-visible?** yes. `README.md` is the first thing a prospective adopter reads, and the *As a
plain skill* section is an install instruction they follow. What changed is what they are told to do:
a claim they could only compare against became a command they run, and the command was wrong on its
first draft. Someone installing `0.6.0` today is told *21 files*; someone installing the next release
is told to run a check.

**Child fix tasks raised**
- none. Every criterion is met.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **Worked through `specify` to `review` and closed**, under the grant, 2026-08-23. The owner answered the one open question — **replace the number with a check the adopter runs** — and the two rejected options are in §1. **The instruction failed its own verbatim test before it shipped**: the first draft assumed a `tasks` folder the reader has not got, and exited 2. That is the third item on T-241's finding threshold, so publishing it would have shipped the class of defect the audit that raised this record exists to catch. `adopter_visible` is **yes** — this changes what an installer is told to do. |
| 2026-08-23 | → proposed | **Raised as finding 1 of [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md)**, the audit of the published `0.6.0`, 2026-08-23. Raised rather than fixed because [`audit`](../plugin/skills/taskmd/docs/method/audit.md)'s no-inline-fix rule applies and the repair is one word — which that document names as the case where the rule is most often waived. **`parent: T-241`**, so the umbrella stays open until this closes, per METHOD §4. **The owner's grant of 2026-08-23 reaches this record**, in its words *"including anything raised during the work of these tasks"* — it covers this record's `specify` through `review`, committing and pushing. |
