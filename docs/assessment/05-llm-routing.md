# Cobalt Assessment — Pass 5: LLM routing, Cortex, and prompts

Date: 2026-08-21 · Baseline: `617771e` (main) · Assessor: Claude Fable 5 · Mode: read-only (code read; mocked tests run; **no LLM calls**; no DB writes)

Scope: `llm.py` (333), `brain/cortex.py` (250), `core/orchestrator.py` (156), `brain/base.py` (109), `brain/{engineering,ops}.py`, `persona.py` (142), `prompt.py` (155), `configs/prompts.yaml` (226), `configs/config.yaml` (models/active_profile/network/keys/persona/departments), every LLM/embedding call site in `src/` and `dev_utils/`, `tests/test_llm.py`, `test_cortex.py`, `test_orchestrator.py`.

Verdict legend: **RETAIN** · **BROKEN-FRICTION** · **KILL-candidate** (proposal — Dejan decides). **UNVERIFIED** = inferred, not read/run. ORIGINAL INTENT (§7) from tracked sources only (commit log; PRD/Manifest/ADR text in `dev_utils/`; docstrings; `COBALT-REQUIREMENTS.md`); vault ADRs not read; `cobalt_master_context.txt` absent.

---

## 0. Headline findings

| # | Finding | Evidence |
|---|---|---|
| **H-1** | **The routing layer (`LLM` class) is sound in design and is what almost everything uses** — role → `active_profile` alias → `models` registry → `provider/model_name` string → LiteLLM `completion()`, with `api_base` derived from `network.nodes[node_ref]` for local models and API keys pulled from vault-populated `config.keys` (`llm.py:46-82, 90-128`). 9 of 11 production call sites go through it (§1). Five roles map to `mainframe` (LM Studio), one (`researcher`) to `cloud_gemini_3_1_pro_preview` (`config.yaml:73-80`). | file:line |
| **H-2** | **Out-of-band census (LiteLLM-migration inventory)** — calls that bypass `LLM`/`active_profile`: (1) `memory/postgres.py:242-245` and `:761-765` `embedding(model="text-embedding-3-small")` (OpenAI, 2 sites); (2) `tools/extractor.py:182-190` `completion(model=config.llm.model_name)` → default **`gemini/gemini-1.5-pro`** (`config.py:76`; no `llm:` block in YAML; no `api_key` passed → needs `GEMINI_API_KEY` in env); (3) `dev_utils/check_gemini_models.py` `google.generativeai` direct (file is not valid Python). **Routed but provider-locked**: (4) scheduler briefing passes `tools=[{"googleSearch": {}}]` (`scheduler.py:74-78,156-162`) — only Gemini honours it, so the `researcher` role cannot be re-pointed to a non-Gemini model without breaking grounding; (5) `briefing.py:31-33` `LLM(model_name=…)` — kwarg silently ignored (fields are `role/api_key`; pydantic default `extra=ignore`) → always `default` role; its `"gpt-4o"` fallback string is dead. **Dead/phantom**: (6) `cli.py:188` calls `self.llm.think(...)` — `LLM` has no `think` (`AttributeError`; CLI path already unreachable from `__main__`). No other direct provider SDK usage exists. | grep (§1 table) |
| **H-3** | **What routing actually executes in production**: `Cortex.route` → "hi" fast-exit (`cortex.py:56`) → orchestrator keyword check against an **empty list** (Pass 4 H-4: `rules.cortex_routing` never reaches config) → hardcoded `web_keywords` (`"http://", "https://", "browser", "scrape", "search", "summarize the top"`, `:70`) → `None` = DEFAULT → **one LLM classification call** (`_classify_domain`, `ask_structured(DomainDecision)`, `fast_chat`=mainframe, `temperature 0.7` default → non-deterministic routing) → high-risk check against an **empty list** → department dispatch. So the "deterministic Triage Desk" (`87e16c7`) is reduced to six hardcoded substrings (and `"search"` collides with the `search` tool), the SECURITY INTERCEPT never fires, and every non-web message costs a classification round-trip. DEFAULT/FOUNDATION return `None` → Mattermost runs its **own** 3-iteration ReAct loop (`mattermost.py:578-708`) with `brain.llm` (fast_chat) and `PromptEngine.build_system_prompt()` **without tools** (`:585`, so the tool list is empty in the prompt). | file:line |
| **H-4** | **Hybrid/local support: present, minimal, and missing the requirement-level controls.** Local = `models.mainframe {provider: openai, model_name: mainframe, node_ref: cortex}` → `api_base http://localhost:1234/v1`, `api_key "dummy-local-key"` (`llm.py:126-128`); `ops/start_mainframe.sh` still loads the 122B MoE (Pass 0). **Absent**: per-call `reasoning_effort` (Requirements §10; no such kwarg anywhere), think-tag stripping in `llm.py` (only `semantic_tagger.py:285-286` strips `</think>` — `ask_structured` will fail JSON parsing on a thinking model unless LM Studio strips), cloud-down fallback to local with a red flag (§10; `_call_provider` just re-raises, `:160-163`), retries/backoff (only `OrchestratorEngine` retries 3×, `:61-75`), the 3-tries escalation rule (#13), timeouts, `drop_params`, model-specific `max_tokens` (4000 default everywhere; tagger 24 000). `context: 65536` in the registry is never read. `keys.lmstudio → LM_STUDIO_API_KEY` is resolved but never needed. | file:line |
| **H-5** | **Prompt inventory: 8 YAML prompts, 4 live, 1 of those unreachable; ≥14 hardcoded prompts in `.py`.** Live from `prompts.yaml`: `scheduler.morning_briefing` (`scheduler.py:65-68`), `routing.classify_domain` (`cortex.py:175-180`), `research.semantic_tagger` (`semantic_tagger.py:151`), `proposal.security_intercept` (`cortex.py:120`, unreachable — H-3). **Dead in YAML**: `system.core_identity` (only consumer `Persona.get_system_prompt` has **zero callers**; and it would `AttributeError` on `prompts.system.core_identity` since `prompts.system` is a dict, `persona.py:57-59`), `ops.system` and `engineering.system` (departments carry **verbatim hardcoded copies** as `default_prompt`, `ops.py:17-40`, `engineering.py:17-41` — the YAML is never read), `orchestrator.plan_execution` (orchestrator hardcodes its own architect prompt, `orchestrator.py:39-58`). Hardcoded in Python: `PromptEngine` header/context/memory-protocol/directives/ACTION protocol/tool list (`prompt.py:44-155`), `Persona` fallback (`persona.py:70-111`), orchestrator architect + per-step execution context (`orchestrator.py:39-58,103-124`), `BriefingAgent` system prompt (`scheduler.py:141`), `UniversalExtractor` prompt (`extractor.py:116-165`), `LLM.ask_structured` JSON instruction (`llm.py:285-290`), `MorningBriefing` synthesis (`briefing.py:78-84`), `DeepResearch` plan/synthesis (`deep_dive.py:48,83-88`), Mattermost approval summary (`mattermost.py:438`), `Cortex` classify fallback (`cortex.py:179`), tagger fallback (`semantic_tagger.py:160-178`), department prompts (above). `.clinerules` rule 3 ("prompts as config") is violated by most of them. Also: persona directives are injected **twice** into the same system prompt (`prompt.py:54,63-64` and `:120-121`). | file:line |
| **H-6** | **Token/cost accounting: none.** `response.usage` is never read (`llm.py:153-158`), no LiteLLM callbacks/`completion_cost`/`token_counter`, no budget, no per-role or per-day logging; the only per-call log is `logger.debug("Executing: model | base")` (`:150`) and a stale hardcoded INFO line "Persona Roles: Chief of Staff, Software Architect, Senior Developer, Business Analyst" on every `generate_response` (`:214-215`). Cloud spend (Gemini researcher, OpenAI embeddings on every `add_log`) is invisible. | grep |
| **H-7** | **Tests**: `test_llm.py` **9 failed**, `test_cortex.py` 16 errors (Pass 3) — both patch a non-existent `cobalt_agent.config.load_config` (tests predate `get_config`, `bdd1b5a` "LLM test mocks"); `test_orchestrator.py` 7 pass (mocks LLM). **No passing test covers the routing layer today.** | run output |
| **H-8** | **Three ACTION grammars + three ReAct loops** (Pass 2/3): `PromptEngine` teaches `key="value"` (`prompt.py:126-139`); `BaseDepartment` (`base.py:51-97`) and `BriefingAgent` (`scheduler.py:165-227`) parse `tool {json}`; Mattermost parses `key="value"` with its own loop. `BriefingAgent` appends observations as `role: system` (`scheduler.py:170,194,219,223,227`), `BaseDepartment` as `role: user` — multiple system messages mid-conversation is rejected/merged differently per provider (UNVERIFIED for Gemini via LiteLLM). `BaseDepartment` also rebuilds a `ToolManager()` (7 `PostgresMemory`) per department instance (Pass 2 H-9). | file:line |

---

## 1. Complete LLM/embedding call census

| # | Call site | Path | Model actually used (prod config) | Via `LLM`? | Notes |
|---|---|---|---|---|---|
| 1 | `main.py:44,146,163` | `LLM(role="default").generate_response` | mainframe | yes | `process_input`/`send_message` (CLI-era; Mattermost uses Cortex). |
| 2 | `brain/cortex.py:32,126,183` | `LLM(role="fast_chat")` `.ask` (intercept, unreachable) / `.ask_structured(DomainDecision)` | mainframe | yes | Classification at T=0.7. |
| 3 | `core/orchestrator.py:33,66` | `LLM(role="architect").ask_structured(OrchestrationState)` ×≤3 | mainframe | yes | Unreachable in prod (keyword list empty) except via tests. |
| 4 | `brain/base.py:24,44` (Engineering `coder`, Ops `default`, BriefingAgent override) | `generate_response` loop ≤4 | mainframe | yes | |
| 5 | `services/scheduler.py:77,124,156` | `BriefingAgent(role="researcher")` + `tools=[googleSearch]` | **gemini/gemini-3.1-pro-preview** | yes (provider-locked) | Only cloud role in use; daily 08:00. |
| 6 | `skills/research/deep_dive.py:34,51,91` | `LLM(role="default").ask_structured` ×2 | mainframe | yes | Cortex INTEL. |
| 7 | `skills/productivity/briefing.py:33,88` | `LLM(model_name=…)` → default; `.ask_structured` | mainframe | yes (kwarg ignored) | Cortex INTEL "briefing". |
| 8 | `skills/research/semantic_tagger.py:247-248` | `LLM(role='strategist').ask(T=0.0, max_tokens=24000)` | mainframe | yes | Manual runs only. |
| 9 | `interfaces/mattermost.py:439,602` | `brain.llm.generate_response` (Cortex's fast_chat) | mainframe | yes | Approval summary; DEFAULT ReAct loop. |
| 10 | `interfaces/cli.py:188` | `self.llm.think(...)` | — | **no such method** | Dead path. |
| 11 | `memory/postgres.py:242,761` | `litellm.embedding("text-embedding-3-small")` | **OpenAI** | **no** | Every `add_log`/`search`; FastPath. |
| 12 | `tools/extractor.py:182` | `litellm.completion(config.llm.model_name)` | **gemini/gemini-1.5-pro** (default) | **no** | Watcher/extract path (dead in prod). |
| 13 | `dev_utils/check_gemini_models.py` | `google.generativeai` | Gemini | **no** | Broken file. |
| 14 | `dev_utils/test_routing.py`, `live_run_orchestrator.py:94` | `LLM(role=coder/researcher)` | mainframe / Gemini | yes | Manual smoke. |

**Migration inventory (to bring under the routing layer)**: #11 (add an `embedding` role/alias to `active_profile` + registry, route through LiteLLM with the same key resolution; consider a local embedder — dimension change ⇒ migration, Pass 1 H-7), #12 (use `LLM(role=…)`), #5 (make grounding a role capability, not a hardcoded tool), #7 (fix the ctor call), #10 (delete/replace), #13 (delete). Also `LLMConfig.model_name` default should not silently exist.

---

## 2. Routing logic — intended vs executed

| Stage | Intended (docs/commits) | Executed today |
|---|---|---|
| Deterministic triage (`87e16c7`) | keyword lists from `rules.yaml cortex_routing` route ORCHESTRATOR / flag high-risk | lists empty → skipped; only `web_keywords` hardcoded in code fire |
| Classification | config-driven departments (`config.yaml departments`) + `routing.classify_domain` prompt (`eef5bdf` "Intent-Based Routing") | works as designed; LLM call per message at T=0.7; `DomainDecision` via schema-in-prompt (no provider JSON mode) |
| Security intercept (`5becd1e`) | `high_risk_keywords` → proposal card | never (empty list) |
| Department dispatch | TACTICAL/INTEL/OPS/ENGINEERING/GROWTH/DEFAULT | works; TACTICAL scan broken (Pass 4), GROWTH stub, OPS is keyword code (no LLM) |
| Split-brain orchestrator (`8c6c5d8`) | Architect plan → drones | unreachable (keyword list empty) |
| DEFAULT chat | "main chat loop" | Mattermost-local ReAct loop, tool list empty in prompt, `key=value` grammar |
| Model selection (`4f44d94`, `91edb24`) | `active_profile` switchboard | works; 5 roles → mainframe, 1 → Gemini |

---

## 3. Hybrid / local-model support — state

Exists: registry + node topology (`config.yaml:8-45`), `api_base` derivation, dummy key, `env_key_ref` → vault/env key lookup (`llm.py:90-124`, convoluted: `keys[ref]` yields the env-var *name*, then `keys[name]` the value — relies on vault secrets being named exactly `GEMINI_API_KEY` etc.; `keys` in YAML maps alias → env var name, `config.yaml:30-35`), `switch_role()` hot-swap, `dev_utils/test_routing.py` smoke (imports `src.…`).
Missing (Requirements §10/§11#13/#14): per-call `reasoning_effort`/thinking off for triage; think-tag hygiene in the generic path; cloud-outage fallback + UI flag; retries/timeouts/3-tries escalation; per-role `max_tokens`/`temperature` defaults in config; any registry validation (`models: dict[str, Any]`, `active_profile: dict[str,str]` unvalidated; a typo in an alias → `ValueError` at `LLM()` construction, `llm.py:53-54`, which would crash `main.py:44` at boot); `context` field unused; embedding role.

---

## 4. Prompt inventory — location, rigidity

| Prompt | Lives in | Consumer | Status |
|---|---|---|---|
| `system.core_identity` | YAML | `Persona.get_system_prompt` (no callers) | DEAD |
| `scheduler.morning_briefing` | YAML | `CobaltScheduler` | live; contains the only in-play hard rules (Pass 4) |
| `ops.system`, `engineering.system` | YAML **and** `.py` copies | `.py` copies only | YAML DEAD; drift risk |
| `proposal.security_intercept` | YAML | `Cortex._generate_proposal` | live but unreachable |
| `routing.classify_domain` | YAML | `Cortex._classify_domain` | live |
| `orchestrator.plan_execution` | YAML | none (orchestrator hardcodes) | DEAD |
| `research.semantic_tagger` | YAML (+ `.py` fallback) | tagger | live |
| PromptEngine identity/context/memory/directives/protocol/tools | `.py` | Mattermost DEFAULT loop, CLI | hardcoded; directives duplicated; claims "User: Administrator", "Operating System: Python Environment (CLI)"; tool list rendered from class names (Pass 2 H-7) |
| Architect + execution-context | `.py` | orchestrator | hardcoded; embeds `data/`, `docs/` map |
| BriefingAgent system | `.py` | scheduler | hardcoded |
| UniversalExtractor | `.py` | extractor | hardcoded |
| `ask_structured` JSON instruction | `.py` | all structured calls | hardcoded; schema dumped into system prompt (fine) |
| MorningBriefing / DeepResearch / Mattermost summary / fallbacks | `.py` | respective | hardcoded |
| `config.yaml persona.*` (roles/skills/tone/directives) | YAML | `PromptEngine` | live; `TACTICAL OVERWATCH` directive = the only place A/A-/B/B-/C grading is mentioned |

Rigidity: `PromptsConfig` is eight `Optional[dict]` buckets (`config.py:210-219`) — adding a prompt is a YAML edit, but the consumers that would read it are hardcoded; `Persona.create_override` (split-brain personas, `eef5bdf`) has no callers.

---

## 5. Token / cost accounting — none (H-6). Cloud exposure today: Gemini (daily briefing; `DeepResearch`/`Cortex` only if profile changes), OpenAI embeddings (every memory write/search, ingest runs). No ledger, no budget, no alerting.

## 6. RETAIN / BROKEN-FRICTION / KILL-candidate summary
**RETAIN**: `LLM` class as the single routing seam (role→alias→registry→LiteLLM, `api_base` from network nodes, vault-backed keys, `switch_role`); `ask_structured` (Pydantic-validated outputs); `config.yaml` registry/switchboard/persona/departments; `routing.classify_domain` + `research.semantic_tagger` + `scheduler.morning_briefing` as config-resident prompts; `OrchestratorEngine` retry pattern (the only 3-tries implementation).
**BROKEN-FRICTION**: `cortex_routing` dropped → triage/intercept dead (H-3); classification at T=0.7; out-of-band embeddings/extractor (H-2); provider-locked grounding; `briefing.py` ctor; dead YAML prompts + hardcoded copies (H-5); duplicated directives; no reasoning_effort/think-tag/fallback/retry/timeouts/budget (H-4, H-6); stale log line; three ACTION grammars & loops (H-8); `LLM()` boot crash on alias typo; tests (H-7); `PromptEngine` tool listing; `BaseDepartment` rebuilds `ToolManager` per instance.
**KILL-candidates**: `Persona.get_system_prompt`/`create_override` + `system.core_identity`; YAML `ops.system`/`engineering.system`/`orchestrator.plan_execution` **or** the `.py` copies (one must go); `cli.py` `think` path; `LLMConfig.model_name` default; `dev_utils/check_gemini_models.py`; Mattermost's private ReAct loop (fold into `BaseDepartment`); `generate_response_skill`/`search_context` legacy params; `briefing.py` (Pass 4 duplicate).

---

## 7. Component map — ORIGINAL INTENT

| Component | File | Verdict | ORIGINAL INTENT (documentation trail) |
|---|---|---|---|
| `LLM` routing class | `llm.py` | RETAIN | `91edb24` (02-13) "Hybrid Cloud/Local LLM support"; `eef5bdf` (02-18) "Intent-Based Routing, Qwen3-80B integration"; `4f44d94` (03-06) "LiteLLM /v1 proxy routing and Jinja template safety nets"; `bdd1b5a` "LLM test mocks"; Requirements §4/§10 (hot-swappable LiteLLM, local-first, cloud for hard analysis); ADR-002 "Hybrid AI Compute" (DeepSeek local / o3-mini / Gemini 1.5 Pro architect — superseded model names); System Manifest §4 "Models: DeepSeek-R1, o3-mini, Gemini 1.5 Pro" (`generate_constitution.py:169-170`). |
| `config.yaml models/active_profile/network/keys` | | RETAIN | `4f44d94` ("UNIVERSAL MODEL REGISTRY (2026 Edition)", "ACTIVE SWITCHBOARD" headers); `cc14caa` "Zero-Trust config routing" (keys via vault). |
| `Cortex` classification + departments | `cortex.py` | BROKEN-FRICTION | `eef5bdf` "Intent-Based Routing… Dynamic Persona Injection"; `87e16c7` (02-25) "Deterministic Fast-Path (Triage Desk) in Cortex to prevent identity bias"; System Manifest §2 CoS "Orchestration: Directing the 5 Departments"; `config.yaml:111-131` "COBALT ORGANIZATIONAL CHART". |
| `rules.yaml cortex_routing` | | BROKEN (dropped) | `87e16c7`; `cc14caa` ("use config-defined keywords" comments). |
| `OrchestratorEngine` | `orchestrator.py` | RETAIN (unreachable) | `8c6c5d8` (02-26) "Phase 4 Split-Brain Orchestrator"; docstring "Manager's Clipboard… Architect (Planner) and specialized Drones (Executors)… Self-healing retry loop to overcome local LLM JSON hallucinations". |
| `BaseDepartment` + `EngineeringDepartment`/`OpsDepartment` | `base.py`, `engineering.py`, `ops.py` | RETAIN loop / BROKEN prompts | `05b0617` (02-26) "Phase 6 Drone Polymorphism and Unified ReAct Engine"; `87e16c7` "secure The Forge… explicit Tool Manual"; `a55a96a` (02-08) ReAct pattern; System Manifest departments Scribe/Strategos. |
| `PromptEngine` | `prompt.py` | BROKEN-FRICTION | Docstring "Includes Memory Protocol & Temporal Gating… Prevents the 'Bag Holder' scenario"; `53611fe`/`0bf87fd` era strict-data rules ("RSI (20)"). Commit for memory protocol: UNVERIFIED. |
| `Persona` / `persona.*` config | `persona.py`, `config.yaml:86-109` | KILL-candidate (class) / RETAIN (config) | `eef5bdf` "Dynamic Persona Injection"; `create_override` docstring "temporary overrides for Split-Brain agents" (`8c6c5d8`). |
| `configs/prompts.yaml` | | RETAIN (reconcile) | File header "Centralized storage for all LLM prompts"; `.clinerules` rule 3 "PROMPTS AS CONFIG"; `cc14caa` (prompts nested under `prompts` section, `config.py:546-548`). Why `.py` copies remained: UNVERIFIED. |
| `BriefingAgent` + `scheduler.morning_briefing` | `scheduler.py` | BROKEN-FRICTION | `0bf87fd` morning briefing; `scheduler.py:54-58` docstring "Runs the Gemini 3.1 Pro query… googleSearch grounding"; Requirements §5 premarket agent. |
| `DeepResearch` | `deep_dive.py` | RETAIN (minor) | Docstring "Plan → Search → Analyze → Report"; System Manifest Scout "Web Browsing & Due Diligence"; Requirements §8 research engine precursor. |
| Embedding calls | `postgres.py` | BROKEN-FRICTION (out-of-band) | `8463874` RAG memory (Pass 1 intent); no ADR for cloud embedder. |
| `UniversalExtractor` LLM call | `extractor.py` | BROKEN-FRICTION (out-of-band) | `333c2c3` watcher daemon (Pass 2). |
| `dev_utils/test_routing.py` | | RETAIN (manual) | Docstring "LLM SWITCHBOARD ROUTING TEST"; `4f44d94`. |
| `dev_utils/check_gemini_models.py` | | KILL-candidate | UNVERIFIED (no doc; broken). |

## 8. Hardcoded values
`llm.py:127` `"dummy-local-key"`; `:109` `f"{ref.upper()}_API_KEY"`; `:136-137` T=0.7 / max_tokens 4000; `:214-215` stale roles log; `cortex.py:56` "hi" fast-exit; `:70` `web_keywords`; `:158` fallback departments; `:179` fallback classify prompt; `orchestrator.py:61` 3 retries; `:110-115` system map; `base.py:41` 4 loops; `scheduler.py:74` `googleSearch`; `semantic_tagger.py:251` 24 000 tokens; `config.py:76` `gemini/gemini-1.5-pro`; `prompt.py:84-85` "Python Environment (CLI)", "User: Administrator"; `briefing.py:31` `"gpt-4o"`; `config.yaml:44` `context: 65536` (unused); `ops/start_mainframe.sh` 122B model id + 32768 context.

## 9. Tests run
`uv run pytest tests/test_llm.py -q` → **9 failed** (`AttributeError: module 'cobalt_agent.config' does not have the attribute 'load_config'`, `tests/test_llm.py:38,59,…`). `test_orchestrator.py` 7 pass (Pass 3 run). No test exercises `_call_provider` key resolution, `api_base`, `ask_structured` parsing, or Cortex routing successfully today.

## 10. UNVERIFIED
- Whether LiteLLM ≥1.81.8 forwards `tools=[{"googleSearch": {}}]` to Gemini grounding as intended (not executed).
- Whether LM Studio strips `<think>` blocks for the `mainframe` alias (if not, `ask_structured` fails on thinking output).
- Which vault secret names exist (`GEMINI_API_KEY`, `OPENAI_API_KEY`, `LM_STUDIO_API_KEY`) — key-resolution path depends on exact names.
- Whether Gemini rejects the `BriefingAgent`'s mid-conversation `system` messages via LiteLLM.
- ADR(s) in the vault covering the 122B→27B migration or the cloud embedder choice.
