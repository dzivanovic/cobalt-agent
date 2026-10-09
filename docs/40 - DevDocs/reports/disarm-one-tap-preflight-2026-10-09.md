# Card 134 (DISARM one-tap) preflight · 2026-10-09 · read-only
Main HEAD `1458693d`. Card `prompts/2026-10-08/134-disarm-one-tap-card.md`, job `disarm-one-tap-1008`. 24 checks, 0 fails, 9 notes (moved lines). Ready YES.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 0a | `grep -n "refuse" ops/desk/desk-launch.sh`, build mode (`:686`–`:762`, `:895`–`:914`) vs the header | card path `…/prompts/2026-10-08/134-disarm-one-tap-card.md` is absolute, ends `-card.md`, chars in `[A-Za-z0-9 ._/-]`, no `..`; `grep -c "«FILL"` 0; `## ROWS` present | OK |
| 0b | `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` | all seven non-empty; `TIP`, `CHECK REPORT`, `HOUSE B` empty (build, per `CARD.md`); no `TAG`, no `TREE STATE`, no `DB` line | OK |
| 0c | JOB / BRANCH / WORKTREE rules (`:732`–`:757`) | `disarm-one-tap-1008` is `[a-z0-9-]`; `ops/disarm-one-tap-1008` plain; worktree one name, not `agy-trial` | OK |
| 0d | REPORT rule (`:901`–`:904`) | `/Users/cobalt/cobalt-wt/disarm-one-tap-1008/docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md` sits inside the worktree | OK |
| 0e | worktree / branch absent (`:905`–`:911`): `git rev-parse --verify --quiet refs/heads/ops/disarm-one-tap-1008`; `ls /Users/cobalt/cobalt-wt` | exit 1; no `disarm-one-tap-1008` dir | OK |
| 0f | card committed and clean (`:760`–`:762`): `git log -1 --format=%h -- <card>`; `git status` | `1458693d`; not in the status list | OK |
| 1 | BASE `6f55636b`: `hex8`; `git merge-base --is-ancestor 6f55636b HEAD` | 8 hex, a main commit, exit 0 (see NOTE 1) | OK |
| 2 | RULINGS `2026-10-08 R689`: `grep -n "^| R689 " reports/cto-2026-10-08.md`; `git show HEAD:…cto-2026-10-08.md` | one row, `:42`, `HIS RULING … APPROVED · HIS RULING · APPLIED`, same text in HEAD; working-tree diff only drops an unrelated OWED line | OK |
| 3 | draft report committed: `git log -1 --format=%h -- reports/disarm-one-tap-draft-2026-10-08.md`; decisions file read | `b8603d50`; decisions file: D1–D7 KEEP, D6 BASE refill | OK |
| 4 | `radar_panel.py` DISARM block: `grep -n "DISARM_TAP\|ARM_BUTTON"` | `:1178` comment, `:1179 ARM_BUTTON = '<button class="arm-key">ARM</button>'`, `:1180`–`:1183 DISARM_TAP = (` text input `maxlength="80" placeholder="disarm reason (required)"` + `DISARM` button; `:1435 _card_form(card.id, '/disarm', DISARM_TAP, source='panel')` | OK |
| 5 | `radar_panel.py` ARMED block `:1427`–`:1436` | `elif card.state is CardState.ARMED:`; `:1433 /triggered`; `:1434` comment `R627: ARMED -> WATCH, his tap with a reason the store requires.`; `:1435` the DISARM form | OK |
| 6 | `_hidden_input :1190`, `_card_form :1201`–`:1214`, `_dot_html :1116`–`:1141` | all at the cited lines; `_card_form` rewrites `<button` to `<button type="button" data-tap="1"` (the card's expected chip markup) | OK |
| 7 | `PANEL_CSS` `:1523`, `:1532` | `:1523` holds `.tap-strip{display:grid;…}.tap-strip[hidden]{display:none}`; `:1532 .s3-form button.arm-key{min-height:44px;padding:0 14px}` | OK |
| 8 | `PANEL_JS` click handler `:1575`–`:1584` | `:1575`–`:1576` `[data-dot-toggle]` toggles `dot.parentElement.querySelector('.tap-strip')`, before `:1583`–`:1584` `[data-tap]`; `:1577`–`:1578` takes only `.tap-strip [data-grade]`; `:1584` posts every `input[name]` of the `[data-card-tap]` block | OK |
| 9 | tick guards: `grep -n "tap-strip:not"` | `:1614` and `:1626` (card cites `:1609`, `:1620`) | OK · NOTE 2 |
| 10 | `web.py:2020`–`:2033` | `@app.post("/radar/card/{card_id}/disarm")` at `:2020`; `:2025 reason = form.get("reason", "").strip()`; `:2026`–`:2028` the 80-char `_TapInputRefused`; `:2030 reason=reason or None`; `:2033 return await _card_tap(…)` | OK |
| 11 | `web.py` import `:75`–`:82`, `_TapInputRefused :1672`, `_card_tap :1775`–`:1796`, 422 at `:1788`–`:1789`, `askReason :174`–`:179` / `:713` | all as cited; `from .radar_panel import (` block lists six names | OK |
| 12 | `cards/store.py _assert_reason` | `:384`–`:410` (card `:383`–`:410`; `:383` is the `@staticmethod` line); empty ARMED → WATCH reason raises `CardStateError` | OK |
| 13 | the panel is the only caller: `grep -rn "/disarm" src` | `radar_panel.py:1435` and the route `web.py:2020`; the sheet posts `/card/{id}/move` | OK |
| 14 | reason becomes required with a test: card rows A and B read against `test_s3_c3_panel_offline.py` | row A: the parametrized off-list test refuses `{}`, `"   "`, an off-list word, `x*81` and `"Setup broke"` (422, `calls == []`); the three old tests (`:256`–`:262`, `:265`–`:271`, `:274`–`:282`), `:285`–`:295` and the market-reset param `:469` all at the cited lines | OK |
| 15 | red on BASE for the stated reason: `grep -rn "DISARM_REASONS\|disarm-chips\|disarm-toggle\|_disarm_chips" src tests`; read of `:2020`–`:2033` and `:1181` | no hit: the chip test fails at collection (no `DISARM_REASONS`). `{}` / `"   "` reach the store (409), `"spread blew out"` and `"Setup broke"` pass (200), `x*81` answers the 80-char text, not the new one. `:1181` renders `<input name="reason"` and `disarm reason (required)` | OK |
| 16 | controls green on BASE: `test_radar_panel_cards.py` `ARM_TAP`, `BASE_*_SHA256`, `test_the_sheet_keeps_its_arm_and_disarm_buttons`, `POST_ALLOWLIST`; `test_radar_panel.py` `TICK_GUARDS` | all exist and assert what the card says; row C's seam test asserts on `PANEL_JS` text only (CONTROL, green on BASE); no route added | OK · NOTE 3–7 |
| 17 | ladder pin: `grep -n "PIN_HEALTHY" test_radar_panel_cards.py` | `PIN_HEALTHY_LADDER_SHA256 = "9a52577c…"` — matches the card's `was 9a52577c…`; 118, 137 and 126 left it unchanged, so the re-capture is still the card's to do | OK · NOTE 5 |
| 18 | every new test offline: both test files for DB marks | new tests use `GatedCards` recorders, rendered markup and `PANEL_JS` text; the DB-reaching tests in both files are the existing `skipif` ones, not the card's | OK |
| 19 | no new command beyond existing scripts (R411, R412): `grep -n "restarts" src/cobalt/jobs/cli.py` | the card adds none; row E is `cobalt jobs restarts` (`cli.py:194`, `:196`) | OK |
| 20 | RESTARTS class home per path, `src/cobalt/jobs/restarts.py` | `src/` → `static import reach` `:220`; `tests/` → `test/documentation; no resident` `:245`–`:246`; `docs/` → `DOCS` `:225`–`:228`; `jobs.yaml:90` `imports: [cobalt.aset.__main__, cobalt.aset.web]` (aset), `:194` `imports: [cobalt.cli]` (radar). Expected `com.cobalt.aset com.cobalt.radar` stands; not run (read-only) | OK |
| 21 | cards 118, 137, 126 landed in BASE: `git merge-base --is-ancestor b67c96c6 6f55636b`; same for `8f42bf2e` | both exit 0 (stt-model-fix and radar-display-fix are in BASE) | OK |
| 22 | BASE vs HEAD code: `git diff --stat 6f55636b HEAD -- src tests configs` | empty — `1458693d` is docs only, so every cite above holds at BASE too | OK |
| 23 | RECORDS facts: `replay/cards.py` `:351`–`:357`, `:387`–`:391`; card 92 file | `recorded_reason` at `:357`, `"reason": t.reason` at `:390`; `prompts/2026-10-07/92-radar-arm-disarm-card.md` exists; the only `src` hits for disarm are the four files RECORDS names | OK |
| 24 | dot-tray tests unaffected by `class="tap-strip disarm-chips"`: `grep -rn "tap-strip" tests` | `test_radar_panel_cards.py:371`, `:377` match `class="tap-strip" data-card-id=` exactly, `test_radar_panel.py:1113` is a guard string | OK |

## ISSUES
- NOTE 1: BASE `6f55636b` is one docs commit behind main HEAD `1458693d`; no `src`, `tests` or `configs` difference. The launcher needs only a real commit, and cards 118, 137 and 126 are in it. The desk may refill to `1458693d` if it wants the exact HEAD.
- NOTE 2: tick guards moved: `radar_panel.py:1609` → `:1614`, `:1620` → `:1626` (card 118). `PANEL_JS` is otherwise as cited.
- NOTE 3: `test_radar_panel_cards.py` moved (118, 137): pins `:392`–`:399` → `:475`–`:482` (comment block `:476`–`:479`, so the new comment goes under `:479`, not `:396`); `_page :442` → `:525`; pin test `:495`–`:510` → `:579`–`:593` (assert `:592`, not `:509`).
- NOTE 4: R627 block moved: `ARM_KEY_CSS :947`, `ARM_TAP :948`–`:951`, `DISARM_TAP :952`–`:956`, `BASE_*_SHA256 :959`–`:961`, `_tap_blocks :964`, arm/disarm render test `:971`–`:993`, unchanged test `:1000`–`:1014`, sheet test `:1022`–`:1035`. The card's `:860`–`:952`, `:865`–`:878`, `:888`–`:910`, `:917`–`:931`, `:939`–`:952` are stale.
- NOTE 5: `POST_ALLOWLIST` `:994`–`:999` → `:1064`–`:1078` (`/arm` and `/disarm` at `:1077`). Dot-tray exact-class tests `:288`, `:294` → `:371`, `:377`.
- NOTE 6: `test_radar_panel.py TICK_GUARDS :1112` → `:1113`.
- NOTE 7: `_assert_reason` starts at `:384` (`:383` is the decorator). The 2026-10-08 `grep -n "<input name=\|_price_input(\|_card_form("` line numbers in `## RECORDS` (`:1177`–`:1333`) predate 118; the claim (only DISARM asks for typed text) holds at HEAD. Builder re-reads every cite (D6).
- NOTE 8: row D wants BASE's `/triggered` fragment hash captured first; the existing `BASE_TRIGGERED_ARTICLE_SHA256` (`:959`) is card 92's capture of the whole TRIGGERED article, a different fragment, so the new hash is the builder's to capture and quote.
- NOTE 9: not run, by this seat's rules: the red/green pytest runs and `cobalt jobs restarts`. Reds are proved by reading the BASE code; the builder's gate runs them.

PREFLIGHT DONE · card: disarm-one-tap-1008 · checks: 24 · fails: 0 · ready: YES
