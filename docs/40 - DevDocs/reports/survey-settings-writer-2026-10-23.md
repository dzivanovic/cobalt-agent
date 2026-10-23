# Survey: who broke "user".trader_settings on 2026-10-21 about 18:13 ET
Seat `survey-settings-writer` (Opus 5.5), prompt `prompts/2026-10-23/1017-survey-settings-writer.md`. Read-only. Times ET: DB `updated_et` from P1/P2; log times from the log line; run times from `date`.

## §0 Headline
- Cause PROVEN: the production radar's vault-note mirror (`mirror_sources` → `_mirror_rows`, `src/cobalt/radar/notes.py:711-720`) rewrote every `radar.*` row absent from the notes as `{"status":"removed",…}` at 18:12:55 ET, triggered by the desk's WBD edit to `Radar Lists.md` (R2343 18:11 ET; file mtime 18:11:54).
- P1: `radar.cards_enabled` and `radar.benchmark` both type `object`, raw `{"block": null, "error": null, "status": "removed", "note_sha256": null, "block_sha256": null}`, updated 2026-10-21 18:12:55.649090 ET, source `vault:radar-notes@8d09a14dd681`.
- Replay key holds no `top_n` (P1); last replay DONE 10-16 21:26:44, first `top_n` fail 10-21 21:10:04.
- HIT ON HIS REAL SETTINGS: both keys hold the mirror tombstone, not his values; same transaction rewrote `radar.list.tier_a/b/c` and `radar.note.lists`. A restore stays exposed: the next edit of either radar note re-tombstones every non-note `radar.*` key.

## Q1 values
| read | key | type | raw | updated_et | source |
|---|---|---|---|---|---|
| P1 | radar.benchmark | object | `{"block": null, "error": null, "status": "removed", "note_sha256": null, "block_sha256": null}` | 2026-10-21 18:12:55.649090 | vault:radar-notes@8d09a14dd681 (kind `vault:`) |
| P1 | radar.cards_enabled | object | same as above | 2026-10-21 18:12:55.649090 | vault:radar-notes@8d09a14dd681 (kind `vault:`) |
| P3 | history/audit tables | — | only `user.trader_settings` matches; no history or audit table | — | — |

Same `updated_at` second (P2, one transaction, 18:12:55.649090): `radar.note.lists`, `radar.cards_enabled`, `radar.benchmark`, `radar.list.tier_a`, `radar.list.tier_b`, `radar.list.tier_c`. `radar.note.screens` and `radar.screen.*`/`radar.pool` stay at 2026-09-14 04:01:14 (same label). The label `@8d09a14dd681` is the Screens note hash (`notes.py:746` takes screens first), so it hides that the Lists note changed.

## Q2 writers
| writer | file:line | source label | keys | ran 17:30-18:15 | line that says so |
|---|---|---|---|---|---|
| vault-note mirror (radar S3, every cycle; skips only when both note hashes are unchanged `notes.py:736-744`) | `src/cobalt/radar/notes.py:747` from `radar/runner.py:320` | `vault:radar-notes@<hash12>` (`:749`) | `radar.note.*`, `radar.<block key>`, AND any existing `radar.*` key not in the notes as `removed` (`:711-720`) | y | P2 18:12:55.649; `radar.err:90813-90818` cycle 18:12:55; `radar.err:90819` first fail 18:13:55 |
| `apply_settings` via `settings load --from/--from-git` | `src/cobalt/settings/cli.py:317` (put `:104`) | loader label (`yaml:…`, `git:…`) | any | n | no `settings applied`/`settings load` line 17:00-18:59 in radar, replay, heartbeat, prefill-drc, daymode-propose, cos logs (count 0 each) |
| `settings load --optional` | `cli.py:237` | loader label | optional keys | n | same |
| `settings load --card` | `src/cobalt/settings/card.py:322` | `card:<file>@sha256:<digest>` | card keys; deletes keys the file omits | n | same; P2 newest `card:` row 09-20 |
| ASET change line | `src/cobalt/aset/web.py:1365` | `aset.change_line@sha256:<hash>` | change-line keys | n | no `settings` line in aset.log/aset.err 17:00-18:59; P2 newest 09-30 |
| migration seed | `src/cobalt/db_migrations/0004_radar_pool.sql:73` | `db_migration:0004` | `aset.account_mode` | n | P2 09-12 |

No other writer: grep of `src/ ops/ scripts/` for `.put(` on a settings store hits only `cli.py:104` and `notes.py:747`; SQL writers only `0004_radar_pool.sql:73` and its rollback `:12`. Window rows (`reports/cto-2026-10-21.md`): R2335 17:27, R2336 17:27, R2337 17:32, R2338 17:35, R2339 17:38, R2340 17:38, R2341 18:03, R2342 18:05, R2343 18:11 (WBD removed from `Radar Lists.md:238`).

