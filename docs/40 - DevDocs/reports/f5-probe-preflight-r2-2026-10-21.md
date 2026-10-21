# f5-probe-preflight-r2 — 2026-10-21

Read only. `date` → Wed Oct 21 12:17 EDT 2026. `git rev-parse main HEAD` → `41804777` both (card BASE `d988d543` trails by desk commits only: NOT a fail). Card 973 as committed in `41804777`; round 1 `reports/f5-probe-preflight-2026-10-21.md`; amend `reports/draft-f5-probe-amend-2026-10-21.md`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card 973>`; `git log --oneline -3 -- <card 973>` | empty diff; committed `41804777` (amend), `214de8b4` | OK |
| 2 | header read (`CARD.md` keys) | JOB `f5-probe`, LADDER `S5-P2 · F5`, CLASS K2, INSTALL none, BRANCH `ops/f5-probe`, WORKTREE `f5-probe`, BASE, TIP/HOUSE B empty (desk fills), BAND HIGH, RESTARTS `com.cobalt.radar`, `RULINGS: 2026-10-18 R1863`, REPORT and CHECK REPORT paths; no MIGRATIONS key (deploy-only) | OK |
| 3 | `git grep` `cli.py`, `jobs.yaml` | `cli.py:91` imports `checkpoints`, `:579` `checkpoints_cli.add_parser(sub)`; `jobs.yaml:203` `imports: [cobalt.cli]` (radar); no other resident hit on `cobalt.cli` or `cobalt.prefill` imports | OK |
| 4 | `git grep` `checkpoints.py` (main) vs card anchors | `:91` WRITER, `:104` GROUPS_URL, `:107-110` SECTORS, `:115-121` PHRASES, `:167` window_refusal, `:200` parse_groups, `:224` fetch_groups (`async def`; `raise_for_status` `:232`, `parse_groups(response.text)` `:235`), `:238` fetch_figures (only call in `run_checkpoint` `:704`), `:283` compute_delta, `:353` _strings, `:363-391` validate_reply (digit refusal `:372-374`), `:405` _SYSTEM, `:413-439` narrate (request `:417-427`, empty delta `:423-425`), `:559` default_stores, `:576` check_demand, `:652` run_checkpoint, `:813` cmd_run (passes no `keep`), `:837-844` add_parser; all hold | OK |
| 5 | `git grep` `env.py`, `client.py`, `note.py`, `vault.py`, `cos/probe.py` | `env.py:60` resolve_env, `client.py:89` call_sync, `note.py:250` daily_note_path, `vault.py:155` resolve_vault_path, `cos/probe.py:208` `_scratch`, `:487` `_verdict`, `:515` `main` | OK |
| 6 | `git grep` FINAL rows | `F5-FINAL:176` X2, `:178` X4 (digit/number-word → phrase removed; under 15 of 20 → degraded-by-default), `:179` X5, `:180` X6, `:181` X7, `:184` X10, `:187` X13; the card's quotes match | OK |
| 7 | `git grep` test file; `f5-x3-measure` `:66-71` | `test_checkpoints_offline.py` `:12` X2 owed, `:138` cp, `:307` groups_http, `:327` TestNumbers, `:682` test_0745_at_0820; `f5-x3-measure:69` holds the sector rotation (`SECTORS[i]` takes the Change of `SECTORS[i+1]`); rule D's index terms are the card's own (NOTE 2) | OK |
| 8 | BUILD-HUB `:14` launch line vs `## ORDER` | builder commands `uv run pytest *`, `uv run cobalt jobs restarts *`, git add/commit/diff/log/show, ls, grep, wc, date, `sh ops/desk/*`; no network, no `COBALT_ENV=production`; the card runs no probe and no `cobalt checkpoint run` outside a test | OK |
| 9 | P2 boundary | production refused; unset/unknown refused (`resolve_env` first sentence); scratch `mkdtemp(prefix="f5-probe-")` refused under repo, `~/.claude`, vault; `finally` removal; no VaultWriter / ensure_daily_note / CheckpointStore / VaultWriteStore / send_dm / as_job / launchctl / plist; crash = `FAIL error <ExceptionName>`; tests patch each to raise | OK |
| 10 | `check_demand` chain (X6 step 2) | read only, no database, reads the resolved (dev) vault's radar notes; unchanged since round 1 (`checkpoints.py` and `measure.py`/`notes.py` have no diff vs HEAD) | OK (NOTE 3) |
| 11 | X4 `PROBE X4` line | present; 15/20 bar = FINAL `:178`; number-word list = drafter DECISION 4; clause counts and phrase ids only, `clause_holds_no_reply_text` test | OK |
| 12 | X5 / X7 / X10 (row H1) | each `PROBE <X> NOT RUN — needs his hand: <leg>`, exit 3, nothing run; test parametrized over the three | OK |
| 13 | X6 pass rule | `OK` iff the four statuses hold no `degraded (prompt_refused)` and no `degraded (empty delta)`; prompts `compute_delta(S0,None)`, `(S1,S0)`, `(S2,S1)`, `(S3,S2)` through `narrate()` | OK |
| 14 | X13 line | `OK (offline: the window rule refuses a late fire on 4 of 4 slots; launchd leg not run, no plist loaded)`; `REFUSED: slot <HH:MM> window closed at <HH:MM>` (`:167-175`, `:683-688`); stores raise on any call; a patched `window_refusal` fails and names the slot | OK |
| 15 | X2 fixture row | `## RECORDS` ROW (b) OWED, G1 and `## NOT IN THIS JOB` mark it owed after the first X6 run; "does not gate the plist load (R2282)" | OK |
| 16 | exit codes | OK 0, FAIL 1, NOT RUN 3 (P1), argparse 2 (C1) | OK |
| 17 | `ls` / `grep -c -F` on main for each `## DEPLOY PROOF` `before` | `ls …checkpoint_probe.py` → `No such file or directory`; `grep -c -F "PROBE_ITEMS = ("` → `0`; `ls …test_checkpoint_probe.py` → `No such file or directory`; `ls ops/com.cobalt.checkpoint-0715.plist` → listed | OK |
| 18 | `ops/desk/deploy-smoke.sh` mapping vs DEPLOY PROOF | only `ls` and `grep -c -F` (both mapped, `:11-12`, `:122`, `:189`); no `curl`, no `5010`, no `db query` in the card's marker lines | OK |
| 19 | red test first (K25) | each row names its test(s) and RED on BASE (`invalid choice: 'probe'`; G1 `TypeError … 'keep'`) | OK |
| 20 | RECORDS line 1, `grep -n -F` of the 972 item 6 text in the card | `68:` the text, verbatim | OK |
| 21 | RECORDS line 2, `grep -n -F` of the R2284 text in the card | `69:- f5-probe 973 — X6 = 1 real Groups fetch + 3 rule-D derived prompts; keep-groups on the probe path only, run path never writes a body (test); X4 <15/20 → narrative degraded-by-default per FINAL :178, not a load block — brain 9b07db5a 2026-10-21` verbatim; R2284 is `cto-2026-10-21.md:13` | OK |
| 22 | ruling (i): "1 real fetch + 3 derived by rule D" | X6 clause starts `figures: 1 real fetch + 3 derived by rule D · prompts 4 · prompt_refused 0 · …`; `::test_x6_four_prompts_one_per_slot_pair` records ONE Groups GET and asserts the line holds `1 real fetch + 3 derived by rule D` | OK |
| 23 | ruling (ii): keep seam probe-path only, a test pins it, kept file under `.f5-probe/` | G1: `keep=None` default; `--keep-groups` X6 only; PATH must be under `/Users/cobalt/cobalt-wt/.f5-probe/` (off-root → `FAIL refused: --keep-groups PATH must be under …`), absolute, not existing, parent a dir, not under repo / vault / `~/.claude`; "THE RUN PATH NEVER WRITES A BODY (R2284)"; `keep=` passed only by the probe's X6; new `::test_the_run_path_writes_no_body` (`fetch_groups` / `fetch_figures` without `keep`, then `checkpoint run --slot 0745 --dry-run` through the real `run_checkpoint`: cwd, `HOME` and the root stay empty, no file holds the body; plus a by-content pin that `keep=` is only in `fetch_groups`, `fetch_figures` and the pass-on). The off-root test monkeypatches the root to a `tmp_path` subdir. On main today `fetch_figures(cfg)` is called once (`:704`), `cmd_run` passes none: the pin holds at BASE | OK |
| 24 | ruling (iii): X4 < 15/20 is a result, not a load block; number-word removes the phrase | X4 row: "THE CONSEQUENCE IS KNOWN, NOT A LOAD BLOCK (FINAL `:178`, R2284)"; below 15 of 20 adds `→ narrative degraded-by-default (FINAL :178)`; each hit phrase adds `→ <phrase_id> removed from the enum (FINAL :178)`; every FAIL clause ends `; plist load not blocked by X4`; exit 1 kept; tests `::test_x4_fifteen_valid_is_ok_fourteen_fails` (14 → FAIL with both strings; 15 → neither) and `::test_x4_a_number_word_fails_and_names_the_phrase`; digit case handled by `validate_reply` `:372-374` (counted invalid `UnsourcedFigure`) | OK |
| 25 | the amend's six decisions vs R2284 | D1 digit via `validate_reply`, no new scan; D2 clause wording; D3 off-root refusal text; D4 run-path pin three legs; D5 distinct sector Changes + one GET; D6 growth: none contradicts R2284 (X6 = 1 real + 3 derived; keep on probe path only; X4 below 15/20 not a load block) | OK |
| 26 | what blocks the card's own build | nothing: no migration, no network, no production command; every needed file exists on main; the new files are absent as the card says | OK |

## ISSUES
1. NOTE: BASE `d988d543` trails main `41804777` by desk commits; the desk resets it at launch.
2. NOTE: rule D's index terms (price minus k × 0.50, change % minus k × 0.10) are the card's own; `f5-x3-measure-2026-10-20.md:69` holds only the sector rotation. Not a fail.
3. NOTE (#10): `check_demand` reads the radar notes of the resolved (dev) vault; read only.
4. NOTE: the X6 test needs the eleven constructed Changes distinct so a rotation moves ranks (card says so).
5. NOTE: `fetch_groups` is `async def` (`:224`). The pin "`fetch_groups(groups)` called without `keep`" must be run through `asyncio.run`; a builder detail, not a card defect. The amend's report said the def is at `:222`; `main` has it at `:224`, as the card cites.
6. NOTE: `PHRASES` ids (`prior_close`, `index_move`, `leader`, `laggard`, `rank_move`) and the keys `lines`, `phrase_id`, `refs` hold no number-word, so X4's number-word leg can only fire on a changed enum; its test constructs a reply. Correct as a guard; the real run will report `number-word hits` empty.

Blocks the card's own build: nothing.

PREFLIGHT DONE · card: f5-probe · checks: 26 · fails: 0 · ready: YES
