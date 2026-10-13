# desk-refresh-1013 — build report (card 458), 2026-10-13

## §0 Headline
- Card 458 is built at `dbc79911` on `f7d71571`: rows S1, S2, S3, W1 and R2 (RUN), 5 of 5.
- The desk's Stop hook now prints its size every turn (or UPDATE §5 first) and REFRESH NOW at 300,000. It sends WRITE HANDOVER NOW once, and a detached `--forced` refresh launches the successor if the desk does not.
- The wake-up gains the four W1 texts (+966 bytes). The `- LAUNCH` line is byte for byte unchanged.
- Suites: offline 4317/0, live-note 146/0, `tests/ops` 3493 passed. DB: none. RESTARTS: none.
- 3 decisions (E2 red-on-BASE note, wait-env refusal, no DevDocs page), none for Dejan. Started 06:43 ET, closed 07:17 ET (`date`).

## L74
A system reminder at session start asked that commits end with a `Claude-Session:` line. Recorded here once, as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"`, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/458-desk-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/458-desk-refresh-card.md" · 0 · 981f443dc49e0f6cf19b7ed8da17df9bf63e9eaa
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/458-desk-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Tue Oct 13 06:43:48 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/desk-refresh-1013
    ?? "docs/40 - DevDocs/reports/desk-refresh-build-2026-10-13.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · f7d71571 docs(desk): card 458 amend, 15 min forced refresh, four notes folded
