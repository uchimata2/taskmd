"""The audit's cycle partition, asserted on every change (T-255).

`tools/audit_cycles.py` holds the membership rules and prints the columns a session pastes into
T-244 §2. This module imports the same rules and asserts the partition, so a file added under
`plugin/` fails here without anyone remembering to ask.

**Two consumers, one home for the rules.** The script exists because a table has to be pasted and a
test emits only a pass or a failure; the test exists because nothing would run the script - and a
check nobody performs is the defect being fixed, not the fix. Neither restates the other's rules.
"""

import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import audit_cycles  # noqa: E402


def git_is_available():
    try:
        done = subprocess.Popen(["git", "--version"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        done.communicate()
    except OSError:
        return False
    return done.returncode == 0


GIT = git_is_available()


@unittest.skipUnless(GIT, "the subject is derived with `git ls-files`")
class EveryTrackedPathInTheSubjectBelongsToOneCycle(unittest.TestCase):
    """The property htmldeck's `PR-06` did not have: a partition that fails on an unassigned item.

    Its plan stated counts rather than deriving them, its two coverage tables could not reconcile,
    four files went unread, and the run looked complete. That is what this assertion is for.
    """

    def test_the_partition_is_complete(self):
        ok, lines, _, _ = audit_cycles.verdict(ROOT)
        self.assertTrue(ok, "\n".join(lines))

    def test_an_unassigned_path_is_reported_by_name(self):
        """The rule must be shown able to fire, on a case it exists to catch.

        A partition check that has only ever passed is worth exactly the confidence that it *would*
        catch something, and this task exists because that confidence was misplaced once already.
        The specimen is injected into the derived list rather than written to disk, so the check
        under test is the assignment and not the filesystem.
        """
        specimen = "plugin/skills/taskmd/docs/method/a-new-document.md"
        before = audit_cycles.subject(ROOT)
        _, unassigned, doubled = audit_cycles.assign(before + [specimen])
        # Membership, not equality: asserting the specimen is the *only* unassigned path would make
        # this test fail for someone else's reason the moment the tree genuinely has one, and it
        # would report the specimen as the problem. Measured on 2026-08-23, when it did exactly that.
        self.assertIn(
            specimen, unassigned,
            "a path under plugin/ that no cycle claims must be reported by name; got %r"
            % (unassigned,))
        self.assertNotIn(specimen, [path for path, _ in doubled],
                         "the specimen must not also be claimed twice")
        self.assertNotIn(specimen, audit_cycles.assign(before)[1],
                         "the specimen must not already be in the subject, or this proves nothing")

    def test_no_path_is_claimed_by_two_cycles(self):
        """A doubled member is invisible in a total - the sum still reconciles and one reading is wrong."""
        _, _, _, paths = audit_cycles.verdict(ROOT)
        _, _, doubled = audit_cycles.assign(paths)
        self.assertEqual(doubled, [], "a path claimed by two cycles: %r" % (doubled,))

    def test_the_counts_sum_to_the_subject(self):
        """Both directions. A count that merely matches a total has not been checked per item."""
        _, _, assignment, paths = audit_cycles.verdict(ROOT)
        per_cycle = sum(
            len([p for p, c in assignment.items() if c == number])
            for number, _, _, _ in audit_cycles.CYCLES)
        self.assertEqual(
            per_cycle, len(paths),
            "the cycles sum to %d and the subject holds %d tracked path(s)" % (per_cycle, len(paths)))
        self.assertEqual(sorted(assignment), sorted(paths),
                         "the assigned set and the subject are not the same set")


if __name__ == "__main__":
    unittest.main(verbosity=2)
