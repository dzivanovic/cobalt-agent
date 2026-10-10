JOB: s4-p2-1009
LADDER: S4-P2 · F9
BRANCH: deploy/s4-p2-1009
WORKTREE: deploy-s4-p2-1009
BASE: main
TIP: 44cd4e98
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-s4-p2-1009.md
RULINGS: 2026-10-06 R598
TAG: deploy-2026-10-10-s4-p2
MIGRATIONS: 0024 · production at 0023 · creates: the table `"user".strike_alerts` (one row per strike seam transition: pushed, shown and DM times and the DM result; `user_id` with the tenant GUC default, owner `cobalt_user`) and its index `strike_alerts_seam_at` · old code on the new schema: additive, touches no existing object; the old code never reads or writes the table, so a code revert alone runs on 0024; the rollback drops the table and every strike alert record, the seam rows in `"user".card_transitions` stay
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/s4-p2-1009` | `44cd4e98` | `44cd4e98` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s4-p2-check-2026-10-10.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "0024_strike_alerts" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` · before `0` · after `4` (the migration registered in FORWARD and REVERSE)

## READ-BACK
`COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) AS m0024 FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'user' AND c.relname = 'strike_alerts'"`
- BEFORE `0` (the 0023 level: no strike alerts table)
- AFTER `1` (the table exists)

## SMOKE READS
- the strike migration registered · `grep -c -F "0024_strike_alerts" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` · exit 0, a count of 1 or more

Card 73 (S4-P2, F9 delivery: the pinned `/strike` tab, the ack and its record, the phone fallback, `cobalt strike week`). RESTARTS: com.cobalt.aset com.cobalt.radar (the check's stop line). The deploy runs when READY at any hour (L43); it deploys alone and carries migration 0024. His proof B5 (open `/strike` on the trading PC, press ARM, see one live alert) is after the deploy and is his.

## RECORDS
- s4-p2-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s4-p2-check-2026-10-10.md` last line: CHECK DONE · job: s4-p2-1009 · pass: 1 · tip: 44cd4e98 · house A: Sol FINDINGS: 4 · findings: 9 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 5 · house B: Grok FINDINGS: 3 · suites: offline 4166/0 · with-DB 5063/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 238152
- s4-p2-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/s4-p2-1009` → `44cd4e98`; code tip `44cd4e98`
- written by deploy-card.sh at 2026-10-10 02:38 ET (`date`); trial merge of the heads onto main in order: clean
