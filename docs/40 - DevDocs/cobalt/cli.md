# `src/cobalt/cli.py`

S2-P1 registers the `radar` command group and guarded `db query` subcommand through their module-owned parser builders.

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
cobalt day-open [--date YYYY-MM-DD] [--json] | day-open verdict "<line>"
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

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Two new command groups: `cobalt db migrate [--allow-prod] [--rollback]`
and `cobalt settings load|show`, plus `cobalt taxonomy
load|migrate-strategy-notes|migrate-trade-notes|add-alias|sync-frontmatter`.

## 2026-09-14 — `day-open` (RULED, A)

The morning sweep, in code: `cobalt.dayopen.cli.add_parser` mounts
`day-open`. See `docs/40 - DevDocs/cobalt/dayopen/` for the module.

---

## 2026-09-17 — S2-P4: `cobalt replay`

`replay_cli.add_parser(sub)` mounts `cobalt replay nightly [--date]
[--dry-run]` (`replay/cli.md`).

## 2026-09-17 — S2-P4: `cobalt smoke`

`smoke_cli.add_parser(sub)` mounts `cobalt smoke <suite> --cutoff ISO8601
[--date] [--prod] [--json]`, the read-only sprint smoke checklist
(`smoke/cli.md`). The module docstring's command map now also lists
`cobalt replay nightly` and `cobalt smoke`.

## 2026-09-23 — voice V1: `cobalt voice turn`

One registration pair: `from cobalt.voice import cli as voice_cli` and
`voice_cli.add_parser(sub)` (after the archiver's block, reflowing none of
its neighbours) mounts `cobalt voice turn --text | --audio | --confirm
[--dry-run] [--session]` — the voice turn function's CLI caller
(`voice/cli.md`). `--confirm` refuses in production.

## 2026-09-24 — DRC K1: the `drc` group

`drc_cli.add_parser(sub)` mounts `cobalt drc state-book`. It dry-runs by
default and writes only with `--apply --sha256` (`drc/cli.md`). This is
the ONE `drc` group: D3's `cobalt drc build` joins it later (L3).

## 2026-10-05 — adoption-port

`cobalt validate --no-db` skips the three checks that read
`"user".trader_settings` (Sheets, the SheetMode coupling, Day modes with
their Hotkey files and Step-downs lines) and prints one
`SKIPPED (--no-db):` line for each. Every other check runs unchanged.
Without the flag, `validate` makes the same calls in the same order.
DEPLOY-HUB STEP-G (d2) runs it from the gate, which has no `.env`
(`reports/s3-d2-probe-2026-10-05.md`). Tests:
`tests/cobalt/test_validate_no_db.py`.

2026-10-05 (check, O2): `test_without_the_flag_the_three_checks_still_run_in_order`
pins the no-flag path. The SheetMode coupling still exits 1 on an
unmodelled sheet, and Day modes still runs after it on the same sheets
object. The first no-flag test passed on the first DB read alone.
