# Gate run: F20 `com.cobalt.cos` (deferred), re-run on the deployed probe — 2026-10-20
Prompt `prompts/2026-10-19/873-cos-gate-run.md` · seat `cos-gate-run` · Opus 5.5 · dev (no `COBALT_ENV`) · `com.cobalt.cos` stays unloaded.

## RESULTS
GATE RESULT: com.cobalt.cos · D14 · NOT RUN — his decision, written from his ruling's R row by the desk
GATE RESULT: com.cobalt.cos · agent stopped · NOT RUN — his decision, written from his ruling's R row by the desk
GATE RESULT: com.cobalt.cos · X1 · OK (shell, not under a LaunchAgent)
GATE RESULT: com.cobalt.cos · X13 · FAIL — CLI's first line: `Permission deny rule (.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax, …`; the reply line after it was `OK`
GATE RESULT: com.cobalt.cos · X2 · OK — no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)
GATE RESULT: com.cobalt.cos · X10 · OK — no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)
GATE RESULT: com.cobalt.cos · X3 · OK — cap: turn stopped at max turns; kill: the session died; timeout: timeout after 10s, the CLI was killed
GATE RESULT: com.cobalt.cos · X14 · OK — ok 20/20 · max num_turns 6 · max seconds 7.4 (caps: max_turns 30, timeout 900s)
GATE RESULT: com.cobalt.cos · X11 · OK — init tools 7, all mcp__cobalt__* allowlisted (planted server started: no)
GATE RESULT: com.cobalt.cos · X12 · OK — neither dummy in the child
GATE RESULT: com.cobalt.cos · X15 · NOT RUN — waits for his word
GATE RESULT: com.cobalt.cos · X17 · OK — sonnet ok 20/20 · opus ok 20/20
GATE RESULT: com.cobalt.cos · X18 · OK — 8 deploy logs since 2026-10-15, no restart: median 30.5 s, max 641 s
GATE RESULT: com.cobalt.cos · X20 · OK — 1 passed

## DECISIONS
ASK DESK (for Dejan): Today the old agent (com.cobalt.agent) runs your Mattermost DM listener, the scheduler, the Scribe and the memory layer; may it stop after your trading day, with each of those four moved to a named new-core job or retired (you name which), and will you tap one test link on your phone so we read that the page sees its #k= key?
ASK DESK: X13 FAIL. The model replied `OK`, but stderr carried a settings warning first (`.claude/settings.local.json` deny rule `Bash(git push*:*)`). Rule it, or fix the rule to `Bash(git push*)` and re-run X13. Default: cos stays unloaded. [17:31]
ASK DESK: D14 NOT RUN. The desk writes it from his ruling's R row. Default: cos stays unloaded. [17:31]
ASK DESK: agent stopped NOT RUN. The desk writes it from his ruling's R row; the stop happens inside the bootstrap deploy hub. Default: cos stays unloaded. [17:31]
ASK DESK: X15 NOT RUN. Waits for his phone read on the `#k=` test link. Default: cos stays unloaded. [17:31]
ASK DESK: X1 `OK (shell, not under a LaunchAgent)` leaves the login under a LaunchAgent unproven; the first LaunchAgent run is the bootstrap deploy. Default: the line does not count for the bootstrap card. [17:31]
ASK DESK: X14 measured max num_turns 6 (cap `cos.max_turns` 30) and max seconds 7.4 (cap `cos.turn_timeout_s` 900). Default: the shipped values stand until the desk rules. [17:31]

## RECORDS
Step 0:
- `date` → `Tue Oct 20 17:25:39 EDT 2026`
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `52d4e906` (the prompt names `7e7bee6b`; main has moved since, to the R2194 desk commit, probe tag `deploy-2026-10-20-cos-probe-fr1`, later fr2b)
- `ls /Users/cobalt/cobalt/src/cobalt/cos/probe.py` → `/Users/cobalt/cobalt/src/cobalt/cos/probe.py`

Step 1, X20: `uv run pytest tests/cobalt/test_hitl_offline.py::test_x20_redact_keeps_the_card_fragment_key` · exit 0
```
collected 1 item
tests/cobalt/test_hitl_offline.py .                                      [100%]
============================== 1 passed in 0.05s ===============================
```

Step 2, X11: `uv run cobalt cos probe X11` · exit 0
```
AUTH exit 0 · loggedIn=true authMethod=claude.ai
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
PROBE X11 OK init tools 7, all mcp__cobalt__* allowlisted (planted server started: no)
```

