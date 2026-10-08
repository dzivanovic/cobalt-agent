# price-floor-1008 — build report (2026-10-08)

## §0 Headline
- BUILT on `059da441`, tip `f105b82e`: the radar removes every stock priced at or below `radar.yaml` `price_floor: 5.00` once per scan in `_collect`; an admitted member under it LEAVEs as `price_floor`; its radar WATCH card EXPIREs; `/radar`'s reads hide `price_floor` rows, the DRC readers keep them.
- Migration `0023_radar_price_floor` widens `excluded_by`'s CHECK; forward/back twice on `cobalt_dev`, F2 = F0, left at 0013.
- Suites: offline 4022/0 · with-DB 4909/0 · live-note 146/0. RESTARTS: `com.cobalt.aset com.cobalt.radar` (as the card expected).
- Rows 7 of 7, 18 mutations all red, decisions 0.

## L74
A system reminder at the session's start asked that commits end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md"` (12:44 ET), output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md" · 0 · 1b76e1f62a4e3f4984b1db328ff38f33efcb900b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R692 row · grep -n "^| R692 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 45:| R692 | 11:53 ET | HIS RULING (words R692): global $5 price floor after lists are gathered, not in Finviz filters; brain specs it; built with in-flight fixes; desk tells him when S3 smoke can resume. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW at 11:55 ET (LAWS fold at the close) |
RULING 2026-10-08 R692 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R692 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 510ee1dad54dfa6e213184a52470bfd968931f1d
RULING 2026-10-08 R692 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output

- THE MECHANICAL ROWS · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · whole:
```
clock · date · 0 · Thu Oct  8 12:44:21 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/price-floor-1008
    ?? "docs/40 - DevDocs/reports/price-floor-build-2026-10-08.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 059da441 docs(desk): price floor brain spec and drafter prompt 136 (R692)
diff · git diff --stat 059da441 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/price-floor-1008 · 0 · 059da441 docs(desk): price floor brain spec and drafter prompt 136 (R692)
env here · ls /Users/cobalt/cobalt-wt/price-floor-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env
PREFLIGHT OK
```
- BASE · `git show --stat 059da441` · 0 · `docs(desk): price floor brain spec and drafter prompt 136 (R692)`; `136-draft-price-floor.md | 7 +++++++`, `price-floor-answer-2026-10-08.md | 20 ++++++++++++++++++++`, 2 files changed, 27 insertions(+).
- RESTARTS range · `uv run cobalt jobs restarts 059da441..HEAD` · 0 · `docs/40 - DevDocs/reports/price-floor-build-2026-10-08.md	A	DOCS	-` / `RESTARTS: none` (only the untracked report; no committed change).
- READ report · `docs/40 - DevDocs/reports/price-floor-answer-2026-10-08.md` read whole (Read tool); last line: `- A position or armed card is never auto-closed when the price falls under $5. Only WATCH cards expire.`
- THE CARD'S SYMBOLS (each hit quoted from tool output):
  - `grep -rn -F "members_for_day(" src tests` · 0 · callers `src/cobalt/replay/runner.py:403`, `src/cobalt/radar/evaluate_cli.py:183`, `:382`, `src/cobalt/radar/store.py:492` (`members_for_replay`), `src/cobalt/radar/handicap_dry_run.py:511`, `src/cobalt/radar/audit_export.py:339`, `src/cobalt/aset/radar_panel.py:616`; fakes `tests/cobalt/test_replay_formations.py:78`, `test_replay_runner.py:407`, `:844`, `test_radar_evaluate_cli.py:31`, `:134`, `test_radar_panel.py:61`; real-store reads `test_radar_handicap_store.py:134`, `:209`, `:215`, `:218`, `:232`, `test_radar_handicap_dry_run.py:173`, `test_radar_panel.py:199`, `:1528`, `test_radar_store.py:182`, `:192`, `test_radar_handicap_fix_r1_runs.py:161`.
  - `RadarRunner(` / `_collect(` (Grep) · `tests/cobalt/test_radar_evaluate.py:542`, `test_radar_replay.py:285`, `:463`, `:473`, `test_radar_runner.py:36`, `:117`, `:362`, `test_radar_handicap_group.py:70`, `:72`, `src/cobalt/radar/handicap_dry_run.py:153`, `:162`, `src/cobalt/radar/runner.py:103`, `:189`, `:444`, `:530`.
  - `grep -rn -F "open_radar_cards(" src tests` · 0 · `src/cobalt/cards/store.py:1017`, `src/cobalt/radar/evaluate.py:1745`, `:1785`, `tests/cobalt/radar_p2_support.py:224` and four test readers.
  - `grep -rn -F "ExcludedBy" src` · 0 · `radar/models.py:193`, `:222`, `radar/runner.py:163`, `:169`, `radar/pool.py:23` … `:447`, `radar/handicap_dry_run.py:49`, `:380`; `replay/models.py:31` is a separate `Literal` for `"user".missed` (untouched, `## NOT IN THIS JOB`).
  - `grep -rn -F "RadarConfig(" src tests` · 0 · `src/cobalt/radar/config.py:155`, `:176` only.
  - `MetricHeaders(` / `required_headers=` (Grep) · `MetricHeaders` defined `config.py:30`, constructed by hand nowhere; `required_headers=` reads `config.export.required_headers` at `collector.py:187`, `handicap_dry_run.py:126`, `:401`, `h1_support.py:121`, `test_radar_handicap_group.py:53`; literal lists `test_radar_collector.py:20`, `:31` (`["Ticker", "Volume"]`, parse tests, not the config).
  - ORDER PINS (Grep `FORWARD\[|REVERSE\[|forward\[|reverse\[|0022_prediction_records` over `tests`): the files row M names, at the lines it names, plus `tests/cobalt/predictions_db_support.py:3`, `:21`, `:28` (apply 0022 by name, not a pin), `test_migrate_proof.py:1510` (`FORWARD[0]`), `test_tenancy.py:480` (`reverse.index` of 0005), `test_x5_tap_refresh_db.py:14` (docstring) — none of those four moves with a 0023.
  - `src/cobalt/replay/movers.py:111` `EPISODE_EXCLUSIONS = {"config_cap", "not_equity", "screen_inactive", "manual"}`; `:467` `if any(e.entered_at is not None for e in eps): continue` — an admitted episode never reaches the `:471` refusal.
  - `cards/models.py:93`–`:95` WATCH → {ARMED, PASSED, EXPIRED, MISSED}; `cards/store.py:1024` `FROM aset_sizings WHERE origin = 'radar' AND state = ANY(%s) ORDER BY id`; `:1266`–`:1281` `expire_radar_card` logs `IllegalTransition`.
  - `0004_radar_pool.sql:42`–`:43` `excluded_by TEXT CHECK (excluded_by IN ('config_cap', 'not_equity', 'screen_inactive', 'manual'))`, `:48` `CHECK (entered_at IS NOT NULL OR excluded_by IS NOT NULL)`.
