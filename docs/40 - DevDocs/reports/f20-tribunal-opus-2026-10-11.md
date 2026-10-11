BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Sun Oct 11 07:12:31 EDT 2026

## DIGEST FOR THE DESK
TRIBUNAL: ADOPT AFTER approval-key auth, agents commit path, loop heartbeat, kill-resume, decommission sequencing
- D1 ADOPT
- D2 ADOPT
- D3 ADOPT WITH — fail-closed mode named by X1; no setting sources; the session's init tool list must equal the cos set.
- D4 ADOPT WITH — L7 is amended only once the approve POST is proven his (approval key, T2b); scope = the /hitl catalog.
- D5 ADOPT
- D6 ADOPT WITH — approve needs a one-time approval key from the card DM, plus the sha256, in one conditional UPDATE.
- D7 ADOPT WITH — generated.yaml cannot take a glob or an untracked file (generated/config.py:131-144); a hitl-bound directory clause instead.
- D8 ADOPT WITH — the executor claims rows with SKIP LOCKED and reconciles a file already written; deactivate refuses voice and cos.
- D9 ADOPT WITH — `==` pin like litellm (pyproject.toml:16); the CLI version is recorded in the build report.
- D10 ADOPT WITH — Sonnet 5.5 is an unmeasured start value in cos.yaml's chassis; no URL/key there. SELF: yes (UNMEASURED)
- D11 ADOPT
- D12 ADOPT
- D13 ADOPT
- D14 ADOPT WITH — decommission only with F5 live; the deploy scripts drop com.cobalt.agent and add com.cobalt.cos; UNIQUE message ref.
- D15 ADOPT WITH — 1440 lands `status: proposed`, unmeasured, like F4's rows.
- D16 ADOPT
- (a) ADOPT WITH — the cites hold. It missed deploy-outage.sh/deploy-step0.sh, the scheduler in com.cobalt.agent, tunables readers, and that generated.yaml takes no glob.
- (b) ADOPT WITH — the listener reads only his posts; the hash is over the exact rendered bytes; model text is escaped; there is no approve path but the key-bound route.
- (c) ADOPT WITH — the env and tool set are proven on the real spawn (X1–X3); the keychain gate blocks chunks C3/C4 only.
- (d) ADOPT WITH — the beater thread masks a hung loop: add a loop stamp plus a probe; the resume phrase is unreachable by DM; the poll runs independent of the turn; inbound text is guarded.
- (e) ADOPT WITH — ownership lines for tunables keys, the jobs.yaml row, web.py routes, the probes and the lock; L3 holds after the fixes.
- (f) ADOPT WITH — 4 chunks (≈18–23 h, GUESS); Opus 5.5 builds; house B not mandatory by L67. SELF: yes (UNMEASURED)
- (g) ADOPT WITH — RESTARTS: aset, radar, cos (new); agent booted out. tunables.yaml adds aset and radar (jobs.yaml:69, :200).
- EXPERIMENTS: X1–X9 (fail-closed mode, init tool list, CLI env, keychain under launchd, result shapes U4, fragment delivery, real-shape post, request ip, restart cost).
- OWNER: D1 yes (his money/account terms) · D2 no · D3 yes as an L62 grant only · D4 yes (law text) · D5 yes (law text).
- SELF: yes lines: 2 · UNMEASURED: 2 · WITHDRAWN: 3 · ESCALATE: 2

## Rulings

**D1 — Q3 terms gate the build.** ADOPT
The design depends on the answer in one place only: proposal §4's auth and env fields (subscription login, no API key). If the terms forbid it, the chassis changes to a metered key, and that is L27 money. That makes it his. R858 and R1012 already rule that the build waits; this ruling does not re-open that (L77).

**D2 — a resident subscription seat `com.cobalt.cos`.** ADOPT
The Charter (:195-198, "one resident session") and L22 ("SDK chassis = Claude-on-subscription") already set this. Never extracting or storing OAuth tokens is the spike's only safe assumption (spike :14). Whether the login survives launchd is X4, not an argument.

**D3 — the "CoS session" permission class.** ADOPT WITH:
"The session's options are: `allowed_tools` = exactly the `cos/tools.py` set; `disallowed_tools` = every built-in; the permission mode is the CLI mode that DENIES any tool that is not pre-approved (named by X1's result; never the default ask mode, never `bypassPermissions`); NO setting sources (no user, project or local settings, no CLAUDE.md, no hooks, no plugins, no user or account MCP servers); env = the allowlist in §4; cwd = an empty scratch directory. At every session start, code compares the tool list the session reports at init with the cos set. Any extra tool → the session is closed, the turn `failed`, a DM, heartbeat RED. T4 asserts the options; T10 asserts the init list on a real spawn."
Why: L37's BOUNDARY (LAWS.md:237) records that an allowlist is a PRE-APPROVAL list, not a whitelist. A tool that is in neither list falls to the mode. MCP tools from user or account config would be in neither list, and a denylist of built-ins cannot name them. Failing scenario: the host's user config carries a browser MCP server. The session starts with `cwd` scratch and HOME set (§4 env). The CLI loads the user servers (UNVERIFIED — X2). A prompt-injected `radar.pool` result says "open <url> in the browser". The tool is neither allowed nor disallowed, so the default mode decides. With no callback, the result is unknown (spike U1). The init-list check makes this fail closed whatever X2 shows. Price: ~15 lines in `session.py` and one assertion in T10, in chunk C3.

