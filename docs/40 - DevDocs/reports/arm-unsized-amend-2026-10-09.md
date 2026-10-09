# arm-unsized card amend — 2026-10-09

## §0 Headline
- Card `152` amended in place for the preflight's seven FAILs (#1, #6, #12, #8, #10, #11, #13).
- Header `REPORT:` is now the worktree path. Every cite and row C's RUN command now hold at BASE `90342cfc`. Row B is rewritten for the current test.
- The `:disabled` CSS line goes after `DISARM_CHIPS_CSS`, so `:1028` stays true and untouched.
- Row B also covers a second `ARM_TAP` assertion the preflight missed (`:1063`).

## CHANGES
- #1: header `REPORT:` → `/Users/cobalt/cobalt-wt/arm-unsized-1009/docs/40 - DevDocs/reports/arm-unsized-build-2026-10-09.md`.
- #6, #12: `## RECORDS` BASE bullet now says `90342cfc`. Row C's RUN is `git -C <worktree> diff --stat 90342cfc HEAD -- src/cobalt/cards/store.py src/cobalt/aset/web.py`, printing nothing, with the reason (the DISARM merge's `web.py` change is inside BASE). The one remaining `6f55636b` is the history note in `## RECORDS`.
- #8, #10, #11: re-pointed to `90342cfc`.
  - `radar_panel.py`: WATCH branch `:1420`–`:1426` → `:1434`–`:1440`; comment `:1424` → `:1438`; re-render `:1564` → `:1579`; handler `:1569`/`:1583`–`:1584` → `:1573`, `:1598`–`:1599`; `ARM_BUTTON` `:1179` (unchanged); `_card_form` `:1201`–`:1214` → `:1215`–`:1228`; CSS `.arm-key` `:1532` → `:1546`; `.key-disabled` `:1523` → inside `:1537`.
  - `web.py`: `_card_tap` `:1776`–`:1797`; 409 `:1793`–`:1794`; `radar_card_arm` `:2009`–`:2018`; `_grade_options` `:349`–`:358`; label/disabled `:353`, `:358`.
  - tests: `ARM_TAP` `:949`; `_tap_blocks` `:978`; pin `:482` (pool `:481`, API `:483`, comment `:480`); pin test `:580`/`:593`; `BASE_*` `:973`–`:975`; `:1074`; sheet test `:1095`; R627 block `:944`–`:1108`.
  - `store.py` cites were already true. The `test_s3` cites were already true.
- #13, row B rewritten:
  - `:993` and `:1063` move to `ARM_UNSIZED_TAP`.
  - The `:1024` data-key check gains `ARM_UNSIZED_TAP`.
  - The DISARM assertions and the CSS order (`:1025`–`:1029`) stay.
  - The pin comment now says `was 1866a7ad…`, because `9a52577c…` was the pre-R689 hash.
  - RED list: pin test, `:993`, `:1063`.
- Row A: the CSS line moves from "after `ARM_KEY_CSS`" to after the `DISARM_CHIPS_CSS` line (`:1547`). It is asserted as `lines[lines.index(DISARM_CHIPS_CSS) + 1] == ARM_UNSIZED_CSS`, with a new test constant `ARM_UNSIZED_CSS`. The new test goes after `:1029`.
- `## READ` cites refreshed the same way. The `## NOT IN THIS JOB` fence is unchanged except the refreshed `:1095` and a mention of the DISARM chips. `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B` and `RULINGS` are untouched.

## DECISIONS
1. `:disabled` goes after `DISARM_CHIPS_CSS`, not a change to `:1028`. Why: it keeps R689's adjacency pin whole, the two selectors do not interact, and no test line has to be loosened.
2. Added `:1063` and `:1024` to row B. Why: `test_disarm_chips_leave_arm_and_triggered_unchanged` asserts `ARM_TAP` on the unsized WATCH card too, so it would go red after row A. The preflight did not list it, and it is the same fix as `:993`.
3. The pin comment says `was 1866a7ad…`. Why: that is the current value at `:482`.
4. Not acted on (card says change nothing else): the preflight NOTE that row C's real `CardStore()` calls `env.resolve_db_name()` (`store.py:108`–`:109`). The builder should confirm it needs no DB under `world`.
5. Kept `RULINGS: 2026-10-08 R685` (preflight NOTE #4).

## RECORDS
Every read is `git -C /Users/cobalt/cobalt show 90342cfc:<path>`.
- `src/cobalt/aset/radar_panel.py`: `RadarCardRow` `:226`, `:256`–`:259`; `CardView` `:378`, `:393`, `:401`–`:402`; `view` `:905`, `:911`–`:932`; `key-disabled` `:1154`–`:1155`, note `:1160`; `ARM_BUTTON` comment `:1178`, button `:1179`; `DISARM_REASONS` `:1181`; `_disarm_chips` `:1184`–`:1197`; `_card_form` `:1215`–`:1228`; `_card_detail` `:1415`, WATCH branch `:1434`–`:1440`, comment `:1438`; `PANEL_CSS` `:1535`, `.key-disabled{opacity:.45}` inside `:1537`, `.arm-key` `:1546`, DISARM line `:1547`, close `:1548`; `post` `:1573`, `refreshLadder()` `:1579`; `[data-tap]` `:1598`–`:1599`.
- `src/cobalt/aset/web.py`: `_grade_options` `:349`–`:360`, `disabled` `:358`; `_card_tap` `:1776`–`:1797`, 409 `:1793`–`:1794`; `radar_card_arm` `:2009`–`:2018`.
- `src/cobalt/cards/store.py`: `__init__` `:108`–`:109`; `_connect` `:111`; `transition` `:248`; SELECT `:284`–`:289`; guard `:308`–`:318`; key UPDATE `:1379`–`:1386`; `commit`/`rollback`/`close` `:373`/`:377`/`:381`.
- `tests/cobalt/test_radar_panel_cards.py`: `_sized` `:109`; `evaluated` `:121`, `base` `:128`, variants `:137`/`:138`; `_ladder` `:189`; `:388`–`:391`; pins `:480`–`:483`, pin asserts `:592`–`:594`; `ARM_KEY_CSS` `:948`; `ARM_TAP` `:949`; `DISARM_CHIPS_CSS` `:962`–`:966`; `BASE_*` `:973`–`:975`; `_tap_blocks` `:978`; R627 test `:986`–`:1029` (`:993`, `:1021`, `:1024`, `:1025`–`:1029`); `:1055`–`:1066` (`:1063`); `:1074`; `:1095`.
- `tests/cobalt/test_s3_c3_panel_offline.py`: `world` `:133`–`:146`; `UNSIZED` `:215`–`:218`; `:247`–`:253`.
- Preflight `reports/arm-unsized-preflight-2026-10-09.md` `## ISSUES` and `## CHECKS` read. The card was read, then rewritten with the Write tool.
- No command run beyond `git show`, `grep` and reads. No git write, no launch.

ARM UNSIZED CARD AMENDED · decisions: 5
