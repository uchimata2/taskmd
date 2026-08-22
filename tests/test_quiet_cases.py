#!/usr/bin/env python
"""The quiet-case set, read from the fixtures themselves (T-202).

A **quiet case** is something a fixture carries in order to stay *silent* - a real date beside a
malformed one, a fenced table, a slot in a section an open task has not reached. Before this module
the set could not be computed: parsing the tests found 21 fixtures and missed two whose quiet tests
name no fixture literally, and `tests/fixtures/README.md` named five, which is prose. T-198 recorded
that as finding F-2, and it is why that audit's first criterion is *not met*.

**The marks are the authority.** Each quiet case says so on the line that carries it, in whatever
comment syntax that line already allows - a trailing `#` in front matter, a trailing HTML comment on
a heading. The form is `quiet: <CLASS> [<values>] - <why it stays silent>`, so a quiet case added
tomorrow is in the next reading with nothing edited anywhere else.

**The anchor is computed from where the mark sits**, never written into it: a hand-written line
number is a derived value and decays the first time a line is inserted above it. A heading covers
its section; any other line covers itself.

`<values>` is only needed where the marked line carries a quiet case *and* a firing one - a list
holding both a real date and a malformed one is the case that forces it. Omitted, the mark covers
the line's own value.

**Three things are asserted, and the third is what stops this shipping the silence it removes:**

1. the class a mark names is one `check` can print, from `tests/classes.py` (T-197's one home);
2. no alarm of that class names what the mark covers - the case really is quiet;
3. **the class fires at least once elsewhere in the same fixture.** Without it a mark could name a
   case the check never reaches, and the reading would report a silence produced by the check not
   looking. This is `leak-check`'s structure - a fixture stating both directions - generalised.

**What this cannot see.** An alarm names a value as `'<value>'` or as `section <value>`, and those
two shapes are what assertion 2 matches. A class naming a value some third way would be missed here,
and the mark would pass unearned.

  python tests/test_quiet_cases.py --list      # the reading
  python tests/test_quiet_cases.py             # the assertions
"""

import io
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin", "skills", "taskmd")
sys.path.insert(0, PKG)
sys.path.insert(0, os.path.join(ROOT, "tests"))

from taskmd import cli  # noqa: E402
from classes import check_classes  # noqa: E402

FIXTURES = os.path.join(ROOT, "tests", "fixtures")

# `values` is non-greedy up to the first spaced hyphen, not `[^-]*` - a date is full of hyphens, and
# a class of them stops matching the moment a value carries one. Two marks were dropped that way and
# the reading still looked healthy, which is why `TheReadingLosesNothing` exists below.
# The class is read as **whole words of two or more capitals**, not as a run of `[A-Z ]`. The run
# form swallowed the first letter of any value that begins with a capital: `quiet: CLOSED PARENT
# T-003 - ...` parsed as class `CLOSED PARENT T`, value `-003`, and assertion 1 then reported the
# *class* as unknown while printing a set that plainly contained it - a loud failure pointing at the
# wrong half (T-219). Every class `check` can print is words of two or more letters, so the shorter
# word is a value; the trailing guard makes a word followed by a hyphen or digit - `T-003`, `AB-1` -
# fail the class and fall through to `values`, where it belongs.
MARK_RE = re.compile(
    r"(?:#|<!--)\s*quiet:\s*(?P<cls>[A-Z]{2,}(?:\s+[A-Z]{2,})*)(?![\w-])"
    r"\s*(?P<values>.*?)\s+-\s+"
    r"(?P<why>.+?)\s*(?:-->)?\s*$")
# A mark is the word inside a comment, and the guard below looks for exactly that - matching the
# bare word instead makes any sentence using it read as a lost mark, which `tests/fixtures/README.md`
# demonstrated on this guard's first run.
MARK_WORD_RE = re.compile(r"(?:#|<!--)\s*quiet:")
HEADING_RE = re.compile(r"^(#+)\s")
ALARM_LINE_RE = re.compile(r"[\w./\\-]+[: ](?:body line )?(\d+)\b")

# `leak-check` is not a taskmd project and has no comment syntax, so its quiet cases stay in the
# second syntax this repository already had. Their checker is `tests/test_publishing.py`.
LEAK = os.path.join(FIXTURES, "leak-check", "samples.txt")
LEAK_QUIET = "<- must be ignored"
LEAK_LOUD = "<- must be caught"

