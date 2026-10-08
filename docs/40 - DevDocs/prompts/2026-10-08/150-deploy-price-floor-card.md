JOB: price-floor-1008
LADDER: OFF-LADDER — reports/cto-2026-10-08-words.md 2026-10-08 R692
BRANCH: deploy/price-floor-1008
WORKTREE: deploy-price-floor-1008
BASE: main
TIP: e34ad12c
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-price-floor-1008.md
RULINGS: 2026-10-08 R692
TAG: deploy-2026-10-08-price-floor
MIGRATIONS: 0023 · production at 0022 · creates: nothing; widens the `excluded_by` CHECK on `system.radar_membership` (drop and re-add `radar_membership_excluded_by_check`) by the value `price_floor` · old code on the new schema: the old code writes only the four old `excluded_by` values, all still allowed by the wider CHECK, and reads the column by name — a code revert alone runs on 0023; the rollback clears `price_floor` rows and restores the four-value CHECK
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/price-floor-1008` | `e34ad12c` | `e34ad12c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/price-floor-check-2026-10-08.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "price_floor" /Users/cobalt/cobalt/configs/cobalt/radar.yaml` · before `0` · after `1` (the floor, 5.00)
- `grep -c -F "price_floor: Decimal = Field(gt=0)" /Users/cobalt/cobalt/src/cobalt/radar/config.py` · before `0` · after `1` (the config model refuses a missing or non-positive floor)

## READ-BACK
`COBALT_ENV=production uv run cobalt db query --side system --prod "SELECT count(*) AS m0023 FROM pg_catalog.pg_constraint WHERE conname = 'radar_membership_excluded_by_check' AND strpos(pg_catalog.pg_get_constraintdef(oid), 'price_floor') > 0"`
- BEFORE `0` (the CHECK holds the four old `excluded_by` values, the 0022 level)
- AFTER `1` (the widened CHECK allows `price_floor`)

## SMOKE READS
- the floor in the shipped config · `grep -c -F "price_floor" /Users/cobalt/cobalt/configs/cobalt/radar.yaml` · exit 0, a count of 1 or more
- the config model field · `grep -c -F "price_floor: Decimal = Field(gt=0)" /Users/cobalt/cobalt/src/cobalt/radar/config.py` · exit 0, a count of 1 or more

Card 137 (the $5 price floor, his R692). The floor ships in `configs/cobalt/radar.yaml` with the code; no settings row, no settings load. RESTARTS: com.cobalt.aset com.cobalt.radar (the check's stop line). The deploy runs when READY at any hour (L43); it deploys alone. The check ended `held unfixed: 0 · ready: YES` at tip `e34ad12c`.

## RECORDS
- price-floor-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/price-floor-check-2026-10-08.md` last line: CHECK DONE · job: price-floor-1008 · pass: 1 · tip: e34ad12c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4023/0 · with-DB 4910/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 228719
- price-floor-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/price-floor-1008` → `e34ad12c`; code tip `e34ad12c`
- written by deploy-card.sh at 2026-10-08 14:59 ET (`date`); trial merge of the heads onto main in order: clean
