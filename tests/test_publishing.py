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

import collections
import os
import re
import shutil
import subprocess
import sys
import tempfile
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


def _cli():
    import sys
    sys.path.insert(0, os.path.join(ROOT, "plugin", "skills", "taskmd"))
    from taskmd import cli
    return cli


#: One marked kind of list. `name` is the marker token, so the region is
#: `<!-- taskmd:<name> -->` … `<!-- taskmd:end-<name> -->`; `pattern` reads the members out of the
#: region's prose; `owned` returns the set the code owns; `required` names the documents that must
#: carry a region of this kind.
Kind = collections.namedtuple("Kind", "name pattern owned required")

# T-139 generalised this from commands to any marked list of a set the code owns. Adding a kind is
# one row here and a pair of markers in the document - no test below is edited, and none names a
# member of any set.
#
# The patterns differ because the registers do. A command is written as an invocation in both places
# that list them (`taskmd context <id>` in a table of purposes, `python -m taskmd context T-002` in a
# block of invocations), so one expression reads both. An advisory is written as a backticked
# all-caps name. `{3,}` on the first word is not decoration: the advisory region also contains
# `` `OK` ``, in the sentence about `check` saying it twice over a duplicated index, and a two-letter
# token would have been read as a fourth advisory.
KINDS = (
    Kind("commands",
         re.compile(r"taskmd\s+([a-z][a-z0-9-]*)"),
         lambda cli: set(cli.COMMANDS),
         ("README.md", os.path.join("plugin", "skills", "taskmd", "taskmd", "cli.py"))),
    Kind("advisories",
         re.compile(r"`([A-Z]{3,}(?: [A-Z]+)*)`"),
         lambda cli: set(cli.ADVISORY_PREFIXES),
         ("README.md",)),
    Kind("list-options",
         re.compile(r"(--[a-z][a-z0-9-]*)"),
         lambda cli: set(flag for flag, _, _, _ in cli.LIST_OPTIONS),
         (os.path.join("plugin", "skills", "taskmd", "taskmd", "cli.py"),)),
)


def opens(marker, line):
    """True when this line *is* the opening marker, rather than merely containing one.

    **A marker counts only alone on its line**, and that rule was written by running the sweep, not
    foreseen. Discovery below reads every tracked file, and T-134's own task record describes the
    mechanism it built - `` `<!-- taskmd:commands -->` `` inline in a sentence, inside backticks.
    The first run read that record as a document listing the commands and failed, naming a task file
    as behind. Excluding `tasks/` would have been an exclusion list to maintain, and wrong anyway:
    the next document to describe the markers would be documentation. A real region marker sits on
    its own line in all three places that use one, and a quotation never can.

    Takes the marker name rather than a `Kind`: since T-147 a region also carries a claim that is
    **text** - a quoted transcript - and that consumer has no set and no pattern.
    """
    return line.strip() == "<!-- taskmd:%s -->" % marker


def closes(marker, line):
    return line.strip() == "<!-- taskmd:end-%s -->" % marker


def region_lines(path, marker):
    """The lines inside a document's region, or None if it carries none of this marker.

    Opt-in by marker rather than by guessing which documents are lists (T-134 Q1). A heuristic -
    "any document naming every current member is a list" - needs no markup and stops checking a
    document the moment one name drops out of it, which is the failure being guarded.
    """
    lines = read(path).splitlines()
    start = next((i for i, line in enumerate(lines) if opens(marker, line)), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if closes(marker, lines[i])), None)
    if end is None:
        raise AssertionError("%s opens a taskmd:%s region and never closes it" % (path, marker))
    return lines[start + 1:end]


def marked_region(path, kind):
    """The names inside a document's region of this kind, or None if it carries none."""
    lines = region_lines(path, kind.name)
    return None if lines is None else set(kind.pattern.findall("\n".join(lines)))


def tracked_files():
    """Every file a clone receives, so a document that opts in is checked wherever it is.

    `git ls-files` for the same reason the dash gate above uses it: it is the definition of what
    ships, and it needs no exclusion list of its own to keep in step.
    """
    listed = subprocess.check_output(["git", "ls-files", "--cached", "--others",
                                      "--exclude-standard"], cwd=ROOT)
    return [p for p in listed.decode("utf-8").splitlines() if p]


