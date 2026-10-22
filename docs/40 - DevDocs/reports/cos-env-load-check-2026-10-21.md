# cos-env-load — check report (2026-10-21)

## §0 Headline
- The build is right: `run.py` loads `ENV_FILE` as `main`'s first statement, with `override` left `False`. Grok (house A, `FINDINGS: 1`) and I wrote 5 findings, and 2 held.
- O1 and O2 held: no test pinned that the load comes before the registry read, or that importing loads nothing. Two new pins, each red under its mutation, are committed in `5b813fa4`, with no `src/` change.
- Gate green: offline 9076/0 · with-DB 5922/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed.
- One decision (O3/X6): RESTARTS is `com.cobalt.cos com.cobalt.radar`, not cos only. X4 (prefill-refresh) is out of scope.

## L74
The session's attribution reminder asked for a `Claude-Session:` line on commits. Recorded once and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1000-cos-env-load-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1000-cos-env-load-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1000-cos-env-load-card.md" · 0 · 7b407c4c2a2bf495835d8ae9776e6b9c4c584798
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1000-cos-env-load-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …/cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …/cto-2026-09-24.md` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, whole:
```
clock · date · 0 · Wed Oct 21 18:56:59 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-env-load
head · git log --oneline -1; git log --stat --format=%h 9293c759..HEAD · 0 · (6 lines)
    72094446 docs(cos-env-load): build report — 9293c759
    72094446
    
     .../reports/cos-env-load-build-2026-10-21.md       | 214 +++++++++++++++++++++
     .../reports/cos-env-load-build-2026-10-21.result   |  15 ++
     2 files changed, 229 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-env-load/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-env-load/docs/40 - DevDocs/reports/cos-env-load-build-2026-10-21.md" · 0 · BUILT · job: cos-env-load · tip: 9293c759 | on 7f89b98f | migration: none | offline 4948/0 | with-DB 5920/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.cos com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 187139
range · git log --oneline 7f89b98f..9293c759 · 0 · (3 lines)
    9293c759 fix(cos-env-load): the E1/E2 tests restore the unpatched db factory under dev_db_tx (W red, G1 guard)
    45bc45cb fix(cos-env-load): com.cobalt.cos loads the repo env file at the top of main (E1, E2, D0; L1, L28, L32)
    6f92bd6c wip(cos-env-load): red — E1, E2 tests on BASE
