JOB: daymode-enabled-modes
LADDER: OFF-LADDER — reports/cto-2026-10-29.md R2563
CLASS: K3
BRANCH: main
WORKTREE: none
BASE: «FILL: 8-hex commit on main at launch; no code past it»
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-daymode-enabled-modes.md
RULINGS: «FILL: the desk's rows binding this job»
WRITE RULING: 2026-10-29 R2563

## ROWS

| row | command | table | count read | expected rows | backup | inverse |
|---|---|---|---|---|---|---|
| P1 | `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward --apply` | `user.trader_settings` | `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE source = 'yaml:/Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward'"` | 1 | `COBALT_ENV=production uv run cobalt backup run` | `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/rollback --apply` |

## NOT IN THIS JOB
- Any key but `daymode.enabled_modes`: `aset.enabled_grades`, `aset.sheet_modes`, `daymode.reduced_sheet`, `daymode.reduced_enabled_grades`, `daymode.hotkey_file_template`, `daymode.stepdowns` stay byte-equal to production.
- A hand edit of `"user".trader_settings` (`db apply`, SQL, psql); the one route is `cobalt settings load` (`src/cobalt/settings/cli.py:1-8`).
- The two YAML files in git: they never return to `configs/cobalt/` (`bd25d471d`, L32); they live under `data/` (git-ignored, `.gitignore:6`).
- The sheet check (`src/cobalt/daymode/match.py`): card 1082.
- The 20:00–21:00 ET window: the apply is refused there (`src/cobalt/settings/cli.py:88-100`, `assert_writable`).

## READ
- `src/cobalt/settings/cli.py:249-330` `cmd_load` (the `--from` route, its diff print, its round trip); `:283` the source label `yaml:<dir>`.
- `src/cobalt/settings/models.py:33-48` (`DAYMODE_KEYS`, `SETTING_KEYS`, the two file names), `:349-386` `rows_from_yaml` (the two files' shape: `aset.yaml` top key `sheet_modes` holding `enabled_grades`; `daymode.yaml` top key `daymode` holding the five keys).
- `src/cobalt/settings/store.py:83-104` `put` (an unchanged key is skipped, `:90-92`: its `source` and `updated_at` stay).
- `src/cobalt/daymode/config.py:178-185` (`lowest_enabled`, `highest_enabled`), `:284-289` (an unknown mode refused).

## RECORDS
- THE ROUTE (drafter, from the code): `settings load --from <dir>` reads `aset.yaml` and `daymode.yaml` from `<dir>` (`models.py:358-361`) and writes all seven `SETTING_KEYS` (`cli.py:297-317`); a key equal to the database is skipped (`store.py:90-92`). `--from-git` has no source: `bd25d471d^` holds `enabled_modes: [reduced]` and no `trade_count_over_band` row, which `config.py:265-271` refuses.
- THE FILES (made by the desk before launch, outside the repo): from ONE production read of the seven rows, `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT key, value::text AS v FROM trader_settings WHERE key IN ('aset.sheet_modes', 'aset.enabled_grades', 'daymode.reduced_sheet', 'daymode.reduced_enabled_grades', 'daymode.enabled_modes', 'daymode.hotkey_file_template', 'daymode.stepdowns') ORDER BY key"`, in the shape of `data/backups/pre-stack-0919/daymode-settings-rollback/{aset,daymode}.yaml`. `…/daymode-open-2026-10-29/rollback/` = production's values. `…/forward/` = the same, but `enabled_modes: [reduced, half, full]`. Those 09-19 files are a shape only: the ASET change line writes `aset.sheet_modes` (`src/cobalt/settings/drc.py:151-160`), and `daymode.stepdowns` gained `trade_count_over_band` on 09-19 (`reports/deploy-2026-09-19.md:145`).
- «FILL: the production read above, time and output whole»
- «FILL: `shasum -a 256` of the four files, with time»
- GATE 1 «FILL: `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward --dry-run`, whole: six `=` lines, ONE `~ daymode.enabled_modes` (db `["reduced"]`, file `["reduced", "half", "full"]`), `DRY RUN — 1 setting(s) would change. Nothing written.` (`cli.py:313`)»
- GATE 2 «FILL: the same with `…/rollback --dry-run`, whole: seven `=` lines, `no differences — the database already holds these settings.` (`cli.py:309`)»
- No launch unless GATE 1 and GATE 2 read as above (the hub has no dry-run step; the guard passes only the card's command).
- THE COUNT: only the changed key takes the source `yaml:<forward dir>` (`cli.py:283`, `store.py:90-92`): before 0, after 1. An after above 1 = a second key moved: FAILED verify, backup path in `## ROLLBACK`. The WRITE output's `applied:` line (`cli.py:320`) names `aset.enabled_grades: unchanged`.
- THE EFFECT: stage 1 stays `reduced`, the lowest enabled (`config.py:178`); the 09:00 proposal may climb to `full`, the highest enabled (`config.py:181-182`; `propose.py:58-61` clamp). The ladder is `reduced < half < full` (`config.py:156-158`, `aset.sheet_modes.order [half, full]`).
- RESTARTS: none. The runtime reads the rows on every call (`config.py:309-326` → `TraderSettings.from_db`); no cache in `src/cobalt/settings/` or `src/cobalt/daymode/` (git grep `cache`: one hit, `settings/card.py:231` "no cache").
- HITL: a trading-logic change of his own sheet (L7). His ruling R2563 (`cto-2026-10-29.md:10`, HIS RULING · APPROVED) names it; the files are pinned by GATE 1, GATE 2 and the four sha256 above.
- Order: independent of card 1082; one prodwrite seat at a time.
