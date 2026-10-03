# BRAIN — parallel builds and idle workers, 2026-10-01 (his R17; seat `brain` f80eab82, Opus 5.5, read-only)

`D` = `docs/40 - DevDocs` · `M` = `Vault/Think/6 - Permanent/Memory` · `DT` = desk transcript `~/.claude/projects/-Users-cobalt-cobalt/5efe8feb-….jsonl` · `GT` = guard-build transcript `~/.claude/projects/-Users-cobalt-cobalt-wt-desk-size-guard-1001/ee26d4c9-….jsonl` · times ET (transcripts are UTC−4)

## §0 Headline
1. A: B is not safe to build today. The test database name is hard-coded on purpose (`src/cobalt/env.py:79-86`: "Deliberately takes no argument and reads no config file: a per-component `db_name` is exactly how production came to write into `cobalt_dev`"). A database per build reverses that safety rule, so it is a REDESIGN that needs an ADR and the tribunal (L67).
2. A, middle step (recommended): builds launch while the lock is held and take the lock only at their with-DB steps. A with-DB step WAITS for the lock instead of failing. A full with-DB turn holds it about 20 min (pass 1 ≈11:40, pass 2 ≈3:40, plus migrate; `f15-p1-check-2026-09-30.md`, `e1-inline-check-2026-09-30.md`). Everything else in a build runs side by side.
3. B: the files do not show workers idling 20–25 min on the desk today. The guard build's two FAILED lines were answered in 38 s and 22 s. The real waits are the lock queue (A) and yesterday's 71-min watch miss. Desk mistakes the card could have prevented caused the two FAILED stops themselves.
4. The lock is free now (`ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`, 08:23). Cards 04, 05 and 06 can launch, one with-DB step at a time.

## A — ONE TEST DATABASE
**What L76 holds today** (`M/LAWS.md` `### L76`): one owner. `desk-launch.sh` refuses a build or check LAUNCH while any `~/cobalt-wt/*/.env` exists (`ops/desk/desk-launch.sh:428-433`, `:457`, `:495`, `:534`). Yet a build needs the lock only at three points: PREFLIGHT's probe, E2 when a red is a with-DB test, and W (`D/prompts/BUILD-HUB.md:39`, "Taken at PREFLIGHT (the probe), at E2 only when …, and at W"). The launch refusal makes builds queue for the whole run, not just those minutes.

