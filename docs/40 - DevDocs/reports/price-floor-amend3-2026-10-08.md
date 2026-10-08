# card 137 price floor — amend 3 · 2026-10-08

## §0 Headline
- Preflight r2 FAIL 13 fixed with option (a): `_collect` keeps its 2-tuple, `floored` travels on `self._floored`.
- The three unpackers (`handicap_dry_run.py:162`, `test_radar_replay.py:473`, `test_radar_handicap_group.py:72`) are untouched.
- NOTE 6 and NOTE 7 are spelled out in row F1. Nothing else on the card changed.

## CHANGES
Card `prompts/2026-10-08/137-price-floor-card.md`, row F1 only, two edits:
1. "`_collect` returns `floored` … (a third tuple item)" became: `_collect` keeps `(candidates, source_sets)`. `__init__` sets `self._floored: dict[str, Decimal] = {}`. `_collect` reassigns it at the end of its post-pass (ticker → lowest readable price). `cycle()` reads it right after `await self._collect(...)` (`runner.py:189`). The three unpackers are named as untouched.
2. Files column: `test_radar_collector.py:72` list CSV gains a `Price` column (NOTE 6). NOTE 7 states that `test_radar_handicap_dry_run.py` runs the real `_collect` with the shipped 5.00 floor, and that the builder proves it green.

## DECISIONS
1. (a) over (b): (a) touches zero extra files; (b) adds three files. Neither cited line breaks a stated row, since all three only read the 2-tuple. Default taken.
2. `_floored` holds a dict (ticker → price) because F3's evidence needs `price`. It is reassigned on every call, so a direct `_collect` caller never sees stale data. `cycle()` runs one scan at a time, so there is no race.
3. No `## RECORDS` AMEND 3 line was added to the card (change nothing else).

## RECORDS
- `grep` of `_collect|RadarRunner` over `src`, `tests` `*.py`. Real callers of `RadarRunner._collect`, two in `src` and two in `tests`:
  - `src/cobalt/radar/runner.py:189` (`cycle`, 2-tuple unpack)
  - `src/cobalt/radar/handicap_dry_run.py:162` (2-tuple; `collect_scan` returns its own 3-tuple with the collector, a different tuple)
  - `tests/cobalt/test_radar_replay.py:473` (2-tuple)
  - `tests/cobalt/test_radar_handicap_group.py:72` (2-tuple)
- Other `_collect` hits are unrelated: `taxonomy/predicate.py`, `tests/cobalt/test_jobs_restarts.py:291`, comments at `radar/handicap.py:93` and `radar/notes.py:551`.
- Constructors of `RadarRunner`: `runner.py:444`, `:530`; `handicap_dry_run.py:153`; `test_radar_evaluate.py:542`; `test_radar_replay.py:285`, `:463`; `test_radar_runner.py:36`, `:117`, `:362`; `test_radar_handicap_group.py:70`. No subclass (`class X(RadarRunner)` found nowhere) and no `setattr` of `_collect`. `tests/experiments/handicap_h1/h1_support.py:87` goes through `collect_scan`.
- Read `runner.py:58`–`:217` (`__init__` `:62`–`:95`, `_collect` `:103`–`:172`, `cycle` `:174`–`:215`), `handicap_dry_run.py:146`–`:163`, `test_radar_replay.py:458`–`:479`, `test_radar_handicap_group.py:60`–`:73`, `test_radar_collector.py:62`–`:81` (CSV body `:72`–`:73`, `load_config()` `:77`), `test_radar_handicap_dry_run.py` (`load_config()` `:80`–`:138`, fixtures `:69`–`:70`).
- HEAD is now `ef608126e71493ce1d7e52c120ff79b9e5a6e7f8`. `git diff --stat 059da441 HEAD -- src configs tests ops` printed nothing, so BASE and every `file:line` stand.

PRICE FLOOR CARD AMENDED3 · decisions: 3
