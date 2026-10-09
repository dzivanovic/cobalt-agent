# https-only card amend — 2026-10-09

## §0 Headline
- Card `156` amended in place for every preflight FAIL and NOTE; cites re-proved against `e4586978`.
- Only `aset/web.py` (`widget_html` calls `:468`→`:469`, `:911`→`:912`) and `test_radar_panel_cards.py` (`:701`–`:703`→`:703`–`:705`) shifted.
- `HOST:` holds the one `«FILL`; the desk fills it and `BASE` after this report.
- Decisions: 3.

## CHANGES
- MACHINE STEPS intro: every `tailscale`, `launchctl kickstart`, `curl`, `uv run python -c` command is a HIS step, none on a desk line, no allow-list change (FAIL 11). M0–M3 are DONE.
- M0–M3 written as done: `HOST` is `cobalt.taild24291.ts.net`; `tailscale serve` is up; `https://<HOST>/api/health` returns 200 on the Mac Studio; the MSI opens it. M1 recorded as not needed (M2 succeeded).
- M3: the `uv run python -c` leg and the MSI mic/log checks are dropped from the done proof, since only the curl 200 and the MSI open are proven.
- M4: exact launch command added; proof cell reworded, so `«FILL` stands only on the `HOST:` line (NOTE 1, NOTE 2).
- M6: `DEPLOY-HUB.md:146` named as a RECORD for the deploy hub's STEP (new value `http://127.0.0.1:5010`); marker extended to `0.0.0.0:5010` (FAIL 7).
- Row B: the `isSecureContext` ordering asserts run first, before any `cfg.https_url` access (NOTE 3); the full `tests/cobalt` suite runs for the other renders at `aset/web.py:469`, `:912`, and a voice-config error now also breaks the sheet and `/radar` (NOTE 4); `test_radar_panel_cards.py` cite re-pointed to `:703`–`:705`.

## DECISIONS
1. FAIL 0c needs no card change. `ops/desk/desk-launch.sh:266` tests `*"HIS RULING"*APPROVED*`; the R718 row `| HIS RULING · APPROVED · APPLIED |` matches it. Default: the card stays.
2. M6 marker conflict: `:146`'s new value `http://127.0.0.1:5010` makes the first `grep -c` read `1` once the hub's STEP lands, and `0.0.0.0:5010` reads `1` until then. Default: the proof states `0`/`1` after M6, and `1`/`0` after the STEP.
3. M3 keeps only what the desk proved; the heartbeat TLS leg (`uv run python -c`) and the MSI mic/log-peer proof are not claimed. The M5 curls still prove `https://<HOST>/api/health` → `200`.

## RECORDS
- BASE read: `git -C /Users/cobalt/cobalt rev-parse --short=8 e4586978` → `e4586978`.
- `git -C /Users/cobalt/cobalt diff --stat 6f55636b e4586978 -- src tests configs ops` → 9 files: `ops/desk/bare-guard.py`, `ops/desk/stop-guard.py`, `aset/radar_panel.py`, `aset/web.py`, `tests/cobalt/test_radar_panel.py`, `test_radar_panel_cards.py`, `test_s3_c3_panel_offline.py`, `tests/ops/test_bare_guard.py`, `test_stop_guard.py`. `voice/web.py`, `aset/config.py` and the other cited files did not change.
- `git -C /Users/cobalt/cobalt diff --stat e4586978 -- src tests configs ops` → `configs/cobalt/rules.yaml` only (uncommitted); every cited file reads the same as `e4586978`.
- `git -C /Users/cobalt/cobalt show e4586978:src/cobalt/voice/web.py`: `peer_gate` `:70`; `_WIDGET` `:198`; `start()` `:268`; `pickType()` `:270`; `navigator.mediaDevices` `:271`, `:273`; `no microphone` `:271`, `:274`, `:300`; `widget_html` `:306`–`:308`. All as the card says; no `isSecureContext` anywhere.
- Grep of the same tree: `aset/config.py:77`–`:86` (`bind` `:81`, `host` `:86`); `aset/web.py:469`, `:912` call `widget_html()`; `heartbeat/probes.py:128`, `:154`; `s2.yaml:135`, `:142`, `:149`, `:157`; `deploy-smoke.sh:12`, `:135`, `:136`; `test_deploy_smoke.py:43`, `:134`; `test_smoke.py:1488`, `:1499` (`:544`, `:548`, `:1512` unchanged by the card); `DEPLOY-HUB.md:11`, `:123`, `:146`, `:147`; `test_voice_web.py:34` (`cfg` fixture) and `:232`–`:308` widget tests.
- `test_radar_panel_cards.py:703` (`from cobalt.voice.web import widget_html`), `:705` (`widget_html()` call).
- `desk-launch.sh:266` quoted: `*"HIS RULING"*APPROVED*` (the desk's FACTS line cite, taken from the prompt; the file was not opened).
- Card `grep «FILL` → `15:HOST:` only.

HTTPS CARD AMENDED · decisions: 3
