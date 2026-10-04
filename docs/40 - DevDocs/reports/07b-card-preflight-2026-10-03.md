# 07b card preflight — 2026-10-03

Card: `prompts/2026-10-03/07b-desk-tools-port-card.md`. BASE `5ff16b1f`. Sources: `07` (base `a09f0862`, header TIP `bb930cac`, branch head `b5eb3530`), `09` (base `a09f0862`, header TIP `1bfd26e3`, branch head `a6bef8cb`).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `rev-parse --verify 5ff16b1f^{commit}` · `merge-base --is-ancestor 5ff16b1f ops/adoption-port-1003` · `rev-parse --verify a09f0862^{commit}` / `bb930cac^{commit}` / `1bfd26e3^{commit}` · `log --oneline bb930cac..ops/brain-hub-1003` · `log --oneline 1bfd26e3..ops/worker-watch-1003` | `5ff16b1fcd8d…` · exit 0 (ancestor) · `a09f0862…` / `bb930cac…` / `1bfd26e3…` all resolve · `b5eb3530` fix O1, `03ce2125`, `46bd070e` sit past 07's TIP · `a6bef8cb` fix O1/O2, `e296a7cc`, `82db3ade` sit past 09's TIP. The card names no source hash: "`07` tip" / "`09` tip" only; the sources' header TIPs are the unchecked builds, the checked heads are later (`b5eb3530`, `a6bef8cb`). | FAIL |
| 2 | `rev-parse --verify ops/desk-tools-port-1003` · `ls /Users/cobalt/cobalt-wt/` | `fatal: Needed a single revision` (branch absent) · no `desk-tools-port-1003` in the listing | OK |
| 3 | `diff --name-only a09f0862 <head>` for 07, 09, and `a09f0862 5ff16b1f` | **07 files:** `docs/…/prompts/2026-10-03/08-brain-handover.md`, `docs/…/prompts/BRAIN-HUB.md`, `docs/…/prompts/STANDING-LIST.md`, `docs/…/reports/brain-hub-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_size_guard.py`. **09 files:** `docs/…/reports/worker-watch-build-2026-10-03.md`, `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py`. **BASE since `a09f0862`:** 142 paths (incl. `STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `desk-watch.sh`, `wait-stop-line.sh`, `tests/ops/test_desk_size_guard.py`). **Intersection 07:** `docs/…/prompts/STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_size_guard.py`. **Intersection 09:** `ops/desk/desk-watch.sh`, `ops/desk/wait-stop-line.sh`. Rows P1/P2 hand-merge only `desk-launch.sh`, `desk-watch.sh`, `wait-stop-line.sh`; `STANDING-LIST.md` and `test_desk_size_guard.py` get "from `git show <07 tip>:<path>`, hash-proven", which would overwrite BASE's changes. | FAIL |
| 4 | red-first tests: `test_desk_launch_brain.py` (absent at BASE, in 07's set), `test_desk_watch.py`, `test_idle_wake.py`, `test_stop_guard.py` (in 09's set) | each exists at its source head and is in `07's files` / `09's files` | OK |
| 5 | cites: unknown-kind refusal at BASE `desk-launch.sh:437` `kind '$kind' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops` (no `brain`, so the card's "now lists `recut` and `brain`" is a to-do, not a stale cite); `recut` kind `:848`; `-r2` check reports hold B5 (brain) and O1/O2 (watch); `O6` is in `worker-watch-check-2026-10-03.md` (7 hits), not in `-r2` | cites hold | OK |
| 6 | `ls` the `## READ` files: `07-brain-hub-card.md`, `09-worker-watch-card.md`, `brain-hub-check-2026-10-03-r2.md`, `worker-watch-check-2026-10-03-r2.md`; `grep -n -F "## §0"` | all four exist; `## §0 Headline` at `:3` in both | OK |
| 7 | `grep -n -E "^\| R(47\|157\|154) " cto-2026-10-02.md` | `:54 R47 … HIS RULING · APPROVED` · `:161 R154 … HIS RULING · APPROVED` · `:164 R157 … HIS RULING · APPROVED` | OK |
| 8 | `git show 5ff16b1f:src/cobalt/jobs/restarts.py`; `grep -n -F` on the adoption-port worktree (restarts.py identical to BASE: `diff --stat 5ff16b1f bd19a0b3 -- src/cobalt/jobs/restarts.py` empty) | `:38 OPS_DESK_PREFIX = "ops/desk/"` holds · `:228 … "DOCS"` (card says `:219`) · `:246 rule = "test/documentation; no resident"` (card says `:239`) · homes exist for ops/desk, tests/ops, docs | FAIL |
| 9 | ported set vs header | no `src/`, migration or with-DB test in either set; all paths under `ops/`, `tests/ops/`, `docs/`, so `TREE STATE: unchanged` and `DB: none` hold · `HOUSE B: as needed` filled · `grep -c -F "«FILL"` → `0` | OK |

## ISSUES
- #1 FAIL: the card names no source head; "07 tip" / "09 tip" read from the 07/09 headers are `bb930cac` / `1bfd26e3`, which lack the check fixes `b5eb3530` (07, the O1 `prompt`-kind fix) and `a6bef8cb` (09, O1/O2). Name the heads, `b5eb3530` and `a6bef8cb`, in P1/P2.
- #3 FAIL: shared path `docs/40 - DevDocs/prompts/STANDING-LIST.md` has no hand-merge row (changed by 07 and by BASE).
- #3 FAIL: shared path `tests/ops/test_desk_size_guard.py` has no hand-merge row (changed by 07 and by BASE).
- #8 FAIL: `## RECORDS` cites `restarts.py:219` (DOCS) and `:239` (test/documentation); at BASE they are `:228` and `:246`.

PREFLIGHT DONE · card: 07b · checks: 9 · fails: 3 · ready: NO
