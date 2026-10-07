# Worktree survey 2026-10-07

## §0 Headline
- Trees surveyed: 113 under `/Users/cobalt/cobalt-wt` (main checkout excluded).
- LANDED-CLEAN 86 · UNMERGED-CLEAN 25 · DIRTY 1 (`heartbeat-note-absent`) · ENV 0 · KEEP 1 (`agy-trial`, also 2 untracked lines).
- RECENT (last commit dated 2026-10-07): 9, all LANDED-CLEAN; the desk checks them by hand (flag is by date, not by hour).
- No `.env` in any tree. Nothing was changed.

## TABLE
Columns: tree · branch · merged · ahead · unsaved · .env · last commit · class. Last commit is the branch tip's date.

| tree | branch | merged | ahead | unsaved | .env | last commit | class |
|---|---|---|---|---|---|---|---|
| adoption-hubs-1003 | ops/adoption-hubs-1003 | no | 19 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| adoption-port-1003 | ops/adoption-port-1003 | yes | 0 | 0 | no | 2026-10-04 | LANDED-CLEAN |
| adoption-scripts-1003 | ops/adoption-scripts-1003 | no | 9 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| adoption-scripts-b-1003 | ops/adoption-scripts-b-1003 | no | 11 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| adoption-scripts-b2-1003 | ops/adoption-scripts-b2-1003 | no | 20 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| agy-trial | ops/agy-trial-0915 | no | 8 | 2 | no | 2026-09-15 | KEEP |
| agy-trial-rebuilt | ops/agy-trial-0915-rebuilt | yes | 0 | 0 | no | 2026-09-17 | LANDED-CLEAN |
| aset-interim-close-1001 | s3/aset-interim-close-1001 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| bars-chunk-1a | bars/chunk-1a-0920 | no | 20 | 0 | no | 2026-09-20 | UNMERGED-CLEAN |
| bars-chunk-2 | bars/chunk-2-0920 | no | 17 | 0 | no | 2026-09-21 | UNMERGED-CLEAN |
| bars-chunk-e | bars/chunk-e-0920 | no | 8 | 0 | no | 2026-09-20 | UNMERGED-CLEAN |
| brain-hub-1003 | ops/brain-hub-1003 | no | 12 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| close-timer-1003 | ops/close-timer-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| cobalt-guard-1004 | ops/cobalt-guard-1004 | yes | 0 | 0 | no | 2026-10-04 | LANDED-CLEAN |
| cobalt-guard-b-1004 | ops/cobalt-guard-b-1004 | yes | 0 | 0 | no | 2026-10-04 | LANDED-CLEAN |
| degraded-line | s2/degraded-line-0921 | yes | 0 | 0 | no | 2026-09-21 | LANDED-CLEAN |
| deploy-0930-1 | deploy/drc-0930 | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| deploy-0930-2 | deploy/s3-0930 | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| deploy-0930-3 | deploy/e1-0930 | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| deploy-0930-4 | deploy/f15-e1-0930 | yes | 0 | 0 | no | 2026-10-01 | LANDED-CLEAN |
| deploy-0930-5 | deploy/f15-e1-0930b | yes | 0 | 0 | no | 2026-10-01 | LANDED-CLEAN |
| deploy-1001-1 | deploy/voice-guard-1001 | no | 10 | 0 | no | 2026-10-02 | UNMERGED-CLEAN |
| deploy-1002-1 | deploy/aset-interim-close-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| deploy-1002-2 | deploy/scripts-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| deploy-1003-1 | deploy/set1-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| deploy-1003-2 | deploy/set2-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| deploy-1003-3 | deploy/set2b-1003 | no | 3 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| deploy-1003-4 | deploy/set2c-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| deploy-1003-5 | deploy/set2d-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| deploy-1004-1 | deploy/set3-1004 | no | 4 | 0 | no | 2026-10-04 | UNMERGED-CLEAN |
| deploy-1004-2 | deploy/set3b-1004 | yes | 0 | 0 | no | 2026-10-04 | LANDED-CLEAN |
| deploy-1005-1-attempt2 | deploy/s3-1005-attempt2 | no | 4 | 0 | no | 2026-10-05 | UNMERGED-CLEAN |
| deploy-desk-stop-guard-1007 | deploy/desk-stop-guard-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| deploy-drc-d5-o1-b2-1006-attempt2 | deploy/deploy-drc-d5-o1-b2-1006-attempt2 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| deploy-flake-fix-2-1006 | deploy/deploy-flake-fix-2-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| deploy-guard-b-1005 | deploy/deploy-guard-b-1005 | yes | 0 | 0 | no | 2026-10-05 | LANDED-CLEAN |
| deploy-guard-g2-1006 | deploy/deploy-guard-g2-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| deploy-hub-text-1003 | ops/deploy-hub-text-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| deploy-launcher-next-flow-1006 | deploy/launcher-next-flow-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| deploy-radar-arm-disarm-1007 | deploy/radar-arm-disarm-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| deploy-radar-direction-color-1007-attempt2 | deploy/radar-direction-color-1007-attempt2 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| deploy-radar-ladder-refresh-1006 | deploy/deploy-radar-ladder-refresh-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| deploy-steps-1003 | ops/deploy-steps-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| deploy-worktree-salvage-1007 | deploy/worktree-salvage-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| desk-size-guard-1001 | ops/desk-size-guard-1001 | no | 8 | 0 | no | 2026-10-01 | UNMERGED-CLEAN |
| desk-stop-guard-1006b | ops/desk-stop-guard-1006b | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| desk-tools-a-1002 | ops/desk-tools-a-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| desk-tools-b-1002 | ops/desk-tools-b-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| desk-tools-port-1003 | ops/desk-tools-port-1003 | yes | 0 | 0 | no | 2026-10-04 | LANDED-CLEAN |
| dev-rebuild-1002 | ops/dev-rebuild-1002 | no | 7 | 0 | no | 2026-10-02 | UNMERGED-CLEAN |
| dev-rebuild-port-1003 | ops/dev-rebuild-port-1003 | yes | 0 | 0 | no | 2026-10-04 | LANDED-CLEAN |
| devdb-lock-1001 | ops/devdb-lock-1001 | no | 7 | 0 | no | 2026-10-01 | UNMERGED-CLEAN |
| devfix-aset-sizings-1007 | ops/devfix-aset-sizings-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| devfix-route-1002 | ops/devfix-route-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| drc-d1 | drc/d1-trading-log | no | 1 | 0 | no | 2026-09-29 | UNMERGED-CLEAN |
| drc-d5-1004 | drc/d5-reconcile-1004 | yes | 0 | 0 | no | 2026-10-05 | LANDED-CLEAN |
| drc-d5-o1-b2-1006 | ops/drc-d5-o1-b2-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| drc-k3-1004 | drc/k3-surfaces-1004 | yes | 0 | 0 | no | 2026-10-05 | LANDED-CLEAN |
| e1-fix-0930 | s3/e1-fix-0930 | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| e1-inline-0930 | s3/e1-inline-0930 | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| f15-p1-0930 | f15/p1-records | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| f15-p2-1004 | f15/p2-replay-1004 | yes | 0 | 0 | no | 2026-10-05 | LANDED-CLEAN |
| flake-fix-2-1006 | ops/flake-fix-2-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| grok-deny | ops/grok-deny-0915 | yes | 0 | 0 | no | 2026-09-17 | LANDED-CLEAN |
| guard-g2-1006 | ops/guard-g2-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| handicap-h1 | radar/handicap-h1-0922 | yes | 0 | 0 | no | 2026-09-25 | LANDED-CLEAN |
| heartbeat-mr | ops/heartbeat-market-reset | yes | 0 | 0 | no | 2026-09-10 | LANDED-CLEAN |
| heartbeat-note-absent | heartbeat/note-absent | yes | 0 | 1 | no | 2026-09-12 | DIRTY |
| jev-trial | jev/trial-0923 | no | 27 | 0 | no | 2026-09-23 | UNMERGED-CLEAN |
| launcher-checks-1002 | ops/launcher-checks-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| launcher-fixround-1005 | ops/launcher-fixround-1005 | yes | 0 | 0 | no | 2026-10-05 | LANDED-CLEAN |
| launcher-next-flow-1006 | ops/launcher-next-flow-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| lock-relief-1003 | ops/lock-relief-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| mover-bars | replay/mover-partial-0924 | yes | 0 | 0 | no | 2026-09-24 | LANDED-CLEAN |
| note-daily-stop-1001 | s3/note-daily-stop-1001 | no | 6 | 0 | no | 2026-10-02 | UNMERGED-CLEAN |
| ops-0921 | ops/2026-09-21 | yes | 0 | 0 | no | 2026-09-22 | LANDED-CLEAN |
| ops-2026-09-15 | ops/2026-09-15 | yes | 0 | 0 | no | 2026-09-16 | LANDED-CLEAN |
| ops-2026-09-16 | ops/2026-09-16 | yes | 0 | 0 | no | 2026-09-16 | LANDED-CLEAN |
| ops-2026-09-17 | ops/2026-09-17 | yes | 0 | 0 | no | 2026-09-17 | LANDED-CLEAN |
| ops-2026-09-18 | ops/2026-09-18 | yes | 0 | 0 | no | 2026-09-18 | LANDED-CLEAN |
| ops-day-open | ops/day-open | yes | 0 | 0 | no | 2026-09-15 | LANDED-CLEAN |
| ops-glob-1002 | ops/ops-glob-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| ops-seam-1002 | ops/ops-seam-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| order-open-test-1003 | ops/order-open-test-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| page-bars-hotfix | s2/page-bars-hotfix-0921 | yes | 0 | 0 | no | 2026-09-21 | LANDED-CLEAN |
| panel-order | s2/panel-order-0921 | yes | 0 | 0 | no | 2026-09-21 | LANDED-CLEAN |
| radar-arm-disarm-1007 | ops/radar-arm-disarm-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| radar-direction-color-1007 | ops/radar-direction-color-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| radar-ladder-refresh-1006 | ops/radar-ladder-refresh-1006 | yes | 0 | 0 | no | 2026-10-06 | LANDED-CLEAN |
| radar-stop-record | radar/stop-record-0928 | no | 7 | 0 | no | 2026-09-28 | UNMERGED-CLEAN |
| rename-follow-up-1003 | ops/rename-follow-up-1003 | yes | 0 | 0 | no | 2026-10-03 | LANDED-CLEAN |
| replay-deadline | fix/replay-deadline-0924 | yes | 0 | 0 | no | 2026-09-25 | LANDED-CLEAN |
| rubberband-proof | s2/rubberband-proof-0921 | no | 2 | 0 | no | 2026-09-21 | UNMERGED-CLEAN |
| s2-p2-cards | sprint-2/stack | yes | 0 | 0 | no | 2026-09-19 | LANDED-CLEAN |
| s2-p3-radar-panel | sprint-2/radar-panel | yes | 0 | 0 | no | 2026-09-15 | LANDED-CLEAN |
| s2-smoke-fix | s2/smoke-fix-0922 | yes | 0 | 0 | no | 2026-09-23 | LANDED-CLEAN |
| s3-exits-c1 | s3/exits-c1 | yes | 0 | 0 | no | 2026-09-28 | LANDED-CLEAN |
| s3-exits-c2 | s3/exits-c2 | no | 1 | 0 | no | 2026-09-28 | UNMERGED-CLEAN |
| s3-exits-c3 | s3/exits-c3 | no | 1 | 0 | no | 2026-09-29 | UNMERGED-CLEAN |
| s3-exits-c4 | s3/exits-c4 | no | 1 | 0 | no | 2026-09-29 | UNMERGED-CLEAN |
| seam-0930 | seam/drc-s3-0930 | yes | 0 | 0 | no | 2026-09-30 | LANDED-CLEAN |
| setups-c1 | setups/seven-0921 | yes | 0 | 0 | no | 2026-09-24 | LANDED-CLEAN |
| slot-guard-1002 | ops/slot-guard-1002 | no | 10 | 0 | no | 2026-10-02 | UNMERGED-CLEAN |
| stacked-0923 | deploy/stacked-0923 | yes | 0 | 0 | no | 2026-09-24 | LANDED-CLEAN |
| stacked-0925 | deploy/stacked-0925 | yes | 0 | 0 | no | 2026-09-27 | LANDED-CLEAN |
| stale-marker | s2/stale-marker-0921 | yes | 0 | 0 | no | 2026-09-22 | LANDED-CLEAN |
| stale-score | cards/stale-score-0922 | yes | 0 | 0 | no | 2026-09-24 | LANDED-CLEAN |
| voice-peers-1001 | ops/voice-peers-1001 | yes | 0 | 0 | no | 2026-10-01 | LANDED-CLEAN |
| voice-v1 | voice/v1-0923 | yes | 0 | 0 | no | 2026-09-24 | LANDED-CLEAN |
| worker-steps-1002 | ops/worker-steps-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |
| worker-watch-1003 | ops/worker-watch-1003 | no | 8 | 0 | no | 2026-10-03 | UNMERGED-CLEAN |
| worktree-salvage-1007 | ops/worktree-salvage-1007 | yes | 0 | 0 | no | 2026-10-07 | LANDED-CLEAN · RECENT |
| x5-tap-refresh-1002 | s3/x5-tap-refresh-1002 | yes | 0 | 0 | no | 2026-10-02 | LANDED-CLEAN |

Notes:
- Dirty detail: `agy-trial` has 2 untracked lines (`docs/.../audit-house-2026-09-16.md`, `tmp/`); `heartbeat-note-absent` has 1 modified file (`docs/.../heartbeat-note-absent-2026-09-12.md`).
- All dates are branch-tip dates from `git branch --format`. Same-day commits cannot be told apart from the last 12 hours, so every 2026-10-07 branch is marked RECENT.

## RECORDS
- `git -C /Users/cobalt/cobalt worktree list` (main plus 113 trees).
- `git -C /Users/cobalt/cobalt branch --merged main` (merged yes/no).
- `git -C /Users/cobalt/cobalt branch --format='%(refname:short) %(ahead-behind:main) %(committerdate:short)'` (ahead count and last commit date for every branch, in one call).
- `ls /Users/cobalt/cobalt-wt/*/.env`: no match in any tree.
- `git -C <tree> status --porcelain` for each of the 113 trees. Only `agy-trial` (2 lines) and `heartbeat-note-absent` (1 line) printed anything.
- No git write, no launch, no delete. The only file written is this report.

WORKTREE SURVEY DONE · trees: 113 · landed-clean: 86 · unmerged-clean: 25 · dirty: 1 · env: 0 · keep: 1 · recent: 9