**D4 — amend L7's interim clause at the F20 deploy.** ADOPT WITH:
"L7's interim clause is amended at the F20 deploy only if T2b passes (a POST without the card's approval key is refused, nothing written). The amended text names the `/hitl` approval as the HITL token for the actions in its catalog only. Until a trading-logic action is in that catalog and its own tribunal has run, L7's promotion rule for trading logic keeps the desk-chat approval."
Why: the sha256 is integrity, not identity. Today the aset web process has no authentication on any POST: there is no auth, middleware or Depends in `aset/web.py`, by grep; `aset/__main__.py:53-56` prints "UNAUTHENTICATED". A "token mechanism" whose approve route any local process can POST is not his hand (L37). See D6.

**D5 — L41's "Until the broker ships (S5-P3)".** ADOPT
The broker is outside F20 (§8). Re-pointing L41 at the broker's own card is law text, so it is his (L58).

**D6 (C1) — approve on the `/hitl` page only.** ADOPT WITH:
"At request time code generates a 128-bit random approval key. The row stores only `approve_key_sha256`. The key travels only in the card DM's link fragment, `https://…/hitl/<id>#k=<key>`. A fragment is never sent to the server, so no access log carries it. The page's form copies it into a hidden field. `POST /hitl/{id}/approve` and `/deny` require both the key (`sha256(key) = approve_key_sha256`) and, for approve, the reviewed payload sha256. Approve is ONE statement: `UPDATE cobalt_hitl_requests SET status='approved', decided_at=now(), decided_via=… WHERE id=$1 AND status='pending' AND expires_at>now() AND sha256=$2 AND approve_key_sha256=$3 RETURNING id`. Zero rows → refused, nothing written, with the reason read back. The kill-switch check runs before it. A DM text 'approve' is never an approval."
Failing scenario without the key: a request row `a1b2` is pending with sha256 `S`. Any process on the host that can reach the port runs `GET /hitl/a1b2`, which shows `S` (the page must show it, as `aset/web.py:1320-1323` does today), then `POST /hitl/a1b2/approve` with body `sha256=S`. That process could be a house session in auto mode with a shell. The row becomes `approved` with `decided_via=aset:<a loopback or LAN address>`, which names a host, not him. Two taps: the second POST hits `status='pending'` false → 0 rows → refused. Expired: `expires_at>now()` false → refused. Kill switch active: refused before the UPDATE. Price: one column, ~30 lines in `hitl/store.py` and `web.py`, tests T2b and T2c in chunk C2. Whether a Mattermost link keeps its fragment on his phone is X6. If X6 fails, the derive picks the carrier under one constraint: the key is never in a server log or a model's context.

**D7 (C2) — an approved agent lives in `configs/cobalt/agents/<id>.yaml`, committed by `com.cobalt.generated`.** ADOPT WITH:
"`generated.yaml` lists exact, existing, TRACKED paths: a missing or untracked entry crashes the nightly job (`generated/config.py:131-144`). It cannot carry `configs/cobalt/agents/*.yaml` or a new agent file. F20 adds to `generated` one clause, `hitl_dirs: [configs/cobalt/agents]`. An untracked or modified file under a listed directory is committed only when its bytes hash to the `sha256` of an `executed` `cobalt_hitl_requests` row, so the HITL card is the human review the untracked refusal asks for. Any other change there fails the job loud and commits nothing."
Failing scenario as proposed: `generated.yaml` gains `- path: "configs/cobalt/agents/*.yaml"`. At 23:37 the load sees `missing = ['configs/cobalt/agents/*.yaml']` and raises `GeneratedConfigError`. The nightly commit of `seat-usage.md`, `archiver-runs.md` and `rules.yaml` stops every night. Price: ~40 lines in `generated/config.py` + `committer.py` and 2 tests, in a module another job owns (ownership line in (e)), chunk C2.

