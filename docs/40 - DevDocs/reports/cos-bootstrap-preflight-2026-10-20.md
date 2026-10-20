# Card 929 (cos bootstrap, 4.6L-BO) — preflight 2026-10-20

Card `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md`, committed in `22ac1970`. Read-only. Two FAILs: smoke read 5 would run RED, and two `cto-2026-10-20.md` line numbers are stale.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header values and names (read card; `CARD.md:17,25,150`) | `JOB cos-bootstrap`, `LADDER S5-P3 · F20`, `BRANCH/WORKTREE/TIP none`, `BASE main`, `SET cos`, `TICKERS none`, `MIGRATIONS none`. `TAG` and `RULINGS` carry `«FILL»` (check 17). `WAITS:` is not in `CARD.md` (see NOTE 3). | OK |
| 2 | `git diff HEAD --stat -- <card>` and `git log -1 --format=%h -- <card>` | empty diff; last commit `22ac1970` | OK |
| 3 | `git grep -n main:` `run.py` (`:99 :103 :105 :109 :150`), `session.py` (`:76-85`), `actions.py` (`:62-71`) | `run.py:99 poll_s = tunable_int`, `:103 SCRATCH_DIR.mkdir`, `:105 turns.ensure_schema`, `:109 hitl.ensure_schema`, `:150 store.register`, `:155 store.mark_running`. `session.py:76 def tunable_int` … `:84` raise, `:85` return. `actions.py:62 def request_ttl_min`, null raise `:67-71`. | OK |
| 4 | `git grep -n main:` `tunables.yaml`, `jobs.yaml`, plist, migrations | `tunables.yaml:1008-1009` `cos.poll_interval_s` null; `:1026-1027` `hitl.request_ttl_min` null. `jobs.yaml:214 enabled: false`. `com.cobalt.cos.plist:33`, `:35` are the `cos.log` and `cos.err` paths. `0001_cobalt_cos.sql:14`, `:28`; `0001_cobalt_hitl.sql:20` are `CREATE TABLE IF NOT EXISTS`. | OK |
| 5 | `git grep -n main:` `run.py` `refuse_if_agent_alive` | `:44 def`, `:52 raise CosRefused`, `:57` end; called at `:147` before `store.register` | OK |
| 6 | `git grep -n -E "R219[6-8]" main -- reports/cto-2026-10-20.md` | R2198 at `:25`, R2197 at `:26`, R2196 at `:27`. The card cites `:21` (R2198) and `:22` (R2197). | FAIL |
| 7 | `git grep R1112 / R1854 main -- reports` | R1112 `cto-2026-10-11.md:31` and R1854 `cto-2026-10-18.md:99`, both `HIS RULING · APPROVED` | OK |
| 8 | `git grep -n C4a main -- prompts/2026-10-18/730-f20-card.md` | row `C4a` (`:37`) names the plist, `jobs.yaml` row and `start_cos.sh` | OK |
| 9 | gate report `tail -n 3 reports/cos-gate-run-2026-10-20.md` | `GATES DONE · ok: 10 · fail: 1 · not run: 3`, matches the card | OK |
| 10 | smoke and marker forms vs `ops/desk/deploy-smoke.sh` (read at `main`) | Both markers are `ls` and `grep -c -F`. Reads 1-5 are `grep -c -F "<s>" <path>` with no `$`, backtick or quote problem. Reads 1-4 have expectation `` `0` ``. **Read 5**: the script cuts the expectation at the first `;`, leaving `` `0` — `Traceback` = 0 proves the poll ``. That is not `` `v` `` or any `exit 0, …` form, so the script prints "expectation … is not one this script reads" and the row is RED. | FAIL |
| 11 | production markers now: `ls …/logs/cos.err`; `grep -c -F "com.cobalt.cos" …/bootstrap-owed.json` | `No such file or directory`; `1`. Both equal the card's `before`. | OK |
| 12 | commands given to the hub vs `DEPLOY-HUB.md` line 11 | `sh ops/desk/deploy-step-c.sh --bootstrap-only` and `--owed-clear` are covered by `sh /Users/cobalt/cobalt/ops/desk/*`. `launchctl bootstrap gui/501 …/ops/com.cobalt.cos.plist` and `bootout gui/501/com.cobalt.cos` are generated from the `add` line. `launchctl print gui/501/*`, `grep`, `ls` are listed. `deploy-smoke.sh` is under `ops/desk/`. | OK |
| 13 | `WAITS:` line | `cos-cutover-tooling DEPLOYED, cos-tunables DEPLOYED, agent retired` | OK |
| 14 | F-14 listener overlap | `refuse_if_agent_alive` (`run.py:44-57`) refuses to start while the agent pidfile is live. The card's ORDER and NOT IN THIS JOB never touch `com.cobalt.agent`; the retirement is a separate desk job. | OK |
| 15 | RESTARTS homes | The card has no `RESTARTS` field: no merge, no outage. STEP-R is listed under "HUB STEPS WITH NO CARD VALUE". NOT IN THIS JOB names `aset`, `radar`, `agent` as untouched and R60 restarts of a loaded cos as later. The cos `reads:` homes are in `jobs.yaml:218-223`. | OK (NOTE 4) |
| 16 | MIGRATIONS line | `MIGRATIONS: none` plus the RECORDS line: first start CREATEs IF NOT EXISTS, additive. No number is given. | OK |
| 17 | `«FILL` tokens | `RULINGS` (his D14 / agent-stopped row), `TAG`, GATE RESULT D14, agent stopped, X15. Decisions file item 7 keeps `RULINGS` and `TAG` as `«FILL»`. His three open decisions are D14, agent stopped and X15; none is invented. | OK |
| 18 | GATE RESULTS vs `bootstrap-owed.json` gate list for `com.cobalt.cos` | List is D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20 (14). The card has one `GATE RESULT:` line for each of the 14 with non-empty text, so `deploy-step-c.sh --bootstrap-only` (`:185`) passes them. | OK |
| 19 | the card's own launch blockers | Beyond WAITS: none found. See NOTE 3 about the `WAITS` header. | OK |