- `wc -l` · `runner.py 558`, `config.py 236`, `models.py 243`, `store.py 495`, `replay/runner.py 549`, `evaluate_cli.py 482`, `audit_export.py 480`, `handicap_dry_run.py 515`, `db_migrations/__init__.py 183`, `placement.py 206`, `radar.yaml 41`, `ops/desk/gate-lists.md 48`.
- THE CARD'S RECORDS, copied: PRICE IN EVERY EXPORT; THE CHECK; STICKINESS; DEPLOY; RESTARTS expected `com.cobalt.aset com.cobalt.radar`; DB (the new with-DB file needs 0023, PASS 2 only); ORDER (parallel with 118 / 134, no shared file); AMEND 2; AMEND 4 (the fixture sweep); BASE `059da441`. Re-read here: THE CHECK (`0004:42`–`:43`, above), the registry (`__init__.py:135`–`:157`, `0022` at `:156`; `:160`–`:181`, `0022` at `:161`, Read tool), the five `members_for_day` fakes (grep above), the BASE head (preflight row `head`).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3991 passed, 787 skipped, 1 xfailed, 36 warnings in 672.43s (0:11:12)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.62s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written, no `src/` edit: NEW `tests/cobalt/test_radar_price_floor.py` (offline, F1–F5), NEW `tests/cobalt/test_radar_price_floor_db.py` (row M offline SQL/registry checks + the three with-DB tests), `tests/cobalt/test_radar_config.py` (F1 `Price` header, F4 tunable), and the order pins of row M (16 files, every list / offset one place out for `0023`).

