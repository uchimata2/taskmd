#!/usr/bin/env python
"""Entry point: `python -m taskmd <command>`.

A module rather than a top-level script, so a clone runs it without the package being installed
and without the launchers in T-011 having to carry a file path.
"""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
