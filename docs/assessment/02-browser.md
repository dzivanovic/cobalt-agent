# Cobalt Assessment — Pass 2: Browser / Playwright subsystem (+ Finviz scanner pipeline)

Date: 2026-08-21 · Baseline: `1c9c0e5` (main) · Assessor: Claude Fable 5 · Mode: read-only toward the system (code read; only fully-mocked tests run; live DB queried with `SELECT` only; **no browser sessions, no Finviz/LLM/network calls**)

Scope: `tools/browser.py` (771), `tools/aom.py` (491), `tools/maps.py` (268), `tools/extractor.py` (336), `tools/daemon.py` (264), `skills/research/finviz_extractor.py` (752), browser-side FastPath integration; plus — because Pass 0 found the scanner pipeline orphaned and Dejan flagged it income-critical — `skills/research/finviz_api.py` (435), `scanner_orchestrator.py` (115), `enrich_metadata.py` (163), `semantic_tagger.py` (329, invocation surface only; LLM logic is Pass 4/5), `configs/scanners.yaml`, `dev_utils/live_run_*.py`, and `tests/test_browser_actions.py`, `test_browser_aom.py`, `test_daemon.py`, `test_universal_extractor.py`, `test_finviz_extractor.py`.

Verdict legend: **RETAIN** · **BROKEN-FRICTION** · **KILL-candidate** (proposal — Dejan decides). **UNVERIFIED** = inferred, not read/run.

---

## 0. Headline findings

