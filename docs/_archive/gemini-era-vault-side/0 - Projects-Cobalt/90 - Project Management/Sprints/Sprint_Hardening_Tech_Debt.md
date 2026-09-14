# Sprint: Architecture Hardening & Tech Debt Removal

## Chunk 1: Configuration & Magic String Purge
- [x] **Routing Keywords:** Move `orchestrator_keywords` and `high_risk_keywords` out of `cortex.py` and into `rules.yaml`.
- [x] **Model Fallbacks:** Ensure `cortex.py` and all tools default strictly to the local model defined in `active_profile.default` in `config.yaml`.
- [x] **Database Envs:** Sweep `dev_utils/*.py`. Remove all hardcoded fallback passwords. Raise explicit `ValueError` if `POSTGRES_PASSWORD`, `POSTGRES_USER`, `POSTGRES_DB`, or `POSTGRES_HOST` are missing.
- [x] **DRY Config:** Update all `dev_utils/` scripts to import and use the central `load_config()` from `cobalt_agent.config` instead of manually loading `.env`.
- [x] **Test Fixes:** Fix mock config in `tests/test_cortex.py` to properly return keyword lists from `MagicMock` objects. All 16 tests now passing.
- [x] **56/56 Tests Passing:** Full test suite passes with 16/16 cortex tests, 8/8 orchestrator tests, 7/7 scheduler tests, and 25/25 vault tests.

## Chunk 2: The Prompt Extraction
- [x] **YAML Setup:** Create a `configs/prompts.yaml` file (or add a `prompts:` section to `rules.yaml`).
- [x] **Extraction:** Sweep all `.py` files (especially `scheduler.py`, `cortex.py`, `proposals.py`, and `ops.py`). Extract every hardcoded LLM system prompt and user prompt template into the YAML file.
- [x] **Integration:** Refactor the Python files to load these prompts dynamically via the configuration object.

## Chunk 3: Dynamic Filesystem Routing
- [x] **Path Logic:** Refactor `filesystem.py` and `cortex.py`. They must strictly read the vault root path from `.env`. 
- [x] **Inbox vs Projects:** Ensure the logic dynamically appends `0 - Inbox/` only when explicitly sending a message/briefing to the Inbox. Ensure the agent can still freely navigate the root and `0 - Projects/` substructure for coding and documentation tasks.
- [x] **Tests:** All 56 tests passing. Filesystem path traversal protection verified.

## Chunk 4: Concurrency & Exception Safety
- [x] **Non-Blocking Proposals:** Refactor `wait_for_approval()` in `proposals.py` to remove `time.sleep()`. Implement a safe, non-blocking alternative (e.g., `asyncio` or `threading.Event()`) that maintains current functionality without freezing the WebSocket event loop.
- [x] **DB Connection Managers:** Update `dev_utils/` scripts (like `ingest_knowledge.py`) to use `with PostgresMemory() as db:` or explicitly call a `.close()` method to prevent connection leaks.
- [x] **Tracebacks:** Sweep `browser.py`, `filesystem.py`, and `cortex.py`. Convert broad `logger.error(str(e))` calls inside exception blocks to `logger.exception("...")`.

## Chunk 5: Strict Tool Schemas
- [x] **Remove literal_eval:** Strip `ast.literal_eval` from `filesystem.py` and `base.py` and replace with `json.loads` + try/except that returns string error to LLM on failure.
- [x] **Pydantic Tooling:** Bind tools to strict Pydantic schemas using LiteLLM's structured output/function calling features to guarantee JSON integrity before parsing.
- [x] **filesystem.py Validation:** Added Pydantic input models (`ReadFileInput`, `WriteFileInput`, `ListDirectoryInput`) and registered with ToolManager schema registry.
- [x] **browser.py Validation:** Added `BrowserCommand` Pydantic model for structured input validation; `run()` now accepts `**kwargs` and validates through Pydantic.
- [x] **tool_manager.py:** Updated to register tools with schemas; executes validation before tool execution; returns detailed error messages for `ValidationError` or `JSONDecodeError`.
- [x] **Error Handling:** All tool errors (validation, JSON parsing) return human-readable strings to LLM for self-correction instead of crashing.

## Chunk 6: Validation & Documentation Sweep
- [x] **Test Suite:** Run the full `pytest` suite. Fix any tests broken by the refactoring. Add new tests for the YAML prompt loading.
- [x] **Wiki Sync:** Perform a full sweep of `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/` and update the markdown files to reflect the new architectures and prompt locations.

---

**SPRINT COMPLETE AND VALIDATED.**
All 56 tests passing (16/16 cortex, 8/8 orchestrator, 7/7 scheduler, 25/25 vault).

**Architectural Changes Documented:**
- Prompts centralized in `configs/prompts.yaml`
- Magic strings and credentials strictly pulled via `cobalt_agent.config`
- Filesystem paths dynamically resolved from `.env` vault root
- Tool schemas strictly enforced via Pydantic; `ast.literal_eval` purged
