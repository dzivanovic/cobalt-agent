# launcher-shadow-check-1011 — build report (2026-10-11)

## §0 Headline
- All 9 rows are built on BASE `a76d8855`, code tip `a8c18242`. A shadow card's check now launches, preflights and fills on `SHADOW BUILT · job · tip`, with one untracked root `SHADOW-INSTRUCTIONS.md` allowed. `desk-done.sh` knows kind `shadow`. CHECK-HUB carries the four shadow lines.
- Suites at the tip: offline 4199/0, live-note 146/0, `tests/ops` 3197 passed / 0 failed. DB: none, so `cobalt_dev` was not taken. RESTARTS: none.
- W found one red that E3 did not show: `tests/ops/test_house_probe.py:193` pins CHECK-HUB at 123 lines, and the card's four lines make it 127. I fixed it in a second commit, `a8c18242`. That file is outside the rows' files, so it is DECISION 2.
- The first stop, at W, was my RUN probe in `docs/_inflight/`. The desk removed it; I verified that before resuming.

## L74
- A system notice in this session asked that commits end with a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md"` (21:47 ET):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md" · 0 · 258103eaff86889bc42f3c08341278f60228a02a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 72:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`:
```
clock · date · 0 · Sun Oct 11 21:47:11 EDT 2026
status · git status --short --branch · 0 · ## ops/launcher-shadow-check-1011
head · git log --oneline -1 · 0 · a76d8855 docs(desk): R1132 card 386 L6 and sweep re-issue
diff · git diff --stat a76d8855 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/launcher-shadow-check-1011 · 0 · a76d8855 docs(desk): R1132 card 386 L6 and sweep re-issue
env here · ls /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat a76d8855` → `docs(desk): R1132 card 386 L6 and sweep re-issue`, `docs/40 - DevDocs/reports/cto-2026-10-11.md | 1 +`.
- Symbols (each `grep -n -F`, at BASE):
  - `not built` in `ops/desk/desk-launch.sh` → `1399: … refuse "not built — no build report: $report"`, `1403: *) refuse "not built — $last" ;;`
  - `is not clean (the check session commits there)` → `1411: [ -z "$(git -C "$WT/$wt" status --porcelain)" ] || refuse "$WT/$wt is not clean (the check session commits there)"`
  - `self-check: ` in `ops/desk/preflight.sh` → `24`, `233: "BUILT · job: $job · tip: $tip"*"self-check: "[0-3]" of 3"*)`, `234`, `236`
  - `is not a BUILT line of job` in `ops/desk/card-fill.sh` → `69`
  - `done_re=` in `ops/desk/desk-done.sh` → `22: build) done_re='^BUILT' ;;` … `26: close) done_re='^CLOSE PUSHED' ;;`
  - `NO SECOND PASS, NO FURTHER HOUSE` in `CHECK-HUB.md` → `21`
  - test helpers: `tests/ops/test_preflight.py` `def test_` list (`:193`, `:224`, `:256`, `:292`, `:412` among them); `tests/ops/test_card_fill.py` `:26 desk`, `:43 fill`, `:49`, `:95`; `tests/ops/test_desk_done.py` `:29 stubs`, `:52 done_`, `:62`, `:85`.
- `wc -l` (BASE): desk-launch.sh 1687 · preflight.sh 263 · card-fill.sh 97 · desk-done.sh 65 · CHECK-HUB.md 123 · test_desk_launch_prechecks.py 1307 · test_preflight.py 429 · test_card_fill.py 144 · test_desk_done.py 169.
- `tail -n 3` of 366's build report: last line `SHADOW BUILT · job: strike-fallback-env-1010-sonnet · tip: 813036e8 | on 8f4bbe28 | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | decisions: 4 · builder: claude-sonnet-5-5 · gate: strike-fallback-env-1010-sonnet-gate · passes: 2 · suites at first run: green · builder tokens: 273992 · wall: 1.2` (no `self-check:` field, as the card's record says).
- Card records re-read: the `not built` lines (`:1399`, `:1403`) and the clean-tree line (`:1411`), as above. 366's last line, as above. Not re-read: 366's worktree status (`git -C … status` is not a listed string, `## RECORDS`). The dry RUN at E2 shows that tree refused as `is not clean` once L1 passes, and accepted after L4.
- `uv run cobalt jobs restarts a76d8855..HEAD` → header line only, `RESTARTS: none` (an empty range).
- DB: none: no lock probe.

