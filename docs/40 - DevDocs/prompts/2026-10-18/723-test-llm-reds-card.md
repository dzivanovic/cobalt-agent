JOB: test-llm-reds-1018
LADDER: OFF-LADDER — reports/cto-2026-10-15.md 2026-10-15 R1598
CLASS: K5
INSTALL: none
BRANCH: test/test-llm-reds-1018
WORKTREE: test-llm-reds-1018
BASE: 279c99ce
TIP: 9850f4d0
REPORT: /Users/cobalt/cobalt-wt/test-llm-reds-1018/docs/40 - DevDocs/reports/test-llm-reds-1018-build-2026-10-18.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/test-llm-reds-1018-check-2026-10-18.md
HOUSE B: none
BAND: MID
RESTARTS: none
RULINGS: 2026-10-18 R1833

## ROWS

The 9 reds of `tests/test_llm.py` on BASE (recorded: `reports/jev-shadow-build-2026-10-15.md:85` and `:203`, run `uv run pytest -q tests/test_vault.py tests/test_llm.py tests/cobalt/test_modelaccess_config.py` → `9 failed, 46 passed`, all 9 in `tests/test_llm.py`, each `AttributeError: <module 'cobalt_agent.config' …> does not have the attribute 'load_config'`). The cause is a STALE TEST, not a code defect: every red patches `cobalt_agent.config.load_config`, which `src/cobalt_agent/config.py` never defines (it holds `_load_config` at `:525` and the public `get_config` at `:664`), while `LLM` reads `get_config` (`src/cobalt_agent/llm.py:47` and `:85`, a local import resolved at call time, so a patch of `cobalt_agent.config.get_config` is seen). `git diff d601b1f6 -- src/cobalt_agent/config.py` touches no `load_config` line (jev-shadow-build `:85`). The nine tests are the nine lines of `tests/test_llm.py` that hold `patch("cobalt_agent.config.load_config")`: `:38` `test_llm_initialization_with_default_role`, `:59` `test_llm_initialization_with_custom_role`, `:69` `test_switch_role_updates_model`, `:97` `test_generate_response_calls_completion`, `:119` `test_ask_method_calls_completion`, `:151` `test_ask_structured_returns_pydantic_model`, `:194` `test_llm_api_base_resolved_for_local_model`, `:203` `test_llm_no_api_base_for_cloud_model`, `:219` `test_ask_structured_contains_both_system_prompt_and_json_schema` (all proved on BASE by `grep`; 9 lines, matching the recorded 9). The job edits `tests/test_llm.py` only; no `src/` line changes. Rows T2 and T3 are PREDICTED from reading the code, not recorded: each is built only when its RED is proved (L70). The order is T1, T2, T3.

