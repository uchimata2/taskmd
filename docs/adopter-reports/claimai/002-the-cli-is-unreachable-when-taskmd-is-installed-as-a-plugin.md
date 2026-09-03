# The CLI is unreachable when taskmd is installed as a plugin, and the cache keeps every version

| Field | Value |
| :--- | :--- |
| **Target** | `taskmd` — the maintainer's own repository, cloned beside the reporting project |
| **Kind** | Feature |
| **Status** | `open` |
| **Severity** | Medium — every adopter writes the same launcher, and the obvious version of it silently picks an old build |
| **Found while** | Setting the project up on 2026-08-23; the launcher has been the only supported invocation since |
| **Version seen** | 0.6.0 |

## What happens

Installed as a plugin, `taskmd` is **not on `PATH`**. Every command in this project's own
documentation goes through a wrapper:

```
pwsh -File tools/taskmd.ps1 list --open --limit 1
```

The wrapper resolves the installed plugin version at run time and anchors `--root` to the project. It
exists because a hard-coded cache path carries both a version number that changes on update and a
home directory — and a home directory is exactly what a handoff or a committed config may not record.

**The cache keeps every version.** A first-match glob picks the oldest, which is a different tool with
different behaviour, and nothing says so.

## What to change

1. **Ship a launcher, or document the invocation.** The commands in the README assume a `taskmd` on
   `PATH` that a plugin install does not provide.
2. **Say that the cache keeps every version**, and that any resolution must sort as versions rather
   than take the first match.
3. **Have `taskmd --version` report which install answered.** With several versions cached, the
   question *which one just ran* has no cheap answer today.

## Related

- The same gap in `htmldeck`, staged in this project's `upstream/htmldeck/` set. Two tools, one
  packaging problem — which suggests it belongs wherever plugin tooling is documented, not in either
  repository alone.
