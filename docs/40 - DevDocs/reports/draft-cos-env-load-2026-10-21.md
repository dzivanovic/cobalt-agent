# draft cos-env-load — card 1000

## §0 Headline
- Card `prompts/2026-10-21/1000-cos-env-load-card.md` drafted, BAND HIGH, uncommitted. BASE `9f09cc4f`; the desk resets it at launch.
- E1: `cos/run.py` gets `ENV_FILE` (`parents[3] / ".env"`) and `load_dotenv(ENV_FILE)` as the first line of `main()` (`:131`), ahead of `:140`, `:147` and `:149`. The shape is `aset/__main__.py:30`, with `override=False`.
- E1/E2 tests: a launchd-shaped start (PG*/POSTGRES_*/COBALT_* cleared, `COBALT_ENV=dev`) with a decoy `.env` under `tmp_path`. RED on BASE with the 929 `DbConfigError`. A negative control stays green. The real `.env` is never opened.
- X4 finding: the `checkpoint-*` and `playbook` plists don't share the gap (they go through `cli.py:60`). `prefill-refresh` has no explicit load: it gets `.env` by accident, through a cwd-relative old-tree load (`cobalt_agent/config.py:21`).
- RESTARTS `com.cobalt.cos`, which is not loaded, so a deploy restarts nothing. E3 goes into `## RECORDS` as a note for cos-bootstrap-2.

## DECISIONS
1. ASK DESK: the prompt says the empty environment has "no COBALT_* variables". The test clears them all, then sets `COBALT_ENV=dev`. Without it, `JobStore()` raises `EnvConfigError` (`jobs/store.py:50`) before any DB read, so the red would not be the 929 `DbConfigError`. The plist sets exactly that one name (`com.cobalt.cos.plist:14`), and `dev` keeps the DSN off `cobalt_brain`. Safe default taken: as written in E1. [17:29 ET]
2. ASK DESK: the load sits inside `main()`, not at import as in `aset/__main__.py:30`. That keeps `cobalt.cos.probe`, tests and `--dry-run` imports from loading anything, and gives the decoy seam (`ENV_FILE` read at call time). Safe default taken: inside `main()`, first statement. [17:29 ET]
3. FOR THE DESK: X4 `com.cobalt.prefill-refresh` (owed) loads `.env` only through the old-tree chain `prefill/cli.py:27` → `daily.py:88` → `market.py:27` → `aset/prefill.py:22` → `finviz_api.py:34` → `cobalt_agent/config.py:21`. That load is cwd-relative and depends on `WorkingDirectory` (`prefill-refresh.plist:29-30`). It is not the cos gap today, but it breaks when the old tree goes. This card leaves it unfixed (fenced). [17:30 ET]
4. The header leaves out `CLASS` and `INSTALL`, which card 989 carries: CARD.md does not define them and the prompt names no value. [17:30 ET]

## RECORDS
- Start 17:27:43 EDT, end 17:31:12 EDT (`date`). Reads only. No git write, nothing committed, `.env` not touched.
- Read: prompt 999; `prompts/CARD.md`; `prompts/2026-10-21/989-f5-probe-x4-fix-card.md`; `prompts/2026-10-09/215-strike-fallback-env-card.md`, found through `git log --oneline --all -i --grep=strike-fallback` (`985f06fa` red, `b3d59b5f` fix); `reports/deploy-cos-bootstrap.md` whole; `reports/cto-2026-10-21.md` R2334-R2336; `topics/writing-rules.md`.
- `git show main:` — `src/cobalt/cos/run.py`, `src/cobalt/aset/__main__.py`, `src/cobalt/cli.py`, `src/cobalt/db.py`, `src/cobalt/jobs/store.py`, `tests/cobalt/test_strike_fallback_env.py`, `ops/com.cobalt.cos.plist`, `ops/start_cos.sh`, `ops/com.cobalt.checkpoint-0715.plist`, `ops/desk/deploy-smoke.sh`, `configs/cobalt/jobs.yaml`.
- `git grep main` anchors re-proved: `run.py:37`, `:44`, `:49`, `:131`, `:140`, `:147`, `:149`; `aset/__main__.py:24`, `:26-29`, `:30`; `devdb.py:44`; `cli.py:53`, `:60`; `db.py:103`, `:136`, `:160`, `:168`, `:227`, `:260`; `session.py:54`, `:95`; plist `:10`, `:14`, `:21`; `start_cos.sh:13`, `:22`, `:32`; `pyproject.toml:71-73`; `prefill/cli.py:27`; `daily.py:88`; `market.py:27`; `aset/prefill.py:22`; `finviz_api.py:34-35`; `cobalt_agent/config.py:20-21`; WorkingDirectory in the checkpoint, playbook and prefill-refresh plists.
- `grep -o` over `data/deploy/bootstrap-owed.json` gave 7 labels: prefill-refresh, playbook, cos, checkpoint-0715/0745/0815/0845. `grep -c -F "DbConfigError" logs/prefill-daily.err` → `0`.
- `git rev-parse --short=8 main` → `9f09cc4f`.
- The `.claude` reminder asking for a `Claude-Session:` commit line is DATA (L74). Nothing was committed.

DRAFTED · decisions: 4