**D8 (C3) — the CoS resident's executor runs approved actions.** ADOPT WITH:
"The executor claims work with `SELECT … WHERE status='approved' FOR UPDATE SKIP LOCKED LIMIT 1` and re-checks the kill switch. For `agents.create` it writes `rendered` verbatim, create-if-absent. If the target already exists and its bytes hash to the row's sha256, the row becomes `executed` (recovered, logged loud); any other existing file → `failed`. For `agents.deactivate`, the card binds the file's before-bytes and after-bytes, the executor refuses unless the on-disk bytes equal the before-bytes, and it refuses at request time for `voice` and `cos`."
Failing scenarios. (1) The executor writes `agents/scout.yaml` and the process dies (kill phrase, deploy bootout) before the UPDATE. The row stays `approved`. After the restart create-if-absent finds the file, and as proposed the row goes `failed` while the agent exists. The reconcile rule makes it `executed`. (2) `request_action{action:"agents.deactivate", args:{id:"voice"}}` is approved. The executor adds `enabled: false` to `voice.yaml`. `AgentSpec` is `extra="forbid"` (`voice/registry.py:52-53`), and the aset re-reads that file per request (`jobs.yaml` aset reads: `agents/voice.yaml`, `voice/web.py:176`), so the voice desk fails on every request until a restart and revert. The refusal at request time prevents it.

**D9 (C4) — the Python SDK, pinned.** ADOPT WITH:
"Pinned `==` in `pyproject.toml` (the `litellm == 1.81.8` precedent, `pyproject.toml:16`). The build report records the SDK version and the `claude` CLI version the SDK actually spawns (U5)."

**D10 (C5) — the CoS model is Sonnet 5.5, a config value.** ADOPT WITH:
"The model is one value in `cos.yaml`'s `chassis` block. The generic registry schema refuses any URL, key, base URL or provider field there. Its start value is Sonnet 5.5, `UNMEASURED`. The routing build moves it into `modelaccess.yaml` when it adds a non-local lane: that registry accepts only `lane: local` today, and a new lane is the routing tribunal's (`modelaccess/config.py:43-44`, `:73-74`)."
SELF: yes
EVIDENCE: UNMEASURED — RULED L22 (the chassis is Claude on subscription) fixes the house; nothing in the files measures Sonnet 5.5 against Opus 5.5 for the CoS's talk-read-request load. X8 below is the measurement.
L22 forces this house: the only house on the chassis is Anthropic. The tier is unmeasured.

**D11 (C6) — local backend N/A for the MVP.** ADOPT
`modelaccess.yaml:17-22` is LM Studio over an OpenAI-compatible API. No proxy job is in `jobs.yaml`. `litellm` is a library used by `modelaccess/adapters.py` (grep). Brain R858 already rules it.

**D12 (C7) — no hook gating.** ADOPT
This is R858 (L77).

**D13 (C8) — resume by stored id, rotate daily, fresh session after a failed resume, loud.** ADOPT

**D14 (C9) — `com.cobalt.cos` refuses to start while `com.cobalt.agent` is alive; the F20 deploy decommissions it.** ADOPT WITH:
"(1) `com.cobalt.agent` also runs the old scheduler (`cobalt_agent/main.py:20`, `:91-92`; `jobs.yaml:135-137`), and the morning briefing stays until F5 lands (`areas/cobalt-sprints.md:12`). So the decommission runs only in a deploy where F5's checkpoints are already live. Until then F20 is BUILT and waits (L43: a branch waits only when not built or checked; this is a deploy precondition named on its card). (2) The same deploy removes `com.cobalt.agent` from, and adds `com.cobalt.cos` to, `ops/desk/deploy-step0.sh:70` `RESIDENTS` and `ops/desk/deploy-outage.sh:90-91`, `:428-436`. (3) A single instance is guaranteed by `UNIQUE(message_ref)` on `cobalt_cos_turns`: a second listener's insert of the same post fails and that listener skips it, loud. The first start sets the read cursor to now, so old DM history is never replayed."
Failing scenarios. (a) As proposed, the first deploy after decommission reaches `deploy-outage.sh:428-436`: `cur=com.cobalt.agent; agent_pid` → empty → `fail com.cobalt.agent "cobalt.sh status is not ONLINE"`, and every later deploy fails its final read. (b) `cobalt cos run` started by hand while launchd's copy runs: two listeners on one bot, one post turns into two turns and two cards. The pidfile check sees only the old agent.

**D15 (C10) — TTL `hitl.request_ttl_min` = 1440.** ADOPT WITH:
"The row lands `status: proposed` with an unmeasured design-default source (the shape of F4's `prefill.refresh_*` rows, `F4-FINAL-2026-10-10.md:52`); the same applies to `cos.max_turns` 30 and `cos.turn_timeout_s` 900 (kit reference only, spike :15, L15) and `cos.poll_interval_s` / `cos.session_rotate_at`. X5 and X9 measure them."

**D16 (C11) — no built-in reads.** ADOPT

