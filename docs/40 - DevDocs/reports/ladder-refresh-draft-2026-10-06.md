## §0 Headline
- Card `prompts/2026-10-06/54-radar-ladder-refresh-card.md` drafted: BUILD lane, rows A (`PANEL_JS` gets `tickLadder` + `window.setInterval(tickLadder,interval)`) and B (DOC).
- Lane: build. `DEVFIX-HUB.md` only rebuilds a table and cannot edit `src/` or `tests/`.
- RESTARTS is `com.cobalt.aset com.cobalt.radar`, not aset alone. `com.cobalt.radar` reaches `radar_panel` through a function-local import (proof in `## DECISIONS` 1).
- The tests are static assertions on the script text, since no JS runner exists in `tests/`. Browser timing is UNPROVEN until a post-deploy `aset.log` read.

## CARD
- Path: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md` (uncommitted; the desk commits it).
- Left for the desk: `BASE: «FILL: main HEAD at launch, 8 hex»` (it read `542a8348` at drafting). `TIP`, `CHECK REPORT` and `HOUSE B` are empty, the build-launch shape (`CARD.md:18`, `:20`, `:21`). `RULINGS: 2026-10-06 R556` is filled. No `DB` key: the rows touch `src/` and `tests/` (`CARD.md:22`).

## DECISIONS
1. ASK DESK: the prompt expects RESTARTS `com.cobalt.aset` only. The code gives `com.cobalt.aset com.cobalt.radar`, because `restarts.py:133` walks every import node: `cli.py:82` → `voice/cli.py:29` → `voice/turn.py:43` → `voice/confirm.py:77` (`from cobalt.aset.web import …`, function-local) → `aset/web.py:75` → `radar_panel`. Default: the card expects both, and the build quotes `uv run cobalt jobs restarts <BASE>..HEAD`. [16:48 EDT]
2. ASK DESK: rule (2) skips the tick while any `.ladder-item.open`. `render_ladder` opens the top 2 at load (`radar_panel.py:1451`), so a page loaded with cards does not refresh until he closes them. A refresh while a card is only expanded destroys nothing, because `keep` restores the open set (`:1519`, `:1526`). The alternative: count only open tap strips, focused or typed inputs, open TERMINAL and a `post()` in flight as work in progress. Default: as the prompt says (skip while open). The card's `## RECORDS` BEHAVIOUR NOTE names the effect. [16:48 EDT]
3. ASK DESK: the card adds `details.terminal[open]` as work in progress. The ✓ correct leg inputs and their `card-status` sit inside TERMINAL (`:1483`, `_terminal_legs`), and a swap closes the `<details>`. Default: included (the tick pauses while TERMINAL is open). [16:48 EDT]
4. ASK DESK: the tests are static assertions on `PANEL_JS`, each red on BASE and under a named mutation. They prove the text, not the runtime. `playwright` is in `pyproject.toml:30`, but no test under `tests/cobalt` uses it. Default: no browser harness. The live proof is `logs/aset.log` showing `GET /radar` once per interval after the deploy (a smoke-read line for the deploy card). [16:48 EDT]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `542a8348a9766ee6bcfb5c54818108d0aab60806` (BASE at drafting).
- `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests ops/desk` → no output.
- Read whole: `prompts/2026-10-06/39-drc-d5-o1-b2-card.md` (shape), `prompts/CARD.md`, `prompts/DEVFIX-HUB.md:1`–`:15`; `grep -n "^#"` of `prompts/BUILD-HUB.md`.
- `src/cobalt/aset/radar_panel.py` read `:1440`–`:1495` (`render_ladder`), `:1505`–`:1609` (`PANEL_JS`, `render_radar_page`, `render_failed_page`). `grep` anchors: `refreshLadder` `:1518`, `post` `:1528`, `:1534`, `refreshPool` `:1560`, the failure text `:1571`, `setInterval` `:1576`, `data-refresh-seconds` `:1589`, `<input>` `:1185`–`:1326`. `grep -c "<select\|<textarea"` → 0.
- `src/cobalt/aset/web.py:898`–`:929` (`/radar` returns a 200 FAILED page on error; `/api/radar/pool`).
- Tests: `grep` of `tests/` for `PANEL_JS|refreshPool|refreshLadder|setInterval|jsdom|node` → `test_radar_panel.py:563`, `:1038`, `:1047`, `:1097`; `test_radar_panel_cards.py:646`, `:653`, `:656`, `:666`; `test_s3_c3_panel_offline.py:547`; `test_x29_ladder_render.py:54`–`:61`. Read `test_radar_panel.py:560`–`:629` and `:1030`–`:1119`, `test_radar_panel_cards.py:395`–`:434`, `:495`–`:509`, `:636`–`:680`, `test_s3_c3_panel_offline.py:540`–`:564`, and `test_x29_ladder_render.py` whole.
- JS runner: `grep -rln "jsdom\|\"node\"\|…playwright…" tests pyproject.toml` → only `pyproject.toml` (`:30` `playwright>=1.40.0`) and browser-scraper tests outside `tests/cobalt`, plus a non-JS `"node"` key at `test_radar_audit_export.py:114`. `grep -rln playwright tests/cobalt` → no output.
- Restarts: `restarts.py:120`–`:149`; `configs/cobalt/jobs.yaml:39`–`:91`, `:184`–`:195`; `grep` of `radar_panel|aset.web` in `src/cobalt` (only `aset/web.py`, plus `voice/confirm.py:77`); `cli.py:82`; `voice/cli.py:29`; `voice/turn.py:43`; `voice/confirm.py:72`–`:79`; `aset/__init__.py` has no import. `ops/desk/gate-lists.md` has no radar-panel entry (`grep` → no output); the restart classes come from `jobs.yaml` + `restarts.py`.
- Doc: `docs/40 - DevDocs/cobalt/aset/radar_panel.md` read whole (`:55` PANEL_JS paragraph, `:68` terminal today-only).
- Finding: `radar-page-read-2026-10-06.md` read whole (26 = 22 EXPIRED + 4 WATCH). `grep` of `radar-screen-trace-2026-10-06.md` (`:4`, `:8`, `:19`, `:42`) and of `cards-origin-survey-2026-10-06-r2.md` headings. `tail -n 30 logs/aset.log`: only `/api/radar/pool` polls, plus one `GET /radar` at a page load.
- Ruling: `grep -n "^| R556 " reports/cto-2026-10-06.md` → `:100`, `HIS RULING · APPROVED`. `git log -S` → `8bceed0a`.
- Nothing was run but reads. No git write, no launch.

LADDER REFRESH CARD DRAFTED · decisions: 4
