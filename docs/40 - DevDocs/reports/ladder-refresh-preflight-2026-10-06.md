# Preflight — card 54 (radar ladder refresh build), 2026-10-06

Read-only. Every command was run in this session. `git` commands use `-C /Users/cobalt/cobalt`. `src`, `tests` and `configs` at the working tree equal BASE (`git diff --stat 8c554d77 HEAD -- src tests configs` prints nothing; `git status` at start shows none modified there).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git merge-base --is-ancestor 8c554d77 main` | exit 0, no output | OK |
| 1b | `git rev-parse --verify ops/radar-ladder-refresh-1006` (and the bare worktree name) | `fatal: Needed a single revision`, exit 128 | OK (new) |
| 1c | `ls /Users/cobalt/cobalt-wt/radar-ladder-refresh-1006` | `No such file or directory` | OK (new) |
| 1d | card header, `grep -n ^KEY:` | `BRANCH: ops/radar-ladder-refresh-1006`, `WORKTREE: radar-ladder-refresh-1006`, `BASE: 8c554d77`, `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `REPORT:` under the worktree; `RULINGS: 2026-10-06 R556`; no `DB` key (right: rows touch `src/`, `tests/`) | OK |
| 1e | `git log --oneline 8c554d77..main -- src tests configs` | empty | OK |
| 2a | `grep -n "^| R556 " reports/cto-2026-10-06.md` | `102:\| R556 \| 14:20 ET \| HIS RULING (...) fix the empty radar screen if the brain says GO ... \| HIS RULING · APPROVED \|` | OK (line 102 now; card says `:100` "at drafting") |
| 2b | `git show 8c554d77:<cto-2026-10-06.md>` grep | row is at `:101` in the BASE commit, so R556 is committed (the working copy has 2 uncommitted desk rows after it, not R556) | OK |
| 3-js | `radar_panel.py` at BASE (`git show 8c554d77:...`) | `render_ladder` `:1442`–`:1492` OK; `:1451` `open_class = " open" if index <= 2` OK; `:1492` `<details class="terminal">` OK; `:1508` `PANEL_JS = r"""` OK; `refreshLadder` `:1518`–`:1527` OK (`keep=openIds()` `:1519`, toggle `:1526`, throw `:1524`); `post()` `:1528`–`:1538` (`status(...'sending'` `:1529`, `finally`-less `catch` `:1537`) OK; dot toggle `:1546` OK; `let cursor` `:1558`, `const interval` `:1559` OK; `refreshPool` `:1560`–`:1574`, first `catch(error)` `:1569`, failure markup `:1571`, `mirrorStale(next)` `:1568` OK; `window.COBALT_RADAR` `:1575` OK; `setInterval(refreshPool,interval)` `:1576` OK; `render_radar_page` `:1581`–`:1589`, `data-refresh-seconds` `:1589` OK | OK |
| 3-inputs | `grep -n "<input\|<select\|<textarea" radar_panel.py` | first `:1185`, last `:1326`; 0 `<select`, 0 `<textarea` | OK |
| 3-pins | `test_radar_panel_cards.py` | `PIN_HEALTHY_LADDER_SHA256` `:396`, used `:507`; `MIRROR_DEGRADED_LINE` `:400`, asserted `:657`; `:648` `js.index("mirrorDegraded(next)") < ... < js.index("catch(error)")`; focus list `:670`–`:672`; `:665`–`:679`; `:646`–`:657` | OK |
| 3-tests | `test_radar_panel.py` | `:1038`–`:1047` (`setInterval(refreshPool,interval)` `:1047`); `:1050`–`:1058` monkeypatch `build_radar_panel` route test; `:1096`–`:1103` (`"cursor=" not in source[index("catch(error)"):]` `:1103`); next test starts `:1106`/`:1111`, so "after `:1103`" is free | OK |
| 3-x29 | `test_x29_ladder_render.py` | `_js_function` `:40`; `refresh_pool=` `:54`, `post=` `:55`, `pool_rerenders_ladder` `:56`, final assert `:63`; `:44`–`:63` is the test | OK |
| 3-s3 | `test_s3_c3_panel_offline.py` | `:546`–`:550` `test_the_panel_script_posts_every_card_tap` | OK |
| 3-web | `web.py` | `radar` `:900` (decorator `:899`), `build_radar_panel(since=None, snapshot=True)` `:904`, FAILED log `:908`; imports `:75`, `:2014`, `:2040` | OK |
| 3-restarts | `restarts.py`, `jobs.yaml`, import chain | `ast.walk` `:133`, Import `:134`, ImportFrom `:136`; `jobs.yaml:90 imports: [cobalt.aset.__main__, cobalt.aset.web]`, `:194 imports: [cobalt.cli]`; `cli.py:82`, `voice/cli.py:29`, `voice/turn.py:43`, `voice/confirm.py:77` as cited; `grep -rln radar_panel src` = `aset/web.py` plus comments only in `voice/web.py:293`, `aset/drc_page.py:2` | OK |
| 3-misc | `pyproject.toml:30`, `radar_panel.md:55`/`:68`, `cards/store.py:1054`–`:1055` | `"playwright>=1.40.0"`; `:55` "The pool refresh loop is unchanged"; `:68` "Terminal cards are today's only"; `store.py:1054` `... WHERE state = ANY(%s) OR (state_at AT TIME ZONE 'America/New_York')::date = %s` | OK |
| 3-nojs | `grep -rln "playwright" tests/cobalt`; `grep -rlE "jsdom\|playwright\|quickjs\|mini_racer\|dukpy"` in `tests/` | none under `tests/cobalt` for playwright; hits only in `tests/test_browser_*.py`, `test_finviz_extractor.py` (none run `PANEL_JS`) | OK |
| 4a | reasoning on BASE text (no test run) | Tests (1) `tickLadder` absent, (2) body absent, (2b) body absent, (3) catch/`ladder-refresh-status` absent (`REFRESH FAILED` exists only in `refreshPool`), (4) `post()` has no `finally` (`:1537` catch only), (5) `refreshSeconds` already occurs once at `:1559`, so it is red only on its second half (`setInterval(tickLadder,interval)` absent). Route control: `render_ladder` shows `view.empty_message` in `.empty-state` (`:1446`–`:1447`) and `data-card-id` per card (`:1466`), so it is green on BASE. Controls read text that BASE already holds | OK |
| 4b | rule (2)/(4) vs rule (1)/(2b) | Rule (1) and (2b): the tick calls the existing `refreshLadder()` (`:1518`–`:1527`), which fetches and swaps in one function with no hook, and `refreshLadder` stays unchanged. Rule (2) and (4) and test (2): guards "checked again just before the swap", "a result that arrives while one holds is dropped, never swapped", "each guard appears both before the fetch and before the swap" in `tickLadder`'s body. `tickLadder` cannot interpose between the fetch and the swap inside `refreshLadder()`. A build can satisfy one set only: a second check inside `tickLadder` before a call to `refreshLadder()` is a pre-fetch check, and X1 ("including a result that lands after one of these began") cannot be met | **FAIL** |
| 4c | X1 vs rule (2) | X1 no longer lists "a card is open"; matches rule (2) | OK |
| 5a | card `files` columns; `## NOT IN THIS JOB` | row A: `radar_panel.py` (`PANEL_JS` only), `tests/cobalt/test_radar_panel.py`; row B: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`. No migration, table, setting, route or command (matches R411, R412) | OK |
| 5b | `## RECORDS` RESTARTS | `com.cobalt.aset com.cobalt.radar`, with the import chain above re-read; test file and DevDocs page are not residents | OK |
| 5c | `cobalt_dev` / L76 / `--deselect` in card | none named; the new tests monkeypatch `build_radar_panel` and read text, no DB | OK |
| 6a | `grep -n "«FILL" card` | no output (BASE already filled; TIP, CHECK REPORT, HOUSE B empty as intended). The draft report line 9 only quotes the old token | OK |
| 6b | `git diff --stat HEAD -- prompts/2026-10-06 ladder-refresh-draft ladder-refresh-amend`; `git log --oneline -2 -- <card, prompt 56, both reports>` | no diff for the card, prompt 56 or the two reports; `d8dc80dd`, `be853d53` | OK (committed, clean) |
| 6c | header sections order | `## ROWS`, `## NOT IN THIS JOB`, `## READ`, `## CHECK ASKS`, `## RECORDS`, bare headings | OK |

## ISSUES
- 4b FAIL: rule (2) "checked again just before the swap / a late result is dropped" and rule (4) "a tick result that lands after a `post()` started is dropped" cannot be built with `tickLadder` calling the unchanged `refreshLadder()` (rule (1), test (2b)); test (2)'s "guard before the fetch and before the swap" has no place to sit. Fix the card either way: (a) `tickLadder` does its own `fetch('/radar')`, parses, re-checks the guards and the send counter, then swaps and restores the open ids, and the `refreshLadder()` wording in rule (1), test (1) and (2b) changes to match; or (b) drop the late-result guard and say the guards are checked before the fetch only, with the `post()` race named as UNPROVEN.

(R556 `:100` in `## RECORDS` reads `:102` in the working copy and `:101` at BASE; the text says "at drafting", so not a FAIL.)

PREFLIGHT DONE · card: radar-ladder-refresh-54 · checks: 26 · fails: 1 · ready: NO