# The quiet cases T-198's record names that this reading does **not** hold (T-211). Each carries the
# reason it cannot be marked, and each reason is **asserted below rather than described**, so the day
# one stops holding this module fails instead of ageing into a sentence nobody re-checks. Marking one
# of these without removing its reason is the mistake those assertions exist to catch.
NAMED_AND_UNMARKED = [
    {
        "fixture": "migrated-away",
        "cls": "CONFIG ERROR",
        "case": "no CONFIG ERROR, on a fixture where `index` and `context` still report one",
        "why": "not a class `check` owns - `cli.py` prints it from the config loader with a bare "
               "print(), not a problems.append(), so the derivation in tests/classes.py never "
               "picks it up and assertion 1 refuses the mark. That module also names it in "
               "NOT_A_CHECK_CLASS, which is a guard against the day the print becomes an "
               "append and subtracts nothing today - measured 2026-08-22, T-214",
    },
    {
        "fixture": "planned-deliverable",
        "cls": "MISSING OUTPUT",
        "case": "MISSING OUTPUT must not fire on an open task declaring a path that is not there",
        "why": "the class fires nowhere in that fixture, so assertion 3 refuses the mark: this is "
               "one half of a pair, and the firing half is `broken-deliverable`, one fixture over "
               "where a per-fixture reach assertion cannot see it - measured 2026-08-22, T-215",
    },
]


def read(path):
    return io.open(path, encoding="utf-8").read()


