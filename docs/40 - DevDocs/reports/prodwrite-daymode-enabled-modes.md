# prodwrite-daymode-enabled-modes — card 1081 (P1)

## §0 Headline
WRITTEN: `daymode.enabled_modes` `["reduced"]` → `["reduced","half","full"]`; six keys unchanged; count 0 → 1 (expected 1); backup `ssd/534339ca`. Stray file to delete: DECISIONS 2. (Full headline above the stop line.)

## L74
none

## AUTHORIZATION
rule (0) · `sh /Users/cobalt/cobalt/ops/desk/authorize.sh prodwrite "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1081-daymode-enabled-modes-card.md"` · exit 0 · 2026-10-29 ~19:06 EDT
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1081-daymode-enabled-modes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-29/1081-daymode-enabled-modes-card.md" · 0 · d8ee9cd2807aabe62abd1b437079d56beee77bbf
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-29/1081-daymode-enabled-modes-card.md" · 0 · nothing
STANDING LIST 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
STANDING LIST 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
STANDING LIST 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
RULING 2026-10-29 R2563 row · grep -n "^| R2563 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · 28:| R2563 | 11:05 ET | HIS RULING · APPROVED ("enable everything I need to use. I want all enabled"): all day modes enabled; desk reading: sheet check warns, never refuses (A). Drafter prompt 1080 → cards 1081, 1082. | APPROVED — pending fold |
RULING 2026-10-29 R2563 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2563 |" -- "docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · 868d51c0f73ee71ddee4b9c91c1ea85ce0a3c808
RULING 2026-10-29 R2563 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · the row as grepped
WRITE RULING 2026-10-29 R2563 row · grep -n "^| R2563 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · 28:| R2563 | 11:05 ET | HIS RULING · APPROVED ("enable everything I need to use. I want all enabled"): all day modes enabled; desk reading: sheet check warns, never refuses (A). Drafter prompt 1080 → cards 1081, 1082. | APPROVED — pending fold |
WRITE RULING 2026-10-29 R2563 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2563 |" -- "docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · 868d51c0f73ee71ddee4b9c91c1ea85ce0a3c808
WRITE RULING 2026-10-29 R2563 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · the row as grepped
AUTHORIZED
```

## SHAPE
rule (1a) · the card's `## ROWS` re-read (Read tool, card lines 13–15) · one data row (P1), seven cells:
- `command` = `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward --apply`: starts `COBALT_ENV=production uv run cobalt `; holds none of `"` `'` `\` `$` backtick `|` `&` `;` `<` `>` `*` `?` `%` `#`; verb `settings` (not an option, not `db migrate`/`db query`/`db dev-rebuild`/`backup`); no word starts `--rollback` or `--down-to`; not a `db apply`.
- `table` = `user.trader_settings` (`user.` + `[a-z0-9_]`).
- `count read` starts `COBALT_ENV=production uv run cobalt db query --side `, holds ` --prod `, names `trader_settings`, holds no `%`, `$` or backtick.
- `expected rows` = `1` (digits only). `backup` = `COBALT_ENV=production uv run cobalt backup run` (exact). `inverse` starts `COBALT_ENV=production uv run cobalt `.
→ PASS.

rule (1b) · `git -C /Users/cobalt/cobalt diff --stat 1903c47f HEAD -- . ':(exclude)docs'` · exit 0 · output: (nothing) → PASS.

## BACKUP
rule (2a) · `COBALT_ENV=production uv run cobalt backup status` · exit 0
```
forget policy: daily 14 / weekly 8 / monthly 12
sources      : /Users/cobalt/Vault/Think, /Users/cobalt/cobalt/data/.cobalt_vault
database     : cobalt_brain
  ssd   local ARMED /Volumes/COBALT-BACKUP/restic
  b2    b2    off   (no repo configured)

newest snapshot: 21.4 h old
```
→ `database     : cobalt_brain` (not OFF), `ssd` ARMED → PASS.

rule (2b) · `COBALT_ENV=production uv run cobalt backup run` (foreground) · exit 0
```
2026-10-29 19:06:34.277 | INFO     | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.backup RUNNING (timeout 3600s, heartbeat every 1200s)
2026-10-29 19:07:27.210 | INFO     | cobalt.backup.pgdump:dump_database_to:113 - backup: cobalt_brain via pg_dump inside cobalt_memory — 11805.0 MB
2026-10-29 19:07:27.215 | INFO     | cobalt.backup.restic:snapshot:246 - backup: cobalt_brain dumped, 11805.0 MB
2026-10-29 19:07:52.310 | INFO     | cobalt.backup.restic:_snapshot_one:300 - backup: ssd: snapshot 534339ca — 1 new / 3 changed, 595.6 MB added, 1 pruned
2026-10-29 19:07:52.515 | INFO     | cobalt.jobs.wrapper:job_run:199 - F17: com.cobalt.backup DONE
ssd: snapshot 534339ca — 1 new / 3 changed, 595.6 MB added, 1 pruned
```
→ `<path>` = `ssd/534339ca` (ssd = `/Volumes/COBALT-BACKUP/restic`).

