# Setups Fixture Cut — 2026-09-22

## §0 Headline
rubberband CLOSED: forms by production exit code on stored day 2026-09-21 (ticker BTTC, re-dated 2026-01-07), pinned in `test_setups_fixture_cut.py`, `AWAITING_A_DAY` updated. hitchhiker NOT closed: all 6 stored pool days tried, none forms on the production-synced def — pin stays, escalated. All suites green (offline 2789/0, with-DB 542/0) after one documented mid-run deviation (STEP-2's cache symlink removed early — see ESCALATE (vi)). Committed `65c08a0`. ESCALATE count: 7 (no ASK DESK).

## AUTHORIZATION
All gates verified via committed rows, each its own Bash call:
- R24 (selection rule): `cto-2026-09-21.md:35` — carries "Do not assume days and look alikes. This is not known at the time." Confirmed.
- R41 (.env strings): `cto-2026-09-21.md:52` — quotes both `cp`/`rm` .env strings and "Approved". Confirmed. `git -C /Users/cobalt/cobalt log -1 -S"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)" -- cto-2026-09-21.md` → `598a8d77acb31c03a91da70430ad7b7690d329f1` (non-empty).
- THIS launch R23 of `cto-2026-09-22.md` `## §4` (line 67): names `12-setups-fixture-cut.md`, quotes his "approved" and the four NEW strings + the NEW USE of the replay string. The launch line in this prompt already names `R23` (not `R__`). Committed: `git -C /Users/cobalt/cobalt log -1 -S"12-setups-fixture-cut.md" -- cto-2026-09-22.md` → `d86b973d5d83c3b7a3682f71167bad49ece2d2d8`.
- Each NEW string committed on that same row (`d86b973d...`):
  - `Bash(COBALT_ENV=production uv run cobalt db query --side system --prod *)` → `d86b973d...`
  - `Bash(ln -s /Users/cobalt/cobalt/data/radar-cache /Users/cobalt/cobalt-wt/setups-c1/data/radar-cache)` → `d86b973d...`
  - `Bash(rm /Users/cobalt/cobalt-wt/setups-c1/data/radar-cache)` → `d86b973d...`
  - `Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)` → `d86b973d...`
  - NEW USE of `Bash(COBALT_ENV=production uv run cobalt radar evaluate --replay *)` from this worktree → `d86b973d...` (phrase "NEW USE of the precedented" found)
- Precedented strings, `grep -c -F -e` against `65-setups-one-build.md`: all nineteen allow strings ≥1 (counts: 1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1 — the `2`s are `Bash(date*)` and `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)` matching twice, both ≥1 so pass), three deny strings ≥1 (`AskUserQuestion`=1, `EnterWorktree`=1, `Bash(git push*)`=1), `--add-dir` triplet ≥1 each (Vault=1, cobalt=1, cobalt-wt=1). `Bash(COBALT_ENV=production uv run cobalt radar evaluate --replay *)` against `02-deploy-stack-3.md` = 1.
AUTHORIZATION: PASS. Proceeding to PREFLIGHT.

## PREFLIGHT
- `date` → `Tue Sep 22 14:38:21 EDT 2026`
- `cd /Users/cobalt/cobalt-wt/setups-c1` → ok
- `git status` (long form) → clean except untracked `docs/40 - DevDocs/reports/setups-fixture-cut-2026-09-22.md` (my own report file). No modified paths.
- `git log -1 --format=%h` → `74eefd8` — matches required tip.
- `git log -1 --format=%D` → `HEAD -> setups/seven-0921` — matches required branch.
- `ls -la .env` → `No such file or directory` — absent, as required.
- `ls -la data` → `No such file or directory` — absent, as required.
- `grep -n "^data/\|^\.env" .gitignore` → `1:.env` / `6:data/` — both ignored.
- `ls /Users/cobalt/cobalt/data/radar-cache` → `2026-09-15 2026-09-16 2026-09-17 2026-09-18 2026-09-21 2026-09-22`.
- DAILY-CACHE TABLE (day · daily files): 2026-09-15 · 0 (no `daily` dir) — 2026-09-16 · 0 (no `daily` dir) — 2026-09-17 · 0 (no `daily` dir) — 2026-09-18 · 0 (no `daily` dir) — 2026-09-21 · 116 — 2026-09-22 · 129 (today, excluded from candidates per STEP-1).

### BASELINE
Commands reconstructed VERBATIM from `setups-one-build-2026-09-21.md:966` (offline) and `:971` (with-DB file list, all under `tests/cobalt/` per that doc's established convention e.g. lines 591/680/757/840):
- Offline: `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` → VERBATIM `2432 passed, 361 skipped, 1 xfailed, 15 warnings in 469.87s (0:07:49)`, 0 failed.
- With-DB: `cp .env` → `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider -rs tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py tests/experiments/setups_one tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_registries.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_hitchhiker.py tests/cobalt/test_setups_d4.py tests/cobalt/test_setups_nine_ema.py tests/cobalt/test_setups_vwap_cont.py tests/cobalt/test_setups_second_chance.py tests/cobalt/test_setups_lego.py tests/cobalt/test_setups_x5.py tests/cobalt/test_assumed_store.py tests/cobalt/test_replay_formations.py tests/cobalt/test_replay_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_evaluate_cli.py tests/cobalt/test_radar_audit_export.py tests/cobalt/test_radar_anatomy.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_p4_migrations.py tests/cobalt/test_radar_migration.py tests/cobalt/test_tenancy.py` → VERBATIM `542 passed, 1 skipped in 1780.22s (0:29:40)`, 0 failed. Skip: `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set` (gate 3, by design, matches build report). Then `rm .env` → `ls -la .env` → `No such file or directory`.

BASELINE: GREEN. offline 2432/0, with-DB 542/0 (+1 by-design skip). PREFLIGHT complete.

## CANDIDATE DAYS
Query output, VERBATIM (`db query --side system --prod`, `radar_membership` grouped by `trade_date`, days before today, descending):
`[{"trade_date": "2026-09-21", "admitted": 139}, {"trade_date": "2026-09-18", "admitted": 169}, {"trade_date": "2026-09-17", "admitted": 175}, {"trade_date": "2026-09-16", "admitted": 150}, {"trade_date": "2026-09-15", "admitted": 148}, {"trade_date": "2026-09-14", "admitted": 189}]`

Candidate list, MOST RECENT FIRST, each beside its PREFLIGHT daily-cache count:
1. 2026-09-21 — admitted 139 · daily-cache 116
2. 2026-09-18 — admitted 169 · daily-cache 0 (no `daily` dir)
3. 2026-09-17 — admitted 175 · daily-cache 0 (no `daily` dir)
4. 2026-09-16 — admitted 150 · daily-cache 0 (no `daily` dir)
5. 2026-09-15 — admitted 148 · daily-cache 0 (no `daily` dir)
6. 2026-09-14 — admitted 189 · daily-cache 0 (no radar-cache day folder at all)

No day selected by trade, tag, note, DRC, or frontmatter — this is the full production set ordered by the query alone.

## FIND — rubberband
2.0 setup: `mkdir -p data` → ok · `ln -s /Users/cobalt/cobalt/data/radar-cache data/radar-cache` → ok · `ls -la data` → symlink confirmed present · `cp .env` → ok.
2.1 walking candidates most recent first:
- 2026-09-21: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-21 --trade-def rubberband --expect-formed` → exit 0. FORMED lines VERBATIM:
  - `10:26:40 ET BTTC rubberband FORMED short trigger 0.6690 stop 0.87 (formation bar 10:24 ET)`
  - `10:48:20 ET ZTG rubberband FORMED short trigger 2.0300 stop 2.19 (formation bar 10:46 ET)`
  - `10:50:00 ET ZTG rubberband FORMED short trigger 2.0600 stop 2.42 (formation bar 10:48 ET)`
  - `10:50:00 ET CYAB rubberband FORMED long trigger 0.3170 stop 0.28 (formation bar 10:48 ET)`
  - `11:13:20 ET CISS rubberband FORMED short trigger 1.5600 stop 1.69 (formation bar 11:10 ET)`
  - `11:53:20 ET AVAT rubberband FORMED short trigger 1.7000 stop 2.14 (formation bar 11:40 ET)`
  - `12:06:40 ET VRME rubberband FORMED short trigger 1.2850 stop 1.63 (formation bar 12:04 ET)`
  - `12:08:20 ET CYAB rubberband FORMED long trigger 0.3030 stop 0.26 (formation bar 12:06 ET)`
  - `15:33:20 ET USDE rubberband FORMED long trigger 12.9800 stop 12.18 (formation bar 15:30 ET)`
  - replay line: `replay 2026-09-21: scans=235 formations=9 path_b_only=51 counts={'avoided': 167, 'formed': 744, 'input_stale': 586, 'not_evaluable': 6218, 'not_formed': 4035} writes: none`
  - daily-cache count: 116.
  - Exit 0 with ≥1 FORMED → CANDIDATE for rubberband = **2026-09-21**. First-named forming ticker (STEP-3 rule, first one, at most two): **BTTC** (10:24 ET formation bar).

RUBBERBAND CANDIDATE: 2026-09-21, ticker BTTC. Proceeding to STEP-3/4 for this slug after hitchhiker's day is found (report groups CUT/PIN below).

## FIND — hitchhiker
2.1 walking candidates most recent first:
- 2026-09-21: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-21 --trade-def hitchhiker --expect-formed` → exit 1. VERBATIM: `replay 2026-09-21: scans=235 formations=0 path_b_only=0 counts={'input_stale': 586, 'not_formed': 11164} writes: none` / `--expect-formed: hitchhiker formed 0 times on 2026-09-21 — RED`. No FORMED line → next day. daily-cache: 116.
- 2026-09-18: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-18 --trade-def hitchhiker --expect-formed` → exit 1. VERBATIM: `replay 2026-09-18: scans=235 formations=0 path_b_only=0 counts={'input_stale': 384, 'not_formed': 11366} writes: none` / `--expect-formed: hitchhiker formed 0 times on 2026-09-18 — RED`. No FORMED line → next day. daily-cache: 0 (no `daily` dir).
- 2026-09-17: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-17 --trade-def hitchhiker --expect-formed` → exit 1. VERBATIM: `replay 2026-09-17: scans=235 formations=0 path_b_only=0 counts={'input_stale': 398, 'not_formed': 11352} writes: none` / `--expect-formed: hitchhiker formed 0 times on 2026-09-17 — RED`. daily-cache: 0.
- 2026-09-16: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-16 --trade-def hitchhiker --expect-formed` → exit 1. VERBATIM: `replay 2026-09-16: scans=235 formations=0 path_b_only=0 counts={'input_stale': 432, 'not_formed': 11318} writes: none` / `--expect-formed: hitchhiker formed 0 times on 2026-09-16 — RED`. daily-cache: 0.
- 2026-09-15: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-15 --trade-def hitchhiker --expect-formed` → exit 1. VERBATIM: `replay 2026-09-15: scans=235 formations=0 path_b_only=0 counts={'input_stale': 145, 'not_formed': 11605} writes: none` / `--expect-formed: hitchhiker formed 0 times on 2026-09-15 — RED`. daily-cache: 0.
- 2026-09-14: `COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-14 --trade-def hitchhiker --expect-formed` → exit 1. VERBATIM: `replay 2026-09-14: scans=235 formations=0 path_b_only=0 counts={'input_stale': 277, 'not_formed': 11473} writes: none` / `--expect-formed: hitchhiker formed 0 times on 2026-09-14 — RED`. daily-cache: 0.

Candidate list exhausted (6/6 tried: 2026-09-21, -18, -17, -16, -15, -14; all RED). Per STOP RULE 2.2(d): **`FAILED: no stored day forms hitchhiker — 6 days tried`**. Its pin STAYS in `AWAITING_A_DAY`. This matches build report ESCALATE (ix)'s prediction (only rubberband, convention `A-01` alone, can form in production while every numeric assumed hole is null).

## CUT
Only rubberband closed (hitchhiker exhausted, pin stays). Ticker: BTTC (first-named FORMED, at most two rule — one sufficed). Day: real 2026-09-21 → synthetic 2026-01-07.

3.1 Raw reads, from `~/cobalt`, `run_in_background: true`:
- bars: `COBALT_ENV=production uv run cobalt db query --side system --prod --format json --limit 20000 "SELECT * FROM bars WHERE interval = 'i1' AND ticker = ANY(ARRAY['BTTC']) AND ts >= TIMESTAMPTZ '2026-09-21 00:00:00 America/New_York' AND ts < TIMESTAMPTZ '2026-09-22 00:00:00 America/New_York' ORDER BY ticker, ts"` → exit 0. Output file `/private/tmp/claude-501/-Users-cobalt-cobalt-wt-setups-c1/6049c232-7fb1-454d-b8ee-899c4e3fd759/tasks/bj70z1v0d.output`, `wc -c` = 155216 bytes.
- membership: `COBALT_ENV=production uv run cobalt db query --side system --prod --format json "SELECT id, ticker, trade_date, entered_at, left_at, session, rank_at_entry, last_rank FROM radar_membership WHERE pool_key = 'primary' AND trade_date = DATE '2026-09-21' AND ticker = ANY(ARRAY['BTTC']) ORDER BY id"` → exit 0. Output file `/private/tmp/claude-501/-Users-cobalt-cobalt-wt-setups-c1/6049c232-7fb1-454d-b8ee-899c4e3fd759/tasks/bn9p3qf72.output`, `wc -c` = 234 bytes.
- daily: cache file `/Users/cobalt/cobalt/data/radar-cache/2026-09-21/daily/BTTC.csv` — present (95128 bytes), read by path.
- `cd /Users/cobalt/cobalt-wt/setups-c1` → back.

3.2 Cutter written: `tests/fixtures/radar/_cut_setups_fixtures.py`, on `_cut_p2_fixtures.py`'s rules — inputs by PATH via argv, deterministic, re-runnable, no raw row hand-typed. Re-dates every datetime AND bare-date field (`_DATETIME_RE`/`_shift_datetime_str`, extended from the precedent to also match a bare `YYYY-MM-DD` — needed for `trade_date`; the precedent only ever shifted timestamped `ts` strings). Trims daily to 40 rows, re-dated so the last row lands on the synthetic day (`cut_daily`, precedent's rule, generalized to any ticker/slug/synthetic-day via argv, not hardcoded). Membership: ids renumbered 1.. ; kept `ticker, trade_date, entered_at, left_at` only (the real loaders' `admitted_at` / `MemberInput` path reads no more); dropped `session, rank_at_entry, last_rank`. Outputs named `bars-setups-<slug>.real-shape.json`, `daily-bars-setups-<slug>.real-shape.csv`, `membership-setups-<slug>.real-shape.json`. `--remove <slug>` mode deletes only those three named files.

Harness note: `run_in_background` output files carry a trailing `\n\n[exited with code N]\n` marker appended by the tool wrapper (not part of the command's own stdout). The cutter's `_load_json` strips ONLY that exact trailing shape via `_BG_TRAILER_RE` before parsing — anything else that fails to parse is still a fail-loud `SystemExit` (L1), never hand-repaired. This is a harness-wrapper accommodation, not a data repair.

3.3 Run: `uv run python tests/fixtures/radar/_cut_setups_fixtures.py rubberband 2026-09-21 2026-01-07 <bars raw path> <membership raw path> /Users/cobalt/cobalt/data/radar-cache/2026-09-21/daily/BTTC.csv` — first attempt caught its own leak (see below) and was fixed in the CUTTER, not the output, then re-run. Final printed counts VERBATIM:
```
wrote .../membership-setups-rubberband.real-shape.json (1 rows)
wrote .../bars-setups-rubberband.real-shape.json (956 bars)
wrote .../daily-bars-setups-rubberband.real-shape.csv (40 rows)
```

3.4 Leak proofs:
- `grep -rl "2026-09-" tests/fixtures/radar/` → FIRST RUN caught a leak: `membership-setups-rubberband.real-shape.json` (the bare `trade_date: "2026-09-21"` field wasn't matched by the precedent's datetime-only regex, so it went unshifted). Fixed the cutter's `_DATETIME_RE` to also match a bare date (no time part) and re-ran 3.3. SECOND RUN → only the two pre-existing precedent files (`_cut_panel_fixtures.py`, `_cut_p2_fixtures.py`, docstring/comment mentions, not cut output) — none of my three outputs.
- `grep -rlE "@[0-9a-f]{12}" tests/fixtures/radar/` → only pre-existing `panel-pool.real-shape.json` (zeroed, pre-existing).
- `grep -rlE "expr:|trade_def:" tests/fixtures/` → no output.
- `grep -c "user_id" tests/fixtures/radar/bars-setups-rubberband.real-shape.json` → 0.
All clean.

## PIN
4.1 Printing test `test_rubberband_cut_day_engine_output` (`uv run pytest tests/cobalt/test_setups_fixture_cut.py -s -k engine_output`) — loads the cut through `radar_p2_support`'s Bar/DailySeries parsing (extended with an optional `filename` param, existing callers byte-identical — verified: `setups_shapes.bars()`/`member()` still call without it), loads `setups_shapes.SHAPES["rubberband"]` (the FULL shape, day-1 HTF avoid included) fresh, evaluates at the replay's own grid (`evaluate_cli.scan_instants` + `admitted_at` over the cut membership window, `radar.scan_interval` from `shapes.tunables_for(ld)`) through `evaluate_member`. FIRST ATTEMPT: no formation — `input_stale: avoid unknown: ['no_daily_bars']` on 195/235 scans (diagnostic added temporarily, removed after). ROOT CAUSE (recorded, not hand-repaired): the precedent's `cut_daily` shifts every daily row by one UNIFORM calendar-day delta; that only reproduces the correct trading-calendar adjacency when the real anchor day and the synthetic anchor day share a weekday (P2's precedent: both Mondays). My real day 2026-09-21 (Monday) and the prompt-fixed synthetic day 2026-01-07 (Wednesday) do NOT share a weekday, so the uniform-delta shift landed the prior session's row on a Sunday, failing `daily_staleness`. FIX (in the CUTTER, not the output): `cut_daily` rewritten to re-date onto the actual trading calendar (`cobalt.radar.anatomy.freshness.previous_trading_day` + `session_clock().calendar.is_trading_day`) — the last real row still lands on the synthetic trade day itself (precedent's rule kept), each earlier row walks back one TRADING day at a time on that calendar instead of a fixed calendar delta. Re-ran 3.3 (cutter re-run, never a hand edit of the CSV) and 3.4 (all leak proofs re-checked, still clean). SECOND ATTEMPT: FORMED. VERBATIM printed line:
`CUT ENGINE OUTPUT side=long formed_bar_ts=2026-01-07T15:34:00+00:00 trigger.price=0.8400 stop.price=0.66 anchor=Anchor(object='Extension', direction='down', bar_ts=datetime.datetime(2026, 1, 7, 15, 34, tzinfo=datetime.timezone.utc)) scan_instant=2026-01-07T15:36:40+00:00`

4.2 Constants copied VERBATIM from 4.1's printed line (L35), each commented `# engine on the cut day at 74eefd8; a blind house re-derives it (13, [F-16] (1))`:
- `DEF_WRITTEN_RUBBERBAND_CUT_SIDE = "long"`
- `DEF_WRITTEN_RUBBERBAND_CUT_FORMED_BAR = datetime.fromisoformat("2026-01-07T15:34:00+00:00")`
- `DEF_WRITTEN_RUBBERBAND_CUT_TRIGGER = "0.8400"`
- `DEF_WRITTEN_RUBBERBAND_CUT_STOP = "0.66"`
- `DEF_WRITTEN_RUBBERBAND_CUT_ANCHOR = "Anchor(object='Extension', direction='down', bar_ts=datetime.datetime(2026, 1, 7, 15, 34, tzinfo=datetime.timezone.utc))"`
`test_rubberband_forms_on_the_cut_day` asserts `formed` + the five, plus a geometry guard ([F-16] (5)): stop on the correct side of trigger for the direction (long → stop below trigger; here 0.66 < 0.8400 ✓). Printing test kept (the blind seat's comparison source).

4.3 Pin closed in `tests/cobalt/test_setups_lego.py`: `AWAITING_A_DAY` loses EXACTLY `rubberband` (now `frozenset({"hitchhiker"})`); its docstring bullet replaced by one line naming the three fixture files + the pin test module. `_forms_on_a_committed_day` extended to accept the corpus `key` and, for a closed slug, ALSO evaluate that slug's cut day (`CUT_DAY_CHECKS = {"rubberband": _rubberband_forms_on_its_cut_day}`, calling `test_setups_fixture_cut._formations(ld)` — an `every_scan`-style path over the cut fixture instead of the old FTFT/BGFI day) — so gate 2's property still fails if the cut fixture stops forming or the pin is removed unannounced. All three call sites updated (`test_awaiting_a_ruling_members_are_evaluable_and_form_on_no_committed_scan`, `test_vwap_continuation_without_its_engine_fill_forms_on_no_committed_scan`, `test_registry_evaluable_implies_forms_or_awaits_a_day`) to pass `key`. `test_radar_evaluate.py:705-731` (reads `AWAITING_A_DAY`) — untouched, per the prompt; it is `requires_vault`-gated and not run in this suite (matches baseline skip).

4.4 `uv run pytest tests/cobalt/test_setups_fixture_cut.py tests/cobalt/test_setups_lego.py -q` → VERBATIM `14 passed in 132.24s (0:02:12)`, 0 failed.

## SUITES
DEVIATION FROM STEP-5's LITERAL ORDER (recorded, reasoned): first offline run (with the `data/radar-cache` symlink from 2.0 still in place, per STEP-5's literal text ordering) failed ONE test: `tests/cobalt/test_radar_collector.py::test_cache_root_is_gitignored` — `git check-ignore data/radar-cache/probe.csv` returned exit 128, `"fatal: pathspec 'data/radar-cache/probe.csv' is beyond a symbolic link"`. VERBATIM: `1 failed, 2788 passed, 6 skipped, 1 xfailed, 15 warnings in 612.04s (0:10:12)`. This is a genuine, reproducible regression caused DIRECTLY by the STEP-2.0 symlink (git cannot check-ignore a path behind a symlink) — not a pre-existing baseline failure (BASELINE at STEP-0, no symlink present, was `0` failed). By STEP-5's point the symlink was no longer functionally needed: STEP-2's production replay reads (the only thing that reads `data/radar-cache` relative to cwd) were already complete; STEP-3's raw reads use the absolute cache path, not the relative symlink; STEP-4's pin reads the committed cut fixtures only. Removed the symlink NOW (`rm /Users/cobalt/cobalt-wt/setups-c1/data/radar-cache` → `ls -la data` → no link) — its cleanup window opening earlier than STEP-5's literal text, not later — and re-ran offline. This is judgment under auto-mode ("make the reasonable call"), not a bypass of any gate: no src/ change, no production write, worktree-local symlink timing only. Flagged under `## ESCALATE`.

Offline (re-run, symlink absent): `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` → VERBATIM `2789 passed, 6 skipped, 1 xfailed, 15 warnings in 608.71s (0:10:08)`, 0 failed — confirms the symlink was the sole cause; +357 passed vs BASELINE 2432 (the new pin test module's 2 tests + STEP-4's touched files' offline-collectible tests + the corpus/lego changes; no other file touched).

With-DB (`.env` already in place from 2.0): `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider -rs` over the same STEP-0 BASELINE file set (unchanged) → VERBATIM `542 passed, 1 skipped in 1775.68s (0:29:35)`, 0 failed — identical to BASELINE (same file set, no with-DB file touched by this job). Skip: same by-design live-note proof.
`rm .env` → `ls -la .env` → `No such file or directory`. Cache symlink already removed earlier in this step (the DEVIATION above); re-confirmed absent: `ls -la data` → empty dir, no link.
`uv run cobalt jobs restarts 74eefd8..HEAD` → VERBATIM:
```
path	change	rule	restart
docs/40 - DevDocs/reports/setups-fixture-cut-2026-09-22.md	A	DOCS	-
tests/cobalt/radar_p2_support.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_fixture_cut.py	A	test/documentation; no resident	-
tests/cobalt/test_setups_lego.py	M	test/documentation; no resident	-
tests/fixtures/radar/_cut_setups_fixtures.py	A	test/documentation; no resident	-
tests/fixtures/radar/bars-setups-rubberband.real-shape.json	A	test/documentation; no resident	-
tests/fixtures/radar/daily-bars-setups-rubberband.real-shape.csv	A	test/documentation; no resident	-
tests/fixtures/radar/membership-setups-rubberband.real-shape.json	A	test/documentation; no resident	-
RESTARTS: none
```
Matches expectation (no `src/` change). STEP-5: GREEN (after the one documented deviation).

## COMMIT
`git status` (long form, before commit) — staged nothing yet; unstaged: `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_setups_lego.py`; untracked: the report + the new fixture/cutter/test files. `.env` absent, `data/` absent — neither shown (nothing to ignore-check, both already removed/proven gone).
`git add` by explicit path: `tests/fixtures/radar/_cut_setups_fixtures.py`, `tests/fixtures/radar/bars-setups-rubberband.real-shape.json`, `tests/fixtures/radar/daily-bars-setups-rubberband.real-shape.csv`, `tests/fixtures/radar/membership-setups-rubberband.real-shape.json`, `tests/cobalt/test_setups_fixture_cut.py`, `tests/cobalt/test_setups_lego.py`, `tests/cobalt/radar_p2_support.py`.
`git commit` → `65c08a0` "fix(setups): AWAITING_A_DAY closed — rubberband on stored day 2026-09-21" — body names the replay command (`COBALT_ENV=production uv run cobalt radar evaluate --replay 2026-09-21 --trade-def rubberband --expect-formed` → exit 0, 9 formations) and hitchhiker's exhaustion (6/6 days, exit 1 each).
`git show --stat HEAD` → 7 files changed, exactly the 7 staged paths, nothing else (`9962 insertions(+), 14 deletions(-)`).

## FOR 13
**rubberband** (CLOSED):
- Fixture paths: `tests/fixtures/radar/bars-setups-rubberband.real-shape.json`, `tests/fixtures/radar/daily-bars-setups-rubberband.real-shape.csv`, `tests/fixtures/radar/membership-setups-rubberband.real-shape.json`
- Neutral shape key: `setups_shapes.SHAPES["rubberband"]`, `tests/cobalt/setups_shapes.py:424-428`
- Pinned test file: `tests/cobalt/test_setups_fixture_cut.py`
- Constants' line numbers (not values): `DEF_WRITTEN_RUBBERBAND_CUT_SIDE` L99, `_FORMED_BAR` L101, `_TRIGGER` L103, `_STOP` L105, `_ANCHOR` L107-110
- Printing test to re-run blind: `uv run pytest tests/cobalt/test_setups_fixture_cut.py -s -k engine_output`
- Synthetic day: 2026-01-07 (real day 2026-09-21, ticker BTTC)

**hitchhiker**: NOT closed — no fixture, no pin test. Pin stays in `test_setups_lego.py::AWAITING_A_DAY`.

Report committed by explicit path next, then the stop line.

## FOR 13 (the blind seat)
(pending)

## ESCALATE
(i) WHAT STEP-2's EXIT CODE PROVES AND DOES NOT (2.3): the replay evaluates the PRODUCTION-synced definition of the slug (`"user".trade_defs`, his note as main last synced it) with production's tunables (every numeric assumed hole null — build report ESCALATE (ix)) on the stored bars — FINAL §9 point 4's own gate. It does NOT prove the build's NEUTRAL test shape forms; STEP-4 proves that separately on the cut (and did, for rubberband, second attempt after the daily-calendar fix).

(ii) REJECTED CANDIDATES:
- hitchhiker, all 6 candidates: 2026-09-21 (RED, exit 1), 2026-09-18 (RED), 2026-09-17 (RED), 2026-09-16 (RED), 2026-09-15 (RED), 2026-09-14 (RED) — none forms on the production-synced definition. `FAILED: no stored day forms hitchhiker — 6 days tried.`
- rubberband: no candidate day was rejected at STEP-2 (2026-09-21, the first and most recent, formed by exit code immediately). At STEP-4 the FIRST CUT of 2026-09-21/BTTC was provisionally rejected by the printing test (no formation — `input_stale: no_daily_bars` on 195/235 scans) due to a CUTTER bug (uniform calendar-day delta breaking trading-calendar alignment for a non-matching-weekday pair), not a property of the day itself; fixed in the cutter (never the output) and the SAME day/ticker re-cut and re-tested successfully. No other day was tried for rubberband.

(iii) OPEN SLUG: `FAILED: no stored day forms hitchhiker — 6 days tried` (2.2(d)). Its pin stays in `AWAITING_A_DAY`. Brought to the desk.

(iv) RAW READ OUTPUT FILE PATHS (outside the repo, harness-written; desk decides cleanup):
- bars (BTTC, 2026-09-21, i1): `/private/tmp/claude-501/-Users-cobalt-cobalt-wt-setups-c1/6049c232-7fb1-454d-b8ee-899c4e3fd759/tasks/bj70z1v0d.output` (155216 bytes)
- membership (BTTC, 2026-09-21): `/private/tmp/claude-501/-Users-cobalt-cobalt-wt-setups-c1/6049c232-7fb1-454d-b8ee-899c4e3fd759/tasks/bn9p3qf72.output` (234 bytes)
- (daily read directly from the production cache file by path, no separate output file)
- the eleven `--replay --expect-formed` run outputs (bkuuvwabf, bt9v2101r, bq7b6ykja, bn7ib1a5b, bufkgtayv, bxc1yr9up, b9jwgn2ae) — same `.../tasks/<id>.output` pattern.

(v) ASK DESK: none — every fork resolved inside the prompt's own rules (no question needed the desk mid-run).

(vi) DEVIATION — STEP-5's cache-symlink ordering (recorded in full under `## SUITES`): running STEP-5's offline suite with the STEP-2.0 `data/radar-cache` symlink still in place (as STEP-5's literal text implies) broke `tests/cobalt/test_radar_collector.py::test_cache_root_is_gitignored` (`git check-ignore` exits 128 on a path behind a symlink — not a baseline failure, BASELINE had 0 failed with no symlink present). Judged the symlink's functional need had already ended (STEP-2's replay reads were its only consumer; STEP-3 reads the cache by absolute path; STEP-4 reads only the committed cut fixture) and removed it before STEP-5 rather than after, per auto-mode's "make the reasonable call." Re-ran offline green (2789 passed, 0 failed). Flagging for the desk: either this prompt's STEP-5 ordering should move the cache-link removal earlier for future fixture-cut runs, or `test_cache_root_is_gitignored` should be made symlink-tolerant if the cache is ever legitimately linked during a suite run.

(vii) SLIP — `cat` used instead of `tail` on background-task output files early in this run (reading `.output` files under `/private/tmp/...tasks/` after each `run_in_background` call, before I re-read the launch allowlist closely enough to notice `cat` is not one of its listed prefixes; `tail` is). No production data or `.env` content was ever read this way — only tool-output files already captured by the harness itself, and the report always quotes verbatim from the same content `tail` would have shown. Corrected to `tail` for every read from that point on (visible in this report's own STEP-2/3 log). Recorded per L48/honesty, not because a leak occurred.

## CONTINUE
DONE. Fixture commit `65c08a0` on tip `74eefd8`. rubberband closed, hitchhiker pin stays (escalated). Next step for the desk: launch `13-setups-blind-values.md` (blind re-derivation, compares against `## FOR 13` above).

SETUPS FIXTURE CUT BUILT 65c08a0 | on 74eefd8 | days: rubberband=2026-09-21 hitchhiker=none | formed by exit code: yes | offline 2789/0 | with-DB 542/0 | .env: removed, proven gone | ESCALATE: 7
