"""Re-export of the package's class derivation, so the tests and the shipped flag share one (T-236).

**The derivation moved into the package on 2026-08-23 and this file is what is left of it.** It has
to be in the package because `check --classes` prints from it and `tests/` is outside `plugin/`, so
an install receives none of this directory. Keeping a second copy here is the defect T-191 found,
re-created in the place written to remove it — so this file computes nothing.

It stays rather than being deleted because two readers import from it by name:
`tests/test_publishing.py`'s `TestTheDerivationCanStillRead` and
`TestTheGuardOnTheDerivedSetStillBites`. Deleting it would move a shipped-code change into their
import lines for no gain.

  python -c "import sys; sys.path.insert(0, 'tests'); import classes; print(sorted(classes.check_classes()))"
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin", "skills", "taskmd")

if PKG not in sys.path:
    sys.path.insert(0, PKG)

from taskmd.classes import (  # noqa: E402  - the path insert above has to come first
    NOT_A_CHECK_CLASS,
    PROBLEM_PREFIX_RE,
    check_classes,
)

__all__ = ["NOT_A_CHECK_CLASS", "PROBLEM_PREFIX_RE", "check_classes"]


if __name__ == "__main__":
    found = sorted(check_classes())
    print("%d classes: %s" % (len(found), ", ".join(found)))