## E0 BASELINE
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.42s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `2 failed, 4197 passed, 800 skipped, 1 xfailed, 36 warnings in 644.31s (0:10:44)`. Both failures are `test_validate_prints_the_strike_block` and `test_no_db_skips_the_db_checks_and_exits_clean`, each on:
  ```
  FAILED: docs/PLACEMENT.md violations:
    docs/_inflight/__pycache__/run_386_dry.cpython-314-pytest-9.0.2.pyc: docs/_inflight/ may hold only README.md (set COBALT_INFLIGHT_OK=1 for a deliberate in-flight window)
    docs/_inflight/run_386_dry.py: docs/_inflight/ may hold only README.md (set COBALT_INFLIGHT_OK=1 for a deliberate in-flight window)
  ```
  The paths are my RUN probe, written before E0 (see `## DECISIONS` 1). The probe touches nothing on BASE's code. I cannot rerun E0 without these files until the desk removes them.

## E2 RED
Tests written (no `src/`, no `ops/` edit), committed `d71ff562 wip(launcher-shadow-check-1011): red`.
- Run on BASE: `uv run pytest -q -rf -p no:cacheprovider --color=no --tb=line -k "386 or check_hub_shadow" <the five files>` → `15 failed, 47 passed, 210 deselected`. Reds, each for its row's reason:
  - L1 A1 `test_386_a1_…`, A2 `[bare-True]`, L4 B1 `test_386_b1_…` → `REFUSED: not built — SHADOW BUILT · job: x-job · tip: <tip> | on <base> | offline 1/0 | …` (`desk-launch.sh:1403`).
  - L5 C1 `test_386_c1_…` → `FAILED PREFLIGHT: report`. L6 D1 `test_386_d1_…` → `FAILED PREFLIGHT: status` (status `## shadow/x-job` / `?? SHADOW-INSTRUCTIONS.md`).
  - L7 E1, E3 → `REFUSED: the report's last line is not a BUILT line of job x-job: SHADOW BUILT · job: x-job · tip: 1a2b3c4d | …` (`card-fill.sh:69`).
  - L9 F1 ×2, F2 `[shadow-BUILT…]`, `[shadow-CHECK DONE…]`, F3 → `REFUSED: unknown kind: shadow`. F2's two shadow cases are red on BASE only because kind `shadow` is unknown there, not for their own reason. The mutation run in E3 shows the BUILT case going red for its own reason.
  - L2 / L6 / L8 hub tests → `assert 0 == 1` / `assert 0 == 2` / `assert 0 == 1` (no line starts `On a shadow card`; the sentence appears zero times).
- Green on BASE (the two-sided controls): A2 `other job`, `other tip`, `tip9`, `job prefix`; A3/A4 (6 cases: non-shadow, SHADOW OF + `ops/`, `shadow/` with no SHADOW OF, blank SHADOW OF, SHADOW OF below `## ROWS`, `x-shadow/`); A5; A6; B2/B3 (4 cases); B4 (2); C2 (8); C3; D2 (4); D3 (3); D4; E2 (10); F2 `[build-SHADOW BUILT…]`; `test_l2_the_launch_line_is_unchanged`.
- Rewritten once and why: A5 and B4 first rewrote an unchanged report, which failed with `CalledProcessError … commit … 'report'`; they now use the fixture's own `BUILT` report. B2/B3 first used a `SHADOW BUILT` report and refused `not built` on BASE, so they were not two-sided; they now use the `BUILT` report and reach the `:1411` test on both sides. B2–B4 first expected text without the worktree path; it was added (`refused` matches from `REFUSED: `).
- RUN, before (BASE), `uv run pytest -q -rP -p no:cacheprovider --color=no docs/_inflight/run_386_dry.py` (my probe: the dry check launch on card 366, `DESK_LAUNCH_DRY=1`, with a stub `claude` on PATH). The card's own line puts `DESK_LAUNCH_DRY=1` in front of the command, and that prefix is not a listed string:
  ```
  == /Users/cobalt/cobalt/ops/desk/desk-launch.sh · exit 1
  -- stderr
  WARNING: desk size unread — guard skipped
  REFUSED: not built — SHADOW BUILT · job: strike-fallback-env-1010-sonnet · tip: 813036e8 | on 8f4bbe28 | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | decisions: 4 · builder: claude-sonnet-5-5 · gate: strike-fallback-env-1010-sonnet-gate · passes: 2 · suites at first run: green · builder tokens: 273992 · wall: 1.2
  == /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/ops/desk/desk-launch.sh · exit 1
  (the same two lines)
  2 passed in 0.75s
  ```