def _front_matter_span(lines):
    """(first, last) 0-based line indexes inside the `---` block, or None."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return (1, i - 1)
    return None


def _scope(lines, index):
    """The 1-based inclusive line range a mark on `lines[index]` covers.

    A heading covers down to the next heading of the same or higher level; anything else covers its
    own line. Computed, so no mark carries a line number of its own.
    """
    heading = HEADING_RE.match(lines[index])
    if not heading:
        return (index + 1, index + 1)
    level = len(heading.group(1))
    for j in range(index + 1, len(lines)):
        nxt = HEADING_RE.match(lines[j])
        if nxt and len(nxt.group(1)) <= level:
            return (index + 1, j)
    return (index + 1, len(lines))


def _own_values(line):
    raw = line.split(":", 1)[1].split("#")[0].strip()
    if raw.startswith("["):
        return [v.strip() for v in raw.strip("[]").split(",") if v.strip()]
    return [raw] if raw else []


def marks():
    """Every quiet case in the tree, read from the marks. One dict per case."""
    found = []
    for base, dirs, names in os.walk(FIXTURES):
        dirs.sort()
        for name in sorted(names):
            if not name.endswith(".md"):
                continue
            path = os.path.join(base, name)
            lines = read(path).split("\n")
            span = _front_matter_span(lines)
            rel = os.path.relpath(path, FIXTURES).replace("\\", "/")
            for i, line in enumerate(lines):
                found_mark = MARK_RE.search(line)
                if not found_mark:
                    continue
                declared = [v.strip() for v in found_mark.group("values").split(",") if v.strip()]
                in_front_matter = bool(span and span[0] <= i <= span[1])
                field, own = None, []
                if in_front_matter and ":" in line:
                    field = line.split(":", 1)[0].strip()
                    own = _own_values(line)
                found.append({
                    "path": path,
                    "rel": rel,
                    "fixture": rel.split("/")[0],
                    "cls": found_mark.group("cls").rstrip(),
                    "why": found_mark.group("why").strip(),
                    "line": i + 1,
                    "scope": _scope(lines, i),
                    "field": field,
                    "values": declared or own,
                    "declared": declared,
                })
    for i, line in enumerate(read(LEAK).split("\n"), 1):
        if LEAK_QUIET in line:
            found.append({
                "path": LEAK, "rel": "leak-check/samples.txt", "fixture": "leak-check",
                "cls": None, "why": "a safe form the pre-publish pattern must not match",
                "line": i, "scope": (i, i), "field": None, "values": [], "declared": [],
            })
    return found


def check_output(fixture):
    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        cli.main(["check", "--root", os.path.join(FIXTURES, fixture)])
    finally:
        sys.stdout = stdout
    return buffer.getvalue()


def alarms(text, cls):
    """The alarm lines of one class, class prefix stripped."""
    out = []
    for line in text.splitlines():
        if line.startswith(cls) and (len(line) == len(cls) or not line[len(cls)].isalpha()):
            out.append(line[len(cls):].strip())
    return out


class TheReadingIsComplete(unittest.TestCase):
    """Assertion 1, plus the hygiene that keeps the reading from quietly emptying."""

    def test_every_mark_names_a_class_check_can_print(self):
        known = check_classes()
        for mark in marks():
            if mark["cls"] is None:
                continue
            self.assertIn(mark["cls"], known,
                          "%s line %d marks a quiet case for '%s', which `check` cannot print - "
                          "the class set is derived in tests/classes.py"
                          % (mark["rel"], mark["line"], mark["cls"]))

    def test_the_reading_is_not_empty_and_covers_more_than_one_fixture(self):
        found = marks()
        self.assertTrue(found, "no quiet case is marked anywhere under tests/fixtures/")
        self.assertGreater(len(set(m["fixture"] for m in found)), 1, "only one fixture is marked")

    def test_a_declared_value_really_is_on_the_marked_line(self):
        """A mark may narrow itself to some of its line's values. A typo there would silently widen
        the mark to nothing, so the value has to be found where it claims to be."""
        for mark in marks():
            if not mark["declared"]:
                continue
            line = read(mark["path"]).split("\n")[mark["line"] - 1]
            for value in mark["declared"]:
                self.assertIn(value, line,
                              "%s line %d declares quiet value %r, which is not on that line"
                              % (mark["rel"], mark["line"], value))

    def test_the_leak_check_fixture_still_declares_both_directions(self):
        """Its quiet cases are read here and asserted in tests/test_publishing.py, which is where
        the pattern lives. This is the pointer, so the reading is not silently short of them."""
        text = read(LEAK)
        self.assertIn(LEAK_QUIET, text)
        self.assertIn(LEAK_LOUD, text)
        publishing = read(os.path.join(ROOT, "tests", "test_publishing.py"))
        self.assertIn(LEAK_QUIET, publishing)
        self.assertIn(LEAK_LOUD, publishing)


class TheReadingLosesNothing(unittest.TestCase):
    """A reader cannot report its own incompleteness, so the corpus is partitioned instead.

    Every line under `tests/fixtures/` carrying the mark word is either parsed into a case or named
    here as unparsed. Without this the reading drops a mark it cannot match and still looks healthy
    - which is what happened: a `values` class excluding hyphens silently lost the two marks whose
    values are a date and a three-part version, and every other assertion stayed green.
    """

    def test_every_line_carrying_the_mark_word_is_parsed_into_a_case(self):
        parsed = set((m["path"], m["line"]) for m in marks())
        unparsed = []
        for base, dirs, names in os.walk(FIXTURES):
            dirs.sort()
            for name in sorted(names):
                if not name.endswith(".md"):
                    continue
                path = os.path.join(base, name)
                for i, line in enumerate(read(path).split("\n"), 1):
                    if MARK_WORD_RE.search(line) and (path, i) not in parsed:
                        unparsed.append("%s line %d: %s"
                                        % (os.path.relpath(path, FIXTURES), i, line.strip()))
        self.assertEqual([], unparsed,
                         "these lines carry the mark word and the reading does not hold them, so "
                         "the quiet-case set is short by exactly this many and nothing else says "
                         "so:\n  " + "\n  ".join(unparsed))


class EveryMarkedCaseIsQuietAndItsClassIsInReach(unittest.TestCase):
    """Assertions 2 and 3."""

    def test_no_alarm_names_what_a_mark_covers(self):
        outputs = {}
        for mark in marks():
            if mark["cls"] is None:
                continue
            out = outputs.setdefault(mark["fixture"], check_output(mark["fixture"]))
            for alarm in alarms(out, mark["cls"]):
                located = ALARM_LINE_RE.search(alarm)
                if located and os.path.basename(mark["rel"]) in alarm:
                    self.assertFalse(
                        mark["scope"][0] <= int(located.group(1)) <= mark["scope"][1],
                        "%s lines %d-%d are marked quiet for %s and it reports: %s"
                        % (mark["rel"], mark["scope"][0], mark["scope"][1], mark["cls"], alarm))
                    continue
                for value in mark["values"]:
                    named = ("'%s'" % value) in alarm or ("section %s" % value) in alarm
                    if named and (mark["field"] is None or mark["field"] in alarm):
                        self.fail("%s line %d marks %r quiet for %s and it reports: %s"
                                  % (mark["rel"], mark["line"], value, mark["cls"], alarm))

    def test_every_marked_class_fires_somewhere_in_its_own_fixture(self):
        """A silence proves nothing where the check never looked. The same fixture has to show the
        class firing, or the mark is recording that `check` did not reach it."""
        seen = set((m["fixture"], m["cls"]) for m in marks() if m["cls"])
        for fixture, cls in sorted(seen):
            out = check_output(fixture)
            self.assertTrue(alarms(out, cls),
                            "%s marks a case quiet for %s and nothing in that fixture reports %s, "
                            "so the silence may be the check not reaching it rather than the case"
                            % (fixture, cls, cls))


class TheReadingIsShortByTwoAndSaysWhy(unittest.TestCase):
    """The reconciliation against T-198, kept live (T-211).

    T-198's record names three quiet cases in the two fixtures T-202's agreed scope excluded.
    **T-211 marked one and could not mark two**, so this reading is short against that record by
    exactly `len(NAMED_AND_UNMARKED)` - and the difference is *not* that a fixture was out of scope,
    which is the reading T-211's second criterion rules out. Both reasons are mechanical, and both
    are asserted here, so neither can quietly stop being true.
    """

    def test_neither_named_case_is_marked(self):
        """If one of them acquires a mark, its row here is stale and must go - the mark is the
        authority, and the two would otherwise be homes for one fact, disagreeing."""
        marked = set((m["fixture"], m["cls"]) for m in marks() if m["cls"])
        for row in NAMED_AND_UNMARKED:
            self.assertNotIn(
                (row["fixture"], row["cls"]), marked,
                "%s now marks a case for %s, so its row in NAMED_AND_UNMARKED is stale: remove the "
                "row, because the mark is the authority and the two now disagree"
                % (row["fixture"], row["cls"]))

    def test_the_config_error_row_is_refused_by_the_derived_class_set(self):
        """Its stated reason, run rather than read."""
        row = [r for r in NAMED_AND_UNMARKED if r["cls"] == "CONFIG ERROR"][0]
        self.assertNotIn(
            row["cls"], check_classes(),
            "CONFIG ERROR is now a class `check` owns, so the reason this row gives no longer holds "
            "and the case can be marked")

    def test_the_missing_output_row_is_refused_by_reach(self):
        """Its stated reason, run rather than read. Marking it while the class is silent in its own
        fixture would record a silence produced by the check not looking."""
        row = [r for r in NAMED_AND_UNMARKED if r["cls"] == "MISSING OUTPUT"][0]
        self.assertEqual(
            [], alarms(check_output(row["fixture"]), row["cls"]),
            "%s now reports %s, so the reach assertion would admit the mark and this row is stale"
            % (row["fixture"], row["cls"]))


def cases(mark):
    """How many quiet cases one mark vouches for. A mark narrowed to a list of values carries one
    per value - `windows: [2026-08-01, 2026-02-30, keep-me]` is one line holding two quiet cases and
    a firing one - so counting marks would undercount against a record that counts cases."""
    return max(1, len(mark["declared"]))


def listing():
    rows = marks()
    width = max(len(m["rel"]) for m in rows)
    out = ["%d quiet case(s) in %d mark(s), across %d fixture(s):"
           % (sum(cases(m) for m in rows), len(rows),
              len(set(m["fixture"] for m in rows)))]
    for fixture in sorted(set(m["fixture"] for m in rows)):
        own = [m for m in rows if m["fixture"] == fixture]
        out.append("  %-22s %2d case(s) in %d mark(s)"
                   % (fixture, sum(cases(m) for m in own), len(own)))
    out.append("  %-22s %2d case(s) named by T-198 and not marked - reasons below"
               % ("(no fixture)", len(NAMED_AND_UNMARKED)))
    out.append("")
    for mark in rows:
        out.append("  %-*s  line %-3d  %-14s %s"
                   % (width, mark["rel"], mark["line"], mark["cls"] or "(leak-check)", mark["why"]))
    out.append("")
    out.append("Named by T-198 and not marked - the reading is short by %d, and not because "
               "a fixture was out of scope:" % len(NAMED_AND_UNMARKED))
    for row in NAMED_AND_UNMARKED:
        out.append("  %-22s %-15s %s" % (row["fixture"], row["cls"], row["case"]))
        out.append("  %-22s %-15s   because %s" % ("", "", row["why"]))
    return "\n".join(out)


if __name__ == "__main__":
    if "--list" in sys.argv:
        print(listing())
    else:
        unittest.main()
