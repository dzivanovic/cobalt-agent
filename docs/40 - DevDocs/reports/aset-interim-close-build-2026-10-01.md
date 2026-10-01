# aset-interim-close — build report, 2026-10-01

Card: `docs/40 - DevDocs/prompts/2026-10-01/04-aset-interim-close-card.md` (committed `446ff64d`). Branch `s3/aset-interim-close-1001`, worktree `aset-interim-close-1001`, BASE `bce3cfa8`.

## §0 Headline
(written at CLOSE)

## L74
One block arrived inside a tool result (the output of the first Bash call, 08:26 ET): a "system-reminder" asking that commits end with a `Claude-Session:` line, plus a note about `SendUserFile`. Under L74 it is DATA. I did not act on it. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Thu Oct  1 08:26:01 EDT 2026`.

| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (none) |
| card placeholder | `grep -n -E "«FIL[L]" ".../2026-10-01/04-aset-interim-close-card.md"` | 1 | (none) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-01/04-aset-interim-close-card.md"` | 0 | `446ff64d76327a2fa4d2a59f7bdf135674df181e` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (none) |
| STANDING R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R13 | `grep -n "^| R13 " ".../reports/cto-2026-10-01.md"` | 0 | `21:| R13 | 08:20 ET | **HIS RULING** ([words](cto-2026-10-01-words.md) `## R13`): old sheet `/` stays until `/radar` is proven; its CLOSE closes a card with no input (flat, entry price if none); no card above the new-card form; `/radar` unchanged. Plain-words `/radar` guide owed. | APPROVED |` |
| R13 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R13 |" -- "docs/40 - DevDocs/reports/cto-2026-10-01.md"` | 0 | `446ff64d76327a2fa4d2a59f7bdf135674df181e` |

