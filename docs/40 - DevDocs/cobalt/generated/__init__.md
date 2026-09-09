# `src/cobalt/generated/__init__.py`

## What it does
Names the package and re-exports the config loader. The docstring is the
package's reason for existing, and it is worth reading before the code.

## Why the package exists
Three tracked files are rewritten by scheduled jobs and nothing commits
them:

| file | written by |
|---|---|
| `docs/40 - DevDocs/reports/seat-usage.md` | `com.cobalt.seat-usage`, hourly 06:00-23:00 ET |
| `docs/30 - Design/archiver-runs.md` | `com.cobalt.archiver`, one row per nightly run |
| `configs/cobalt/rules.yaml` | `com.cobalt.prefill-daily`, `generated_at` at 05:15 |

So `~/cobalt` — which **is** production (R4, 2026-09-08) — is
permanently dirty. **A permanently dirty working tree is one nobody
reads.** Every deploy starts by squinting at `git status` deciding which
lines are "just the jobs", which is precisely the state in which a real
uncommitted change gets waved through.

The 09-08 and 09-09 ledger appendices both record leaving those files
uncommitted *"deliberately"*. That is a decision being re-made by hand
every single day, which is the definition of a rule that wants to be
code.

## The shape
`configs/cobalt/generated.yaml` declares the paths →
`config.load_generated_config()` validates them (they must exist **and**
be tracked) → `committer.commit_generated()` stages only the dirty ones
and commits → `cli` wires it to `cobalt generated commit`, which
`com.cobalt.generated` runs at 23:37 ET daily.

## Neighbours
`jobs/` (the F17 wrapper this runs inside, and the registry row),
`cobalt/cli.py` (the parser), `ops/com.cobalt.generated.plist`.
