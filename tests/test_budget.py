#!/usr/bin/env python
"""Proof for T-115: the tier 1 budget is enforced by running, not by remembering.

`CLAUDE.md` *Working method* states a budget — tier 1, whatever the harness loads unasked,
stays smaller than `reference/TASK-WORKFLOW.md`, the flat alternative it replaced. Until
this file existed the only thing that could report a breach was a shell one-liner somebody
had to think to run, which is silence with a command attached.

Six things are proven by running, not by reading:

1. Membership is **derived from the tree**. Adding a skill moves the figure with nothing
   edited here — T-063's rule, re-proved rather than trusted.
2. The unit is **characters**, not bytes. On the real repository the two disagree about the
   verdict, which is how the defect was found; a synthetic tree pins it so it cannot come
   back quietly.
3. A tier 1 pushed over the bound is **reported failing**.
4. A tier 1 under the bound passes, so the check is not merely stuck red.
5. A **block-level comment is not counted** - the harness strips it before injecting, so a
   justification for the maintainer costs the file and not the session. One inside a code
   fence is content and survives, which is the half that is easy to get wrong (T-153).
6. The report names what the figure **does not** govern, so a pass is never read as a clean
   load path (T-154).

This lives in `tests/` and not in `check` on purpose: `plugin/` is what an install copies,
and no adopter should receive a rule comparing two files only this repository has.

  python tests/test_budget.py
"""

import glob
import io
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIER1_FILE = "CLAUDE.md"                        # loaded unasked, every turn
SKILL_GLOB = os.path.join("plugin", "skills", "*", "SKILL.md")
BOUND_FILE = os.path.join("reference", "TASK-WORKFLOW.md")
DESCRIPTION = "description: "                   # a served skill's description joins tier 1
FENCE = "```"                                   # a comment inside one is content, not a comment

# T-154. The figure below is a share of the load path, not the load path. Both lines are printed on
# every run because the misreading they prevent happens where the *result* is read, and putting them
# in `CLAUDE.md` instead would charge every session for a caveat about a check it never runs.
SCOPE = (
    "scope  this repository's own tier 1 - the files named above. The harness, the user's own files\n"
    "       and the skill catalogue are loaded unasked as well, are counted by nothing here, and\n"
    "       were the larger part when last measured. A pass is not a clean load path (E-01)"
)
UNMEASURED = (
    "also   instruction count is a second constraint on the same file, and it is the one reported to\n"
    "       bind - for adherence, not for tokens. Nothing here measures it, and nothing claims to (E-04)"
)


def _chars(path):
    """The file's content as text, so len() is characters and not bytes."""
    with io.open(path, encoding="utf-8") as handle:
        return handle.read()


def strip_block_comments(text):
    """Drop block-level HTML comments: the harness removes them before injecting the file.

    *Block-level* means the comment opens a line of its own. One inside a fenced code block
    is content and is kept, which is the case this must not get wrong - see T-153.

    The budget counts what a session is handed, so it counts the result of this and not the
    file. That makes the check depend on a documented behaviour no session here has yet
    observed; `report` says so on every run rather than letting the dependency go quiet.
    """
    kept, in_fence, in_comment = [], False, False
    for line in text.splitlines(True):
        stripped = line.strip()
        if in_comment:
            in_comment = "-->" not in line
            continue
        if stripped.startswith(FENCE):
            in_fence = not in_fence
        if not in_fence and stripped.startswith("<!--"):
            in_comment = "-->" not in stripped[len("<!--"):]
            continue
        kept.append(line)
    return "".join(kept)


def measure(root):
    """Return (tier 1 characters, bound characters, the paths counted into tier 1).

    Tier 1 is `CLAUDE.md` plus the `description` of every skill the tree serves. The
    description's own characters are counted; the newline the shell pipeline used to put
    after each one was an artefact of the pipeline, not part of the description.
    """
    members = [TIER1_FILE]
    text = strip_block_comments(_chars(os.path.join(root, TIER1_FILE)))
    for skill in sorted(glob.glob(os.path.join(root, SKILL_GLOB))):
        for line in _chars(skill).splitlines():
            if line.startswith(DESCRIPTION):
                text += line[len(DESCRIPTION):]
                members.append(os.path.relpath(skill, root).replace(os.sep, "/"))
    return len(text), len(_chars(os.path.join(root, BOUND_FILE))), members


def report(root):
    """The figures, the margin, what was counted - and what the figure does not govern."""
    tier1, bound, members = measure(root)
    verdict = "over by %d" % (tier1 - bound) if tier1 > bound else "under by %d" % (bound - tier1)
    raw = _chars(os.path.join(root, TIER1_FILE))
    commented = len(raw) - len(strip_block_comments(raw))
    lines = ["tier 1 %d chars %s (bound %d, %s) from: %s" % (
        tier1, verdict, bound, BOUND_FILE.replace(os.sep, "/"), ", ".join(members)
    )]
    if commented:
        lines.append(
            "       %d chars of block comment are not counted: the harness is documented to strip"
            " them before injecting and this check follows it - not yet observed here (T-153)"
            % commented
        )
    lines.extend([SCOPE, UNMEASURED])
    return "\n".join(lines)


