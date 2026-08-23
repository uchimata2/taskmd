---
id: T-161
title: Give the entry-point comments' pointer a reader
type: fix
status: done
phase: review
parent: T-142
blocked_by: []
related: [T-064, T-099, T-139, T-160]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-16
updated: 2026-08-16
adopter_visible: yes
deliverables: []
---

# T-161 — Give the entry-point comments' pointer a reader

## 1. Specify

**Outcome**
The two entry-point shims' pointer to `SKILL.md` cannot be deleted, moved or left dangling without
something failing.

**Why this one**
Raised from [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md)'s `implement`,
which found the gap while establishing what its own green suite proved. `tests/test_runtime.py` reads
both shims twice and neither reading can see this:

- `test_every_entry_point_produces_what_the_module_produces` **executes** them, so it covers
  behaviour and nothing about the prose;
- `test_no_entry_point_names_a_command_a_flag_or_a_field` strips every comment line first, by an
  explicit decision stated in its own docstring — *a launcher's body is what carries logic; its prose
  is allowed to say anything, and does.*

So T-142 replaced a comment that had been false for weeks with a comment that could go false again
the same way, and the suite would stay green through both.

**This is T-160's shape, one file over.** That task found a printed line whose provenance clause no
test had ever read, and its answer was not to trust the new wording but to add the reader — proved by
failing against the old text. The same argument applies here and the same remedy is available.

**What the pointer is worth guarding.** It is the only thing in either shim that reaches the fallback
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) shipped. If `SKILL.md`
moves inside the skill folder, or the paragraph it names is renamed away, the shims keep saying
*it is stated once, in ../skills/taskmd/SKILL.md* and the stranded adopter follows it to nothing —
which is the failure mode T-142 was raised to remove, restored by a different route.

**Scope**
- In: `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd`, and whether the path each names resolves.
- In: whether the target still contains the fallback, or only that a file is there. A path that
  resolves to a `SKILL.md` with no fallback paragraph in it is the more likely failure.
- In: whether this is written as its own test or falls out of whatever
  [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) settles —
  that task is generalising the guard for marked lists, and a bespoke fifth guard written beside it
  is the duplication it exists to stop. **Read T-139's outcome before writing anything here.**
- Out: the wording of either comment, which T-142 settled and verified.
- Out: the fallback itself, which is T-099's and unchanged.
- Out: guarding prose in general. The claim worth a reader is the **pointer**; the rest of the
  comment is argument, and `test_no_entry_point_names_a_command_a_flag_or_a_field`'s ruling that
  prose may say anything is not reopened here.

**Inputs**
- `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd` — the two pointers.
- `tests/test_runtime.py` — `entry_points`, and the two tests named above.
- [T-160](T-160-retire-the-budget-check-s-unobserved-premise-warning.md) — a citation given a reader,
  and the way it was proved.
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) — the
  general guard, whose answer may supply this one.

**Acceptance criteria**

*Written 2026-08-16, T-139 having closed on 2026-08-15 and its outcome read.*

- [ ] Deleting the pointer from either shim fails the suite — shown by making it fail
- [ ] Pointing it at a path that does not resolve fails the suite
- [ ] A target that resolves but no longer carries the fallback fails the suite — the case §1 names as
      the likelier one, and the one an existence check alone would pass
- [ ] The reader writes **no path and no launcher name of its own**: the pointer comes out of the
      shim, the target out of the filesystem, and what the target must still say out of the shim's own
      delegation

**Open questions**
- **Is this its own test, or an instance of T-139's mechanism?** Decide at `specify`, and not before
  T-139 closes. Recorded as a soft link rather than a dependency edge: this task can be specified
  either way and nothing here is blocked, but someone working it without knowing T-139's answer would
  make the worse choice — which is exactly what `related` is for (METHOD §4).

  **Answered 2026-08-16: its own test.** T-139 generalised T-134 to *any marked list of a set the code
  owns* — a region of prose whose members are compared with a set computed from the code. Two things
  here are not that. The claim is a **reference**, not a membership: one path, and the question is
  whether it resolves and whether what it resolves to still says the thing. And the carriers are a
  `.sh` and a `.cmd`, where an HTML marker pair has no meaning and would be the only two in the tree
  outside Markdown. Declaring a one-member set to reach the mechanism would be reuse in name only,
  and the failure it catches — *the target moved* — is one the mechanism cannot express.

  The soft link still earned its place: reading T-139 first is what makes the answer *no* defensible
  rather than unconsidered, and it supplied the shape used anyway — derive the subject from the tree,
  name nothing in the test, and prove it by making it fail.

## 2. Plan

