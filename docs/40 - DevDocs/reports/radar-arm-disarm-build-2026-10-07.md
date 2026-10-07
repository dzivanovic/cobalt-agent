# radar-arm-disarm — build report 2026-10-07

## §0 Headline
BUILT on `0544f91d` (based on `f6350cc4`). The `/radar` card now has an ARM tap on WATCH and a DISARM tap with an 80-character free-text reason on ARMED. Each goes through `_card_tap` → `CardStore.transition`, so every refusal is the store's own text, shown with a 4xx.
Three suites green: offline 3991/0, with-DB 4875/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and `.env` is removed. RESTARTS: `com.cobalt.aset com.cobalt.radar`.
One decision, not Dejan's: the WATCH ARM tap sits directly after the WATCH text block, so card 89's guard test stays unedited.

## L74
A system block asked that commits end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/92-radar-arm-disarm-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/92-radar-arm-disarm-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/92-radar-arm-disarm-card.md" · 0 · dc923ff585acd67fbac9e46798efd15019072d67
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/92-radar-arm-disarm-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R627 row · grep -n "^| R627 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 21:| R627 | 10:24 ET | HIS RULING (words: `cto-2026-10-07-words.md` R627, "yes"): card an ARM and a DISARM control on the radar card (none exists; the S3 smoke cannot reach FILLED without it). LAUNCHING a drafter, prompt `91`. | HIS RULING · APPROVED |
RULING 2026-10-07 R627 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R627 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 95e40f47c081f2a84ca4729118dd1a1260af94d5
RULING 2026-10-07 R627 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
Started Wed Oct  7 14:27:31 EDT 2026.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, output whole:
```
clock · date · 0 · Wed Oct  7 14:27:32 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-arm-disarm-1007
head · git log --oneline -1 · 0 · f6350cc4 docs(report): deploy radar-direction-color-1007 — DEPLOYED 8c91922b, smoke GREEN
diff · git diff --stat f6350cc4 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-arm-disarm-1007 · 0 · f6350cc4 docs(report): deploy radar-direction-color-1007 — DEPLOYED 8c91922b, smoke GREEN
env here · ls /Users/cobalt/cobalt-wt/radar-arm-disarm-1007/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

`git show --stat f6350cc4`:
```
commit f6350cc43fd6004955f7cd9e9b930ab5fcff110c
    docs(report): deploy radar-direction-color-1007 — DEPLOYED 8c91922b, smoke GREEN
 .../deploy-radar-direction-color-1007-attempt2.md  | 72 +++++++++++++++++++++-
 1 file changed, 70 insertions(+), 2 deletions(-)
