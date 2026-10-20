# cos-probe-fr2b preflight — card 923 (read-only)

HEAD `04138f61`; card BASE `be5fc23d` (trails by desk commits only; not a fail).

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header of `923-…-card.md` | JOB `cos-probe-fr2b`, BRANCH `ops/cos-probe-fr2b`, WORKTREE `cos-probe-fr2b`, REPORT under `cobalt-wt/cos-probe-fr2b/…`, BAND HIGH, `TIP:` empty; `grep -c -F "«FILL"` → `0` | OK |
| 2 | `ls /Users/cobalt/cobalt-wt/` | no `cos-probe-fr2b` (fresh) | OK |
| 3 | `git diff --numstat 27c35e37..dfea631a` | README 6/0 · probe.py 81/30 · test_cos_probe.py 147/14 · build report 193/0 · `.result` 15/0 (README 6, probe 111, tests 161; 234+/44− on the three) | OK |
| 4 | `git diff --stat 27c35e37 HEAD -- <3 files>` and `-- src tests configs ops` | both empty (main unchanged on them) | OK |
| 5 | `git merge-base --is-ancestor dfea631a HEAD` | exit 0 (why a plain re-merge is refused) | OK |
| 6 | `BUILD-HUB.md:14` vs the card's commands | allows `Edit(cobalt-wt/**)`, `git show*`, `git diff *`, `uv run pytest *`, `uv run cobalt jobs restarts *`, `git add/commit`; card uses only these and denies `git apply`/`cherry-pick`/`mv`/`rm` | OK (see NOTE 1) |
| 7 | marker 1 `grep -c -F "under the scratch HOME" probe.py` | main `1`; `dfea631a` none (0) → before 1 · after 0 | OK |
| 8 | marker 2 `grep -c -F ".claude.json" probe.py` | main `2`; `dfea631a` none (0) → before 2 · after 0 | OK |
| 9 | marker 3 `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes"` | main `0`; `dfea631a` `1` | OK |
| 10 | marker 4 `grep -c -F "## 2026-10-20 — cos-probe-fr2" README.md` | main `0`; `git grep -c` on `dfea631a` → `2` (lines 52, 55) → before 0 · after 2 | OK |
| 11 | marker 5 `grep -n -F …` row vs `ops/desk/deploy-smoke.sh` `shape()` (lines 114-146) | mapped forms are `ls`, `grep -c -F "…"`, `curl`, `db query`; `grep -n -F` is NOT mapped → "not a mapped smoke command" RED at deploy | **FAIL** |
| 12 | RED tests named in P1 exist at `dfea631a` | all four plus H4 control found (`test_cos_probe.py` lines 288, 452, 469, 503; H1 test count 1) | OK |
| 13 | E1 forms | `git diff --stat`, `git diff <a> <b> -- paths` are runnable by the build line; (b) empty is a valid equality proof | OK |
| 14 | RESTARTS homes | `configs/cobalt/jobs.yaml:193` `com.cobalt.radar` imports `cobalt.cli` (static reach to `cos/probe.py`); the failed deploy's tool run on the same diff gave `com.cobalt.radar` (`deploy-cos-probe-fr2.md`); `restarts.py` has no per-path entry, none needed | OK |
| 15 | migrations / RED first | none; P1 tests ported and run RED on BASE `probe.py`, then P2 GREEN | OK |
| 16 | probe at `dfea631a`: credential read / write bounds | no `open(` of a credential; `.claude.json` count 0; writes only under `tempfile.mkdtemp(prefix="cos-probe-")` root (lines 209-214, 344-360); refuses root equal to real HOME or repo | OK |
| 17 | RULINGS | `R1863` is `HIS RULING · APPROVED` (`cto-2026-10-18.md:90`); route R2185-R2186 recorded in the card | OK |
| 18 | card committed, clean | `git diff HEAD --stat` on the card → empty; `git log` → `04138f61` | OK |

## ISSUES
- FAIL 11: `## DEPLOY PROOF` row 5 uses `grep -n -F`; `deploy-smoke.sh` maps only `grep -c -F "<s>" <path>`, so this row goes RED at smoke. Fix: rewrite it as the `-c` form, e.g. `grep -c -F "(check)" "…/cos/README.md"` · before `0` · after `1`, or drop it (marker 4 already proves the two headings).
- NOTE 1: `BUILD-HUB.md:14` allows `Edit(…cobalt-wt/**)` but no `Write`, while the card says "Write of the whole file, or Edit hunk by hunk" and the seat must also create its report and `.result`. Edit hunk by hunk works for the three existing files; the card's own default is fine, but expect the builder to rely on Edit for them.
- NOTE 2: nothing blocks the card's own build except FAIL 11, which only affects the deploy smoke, not the build.

PREFLIGHT DONE · card: cos-probe-fr2b · checks: 18 · fails: 1 · ready: NO
