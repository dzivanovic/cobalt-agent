JOB: restore-cards-enabled
LADDER: OFF-LADDER — reports/cto-2026-10-24.md R2410
CLASS: K3
BRANCH: main
WORKTREE: none
BASE: 1ef351db
TAG:
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-restore-cards-enabled.md
RULINGS: 2026-10-24 R2412
WRITE RULING: 2026-10-24 R2412

## ROWS

| row | command | table | count read | expected rows | backup | inverse |
|---|---|---|---|---|---|---|
| P1 | `COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml --sha256 5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17 --apply` | `user.trader_settings` | `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE key = 'radar.cards_enabled' AND strpos(source, 'card:p2-live-settings-htf.yaml@sha256:5993c57f') = 1"` | 1 | `COBALT_ENV=production uv run cobalt backup run` | none |

## RECORDS
- What the write does: reloads `radar.cards_enabled` (value `true`, `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml:2`) over the mirror tombstone (`vault:radar-notes@8d09a14dd681`, 2026-10-21 18:12:55 ET). The other `card.*` rows stay `=` (`reports/survey-restore-prep-2026-10-23.md` Q4). Use the htf file, not the 09-19 file (it would drop `htf_level_proximity` from `card.curves`).
- DECISION (no dry run): the hub has no dry-run step and runs ONE write per card (`prompts/PRODWRITE-HUB.md:3,43`), and the guard passes only the card's command, so `--dry-run` is not a card row. The dry run is met by the hub's step (3) `count read` BEFORE (expected 0: the key's source is the vault tombstone, not `card:`), then the one `--apply`, then step (5) `count read` AFTER (expected 1). `apply` itself needs `--sha256` and refuses a file whose bytes hash differently (`src/cobalt/settings/cli.py:171-172`), so a wrong file writes nothing.
- Source label: a card load writes `card:<file name>@sha256:<digest>` (`src/cobalt/settings/card.py:324`); the count read matches its first 8 digest hex.
- The count read names the table as the string literal `'user.trader_settings'` in its select list: the launcher requires the whole name `user.trader_settings` in the read (`ops/desk/desk-launch.sh:2437-2446`), and `--side user` pins `search_path` to `"user"`, so the FROM is `trader_settings`.
- inverse `none`: no cobalt command restores the tombstone; the rollback is the step (2) backup path the hub writes under `## ROLLBACK`.
- TIME WINDOW: the write is refused 20:00–21:00 ET (`apply_settings` → `assert_writable`, `src/cobalt/session/guard.py:7,67`). Launch outside it, or after 21:00 ET.
- Order: this card first, then `1030-restore-radar-benchmark-card.md` (one seat at a time, `desk-launch.sh:2472`). Radar cycle clean after both (R2410).
- The vault-note mirror re-tombstones non-note `radar.*` keys on the next radar note edit (`reports/survey-settings-writer-2026-10-23.md:8,54`); the port card `1031` closes that after the restore.