## ROLLBACK
- backup: `ssd/534339ca`
- inverse (card P1 cell, verbatim, NOT typed by this seat): `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/rollback --apply`

## COUNT BEFORE
rule (3) · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE source = 'yaml:/Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward'"` · exit 0
```
tbl	n
user.trader_settings	0
```
→ `<a>` = 0.

## WRITE
rule (4) · typed ONCE · before: `2026-10-29 19:08:04 EDT` · after: `2026-10-29 19:08:08 EDT` (both `date`)
`COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward --apply` · exit 0
```
2026-10-29 19:08:06.840 | INFO     | cobalt.settings.cli:apply_settings:113 - settings applied: keys ['aset.enabled_grades', 'aset.sheet_modes', 'daymode.enabled_modes', 'daymode.hotkey_file_template', 'daymode.reduced_enabled_grades', 'daymode.reduced_sheet', 'daymode.stepdowns'] · deleted [] · source yaml:/Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward · at 2026-10-29T23:08:06+00:00
cobalt settings load — APPLY from yaml:/Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward

  = aset.sheet_modes
  = aset.enabled_grades
  = daymode.reduced_sheet
  = daymode.reduced_enabled_grades
  ~ daymode.enabled_modes
      db  : ["reduced"]
      file: ["reduced", "half", "full"]
  = daymode.hotkey_file_template
  = daymode.stepdowns

applied: {'aset.sheet_modes': 'unchanged', 'aset.enabled_grades': 'unchanged', 'daymode.reduced_sheet': 'unchanged', 'daymode.reduced_enabled_grades': 'unchanged', 'daymode.enabled_modes': 'updated', 'daymode.hotkey_file_template': 'unchanged', 'daymode.stepdowns': 'unchanged'}
from_db() == from_yaml() — field-by-field diff EMPTY.
```

## VERIFY
rule (5) · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT 'user.trader_settings' AS tbl, count(*) AS n FROM trader_settings WHERE source = 'yaml:/Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward'"` · exit 0
```
tbl	n
user.trader_settings	1
```
→ `<b>` = 1 = `expected rows` 1 → PASS. The WRITE output's `applied:` line names `daymode.enabled_modes: 'updated'` and the other six `'unchanged'`, and `deleted []`.

## DECISIONS
1. FOR DEJAN · Card 1081 `## RECORDS` SEAT STEPS (5) asks for a read-back query of the seven rows with `updated_at`. PRODWRITE-HUB (6) says "Nothing else is run" after VERIFY. Safe default: not run; the hub's order governs. What we have instead, from the WRITE output: six keys `unchanged`, `daymode.enabled_modes` db `["reduced"]` → file `["reduced", "half", "full"]` `updated`, `deleted []`, and `from_db() == from_yaml() — field-by-field diff EMPTY`. The count went 0 → 1, so only one key took the forward source. ASK DESK: run the seven-row read-back from the desk if you want it on file [2026-10-29 19:08 EDT].
2. FOR DESK · Seat error: at 19:08 this seat made one stray file through the Write tool, `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-daymode-enabled-modes.md.tmp-unused` (content: `x`). That breaks the rule "a Write or Edit outside `<REPORT>`". It is not a production file. This seat has no `rm`, so the desk should delete it and not commit it.
3. Observed: the working tree has uncommitted changes to `configs/cobalt/rules.yaml` and `.claude/settings.json` (session git status). (1b) checks only BASE..HEAD. `grep rules.yaml src/cobalt/settings` finds nothing (Grep tool), so the write route does not read that file. No action taken.

## RECORDS
- Card `## RECORDS`, as read: route `settings load --from <dir>` writes the seven `SETTING_KEYS` and skips a key equal to the database; the files were made by the desk from one production read (R686). forward = production with `daymode.enabled_modes: [reduced, half, full]`. The four sha256 were checked by the desk before launch (this seat cannot run `shasum`). No dry-run gate (route (b), R2580). Expected count before 0, after 1. No restarts. HITL ruling R2563. Independent of card 1082.
- Refused calls: none.
- CONTINUE messages received: none.
- L74: none arrived in a tool result.
- Times: started 19:05:57 EDT; write 19:08:04–19:08:08 EDT; report closed 19:08:24 EDT (all `date`). The 20:00–21:00 ET refusal window was not hit.

## §0 Headline (final)
Card 1081 P1 WRITTEN at 19:08 EDT. Production `daymode.enabled_modes` is now `["reduced","half","full"]` (was `["reduced"]`). The other six keys are unchanged and nothing was deleted. The count went 0 → 1, as expected. Backup `ssd/534339ca` was taken first; the inverse is in `## ROLLBACK`, not run. One seat error: a stray file `…prodwrite-daymode-enabled-modes.md.tmp-unused` for the desk to delete (DECISIONS 2).

WRITTEN · job: daymode-enabled-modes · rows: 1 · backup: ssd/534339ca
