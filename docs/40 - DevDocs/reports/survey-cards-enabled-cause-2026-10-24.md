# SURVEY — why `/radar` still fails `radar.cards_enabled` after the K3 load (2026-10-24)
[surveyed 2026-10-24 22:52–22:54 ET · seat survey-cards-enabled-cause · prompt 1038]

## §0 Headline
- CAUSE: `/radar` replays a stale `failed_stage='evaluate'` stamp on `radar_pool`. The last scan wrote it at 2026-10-23 19:59:22 ET, while the mirror tombstone was still in place. No scan has run since the 21:04:28 K3 load (`market_reset`, then `idle:overnight`).
- CLASS: DATA. The row already holds JSON boolean `true` from source `card:p2-live-settings-htf.yaml@sha256:5993c57f…`, written 21:04:28.496 ET. The next scan clears the stamp, so no reload is needed.
- A K3 reload holds. The mirror re-runs only when a radar note's hash changes (`notes.py:736-744`); a restart does not re-run it.
- RECURRENCE (CODE, latent): any edit to `Radar Screens.md` or `Radar Lists.md` re-runs `_mirror_rows`, which tombstones `radar.cards_enabled` again (`notes.py:711-720`). The 2026-10-21 18:11:54 ET edit of `Radar Lists.md` started this failure.
- `radar.benchmark` shares the past cause and the recurrence risk. It now holds a valid object (`optional:radar-benchmark.yaml`, 21:07:39 ET) and plays no part in the panel error.

## P1 rows
| key | value | vtype | source | updated_et |
|---|---|---|---|---|
| radar.benchmark | `{"top_n": 20, "min_move_pct": "10"}` | object | optional:radar-benchmark.yaml | 2026-10-24 21:07:39.438341 |
| radar.cards_enabled | `true` | boolean | card:p2-live-settings-htf.yaml@sha256:5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17 | 2026-10-24 21:04:28.496454 |

- Both rows were written at or after 21:04:28. Neither carries a `vault:radar-notes@…` source.

## Q2 file line
- `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml:2`: `  radar.cards_enabled: true`.
- Packet copy `prompts/2026-09-20/16-packet/p2-live-settings-htf.yaml:2`: `  radar.cards_enabled: true`. Equal.

## Q3 writer vs reader
| step | file:line | shape |
|---|---|---|
| parse file | `settings/card.py:240-276` (`load_card_file`) | YAML `true` becomes Python `bool`, validated by `from_rows` (`:273`) |
| to rows | `settings/card.py:198-210` (`rows()`, `:201`) | `{radar.cards_enabled: True}`, JSON round-tripped (`:210`) |
| apply | `settings/card.py:320-326` → `settings/cli.py:76`, `:104` `store.put` | — |
| store | `settings/store.py:97`, `:103` | `json.dumps(value)` into `%s::jsonb` = jsonb `true` (P1 vtype boolean) |
| reader | `settings/card.py:236-237` → `:170-196`, field `:149` `cards_enabled: bool` | accepts jsonb `true` |
| /radar route | `aset/web.py:903-913` → `build_radar_panel` `aset/radar_panel.py:949`, `:962` → `build_pool_view` `:536` | — |
| the raise | `aset/radar_panel.py:585-587` | `RadarPanelError(f"FAILED: radar {pool.failed_stage}: {detail}")` from the stored `radar_pool` row; `cards_enabled` is not read on this path |
| stamp writer | `radar/runner.py:431-438` → `radar/store.py:236-261` (`stamp_failure`) | `failed_stage='evaluate'`, `failed_detail=` the CardSettingsError text |
| stamp clear | `radar/runner.py:305`, `:474-475` → `radar/store.py:193-229` (`put_pool`) | the next scan's S2 row writes `failed_stage=None` |

- The loader wrote `true` in a shape the reader accepts. The `load_card` round trip proved it (`card.py:330-336`).
- Changes since 2026-09-20 on the named paths: only the mirror-scope fix `3067e8b9` and port `283389ff` are relevant, and both were reverted (`41bb2402`, `9c7593c0`). Main's `notes.py:711-720` still tombstones every unowned `radar.*` key. The loader, reader and store have no relevant change.

## Q4 timeline
| time ET | event | evidence |
|---|---|---|
| 2026-10-21 18:11:03 | scan starts | `logs/radar.err:90812` |
| 2026-10-21 18:11:54 | `Radar Lists.md` edited | `ls -lT` mtime |
| 2026-10-21 18:13:55 | first `radar.cards_enabled: Input should be a valid boolean` (mirror ran in that cycle, with the new note hash) | `logs/radar.err:90819-90820` |
| 2026-10-23 19:59:22 | last scan; S5 fails; `evaluate` stamped on the pool row | `logs/radar.err:97432-97434` |
| 2026-10-23 20:01:03 → | `paused_market_reset`, then `idle:overnight`; no `scanning` cycle or mirror line on 2026-10-24 | `logs/radar.err:97435-…`; grep on 2026-10-24 found none |
| 2026-10-24 21:04:28 | K3 load writes jsonb `true` | P1 |
| 2026-10-24 21:07:39 | `radar.benchmark` reloaded | P1 |
| 2026-10-24 22:40:51, 22:43:41 | `/radar` replays the stored stamp | `logs/aset.err:20753`, `:20769` |
| 2026-10-24 22:51:35 | radar still `idle:overnight` | `logs/radar.err` tail |

