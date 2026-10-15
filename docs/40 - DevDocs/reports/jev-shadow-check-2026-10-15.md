# jev-shadow-1015 — CHECK (one pass)

## §0 Headline
Check of card 591 at `d0fdd674`. House A was Grok (2 findings); there was no house B (`as needed`, and Gemini OUT at the probe). 8 findings, 0 dropped, **7 held, all fixed** (opus-own 5: O1, O3, O4, O5, O6 · house 2: H1, H2); O2 REJECTED by F9's carded definition (open, FOR DEJAN).
The two most serious: a `--day` batch crashed on any closed card with no empty-`TIP:` commit (O1); LiteLLM still read `OPENROUTER_API_KEY` from the environment for an openrouter model after F13 (O4).
New tip `5316fafe`. Gate exit 0: `tests/ops: run (deploy gate)`, offline 8307/0, with-DB 5471/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`. The F13, F2 and F3 mutations were re-run here and each goes red.
ready: YES · decisions 3 · for Dejan 1.

## L74
- A system reminder in this session (not a tool result) asked that commits end with a `Claude-Session:` line. CHECK-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/603-jev-shadow-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/603-jev-shadow-check-card.md" · 0 · 6e883218304bf9454f1e0127e5c49d4115a900cd
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/603-jev-shadow-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 89:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
RULING 2026-10-15 R1535 row · grep -n "^| R1535 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 86:| R1535 | 07:03 ET | HIS RULING · APPROVED (brain relay quoting him, L79; words file): the OpenRouter key is JEV's alone; authority for the JEV card row removing `openrouter_api_key` from the old-tree mapping; goes in the tribunal packet. | APPLIED: LAWS.md L27 at 07:04 |
RULING 2026-10-15 R1535 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1535 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1f067493f0fd17d67a30d11feab33c2261f3de5d
RULING 2026-10-15 R1535 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → row 35 (STANDING `Bash(grok *)`), `grep -n "^| R19 "` → row 37 (four house strings STANDING), `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty). Time: `Thu Oct 15 16:14:54 EDT 2026`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Thu Oct 15 16:14:59 EDT 2026
status · git status --short --branch · 0 · ## feat/jev-shadow-1015
head · git log --oneline -1; git log --stat --format=%h d0fdd674..HEAD · 0 · (6 lines)
    f298a7bf docs(jev-shadow-1015): build report — d0fdd674
    f298a7bf
    
     .../reports/jev-shadow-build-2026-10-15.md         | 224 +++++++++++++++++++++
     .../reports/jev-shadow-build-2026-10-15.result     |  15 ++
     2 files changed, 239 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/jev-shadow-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/jev-shadow-1015/docs/40 - DevDocs/reports/jev-shadow-build-2026-10-15.md" · 0 · BUILT · job: jev-shadow-1015 · tip: d0fdd674 | on d601b1f6 | migration: none | offline 4561/0 | with-DB 5464/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | rows: 20 of 20 | self-check: 3 of 3 | decisions: 9 · for Dejan: 0 · tokens: 479505
range · git log --oneline d601b1f6..d0fdd674 · 0 · (3 lines)
    d0fdd674 fix(jev-shadow-1015): configs/cobalt/classify/trial.yaml, route.yaml classified (L42)
    06e016b2 feat(jev-shadow-1015): JEV shadow router, one host spend ledger, old-tree OpenRouter key paths closed (D2, F13, F2, F3, J1, F4-F11, F1, F12; L10, L35, L8, L32, R1532, R1535)
    1f71790c wip(jev-shadow-1015): red — P0 port of src/cobalt/classify from f4e8de85 and the red tests (D2, F13, F2, F3, J1, F4-F11, F1, F12)
