# Cobalt Assessment — Pass 3: Mattermost interface and HITL approval loop

Date: 2026-08-21 · Baseline: `cbd975d` (main) · Assessor: Claude Fable 5 · Mode: read-only toward the system (code read; only mocked/pure tests run; Mattermost's own tables in `cobalt_brain` queried with `SELECT` only; **no messages sent, no DB writes, no secrets read or printed**)

Scope: `interfaces/mattermost.py` (854), `core/proposals.py` (652), the HITL touchpoints in `main.py`, `brain/base.py`, `brain/cortex.py:118-150`, `tools/tool_manager.py` (`DANGEROUS_TOOLS`/`bypass_hitl`), `config.py` (MattermostConfig, `MATTERMOST_CREDS` routing, `inject_secrets`), `configs/prompts.yaml proposal`, `configs/rules.yaml cortex_routing`, senders in `services/scheduler.py` and `tools/daemon.py`, and `tests/test_proposals_intent.py`, `test_cortex.py`, `test_orchestrator.py`.

Verdict legend: **RETAIN** · **BROKEN-FRICTION** · **KILL-candidate** (proposal only — Dejan decides). **UNVERIFIED** = inferred, not read/run.

**Intent sources available** (tracked only — the vault's ADR/PRD notes are gitignored and were not read; `cobalt_master_context.txt` is absent from disk): git commit subjects/bodies (34 commits), the ADR/PRD/task text embedded in `dev_utils/generate_constitution.py` (Security Architecture note, ADR-001..003), `dev_utils/create_missing_tasks.py` (task "33 Mattermost C2 Integration"), `dev_utils/create_prd.py` (PRD-001), `configs/prompts.yaml`, `COBALT-REQUIREMENTS.md`. Commit `37f51ed` cites "ADR-014" (vault; not read). Intent is recorded separately from the verdict and did not influence it.

---

## 0. Headline findings

| # | Finding | Evidence |
|---|---|---|
| **H-1** | **The "token" is not a token — it is the proposal's 8-hex row id, and authorization is "anyone who can post where the bot listens".** `task_id = uuid.uuid4().hex[:8]` (`proposals.py:341`; 32 bits), printed in the approval card (`:273`). The listener accepts `approve|reject <8 chars>` from **any user in any channel/DM the bot sees**; the only identity check is "not the bot itself" (`mattermost.py:375`). The intended channel check is inverted — `ProposalEngine.handle_approval_response` compares the Mattermost **channel id** with the configured channel **name** `cobalt-approvals` (`proposals.py:499`), so for every approval it returns `None`, and the fallback path (`mattermost.py:396-472`) approves and **executes with no channel or user check at all**. Today's blast radius is small by configuration, not by code: Mattermost has 5 accounts (4 bots + `dejan_z`), `cobalt-approvals` is private with 2 members (`cobalt` bot, `dejan_z`). | code + live MM tables |
| **H-2** | **The approver cannot see what they are approving.** `Proposal.format_for_mattermost` (`proposals.py:252-274`) renders Action (= tool name only), Justification, Risk, and an Intent block — **never `parameters`** — and the live flow hard-codes `justification="AI-initiated action requiring human approval"`, `risk_assessment="Standard approval workflow"`, empty `IntentAlignment` (`mattermost.py:551-558, 660-667`). A `write_file` card shows neither path nor content; a `browser` card shows no URL. After approval the stored `tool_kwargs` run verbatim with `bypass_hitl=True` (`mattermost.py:416-420`). | file:line |
| **H-3** | **Replay is prevented; the "happy path" would not execute.** Re-`approve` of an approved/rejected id → `approve_and_get_payload` returns `None` → "No pending approval" (`proposals.py:432-439`) — good. But had the channel check ever passed, `handle_approval_response` marks the row approved and returns a "queued for execution" string **without executing** (`:503-508`), and the interface returns early (`mattermost.py:389-393`) — the tool would never run. Execution today happens only because the check is broken. The reject branch in `mattermost.py:474-498` is unreachable (the engine already handled it). | file:line |
| **H-4** | **On the schema.sql-first `hitl_proposals` DDL (Pass 1 H-2) HITL dies silently.** `create_proposal` inserts `(id, status, tool_name, tool_kwargs, created_at, updated_at)` (`proposals.py:63-68`) → fails on `instrument_id NOT NULL` / unknown columns → re-raised → swallowed by `think_and_reply`'s `except` (`mattermost.py:721-722`) → **no message to the user, no proposal**. `get_proposal` selects the same columns → `None` → every `approve` answers "No pending approval". Status literals also differ (`'pending'` vs `CHECK ('PENDING',…)`). | file:line |
| **H-5** | **Per-approval object churn (Pass 1 H-6 traced).** Each `approve/reject` message: `ProposalEngine()` (`mattermost.py:385`) → `HITLProposalStore()` → **`PostgresMemory()`** (≈10 DDL); then `self.proposal_engine.approve_and_get_payload` (engine from `main.py:187`, its store cached); then `ToolManager()` (`mattermost.py:416`) → **7 more `PostgresMemory()`** (Pass 2 H-9) → ≈ **8 constructions / ~80 DDL statements per approval**, plus 1–2 REST posts each needing team+channel lookups. Each ordinary `ACTION:` iteration builds another `ToolManager()` (`:631`). `HITLProposalStore` opens/closes a connection per operation and prints `[DEBUG]` lines to stdout (`proposals.py:61,69,75,171,177`). | file:line |
| **H-6** | **`MATTERMOST_CREDS` handling: the token is logged at DEBUG — suppressed in prod, printed to the terminal by dev tools.** Vault secret `MATTERMOST_CREDS` (JSON `{url, token}`) is merged into `master_data['mattermost']` (`config.py:580-581`); then `config.py:622` `logger.debug(f"Final merged configuration: {master_data}")` emits **the whole config incl. the token and every vault secret in `keys`**. `mattermost.py:77` logs `driver_options` (with token) at DEBUG. `main.py:62-82` removes loguru's default sink and logs at INFO → suppressed in the agent. But loguru's default stderr sink is **DEBUG** (v0.7.3) and `dev_utils/db_status.py`, `dev_utils/live_run_orchestrator.py`, `skills/research/enrich_metadata.py` (and anything constructing `FinvizApiClient`) call `get_config()` without `logger.remove()` → **all vault secrets + Mattermost token print to the terminal** on every run (verified by reading; deliberately not executed). Also `RAW WEBSOCKET PAYLOAD` is logged twice at INFO per event (`mattermost.py:338,817`) into `logs/agent_*.log` (7-day retention) — every message body, including anything a human pastes. `Config.inject_secrets` (`config.py:435-500`, keys `mattermost_url`/`mattermost_token`) is dead code. | file:line |
| **H-7** | **Failure behaviour: a failed login ends the process and nothing restarts it.** `start_mattermost_interface`: `connect()` False → `logger.error` + `return` (`main.py:182-184`) → `finally` blocks → `__main__` `finally` → `scheduler.shutdown()` → exit 0; `cobalt.sh` leaves a stale PID; `ops/com.cobalt.agent.plist` has **no `KeepAlive`** → agent stays down until someone notices (and the notification channel is the thing that failed). Once connected, the native WS loop reconnects forever with 5→60 s backoff (`mattermost.py:803-845`, RETAIN). Per-event exceptions are swallowed (`:729-730`). `get_my_user_id()` is a REST call **per message** (`:375`); if it fails the bot's own posts are no longer filtered (self-loop risk, UNVERIFIED ever occurred). **Four** Mattermost sessions exist: interface (`main.py:179`), `ProposalEngine.connect_mattermost` (`:188`, `proposals.py:313`), scheduler briefing (`scheduler.py:105-107`), daemon alerts (`daemon.py:228`). | file:line |
| **H-8** | **Timestamps are skewed by 5 h in the live table**: all 5 rows show `created_at → updated_at` ≈ 5 h 00 m (e.g. `15:01:13 → 20:01:41`). `create_proposal` writes `datetime.now()` (naive local, `proposals.py:54`), `update_status` uses DB `CURRENT_TIMESTAMP` (UTC, `:172`) into `TIMESTAMP` without tz. Real approval latency was ~15–30 s. | live DB + file:line |
| **H-9** | **Cortex "SECURITY INTERCEPT" proposals are never persisted.** `high_risk_keywords` (`rules.yaml`: delete/move/remove/format/execute/kill/reorganize) → `Cortex._generate_proposal` (`cortex.py:118-150`) asks the LLM for a card and returns it with a fresh `task_id` that is **not stored** → any `approve <id>` → "No pending approval". Functionally a hard block with a misleading UI. Cortex also re-classifies before checking risk (`:77,80`) — one LLM call wasted per intercepted message. | file:line |
| **H-10** | **Tests**: `test_proposals_intent` 3 pass (and *document* that `intent_alignment` is not enforced — defaults to empty); `test_orchestrator` 7 pass; **`test_cortex` 16 errors** — fixture patches `cobalt_agent.brain.cortex.load_config`, which does not exist (`tests/test_cortex.py:53`). **No tests** for `MattermostInterface`, `ProposalEngine`, `HITLProposalStore`, the approve/reject regexes, or the approval→execute path. | run output |

---

## 1. Component map — verdict + ORIGINAL INTENT

| Component | File:lines | Verdict | Notes | ORIGINAL INTENT (documentation trail) |
|---|---|---|---|---|
| `MattermostInterface.connect/disconnect/send_message/send_message_to_channel_id/get_my_user_id` | `mattermost.py:52-208` | RETAIN | `mattermostdriver` REST; `send_message` does team+channel lookups per call (2 REST round-trips) — cache ids. | Commit `5becd1e` (2026-02-24) "Integrated Mattermost regex listener"; task **33 Mattermost C2 Integration** ("Red Phone… remote command and control; Bot account 'Cobalt'; webhooks; kill switch `/cobalt stop`; interactive approve buttons", `create_missing_tasks.py:119-141`); Requirements §4/§9 (DM over Mattermost/Tailscale). Buttons/slash-commands/kill-switch never built. |
| `start_listening` (native `websockets` loop, backoff) | `mattermost.py:789-854` | RETAIN | Bearer header auth; ping 20 s; backoff 5→60 s; `brain` arg ignored (uses `self.brain`). | Commit `4f44d94` (2026-03-06) "Stabilized Mattermost native WebSocket connections and HITL Bouncer". |
| `_run_websocket_in_process`, `_handle_events` | `mattermost.py:732-787` | KILL-candidate (dead) | Never called (grep). Multiprocessing/`mattermostdriver.init_websocket` predecessor of the native loop. | UNVERIFIED — presumably the pre-`4f44d94` WS approach. |
| `_handle_mattermost_event`: boot notice, system-message filter, self-filter | `mattermost.py:327-378` | BROKEN-FRICTION | Boot message to `town-square` on `hello`/`status_change`; REST `get_my_user_id` per message (H-7). | Boot notice: UNVERIFIED (no doc). |
| Approval interceptor (`approve`/`reject` regex → engine → execute → broadcast) | `mattermost.py:380-500` | BROKEN-FRICTION (security H-1/H-2/H-3) | Executes via `ToolManager().execute_tool(bypass_hitl=True)` (`:416`); result → LLM summary → **`town-square` (public)** (`:452-458`); confirmation to approvals channel. Rejection branch dead (H-3). | Commits `5becd1e` "cryptographic task approval", `770c43b` (02-25) "End-to-End Zero Trust HITL architecture", `cf9cf4f` (03-01) "persistent HITL approvals"; Requirements §3/§11#1 "tokenized HITL approval pattern"; Security Architecture note §4 "One-Time Execution Token (OTET)… expires after execution or 500 ms" (`generate_constitution.py:206-211`) — describes a Sentinel→Ion **trade-execution** token that was never built and is now out of scope (no execution, ever). The implemented mechanism (reply "Approve <id>") is a different, weaker design than the documented one. |
| Cortex routing + per-message `ReAct` loop inside the interface | `mattermost.py:502-725` | BROKEN-FRICTION | Duplicates `BaseDepartment.run` with its own 3-iteration loop and `ToolManager()` per ACTION; runs in `asyncio.to_thread` (unbounded concurrency); `memory.add_log` of assistant replies only. | Commit `a55a96a` (02-08) ReAct pattern; `05b0617` (02-26) "Unified ReAct Engine" (intent was *one* engine — this loop contradicts it). |
| `_parse_action_response`, `_parse_action_string_wrapper` | `mattermost.py:210-325` | BROKEN-FRICTION | Third ACTION grammar (`key="value"`); defaults tool to `browser`; "Fuzzy Match Hack" maps `scrape`/`search` → `browser` (`:287-290`) — hijacks the real `search` tool. | Commit `4f44d94` "Resolved … ReAct parsing errors". Fuzzy hack: UNVERIFIED. |
| `HITLProposalStore` | `proposals.py:32-215` | RETAIN → single store (Pass 1 H-4) | Raw SQL on `PostgresMemory._get_conn()`; `print()` debug; manual commit/close on autocommit. | Commit `cf9cf4f` "persistent HITL approvals" (survive restarts). |
| `IntentAlignment`, `Proposal` (+`format_for_mattermost`) | `proposals.py:218-274` | RETAIN schema / BROKEN card (H-2) | Defaults make intent optional; card omits parameters. | Commit `37f51ed` (03-08) "intent-driven proposal loop… enforced intent_alignment schema… synced ADR-014" (ADR-014 in vault, not read). Test file admits enforcement "must happen at a higher validation layer" — it doesn't. |
| `ProposalEngine.create_proposal / send_proposal / approve_and_get_payload ("Airlock") / handle_approval_response` | `proposals.py:278-511` | BROKEN-FRICTION (H-1/H-3) | `send_proposal` posts the card via its **own** Mattermost session; "Airlock" = commit-then-execute pattern. | Commits `cf9cf4f`, `4f44d94`. Note: "The Airlock" in the Security Architecture note (`generate_constitution.py:214-218`) means network isolation of `Scout` — same word, different concept. |
| `ProposalEngine.wait_for_approval / execute_approved / set_approval_callback / start_monitoring / _monitor_approval_channel / stop_monitoring`; `create_proposal_and_send_to_mattermost` | `proposals.py:513-652` | KILL-candidate (dead/no-op) | No callers (grep); `_monitor_approval_channel` is a log line; `execute_approved` references `tool_name` before assignment if action lacks the `Tool: ` prefix (`:573-582`). | Commit `770c43b` "shared memory callbacks" — superseded by the persistent store (`cf9cf4f`). |
| `DANGEROUS_TOOLS` + `bypass_hitl` ("Bouncer"/"VIP pass") | `tool_manager.py:32-40,112-170` | RETAIN gate / BROKEN (Pass 2 H-7) | Any caller can pass `bypass_hitl=True`; only legitimate caller is the approval path. | `tool_manager.py:55-57` docstring ("Bouncer"); commit `4f44d94` "HITL Bouncer". |
| `BaseDepartment` `requires_approval` passthrough | `base.py:83-94` | RETAIN | Returns the dict to the caller; scheduler treats it as an error (`scheduler.py:83-86`). | Commits `05b0617`, `770c43b`. |
| `Cortex._generate_proposal` + `high_risk_keywords` + `prompts.yaml proposal.security_intercept` | `cortex.py:77-81,118-150`; `rules.yaml:1005-1006` | BROKEN-FRICTION (H-9) | Unpersisted card; LLM-generated justification. | Commits `5becd1e` "high-risk action interception", `87e16c7` (02-25) "deterministic Triage Desk"; `rules.yaml cortex_routing`. |
| `config.py` `MATTERMOST_CREDS` vault routing | `config.py:557-592` | RETAIN mechanism / BROKEN logging (H-6) | Token lives only in RAM (`master_data['mattermost']`), not in `os.environ` — good. | Commit `5becd1e` "Removed static API keys from .env and rewired config.py to use Vault"; `cc14caa` (04-07) "Zero-Trust config routing"; Security Architecture note §3 "No Hardcoded Keys… loaded into memory only at runtime". |
| `Config.unlock_vault / inject_secrets` | `config.py:407-500` | KILL-candidate (dead) | Expects vault keys `mattermost_url`/`mattermost_token`/`openai_api_key`…; never called. | UNVERIFIED — earlier naming scheme before `MATTERMOST_CREDS`. |
| `main.start_mattermost_interface` | `main.py:175-207` | BROKEN-FRICTION (H-7) | Builds interface + second engine session; attaches `cortex` as `brain`. | Commit `4f44d94`. |
| Scheduler briefing broadcast; daemon watcher alert | `scheduler.py:104-107`; `daemon.py:218-265` | BROKEN-FRICTION | New `MattermostInterface()`+login per send; `town-square` hard-coded. | `0bf87fd` (02-09) morning briefing; `333c2c3` (02-28) watcher daemon; task 33 "Incoming Webhooks for alerts". |

---

## 2. The approval flow, end to end (as the code actually runs)

```
[Dejan DMs/posts]  ──WS──►  _handle_mattermost_event (mattermost.py:327)
   text starts with "approve"/"reject"?
     yes → ProposalEngine()#new → handle_approval_response
              approve → channel_id != "cobalt-approvals" (name) → None            (proposals.py:499)
              reject  → mark rejected (if pending) → return "🛑 …" → sent → return  (:478-493)
           approve fallback (mattermost.py:396):
              self.proposal_engine.approve_and_get_payload(id)  → status pending? → set approved → payload
              ToolManager()#new(7×PostgresMemory).execute_tool(name, kwargs, bypass_hitl=True)
              LLM summary (brain.llm) → send_message("town-square")  ← public
              send_message_to_channel_id(approvals, "✅ … broadcast to town-square")
     no  → brain.route(text) in asyncio.to_thread
              Cortex high-risk keyword → _generate_proposal → card (NOT stored) → reply
              department returns {"status":"requires_approval"} → proposal_engine.create_proposal → store.get_proposal
                    → Proposal(card without parameters) → proposal_engine.send_proposal (2nd MM session) → "Action paused. Proposal [id] …"
              else ReAct loop (3 iters, ToolManager() per ACTION) → dangerous tool → same create/send path
```
Live table: 5 proposals, all approved, 2026-03-04..06 (`browser` ×4 with `url`/`query`, `write_file` ×1 with `filepath`/`content`); ids are 8 hex; no rejections ever recorded.

---

## 3. Security path — answers to the specific questions

1. **Can a proposal execute without a valid token?** Not through the interface: execution requires a *pending* row with that id (`approve_and_get_payload`). But (a) the id is an identifier, not a secret/HMAC — 32 bits, shown in the card; (b) **no user authorization**, **no channel enforcement** (inverted check); (c) `bypass_hitl=True` is a plain kwarg any code path can pass; (d) `execute_approved` (dead) would run without a DB check given `approved=True` on the object. Risk today is bounded by Mattermost membership (1 human, private channel), not by Cobalt.
2. **Replay / guessing**: replay blocked by status; guessing is 2³² over chat, irrelevant while the only posters are Dejan and bots — but any future shared channel/team member or a compromised bot account (`playbooks`, `calls`, `system-bot` exist) could approve. Ids also leak to `town-square` in rejection/execution broadcasts.
3. **Two DDLs**: see H-4 — schema.sql-first database ⇒ HITL silently non-functional; prod has the runtime DDL so it works there.
4. **Additional**: the approver sees no parameters (H-2); approved `tool_kwargs` execute verbatim; results of approved tools are broadcast to a public channel; timestamps skewed (H-8); Cortex intercept cards are un-approvable (H-9).

---

## 4. Hardcoded paths, names and structural assumptions

| Where | Value |
|---|---|
| `mattermost.py:350,457,467,491,497`, `scheduler.py:107`, `daemon.py:259` | channel `town-square` |
| `config.py:118-119` vs `configs/config.yaml:82-84` | defaults `cobalt-approvals` / `cobalt-team`; YAML sets team `cobalt-bridge` (matches live MM); tests mock `cobalt-team` |
| `mattermost.py:72,762`, `config.py:117` | port `8065`; `basepath /api/v4`; scheme default http |
| `mattermost.py:383,396,475`, `proposals.py:473,478` | `approve\s+(\w{8})` / `reject\s+(\w{8})`; `startswith("approve"/"reject")` |
| `proposals.py:241,341`, `postgres.py:1049` | 8-char ids from `uuid4` (three generators) |
| `proposals.py:273` | card instruction "Reply exactly with 'Approve {id}'" |
| `mattermost.py:554-555,663-664` | constant justification/risk strings |
| `mattermost.py:271,288-290` | default tool `browser`; `scrape`/`search` → `browser` |
| `mattermost.py:593` / `base.py:41` | `MAX_ITERATIONS=3` / `max_loops=4` |
| `mattermost.py:796-798,808` | backoff 5 s→60 s ×2; ping 20/20 |
| `mattermost.py:349` | boot text "🟢 Cobalt System Online … HITL Bouncer active." |
| `proposals.py:54,172`; DDL `TIMESTAMP` | naive local vs UTC |
| `proposals.py:64,172` vs `schema.sql:163` | status `'pending'/'approved'/'rejected'` vs `'PENDING'/'APPROVED'/'REJECTED'/'EXPIRED'` |
| `config.py:580` | vault key name `MATTERMOST_CREDS` (JSON `{url, token}`); alt env `COBALT_MATTERMOST__URL/TOKEN` via pydantic-settings (UNVERIFIED which is used in prod) |
| `config.py:479-482` (dead) | vault keys `mattermost_url`, `mattermost_token` |
| `rules.yaml:1006` | `high_risk_keywords` list |
| `prompts.yaml:111-125` | `security_intercept` template |
| `cortex.py:69` | web triage keywords incl. `"search"` (also a tool name) |

---

## 5. Tests run
- `uv run pytest tests/test_proposals_intent.py tests/test_cortex.py tests/test_orchestrator.py -q` → **10 passed, 16 errors** (all `test_cortex.py`: `AttributeError: module 'cobalt_agent.brain.cortex' does not have the attribute 'load_config'` at the fixture, `tests/test_cortex.py:53`).
- No Mattermost traffic, no DB writes; Mattermost tables read via catalog `SELECT` only (team/channel names, member usernames, counts).

## 6. RETAIN / BROKEN-FRICTION / KILL-candidate summary
**RETAIN**: native WS listener + backoff; REST helpers; persistent `hitl_proposals` concept + `HITLProposalStore` (as the single store); `DANGEROUS_TOOLS` gate with post-approval bypass only; `approve/reject <id>` chat UX; `Proposal`/`IntentAlignment` schema; vault-routed `MATTERMOST_CREDS` (RAM-only); private approvals channel as set up.
**BROKEN-FRICTION**: authz/channel check (H-1, H-3); content-free approval card (H-2); DDL conflict behaviour (H-4); per-approval object churn + per-ACTION `ToolManager()` (H-5); secret-bearing DEBUG logs + raw payload INFO logs (H-6); exit-on-login-failure, no `KeepAlive`, four MM sessions, per-message `get_my_user_id` (H-7); naive timestamps (H-8); unpersisted Cortex intercept (H-9); duplicated ReAct loop + third ACTION grammar + fuzzy tool remap; public broadcast of approved-tool results; `print()` debugging in store; tests (H-10).
**KILL-candidates**: `wait_for_approval`, `execute_approved`, `set_approval_callback`, `start/stop_monitoring`, `_monitor_approval_channel`, `create_proposal_and_send_to_mattermost`; `_run_websocket_in_process`, `_handle_events`; `Config.unlock_vault`/`inject_secrets`; `PostgresMemory` `_hilt_` trio (Pass 1); unreachable reject branch (`mattermost.py:474-498`); `handle_approval_response` approve branch (or make it the one true path); `_generate_proposal` as-is (persist it or drop the card); fuzzy `scrape/search→browser` remap.

## 7. Inputs to other passes / INFRA
- **INFRA-0**: add `logger.remove()`/level control to every entry point or drop `config.py:622`; rotate the Mattermost bot token if dev tools have been run with terminal logs captured (UNVERIFIED exposure; the line exists since at least `cc14caa`).
- **INFRA-0.5 / ops**: `KeepAlive` (or `cobalt.sh` supervisor) + out-of-band alert for "Mattermost login failed" (voice/CLI/log watch).
- **INFRA-1**: HITL will not work on a `cobalt_dev` created from `schema.sql` first (H-4).
- **Pass 5**: three ACTION grammars; `Cortex` double LLM call on intercept; `mattermost.py` own ReAct loop.
- **Pass 7**: `MattermostConfig` defaults vs YAML; env vs vault precedence for the token.
- **Requirements §11#1 "tokenized HITL"**: the implemented design is id-based chat approval with no identity binding; a real token (per-proposal secret known only to the approver, or Mattermost interactive message callbacks with user id verification) is a design decision for Dejan, not a fix.

## 8. UNVERIFIED (explicitly)
- Whether the bot token in prod comes from vault `MATTERMOST_CREDS` or `COBALT_MATTERMOST__*` env (`.env` not read).
- Whether any dev_utils run has written the DEBUG config dump to a persisted log (terminal sessions/`logs.vscode/` not read).
- Whether the self-loop (H-7, `get_my_user_id` failure) or the `hello` boot event payload contains sensitive fields (not reproduced).
- ADR-014 content (vault; cited by commit `37f51ed`).
- Whether `COBALT_SYSTEM__DEBUG_MODE`/`debug_mode: true` (`config.yaml:4`) changes any log level (no code found that uses it for logging — it only feeds the phantom `vault.master_key` branches).
