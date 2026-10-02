JOB: scripts-1002
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R37
BRANCH: deploy/scripts-1002
WORKTREE: deploy-1002-2
BASE: main
TIP: 76f7f7d5 24001f82 0c2d9764 30452b64 8914827e e416589c 46712ab4 1ad4c546 dcdd170d
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-10-02-2.md
RULINGS: 2026-10-02 R37, 2026-10-02 R135, 2026-10-02 R148
TAG: deploy-2026-10-02-2
MIGRATIONS: none
SET: scripts

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/voice-peers-1001` | `76f7f7d5` | `76f7f7d5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-peers-check-2026-10-01.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `ops/ops-glob-1002` | `9fa18f14` | `24001f82` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-glob-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 3 | `ops/ops-seam-1002` | `551f07e0` | `0c2d9764` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-seam-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 4 | `ops/desk-tools-a-1002` | `30452b64` | `30452b64` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-a-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 5 | `ops/desk-tools-b-1002` | `8914827e` | `8914827e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-b-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 6 | `ops/worker-steps-1002` | `e416589c` | `e416589c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/worker-steps-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 7 | `ops/devfix-route-1002` | `46712ab4` | `46712ab4` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-route-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 8 | `ops/launcher-checks-1002` | `1ad4c546` | `1ad4c546` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |
| 9 | `s3/x5-tap-refresh-1002` | `2a5fa102` | `dcdd170d` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x5-tap-refresh-check-2026-10-02.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "100.82.85.27" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · before `0` · after `1`
- `grep -c -F "OPS_DESK_PREFIX" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · before `0` · after `2`
- `ls /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh` · before `No such file or directory` · after listed
- `ls /Users/cobalt/cobalt/tests/ops/test_install_ops.py` · before `No such file or directory` · after listed
- `ls /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `No such file or directory` · after listed
- `ls /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `No such file or directory` · after listed
- `ls /Users/cobalt/cobalt/ops/desk/gate.sh` · before `No such file or directory` · after listed
- `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` · before `No such file or directory` · after listed
- `grep -c -F "ships_checked() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "tap_version = conn.execute(" /Users/cobalt/cobalt/src/cobalt/cards/store.py` · before `0` · after `1`

## SMOKE READS
- voice peers · `grep -c -F "100.104.48.21" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · exit 0, `1`
- voice peers loopback kept · `grep -c -F "127.0.0.1" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · exit 0, `1`
- ops/desk rule · `grep -c -F "path.startswith(OPS_DESK_PREFIX)" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · exit 0, `1`
- lock release script · `ls /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh` · exit 0, listed
- install-ops kind · `grep -c -F "install-ops" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- desk tools a · `ls /Users/cobalt/cobalt/ops/desk/install-fixed.sh` · exit 0, listed
- desk tools b · `ls /Users/cobalt/cobalt/ops/desk/gate-clean.sh` · exit 0, listed
- worker steps · `ls /Users/cobalt/cobalt/ops/desk/preflight.sh` · exit 0, listed
- devfix kind · `grep -c -F "devfix)" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- devfix report name class (check O1) · `grep -c -F "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- launcher WATCH line · `grep -c -F "watch_line() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, `1`
- X5 tap version read after the lock · `grep -c -F "taps_moved = int(tap_version) != update.tap_version" /Users/cobalt/cobalt/src/cobalt/cards/store.py` · exit 0, `1`
- X5 with-DB test landed · `ls /Users/cobalt/cobalt/tests/cobalt/test_x5_tap_refresh_db.py` · exit 0, listed

## RECORDS
- THE WINDOW (the drafter, 16:32 ET Friday 2026-10-02, `date`): his per-case window word `cto-2026-10-02.md` R135 (14:45 ET, `HIS RULING` · `APPROVED`, committed `4a9360d2`): the deploy runs after the 16:00 ET close Friday 10-02, as soon as every check of the set is done and READY; the outage is done before 04:00 ET Saturday 10-03. R135 does not name this card's `JOB`; P1 (iv) asks that the row name it — see the drafter's report `## DECISIONS` 2.
- THE RESTART SET, from the checks' stop lines: `RESTARTS: com.cobalt.aset` (`05`), `RESTARTS: com.cobalt.radar` (`15`), `RESTARTS: none` (`16`, `17`, `18`, `19`, `12`, `21`), `RESTARTS: com.cobalt.aset com.cobalt.radar` (`22`). Union `com.cobalt.aset com.cobalt.radar`. The hub derives its own at STEP-R (L42).
- THE CHECKS, each the last line of its report (16:28 ET):
  - `05` `CHECK DONE · job: voice-peers · pass: 1 · tip: 76f7f7d5 · house A: Grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3777/0 · with-DB 4547/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0`
  - `15` `CHECK DONE · job: ops-glob · pass: 1 · tip: 9fa18f14 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0`
  - `16` `CHECK DONE · job: ops-seam · pass: 1 · tip: 551f07e0 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0`
  - `17` `CHECK DONE · job: desk-tools-a · pass: 1 · tip: 30452b64 · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0`
  - `18` `CHECK DONE · job: desk-tools-b · pass: 1 · tip: 8914827e · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0`
  - `19` `CHECK DONE · job: worker-steps · pass: 1 · tip: e416589c · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0`
  - `12` `CHECK DONE · job: devfix-route · pass: 1 · tip: 46712ab4 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0`
  - `21` `CHECK DONE · job: launcher-checks · pass: 1 · tip: 1ad4c546 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0`
  - `22` `CHECK DONE · job: x5-tap-refresh · pass: 1 · tip: 2a5fa102 · house A: Grok FINDINGS: 0 · findings: 0 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0`
  - `15`'s one open item is O3 (a rename into `ops/desk/` drops the old path in `changes()`); the judge seat moved it to tomorrow's list (`brain-direction-2026-10-02.md` `## TOMORROW`, "rename follow-up"). `22`'s one decision is an ASK DESK on another job's lock; this check took no lock. Neither is a held defect.
- EVERY CHECK REPORT IS COMMITTED ON `main` (`git -C /Users/cobalt/cobalt log -1 --format=%h -- <path>`, 16:30 ET): `05` `0985506c`, `15` `163f7856`, `16` `20769c97`, `17` `c99f6fb0`, `18` `99ecfe74`, `19` `08efcbe8`, `12` `47cf2850`, `21` `04780275`, `22` `7d5a231e`. None of the nine is dirty (`git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports"` names none of them).
- HEADS (`git -C /Users/cobalt/cobalt log -1 --format=%h <branch>`, 16:29 ET), in merge order: `05` `76f7f7d5` = tip · `15` `24001f82`, past `9fa18f14` by `24001f82` (`ops-glob-build-2026-10-02.md` only) · `16` `0c2d9764`, past `551f07e0` by `0c2d9764` (`ops-seam-build-2026-10-02.md` only) · `17` `30452b64` = tip · `18` `8914827e` = tip · `19` `e416589c` = tip · `12` `46712ab4` = tip · `21` `1ad4c546` = tip · `22` `dcdd170d`, past `2a5fa102` by `dcdd170d` (`x5-tap-refresh-build-2026-10-02.md` only). Each past-tip commit is docs only (`git -C /Users/cobalt/cobalt log --oneline --stat <tip>..<branch>`).
- MERGE ORDER AND STACKS: `16`, `17`, `18`, `19` stand on `15`'s checked tip `9fa18f14`. `12` stands on `16`'s checked tip `551f07e0`. `21` stands on `12`'s OLD head `63649058`: `git -C /Users/cobalt/cobalt merge-base --is-ancestor 63649058 ops/launcher-checks-1002` → exit 0, and `… --is-ancestor 46712ab4 ops/launcher-checks-1002` → exit 1, so `21` does NOT carry `12`'s check commits (`1df6759e`, `46712ab4`); both heads ship, `12` merged first (R121).
- FILES TWO SHIPS BOTH CHANGE (the `merge-tree` half is the hub's own gate at STEP-T, L68):
  - `12` × `21` after `63649058`: `ops/desk/desk-launch.sh` (`12`: `46712ab4`, one line at 648 of `63649058`; `21`: `a2dd9400`, `039ccab9`, `1ad4c546`, hunks at 2, 70, 110, 167–182, 259, 485, 506, 561–567, 606, 717–731) and `tests/ops/test_desk_launch_devfix.py` (`12`: `1df6759e`, insert after line 243; `21`: `a2dd9400`, insert after line 89). No hunk overlaps.
  - `16` × `22`: `docs/40 - DevDocs/prompts/BUILD-HUB.md` (`16`: lines 8–106 by its port commits; `22`: lines 84 and 88, its TREE STATE row) and `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (`16`: lines 8–113 and 180; `22`: lines 105 and 109). Both branches edit the same blobs (`88a9fce3`, `c95b23dc`). The closest pair is `22`'s line 109 and `16`'s lines 111–113: one unchanged line between.
  - `16` × `main` `5bf129ae` (the NO OUTSIDE HOUSE line): `docs/40 - DevDocs/prompts/CHECK-HUB.md`; `main` inserts after line 27, `16` edits lines 8, 10, 12, 52, 56, 65, 114, 118.
  - `17`, `18`, `19` add new files only, disjoint from each other and from the rest. `05` and `15` share no file with another ship.
- `main` SINCE EACH BASE (`git -C /Users/cobalt/cobalt log --oneline <base>..main -- . ":(exclude)docs"`): since `05`'s base `446ff64d`: `1a5f22e2`, `b8bf83eb`, `d13cc261`, `fb0922a9`, `4898ceaa`, `01bfe67f`, `5ed7c3fd`, `c1834c74` (ASET `src/cobalt/aset/`, its tests, `ops/desk/stage-copy.sh`, the nightly rewrite); none touches `configs/cobalt/voice.yaml` or `tests/cobalt/test_voice_*.py`. Since `15`'s base `a0188b69` and `22`'s base `53a85f27`, outside reports and cards: `c858b0c8` (`CTO-DESK-WAKEUP.md`) and, for `15` only, `5bf129ae` (`CHECK-HUB.md`, above); no shipped code path.
- MIGRATIONS: `git -C /Users/cobalt/cobalt log --oneline main..<branch> -- src/cobalt/db_migrations` → EMPTY for all nine ships (`launcher-checks` read stands for `15`, `16`, `12`, `21`, which it carries). Production stands at 0022 (`deploy-2026-10-02-1.md` line 241; its stop line `migrations: none`).
- TREE STATE: `22` adds the with-DB file `tests/cobalt/test_x5_tap_refresh_db.py` and its row edits the pass-1 / pass-2 lines of `BUILD-HUB.md` and `DEPLOY-HUB.md` (deselect in pass 1, run in pass 2). The gate reads `main`'s lines and adds the deselects the set's build reports name (STEP-G (c)).
- `tests/ops/` is new in this set (`ls /Users/cobalt/cobalt/tests/ops` → No such file, 16:31 ET); STEP-G runs `tests/cobalt tests/taxonomy` and does not run it. The checks ran it on each branch.
- NAMES FREE (16:31 ET): `ls -d /Users/cobalt/cobalt-wt/deploy-1002-2` → No such file; `rev-parse --verify --quiet` of `refs/heads/deploy/scripts-1002`, `refs/tags/deploy-2026-10-02-2`, `refs/tags/pre-scripts-1002` → exit 1 each; `ls` of `reports/deploy-2026-10-02-2.md` → No such file. `deploy-2026-10-02-1` was the ASET deploy.
- NO PRODUCTION `db query` is on this card: `MIGRATIONS` is `none`; the smoke reads are file reads of the landed tree.
- NOT IN THIS SET: `11` dev-rebuild (`07cc965f`) and `13` slot-guard (`834d4c69`) — see the drafter's report `## DECISIONS` 1. `06` note-daily-stop: check not done at 16:32 ET (`note-daily-stop-check-2026-10-01.md` last line `(run in progress — next step under ## CONTINUE)`); the desk adds its row if it reads READY.
- AFTER DEPLOYED: the desk runs `sh /Users/cobalt/.claude/ops/desk-launch.sh install-ops` (built in `16`) before any launch; no build or check is launched until it has run. His one install after DEPLOYED is the `bare-guard.py` hook entry in `.claude/settings.json`; the brain hands him the text. Then the close: `desk-launch.sh close 2026-10-02` after this deploy's stop line (direction row 7).
- THE JUDGE SEAT'S FLAKE RULE (2026-10-02 R41, desk row R129), byte for byte: "A gate red ONLY on a `DeadlockDetected` at setup of a test whose `migrated` fixture applies a migration (an `ALTER TABLE … OWNER TO` or another DDL of `0002`), where that test passes alone, is the known flake: re-run that pass once in the same take and quote both runs; a deploy that ended FAILED on it is re-cut once with fresh gate names, no ask. A second red on it, or any other red, is a real FAILED."
