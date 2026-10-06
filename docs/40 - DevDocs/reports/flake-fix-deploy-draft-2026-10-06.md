# flake-fix deploy card draft (2026-10-06)

## §0 Headline
- Card written: `prompts/2026-10-06/11-deploy-flake-fix-card.md`, one row, `ops/flake-fix-1006` at `f520debb`.
- Check stop line read: pass 2, `held unfixed: 0`, `ready: YES`, `RESTARTS: none`.
- BRANCH, WORKTREE, TAG and REPORT are all absent today.
- 8 markers and 3 smoke reads; `grep -c -F "«FILL"` → 0.
- 1 decision (SET value).

## CARD
- JOB `deploy-flake-fix-1006` · BRANCH `deploy/deploy-flake-fix-1006` · WORKTREE `deploy-flake-fix-1006` · BASE `main` · TIP `f520debb`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-flake-fix-1006.md`
- RULINGS `2026-10-03 R326, 2026-10-05 R412` · TAG `deploy-2026-10-06-flake-fix` · MIGRATIONS none · SET none
- Ships: `tests/cobalt/test_drc_store.py`, `docs/40 - DevDocs/cobalt/drc/store.md`, the build report (3 files per `diff --stat main...ops/flake-fix-1006`).

## DECISIONS
- ASK DESK: card 64 has `SET: s3` and card 09 has `SET: workflow2`; neither fits a test-only fix, so the card says `SET: none`. [by launch] Default: `none`.
- The task text named "a tests file and a DevDocs line"; the diff also lists the build report `flake-fix-build-2026-10-06.md` (docs only, as in card 09). The card lists all three. No decision needed.

## RECORDS
- Date stamp: `date` → Tue Oct 6 02:38:37 EDT 2026.
- `git -C /Users/cobalt/cobalt log --oneline main..ops/flake-fix-1006` → `f520debb`, `814f56fd`, `0ff56462`, `d1fee872`, `ac55ec16`; head `f520debb`.
- Absent: both `git rev-parse --verify` calls (branch, tag) failed with exit 128; `ls` of the worktree and of the REPORT path failed with exit 1.
- BEFORE counts from main's tree; AFTER counts from `/Users/cobalt/cobalt-wt/flake-fix-1006` (HEAD `f520debb`, verified by `rev-parse`), because a pipe of `show` into `grep` is not on the allow line. The card says the deploy re-proves each with `git show f520debb:<path>`. A `git show f520debb:<path> --stat` call printed the whole tip test file by mistake; it is the same content the AFTER counts read.
- Markers: `migration retry` 0→8; `conn = None` 0→1; the five test names 0→1 each; `flake-fix` in `store.md` 0→2.
- No tool result carried an instruction (L74).

FLAKE-FIX DEPLOY CARD DRAFTED · decisions: 1