diff · git diff --stat f7d71571 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-refresh-1013 · 0 · f7d71571 docs(desk): card 458 amend, 15 min forced refresh, four notes folded
env here · ls /Users/cobalt/cobalt-wt/desk-refresh-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat f7d71571` | 0 | `docs(desk): card 458 amend, 15 min forced refresh, four notes folded`; `458-desk-refresh-card.md` 8 ++++----, `draft-458-amend-2026-10-13.md` 20 +, 2 files, 24 insertions, 4 deletions |
| symbols | `grep -n -F "def " ops/desk/stop-guard.py` | 0 | `186:def is_desk(event):` `206:def desk_report():` `212:def report_lines(report):` `224:def owed_block(lines):` `263:def queued(lines):` `281:def listed():` `306:def unsettled(items):` `339:def desk(event):` `380:def main():` `400:def worker(event, cwd):` (and 115-166 the worker helpers) |
| count file | `grep -n -F ".desk-stop" ops/desk/stop-guard.py` | 0 | `341:    count_file = Path(str(event.get("transcript_path")) + ".desk-stop")` |
| guard callers (KEPT) | `grep -n -F "desk-context.sh --guard" ops/desk/desk-launch.sh ops/desk/wait-stop-line.sh` | 0 | `desk-launch.sh:118`, `desk-launch.sh:365`, `wait-stop-line.sh:9` (comments naming the guard; untouched) |
| wake-up :40 | `grep -n -F "starts with MEASURE."` | 0 | `40:EVERY TURN: every turn begun by his message or a stop line starts with MEASURE. …` |
| wake-up :40 | `grep -n -F "at the next turn boundary, always."` | 0 | `40:` (same line) |
| wake-up :42 | `grep -n -F "OWED (his 10-06 R590"` | 0 | `42:OWED (his 10-06 R590; …` |
| wake-up :23 | `grep -n -F "3. No HANDOVER"` | 0 | `23:3. No HANDOVER line (crash, reboot, hand launch) → no predecessor. …` |
| wake-up :36 | `grep -n -F "8. ACT"` | 0 | `36:8. ACT on step 6's notes: …` |
| wake-up :13 | `grep -n -F -e "- LAUNCH "` | 0 | `13:- LAUNCH (at REFRESH: \`sh /Users/cobalt/.claude/ops/desk-launch.sh desk\` runs this line; …` |
| callers of the hook file | `grep -rln -F "stop-guard.py" ops src tests` | 0 | `ops/desk/stop-guard.py`, `ops/desk/idle-wake.py`, `tests/ops/test_stop_guard.py`, `tests/ops/test_idle_wake.py` |
| hub test | `grep -n -F "WAKEUP" tests/ops/test_hub_lines.py` | 0 | `116`, `122`, `152` (the `- LAUNCH` line read) |
| restarts prefix | `grep -n -F "\"ops/desk/\"" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` |
| R1323 | `grep -n -F "R1323" …/cto-2026-10-13.md` | 0 | `13:| R1323 | 06:28 ET | DESK RECORD, brain (L79) …` · `34:OWED: desk refresh card (R1323): card 458 …` |
| wc -l | `wc -l` the three row files | 0 | `418 ops/desk/stop-guard.py` · `811 tests/ops/test_stop_guard.py` · `53 docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |
| wc -c BEFORE | `wc -c` wake-up | 0 | `12794` |
| restarts | `uv run cobalt jobs restarts f7d71571..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-refresh-build-2026-10-13.md	A	DOCS	-` · `RESTARTS: none` (the untracked report only) |
| `## READ` reports | Read tool, whole | — | `desk-refresh-answer-2026-10-13.md` last line: ``…one install line by day; survey row 5 KEPT` `` |

Card `## RECORDS`, copied: the drafter's reads at `4181367b`; the hook event and the install at `~/.claude/settings.json:27-36` (not re-read: outside the listed reads); `listed()` runs `desk-list.sh` (`:281-292`, re-read: Read of stop-guard.py); `wait-stop-line.sh:64` guard (KEPT, not touched); REFRESH today `:13`, `:40`, `:47` (re-read above); the stamp's place `owed_block` `:224-260`, `queued` `:263-278` (re-read); `desk-context.sh` plain mode `:74-82` (re-read, Read tool); RESTARTS rules (`:38` re-read); 0 hits of the new texts (to be re-read by the deploy proof).
DB: none — no lock probe.

## E0 BASELINE
- Offline, on `f7d71571`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 680.87s (0:11:20)`, exit 0.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.31s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written: `tests/ops/test_stop_guard.py` section `# ---- card 458` (helper `Sized(Desk)`: fake `desk-context.sh` logging to `ctx.log`, fake `desk-launch.sh` / `desk-commit.sh` beside the hook and `claude` on `PATH` logging to `calls.log`); NEW `tests/ops/test_desk_refresh_wakeup.py`. No `src/` or `ops/` edit.
`uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stop_guard.py tests/ops/test_desk_refresh_wakeup.py` → `18 failed, 95 passed, 15 warnings in 26.94s`. Every red, first line:
- S1 `test_s1_a_fresh_desk_gets_its_size_line` → `assert (0, '', '') == (2, '', 'DESK... / 300,000\n')` (BASE runs no size part)
- S1 `test_s1_the_size_line_comes_before_the_owed_line` → `assert (2, 'start it: b\n') == (2, 'DESK SIZ...tart it: b\n')` (BASE blocks on the OWED item only; the size line is missing — the card wrote "exit 0 and stderr ''" for all four, which BASE cannot give with `OWED: b`; same reason: no size part)
- S1 `test_s1_an_unreadable_size_is_said` → `assert (0, '') == (2, 'DESK SIZ...ript for x\n')`
- S1 `test_s2_no_stamp_or_a_stale_hour_asks_for_section_5_first[none]` and `[stale]` → `assert (0, '') == (2, 'UPDATE §... / 300,000\n')`
- S2 `test_s2_at_300000_the_order_replaces_the_size_line` → `assert (0, '') == (2, 'REFRESH ... (3) stop.\n')`
- S2 `test_s2_299999_is_still_a_size_line` → `assert (0, '') == (2, 'DESK SIZ... / 300,000\n')`
- S2 `test_s2_the_order_file_starts_the_refresh_once` → `assert '' == 'REFRESH NOW:..., (3) stop.\n'`
- S3 `test_s3_the_final_message_is_sent_once` → `assert (0, '') == (2, 'WRITE HANDOVER NOW\n')`
- S3 `test_s3_no_line_forces_the_line_the_launch_and_the_stop` → `assert '| x |' == 'HANDOVER: FO...or reconciles'`
- S3 `test_s3_another_handover_line_launches_without_a_forced_line` → `assert [] == ['desk-launch...8eedc3cc8a0b']`
- S3 `test_s3_a_live_successor_is_never_doubled` → `FileNotFoundError: … wt/.job-state/DESK-REFRESH` (BASE logs nothing)
- S3 `test_s3_the_refresh_logs_each_step` → `AssertionError: a failed step: the next still runs` / `assert [] == ['claude stop...8eedc3cc8a0b']`
- W1 `test_w1_each_new_text_occurs_once` → `assert 0 == 1` (the SIZE text absent)
- W1 `test_w1_the_replaced_texts_are_gone` → `assert 1 == 0` (`starts with MEASURE.` present)
- W1 `test_w1_the_state_line_follows_the_owed_paragraph` → `assert '' == 'STATE (card ...nything else.'`
- W1 `test_w1_the_3a_line_follows_step_0_item_3` → `assert '4. No seat c... tab close`).' == '3a. Last lin...re the plate.'`
- W1 `test_w1_reconcile_ends_read_item_8` → `assert False` (endswith)