def documents_carrying(marker):
    """Every tracked file with a region of this marker, discovered rather than written down."""
    found = []
    for rel in tracked_files():
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        try:
            text = read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if any(opens(marker, line) for line in text.splitlines()):
            found.append(rel)
    return sorted(found)


class TheFixtureReadmeNamesTheFixturesThereAre(unittest.TestCase):
    """T-195. `tests/fixtures/README.md` is the document somebody reads before adding a fixture, it
    describes a set the tests own, and nothing compared the two - so it had fallen six behind, four
    of them for days. Same class as T-134 and T-139, in the one place neither looked.

    **No marked region here, unlike the lists above.** Those need one because their documents mix
    members with prose that merely mentions a member; this document is about nothing else, and a
    backticked directory name in it is unambiguous. The set is read from the directory, so a fixture
    added tomorrow is in the comparison without anybody adding a row.
    """

    def setUp(self):
        self.readme = os.path.join(ROOT, "tests", "fixtures", "README.md")
        self.text = read(self.readme)

    def fixtures(self):
        base = os.path.join(ROOT, "tests", "fixtures")
        return set(name for name in os.listdir(base)
                   if os.path.isdir(os.path.join(base, name)) and not name.startswith("_"))

    def named(self):
        return set(re.findall(r"`([a-z][a-z0-9-]*)`", self.text))

    def test_every_fixture_is_named(self):
        missing = sorted(self.fixtures() - self.named())
        self.assertEqual([], missing,
                         "tests/fixtures/README.md names no fixture called %s, so a reader looking "
                         "for one finds a directory the document does not admit to"
                         % ", ".join(missing))

    def test_a_name_the_directory_cannot_answer_fails_too(self):
        """The other direction, without which a deleted fixture leaves its paragraph behind. Only
        names that look like a fixture are judged: the document backticks plenty of other things,
        so the comparison is against what the directory has ever held rather than against every
        lowercase token."""
        looks_like_one = set(n for n in self.named()
                             if n.startswith(("broken-", "alt-", "backend-")) or
                             n in ("ordering", "leak-check", "planned-deliverable",
                                   "nested-at-root", "abandoned-slot", "wide-table-row",
                                   "label-shaped-value", "malformed-date", "migrated-away",
                                   "section-reference"))
        gone = sorted(looks_like_one - self.fixtures())
        self.assertEqual([], gone,
                         "tests/fixtures/README.md describes %s, which is not there"
                         % ", ".join(gone))

    def test_no_fixture_is_given_an_ordinal(self):
        """T-188's ruling, in the place that produced this task's second finding: `planned-deliverable`
        and `nested-at-root` were **both** the third positive case. An ordinal is a count of the set
        as it stood when the sentence was written, and nothing re-reads it."""
        ordinals = re.findall(r"\b(?:the )?(second|third|fourth|fifth|sixth|seventh|eighth|ninth|"
                              r"tenth) positive case", self.text)
        self.assertEqual([], ordinals,
                         "tests/fixtures/README.md numbers its positive cases: %s"
                         % ", ".join(sorted(set(ordinals))))


