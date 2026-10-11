# SDK spike live 2026-10-11 (S5 Lane C; gates F20, F21; closes U1-U5 of `reports/sdk-spike-2026-10-10.md`)

Desk copy of `/Users/cobalt/cobalt-wt/sdk-spike-1010/report.md` (seat `c4dd3950`, 15:13-15:24 EDT). The evidence logs stay in `/Users/cobalt/cobalt-wt/sdk-spike-1010/out/`.

## §0 Headline
- Verdict PARTIAL. HITL (Q1) WORKS and the failure surface (Q4) WORKS. Both ran live on THE PIN `claude-agent-sdk==0.2.160` (bundled CLI 2.1.283), on his subscription login (`apiKeySource: "none"`).
- Q1: a `PreToolUse` hook or `can_use_tool` posts a card to the local sink and blocks the call until the reply comes. Approve runs the call; deny and no-reply refuse it. A hook that outlives its own timeout fails CLOSED. Jailed reads pass with no card.
- Q4: kill → `ProcessError` exit -9. Hang and timeout → caller watchdog `TimeoutError` only. `max_turns` → `error_max_turns`, distinct from success. Session ids survive and resume, even after a kill.
- Q3 PARTIAL: Anthropic's terms name Agent SDK use on Pro/Max ("ordinary, individual usage") and also steer "developers building products" to API keys. Cobalt's side of that line is his ruling.
- Q2 FAILS direct: LM Studio :1234 rejects the CLI's request (HTTP 400). LiteLLM :4000 is not running, so the proxy path is UNKNOWN.

## ANSWERS (summary; per-row evidence lines are in the seat's report)
| # | Question | Verdict | F20/F21 may rely on |
|---|---|---|---|
| Q1 | HITL: block risky call → card on sink → wait → allow/refuse; jailed read free | WORKS | A per-tool `PreToolUse` hook (async Python, awaits our card) gates risky tools whatever the allow rules say. It fails closed on hook timeout, so set `HookMatcher.timeout` ≥ the card TTL. Use `allowed_tools` path rules (`Read(//jail/**)`) for free jailed reads, and `can_use_tool` as the deny-by-default backstop. The model sees our reason string as an `is_error` tool result. On the hook path the CLI prefixes "PreToolUse:Bash hook error:", even for a clean deny. |
| Q4 | Failure surface: dead, hung, timeout, `max_turns`; distinguishable; session id kept | WORKS | Fail-loud = test `ResultMessage.is_error` and `terminal_reason`, never `subtype` alone (an API error arrives as subtype "success" with is_error true). `max_turns` is distinguishable both ways (`ClaudeSDKClient` returns normally; `query()` raises `ResultError`). The SDK has no inactivity detection: a hung CLI is silent until OUR watchdog fires, so the L18 heartbeat/timeout is mandatory. A dead CLI raises at once, but its tool children are orphaned, so the runner must kill the process group. Store `session_id` per task row; it resumes with context after a crash. |
| Q3 | ToS for Agent SDK / Claude Code on a subscription | PARTIAL | Never extract, store or route OAuth tokens. Sessions run on the unmodified CLI with his own login. No third party ever signs in through Cobalt. Whether unattended runs need an API key is HIS RULING (D7 of the seat's list, D2 below). Sources: `code.claude.com/docs/en/legal-and-compliance`, `code.claude.com/docs/en/agent-sdk/overview`, `anthropic.com/legal/consumer-terms` (effective 2025-10-08). |
| Q2 | Local backend via `ANTHROPIC_BASE_URL` | FAILS (direct LM Studio); proxy UNKNOWN | LM Studio's Anthropic-shaped endpoint rejects the CLI's request on the first call (HTTP 400). The L22 LiteLLM proxy path is untested (nothing on :4000). F20 runs subscription sessions only; local work stays on the fast wire. |
| U5 | Versions | RECORDED | SDK 0.2.160, bundled CLI 2.1.283, host `claude` 2.1.296, python 3.14.3. The SDK runs its own bundled CLI; pin both through THE PIN. |
| F21 | Depends on SDK? | NO DEPENDENCY (unchanged) | F21 proceeds on the fast wire. |

## UNKNOWN
- U2b: the LiteLLM-proxy path (L22) for SDK sessions: no proxy answers on :4000; needs a seat allowed to start one.
- U6: hook/gate behavior under parallel tool calls in one turn, and under subagents; not run.
- U7: card wait beyond 300 s (a human away for hours): 300 s held with no CLI cutoff; longer is untested.
- U8: subscription rate-limit behavior under sustained unattended load (`RateLimitEvent` seen: `five_hour`, status `allowed`, overage `org_level_disabled`).
- U9: the two-session test (subscription CoS + local worker via proxy, `SPRINT-LADDER-v0_1.md:470`), still owed with U2b.

## DECISIONS
- D1 ASK DESK: report path (default: scratch report, desk copies). DONE: this file.
- D2 ASK DESK: Q3 ruling: is Cobalt's unattended CoS on his own Max login "ordinary, individual usage", or must unattended sessions move to a Console API key? (default: subscription for his single-user use; F20 keeps auth a config switch so moving to a key changes config, not code).
- D3 F20 HITL = `PreToolUse` hook per risky tool, plus `can_use_tool` deny-by-default backstop, plus `allowed_tools` path rules for jailed reads; `HookMatcher.timeout` ≥ card TTL; Cobalt keeps its own card ledger, since a hook-timeout refusal is absent from `permission_denials`. Default taken.
- D4 F20 runner sets `setting_sources=[]` and `strict_mcp_config=True` (claude.ai connector tools otherwise entered the jailed session). Default taken.
- D5 F20 runner: fail on `is_error`/`terminal_reason`, own watchdog per session, kill the CLI's process group on teardown, `session_id` stored per task row. Default taken.
- D6 Inner sessions ran on `claude-haiku-5-5` to spare his quota. Default taken.
- D7 The `max_turns` test used `max_turns=2` and the local session 6; every other session ran at 30. Default taken.
- D8 Q2 port: probed :1234 and :4000 with GET only; a dummy `ANTHROPIC_AUTH_TOKEN` so his OAuth bearer never went to localhost. Default taken.
- D9 The base prompt asks for a git worktree before edits; SPIKE-HUB holds (plain scratch dir, no git). Worked in place; nothing committed.
- D10 Re-spike owed for U2b/U9 (LiteLLM proxy started by a launched seat). Desk schedules (default: after F20 design, not blocking it).

SDK SPIKE LIVE DONE · verdict: PARTIAL · decisions: 10
