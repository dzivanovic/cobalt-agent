# VOICE v3 — SEAM S1: THE NEW CORE'S ONE MODEL-ACCESS MODULE (2026-09-23)

**What this is.** The seam document the voice v3 FINAL requires BEFORE V1's build prompt (`docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md` `## Seam` S1: "the seam document is a precondition before V1's build prompt"; L72 as amended 2026-09-22 P-b: a seam two lanes share is settled in ONE document both prompts cite before either launches). Drafted by the Opus 5.5 seat `voice-build-draft-0923` for the CTO desk (`prompts/2026-09-23/42-draft-voice-build.md`). Design approved: `cto-2026-09-23.md` R57 (FINAL `43a11a1`, sha256 prefix `8c469b9544282b55`), item 2 = B, item 3 = B + his clause (R56).

**What this is NOT.** It rewrites no routing law. L5, L21–L27, L29, L49 and the routing sentences of L24 / L27 are FROZEN until the routing tribunal rules (LAWS.md "How to read this file"; `ROUTING-v2-2026-09-22.md` is a proposal in that lane). This document CITES them. It decides only the shape of the module V1 creates and what later callers share, so that no second copy is ever built (L3).

## 1. The facts it rests on (file-checked 2026-09-23 on `main` `ffee37ad`)

| # | Fact | Where |
|---|---|---|
| S1-F1 | The new core makes no model call today; no LiteLLM caller under `src/cobalt/` | FINAL F2 `[F-20]`, `[F-21]` (`radar/audit_export.py` is prose, not a caller) |
| S1-F2 | `litellm == 1.81.8` is already a direct, pinned dependency; `openai>=1.0.0` too | `pyproject.toml:16-17` |
| S1-F3 | The local model is LM Studio's OpenAI-compatible server on `127.0.0.1:1234`, model alias `mainframe`; thinking always on and inlined; `/no_think` soft switch works | `heartbeat/probes.py:252-258` (`def mainframe`, port 1234); `configs/config.yaml:44-46` (old tree, READ-ONLY reference); CLAUDE.md "Environment facts"; FINAL F8 |
| S1-F4 | The old tree's caller (`src/cobalt_agent/llm.py`) builds `api_base` and passes it to LiteLLM; it is KILL/strangler code and never crosses (CLAUDE.md strangler rules, L15) | `src/cobalt_agent/llm.py:72-150` |
| S1-F5 | The JEV trial builds `src/cobalt/classify/` on the UNMERGED branch `jev/trial-0923` (tip `199fa082`): a metered OpenRouter `POST /api/v1/systemone` door with its own urllib transport, `read_secret("OPENROUTER_API_KEY")` at call time and an outbound secret guard `_guard_outbound`. It sets aside L5's one door for THAT TRIAL ONLY, by his per-case override | `prompts/2026-09-23/28-jev-trial-build.md` line 1 and WHY (R34 / R38 / R42 / R47 of `cto-2026-09-23.md`) |
| S1-F6 | The routing v2 derive words L5 as "every model call Cobalt's CODE makes … goes through ONE model-access module" — PROPOSED, not law | `ROUTING-v2-2026-09-22.md:32` |
| S1-F7 | L22 names the plane: FAST WIRE (LiteLLM / direct, single-shot) for pipeline inference; the voice Plan call is one single-shot call per turn | LAWS L22; FINAL `[F-01]` |

## 2. The ruling of this seam (what V1 creates)

**ONE package, `src/cobalt/modelaccess/`, created by voice V1 with the LOCAL lane only.** The name stands unless the routing tribunal rules another; a rename is then ONE move by the routing build, never a second module. No other new-core module calls a model endpoint, imports `litellm`, or opens an HTTP connection to a model server. A second caller of a model is a caller of this package.

### 2.1 Files

| File | Holds |
|---|---|
| `modelaccess/__init__.py` | the public surface only: `call`, `call_sync`, `ModelRequest`, `ModelMessage`, `ModelResult`, `ModelCallError`, `load_routes` |
| `modelaccess/models.py` | the Pydantic types of §2.2 |
| `modelaccess/config.py` | the route registry schema + loader for `configs/cobalt/modelaccess.yaml` (L10: a bad file crashes with its line; a missing key crashes, L1) |
| `modelaccess/guard.py` | `refuse_if_secret_shaped(text, *, where)` — the outbound guard, built on the existing `cobalt.redact.redact` + `cobalt.redact.secrets.load_literals`; a prompt whose redaction differs from itself is REFUSED, never sent redacted |
| `modelaccess/adapters.py` | ONE adapter per route `kind`; V1 ships `openai_compatible` only |
| `modelaccess/client.py` | `call()` / `call_sync()`: resolve the route → guard → adapter → validate → `ModelResult` |
| `configs/cobalt/modelaccess.yaml` | the routes (V1: exactly one, `local.plan`) |