class EveryMarkedListNamesTheSetTheCodeOwns(unittest.TestCase):
    """T-134, generalised by T-139 on the project owner's ruling of 2026-08-15: the guarded thing is
    *any* marked list of a set the code owns, not the command lists.

    T-134 guarded the commands and stopped, correctly for its scope. Nothing generalised it, so the
    next enumerated set to drift was the next one nobody was watching: T-138 shipped a third advisory
    line and left `README.md` naming two, caught four days later by a person's grep. That is the
    third instance of one fault - T-073 was the first - which is evidence about the class.

    **A marker is a claim of completeness, not a claim of importance.** It is why the problem
    prefixes are not marked: `README.md` describes one of them and never says it is describing all of
    them, so a region there would assert something the document does not mean.

    **A count of one of these sets is either dated as a measurement or not written at all** (T-188).
    A marked list of members is guarded by everything above; a *number* of them is not, names none of
    them, and so no pattern reading names can see it. The paragraph you are reading said `fifteen`
    while seventeen existed, and the sentence it supported never needed the figure. Two exemptions,
    and they are the same one: a number a recorded decision **fixes** is not a count of a mutable set
    - four commands, four phases, three edge kinds - and a number written as *measured on a date* is
    a record of that day rather than a claim about now. Everything else drops the number, because the
    detector this would need is a mapping from prose nouns to code sets, which is a hand-kept list of
    exactly the kind this class is about."""

    def test_every_required_document_carries_its_region(self):
        """Without this, every assertion below passes on a tree where the markers were deleted -
        the region becomes unreadable, there is nothing to compare, and nothing fails (T-134 D2).

        This is the one place a document is named, and the naming is deliberate: discovery below
        finds what *has* a region, and no scan can tell you about a region someone removed."""
        for kind in KINDS:
            for where in kind.required:
                self.assertIsNotNone(
                    marked_region(os.path.join(ROOT, where), kind),
                    "%s carries no taskmd:%s region, so nothing checks the list in it"
                    % (where, kind.name))

    def test_each_marked_list_names_exactly_the_set_that_exists(self):
        """Both directions, over every document that opts in - **discovered**, not listed.

        T-134 rejected "the test naming the documents" as a third statement of where the surface is
        written, then shipped exactly that, so a third document opting in would have been read by
        nothing. The floor above and this sweep are different questions: which documents must have a
        region, and which documents have one."""
        cli = _cli()
        for kind in KINDS:
            carriers = documents_carrying(kind.name)
            self.assertTrue(carriers, "no document carries a taskmd:%s region, so this kind is "
                                      "declared and checked against nothing" % kind.name)
            expected = kind.owned(cli)
            self.assertTrue(expected, "the code owns no %s, so the comparison below is vacuous"
                                      % kind.name)
            for where in carriers:
                listed = marked_region(os.path.join(ROOT, where.replace("/", os.sep)), kind)
                self.assertEqual(expected, listed,
                                 "%s's %s list is behind: it does not name %s, and it names %s "
                                 "which do not exist"
                                 % (where, kind.name,
                                    sorted(expected - listed) or "nothing missing",
                                    sorted(listed - expected) or "nothing extra"))

    def test_a_name_mentioned_in_a_sentence_is_not_a_list(self):
        """On the real tree. `README.md` names commands in prose outside their region - an FAQ row,
        a paragraph about filters - an advisory outside theirs, in the `WIDE ROW` paragraph that
        contrasts itself with them, and three of `list`'s four options across the same document.
        None of that is checked, because the region is what declares an intent to be complete.

        **A kind `README.md` carries no region of is still exercised, with the whole file counting as
        outside.** Written that way by adding the third kind (T-149), which is what exposed it: this
        loop called `next()` with no default, so a kind this one document does not happen to carry
        raised `StopIteration`. The comment above `KINDS` promised that adding a kind is one row, and
        it was true only of a kind `README.md` already listed - which the next one will usually not
        be, since a region is a claim about the document that makes it.

        Each half asserts its own premise first, so it fails rather than passing vacuously if the
        README stops mentioning anything outside its regions."""
        cli = _cli()
        lines = read(os.path.join(ROOT, "README.md")).splitlines()
        for kind in KINDS:
            begin = next((i for i, line in enumerate(lines) if opens(kind.name, line)), None)
            if begin is None:
                outside = lines
            else:
                end = next(i for i in range(begin + 1, len(lines)) if closes(kind.name, lines[i]))
                outside = lines[:begin] + lines[end + 1:]
            named = set(kind.pattern.findall("\n".join(outside)))
            self.assertTrue(named,
                            "this test is vacuous unless README.md names a %s outside the region; "
                            "it no longer does, so the case is untested" % kind.name)
            expected = kind.owned(cli)
            self.assertNotEqual(expected, named & expected,
                                "every %s now appears outside the region too, so this test can no "
                                "longer distinguish a mention from a list" % kind.name)


#: The marker on a quoted transcript. One region carries a claim about *text*, where `KINDS` carry
#: claims about a set - the two consumers `region_lines` was split out for (T-147).
SAMPLE = "sample-check"


