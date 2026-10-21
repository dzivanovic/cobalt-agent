# cobalt.cos — the chief of staff (F20)

## 2026-10-18 — f20-cos-1018
Built by card 730 from `docs/30 - Design/F20-FINAL-2026-10-11.md` (approved R1055; subscription only, R1112). One resident session he talks to in his Mattermost DM. `com.cobalt.cos` is registered `enabled: false` and its bootstrap is deferred: nothing runs until the deploy's D14 checklist, T10 and X1 (the build report's `BOOTSTRAP:` block).

### Modules
| file | what |
|---|---|
| `listener.py` | Deterministic DM reader (L2), no LLM in the watch loop. Per post: the bot's own posts are skipped; the kill phrase is matched FIRST (`killswitch.matches_kill_phrase`) → `killswitch.engage`, no turn row, no session; every other post (an "approve …" text included) is one `cobalt_cos_turns` row inserted `pending` before the session, then `running` → `done` / `failed`. There is no resume path: the switch stops this resident, so nothing here hears `COBALT RESUME` (F-31, T7'). |
| `session.py` | The Agent SDK wrapper; the SDK is imported only inside `sdk_client_factory`. |
| `tools.py` | The in-process tool server: `cards.open`, `radar.pool`, `jobs.status`, `hitl.list`, `agents.list` (read), `request_action`, `draft_agent` (request). No approve, decide or execute tool. Every tool returns text; a refusal is a `refused: …` result. |
| `store.py` | `cobalt_cos_sessions`, `cobalt_cos_turns` (USER side, `migrations/0001_cobalt_cos.sql`). `message_ref` is UNIQUE (T11). |
| `run.py` | The resident loop: each iteration `JobStore.beat` → listener poll → one executor claim → sweeper → outcome report. No `_Beater`, so a hung poll goes ZOMBIE (T12). Refuses to start while the `com.cobalt.agent` pidfile is alive (F-14). |
| `cli.py` | `cobalt cos run [--dry-run]`. |

### The session class (FINAL §4)
- Allowed: the seven tools above (`mcp__cobalt__<name>`); built-in base set empty (`tools=[]`); every built-in also disallowed (Bash, Write, Edit, NotebookEdit, WebFetch, WebSearch, Task, Agent, Read, Grep, Glob, …).
- `setting_sources=[]`, `strict_mcp_config=True` (spike D4). Mode `dontAsk`, never `bypassPermissions` (L55). No hook, no `can_use_tool` (C7, U1).
- Child env: exactly `PATH`, `HOME`, `USER`, `LANG`, `COBALT_ENV`. The SDK merges the parent's `os.environ`, so the spawn runs with `os.environ` replaced by that set and restored after (L41).
- cwd: `data/cos/scratch`. Model: `configs/cobalt/agents/cos.yaml` (Sonnet 5.5, UNMEASURED, X17).
- Fails on `is_error` or a `terminal_reason` other than `completed`, never on subtype alone (D5); Cobalt counts rounds and kills the CLI tree at `cos.max_turns`; `asyncio.wait_for(cos.turn_timeout_s)`; no result → failed; every failure DMs; resume by stored id, a failed resume opens a fresh session and DMs.

### Tables
`cobalt_cos_sessions` (channel, agent_id, session_id, started_at, rotated_at, state active/rotated/failed) · `cobalt_cos_turns` (message_ref UNIQUE, state pending/running/done/failed, started_at, finished_at, num_turns, result_subtype, is_error, terminal_reason, error).

### Tunables
`cos.max_turns` 30, `cos.turn_timeout_s` 900 (kit values, UNVERIFIED, X3/X14), `cos.poll_interval_s` and `cos.session_rotate_at` null (no value set; readers raise).

### Laws
L2 (deterministic listener), L3 (one listener: refuses while the old agent lives), L18 (a turn row per post, heartbeat from the loop), L37 (no approve verb; a DM text is never an approval), L41 (no credential in the child env), L55 (never `bypassPermissions`).

Tests: `test_cos_offline.py`, `test_cos_listener.py`, `test_cos_registry.py`, `test_cos_probes.py`, `test_cos_db.py` (with-DB).

## 2026-10-18 — f20-cos-1018 (check)
`session.py`: the open (`connect`) runs under `cos.turn_timeout_s` like the turn; a tool-result message is not a round; a max-turns stop keeps the partial reply. `listener.py`: a failed turn posts its partial reply; a raising turn ends its row `failed`; after the kill phrase no later post of the batch opens a session. `run.py`: the scratch cwd is emptied at start. Check O1–O6, G2–G4.

