## §0 Headline
- Card `137` amended in place for the brain's ruling (L79): `price_floor: 5.00` in `configs/cobalt/radar.yaml`, validated by `RadarConfig` at load.
- Row S, the SETTINGS LOAD record and every `trader_settings`, `settings/card.py` and L69 reference are gone. Deploy is the merge plus the radar restart.
- Header unchanged: BASE stays `059da441`.
- Wrong line numbers fixed (`build_runner`, the `needed` set). Nothing launched, nothing run.

## CHANGES
All in `docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md`.
- WHY: floor named as `price_floor` in `radar.yaml`; "FOUR CODE FACTS" is now THREE (the settings-load fact removed); a sentence names the floor's home.
- F1: floor is `self.config.price_floor`; L69 removed; `needed` set cited at `config.py:179`–`:185`; the 10.00 test is `test_the_floor_is_read_from_the_config` (`load_config().model_copy(update=…)`); the runner fake's config is `load_config()` (`test_radar_runner.py:36`, `:117`); `test_radar_runner.py` files entry loses "and settings".
- F4: rewritten. `RadarConfig.price_floor: Decimal = Field(gt=0)`, no default; `radar.yaml` gains `price_floor: 5.00` after `list_chunk_size: 50`; reds: a config without the key fails, `0`, `0.00` and `-5` fail, 5.00 and 4.99 removed, 5.01 kept; `test_no_floor_literal_in_the_radar` now covers `runner.py` and `config.py`. Files: `configs/cobalt/radar.yaml`, `radar/config.py`, `test_radar_config.py`, `test_radar_price_floor.py`.
- Row S deleted.
- NOT IN THIS JOB: "settings load included" removed.
- READ: `settings/card.py` removed; `runner.py`, `config.py`, `test_radar_config.py` ranges added.
- X6 rewritten for the config-load refusal.
- RECORDS: SETTINGS LOAD bullet deleted; DEPLOY is "the merge plus the radar restart"; RESTARTS drops `settings/card.py` and the packet file, and states the `radar.yaml` class; BASE bullet re-proved against HEAD `b794eca5`; branch and worktree absence re-run.

## DECISIONS
1. BASE stays `059da441`. `git diff --stat 059da441 HEAD -- src configs tests ops` printed nothing.
2. The missing-setting runtime refusal and its `failed_stage="membership"` stamp are not built. A bad config stops `build_runner` (`runner.py:410`) at the resident's start, and `cobalt radar check` (`config.py:218`–`:222`). No other path needs them. The replay tool (`:531`) loads the same file.
3. RESTARTS class for `configs/cobalt/radar.yaml`: `resident reads` (`restarts.py:207`–`:210`, `:220` is the import rule), because `jobs.yaml:190` lists it under `com.cobalt.radar` and no other job lists it. Expected set unchanged: `com.cobalt.aset com.cobalt.radar`. `aset` stays through `radar.store`.
4. Fixed `file:line` slips in the card: `build_runner` is `:409`–`:458`, not `:432` (`:432` is the `EvaluateStage` block); the `needed` set is `config.py:179`–`:185`, not `:174`–`:180`.
5. F1 had `price` both as `_number` and as `_price`. Now: metrics keep the `_number` float, the floor comparison uses `_price` Decimal.
6. The F3 evidence label `"via": "radar.price_floor"` stays. It is an event tag, not a setting key.
7. UNPROVEN (L70): a YAML `5.00` loads as float `5.0`, and pydantic v2 is expected to build `Decimal` from a float through its string form. No run tool on this seat. The boundary test `test_the_floor_boundaries_behave_as_before` pins 4.99, 5.00 and 5.01.
8. `jobs restarts` is not run here; row R runs it on the build.

## RECORDS
- `Read` of the prompt, the card (whole), `configs/cobalt/radar.yaml` (whole, 41 lines), `src/cobalt/radar/config.py` (whole, 236 lines), `topics/writing-rules.md`.
- `radar/config.py`: `RadarConfig` `:155`–`:163`, `list_chunk_size: int = Field(gt=0)` `:160`, `extra="forbid"` `:156`, `ValidationError` wrap `:175`–`:178`, `needed` `:179`–`:185`, `missing` check `:186`–`:188`, `command` `:218`–`:222`, `load_config` `:166`. `MetricHeaders` `:30`–`:33`.
- `radar/runner.py`: `self.config` `:83`; `_collect` `:103`–`:172`; `cycle` `:174`–`:215`; `build_runner` `:409`–`:458` (`load_config()` `:410`, `CardStore()` `:435`, `RadarRunner(` `:444`); `_scan_replay` `:502`–`:541` (`load_config()` `:531`, header `:523`). Only `load_config()` builds the config: `Grep RadarConfig\(` over `*.py` printed `config.py:155` and `:176`.
- `jobs.yaml:184`–`:195`: `com.cobalt.radar` lists `configs/cobalt/radar.yaml` at `:190`; `com.cobalt.aset` imports `cobalt.aset.web` at `:90`. No other `radar.yaml` line in the registry.
- `restarts.py:207`–`:210` `resident reads`; `:216`–`:222` import reach and non-Python asset; `:225`–`:228` DOCS; `:230`–`:233` operator script; `:245`–`:246` tests.
- `collector.py:131`–`:133` missing-header `SourceFailure`; `:158`–`:162` `_params`; `:193`–`:208` `screen`, `listed`.
- Tests that touch the shipped file build from it: `test_radar_config.py:39`–`:134`, `test_radar_handicap.py:212`–`:229`. `test_radar_runner.py` builds from `load_config()` at `:36`, `:117`, `:363`. No test needs the key added by hand.
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `b794eca504d5d05d88911b842c04cd137354efc2`. `git diff --stat HEAD -- src/cobalt configs tests ops/desk` and `git diff --stat 059da441 HEAD -- src configs tests ops` printed nothing.
- `git rev-parse --verify --quiet ops/price-floor-1008` exit 1. `ls /Users/cobalt/cobalt-wt` has no `price-floor-1008`.
- Final `Grep` over the card for `trader_settings`, `settings_store`, `settings/card`, `L69`, `CardSettings`, `settings load`, `COBALT_ENV`, `packet`, `row S`, `card_settings`: nothing; `radar.price_floor` appears only in the F3 evidence label (decision 6).
- Allow-line walk of the card: no env var, `uv`, `shasum` or production command remains except row R's `uv run cobalt jobs restarts`, which is the build seat's own command.

PRICE FLOOR CARD AMENDED · decisions: 8