## E3 THE ROWS
Committed `ba37c2a9 fix(launcher-shadow-check-1011): a shadow card's check launches on SHADOW BUILT and its one SHADOW-INSTRUCTIONS.md (L1, L2, L4-L9; L1, L3, L72)`.
- L1 / L4 `ops/desk/desk-launch.sh` (kind `check` only): `shadow=1` when BRANCH matches `shadow/?*` and the header (above the first blank line) holds a non-empty `SHADOW OF:`. A new case arm accepts `SHADOW BUILT · job: $job · tip: $tip` (bare, or followed by a space) only when `shadow` is set, and otherwise refuses `not built — $last`. At `:1411` the porcelain output exactly `?? SHADOW-INSTRUCTIONS.md` is treated as clean on a shadow card. The header comment of the rule (`:157-159`) now names both. Green: `tests/ops/test_desk_launch_prechecks.py` → `165 passed`.
- L5 / L6 `ops/desk/preflight.sh`: the same shadow test, for kind `check` only (kind `shadow` sets `kind=build` and is never one). The status row accepts the branch line plus exactly `?? SHADOW-INSTRUCTIONS.md` and prints `status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)`. The report row accepts `SHADOW BUILT · job: $job · tip: $tip` (bare, or followed by a space) on a shadow card, with no self-check field. Green: `tests/ops/test_preflight.py` → `50 passed`.
- L7 `ops/desk/card-fill.sh`: the header's `BRANCH` and `SHADOW OF` are read by `find`. On a shadow card, a last line matching `SHADOW BUILT · job: (\S+) · tip: ([0-9a-f]{8})(?=\s|$)` fills TIP without needing `self-check: 3 of 3`.
- L9 `ops/desk/desk-done.sh`: kind `shadow`, `done_re='^SHADOW (BUILT|ROLE)'`, then `kind=build`, so a FAILED line takes the `build|check` arm at `:35` (kept for CONTINUE) with no edit outside `:2-28`. The usage line and header comment name it.
- L2 / L6 / L8 `CHECK-HUB.md`: the brain's line after `:21`; the drafter's L8 line directly under the `THE MECHANICAL ROWS` bullet, then the L6 sentence; the L6 sentence again directly under the `(i)`–`(viii)` paragraph. `git diff --stat` for the file: `4 ++++`.
- Green after all rows: `uv run pytest … tests/ops/test_card_fill.py tests/ops/test_desk_done.py tests/ops/test_check_hub_shadow.py tests/ops/test_hub_lines.py tests/ops/test_preflight.py` → `126 passed`.
- RUN, after L1 and L4 (`docs/_inflight/run_386_dry.py::test_run_worktree_script`): exit 0. stdout `cd /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet` and the CHECK-HUB line for `strike-fallback-env-1010-sonnet-check`. stderr `WARNING: desk size unread — guard skipped` and `WATCH: sh /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/ops/desk/desk-watch.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/366-shadow-strike-fallback-env-1010-sonnet-card.md"`.
- RUN, after L1 alone (L4 undone by mutation): exit 1, `REFUSED: /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet is not clean (the check session commits there)`.
- MUTATIONS (Edit tool, each undone; `git diff --stat` after the last one showed only the fix):
  - L1 arm → `refuse` unconditionally: `3 failed` — A1, A2 `[bare-True]`, B1 — `REFUSED: not built — SHADOW BUILT · job: x-job · tip: …`.
  - L1 shadow gate removed (arm accepts always): `6 failed` — every A3/A4 case.
  - L1 exactness → `"SHADOW BUILT · job: $job"*`: `3 failed` — A2 `other tip`, `tip9`, `job prefix`.
  - L4 exception undone: `1 failed` — B1 `… x-job is not clean (the check session commits there)`.
  - L4 `[ -z "$shadow" ] || dirt=""`: `4 failed` — every B2/B3 case. L4 gate removed: `2 failed` — both B4 cases.
  - L5 shadow arm `ok=1`: `2 failed` — C1, D1 `FAILED PREFLIGHT: report`. L5 gate removed: `3 failed` — C2 non-shadow, SHADOW OF + `ops/`, `shadow/` with no SHADOW OF.
  - L6 exception `ok=1`: `1 failed` — D1. L6 gate removed: `4 failed` — D3 ×3, D4. L6 path match removed: `2 failed` — D2 `_subdirectory`, `_tracked_and_modified`. D2 `_second_file` and `_modified_beside` stay green under that mutation because the existing two-line status guard pins them.
  - L7 acceptance off: `2 failed` — E1 `REFUSED: the report's last line is not a BUILT line of job x-job: SHADOW BUILT …`, E3. L7 gate removed: `4 failed` — E2 non-shadow, SHADOW OF + `ops/`, `shadow/` with no SHADOW OF, SHADOW OF below the header.
  - L9 `kind=build` dropped: `1 failed` — F3 `assert 0 == 1` (closed, not kept). L9 `^(SHADOW )?(BUILT|ROLE)`: `1 failed` — F2 `[shadow-BUILT…]`.
  - Hub: `fixes none` → `fixes some`, the §7 copy removed, and the L8 / L6 lines swapped: `3 failed` — L2 `assert … == …` (`fixes none`/`fixes some`), L6 `assert 1 == 2`, L8 `assert 63 == (61 + 1)`. Launch line `--name <job>-chk`: `1 failed` — `test_l2_the_launch_line_is_unchanged`.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (`Grep desk-launch.sh|preflight.sh|card-fill.sh|desk-done.sh` there → only `cobalt/jobs/restarts.md`, which describes the restarts classifier, not these scripts). No line was added; see `## RECORDS`.