## Q3 paths
| path | file:line | env | root | verdict |
|---|---|---|---|---|
| prod radar daemon mirror after a vault note edit | `notes.py:711-720`, `runner.py:320` | production | /Users/cobalt/Vault/Think | proven (P2 18:12:55 + radar.err:90813-90819 + note mtime 18:11:54 + R2343) |
| deploy smoke | `ops/desk/deploy-smoke.sh:44,202` | production | — | ruled out: `db query` only, SELECT/WITH only (`db_query.py:98-103`) |
| deploy step C dry run | `ops/desk/deploy-step-c.sh:106` | production `--dry-run` | — | ruled out: dry run; no `settings load` or `/settings/daily/apply` in `ops/desk` (git grep 0 hits) |
| gate.sh, house-probe.sh, devdb-copy-env.sh | no `COBALT_ENV=` line | — | — | ruled out for this write: no settings writer in them; label and time match the mirror |

F5 gate pass 3 report and card 1000 not read: rule (a) settles the cause.

## Q4 replay
- P1: `radar.benchmark` holds no `top_n`; tombstone since 2026-10-21 18:12:55 ET; writer the vault-note mirror.
- `replay.err:825` last DONE 2026-10-16 21:26:44; `:827`,`:830` 10-19/10-20 failed on archiver; `:833-836` first `top_n` fail 2026-10-21 21:10:04 (`input_value={'block': None, …}`); `:926` 10-22 same.

## Values before and after
| key | before 18:12:55 | after |
|---|---|---|
| radar.cards_enabled | not recorded (a valid boolean: no `valid boolean` error before `radar.err:90820`) | tombstone object (P1) |
| radar.benchmark | not recorded (held `top_n`: replay DONE 10-16) | tombstone object (P1) |

Restore (his; run nothing): `cards_enabled` is a card key → `cobalt settings load --card <reviewed card file> --sha256 <hash> --apply` (the card path deletes keys the file omits, `card.py:296-303`); `radar.benchmark` → `cobalt settings load --optional <reviewed file> --sha256 <hash> --apply` (form named by the 09-21 replay error, `replay.err:3`). Either lasts only until the next radar note edit.

## DECISIONS
- ASK DESK: the mirror tombstones every non-note `radar.*` key on any note edit (`notes.py:712-713`); a code fix (restrict to `radar.note.*`/note block keys) and holding radar note edits until it lands are the desk's call. Default taken: reported only, no code. [08:21]

## RECORDS
- `date` → Fri Oct 23 08:20:07 EDT 2026 (exit 0); `ls` report → absent (exit 1).
- P1 (exit 0): `COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT key, jsonb_typeof(value) AS vtype, value::text AS raw, source, updated_at, (updated_at AT TIME ZONE 'America/New_York') AS updated_et FROM \"user\".trader_settings WHERE key IN ('radar.cards_enabled', 'radar.benchmark') ORDER BY key"`
- P2 (exit 0): `COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT key, jsonb_typeof(value) AS vtype, source, (updated_at AT TIME ZONE 'America/New_York') AS updated_et FROM \"user\".trader_settings ORDER BY updated_at DESC LIMIT 60"` → 25 rows.
- P3 (exit 0): `COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema IN ('user', 'system') AND (strpos(table_name, 'setting') > 0 OR strpos(table_name, 'audit') > 0 OR strpos(table_name, 'history') > 0) ORDER BY 1, 2"` → 1 row.
- Read `notes.py:660-762`, `runner.py:295-334`; `git log -L 711,721:notes.py` → b771fab8 (09-12), 23606f7e (09-10).
- `grep -n "valid boolean" logs/radar.err` → first 90820; read `radar.err:90800-90821`.
- `ls -lT` Radar Lists.md → Oct 21 18:11:54; Radar Screens.md → Sep 13 11:39:25.
- `grep` cto-2026-10-21.md R2335-R2343 (exit 0); `configs/cobalt/radar.yaml:16-17` note paths.
- Grep `src/` `.put(` → `cli.py:104`, `notes.py:747`; `apply_settings(` → `cli.py:237,317`, `card.py:322`, `web.py:1365`; SQL writers → `0004_radar_pool.sql:73`, rollback `:12`.
- `grep` aset.log/aset.err 10-21 17-18h `settings` → none (exit 1); `grep -c` six other logs → 0 each.
- `grep` replay.err status lines (exit 0); replay.log no `com.cobalt.replay` lines (exit 1).
- `git grep COBALT_ENV=` desk scripts → deploy-smoke.sh:14,44,202, deploy-step-c.sh:106; `git grep` settings load / settings/daily/apply in ops/desk → none (exit 1).
- `date` → Fri Oct 23 08:21:36 EDT 2026.

SURVEYED · cause: prod radar vault-note mirror (notes.py:711-720) tombstoned radar.cards_enabled and radar.benchmark at 10-21 18:12:55 ET after the R2343 Radar Lists.md WBD edit · decisions: 1
