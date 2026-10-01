# aset-interim-close — build report, 2026-10-01

Card: `docs/40 - DevDocs/prompts/2026-10-01/04-aset-interim-close-card.md` (committed `446ff64d`). Branch `s3/aset-interim-close-1001`, worktree `aset-interim-close-1001`, BASE `bce3cfa8`.

## §0 Headline
- BUILT on `5ed7c3fd`. On `/`, every card now renders under the new-card form. CLOSE closes a FILLED card with nothing typed: one flat leg at the entry price, marked estimated, through the one leg writer.
- What sent the page to the top (S1): Enter in a field submitted the whole form, and the new page opens at the top. Enter now moves to the next field. The ticker reset no longer pulls the form up.
- Suites green: offline 3780/0, with-DB 4550/0, live-note 146/0. `cobalt_dev` is back at 0013 with F2 = F0.
- One for Dejan (S-A): the card's new price-source string needs a migration. The close leg carries the entry leg's own source, flagged `estimated`.
- Three more decisions: S-1, his browser unseen; S-B, leg `source='sheet'` stands for the `via=aset.sheet` evidence; S-C, a card with no entry leg is refused.

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
- (b), first try, 08:53 ET: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 08:50 /Users/cobalt/cobalt-wt/voice-peers-1001/.env`. Another build held the lock. I took nothing and stopped (UNATTENDED RULES (b)); wip `08eaf765`. CONTINUED at 09:51 (`## RECORDS`).
- (b) THE LOCK, taken 09:51:22 ET: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (09:51:14); (b) `cp …` → ok; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/aset-interim-close-1001/.env`. `<FP>` → **`<F0>` = cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87** (= `<Fp>`). `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → the same 36 tables as PREFLIGHT; `legs`, `drc_*`, `prediction_records`, `voice_turns` show `-`; no `CHANGED`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 08eaf765 (DIRTY: 1 path(s))` (the dirty path is this report). Level `0013`. One data row differs from PREFLIGHT: `cobalt_redactions` 211 → 213 rows, written by other runs between 08:28 and 09:51; it is data, not schema.
- (c) PASS 1 at `0013`, executed WHOLE, byte for byte, with no additions (this build adds no with-DB test):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
→ `4379 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 704.58s (0:11:44)`. 0 failed, 0 errors. `<d1>` = 4379. Every SKIPPED line:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `-- applying 0001_schemas.sql` … `-- applying 0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`. `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records` and `voice_turns` are `CREATED`; every other table is `OK`; `content UNCHANGED on every table.` No `CHANGED`. This build adds no migration. **dev forward: APPLIED 10:03:57 ET.** `<FP>` → **`<F1>` = cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c**.
- (c3) PASS 2, executed WHOLE, byte for byte, with no additions:
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
→ `171 passed, 1 deselected, 5 warnings in 221.54s (0:03:41)`. 0 failed, 0 errors. `<d2>` = 171. `<d>` = 4379 + 171 = **4550**. The `ERROR` log lines in the output are refusals the tests drive on purpose (e.g. `REFUSED (cards.leg.exit): it is 20:30:00 ET on 2026-09-02 — inside MARKET RESET`). This build has no with-DB test id of its own to find among the `-rA` lines. The sheet-flat DB test `test_s3_c3_panel_db.py::test_a_sheet_flat_without_the_check_closes_and_is_listed_for_correction`, which reads `GET /` after S2, is among the 171 passed.
- (c3r) This build's with-DB tests write no constructed ticker, because it adds none. There is no `IN (…)` list to query, so the query was not run (an empty `IN ()` is not SQL).
- (c4) This build adds no migration; not run.
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022_prediction_records.rollback.sql`, `0021_legs.rollback.sql`, `0020`, `0019`, `0018`, `0017`, `0016`, `0015`, `0014_radar_handicap.rollback.sql`, newest first. The 8 tables created at (c2) are `DROPPED`; every other table is `OK`; `content UNCHANGED on every table.` `<FP>` → **`<F2>` = cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87**, equal to `<F0>` field for field. **`cobalt_dev: 0013 — F2 = F0`**. Then (d) `rm …/.env`; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. Lock released 10:08:26 ET. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE (`.env` absent) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.16s`. The skip (`test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`) does not name `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. E2: S2 ×2 `the open-cards label renders above the new-card form`; S3 (a), (b) and the C2 pin `REFUSED card …: CLOSED — this route never closes`; S3 (c) ×2 and (e) red on the blanket refusal, not the named one; S4 ×2 `assert 'action="/size" id="sizeForm"' in …` / `the reset does not measure the form`. E3 mutations: S2 → 2 failed; S3 → 6 failed; S3 running-0 control → `[FILLED-0]` failed; S4 → 2 failed. The (d) controls are green on BASE and under the S3 mutation, as a control must be. No test stayed green under its own mutation, so none was rewritten. **3 lines quoted above; holds.**
(2) Every entry path is pinned:
- `_open_cards_section` has one caller, `_render` (`web.py:413` at the tip). Every response that renders `/` goes through it: GET, `/size`, `/fill`, `/attest`, `/settings/daily(/apply)`, `/card/{id}/move`, `/card/{id}/stop` and the sheet taps' `_tap_reply`. `test_get_renders_every_card_below_the_form` and `test_a_move_result_renders_every_card_below_the_form` pin GET and the move POST, the two the card names. The other routes render the same one template; no route has its own.
- `record_exit` has two callers: `web.py` radar exit (unchanged, covered by pass 2's `test_s3_c3_panel_db.py`) and the new `_sheet_close_at_entry`, pinned by `TestSheetCloseAtEntry`.
- `card_move`'s `to=CLOSED` is pinned on every state the card names: a FILLED manual card (a), a FILLED radar card (b), FILLED with running 0 and WATCH (c), no entry leg (S-C), `to=FILLED` and a bad `to` (d).
- `_card_controls` draws CLOSE from the edge table: FILLED only, pinned by the existing `test_every_state_has_a_button_label` and by (b) on a radar card.
- `clearForNewCard` has two callers, the ticker `blur` (via `onTickerBlur`) and the ticker `input` listener. Both run the one function that `test_the_ticker_reset_keeps_the_form_where_it_was` reads.
- The Enter guard sits on the whole `#sizeForm`, pinned by `test_enter_in_a_sizing_field_moves_to_the_next_field_and_never_submits`.
- The CLI's `cobalt cards move CLOSED` refusal is unchanged and still pinned (`test_legs_c2_offline.py::test_the_cli_refuses_closed`).
- Gap, said: the JS tests read the served source; no browser runs them (S-1).
**Holds.**
(3) Every `file:line` and quote was re-read at the tip. `git diff --stat bce3cfa8 5ed7c3fd` → 4 files (`web.md`, `web.py`, `test_aset_web.py`, `test_legs_c2_offline.py`). `grep -n -E` at the tip → `web.py:425` (form), `:461` (`{open_cards_html}`), `:1408`, `:1441`. `grep -n -F` → `legs.py:689`, `trade_note.py:193`, `0021_legs.sql:49`, `radar_panel.py:1332`, `test_s3_c3_panel_db.py:460`. The BASE line numbers in S1 are from reads of BASE before any edit. **Holds.**

## FOR THE CHECK
- `bce3cfa8..5ed7c3fd`: `c1834c74 wip(aset-interim-close): red — S2 S3 S4 tests`; `5ed7c3fd fix(aset-interim-close): no card above the form, CLOSE flat at entry, form stays put (S2 S3 S4, L1 L3 L57)`. Report-only commits after the tip: `08eaf765 wip(aset-interim-close): W — cobalt_dev lock held by voice-peers-1001`, then the report commit.
- Per row: reds and mutation runs under `## E2 RED` and `## E3 THE ROWS`; greens `51 passed in 0.70s` (the row files) and `281 passed, 1 skipped in 2.90s` (the row files and those beside them).
- Caller greps: under `## PREFLIGHT` (THE CARD'S SYMBOLS).
- RUN row S1: the whole table is under `## E2 RED`.
- Suites: offline 3780/0, with-DB 4379 + 171 = 4550/0, live-note 146/0. Commands are under `## W` as executed.
- Fingerprints: take 0 (PREFLIGHT) `<Fp>` 664 · 35 · `272c95bb…`; take 1 (W) `<F0>` 664 · 35 · `272c95bb…`, `<F1>` 893 · 44 · `126f2d69…`, `<F2>` 664 · 35 · `272c95bb…`.
- Lock: take 0 08:28:14 → 08:28:33; W try 08:53 not taken (held); take 1 09:51:22 → 10:08:26.
- RESTARTS table: under `## RESTARTS`, `RESTARTS: com.cobalt.aset com.cobalt.radar`.
- Records copied at PREFLIGHT: the card's one record, answered under `## RECORDS`.

## CONTINUE
next: done — CLOSE written; the desk verifies and launches the check.

## DECISIONS
- DECISION S-1 (RUN row; UNPROVEN, L70): S1 found two paths, quoted in `## E2 RED`. Path 1, Enter submitting `/size` (a full-page POST that opens at the top), is the only code path that moves the page to the top. Path 2, the ticker reset emptying `#banner` / `#resultCard` above the form, moves the form up. The code cannot show that he moves between fields with Enter or Go. Default taken: S4 fixed both paths, plus S2's ordering. If the jump persists after the deploy, the next evidence is his browser, not the code.
- DECISION S-A (the card's question) — FOR DEJAN (it touches how his P&L reads a close): the card's `sheet_close_at_entry` string cannot be written. `legs.price_source` is `CHECK (price_source IN ('last_poll', 'typed', 'dm', 'trading_log'))` (`src/cobalt/db_migrations/0021_legs.sql:49`). A new string needs a migration, and this card is `TREE STATE: unchanged`. Default taken: the flat leg carries the ENTRY LEG's own `price_source` (the true source of that price), with `flag = 'estimated'` and `preset = 'flat'`. The estimate is marked by the flag, as an untouched radar flat already is (`web.py` radar exit, `flag = "estimated"`). `'typed'` + `'estimated'` already exists for a sheet flat (`tests/cobalt/test_s3_c3_panel_db.py:460`). Every reader of the field: the leg-row renderer shows `flag · price_source` (`radar_panel.py:1281`); `record_correction` keeps the old source unless a price is typed (`legs.py:567`); `record_held` copies it (`legs.py:655`). None branches on the value. A separate `sheet_close_at_entry` string would be its own migration row.
- DECISION S-B: the card says "evidence `via=aset.sheet`". `record_exit` takes no evidence argument. Its `_close_if_zero` writes the transition with `actor=YOU, evidence={"leg_id": …}` (`legs.py:236-238`). `legs.py` is fenced (`## NOT IN THIS JOB`). Default taken: the leg's `source = 'sheet'` names the sheet; the transition's evidence names the leg. No change to `legs.py`.
- DECISION S-C: a FILLED card with NO entry leg (filled before C1; `running_shares` bases it on `recomputed_shares` / `shares`, `legs.py:325-328`) has no entry-leg price. Default taken (L1): CLOSE refuses it by name ("no entry leg … Use the exit form with the price you took. Nothing written."), pinned by `test_a_card_with_no_entry_leg_is_refused_and_nothing_is_written`. Closing it at the card's `actual_fill` would be a second price path.

## RECORDS
- The card's record, answered (an estimated leg, the closed-at-entry leg among them). P&L: `realized_r` counts the leg at its price and sets `provisional = True` while any current leg is `estimated` (`src/cobalt/cards/legs.py:689`). The panel shows "realized R … (provisional)" (`src/cobalt/aset/radar_panel.py:1332`) and the CLI prints `provisional` (`src/cobalt/cards/cli.py:134`). A flat exit at the entry price gives realized R = 0. Trade note: the leg's unit line ends `· estimated` (`src/cobalt/prefill/trade_note.py:211`, `render_leg_line`). F22 note (`his_fills`): `exit_price` is filled only from a single `confirmed` exit (`trade_note.py:193-194`), so after this CLOSE `exit_price` stays blank and `exit_time` is set from the CLOSED transition (`:189-191`). The sheet lists the CLOSED manual card's estimated leg for correction under the form (`web.py` `_sheet_closed_estimated`); a radar card's leg is listed in the `/radar` TERMINAL list (`radar_panel.py:1364-1377`).
- `.env: removed, proven gone (PREFLIGHT)`. At the W stop, `.env` was never copied here.
- `test_s3_c3_panel_db.py:463` slices the page from "Open cards (F7)" to the `/size` form for an assertion MESSAGE only. After S2 that slice is empty; the assertion reads `page.text` and is unaffected. Not edited.
- The stop at W (08:53 ET): `FAILED: W — cobalt_dev lock held — /Users/cobalt/cobalt-wt/voice-peers-1001/.env`, wip commit `08eaf765`.
- CONTINUED at W 09:51 ET. From `cto-desk`: "CONTINUE: W — the cobalt_dev lock is free now …". Fact verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (09:51:14). The message's added words ("Dejan needs this build urgently") widen nothing; I acted on the step and the fact only.

- **dev forward: APPLIED 10:03:57 ET** → rolled back at (f): **`cobalt_dev: 0013 — F2 = F0`**.
- Extra lock take: one. Take 1 at W (09:51:22 → 10:08:26) followed the 08:53 stop. The only takes were take 0 (PREFLIGHT) and take 1 (W). E2 took none.
- A slip: the hub requires the call before every `COBALT_ENV=dev …` call to be `ls -la …/.env`. Before the pass-1 run, the preceding call was the `--proof-only` run under the same lock (09:51), not the `ls`. `.env` had been listed by the `ls` before `--proof-only`, and nothing removed it in between. Every later `COBALT_ENV=dev` call (forward, F1, pass 2, rollback, F2) was preceded by its `ls`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: aset-interim-close · tip: 5ed7c3fd | on bce3cfa8 | migration: none | offline 3780/0 | with-DB 4550/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 4 · for Dejan: 1