### 2.2 Interface (the contract later callers share)

```
ModelMessage   {role: "system"|"user"|"assistant", content: str}
ModelRequest   {route: str,                 # a ROUTE NAME from the registry — never a provider, model or URL
                caller: str,                # e.g. "voice.plan" — recorded, used for per-caller counts
                request_id: str,            # the caller's id (voice: the turn id) — recorded
                messages: list[ModelMessage],
                response_schema: dict|None, # a JSON schema the caller validates against anyway (Pydantic)
                max_output_tokens: int|None,
                timeout_s: float|None}      # None = the route's default; a caller may only LOWER it
ModelResult    {route, caller, request_id,
                lane: "local",              # V1: always local
                kind: "openai_compatible",
                model_returned: str,        # AS RETURNED by the server, never the configured alias
                content: str,               # the reply text after the route's think policy (§2.4)
                think_block: "absent"|"empty_removed",
                finish_reason: str|None,
                usage: {input_tokens: int|None, output_tokens: int|None},
                latency_ms: int,            # request built → validated result (time.perf_counter)
                at: datetime (UTC)}
ModelCallError(kind, route, caller, request_id, detail)   # detail passes redact(); raised `from None`
  kind ∈ {route_unknown, prompt_refused, unreachable, timeout, http_status, bad_response, empty, think_leak, schema_refused}
async def call(req: ModelRequest) -> ModelResult          # the FastAPI path — never blocks the loop (FINAL [F-04])
def call_sync(req: ModelRequest) -> ModelResult           # CLI / jobs / tests — the same code path under the hood (L3)
```

A caller never sees a URL, a key, a provider name or a model file. It names a route. It gets a `ModelResult` or a `ModelCallError` — never `None`, never an empty string presented as an answer (L1: `empty` is an error kind).

### 2.3 The route registry (`configs/cobalt/modelaccess.yaml`, schema `extra="forbid"`)

```
routes:
  local.plan:
    lane: local                      # V1 accepts only "local" (validator)
    kind: openai_compatible          # V1 accepts only this kind (validator)
    api_base: http://127.0.0.1:1234/v1   # lane local ⇒ host must be loopback (validator refuses any other host)
    model: mainframe                 # the LM Studio alias (S1-F3)
    no_think: true                   # append the `/no_think` soft switch to the last user message
    think_policy: forbid_nonempty    # §2.4
    timeout_s: <from E4>             # engine tunable, set by the V1 builder from E4 with its source line
    max_output_tokens: <from E4>
    key_name: null                   # LM Studio needs none today; if it ever does, a VaultManager NAME, fetched at call time via cobalt.redact.secrets.read_secret — never a value
```

