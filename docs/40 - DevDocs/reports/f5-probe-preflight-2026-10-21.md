# f5-probe-preflight — 2026-10-21

Read only. `date` → Wed Oct 21 07:41 EDT 2026. `git rev-parse main` and `HEAD` → `214de8b4` (the card's BASE `d988d543` trails by desk commits only: NOT a fail).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card 973>`; `git log --oneline -3 -- <card 973>` | empty diff; committed `214de8b4` | OK |
| 2 | header read (`CARD.md` keys) | JOB `f5-probe`, BRANCH `ops/f5-probe`, WORKTREE `f5-probe`, BAND HIGH, CLASS K2, RESTARTS `com.cobalt.radar`, `RULINGS: 2026-10-18 R1863`, CHECK REPORT path, no `«FILL`, no MIGRATIONS key (deploy-only), INSTALL none | OK |
| 3 | `git grep -n main -- cli.py` / `jobs.yaml` | `cli.py:91` imports `checkpoints`, `:579` `add_parser`; `jobs.yaml:193` radar, `:203` `imports: [cobalt.cli]`; no other label imports `cobalt.cli` or `cobalt.prefill` | OK |
| 4 | Read `checkpoints.py` (main) vs card anchors | `:91` WRITER, `:104` GROUPS_URL, `:107-110` SECTORS, `:115-121` PHRASES, `:167-175` window_refusal, `:200-221` parse_groups, `:224-235` fetch_groups, `:238-256` fetch_figures, `:283-323` compute_delta, `:353` _strings, `:363-391` validate_reply, `:405-410` _SYSTEM, `:413-439` narrate (`:417-427` request, empty delta `:423-425`), `:576-584` check_demand, `:652` run_checkpoint (refusal `:683-688`, note stop `:747-751`), `:813-834` cmd_run, `:837-844` add_parser; all hold | OK |
| 5 | `git grep` `env.py`, `client.py`, `guard.py`, `note.py`, `vault.py` | `env.py:60` resolve_env (`:60-70`), `client.py:89` call_sync, guard `:126-133`, `guard.py:40-45`, `note.py:250` daily_note_path, `vault.py:155` resolve_vault_path | OK |
| 6 | `git grep` FINAL rows | `F5-FINAL:171` heading, `:176` X2, `:178` X4, `:179` X5, `:180` X6, `:181` X7, `:184` X10, `:187` X13; quotes match | OK |
| 7 | `grep -n` test file / x3-measure | `test_checkpoints_offline.py` `:12` X2 owed, `:138` cp, `:307` groups_http, `:327` TestNumbers, `:682` test_0745_at_0820; `f5-x3-measure-2026-10-20.md:69` is the sector rotation rule (it does not hold the index 0.50 / 0.10 terms; those are the card's own, see ISSUES) | OK |
| 8 | BUILD-HUB `:14` launch line and `:16` list vs `## ORDER` | builder commands: `uv run pytest *`, `uv run cobalt jobs restarts *`, git add/commit/diff/log/show, ls, grep, wc, date, `sh ops/desk/*`; no network, no `git mv`/`rm`/`mv`, no `COBALT_ENV=production`; the card runs no probe and no `cobalt checkpoint run` | OK |
| 9 | P2 boundary read | production refused, unset/unknown refused (`resolve_env` first sentence), scratch `mkdtemp(prefix="f5-probe-")` refused under repo / `~/.claude` / vault, `finally` removal, no VaultWriter / ensure_daily_note / CheckpointStore / VaultWriteStore / send_dm / as_job / launchctl / plist, no voice call; tests patch each to raise | OK |
| 10 | `check_demand` → `radar_planned_rpm` → `configured_sources` (measure.py:133, notes.py:384) | read only, no database; reads the radar notes of the resolved (dev) vault | OK (NOTE 3) |
| 11 | X4 `PROBE X4` line | present, `OK`/`FAIL` clause counts only, 15/20 bar = FINAL `:178`, number-word list = drafter DECISION 4 | OK |
| 12 | X5 / X7 / X10 (row H1) | each `PROBE <X> NOT RUN — needs his hand: <leg>`, exit 3, nothing run | OK |
| 13 | X6 pass rule | `OK` iff 0 `prompt_refused` over four slot-pair prompts (`compute_delta(S0,None)`, `(S1,S0)`, `(S2,S1)`, `(S3,S2)`), through `narrate()` | OK |
| 14 | X13 line | `OK (offline: …)`, four late fires refused with `REFUSED: slot <HH:MM> window closed at <HH:MM>` (`:167-175`, `:683-688`), stores raise on any call, launchd leg not run | OK |
| 15 | X2 fixture row | card `## RECORDS` ROW (b) OWED and G1 mark it owed after the first X6 run; `## NOT IN THIS JOB` names it; "does not gate the plist load (R2282)" | OK |
| 16 | exit codes | OK 0, FAIL 1, NOT RUN 3 (P1), argparse 2 (C1) | OK |
| 17 | `ls` / `grep -c -F` on main for each `## DEPLOY PROOF` `before` | probe module: `ls: …checkpoint_probe.py: No such file or directory`; `PROBE_ITEMS = (` count `0`; test file: `ls: …test_checkpoint_probe.py: No such file or directory`; plist `ops/com.cobalt.checkpoint-0715.plist` listed | OK |
| 18 | `deploy-smoke.sh` mapping vs DEPLOY PROOF lines | only `ls` and `grep -c -F` (both mapped); no `curl`, no `http://127.0.0.1:5010/`; marker lines in `- \`cmd\` · before · after` form | OK |
| 19 | red test first (K25) | each row names a test and its RED on BASE (`invalid choice: 'probe'`, or `TypeError … 'keep'` for G1) | OK |
| 20 | RECORDS line 1 (`972` item 6, verbatim) | card `## RECORDS` first bullet is the same text, character for character | OK |
| 21 | RECORDS line 2 (`f5-probe 973 — X6 = 1 real Groups fetch + 3 rule-D derived prompts; keep-groups on the probe path only, run path never writes a body (test); X4 <15/20 → narrative degraded-by-default per FINAL :178, not a load block — brain 9b07db5a 2026-10-21`) | not in the card (`grep` of the card for "run path never writes" and "not a load block" finds nothing); the ruling is R2284 in `reports/cto-2026-10-21.md:12`, committed with the card | FAIL |
| 22 | ruling (i): the report states "1 real fetch + 3 derived by rule D" | X6 row says "S3 real, S2/S1/S0 derived by rule D" but the clause is `prompts 4 · prompt_refused 0 · …`; the phrase is nowhere in the card or in what the probe prints | FAIL |
| 23 | ruling (ii): `keep=` / `--keep-groups` probe path only, run path never writes a body, a test pins it, kept file under `/Users/cobalt/cobalt-wt/.f5-probe/` | G1 has `keep=None` default and X6-only flag; the tests listed do not pin that `cobalt checkpoint run` never writes a body (`test_checkpoint_run_is_unchanged` only reaches `cmd_run`); G1 bars repo / vault / `~/.claude` paths but does not require `/Users/cobalt/cobalt-wt/.f5-probe/` (that path appears only in `## RECORDS` ROW (b)) | FAIL |
| 24 | ruling (iii): X4 < 15/20 is a RESULT with a known consequence (degraded-by-default, FINAL `:178`; a digit or number-word in an accepted line removes that phrase), not a load block | X4 row prints `FAIL` for < 15 and states no consequence in the row or the clause; drafter DECISION 5 default was "line does not count until the brain rules"; R2284 ruled | FAIL |
| 25 | what blocks the card's own build | nothing: no migration, no network, no production command; every needed file exists on main | OK |

## ISSUES
1. FAIL (#21): add the second `## RECORDS` line verbatim (R2284 text above).
2. FAIL (#22): the X6 clause (and a test) must carry "1 real fetch + 3 derived by rule D" (for example `figures: 1 real fetch + 3 derived by rule D`).
3. FAIL (#23): add a test that `cobalt checkpoint run` (and `fetch_groups` / `fetch_figures` called without `keep`) writes no body; G1's PATH rule must also require the kept file under `/Users/cobalt/cobalt-wt/.f5-probe/`.
4. FAIL (#24): X4 row: below 15/20 is the known result "narrative degraded-by-default (FINAL `:178`)", not a load block; add a number-word / digit hit rule "that phrase is removed from the enum" to the clause or the row; keep exit 1 as the FAIL result and say the plist load is not blocked by it.
5. NOTE: BASE `d988d543` trails main `214de8b4` by desk commits; the desk resets it at launch.
6. NOTE: rule D's index terms (price minus k × 0.50, change % minus k × 0.10) are the card's own; `f5-x3-measure-2026-10-20.md:69` holds only the sector rotation. Not a fail: the card defines them.
7. NOTE (#10): `check_demand` reads the radar screens and lists notes of the resolved vault (dev, since the probe is dev only); read only, no write.
8. NOTE: the X6 test expects `rank_move` lines in the three derived-slot prompts; a rotation by one place changes ranks only when the constructed Changes are distinct; the test's constructed figures must be.

PREFLIGHT DONE · card: f5-probe · checks: 25 · fails: 4 · ready: NO