## 2026-10-18 — f20-cos-1018 (fix round W)
`run.py`: a failed run's `mark_finished` passes `result` as `job_run`'s does, so the resident's start and finish rows equal the wrapper's by field (G7; no `_Beater`, `jobs/wrapper.py` unchanged). The max-turns kill is the tree kill (`_kill_tree`: the CLI and every descendant; a `killpg` would hit the resident's own group), pinned by a real three-process stub (G5). `cobalt cos run` without `--dry-run` starts the resident (G6, pinned on fakes).

## 2026-10-18 — f20-cos-1018 (check r2)
`session.py`: `_SdkClient.connect` opens the CLI in a new session (the SDK's `anyio.open_process` wrapped for the open only), so the CLI leads its own process group; `_kill_tree` walks the tree, then `killpg`s that group, so a descendant reparented out of the tree when its parent exited dies too. The resident's own group is never signalled. Check r2 O1.

## 2026-10-19 — cos-probe-1019
NEW `probe.py`, mounted by `cli.py` as `cobalt cos probe <item>` (card 877): one live first-gate item, X2, X10, X11, X12, X3, X14 or X17 (FINAL `## First-gate experiments`), on the resident's own `CosSession` and `sdk_client_factory`. One stdout line, `PROBE <item> OK|FAIL <clause>`, exit 0 / 1; a clause holds names, counts and reasons only. The boundary: a `tempfile.mkdtemp(prefix="cos-probe-")` scratch (`home/` = the spawn's HOME, `home/work/` = cwd; refused under the real HOME or the repo; removed after); `os.environ` = the `child_env` names with the scratch HOME through `_scrubbed_environ` (X12 adds two constructed dummies); `notify` an in-memory list, `tool_call` a constructed stub (no DM, no store, no row); refused under `COBALT_ENV=production`; `claude auth status` (exit code only) before any spawn. Tests: `test_cos_probe.py` (stubs only, no `claude` spawned).

## 2026-10-19 — cos-probe-1019 (check)
`probe.py`: X2 / X10 FAIL when the stream holds no init message (a session that never ran proves no refusal); the resident's `cobalt.cos.session` log is disabled for the probe's run (a failed turn's reason carries exception text; the clause keeps the cut reason); the printed clause is folded to one line. Check O1, O2, O3, A2.

## 2026-10-20 — cos-probe-fr1 (check)
`probe.py`: `claude auth status` and `ps` run with `cwd` = the scratch `home/work`, never the repo's cwd; X14 FAILs when any DM's measured `num_turns` passes `cos.max_turns`. Check G2, G5.

## 2026-10-20 — cos-probe-fr2
`probe.py` (card 918, R2177 option A): the probe runs under the REAL HOME (the parent's `child_env` HOME; no HOME, or a HOME that is not a directory, is refused before any spawn), because a scratch HOME holds no login and the live resident runs under his. The scratch is `<root>/work/` (the session cwd, the only place the session may write), with the canary, the planted server's stub and marker in `<root>`, outside the cwd. The plant for X2 / X10 / X11 is a project-scope `<root>/work/.mcp.json` naming `browser`; X2 / X10's written-file check counts only the cwd entries the turn added. The auth check stays first, in the scratch cwd; it keeps the exit code and the quote `loggedIn=<v> authMethod=<v>` (any other key dropped in memory), printed as one stderr line `AUTH exit <n> · <quote>` on every run and carried in the FAIL clause `under the real HOME (<quote>)`. The probe's code opens no file under the real HOME; the CLI keeps its own state there (a project entry per scratch cwd in its state file, a transcript per session under `~/.claude/`), uncleaned, at most 67 sessions over the seven gate items, each keyed to a `cos-probe-` cwd. Tests: `test_cos_probe.py` (H1–H4).

## 2026-10-20 — cos-probe-fr2 (check)
`probe.py`: an auth-quote value must match `[a-z0-9._-]+` whole (a trailing newline is `unread`); X2 / X10 count a write over the planted `.mcp.json` as a written file (the before-set holds each entry's bytes); `_x11`'s docstring names the plant project-scope. Check O1, O2, O3.

## 2026-10-21 — cos-env-load
`run.py` (card 1000): card 929's launchd start died twice on `DbConfigError: Missing Postgres settings for the APP credential` at `store.ensure_schema()`: the plist hands the process only `PATH` and `COBALT_ENV`, `start_cos.sh` exports no Postgres setting, and nothing in `cos` loaded `.env`. NEW module constant `ENV_FILE` (the repo root's `.env`, beside `SCRATCH_DIR`); `main()` calls `load_dotenv(ENV_FILE)` as its first statement, before the registry read, `refuse_if_agent_alive` and the first store, as `aset/__main__.py` does. `override` stays `False`: a name already in the environment wins. The load runs in `main`, not at import (importing `cobalt.cos.run` loads nothing); with no file and no environment the start still fails loud. `ops/start_cos.sh` and the plist are unchanged. Tests: `test_cos_env_load.py` (E1, E2; a decoy `.env` under `tmp_path`, the real one never opened).

## 2026-10-21 — cos-env-load (check)
`test_cos_env_load.py`: two more pins on `run.py`'s load, no code change. The load runs before `load_job_registry()` (a recorder at the registry read sees the decoy names), and `load_dotenv` is called once, as `main`'s first statement and at no module level (read from the syntax tree). Check O1, O2.