def _tree(root, tier1_text, bound_text, descriptions=()):
    """Write a minimal tree measure() can read: a tier 1 file, a bound, and n skills."""
    with io.open(os.path.join(root, TIER1_FILE), "w", encoding="utf-8") as handle:
        handle.write(tier1_text)
    os.makedirs(os.path.join(root, "reference"))
    with io.open(os.path.join(root, BOUND_FILE), "w", encoding="utf-8") as handle:
        handle.write(bound_text)
    for index, description in enumerate(descriptions):
        skill = os.path.join(root, "plugin", "skills", "skill%d" % index)
        os.makedirs(skill)
        with io.open(os.path.join(skill, "SKILL.md"), "w", encoding="utf-8") as handle:
            handle.write("---\nname: skill%d\n%s%s\n---\n" % (index, DESCRIPTION, description))
    return root


class TestTheBudgetItself(unittest.TestCase):
    """The assertion this file exists for: the real tree, against its real bound."""

    def test_tier_1_stays_under_the_bound(self):
        tier1, bound, _ = measure(ROOT)
        print("\n" + report(ROOT))
        self.assertLessEqual(
            tier1, bound,
            "\n" + report(ROOT) + "\n"
            "Tier 1 is what a session is handed unasked, and it is now larger than the flat\n"
            "document splitting it was supposed to beat. What leaves is not this check's\n"
            "call - see CLAUDE.md 'Working method' and the task that raised the breach."
        )


class TestTheCheckCatchesWhatItClaims(unittest.TestCase):
    """A check that has only ever passed has not been tested."""

    def setUp(self):
        import shutil
        import tempfile
        self.root = tempfile.mkdtemp(prefix="taskmd-budget-")
        self.addCleanup(shutil.rmtree, self.root, True)

    def test_a_tier_1_over_the_bound_is_reported(self):
        _tree(self.root, "x" * 120, "y" * 100)
        tier1, bound, _ = measure(self.root)
        self.assertEqual((tier1, bound), (120, 100))
        self.assertGreater(tier1, bound)
        self.assertIn("over by 20", report(self.root))

    def test_a_tier_1_under_the_bound_passes(self):
        _tree(self.root, "x" * 80, "y" * 100)
        tier1, bound, _ = measure(self.root)
        self.assertLess(tier1, bound)
        self.assertIn("under by 20", report(self.root))

    def test_membership_is_derived_from_the_tree(self):
        _tree(self.root, "x" * 80, "y" * 100)
        bare, _, members = measure(self.root)
        self.assertEqual(members, [TIER1_FILE])

        skill = os.path.join(self.root, "plugin", "skills", "late")
        os.makedirs(skill)
        with io.open(os.path.join(skill, "SKILL.md"), "w", encoding="utf-8") as handle:
            handle.write("---\nname: late\n%s%s\n---\n" % (DESCRIPTION, "z" * 30))

        grown, _, members = measure(self.root)
        self.assertEqual(grown - bare, 30, "a served skill's description joins tier 1")
        self.assertEqual(members, [TIER1_FILE, "plugin/skills/late/SKILL.md"])

    def test_a_block_comment_leaves_the_counted_figure(self):
        """T-153: a justification for the maintainer costs the file, not the session."""
        _tree(self.root, "x" * 80 + "\n", "y" * 100)
        bare, _, _ = measure(self.root)

        with io.open(os.path.join(self.root, TIER1_FILE), "a", encoding="utf-8") as handle:
            handle.write("<!--\n" + ("z" * 200) + "\n-->\n")

        commented, _, _ = measure(self.root)
        self.assertEqual(commented, bare, "the comment is not counted")
        self.assertGreater(
            os.path.getsize(os.path.join(self.root, TIER1_FILE)), bare, "it is still in the file"
        )
        self.assertIn("chars of block comment are not counted", report(self.root))

    def test_a_comment_inside_a_code_fence_is_kept(self):
        """The case the strip must not catch. Stripping it would silently lose an example."""
        fenced = "start\n\n```\n<!-- shown on purpose -->\n```\n"
        _tree(self.root, fenced, "y" * 500)
        kept, _, _ = measure(self.root)
        self.assertEqual(kept, len(fenced), "nothing inside the fence was stripped")
        self.assertNotIn("chars of block comment", report(self.root))

    def test_the_unit_is_characters_and_the_two_units_disagree(self):
        """The defect this file was written for, reduced to a tree that cannot drift.

        The bound is denser in multi-byte punctuation than tier 1, so counting bytes
        flatters tier 1 - which is exactly how the real repository read as passing by 8
        while being over by 9.
        """
        _tree(self.root, "x" * 105, ("y" * 70) + ("—" * 30))
        tier1, bound, _ = measure(self.root)
        self.assertEqual((tier1, bound), (105, 100), "characters")
        self.assertGreater(tier1, bound, "in characters, tier 1 is over")

        as_bytes = [
            os.path.getsize(os.path.join(self.root, TIER1_FILE)),
            os.path.getsize(os.path.join(self.root, BOUND_FILE)),
        ]
        self.assertEqual(as_bytes, [105, 160], "bytes")
        self.assertLess(as_bytes[0], as_bytes[1], "in bytes the same tree reads as passing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