One test in `Launchers`, beside the two that already read the shims and cannot see this.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Split the shims out of `entry_points()` — the files under `bin/`, which delegate, against the launchers, which do not. Both halves are needed and neither is written down | a `shims()` helper in `tests/test_runtime.py` |
| 2 | Read the pointer out of each shim's **prose**, with a pattern for what a document reference looks like on either platform, and assert there is exactly one | the pointer, derived |
| 3 | Resolve it against the shim's own directory and assert the target is a file | criterion 2 armed |
| 4 | Read each shim's **body** for the launcher it delegates to — matched against `entry_points()`, so the name comes from the tree — and assert the target names it | criterion 3 armed; this is what makes it a fallback rather than a file |
| 5 | Make it fail three ways: pointer deleted, pointer dangling, fallback gone from the target | three recorded failures in §3 |
| 6 | Run the suite, `check` and `index` | green output quoted in §3 |

## 3. Implement

**Decisions & assumptions**
- **Its own test, not T-139's mechanism** — 2026-08-16. The argument is in §1's answered question,
  where it belongs, because it is the ruling this task was raised to take.
- **What the target must still say is read out of the shim's own body** — 2026-08-16. The shim
  `exec`s a launcher; the fallback in `SKILL.md` tells a stranded adopter to run that same launcher.
  So the sentence under guard is identified by a name the tree already holds, matched against
  `entry_points()`, and the test writes neither the launcher's name nor a word of the paragraph.
  Naming the paragraph — by heading, by a phrase, by a marker — would have been a second copy of the
  thing whose single copy is the point.
- **Existence alone was rejected as the whole check** — 2026-08-16. It is the version that passes on
  the likelier failure: `SKILL.md` is a file that will still be there long after any particular
  paragraph in it is not. §1 named that case and it is criterion 3.
- **`assertTrue(x in text)` rather than `assertIn`** — 2026-08-16. `assertIn` prints the container,
  and the container is a whole document; the first run of the third failure buried its own message
  under `SKILL.md`. Written after seeing it, not predicted.
- **Both shims are covered by one loop, derived** — 2026-08-16. `shims()` is *the entry points under
  `bin/`*, so a third one arrives in this test without anyone remembering it exists — the reason
  `entry_points()` was derived in the first place (T-068).

**Evidence — made to fail three ways, on the real tree**

Pointer deleted, the prose naming the fallback in words instead:

```
AssertionError: 1 != 0 : bin/taskmd should name exactly one document - the way in that does not
depend on PATH - and names none
```

Pointer left in place but pointing one directory short:

```
AssertionError: False is not true : bin/taskmd sends a reader who could not run the command to
skills\SKILL.md, which is not there
```

Target resolving, fallback removed from it — the case an existence check passes:

```
AssertionError: False is not true : bin/taskmd points at skills\taskmd\SKILL.md for the way in that
does not depend on PATH, and that document no longer tells anyone to run taskmd.sh
```

Everything restored — `git diff --stat -- plugin/` is empty — then the suite, `check` and `index`:

```
265 passed, 3 skipped, 6 subtests passed in 27.28s
```

**Outputs produced**
- `tests/test_runtime.py` — `Launchers.POINTER`, `shims()`, `prose_and_body()`, and
  `test_each_shims_pointer_reaches_the_fallback_it_promises`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Deleting the pointer from either shim fails the suite | met | §3, first failure. Rewriting it as prose is the realistic form of deletion and is what was run |
| Pointing it at a path that does not resolve fails the suite | met | §3, second failure |
| A target that resolves but no longer carries the fallback fails the suite | met | §3, third failure. `SKILL.md` was left in place and only the two launcher invocations removed |
| The reader writes no path and no launcher name of its own | met | The pointer comes from the shim's prose, the target from `os.path.isfile`, the launcher name from `entry_points()`. The only literals are `POINTER`'s shape and `bin/`, which `entry_points()` already had |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | Full lifecycle in one session under the authorisation below. `specify` answered the parked question — its own test, because the claim is a reference rather than a set membership, and the carriers are a `.sh` and a `.cmd` where T-139's markers mean nothing. `implement` derived every name in it from the tree and proved all three failures, including the one an existence check would pass. `review` judged four criteria met, no child task. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, unattended**, given 2026-08-16 as the subject of a handoff — *a vast amount of task alone, unattended*, the maintainer having selected the batch from a list put to them and answered two questions about it. It covers [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md), [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) and [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) and **nothing else** — not the six `decision` tasks beside them, not the three parked on the `InstructionsLoaded` hook, and **not anything these four raise**, which are filed and left. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. |
| 2026-08-16 | → proposed | Raised from [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md)'s `implement`, which established what its own green suite covered and found the answer was *not this*. Filed rather than fixed there: the standing authorisation of 2026-08-16 covers four named tasks and explicitly not what they raise, and the guard is the class [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) is generalising — so a bespoke test written the day before that ruling is the duplication T-139 exists to stop. `medium` because the pointer is the stranded adopter's only route to the fallback; `xs` because it is one assertion once the mechanism is chosen. |
