# STACKED DEPLOY DRAFT — 2026-09-23 (drafter `stacked-deploy-draft-0923`, Opus 5.5)

## §0 Headline
Three prompts written in `prompts/2026-09-23/`: `07-stacked-deploy.md` (deploy on his DONE TRADING word, R5), `08-review-stacked-deploy.md` (L67 read: Grok + Gemini + Opus 5.5), `09-s2-smoke-look.md` (≥21:40 look + S2 close verdict).
BIG DIFFERENCE vs `05`: `setups/seven-0921` ships PRODUCTION MIGRATION `0013_tunables_slug_nullable`, so `07` is a write path (L29): Opus 5.5 + `acceptEdits`, and it adds `d3`'s migration leg (proof-only preflight, snapshot, `--allow-prod` inside the residents-down window, 0013 never rolled back unattended).
Restarts predicted: `com.cobalt.aset com.cobalt.radar` (both down). Downtime cannot match yesterday's 93 s: the migration runs inside the window (L66).
`07` carries 16 NEW rule strings (11 re-pointed from `05`, 5 without a precedent shape) for his ONE approval list. `08` and `09` add none. ESCALATE: 14.

## Files written
| file | bytes (`wc -c`, 06:4x) | shape | NEW strings |
|---|---|---|---|
| `prompts/2026-09-23/07-stacked-deploy.md` | ≈74 KB | `2026-09-22/05-stacked-deploy.md` + `2026-09-19/53-deploy-d3.md`'s migration leg | 16 (listed below) |
| `prompts/2026-09-23/08-review-stacked-deploy.md` | ≈30 KB | `2026-09-22/06-review-stacked-deploy.md` + the Opus seat of `2026-09-21/66-setups-one-check.md:36` | none: `06`'s 9 strings + `"Bash(claude -p --model claude-opus-5-5 *)"` (09-22 R32; byte for byte in `79`'s line). Grok / agy stand on 09-22 R30 "through 2026-09-23 23:59 ET". Mechanically checked (whole-string match): 9 of 10 in `06`, 10 of 10 in `79`. |
| `prompts/2026-09-23/09-s2-smoke-look.md` | ≈9 KB | `2026-09-22/03-s2-smoke-look.md` | none: the `--allowedTools … --add-dir` segment is md5-identical to `03`'s (`21b80136…`) |