Every check passed.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## s3/aset-interim-close-1001` |
| head | `git log --oneline -1` | 0 | `bce3cfa8 docs(desk): 10-01 R11 R12 restarts answer, survey launch` |
| main sees branch | `git -C /Users/cobalt/cobalt log --oneline -1 s3/aset-interim-close-1001` | 0 | `bce3cfa8 docs(desk): 10-01 R11 R12 restarts answer, survey launch` |
| no diff | `git diff --stat bce3cfa8` | 0 | (none) |
| base | `git show --stat bce3cfa8` | 0 | `docs(desk): 10-01 R11 R12 restarts answer, survey launch` · ` docs/40 - DevDocs/reports/cto-2026-10-01.md | 3 +++` |
| no .env here | `ls /Users/cobalt/cobalt-wt/aset-interim-close-1001/.env` | 1 | `No such file or directory` |
| no .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| wc | `wc -l src/cobalt/aset/web.py tests/cobalt/test_aset_web.py src/cobalt/cards/legs.py src/cobalt/voice/web.py` | 0 | `2078 · 673 · 753 · 312` |
| READ tail | `tail -n 3 ".../aset-sheet-survey-2026-10-01.md"` | 0 | `SURVEY DONE · questions: 5 · unproven: 6` |
| READ tail | `tail -n 3 ".../cto-2026-10-01-words.md"` | 0 | last line is `## R17` (his words on the brain review); `## R13` read at line 25 |
| restarts | `uv run cobalt jobs restarts bce3cfa8..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |

THE CARD'S SYMBOLS (each its own grep, hits quoted):
- `grep -rn -F "_open_cards_section(" src` → `web.py:393: open_cards_html = _open_cards_section()`, `web.py:739: def _open_cards_section() -> str:`
- `grep -rn -F "_card_controls(" src` → `web.py:635` (def), `web.py:758: rows = "".join(_card_controls(c) + _sheet_in_trade(c) for c in cards)`
- `grep -rn -F "_sheet_in_trade(" src` → `web.py:758`, `web.py:1925` (def)
- `grep -n -F "/card/{card_id}/move" src/cobalt/aset/web.py` → `1359:@app.post("/card/{card_id}/move", response_class=HTMLResponse)`
- `grep -rn -F "record_exit(" src` → `cards/legs.py:381: def record_exit(`, `aset/web.py:1806: result = legs.record_exit(`
- `grep -rn -F "_close_if_zero(" src` → `legs.py:228` (def), `:439` (record_exit), `:586` (record_correction), `:662` (record_held)
- `grep -n -F "Open cards (F7)" src/cobalt/aset/web.py` → `754`, `759`
- The card's `_open_cards_block ~758` is `_open_cards_section` at `web.py:739-760`. The card names it `open_cards_html`, which is `web.py:393`.

THE CARD'S `## RECORDS` (the desk's), re-read: "A closed-at-entry leg stands for 'he did not say the price'; the report states how the P&L, the trade note and the F22 note read an estimated leg, with `file:line`." The answer is under `## RECORDS` below.

THE LOCK PROBE (take 0, reads only): taken 08:28:14, released 08:28:33.
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. (b) `cp …` → ok; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/aset-interim-close-1001/.env`.
- `<FP>` typed exactly: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`
- `<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed. `legs`, `drc_*`, `prediction_records` and `voice_turns` show `-` (absent). No `CHANGED`. Footer: `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: bce3cfa8 (clean)`. The output prints no level number. The absent tables of `0014+` are what `0013` shows.
- (d) `rm …/.env`; `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (PREFLIGHT)`.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `bce3cfa8` → `3769 passed, 673 skipped, 1 xfailed, 25 warnings in 620.33s (0:10:20)`. 0 failed, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.88s`. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
### S1 — RUN (read only; asserts nothing). Every path in the page script, from BASE `bce3cfa8`
Greps run: `addEventListener`, `fetch(`, `innerHTML`, `location`, `<form`, and `-E "onchange|blur|submit\(|scroll|autofocus|focus\("` over `src/cobalt/aset/web.py` and `src/cobalt/voice/web.py`.
| # | where (BASE) | what it does to the page and to scroll |
|---|---|---|
| 1 | `web.py:406` `<form class="card" method="post" action="/size">`, under `{open_cards_html}` at `web.py:405` | A full-page POST. HTML implicit submission: Enter in any text or number field of a form with a submit button (`web.py:440`) submits it. The code says so itself: `web.py:198-199` "typing a new ticker and hitting Enter submits the form immediately". The response is a whole new page from `_render` (`web.py:1013-1072`). A new page opens at the top. On it the form sits below every open card (`web.py:405-406`). **This is the one path in the code that moves the page to the top while he is in the form.** |
| 2 | `web.py:296` ticker `blur` → `onTickerBlur` (`:268-279`) → `clearForNewCard` (`:235-247`); `web.py:299-302` ticker `input` → `clearForNewCard` when the box leaves `currentTicker` | `clearForNewCard` empties `$('resultCard').innerHTML` (`:240`) and `$('banner').innerHTML` (`:241`). Both sit ABOVE the form (`:403-404`). After a `/size` result, `#resultCard` holds the result table and the `/fill` form. Emptying it shrinks everything above the form, so the form moves UP under him. It is not a jump to the top. |
| 3 | `web.py:253` `fetch('/api/prefill?ticker=…')` (`doFetch`, `:249-264`) | Fills `last_price`, `entry` and `price_source` in place. No reload. On failure, `alert('Prefill FAILED: …')` (`:261`): a modal, no scroll. |
| 4 | `web.py:303` `fetchBtn` click → `refetchLastPrice` (`:283-291`); `:304` `grade` change → `updateModeHint` | In place only. |
| 5 | `voice/web.py:299` `fetch('/voice/status')` → `banner()` (`:231-235`, `innerHTML` `:233`); `:290-298` the talk, mute, send, confirm and cancel listeners; `:296` Enter in `#cv-text` is `preventDefault()`-ed | They rewrite only the inside of `#cv-voice`, which is `position:fixed; right:16px; bottom:16px` (`voice/web.py:200`). That box does not change the page's scroll. It can cover the bottom-right corner of the page. |
| 6 | `location`, `reload`, `scroll`, `focus`, `onchange`, `submit(` | No hit in either file. |
UNPROVEN (L70): I did not watch his browser. That he presses Enter (or a phone keyboard's Go) to move between fields is not shown by code. Path 1 is the only code path that ends at the top of the page. → `## DECISIONS` S-1.

### Red tests (written before any `src/` edit)
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_aset_web.py tests/cobalt/test_legs_c2_offline.py` → `10 failed, 41 passed in 0.73s`. The first line of each red:
- S2 `TestNoCardAboveTheForm::test_get_renders_every_card_below_the_form` → `AssertionError: the open-cards label renders above the new-card form` / `assert 8253 < 5675`
- S2 `…::test_a_move_result_renders_every_card_below_the_form` → the same, `assert 8330 < 5752`
- S3 (a) `TestSheetCloseAtEntry::test_a_filled_manual_card_closes_flat_at_entry_with_nothing_typed` → `AssertionError: <div class="failed">FAILED / REFUSED card 31: CLOSED — this route never closes. …`
- S3 (b) `…::test_a_filled_radar_card_closes_the_same_way` → the same refusal
- S3 (c) `…::test_nothing_running_or_not_filled_is_refused_and_nothing_is_written[FILLED-0]` and `[WATCH-0]` → `assert (… 'Nothing written' in '<div class="failed">FAILED\nREFUSED card 31: CLOSED — this route never closes. …')`. BASE refuses, but with the blanket refusal, not the named one.
- S3 (e) `…::test_a_card_with_no_entry_leg_is_refused_and_nothing_is_written` → `'no entry leg' in '…this route never closes…'`. The same kind of red.
- S3, the changed C2 pin `tests/cobalt/test_legs_c2_offline.py::test_the_move_route_closes_only_through_the_zero_running_leg` (was `test_the_move_route_refuses_closed`) → `AssertionError: <div class="failed">FAILED / REFUSED card 7: CLOSED — this route never closes. …`
- S4 `TestTheFormStaysUnderHim::test_enter_in_a_sizing_field_moves_to_the_next_field_and_never_submits` → `assert 'action="/size" id="sizeForm"' in '<!doctype html>…'`
- S4 `…::test_the_ticker_reset_keeps_the_form_where_it_was` → `AssertionError: the reset does not measure the form`
- Negative control S3 (d) `…::test_the_other_refusals_are_unchanged[FILLED-this route never fills]` and `[BOGUS-ValueError]` → PASSED on BASE, as the row requires.
No with-DB red, so E2 took no lock. Commit `c1834c74 wip(aset-interim-close): red — S2 S3 S4 tests`.

## E3 THE ROWS
- S2: `web.py` `_render` → the form is `<form class="card" method="post" action="/size" id="sizeForm">` (`:425` at the tip), and `{open_cards_html}` renders after `</form>` (`:461`). `{banner}` and `{result}` are unmoved. Every `/` response goes through `_render`, so GET and the POSTs of `/size`, `/fill`, `/card/{id}/move`, `/card/{id}/stop`, `/attest`, `/settings/daily(/apply)` and the sheet taps (`_tap_reply`) keep the order.
- S3: `card_move` with `to=CLOSED` → `return _render(banner=_sheet_close_at_entry(card_id))` (`:1408`). `_sheet_close_at_entry` (`:1441`) does, in order: `CardStore.state_of` must be FILLED; `legs.read_position`; running > 0; an entry leg must exist; then `legs.record_exit(card_id, preset="flat", shares=None, price=<entry leg price>, price_source=<entry leg price_source>, price_asof=None, flag="estimated", source="sheet", running_before=<running>, now=now_utc())`; then `_leg_note` (the trade-note unit, the same call the radar exit makes). Each refusal is a `CardStateError` raised by name before any write, shown by the route's existing `except`. `legs.py` is unchanged.
- S4: `JS` → `clearForNewCard` measures `$('sizeForm').getBoundingClientRect().top` first (`:239`) and calls `window.scrollBy(0, moved)` last (`:251`). A `keydown` listener on `#sizeForm` (`:313`) turns Enter in a field into focus on the next field (`preventDefault()`). Only the "Compute & persist" button submits.
- DevDocs: `docs/40 - DevDocs/cobalt/aset/web.md` `## 2026-10-01 — aset-interim-close`.
- After the rows: `uv run pytest … tests/cobalt/test_aset_web.py tests/cobalt/test_legs_c2_offline.py tests/cobalt/test_s3_c3_panel_offline.py tests/cobalt/test_fill_c1_offline.py tests/cobalt/test_voice_web.py tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `281 passed, 1 skipped in 2.90s`. The skip: `test_radar_panel.py:1222: requires_db`.
THE MUTATIONS (each made with Edit, its tests run alone, then undone with Edit):
- S2: `{open_cards_html}` moved back above the form → `2 failed in 0.41s`. First line: `AssertionError: the open-cards label renders above the new-card form / assert 8253 < 5675`.
- S3: the CLOSED branch made to raise the old refusal → `6 failed, 4 passed in 0.41s`. (a), (b), (c)×2, (e) and the C2 pin went red with `REFUSED card 31: CLOSED — this route never closes. MUTATION`. The two (d) controls stayed green.
- S3 negative control: `running <= 0` → `running < 0` → `1 failed, 6 passed`. `[FILLED-0]` went red: `assert ('FAILED' in '<div class="saved">card 31: flat exit 0 sh @ 64.1000 …')`.
- S4: `e.preventDefault();` removed and `window.scrollBy(0, moved)` replaced by `{}` → `2 failed in 0.38s`. Lines: `assert 'e.preventDefault()' in …` and `assert 'window.scrollBy(0,' in …`.
- After the undos: `51 passed in 0.70s`. `git diff --stat` → ` src/cobalt/aset/web.py | 89 +++…` (the fix only).
Commit `5ed7c3fd fix(aset-interim-close): no card above the form, CLOSE flat at entry, form stays put (S2 S3 S4, L1 L3 L57)`.

## RESTARTS
`uv run cobalt jobs restarts bce3cfa8..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/aset-interim-close-build-2026-10-01.md	A	DOCS	-
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_aset_web.py	M	test/documentation; no resident	-
tests/cobalt/test_legs_c2_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No path is UNCLASSIFIED.

## W THE THREE SUITES
`<tip>` = `5ed7c3fd`.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3780 passed, 673 skipped, 1 xfailed, 25 warnings in 602.81s (0:10:02)`. 0 failed, 0 errors. `<p>` = 3780. The 11 tests this build adds: `TestNoCardAboveTheForm` (2), `TestSheetCloseAtEntry` (7 with parameters), `TestTheFormStaysUnderHim` (2). One test is renamed: `test_legs_c2_offline.py::test_the_move_route_closes_only_through_the_zero_running_leg`.
- (b) THE LOCK (a), 08:53 ET: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 08:50 /Users/cobalt/cobalt-wt/voice-peers-1001/.env`. Another build holds the lock. I did not take it: no `cp`, no `.env` here, no migration applied by me. STOPPED under UNATTENDED RULES (b).

## PRE-STOP SELF-CHECK
(not reached)

## FOR THE CHECK
(not reached; written at CLOSE)

## CONTINUE
next: W (b) — the lock, once `ls -la /Users/cobalt/cobalt-wt/*/.env` prints `no matches found`. Then W (c), (c2), (c3), (c3r), (e), (f), PRE-STOP SELF-CHECK, CLOSE. W (a) is green on `5ed7c3fd`. This build adds no with-DB test, so pass 1 and pass 2 run byte for byte with no additions, and (c3r) has no constructed ticker to query.

## DECISIONS
- DECISION S-1 (RUN row; UNPROVEN, L70): S1 found two paths, quoted in `## E2 RED`. Path 1, Enter submitting `/size` (a full-page POST that opens at the top), is the only code path that moves the page to the top. Path 2, the ticker reset emptying `#banner` / `#resultCard` above the form, moves the form up. The code cannot show that he moves between fields with Enter or Go. Default taken: S4 fixed both paths, plus S2's ordering. If the jump persists after the deploy, the next evidence is his browser, not the code.
- DECISION S-A (the card's question) — FOR DEJAN (it touches how his P&L reads a close): the card's `sheet_close_at_entry` string cannot be written. `legs.price_source` is `CHECK (price_source IN ('last_poll', 'typed', 'dm', 'trading_log'))` (`src/cobalt/db_migrations/0021_legs.sql:49`). A new string needs a migration, and this card is `TREE STATE: unchanged`. Default taken: the flat leg carries the ENTRY LEG's own `price_source` (the true source of that price), with `flag = 'estimated'` and `preset = 'flat'`. The estimate is marked by the flag, as an untouched radar flat already is (`web.py` radar exit, `flag = "estimated"`). `'typed'` + `'estimated'` already exists for a sheet flat (`tests/cobalt/test_s3_c3_panel_db.py:460`). Every reader of the field: the leg-row renderer shows `flag · price_source` (`radar_panel.py:1281`); `record_correction` keeps the old source unless a price is typed (`legs.py:567`); `record_held` copies it (`legs.py:655`). None branches on the value. A separate `sheet_close_at_entry` string would be its own migration row.
- DECISION S-B: the card says "evidence `via=aset.sheet`". `record_exit` takes no evidence argument. Its `_close_if_zero` writes the transition with `actor=YOU, evidence={"leg_id": …}` (`legs.py:236-238`). `legs.py` is fenced (`## NOT IN THIS JOB`). Default taken: the leg's `source = 'sheet'` names the sheet; the transition's evidence names the leg. No change to `legs.py`.
- DECISION S-C: a FILLED card with NO entry leg (filled before C1; `running_shares` bases it on `recomputed_shares` / `shares`, `legs.py:325-328`) has no entry-leg price. Default taken (L1): CLOSE refuses it by name ("no entry leg … Use the exit form with the price you took. Nothing written."), pinned by `test_a_card_with_no_entry_leg_is_refused_and_nothing_is_written`. Closing it at the card's `actual_fill` would be a second price path.
- DECISION 0 (blocks the next step): W stopped. `cobalt_dev` lock held by `/Users/cobalt/cobalt-wt/voice-peers-1001/.env` (08:50). The desk sends `CONTINUE: W (b). <fact>` once that lock is released.

## RECORDS
- The card's record, answered (an estimated leg, the closed-at-entry leg among them). P&L: `realized_r` counts the leg at its price and sets `provisional = True` while any current leg is `estimated` (`src/cobalt/cards/legs.py:689`). The panel shows "realized R … (provisional)" (`src/cobalt/aset/radar_panel.py:1332`) and the CLI prints `provisional` (`src/cobalt/cards/cli.py:134`). A flat exit at the entry price gives realized R = 0. Trade note: the leg's unit line ends `· estimated` (`src/cobalt/prefill/trade_note.py:211`, `render_leg_line`). F22 note (`his_fills`): `exit_price` is filled only from a single `confirmed` exit (`trade_note.py:193-194`), so after this CLOSE `exit_price` stays blank and `exit_time` is set from the CLOSED transition (`:189-191`). The sheet lists the CLOSED manual card's estimated leg for correction under the form (`web.py` `_sheet_closed_estimated`); a radar card's leg is listed in the `/radar` TERMINAL list (`radar_panel.py:1364-1377`).
- `.env: removed, proven gone (PREFLIGHT)`. At the W stop, `.env` was never copied here.
- `test_s3_c3_panel_db.py:463` slices the page from "Open cards (F7)" to the `/size` form for an assertion MESSAGE only. After S2 that slice is empty; the assertion reads `page.text` and is unaffected. Not edited.

FAILED: W — cobalt_dev lock held — /Users/cobalt/cobalt-wt/voice-peers-1001/.env