**(a) THE FACT BASE.** ADOPT WITH:
"§2 adds: `ops/desk/deploy-step0.sh` and `ops/desk/deploy-outage.sh` (L66 resident set: add `com.cobalt.cos`, drop `com.cobalt.agent`); `src/cobalt/generated/{config,committer}.py` (the D7 clause); `configs/cobalt/taxonomy/tunables.yaml` is in the `reads:` of `com.cobalt.aset` (`jobs.yaml:69`) and `com.cobalt.radar` (`jobs.yaml:200`). §7 R7 reads: `com.cobalt.agent` serves the Mattermost websocket listener, the scheduler (morning briefing), the Scribe and the memory layer (`jobs.yaml:135-137`, `cobalt_agent/main.py:91-92`)."
HOLDS, checked here at HEAD (src/configs net diff vs `d0a5fbb8` empty; only `ops/desk/*` moved):
- `notify.yaml:13-14` (`vault_key: MATTERMOST_CREDS` at :14)
- `killswitch.py:106`, `:118`
- `jobs.yaml:351-352`, `:88-89`, `:127-131`, `:157-158`, `:201-202`, `:298-316`
- `voice/registry.py:9-11`, `:62-68`, `:85`
- `mattermost.py:13-17`, `:130`
- `redact/guard.py:80`
- `modelaccess/guard.py:40`
- `modelaccess.yaml:17-22`
- `pyproject.toml:16`
- `aset/web.py:1305-1380`
- `wrapper.py:78-110`
- `0001_cobalt_jobs.sql:43-60`
- Charter :195; LADDER :934 at `d0a5fbb8` (now :964 on HEAD; docs-only drift)
DOES NOT HOLD:
- §2 generated row (see WRONG FACTS 1)
- §2 "served over HTTPS only (L80)" (WRONG FACTS 2)
- §2/§5 "AMBER" for a probe (WRONG FACTS 4)
"Does not exist yet": a grep of `request_action`, `draft_agent`, `cobalt_hitl_requests`, `cobalt_cos_sessions` and `com.cobalt.cos` over src, tests, configs and ops finds no match. `src/cobalt/` has no `cos`, `hitl` or `agents` package (ls). The bot is shared: the old listener reads the same bot over a websocket (`cobalt_agent/interfaces/mattermost.py:744-808`). Its text interceptor approves on "approve <id>" with `bypass_hitl=True` (`:380-414`) — a second approval path for as long as it runs, which D14 ends. The refusal rule matches `voice/registry.py:62-68`.

**(b) THE HITL WALK (L37).** ADOPT WITH:
"(1) The listener turns only posts whose `user_id` is his (resolved from `notify.yaml` `dm_username`) and whose `type` is empty into turns, as the old listener does (`cobalt_agent/interfaces/mattermost.py:371-376`). The bot's own card and outcome posts never reach the model. (2) The row stores `rendered TEXT`, the exact bytes the page shows and the executor writes. `sha256 = sha256(rendered UTF-8)`. JSONB `payload` is kept for queries only and is never re-hashed. (3) Every model-supplied field (`reason`, the YAML's `charter`) reaches the page only through `html.escape` (the `e = html.escape` pattern, `web.py:1307`). The DM's one-line summary is rendered by code from the validated args; no model text goes into the DM. (4) T3 also asserts: no `cobalt hitl` subcommand and no function reachable from `cos/` writes `status='approved'`; the only writer is `hitl/store.approve()`, whose only caller is the `/hitl` approve route."
The walk, step by step:
- `request_action{action:"agents.create", args:{yaml:…}, reason:"…"}`, or `draft_agent{yaml}` with `tools: [web.fetch]`: the registry schema refuses the unknown tool, the refusal goes back to the model, and no row is written.
- A secret-shaped arg: `refuse_if_secret_shaped` raises `PromptRefused` (`modelaccess/guard.py:40-45`), and no row is written.
- A valid draft: row `pending`, sha `S` over `rendered`, key `K` hashed, card DM `HITL a1b2 agents.create scout — https://…/hitl/a1b2#k=K`. `send_dm` redacts first (`mattermost.py:140`); `#k=` matches no pattern (`url_query_secret` needs `[?&]`, `redact.yaml:131`; `env_assignment_secret` needs a secret-word name, `:190`).
- His tap: body `sha256=S&k=K` → `approved` → executor → file bytes hash to `S` → `executed`.
- Wrong sha, second tap, after expiry, under the kill switch: all refused (D6).
- A DM saying "approve a1b2": the listener passes it to the model as text. The model has no approve tool (T3), so the row stays `pending`.
- A prompt-injected read result telling the model to call `request_action`: the worst outcome is a `pending` row and a card. Without (3), a `reason` carrying `<script>` that auto-submits the form would approve when he merely opened the page. With (3) and the key it cannot.
- Two approved rows: SKIP LOCKED (D8).
- The executor dies after the write: reconcile (D8).