## Differences vs `05` (what changed and why)
| # | `05` (09-22, ran green) | `07` (09-23) | why |
|---|---|---|---|
| 1 | Sonnet 5, `--permission-mode auto` | Opus 5.5, `--permission-mode acceptEdits` | migration 0013 + a vault write = L29 write path; L62 (no bare `--bg` on a write path); L63 state note = interim practice |
| 2 | authority: 09-22 R3 (daytime from 11:00) | 09-23 R5 ("I want the work done after I am done trading.") + P-HIS: R__L carries `DONE TRADING <time>` | his ruling today |
| 3 | window 11:00–19:55 | no lower bound but his word; date 2026-09-23; 19:55 hard / 19:58 merge clocks kept | R5; the 20:00 / 20:30 / 21:10 / 21:40 jobs never crossed |
| 4 | branches stale-marker + ops | `setups/seven-0921` (34 commits, 72 non-docs paths) + `s2/smoke-fix-0922` (5 commits, 10 non-docs paths); one shared path `tests/cobalt/test_replay_runner.py`, different hunks | today's built + checked set (L43) |
| 5 | restart set aset only; radar stays up; STEP-2.7 radar-path empty diff | BOTH residents down; 2.7 dropped; a narrower derived table still takes both down (L66 names both, the migration is inside) | setups touches radar/cards/taxonomy code + `tunables.yaml` (read by both, `jobs.yaml:69`, `:169`); both builds' tables say both |
| 6 | no migration; `jobs.yaml` hunk proof (2.6) | 2.6 = no `ops`/`jobs.yaml` diff + EXACTLY the three `db_migrations` paths; P14-M `--allow-prod --proof-only`; 3.4 `backup run`; 4.4 `db migrate --allow-prod` (foreground, 600 s) with no-CHANGED / no-CREATED gate and a `pg_catalog` `attnotnull` read-back; STEP-5 (2b) 0013 STAYS | `d3` §0 P13, §3.2, §4.5, §8 (3) |
| 7 | with-DB: `.env` in → dev migrate → suite → `rm` → validate (UNPROVEN, no creds) | dev `--proof-only` → forward migrate to 0013 → suite → LIVE-NOTE test → validate WHILE `.env` IS IN → `rm` | fixes `deploy-2026-09-22.md` 2.4 `UNPROVEN IN THE GATE`; the live-note proof is the setups build's gate 3 ("a SKIP there is RED") |
| 8 | P5/P6 two builds, two checks | + P7 `68` DEVDB REPAIRED, + P8 blind values `05` (`MISMATCH: 0`), setups check accepts `defects that HOLD: 1` (R4(a) cutter only) | task items (iii)–(v) |
| 9 | identity check on named paths | smoke fix tree-wide; setups tree-wide minus main's NINE moved non-docs paths (setups touches none — drafter `comm`, 06:3x) | setups base `5b208a0` predates yesterday's deploy |
| 10 | report commits: `-m "<subject>"` only | every commit adds `-m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"` | `deploy-2026-09-22.md` ESCALATE 1 |
| 11 | smoke (e): radar never restarted, carried per-ticker record = baseline | radar RESTARTED: fresh `radar cycle:` after `<t up>` (≤3 tails); heartbeat radar line OK or ONLY the carried kind, two reads ≥100 s apart; `TaxonomyConfigError` count = baseline; markers `EVALUATOR_VERSION = "s2p2.2"` and `unranked_rows`; cards read = baseline; `attnotnull` = `f` | today's code paths; 09-22 R2 review fold kept |
| 12 | relaunch rule (i)–(v) | + `attnotnull` read on relaunch (i: merged but not migrated → run 4.4/4.5 first); (vi) resume inside STEP-6 | the migration and STEP-6 are new resumable points |
| 13 | no vault write | STEP-6: his 09-22 R119 rows via `cobalt taxonomy assumed write` (dev vault `--apply` first, prod `--dry-run`, prod `--apply`, parser `tunables --assumed` before/after), ONLY after a green smoke; `taxonomy load` NOT run | L28 / L65; `ADDING-A-SETUP.md` "Rolling back after the assumed note" (rows loaded → rollback order changes) |
| 14 | STEP-6 close | STEP-7 close; ROLLBACK SHAPE named in the Deploy table (L54) | L54 "every deploy report names which rollback shape" |
| 15 | placeholders `R10` / `R11` | `R__A` (his approval) / `R__L` (launch); gate `grep -n -E "R_[_]"` | desk fills |

## RULE PROOF — `07`'s 54 allow strings (whole-string match against `05`'s launch line and `d3`'s strings, run 06:3x)
- `05` byte for byte (32): `git -C /Users/cobalt/cobalt add *` · `commit *` · `reset --soft HEAD~1` · `tag *` · `revert --no-edit *` · `revert --abort` · `git -C * status*` · `log*` · `diff*` · `rev-parse*` · `rev-list*` · `merge-base*` · `show*` · `cd *` · `uv run pytest *` · `COBALT_ENV=dev uv run pytest *` · `COBALT_ENV=dev uv run cobalt db migrate` · `COBALT_ENV=production uv run cobalt validate*` · `… jobs *` · `… heartbeat show*` · the six `launchctl bootout/bootstrap/kickstart` strings for aset and radar · `launchctl print gui/501/*` · the `curl … http://127.0.0.1:5010/*` string · `grep *` · `tail *` · `ls *` · `date*`.
- `d3` byte for byte, absent from `05` (6): `COBALT_ENV=dev uv run cobalt db migrate --proof-only` · `COBALT_ENV=production uv run cobalt backup run*` · `… backup status*` · `… db migrate --allow-prod --proof-only` · `… db migrate --allow-prod` · `… db query *`.
- NEW (16) — see the approval list below.
- `05` strings NOT carried (11): `merge --ff-only deploy/stacked-0922` · the stale-marker and ops-0921 `rebase main` / `rebase --abort` pairs · the four `stacked-0922` gate merges / abort · the `stacked-0922/.env` `cp` / `rm`.
- Denies (3) byte for byte `05`: `"AskUserQuestion"` `"EnterWorktree"` `"Bash(git push*)"`. `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt` as `05`.