Step 3, X12: `uv run cobalt cos probe X12` · exit 0
```
AUTH exit 0 · loggedIn=true authMethod=api_key
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
PROBE X12 OK neither dummy in the child (child env names: CLAUDE_AGENT_SDK_VERSION, CLAUDE_CODE_ENTRYPOINT, CLAUDE_CODE_SDK_READS_SESSION_STATE, HOME, LANG, PATH, PWD, USER)
```
X12's AUTH line reads `authMethod=api_key`; every other probe reads `claude.ai`.

Step 4, X3: `uv run cobalt cos probe X3` · exit 0
```
AUTH exit 0 · loggedIn=true authMethod=claude.ai
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
Fatal error in message reader: Command failed with exit code -9 (exit code: -9)
Error output: Check stderr output for details
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
PROBE X3 OK cap: ok=False subtype=None terminal=None reason=turn stopped at max turns; kill: ok=False subtype=None terminal=None reason=the session died; timeout: ok=False subtype=None terminal=None reason=timeout after 10s; the CLI was killed
```

Step 5, X1: `claude auth status` · exit 0 · first non-empty line `{`; the JSON reads `"loggedIn": true`, `"authMethod": "claude.ai"`, `"apiProvider": "firstParty"`, `"subscriptionType": "max"`.
Step 5, X13: `claude -p --model claude-sonnet-5-5 'Reply with exactly the word OK'` · exit 0
```
Permission deny rule (.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax, so it is matched as a literal prefix (the * is not expanded) and matches only commands containing a literal * at that position. Use Bash(git push*) for wildcard matching.
OK
```

Step 6, X2: `uv run cobalt cos probe X2` · exit 0
```
AUTH exit 0 · loggedIn=true authMethod=claude.ai
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)
```
Step 6, X10: `uv run cobalt cos probe X10` · exit 0
```
AUTH exit 0 · loggedIn=true authMethod=claude.ai
[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5","query_source":"sdk"}
PROBE X10 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)
```

Step 7, X18: Grep `bootout gui/501/com.cobalt.aset` in `reports/deploy-*.md` → 43 files; 8 deployed on or after 2026-10-15 and brought `com.cobalt.aset` back. Each span runs from the report's `<t down>` (the `date` read just before the bootout, step 4.1) to its `<t up>` (the `date` read after `launchctl bootstrap`, `state = running`). No report states a first `/api/health` 200. Where a report has two outages, the first is counted.
- `deploy-jev-shadow-1015.md` · 32 s (18:18:33 → 18:19:05, attempt 1 rollback; attempt 2 18:25:45 → 18:26:04, 19 s) · com.cobalt.aset
- `deploy-f4-refresh-attempt2.md` · 28 s (12:42:45 → 12:43:13, 2026-10-18) · com.cobalt.aset
- `deploy-f23-playbook.md` · 43 s (13:54:13 → 13:54:56, 2026-10-18) · com.cobalt.aset
- `deploy-f20-cos-attempt2.md` · 23 s (06:23:37 → 06:24:00, 2026-10-19) · com.cobalt.aset
- `deploy-f16-close-fr2-attempt2.md` · 17 s (00:39:43 → 00:40:00, 2026-10-20; rollback 00:40:42 → 00:40:58, 16 s) · com.cobalt.aset
- `deploy-f21-vectors-1013.md` · 606 s (01:44:14 → 01:54:20, 2026-10-20) · com.cobalt.aset
- `deploy-f16-close-fr3.md` · 29 s (03:42:45 → 03:43:14, 2026-10-20) · com.cobalt.aset
- `deploy-f5-checkpoints-fr2.md` · 641 s (09:59:24 → 10:10:05, 2026-10-20) · com.cobalt.aset

Sorted: 17, 23, 28, 29, 32, 43, 606, 641 → median 30.5 s, max 641 s. The 606 s and 641 s spans include the merge and validate steps between bootout and bootstrap.
Reads: Grep over `reports/deploy-*.md`; `deploy-f16-close-fr2-attempt2.md:136-160`; `deploy-jev-shadow-1015.md:194-207`.

Step 8, X14: `uv run cobalt cos probe X14` (background) · exit 0 · last line:
```
PROBE X14 OK ok 20/20 · max num_turns 6 · max seconds 7.4 (caps: max_turns 30, timeout 900s)
```

Step 9, X17: `uv run cobalt cos probe X17` (background, after X14 exited) · exit 0 · last line:
```
PROBE X17 OK sonnet ok 20/20 · opus ok 20/20
```

Every probe prints `[claude-code:unrecognized_model] {"model":"claude-sonnet-5-5",…}` before its result.
Other reads: `topics/writing-rules.md`.
`date` at end → `Tue Oct 20 17:31:49 EDT 2026`

GATES DONE · ok: 10 · fail: 1 · not run: 3
