# `src/cobalt/cli.py`

## What it does
The new core's top-level CLI. Command groups are mounted by the modules
that own them — `cli.py` holds the vault commands and `validate`, and
everything else is `add_parser(sub)` from its own package.

```
cobalt vault restore --write-id N [--dry-run] · writes · overrides
cobalt session now/backfill/blocks
cobalt cards state/history/move/backfill/expire/edges
cobalt daymode show/propose/decide/attest
cobalt jobs list/register/check/run
cobalt stop | cobalt resume                       (F17d kill phrase)
cobalt heartbeat beat/show
cobalt validate
```

## `restore` goes through the same writer
Same markers, same mtime/hash guard, same atomic rename, and its own
audit row. There is no second write path, not even for undo.

## `validate` is the F16 gate
One name an operator can remember for the config check the tests run.
It calls **the same loaders the runtime does**, so a config that passes
here is one the runtime can boot on. Building the object *is* the check.

It covers: every trade_def and the tunable registry · the NYSE calendar
and the session boundaries · the sheet order, the day-mode ladder, the
`reduced` pointer, the derived `.htk` names and the step-down table ·
the trade-count band rows · card-state reachability · F19's patterns and
the literal guard's status · the notify channel · the job registry.

### Two cross-checks nothing else can do
- **registry ↔ `ops/`** — exact label match. A registry that has drifted
  from launchd reports green for a job that is gone; a plist with no row
  is a job nobody watches.
- **registry ↔ plists** — every schedule and every `COBALT_ENV`. launchd
  cannot read a tunables row, so the heartbeat's `StartInterval 900` is
  a mirror of `heartbeat.interval_min`, and a mirror nobody compares is
  a mirror that drifts.

### The `SheetMode` coupling check
A sheet declared in config with no `SheetMode` enum member would pass
every day-mode check and then fail at card-creation time, at 09:31 on a
live morning. `validate` turns that into a config-gate failure.

## `JobStopped` exits 0
A job turned away by the kill switch did not fail — the operator stopped
it on purpose, and a non-zero exit would paint F18 red for a state he
caused deliberately.

## `load_dotenv` is deliberate and visible
`db.connect()` composes its DSN from `.env` parts today. The prefill and
ASET entry points get them by *accident*, through a transitive old-tree
import; this CLI has no such chain, so it loads the same file on purpose.