Offline: `uv run pytest -q -rf -p no:cacheprovider --color=no --tb=no <the 19 files>` → `50 failed, 221 passed, 166 skipped in 1.69s`. The 50 reds, each for its row's reason (first lines from the `--tb=line` runs):
- F1: `test_a_row_at_or_below_the_floor_never_becomes_a_candidate` → `assert {'AAFA', 'AAF...AAFC', 'AAFD'} == {'AAFC'}` (A, B, D are candidates on BASE); `test_the_floor_is_read_from_the_config` → `assert {'CFGA', 'CFGB', 'CFGC'} == {'CFGC'}`; `test_a_row_with_no_price_is_kept_and_flagged` → `KeyError: 'price'`; `test_a_ticker_floored_by_one_source_is_removed_from_every_source` → `assert {'KEEP', 'TWOS'} == {'KEEP'}`; `test_the_removal_is_logged_once_per_source` → `assert 0 == 2`; `test_radar_config.py::test_required_headers_must_carry_price` red (BASE has no `Price` in `required_headers`, nothing refused).
- F2: `test_an_admitted_member_that_crosses_under_departs_with_price_floor` and `test_a_floored_member_held_by_a_degraded_source_still_departs_once` → `At index 0 diff: (<Action.RETAIN: 'retain'>, None) != (<Action.LEAVE: 'leave'>, 'price_floor')`; `test_a_never_admitted_episode_under_the_floor_closes_without_price_floor` → `(<Action.ADMIT: 'admit'>, None) != (<Action.LEAVE: 'leave'>, None)`; `test_a_member_back_above_the_floor_is_a_candidate_again` → RETAIN ≠ LEAVE price_floor; `test_a_floored_fund_member_departs_as_price_floor_not_not_equity` → `(<Action.LEAVE: 'leave'>, 'not_equity') != (<Action.LEAVE: 'leave'>, 'price_floor')`.
- F3: `test_a_watch_card_under_the_floor_expires`, `test_no_floored_ticker_reads_no_card`, `test_an_expiry_failure_is_stamped_evaluate_and_the_cycle_goes_on`, `test_an_illegal_transition_is_logged_not_raised`, `test_a_reset_crossing_at_the_expiry_drops_the_cycle` → `TypeError: RadarRunner.__init__() got an unexpected keyword argument 'card_store'. Did you mean 'radar_store'?`; `test_build_runner_hands_one_card_store_to_both_stages` → `assert 0 == 2` (`card_store=card_store`). Controls PASS on BASE: `test_the_replay_runner_has_no_card_store`, `test_open_radar_cards_reads_radar_origin_only`.
- F4: `test_the_floor_boundaries_behave_as_before` and `test_radar_config.py::test_the_shipped_config_carries_price_floor` → `AttributeError: 'RadarConfig' object has no attribute 'price_floor'`; `test_no_floor_literal_in_the_radar` → `assert 'self.config.price_floor' in …`; `test_a_config_without_price_floor_is_refused_naming_it` and `test_a_non_positive_price_floor_is_refused[0|0.00|-5]` red (the key-less file loads; the `0.01` control is refused as an extra key on BASE).
- F5: `test_every_drc_caller_asks_for_price_floor_rows` → `('radar/store.py', ['        return [row for row in self.members_for_day(pool_key, trade_date) if row["entered_at"] is not None]'])`; `test_members_for_day_filters_price_floor_rows_unless_asked` → `TypeError: RadarStore.members_for_day() got an unexpected keyword argument 'price_floor_rows'`.
- M (offline): `test_radar_price_floor_db.py::test_0023_is_registered_last_and_its_rollback_first`, `test_0023_creates_no_table_and_matches_the_excluded_by_in_check_only`, `test_the_rollback_states_its_cost_and_is_guarded` (no `0023` files); the order pins — `test_archiver_migrations.py` (4), `test_radar_score_migration.py` (1), `test_drc_k1_store.py` (2), `test_f15_p1_records_offline.py` (1, renamed `…_registered_second_last_…`), `test_assumed_store.py` (1), `test_seam_drc_s3_registry.py` (1), `test_legs_migration.py` (1), `test_drc_d2_fix_r1_db.py` (2), `test_drc_d3_experiments.py` (1), `test_drc_store.py` (2), `test_voice_store.py` (1), `test_p4_migrations.py` (1), `test_radar_handicap_store.py` (1), `test_tenancy.py` (1), `test_radar_migration.py` (1) — all red for no `0023` in the registry. Row M's grep proved the pin set (PREFLIGHT); `test_tenancy.py:516` and `test_radar_migration.py:34` are `[:12]` heads, widened to `[:13]` with `0023` first (the smallest change keeping the whole list pinned).