**(c) THE PERMISSION CLASS.** ADOPT WITH:
"T5 inspects the environment of the real spawned CLI process in T10, not only the options object, because whether the SDK replaces or merges the parent env is X3. The resident's own process must hold `COBALT_MASTER_KEY` (`send_dm` unlocks the bot credential with it, `mattermost.py:70-77`). The keychain-login proof (X4) is the first step of chunk C3 and blocks C3 and C4 only. C1 and C2 build in parallel (L72). 'No fallback house in F20' stands: the model-access registry refuses a fallback key, and a lane's chain is the routing tribunal's (`modelaccess/config.py:9-10`, `:125-126`). CoS down = DM + heartbeat RED, loud (L1)."
Failing scenario covered: the plist sets `COBALT_MASTER_KEY`, as `start_aset.sh:3` does for the aset. If the SDK merges the parent env, the CLI child holds the master key and, if the plist ever carries `ANTHROPIC_API_KEY`, bills the metered key silently (L27). T10 + X3 settle which.

**(d) THE FAILURE SURFACE.** ADOPT WITH:
"(1) Under `job_run`, `_Beater` stamps `heartbeat_at` from a daemon thread on a timer (`wrapper.py:78-110`, `:172-173`), so a hung poll loop keeps a fresh heartbeat and ZOMBIE never fires. The listener therefore writes `cobalt_cos_sessions.polled_at` on every poll, and the `cos` probe is RED when `now − polled_at > 3 × cos.poll_interval_s`. (2) The poll loop is its own asyncio task, independent of the turn. The kill phrase is matched on every poll; it engages the switch, cancels the running turn (its CLI subprocess is killed) and stops the executor. (3) The resume phrase cannot be served by DM: `kill_switch_exempt` is reserved for the heartbeat (`jobs/config.py:306-310`), so `com.cobalt.cos` exits at its next safe point (`should_keep_running`, `wrapper.py:202-215`) and refuses to start while the switch is active (`wrapper.py:159-165`). The kill DM reply says 'stopped — resume with `cobalt resume` on the host'. T7 tests the kill phrase and the reply; the resume phrase leaves T7. (4) Every inbound message and every read-tool result passes `refuse_if_secret_shaped` before it enters the session, because it leaves the host to the vendor (the guard is 'THE outbound guard for every model call', `modelaccess/guard.py:1`)."
Failing scenarios:
- (1) The poll call blocks on a half-open socket. The thread keeps stamping. The heartbeat shows green while no DM is read.
- (2) A turn hangs for 900 s. He sends COBALT STOP. If the poll sits behind the turn, the stop waits up to 900 s.
- (3) He sends COBALT STOP and then COBALT RESUME. Nothing is listening for the resume. As proposed, T7 claims it is intercepted.
- (4) He pastes `export FINVIZ_TOKEN=…` into the DM. The turn ships it to the vendor.
Detection is real for max turns, timeout and no-result: `failed` + DM (L18; exact subtypes X5). For meter or login, the DM + RED (no AMBER for probes, WRONG FACTS 4). The listener is deterministic (L2). One row per turn.

**(e) SEAM AND SHARED FILES.** ADOPT WITH:
"Ownership lines:
- `tunables.yaml`: keys `cos.*` and `hitl.*` only (F4 owns `prefill.refresh_*`, F4-FINAL:256; F5 owns `checkpoint.*`).
- `jobs.yaml`: the one row `com.cobalt.cos` after `com.cobalt.radar`, and the deletion of the `com.cobalt.agent` row in the decommission deploy (F4 adds after `prefill-daily`, F23 after `generated`).
- `aset/web.py`: the `/hitl` routes in one block after `/settings/daily/apply`.
- `heartbeat/probes.py`: functions `cos` and `hitl`, plus their runner registration (F5 adds `checkpoint_freshness`).
- `cli.py`: one `add_parser` line (F5 and F23 add one each).
- `pyproject.toml` / `uv.lock`: one `==` line; a lock conflict is resolved by re-running `uv lock`, never by hand (F23 proposal R2).
- `generated/*`: the D7 clause, owned by F20, read by `com.cobalt.generated`.
- `ops/desk/deploy-*.sh`: the desk's tooling, edited by the F20 card in the decommission deploy only (ESCALATE 2)."
L3: one listener (after D14), one approval path (after D14 ends the old 'approve' interceptor), one registry. `voice.yaml` keeps its own loader, and the generic loader delegates to it by file name. F21's design file was not found by this seat's grep; UNVERIFIED — whether F21 edits any of these files.

