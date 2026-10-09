# https-only draft — 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/156-https-only-card.md` drafted: one card, rows A–E, plus `## MACHINE STEPS` M0–M7.
- Bind source: the gitignored `configs/dev/aset.local.yaml:28` `bind: lan` → `0.0.0.0` (`aset/config.py:86`). Loopback is set by machine step M5; row C refuses `lan`.
- Probes move to `https://<HOST>/` (L80(c)): `probes.py:128`, `:154`; `s2.yaml:135`–`:157`; `deploy-smoke.sh:135`; `DEPLOY-HUB.md:11` (M6).
- `HOST` stays `«FILL»` until M0–M3 prove `tailscale serve`. The card cannot launch before https answers.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md`: JOB `https-only-1009`, BASE `6f55636b`, RULINGS `2026-10-09 R718`, `DB` left out.

| row | builds | red first |
|---|---|---|
| A | `VoiceConfig.https_url`, required, `https://…ts.net/` only | the key is refused as extra on BASE |
| B | voice banner: `isSecureContext` false → "voice needs the https address: <url>"; "no microphone" only on a secure page | `test_an_insecure_page_shows_the_https_line` |
| C | `ServerConfig.bind` loopback only; `__main__` lan branch dropped | `test_lan_bind_is_refused` |
| D | heartbeat, smoke and deploy-smoke read `https://<HOST>/` | `test_every_probe_reads_the_configured_https_url` |
| E | RUN `cobalt jobs restarts` | — |

## DECISIONS
- ASK DESK: one card or two? Default: ONE. Rows A–D share the one https URL (row D's test pins every copy to `voice.yaml`), each change is small, and one deploy ships them. [11:33]
- ASK DESK: where does the https URL live? Default: `configs/cobalt/voice.yaml` `https_url` (committed, required, L1). The hostname is also typed literally in the two probe defaults, `s2.yaml`, `deploy-smoke.sh` and `DEPLOY-HUB.md`, because a shell case pattern and an allow string cannot read YAML. Row D's test pins them to the config value. [11:33]
- ASK DESK: probes on `http://127.0.0.1:5010` or the https URL? Default: the https URL (L80(c)). Dependency: the cert name `<HOST>` and a running `tailscale serve`. When serve is down, `sheet_http` is red even with aset up, which is true for his devices. Python's TLS path is proven at M3. [11:33]
- ASK DESK: does row C drop `lan` from code, or does M5 alone change the bind? Default: drop it, so no config can reopen the bind. Cost: the deploy must follow M5, or aset crash-loops. DEPLOY ORDER and the M5 marker on the deploy card hold that. [11:33]
- ASK DESK: `HOST` is unknown at drafting. Default: `«FILL»` in the card body. The hub's `«FILL»` gate blocks the launch until M0–M3 are done, which enforces serve-first. [11:33]
- ASK DESK: the voice peer gate behind serve. Default: unchanged. uvicorn's proxy-header middleware (trusting 127.0.0.1 only) gives `request.client.host` = the `X-Forwarded-For` tailnet IP. M3 proves it on the log line. If the log shows `127.0.0.1`, the gate admits any tailnet device, and that becomes its own item. [11:33]
- ASK DESK: `REPORT` path. Default: inside the worktree (`/Users/cobalt/cobalt-wt/https-only-1009/…`), per `CARD.md` `REPORT` for a build and the precedent card `118`. The drafter prompt named the main-checkout path. [11:33]
- ASK DESK: the other Mac listeners (Mattermost `*:8065`, `*:18080`, Postgres `*:5432`, LM Studio `127.0.0.1`). Default: out of scope; L80 covers aset's pages only. [11:33]
- ASK DESK: `DEPLOY-HUB.md` edits (allow entry `:11`, reads `:123`, `:147`). Default: desk step M6, because a fixed hub file is the desk's, not a build row. [11:33]
- ASK DESK: the card number `156` is shared with the untracked `prompts/2026-10-09/156-brain-handover.md`. Default: keep `156-https-only-card.md` as ordered; the names differ. [11:33]

## RECORDS
- 11:33 ET `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `6f55636b`; `git diff --stat HEAD -- src tests configs/cobalt/voice.yaml configs/cobalt/smoke configs/dev/aset.yaml ops/desk/deploy-smoke.sh` → empty.
- `ls` of the card, both reports and `/Users/cobalt/cobalt-wt/https-only-1009` → all absent before writing.
- Read: `LAWS.md:391`–`:393` (L80); `prompts/CARD.md`; `prompts/2026-10-08/117-draft-radar-display-fix.md`, `118-radar-display-fix-card.md`; `topics/writing-rules.md`; `areas/cobalt.md` `## What Cobalt is`, `## Build rules` on.
- Read: `src/cobalt/aset/__main__.py` (all); `src/cobalt/aset/config.py:60`–`:139`; `configs/dev/aset.local.yaml` (all); `configs/dev/aset.yaml:28`–`:42`; `git check-ignore -v configs/dev/aset.local.yaml` → `.gitignore:50`; `ops/com.cobalt.aset.plist` (all); `ops/start_aset.sh` (all, exec `:73`).
- Read: `src/cobalt/voice/web.py:1`–`:313`; `src/cobalt/voice/config.py` (all); `configs/cobalt/voice.yaml:17`–`:46`.
- Read: `src/cobalt/heartbeat/probes.py:100`–`:189`; `runner.py:110`–`:149`; `configs/cobalt/smoke/s2.yaml:125`–`:165`; `ops/desk/deploy-smoke.sh:1`–`:160`; `grep` `DEPLOY-HUB.md` → allow `Bash(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*)` at `:11`, reads at `:123`, `:147`; `grep -rn` curl allow in `~/.claude/ops` → empty; `cobalt.sh` curls only `:1234`, `:8065` (`:36`, `:52`).
- Read: `src/cobalt/jobs/restarts.py:190`–`:264`; `configs/cobalt/jobs.yaml:68`, `:80`–`:91`, `:262`–`:272`.
- Read: `tests/cobalt/test_voice_web.py:1`–`:60`, `:225`–`:313`; `tests/cobalt/test_aset_config.py:100`–`:129`; `grep` 5010 in tests → `test_smoke.py:544`, `:548`, `:1488`, `:1499`, `:1512`; `test_deploy_smoke.py:43`, `:134`; `test_aset_config.py:114`; `sheet_daymode` tests pass their own URL (`test_sheet_daymode_probe.py:100`–`:159`).
- Read: uvicorn `0.40.0` (`uv.lock:5599`–`:5600`); `.venv/lib/python3.14/site-packages/uvicorn/config.py:207`, `:338`, `:474` (proxy headers on, trusted `127.0.0.1`).
- `grep` `100.70.206.126|ts.net|:5010` in `src`, `configs`, `ops`, `scripts` → only the probe, smoke, deploy-smoke, voice peer and comment lines listed above; no page builds an absolute URL.

HTTPS ONLY CARD DRAFTED · decisions: 10