class AQuotedRunIsWhatTheCommandPrints(unittest.TestCase):
    """T-147. A pasted transcript rots differently from a list, which is why T-134's guard could not
    see it: an enumeration drifts by losing a member a reader knows to look for, and a transcript
    reads as *evidence* - it carries a shape nobody re-derives, because the point of pasting output
    is that it was observed.

    The README's `check` sample had been wrong for three days when T-141 found it. `examined()`
    builds that summary from the checks that actually ran (T-095), so **every new check changes the
    line by construction** - two of the last three did. It is not a documentation habit that can be
    improved; it is a guarantee that the quote goes stale on a schedule.

    **Guarded by comparison, never by generation** - the project owner's ruling of 2026-08-16, whose
    reason is in T-147 §1: the README is what a stranger reads before installing, and a
    machine-written block in it buys correctness with the thing `docs/SCOPE.md` §5 *humanized*
    protects."""

    def a_project_holding_nothing_but_its_task_folder(self, work):
        """The state the README's own two lines put a reader in: `mkdir tasks`, and no repository.

        The folder name is the schema's, not this test's - a project that renamed `tasks_dir` would
        otherwise be compared against a directory it does not have."""
        cli = _cli()
        os.mkdir(os.path.join(work, cli.load_schema(ROOT).tasks_dir))

    def test_the_readme_sample_run_is_what_the_command_prints_today(self):
        """Run, then diffed. Nothing here writes a denominator, a count or a line of the output."""
        cli = _cli()
        quoted = region_lines(os.path.join(ROOT, "README.md"), SAMPLE)
        self.assertIsNotNone(quoted, "README.md carries no taskmd:%s region, so its sample run is "
                                     "guarded by nothing" % SAMPLE)
        # The tool's own idea of a fence, so the region may hold the block markup a reader sees.
        expected = [ln for ln in quoted if not cli.FENCE.match(ln) and ln.strip()]
        self.assertTrue(expected, "the taskmd:%s region is empty" % SAMPLE)

        work = tempfile.mkdtemp()
        try:
            self.a_project_holding_nothing_but_its_task_folder(work)
            env = dict(os.environ, PYTHONPATH=os.path.join(ROOT, "plugin", "skills", "taskmd"))
            run = subprocess.run([sys.executable, "-m", "taskmd", "check"], cwd=work, env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        finally:
            shutil.rmtree(work, ignore_errors=True)
        self.assertEqual(0, run.returncode, run.stdout)
        printed = [ln for ln in run.stdout.decode("utf-8").splitlines() if ln.strip()]
        # The diff *is* the repair instruction, and unittest truncates it by default to 640-odd
        # characters - which lands mid-summary on a line this long and hides the changed word.
        self.maxDiff = None
        self.assertEqual(printed, expected,
                         "README.md quotes a `check` run this tool no longer produces")

    def test_no_record_of_a_past_run_is_in_the_guarded_set(self):
        """**METHOD §1.5 forbids rewriting what a record says about the past**, and this repository is
        full of transcripts that are exactly that: 195 of the 204 taskmd-shaped blocks in the tree
        are inside task records (T-147 §1, counted). A guard that re-derived them would not be
        keeping documents true, it would be destroying the evidence a closed task exists to hold.

        Marking is opt-in, so this cannot happen by resemblance - only by someone putting the marker
        in a record on purpose. That is the person this assertion is addressed to, and the folder is
        read from the schema so it stays right for a project that renamed it."""
        cli = _cli()
        tasks = cli.load_schema(ROOT).tasks_dir.replace("\\", "/").rstrip("/") + "/"
        inside = [rel for rel in documents_carrying(SAMPLE) if rel.startswith(tasks)]
        # `assertFalse`, not `assertEqual([], ...)`: the failure is a sentence about what a record
        # is for, and a list diff in front of it is noise.
        self.assertFalse(inside,
                         "%s carries a taskmd:%s region; a record of a run that happened must not "
                         "be re-derived" % (", ".join(inside), SAMPLE))


# --------------------------------------------------------------------------------------------
# The leak check, run by the suite instead of remembered at publication (T-186).
#
# `docs/PUBLISHING.md` §6 is the same shape §5 was before T-126: a command a person types before
# publishing, so it runs at publication or never. Four records have broken one of its two written
# remedies -- T-013, T-018, T-129 and T-142 -- every one caught by a person and two by accident.
#
# **Nothing about the rule is written here.** The pattern, the exclusion and the accepted set are
# read out of §6, which stays their one home. That is not only T-126's shape: the check reads this
# file too, so a restated pattern would be a tripping literal in a tracked document, and this test
# would fail on its own source. Lifting is what makes the test possible at all.

LEAK_PATTERN_RE = re.compile(r"grep -nIE '([^']+)'")
LEAK_EXCLUDE_RE = re.compile(r"':!([^']+)'")
ACCEPTED_BLOCK_RE = re.compile(r"```text\n# accepted[^\n]*\n(.*?)```", re.S)

FIXTURE = os.path.join("tests", "fixtures", "leak-check", "samples.txt")
CAUGHT = "<- must be caught"
IGNORED = "<- must be ignored"


def leak_check_from_the_document():
    """The pattern, the exclusion and the accepted set, lifted from `docs/PUBLISHING.md` §6.

    Strict for the same reason `gate_from_the_document` is: a shape this cannot parse means the
    documented check and the enforced one have come apart, which is the state this exists to stop.
    """
    text = read(PUBLISHING)
    parts = text.split("## 6. The pre-publish check", 1)
    if len(parts) != 2:
        raise AssertionError("docs/PUBLISHING.md has no '## 6. The pre-publish check' - the check "
                             "has moved, and this test reads it from there rather than restating it")
    body = parts[1].split("\n## ", 1)[0]
    pattern = LEAK_PATTERN_RE.search(body)
    exclude = LEAK_EXCLUDE_RE.search(body)
    block = ACCEPTED_BLOCK_RE.search(body)
    if not pattern:
        raise AssertionError("could not read the grep pattern out of docs/PUBLISHING.md section 6")
    if not exclude:
        raise AssertionError("could not read the ':!...' exclusion out of docs/PUBLISHING.md "
                             "section 6")
    if not block:
        raise AssertionError("docs/PUBLISHING.md section 6 has no fenced '# accepted' block; the "
                             "accepted set is what a passing run is compared against, and this "
                             "test will not guess it")
    accepted = {}
    for line in block.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        where, _, count = line.rpartition(" ")
        try:
            accepted[where.strip()] = int(count)
        except ValueError:
            raise AssertionError("docs/PUBLISHING.md section 6's accepted block has a row this "
                                 "cannot read as '<path> <lines>': %r" % line)
    if not accepted:
        raise AssertionError("docs/PUBLISHING.md section 6's accepted block is empty; if nothing "
                             "is accepted any more, the block should say so rather than vanish")
    return re.compile(pattern.group(1)), exclude.group(1), accepted


def leak_hits(rx, skip=None):
    """What a run reports, as {path: number of matching lines}.

    Binary files are skipped, which is what `grep -I` does in the documented command.
    """
    found = collections.defaultdict(int)
    for rel in tracked_files():
        if skip is not None and rel.startswith(skip):
            continue
        try:
            text = read(os.path.join(ROOT, rel))
        except (UnicodeDecodeError, OSError, ValueError):
            continue
        for line in text.splitlines():
            if rx.search(line):
                found[rel] += 1
    return dict(found)


@unittest.skipUnless(GIT, "no git: the scanned set is what `git ls-files` reports, so there is "
                          "nothing to resolve")
class TheLeakCheckIsRunHereRatherThanRemembered(unittest.TestCase):
    """Named for the failure it removes: the check worked, and nobody ran it.

    Every instance it has caught was found by a person reading its output, twice while doing
    something else. §6 states the pass condition as a set so that a machine can hold it; this is
    the machine.
    """

    def test_the_document_still_yields_a_pattern_an_exclusion_and_a_set(self):
        rx, exclude, accepted = leak_check_from_the_document()
        self.assertTrue(rx.pattern, "section 6's pattern is empty")
        self.assertTrue(exclude, "section 6's exclusion is empty")
        for where in accepted:
            self.assertTrue(os.path.exists(os.path.join(ROOT, where)),
                            "docs/PUBLISHING.md section 6 accepts hits in %s, which does not "
                            "exist - the accepted set has outlived the file it names" % where)

    def test_every_hit_is_one_the_document_accepts(self):
        """The set, not the count. A total would go red the day the accepted set legitimately
        changes and be repaired by editing a number in here - the second home §6 exists to avoid."""
        rx, exclude, accepted = leak_check_from_the_document()
        self.assertEqual(
            accepted, leak_hits(rx, skip=exclude),
            "the pre-publish check no longer prints what docs/PUBLISHING.md section 6 says it may. "
            "A file on the left only is a hit the document accepts and the tree no longer has; a "
            "file on the right only, or a different count, is a finding - see section 6 for the "
            "two written remedies before reaching for the accepted block")

    def test_the_fixture_still_proves_the_pattern_can_fire(self):
        """§6's second run. A clean tree cannot show the pattern works; the fixture can, and it
        says which of its own lines must be caught, so no count is written down here."""
        rx, _, _ = leak_check_from_the_document()
        lines = read(os.path.join(ROOT, FIXTURE)).splitlines()
        must = set(i for i, line in enumerate(lines, 1) if CAUGHT in line)
        must_not = set(i for i, line in enumerate(lines, 1) if IGNORED in line)
        self.assertTrue(must, "%s no longer marks any line '%s'" % (FIXTURE, CAUGHT))
        self.assertTrue(must_not, "%s no longer marks any line '%s'" % (FIXTURE, IGNORED))
        caught = set(i for i, line in enumerate(lines, 1) if rx.search(line))
        self.assertEqual(must, caught & (must | must_not),
                         "the fixture's marked lines and what the pattern catches have come apart; "
                         "a class that stopped firing reads as a hole in the branch that did not, "
                         "and the repair it invites is loosening a branch that was already correct")


# The class set is derived in `tests/classes.py`, which is its one home since T-197 - it is compared
# against here and in `tests/test_cli.py`, and a second derivation would be the defect T-191 found.
sys.path.insert(0, os.path.join(ROOT, "tests"))
from classes import check_classes  # noqa: E402


def bindings():
    """Every shipped binding, read from the directory so a new one is covered unasked."""
    base = os.path.join(ROOT, "plugin", "skills", "taskmd", "docs", "bindings")
    return sorted(os.path.join(base, name) for name in os.listdir(base) if name.endswith(".md"))


class EveryBindingDeclaresWhatCannotOccur(unittest.TestCase):
    """`BINDING.md` §4 requires each binding to name the classes its backend makes impossible.

    **Only the hygiene is mechanical, and the clause says so.** Whether a class really cannot occur
    on some hosting service is a fact about that service; nothing running here knows it, so that half
    is reviewed by a person. What this catches is the half a hand-kept list dies of: a binding that
    never carried the statement, and a binding naming a class the validator no longer reports.
    """

    MARKER = "cannot-occur"

    def test_every_binding_carries_the_region(self):
        missing = [os.path.relpath(p, ROOT).replace(os.sep, "/")
                   for p in bindings() if region_lines(p, self.MARKER) is None]
        self.assertEqual([], missing,
                         "%s carries no taskmd:%s region, so BINDING.md section 4 asks it for a "
                         "statement it does not make" % (", ".join(missing), self.MARKER))

    def test_every_class_named_is_one_the_validator_reports(self):
        known, unknown = check_classes(), []
        for path in bindings():
            lines = region_lines(path, self.MARKER)
            if lines is None:
                continue
            named = set(re.findall(r"`([A-Z]{3,}(?: [A-Z]+)*)`", "\n".join(lines)))
            for name in sorted(named - known):
                unknown.append("%s names `%s`" % (os.path.relpath(path, ROOT).replace(os.sep, "/"), name))
        self.assertEqual([], unknown,
                         "a binding declares a class the validator does not report, so the "
                         "declaration has drifted from the code it is about:\n  " +
                         "\n  ".join(unknown))

    def test_the_derivation_finds_the_classes_the_bindings_actually_name(self):
        """The case without which both tests above pass vacuously.

        If `check_classes()` returned nothing, `test_every_class_named` would report every name as
        unknown - loud, and survivable. If it returned too much, that test passes by construction and
        nothing says so. So the derivation is held against a class each shipped binding names: a run
        where these are absent is a derivation that has stopped reading the code.
        """
        known = check_classes()
        for name in ("DUPLICATE ID", "STALE INDEX", "PARKED TASK", "SECTION REF"):
            self.assertIn(name, known, "check_classes() no longer finds %r" % name)
        self.assertGreater(len(known), 15, "check_classes() found only %d classes" % len(known))


class TestTheGuardOnTheDerivedSetStillBites(unittest.TestCase):
    """`NOT_A_CHECK_CLASS` subtracts nothing today, so nothing was exercising it (T-214).

    Measured 2026-08-22: `CONFIG ERROR` is in neither the problem prefixes nor `ADVISORY_PREFIXES`,
    so it is not in the union the constant is subtracted from. `cli.py` prints it from the config
    loader with a bare `print()`, before any check runs.

    **That makes it a guard for a world one edit away, not dead code.** Turning either of those two
    prints into a `problems.append` puts the class into the union and the subtraction starts
    mattering. The danger is the ordinary one for a guard nobody reads: if the derivation's shape
    changed so the class could never enter the union again, the line would be inert permanently and
    nothing would report it - the same silence T-191 and T-197 exist over, one module down.

    So this feeds `check_classes` the one source shape the guard exists for, and asserts both
    directions. **The second assertion is what stops the first passing vacuously**: without it, a
    `check_classes` that had quietly dropped the subtraction would still produce a set with no
    `CONFIG ERROR` in it, because the synthetic source might have stopped matching the regex.
    """

    #: The shape `cli.py` would have if either `print("CONFIG ERROR ...")` became a problem. Written
    #: here rather than read from anywhere, because the point is a source this repository does *not*
    #: contain - a fixture for a one-line edit.
    APPENDS_CONFIG_ERROR = 'problems.append("CONFIG ERROR  %s" % exc)'

    def test_the_class_does_not_come_out_of_a_source_that_appends_it(self):
        self.assertNotIn("CONFIG ERROR", check_classes(source=self.APPENDS_CONFIG_ERROR),
                         "the derivation now returns CONFIG ERROR, so the subtraction in "
                         "tests/classes.py has stopped being applied")

    def test_it_would_come_out_without_the_guard(self):
        """The companion. Without this, the test above cannot tell a working guard from a source
        the regex never matched in the first place."""
        import classes as classes_module
        kept = classes_module.NOT_A_CHECK_CLASS
        try:
            classes_module.NOT_A_CHECK_CLASS = ()
            self.assertIn("CONFIG ERROR", check_classes(source=self.APPENDS_CONFIG_ERROR),
                          "with the guard emptied the class still does not appear, so the test "
                          "above is passing on a source the derivation cannot read - the guard is "
                          "not what is keeping it out")
        finally:
            classes_module.NOT_A_CHECK_CLASS = kept

    def test_the_guard_is_inert_against_the_real_source_and_that_is_recorded(self):
        """The measurement the two above are built on, kept live rather than written in prose.

        The day this fails, `CONFIG ERROR` has entered the real union - which is a change to shipped
        behaviour somebody made deliberately, and the two tests above become the live guard rather
        than a fixture-driven one. Failing here is the notification.
        """
        import classes as classes_module
        kept = classes_module.NOT_A_CHECK_CLASS
        try:
            classes_module.NOT_A_CHECK_CLASS = ()
            self.assertNotIn("CONFIG ERROR", check_classes(),
                             "CONFIG ERROR is now in the derived set before subtraction, so the "
                             "guard has started biting on the real source. That is not a defect - "
                             "it means cli.py now reports it as a problem, and this test is the "
                             "record of when that stopped being true")
        finally:
            classes_module.NOT_A_CHECK_CLASS = kept


if __name__ == "__main__":
    unittest.main()