## RESTARTS
`uv run cobalt jobs restarts a76d8855..HEAD` (row L3, RUN):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md	A	DOCS	-
ops/desk/card-fill.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_card_fill.py	M	test/documentation; no resident	-
tests/ops/test_check_hub_shadow.py	A	test/documentation; no resident	-
tests/ops/test_desk_done.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
(The report row shows because the report file was untracked in the tree when this ran.)

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames a76d8855` → `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `ops/desk/card-fill.sh`, `ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_card_fill.py`, `tests/ops/test_check_hub_shadow.py`, `tests/ops/test_desk_done.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_preflight.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 10 paths)`**.
- First W, after `CONTINUE: W` (05:45 ET), on `ba37c2a9`:
  - `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-shadow-check-1011 offline` → `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-offline-20261012-054559.log`. That is E0's 4197 passes plus the two PLACEMENT tests, green once the probe paths were removed.
  - `… livenote` → `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-livenote-20261012-054600.log`.
  - `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1 failed, 3196 passed, 1 xfailed, 15 warnings in 619.24s`. The red was `test_check_hub_seat_order_is_grok_gemini_and_openai_only_by_header`, `tests/ops/test_house_probe.py:193`: `assert 127 == 123`. Card 298 S1 pins CHECK-HUB at exactly 123 lines; this card's rows L2, L6 and L8 add four.
- The W red fixed: `tests/ops/test_house_probe.py:193` → `assert len(lines) == 127  # card 386 L2, L6 (two), L8: four shadow lines`. Committed `a8c18242 fix(launcher-shadow-check-1011): CHECK-HUB line-count pin follows the four shadow lines (L2, L6, L8; L68)`. This file is outside the rows' files: DECISION 2. Its red, at 123, is the first W's line quoted above.
  - Running it with `test_check_hub_shadow.py` and `test_hub_lines.py` gave `1 failed, 48 passed`. The red was a different test, `test_no_card_probes_grok_and_gemini_and_never_calls_codex` (`'grok: OUT — TIMEOUT' != 'grok: OUT — You have hit your usage limit…'`), a stub-timing case of `house-probe.sh`, which this build does not touch. Re-run alone: `26 passed`. In the full `tests/ops` run of the first W and the second it passed.
