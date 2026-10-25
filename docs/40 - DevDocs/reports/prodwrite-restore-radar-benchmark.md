# prodwrite-restore-radar-benchmark

CARD: `docs/40 - DevDocs/prompts/2026-10-23/1030-restore-radar-benchmark-card.md` · JOB: restore-radar-benchmark · started `Sat Oct 24 21:05:42 EDT 2026`

## §0 Headline
WRITTEN. `radar.benchmark` is back in production `user.trader_settings` with source `optional:radar-benchmark.yaml`. The row count went from 0 to 1, as the card expected.
I took backup `ssd/7870db8b` before the write and ran the write once, at 21:07:39 ET. The file's sha256 matched `10aef996…`.
One observation for Dejan is under DECISIONS: `min_move_pct` loaded as the string `"10"`.

## L74
none

## AUTHORIZATION
rule (0) · `sh /Users/cobalt/cobalt/ops/desk/authorize.sh prodwrite "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1030-restore-radar-benchmark-card.md"` · exit 0 · output verbatim:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1030-restore-radar-benchmark-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1030-restore-radar-benchmark-card.md" · 0 · 9c493c240e8b895ef5458f6f9e633c14847340e6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1030-restore-radar-benchmark-card.md" · 0 · nothing
STANDING LIST 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
STANDING LIST 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
STANDING LIST 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
RULING 2026-10-24 R2412 row · grep -n "^| R2412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 13:| R2412 | 19:55 ET | HIS RULING · APPROVED (brain relay, 10-14 item 5, reports/brain-direction-2026-10-02.md:262): Dejan said "Restore yes" (2026-10-24) to reload radar.cards_enabled = true (htf card, sha256 5993c57f…) and radar.benchmark {top_n 20, min_move_pct 10} (sha256 10aef996…). | APPROVED |
RULING 2026-10-24 R2412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 1ef351dbd7c087b253b0c6f3e2101672feac870b
RULING 2026-10-24 R2412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · the row as grepped
WRITE RULING 2026-10-24 R2412 row · grep -n "^| R2412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 13:| R2412 | 19:55 ET | HIS RULING · APPROVED (brain relay, 10-14 item 5, reports/brain-direction-2026-10-02.md:262): Dejan said "Restore yes" (2026-10-24) to reload radar.cards_enabled = true (htf card, sha256 5993c57f…) and radar.benchmark {top_n 20, min_move_pct 10} (sha256 10aef996…). | APPROVED |
WRITE RULING 2026-10-24 R2412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 1ef351dbd7c087b253b0c6f3e2101672feac870b
WRITE RULING 2026-10-24 R2412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · the row as grepped
AUTHORIZED
```

## SHAPE
- rule (1) row · Read card lines 12-16 · one data row `P1`, seven cells. `command` starts `COBALT_ENV=production uv run cobalt `, verb `settings load`, holds none of `"` `'` `\` `$` backtick `|` `&` `;` `<` `>` `*` `?` `%` `#`, no `--rollback` / `--down-to` word; not a `db apply`. `table` `user.trader_settings`. `count read` starts `COBALT_ENV=production uv run cobalt db query --side `, holds ` --prod `, names `user.trader_settings`, holds no `%`, `$` or backtick. `expected rows` `1` (digits). `backup` exactly `COBALT_ENV=production uv run cobalt backup run`. `inverse` `none`. → pass.
- rule (1) code · `git -C /Users/cobalt/cobalt diff --stat 1ef351db HEAD -- . ':(exclude)docs'` · exit 0 · output: nothing → pass.

## BACKUP
- rule (2) status · `COBALT_ENV=production uv run cobalt backup status` · exit 0 · output verbatim:
```
forget policy: daily 14 / weekly 8 / monthly 12
sources      : /Users/cobalt/Vault/Think, /Users/cobalt/cobalt/data/.cobalt_vault
database     : cobalt_brain
  ssd   local ARMED /Volumes/COBALT-BACKUP/restic
  b2    b2    off   (no repo configured)

newest snapshot: 0.0 h old
```
- rule (2) run · `COBALT_ENV=production uv run cobalt backup run` · exit 0 · output verbatim:
```
2026-10-24 21:06:03.154 | INFO     | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.backup RUNNING (timeout 3600s, heartbeat every 1200s)
2026-10-24 21:06:48.604 | INFO     | cobalt.backup.pgdump:dump_database_to:113 - backup: cobalt_brain via pg_dump inside cobalt_memory — 10246.8 MB
2026-10-24 21:06:48.608 | INFO     | cobalt.backup.restic:snapshot:246 - backup: cobalt_brain dumped, 10246.8 MB
2026-10-24 21:07:09.375 | INFO     | cobalt.backup.restic:_snapshot_one:300 - backup: ssd: snapshot 7870db8b — 0 new / 1 changed, 37.1 MB added, 1 pruned
2026-10-24 21:07:09.541 | INFO     | cobalt.jobs.wrapper:job_run:199 - F17: com.cobalt.backup DONE
ssd: snapshot 7870db8b — 0 new / 1 changed, 37.1 MB added, 1 pruned
```
- path: `ssd/7870db8b`

