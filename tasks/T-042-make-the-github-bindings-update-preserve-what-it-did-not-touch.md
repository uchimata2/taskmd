---
id: T-042
title: Make the GitHub binding's update preserve what it did not touch
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-010, T-041]
work_package: v0.1
owner: maintainer
business_value: critical
effort: m
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-042 — Make the GitHub binding's update preserve what it did not touch

## 1. Specify

**Outcome**
`docs/bindings/github-issues.md`'s `update` operation satisfies BINDING §1's byte-identical
guarantee when followed, and its warning names the failure that actually happens rather than the one
that was imagined — both demonstrated on a live repository, not argued.

**Why this one**
T-041 executed the operation and found two defects, one in each direction:

1. **Following the binding correctly corrupts the body.** `gh issue view --json body --jq .body`
   appends jq's trailing newline; feeding that back through `--body-file` stores a body one byte
   longer. Measured across three no-op round trips: 230 → 231 → 232 bytes. Monotonic, unbounded,
   invisible in rendered Markdown, and caused by the procedure the binding prescribes.
2. **The warning understates what a careless rewrite destroys.** It names "fields the schema does
   not name". T-041's run also silently destroyed a **soft edge** — and `related` has no native
   carrier on this backend, so the body is its only home. No far end holds a copy, no derived view
   can notice, and the resulting issue is perfectly well-formed with one fewer edge. `gh` returned
   exit 0 for the destructive edit and exit 0 for the correct one.

This is `business_value: critical` because it is the one operation in the binding that can lose data
that exists nowhere else, and because defect 1 means the binding does not currently conform to the
contract it claims to implement.

**Scope**
- In: the `update` operation's procedure and its warning; whatever else in the binding has to change
  so `read` and `update` compose without drift.
- Out: the carrier decisions. D2 put `related` in the body and D3 made `state` a rendering; both
  stand. If defect 2 is judged to be an argument against D2 rather than against the wording, that is
  a separate task with T-010's criteria in view — not a reversal made while fixing a sentence.

**Inputs**
- T-041 §3 — the transcripts, the byte counts and the verdict on the wording
- `docs/BINDING.md` §1, `update`, for the guarantee being missed
- The fixture repository, which stands until first publication (T-037)

**Acceptance criteria**
- [ ] A no-op update — fetch the body, write it back unchanged — leaves the stored body **byte-identical**,
      shown by repeating it at least three times and measuring, since one clean cycle is what the
      broken procedure also looks like
- [ ] A real update changes only the intended field, with the rest byte-identical, measured the same way
- [ ] The warning names all three of what T-041 found: the soft edges in the body, the fields the
      schema does not name, and that `gh` exits 0 either way
- [ ] The destructive case is **run again after the fix** and still destroys what it destroyed
      before — the fix must make the correct path safe without making the careless path look safe
- [ ] Nothing in the fix requires a tool the binding does not already assume; if it needs one, that
      is stated as an assumption per BINDING §4

**Open questions**
- None blocking `specify`. The likely shape is to prescribe a fetch that does not add the newline
  and to say so explicitly rather than leaving it to whoever pipes the command — but which
  invocation to standardise on is `plan`'s to choose, and criterion 1's repeat-and-measure is what
  decides between candidates rather than preference.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Find a fetch that round-trips byte-identically using `gh` alone. The broken one is `--json body --jq .body`; the obvious candidate is a Go `--template`, which has no reason to append anything. Test each by writing back exactly what it read and measuring. | A named invocation, and the measurement that chose it over the others |
| 2 | Prove the no-op is stable across repeated cycles, not one. **One clean cycle is what the broken procedure also looks like** — it took three to see the drift. | Byte counts across at least three no-op cycles |
| 3 | Prove a real single-field update leaves everything else byte-identical, compared as bytes. | A byte comparison of the untouched region |
| 4 | Rewrite `update` in the binding: the fetch command, and a warning naming all three hazards T-041 found. | `docs/bindings/github-issues.md` |
| 5 | Run the destructive rewrite again and confirm it still destroys what it destroyed before. | The transcript, and the grep counts |
| 6 | Confirm the fix introduces no tool the binding did not already assume; if it does, write it into the assumptions per BINDING §4. | A verdict, and an assumption entry if one is owed |

**Sequencing.** Step 1 is first because it can fail, and its failure changes the shape of everything
after it: if no `gh`-only invocation round-trips, the fix needs a post-processing step, which
criterion 5 then forces into the assumptions section as a new prerequisite for adopters. Cheaper to
discover that before writing any prose. Step 5 comes after step 4 rather than beside step 3, because
what it tests is the claim the *new* wording makes — running it against the old text would prove
nothing about the fix.

**Shape of the deliverable — decided.** The fix is a corrected command plus a warning in the
existing `update` section, not a new "pitfalls" section. A separate section would be read after the
operation it warns about, and the whole failure mode here is someone acting on the command in front
of them. Rejected: adding a worked "safe update" script to the binding — A3 and non-goal 8 keep this
a document, and a script would also be the tool criterion 5 exists to prevent.

**Output paths**
- `docs/bindings/github-issues.md` — the `update` operation
- This task's §3 — the invocation comparison, the cycle measurements, and the re-run transcript

## 3. Implement

Run against the fixture repository on 2026-08-07, `gh` 2.96.0, on a fresh issue whose property block
carried `review_ticket: SYNTHETIC-0001` (a fabricated value referring to nothing), the soft edge
`Related: #1`, and a line of prose below the block.

**Step 1 — three candidate fetches, one of them byte-exact.** The stored body is 204 bytes:

| Fetch | Bytes returned | Tail |
| :--- | ---: | :--- |
| `--json body --jq .body` | 205 | `". \n \n` |
| `--json body -q .body` | 205 | `". \n \n` |
| `--json body --template '{{.body}}'` | **204** | `g ". \n` |