With-DB red, ONE lock take:
- `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh price-floor-1008 90` (background) → `lock taken: price-floor-1008`, exit 0, 13:11:08 ET. `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line: `-rw-------  1 cobalt  staff  2186 Oct  8 13:11 /Users/cobalt/cobalt-wt/price-floor-1008/.env`.
- `<FP>` → **F0** `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` / `TABLES 0011` (= `## LEVEL 0013` of `ops/desk/gate-lists.md`), `NOTHING WAS APPLIED`. NO forward.
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_price_floor_db.py` — first run: the three with-DB tests ERRORED at setup, `AssertionError: with-DB test without an offline skip mark` (the suite's conftest guard). Rewritten: each takes `@requires_db` from `radar_migrated_support`, as `test_radar_store.py` does. Second run → `6 failed in 0.34s`: the three offline M tests (no `0023` file) and the three with-DB tests, each `psycopg.errors.CheckViolation: new row for relation "radar_membership" violates check constraint "radar_membership_excluded_by_check"` on its `price_floor` insert (`PFLA`, `PFLR`, `PFDA`) — the row's named reason. The `0001`…`0022` applies were inside the test's own transaction (`migrated_radar`).
- `<FP>` again → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = F0.
- `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh price-floor-1008` → `lock released`; `ls /Users/cobalt/cobalt-wt/price-floor-1008/.env` → `No such file or directory`, 13:11:44 ET. **`.env: removed, proven gone (E2)`**.

## E3 THE ROWS
Built in one pass, card order M, F1, F2, F5, F3, F4 (F1's code reads F4's `config.price_floor`, so the config key landed with F1; each row's tests were run alone after the pass and under its mutations below). Commit `f105b82e` `feat(price-floor-1008): the radar's price floor — …` (33 files).

