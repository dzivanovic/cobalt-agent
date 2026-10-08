# Price floor card draft (R692) · drafter `price-floor-draft` · 2026-10-08

## §0 Headline
- Card `prompts/2026-10-08/137-price-floor-card.md` written, with 8 rows: M (migration 0023), F1–F5, S (the settings file), R (restarts). The desk commits it before the build launches.
- `excluded_by` has a CHECK constraint (`0004_radar_pool.sql:42`–`:43`). The card therefore carries migration `0023`: production goes 0022 → 0023, CHECK widened, no table.
- Code wins over the answer in three places: a member must stay a candidate to depart at once; the hide sits in `members_for_day`, with 5 DRC callers opting back in; the settings load runs after the merge, never in the deploy hub.
- 13 decisions below, every one at its default. Nothing waits for him.

## CARD
- Path: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md`.
- Header: `JOB: price-floor-1008` · `LADDER: OFF-LADDER — reports/cto-2026-10-08-words.md R692` · `BRANCH: ops/price-floor-1008` · `WORKTREE: price-floor-1008` · `BASE: 059da441` · `REPORT: /Users/cobalt/cobalt-wt/price-floor-1008/docs/40 - DevDocs/reports/price-floor-build-2026-10-08.md` · `RULINGS: 2026-10-08 R692` · `TIP`, `CHECK REPORT`, `HOUSE B` empty · no `DB` key.
- Checked against `ops/desk/desk-launch.sh` build mode:
  - `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` (`:721`): all filled.
  - JOB `[a-z0-9-]` (`:731`–`:733`) and BRANCH plain (`:734`–`:736`): pass.
  - RULINGS `<date> R<n>` (`:737`–`:741`), and the row at `cto-2026-10-08.md:45` holds `HIS RULING` + `APPROVED` and is committed (`:244`–`:270`): pass.
  - WORKTREE pattern, not `agy-trial` (`:753`–`:756`): pass.
  - build: no `TAG`, `^## ROWS` present, BASE 8 hex and a commit (`:895`–`:899`): pass.
  - REPORT matches `$WT/$wt/docs/40 - DevDocs/reports/*.md` (`:900`–`:903`): pass.
  - The worktree is absent and branch `ops/price-floor-1008` does not exist (`:904`–`:910`): pass.
  - No `«FILL` (`:695`), and the card path is in `[A-Za-z0-9 ._/-]` (`:690`–`:693`): pass.
- Rows: M `0023` + rollback + order pins + `gate-lists.md` PASS 1/2. F1 the post-pass filter on `Price` (config, `required_headers`, runner). F2 `ExcludedBy.PRICE_FLOOR`, admitted members leave at once. F5 `members_for_day(price_floor_rows=False)` hides the rows; the DRC callers pass True. F3 WATCH → EXPIRED through `CardStore.transition`. F4 `radar.price_floor` in `settings/card.py`; a missing row refuses the cycle. S the packet file for the load. R `cobalt jobs restarts`.
- Every red named in the prompt is a row's red: ≤ 5.00 never a candidate (F1); 5.00 removed and 5.01 kept (F1); crosses under → `price_floor`, absent from the departed and excluded reads (F2, F5); no price → kept and flagged (F1); WATCH → EXPIRED, with ARMED, TRIGGERED, FILLED and manual untouched (F3); missing setting refuses loud (F4); read from `trader_settings`, no literal (F1, F4).

