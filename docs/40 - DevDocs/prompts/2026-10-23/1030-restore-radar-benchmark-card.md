JOB: restore-radar-benchmark
LADDER: OFF-LADDER — reports/cto-2026-10-24.md R2410
CLASS: K3
BRANCH: main
WORKTREE: none
BASE: 1ef351db
TAG:
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-restore-radar-benchmark.md
RULINGS: 2026-10-24 R2412
WRITE RULING: 2026-10-24 R2412

## ROWS

| row | command | table | count read | expected rows | backup | inverse |
|---|---|---|---|---|---|---|
| P1 | `COBALT_ENV=production uv run cobalt settings load --optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880 --apply` | `user.trader_settings` | `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE key = 'radar.benchmark' AND strpos(source, 'optional:radar-benchmark.yaml') = 1"` | 1 | `COBALT_ENV=production uv run cobalt backup run` | none |

## RECORDS
- What the write does: reloads `radar.benchmark` (value `{top_n: 20, min_move_pct: 10}`, `data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml:2`) over the mirror tombstone. It touches only that key (`reports/survey-restore-prep-2026-10-23.md` Q4). The replay movers step reads `radar.benchmark top_n`.
- DECISION (no dry run): as card `1029`: the hub has no dry-run step and the guard passes only the card's command. The dry run is met by step (3) `count read` BEFORE (expected 0: the source is the vault tombstone), the one `--apply`, and step (5) `count read` AFTER (expected 1). `--apply` needs `--sha256` and a mismatching file writes nothing (`src/cobalt/settings/cli.py:171-172`).
- Source label: an optional load writes `optional:<file name>`, with no digest (`src/cobalt/settings/cli.py:218`).
- The count read names the table as the string literal `'user.trader_settings'` (`ops/desk/desk-launch.sh:2437-2446` wants the whole name); `--side user` pins `search_path` to `"user"`.
- inverse `none`: the rollback is the step (2) backup path the hub writes under `## ROLLBACK`.
- TIME WINDOW: the write is refused 20:00–21:00 ET (`src/cobalt/session/guard.py:7,67`).
- Order: after `1029-restore-cards-enabled-card.md` has ended (`WRITTEN`); one prodwrite seat at a time (`ops/desk/desk-launch.sh:2472`).