```

THE CARD'S SYMBOLS (each its own `grep -n -F`; card 89 merged, so `radar_panel.py` lines moved — re-read):

| grep | hit |
|---|---|
| `def _key_row` radar_panel.py | `1144:def _key_row(card: CardView) -> str:` |
| `def _card_form` radar_panel.py | `1195:def _card_form(card_id: int, path: str, inner: str, *, source: str, cls: str = "s3-form") -> str:` |
| `def _card_detail` radar_panel.py | `1395:def _card_detail(card: CardView, *, stale: str \| None = None) -> str:` (card said `:1381`; WATCH block now `:1414`–`:1418`, ARMED `:1419`–`:1426`, `card-status` `:1445`) |
| `PANEL_CSS` radar_panel.py | `1511:PANEL_CSS = r"""` (the `.s3-form` line is `:1521`; `.key{min-height:44px…}` on `:1513`) |
| `PANEL_JS` radar_panel.py | `1525:PANEL_JS = r"""` (`post` `:1547`–`:1557`; `[data-key]` `:1568`–`:1569` before `[data-tap]` `:1572`–`:1573`) |
| `def _card_controls` web.py | `655:def _card_controls(card: dict) -> str:` |
| `def card_move` web.py | `1380:async def card_move(card_id: int, request: Request) -> str:` |
| `def _card_tap` web.py | `1775:async def _card_tap(card_id: int, request: Request, gate: str, work):` |
| `/radar/card/{card_id}/` web.py | `1554 /key`, `1606 /dot/{factor}`, `1645 /promote`, `1650 /release`, `1799 /triggered`, `1818 /fill`, `1849 /pass`, `1860 /exit`, `1914 /held`, `1938 /correct`, `1975 /stop`, `1988 /stop/reset` |
| `def transition` store.py | `248:    def transition(` |
| `def _assert_reason` store.py | `384:    def _assert_reason(` |
| `ALLOWED` models.py | `92:ALLOWED: dict[CardState, frozenset[CardState]] = {` |
| `def assert_edge` models.py | `199:def assert_edge(` |
| `class IllegalTransition` models.py | `139:class IllegalTransition(RuntimeError):` |
| `PIN_HEALTHY` test_radar_panel_cards.py | `396` POOL, `397` LADDER `b3174d30…`, `398` API; asserted `507`–`509` |
| `POST_ALLOWLIST` test_radar_panel_cards.py | `885:POST_ALLOWLIST = {`, `910:    assert posts == POST_ALLOWLIST` |
| `NEW_ROUTES` test_s3_c3_panel_offline.py | `42:NEW_ROUTES = [`, `382`, `385`, `388` |

Callers, `grep -rn -F "_card_tap(" src`: `web.py:1775` (def), `:1815` triggered, `:1846` fill, `:1857` pass, `:1911` exit, `:1935` held, `:1972` correct, `:1985` stop, `:2004` stop_reset.
Callers, `grep -rn -F "_card_detail(" src`: `radar_panel.py:1395` (def), `:1487` (`render_ladder`).

`wc -l`: `web.py` 2231, `radar_panel.py` 1680, `test_s3_c3_panel_offline.py` 661, `test_radar_panel_cards.py` 958.

`## READ` names no report.

CARD `## RECORDS`, copied: (1) THE MOVE EDGE NEEDS NO CHANGE — re-read: `store.py:276` session gate, `:285`–`:287` `FOR UPDATE`, `:301` `assert_edge`, `:308`–`:318` unsized ARM, `:321` / `:400`–`:410` disarm reason. Holds. (2) THE SHEET'S ARM AND DISARM ALREADY REACH RADAR CARDS — `_card_controls` `web.py:709`–`:722` draws a button per `ALLOWED[state]`; one-click fill manual-only `:696`–`:699`. Holds. (3) REASON FORM — `askReason` `web.py:174`–`:179`, `window.prompt`, free text. Holds; the panel forbids `prompt(` (`test_radar_panel_cards.py:869`, `:876`). (4) RESTARTS expected `com.cobalt.aset com.cobalt.radar` — run at row E. (5) DB: key left out; every new test offline. (6) BASE at drafting `95e40f47`; BASE refilled `f6350cc4` with card 89 merged; lines re-read above.

`uv run cobalt jobs restarts f6350cc4..HEAD` → exit 0:
```
path	change	rule	restart
RESTARTS: none
```

PROVEN BY FIRST REAL USE: per BUILD-HUB's table (`sh …/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT, exit 0).

## E0 BASELINE
On `f6350cc4`. `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0:
`3975 passed, 787 skipped, 1 xfailed, 36 warnings in 603.81s (0:10:03)` — 0 failed, 0 errors.

`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.28s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only; no `src/` edit. No with-DB red (every new test offline), so no lock take. Red commit `5bc72f94`.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_s3_c3_panel_offline.py tests/cobalt/test_radar_panel_cards.py` on BASE → `15 failed, 79 passed, 10 skipped in 2.39s` (the 10 skips: `reaches cobalt_dev (lock-relief G1)`, pre-existing). Each red, its first line:

| row | test | red |
|---|---|---|
| A | `test_arm_moves_a_watch_card_to_armed_by_you` | `test_s3_c3_panel_offline.py:233: AssertionError: {"detail":"Not Found"}` `assert 404 == 200` |
| A | `test_a_second_arm_tap_is_refused_by_the_edge` | `:240: assert 404 == 200` (`post('/radar/card/1/arm')`) |
| A | `test_arm_on_an_unsized_card_shows_the_store_refusal` | `:251: {"detail":"Not Found"}` `assert 404 == 409` |
| B | `test_disarm_without_a_reason_is_refused_by_the_store[data0]`, `[data1]` | `:260: {"detail":"Not Found"}` `assert 404 == 409` (×2) |
| B | `test_disarm_with_a_reason_moves_the_card_to_watch` | `:268: {"detail":"Not Found"}` `assert 404 == 200` |
| B | `test_a_disarm_reason_over_80_characters_is_refused` | `:277: {"detail":"Not Found"}` `assert 404 == 422` |
| A/B (X2) | `test_a_disarm_on_watch_and_an_arm_on_triggered_are_refused_by_the_edge` ×2 | `:292: {"detail":"Not Found"}` `assert 404 == 409` (×2) |
| D(1) | `test_market_reset_refuses_every_post_and_writes_nothing[/radar/card/1/arm-…]`, `[…/disarm-…]` | `:477: {"detail":"Not Found"}` `assert 404 == 409` (×2) |
| D(1) | `test_the_new_routes_sit_in_one_block_directly_after_release` | `:497: At index 8 diff: '/drc' != '/radar/card/{card_id}/arm'` |
| C | `test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only[False]`, `[True]` | `test_radar_panel_cards.py:895: assert [] == [('1', '<inpu...RM</button>')]` (×2) |
| D(1) | `test_post_routes_are_exactly_the_explicit_allowlist` | `:1006: Extra items in the right set: '/radar/card/{card_id}/disarm' '/radar/card/{card_id}/arm'` |

GREEN on BASE, as the card says: `test_radar_arm_disarm_leaves_keys_sheet_and_other_states_unchanged[False|True]` and `test_the_sheet_keeps_its_arm_and_disarm_buttons`. The hash parts of D(2) were captured on BASE first, each read from the failing assertion against a `"CAPTURE"` placeholder (`--tb=line`):
- TRIGGERED article: `194886823f9810a554de693cc3e8a8ab128aa503ceee773028cc35cbf79a6e7f` (`:926`)
- FILLED article: `5a522d9c06df4f3fbac199e82b6a111e6a9c38d882bcea786b784b326fc42a87` (`:927`)
- terminal section: `c1021a1b3e63e2fd680fb9723d4879f3d579e9bc977ef4cf2552fa3385ed1906` (`:930`)
Both frames printed the same values (the ladder fragment does not depend on the frame).

The pin test `test_bars_stale_badge_absent_and_output_unchanged_when_healthy` is GREEN on BASE (it goes red at row C, then is re-pinned).

No RUN row's test (row E is a tool run at RESTARTS).

## E3 THE ROWS
Fix commit `0544f91d` `feat(radar-arm-disarm): ARM and DISARM taps on the radar card through CardStore.transition (rows A-D, L1 L3 L72)` — `src/cobalt/aset/web.py`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py` (the re-pin), the two DevDocs pages.

- A — `POST /radar/card/{card_id}/arm` appended after `/stop/reset` (`web.py:2007`), `_card_tap(…, "aset.radar.arm", work)`, `work` = `CardStore().transition(card_id, CardState.ARMED, actor=Actor.YOU, evidence={"via": f"{source}.arm"})`; no pre-check.
- B — `POST /radar/card/{card_id}/disarm` directly after (`web.py:2020`), gate `aset.radar.disarm`; `reason = form.get("reason", "").strip()`; `> 80` → `_TapInputRefused` (422); `transition(card_id, CardState.WATCH, actor=Actor.YOU, evidence={"via": f"{source}.disarm"}, reason=reason or None)`; no empty-reason check in the route.
- After A + B: `uv run pytest … test_s3_c3_panel_offline.py test_radar_panel_cards.py` → `2 failed, 92 passed, 10 skipped in 2.43s`; the two reds are row C's (`test_radar_panel_cards.py:895: assert [] == [('1', '<inpu...RM</button>')]`).
- C — `ARM_BUTTON` and `DISARM_TAP` constants beside `TRIGGERED_BUTTON` (`radar_panel.py:1178`–`:1183`); WATCH: `_card_form(card.id, '/arm', ARM_BUTTON, source='panel')` directly after the WATCH text block's `</div>` (see DECISIONS 1); ARMED: `_card_form(card.id, '/disarm', DISARM_TAP, source='panel')` after the TRIGGERED tap, inside the ARMED block; `PANEL_CSS` gets the line `.s3-form button.arm-key{min-height:44px;padding:0 14px}` directly after the `.s3-form` line. After C, the only red was the ladder pin: `test_radar_panel_cards.py:508: AssertionError: 9a52577cbe07733c1f933857e2ed14d531a12a911c64bd899be3b48a0e16ff15` (`- b3174d30…`) ×2 frames; POOL (`:507`) and API (`:509`) held.
- D(5) — `PIN_HEALTHY_LADDER_SHA256` re-captured: old `b3174d308594f6325c225260d988fa563093a70db4387057fd63101a1b53c92e` → new `9a52577cbe07733c1f933857e2ed14d531a12a911c64bd899be3b48a0e16ff15`, with the comment line `# LADDER pin re-captured 2026-10-07 on ops/radar-arm-disarm-1007 (was b3174d30…): R627 adds the ARM tap (WATCH) and the DISARM tap with its reason (ARMED); healthy bars still add nothing.` POOL and API pins unchanged.
- D(1)–(4) — landed at E2 (test data); green after A + B.

GREEN after all rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_s3_c3_panel_offline.py tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_radar_panel.py tests/cobalt/test_aset_web.py` → `217 passed, 40 skipped in 2.76s` (every skip `reaches cobalt_dev (lock-relief G1)` or `requires_db: radar read-layer integration needs cobalt_dev`).

THE MUTATIONS (Edit tool; each undone; `git diff --stat` after the last undo → `radar_panel.py | 13 ++++++++++++-`, `web.py | 29 +++…`, `test_radar_panel_cards.py | 3 ++-`, the fix only):

| row | mutation | run | result, first failing line |
|---|---|---|---|
| A | `@app.post("/radar/card/{card_id}/arm")` → `…/arm-mutated` | offline file `-k "arm and not disarm"` | `4 failed, 1 passed` — `:233: {"detail":"Not Found"} assert 404 == 200` (arm, second-arm `:240`, unsized `:251`, market reset `/arm` `:477`) |
| B | `len(reason) > 80` → `> 8000` | offline file `-k disarm` | `1 failed, 6 passed` — `:277: {"status":"ok","card_id":1,"state":"WATCH","transition_id":77} assert 200 == 422` |
| B | `reason=reason or None` → `reason=reason or "auto"` | offline file `-k disarm` | `2 failed, 5 passed` — `:260: … assert 200 == 409` (`[data0]`, `[data1]`) |
| C | WATCH `_card_form(…'/arm'…)` → `""` | cards file `-k "taps_render_on_watch_and_armed_only or output_unchanged_when_healthy"` | `4 failed` — `:509: AssertionError: f5193ed0… == 9a52577c…` (pin ×2) and `:896: assert [] == [('1', '<inpu...RM</button>')]` (×2) |
| C | `DISARM` button gets `data-key="pass"` | cards file `-k taps_render_on_watch_and_armed_only` | `2 failed` — `:897: At index 0 diff: … class="arm-key danger" data-key="pass">DISARM…` |
| D(2) control | `_key_row`'s `pass` button loses `data-key="pass"` | cards file `-k "leaves_keys… or sheet_keeps…"` | `:926: assert (4 == 4 and 4 == 5)` ×2 frames |
| D(3) control | `_card_controls` label `CardState.ARMED: "ARM"` → `"ARM!"` | same run | `:941: assert '<form method="post" action="/card/9/move" … <button type="submit">ARM</button></form>' in '<div class="crow">…'` (3 failed in all) |
| C / D(2) | TRIGGERED body also gets the ARM tap | cards file `-k "leaves_keys… or taps_render… or sheet_keeps…"` | `4 failed, 1 passed` — `:901: '"/arm"' not in …` (×2) and `:927: d89d79ce… == 194886823f98…` (TRIGGERED hash ×2) |
| D(1) | `/radar/card/{card_id}/disarm` → `/radar/disarm/{card_id}` | `-k "explicit_allowlist or directly_after_release"` | `2 failed` — `:1007: Extra items in the left set: '/radar/disarm/{card_id}'` and offline `:495: a pre-existing route moved, or a route was added outside the block` |

No named test stayed green under its mutation; none was rewritten.

## RESTARTS
Row E (RUN, asserts nothing). `uv run cobalt jobs restarts f6350cc4..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-arm-disarm-build-2026-10-07.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. Matches the card's expected `com.cobalt.aset com.cobalt.radar`.

## W THE THREE SUITES
`<tip>` = `0544f91d`. The card carries no `DB` key, so the full gate: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-arm-disarm-1007 all --deploy` (no `--deselect`: no with-DB test of this build; no `--tickers`: no new test writes `cobalt_dev`; no `--migration`). Exit 0. Verdict lines, whole:
```
offline 3991/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4875/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-arm-disarm-1007-all-20261007-144343.log
```
`grep -n -F "OUTSIDE" <log>` → nothing: no skip outside the allowed set.

- (a) offline: log `:863` `3991 passed, 787 skipped, 1 xfailed, 36 warnings in 589.54s (0:09:49)` → `<p>` = 3991 (E0 3975 + the 16 tests this build adds: in `test_s3_c3_panel_offline.py` `test_arm_moves_a_watch_card_to_armed_by_you`, `test_a_second_arm_tap_is_refused_by_the_edge`, `test_arm_on_an_unsized_card_shows_the_store_refusal`, `test_disarm_without_a_reason_is_refused_by_the_store[data0|data1]`, `test_disarm_with_a_reason_moves_the_card_to_watch`, `test_a_disarm_reason_over_80_characters_is_refused`, `test_a_disarm_on_watch_and_an_arm_on_triggered_are_refused_by_the_edge[×2]`, `test_market_reset_refuses_every_post_and_writes_nothing[/arm|/disarm]`; in `test_radar_panel_cards.py` `test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only[False|True]`, `test_radar_arm_disarm_leaves_keys_sheet_and_other_states_unchanged[False|True]`, `test_the_sheet_keeps_its_arm_and_disarm_buttons`).
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:880`); proof-only → `LEVEL 0013` (`:932`).
- (c) pass 1, executed command (log `:935`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py` → `:1088` `4686 passed, 7 skipped, 83 deselected, 3 xfailed, 43 warnings in 743.48s (0:12:23)` → `<d1>` = 4686; the 7 skips are the seven quoted above.
- (c2) `dev forward: APPLIED 15:06:21` (`:1090`), 0014 … 0022 applied after the baseline; `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1165`).
- (c3) pass 2 → `:1800` `189 passed, 1 deselected, 5 warnings in 227.03s (0:03:47)` → `<d2>` = 189; `<d>` = 4686 + 189 = 4875 = `with-DB 4875/0`. This build adds no with-DB test. The store's unsized-ARM gate the routes rely on: `:1736` `PASSED tests/cobalt/test_radar_cards_db.py::test_unsized_arm_is_refused_inside_the_locked_transition_and_sized_arm_passes`.
- (c3r) `stray rows: not read (no --tickers given)` — no test of this build writes `cobalt_dev`.
- (f) ROLLBACK `--down-to 0013` (`:1804`), 0022 → 0014 reversed newest first; `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1865`) = F0 field for field → `cobalt_dev: 0013 — F2 = F0` (`:1916`); `lock released` (`:1918`); `.env: removed` (`:1922`). Mine: `ls /Users/cobalt/cobalt-wt/radar-arm-disarm-1007/.env` → `No such file or directory`.
- (e) live-note → `:1987` `146 passed, 1 skipped, 15 warnings in 24.95s` → `<l>` = 146; the skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.

The log's `code: 0544f91d (DIRTY: 1 path(s))` is this report, uncommitted while the gate ran; no code path was dirty.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED: rows A, B, C, D(1) red at E2 (table there: 404 / no `/arm` block / route order / allowlist); D(2) and D(3) green on BASE by design and red under their controls at E3 (`:926` key row, `:941` sheet ARM, `:927` TRIGGERED hash); the pin red at row C (`:508`) and under the C mutation (`:509`); every A / B test red under its mutation (E3 table). None stayed green; none rewritten. ✔
(2) Every entry path pinned: `_card_tap` callers (`web.py:1815` … `:2004`, plus the two new) — the new two pinned by the offline tests through `TestClient`, their gates by `GatedCards` (the real `assert_edge` and `_assert_reason`) and market reset (`assert_writable` before `work`); a second ARM, DISARM on WATCH, ARM on TRIGGERED pinned (X2 test); the unsized refusal pinned verbatim offline and, in the real store under the row lock, by `test_radar_cards_db.py` (PASSED at pass 2). `_card_detail`'s one caller `render_ladder` (`radar_panel.py:1487`) pinned in both frames. The sheet's path (`/card/{id}/move`, `_card_controls`) pinned unchanged by `test_the_sheet_keeps_its_arm_and_disarm_buttons`. ✔
(3) Re-read at the tip: `grep -n -F "/radar/card/{card_id}/" src/cobalt/aset/web.py` → `2007` arm, `2020` disarm; `grep -n -F "R627" src/cobalt/aset/radar_panel.py` → `1178`, `1424`, `1434`; the gate's counts and fingerprints from `grep -n -F` / Read of the log, cited by line. ✔

## FOR THE CHECK
- Range `f6350cc4..0544f91d`: `5bc72f94 wip(radar-arm-disarm): red — ARM / DISARM route, tap, allowlist and unchanged-render tests (rows A-D)`; `0544f91d feat(radar-arm-disarm): ARM and DISARM taps on the radar card through CardStore.transition (rows A-D, L1 L3 L72)`. The report commit follows.
- Per row: reds at `## E2 RED`, greens and mutations at `## E3 THE ROWS`.
- Callers: `## PREFLIGHT` (`_card_tap(` 9 hits, `_card_detail(` 2 hits).
- Row E (RUN) output whole: `## RESTARTS`.
- Suites and the executed pass-1 command: `## W`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. One lock take, inside `gate.sh` (gate started 14:43:43 per the log name; `lock: waited 0 min`; forward 15:06:21; released before 15:11:28 `date`); the log prints no clock at take or release.
- BASE hashes (D(2)): TRIGGERED `194886823f98…`, FILLED `5a522d9c06df…`, terminal `c1021a1b3e63…` (whole at E2). Pin old `b3174d30…` → new `9a52577c…` (whole at E3).
- X3: `PANEL_JS`, `_key_row`, `_card_controls`, `card_move` have no hunk in `git diff f6350cc4 0544f91d -- src` (the diff holds only the constants, the two `_card_detail` blocks, the CSS line and the two routes).
- X4: a refused ARM / DISARM answers 409 / 422 JSON with `reason` through `_card_tap`; `PANEL_JS` `post` shows `REFUSED <status> · <reason>` on `!response.ok` and `saved` only on 2xx (`radar_panel.py:1552`–`:1555`).
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: CLOSE (done)

## DECISIONS
1. ASK DESK: where the WATCH card's ARM tap sits [15:11 EDT]. Row C (1) says the WATCH block "gets, after its text," the ARM `_card_form`. If the tap goes INSIDE `<div class="state-block watch-state">`, card 89's guard `test_radar_direction_touches_only_strip_and_title` turns red. That test is at `test_radar_panel_cards.py:831`–`:835`: it `re.fullmatch`es the block as `<b>WATCH</b> · proposed key … · trigger … · stop …</div>` with nothing after the text. Editing it lies outside the rows. Safe default taken: the tap is rendered directly after the WATCH text block's `</div>`, as part of the same WATCH `state_body` (`radar_panel.py:1421`–`:1426`). Card 89's guard stays green unedited, and row C's test holds: the WATCH article carries exactly one `/arm` block, with a `card-status` sink. The ARMED DISARM tap is inside the ARMED block, as the card says. If the desk wants the tap inside the WATCH div, the fix is one line plus card 89's regex.

## RECORDS
- `.env: removed, proven gone (W)`: gate `.env: removed`, and `ls …/radar-arm-disarm-1007/.env` → `No such file or directory`.
- Card records re-read at PREFLIGHT: all hold (see `## PREFLIGHT`). BASE was refilled to `f6350cc4` (card 89 merged), so `radar_panel.py` lines moved: `_card_detail` `:1395`, the `.s3-form` CSS line `:1521`, `PANEL_JS` `post` `:1547`–`:1557`.
- The L74 line: see `## L74`.
- Extra calls on listed prefixes: `uv run cobalt jobs restarts --help` (usage read at PREFLIGHT). No refusal, no extra lock take, no CONTINUE.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-arm-disarm · tip: 0544f91d | on f6350cc4 | migration: none | offline 3991/0 | with-DB 4875/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 232402
