# Ladder refresh card 54, amend 2 — 2026-10-06

## §0 Headline
- Card 54 amended per option (a): `tickLadder` does its own `fetch('/radar')`, re-checks guards and the send counter before the swap, restores open ids by copying `keep`'s logic.
- `refreshLadder` unchanged; `post()` still uses it. No guard names `.ladder-item.open` or `openIds`.
- Every existing text test checked against the new `tickLadder` text: none forbids it.
- 1 decision for the desk.

## CHANGES
All in `prompts/2026-10-06/54-radar-ladder-refresh-card.md`, row A (line 18) unless noted.
- Rule (1): replaced "calls the existing `refreshLadder()`" with `tickLadder`'s own fetch, parse (`:1521`–`:1524`), post-await guard and counter re-check, drop, swap, `keep`-logic restore; `refreshLadder` unchanged, `post()` still calls it, `tickLadder` does not call it.
- Rule (2): guards checked in `tickLadder`'s own body before the fetch and again before the swap. The restore reads the open ids via `items().filter(x=>x.classList.contains('open'))` once, after the second check and before `replaceWith`, to restore, not to pause. The sentence naming `refreshLadder`'s `keep` as the restorer now names `tickLadder`'s copy.
- Rule (4): `tickLadder` reads the counter again after the `await`; a result landing while a `post()` is mid-send is dropped.
- Rule (5) text constraints: appended that `tickLadder` sits after `refreshPool`'s closing `\n }\n`, uses `catch(failure)`, holds no `cursor=`.
- Test (1): `tickLadder` holds `fetch('/radar'` and `replaceWith(`, does not name `refreshLadder`; `post()` still holds `await refreshLadder()`.
- Test (2): guard list before the fetch and again between the `await` and `replaceWith(`, each guard and the counter in both stretches.
- Test (2b): body names neither `.ladder-item.open` nor `openIds`; no guard names `classList.contains('open')`; restore after `replaceWith(` uses `classList.toggle('open',keep.indexOf(`. Mutation unchanged.
- Test (4): `tickLadder` checks both before the fetch and the counter again before the swap.
- `## RECORDS` BEHAVIOUR NOTE: "existing `refreshLadder` rule" now "`refreshLadder`'s rule, copied into `tickLadder`'s restore".
- Not touched: tests (3), (5), route control, controls, row B, CHECK ASKS (X1–X3 hold as written), `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`. No `«FILL`.

## DECISIONS
- ASK DESK: the send counter covers a `post()` mid-send only. A `post()` that starts and finishes while a tick's fetch is in flight leaves the counter at 0 at the swap, so the tick's older response can overwrite the ladder `post()` just refreshed [by the build start]. Default: leave as written; the next tick (one interval) corrects it, and it is named UNPROVEN in the build report. Alternative: `post()` also bumps a monotonic count and the tick drops its result if the count changed since its fetch began.

## RECORDS
Reads at main HEAD `17e6a8bf` (`git -C /Users/cobalt/cobalt rev-parse HEAD`); `src`/`tests` same as BASE `8c554d77` per preflight.
- Card 54, whole; preflight report check 4b and ISSUES 4b; `topics/writing-rules.md`.
- `radar_panel.py:1508`–`:1578`: `refreshLadder` `:1518`–`:1527` (`keep` `:1519`, fetch `:1520`, `!ok` throw `:1521`, `DOMParser` `:1522`, `getElementById` `:1523`, absent throw `:1524`, swap `:1525`, restore `:1526`); `post()` `:1528`–`:1538` (`await refreshLadder()` `:1534`); `refreshPool` `:1560`–`:1574` ending at ` }` `:1574`; `window.COBALT_RADAR` `:1575`; `setInterval(refreshPool,interval)` `:1576`.
- Existing tests against the new `tickLadder` text:
  - X29 `test_x29_ladder_render.py:54` `refresh_pool=_js_function(source,"async function refreshPool(){")`, `:40`–`:41` cuts at `"\n }\n"`, `:56` `"refreshLadder" in refresh_pool or "fetch('/radar'" in refresh_pool`, `:63` asserts it false: reads `refreshPool`'s body only, `tickLadder` sits after it. A `fetch('/radar'` in `tickLadder` is allowed. `:57` `"await refreshLadder()" in post` holds, `post()` unchanged there. A `post()` edit must keep its inner lines indented deeper than one space, so `\n }\n` still ends `post` where it does today (`:55`).
  - `test_radar_panel.py:1047` `"window.setInterval(refreshPool,interval)" in source`: line `:1576` unchanged.
  - `test_radar_panel.py:1098`–`:1103`: `:1099` `"refresh-failed','stale-data"` already in `refreshPool`; `:1101` `classList.toggle('open'` already present; `:1103` `"cursor=" not in source[source.index("catch(error)"):]` covers `tickLadder`, so it holds no `cursor=` and its catch is `catch(failure)` (first `catch(error)` stays `refreshPool`'s, `:1569`).
  - `test_radar_panel_cards.py:648` `js.index("mirrorDegraded(next)") < js.index("mirrorStale(next)") < js.index("catch(error)")`: all inside `refreshPool`, unchanged. `:653`–`:655` forbidden list (`refreshLadder`, `fetch(`, …) reads only `mirrorStale`'s one line (`:649`–`:650`), unchanged. `:656` `setInterval(refreshPool,interval)`, `:657` `MIRROR_DEGRADED_LINE`: unchanged.
  - `test_radar_panel_cards.py:665`–`:672` focus law (`alert(`, `confirm(`, `prompt(`, `.focus(`, `autofocus`, `<form`, `XMLHttpRequest`, `location.reload`, `submit(`) over the whole script: `tickLadder` must hold none; the card says so via the focus-law line.
  - `test_radar_panel_cards.py:495`–`:508` pins hash `render_ladder`, `render_pool`, API json: no change to them.
  - `test_s3_c3_panel_offline.py:546`–`:550` `post(block.dataset.cardId,block.dataset.path,body)`: click handler `:1554` unchanged.
  - `grep PANEL_JS|refreshLadder|tickLadder` in `tests/`: only the files above; no other test reads these names.
- No test forbids `fetch('/radar'` outside `refreshPool`.

LADDER REFRESH CARD AMENDED · decisions: 1