| # | Finding | Evidence |
|---|---|---|
| **H-1** | **The scanner pipeline works as a *collector* and has demonstrably run — but nothing in production invokes it.** `FinvizApiClient` (HTTP CSV export, 151 columns) → `ScannerOrchestrator` (dedupe + upsert `instruments`, append `market_snapshots`) → `MetadataEnricher` → `SemanticTagger` all executed in **2026-03-26..28**: 2 209 snapshots from 4 scanners (`morning_down_gapper` 1 536, `morning_up_gapper` 322, `day_scan_custom` 279, `low_float_gappers` 206), 345 instruments all theme-tagged, 239 with `shares_float`; last touch 2026-04-05. Zero runs since. Nothing under `src/` outside `skills/research/` references these modules (grep); the only runtime scheduler job is the 08:00 morning briefing (Pass 0 §4). `configs/scanners.yaml` `schedule:` blocks (04:00-10:00 every 2 min etc.) are read by **no code** — `ScannerOrchestrator.run_ingestion_cycle` reads only `active` + `filters`. | live DB (§3), `scanner_orchestrator.py:25-47`, grep |
| **H-2** | **Two Finviz acquisition paths exist; the Playwright scraper is superseded by the API.** `finviz_api.py` = authenticated CSV export via `elite.finviz.com/export.ashx?…&auth=<token>` (plus `quote_export.ashx`, `news_export.ashx`), async httpx, no browser, dynamic filters from YAML, all 151 columns. `finviz_extractor.py` = 752-line headless-Chromium login + table scrape of **one** hard-coded preset (`PRESET_URLS`, `:200-202`), with 4-level table/pagination heuristics, a `logs/debug_table.png` screenshot per page (`:228`), and a FastPath write-back of a script nobody can replay (H-6). The API path is what actually populated the DB. | `finviz_api.py:72-91,241-297`, `finviz_extractor.py` |
| **H-3** | **`dev_utils/live_run_orchestrator.py` — the only end-to-end runner — is broken against current code**: it constructs `SemanticTagger(db_connection=conn, llm=llm)` and calls `run_tagging_cycle(batch_size=100)` (`:132,137`); the class now takes `SemanticTagger(batch_size=20)` and exposes `run_batch()` (`semantic_tagger.py:810,269`). `TypeError` at step 5, after ingestion has already committed. The individual runners (`live_run_dynamic_scanners.py`, `live_run_finviz.py`, `live_run_finviz_quote.py`) match the API and only print. | file:line above |
| **H-4** | **`BrowserTool`'s structured-action DSL is unreachable end-to-end.** (a) `description` advertises `{'type':'fill','selector':…}` (`browser.py:92-95`) but `_parse_browser_action` accepts only `{'action':'click'/'type'/'maps'/'extract'/'inject_credentials', 'id':int…}` (`:119-147`); (b) the system prompt teaches `ACTION: browser url="…" query="…"` (`prompt.py:130`), `BaseDepartment` parses `ACTION: tool {json}` (`base.py:61-73`), Mattermost has a third parser (`mattermost.py:256`); (c) element IDs come from `hash(f"{node_name}_{id(node)}")` — a **memory address**, new every extraction (`aom.py:452`), and the LLM never sees them anyway: `extract` returns only `"Extracted N elements"` (`browser.py:272`); (d) `_execute_extract` launches a **second** Playwright session inside the running one and re-navigates (`:254-256`). Net: only "URL → cleaned body text" (and the llms.txt pre-flight) works. | file:line above |
| **H-5** | **The Zero-Trust domain whitelist is not enforced on the main browsing path.** `config.yaml browser.allowed_domains` (`finviz.com, tradingview.com, sec.gov, example.com`) is checked only in `AOMExtractor._validate_url` (`aom.py:46-85`). `BrowserTool.run/_playwright_task` navigates any URL (`browser.py:628`) and the pre-flight issues `requests.get` to any host (`:515,537`); `DaemonTool` watchers likewise. | file:line above |
| **H-6** | **FastPath is dead from the browser side too** (completing Pass 1 H-5): `_execute_fast_path_lookup` / `_execute_fast_path_write_back` / `_generate_*` (`browser.py:362-479`) are **never called** from `run()` or `_playwright_task` (grep: definitions only). `finviz_extractor._generate_fast_path_cache_entry` (`:536-623`) writes a `playwright_script` of pseudo-actions `navigate`/`extract_all_pages` that no executor understands, with a `context_signature` of a logged-in page body (never reproducible) and a full CDP DOM snapshot as JSONB. The live table's single row (2026-03-18) is this. **FastPathCache is therefore dead end-to-end.** | file:line above; Pass 1 H-5 |
| **H-7** | **Four registered "tools" cannot be executed and their prompt listing is garbage.** `ToolManager` registers `AOMExtractor()`, `Maps()`, `UniversalExtractor()`, `DaemonTool()` (`tool_manager.py:86-100`); none has `.run()`/`.name`/`.description` (grep) → `execute_tool` → `AttributeError` → `"Error executing tool …"`. `get_tool_descriptions()` returns `tools.values()` incl. schema classes and `None`s (`:104,110`) and `PromptEngine` renders `type(tool).__name__` → the LLM sees `ModelMetaclass`, `NoneType`, `AOMExtractor`… (`prompt.py:144-155`). `DaemonTool`'s `BackgroundScheduler` is **never started** (no `.start()` call anywhere) → `schedule_watcher` registers jobs that never fire. | file:line above |
| **H-8** | **`market_snapshots` typed columns are empty**: all 2 209 rows have `price IS NULL`, `volume IS NULL`; everything sits in `raw_data` JSONB under Finviz's display column names (151 keys incl. `Float %`, `Short Float`, `EPS Growth Quarter Over Quarter`, `Revenue Surprise`, `Earnings Date`, `Relative Volume`…). No Pydantic model anywhere on this path (non-negotiable #3). Same Finviz export = a ready fundamentals/short-float/earnings-date source for §8 Tier 1. | live DB (§3); `scanner_orchestrator.py:96-102` |
| **H-9** | **Start-up cost**: `ToolManager()` constructs `BrowserTool` (→`PostgresMemory`), `KnowledgeSearchTool` (→PM), `DaemonTool` (→PM + its own `BrowserTool`→PM + `UniversalExtractor`→PM), `UniversalExtractor` (→PM) = **7 `PostgresMemory()`** (each ≈10 DDL statements, Pass 1 H-6) — and `BaseDepartment.__init__` builds a fresh `ToolManager()` per department (`base.py:25`), so Cortex/scheduler/engineering each repeat it. `UniversalExtractor` and `AOMExtractor` import `get_config` fine, but `UniversalExtractor` calls LiteLLM with `config.llm.model_name` whose default is **`gemini/gemini-1.5-pro`** (`config.py:76`; `configs/config.yaml` has no `llm:` section) — bypassing `active_profile`/mainframe routing. | file:line above |
| **H-10** | **Tests**: 49 + 5 pass (all mocked: `sync_playwright`, `requests.get`, `PostgresMemory`, Mattermost). `tests/test_finviz_extractor.py` fails at import (`FinvizStockData`, Pass 0 F-6). **Zero tests** exist for `finviz_api`, `scanner_orchestrator`, `enrich_metadata`, `semantic_tagger` — the income path is untested. `TestLLMExtraction` (2 tests) calls the real LLM (not run). | run output (§6) |

