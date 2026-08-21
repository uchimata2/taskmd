"""The set of classes `check` can print, derived from the code (T-197).

**One home for a set two test files compare against.** `tests/test_publishing.py` needs it to judge
each binding's *cannot occur* declaration; `tests/test_cli.py` needs it so every fixture is asserted
silent about every class but its own. Before this module the second was a hand-typed list of
fourteen against a real twenty-one, and nothing anywhere compared the two — which is the defect
T-191 found and this exists to remove. Writing the derivation twice would have re-created it in the
place that was watching for it.

**Why the problem prefixes are read out of the source and the advisory ones are not.**
`ADVISORY_PREFIXES` is already a module constant with one home, so it is imported. The problem
prefixes have no constant: each is embedded in the format string at its own `problems.append` site,
padded to a column. Giving them a constant would change `cli.py` at every append site, which is a
plugin change with adopter reach and is out of T-197's scope — so this reads them where they live.

**The cost of reading source text, stated rather than hidden.** A prefix that stopped matching this
pattern would silently leave the set, and a shrunken set makes the assertions that use it *weaker*
rather than louder. `TestTheDerivationCanStillRead` in `tests/test_publishing.py` is the reader that
catches it: it holds the derivation against classes the shipped bindings name and against a floor on
the size of the set.

  python -c "import sys; sys.path.insert(0, 'tests'); import classes; print(sorted(classes.check_classes()))"
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin", "skills", "taskmd")

# The literal at each `problems.append` site, up to the column padding. `[A-Z][A-Z ]+` stops at the
# first lowercase, which is where every message's variable part begins.
PROBLEM_PREFIX_RE = re.compile(r'problems\.append\(\s*"([A-Z][A-Z ]+)')

# Reported by the config loader while the schema loads, before any check runs. It is not a class
# `check` owns, so it is not one a binding can declare or a fixture be asserted silent about.
NOT_A_CHECK_CLASS = ("CONFIG ERROR",)


def _cli():
    if PKG not in sys.path:
        sys.path.insert(0, PKG)
    from taskmd import cli
    return cli


def check_classes():
    """Every class `check` can print — the problem prefixes and the advisories together."""
    cli = _cli()
    with open(cli.__file__, encoding="utf-8") as handle:
        source = handle.read()
    problems = set(found.rstrip() for found in PROBLEM_PREFIX_RE.findall(source))
    return (problems | set(cli.ADVISORY_PREFIXES)) - set(NOT_A_CHECK_CLASS)


if __name__ == "__main__":
    found = sorted(check_classes())
    print("%d classes: %s" % (len(found), ", ".join(found)))