GREEN on BASE (pins and negative controls): `test_s1_the_continuation_stop_runs_no_size`, `test_s2_the_stamp_under_the_owed_block_keeps_the_block` (both pins, as the card says), `test_w1_the_launch_line_is_unchanged` (pin), and two the card listed as RED: `test_s2_a_refreshed_desk_stops_silently` and `test_s3_a_desk_that_refreshed_itself_is_left_alone` — each asserts exactly what BASE does (exit 0 / stderr `""`; no call, no line), so neither can be red on BASE; each is shown red by its E3 mutation instead (DECISION E2).
Commit: `43038a8b wip(desk-refresh-1013): red`.

## E3 THE ROWS
Built in card order, in `ops/desk/stop-guard.py` (header paragraph naming `card 2026-10-13 458`; constants after `UNREADABLE`; `desk()` gains `turn = [] if event.get("stop_hook_active") else per_turn(event, lines)` and the per-turn-only exit 2 with count `0`; new `here`, `now_iso`, `handed_over`, `stamped`, `measure`, `per_turn`, `order`, `refresh_log`, `seconds`, `when`, `forced`; `main()` reads `--forced <sid> <transcript>` first) and in the wake-up (W1, four edits, `- LAUNCH` untouched).
- S1: size line, UNREAD line, R2 `UPDATE §5 CURRENT NOW` first, OWED line last; count `0` on per-turn only; nothing on `stop_hook_active`; nothing when no `desk-context.sh` stands beside the hook.
- S2: at `n >= 300000` the REFRESH NOW line; first order writes `<transcript>.desk-refresh` (ET ISO) and `Popen([sys.executable, __file__, "--forced", sid, transcript], DEVNULL ×3, start_new_session=True)`, not waited on; last report line `HANDOVER: predecessor <p> ` with the sid starting `<p>` → no per-turn line.
- S3: (a) a one-line order file at ≥300k → `WRITE HANDOVER NOW`, second line appended; two lines → REFRESH NOW again. (b) `--forced`: TURN_WAIT then LINE_WAIT, poll 5 s; a predecessor line naming this sid at any poll → done; another live `cto-desk` row → logged, nothing launched; else FORCED line + `desk-commit.sh` (no new line only), `desk-launch.sh desk`, `claude stop`/`claude rm` of the row id (8+ chars of `[0-9a-f-]`) that is a prefix of the sid or starts with it; each step one line in `.job-state/DESK-REFRESH`; a failed step logged and the next runs.
- W1: wake-up `wc -c` 12794 → 13760 (+966 bytes): `:40` two replacements, STATE line after `:42`, 3a after `:23`, RECONCILE appended to READ 8.
One test fix during E3: `test_s2_no_stamp_or_a_stale_hour_asks_for_section_5_first[stale]` computed `stamp(1)` at collection (06:59) and the run crossed into 07:00 (`date` → `07:00:43`); the parameter is now the hour offset and the stamp is built in the test body.