PREFLIGHT OK
```
THE RANGE: `git log --stat --format=%h 7f89b98f..9293c759` → `9293c759` `tests/cobalt/test_cos_env_load.py | 11 ++++++++++-` · `45bc45cb` `docs/40 - DevDocs/cobalt/cos/README.md | 3 +++`, `src/cobalt/cos/run.py | 10 ++++++++++` · `6f92bd6c` `tests/cobalt/test_cos_env_load.py | 119 +++…`. Path union: `src/cobalt/cos/run.py`, `tests/cobalt/test_cos_env_load.py`, `docs/40 - DevDocs/cobalt/cos/README.md`.
Not a "DB: none" card (no `DB:` header line).
`ls <S>` → `No such file or directory` (fresh).
THE HOUSE PROBES: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → exit 0:
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line → Sol not probed. `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.
PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` proven here; the rest at first use.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, whole:
```
26 …/cos-env-load-check/STAGED-CARD
8077 …/cos-env-load-check/diff.md
16068 …/cos-env-load-check/files/1000-cos-env-load-card.md
31557 …/cos-env-load-check/files/cos-env-load-build-2026-10-21.md
8922 …/cos-env-load-check/files/wt/docs/40 - DevDocs/cobalt/cos/README.md
7077 …/cos-env-load-check/files/wt/src/cobalt/cos/run.py
4440 …/cos-env-load-check/files/wt/tests/cobalt/test_cos_env_load.py
386 …/cos-env-load-check/rulings.md
STAGED 8 files · 76553 bytes · commits 3
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920`.) commits 3 = PREFLIGHT's range count.
`stage-copy.sh`, each one call → `COPIED <bytes> <dest>`: `files/deploy-cos-bootstrap.md` 26437 · `files/cos-gate-run-2026-10-20.md` 8549 · `files/215-strike-fallback-env-card.md` 9533 · `files/wt/src/cobalt/aset/__main__.py` 2728 · `files/wt/src/cobalt/cli.py` 27306 · `files/wt/src/cobalt/db.py` 14043 · `files/wt/src/cobalt/jobs/store.py` 13512 · `files/wt/src/cobalt/env.py` 3825 · `files/wt/ops/com.cobalt.cos.plist` 1335 · `files/wt/ops/start_cos.sh` 1162 · `files/wt/tests/cobalt/test_strike_fallback_env.py` 3003 · `files/wt/tests/conftest.py` 3216 · `files/wt/src/cobalt/cos/session.py` 14955 · `files/wt/tests/cobalt/conftest.py` 18003 · `files/wt/ops/com.cobalt.checkpoint-0715.plist` 2828 · `files/wt/ops/com.cobalt.playbook.plist` 2165 · `files/wt/ops/com.cobalt.prefill-refresh.plist` 16276 · `files/wt/src/cobalt/prefill/cli.py` 4143 · `files/wt/configs/cobalt/jobs.yaml` 27165 · `files/wt/src/cobalt/cos/cli.py` 1643 · `files/wt/pyproject.toml` 2945.
`stage-copy.sh /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json …` → exit 1 `REFUSED: the source is not under a job worktree or the main tree's docs/: /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` (an extra copy I added for X4; the card's RECORDS carry its `grep -o` reading; `## RECORDS`).
`<S>/HOUSE-INSTRUCTIONS.md` written (17745 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.
House start: `date` → `Wed Oct 21 18:59:10 EDT 2026`; gates R17, R19 → one row each (as AUTHORIZATION); `ls -la <S>` → `diff.md`, `files`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`, `STAGED-CARD`; `cd <AGY>`; Grok started (`grok -m grok-4.7 --sandbox cobalt-job --allow "Write(…/tribunal-bars-0920/**)" -p "…"`, the GROK line as written, `run_in_background`, `timeout` 2700000); `cd <WT>`; `git status --short --branch` → `## ops/cos-env-load`. No house B (not needed).

## OWN FINDINGS
Read: the card; the diff `7f89b98f..9293c759` (`git diff 7f89b98f 9293c759 -- src tests`); `src/cobalt/cos/run.py` whole at the tip; `src/cobalt/cos/session.py:90-224`; `tests/cobalt/conftest.py:100-359`; `tests/cobalt/test_db_only_selection.py:1-30`, `:205-464`; the build report whole; greps below.

FINDING O1
ROW: E1 (X1)
CLAIM: The clause "before `load_job_registry().spec(JOB_LABEL)`" (tip `src/cobalt/cos/run.py:150`) is pinned by no test: the only order pin is the recorder at `refuse_if_agent_alive` (`tests/cobalt/test_cos_env_load.py:72-73`), so a mutation that moves `load_dotenv(ENV_FILE)` from `run.py:141` to just after `spec = load_job_registry().spec(JOB_LABEL)` (`:150`) keeps all four tests green.
RUN: COMMAND, under that one mutation made with the Edit tool and undone after: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_env_load.py`
EXPECT: `4 passed` under the mutation. Fix: a test in `tests/cobalt/test_cos_env_load.py` whose recorder at `cobalt.jobs.config.load_job_registry` keeps the three DB names at call time; red under the mutation, green at the tip.

FINDING O2
ROW: E1
CLAIM: The clause "Not at import time: importing `cobalt.cos.run` … loads nothing" is pinned by no test: a mutation that adds a module-level `load_dotenv(ENV_FILE)` after `ENV_FILE = …` (`src/cobalt/cos/run.py:40`) keeps all four tests green (the worktree holds no `.env`, and the tests repoint `ENV_FILE` before `main`).
RUN: COMMAND, under that one mutation made with the Edit tool and undone after: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_env_load.py`
EXPECT: `4 passed` under the mutation. Fix: a test in `tests/cobalt/test_cos_env_load.py` that reads `run.py`'s syntax tree (by content, no hash) and finds `load_dotenv` called once, as the first statement of `main`, and at no module level; red under the mutation, green at the tip.

FINDING O3
ROW: X6 (R1)
CLAIM: RESTARTS is not `com.cobalt.cos` only: the tool's rule `static import reach` adds `com.cobalt.radar` for `src/cobalt/cos/run.py` (through `src/cobalt/cos/cli.py:18` `from .run import main`), and radar is `enabled: true` (`configs/cobalt/jobs.yaml:193-197`, build report `## RESTARTS`), so a deploy of this card restarts radar by the tool's rule although cos itself is not loaded.
RUN: COMMAND `uv run cobalt jobs restarts 7f89b98f..9293c759`
EXPECT: last line `RESTARTS: com.cobalt.cos com.cobalt.radar`.

FINDING O4
ROW: X4
CLAIM: `com.cobalt.prefill-refresh` (owed, `ops/com.cobalt.prefill-refresh.plist:25-27` `uv run prefill refresh`) enters `src/cobalt/prefill/cli.py`, which holds no `load_dotenv`; it gets the Postgres names only from the cwd-relative `load_dotenv()` at `src/cobalt_agent/config.py:21`, deep in its import chain. The checkpoint plists (`ops/com.cobalt.checkpoint-0715.plist:25-28`, and `-0745`, `-0815`, `-0845` at the same lines) and `ops/com.cobalt.playbook.plist:28-31` run `uv run cobalt …`, which loads at `src/cobalt/cli.py:60`: no gap.
RUN: COMMAND `grep -c -F "load_dotenv" src/cobalt/prefill/cli.py`
EXPECT: `0`.

X2 (no finding): `grep -rn load_dotenv src` → the one call `src/cobalt/cos/run.py:141` `load_dotenv(ENV_FILE)`, no `override=` (default `False`); no cwd-relative call in `cos/`. Pinned by `test_e2_the_environment_wins_over_the_file` (the build's M3).
X3 (no finding): the one spawn path of the resident: `src/cobalt/cos/session.py:295` `build_options(...)` → `:108` `"env": child_env()` → `:95` keeps only `ALLOWED_ENV` (`:54` `PATH`, `HOME`, `USER`, `LANG`, `COBALT_ENV`); `:305` `with _scrubbed_environ(options["env"])` (`:118-127`: `os.environ` is exactly that dict for the spawn) around `_SdkClient.connect` (`:187-189`) → `ClaudeSDKClient` (`:219`). The probe's spawn, `src/cobalt/cos/probe.py:286` and `:501` `_scrubbed_environ(_probe_env(extra))`, is not the resident. The loaded names do not reach the SDK child by this path.
X5 (no finding): the tests write only a decoy under `tmp_path` (`test_cos_env_load.py` `_launchd_start`); `test_e1_the_env_file_is_the_repo_one` compares paths and stats `pyproject.toml`, never `.env`.
ASK DESK 1 of the build (the `FACTORY = db.connect` restore past `dev_db_tx`), read: while the module's `psycopg.connect` is the raising recorder (`test_cos_env_load.py:78`), `db._open` reaches no socket; no finding written.

## Findings
Grok's completion notice at `date` → `Wed Oct 21 19:12:51 EDT 2026`; `ls -la <S>` → `house-a.md` 2187 bytes (19:12), written by Grok; Grok's stdout: the path `…/cos-env-load-check/house-a.md`, `[exited with code 0]`. Last line of `house-a.md`: `FINDINGS: 1`. House B: none (not needed).
`grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: \`grep -n -E "load_dotenv|…" src/cobalt/cli.py src/cobalt/prefill/cli.py ops/com.cobalt.prefill-refresh.plist ops/com.cobalt.checkpoint-0715.plist ops/com.cobalt.playbook.plist pyproject.toml\`` — one command line with an allowed beginning: kept.

| id | house | row | claim | run |
|---|---|---|---|---|
| G1 | A Grok | X4 | `com.cobalt.prefill-refresh` starts under launchd with no Postgres name and no `load_dotenv` in `src/cobalt/prefill/cli.py`; checkpoint and playbook go through `cobalt.cli:main`, which loads at `cli.py:60`. | COMMAND |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | mutation by Edit: `load_dotenv(ENV_FILE)` moved from `main`'s top to just after `spec = load_job_registry().spec(JOB_LABEL)`; `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_env_load.py` | `....` `4 passed in 0.07s` | HELD — the row's clause "before `load_job_registry().spec(JOB_LABEL)`" is unpinned |
| O2 | own | mutation by Edit: a module-level `load_dotenv(ENV_FILE)` added after `ENV_FILE = …`; the same command (O1's new test now in the file) | `.....` `5 passed in 0.09s` | HELD — the clause "Not at import time" is unpinned |
| O3 | own | `uv run cobalt jobs restarts 7f89b98f..9293c759` | `docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-` · `src/cobalt/cos/run.py	M	static import reach	com.cobalt.cos,com.cobalt.radar` · `tests/cobalt/test_cos_env_load.py	A	test/documentation; no resident	-` · `RESTARTS: com.cobalt.cos com.cobalt.radar` | REJECTED — R1: "RUN — asserts nothing … the tool's last line is the record"; the fence holds `configs/cobalt/jobs.yaml`. OPEN, `## DECISIONS` |
| O4 | own | `grep -c -F "load_dotenv" src/cobalt/prefill/cli.py` | `0` | REJECTED — NOT IN THIS JOB: "The CHECK ASK X4 finding (`prefill-refresh`'s accidental load): a finding only, never fixed here." → OUT OF SCOPE |
| G1 | house A Grok | `grep -n -E "load_dotenv\|<string>prefill</string>\|…\|^prefill = " src/cobalt/cli.py src/cobalt/prefill/cli.py ops/com.cobalt.prefill-refresh.plist ops/com.cobalt.checkpoint-0715.plist ops/com.cobalt.playbook.plist pyproject.toml` (as Grok wrote it) | exactly Grok's 13 EXPECT lines: `src/cobalt/cli.py:53`, `:58`, `:60`; `ops/com.cobalt.prefill-refresh.plist:26`, `:27`, `:29`; `ops/com.cobalt.checkpoint-0715.plist:27`, `:32`; `ops/com.cobalt.playbook.plist:30`, `:31`, `:33`; `pyproject.toml:72`, `:73`; no `src/cobalt/prefill/cli.py` line | REJECTED — the same fence line as O4 → OUT OF SCOPE |

The red of the held tests (each under its mutation, then the mutation undone):
- O1 → `tests/cobalt/test_cos_env_load.py::test_e1_the_load_runs_before_the_registry_read`, under O1's mutation: `1 failed in 0.07s`, first failing line `E       AssertionError: assert {'COBALT_DB_P...S_HOST': None} == {'COBALT_DB_P...host.invalid'}` (`{'POSTGRES_HOST': None} != {'POSTGRES_HOST': 'decoy-host.invalid'}`, the same for the two credentials), `tests/cobalt/test_cos_env_load.py:117`.
- O2 → `tests/cobalt/test_cos_env_load.py::test_e1_the_load_is_main_first_statement_and_never_at_import`, under O2's mutation: `1 failed in 0.05s`, first failing line `E       AssertionError: assert [Call(func=Na... keywords=[])] == []` (`Left contains one more item: Call(func=Name(id='load_dotenv', ctx=Load()), args=[Name(id='ENV_FILE', ctx=Load())], keywords=[])`), `:142`.
After each undo `git diff --stat` → `tests/cobalt/test_cos_env_load.py` only (no `src/` change). Then `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_env_load.py tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_probe.py tests/cobalt/test_strike_fallback_env.py tests/cobalt/test_cos_listener.py tests/cobalt/test_db_only_selection.py` → `104 passed, 2 skipped, 12 warnings in 7.73s` (skips: `test_db_only_selection.py:617`, `:643` `Postgres env settings not available`).
Commit `5b813fa4 wip(cos-env-load): check red — O1, O2` (`tests/cobalt/test_cos_env_load.py`, 49 insertions). The tests are red only under the mutation: the tip's code is right, and the defect was the missing pin.

## FIXES
- O1: FIXED — the pin `test_e1_the_load_runs_before_the_registry_read` (in `5b813fa4`); no `src/` change. Its dated docs line: `docs/40 - DevDocs/cobalt/cos/README.md` `## 2026-10-21 — cos-env-load (check)`, commit `773fe012 fix(cos-env-load): the load pinned before the registry read and never at import (check O1, O2)`.
- O2: FIXED — the pin `test_e1_the_load_is_main_first_statement_and_never_at_import` (in `5b813fa4`); the same docs commit `773fe012`.

## Suites
RESTARTS first: `uv run cobalt jobs restarts 7f89b98f..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-env-load-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-env-load-build-2026-10-21.result	A	DOCS	-
src/cobalt/cos/run.py	M	static import reach	com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_cos_env_load.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row.
W, one call on HEAD `773fe012` (code tip `5b813fa4`): `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-env-load all --deploy --deploy-gate` (no `--deselect`, no `--tickers`, no `--migration`: the new tests are offline and write no row) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9076/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5922/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-env-load-all-20261021-191428.log
```
From the log (`grep -n -F " passed" <log>`): `:956` `4950 passed, 878 skipped, 4 xfailed, 36 warnings in 723.68s` (tests/cobalt + tests/taxonomy offline: the build's 4948 + my 2) · `:1031` `4126 passed, 1 xfailed, 16 warnings in 898.21s` (tests/ops, deploy gate; 4950 + 4126 = 9076) · `:1275` `5678 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 893.78s` (pass 1) · `:2257` `244 passed, 1 deselected, 5 warnings in 245.40s` (pass 2; 5678 + 244 = 5922) · `:2458` `148 passed, 1 skipped, 15 warnings in 26.41s` (live-note; the skip is `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`). `grep -n -F "OUTSIDE" <log>` → nothing. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1048`) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2331`).
**offline 9076/0 · with-DB 5922/0 · live-note 148/0 · cobalt_dev: 0013 — F2 = F0 · .env: removed** (`ls /Users/cobalt/cobalt-wt/cos-env-load/.env` → `No such file or directory`) · **RESTARTS: com.cobalt.cos com.cobalt.radar**.

## Scope
PREFLIGHT's path union (`src/cobalt/cos/run.py`, `tests/cobalt/test_cos_env_load.py`, `docs/40 - DevDocs/cobalt/cos/README.md`) plus my commits (`tests/cobalt/test_cos_env_load.py`, `docs/40 - DevDocs/cobalt/cos/README.md`): every path is in the `files` of E1, E2 or D0. Nothing inside `## NOT IN THIS JOB` ((iii) empty).

## Checked against the branch
(i) `git log --oneline 9293c759..HEAD -- . ":(exclude)docs"` → `5b813fa4 wip(cos-env-load): check red — O1, O2` → `<tip now>` = `5b813fa4` (my newest code commit; `773fe012` above it is docs only).
(ii) `git log --stat --format=%h 9293c759..HEAD` → `773fe012` `docs/40 - DevDocs/cobalt/cos/README.md | 3 +++` · `5b813fa4` `tests/cobalt/test_cos_env_load.py | 49 +++` · `72094446` the build report and its `.result` (docs). Non-docs paths: `tests/cobalt/test_cos_env_load.py` only, a row's file. No WIDENED.
(iii) `git log --oneline 7f89b98f..HEAD -- ops/start_cos.sh ops/com.cobalt.cos.plist configs/cobalt/jobs.yaml src/cobalt/db.py src/cobalt/env.py src/cobalt/jobs src/cobalt/aset/__main__.py src/cobalt/cli.py src/cobalt/devdb.py src/cobalt/prefill/cli.py src/cobalt_agent src/cobalt/cos/session.py src/cobalt/cos/cli.py src/cobalt/cos/probe.py ops` → empty.
(iv) `grep -n -F "def test_e1_the_load_runs_before_the_registry_read" tests/cobalt/test_cos_env_load.py` → `100:` (O1); `grep -n -F "def test_e1_the_load_is_main_first_statement_and_never_at_import" tests/cobalt/test_cos_env_load.py` → `124:` (O2). Both in `5b813fa4 wip(cos-env-load): check red`. Its `fix(cos-env-load):` commit `773fe012` sits above it, but it is docs only, so (i) (docs excluded) does not show it: `git log --stat` (ii) shows the order `773fe012` over `5b813fa4`. No `src/` fix was owed: the tip's code already does what the pins ask.
(vi) `git log --stat --format=%h 7f89b98f..HEAD -- src/cobalt/db_migrations tests/cobalt` → `5b813fa4`, `9293c759`, `6f92bd6c`, each `tests/cobalt/test_cos_env_load.py` only; no migration, and no with-DB test that needs a level above `0013` (the file is offline: `psycopg.connect` is a raising recorder). Gate lists not owed.
(vii) The card's `## RECORDS` commands: `grep -c -F "DbConfigError" /Users/cobalt/cobalt/logs/prefill-daily.err` → `0` (as recorded) · `ls /Users/cobalt/cobalt/logs/cos.err` → `/Users/cobalt/cobalt/logs/cos.err` (listed, as E3 records) · `grep -o -F "com.cobalt." /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` → 7 hits (the record names 7 labels) · `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` → `1` · `grep -n -F "imports: [cobalt.cos.run]" configs/cobalt/jobs.yaml` → `226:    imports: [cobalt.cos.run]`. The `rev-parse` and `launchctl print` of the records are not on my list: not run.
(viii) L32: this report holds the decoy values only (`decoy-host.invalid`, `decoy_user`, `decoy-pass`, `5999`), all constructed; the `F0` values come from the build report and are fingerprints, not trader values.
(v) `ls /Users/cobalt/cobalt-wt/cos-env-load/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cos-env-load` alone.

## OPEN
- O3 (REJECTED — R1): RESTARTS is `com.cobalt.cos com.cobalt.radar`, not cos only (X6). The rule is `static import reach`. It would be settled by the desk's call on whether a deploy of this card restarts `com.cobalt.radar` (`## DECISIONS` 1). `configs/cobalt/jobs.yaml` is fenced, so no fix here.
- OUT OF SCOPE (not open): O4 and G1 (X4, `com.cobalt.prefill-refresh` gets the Postgres names only through the cwd-relative `src/cobalt_agent/config.py:21` load). The fence names it a finding only.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
1. O3 / X6 (outside the rows): the RESTARTS tool says `com.cobalt.cos com.cobalt.radar`. The build's DECISION R1 said the same. `com.cobalt.radar` is in the set because the `cobalt` CLI statically reaches `src/cobalt/cos/cli.py:18` `from .run import main` (a function-local import). The card's header and X6 expected cos only and "a deploy restarts nothing". Default taken: the tool's line is the record and the stop line carries it, so a deploy of this card restarts `com.cobalt.radar` by the tool's rule unless the desk rules otherwise. Nothing is changed (`jobs.yaml` is fenced).

## RECORDS
- Session id: `0a2fc9ad-7b1c-4169-b398-f0dbe94e3b72`; job directory `/Users/cobalt/.claude/jobs/0a2fc9ad`. `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 0a2fc9ad` → `context 189692 of 400000 — ok`.
- REFUSED, not needed: `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json …` — `REFUSED: the source is not under a job worktree or the main tree's docs/: /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` (an extra copy for X4, beyond the files `## 1` (3) names).
- Houses: house A Grok `FINDINGS: 1`; house B none (card `HOUSE B: as needed`, not needed). Gemini was UP at the probe and was not seated. No house produced nothing; no finding was dropped.
- The judgment of the build's ASK DESK 1 (`FACTORY = db.connect` restored past `dev_db_tx`): read, and no finding written. The with-DB pass ran the module green (`with-DB 5922/0`, with no G1 guard trip), and `psycopg.connect` stays the module's raising recorder.
- No extra lock take: `gate.sh` took and released the one lock (`lock: waited 0 min`, `.env: removed`).
- Read order: I opened `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down) after `## 4`, not before `## 2`. It holds nothing that bears on this card's rows.
- The report and its `.result` are on `main` under `docs/40 - DevDocs/reports/`. My git strings commit only in this worktree, so the desk commits both (REPORT: "the desk commits it").
- files opened: 14 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); the build report; the house-probe output; `src/cobalt/cos/run.py`; `docs/40 - DevDocs/cobalt/cos/README.md`; `tests/cobalt/conftest.py`; `tests/cobalt/test_db_only_selection.py`; `src/cobalt/cos/session.py`; Grok's stdout; `<S>/house-a.md`; the gate's output; `areas/cobalt.md`.
- Check of `cos-env-load`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-env-load · pass: 1 · tip: 5b813fa4 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9076/0 · with-DB 5922/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189692
