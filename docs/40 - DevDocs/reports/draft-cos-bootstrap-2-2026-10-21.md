## §0 Headline
- Card `prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md` drafted: bootstrap-only, `com.cobalt.cos · add`, the 14 GATE RESULT lines of 929 kept, each naming `com.cobalt.cos`.
- Marker 1 now reads `data/cos/scratch` (made at `run.py:106`, absent today); no marker reads the old logs.
- Smoke (s) pins `Traceback` and `DbConfigError: Missing Postgres settings` at 929's `2` each; the four absence counts stay `0`. No curl row.
- Nothing committed. 4 decisions, defaults taken.

## DECISIONS
1. ASK DESK: the ruling's two forms for marker 1 cannot be written in a mapped shape. `deploy-smoke.sh` has no time filter. A fresh log path needs a plist change, and a good start writes no cos-only log line. Default: marker 1 is `ls /Users/cobalt/cobalt/data/cos/scratch` · before `No such file or directory` · after listed. The scratch dir is made only after the `.env` load, `ensure_schema`, `register` and the tunable read. The "no new log line" proof moved to smoke (s) as counts pinned at 2.
2. Marker 1's after value is a bare `listed`. `deploy-smoke.sh` `value_is` reads a backticked `listed` as a literal string, and that string is in no `ls` output. 929's backticked form would have read RED at smoke (d).
3. ASK DESK: `CONTRACT: migrations-on-the-end line` traces to no file (grep over prompts, ops/desk and LAWS finds only prompt 1003). Default: `MIGRATIONS: none`, no `db query` row and no `## READ-BACK`, so the stop line ends `migrations applied: none`. The preflight checks this against DEPLOY-HUB and `deploy-smoke.sh`.
4. `RESTARTS` and `WAITS` are header lines that no tool reads (`grep` over `desk-launch.sh`, `deploy-card.sh`, `authorize.sh`). `RESTARTS: none` holds because nothing merges. cos-env-load's radar restart (L42) and the cos load are stated in `## RECORDS`. Kept 929's ORDER (smoke (s) before `--owed-clear`) because 929 hub DECISIONS 2 stands per R2335. DEPLOY-HUB 4.6L-BO line 146 orders the clear right after the print.

## RECORDS
- 20:16:43 ET start (`date`).
- Read: prompt 1003; `areas/cobalt.md` from `## What Cobalt is` and `## Build rules` down; `CARD.md`; card 929; `reports/deploy-cos-bootstrap.md`; `reports/deploy-cos-env-load.md`; `reports/draft-cos-fill-prose-2026-10-21.md`; `writing-rules.md`; LAWS L36, L42, L75, L79, L80.
- Read: `ops/desk/deploy-smoke.sh` whole; `desk-launch.sh:2160-2240` (bootstrap-only checks); `deploy-step-c.sh` (bootstrap-only and owed-clear lines); DEPLOY-HUB lines 1-48, 63, 94-95, 146, 157, 160, 164, 171.
- Read: `cto-2026-10-21.md` R2300-R2348 (R2335, R2340); card 1000 lines 17, 33, 63, 66 (E3 note).
- `git show main:` `src/cobalt/cos/run.py` (`ENV_FILE` :40, `tunable_int` :102, rmtree :105, mkdir :106, `turns.ensure_schema` :108, `hitl.ensure_schema` :112, `load_dotenv(ENV_FILE)` :141, `refuse_if_agent_alive()` :157, `store.ensure_schema()` :159, `register` :160, `mark_running` :165), `ops/com.cobalt.cos.plist` (logs :33, :35), `ops/start_cos.sh`.
- `git grep main`: `configs/cobalt/jobs.yaml:206` cos row, `:214` `enabled: true`. `0001_cobalt_cos.sql:14`, `:28`; `0001_cobalt_hitl.sql:20`. `session.py:76`, `:82`, `:84`; `actions.py:62`. Row C4a of card 730 names `ops/com.cobalt.cos.plist`.
- 20:18 ET: `ls -la` shows `logs/cos.err` (3040 B, 17:23) and `logs/cos.log` (0 B). `data/cos` and `data/cos/scratch` are absent.
- 20:18 ET: `grep -c -F` on `logs/cos.err`: Traceback 2 · DbConfigError 4 · `DbConfigError: Missing Postgres settings` 2 · CosRefused 0 · CosConfigError 0 · CoS step 0 · CoS turn FAILED 0. On `logs/cos.log`: Error 0.
- `bootstrap-owed.json:4` lists the cos gate items D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20.
- 20:20 ET card written. A grep shows no placeholder token, and every `GATE RESULT:` line names `com.cobalt.cos`. `deploy-smoke.sh --dry-run` was not run because it is not on this seat's allow line.

DRAFTED · decisions: 4