- RESTARTS again: `uv run cobalt jobs restarts a76d8855..HEAD` → the table above plus `tests/ops/test_house_probe.py M test/documentation; no resident -`, `RESTARTS: none`. `git diff --name-only --no-renames a76d8855` → the 10 paths above plus `docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md` and `tests/ops/test_house_probe.py`, every one under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 12 paths)`**.
- Second W, on `<tip>` = `a8c18242` (one more gate call each, `## RECORDS`):
  - (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-shadow-check-1011 offline` → `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-offline-20261012-055821.log`.
  - (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-shadow-check-1011 livenote` → `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-livenote-20261012-055822.log`.
  - `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3197 passed, 1 xfailed, 15 warnings in 618.24s (0:10:18)`. This build adds the 386 tests (58 cases across `test_desk_launch_prechecks.py`, `test_preflight.py`, `test_card_fill.py`, `test_desk_done.py`: `uv run pytest --collect-only -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py tests/ops/test_preflight.py tests/ops/test_card_fill.py tests/ops/test_desk_done.py -k 386` → `58/268 tests collected (210 deselected) in 0.03s`) and `tests/ops/test_check_hub_shadow.py` (4).
  - (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/.env` → No such file.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red against BASE (E2, the 15 reds quoted) or under a mutation (E3, each line quoted). Every two-sided control went red under the mutation that removes its guard: A3/A4 (gate removed, 6), A2 (exactness, 3), B2/B3 (4), B4 (2), C2 (3), D3/D4 (4), D2 `_subdirectory`/`_tracked_and_modified` (2), E2 (4), F2 `[shadow-BUILT]` (1), F3 (1). The launch line is pinned by its own mutation (1). Some controls stay green under every mutation I made because an existing guard pins them, not this build's code: D2 `_second_file`/`_modified_beside` (the two-line status guard, `preflight.sh:110-111`); A2 `other job`, C2 `x-other` and E2 `x-other` (a job that is no prefix fails every pattern); C2 BUILT-without-self-check and E2 `self-check: 2 of 3` (the existing arms); F2 `[build-SHADOW BUILT]` and `[shadow-CHECK DONE]` (`^BUILT`, `^SHADOW`). I name them and did not rewrite them. They pin behaviour the card calls "as today". Tests rewritten: A5, B2–B4 (E2).
(2) Entry paths. The four scripts have no caller in `ops/desk` other than themselves: `grep -rn -F "desk-done.sh" ops/desk` and `grep -rn -F "card-fill.sh" ops/desk` show only their own usage lines, and `grep -rn -F "preflight.sh check" ops/desk` → nothing; the desk types them. Kinds and states:
  - check first pass: A1–A5, B1–B4
  - check resume `E3`: A6
  - preflight `check` / `shadow`: C1–C3, D1–D4
  - card-fill: E1–E3
  - desk-done `shadow` / `build`: F1–F3
  - SHADOW OF blank, below `## ROWS` or absent, and BRANCH `ops/` or `x-shadow/`: A3/A4, C2, D3, E2
  A shadow card launched with PASS-2 is not pinned: DECISION 3.
(3) Re-read at the tip:
  - `grep -n -F "SHADOW BUILT"` over the four scripts → `desk-launch.sh:159,1409,1416`, `preflight.sh:263`, `card-fill.sh:74`, `desk-done.sh:6`
  - `grep -n -F "SHADOW-INSTRUCTIONS.md"` → `desk-launch.sh:160,1426,1428`, `preflight.sh:142,143,149`
  - `grep -n -F "On a shadow card" CHECK-HUB.md` → `22`, `63`
  - the L6 sentence → `64`, `117`
  - `wc -l CHECK-HUB.md` → `127`
  - `git show --stat a8c18242` → `tests/ops/test_house_probe.py | 2 +-`
  The E3 `file:line` mentions (`:1403`, `:1411`, `:69`) are BASE lines, quoted at PREFLIGHT.

## FOR THE CHECK
- Range `a76d8855..a8c18242`:
  - `d71ff562 wip(launcher-shadow-check-1011): red`
  - `ba37c2a9 fix(launcher-shadow-check-1011): a shadow card's check launches on SHADOW BUILT and its one SHADOW-INSTRUCTIONS.md (L1, L2, L4-L9; L1, L3, L72)`
  - `adc285b3 wip(launcher-shadow-check-1011): W — the RUN probe in docs/_inflight breaks PLACEMENT; no listed string removes it` (report only)
  - `a8c18242 fix(launcher-shadow-check-1011): CHECK-HUB line-count pin follows the four shadow lines (L2, L6, L8; L68)`
- Per row, the reds, mutations and greens: `## E2 RED` and `## E3 THE ROWS`. The caller greps: self-check (2). The RUN rows' output WHOLE: E2 (before), E3 (after L1 alone, and after L1 + L4), `## RESTARTS` (L3).
- Suites: `## W`, the second W. With-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none).
- The card's records as re-read: `## PREFLIGHT`.
- Fence: `git diff --stat` shows only the rows' files plus `tests/ops/test_house_probe.py` (DECISION 2). `preflight.sh` edits sit in the status block (`:103-149` at the tip, after the inserted lines) and the report arm. `card-fill.sh` edits sit in `:53-79` at the tip. `desk-done.sh` edits sit in `:2-30` at the tip.

## CONTINUE
next: CLOSE (done)

## DECISIONS
1. ASK DESK: the card's RUN line `DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh check …` cannot be typed: the `VAR=` prefix is not a listed string, and the repo path holds BASE's script. Safe default taken: the dry launch ran from a pytest probe (`-rP`, BUILD-HUB E2's form for a RUN row), with `DESK_LAUNCH_DRY=1` and a stub `claude` on PATH so nothing could launch, against both the repo script and this worktree's script. The before, after-L1-alone and after outputs are quoted in E2 / E3. [22:12 ET]
2. ASK DESK: a file outside the rows' files was changed. `tests/ops/test_house_probe.py:193` (card 298 S1) pins CHECK-HUB.md at exactly 123 lines. This card's rows L2, L6 and L8 require four added lines, and no other hub change. The W red `assert 127 == 123` can only be fixed in that pin. Safe default taken: the pin moved to 127 with a comment naming card 386 (`a8c18242`, a one-line diff), and nothing else in that file changed. If the desk prefers the pin kept elsewhere or removed, it is one line. [06:09 ET]
3. ASK DESK: one entry path is not pinned by a test: a PASS-2 `check` launch on a shadow card. PASS-2 skips the `not built` test, as before. The new `:1411` exception for `SHADOW-INSTRUCTIONS.md` applies to it too, because `shadow` is computed for every check launch. CHECK-HUB says there is no PASS-2 any more (his R438), so no test was added. Safe default taken: behaviour left as built, and the path named here. [06:09 ET]

## RECORDS
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet status --porcelain --branch` — Permission to use Bash has been denied because Claude Code is running in don't ask mode.
- The first stop, at W (22:12 ET): my RUN probe `docs/_inflight/run_386_dry.py` and its `__pycache__/` broke the PLACEMENT tests (E0 `2 failed`), and no listed string removes them. The desk removed both. `.venv/` was created by the first `uv run` (gitignored).
- Extra gate calls: W ran twice (offline and livenote each twice). The second run followed the `a8c18242` fix of the W red.
- `tests/ops/test_house_probe.py::test_no_card_probes_grok_and_gemini_and_never_calls_codex` failed once in a three-file run with a stub-timing mismatch, passed alone (`26 passed`), and passed in both full `tests/ops` runs. It is not this build's code.
- `ops/desk/preflight.sh`'s header comment (`:9-26`) and `ops/desk/card-fill.sh`'s header comment (`:2-13`) still describe the BUILT-only rule. They lie outside the fenced lines (`:103-131`, `:228-247`; `:53-72`), so they were left unchanged.
- L9 is built inside `desk-done.sh:2-28` by `kind=build` in the `shadow)` arm (precedent `preflight.sh:52`), so `:35` is untouched.
- The `SHADOW OF:` value is read from the header only (above the first blank line) in `desk-launch.sh` and `preflight.sh`, as `card-fill.sh`'s `find` reads it (card L7), and as CHECK ASK X1 asks for a line below `## ROWS`. The build arm's `field "SHADOW OF"` (`:1332`) is fenced and unchanged.
- No DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers these `ops/desk/` scripts. Adding a page would widen the job.
- The card's records, as re-read at PREFLIGHT, are above.
- CONTINUED at W 05:45 ET: `cto-desk` sent `CONTINUE: W. the two RUN probe paths are removed`; verified with `ls -la docs/_inflight` → `README.md` only; `ls -la …/.env` → No such file.
- CONTINUED at F1 06:55 ET (`CONTINUE: FIX ROUND row F1`, a new session on wip `418af955`): `.env` No such file; `uv run pytest --collect-only … -k 386` → `58/268 tests collected (210 deselected) in 0.03s`. F1: test `66c4fefc`, red with `:140` set back to 66 (`assert 58 == 66`), green on 58 (`test_check_hub_shadow.py test_hub_lines.py test_house_probe.py` → `50 passed`); `RESTARTS: none`. Gate pass on `66c4fefc` (DB: none form): `gate.sh … offline` → `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-offline-20261012-065653.log`; `gate.sh … livenote` → `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-livenote-20261012-065654.log`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3198 passed, 1 xfailed, 16 warnings in 624.98s (0:10:24)`; `.env` No such file.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

FIXED: G3 — tests/ops/test_check_hub_shadow.py::test_build_report_case_count_matches_collection

BUILT · job: launcher-shadow-check-1011 · tip: 66c4fefc | on a76d8855 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 10 of 10 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 115749
