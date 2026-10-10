# F20 Chief of staff, thin — design proposal · 2026-10-10
Input to the L67 tribunal. No card, no build before the tribunal and his terms word (Q3).
Code cited at `d0a5fbb8`. Direction: brain R858, after `reports/sdk-spike-2026-10-10.md`.

## 1. Scope
- Acceptance (Charter:195-198; LADDER:934): one resident session; he talks only to it in a Mattermost DM; HITL cards in one place, full detail, Approve/Deny; agents are registry entries (L16). The test: a config-drafted agent appears only after an approved HITL card.
- Chassis: one Agent SDK session on his subscription login (L22). No API key, no proxy.
- HITL path: the spike's D2 fallback is the primary path. Risky tools are absent from the session's allowlist. The model asks for an action through one Cobalt tool, `request_action`. Cobalt code writes the request row and the card. Only his tap approves the request (L37), and only Cobalt code executes it. F20 does not use an SDK hook or a `canUseTool` callback (U1).
- First action catalog: `agents.create` and `agents.deactivate`. Nothing else.

## 2. Components and files touched
| Path | New/changed | What |
|---|---|---|
| `src/cobalt/cos/listener.py` | new | A deterministic DM reader (L2: no LLM in the watch loop) on the bot account `notify.yaml` names (`MATTERMOST_CREDS`, `configs/cobalt/notify.yaml:13-14`). It matches the kill and resume phrases first, through `killswitch.matches_kill_phrase` / `matches_resume_phrase` (`src/cobalt/jobs/killswitch.py:106`, `:118`; phrases in `configs/cobalt/jobs.yaml:351-352`). Every other message becomes a turn row and goes to the session. |
| `src/cobalt/cos/session.py` | new | The SDK client wrapper. It fixes the options (§4), max turns, the turn timeout, resume by stored session id, and an env allowlist. |
| `src/cobalt/cos/tools.py` | new | An in-process tool server. Read tools: `cards.open`, `radar.pool`, `jobs.status`, `hitl.list`, `agents.list`. Request tools: `request_action`, `draft_agent` (the model's view of `agents.create`). The server has NO approve or decide tool. |
| `src/cobalt/cos/store.py` + `migrations/0001_cobalt_cos.sql` | new | `cobalt_cos_sessions` (channel, agent_id, session_id, started_at, rotated_at, state) and `cobalt_cos_turns` (id, message ref, state pending/running/done/failed, started_at, finished_at, num_turns, result_subtype, error). One row per turn (L18). |
| `src/cobalt/hitl/{models,store,actions,card}.py` + `migrations/0001_cobalt_hitl.sql` | new | `cobalt_hitl_requests`: id, short_id, agent_id, action, payload JSONB (canonical), sha256, reason, status pending/approved/denied/expired/executed/failed, created_at, expires_at, decided_at, decided_via, deny_reason, result JSONB, error. The action catalog maps each action to one deterministic executor owned by its expert role (L40). |
| `src/cobalt/agents/registry.py` | new | The generic L16 registry over `configs/cobalt/agents/*.yaml`: id, charter, chassis, tools (each named in the code catalog, else refused at load, the same rule as `src/cobalt/voice/registry.py:9-11`, `:62-68`), schedule (optional), memory_namespace, enabled. `voice.yaml` keeps its own loader (`voice/registry.py:85`); the generic loader lists it without re-validating it. |
| `configs/cobalt/agents/cos.yaml` | new | The CoS entry: charter, chassis `{kind: sdk, auth: subscription, model: <alias>}`, tools. |
| `configs/cobalt/taxonomy/tunables.yaml` | changed | New rows (F16): `cos.max_turns` 30, `cos.turn_timeout_s` 900 (kit start values, spike Q4), `cos.poll_interval_s`, `hitl.request_ttl_min`, `cos.session_rotate_at`. |
| `src/cobalt/aset/web.py` | changed | `GET /hitl` (the one place), `GET /hitl/{id}` (full payload, sha256, the rendered file for `agents.create`), `POST /hitl/{id}/approve` and `/deny`. It follows the reviewed-sha256 form pattern already in place (`aset/web.py:1305-1380`): the hidden sha256 must equal the stored one, or nothing is written. The aset is served over HTTPS only (L80). |
| `configs/cobalt/jobs.yaml` + `ops/com.cobalt.cos.plist` | changed / new | Resident `com.cobalt.cos`, `supervisor: self`, `timeout_s` ≥ the turn timeout, `reads:` named, `imports:` named (L42). |
| `configs/cobalt/generated.yaml` | changed | Declares `configs/cobalt/agents/*.yaml` so the 23:37 job commits an approved agent file (`jobs.yaml:298-316`). |
| `src/cobalt/heartbeat/probes.py` | changed | A `cos` probe (row state + session liveness) and a `hitl` probe (pending past the TTL, failed executions): AMBER/RED. |
| `src/cobalt/cli.py` | changed | `cobalt cos run`, `cobalt agents list`, `cobalt hitl list`, and dry runs (L10). |
| `pyproject.toml`, `uv.lock` | changed | Add the Python Agent SDK, pinned. This restarts every resident that reads them (`jobs.yaml:88-89`, `:157-158`, `:201-202`; L42). |

## 3. HITL tool and card flow
1. The model calls `request_action{action, args, reason}` (or `draft_agent{yaml}`).
2. Code validates the action against the catalog and the args against the action's schema, then runs `refuse_if_secret_shaped` on the args (`src/cobalt/modelaccess/guard.py:40`). An unknown action, a bad arg or a secret-shaped arg goes back to the model as a refusal. No row is written.
3. For `agents.create`, code parses the YAML with the registry schema and refuses an unknown tool or a bad chassis. Code renders the canonical payload, hashes it (sha256), writes the request row with status `pending` and `expires_at` = now + TTL, and returns `pending <short_id>` to the model at once. The session never blocks on him.
4. Code sends the card DM through `notify.mattermost.send_dm` (`src/cobalt/notify/mattermost.py:130`), so the F19 redaction runs (`:13-17`; `redact/guard.py:80`). The DM carries the action, a one-line summary, the short id and the `https://…/hitl/<id>` link.
5. On the card page he taps Approve or Deny. The POST carries the reviewed sha256. Approve checks, in order: status `pending`, not expired, sha256 equal, kill switch clear. Then the row becomes `approved`, `decided_via=aset:<request ip>`. Deny records the row and an optional reason.
6. The CoS resident picks up `approved` rows and runs the executor. For `agents.create`, the executor writes `configs/cobalt/agents/<id>.yaml` create-if-absent, and the bytes on disk must hash to the approved sha256. The row becomes `executed` or `failed`, with the error. A DM reports the outcome, and one line goes into the session as a Cobalt message: `HITL <id> executed|denied|expired|failed`.
7. When `expires_at` passes, the row becomes `expired`, the DM reports it, and so does the heartbeat.
- L37: no model holds an approve path, a text "approve" in the DM is not an approval (the listener passes it to the model as plain text), and the approval is the POST from his browser bound to the sha256.
- L7's interim clause says "No HITL token mechanism exists yet". F20 ships one, so the clause is amended at deploy (RULING proposal in the report).

## 4. Session permissions (the new permission class)
- `allowed_tools`: exactly the `cos/tools.py` set. `disallowed_tools`: Bash, Write, Edit, NotebookEdit, WebFetch, WebSearch, Task, and every other built-in.
- `permission_mode`: never `bypassPermissions` (L55; spike Q1). Without a callback, an unlisted tool must be refused. A scratch test proves that before the first deploy (L29: the gate stops file AND command writes).
- Env allowlist for the spawned CLI: PATH, HOME, USER, LANG, COBALT_ENV. `ANTHROPIC_API_KEY` and `ANTHROPIC_BASE_URL` are absent (so the session stays on the subscription meter, L27). So are `COBALT_MASTER_KEY` and the DB credentials: the session holds no credential (L41), and the executors fetch their own credentials.
- `cwd`: an empty scratch directory under the job's own state directory. No repo, no vault.

## 5. Failure surface (L18)
| Case | Detection | Loud |
|---|---|---|
| Turn hits `cos.max_turns` | Result subtype ≠ success (U4: exact subtype unproven) | Turn `failed`; DM "turn stopped at max turns"; partial reply posted |
| Turn exceeds `cos.turn_timeout_s` | `asyncio.wait_for` around the turn; CLI subprocess killed | Turn `failed: timeout`; DM |
| No result event or subprocess dies | Stream ends without a result → treat as failed (U4) | Turn `failed`; DM; the next turn opens a fresh session if resume fails |
| Listener hung | The resident stamps `heartbeat_at` from its loop, not from a free thread (`jobs/wrapper.py:78-110` beater stamps only liveness) | Watchdog marks the row ZOMBIE (`cobalt_jobs`, `src/cobalt/jobs/migrations/0001_cobalt_jobs.sql:43-60`); heartbeat RED |
| Meter out / login expired | CLI error text classified `meter` / `auth` | DM "CoS down: <class>"; heartbeat AMBER; no fallback house in F20 (L25 Phase 1) |
| Kill phrase | Listener, before the session | `killswitch.engage`; the session is not called; executors refuse |
| Executor fails | Exception in the executor | Row `failed`; DM; no retry without a new card |
| Two listeners on one bot | Start check: the `com.cobalt.agent` pidfile alive (`jobs.yaml:127-131`) → refuse to start | FAILED start, loud |

## 6. Tests
- T1 (acceptance, `cobalt_dev`): `draft_agent` → `agents list` without it → approve with the stored sha → file present + listed. Deny and expire → absent.
- T2: sha mismatch, expired, double approve, approve under the kill switch → each refused, nothing written.
- T3 (L37, static): the tool server exposes no approve/decide/execute verb; the approve route exists only in `aset/web.py`.
- T4: session options: the allowlist equals the set, the disallowed list holds every built-in, the mode is never `bypassPermissions`.
- T5: the env of the spawned process has no API key, base URL, master key or DB credential.
- T6 (fake SDK client): hang → timeout `failed`; max-turns subtype → `failed`; stream ends with no result → `failed`; each sends a DM.
- T7: kill and resume phrases are intercepted before the session.
- T8: a secret-shaped arg is refused; a card DM with a token is redacted (F19).
- T9: registry: an unknown tool is refused; `voice.yaml` still loads through its own loader.
- T10 (live scratch, gated, not in the offline suite): a real session told to run Bash and to write a file. No command runs, no file exists. Also records the max-turns and kill result shapes (closes U4). The result goes in the build report.
- L45: the DM-event fixture is a real-shape Mattermost post (redacted).

## 7. Risks
- R1 Q3 terms (U3): the build is gated on his word.
- R2 The CoS draws on the same Claude meter as the build seats (L47); the model is a config value.
- R3 launchd + the CLI's keychain login under a LaunchAgent: UNKNOWN; the build's first step proves it.
- R4 SDK churn: pin the version; T6 runs on a fake client, so CI does not depend on the vendor.
- R5 Prompt injection through read tools: the worst outcome is a request, and a request needs his tap.
- R6 Session context growth: daily rotation at `cos.session_rotate_at`.
- R7 The old listener (`com.cobalt.agent`, `jobs.yaml:127-160`) shares the bot: L3; its decommission is a deploy step (`areas/cobalt-sprints.md:12`). What else that process still serves is UNKNOWN.

## 8. NOT in F20
Running or scheduling specialist agents (F20 registers them; it does not run them) · `@agent:` delegation · memory and genesis import (F21) · voice CoS · local model via a proxy (U2) · hook- or callback-based gating (U1, an optimization row) · actions beyond `agents.create` / `agents.deactivate` · Mattermost interactive buttons · the L41 credential broker · hive mind, council, cost footer.

## 9. Open choices (default · reason)
| # | Choice | Default | Reason |
|---|---|---|---|
| C1 | Where he approves | The aset `/hitl` page only; a DM text "approve" is not an approval | One place (Charter:195-198); the approval is bound to a sha256 by code, never parsed out of text the model also reads (L37) |
| C2 | Where an approved agent lives | `configs/cobalt/agents/<id>.yaml`, committed by `com.cobalt.generated`; plus the request row | L10 config in git; L16 registry entry; `voice.yaml` precedent |
| C3 | Who executes an approved action | The CoS resident's executor, not the aset web process | Keeps executors out of the trading sheet's process and its restarts (L42) |
| C4 | SDK language | Python SDK, pinned | The repo is Python; L15 makes the kit's TS reference only |
| C5 | CoS model | Sonnet 5.5, a config value | F20 is thin (talk, read, request); the Opus meter belongs to builds (L47); Opus is one config line away |
| C6 | Local backend (U2) | N/A for the MVP: subscription only | LM Studio exists (`configs/cobalt/modelaccess.yaml:17-22`, OpenAI-compatible), but no LiteLLM proxy runs (no proxy job in `jobs.yaml`); `litellm` is only a library dependency (`pyproject.toml:16`). Brain R858 |
| C7 | Hook gating (U1) | Not used | Brain R858; a later live proof makes it an optimization row |
| C8 | Session lifetime | Resume by stored id; rotate daily; fresh session after a failed resume, loud | Bounded context; L18 |
| C9 | Old listener | `com.cobalt.cos` refuses to start while `com.cobalt.agent` is alive; the F20 deploy decommissions it | L3; his 09-08 rule: decommission when F20 lands |
| C10 | Request TTL | `hitl.request_ttl_min` = 1440 | One day covers his away time; expiry is loud |
| C11 | Built-in read tools (Read/Grep/Glob) | Not allowed; Cobalt read tools only | Jailing built-in reads is unproven (U1); Cobalt tools are typed and scoped |
