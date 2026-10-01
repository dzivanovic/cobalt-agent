JOB: devdb-lock
LADDER: OFF-LADDER — cto-2026-10-01.md 2026-10-01 R20
BRANCH: ops/devdb-lock-1001
WORKTREE: devdb-lock-1001
BASE: 093028d0
TIP: a9339f0a
REPORT: /Users/cobalt/cobalt-wt/devdb-lock-1001/docs/40 - DevDocs/reports/devdb-lock-build-2026-10-01.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/devdb-lock-check-2026-10-01.md
HOUSE B: as needed
TREE STATE: unchanged
RULINGS: 2026-10-01 R20

## ROWS

| row | what | red first | files |
|---|---|---|---|
| L1 | `ops/desk/take-devdb-lock.sh <worktree> <minutes>` takes the `cobalt_dev` lock ATOMICALLY: `mkdir /Users/cobalt/cobalt-wt/.cobalt_dev.lock` (the mkdir is the lock), writes the worktree name into it, then copies `/Users/cobalt/cobalt/.env` to `/Users/cobalt/cobalt-wt/<worktree>/.env`. If the directory exists it retries every 60 s up to `<minutes>`, then exits 4 with `cobalt_dev lock not free in <minutes> min (held by <worktree name from the lock>)`. `<worktree>` is one directory name, `[A-Za-z0-9._-]`, no `/`; anything else exits 2. `release-devdb-lock.sh <worktree>` removes that worktree's `.env` and the lock directory only if the lock names this worktree, then proves both gone (`ls` prints nothing) and prints `lock released`; a lock held by another worktree is not touched (exit 3). Both scripts install at `/Users/cobalt/.claude/ops/` as symlinks to `ops/desk/` (the desk does the install; not this build) | tests in `tests/ops/test_devdb_lock.py` against a tmp directory standing in for `cobalt-wt` (a `COBALT_WT_ROOT` env override, default the real path): two takes at once → exactly one wins; the loser waits then gets exit 4 with the holder named; release by the wrong worktree changes nothing; a bad name exits 2. RED on `BASE`: the scripts do not exist | `ops/desk/take-devdb-lock.sh`, `ops/desk/release-devdb-lock.sh`, `tests/ops/test_devdb_lock.py` |
| L2 | `desk-launch.sh`: `build` and `check` no longer call `lock_free` at launch (`ops/desk/desk-launch.sh` ~428-433, 457, 495, 534); a resume still refuses another worktree's `.env`; `deploy` still refuses while any lock is held; `desk` and `prompt` and `close` unchanged | tests: with a held lock dir and another worktree's `.env`, `build` and `check` reach the stub `claude`; `deploy` is refused. RED on `BASE`: `build` is refused | `ops/desk/desk-launch.sh`, `tests/ops/test_devdb_lock.py` |
| L3 | `prompts/BUILD-HUB.md` and `prompts/CHECK-HUB.md` THE LOCK: the take (`ls`, then `cp`) becomes `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh <WORKTREE> 90`, the release becomes `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh <WORKTREE>`; exit 4 → `FAILED: <step> — cobalt_dev lock not free in 90 min`. PREFLIGHT probes the with-DB strings at W's first take, so a launch never waits at minute one. `prompts/DEPLOY-HUB.md` STEP-G takes the same lock with the same script and holds it to its stop line. The two strings are added to each hub's `--allowedTools` line and to `STANDING-LIST.md`, exactly `Bash(sh /Users/cobalt/.claude/ops/take-devdb-lock.sh *)` and `Bash(sh /Users/cobalt/.claude/ops/release-devdb-lock.sh *)` (his R20 approves these two strings only) | RUN — asserts nothing. `grep -n` every old `ls -la /Users/cobalt/cobalt-wt/*/.env` take step and every `.env` `cp` / `rm` allow string in the three hubs, quote them before and after, and prove no allow line holds a third new string | `prompts/BUILD-HUB.md`, `prompts/CHECK-HUB.md`, `prompts/DEPLOY-HUB.md`, `prompts/STANDING-LIST.md` |
| L4 | RUN — asserts nothing. A worker's report whose last line is an old `FAILED` stays stale after a `CONTINUE`: `BUILD-HUB.md:32` says the worker restores the in-progress last line; quote that text and the check hub's equal, and where a hub keeps the stale line (the guard build did, 07:55 to 08:26 ET). If the file's text is the cause, fix the sentence in the three hubs so the first act after any `CONTINUE` is writing `RESUMED: <step> <time from date>` as the report's last line | — (tool output quoted; the sentence change, if any, is a prompt edit with no test) | `prompts/BUILD-HUB.md`, `prompts/CHECK-HUB.md`, `prompts/DEPLOY-HUB.md` |

## NOT IN THIS JOB
- A scratch database per build: parked (brain's report, A; ADR and tribunal first).
- The symlink install under `/Users/cobalt/.claude/ops/` and the LAWS L76 text: the desk's (LAWS is already amended, in force at install).
- Any other allow string; the other fixed files; `src/`.
- A change to the lock's meaning: still one owner of `cobalt_dev`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/brain-parallel-builds-2026-10-01.md` `## A`.
- `ops/desk/desk-launch.sh` (the `lock_free` calls); `prompts/BUILD-HUB.md` THE LOCK (~line 39) and RECOVERY; the same sections of `CHECK-HUB.md` and `DEPLOY-HUB.md` (STEP-G).
- L76 in `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` (`grep -n "^### L76 "`).

## RECORDS
- His R20 ("Yes, on all four") approves the two strings and the amended L76; its row is committed on `main` with `HIS RULING` and `APPROVED`.
- A fixed file's procedure change is read by one other house before it is installed (L9, L67); the check names it.
