JOB: voice-peers
LADDER: OFF-LADDER — cto-2026-09-28.md 2026-09-28 R95
BRANCH: ops/voice-peers-1001
WORKTREE: voice-peers-1001
BASE: 446ff64d
TIP:
REPORT: /Users/cobalt/cobalt-wt/voice-peers-1001/docs/40 - DevDocs/reports/voice-peers-build-2026-10-01.md
CHECK REPORT:
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-01 R14

## ROWS

| row | what | red first | files |
|---|---|---|---|
| V1 | `configs/cobalt/voice.yaml:44` `allowed_peers` becomes localhost plus all five tailnet devices, exactly as ruled (2026-09-28 R95, his words "yes change it as well as fedor. all tailscale machines included"): `["127.0.0.1", "::1", "100.70.206.126", "100.73.178.42", "100.66.219.53", "100.104.48.21", "100.82.85.27"]` (cobalt, badass, dejans-s25, fedora, msi; the desk's `tailscale status`, 2026-10-01 08:2x ET). The source comment on the line says so, with the R95 row. Today a request from any of them gets a named 403 (`src/cobalt/voice/web.py:72-75`), seen live on the sheet as "voice status refused (HTTP 403)" | test in `tests/cobalt/test_voice_config.py`: the loaded config's `allowed_peers` holds each of the seven literals, every entry parses as an IP literal (the validator at `src/cobalt/voice/config.py:65`), and `voice.web`'s peer check admits a socket peer `100.104.48.21` and still refuses `192.168.1.5` and `100.70.206.127`. RED on `BASE`: `100.104.48.21` is refused | `configs/cobalt/voice.yaml`, `tests/cobalt/test_voice_config.py`, `tests/cobalt/test_voice_web.py` |
| V2 | RUN — asserts nothing. The headers (`X-Forwarded-For` and the like) are still never read (`voice/web.py:14-15`); quote the grep that proves it, and quote what the voice resident reads at start (`grep -n voice.yaml` over `src/` and `configs/`) so the deploy's restart class is derived, not assumed (L42) | — (tool output quoted in the report) | none (read only) |

## NOT IN THIS JOB
- Any `src/` change: the peer check is correct; only the config line was never shipped.
- Tailnet IPv6 addresses, a `tailscale serve` peer (E8), any subnet or wildcard: a literal per device only.
- Voice behaviour, the widget, `/voice/status`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-28.md` rows R94 and R95; `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-28-words.md` `## R95`.
- `src/cobalt/voice/web.py` lines 1-20 and 60-80; `src/cobalt/voice/config.py` lines 55-75; `configs/cobalt/voice.yaml` lines 40-45.

## RECORDS
- `tailscale status`, 2026-10-01 08:2x ET: cobalt 100.70.206.126 (macOS), badass 100.73.178.42 (windows, offline 18 h), dejans-s25 100.66.219.53 (android), fedora 100.104.48.21 (linux), msi 100.82.85.27 (windows).