## ISSUES

- FAIL 6: RECORDS cites `reports/cto-2026-10-20.md:22` for R2197 and `:21` for R2198. At `main` they are `:26` and `:25`, and the file is edited all day. Fix: cite by row id ("row R2197, R2198"), or the right lines at the commit.
- FAIL 10: SMOKE READS row 5 (`cos turn failures`) packs a `;` into its note. `deploy-smoke.sh` stops the expectation at the first `;`, so the row is RED even when the count is 0. In a live run a red smoke row sends the hub to STEP-5, which boots cos back out. Fix: make the expectation just `` `0` `` and move the `Traceback` / UNPROVEN / `FAILED:` text to a `## RECORDS` or `## CHECK ASKS` line, or write it with no `;`. Then run `deploy-smoke.sh --dry-run` on the card.
- NOTE 1: `TAG` is `«FILL: deploy-<run date>-cos-bootstrap»`. This is the brain's ruling (decisions item 7), not a defect. The desk fills it at launch (other cards use `deploy-<date>-<job>`).
- NOTE 2: BASE is `main`, as the spec says. The tree is ahead by desk commits only, not a fail.
- NOTE 3: `WAITS:` is not in `CARD.md` and `desk-launch.sh` / `deploy-card.sh` do not mention it. Whether the launcher ignores or rejects an unknown header is not proved here. The cutover-tooling card (T2) must admit a bootstrap-only card anyway, so check it there.
- NOTE 4: the card does not list restart homes for cos. That is consistent with a no-merge card, but a reader who wants them must go to `jobs.yaml:218-223`.
- Current state: `cos.err` is absent, the owed entry is present, and `jobs.yaml:214` is `enabled: false`. The tunables stay `null` until the K5 card (WAITS).

PREFLIGHT DONE · card: cos-bootstrap · checks: 19 · fails: 2 · ready: NO