- **M** — `src/cobalt/db_migrations/0023_radar_price_floor.sql` (DO block: the one `system.radar_membership` CHECK whose definition holds `'config_cap'`, `found_count <> 1` raises; no-op when `radar_membership_excluded_by_check` already holds `'price_floor'`; else drop + `ADD CONSTRAINT radar_membership_excluded_by_check CHECK (excluded_by IN ('config_cap', 'not_equity', 'screen_inactive', 'manual', 'price_floor'))`), its rollback (`-- COST:` line; `to_regclass` guard; `SET excluded_by = NULL WHERE excluded_by = 'price_floor' AND entered_at IS NOT NULL`; the four-value CHECK back), `__init__.py` (`FORWARD` last, `REVERSE` first, two docstring entries, the seam paragraph), `placement.py` (the card's comment line beside the `0020` one), `ops/desk/gate-lists.md` (PASS 1 ends `--deselect tests/cobalt/test_radar_price_floor_db.py`, PASS 2 ends `tests/cobalt/test_radar_price_floor_db.py`). The E2 red at E2 had shown the constraint's name, `radar_membership_excluded_by_check`.
- **F1** — `config.py` `MetricHeaders.price`, `needed` gains it; `radar.yaml` `required_headers` gains `Price`, `metric_headers.price: Price`; `runner.py` `metrics["price"] = _number(…)`, `_price()` → `Decimal | None`, the post-pass after the source loop (`floored`, every `SourceSet` stripped, one `radar price floor <floor>: <source> removed <n> (<tickers>)` line per source), `_flag_price_unknown` (one `radar price unknown: <ticker> (<source>) — kept` per ticker per ET day), `self._floored` set at the end of `_collect`; the 2-tuple return kept. Test side, as the card names: `test_radar_runner.py` header gains `Price`; `test_radar_collector.py:72` and `test_radar_daily.py:161` CSV bodies gain `Price` (`10.00`); `screen-handicap.real-shape.csv` `MSTZ 2.35→12.35`, `ZTG 2.18→12.18`, `WETO 1.64→11.64` (nothing else); `test_radar_handicap_group.py` the fifth `price` key; `test_radar_replay.py:452` the four rows `{**row, "Price": "10.00"}`. `test_radar_handicap_dead.py`, `test_radar_handicap_dry_run.py`, `test_radar_handicap.py`, `test_replay_movers.py`, `h1_support.py`: not edited (no hand-built `MetricHeaders` / `required_headers` exists, PREFLIGHT grep; the first four ran green below).
- **F2** — `models.py` `ExcludedBy.PRICE_FLOOR`; `_collect` keeps a floored ticker as a candidate only when its open episode is admitted (`entered_at` not None), `excluded_by=PRICE_FLOOR` (wins over `NOT_EQUITY`); `pool.py` untouched.
- **F5** — `store.py` `members_for_day(…, *, price_floor_rows=False)` (False adds `AND excluded_by IS DISTINCT FROM 'price_floor' `; params unchanged), `members_for_replay` passes `True`; `replay/runner.py:403`, `evaluate_cli.py:183`, `:382`, `audit_export.py:339`, `handicap_dry_run.py:511` pass `True`; `radar_panel.py` untouched; fakes `test_replay_runner.py:407`, `:844`, `test_radar_evaluate_cli.py:31`, `:134`, `test_replay_formations.py:78` take `*, price_floor_rows=False`.
- **F3** — `RadarRunner(card_store=None)`; `build_runner` builds ONE `CardStore()` for `EvaluateStage` and the runner; `_expire_floored` after S1 (WATCH + floored only, `transition(…, CardState.EXPIRED, actor=Actor.COBALT, evidence={via, price, floor, scan_id}, reason="price floor", before_commit=gate("price_floor:card", …))`, `IllegalTransition` logged); `StageDropped` → `_dropped(…, "membership", e)`; any other error → `price floor expiry failed: …`, stamped `failed_stage="evaluate"` on the S2 row and the cycle result, cycle goes on. `_scan_replay` passes no card store.
- **F4** — `RadarConfig.price_floor: Decimal = Field(gt=0)`, `from decimal import Decimal`; `radar.yaml` `price_floor: 5.00` after `list_chunk_size: 50` under the card's comment line. The runner reads `self.config.price_floor`; no literal.
- DevDocs: one `## 2026-10-08 — price-floor-1008` entry each in `radar/runner.md`, `radar/config.md`, `radar/models.md`, `radar/store.md`, `radar/evaluate_cli.md`, `radar/audit_export.md`, `radar/handicap_dry_run.md`, `replay/runner.md`, `db_migrations/__init__.md`, `db_migrations/placement.md`.

Greens after the pass: row M + neighbours (19 files incl. `test_migrate_proof.py`, `test_placement.py`) → `268 passed, 187 skipped in 2.91s`; the rows' tests + radar/replay neighbours (20 files) → `448 passed, 10 skipped in 71.06s (0:01:11)`; after every mutation was undone, `test_radar_price_floor.py test_radar_price_floor_db.py test_radar_config.py test_radar_runner.py test_archiver_migrations.py test_seam_drc_s3_registry.py` → `121 passed, 13 skipped in 0.45s`; `git diff --stat` then showed only the unmutated fix.

THE MUTATIONS (each made with Edit, the row's tests run alone, undone with Edit):
| row | mutation | result · first failing line |
|---|---|---|
| M | `0023` dropped from `FORWARD` | `4 failed, 54 passed, 13 skipped` · `test_radar_price_floor_db.py:45: AssertionError: assert (PosixPath('…/0022_prediction_records.sql') == PosixPath('…/0023_radar_price_floor.sql'))` (+ `test_archiver_migrations.py:84`, `:189`, `test_seam_drc_s3_registry.py:20`) |
| M | the forward CHECK without `'price_floor'` | `1 failed, 2 passed, 3 skipped` · `test_radar_price_floor_db.py:53: assert "CHECK (excluded_by IN (… 'price_floor'))" in …` |
| F1 | `floored` always empty (`… and False`) | `5 failed` · `:182: AssertionError: assert {'AAFA', 'AAF...AAFC', 'AAFD'} == {'AAFC'}` (+ `:193`, `:222`, `:233`, `:252`) |
| F1 | `<=` → `<` | `3 failed` · `:182: AssertionError: assert {'AAFB', 'AAFC'} == {'AAFC'}` (+ `:193` `CFGB`, `:233` `BNDA`) |
| F1 | unknown-price dedup off | `1 failed` · `:215: AssertionError: ('NOPC', […]) assert 2 == 1` |
| F1 | `metric_headers.price` out of `needed` | `1 failed` · `test_radar_config.py:145: Failed: DID NOT RAISE <class 'cobalt.radar.config.RadarConfigError'>` |
| F2 | admitted exception removed | `4 failed, 1 passed` · `:266: (<Action.RETAIN: 'retain'>, None) != (<Action.LEAVE: 'leave'>, 'price_floor')` (+ `:273`, `:291`, `:303` `(LEAVE, None) != (LEAVE, 'price_floor')`); the never-admitted control stays green |
| F2 control | every open episode kept (not only admitted) | `1 failed` · `:283: (<Action.EXCLUDE: 'exclude'>, 'price_floor') != (<Action.LEAVE: 'leave'>, None)` — the X3 case |
| F5 | store filter off | `1 failed, 1 passed` · `:424: assert "excluded_by IS DISTINCT FROM 'price_floor'" in 'SELECT …'` |
| F5 | `replay/runner.py` loses the keyword | `1 failed` · `:397: AssertionError: ('replay/runner.py', [… members_for_day(deps.radar_config.pool_key, trade_date)]'])` |
| F3 | WATCH guard removed | `1 failed, 4 passed` · `:321: … Left contains 3 more items, first extra item: ('transition', 2, 'EXPIRED', 'cobalt', 'price floor')` |
| F3 | `floored` guard removed | `1 failed` · `:334: assert ['open_radar_cards'] == []` |
| F3 | `IllegalTransition` re-raised + S2 stamp off | `2 failed, 1 passed` · `:345: AssertionError: assert None == 'evaluate'`; `:353` `failed_stage` `'evaluate'` |
| F3 | `StageDropped` branch removed | `1 failed` · `:360: assert ('scanning', 'evaluate') == ('dropped', 'membership')` |
| F3 controls | `build_runner` two `CardStore()`s; replay given `card_store=None` | `2 failed` · `:364: assert 'card_store' not in …`; `:369: assert 2 == 1` |
| F4 | `price_floor: Decimal = Decimal(0)` | `4 failed, 1 passed` · `test_radar_config.py:164: Failed: DID NOT RAISE` (+ `:177` ×3) |
| F4 | runner `floor = Decimal("5.00")` | `2 failed` · `:193: assert {'CFGA', 'CFGB', 'CFGC'} == {'CFGC'}`; `:240: AssertionError: ('runner.py', '5.00')` |
| F4 | `radar.yaml` `price_floor: 6.00` | `2 failed` · `test_radar_config.py:155: assert Decimal('6.0') == Decimal('5.00')` (+ `test_radar_price_floor.py:230`) |
No named test stayed green under its mutation. The with-DB tests' mutation is their E2 red (BASE CHECK refuses `price_floor`, quoted under `## E2 RED`); their green is W's PASS 2.

## RESTARTS
Row R (RUN, asserts nothing). `uv run cobalt jobs restarts 059da441..HEAD` → the table whole:
```
path	change	rule	restart
configs/cobalt/radar.yaml	M	resident reads	com.cobalt.radar
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/audit_export.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate_cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/handicap_dry_run.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/price-floor-build-2026-10-08.md	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/db_migrations/0023_radar_price_floor.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0023_radar_price_floor.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/audit_export.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/handicap_dry_run.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
tests/… (27 rows)	M/A	test/documentation; no resident	-
tests/fixtures/radar/screen-handicap.real-shape.csv	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
(The 27 `tests/cobalt/…` rows are each `test/documentation; no resident	-`, listed whole in the tool output.) No `UNCLASSIFIED` row. `RESTARTS: com.cobalt.aset com.cobalt.radar` = the card's expected set: no DECISION R.

## W THE THREE SUITES
`<tip>` = `f105b82e`. ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh price-floor-1008 all --deploy --deselect tests/cobalt/test_radar_price_floor_db.py --tickers PFLA,PFL0,PFL1,PFL2,PFL3,PFLB,PFLR,PFLS,PFLT,PFLU,PFDA,PFDB,PFDC --migration` (background), exit 0. The verdict lines whole:
```
offline 4022/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (PFLA,PFL0,PFL1,PFL2,PFL3,PFLB,PFLR,PFLS,PFLT,PFLU,PFDA,PFDB,PFDC)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4909/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/price-floor-1008-all-20261008-131945.log
```
- (a) OFFLINE → log `:866` `4022 passed, 790 skipped, 1 xfailed, 36 warnings in 623.44s (0:10:23)` → **offline 4022/0**. Added by this build: `tests/cobalt/test_radar_price_floor.py` (22 tests: `5 failed, 17 deselected` in the F1 mutation run), `test_radar_config.py` (+6), `test_radar_price_floor_db.py` (3 offline; 3 with-DB skipped offline at `:627`–`:629`).
- (b) `lock taken: price-floor-1008` (`:872`, `lock: waited 0 min`), **F0** (`:883`) `664 35 272c95bbb12241e3611e4b36326ccf87`, `LEVEL 0013` (`:935`).
- (c) PASS 1 (`:936` `pass 1: whole (deploy)`), the executed command (`:938`) whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_radar_price_floor_db.py` → `:1091` `4714 passed, 7 skipped, 89 deselected, 3 xfailed, 43 warnings in 759.26s (0:12:39)` → **d1 = 4714**. The seven SKIPPED lines (quoted above) are the allowed set; `grep -c -F "OUTSIDE the allowed set" <log>` → `0`.
- (c2) `:1093` **`dev forward: APPLIED 13:43:13`**; **F1** (`:1169`) `893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2 (`:1171`, the PASS 2 line of `gate-lists.md` with `tests/cobalt/test_radar_price_floor_db.py` at its end, plus the gate's own copy from `--deselect`) → `:1897` `195 passed, 1 deselected, 5 warnings in 226.59s (0:03:46)` → **d2 = 195**; d1 + d2 = 4909 = `with-DB 4909/0`. This build's with-DB ids PASSED (`grep -n -F "test_radar_price_floor_db" <log>`; the fixed string `PASSED <id>` misses them because of the ANSI colour codes between the two): `:1891` `test_0023_is_registered_last_and_its_rollback_first`, `:1892` `test_0023_creates_no_table_and_matches_the_excluded_by_in_check_only`, `:1893` `test_the_rollback_states_its_cost_and_is_guarded`, `:1894` `test_0023_admits_price_floor_and_keeps_the_four`, `:1895` `test_0023_rollback_clears_price_floor_and_restores_the_check`, `:1896` `test_members_for_day_hides_price_floor_rows_and_the_drc_reads_them`.
- (c3r) `stray rows: none (PFLA,…,PFDC)`.
- (c4) `:2154` `forward, back, forward, back — F = F0 twice`.
- (f) **F2** (`:1969`) `664 35 272c95bbb12241e3611e4b36326ccf87` = F0; `:2155` **`cobalt_dev: 0013 — F2 = F0`**; `:2157` `lock released`; `.env: removed`; `ls /Users/cobalt/cobalt-wt/price-floor-1008/.env` → `No such file or directory` (13:48 ET).
- (e) LIVE-NOTE `:2226` `146 passed, 1 skipped, 15 warnings in 25.61s` → **live-note 146/0**; the skip is `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC`, none names `COBALT_LIVE_VAULT_ROOT`.
No red at W that E2 / E3 did not show: no second fix commit.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." — every new test's E2 red is quoted under `## E2 RED` (50 offline reds + the 3 with-DB `CheckViolation` reds); every row's mutation reds under `## E3` THE MUTATIONS (18 mutations, each red). The two card-named controls (`test_the_replay_runner_has_no_card_store`, `test_open_radar_cards_reads_radar_origin_only`) passed at E2 as controls; the first went red under its mutation (`:364`), the second is a static read of `cards/store.py`, a file this card does not edit (`## NOT IN THIS JOB`). The never-admitted test, green under the F2 mutation (it is the control), went red under its own mutation (`:283`). Rewritten: the three with-DB tests gained `@requires_db` after the conftest guard error (E2). The edited order pins and fixture/fake edits went red at E2 (pins) or are inputs of tests that went red under mutation.
(2) "Every entry path of each rule pinned by a test." — callers from PREFLIGHT: `_collect` (resident `cycle()` — the F2/F3 tests run `cycle()`; `handicap_dry_run.collect_scan:162`, `test_radar_handicap_group.collect:72`, `test_radar_replay.py:473` — green in the 448-test run and in W); `RadarRunner(` (`build_runner` — `test_build_runner_hands_one_card_store_to_both_stages`; `_scan_replay` — `test_the_replay_runner_has_no_card_store`; test constructors without `card_store` — green); `members_for_day(` (six DRC-side calls — `test_every_drc_caller_asks_for_price_floor_rows`; `radar_panel.py:616` default — same test + `test_members_for_day_filters_price_floor_rows_unless_asked` + the with-DB `test_members_for_day_hides_…`; the five fakes — `test_replay_runner.py`, `test_radar_evaluate_cli.py`, `test_replay_formations.py` green); `open_radar_cards(` (the floor stage — the F3 fake tests; `CardStore.open_radar_cards` origin — the static control); `load_config` (`required_headers`/`price_floor` refusals — `test_radar_config.py`). Edge inputs: price `""`, `-`, unparseable, absent key; `4.99` / `5.00` / `5.01`; one source floored of two; a degraded `held` source; a fund (NOT_EQUITY) member; a never-admitted episode; a re-entry above the floor; card states WATCH / ARMED / TRIGGERED / FILLED; transition errors (generic, `IllegalTransition`, `StageDropped`). Day state: the unknown-price flag over two cycles of one ET day.
(3) "Every `file:line`, count and quote re-read from tool output at the tip." — re-run at `f105b82e`: `grep -rn -F "price_floor_rows" src` (the seven sites, `replay/runner.py:403`, `evaluate_cli.py:183`, `:382`, `store.py:55`, `:67`, `:499`, `handicap_dry_run.py:511`, `audit_export.py:339`), `grep -n -F "0023_radar_price_floor" src/cobalt/db_migrations/__init__.py src/cobalt/db_migrations/placement.py` (`__init__.py:96`, `:98`, `:108`, `:163`, `:168`; `placement.py:106`), `grep -n -F "price" configs/cobalt/radar.yaml` (`:25` `price: Price`, `:30` the comment, `:31` `price_floor: 5.00`), `git log --oneline 059da441..HEAD` (two commits), and the gate log's lines by `grep -n` (W above).

## FOR THE CHECK
- `059da441..f105b82e`: `e0713d36 wip(price-floor-1008): red — price floor tests and the 0023 order pins (M, F1-F5)`; `f105b82e feat(price-floor-1008): the radar's price floor — once after every source, admitted members leave as price_floor, WATCH cards expire, floor in radar.yaml, 0023 (M, F1, F2, F5, F3, F4; L1, L3, L32, L76)`.
- Per row: reds `## E2 RED`; mutations and greens `## E3 THE ROWS`; with-DB greens W (c3).
- Caller greps: `## PREFLIGHT` THE CARD'S SYMBOLS.
- RUN row R: `## RESTARTS` (whole).
- Suites: W (offline 4022/0, with-DB 4909/0 = 4714 + 195, live-note 146/0; commands as executed in W).
- F0 / F1 / F2: E2 take — F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, after = F0 (no forward); W take — F0 `664 35 272c95bb…`, F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 `664 35 272c95bb…` = F0, twice (`--migration`).
- Lock: E2 taken 13:11:08, released 13:11:44 ET; W taken by `gate.sh` (log started 13:19:45 ET, `waited 0 min`), released before 13:48 ET (`lock released`, `:2157`).
- Records copied at PREFLIGHT: `## PREFLIGHT` last bullet.
- For CHECK ASK X1–X7: X1 `test_a_row_at_or_below_…`, `test_a_ticker_floored_by_one_source_…`, `test_a_floored_member_held_by_a_degraded_source_…`, the F3 card tests; X2 the two F2 LEAVE tests; X3 the never-admitted test + its mutation (`EXCLUDE price_floor` caught); X4 the F5 tests (offline SQL, caller text, with-DB three-row read); X5 `test_a_watch_card_under_the_floor_expires` (ARMED/TRIGGERED/FILLED never passed) + the origin control; X6 `test_radar_config.py` F4 tests + `test_no_floor_literal_in_the_radar`; X7 `test_0023_admits_price_floor_and_keeps_the_four` (two `excluded_by` CHECKs after 0023, the `entered_at` one kept) + the rollback test.

## CONTINUE
next: none (the desk verifies and launches the check)

## DECISIONS
none

## RECORDS
- L74: one `Claude-Session:` request (a system reminder at the start) recorded under `## L74`; not acted on.
- `.env: removed, proven gone (E2)` 13:11:44 ET; `.env: removed` (W, the gate) and `ls` → `No such file or directory` 13:48 ET.
- One extra lock take beyond W: E2's with-DB red (the hub's E2 take).
- E2 rewrite: the three with-DB tests first errored `with-DB test without an offline skip mark` (the suite conftest); each now carries `@requires_db` from `radar_migrated_support`.
- Row order: F1's runner reads `config.price_floor` (F4), so F4's config key was written in the same pass as F1; each row's tests and mutations were run per row afterwards (E3).
- `radar.yaml` `price_floor: 5.00` is a YAML float, so the loaded value prints `5.0` (`Decimal('5.0')`; equal to `Decimal("5.00")`, the tests compare by value): the log line reads `radar price floor 5.0: …` and card evidence `"floor": "5.0"`. Not a defect against the card; noted for the reader of the logs.
- F3's `CardStore.transition` call is proven against a recording fake (as the card's tests specify); its keywords (`actor`, `evidence`, `reason`, `before_commit`) match `cards/store.py:248`–`:260` as read at PREFLIGHT.
- `test_tenancy.py:516` and `test_radar_migration.py:34` were `[:12]` heads opening on `0022`; widened to `[:13]` with `0023` first (no other change).
- `tests/experiments/handicap_h1/h1_support.py`, `test_radar_handicap.py`, `test_replay_movers.py`: no hand-built `MetricHeaders` / `required_headers` (PREFLIGHT grep), not edited.
- Context at the last step: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh caf5c1a5` → `context 397831 of 400000 — ok`.
- The card's records as re-read at PREFLIGHT: `## PREFLIGHT` last bullet.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: price-floor-1008 · tip: f105b82e | on 059da441 | migration: 0023, rolled back | offline 4022/0 | with-DB 4909/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 397831
