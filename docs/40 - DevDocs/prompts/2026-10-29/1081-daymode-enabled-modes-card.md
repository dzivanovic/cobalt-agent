JOB: daymode-enabled-modes
LADDER: OFF-LADDER — reports/cto-2026-10-29.md R2563
CLASS: K3
BRANCH: main
WORKTREE: none
BASE: 1903c47f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-daymode-enabled-modes.md
RULINGS: 2026-10-29 R2563
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
- THE READ (desk, 2026-10-29, R686 `cto-2026-10-08.md:39`; query of the line above): seven rows. Desk compared the four YAMLs line by line against it. Rollback = production's values; forward = the same with `daymode.enabled_modes: [reduced, half, full]`. No other key differs.
- sha256 (taken 2026-10-29): forward/aset.yaml `50278015d5f4237233aca170f0eef6ef0a1509c46ac67c1fe06c6f342a6077db`; forward/daymode.yaml `0b351b94a378270e1f622d5c6be62f8845034ec9c63b12e2f08b9bc359e0493f`; rollback/aset.yaml `50278015d5f4237233aca170f0eef6ef0a1509c46ac67c1fe06c6f342a6077db`; rollback/daymode.yaml `e124a28cc508617568f1369eae0c7d950feb981d6387b6fb1a6bb4156969bab6`.
- NO DRY-RUN GATE: `bare-guard.py:1099-1105` admits the prodwrite seat only the card's ONE command, the two backup strings and the one `db query` read. Route (b), ruled R2580: bare `--from <forward> --apply`; `--sha256` is refused with `--from` (`cli.py:268-271`). The pin is the four sha256 above.
- DESK PRE-LAUNCH: `shasum -a 256` of the four files equals the four above; any difference: no launch.
- PROVEN (`git show main:<path>`): `--from --apply` touches ONLY the seven keys of the dir and deletes nothing. `cmd_load` builds `rows` from `TraderSettings.rows_from_yaml` (`cli.py:284`), which returns exactly the seven `SETTING_KEYS` (`models.py:376-385`), and calls `apply_settings(rows, source=source_label, store=store)` with no `delete` (`cli.py:317`); `apply_settings` passes `delete` to `put` only when non-empty (`cli.py:102-104`); `put` upserts the keys in `rows`, skips a key equal to the database (`store.py:89-104`, `:90-92`) and deletes only keys named in `delete` (`store.py:105-108`). The card-file omitted-key deletion (`card.py:296-303`) is the `--card` route, not this one.
- SEAT STEPS: (1) `backup run` (the row's backup cell); (2) the row's count read, expected 0; (3) the ONE command; (4) the count read again, expected 1; (5) read-back: the one admitted `db query` of the seven rows, the query of the READ line with `updated_at` added to the selected columns (the guard checks the command's words, not its SQL: `bare-guard.py:996-1018`), matched against the forward YAML: six values unchanged, `daymode.enabled_modes` = `["reduced","half","full"]`. The report lists every key whose `updated_at` or `source` moved; only `daymode.enabled_modes` may. Any other output: FAILED, nothing more written, backup path in `## ROLLBACK`.
- THE COUNT: only the changed key takes the source `yaml:<forward dir>` (`cli.py:283`, `store.py:90-92`): before 0, after 1. An after above 1 = a second key moved: FAILED verify, backup path in `## ROLLBACK`. The WRITE output's `applied:` line (`cli.py:320`) names `aset.enabled_grades: unchanged`.
- THE EFFECT: stage 1 stays `reduced`, the lowest enabled (`config.py:178`); the 09:00 proposal may climb to `full`, the highest enabled (`config.py:181-182`; `propose.py:58-61` clamp). The ladder is `reduced < half < full` (`config.py:156-158`, `aset.sheet_modes.order [half, full]`).
- RESTARTS: none. The runtime reads the rows on every call (`config.py:309-326` → `TraderSettings.from_db`); no cache in `src/cobalt/settings/` or `src/cobalt/daymode/` (git grep `cache`: one hit, `settings/card.py:231` "no cache").
- HITL: a trading-logic change of his own sheet (L7). His ruling R2563 (`cto-2026-10-29.md`, `grep -n "^| R2563 "`, HIS RULING · APPROVED) names it, the read is R686 (`cto-2026-10-08.md:39`); the files are pinned by the four sha256 above.
- Order: independent of card 1082; one prodwrite seat at a time.

## ROLLBACK
- The backup path the seat's `backup run` prints.
- Second one-command card, READY and NOT RUN unless his settings read wrong: `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/rollback --apply` (the P1 inverse cell).
