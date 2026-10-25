# prodwrite-restore-cards-enabled — 2026-10-24

## §0 Headline
WRITTEN. `radar.cards_enabled` was reloaded to `true` from `p2-live-settings-htf.yaml` (sha256 5993c57f…), under ruling 2026-10-24 R2412.
Backup first: ssd snapshot `51d3a10f`. Count before 0, after 1, expected 1.
The three `card.*` keys came back `unchanged`, and the round trip was `EQUAL`. One observation is under DECISIONS, FOR DEJAN.
Next: card `1030-restore-radar-benchmark-card.md`.

## L74
none

## AUTHORIZATION
21:02:34 EDT (`date`: `Sat Oct 24 21:02:34 EDT 2026`)
rule (0) · `sh /Users/cobalt/cobalt/ops/desk/authorize.sh prodwrite "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1029-restore-cards-enabled-card.md"` · exit 0 · output:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1029-restore-cards-enabled-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1029-restore-cards-enabled-card.md" · 0 · 9c493c240e8b895ef5458f6f9e633c14847340e6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1029-restore-cards-enabled-card.md" · 0 · nothing
STANDING LIST 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
STANDING LIST 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
STANDING LIST 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
RULING 2026-10-24 R2412 row · grep -n "^| R2412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 12:| R2412 | 19:55 ET | HIS RULING · APPROVED (brain relay, 10-14 item 5, reports/brain-direction-2026-10-02.md:262): Dejan said "Restore yes" (2026-10-24) to reload radar.cards_enabled = true (htf card, sha256 5993c57f…) and radar.benchmark {top_n 20, min_move_pct 10} (sha256 10aef996…). | APPROVED |
RULING 2026-10-24 R2412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 1ef351dbd7c087b253b0c6f3e2101672feac870b
RULING 2026-10-24 R2412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · the row as grepped
WRITE RULING 2026-10-24 R2412 row · grep -n "^| R2412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 12:| R2412 | 19:55 ET | HIS RULING · APPROVED (brain relay, 10-14 item 5, reports/brain-direction-2026-10-02.md:262): Dejan said "Restore yes" (2026-10-24) to reload radar.cards_enabled = true (htf card, sha256 5993c57f…) and radar.benchmark {top_n 20, min_move_pct 10} (sha256 10aef996…). | APPROVED |
WRITE RULING 2026-10-24 R2412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · 1ef351dbd7c087b253b0c6f3e2101672feac870b
WRITE RULING 2026-10-24 R2412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-24.md" · 0 · the row as grepped
AUTHORIZED
```

## SHAPE
- rule (1) row · card `## ROWS` re-read with Read (card line 16): one data row P1, seven cells. `command` starts `COBALT_ENV=production uv run cobalt `, verb `settings load`, holds none of the refused characters, no `--rollback`/`--down-to` word; `table` `user.trader_settings`; `count read` starts `COBALT_ENV=production uv run cobalt db query --side `, holds ` --prod `, names `user.trader_settings`, no `%` `$` backtick; `expected rows` `1`; `backup` `COBALT_ENV=production uv run cobalt backup run`; `inverse` `none`. Not a `db apply` command. PASS.
- rule (1) code · `git -C /Users/cobalt/cobalt diff --stat 1ef351db HEAD -- . ':(exclude)docs'` · exit 0 · output: (nothing). PASS.

## BACKUP
- rule (2) status · `COBALT_ENV=production uv run cobalt backup status` · exit 0 · output:
```
forget policy: daily 14 / weekly 8 / monthly 12
sources      : /Users/cobalt/Vault/Think, /Users/cobalt/cobalt/data/.cobalt_vault
database     : cobalt_brain
  ssd   local ARMED /Volumes/COBALT-BACKUP/restic
  b2    b2    off   (no repo configured)

newest snapshot: 1.3 h old
```
- rule (2) run · `COBALT_ENV=production uv run cobalt backup run` · exit 0 · output:
```
2026-10-24 21:02:51.846 | INFO     | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.backup RUNNING (timeout 3600s, heartbeat every 1200s)
2026-10-24 21:03:37.071 | INFO     | cobalt.backup.pgdump:dump_database_to:113 - backup: cobalt_brain via pg_dump inside cobalt_memory — 10246.8 MB
2026-10-24 21:03:37.076 | INFO     | cobalt.backup.restic:snapshot:246 - backup: cobalt_brain dumped, 10246.8 MB
2026-10-24 21:03:58.276 | INFO     | cobalt.backup.restic:_snapshot_one:300 - backup: ssd: snapshot 51d3a10f — 0 new / 1 changed, 28.7 MB added, 1 pruned
2026-10-24 21:03:58.457 | INFO     | cobalt.jobs.wrapper:job_run:199 - F17: com.cobalt.backup DONE
ssd: snapshot 51d3a10f — 0 new / 1 changed, 28.7 MB added, 1 pruned
```
- `<path>` = `ssd/51d3a10f`

