# 07b card preflight — round 2 (2026-10-03)

Card: `prompts/2026-10-03/07b-desk-tools-port-card.md`. BASE `5ff16b1f`. Sources: `07` head `b5eb3530`, `09` head `a6bef8cb`, both on base `a09f0862`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `rev-parse --verify 5ff16b1f^{commit}` | `5ff16b1fcd8dc57249fad9633f2f9a53cea34f91` | OK |
| 1b | `merge-base --is-ancestor 5ff16b1f ops/adoption-port-1003` | exit 0, no output | OK |
| 1c | `rev-parse --verify` for `b5eb3530`, `a6bef8cb`, `a09f0862` | `b5eb35300a8f…`, `a6bef8cb64f3…`, `a09f08622ac8…` | OK |
| 1d | `merge-base` of `b5eb3530`, `a6bef8cb` with each other and with BASE | all `a09f08622ac8…` (the card's stated base) | OK |
| 2a | `rev-parse --verify ops/desk-tools-port-1003` | `fatal: Needed a single revision` (branch absent) | OK |
| 2b | `ls /Users/cobalt/cobalt-wt/desk-tools-port-1003` | `No such file or directory` | OK |
| 3a | `diff --name-only a09f0862 b5eb3530` (07) | 7 files: `08-brain-handover.md`, `BRAIN-HUB.md`, `STANDING-LIST.md`, `brain-hub-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_size_guard.py` | OK |
| 3b | `diff --name-only a09f0862 a6bef8cb` (09) | 8 files: `worker-watch-build-2026-10-03.md`, `ops/desk/desk-watch.sh`, `idle-wake.py`, `stop-guard.py`, `wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `test_idle_wake.py`, `test_stop_guard.py` | OK |
| 3c | `diff --name-only a09f0862 5ff16b1f` (BASE since base) | 130+ paths (full list run) | OK |
| 3d | intersections | 07 ∩ BASE = `STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_size_guard.py`. 09 ∩ BASE = `ops/desk/desk-watch.sh`, `ops/desk/wait-stop-line.sh`. Rows: P1 (`desk-launch.sh`), P3 (`STANDING-LIST.md`, `test_desk_size_guard.py`), P2 (`desk-watch.sh`, `wait-stop-line.sh`) | OK |
| 4 | `ls-tree` for the red-first tests | `test_desk_launch_brain.py` at `b5eb3530`; `test_desk_watch.py`, `test_stop_guard.py`, `test_idle_wake.py` at `a6bef8cb`; each in its source's ported set | OK |
| 5a | `git grep -c -F "## 7. BRAIN-HUB.md"` `STANDING-LIST.md` at `b5eb3530` | no match. The heading at line 218 is ``## 7. `BRAIN-HUB.md` — THE STANDING BRAIN SEAT…`` (backticked). BASE has no `BRAIN-HUB` at all. The card's `grep -c -F "## 7. BRAIN-HUB.md"` → 1 can never hold | FAIL |
| 5b | `git grep -F recut` / `TREE STATE` at BASE `desk-launch.sh` | `recut` kind (:848), optional TREE STATE (`:508` `grep -q '^TREE STATE:' … \|\| return 0`), unknown-kind refusal at :437 listing `build, check, deploy, devfix, recut, desk, prompt, close, install-ops`. The card says "now lists `recut` and `brain`": `recut` is already there, `brain` is the add | OK |
| 5c | row ids | the card has two rows labelled `P3` (the shared-path merge and the install text). The card's RECORDS and the round-1 preflight cite "row P3" for the two shared paths | FAIL |
| 5d | X3: `grep -n -F /Users/cobalt/cobalt a6bef8cb:ops/desk/stop-guard.py` | line 5: cwd not under `/Users/cobalt/cobalt-wt/<worktree>` → exit 0 (desk and brain exempt); `bare-guard.py` exists at BASE, `stop-guard.py` and `idle-wake.py` come from `09` | OK |
| 6 | `ls` the `## READ` files | `07-brain-hub-card.md`, `09-worker-watch-card.md`, `brain-hub-check-2026-10-03-r2.md`, `worker-watch-check-2026-10-03-r2.md`, `07b-card-preflight-2026-10-03.md` all exist | OK |
| 7 | `grep -n "^| R<n> "` in `cto-2026-10-02.md` | R47 `HIS RULING · APPROVED`; R154 `HIS RULING · APPROVED`; R157 `HIS RULING · APPROVED` | OK |
| 8 | `git grep -n` in `restarts.py` at BASE | `:38 OPS_DESK_PREFIX = "ops/desk/"`, `:228 "DOCS"`, `:246 rule = "test/documentation; no resident"`. All three cites hold; no `src/`, no `configs/` | OK |
| 9 | TREE STATE / DB / header | no with-DB test or migration (files under `ops/`, `tests/ops/`, `docs/`) so `TREE STATE: unchanged`, `DB: none` hold; `HOUSE B: as needed` filled; `grep -c -F "«FILL"` → 0 | OK |

## ISSUES

- FAIL 5a: row P3 (shared files) says `grep -c -F "## 7. BRAIN-HUB.md"` → 1; the heading is ``## 7. `BRAIN-HUB.md` …`` with backticks, so that string counts 0. Use ``grep -c -F "## 7. `BRAIN-HUB.md`"``.
- FAIL 5c: two rows are labelled `P3` (shared-path merge, and the install text); rename one (e.g. `P4`) and fix the RECORDS cite.

PREFLIGHT DONE · card: 07b · checks: 17 · fails: 2 · ready: NO