| row | what | red first | files |
|---|---|---|---|
| T1 | THE PATCH TARGET. Each of the nine `with patch("cobalt_agent.config.load_config") as mock_load:` lines becomes `with patch("cobalt_agent.config.get_config") as mock_load:`; nothing else on those lines or in their bodies. `get_config` exists (`config.py:664`) and is what `llm.py:47` and `:85` call, so the mock config reaches `_resolve_model_config` and `_call_provider` | RUN the whole file BEFORE the edit: `uv run pytest -q -p no:cacheprovider tests/test_llm.py` → `9 failed`, each `AttributeError: … does not have the attribute 'load_config'`, the nine test ids and the first error line quoted whole. RED = those nine ids. After the edit the same command is run and EVERY failure left is quoted whole (the input of T2 and T3); the first four tests that construct only (`default_role`, `custom_role`, `switch_role`, `no_api_base_for_cloud_model`) are expected green here | `tests/test_llm.py` |
| T2 | PREDICTED, UNPROVEN (L70): THE COMPLETION PATCH. `_call_provider` imports `completion` locally (`src/cobalt_agent/llm.py:163`, `from litellm import completion`), so `patch("cobalt_agent.llm.completion")` (`tests/test_llm.py:102`, `:124`, `:156`, `:227`) is never the function called, and the real `litellm.completion` runs. If, after T1, any of `test_generate_response_calls_completion`, `test_ask_method_calls_completion`, `test_ask_structured_returns_pydantic_model`, `test_ask_structured_contains_both_system_prompt_and_json_schema` is red, and its failure is the real LiteLLM call (a provider, auth or network error, or `mock_completion.assert_called_once()` / `call_args` on an unused mock), the four patches become `patch("litellm.completion")` (found by content). If none is red after T1, T2 is not built and the report says `T2: NOT NEEDED` with the run quoted | The test that fails after T1 for this row's reason, named, with the assertion or error line quoted whole; GREEN after the edit, quoted. A test red for another reason is not T2's: it goes under `## DECISIONS`, UNPROVEN, with the output | `tests/test_llm.py` (the patch string of those four lines) |
| T3 | PREDICTED, UNPROVEN (L70): THE LOCAL API BASE. `test_llm_api_base_resolved_for_local_model` asserts `llm._api_base == "http://192.168.1.100:11434"` (`tests/test_llm.py:199`); `_resolve_model_config` builds `f"{protocol}://{ip}:{port}/v1"` (`src/cobalt_agent/llm.py:81`, the OpenAI-compatible base). If, after T1, this test is red on that assertion, the expected string becomes `"http://192.168.1.100:11434/v1"`; the code is not changed (the `/v1` suffix is the code's behaviour, `llm.py:81`). If the test is green or red for another reason, T3 is not built and the report says so with the run quoted | `AssertionError` on `tests/test_llm.py:199`, the `assert 'http://192.168.1.100:11434/v1' == 'http://192.168.1.100:11434'` line quoted whole; GREEN after the edit | `tests/test_llm.py` (the one expected string) |
| Z1 | RUN — asserts nothing. `uv run pytest -q -p no:cacheprovider tests/test_llm.py` → `0 failed`, quoted whole; `git diff <BASE> --stat` → `tests/test_llm.py` only, and `git diff -U0 <BASE> -- tests/test_llm.py` lists only the `patch(` lines, T3's assertion line and nothing else; then `uv run pytest -q -p no:cacheprovider tests/test_vault.py tests/test_llm.py tests/cobalt/test_modelaccess_config.py` (the recorded command) → `0 failed`; `uv run cobalt jobs restarts <BASE>..HEAD` and its `RESTARTS:` line | — (tool output quoted in the report) | none |

## NOT IN THIS JOB
- Any `src/` file, `src/cobalt_agent/config.py` and `src/cobalt_agent/llm.py` included: a code defect found while proving T2 or T3 is a `## DECISIONS` item, never fixed here.
- Any test file but `tests/test_llm.py`; `tests/test_scheduler.py`, `tests/test_scribe.py`, `tests/test_cortex.py`, `tests/test_finviz_extractor.py` (old-tree reds named in `reports/s2-p2-rebase-2026-09-17.md:37`): not part of the 9 and not run for this card.
- Retiring or deleting a test: all nine are fixed, none is removed (nothing under `docs/` or the test set is deleted without his word).
- The gate lists (`ops/desk/gate-lists.md`): `tests/test_llm.py` is in no gate pass and stays out of them.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-build-2026-10-15.md` lines 85, 92 and 203 (the recorded 9 reds and their error).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-check-card-preflight-2026-10-15.md` line 44 and `reports/brain-direction-2026-10-02.md` line 299 (the defect-card direction).
- `tests/test_llm.py` lines 11-34 (`mock_config`) and 36-255; `src/cobalt_agent/llm.py` lines 46-82 (`_resolve_model_config`) and 83-174 (`_call_provider`); `src/cobalt_agent/config.py` lines 525 and 664.

## DEPLOY PROOF
- `grep -c -F "cobalt_agent.config.get_config" /Users/cobalt/cobalt/tests/test_llm.py` · before `0` · after `9`
- `grep -c -F "cobalt_agent.config.load_config" /Users/cobalt/cobalt/tests/test_llm.py` · before `9` · after `0`
- the file's own suite · `uv run pytest -q -p no:cacheprovider tests/test_llm.py` · green: `0 failed`

## RECORDS
- Drafter `draft-k5-test-llm-reds` (prompt 722), 2026-10-18 06:21 EDT from `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `279c99ce` (the BASE); `git -C /Users/cobalt/cobalt status --short -- tests/test_llm.py src/cobalt_agent/config.py src/cobalt_agent/llm.py` printed nothing (the tree equals `main` for them). Nothing was run: no test is run by a drafter.
- `grep -n "load_config" tests/test_llm.py` → nine lines (`:38 :59 :69 :97 :119 :151 :194 :203 :219`), all `patch("cobalt_agent.config.load_config")`; `grep -rn "load_config" src/cobalt_agent` → only `_load_config` (`config.py:90 :408 :410 :412 :525`, `playbook.py:21 :25`) and an alias import in `briefing.py:11`, so no `cobalt_agent.config.load_config` exists.
- The last commit to touch `tests/test_llm.py` or `config.py`: `git log --oneline -1 -- tests/test_llm.py src/cobalt_agent/config.py` → `06e016b2` (jev-shadow-1015; it touched no `load_config` line, per jev-shadow-build `:85`).
- The decision to carry as a defect card is DESK RECORD R1598 (`reports/cto-2026-10-15.md:36`, brain, L79); this card is launched under his 2026-10-18 R1833 (`reports/cto-2026-10-18.md:9`).
- T2 and T3 are read from the code, not from a recorded failure: the nine reds recorded show only the `load_config` error, which stops each test at its first line, so what lies behind it is unrecorded.
