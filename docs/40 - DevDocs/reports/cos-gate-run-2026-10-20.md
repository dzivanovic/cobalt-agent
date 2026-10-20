# Gate run: F20 com.cobalt.cos (deferred), re-run on the deployed probe · 2026-10-20
Prompt `prompts/2026-10-19/873-cos-gate-run.md` · seat `cos-gate-run` · Opus 5.5 · main `45a85ba5` · `com.cobalt.cos` stays unloaded.

## RESULTS
```
GATE RESULT: com.cobalt.cos · D14 · NOT RUN — his decision, written from his ruling's R row by the desk
GATE RESULT: com.cobalt.cos · agent stopped · NOT RUN — his decision, written from his ruling's R row by the desk
GATE RESULT: com.cobalt.cos · X1 · OK (shell, not under a LaunchAgent)
GATE RESULT: com.cobalt.cos · X13 · OK (shell, not under a LaunchAgent)
GATE RESULT: com.cobalt.cos · X2 · FAIL auth: claude auth status exit 1 under the scratch HOME
GATE RESULT: com.cobalt.cos · X10 · FAIL auth: claude auth status exit 1 under the scratch HOME
GATE RESULT: com.cobalt.cos · X3 · FAIL auth: claude auth status exit 1 under the scratch HOME
GATE RESULT: com.cobalt.cos · X14 · FAIL auth: claude auth status exit 1 under the scratch HOME
GATE RESULT: com.cobalt.cos · X11 · FAIL auth: claude auth status exit 1 under the scratch HOME
GATE RESULT: com.cobalt.cos · X12 · OK — neither dummy in the child (child env names: CLAUDE_AGENT_SDK_VERSION, CLAUDE_CODE_ENTRYPOINT, CLAUDE_CODE_SDK_READS_SESSION_STATE, HOME, LANG, PATH, PWD, USER)
GATE RESULT: com.cobalt.cos · X15 · NOT RUN — waits for his word
GATE RESULT: com.cobalt.cos · X17 · FAIL auth: claude auth status exit 1 under the scratch HOME
GATE RESULT: com.cobalt.cos · X18 · OK — 8 deploy logs since 2026-10-15, no restart: median 28.5 s, max 641 s
GATE RESULT: com.cobalt.cos · X20 · OK — test_x20_redact_keeps_the_card_fragment_key passed
```

## DECISIONS
ASK DESK (for Dejan): Today the old agent (com.cobalt.agent) runs your Mattermost DM listener, the scheduler, the Scribe and the memory layer; may it stop after your trading day, with each of those four moved to a named new-core job or retired (you name which), and will you tap one test link on your phone so we read that the page sees its #k= key?
- ASK DESK: X11, X3, X2, X10, X14, X17 FAIL on one cause — the probe's `claude auth status` exits 1 under its scratch HOME, so no probe session ran; the login the probe expects is absent from that HOME while this seat's shell is logged in (X1). Fix the probe's auth carry (no keychain read by a seat, L41), then re-run these six. Default: cos stays unloaded. [12:29]
- ASK DESK: D14, agent stopped — his ruling's R row writes them. Default: cos stays unloaded. [12:29]
- ASK DESK: X15 — waits for his phone read of the `#k=` link. Default: cos stays unloaded. [12:29]
- ASK DESK: X1 `OK (shell, …)` leaves unproven that the CLI is logged in under a LaunchAgent's environment. Default: the line does not count for the bootstrap card. [12:29]
- ASK DESK: X13 `OK (shell, …)` leaves unproven that a `claude -p` call succeeds under a LaunchAgent; the shell run also printed a `.claude/settings.local.json` deny-rule warning line before `OK`. Default: the line does not count for the bootstrap card. [12:29]
- ASK DESK: X14 measured nothing (FAIL before any session): `max num_turns` not measured, `max seconds` not measured, beside `cos.max_turns` 30 and `cos.turn_timeout_s` 900. Default: the shipped values stand until the desk rules. [12:29]
- ASK DESK: X18 — two of eight spans exceed 300 s (f21-vectors 606 s, f5-checkpoints-fr2 641 s), both migration deploys. Default: the line stands as measured. [12:29]
- ASK DESK: main reads `45a85ba5`, not the prompt's `7e7bee6b`; the probe ran on this tree. Default: results stand. [12:29]

## RECORDS
Step 0
- `date` → `Tue Oct 20 12:28:04 EDT 2026`
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `45a85ba5`
- `ls /Users/cobalt/cobalt/src/cobalt/cos/probe.py` → `/Users/cobalt/cobalt/src/cobalt/cos/probe.py` (present)