## NEW strings — for his ONE approval list (one line each)
1. `Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0923)` — STEP-4.3, the one production merge (re-pointed from `05`).
2. `Bash(git -C /Users/cobalt/cobalt-wt/setups-c1 rebase main)` — STEP-1.1.
3. `Bash(git -C /Users/cobalt/cobalt-wt/setups-c1 rebase --abort)` — STEP-1.1 conflict path.
4. `Bash(git -C /Users/cobalt/cobalt-wt/s2-smoke-fix rebase main)` — STEP-1.2.
5. `Bash(git -C /Users/cobalt/cobalt-wt/s2-smoke-fix rebase --abort)` — STEP-1.2 conflict path.
6. `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --no-edit setups/seven-0921)` — STEP-1.4.
7. `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --no-edit s2/smoke-fix-0922)` — STEP-1.4.
8. `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --no-edit main)` — STEP-3.1.
9. `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --abort)` — STEP-1.4 / 3.1 conflict path.
10. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0923/.env)` — STEP-2.3 (a), by name, never printed (L41 interim).
11. `Bash(rm /Users/cobalt/cobalt-wt/stacked-0923/.env)` — STEP-2.3 (e), on every path.
12. `Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)` — STEP-2.3 (d), the live-note proof; READS his vault, writes nothing there.
13. `Bash(COBALT_ENV=dev uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --apply)` — STEP-6.3, the dev-vault proof (L28).
14. `Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --dry-run)` — STEP-6.4.
15. `Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --apply)` — STEP-6.5, THE VAULT WRITE (his `Assumed Defaults.md`, 3 rows of R119).
16. `Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy tunables --assumed)` — STEP-6.1 / 6.6, read-only parser proof (L65).
ALSO FOR THE SAME LIST (not launch-line strings): (a) the desk's `git -C /Users/cobalt/cobalt worktree add -b deploy/stacked-0923 /Users/cobalt/cobalt-wt/stacked-0923 main` (today's R1 shows a desk `worktree add` taking his word); (b) the production migration `0013` (`d3`-precedented strings, a production DDL); (c) the setups build's own owed item "(iv) His chat 'approve' at the deploy (L7, L61) — a trading-logic change for eight defs" (`setups-one-build-2026-09-21.md:1061`).

## The desk's launch order (recommended)
1. House lane, one Grok / Gemini hub at a time: `03` (dev-DB repair read, unblocks `68`) → **`08`** (this read of `07`: it depends on no other result, so it goes early to leave time to fold) → `05` (blind values) → `06` (smoke-fix check). Each launch row after `03` carries the `<nn> is not running` literals `08` greps (`03`, `05`, `06`).
2. `68` re-run (dev lane, not a house hub) as soon as `03` says no string changes → `DEVDB REPAIRED · head: 0011 …`.
3. Fold `08`'s HOLDS into `07` (L19 re-issue), commit.
4. ONE message to him: the 16 NEW strings + (a)–(c) above → his word = row R__A, committed.
5. On his "done trading": the desk checks `68` / `05` / `06` / `08` stop lines are in, writes R__L with `DONE TRADING <time>` and every stop line, commits, runs the `worktree add`, then `cd /Users/cobalt/cobalt` + the `07` launch line. Holds its own commits until `07`'s stop line.
6. `09` on a timer at ≥21:40 ET (launch row R__S).

## ESCALATE
1. WRITE-PATH LAUNCH MODE: `07` uses `acceptEdits` + the full allowlist (L63 state note: interim practice, not law; an unlisted Bash ASKS = a dialog). `d3` ran with NO `--permission-mode` flag, which L62 (amended 09-22) no longer allows on a write path. No launch shape is proven for both L29 and L63 unattended.
2. DOWNTIME: the task asked for a window "as short as yesterday's (93 s)". With BOTH residents and the migration inside it (L66 names "BEFORE the merge and migration"), it cannot be: predicted 93 s + P14-M's `proof cost:` (≈95 s at `d3`) + the radar bootstrap. Shortening it further means migrating after the residents come up — an L66 override that is HIS to give; `07` does not assume it.
3. `cobalt taxonomy load` is NOT in `07`: the R119 rows reach the radar only when `"user".tunables` is re-synced. `ASK DESK`: a separate one-command production job on his word after tonight's smoke (it also re-syncs every strategy note; its dry run must be read first). Rollback after that load has the fixed order in `ADDING-A-SETUP.md:33-37` (empty the unit + reload, then code, then 0013).
4. R119 OUTCOME vs THE STOP LINE: the task fixes the stop-line shape; a STEP-6 failure leaves `STACKED DEPLOY DONE …` (the code is green) and puts `R119: NOT WRITTEN — <why>` in §0 and ESCALATE. `ASK DESK` if a failed R119 should instead end `FAILED: STEP-6 …`.
5. A-24 (`leg.min_size_atr`): R119 keeps it NULL; the engine row is already `value: null` (`tunables.yaml:248-255`), so NO row is written for it (the task text says "three rows … A-24 null"). The parser proof shows it as `hole`.
6. THE ROWS FILE is written by the hub with the Write tool at `/Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml` (outside every worktree and the vault; user data, never committed). Its fields are the engine rows' own `unit` / `scope` / `dynamic` / `status` / `consumers` with `source: assumed`; whether `status: proposed` is accepted with `source: assumed` is UNPROVEN until the dev `--apply` (6.3) — a refusal there stops STEP-6 cleanly.
7. SIBLING-DEPENDENT PATHS (drafter `01` had written none of `03` / `05` / `06` at 06:4x): `07` P6 assumes `reports/s2-smoke-fix-check-2026-09-23.md` and `06`'s DONE shape with `ready … YES` ×3 / `defects that HOLD: 0`; P8 assumes `reports/setups-blind-code-2026-09-23.md` with `23`'s stop line (`SETUPS BLIND CODE SEAT DONE · … MISMATCH: <n> …`); P7 assumes `68` keeps its report path `reports/devdb-repair-2026-09-22.md` and its `DEVDB REPAIRED · head: …` line. `ASK DESK`: fold the real paths / shapes from `01`'s report before `08` stages `07`.
8. P8 treats `UNDERIVABLE: <u>` > 0 as recorded, not a stop (`MISMATCH: 0` is the stop). `ASK DESK` if `<u>` > 0 should hold the setups branch.
9. SETUPS DEPLOY-ACCEPTANCE ITEMS NOT CARRIED (`setups-one-build-2026-09-21.md:1055-1060`): X3 and gate 4 over stored sessions (`cobalt radar evaluate`), the stored-day X5, the daily legs of X7 / X18. No approved string exists for them and they are dev-lane experiments, not deploy steps. Carried: gate 3, the live-note test (2.3 (d)), and the NN#16 smoke. `ASK DESK`: a dev-lane job, or accepted as UNPROVEN (L70).
10. FIRST WITH-DB RUN: both builds' with-DB proofs were OWED (`68`); `07` 2.3 (c) is their first with-DB run. A red there stops the whole run; L43 / L68 SCOPE then drop the red branch and land the other in a desk re-issue. No one-branch file is pre-drafted.
11. `cobalt_dev` STAYS AT 0013 after the gate on every path (no dev restore string). On a FAILED deploy, dev is one migration ahead of production.
12. `EVALUATOR_VERSION` `s2p2.1` → `s2p2.2`: receipts written before the deploy are refused by replay and audit export (build ESCALATE (v), by design). On a STEP-5 rollback, receipts written by the new code in the minutes it ran carry `s2p2.2`, which the old code does not know — READING, UNPROVEN (L70).
13. The radar is booted out if his word comes during RTH or after-hours scanning (R5 sets L43's window aside); the radar's carried per-ticker poll records reset on restart, so smoke (e) accepts OK or the carried kind at any `<n>`.
14. Yesterday's round-2 read lost Grok at launch (`Error: Operation not permitted (os error 1)`); `08` keeps Gemini as the floor and the Opus 5.5 read as an extra reader that never meets the L67 floor alone (same house as the author).

STACKED DEPLOY DRAFTED · prompts: 3 · new rule strings: 16 · restarts predicted: com.cobalt.aset com.cobalt.radar · ESCALATE: 14