## DECISIONS
1. MIGRATION ON THIS CARD. The brain's conditional is met: `excluded_by TEXT CHECK (excluded_by IN ('config_cap','not_equity','screen_inactive','manual'))` (`0004_radar_pool.sql:42`–`:43`). ROW A puts a migration on its own card, and 137 already is its own card (new scope, not a fix on 118 or 134). So `0023` is row M here. Default taken: one card, one deploy, `MIGRATIONS: 0023`.
2. CODE WINS — DEPARTURE. The answer says a member that crosses under "drops out of the candidates, so it departs through the normal membership path". In the code, a member that is no longer a candidate RETAINs for `stickiness_scans` and then leaves with `excluded_by` None (`pool.py:399`–`:404`). Only a candidate carrying `excluded_by` LEAVEs in the same scan (`pool.py:318`–`:324`). The card keeps a floored ADMITTED member as `Candidate(excluded_by=PRICE_FLOOR)`, removed from every list's tickers. `pool.py` is unchanged.
3. CODE WINS — WHERE THE HIDE LIVES. The departed and excluded lists come from `RadarStore.members_for_day` (`store.py:55`–`:73`, called at `aset/radar_panel.py:616`). The DRC replay (`replay/runner.py:403`) and four more readers use it too. The panel may not be edited, so the store hides `price_floor` rows by default. `members_for_replay`, `replay/runner.py:403`, `evaluate_cli.py:183`/`:382`, `audit_export.py:339` and `handicap_dry_run.py:511` pass `price_floor_rows=True`. This widens the brain's fence by four `src` files, one keyword each.
4. `price_floor` IS WRITTEN ON ADMITTED ROWS ONLY. The movers replay refuses a never-admitted episode whose reason is outside its four (`replay/movers.py:111`, `:471`–`:475`), and `"user".missed` has its own CHECK (`0009_picks_missed.sql:76`–`:78`). A floored never-admitted episode closes as a non-candidate with its old reason (`pool.py:279`–`:284`). Result: in the DRC miss line, a sub-$5 mover reads `not_in_any_source`. A `price_floor` miss label is its own item if he wants it.
5. DEGRADED SOURCES. A floored ticker is also cut from a degraded source's held list. Otherwise `decide()` would both HOLD it (`pool.py:303`–`:307`) and LEAVE it (`:318`–`:324`) in one scan. Row F2 has the red for it.
6. CODE WINS — SETTINGS LOAD ORDER. The deploy hub may not load settings (`DEPLOY-HUB.md:3`: "NO settings load, NO `trader_settings` write"), and the loader on BASE refuses an unknown card key (`settings/card.py:268`–`:271`). So the `radar.price_floor` row cannot be loaded before the merge or by the deploy. The step is named in the card's `## RECORDS` SETTINGS LOAD: a dry run, then the apply, run by his hand or his approval row (L28), in the same minute as the radar restart. Between the two, every scan refuses by name and admits nothing (L1).
7. THE FILE REQUIRES THE KEY. The card file is the whole set, and an omitted key is deleted (`settings/card.py:27`–`:29`, `:297`–`:302`). A file without `radar.price_floor` would delete the row and stop every scan, so `load_card_file` refuses it. On the model, the field is optional like the other four, so stored rows from other tests parse; the runner refuses None.
8. THE FLAG. `SourceSet.metrics` holds `float | None` (`models.py:214`). The "price_unknown" flag is `price: None` in the row's metrics (stored in the S5 `pool_unit`) plus one log line per ticker per ET day. No boolean goes into a float map.
9. ONE VERDICT PER TICKER. His "once, after all lists are gathered": a ticker with any readable price ≤ floor in the scan is removed from every source. This is a post-pass after the source loop, not a per-row skip. Default: the conservative reading.
10. THE REFUSAL STAMP. A missing floor stamps `failed_stage='membership'`, one of the five values the CHECK allows (`0006_radar_score.sql:58`–`:59`), so the refusal needs no second migration.
11. PAST ROWS. The hide is by reason, as designed. A row written while the name was above the floor (an earlier `config_cap` departure, say) keeps its reason and stays listed. Card `## NOT IN THIS JOB` records it.
12. NO FALLBACK BUILT. Every source export carries `Price` (`## RECORDS`), so the brain's bar-close fallback has no source to serve. The replay tool's synthetic rows carry no price and are kept and flagged.
13. DEPLOY ALONE. R692's row reads "built with in-flight fixes"; the brain's answer says it deploys alone, before his S3 smoke. The card's `## RECORDS` DEPLOY follows the brain. The desk picks the set at its deploy card.
- The answer's seam `runner.py:103`–`:172` matched the code at HEAD exactly; no other name or line in the answer disagreed.
- FOR HIS DONE LIST: manual sheet cards he types are not filtered (his own picks); only the gathered lists and radar are. No position or ARMED, TRIGGERED or FILLED card is auto-closed when the price falls under $5; only WATCH cards expire.

