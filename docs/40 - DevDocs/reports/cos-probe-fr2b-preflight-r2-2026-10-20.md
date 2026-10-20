# cos-probe-fr2b preflight r2 — card 923 (read-only)

HEAD `05de58a3` (15:05 EDT, `date`); card BASE `be5fc23d` trails by desk commits only (not a fail; the desk resets it at launch).

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header of `923-…-card.md`; `grep -c -F "«FILL"` | JOB `cos-probe-fr2b`, BRANCH `ops/cos-probe-fr2b`, WORKTREE `cos-probe-fr2b`, REPORT under `cobalt-wt/cos-probe-fr2b/…`, BAND HIGH, `TIP:` empty; `«FILL` → `0` | OK |
| 2 | `ls /Users/cobalt/cobalt-wt/` | no `cos-probe-fr2b` (fresh; `cos-probe-fr2` and `deploy-cos-probe-fr2` are the old job's) | OK |
| 3 | `git diff --numstat 27c35e37..dfea631a` | README 6/0 · build report 193/0 · `.result` 15/0 · probe.py 81/30 · test_cos_probe.py 147/14 (README 6, probe 111, tests 161; 234+/44− on the three) | OK |
| 4 | `git diff --stat 27c35e37 HEAD -- <3 files>`; `-- src tests configs ops` | both empty (main unchanged since the spec base) | OK |
| 5 | `git merge-base --is-ancestor dfea631a HEAD` | exit 0 (why `deploy-card.sh` refuses the old tip) | OK |
| 6 | `BUILD-HUB.md:14`, `:16` vs the card's commands | builder uses `git show`, `git diff`, `uv run pytest`, `uv run cobalt jobs restarts`, `git add`/`git commit`, `Edit(cobalt-wt/**)`; all listed; card denies `git apply`/`cherry-pick`/`mv`/`rm`; "Edit ONLY" now matches `:14` | OK |
| 7 | marker 1 `grep -c -F "under the scratch HOME" probe.py` | main `1`; `git grep -c` on `dfea631a` → nothing (0) → before 1 · after 0 | OK |
| 8 | marker 2 `grep -c -F ".claude.json" probe.py` | main `2`; `dfea631a` → nothing (0) → before 2 · after 0 | OK |
| 9 | marker 3 `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes"` | main `0`; `dfea631a` `1` | OK |
| 10 | marker 4 `grep -c -F "## 2026-10-20 — cos-probe-fr2" README.md` | main `0`; `git grep -c -F … dfea631a` → `2` → before 0 · after 2 | OK |
| 11 | each `## DEPLOY PROOF` line vs `ops/desk/deploy-smoke.sh` `shape()` (lines 114-131) and `plain_path` (100-108) | 4 lines remain, all `grep -c -F "<s>" <path>`; patterns hold no `$`, backtick or backslash; paths are absolute, the README one double-quoted with no shell character. The `grep -n -F` row is gone. | OK |
| 12 | the four RED tests plus the H4 control exist at `dfea631a` | `git grep -n` → lines 288, 429, 452, 469, 503 of `test_cos_probe.py` | OK |
| 13 | E1 forms | `git diff --stat`, `git diff <a> <b> -- paths` are admitted by `git diff *`; (b) empty is a valid equality proof; (c) over `src tests configs ops` is the same form | OK |
| 14 | RESTARTS homes | `configs/cobalt/jobs.yaml:193-203` `com.cobalt.radar` `imports: [cobalt.cli]`; `src/cobalt/cos/cli.py:24` imports `.probe` (static reach); the old deploy's tool run on the same diff gave `com.cobalt.radar`; no per-path entry needed | OK |
| 15 | migrations / RED first | `Migrations: none`; P1 ported first, run RED on BASE `probe.py`, then P2 GREEN | OK |
| 16 | probe at `dfea631a`: credential read and write bounds | `git grep -n -F "open("` → docstring text only (lines 15, 16, 23), no `open(` call; `.claude.json` count 0; writes only `mkdtemp(prefix="cos-probe-")` (209) with `rmtree` (217) and `write_text` inside it (344, 345, 360) | OK |
| 17 | RULINGS | `cto-2026-10-18.md:90` `R1863 … HIS RULING · APPROVED`; route R2185-R2186 in the card | OK |
| 18 | `git diff HEAD --stat -- <card>` | empty | OK |
| 19 | `git diff 04138f61 HEAD -- <card>` | exactly two hunks: the WHY/HOW line (`Edit and Write ONLY` → `Edit ONLY`; "written to those bytes (Write of the whole file, or Edit hunk by hunk" → "brought to those bytes (Edit hunk by hunk") and the removed DEPLOY PROOF `grep -n -F` row. Nothing else changed (BASE, markers 1-4, RESTARTS, RULINGS untouched) | OK |

## ISSUES
- NOTE 1: `BUILD-HUB.md:16` says an `Edit(<glob>)` rule also governs the Write tool, so Write is in fact allowed in the worktree; the card's "Edit hunk by hunk" is stricter than the hub, not in conflict. The builder writes its own report and `.result` with Write, as the hub's `## REPORT` expects.
- NOTE 2: README marker 4 counts both headings (`after 2`), the number the failed deploy had wrong in card 918; the card's `2` matches `dfea631a`.
- Nothing blocks the card's own build.

PREFLIGHT DONE · card: cos-probe-fr2b · checks: 19 · fails: 0 · ready: YES