## ROLLBACK
backup: ssd/7870db8b
inverse: none

## COUNT BEFORE
rule (3) · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE key = 'radar.benchmark' AND strpos(source, 'optional:radar-benchmark.yaml') = 1"` · exit 0 · output verbatim:
```
tbl	n
user.trader_settings	0
```
a = 0

## WRITE
rule (4) · before: `Sat Oct 24 21:07:36 EDT 2026` · `COBALT_ENV=production uv run cobalt settings load --optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880 --apply` · exit 0 · typed once · output verbatim:
```
2026-10-24 21:07:39.443 | INFO     | cobalt.settings.cli:apply_settings:113 - settings applied: keys ['radar.benchmark'] · deleted [] · source optional:radar-benchmark.yaml · at 2026-10-25T01:07:39+00:00
cobalt settings load — APPLY from optional:radar-benchmark.yaml

  ~ radar.benchmark
      db  : {"block": null, "block_sha256": null, "error": null, "note_sha256": null, "status": "removed"}
      file: {"min_move_pct": "10", "top_n": 20}

applied: {'radar.benchmark': 'updated'} (sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880)
round trip: database == file, every optional key re-validates.
```
after: `Sat Oct 24 21:07:41 EDT 2026`

## VERIFY
rule (5) · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE key = 'radar.benchmark' AND strpos(source, 'optional:radar-benchmark.yaml') = 1"` · exit 0 · output verbatim:
```
tbl	n
user.trader_settings	1
```
b = 1 = expected rows 1 → pass.

## DECISIONS
- FOR DEJAN (observation, no action taken): the write output prints the file value as `{"min_move_pct": "10", "top_n": 20}`, so `min_move_pct` is the string `"10"` and `top_n` is the integer `20`. The tool says `every optional key re-validates`. The card describes the value as `{top_n: 20, min_move_pct: 10}`. Whether the replay movers step reads a string `min_move_pct` correctly is for the desk to check. This seat ran nothing about it.

## RECORDS
- Card `## RECORDS` as read:
  - What the write does: reloads `radar.benchmark` (value `{top_n: 20, min_move_pct: 10}`, `data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml:2`) over the mirror tombstone. It touches only that key (`reports/survey-restore-prep-2026-10-23.md` Q4). The replay movers step reads `radar.benchmark top_n`.
  - DECISION (no dry run): as card `1029`: the hub has no dry-run step and the guard passes only the card's command. The dry run is met by step (3) `count read` BEFORE (expected 0: the source is the vault tombstone), the one `--apply`, and step (5) `count read` AFTER (expected 1). `--apply` needs `--sha256` and a mismatching file writes nothing (`src/cobalt/settings/cli.py:171-172`).
  - Source label: an optional load writes `optional:<file name>`, with no digest (`src/cobalt/settings/cli.py:218`).
  - The count read names the table as the string literal `'user.trader_settings'` (`ops/desk/desk-launch.sh:2437-2446` wants the whole name); `--side user` pins `search_path` to `"user"`.
  - inverse `none`: the rollback is the step (2) backup path the hub writes under `## ROLLBACK`.
  - TIME WINDOW: the write is refused 20:00–21:00 ET (`src/cobalt/session/guard.py:7,67`).
  - Order: after `1029-restore-cards-enabled-card.md` has ended (`WRITTEN`); one prodwrite seat at a time (`ops/desk/desk-launch.sh:2472`).
- Time window: the write ran at 21:07:39 ET (`date` 21:07:36 before), outside 20:00–21:00 ET.
- Refused calls: none.
- CONTINUE messages received: none.
- L74: none.

WRITTEN · job: restore-radar-benchmark · rows: 1 · backup: ssd/7870db8b