PREFLIGHT OK
```
- THE RANGE typed (`git log --stat --format=%h d601b1f6..d0fdd674`): 3 commits. Path union: `configs/cobalt/jobs.yaml`, `configs/cobalt/classify/{route,trial}.yaml`, `src/cobalt/classify/{__init__,cli,collector,config,ledger,models,route,trial}.py`, `src/cobalt/cli.py`, `src/cobalt_agent/{config,llm}.py`, `tests/cobalt/test_classify_{config,discover,door,fix_r1,fix_r2,fix_r3,keys,models,trial}.py`, `tests/cobalt/test_jev_shadow_1015.py`, five `tests/fixtures/classify/*.json`, and docs (`docs/30 - Design/jev-shadow-design-2026-10-14.md`, `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/classify/*.md`, `docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md`).
- `ls <S>` → `No such file or directory` (fresh).
- House probes (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"`, exit 0), whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
  Gemini: HARNESS (no return time named). No `HOUSE A: OpenAI` header: Sol not probed.
- Seats: `house A: grok · house B: none (not needed)` — the card's `HOUSE B: as needed` (not `mandatory`). The card's X10 asks for house B "for the money"; see `## DECISIONS` ASK DESK 1.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → last line `STAGED 44 files · 761874 bytes · commits 3` (commits 3 = PREFLIGHT's range). Per-file lines (bytes, dest under `<S>`): diff.md 288574; files/603-jev-shadow-check-card.md 28991; files/jev-shadow-build-2026-10-15.md 34075; files/wt/configs/cobalt/classify/route.yaml 4391; …/trial.yaml 21071; files/wt/configs/cobalt/jobs.yaml 21310; files/wt/docs/30 - Design/jev-shadow-design-2026-10-14.md 23357; files/wt/docs/40 - DevDocs/cobalt/classify/{__init__ 595, cli 4072, collector 9261, config 2720, ledger 2686, models 2494, route 4513, trial 2775}.md; files/wt/docs/40 - DevDocs/cobalt/cli.md 6195; files/wt/docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md 2348; files/wt/src/cobalt/classify/{__init__ 936, cli 7400, collector 28233, config 15562, ledger 5632, models 10215, route 33172, trial 8055}.py; files/wt/src/cobalt/cli.py 25870; files/wt/src/cobalt_agent/config.py 25173; files/wt/src/cobalt_agent/llm.py 14281; files/wt/tests/cobalt/test_classify_{config 6942, discover 8204, door 16014, fix_r1 11856, fix_r2 7782, fix_r3 12937, keys 9543, models 4973, trial 8636}.py; files/wt/tests/cobalt/test_jev_shadow_1015.py 35974; files/wt/tests/fixtures/classify/{openrouter-model-entry.real-shape 1076, openrouter-probe-response.real-shape 225, openrouter-probe-s1.real-shape 619, openrouter-systemone-response.openapi-example 298, systemone-openapi-example 2111}.json; rulings.md 727.
`stage-copy.sh` (the `## READ` files the script cannot derive):
- `COPIED 54394 …/files/591-jev-card.md`
- `COPIED 4055 …/files/jev-design-decisions-2026-10-14.md`
- `COPIED 5165 …/files/jev-tribunal-fold-answer-2026-10-15.md`
- `COPIED 3869 …/files/routing-table-answer-2026-10-14.md`
`HOUSE-INSTRUCTIONS.md` written (29370 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House A Grok started `Thu Oct 15 16:17:45 EDT 2026` (date before the gates), background id `bvsugjcck`; no house B. After return: `git status --short --branch` → `## feat/jev-shadow-1015`.

## OWN FINDINGS
Written before either house list was opened. Tests go into `tests/cobalt/test_jev_shadow_1015.py` (its own fixtures: `_repo`, `_commit`, `_card`, `_closed_card`, `_batch`, `Stub`, `_answers`, `_route_cfg`, `_dec`, `_out`, `old_tree`, `_vault`, `fake_vault`).

FINDING O1
ROW: F9
CLAIM: `cmd_route` loads every closed card with `load_card` (`src/cobalt/classify/route.py:730`) BEFORE `run_batch`, and `launch_sha` raises `ClassifyError` for a card with no empty-`TIP:` commit (`route.py:327`), so one such card (a check card carries `TIP:` and `CHECK REPORT:`) crashes the whole `--day` batch: no status row for any card, a non-zero exit.
RUN: TEST
```python
def test_o1_a_closed_card_with_no_launch_commit_is_a_status_row_not_a_crash(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    good = _closed_card(repo, 1)
    path = f"{PROMPTS}/02-c2-card.md"
    report = f"{REPORTS}/c2-check.md"
    _commit(repo, {path: _card("c2", tip="t2-tip", check_report=report),
                   report: f"# check c2\n\n{CHECK_DONE}\n"})
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub)
    assert sorted(r["card_path"] for r in rows) == sorted([good, path])
```
EXPECT: on the tip `ClassifyError: …02-c2-card.md: no commit of the card has an empty TIP: header — no launch commit` raised out of `args.func(args)`.

FINDING O2
ROW: F9
CLAIM: `closed_cards` (`route.py:530-542`) takes every `-card.md` whose `CHECK REPORT:` file ends `CHECK DONE`; a CHECK card names the same `CHECK REPORT:` as its build card, so one closed build yields two cards (two keyed calls, two decision rows) in the day's batch.
RUN: TEST
```python
def test_o2_a_build_and_its_check_card_route_once(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    build = f"{PROMPTS}/01-c1-card.md"
    check = f"{PROMPTS}/02-c1-check-card.md"
    report = f"{REPORTS}/c1-check.md"
    _commit(repo, {build: _card("c1", check_report=report),
                   check: _card("c1", check_report=report),
                   report: f"# check c1\n\n{CHECK_DONE}\n"})
    assert route.closed_cards(repo, DAY) == [build]
```
EXPECT: `assert [build, check] == [build]` — two paths returned.

FINDING O3
ROW: F11 (F7)
CLAIM: `weekly_read` joins EVERY outcome row to its decision (`route.py:634-636`) and never filters `stage`, while F7 writes an outcome after the check AND again after the deploy (`write_outcome(..., stage=)`, `route.py:570`), so 15 cards fill a cell to `n=30` and print a mean (L8 breach).
RUN: TEST
```python
def test_o3_a_check_and_a_deploy_outcome_of_one_card_count_once(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    at = datetime(2026, 1, 5, 12, tzinfo=timezone.utc)
    rows = []
    for i in range(15):
        card = f"c{i}"
        rows.append(_dec(card, band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=at))
        for stage in ("check", "deploy"):
            rows.append({**_out(card, builder="grok-4.7", held=i % 3), "stage": stage})
    text = route.weekly_read(rows, cfg, week=date(2026, 1, 5))
    assert "n=15 insufficient data" in text
    assert "mean" not in text
```
EXPECT: `assert 'n=15 insufficient data' in …` fails (the cell reads `n=30 mean=…`).

FINDING O4
ROW: F13 (X1)
CLAIM: `LLM._call_provider` sets `api_key = None` for an `openrouter` model (`src/cobalt_agent/llm.py:112-113`) and calls `litellm.completion` without `api_key` (`:147-148`, `:158`); LiteLLM then reads `OPENROUTER_API_KEY` from the environment itself (`.venv/…/litellm/main.py:3175-3181`), so the environment path the row closes is re-opened one level down.
RUN: TEST
```python
def test_o4_an_openrouter_model_never_reaches_litellm_with_the_environment_key(old_tree, tmp_path, monkeypatch):
    import litellm.main as lm
    from cobalt_agent.config import _load_config
    from cobalt_agent.llm import LLM

    key, conf = old_tree
    _vault(tmp_path / "data" / ".cobalt_vault", key, {})
    settings = _load_config(conf)
    settings.active_profile = {"default": "cloud_claude_4_6_opus"}
    monkeypatch.setenv(KEY_NAME, "dummy-or-env")
    monkeypatch.setattr("cobalt_agent.config.get_config", lambda: settings)
    seen: dict = {}

    def fake_http(**kwargs):
        seen["api_key"] = kwargs.get("api_key")
        raise RuntimeError("constructed stop")

    monkeypatch.setattr(lm.base_llm_http_handler, "completion", fake_http)
    llm = LLM(role="default")
    with pytest.raises(Exception):
        llm._call_provider([{"role": "user", "content": "hi"}])
    assert seen.get("api_key") != "dummy-or-env"
```
EXPECT: `assert 'dummy-or-env' != 'dummy-or-env'`.

FINDING O5
ROW: F2
CLAIM: `host_ledger_path` refuses only `REPO_ROOT` and `WORKTREES_ROOT` (`src/cobalt/classify/config.py:323-327`); run from a worktree, `REPO_ROOT` is the worktree, so a `spend_ledger` inside the main checkout `/Users/cobalt/cobalt` loads — not "outside every checkout".
RUN: TEST
```python
def test_o5_a_spend_ledger_inside_the_main_checkout_is_refused(tmp_path):
    from cobalt.classify import config as cfg_mod

    raw = yaml.safe_load(TRIAL_YAML.read_text())
    raw["classify"]["spend_ledger"] = "/Users/cobalt/cobalt/scratch/classify-spend.jsonl"
    p = tmp_path / "trial.yaml"
    p.write_text(yaml.safe_dump(raw, sort_keys=False))
    with pytest.raises(cfg_mod.ClassifyConfigError, match="outside every checkout"):
        cfg_mod.load_trial_config(p)
```
EXPECT: run from this worktree: `Failed: DID NOT RAISE <class 'cobalt.classify.config.ClassifyConfigError'>`.

FINDING O6
ROW: F7
CLAIM: `write_outcome` splits the `CHECK DONE` line on ` · ` (`route.py:584-587`); a shadow card's line carries `held: <n> (opus-own <a> · house <b>)` (CHECK-HUB :22), so `held` parses as `3 (opus-own 2` and `_int` stores `null` (`route.py:595`) though the line states it.
RUN: TEST
```python
def test_o6_a_shadow_check_done_line_gives_its_held_count(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    path = f"{PROMPTS}/01-c1-card.md"
    report = f"{REPORTS}/c1-check.md"
    line = CHECK_DONE.replace("held: 3 ·", "held: 3 (opus-own 2 · house 1) ·")
    _commit(repo, {path: _card("c1", check_report=report), report: f"# check c1\n\n{line}\n"})
    out = route.write_outcome(repo, path, tmp_path / "routing-ledger.jsonl")
    assert out is not None and out["held"] == 3
```
EXPECT: `assert None == 3`.

## Findings
House A Grok: completion notice 16:33:21 (`date`); `ls -la <S>` → `house-a.md` 1949 bytes, written by Grok itself (stdout only `…/house-a.md` and a two-sentence preamble). Its list ends `FINDINGS: 2`. House B: none (not needed). The drop rule (`RUN:` followed by `def test_` or an allowed command) keeps both.
- H1 · grok · F11 · `weekly_read` prints a `rows_band` median under n=30 (`route.py:657-660`); the F11 test checks only `mean` · TEST
- H2 · grok · F9 · the wall-clock test pins the bound only at 0 with the real monotonic clock, so `>=`→`>` stays green · COMMAND (`grep -n -F -e … tests/cobalt/test_jev_shadow_1015.py src/cobalt/classify/route.py`)
- O1–O6 · opus-own · as under `## OWN FINDINGS` · TEST each

## Dropped
none

## RUNS
Each test run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no [--tb=short] tests/cobalt/test_jev_shadow_1015.py::<test>` on the tip `d0fdd674` (no form repair was needed).
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `::test_o1_a_closed_card_with_no_launch_commit_is_a_status_row_not_a_crash` | `1 failed` · `route.py:730: in cmd_route` → `route.py:327: ClassifyError` `E cobalt.classify.collector.ClassifyError: docs/40 - DevDocs/prompts/2026-01-05/02-c2-card.md: no commit of the card has an empty TIP: header — no launch commit` | HELD |
| O2 | opus-own | `::test_o2_a_build_and_its_check_card_route_once` | `1 failed` · `Left contains one more item: 'docs/40 - DevDocs/prompts/2026-01-05/02-c1-check-card.md'` | REJECTED — card 591 F9: "the cards whose check CLOSED that day (a card whose `CHECK REPORT:` file's last line starts `CHECK DONE`, committed that day, ASK DESK 16)": a check card meets the carded definition. Test removed again (Edit); OPEN |
| O3 | opus-own | `::test_o3_a_check_and_a_deploy_outcome_of_one_card_count_once` | `1 failed` · `AssertionError: assert 'n=15 insufficient data' in '# Routing read — week of 2026-01-05 …'` | HELD |
| O4 | opus-own | `::test_o4_an_openrouter_model_never_reaches_litellm_with_the_environment_key` | `1 failed` · `AssertionError: assert 'dummy-or-env' != 'dummy-or-env'`; log `CRITICAL: Failed to extract actual hash for 'openrouter'` then `Executing: openrouter/anthropic/claude-4.6-opus` | HELD |
| O5 | opus-own | `::test_o5_a_spend_ledger_inside_the_main_checkout_is_refused` | `1 failed` · `Failed: DID NOT RAISE <class 'cobalt.classify.config.ClassifyConfigError'>` | HELD |
| O6 | opus-own | `::test_o6_a_shadow_check_done_line_gives_its_held_count` | `1 failed` · `assert (… is not None and None == 3)` | HELD |
| H1 | grok | `::test_f11_the_under_30_read_prints_no_median` | `1 failed` · `'median' is contained here:` `low: n=29 median rows=4` | HELD |
| H2 | grok | `grep -n -F -e "batch_wall_clock_s=0" -e "clock=time.monotonic" -e "clock() - t0 >=" tests/cobalt/test_jev_shadow_1015.py src/cobalt/classify/route.py` → `tests/cobalt/test_jev_shadow_1015.py:775: … batch_wall_clock_s=0)` · `:785: … batch_wall_clock_s=0)` · `src/cobalt/classify/route.py:480: clock=time.monotonic) -> list[RouteDecision]:` · `:487: if clock() - t0 >= wall_clock_s:`; then the claim run: Edit `route.py:487` `>=` → `>`, `uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_jev_shadow_1015.py -k "wall_clock"` → `PASSED …::test_f9_the_wall_clock_bound_writes_timeout_rows` `1 passed, 55 deselected`; Edit back, `git diff --stat -- src` → empty | the output shown; the boundary mutation stays green | HELD |
Red commit: `d68bb8cb wip(jev-shadow-1015): check red — O1, O3, O4, O5, O6, H1` (H2's test is a new pinning test, shown red under the mutation in `## FIXES`).

### The card's RUN rows (assert nothing; output quoted)
- **Z0**: `configs/config.yaml` (Read `:34-85`): `keys:` `:34-39` (`openrouter: "OPENROUTER_API_KEY"` `:38`); `provider: "openrouter"` only at `:57` (`cloud_claude_4_6_opus`) and `:61` (`cloud_claude_4_6_sonnet`); `active_profile:` `:78-84` → `default`, `coder`, `architect`, `strategist`, `fast_chat`: `"mainframe"` (provider `openai`, `node_ref: "cortex"`, `:44-49`); `researcher`: `"cloud_gemini_3_1_pro_preview"` (provider `gemini`, `:72-75`). Loader `llm.py:50-51` `model_alias = active_profile.get(self.role, active_profile.get("default"))`, `:59`/`:64` provider. `grep -rn "LLM(" src/` → `core/orchestrator.py:33 role="architect"`, `brain/cortex.py:32 role="fast_chat"`, `brain/base.py:24 role=role`, `skills/research/semantic_tagger.py:247 role='strategist'`, `skills/research/deep_dive.py:34 role="default"`, `skills/productivity/briefing.py:33 LLM(model_name=model_name)` (role defaults `default`, `llm.py:24`), `main.py:44 role="default"`, `services/scheduler.py:124 role=role`. Every role resolves to `mainframe`/`openai` or `cloud_gemini_3_1_pro_preview`/`gemini`; none to `openrouter`. **`com.cobalt.aset`**: Grep `cobalt_agent` over `src/cobalt/aset` → one hit, `src/cobalt/aset/prefill.py:22: from cobalt_agent.skills.research.finviz_api import FinvizApiClient`; `grep -n -E "^(from|import) " src/cobalt_agent/skills/research/finviz_api.py` → `csv`, `io`, `os`, `typing`, `urllib.parse`, `loguru`, `httpx`, `from ...config import get_config`, `from ...security.vault import VaultManager`: no `LLM`, no `litellm` — aset resolves NO LLM role; it reaches `cobalt_agent/config.py` (hence its RESTARTS label), not `llm.py`. Z0: no running service resolves to `openrouter`. (An environment `COBALT_ACTIVE_PROFILE` override cannot be read from this seat, as the build recorded.)
- **P0**: `git diff --stat f4e8de85 d0fdd674 -- <classify tree, its configs, the 9 classify tests, fixtures, the two DevDoc dirs>` → `route.yaml +85` (J1/F5/F8/F10/F1), `trial.yaml +11` (F2), `classify/{cli,collector,config,ledger,models}.md +3` each (one dated line), `route.md +74` (J1), `src/cobalt/classify/cli.py 5 +-` (J1), `collector.py 18 +-` (D2, F2, F3), `config.py +40` (F2), `ledger.py 14 +-` (F2), `models.py 43 +-` (F9, J2), `route.py +783` (J1…F11), `test_classify_discover.py 2 +-`, `test_classify_door.py 13 +-`, `test_classify_fix_r1.py`, `_r2.py`, `_r3.py`, `test_classify_trial.py` `1 +` each, `test_classify_keys.py 2 +-`; `21 files changed, 1085 insertions(+), 24 deletions(-)`. `git diff f4e8de85 d0fdd674 -- tests/cobalt/test_classify_{door,discover,keys,fix_r1}.py` → each fixture's one F2 line (`model_copy(update={"spend_ledger": str(tmp_path / "scratch" / "classify-spend.jsonl"), "carried_spend": []})`) and the door file's carded drop of `test_the_wrapper_is_secret_free_and_execs_the_cli` with its `# -- the wrapper (written, never run)` header (12 lines). The fixtures and `__init__.py`, `trial.py`, `test_classify_config.py`, `test_classify_models.py` print no hunk (byte-equal). `git diff d601b1f6 d0fdd674 -- src/cobalt/cli.py "docs/40 - DevDocs/cobalt/cli.md"` → `cli.py` +2 (`from cobalt.classify import cli as classify_cli  # noqa: E402` after `cards_cli`; `classify_cli.add_parser(sub)` after `drc_cli.add_parser(sub)`), `cli.md` +11 (the trial's `## 2026-09-23 — JEV trial: cobalt classify` section after main's last section); main's lines kept.
- **X0b**: `grep -rn -i "openrouter" src/cobalt_agent configs/config.yaml` (on the check tip, after O4's fix) → `config.py:596` comment; `config.py:597` the loop guard (closes the path); `llm.py:91` flag init, `:111` comment, `:113` the closed branch (closes), `:115` flag set, `:151-154` the placeholder that stops LiteLLM's env fallback (closes, O4); `configs/config.yaml:38`, `:57`, `:59`, `:61`, `:63` (YAML names, not edited, card fence); two `__pycache__` binary matches. No hit is a path that resolves the key. On the BUILD tip `d0fdd674` the same grep would lack `:91`, `:115`, `:151-154`: LiteLLM's own `get_secret_str("OPENROUTER_API_KEY")` (`litellm/main.py:3175-3181`) still resolved it — O4.
- **X0c**: `grep -rn -F "write_text" src/cobalt/classify` → `route.py:704` (`write_read`, the weekly read: `out_dir` default `REPO_ROOT / REPORTS_DIR`, not a ledger), `cli.py:54`, `:105` (discover/probe results under the worktree's `scratch/`, `_scratch_out`; not ledgers). `grep -rn -F ".open(" src/cobalt/classify` → `trial.py:171` (trial results, `results_dir: scratch`; not a ledger), `route.py:483` (`_append`: the routing ledger, and `write_outcome`'s `ledger` argument), `ledger.py:130` (the spend ledger, `record`), `collector.py:276` (the HTTP opener, not a file). `grep -rn -F "mkdir" src/cobalt/classify` → `trial.py:170`, `route.py:482`, `route.py:703`, `ledger.py:123`, `cli.py:53`, `:104`. `grep -rn -F ".write(" src/cobalt/classify` → `trial.py:172`, `route.py:437`, `:442`, `:455`, `:471` (`self.write` = the router's guarded append), `route.py:484`, `ledger.py:131`. Config: `route.yaml:22 spend_ledger: /Users/cobalt/.cobalt/classify/classify-spend.jsonl`, `route.yaml:31 routing_ledger: /Users/cobalt/.cobalt/classify/routing-ledger.jsonl`, `trial.yaml:46` the same `spend_ledger`, `trial.yaml:54 results_dir: scratch`. The two ledgers resolve under `/Users/cobalt/.cobalt/classify/` and are validated by `host_ledger_path`; `write_outcome(repo, path, ledger)` takes its ledger path as an argument with no `host_ledger_path` check and has no CLI caller (recorded, not a finding: no row names its caller).
- **R1**: Glob `docs/40 - DevDocs/prompts/2026-10-0[6-9]/*-card.md` → 59 paths (10-06 17, 10-07 8, 10-08 12, 10-09 22); `2026-10-1[0-3]/*-card.md` → 88 (10-10 18, 10-11 23, 10-12 20, 10-13 27); total **147** = the build's count; `route.yaml:26` `call_ceiling: 518` = 2 × (147 + 11 + 100) + 2, `:28` `batch_wall_clock_s: 1470` = 147 × 10 (its `source` lines).
- **R2**: `uv run cobalt jobs restarts d601b1f6..d0fdd674` (from this worktree) → the table: `route.yaml`, `trial.yaml` `A no resident reads (one-shot: com.cobalt.generated) -`; `configs/cobalt/jobs.yaml M registry; register, no restart -`; docs rows `DOCS -`; `src/cobalt/classify/*.py` and `src/cobalt/cli.py` `static import reach com.cobalt.radar`; `src/cobalt_agent/config.py M static import reach com.cobalt.agent,com.cobalt.aset,com.cobalt.radar`; `src/cobalt_agent/llm.py M static import reach com.cobalt.agent`; tests and fixtures `test/documentation; no resident -`; last line `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` = the card header; the two configs under `no_resident_reads` with readers `com.cobalt.generated` as the card says.
- **X0a**: `uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_jev_shadow_1015.py -k "f3 or f9_a_cap"` → `PASSED tests/cobalt/test_jev_shadow_1015.py::test_f3_a_call_whose_ceiling_cost_passes_the_cap_is_not_sent` · `PASSED …::test_f3_control_a_call_well_under_the_cap_is_sent` · `PASSED …::test_f9_a_cap_refusal_is_a_row` (stdout `ROUTE RUN cards=1 cap_refused=1`) · `3 passed, 53 deselected in 0.26s`. Lines (Read): `test_f9_a_cap_refusal_is_a_row` `:763` `spend = _spend_file(tmp_path, 4.99999)`, `:767` `assert stub.calls == []`; `test_f3_…` `:420` `_send_with_ledger_at(tmp_path, monkeypatch, 4.9999)`, `:423` `clf._send(payload, projected_usd=0.00002)`, `:424` `assert stub.calls == []`, `:425` `assert path.read_text() == before`.

## FIXES
One commit, `5316fafe fix(jev-shadow-1015): … (check O1, O3, O4, O5, O6, H1, H2)`, inside the rows' files (F9/F7/F11 `route.py`, F2 `config.py`, F13 `llm.py`, the test file) plus one dated line each in `docs/40 - DevDocs/cobalt/classify/route.md` and `config.md` (`src/cobalt_agent/` has no DevDoc page, as the build recorded).
- O1 (F9): `cmd_route` loads each card under `try`; a `ClassifyError` becomes `Router.unloaded_row` → status `invalid` (dry run: a `guard=invalid` line); the batch goes on.
- O3 (F11/F7): `weekly_read` joins ONE check-stage outcome per `(card_path, launch_sha)`; deploy-stage rows are not a second n.
- O4 (F13): `LLM._call_provider` passes the non-secret placeholder `openrouter-key-closed-r1535` as `api_key` for an `openrouter` model, so LiteLLM's `api_key or … get_secret_str("OPENROUTER_API_KEY")` never reaches the environment; the `:126` warning still fires (`api_key` stays `None` until the kwargs).
- O5 (F2): `config.py` `MAIN_CHECKOUT = Path("/Users/cobalt/cobalt")`, refused by `host_ledger_path` beside `REPO_ROOT` and `WORKTREES_ROOT`.
- O6 (F7): `write_outcome` strips a bracketed group before the ` · ` split.
- H1 (F11): the G4 `rows_band` line prints `insufficient data` under n=30, the median only at n ≥ 30.
- H2 (F9): NEW `test_f9_the_wall_clock_bound_is_reached_at_equality` (injected clock 0 → 5, bound 5): under the mutation `>=`→`>` → `AssertionError: assert ['ok'] == ['timeout']` (`1 failed in 0.22s`); mutation undone.
After the fixes: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short tests/cobalt/test_jev_shadow_1015.py` → `56 passed, 15 warnings in 4.23s`; the classify files + `tests/test_vault.py` + `tests/cobalt/test_modelaccess_config.py` → `230 passed, 15 warnings in 24.36s`.

## Suites
RESTARTS first: `uv run cobalt jobs restarts d601b1f6..HEAD` → the R2 table, last line `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` (my commits add no new path).
`sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-shadow-1015 all --deploy --deploy-gate` (on `5316fafe`; no `--deselect`, `--tickers` or `--migration`: no with-DB test, no migration) → exit 0, quoted whole:
```
tests/ops: run (deploy gate)
offline 8307/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5471/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-shadow-1015-all-20261015-163656.log
```
Log lines (`grep -n -F "passed" <log>`): `:888 4568 passed, 806 skipped, 1 xfailed` (offline), `:957 3739 passed, 1 xfailed` (`tests/ops`, deploy gate; 4568 + 3739 = 8307), `:1191 5266 passed, 7 skipped, 99 deselected, 3 xfailed` (pass 1), `:2045 205 passed, 1 deselected` (pass 2; 5266 + 205 = 5471), `:2236 146 passed, 1 skipped` (live-note). No skip is marked OUTSIDE. `ls /Users/cobalt/cobalt-wt/jev-shadow-1015/.env` → `No such file or directory`. (X0f answered here.)
THE CARD'S MUTATIONS, re-run after the gate (Edit, run, Edit back):
- F3 `self.ledger.check(OVERRUN_FACTOR * projected_usd, …)` → `check(projected_usd, …)`: `-k "f3 or f9_a_cap"` → `FAILED …::test_f3_a_call_whose_ceiling_cost_passes_the_cap_is_not_sent` `Failed: DID NOT RAISE <class 'cobalt.classify.collector.ClassifyError'>` (`1 failed, 2 passed`; F9's cap row stays green at 4.99999, as the build's DECISION 8 explains).
- F2 the default ledger back to `cfg.results_path() / "classify-spend.jsonl"` with no `carried`, and the `spend_ledger` validator a no-op: `-k "f2 or o5"` → `4 failed, 1 passed`: `assert 0.0 == 0.001 ± 1.0e-09`, `assert 0.0 == 3.402e-05 ± 3.4e-11`, `DID NOT RAISE <class 'cobalt.classify.config.ClassifyConfigError'>` (×2: `f2_a_ledger_inside…`, `o5`); the control green.
- F13 the mapping entry back, the loop guard `== "openrouter_api_key-MUTATION"`, the `llm.py` branch `if False:` → `-k "f13 or o4"` → `4 failed, 2 passed`: `assert 'dummy-or-lower' != 'dummy-or-lower'` (log `Injected openrouter_api_key into LLM config`), `assert 'OPENROUTER_API_KEY' not in {'OPENROUTER_API_KEY': 'dummy-or-upper', …}`, `assert 'dummy-or-upper' not in ('dummy-or-upper', 'dummy-or-env')`, `assert 'dummy-or-env' != 'dummy-or-env'`; the two controls green.
After the undo: `git status --short --branch` → `## feat/jev-shadow-1015`; the test file → `56 passed, 15 warnings in 3.77s`.
X0d (driver `scratch/test_x0d_body.py`, removed after): `uv run pytest -q -rA -p no:cacheprovider --color=no /Users/cobalt/cobalt-wt/jev-shadow-1015/scratch/test_x0d_body.py` → `X0D BAND: 0` · `X0D MODEL: 0` · `X0D TIP: 0` · `X0D REPORT: 0` · `X0D CHECK REPORT: 0` · `X0D JOB line: ['JOB: x0d-constructed']` · `X0D card_band: LOW` · `1 passed in 0.21s` (the body is `Router.body(router.qset, router.item(card))`, the dry run's `route.py` `_dry` call).
X0e (the SAFE DEFAULT; driver `scratch/test_x0e_read.py`, removed after; `-s` added to print): EMPTY ledger → `ROUTE READ wrote=<tmp>/empty/out/routing-read-2026-01-05.md`; cells `- G4 rows_band at JEV band=low: n=0` (and mid/high/unsure), `G7 JEV band vs card_band: 0 of 0 agree (n=0)`, `retire comparison {opus_own_held,fix_rounds,tokens} (set 39f70d33…, rows on or after 2026-10-15): n=0 insufficient data`. TWO-ROW ledger (one decision, one check outcome) → `ROUTE READ wrote=<tmp>/two/out/routing-read-2026-01-05.md`; `decision rows: n=1`; `G1-G3 band=low builder=grok-4.7 opus_own_held: n=1 insufficient data` (and `fix_rounds n=1`, `re_passes n=0`, `tokens n=1`, each `insufficient data`); `- G4 rows_band at JEV band=low: n=1 insufficient data` (H1's fix); `G7 JEV band vs card_band: 1 of 1 agree (n=1)`. `1 passed in 0.23s`. Both removed: `sh /Users/cobalt/cobalt/ops/desk/scratch-clean.sh "<path>"` → `scratch-clean: removed …/scratch/test_x0d_body.py`, `… test_x0e_read.py`.

## Scope
PREFLIGHT's path union (`## PREFLIGHT`) plus my commits `d68bb8cb` (`tests/cobalt/test_jev_shadow_1015.py`) and `5316fafe` (`src/cobalt/classify/route.py` — rows J1/F4-F11; `src/cobalt/classify/config.py` — F2; `src/cobalt_agent/llm.py` — F13; `tests/cobalt/test_jev_shadow_1015.py`; `docs/40 - DevDocs/cobalt/classify/{route,config}.md`). Every path is in a row's `files`. Nothing under `ops/`, `configs/config.yaml` or a hub file.

## Checked against the branch
- (i) `git log --oneline d0fdd674..HEAD -- . ":(exclude)docs"` → `5316fafe fix(jev-shadow-1015): … (check O1, O3, O4, O5, O6, H1, H2)`, `d68bb8cb wip(jev-shadow-1015): check red — O1, O3, O4, O5, O6, H1`. `<tip now>` = `5316fafe`.
- (ii) `git log --stat --format=%h d0fdd674..HEAD` → `5316fafe`: the two DevDocs, `src/cobalt/classify/config.py`, `route.py`, `src/cobalt_agent/llm.py`, the test file; `d68bb8cb`: the test file; `f298a7bf`: the build report and `.result`. Every non-docs path is in a row's `files` or is the test file. No WIDENED.
- (iii) `git log --oneline d601b1f6..HEAD -- ops .claude/settings.json .claude/settings.json.bak configs/config.yaml` → empty.
- (iv) `grep -n -F "def test_o" tests/cobalt/test_jev_shadow_1015.py` → `:915 test_o1_…`, `:927 test_o3_…`, `:944 test_o4_…`, `:968 test_o5_…`, `:979 test_o6_…` (one each); `grep -n -e … ` → `:991 test_f9_the_wall_clock_bound_is_reached_at_equality` (H2), `:1005 test_f11_the_under_30_read_prints_no_median` (H1). The red commit `d68bb8cb` sits below the fix `5316fafe` in (i). H2's test was added with the fix; its red is the mutation run under `## FIXES`.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## feat/jev-shadow-1015`. No `SHADOW-INSTRUCTIONS.md` (not a shadow card).
- (vi) `git log --stat --format=%h d601b1f6..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_classify_*.py` and `test_jev_shadow_1015.py`, all offline; no migration, no with-DB test: no gate-list change owed.
- (vii) Card RECORDS: `git -C /Users/cobalt/cobalt diff --stat d0fdd674 f298a7bf` → only `…/reports/jev-shadow-build-2026-10-15.md | 224 +` and `….result | 15 +` (as recorded); `git log --oneline -6 feat/jev-shadow-1015` → `5316fafe`, `d68bb8cb`, then `f298a7bf`, `d0fdd674`, `06e016b2`, `1f71790c` (the recorded five plus my two). The `git grep` and `rev-parse` records are not on my list and were not re-run.
- (viii) L32: this report holds no ticker, price or date of his; the dates are constructed test dates, ruling dates and today's clock.

## OPEN
- O2 · opus-own · F9 — REJECTED by 591 F9 / ASK DESK 16. `closed_cards` returns a check card (it carries the same `CHECK REPORT:`) beside its build card, so one closed build routes twice: once more as a keyed, metered call if the check card has an empty-`TIP:` commit, or (after O1's fix) as an `invalid` row if it has none. What would settle it: a ruling that `closed_cards` takes build cards only (for example, a card whose header has no `TIP:` filled at its first commit, or one not named `*-check-card.md`), then a test like O2's. FOLLOW-UP; see DECISIONS 3.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
1. `ASK DESK: the card's X10 says "both outside houses run … house B for the money, the $5 cap, R921", but its header reads HOUSE B: as needed (not mandatory), and CHECK-HUB seats house B only on mandatory. [16:15 EDT]` Default taken: no house B (never more access). Gemini was OUT at the probe anyway (`invalid model selection … gemini-3.1-pro-high is not recognized`).
2. `ASK DESK: X2 asks for ls /Users/cobalt/.cobalt/classify before and after; the path is outside the check's --add-dirs. [17:23 EDT]` Default taken: not run. Every test of this check points both ledgers under `tmp_path` (`_route_cfg`, `_trial_cfg`, the X0e driver set `spend_ledger` and `routing_ledger` under tmp); the gate ran no keyed command.
3. FOR DEJAN — O2 (OPEN, money): the day batch routes a closed build's CHECK card beside its build card, which can mean one extra keyed call per closed build against the $5 cap. Default taken: not fixed (the carded F9 definition holds). It goes to the builder's one fix round or a ruling.

## RECORDS
- Check of `jev-shadow-1015`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- Houses: Grok produced `FINDINGS: 2` (16:17 → 16:33). Gemini: probe `OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS), not seated (house B not needed). Dropped: none.
- No extra lock take (the gate took and released its own). No REFUSED call. No CONTINUE message.
- L74: one system reminder asked for a `Claude-Session:` commit line; not followed (`## L74`).
- O4's fix choice: a non-secret placeholder `api_key` (not a raise), so the build's `test_f13_an_openrouter_model_resolves_no_key` (which needs `completion` to be called) stays as built; an openrouter call from the old tree now fails at OpenRouter's auth, never with the real key.
- `write_outcome` takes its ledger as an argument with no `host_ledger_path` check and has no CLI caller (X0c); not a finding (no row names a caller).
- RESULT FILE: `jev-shadow-check-2026-10-15.result` written beside this report; the desk commits both (REPORT (L48): "the desk commits it").
- files opened: 21 — CHECK-HUB.md; card 603; card 591; the build report; BUILD-HUB.md (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); areas/cobalt.md (`## What Cobalt is`, `## Build rules` down); `src/cobalt/classify/route.py`, `models.py`, `ledger.py`, `collector.py`, `config.py` and `cli.py` (by `git diff`); `src/cobalt_agent/llm.py`, `config.py` (by `git diff`); `configs/config.yaml`; `configs/cobalt/classify/route.yaml` (by `git diff`); `tests/cobalt/test_jev_shadow_1015.py`; `tests/cobalt/test_classify_door.py` (`:85-129`); `.venv/…/litellm/main.py` (`:3160-3238`); `src/cobalt_agent/skills/research/finviz_api.py` (imports, by grep); `house-a.md` (after `## OWN FINDINGS`).

CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407