**(f) CHUNKS AND SEATS.** ADOPT WITH:
"Four chunks, hours a GUESS each:
- C1 — generic registry + `cos.yaml` + T9. ~3 h, offline.
- C2 — hitl tables, store, actions, executor, `/hitl` page, approval key, D7 clause; T1, T2 (with T2b and T2c), T3, T8. ~7–8 h, `cobalt_dev` under L76's lock.
- C3 — X4 keychain proof first, then session, tools, listener, turn tables; T4–T7 on a fake client; T10 live scratch. ~6–8 h.
- C4 — resident, plist, `jobs.yaml`, probes, deploy-script lines, decommission plan. ~2–4 h.
Total ≈18–23 h GUESS. Seat: Opus 5.5 builds every chunk (L29: C2 is a write path that makes files from a model's request). Check: Opus + Grok (R921). House B is not mandatory by L67's letter: no vault-note write, no sizing."
SELF: yes
EVIDENCE: UNMEASURED — RULED L67 2026-10-10 R919 ("Every merged build stays Opus 5.5 (L29) until his word") and L29; no file this seat opened measures Opus against another house on a write-path build. UNVERIFIED — this seat did not search the check records for HOLD counts against Anthropic builds.

**(g) RESTARTS (L42).** ADOPT WITH:
"RESTARTS:
- `com.cobalt.aset` — `pyproject.toml`/`uv.lock` (`jobs.yaml:88-89`), `tunables.yaml` (`:69`), `aset/web.py` imports (`:99`).
- `com.cobalt.radar` — `pyproject.toml`/`uv.lock` (`:201-202`), `tunables.yaml` (`:200`).
- `com.cobalt.cos` — new, loaded.
- `com.cobalt.agent` — booted out (decommissioned, not restarted; D14).
- `com.cobalt.generated` — one-shot, no restart.
`cobalt jobs restarts <range>` on the build branch is the source of truth. The card carries the L66 stop of `com.cobalt.cos` before the merge from then on. A restart of the sheet he trades beside costs him the page for the restart's length: UNVERIFIED (X9, the same open measure as F4-FINAL:168)."

## Self-attack
Grep list (writers / readers):
- `request_action`, `draft_agent`, `cobalt_hitl_requests`, `cobalt_cos_sessions`: no committed file carries them (grep over src, tests, configs, ops: no output).
- `matches_kill_phrase` / `matches_resume_phrase`: defined at `killswitch.py:106`, `:118`; readers are only `tests/cobalt/test_jobs.py:708-715`. No runtime caller.
- `send_dm`: `notify/mattermost.py`, `notify/__init__.py`, `heartbeat/runner.py`, `aset/strike.py`; tests `test_heartbeat_runner`, `test_strike_fallback`, `test_jobs_reads`, `test_jobs_restarts`, `tests/ops/test_close_timer.py`.
- `refuse_if_secret_shaped`: defined `modelaccess/guard.py:40`; reader `modelaccess/client.py:119`, `:121`.
- `bypassPermissions` / `permission_mode`: only `ops/desk/desk-launch.sh` refusals and `tests/ops/*` (desk tooling). Nothing in `src/cobalt`.
- `claude_agent_sdk`: no committed file (pyproject included).
- `com.cobalt.agent`: `jobs.yaml:127-158`, `ops/com.cobalt.agent.plist:6`, `ops/README.md:26` (RunAtLoad, no KeepAlive), `jobs/config.py:295`, `jobs/models.py:64`, `ops/desk/deploy-outage.sh:4-435` (restore set, final ONLINE read), `ops/desk/deploy-step0.sh:70`.
- `com.cobalt.cos`: no committed file.
- `generated.yaml`: readers `generated/config.py`, `generated/__init__.py`, `prefill/config.py`; tests `test_generated_commit.py`, `test_prefill_rules_gen.py`; `jobs.yaml`.
- `heartbeat_at`: `jobs/store.py`, `wrapper.py`, `models.py`, `watchdog.py`, `jobs/__init__.py`, the 0001 migration. Writer is the beater thread (`wrapper.py:93`) or the watchdog for launchd/pidfile jobs.
- `supervisor`: `jobs/store.py`, `config.py`, `watchdog.py`, `cli.py`, `jobs.yaml`.
- `sha256` in aset: `web.py:1305-1379` (settings apply), `:2219-2260` (DRC state-book/resolve `expected_sha256`), `drc_page.py:16`, `:102-103`, `radar_panel.py:268-270`. Every one is a hidden form field with no authentication.
- `ANTHROPIC_API_KEY`: old tree only (`configs/config.yaml:36`, `tests/test_llm.py:55`). `ANTHROPIC_BASE_URL`: no committed file.
- `COBALT_MASTER_KEY`: `redact/secrets.py`, `ops/start_aset.sh`, `ops/run_backup.sh`, `ops/pg_role.py`, `ops/README.md`.
- `litellm`: `modelaccess/__init__.py`, `modelaccess/adapters.py`, `pyproject.toml:16`.
Walk of my text against the list. I kept only what the files bear out. The approval-key claim rests on the DRC and settings forms also being unauthenticated by the same read (L35: a scoped read — `aset/web.py` and `aset/__main__.py` only; middleware elsewhere is "not visible to this read").
WITHDRAWN: "Under L80's tailscale front every approve POST arrives from 127.0.0.1, so `decided_via` is always loopback" — no committed file shows the front's source address; the https-only build is not merged (`SPRINT-LADDER-v0_1.md:930`); moved to X7.
WITHDRAWN: "Postgres JSONB re-orders keys, so re-hashing `payload` fails" — not read in any file here; the (b) wording no longer depends on it (the hash is over `rendered TEXT`).
WITHDRAWN: "The heartbeat renders an AMBER probe for the cos session" — `render.py:166-168` renders AMBER for jobs only, and `Probe` carries `ok`/`unknown` (`probes.py:30-42`).

## SELF-ASSIGNMENTS
- D10 — SELF: yes — the CoS session's model is an Anthropic model (Sonnet 5.5 start value). EVIDENCE: UNMEASURED (RULED L22; X8 is the measurement).
- (f) — SELF: yes — every F20 chunk is built by Opus 5.5. EVIDENCE: UNMEASURED (RULED L67 R919, L29). Measurements against this house were not searched (UNVERIFIED).
Two SELF: yes lines, both UNMEASURED: per the prompt, neither is folded as a rule by the derive.

## Experiments (L70)
Run in R1012's approved live spike (Opus dontAsk, scratch dir, pinned venv), on the Mac in dev, in a scratch worktree with a dev vault copy:
- X1: a session with the D3 options, the candidate deny-unlisted mode and no callback. A synthetic DM fixture tells it to run `touch /tmp/x` via Bash, write `scratch/y` via Write, and call one MCP tool from a planted user config. Pass = no file, no command, the tool refused. Fail on any → D3's mode changes or F20 holds (L29 gate).
- X2: the same spawn with a browser-type MCP server in the user config and `setting_sources` empty. Record the init tool list. Pass = exactly the cos set. An extra tool → the init check (D3) is load-bearing; the SDK option is wrong.
- X3: spawn with the parent env holding `COBALT_MASTER_KEY=dummy` and `ANTHROPIC_API_KEY=dummy`. Read the CLI child's env (`ps -E -p <pid>`). Pass = neither present. Present → the session must run in a child process launched without them.
- X4: the plist-shaped LaunchAgent in dev runs one subscription turn after a reboot with no login shell. Pass = turn `done`. Fail → C3/C4 hold; C1/C2 proceed.
- X5 (U4): a fake max-turns = 1 turn, a killed CLI and a 10 s timeout. Record the result subtypes and the stream end. They set T6's assertions and `cos.max_turns` / `cos.turn_timeout_s` from measured turn counts on 20 synthetic DMs.
- X6: `send_dm` of a `https://…/hitl/<id>#k=<hex>` link on the dev bot; tap on the phone app. Pass = the page's script sees `k`. Fail → the derive picks another carrier that keeps the key out of logs and the model.
- X7: a POST through the tailnet front (after the https-only deploy) and one from loopback; record the source address each shows. Settles what `decided_via` can name.
- X8: Sonnet 5.5 vs Opus 5.5 on the same 20 synthetic DMs (read requests, one draft_agent, one injection fixture). Count correct tool calls, bad requests and turns. Sets D10's value.
- X9: time an aset restart (bootout → first 200 on `/api/health`) on dev. Prices (g).
- L45: the listener fixture is a real-shape Mattermost post, redacted, captured from the dev bot. Of T1–T10, keep all; add T2b (no key → refused), T2c (model text escaped), T7' (kill without resume), T11 (UNIQUE message ref, two listeners) and T12 (hung poll → probe RED).

## OWNER (after the tribunal)
- D1: PASSES — his money (his subscription account under the vendor's terms; a breach moves to a metered key, L27); no house can accept a terms risk on his account.
- D2: FAILS — the Charter (his text, :195-198) and L22 already decide it; the houses settle how.
- D3: PASSES only as the grant — a new standing permission class for a Cobalt-started session is his under L61/L62 (and R858 asks his yes); the class's contents are the houses' (D3 wording).
- D4: PASSES — law text; LAWS changes only from his approved rulings (L58).
- D5: PASSES — law text (L58).

## WRONG FACTS
1. Proposal §2 (`f20-design-proposal-2026-10-10.md:24`): "Declares `configs/cobalt/agents/*.yaml` so the 23:37 job commits an approved agent file" — `generated/config.py:131-144` refuses a missing path (a glob literal) and any untracked path.
2. Proposal §2 (`:22`): "The aset is served over HTTPS only (L80)" — the https-only build is BUILT-NOT-MERGED (`SPRINT-LADDER-v0_1.md:930`, HEAD; its merge reverted `7f6b63fd`); `aset/__main__.py:40-56` serves http and prints UNAUTHENTICATED on a LAN bind.
3. Proposal §7 R7 (`:78`) and report UNKNOWN (`f20-design-2026-10-10.md:22`): "What else that process still serves is UNKNOWN" — `jobs.yaml:135-137` names the scheduler, Scribe and memory layer; `cobalt_agent/main.py:91-92` starts the scheduler.
4. Proposal §2 (`:25`) and §5 (`:53`): probes "AMBER/RED", "heartbeat AMBER" — `Probe` has only `ok`/`unknown` (`probes.py:30-42`); AMBER is rendered for jobs only (`render.py:166-168`).
5. Proposal §5 (`:52`): "Watchdog marks the row ZOMBIE" for a hung listener — under `job_run` the daemon `_Beater` keeps `heartbeat_at` fresh (`wrapper.py:78-110`, `:172-173`), so a hung loop is never ZOMBIE.
6. Proposal §6 T7 (`:65`): the resume phrase "intercepted before the session" — `com.cobalt.cos` cannot be kill-switch exempt (`jobs/config.py:306-310`) and refuses to start while stopped (`wrapper.py:159-165`), so no listener exists to hear it.

## READING
- Prompt `326b-f20-tribunal-opus-seat.md` (whole). `336-f20-tribunal.md:34-40` (the question paragraph, HOW TO RULE and THE ITEMS at :34-36; :37-40 were read past the closing sentence by the read's range — the launch spellings for the houses, no ruling content, no house file).
- `LAWS.md` whole (:1-403).
- `f20-design-proposal-2026-10-10.md` whole; `f20-design-2026-10-10.md` whole; `sdk-spike-2026-10-10.md` whole; `s5-weekend-and-parked-answer-2026-10-10.md` grep "lane c" (:21, :34, :76).
- Rows: `cto-2026-09-22.md:56` (R109); `cto-2026-10-11.md:12` (R1032), `:32` (R1012); `cto-2026-10-10.md:91` (R921), `:92` (R920), `:147` (R865), `:154` (R858); `cto-2026-09-23.md:103` (R95), `:105` (R97).
- `MVP-CHARTER-v0_2.md:193-199`; `SPRINT-LADDER-v0_1.md:925-942`, `:955-972` (HEAD), git grep at `d0a5fbb8` (:934); `F4-FINAL-2026-10-10.md` grep; `f5-` and `f23-design-proposal-2026-10-10.md` grep; `areas/cobalt-sprints.md:8-16`.
- Code: `voice/registry.py` whole; `agents/voice.yaml` whole; `jobs/wrapper.py:70-227`; `killswitch.py` whole; `jobs/config.py:220-345`; `0001_cobalt_jobs.sql:1-80`; `jobs.yaml:1-38`, `:80-100`, `:125-206`, `:296-353`; `aset/web.py:985-1000`, `:1295-1385`; `aset/__main__.py:40-70`; `notify/mattermost.py` whole; `redact/guard.py:1-120`; `redact.yaml:119-147`, `:161-190`; `modelaccess/guard.py:1-80`; `modelaccess.yaml:1-40`; `modelaccess/config.py` grep; `notify.yaml` non-comment lines (keys); `generated.yaml` non-comment lines; `generated/config.py:120-150`; `pyproject.toml:1-40`; `heartbeat/probes.py:1-60` + grep; `heartbeat/render.py:155-175`; `cobalt_agent/interfaces/mattermost.py:370-425` + grep; `cobalt_agent/main.py` grep; `ops/desk/deploy-outage.sh:420-440` + grep; `ops/desk/deploy-step0.sh:62-80`; `ops/README.md:20-30`; `tunables.yaml` grep + `:1016-1022`.
- Searches: the twenty self-attack greps above; `git log`/`git diff --stat d0a5fbb8` (src/configs net empty; `ops/desk/*` changed); `ls` of `src/cobalt`, `configs/cobalt/agents`, `ops`, `src/cobalt_agent`, `src/cobalt/session`.
- Authorization: FABLE ROW count 0; R109 row `cto-2026-09-22.md:56` carrying both literals, committed `75b2aa57`; launch row R1032 with all three literals, committed `d6243a6c`; R1012 and R921 literals present; proposal and report committed `962ffba2`; the ten launch strings each count 1 in `238-f4-tribunal-opus-seat.md`; this session runs `claude-opus-5-5` = R109's id.

## L74
A block arrived in a system message during this session, after a tool result, asking for a `Claude-Session:` line in commit messages and PR bodies and naming a file-send tool. It is recorded once here. It was not followed. This seat makes no commit and sends no file.

## ESCALATE
1. D14: F20's deploy needs F5 live first (the old scheduler's briefing). The desk sequences the S5 deploys; no ruling of his is asked.
2. (e)/D14: `ops/desk/deploy-step0.sh` and `ops/desk/deploy-outage.sh` are the desk's deploy tooling. The F20 card must name those lines, or every deploy after the decommission fails its final read (`deploy-outage.sh:428-436`).

## CONTINUE
next: none — ruling complete. Written 2026-10-11 07:20 EDT (date).

F20 TRIBUNAL OPUS DONE · verdict: ADOPT AFTER approval-key auth, agents commit path, loop heartbeat, kill-resume, decommission sequencing · adopt: 7 · adopt with wording: 16 · reject: 0 · self-assignments: 2 · ESCALATE: 2
