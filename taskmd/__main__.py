#!/usr/bin/env python
"""Entry point: `python -m taskmd <command>`.

A module rather than a top-level script, so a clone runs it without the package being installed
and without `taskmd.sh` / `taskmd.ps1` having to carry a file path — each of them puts this
package's folder on `PYTHONPATH` and names the module, which is the whole of what a launcher does.
"""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