Step 1 · X20 · `uv run pytest tests/cobalt/test_hitl_offline.py::test_x20_redact_keeps_the_card_fragment_key` → exit 0
```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/cobalt/cobalt
configfile: pyproject.toml
plugins: anyio-4.12.1, asyncio-1.3.0, logfire-4.22.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

tests/cobalt/test_hitl_offline.py .                                      [100%]

SLOTS WARN user.aset_sizings max_attnum 1474 of 1600 · dropped 1420 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)
============================== 1 passed in 0.06s ===============================
```

Step 2 · X11 · `uv run cobalt cos probe X11` → exit 1
```
PROBE X11 FAIL auth: claude auth status exit 1 under the scratch HOME
```

Step 3 · X12 · `uv run cobalt cos probe X12` → exit 0
```
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
PROBE X12 OK neither dummy in the child (child env names: CLAUDE_AGENT_SDK_VERSION, CLAUDE_CODE_ENTRYPOINT, CLAUDE_CODE_SDK_READS_SESSION_STATE, HOME, LANG, PATH, PWD, USER)
```

Step 4 · X3 · `uv run cobalt cos probe X3` → exit 1
```
PROBE X3 FAIL auth: claude auth status exit 1 under the scratch HOME
```

Step 5 · X1 · `claude auth status` → exit 0
- first non-empty line: `{` (JSON); its status field: `"loggedIn": true`, `"authMethod": "claude.ai"`, `"subscriptionType": "max"`

Step 5 · X13 · `claude -p --model claude-sonnet-5-5 'Reply with exactly the word OK'` → exit 0
```
Permission deny rule (.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax, so it is matched as a literal prefix (the * is not expanded) and matches only commands containing a literal * at that position. Use Bash(git push*) for wildcard matching.
OK
```
- first non-empty line: the deny-rule warning; the reply line: `OK`

Step 6 · X2 · `uv run cobalt cos probe X2` → exit 1
```
PROBE X2 FAIL auth: claude auth status exit 1 under the scratch HOME
```

Step 6 · X10 · `uv run cobalt cos probe X10` → exit 1
```
PROBE X10 FAIL auth: claude auth status exit 1 under the scratch HOME
```

Step 7 · X18 · Grep `bootout gui/501/com.cobalt.aset` over `reports/deploy-*.md` → 43 files; kept those whose deploy ran on or after 2026-10-15 and booted out and brought back aset. Times are each report's `<t down>` / `<t up>` lines.
- `deploy-jev-shadow-1015.md` (2026-10-15, attempt 2, `:334`) · 18:25:45 → 18:26:04 · 19 s · com.cobalt.aset
- `deploy-f4-refresh-attempt2.md` (2026-10-18, `:210`) · 12:42:45 → 12:43:13 · 28 s · com.cobalt.aset
- `deploy-f23-playbook.md` (2026-10-18, `:196`) · 13:54:13 → 13:54:56 · 43 s · com.cobalt.aset
- `deploy-f20-cos-attempt2.md` (2026-10-19, `:224`, `:236`) · 06:23:37 → 06:24:00 · 23 s · com.cobalt.aset
- `deploy-f16-close-fr2-attempt2.md` (2026-10-20, `:162`) · 00:39:43 → 00:40:00 · 17 s · com.cobalt.aset (rolled back after: 00:40:42 → 00:40:58, 16 s)
- `deploy-f21-vectors-1013.md` (2026-10-20, `:209`) · 01:44:14 → 01:54:20 · 606 s · com.cobalt.aset (migration 0028 proofs inside the outage)
- `deploy-f16-close-fr3.md` (2026-10-20, `:148`) · 03:42:45 → 03:43:14 · 29 s · com.cobalt.aset
- `deploy-f5-checkpoints-fr2.md` (2026-10-20, `:257`) · 09:59:24 → 10:10:05 · 641 s · com.cobalt.aset (migration 0029)
- Excluded: `deploy-jev-shadow-1015.md` attempt 1 (`:192`) — bootout left aset `SIGTERMed`, STEP-5 on the old tree. Every other match is dated before 2026-10-15.
- Spans sorted: 17, 19, 23, 28, 29, 43, 606, 641 s → median 28.5 s, max 641 s.

Step 8 · X14 · `uv run cobalt cos probe X14` (background) → exit 1
```
PROBE X14 FAIL auth: claude auth status exit 1 under the scratch HOME
```

Step 9 · X17 · `uv run cobalt cos probe X17` (background, after X14 exited) → exit 1
```
PROBE X17 FAIL auth: claude auth status exit 1 under the scratch HOME
```

Reads: the prompt; `topics/writing-rules.md`; Grep of `reports/deploy-*.md` (bootout, `<t down>`, `<t up>`, title lines).
End `date` → `Tue Oct 20 12:29:08 EDT 2026`

GATES DONE · ok: 5 · fail: 6 · not run: 3