---

## 1. Component map and verdicts

| Component | File:lines | Verdict | Notes |
|---|---|---|---|
| `FinvizApiClient` | `finviz_api.py:38-374` | **RETAIN** (core collector) | Vault key `finviz.com::api_token` (`:201`); `compile_filters` + `execute_dynamic_screener` (`:107-152`) make `scanners.yaml` filters live; `get_screener` presets (`:72-91`) **duplicate** the YAML filters in code; `get_quote`, `get_news` exist (news = Finviz news export, §8 input); token appended to URL (`:274`, Finviz's design) and *not* logged (`:276` truncates before `&auth`). `&c=` hard-coded column list (`:77,81,85,90`), `MASTER_COLUMNS` 151 (`:67`). Unlocks vault on construction (`:106`) and again lazily (`:204-227`); the `config.vault.master_key` branch (`:163-166`) references a field `VaultConfig` doesn't have (`config.py:201-204`) → always falsy, harmless. |
| `ScannerOrchestrator` | `scanner_orchestrator.py` | **RETAIN → fix** | Reads `configs/scanners.yaml` (`:16,25`, CWD-relative), runs active scanners **sequentially** despite "concurrently" comment (`:37-47`), dedupes by `Ticker`/`1_Ticker`/`ticker` (`:54`), tags `active_on_scanners`, upserts `instruments` (metadata `{}`/themes `[]` on insert; only `updated_at` on conflict, `:83-92`), appends `market_snapshots(instrument_id, timestamp, raw_data)` (`:96-102`) — never fills `price/volume/vwap/spread`. psycopg2 `Json`; raw `print()` summary (`:110-116`); caller must `commit()`. No module docstring. |
| `MetadataEnricher` | `enrich_metadata.py` | **RETAIN** | Batches `&t=` ticker lists (`:114`), maps 7 fields into `instruments.metadata` (`:121-129`); own psycopg2 connection via config; `__main__` sweep of "starving" tickers. `sys.path` hack (`:28-29`). |
| `SemanticTagger` (surface) | `semantic_tagger.py:810-317` | Pass 4/5 | `LLM(role='strategist')` per batch (`:250`), prompt from `config.prompts.research.semantic_tagger` with fallback (`:151-156`), writes `active_themes` state objects with status `ACTIVE`/`NONE` (`:206-209`) while the declared `InstrumentThemeState` says `HOT/WARM/COLD` and `_format_theme_state` (HOT) is unused (`:169-171`). `logging` + `loguru` both configured (`:16,22,35-39`). Themes table status casing is mixed (`active`/`ACTIVE`/`DORMANT`) — tagger uses `ILIKE`. |
| `FinvizExtractor` (Playwright) | `finviz_extractor.py` | **KILL-candidate** (superseded by API; keep only if Elite export ever disappears) | Hard-coded login URL (`:154`), selectors (`:176-192`), one preset URL incl. `&ar=10` auto-refresh (`:201`, UNVERIFIED whether it reloads mid-scrape), `networkidle` waits up to 60 s on an ad-heavy site (`:155,487,693`), screenshot per page to `logs/` (`:228`), pagination href rewriting (`:403-498`), `TimeoutError` misuse (`:267`, builtin not Playwright's). Works only with `finviz.com::username/password` in vault. Nothing imports it except the broken test. |
| `BrowserTool` | `browser.py` | **BROKEN-FRICTION** (plain fetch RETAIN; action DSL KILL-candidate) | What works: `run(url)` → pre-flight `llms.txt`/`llms-full.txt`/`Accept: text/markdown` (`:481-565`; heuristics `startswith("#") or "**" in content`, "non-HTML ⇒ hit" `:551`) → headless Chromium `goto` + strip `script/style/nav/footer/header/iframe` + `body.inner_text` (`:605-699`), truncated to 4 000 chars on `str()` (`:87`), in a 1-worker thread pool (`:769`). Action DSL: H-4. Shares the **global `Maps` singleton** across all instances/threads (`maps.py:233`). `_inject_credentials_to_page` fills by `name/id/placeholder` guesses (`:341-345`) — fine, never returns secrets. |
| `AOMExtractor` | `aom.py` | **BROKEN-FRICTION → KILL-candidate** | CDP `DOMSnapshot.captureSnapshot` (`:134`) parsed with an assumed `[type, nameIdx, valueIdx, attr…]` node layout (`:204-210`); ephemeral context; whitelist check (`:46-85`, exact host match — no subdomains, e.g. `elite.finviz.com` would be **rejected**, test `:525` confirms); IDs non-stable (H-4c); `aria-hidden` check compares `("true","true")` (`:346`); as a registered tool it is uncallable (H-7). |
| `Maps` | `maps.py` | **KILL-candidate** | Stores `id → selector` dicts with a `valid` flag; `_lock = None` despite "thread-safe" docstring (`:37`); never holds real `ElementHandle`s; only consumer is the non-functional DSL. |
| `UniversalExtractor` + `compute_delta` | `extractor.py` | **BROKEN-FRICTION** | Prompt hard-coded in `.py` (`:116-155`, `.clinerules` rule 3), `response_format=json_object` to model `config.llm.model_name` (H-9), swallows all errors to empty output (`:210-216`); `compute_delta` **writes** nodes/edges as a side effect of "computing" a delta (`:258-295`); never produced non-AST graph rows in prod (Pass 1). |
| `DaemonTool` / `_run_watcher_job` / `_send_watcher_alert` | `daemon.py` | **BROKEN-FRICTION → KILL-candidate** | Scheduler never started (H-7); job builds `BrowserTool()`+`UniversalExtractor()` per run (`:184,196`, 2 more `PostgresMemory`), pointless `compute_delta([], [], …)` (`:193`), alerts to hard-coded `town-square` (`:259`) via a new `MattermostInterface()` each time. Jobs are in-process only (lost on restart), no persistence. Is this the "news/X watcher" seed? As built, no. |
| `dev_utils/live_run_orchestrator.py` | | **BROKEN** (H-3) | |
| `dev_utils/live_run_dynamic_scanners.py`, `live_run_finviz.py`, `live_run_finviz_quote.py` | | RETAIN as manual smoke runners | Print-only; `live_run_finviz.py:40` prints an `export COBALT_MASTER_KEY=` hint (INFRA-0 policy). |
| `configs/scanners.yaml` | | RETAIN (make authoritative) | 4 scanners with `schedule.start/end/recurrence_minutes` in naive `"HH:MM"` strings (ET implied, no tz) — unused. |
| Tests | §6 | BROKEN-FRICTION | |

---

## 2. What invokes what today (verified by grep + DB)

```
PRODUCTION PROCESS (main.py __main__)
  CobaltScheduler ── only job: morning_briefing 08:00 Mon-Fri
  ToolManager ── registers browser/daemon/aom/maps/extractor (dangerous → HITL) ── browser URL-fetch is the only working browser capability
  Cortex/BaseDepartment ── ACTION: parsing (3 incompatible syntaxes) → execute_tool
  ──► NO path reaches finviz_api / scanner_orchestrator / enrich_metadata / semantic_tagger / finviz_extractor

MANUAL (dev_utils, terminal, needs COBALT_MASTER_KEY + vault token)
  live_run_dynamic_scanners.py ─► FinvizApiClient.execute_dynamic_screener (scanners.yaml) ─► print
  live_run_finviz.py ─► FinvizApiClient.get_screener("Morning Up Gapper") ─► print
  live_run_finviz_quote.py ─► FinvizApiClient.get_quote("NVDA") ─► print
  live_run_orchestrator.py ─► ScannerOrchestrator.run_ingestion_cycle ─► instruments + market_snapshots   [then crashes at SemanticTagger(...)]
  src/…/enrich_metadata.py __main__ ─► instruments.metadata
  src/…/semantic_tagger.py __main__ ─► process_entire_queue ─► instruments.active_themes
  src/…/sync_taxonomy.py __main__ ─► themes (from vault note)
```

---

## 3. Live-DB evidence (read-only)

- `market_snapshots`: 2 209 rows, `2026-03-26 15:45Z .. 2026-03-28 15:37Z` (2 047 on 03-26, 162 on 03-28); 231 distinct instruments; **2 209 NULL `price`, 2 209 NULL `volume`**; `raw_data` keys = Finviz export columns (151), plus `active_on_scanners` tags: `morning_down_gapper` 1 536 · `morning_up_gapper` 322 · `day_scan_custom` 279 · `low_float_gappers` 206.
- `instruments`: 345 (created 03-26..03-28, last `updated_at` 2026-04-05); 345 with `active_themes`, 239 with `metadata.shares_float`.
- `themes`: 21 (e.g. AI & Compute, Nuclear & Power Gen, GLP-1, Post-Earnings Drift, Quantum Computing, Meme Stock Resurgence; status strings `active`/`ACTIVE`/`DORMANT`).
- `browser_fast_path`: 1 row = the Finviz extractor's unreplayable entry (Pass 1).
- `daily_in_play`, `news_events`, `news_mentions`, `key_levels`, `strategy_signals`: **0 rows, no writers** — i.e. the pipeline stops at "snapshots + tags"; nothing ranks, alerts, or produces "stocks in play".

---

## 4. What it would take to wire the scanner pipeline into production (proposal, not done)

Honest sizing: the **collector is the hard part and it exists and works**. The missing pieces are glue, typing, an output, and tests — roughly one sprint, local-model-delegable for the mechanical parts.

1. **Pick the path**: API (`FinvizApiClient`) is production; retire the Playwright scraper (or quarantine it as a manual fallback). Requires the vault secret `finviz.com::api_token` to be current (UNVERIFIED — vault not read; it was valid in March).
2. **Scheduling** (`services/scheduler.py`): add jobs driven by `scanners.yaml.schedule` (start/end window, `recurrence_minutes`, explicit `America/New_York` tz; `CobaltScheduler` is a sync `BackgroundScheduler`, orchestrator is async → `asyncio.run` inside the job or switch to `AsyncIOScheduler`). Gate on market calendar (weekdays; holidays later). Make the window config, not code.
3. **Connection**: give `ScannerOrchestrator` a connection factory from config (today the caller hands it a psycopg2 conn) — or move it onto the memory layer's connection once Pass 1 B-1 (URL-encoding) is fixed; decide psycopg v2 vs v3 (Pass 1 B-14).
4. **Typing**: a Pydantic `MarketSnapshot`/`ScreenerRow` model mapping the Finviz column names → populate `price`, `volume`, `rvol`, `gap`, `float`, `short_float`, `earnings_date`… (the columns already exist in `raw_data`). This is also the cheapest §8 Tier-1 fundamentals feed.
5. **Output = the product**: a deterministic `daily_in_play` writer (rank by RVOL/gap/float per `rules.yaml` thresholds) + Mattermost post/alert on new entrants — the "stocks in play" the requirements open with. Without this step scanning is invisible to Dejan.
6. **Chain**: ingestion → `MetadataEnricher.enrich(enrich_starving=True)` for new tickers → `SemanticTagger.run_batch()` (local model) — all three exist; only the call chain is missing (and H-3 must be fixed).
7. **Tests**: fixture CSVs (recorded once) for `FinvizApiClient` parsing, `ScannerOrchestrator` dedupe/upsert against a mocked cursor or `cobalt_dev`, and the typed mapping; mark the one live call `@pytest.mark.integration`.
8. **Config hygiene**: delete the duplicated `PRESET_QUERIES` (or generate them from YAML); move the `&c=` column list to config; `scanners.yaml` becomes the single source.
9. **HITL**: scanning is read-only → no approval needed; alerts are informational; keep trading-logic thresholds (`rules.yaml`) behind the approval token when they change.

---

## 5. Hardcoded paths, names and structural assumptions

| Where | Value / assumption |
|---|---|
| `finviz_api.py:72-91`, `finviz_extractor.py:200-202` | Preset queries/URLs + `&c=0,1,4,5,129,…` column list in code; `MASTER_COLUMNS=151` (`:67`); `DEFAULT_PRESET_NAME="Morning Up Gapper"` |
| `finviz_api.py:63,201,273`, `finviz_extractor.py:65,111-112,154` | `finviz.com::api_token` / `::username` / `::password` secret-naming convention; `https://elite.finviz.com`; `https://finviz.com/login-email?remember=true` |
| `finviz_api.py:94`, `finviz_extractor.py:70,735`, `dev_utils/live_run_*` | `data/.cobalt_vault` (CWD-relative) |
| `scanner_orchestrator.py:16`, `dev_utils/live_run_dynamic_scanners.py:33` | `configs/scanners.yaml` (CWD-relative) |
| `scanner_orchestrator.py:54` | ticker column may be `Ticker` / `1_Ticker` / `ticker` |
| `finviz_extractor.py:227-228` | `logs/debug_table.png` written every page |
| `finviz_extractor.py:235-262,383-396` | Finviz table/pagination selectors (`table.styled-table-new`, `bgcolor="#d3d3d3"`, `a.tab-link:has-text("next")`…) |
| `browser.py:622`, `aom.py:117`, `finviz_extractor.py:668` | Fixed Chrome/120 Windows user-agent string ×3 |
| `browser.py:509-511,515-517`, `:628,678`, `aom.py:125-128` | `llms.txt` endpoints, 5 s/15 s/2 s timeouts; `Cobalt-Watcher/1.0` UA |
| `browser.py:422`, Pass 1 | FastPath threshold 0.85 |
| `daemon.py:259` | Mattermost channel `town-square` |
| `extractor.py:116-165` | extraction prompt in code; `raw_text[:15000]` |
| `config.py:76` | `LLMConfig.model_name="gemini/gemini-1.5-pro"` default (no `llm:` in YAML) |
| `config.yaml:135-140` | whitelist exact-host list; `example.com` in prod config; no `elite.finviz.com` |
| `semantic_tagger.py:206-209` vs `:777-785` | theme-state vocab mismatch (`ACTIVE/NONE` vs `HOT/WARM/COLD`) |
| `configs/scanners.yaml` | times as naive `"HH:MM"` strings, no timezone |

---

## 6. Tests run

- `uv run pytest tests/test_browser_actions.py tests/test_browser_aom.py tests/test_daemon.py -q` → **49 passed** (all `sync_playwright`/`requests`/Mattermost/config patched; `src.`-prefixed imports in the first two — Pass 0 F-6).
- `uv run pytest tests/test_universal_extractor.py -k "not LLMExtraction" -q` → **5 passed, 2 deselected** (`TestLLMExtraction` calls the real model — not run).
- `tests/test_finviz_extractor.py` → ImportError at collection (`FinvizStockData`, `FinvizExtractionResult` no longer exist); its body is otherwise fully mocked. Also, its `test_vault_master_key_exists` reads `COBALT_MASTER_KEY` from `.env` (Pass 1 H-8 pattern).
- Coverage gaps: no test for `finviz_api` (filter compile, CSV parse, token resolution), `scanner_orchestrator` (dedupe/upsert), `enrich_metadata`, `semantic_tagger`; no test for `BrowserTool.run` URL path beyond pre-flight; `test_browser_aom` asserts the whitelist **rejects** subdomains (`:525`) — i.e. the test enshrines the `elite.finviz.com` problem.

---

## 7. RETAIN / BROKEN-FRICTION / KILL-candidate summary

**RETAIN**: `FinvizApiClient` (+ `get_news`, `get_quote`); `ScannerOrchestrator` (after fixes); `MetadataEnricher`; `configs/scanners.yaml` as the source of truth; `BrowserTool` plain URL fetch + pre-flight; vault-namespaced credential convention; Playwright 1.58 + Chromium 1208 installed.

**BROKEN-FRICTION**: scanner schedule unread / no runtime invocation (H-1); `live_run_orchestrator.py` signature drift (H-3); `market_snapshots` untyped/NULL columns (H-8); sequential scanner execution; duplicated presets vs YAML; whitelist exact-host + not enforced on `BrowserTool` (H-5); 7 `PostgresMemory` per `ToolManager` and one `ToolManager` per department (H-9); `UniversalExtractor` model default (H-9); `DaemonTool` scheduler never started (H-7); three ACTION syntaxes + class-name tool listing (H-4/H-7); tests (H-10).

**KILL-candidates** (Dejan decides): `finviz_extractor.py` (superseded by API); browser action DSL + `Maps` + `AOMExtractor`-as-tool (H-4, H-7) — keep `is_url_allowed` logic, apply it to `BrowserTool`; browser-side FastPath methods + `FastPathCache` entirely (H-6 + Pass 1 K-2); `DaemonTool` in its current form (replace with real scheduled collectors under `services/scheduler.py`); `UniversalExtractor`/`compute_delta` as a production path (graph-from-LLM has never produced prod data; revisit when the research engine defines what the graph is for).

---

## 8. Inputs to other passes / INFRA

- **Pass 3 (HITL)**: `DANGEROUS_TOOLS` includes `browser` → every URL fetch needs approval; `bypass_hitl` path (`tool_manager.py:112-170`); dangerous-tool dicts are returned to `BaseDepartment` (`base.py:83-84`).
- **Pass 4 (scanners/trading logic)**: §4 plan; `semantic_tagger` LLM usage; `daily_in_play` writer; `rules.yaml` consumers.
- **Pass 5 (LLM routing)**: `UniversalExtractor` bypasses routing; three ACTION syntaxes; tool listing; `SemanticTagger` uses role `strategist` (→ mainframe).
- **Pass 6 (scribe/vault)**: none.
- **Pass 7 (config)**: `BrowserConfig` whitelist semantics; `LLMConfig` default; `VaultConfig.master_key` phantom; CWD-relative config paths.
- **Research engine (§8)**: Finviz export already yields float, short float, earnings date, EPS/revenue surprise columns per ticker (`raw_data`), and `get_news` exists — cheap first Tier-1 feed alongside EDGAR/FMP.
- **INFRA-1**: scanner jobs must not run from the dev worktree against prod DB; the schedule config should carry an `env` guard.

## 9. UNVERIFIED (explicitly)
- Whether `finviz.com::api_token` is still valid / present in the vault (vault not read).
- Whether `&ar=10` in the scraper's preset URL triggers page auto-refresh during extraction.
- Whether nested `sync_playwright()` in `_execute_extract` works at all under the running sync session (never exercised by tests).
- Whether any Mattermost/CLI conversation has ever successfully executed a `browser` action with structured `actions` (no log/DB evidence either way; the 4 approved `browser` HITL rows from March have `tool_kwargs` I did not read).