## RECORDS
All read 2026-10-08 11:40–12:05 ET at HEAD `059da441`, in `/Users/cobalt/cobalt`.
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `059da441af15fba4e145b31ebd0d60099fdae274`.
- `git -C /Users/cobalt/cobalt diff --stat HEAD -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" src/cobalt configs tests ops/desk` → nothing.
- `grep -n "^| R692 " …/reports/cto-2026-10-08.md` → `45:| R692 | 11:53 ET | HIS RULING (words R692): … | APPROVED · HIS RULING · …`.
- `git -C /Users/cobalt/cobalt rev-parse --verify --quiet ops/price-floor-1008` → exit 1. `ls /Users/cobalt/cobalt-wt` → no `price-floor-1008`.
- `git -C /Users/cobalt/cobalt log --all --oneline -- "src/cobalt/db_migrations/0023*"` → nothing. Glob `*/src/cobalt/db_migrations/0023*` under `/Users/cobalt/cobalt-wt` → nothing.
- `grep -n "" src/cobalt/radar/runner.py` (whole): `_collect` `:103`–`:172`, `cycle` `:174`–`:362`, `_number` `:399`–`:406`, `build_runner` `:409`–`:458`, `_scan_replay` `:502`–`:555`.
- `grep -n "" src/cobalt/radar/pool.py` (whole): never-admitted close `:279`–`:284`, opens loop `:289`–`:307`, `excluded_by` candidates `:318`–`:329`, stickiness `:399`–`:404`.
- `sed -n 185,240p src/cobalt/radar/models.py`: `ExcludedBy` `:193`–`:197`, `SourceSet.metrics` `:214`, `Candidate` `:218`–`:222`.
- `grep -n` / `sed` of `src/cobalt/radar/store.py`: `members_for_day` `:55`–`:73`, membership writes `:128`–`:172`, `stamp_failure` `:230`–`:263`, `members_for_replay` `:490`–`:492`.
- Grep `members_for_day\(` in `src` → `radar_panel.py:616`, `audit_export.py:339`, `store.py:492`, `evaluate_cli.py:183`, `:382`, `handicap_dry_run.py:511`, `replay/runner.py:403`.
- `sed -n 590,660p src/cobalt/aset/radar_panel.py`: departed `:637`–`:639`, excluded `:640`, current-count check `:629`–`:635`.
- `sed -n 25,60p` and `170,195p src/cobalt/radar/config.py`: `MetricHeaders` `:30`–`:33`, `ExportConfig` `:46`–`:52`, `needed` `:174`–`:188`.
- `grep -n "" configs/cobalt/radar.yaml`: `required_headers` `:21`, `metric_headers` `:22`–`:24`.
- `sed -n 105,260p src/cobalt/radar/collector.py`: header check `:131`–`:133`; `_params` `:158`–`:162`; screen and list share `_request` (`:193`–`:208`).
- `grep -c "\"Price\""` on six 2026-10-08 08:00:12 cache files (3 screens, `tier_a-1`, `tier_b-1`, `tier_c-1`) → 1 each.
- `sed -n 25,60p src/cobalt/db_migrations/0004_radar_pool.sql`, `sed -n 5,16p` (same file): the `excluded_by` CHECK `:42`–`:43`, the entered-or-excluded CHECK `:48`, `failed_stage` `:11`–`:12`.
- Grep `failed_stage|…` over `db_migrations/*.sql`: `0006_radar_score.sql:21`–`:60` widens `failed_stage` (the precedent); nothing touches `excluded_by` after 0004 (`grep -n excluded_by` over 0007, 0008, 0014, 0015 → nothing).
- `sed -n 60,95p src/cobalt/db_migrations/0009_picks_missed.sql`: `missed.excluded_by` CHECK `:76`–`:78`.
- `cat 0020_drc_build_kinds.sql` and its rollback: the CHECK-widening precedent. `sed -n 95,150p placement.py`: the 0020 comment `:104`–`:105`.
- Grep `excluded_by` in `src/cobalt/replay`: `movers.py:111` `EPISODE_EXCLUSIONS`, `:471`–`:475` refusal (`sed -n 440,482p`).
- `sed -n 120,160p src/cobalt/dayopen/checks.py`: reads `excluded_by`, no value list.
- `sed -n 1,340p src/cobalt/settings/card.py`: keys `:61`–`:67`, `CardSettingsError` `:75`, `CardSettings` `:148`–`:198`, `_KEY_BY_FIELD` `:221`–`:227`, `load_card_file` `:240`–`:276` (unknown key `:268`–`:271`), round trip `:330`–`:336`.
- `cat …/prompts/2026-09-19/23-packet/p2-live-settings.yaml` and `cat data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml`: the latter adds `htf_level_proximity`, the last applied set.
- Grep `settings load --card` in `reports/cards-htf-apply-2026-09-20.md` → `:243`, applied 2026-09-20 21:05 ET with sha256 `5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17`. Grep `--card \S+ --sha256 \S+ --apply` over `reports/*2026-10-*.md` → only the brain's answer; over `*2026-09-2[1-9]*.md` → only voice reports that name the command.
- `grep -rn "settings load" …/prompts/DEPLOY-HUB.md ops/desk` → `DEPLOY-HUB.md:3` "NO settings load, NO `trader_settings` write".
- `sed -n 1010,1035p`, `1255,1295p`, `248,275p`, `384,412p src/cobalt/cards/store.py`: `open_radar_cards` `:1017`–`:1025` (`origin = 'radar'`), `expire_radar_card` `:1266`–`:1281`, `transition` `:248`, `_assert_reason` `:384`–`:410` (no reason needed for EXPIRED). `RADAR_OPEN_STATES` `:968`. `cards/models.py:93`–`:95`: WATCH → EXPIRED legal.
- `sed -n 1268,1290p` and `1741,1760p src/cobalt/radar/evaluate.py`: `OpenRadarCard.state: str`, `lifecycle_tickers`.
- `grep -n` of `tests/cobalt/test_radar_runner.py`; `sed -n 56,125p`: the fakes, `Settings.values() == {}` (to update), `SCREEN_HEADER` without `Price`.
- Grep counts in `tests`: `metric_headers|MetricHeaders\(|required_headers` → 6 files; `RadarRunner\(` → 4 files.
- `sed -n 1,22p` and `31,60p ops/desk/gate-lists.md`: a with-DB test above 0013 goes in PASS 1 `--deselect` and PASS 2.
- `grep -n "^def test_\|0022_prediction_records" tests/cobalt/test_archiver_migrations.py`: order pins `:80`–`:162`.
- `ops/desk/desk-launch.sh` `:240`–`:270`, `:690`–`:780`, `:890`–`:918`: the build-mode checks under `## CARD`.
- RESTARTS class homes (`grep -n` of `src/cobalt/jobs/restarts.py`; `jobs.yaml` `imports:` and `:184`–`:194`). `static import reach` `:220`: every changed `src/**/*.py` (runner, config, models, store, evaluate_cli, audit_export, handicap_dry_run, replay/runner, settings/card, placement). `non-Python src asset` `:222`: `0023_radar_price_floor.sql` and its rollback. `resident reads` `:207`–`:210`: `configs/cobalt/radar.yaml` (`jobs.yaml:190`, `com.cobalt.radar`). `operator script; no Cobalt reader` `:230`–`:233`: `ops/desk/gate-lists.md`. `test/documentation; no resident` `:246`: every `tests/` path. `DOCS` `:225`–`:228`: the packet yaml and both reports. Expected `com.cobalt.aset com.cobalt.radar` (radar imports `cobalt.cli`, `jobs.yaml:194`; aset imports `cobalt.aset.web`, `jobs.yaml:90`). Row R runs it.
- Grep `radar/store\.py|radar/runner\.py|settings/card\.py|radar/models\.py|db_migrations` in `prompts/2026-10-08/118-radar-display-fix-card.md` → `:51` only, a read of `cards/store.py`. No file shared with 118 or 134.
- `cat …/topics/writing-rules.md`, `cat prompts/CARD.md`, precedent cards `134` and `120`, `cat reports/price-floor-answer-2026-10-08.md`, `sed -n 144,150p reports/brain-direction-2026-10-02.md` (ROW A).
- `date` → 2026-10-08 12:01 EDT.

PRICE FLOOR CARD DRAFTED · decisions: 13