`-q` is the same jq path under a shorter flag, so it fails identically — worth recording, because
`-q` is the form someone reaches for when shortening a command and it looks unrelated to the bug.
The Go template returns the value verbatim.

**Step 2 — stable across five no-op cycles, not one.** Fetching with `--template` and writing back
unchanged: **204, 204, 204, 204, 204**, and `cmp` against the original fetch reports the file
identical after all five. Compare T-041's 230 → 231 → 232 over three cycles with the jq form. Five
rather than the three the criterion asked for, because the defect being fixed was one that a single
clean cycle would have hidden.

**Step 3 — a real update touches only its field.** Changing `effort: s` to `effort: l`, then
byte-comparing everything except that line: `cmp` reports **identical, 194 bytes**. Total length
unchanged at 204 both sides, and the soft edge and unnamed field both still present.

**Step 5 — the careless rewrite still destroys, after the fix.** Sending a body with only the
intended fields returned **exit 0**, and greps of the stored body afterwards: `Related:` 0,
`review_ticket` 0, prose 0. All three gone, silently, exactly as before. The fix makes the correct
path safe; it does not and must not make the careless path look safe, which is what criterion 4 was
written to catch.

**Step 6 — no new tool, so no assumption is owed.** `--template` is a flag on the `gh` binary the
binding already requires; nothing was added to the adopter's prerequisites. The verdict is narrower
than it looks, though — see the finding below.

**Decisions & assumptions**
- **`--template '{{.body}}'` is prescribed by name, and both jq forms are named as wrong.** — Step 1.
  Saying "fetch the body" and leaving the invocation to the reader is what produced the defect; the
  binding now names the one that works and the two that do not, because `-q` looks like a
  shorthand rather than a second instance of the same bug. — 2026-08-07
- **The warning is rewritten as a list of what is destroyed, not as an instruction to be careful.**
  — T-041 found the old wording warned someone who already knew. Naming the three casualties — soft
  edges, unnamed fields, prose — and the exit-0 silence gives a reader something to check against,
  which "put back everything you are not changing" did not. — 2026-08-07
- **No `gh` version floor is stated, because none was measured.** — `--template`, `--parent` and
  `--add-blocked-by` were all exercised on one version only. Inventing a floor would be the
  unmeasured claim this project exists to remove, and the gap is real → **T-044**. — 2026-08-07

**Findings raised, not fixed here**
- **T-044** — the binding names no `gh` version it requires, and several operations depend on
  recently-added flags. Out of scope here, which is the `update` operation.

**Outputs produced**
- [`docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) — the `update` operation:
  the byte-exact fetch, the two named-wrong forms, and the destruction warning

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A no-op update leaves the body byte-identical, repeated at least three times and measured | met | Five cycles at 204 bytes, `cmp` identical to the original fetch. Exceeded the three asked for deliberately: the defect being fixed is invisible on cycle one, so the criterion's own minimum is close to the number that would have missed it. |
| A real update changes only the intended field, the rest byte-identical, measured the same way | met | `effort: s` → `effort: l`; `cmp` on everything but that line reports identical at 194 bytes, and the soft edge and unnamed field both survived. |
| The warning names all three: soft edges, unnamed fields, and that `gh` exits 0 either way | met | All three, as a list of what a partial rewrite destroys rather than as advice to take care — with the soft-edge entry saying *why* it is the worst of them, that `related` has no other home on this backend. |
| The destructive case is run again after the fix and still destroys what it destroyed before | met | Exit 0; `Related:` 0, `review_ticket` 0, prose 0. The correct path is now safe and the careless path is exactly as dangerous as it was, which is the pairing the criterion demanded. |
| Nothing in the fix requires a tool the binding does not already assume | met | `--template` is a flag on the `gh` binary already required; no prerequisite added. Met as written — and the step exposed that the binding names no `gh` *version* at all, which is a different gap and is → **T-044**. |

Five met, none carried. The task closes the conformance hole it was raised for: `update` now
satisfies BINDING §1's byte-identical guarantee when followed, demonstrated rather than argued.

**Child fix tasks raised**
- **T-044** — no `gh` version floor is stated anywhere in the binding, and several operations rest
  on recently-added flags.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | All five criteria met. The fetch was the whole fix: `--template '{{.body}}'` returns the body verbatim where both jq forms append a newline, and five no-op cycles held at 204 bytes against T-041's 230 → 231 → 232. `-q` is recorded as failing identically to `--jq`, because it reads like a harmless shorthand. The warning was rewritten as a list of what a partial rewrite destroys — soft edges first, since `related` has no other home here — plus the exit-0 silence, and the destructive case was re-run afterwards to confirm the fix did not make it look safe. It did not: exit 0, all three casualties gone. One finding raised: the binding names no `gh` version floor and several operations depend on recent flags → T-044. |
| 2026-08-07 | → planned | Six steps. `specify` was still at `proposed`: its criteria were written when T-041 raised this task and never separately agreed, and the instruction to plan is taken as that agreement, since the criteria were in the commit the owner accepted. Recorded here rather than left implicit — the exit criterion says agreed by the owner, and a task that skipped it silently would be the undocumented-progress failure. Step 1 leads because its failure changes the shape of the rest: no `gh`-only fetch means a post-processing step, which criterion 5 turns into a new adopter prerequisite. |
| 2026-08-07 | → proposed | Raised by T-041, which was itself raised by T-010's review to test the one operation T-010 never executed — and found the operation broken in the ordinary case, not just the careless one. Kept out of T-041 because that task's scope explicitly put wording changes out, so that the record would name the exact text that failed; fixing it there would have left the correction with no evidence of what it corrected. |
