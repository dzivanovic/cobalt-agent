JOB: voice-guard-1001
LADDER: OFF-LADDER — cto-2026-10-01.md 2026-10-01 R41
BRANCH: deploy/voice-guard-1001
WORKTREE: deploy-1001-1
BASE: main
TIP: 76f7f7d5 ee667f3c
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-10-01-1.md
RULINGS: none
TAG: deploy-2026-10-01-1
MIGRATIONS: none
SET: voiceguard

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/voice-peers-1001` | `de483933` | `76f7f7d5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-peers-check-2026-10-01.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `ops/desk-size-guard-1001` | `ee667f3c` | `ee667f3c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-size-guard-check-2026-10-01.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "100.82.85.27" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · before `0` · after `1`
- `grep -c -F -e "--guard" /Users/cobalt/cobalt/ops/desk/wait-stop-line.sh` · before `0` · after `2`
- `grep -c -F "ops/desk/desk-launch.sh" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/ops/test_desk_size_guard.py` · before `No such file or directory` · after listed

## SMOKE READS
- voice peers · `grep -c -F "100.104.48.21" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · exit 0, `1`
- voice peers loopback kept · `grep -c -F "127.0.0.1" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · exit 0, `1`
- size guard launch · `grep -c -F -e "--guard" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- size guard context · `grep -c -F -e "--guard" /Users/cobalt/cobalt/ops/desk/desk-context.sh` · exit 0, a count of 1 or more
- operator classification · `grep -c -F "ops/desk/desk-context.sh" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · exit 0, `1`

## RECORDS
- THE WINDOW (the drafter, 01:58 ET Friday 2026-10-02, `date`): the overnight idle after 21:00 ET Thursday 2026-10-01 (`DEPLOY-HUB.md` P1 (ii)). The outage must begin before 04:00 ET Friday. Thursday was a trading day. No override is cited; `RULINGS` is `none`.
- THE RESTART SET, as the checks' stop lines give it: `RESTARTS: com.cobalt.aset` (`voice-peers-check-2026-10-01.md` last line) and `RESTARTS: com.cobalt.radar` (`desk-size-guard-check-2026-10-01.md` last line, from `src/cobalt/jobs/restarts.py` static import reach). Union `com.cobalt.aset com.cobalt.radar`. The hub derives its own at STEP-R (L42).
- THE CHECKS: voice-peers pass 1 `CHECK DONE · job: voice-peers · pass: 1 · tip: 76f7f7d5 … held: 1 · fixed: 1 · held unfixed: 0 · open: 0 … ready: YES · decisions: 0 · for Dejan: 0`. desk-size-guard pass 2 `CHECK DONE · job: desk-size-guard · pass: 2 · tip: ee667f3c … held: 0 · fixed: 0 · held unfixed: 0 · open: 1 … ready: YES · decisions: 1 · for Dejan: 0`. The one open item is the fence finding O1 / H1 / B1: the `OPS_TOOLS` edit in `src/cobalt/jobs/restarts.py` sits outside the build card's fence. It is not a held defect; the desk's L42 and R127 answer stands.
- HEADS: `git -C /Users/cobalt/cobalt log -1 --format=%h ops/voice-peers-1001` → `76f7f7d5`; `ops/desk-size-guard-1001` → `ee667f3c` (01:58 ET). The voice-peers check's tip is `76f7f7d5`; its head carries the only commit past the last code commit `de483933`, and that commit touches `docs/40 - DevDocs/cobalt/voice/web.md` alone (`git -C /Users/cobalt/cobalt show --stat 76f7f7d5`). The desk-size-guard head is its checked tip.
- MIGRATIONS: `git -C /Users/cobalt/cobalt log --oneline main..ops/voice-peers-1001 -- src/cobalt/db_migrations` and the same for `ops/desk-size-guard-1001` → EMPTY for both. Production stands at 0022 (`deploy-2026-09-30-4b.md`, `migrations applied: all (0022)`, stop line `migrations: 0022`).
- MERGE ORDER `76f7f7d5` then `ee667f3c`. Non-docs paths by `git -C /Users/cobalt/cobalt log --oneline --stat main..<branch> -- . ":(exclude)docs"`: voice-peers → `configs/cobalt/voice.yaml`, `tests/cobalt/test_voice_config.py`, `tests/cobalt/test_voice_web.py`; desk-size-guard → `ops/desk/desk-context.sh`, `ops/desk/desk-launch.sh`, `ops/desk/wait-stop-line.sh`, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/ops/test_desk_size_guard.py`. The two share no file. The `OPS_TOOLS` literal in `src/cobalt/jobs/restarts.py` is edited by `ops/desk-size-guard-1001` only (lines 36–43 of its tree; four entries added). `devdb-lock` (07) edits it too and is not in this set. The `merge-tree` half is the hub's own gate at STEP-T (L68).
- `main` since each branch's cut moved only in `ops/desk/stage-copy.sh` and the nightly rewrite: `git -C /Users/cobalt/cobalt log --oneline ops/voice-peers-1001..main -- . ":(exclude)docs"` and the same for `ops/desk-size-guard-1001` → `d13cc261`, `01bfe67f` for both. A whole-tree `git diff main <branch>` shows `ops/desk/stage-copy.sh` as deleted only because of that move. The branches do not touch it.
- THE WORKTREE, BRANCH AND TAG NAMES ARE FREE (01:58 ET): `ls -d /Users/cobalt/cobalt-wt/deploy-1001-1` → No such file; `rev-parse --verify --quiet refs/heads/deploy/voice-guard-1001`, `refs/tags/deploy-2026-10-01-1` and `refs/tags/pre-voice-guard-1001` → exit 1 each; `ls` of `reports/deploy-2026-10-01-1.md` → No such file.
- NO PRODUCTION `db query` is on this card: `MIGRATIONS` is `none`, so the smoke reads are file reads of the landed tree. The tests are quoted from the gate.
- NOT IN THIS SET: `devdb-lock` (07), `aset-interim-close` (04), `note-daily-stop` (06); each waits on a ruling of his.