- There is NO `fallback` key. The schema refuses one (`extra="forbid"`). Whether any lane carries a fallback is the routing lane's (L23 / L25, frozen); the day it rules, the fallback is configured HERE, never in a caller (FINAL `[F-23]`).
- A second route for the same caller (E4's "second small local model beside it") is a second `lane: local` entry and a caller-config change of the ROUTE NAME, by measurement (L23, L26 frozen as cited). No caller code changes.
- The file lives under `configs/cobalt/` — outside the old loader's top-level `configs/*.yaml` glob (CLAUDE.md config boundary).

### 2.4 Behaviour every caller inherits

1. **Guard first.** Every message's content passes `refuse_if_secret_shaped` before any byte leaves the process; a hit → `ModelCallError(prompt_refused)` naming the KIND of hit, never the text, and ZERO network calls (L4, L41). The literal guard reporting itself inactive (locked vault) does NOT refuse a LOCAL route (the text never leaves the host); it is recorded on the result's log line. (A future non-local route refuses when the literal guard is inactive — the JEV rule, §3.)
2. **Think policy.** The local model inlines `<think>…</think>` (S1-F3). `forbid_nonempty`: an EMPTY think block (whitespace only) is removed and recorded as `think_block: empty_removed`; a NON-EMPTY think block → `ModelCallError(think_leak)` — the caller's turn FAILS, it never executes (FINAL E4, grok: "A think-wrapped reply must FAIL the turn, not execute"). E4 measures what `/no_think` actually emits; the policy is not relaxed without a new measurement and a design change.
3. **Schema.** When `response_schema` is given, the adapter passes it as the OpenAI-compatible `response_format` `json_schema` (strict) only if E4 shows the server honours it; otherwise the schema rides in the system message. Either way the CALLER validates the content with its own Pydantic model; the module never "repairs" content.
4. **Off the loop.** `call()` is truly async (the adapter's async client, or the sync path under `asyncio.to_thread`); no blocking call inside an `async def` route (FINAL `[F-04]`; E6 measures).
5. **No network at import.** The adapter imports `litellm` with its remote model-cost-map fetch disabled (`LITELLM_LOCAL_MODEL_COST_MAP=True` set before import) and its telemetry / callbacks off; a test blocks every non-loopback socket during import and during a call and proves nothing is attempted. If `litellm` cannot be made silent at import, the `openai_compatible` adapter uses the `openai` client already pinned (S1-F2) — the builder records which, with the test output; the INTERFACE above does not change.
6. **Loud, typed failure.** Connection refused → `unreachable`; deadline → `timeout`; non-2xx → `http_status` (status only; the body passes `redact()`); no choices / no content → `empty`; unparseable envelope → `bad_response`. Each is ONE `logger.error` line naming route, caller, request id and kind (L1, L9). The caller maps kinds to its own degraded state (voice: `voice_plan` RED "Cobalt can't think right now (<kind>)", FINAL §7).
7. **The call record (L57).** Every call — success or error — emits ONE structured log line: route, caller, request id, lane, kind, model_returned, latency_ms, usage, error kind. The module keeps no table in V1; the CALLER stores what it needs as its stored inputs (voice: the `voice_turns` row carries route, model_returned, latency_ms, usage and the Plan). A module-owned call ledger is a routing-lane item, not V1's.

## 3. What later callers share, and what they never share

| Later caller | Shares with V1's module | Never shares |
|---|---|---|
| **JEV's collector — the local-lane collector** (the "later build" of `28` NEXT STEP: a typed classifier on the local model) | IS a caller: a `local.*` route, `ModelRequest` / `ModelResult` / `ModelCallError`, the guard, the think policy, the call-record line. No second HTTP client for the local model. | JEV's question schema (`classify/models.py`), its trial runner and results files |
| **The typed-classifier lane on OpenRouter** (`classify/collector.py`, JEV trial, branch `jev/trial-0923`) | When the trial ends and the lane becomes an engine lane, its `systemone` door moves INTO this module as a second `kind` (`openrouter_systemone`), a `lane: metered` route with `key_name: OPENROUTER_API_KEY` fetched at call time, and its ledger / spend cap becomes the module's metered-route check. THAT move is the routing build's, after the routing tribunal rules (L5 / L22 / L27 frozen) — not V1's, not JEV's trial. | — |
| **The guard, one home (L3).** | `modelaccess/guard.py::refuse_if_secret_shaped` is THE outbound guard. `classify/collector.py::_guard_outbound` (unmerged) is a pre-S1 duplicate of the same check. **Seam rule:** whichever of `voice/v1-0923` and `jev/trial-0923` merges SECOND re-points: if JEV merges after V1, its merge (or its next build) replaces the body of `_guard_outbound` with a call to `refuse_if_secret_shaped` (one import, its tests unchanged); if JEV merges first, V1's builder moves the check into `modelaccess/guard.py` and re-points `classify/collector.py` to it — the ONE file outside V1's own paths V1 may touch, and only for that re-point. The stacked gate (L68) proves the seam; it does not decide it. | — |
| **Voice V2–V5** | the same `local.plan` route; nothing new in the module | — |
| **The routing build** (after the tribunal) | EXTENDS this package: fallback chains, metered kinds, the call ledger, the per-class counts of L25's seat-usage column. It never builds a second package. | — |

## 4. How V1 proves the seam (tests the V1 build prompt names)

- Route resolution: unknown route → `route_unknown`; a `lane: local` route with a non-loopback host → the config refuses to load; a `fallback` key → refuses to load.
- Guard: a message carrying a constructed secret-shaped string → `prompt_refused`, ZERO transport calls.
- Think policy over constructed server replies: no block → `absent`; `<think>\n\n</think>` → `empty_removed`; `<think>x</think>{…}` → `think_leak`.
- Every error kind over a fake transport; the log line carries no message content.
- No non-loopback socket at import or call (socket guard in the test).
- `call()` inside a running event loop never blocks it (a concurrent coroutine keeps ticking during a slow fake call).
- ONE live proof in dev (E4): the real `mainframe` returns a `ModelResult` whose `model_returned` is AS RETURNED.
- L3 grep at the V1 build's close: `grep -rln "litellm\|chat/completions\|api/v1/" src/cobalt` → `src/cobalt/modelaccess/` only (plus `classify/` while JEV is unmerged or not yet re-pointed — named, never silent).

## 5. What stays OPEN (not this seam's to decide)

- Any cloud fallback for the Plan call — the routing lane (L23 / L25, frozen).
- Whether `ROUTING-v2`'s L5 wording becomes law — the routing tribunal.
- A module-owned call ledger and quota counts (L25's reason-class column, still owed) — the routing build.
- The package name — stands unless the routing tribunal rules another (one move, then).