**Is a scratch database per build (the desk's B) safe?**
| area | finding | evidence |
|---|---|---|
| DB selection | name from `COBALT_ENV` alone, by design; B needs an override (env var or config). That is the exact shape RULING 7 removed | `src/cobalt/env.py:45-53, 79-86` |
| destructive guard | hard-coded allowlist `("cobalt_dev",)`; a `DROP DATABASE` at the stop line, or a reset on a scratch DB, is refused unless the guard widens | `env.py:48, 89-100` |
| grants | the app role has CONNECT on `cobalt_dev` and nothing else; each scratch DB needs a grant from a superuser step | `ops/cobalt_app_role_provision.py:34, 82` |
| migrations | W migrates forward/back on the DB itself (c2, f), so a scratch DB would hold them; a template copy must stay at `0013` with no open session, or Postgres refuses `CREATE DATABASE … TEMPLATE` | `BUILD-HUB.md` W (c2)–(f) |
| tests | 20 test files name `cobalt_dev` literally (e.g. `tests/experiments/stale_score/test_xl76_devdb_absence.py`); the root fixture is written for `cobalt_dev` | `grep -rln cobalt_dev tests`; `tests/cobalt/conftest.py:1-2` |
| `.env` / lock | `.env` stays the credential copy; the lock would become per-DB. The deploy gate still needs its own DB or the shared one | `L76` last sentence |
| residents | production residents use `cobalt_brain`, so they are not affected | `env.py:44` |
| load | 28 cores, 96 GB (`sysctl`); 3–4 parallel suites fit; disk size of a `cobalt_dev` copy is UNPROVEN | — |
Verdict: possible later, but it is a REDESIGN (CLAUDE.md strangler rule: "REDESIGN needs an ADR") of a safety resolver that exists because of a production incident. It needs the tribunal (L67), a build and a check: tokens he has ruled scarce (R73). Not now.

**Cheapest safe middle step: "launch now, lock at the step, wait for it"**
1. `ops/desk/desk-launch.sh`: `build` and `check` no longer call `lock_free` at launch. The rest is unchanged: a resume still refuses another worktree's `.env` (`:426-433`), and `deploy` still refuses while any lock is held.
2. A new ops script `ops/desk/take-devdb-lock.sh <worktree> <minutes>` takes the lock ATOMICALLY (`mkdir /Users/cobalt/cobalt-wt/.cobalt_dev.lock`, then copies `.env` by name). If the lock is held it re-tries every 60 s up to `<minutes>`, then exits 4. `release-devdb-lock.sh <worktree>` removes both and proves them gone. Why atomic: today's take is `ls` then `cp` (`BUILD-HUB.md:39` (a)–(b)). Two builds that both wait would race on that; one at a time could not.
3. `BUILD-HUB.md` / `CHECK-HUB.md` THE LOCK: (a)+(b) become `take-devdb-lock.sh <WORKTREE> 90`, and (d) becomes `release-devdb-lock.sh`. Exit 4 → `FAILED: <step> — cobalt_dev lock not free in 90 min`. PREFLIGHT probes the with-DB strings at W's first take (UL §5:29 "a rule with no harmless variant is probed by its first real use"), so a launch never waits at minute one.
4. `DEPLOY-HUB.md` STEP-G takes the same lock with the same script and holds it to its stop line. Builds keep running; their W waits behind it.
5. The two new strings go to him alone (L62: "a string not on it is new and is asked for by itself").
Card 05 (config line, tests may be DB-free) is NOT exempt. L68 GATE EARLY says "without all three it is not BUILT", and an exemption is his per-case override (L73). It only waits about 20 min at W.
Cost: one small build (ops scripts + three fixed-file paragraphs + a test), checked by one house (L67). DEPLOY-HUB changes need one other-house read (L67).

**Amended L76 (proposed text, his to rule):**
> `cobalt_dev` has exactly one owner at a time. A with-DB step — a suite, a migrate, a repair — takes the lock only through `take-devdb-lock.sh` (an atomic lock directory plus this worktree's `.env` copy), waits for it, and releases it through `release-devdb-lock.sh` at the end of that step (the lock directory and `.env` removed and proven gone). A build or check may LAUNCH and run every step that does not touch `cobalt_dev` while another session holds the lock. No build leaves a migration applied on `cobalt_dev`: a migration is applied only inside the suite's own rollback transaction, or rolled back before the step releases the lock. A production deploy's with-DB gate takes the lock through the same script and holds it alone from the gate's cut to its stop line; builds may run, and their with-DB steps wait.

**Recommendation A:** the middle step now. A scratch database per build comes back only if the W queue still costs real time after a week of job stats (R73).

## B — IDLE WORKERS
**Measured waits (worker's FAILED or stop line → desk's answer or stop)**
| run | event | worker | desk | wait | cause |
|---|---|---|---|---|---|
| guard `ee26d4c9` | FAILED: AUTHORIZATION | 07:34:22 (GT:111) | CONTINUE 07:35:00 (GT:135) | 38 s | desk launched at 07:33:30 (GT:8) before his "launch" row (R10, `cto-2026-10-01.md:18`) was right |
| guard `ee26d4c9` | FAILED: RESTARTS | 07:55:13 (GT:745) | CONTINUE 07:55:35 (GT:769) | 22 s | the card left `ops/desk/` scripts unclassified. K10: "An unclassified path is classified in the BUILD that adds it". The card's files lacked the class home (`restarts.py:36` OPS_TOOLS) |
| survey `e292c64e` | done | 07:58:45 | stop 07:58:57 (DT) | 12 s | — |
| f15 build 09-30 | FAILED: W | 18:17 | CONTINUE 18:33 (T:1958) | 16 min | the LOCK: the e1 check held it until 18:33 (question A) |
| f15 build 09-30 | BUILT | 19:20 | stop 20:30 | 70 min | watch regex `^(F15 P1 BUILT\|FAILED)`; real line `BUILT ·` |
| every other 09-30/10-01 run | stop line | — | — | 5–33 s | — |
The desk's own statement "The guard build has also lost about 25 minutes to my own errors" (DT, reply before 08:21) is NOT shown by GT. The answers took under a minute. Any lost time is inside the worker's re-runs, which GT does not price. UNPROVEN.

**Why it looks idle to him:** (1) cards 04, 05 and 06 were not launched while the guard held the lock: L76 at launch (A). (2) After `CONTINUE: RESTARTS` at 07:55 the guard's last line STILL reads `FAILED: RESTARTS …` at 08:23 (`tail -1` of its report). BUILD-HUB:32 says the worker will "restore the in-progress last line and resume". The worker did not, so the hub reads as stopped while it runs, and a re-armed watch would fire on the stale line at once (CL W1). (3) The desk writes row times that are not from `date`: R9 says 07:45, but the launch was at 07:33:30 (GT:8). R16 says 08:55 and R17 says 08:25, yet `date` read 08:23 when I checked. That breaks checklist R1 "`date` in the same call as every time written", and it makes the record unusable for timing.

**How to instruct the desk (smallest, no new law):**
1. Before every build launch, the card's `## RECORDS` (the desk's facts, `D/prompts/CARD.md`) answers the two questions that stopped today's build: the authorization row (his row exists, `HIS RULING` + `APPROVED`, committed) and the RESTARTS class of every path in `files` (from `uv run cobalt jobs restarts` on the planned paths, K10). Wording for CL `## launch`, as L7a: "Before `desk-launch.sh build`: his row for this job is committed (`grep -n "^| R<n> "`, `git log -1 -S`); every path in the card's `files` has its RESTARTS class home named in `## RECORDS`, or the row's `files` holds that home (K10)." This touches L62 and K10; it adds no new rule beyond K10.
2. CL W1 addition: "On `CONTINUE`, the desk re-arms the watch only after the hub's last line is no longer the old `FAILED` line." Plus a one-word fix the worker already owes: BUILD-HUB:32 is followed.
3. Times: every §4 time from `date` in that call (CL R1, already a rule). Practice.
4. Job stats gain one column, `waits: FAILED→CONTINUE min`, so a wait is measured, not felt (his R73 stats).
Not recommended: a second watch on `ASK DESK` (those lines carry a safe default and do not block; BUILD-HUB:45), hubs polling the desk, or a time limit on the desk's turns. The data shows the desk answers in under a minute when the notice arrives.

## RULINGS FOR HIM
- A: (1) the middle step and the amended L76 above, yes or no. (2) The two new strings `take-devdb-lock.sh`, `release-devdb-lock.sh` for the standing list, yes or no.
- B: the launch-checklist line L7a above, yes or no.

## UNPROVEN
- U1: disk size of a `cobalt_dev` copy, and Postgres load with 3–4 suites.
- U2: the "25 minutes" the desk names. Not found in GT.
- U3: whether the guard build is running or idle at 08:23. Its stale last line hides it, and I did not ask it (read-only seat).

BRAIN DONE · A: middle step — launch while locked, atomic wait-lock at the with-DB step, amended L76; scratch DB later via ADR · B: no 20–25 min desk waits in the files; pre-answer authorization and RESTARTS in the card (L7a), restore in-progress line, `date` every time
