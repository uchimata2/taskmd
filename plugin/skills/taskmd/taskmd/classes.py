"""The set of classes `check` can print, derived from the code (T-197, T-236).

**One home for a set several readers compare against.** `check --classes` prints it for a binding
author, who needs the names to write the *cannot occur* declaration
[`BINDING.md`](../docs/BINDING.md) §4 asks for; `tests/test_publishing.py` needs it to judge each
binding's declaration, and `tests/test_cli.py` needs it so every fixture is asserted silent about
every class but its own. Before this derivation existed the last of those was a hand-typed list of
fourteen against a real twenty-one, and nothing anywhere compared the two — which is the defect
T-191 found.

**It lives in the package rather than in `tests/`, and that is forced rather than preferred.**
`tests/` sits outside `plugin/`, so an install receives none of it (T-053) and a shipped flag could
not import from there. `tests/classes.py` is now a re-export of this module: one derivation, two
callers, which is what stops T-191's defect being re-created in the code written to remove it.

**Why the problem prefixes are read out of the source and the advisory ones are not.**
`ADVISORY_PREFIXES` is already a module constant with one home, so it is imported. The problem
prefixes have no constant: each is embedded in the format string at its own `problems.append` site,
padded to a column. Giving them a constant would touch `cli.py` at twenty sites and change the
padding that aligns `check`'s output, and the guard below already covers what it would buy.

**The cost of reading source text, stated rather than hidden.** A prefix that stopped matching this
pattern would silently leave the set, and a shrunken set makes the assertions that use it *weaker*
rather than louder. `TestTheDerivationCanStillRead` in `tests/test_publishing.py` is the reader that
catches it: it holds the derivation against classes the shipped bindings name and against a floor on
the size of the set.

**Reading the source works from an installed copy, measured rather than assumed** (T-236). The
derivation opens `cli.__file__`, and until it shipped it had only ever run from a checkout. Run
against this machine's installed `0.5.0` snapshot on 2026-08-23 it read that copy's own prefixes —
fourteen, against twenty-two in the working tree — which is the mechanism working and the snapshot
being older, and is the reason `check --classes` answers for the version the caller actually has.
"""

import io
import re

from . import cli

# The literal at each `problems.append` site, up to the column padding. `[A-Z][A-Z ]+` stops at the
# first lowercase, which is where every message's variable part begins.
PROBLEM_PREFIX_RE = re.compile(r'problems\.append\(\s*"([A-Z][A-Z ]+)')

# Reported by the config loader while the schema loads, before any check runs. It is not a class
# `check` owns, so it is not one a binding can declare, a fixture be asserted silent about, or
# `--classes` print.
#
# **It subtracts nothing today, and that is deliberate rather than dead** (T-214). `cli.py` prints
# `CONFIG ERROR` with a bare `print()`, so `PROBLEM_PREFIX_RE` never finds it and the union below
# never holds it. Turn either of those two prints into a `problems.append` - one line, and a change
# somebody could make for good reasons - and the class enters the union and this line starts biting.
# T-211 measured both states.
#
# **So it has a reader**, in `tests/test_publishing.py`: `TestTheGuardOnTheDerivedSetStillBites`
# feeds `check_classes` the one source shape this line exists for and asserts the class does not
# come out, with a companion assertion that it does come out when the guard is emptied. **Rejected:
# a note and nothing else** - a note cannot fail, and the risk here is not that the line is wrong
# but that it becomes permanently inert with nothing to say so. **Rejected: deleting it** - it does
# real work one edit away, and without it a class no binding can declare and no fixture can be
# marked silent about would enter the set every cross-fixture assertion iterates.
NOT_A_CHECK_CLASS = ("CONFIG ERROR",)


def check_classes(source=None):
    """Every class `check` can print — the problem prefixes and the advisories together.

    `source` overrides the text the prefixes are read from, and exists for exactly one caller:
    the reader on `NOT_A_CHECK_CLASS` above, which has to run this function over the shape that
    makes the subtraction bite. Passing the text rather than asserting on the regex and the
    constant separately is what keeps the guarded line itself in the run - a check built out of
    the pieces would pass on a version of this function that had dropped the subtraction.
    """
    if source is None:
        with io.open(cli.__file__, encoding="utf-8") as handle:
            source = handle.read()
    problems = set(found.rstrip() for found in PROBLEM_PREFIX_RE.findall(source))
    return (problems | set(cli.ADVISORY_PREFIXES)) - set(NOT_A_CHECK_CLASS)
