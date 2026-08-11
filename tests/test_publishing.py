"""The dash gate, run by the suite instead of remembered at publication (T-126).

`docs/PUBLISHING.md` §5 has always held this rule, and holding it was the problem: it is a manual
command in a document read only at publication, and publication is when there is most pressure not
to stop. Measured on the three existing tags, the README carried 0 offending lines at `v0.1.0`, 6 at
`v0.2.0` and 13 at `v0.3.0` — two releases went out with the gate red and nothing said so.

`test_budget.py` is the precedent: a rule nobody runs is a rule nobody keeps, so the suite runs it.

**The covered set and the two characters are not written here.** They are read out of the fenced
command in `docs/PUBLISHING.md` §5, which stays their one home; if they cannot be read, that is a
failure and not a skip, because a gate the suite can no longer parse has drifted.
"""

import os
import re
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLISHING = os.path.join(ROOT, "docs", "PUBLISHING.md")

# The pathspec, as arguments to `git ls-files`, and the characters `grep` is given. Both are
# captured from the one command rather than restated, so adding a covered document to §5 arms this
# test with nothing edited here.
PATHSPEC_RE = re.compile(r"--exclude-standard\s+((?:'[^']+'\s*)+)\)")
DASH_RE = re.compile(r"-e\s+'([^']+)'")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def gate_from_the_document():
    """The pathspec and the characters, lifted from `docs/PUBLISHING.md` §5.

    Deliberately strict. A shape this cannot parse means the documented gate and the enforced one
    have come apart, which is the state this module exists to make impossible.
    """
    text = read(PUBLISHING)
    section = text.split("## 5. The gate", 1)
    if len(section) != 2:
        raise AssertionError("docs/PUBLISHING.md has no '## 5. The gate' - the gate has moved, and "
                             "this test reads it from there rather than restating it")
    body = section[1].split("\n## ", 1)[0]
    paths = PATHSPEC_RE.search(body)
    dashes = DASH_RE.findall(body)
    if not paths:
        raise AssertionError("could not read the pathspec out of docs/PUBLISHING.md section 5; the "
                             "command's shape changed, so the documented gate and this test are no "
                             "longer the same rule")
    if not dashes:
        raise AssertionError("could not read the -e characters out of docs/PUBLISHING.md section 5")
    return [p.strip("'") for p in paths.group(1).split()], dashes


def covered_files(pathspec):
    listed = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"] + pathspec,
        cwd=ROOT).decode("utf-8")
    return [line for line in listed.splitlines() if line]


def git_is_available():
    try:
        done = subprocess.Popen(["git", "--version"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        done.communicate()
    except OSError:
        return False
    return done.returncode == 0


GIT = git_is_available()


@unittest.skipUnless(GIT, "no git: the covered set is a git pathspec, so there is nothing to resolve")
class ThePassingDashGateProvesOnlyThatOnePatternIsAbsent(unittest.TestCase):
    """Named for what a pass does **not** mean, because that is the half most likely to be forgotten.

    Pattern 14 is the only part of `docs/PUBLISHING.md` §2 a script can judge. Failing here proves
    the humanizer rewrite did not happen; passing proves only that one pattern is absent. The rewrite
    is a judgement and needs the skill and an agent.
    """

    def test_the_pathspec_resolves_to_files(self):
        """The gate's exit 2, kept. A run that covers nothing prints nothing, which is also what
        success looks like - this project has hit that three times (T-034, T-080, and §5's own
        exit 2)."""
        pathspec, _ = gate_from_the_document()
        self.assertTrue(pathspec, "section 5's pathspec is empty")
        self.assertTrue(covered_files(pathspec),
                        "the pathspec in docs/PUBLISHING.md section 5 covers 0 files - the gate is "
                        "broken, not the tree")

    def test_no_covered_document_carries_an_em_or_en_dash(self):
        pathspec, dashes = gate_from_the_document()
        offenders = []
        for where in covered_files(pathspec):
            for number, line in enumerate(read(os.path.join(ROOT, where)).splitlines(), 1):
                if any(dash in line for dash in dashes):
                    offenders.append("%s:%d" % (where, number))
        self.assertEqual([], offenders,
                         "%d covered line(s) carry a dash the humanizer removes; run the rewrite in "
                         "docs/PUBLISHING.md section 2, not a find-and-replace:\n%s"
                         % (len(offenders), "\n".join(offenders)))

    def test_the_scan_reports_a_dash_when_one_is_present(self):
        """A clean tree proves nothing on its own. The same characters, the same containment test,
        over text that must be caught - so the assertion above is known to be capable of failing."""
        _, dashes = gate_from_the_document()
        self.assertIn("—", dashes, "the em dash is no longer one of the characters section 5 "
                                        "greps for")
        self.assertIn("–", dashes, "the en dash is no longer one of the characters section 5 "
                                        "greps for")
        drifted = ["A line that reads fine — until you look at the dash.",
                   "And an en dash – the same problem."]
        caught = [line for line in drifted if any(dash in line for dash in dashes)]
        self.assertEqual(drifted, caught)


if __name__ == "__main__":
    unittest.main()