- Next open: the mirror is refused in `market_reset` (`notes.py:732-733`). Outside `market_reset` it returns `unchanged` while both stored note hashes equal the files' hashes (`notes.py:735-744`). The hashes come from the store, not memory, so a restart does not re-run the mirror. The prompt's FACTS line says otherwise and is wrong.
- The 2026-10-21 mirror stored the post-edit hash, so the next scan leaves `true` in place. That scan runs S5 with a valid boolean, and its S2 `put_pool` clears the stamp.
- The next note edit tombstones `true` again until `notes.py:713` is limited to the keys the notes own.
- Not recorded: the time of the next scanning session, and the 2026-10-21 `source`/`updated_at` of the tombstone (overwritten by K3).

## Q5 cause
- CAUSE: `/radar` shows a stale pool-row `evaluate` stamp from the last scan before the K3 load; the stored value is a valid `true`.
- CLASS: DATA. The K3 load of `true` holds with nothing else changed; the stamp clears on the next scan.
- Latent CODE fix, for the desk to decide: `src/cobalt/radar/notes.py:713`. Tombstone only keys the notes own, as the reverted `283389ff` did. The exact owned-key set is not recorded here; take it from `283389ff`.
- `radar.benchmark`: same past cause and same recurrence; not part of the current error.

## DECISIONS
- ASK DESK: card the reverted mirror-scope fix (`notes.py:713`) again before he next edits a radar note? Otherwise the panel error returns. Default taken: none (survey is read-only); flagged for the desk. [22:54]

## RECORDS
- `ls ".../reports/survey-cards-enabled-cause-2026-10-24.md"`: exit 1, absent.
- `date`: exit 0, `Sat Oct 24 22:52:36 EDT 2026`; `date`: exit 0, `Sat Oct 24 22:54:14 EDT 2026`.
- P1, typed once, exit 0: `COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT key, value, jsonb_typeof(value) AS vtype, source, (updated_at AT TIME ZONE 'America/New_York') AS updated_et FROM \"user\".trader_settings WHERE key IN ('radar.cards_enabled', 'radar.benchmark') ORDER BY key"`.
- Read `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml:1-10`; Read `prompts/2026-09-20/16-packet/p2-live-settings-htf.yaml:1-10`.
- `git -C /Users/cobalt/cobalt show main:src/cobalt/settings/card.py`: exit 0.
- `git -C /Users/cobalt/cobalt show main:src/cobalt/radar/notes.py`: exit 0 (read `:690-751`).
- `git -C /Users/cobalt/cobalt grep -n "failed_stage\|failed_detail\|last_scan_at" main -- src/cobalt/aset/radar_panel.py src/cobalt/radar/runner.py src/cobalt/radar/pool.py`: exit 0.
- `git -C /Users/cobalt/cobalt grep -n "screens_note\|lists_note\|notes_dir\|Radar.*\.md" main -- src/cobalt/radar/config.py configs`: exit 0 (`configs/cobalt/radar.yaml:16-17`).
- `git -C /Users/cobalt/cobalt grep -n "def stamp_failure\|def put_pool" main -- src/cobalt/radar`: exit 0.
- `git -C /Users/cobalt/cobalt grep -n "def build_radar_panel\|..." main -- src/cobalt/aset/radar_panel.py`: exit 0.
- `git -C /Users/cobalt/cobalt grep -n "def apply_settings\|store.put(\|json.dumps\|Jsonb\|::jsonb" main -- src/cobalt/settings/cli.py src/cobalt/settings/store.py`: exit 0.
- `git -C /Users/cobalt/cobalt log --since=2026-09-20 ... main -- src/cobalt/settings src/cobalt/aset/radar_panel.py src/cobalt/aset/web.py src/cobalt/radar/notes.py src/cobalt/radar/runner.py`: exit 0.
- Grep `src/` for `radar evaluate|CardSettingsReader|CardSettings\.from_rows|...`; Read working tree `aset/radar_panel.py:555-609`, `aset/web.py:900-914`, `radar/runner.py:300-484`, `radar/store.py:193-262`. The working tree has local changes only under docs and `.claude`, so these files match main.
- `grep -n "cards_enabled" logs/aset.err`: exit 0; Read `logs/aset.err:20660-20773`.
- `ls -lt logs`: exit 0.
- `grep -n "S5 evaluate FAILED" logs/radar.err`: exit 0; `grep -n "cards_enabled: Input should be a valid boolean" logs/radar.err`: exit 0 (first `:90820`, last `:97433`); `tail -n 3` of that result: exit 0.
- `grep -c "radar cycle: scanning" logs/radar.err`: exit 0, 9460; `grep -n "2026-10-24 .*radar cycle: scanning\|2026-10-24 .*mirror" logs/radar.err`: exit 1, none.
- `tail -n 40 logs/radar.err`: exit 0; Read `logs/radar.err:90805-90820`, `:97425-97454`.
- `ls -lT` on both radar notes: exit 0 (`Radar Lists.md` 2026-10-21 18:11:54, `Radar Screens.md` 2026-09-13 11:39:25).
- Times: log lines carry their own ET stamps; P1 `updated_et` is converted in SQL; `date` gives the run times.

SURVEYED · cause: data · decisions: 1