## ROLLBACK
- backup: ssd/51d3a10f
- inverse: none

## COUNT BEFORE
rule (3) · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE key = 'radar.cards_enabled' AND strpos(source, 'card:p2-live-settings-htf.yaml@sha256:5993c57f') = 1"` · exit 0 · output:
```
tbl	n
user.trader_settings	0
```
`<a>` = 0

## WRITE
rule (4) · typed once, foreground · `date` before: `Sat Oct 24 21:04:25 EDT 2026` · `date` after: `Sat Oct 24 21:04:28 EDT 2026`
`COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml --sha256 5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17 --apply` · exit 0 · output:
```
2026-10-24 21:04:28.495 | INFO     | cobalt.settings.cli:apply_settings:113 - settings applied: keys ['card.curves', 'card.proposed_key', 'card.shadow_promotion_bar', 'radar.cards_enabled'] · deleted [] · source card:p2-live-settings-htf.yaml · at 2026-10-25T01:04:28+00:00
cobalt settings load --card — APPLY /Users/cobalt/cobalt/data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml
sha256 5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17

  ~ radar.cards_enabled
      db  : {"block": null, "block_sha256": null, "error": null, "note_sha256": null, "status": "removed"}
      file: true
  = card.proposed_key
  = card.curves
  = card.shadow_promotion_bar

applied: {'radar.cards_enabled': 'updated', 'card.proposed_key': 'unchanged', 'card.curves': 'unchanged', 'card.shadow_promotion_bar': 'unchanged'}; deleted: []
round trip: CardSettings.from_rows(db) == reviewed file — EQUAL.
```

## VERIFY
rule (5) · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE key = 'radar.cards_enabled' AND strpos(source, 'card:p2-live-settings-htf.yaml@sha256:5993c57f') = 1"` · exit 0 · output (`date`: `Sat Oct 24 21:04:35 EDT 2026`):
```
tbl	n
user.trader_settings	1
```
`<b>` = 1 = `expected rows` 1. PASS.

## DECISIONS
- FOR DEJAN (observation, no action taken): the write's INFO line lists all four keys under `settings applied: keys [...]`, while its `applied:` line marks only `radar.cards_enabled` as `updated` and the three `card.*` keys as `unchanged`. The card expected the `card.*` rows to stay `=` (card RECORDS line 19), and the diff shows `=` for each. This seat did not read whether the three `unchanged` rows had their `source` or timestamp rewritten. The only read on the list is the card's count read, so that check was not run. Safe default: nothing more was run. If it matters, the desk can check with a read of `source` for the `card.*` keys.
- Window: the write ran at 21:04:25 EDT, after the 20:00–21:00 ET refusal window (card RECORDS line 24).

## RECORDS
- Card `## RECORDS` as read (card lines 18–26): what the write does (reload `radar.cards_enabled` = `true` from the htf file over the mirror tombstone `vault:radar-notes@8d09a14dd681`; other `card.*` rows stay `=`); DECISION (no dry run: step (3) count before = 0, one `--apply`, step (5) count after = 1; `--sha256` refuses a mismatched file); source label `card:<file name>@sha256:<digest>`; count read names the table as a string literal, `--side user` pins `search_path`; inverse `none` (rollback is the step (2) backup); TIME WINDOW 20:00–21:00 ET refused; order: this card first, then `1030-restore-radar-benchmark-card.md`; the vault-note mirror re-tombstones non-note `radar.*` keys on the next radar note edit, and port card `1031` closes that.
- Refused calls: none.
- `CONTINUE` messages received: none.
- L74 line: none arrived in a tool result.

WRITTEN · job: restore-cards-enabled · rows: 1 · backup: ssd/51d3a10f
