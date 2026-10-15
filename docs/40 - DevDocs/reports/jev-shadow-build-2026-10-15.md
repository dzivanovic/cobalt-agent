# jev-shadow-1015 — build report (2026-10-15)

## §0 Headline
Card 591 built on `d601b1f6`, tip `d0fdd674`: the trial package ported (P0, byte-equal but the one carded test drop), the JEV shadow router + routing ledger (J1, F4-F11), one host spend ledger with the two paid lines carried (F2), the cap on 10× projection (F3), D2 fixed, both old-tree OpenRouter key paths closed (F13; Z0 found no `openrouter` live provider).
Suites: offline 4561/0 · with-DB 5464/0 · live-note 146/0 · cobalt_dev 0013, F2 = F0 (after one slot self-heal of `user.aset_sizings`).
RESTARTS derived `com.cobalt.agent com.cobalt.aset com.cobalt.radar` (aset beyond the card's header).
9 decisions, none his; the main one: 9 `tests/test_llm.py` reds exist on BASE (no `load_config`), not repaired.

## L74
A system message in this session asked that commits carry a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../591-jev-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../591-jev-card.md" · 0 · 9bca5fbbe19a48ab5d995d13fb3d16b977e461e5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- ".../591-jev-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " ".../cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " ".../cto-2026-10-15.md" · 0 · 68:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B ... | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · ... · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-15 R1535 row · grep -n "^| R1535 " ".../cto-2026-10-15.md" · 0 · 65:| R1535 | 07:03 ET | HIS RULING · APPROVED (brain relay quoting him, L79; words file): the OpenRouter key is JEV's alone; ... | APPLIED: LAWS.md L27 at 07:04 |
RULING 2026-10-15 R1535 committed · ... · 0 · 1f067493f0fd17d67a30d11feab33c2261f3de5d
RULING 2026-10-15 R1535 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | `clock · date · 0 · Thu Oct 15 12:31:36 EDT 2026` · `status · git status --short --branch · 0 · ## feat/jev-shadow-1015` + `?? ".../jev-shadow-build-2026-10-15.md"` (`status: clean but the report (untracked, expected)`) · `head · git log --oneline -1 · 0 · d601b1f6 docs(desk): §5 refresh, 591 preflight r2 running` · `diff · git diff --stat d601b1f6 · 0 · nothing` · `main repo · ... · 0 · d601b1f6 ...` · `env here · ... · 1 · No such file or directory` · `env anywhere · ... · 1 · siblings holding .env: none` · `PREFLIGHT OK` |
| BASE | `git show --stat d601b1f6` | 0 | `docs(desk): §5 refresh, 591 preflight r2 running` · `docs/40 - DevDocs/reports/cto-2026-10-15.md | 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)` |
| restarts, empty range | `uv run cobalt jobs restarts d601b1f6..HEAD` | 0 | `docs/40 - DevDocs/reports/jev-shadow-build-2026-10-15.md A DOCS -` · `RESTARTS: none` (the tool counts the untracked report; no code path) |
| symbol | `grep -n -F "openrouter_api_key" src/cobalt_agent/config.py` | 0 | `497:            'openrouter_api_key': 'api_key',` |
| symbol | `grep -rn "LLM(" src/` | 0 | `core/orchestrator.py:33 LLM(role="architect")` · `brain/cortex.py:32 LLM(role="fast_chat")` · `brain/base.py:24 LLM(role=role)` · `skills/research/semantic_tagger.py:247 LLM(role='strategist')` · `skills/research/deep_dive.py:34 LLM(role="default")` · `skills/productivity/briefing.py:33 LLM(model_name=model_name)` · `main.py:44 LLM(role="default")` · `services/scheduler.py:124 LLM(role=role)` |
| symbol | `grep -n ... src/cobalt_agent/config.py` | 0 | `104:class LLMConfig(BaseModel):` · `106: model_name: str = "gemini/gemini-1.5-pro"` · `266: env_prefix="COBALT_"` · `267: env_nested_delimiter="__"` · `272: llm: LLMConfig = Field(default_factory=LLMConfig)` · `280: active_profile: Optional[dict[str, str]] = None` |
| card RECORDS | copied from the card | — | drafter `draft-jev-card` 11:22 ET, `main` `3591d1b0`; `main` holds no `src/cobalt/classify/`; `jev/trial-0923` tip `f4e8de85`; AMEND 1 (brain 0e848919, 12:17 EDT, `main` `226cb495`): check 74 dropped, card 593 superseded, P0 port, D2 carried, Z0/F13 STOP rows. Re-read here: `git diff --stat d601b1f6...f4e8de85` → 38 files, 6140 insertions (the card's count) |

## Z0 — the live provider read (row Z0, edits nothing)
`configs/config.yaml` (read whole `:1-90`): no top-level `llm:` key (Grep `^llm:` over `configs/` → no hit); `models:` `:42`; `provider: "openrouter"` only at `:57` (`cloud_claude_4_6_opus`), `:61` (`cloud_claude_4_6_sonnet`); `active_profile:` `:78-84`: `default: "mainframe"`, `coder: "mainframe"`, `architect: "mainframe"`, `strategist: "mainframe"`, `researcher: "cloud_gemini_3_1_pro_preview"`, `fast_chat: "mainframe"`. Grep of `active_profile|openrouter|^models:|^llm:` over `configs/` → only `config.yaml` lines (no other file sets a profile). Loader: `llm.py:50-51` `model_alias = active_profile.get(self.role, active_profile.get("default"))`; `:59`/`:64` `provider`.

| service | role (caller) | model alias | provider |
|---|---|---|---|
| com.cobalt.agent | `default` (`main.py:44`, `deep_dive.py:34`, `brain/ops.py:42`) | mainframe | `openai` (local node `cortex`) |
| com.cobalt.agent | `fast_chat` (`brain/cortex.py:32`) | mainframe | `openai` |
| com.cobalt.agent | `architect` (`core/orchestrator.py:33`) | mainframe | `openai` |
| com.cobalt.agent | `coder` (`brain/engineering.py:43`) | mainframe | `openai` |
| com.cobalt.agent | `strategist` (`semantic_tagger.py:247`) | mainframe | `openai` |
| com.cobalt.agent | `researcher` (`scheduler.py:77`, `:124`) | cloud_gemini_3_1_pro_preview | `gemini` |
| com.cobalt.agent | `briefing.py:33` `LLM(model_name=…)`: `role` defaults `default` (`llm.py:24`) | mainframe | `openai` |
| com.cobalt.radar | none: Grep `cobalt_agent\.llm|litellm|openrouter` (case-insensitive) over `src/cobalt` → only `modelaccess` docstrings naming litellm; no `LLM(` and no `openrouter` | — | — |

Z0: no running service resolves to `openrouter`. F13 goes ahead as carded. (A `COBALT_ACTIVE_PROFILE` environment override of a running service cannot be read from this seat; recorded under `## RECORDS`.)

## P0 THE PORT
Every ported file written by Write from `git show f4e8de85:<path>`; staged, then `git diff --cached --stat f4e8de85 -- src/cobalt/classify configs/cobalt/classify tests/cobalt/test_classify_*.py (9) tests/fixtures/classify "docs/40 - DevDocs/cobalt/classify" "docs/40 - DevDocs/tests/fixtures/classify"` → exit 0, quoted whole:
```
 tests/cobalt/test_classify_door.py | 12 ------------
 1 file changed, 12 deletions(-)
```
That one hunk is P0's carded drop of `test_the_wrapper_is_secret_free_and_execs_the_cli` (with its section comment), "not ported: tests ops/run_classify_trial.sh, which F12 keeps out". Every other ported file is byte-equal to `f4e8de85` at the port. `git diff --cached d601b1f6 -- src/cobalt/cli.py "docs/40 - DevDocs/cobalt/cli.md"`: `cli.py` +2 only (`from cobalt.classify import cli as classify_cli  # noqa: E402` after `cards_cli`; `classify_cli.add_parser(sub)` after `drc_cli.add_parser(sub)`), main's lines kept; `cli.md` +11, the trial's `## 2026-09-23 — JEV trial: cobalt classify` section appended after main's last section. Not ported: `ops/run_classify_trial.sh`, the trial's reports. Rows of this card later change `collector.py`, `config.py`, `ledger.py`, `models.py`, `cli.py` (classify), `trial.yaml`, 7 classify test fixtures (one line each, F2) and 5 classify DevDocs (one dated line each); every hunk is named under E3.

## E0 BASELINE
Run on BASE `d601b1f6` + the uncommitted P0 port (the card's ORDER puts P0 before the reds; recorded under DECISIONS).
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4512 passed, 806 skipped, 1 xfailed, 36 warnings in 748.37s (0:12:28)` (exit 0); its last skip line `SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.06s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=no tests/cobalt/test_jev_shadow_1015.py` on the P0 port → `33 failed, 16 passed, 15 warnings in 1.75s`. The 16 PASSED are exactly the controls: `test_f13_classify_never_imports_cobalt_agent`, `test_f13_control_gemini_entry_still_injected_and_loaded`, `test_f2_control_a_check_never_creates_the_file`, `test_f3_control_a_call_well_under_the_cap_is_sent`, `test_j1_control_trial_sets_unchanged`, `test_f4_control_trial_render_keeps_its_state`, `test_f5_control_trial_yaml_holds_no_routing`, `test_f6_control_shadow_hub_has_no_opus_builder_row`, `test_j2_control_classify_path_unchanged`, `test_f7_control_check_done_shape`, `test_f8_control_no_routing_ledger_in_the_repo`, `test_f9_control_the_trial_run_still_stops_on_a_cap_error`, `test_f10_control_no_retire_command`, `test_f11_control_design_keeps_g1_to_g6`, `test_f1_control_trial_ceiling_unchanged`, `test_f12_no_route_wrapper_in_ops`.
Reds, first lines (`--tb=line`):
- D2 `test_d2_a_400_digit_cost_never_raises_overflow`: `collector.py:177: OverflowError: int too large to convert to float`.
- F13 (1): `AssertionError: assert 'dummy-or-lower' != 'dummy-or-lower'` (log `Injected openrouter_api_key into LLM config`); (2): `assert 'OPENROUTER_API_KEY' not in {'OPENROUTER_API_KEY': 'dummy-or-upper', …}`; (3): `assert 'dummy-or-upper' not in ('dummy-or-upper', 'dummy-or-env')` (the `api_key` passed to completion).
- F2 (1): `assert 0.0 == 0.001 ± 1.0e-09` (the second checkout reads its own file); (2): `assert 0.0 == 3.402e-05 ± 3.4e-11`; (3): `Regex pattern did not match. Expected regex: 'outside every checkout'` — actual `spend_ledger  Extra inputs are not permitted [type=extra_forbidden …]`.
- F3: `Failed: DID NOT RAISE <class 'cobalt.classify.collector.ClassifyError'>` (`4.9999 + 0.00002 < 5`, the stub was called).
- J1 (1), F4 (1)(2), F5 (1)-(3), F6 (1)(2), J2, F7 (1)(2), F8 (1)(2), F9 (1)-(4), F10 (1)(2), F11 (1)(2): `ImportError: cannot import name 'route' from 'cobalt.classify'`. J1 (2): `argparse.ArgumentError: argument command: invalid choice: 'route' (choose from discover, probe, trial)` → `SystemExit: 2`. F5 (4), F8 (3), F1: `FileNotFoundError: … configs/cobalt/classify/route.yaml`.
Red commit `1f71790c` `wip(jev-shadow-1015): red — P0 port of src/cobalt/classify from f4e8de85 and the red tests (…)` (the port and the tests in one commit; recorded under DECISIONS).
F2's fixture lines: each of the 7 `cfg` fixtures that loads the real `trial.yaml` (`test_classify_door.py`, `_fix_r1.py`, `_fix_r2.py`, `_fix_r3.py`, `_trial.py`: one added line after the load; `_keys.py`, `_discover.py`: the one `return load_trial_config()` line extended) points `spend_ledger` at `tmp_path / "scratch" / "classify-spend.jsonl"` (the path the trial's ledger had, so `test_classify_door.py:346` needs no edit) and sets `carried_spend: []`. Grep `load_trial_config` over `tests` found the 7 fixtures (door `:91`, fix_r1 `:78`, fix_r2 `:79`, fix_r3 `:84`, trial `:74`, keys `:67`, discover `:50`) plus loads that build no classifier (`test_classify_config.py`, door `:123`).

## E3 THE ROWS
- Z0: no `openrouter` live provider (above); F13 built.
- D2 (`collector.py` `_is_number`: `math.isfinite` inside `try … except OverflowError: return False`) → `-k d2` `1 passed`; the classify suites `184 passed in 24.08s`. RED, so a defect: fixed.
- F13 (`src/cobalt_agent/config.py`: `'openrouter_api_key': 'api_key',` removed from `llm_key_mapping`; the vault loop skips a name whose lower case is `openrouter_api_key`; `llm.py`: `api_key = None` when `self._env_key_ref.lower() == "openrouter"` or `target_key_name` upper-cased is `OPENROUTER_API_KEY`, neither `keys_dict.get` nor `os.getenv` read; the `:121-123` warning stands) → `-k f13` `5 passed`. `uv run pytest -q tests/test_vault.py tests/test_llm.py tests/cobalt/test_modelaccess_config.py` → `9 failed, 46 passed`: all 9 in `tests/test_llm.py`, each `AttributeError: <module 'cobalt_agent.config' …> does not have the attribute 'load_config'` (the tests patch `cobalt_agent.config.load_config`; `grep -rn -F "load_config" src/cobalt_agent/config.py` shows only `_load_config`, and `git diff d601b1f6 -- src/cobalt_agent/config.py` touches no `load_config` line). A BASE red, not this row's: DECISION 1.
- F2 (`config.py`: `WORKTREES_ROOT`, `CarriedSpend`, `spend_ledger` + `carried_spend` required, `host_ledger_path`; `ledger.py`: `carried=()` counted by `spent()`/`calls()`; `collector.py` default `Ledger(Path(cfg.spend_ledger), …, carried=…)`; `trial.yaml`: `spend_ledger: /Users/cobalt/.cobalt/classify/classify-spend.jsonl`, `carried_spend` (1.3188e-05, 2.0832e-05, each with its report line)) → `-k "f2 or d2 or f13"` `10 passed`; classify suites `184 passed in 24.46s`.
- F3 (`_send`: `self.ledger.check(OVERRUN_FACTOR * projected_usd, calls=1)`) → `-k f3` `2 passed`; classify door/fix/keys/trial `113 passed`.
- J1, F4-F11 (`route.py` NEW, `route.yaml` NEW, `models.py` `CallStatus` widened + `RouteDecision`, `cli.py` `route.add_route_parsers(csub)`): first full run `2 failed, 47 passed` — F4 (2) `assert 'auth_error' == 'refused'` (`status_of` matched the key name inside the guard's refusal text: fixed in `route.py` to `m.startswith(KEY_NAME)`), F6 (2) a TEST defect (`yaml.safe_dump` sorted the ROUTE question keys, so the load failed on the question order before the table check: the 4 `yaml.safe_dump(raw)` calls of the test file now pass `sort_keys=False`; said here). Then `49 passed`.
- F1, F11, F12 design text (by content): `:48` check 74 dropped (R1580, P0, row D2); `:50` `percentile` `:70-76`, uses `:198-203`; `:52` `10 cards × 10 identical repeats (the M5 count`; `:55` "the Noul call alone"; S6 `:168` no ledger on disk, the two lines carried; S10 `:172` "his approval of the string (not K5; fold F12)"; G5 reads "share of decision rows naming a model other than `claude-opus-5-5`"; a `| G7 |` row added; the `:140` paragraph replaced by R1532's sense. `-k "f11 or f1_ or f12"` `6 passed`.
- R1 listing (`ls` of the 8 prompt folders; Glob `docs/40 - DevDocs/prompts/2026-10-1[0-3]/*-card.md` → 88 paths): `-card.md` names per folder 10-06 17, 10-07 8, 10-08 12, 10-09 22, 10-10 18, 10-11 23, 10-12 20, 10-13 27 = 147. `route.yaml`: `call_ceiling: 518` = 2 × (147 + 11 + 100) + 2 (ASK DESK 11), `batch_wall_clock_s: 1470` = 147 × 10.
- DevDocs: `classify/route.md` NEW; one `## 2026-10-15 — jev-shadow-1015` line in `classify/collector.md`, `config.md`, `ledger.md`, `models.md`, `cli.md`. `src/cobalt_agent/` has no page under `docs/40 - DevDocs/cobalt/` (RECORDS).
- GREEN, the card's second command without `tests/test_llm.py`: `279 passed, 15 warnings in 27.55s`.
- Test rule: `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/cobalt/test_jev_shadow_1015.py` → one hit, `480:    sha = _commit(repo, {path: _card(band="LOW", tip="abcd1234", check_report="c")})` — the constructed `TIP:` value of a tmp card, not a commit of this repo.

THE MUTATIONS (Edit, run, Edit back; the tests file run whole, `--tb=line`):
| row | mutation | red |
|---|---|---|
| D2 | `except OverflowError` → `except ZeroDivisionError` | `test_d2_…`: `collector.py:181: OverflowError: int too large to convert to float` |
| F13 | mapping entry back; loop guard `== "openrouter_api_key-MUTATION"`; `llm.py` `if False:` | `3 failed, 2 passed`: (1) `assert 'dummy-or-lower' != 'dummy-or-lower'`, (2) `assert 'OPENROUTER_API_KEY' not in {…}`, (3) `assert 'dummy-or-upper' not in ('dummy-or-upper', 'dummy-or-env')`; controls green |
| F2 | default ledger back to `results_path()/"classify-spend.jsonl"`, no carried; `spend_ledger` validator a no-op | (1) `assert 0.0 == 0.001 ± 1.0e-09`, (2) `assert 0.0 == 3.402e-05 ± 3.4e-11`, (3) `DID NOT RAISE <class '…ClassifyConfigError'>` |
| F3 | `check(projected_usd, …)` | `DID NOT RAISE <class 'cobalt.classify.collector.ClassifyError'>` |
| F4 | `kept = list(header)` | `AssertionError: TIP:` |
| F6 | `return` before the id loop | `test_f6_sonnet_…`: `DID NOT RAISE` |
| F7 | the `CHECK DONE` test removed | `test_f7_no_outcome_…`: `assert {…'builder': 'claude-opus-5-5' …} is None` |
| F8 | validator on `spend_ledger` only | `test_f8_a_routing_ledger_…`: `DID NOT RAISE` |
| F10 | `retire: Optional[Retire] = None` | `test_f10_route_yaml_without_retire_…`: `DID NOT RAISE` |
| F1 | `call_ceiling: 200` | `assert 200 >= (((2 + 11) + 100) + 147)` |
| J1 | `route.add_route_parsers(csub)` removed | `test_j1_dry_run_…`: `invalid choice: 'route'` → `SystemExit: 2` (and the 4 F9 tests) |
| F5 | `band.value == "unsure-MUTATION"` | `test_f5_unsure_…`: `AttributeError: 'RoutingTable' object has no attribute 'unsure'` |
| F10 (2) | the `dd >= declared` filter removed | `test_f10_rows_before_…`: `assert False` (`all(… "n=0 insufficient data" …)`) |
| F11 (2) | `MIN_N = 29` | `assert 'n=29 insufficient data' in …` (the cell printed a figure) |
| J2 | the row also stores the card state | `assert not ['JOB: t1', 'RESTARTS: com.x.one com.x.two', '## ROWS', …]` |
| F9 (1) | `auth_failed = False` | `assert ['ok', 'trans..._error', 'ok'] == ['ok', 'trans... 'auth_error']`, stdout `ROUTE RUN cards=4 auth_error=1 ok=2 transport_error=1` |
| F11 (1) | G5 counts every named model | `'2 of 3' in 'G5 … claude-opus-5-5: 3 of 3'` false |
| F9 (2) | `startswith("spend cap-MUTATION")` | `assert ['refused'] == ['cap_refused']` |
| F9 (4) | the `CHECK DONE` filter removed from `closed_cards` | `Left contains one more item: '…/02-c2-card.md'` |
| F9 (3) | wall clock `>=` → `>`: STAYED GREEN (the monotonic clock always advances past 0); mutation strengthened to `if False:` | `assert ['ok', 'ok'] == ['timeout', 'timeout']`, stdout `ROUTE RUN cards=2 ok=2` |
After each undo: `Grep MUTATION` over `src`, `configs`, `tests` → no files; the whole-file run then the GREEN command `279 passed`.
Fix commit `06e016b2` `feat(jev-shadow-1015): JEV shadow router, one host spend ledger, old-tree OpenRouter key paths closed (D2, F13, F2, F3, J1, F4-F11, F1, F12; L10, L35, L8, L32, R1532, R1535)`.

## RESTARTS
First `uv run cobalt jobs restarts d601b1f6..HEAD` (exit 1): `FAILED: RestartError: one or more changed paths were unclassified` — `configs/cobalt/classify/route.yaml A UNCLASSIFIED CONFIG …` and `configs/cobalt/classify/trial.yaml A UNCLASSIFIED CONFIG …` (`ESCALATE: unclassified path …` each). Readers: `grep -rn -F "trial.yaml" src` → `classify/config.py:40: CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "classify" / "trial.yaml"` (+ docstrings in `config.py:1`, `route.py:26,169,274,283`, `__init__.py:8`, `cli.py:8`); `grep -rn -F "route.yaml" src` → `route.py:60: ROUTE_CONFIG_PATH = …` (+ docstrings `:4`, `:169`). No job runs `cobalt classify`; the schema (`jobs/config.py:371`, `:398-408`) needs a registered one-shot reader, so both went under `no_resident_reads` with `readers: [com.cobalt.generated]` and a `because` that says exactly that (the `drc.md.j2` precedent; ASK DESK 2). `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py` → `47 passed in 18.29s`. Commit `d0fdd674` `fix(jev-shadow-1015): configs/cobalt/classify/trial.yaml, route.yaml classified (L42)`. The table again (exit 0), abridged to its non-test, non-doc rows (whole in `## FOR THE CHECK`):
```
configs/cobalt/classify/route.yaml	A	no resident reads (one-shot: com.cobalt.generated)	-
configs/cobalt/classify/trial.yaml	A	no resident reads (one-shot: com.cobalt.generated)	-
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
src/cobalt/classify/{__init__,cli,collector,config,ledger,models,route,trial}.py	A	static import reach	com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt_agent/config.py	M	static import reach	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt_agent/llm.py	M	static import reach	com.cobalt.agent
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
The card's header expected `com.cobalt.agent com.cobalt.radar`; the derived table adds `com.cobalt.aset` (`src/cobalt_agent/config.py`'s import reach). The table is the truth (L42).

## W THE THREE SUITES
`<FP>` as typed (BUILD-HUB THE LOCK): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`. This build adds no with-DB test and no migration: no `--deselect`, no `--tickers`, no `--migration`.

GATE 1 — `sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-shadow-1015 all --deploy` → exit 1, quoted whole:
```
tests/ops: skipped (no ops paths)
offline 4561/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 3): no pytest summary line
Exit: cobalt_dev column slots: user.aset_sizings 1566 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate
! _pytest.outcomes.Exit: cobalt_dev column slots: user.aset_sizings 1566 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate !
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-shadow-1015-all-20261015-130316.log
```
SLOTS SELF-HEAL (the gate had released): one lock take by hand, 13:16 EDT (`date` 13:16:09). `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh jev-shadow-1015 90` → `lock taken: jev-shadow-1015`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's. `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db dev-rebuild user.aset_sizings --dry-run` → `DRY RUN — ROLLED BACK · max_attnum 1566 → 54 · rows 1 = 1 · catalog digest equal`; then without `--dry-run` → `REBUILT user.aset_sizings · max_attnum 1566 → 54 · rows 1 = 1 · catalog digest equal`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `SLOTS ok · highest user.card_stop_edits 747 of 1600` · `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `TABLES 0011` (LEVEL 0013). `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh jev-shadow-1015` → `lock released`; `ls /Users/cobalt/cobalt-wt/jev-shadow-1015/.env` → `No such file or directory`. `.env: removed, proven gone (W self-heal)`.

GATE 2 (`<tip>` = `d0fdd674`) — the same call → exit 0, quoted whole:
```
tests/ops: skipped (no ops paths)
offline 4561/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5464/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-shadow-1015-all-20261015-131631.log
```
Every skip is in ALLOWED SKIPS; none is marked OUTSIDE.
- (a) offline: log `:888` `4561 passed, 806 skipped, 1 xfailed, 36 warnings in 744.84s (0:12:24)`; this build adds the 49 tests of `tests/cobalt/test_jev_shadow_1015.py` and the 9 ported classify test files.
- (b) `lock taken: jev-shadow-1015` (`:895`); F0 `:906` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; LEVEL 0013.
- (c) pass 1, executed command `:962`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect …` (PASS 1 of `ops/desk/gate-lists.md` with its one `--db-only` token removed; the 22 `--deselect`s of the list, none added) → `:1123` `5259 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 843.54s (0:14:03)`.
- (c2) `:1125` `dev forward: APPLIED 13:43:27`; F1 `:1203` `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2 (`:1205`, the PASS 2 list, nothing added) → `:1977` `205 passed, 1 deselected, 5 warnings in 230.97s (0:03:50)`. with-DB = 5259 + 205 = 5464.
- (c3r) `stray rows: not read (no --tickers given)` (no with-DB test of this build writes a ticker).
- (f) rollback, F2 `:2045` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 → `cobalt_dev: 0013 — F2 = F0`; `:2098-2099` `lock released`; `ls /Users/cobalt/cobalt-wt/jev-shadow-1015/.env` → `No such file or directory`.
- (e) live-note `:2168` `146 passed, 1 skipped, 15 warnings in 26.67s`.

## PRE-STOP SELF-CHECK
(1) Every added test shown RED for its named reason: the 33 reds under `## E2 RED` (each first line quoted), the 16 controls PASSED there and after; every row's fix re-reddened by its mutation under `## E3` (table). One test stayed green under its first mutation (F9 (3), wall clock `>`): the mutation was strengthened (`if False:`) and went red; said there. The 7 edited classify fixtures: green before and after (`184 passed` twice). — holds.
(2) Entry paths: `inject_secrets` (F13 (1) and the gemini control), `_load_config`'s vault loop (F13 (2)), `LLM._call_provider` both reads (F13 (3): the keys path and, with the key absent from `keys`, the environment; the `:115` env read is pinned only through the same branch); the 8 `LLM(` callers of Z0 all go through `_call_provider`; the classify key path stays `collector.py` `_key` (F13 (4) pins no `cobalt_agent` import). `OpenRouterClassifier.__init__` default ledger (F2 (1)(2), J2 control), `_send` (F3, F9 (1)(2)), `route --card --dry-run` (J1 (2)), `route --day --run` (F9 (1)-(4)), `Router.route` (F4 (2), F5, J2), `load_card` (F4 (1)), `write_outcome` (F7), `weekly_read` (F8 (2), F10 (2), F11). Not pinned by a test: `route --card … --run`, `route-read` (`cmd_route_read`) and `write_read` through the CLI: named here (DECISION 9). — holds with that gap named.
(3) Re-read at the tip: `grep -n -e "openrouter_api_key" -e "OPENROUTER_API_KEY" src/cobalt_agent/config.py src/cobalt_agent/llm.py` → `config.py:597` (the loop guard), `llm.py:112` (the closed branch), no mapping entry; `grep -rn -e "OVERRUN_FACTOR \* projected" -e "except OverflowError" -e "carried=" src/cobalt/classify` → `collector.py:182`, `:307`, `:594`, `route.py:743`, `ledger.py:102`; `git log --oneline d601b1f6..HEAD` (three commits, below); the gate log lines by `grep -n -F` above. — holds.

## FOR THE CHECK
`d601b1f6..d0fdd674`:
- `1f71790c` wip(jev-shadow-1015): red — P0 port of src/cobalt/classify from f4e8de85 and the red tests (D2, F13, F2, F3, J1, F4-F11, F1, F12)
- `06e016b2` feat(jev-shadow-1015): JEV shadow router, one host spend ledger, old-tree OpenRouter key paths closed (D2, F13, F2, F3, J1, F4-F11, F1, F12; L10, L35, L8, L32, R1532, R1535)
- `d0fdd674` fix(jev-shadow-1015): configs/cobalt/classify/trial.yaml, route.yaml classified (L42)
Per row: reds `## E2 RED`, mutations and greens `## E3 THE ROWS`. Caller greps `## PREFLIGHT`, `## Z0`, `## RESTARTS`. RUN rows: R1 is the listing count (147; quoted under E3; the desk runs the dry run over that list after the build, ASK DESK 18); R2 is the RESTARTS table. Suites and executed commands, F0/F1/F2, lock times: `## W` (lock taken 13:16 by hand for the self-heal and released before gate 2; gate 2's take `lock: waited 0 min`, released `:2099`). ASK DESK 19: `ls /Users/cobalt/.cobalt/classify` is the desk's (before and after); every test of this build points both ledgers under `tmp_path` (`_trial_cfg`, `_route_cfg`, the 7 fixture lines), and no command of this build sent a request (no `--run`, `probe`, `discover`).
The whole RESTARTS table: `## RESTARTS` (the second run lists every path of the diff; tests and docs rows `-`).

## CONTINUE
next: none — BUILT

## DECISIONS
1. `ASK DESK: tests/test_llm.py holds 9 reds on BASE (each patches cobalt_agent.config.load_config, which BASE does not define; my diff touches no load_config line). The card's GREEN command lists it and expects 0 failed. [13:48 EDT]` Default: not repaired (the card: "an existing test that goes red otherwise is a finding, never a repair here"); the file is in no gate pass; carried as a finding for a later card.
2. `ASK DESK: L42 for configs/cobalt/classify/trial.yaml and route.yaml — no job reads them, but no_resident_reads requires a registered one-shot reader. [13:10 EDT]` Default: both listed with `readers: [com.cobalt.generated]` and a `because` that says no job runs `cobalt classify` and the label is the schema's need (the `drc.md.j2` precedent).
3. `ASK DESK: E0 ran on BASE plus the uncommitted P0 port, and the red commit holds the port and the red tests together. [12:52 EDT]` Default: the card's ORDER (P0 before the reds) taken as written; the port's byte proof is quoted under `## P0`.
4. `ASK DESK: F2's one fixture line also sets carried_spend: [] (and points spend_ledger at the trial's old tmp path, so test_classify_door.py:346 is unchanged). [12:50 EDT]` Default: kept; the existing tests pin the file's own lines, F2's own tests pin the carried lines.
5. `ASK DESK: retire.declared — ASK DESK 10 says "the deploy date", unknown at build. [13:05 EDT]` Default: `2026-10-15` (the build date); `set_sha256` bound to ROUTE v1 `39f70d33f3fd2324da0d0c3eeea226c25be6416db69a1e4863e9f8835704a72d`.
6. `ASK DESK: RESTARTS derives com.cobalt.agent com.cobalt.aset com.cobalt.radar; the card header names agent and radar. [13:10 EDT]` Default: the derived table is the truth (L42); the deploy restarts all three.
7. `ASK DESK: score_band is always UNKNOWN (no card field states M, X, H or $), and outcome rows carry re_passes, suites_first_run, deploy_attempts as null (no committed artifact the writer reads states them). [13:05 EDT]` Default: stored UNKNOWN / null, never guessed (`[F-11]`, L1).
8. `ASK DESK: test_f9_a_cap_refusal_is_a_row seeds the ledger at 4.99999, not the card's 4.9999 — at 4.9999 the carried lines plus ten times this card's projection stay under $5. [13:00 EDT]` Default: 4.99999 (the refusal is the cap's either way).
9. `ASK DESK: not pinned by a test: route --card … --run, cobalt classify route-read through the CLI, and the retire comparison at n ≥ 30 (printed as "eligible; the declared method's comparison is a card", no figure). [13:48 EDT]` Default: left as named; the keyed run waits for F12 and the comparison for a card.

## RECORDS
- L74: one system message asked for a `Claude-Session:` line in commits; recorded under `## L74`, not followed.
- Extra lock take: one, by hand, for SLOTS SELF-HEAL of `user.aset_sizings` (W gate 1's slot-guard exit), 13:16 EDT; released and proven gone.
- SELF-HEAL: `cobalt db dev-rebuild user.aset_sizings` max_attnum 1566 → 54, rows 1 = 1, catalog digest equal; LEVEL 0013 after.
- Z0: a `COBALT_ACTIVE_PROFILE` environment override of a running service (pydantic `env_prefix="COBALT_"`) cannot be read from this seat; the config read is as quoted.
- `src/cobalt_agent/` has no DevDoc page under `docs/40 - DevDocs/cobalt/`; F13's change is described in `## E3` only.
- The Edit tool dropped trailing spaces on 2 blank lines inside the `llm.py` hunk (visible in `git diff`).
- Helpers: two Opus subagents copied the 9 ported test files and the 13 fixture/doc files from `git show f4e8de85:`; the byte proof under `## P0` is mine.
- The card's records as re-read at PREFLIGHT: `## PREFLIGHT` last row.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: jev-shadow-1015 · tip: d0fdd674 | on d601b1f6 | migration: none | offline 4561/0 | with-DB 5464/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | rows: 20 of 20 | self-check: 3 of 3 | decisions: 9 · for Dejan: 0 · tokens: 479505