Greens: `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_stop_guard.py tests/ops/test_desk_refresh_wakeup.py tests/ops/test_desk_wakeup_rule.py tests/ops/test_hub_lines.py tests/ops/test_idle_wake.py` → `154 passed, 15 warnings in 80.45s (0:01:20)` (every existing test of `test_stop_guard.py` unchanged and green; X1).

MUTATIONS (each made with Edit, run alone, undone with Edit):
| row | mutation | run | first failing line |
|---|---|---|---|
| S1 | `turn = []` | `-k "test_s1_ or test_s2_no_stamp"` → `5 failed, 1 passed` | `test_stop_guard.py:908: AssertionError: assert (0, '', '') == (2, '', 'DESK... / 300,000\n')` (also :917, :926, :934 ×2) |
| S1 pin | `turn = per_turn(event, lines)` (active too) | `-k test_s1_the_continuation_stop_runs_no_size` → `1 failed` | `:942: AssertionError: assert (2, '', 'UPDA... / 300,000\n') == (0, '', '')` |
| S1 pin | `item()` also takes `STATE AT` lines | `-k test_s2_the_stamp_under_the_owed_block_keeps_the_block` → `1 failed` | `:952: AssertionError: assert (2, '', 'star...: AT 07:02\n') == (0, '', '')` |
| S2 | `n <= SIZE_AT` | `-k "test_s2_at_300000 or test_s2_299999 or test_s2_the_order_file"` → `2 failed, 1 passed` | `:963: AssertionError: assert (2, 'DESK SIZ... / 300,000\n') == (2, 'REFRESH ... (3) stop.\n')`, `:981` |
| S2 | `n < SIZE_AT - 1` | `-k test_s2_299999` → `1 failed` | `:973: AssertionError: assert (2, 'REFRESH ... (3) stop.\n') == (2, 'DESK SIZ... / 300,000\n')` |
| S2 control | `if False and body and handed_over(...)` | `-k test_s2_a_refreshed_desk_stops_silently` → `1 failed` | `:994: AssertionError: assert (2, '', 'REFR... (3) stop.\n') == (0, '', '')` |
| S2/S3a | order file read replaced by `raise FileNotFoundError` | `-k "…order_file_starts… or …final_message…"` → `2 failed` | `:985: … assert 2 == 1` (two `desk-launch.sh desk`), `:1006: assert (2, 'REFRESH ... (3) stop.\n') == (2, 'WRITE HANDOVER NOW\n')` |
| S3b control | `refreshed()` → `False and …`; `if False and others`; `if True or not new` | `-k test_s3_` → `3 failed, 3 passed` | `:1041: assert ['desk-commit...8eedc3cc8a0b'] == []` (refreshed itself), `:1056: assert 'HANDOVER: FO...or reconciles' == 'HANDOVER: wr...uccessor next'`, `:1067: assert ['desk-commit...8eedc3cc8a0b'] == []` (live successor) |
| S3b | `ids = []` | `-k "test_s3_no_line or test_s3_the_refresh_logs"` → `2 failed` | `:1022: assert ['desk-commit...unch.sh desk'] == ['desk-commit...8eedc3cc8a0b']`, `:1079: a failed step: the next still runs` |
| W1 | blank line before the STATE line | `tests/ops/test_desk_refresh_wakeup.py` → `1 failed, 5 passed` | `:62: AssertionError: assert '' == 'STATE (card ...nything else.'` |
| W1 pin | two spaces in `--no-chrome  --strict-mcp-config` on `- LAUNCH` | same → `1 failed, 5 passed` | `:83: AssertionError: assert '- LAUNCH (at...t-mcp-config`' == '- LAUNCH (at...t-mcp-config`'` |
After the last undo `git diff --stat` → the three fix files only (`CTO-DESK-WAKEUP.md | 6 +-`, `stop-guard.py | 259 +++-`, `test_stop_guard.py | 6 +-`), the tree at the fix. The W1 red tests `test_w1_each_new_text_occurs_once`, `…replaced_texts_are_gone`, `…3a_line…`, `…reconcile…` were red on BASE (E2) and are the fix's text checks.
Commit: `dbc79911 feat(desk-refresh-1013): desk size every turn, REFRESH NOW at 300k, forced refresh, wake-up rules (S1 S2 S3 W1, L35 L42 L67)`.
DevDocs: no page under `docs/40 - DevDocs/cobalt/` (or `ops/`) covers `ops/desk/stop-guard.py` (`grep -rln -F "stop-guard"` → nothing in both); no page was added (outside the rows' files) — `## RECORDS`.

## RESTARTS
`uv run cobalt jobs restarts f7d71571..HEAD` (at `dbc79911`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-refresh-build-2026-10-13.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_desk_refresh_wakeup.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. Row R2 (RUN): the table above is its output, as the card expected (`ops/desk/` operator script, `tests/` no resident, `docs/` DOCS).

## W THE THREE SUITES
`<tip>` = `dbc79911`. (a0) `git diff --name-only --no-renames f7d71571`, whole:
```
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
ops/desk/stop-guard.py
tests/ops/test_desk_refresh_wakeup.py
tests/ops/test_stop_guard.py
```
Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-refresh-1013 offline` → `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-refresh-1013-offline-20261013-070558.log` (exit 0). The offline set is `tests/cobalt tests/taxonomy`; this build adds no test there.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-refresh-1013 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-refresh-1013-livenote-20261013-070601.log` (exit 0).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3493 passed, 1 xfailed, 16 warnings in 700.59s (0:11:40)` (exit 0). This build's tests run here: 17 new tests in `tests/ops/test_stop_guard.py` (`test_s1_*` ×4, `test_s2_no_stamp…[none|stale]`, `test_s2_the_stamp_under…`, `test_s2_*` ×4, `test_s3_*` ×6) and 6 in `tests/ops/test_desk_refresh_wakeup.py`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/desk-refresh-1013/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason: E2's 18 reds (quoted) and E3's mutation table. The five tests green on BASE (two pins, the launch pin, and the two controls `test_s2_a_refreshed_desk_stops_silently` and `test_s3_a_desk_that_refreshed_itself_is_left_alone`) were each red under a mutation: `:942`, `:952`, `:83`, `:994` and `:1041`. `test_s2_299999…` was green under `<=` and red under `< SIZE_AT - 1` (`:973`). No test needed a rewrite. One parametrization was moved into the test body for an hour-boundary race, not for a wrong red.
(2) Entry paths. The hook file is called from `main()` (stdin event), `--forced` (argv) and `idle-wake.py` (PREFLIGHT grep; it imports `report_last_line` only, `tests/ops/test_idle_wake.py` green in the 154 and 3493 runs). The desk path is pinned with no `desk-context.sh` (every existing G-test, unchanged), with it on first and on active stops (S1 tests), with the OWED line, no stamp or a stale stamp, an unreadable size, 299,999 / 300,000 / 305,000 / 310,000, order files of 0, 1 and 2 lines, and a refreshed last line. `--forced` is pinned for: no line, a self line, another line, a live second desk and a failing step. Not pinned by a test, under `## DECISIONS`: a `DESK_REFRESH_*` value that is not a number (refused and logged); the `Popen` OSError log line; the 600 s / 300 s defaults.
(3) Re-read at the tip: `git show --stat dbc79911` (3 files, 265+/6−), `git log --oneline -3`, `grep -c -F "card 458" ops/desk/stop-guard.py` → `7`, `grep -c -F "WRITE HANDOVER NOW" ops/desk/stop-guard.py` → `1`, `grep -c -F "STATE AT" …CTO-DESK-WAKEUP.md` → `1`, `wc -c` → `13760`. The test line numbers (`:908`–`:1079`, the wake-up test's `:50`–`:83`) are pytest's own output from the runs quoted above.

## FOR THE CHECK
- Range `f7d71571..dbc79911`: `43038a8b wip(desk-refresh-1013): red` · `dbc79911 feat(desk-refresh-1013): desk size every turn, REFRESH NOW at 300k, forced refresh, wake-up rules (S1 S2 S3 W1, L35 L42 L67)`.
- Reds: `## E2 RED`. Mutations: `## E3 THE ROWS`. Greens: E3 `154 passed`, and W's `tests/ops` `3493 passed, 1 xfailed`.
- Caller greps: `## PREFLIGHT` (`grep -rln -F "stop-guard.py" ops src tests` → the hook, `idle-wake.py` and two test files).
- RUN row R2: `## RESTARTS`, whole.
- Suites: offline `4317/0`, live-note `146/0`, `tests/ops` `3493 passed`; with-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). The lock was neither taken nor released (DB: none).
- DEPLOY PROOF at the tip (in the worktree): `card 458` 7 hits, `WRITE HANDOVER NOW` 1, `STATE AT` 1 in the wake-up, `tests/ops/test_desk_refresh_wakeup.py` present.
- X1: every existing test of `test_stop_guard.py` passes unchanged (the only edit to existing lines is `import time`). With no `desk-context.sh` beside the hook, `per_turn` returns `[]` and `desk()` runs exactly as on BASE.
- X2: an active stop runs no per-turn part (`test_s1_the_continuation_stop_runs_no_size` and its mutation). A size-only block writes `0` (`test_s1_a_fresh_desk_gets_its_size_line`).
- X3: REFRESH NOW is pinned byte for byte, with `sh /Users/cobalt/.claude/ops/desk-launch.sh desk` (wake-up `:13`). The edge is pinned at 299,999 and 300,000.
- X4: a self line at any poll ends the refresh; a second live `cto-desk` row launches nothing. The old desk's row must be 8+ chars of `[0-9a-f-]` and in a prefix relation with the full session id. UNPROVEN: a LIST id that is a prefix of a different session's full id (needs two real ids sharing 8+ leading chars).
- X5: `Popen(start_new_session=True)` with all three pipes on DEVNULL, and the hook does not wait. The tests prove the child runs after the hook returns (`test_s2_at_300000…` waits for its calls). UNPROVEN: that the child outlives `claude stop` of the old desk; only a live desk can prove it.
- X6: the stamp sits after the block, before the blank line (`test_s2_the_stamp_under_the_owed_block_keeps_the_block` asserts the bytes `| live: b43daef9\nSTATE AT hh:mm\n\n| session |`). `queued` reads `|` lines only.

## CONTINUE
next: none — BUILT

## DECISIONS
- DECISION E2: two tests the card listed as RED on BASE, `test_s2_a_refreshed_desk_stops_silently` and `test_s3_a_desk_that_refreshed_itself_is_left_alone`, assert exactly BASE's behaviour, so they cannot be red there. Default taken: kept as written; each is shown red under its E3 mutation (`:994`, `:1041`). The card's "exit 0 and stderr ''" red for `test_s1_the_size_line_comes_before_the_owed_line` is `(2, 'start it: b\n')` on BASE; the reason is the same (no size part).
- ASK DESK 1 [07:17]: `DESK_REFRESH_TURN_WAIT` / `DESK_REFRESH_LINE_WAIT` that are not whole seconds are refused, as `DESK_HANDOVER_WAIT` is: the `--forced` child logs `refused` to `DESK-REFRESH` and does nothing. Default taken: that refusal, untested. Production sets neither variable.
- ASK DESK 2 [07:17]: no DevDocs page exists for `ops/desk/stop-guard.py`, so none was written (the rows name no such file). Default taken: no page; the header comment carries the change.

## RECORDS
- L74: a session-start system reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on.
- The card's `## RECORDS` were copied at PREFLIGHT. Re-read there: `stop-guard.py` `:224-292`, `:339-377`; `desk-context.sh:74-82`; wake-up `:13`, `:23`, `:36`, `:40`, `:42`; `restarts.py:38`. Not re-read: `~/.claude/settings.json` (outside this build's reads).
- The mutation runs at the 300k order spawned detached `--forced` children under each test's `tmp_path`, with the fake `claude` and both waits at 0. They touch nothing outside `tmp_path`.
- No extra lock take (DB: none). `.env`: never present.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-refresh-1013 · tip: dbc79911 | on f7d71571 | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 205968
