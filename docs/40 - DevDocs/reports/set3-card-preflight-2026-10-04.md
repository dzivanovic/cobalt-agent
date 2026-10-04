# Set 3 deploy card — preflight (2026-10-04)

Card: `prompts/2026-10-03/39-deploy-set3-card.md` · main at check time `05effc5e`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8` on the four branches | `15ba4b75` · `53fed116` · `525b5ae1` · `47a689a1` = card TIP/SHIPS heads. `tail` of each check report: last non-blank line carries `tip: 685b88d6` / `f5689418` / `5c1d629f` / `47a689a1`, `held unfixed: 0`, `ready: YES`. `merge-base --is-ancestor` code tip → head: rows 1, 2, 3 exit 0; row 4 tip = head | OK |
| 2 | `merge-base --is-ancestor 5ff16b1f <head>` | rows 2 (`53fed116`) and 3 (`525b5ae1`) exit 0; `5ff16b1f` ancestor of row 1 `15ba4b75` exit 0 | OK |
| 3 | `diff --stat main...<head> -- src/cobalt/db_migrations` | row 1: `cli.py` (114+/1−) · row 2: `cli.py`, `dev_rebuild.py` · row 3: `cli.py` (114+/1−) · row 4: empty. No `.sql` anywhere | OK |
| 4 | `before` on main: `grep -c` DEPLOY-HUB `window (v) does not hold` / `ls dev_rebuild.py` / `grep -c claude-fable-5-1 desk-launch.sh` / `ls close-timer.sh` | `0` · `No such file or directory` · `0` · `No such file or directory`. `after` via `git show`: DEPLOY-HUB at `15ba4b75` count `2`; `dev_rebuild.py` at `53fed116` present (879 lines); `desk-launch.sh` at `525b5ae1` `claude-fable-5-1` count `2`; `close-timer.sh` at `47a689a1` present. `diff --stat 5ff16b1f <head> -- DEPLOY-HUB.md`: `53fed116` empty, `525b5ae1` empty; row 4 does not hold `5ff16b1f` but `main...47a689a1` on DEPLOY-HUB.md is empty (it does not touch the file) | OK |
| 5 | `git show <head>:<path>` for the four smoke paths | `tests/ops/test_hub_lines.py` at `15ba4b75`, `tests/cobalt/test_dev_rebuild_cli.py` at `53fed116`, `ops/desk/stop-guard.py` and `idle-wake.py` at `525b5ae1`, `ops/desk/com.cobalt.close-timer.plist` at `47a689a1`: all print. Both test files contain `def test_`. Commands use absolute paths, no `%` | OK |
| 6 | `grep -c -x -F "<card stop line>" <report>` ×4 | `1` · `1` · `1` · `1` (each is also the report's last non-blank line per check 1) | OK |
| 7 | `grep -n "^| R157 \|^| R216 "` | R157 (cto-2026-10-02.md:164): `HIS RULING (B) … \| HIS RULING · APPROVED \|` · R216 (cto-2026-10-03.md:222): `HIS RULING: deploy set 3 whenever the desk is ready … \| HIS RULING · APPROVED \|` | OK |
| 8 | `grep -n "close-timer\|05.s plist\|R136 "` cto-2026-10-03.md | R136 (:142): set2b-1003 FAILED at STEP-C: `05` adds `ops/desk/com.cobalt.close-timer.plist`; brain: `02b` row T6 (STEP-C text), `05` rides set 3. :231: `05` "set 3 after `02b` T6 is DEPLOYED (R136)". :235 and R158 (:164): `02b` DEPLOYED set 2d `a8d8a848`, T6 KEEP (R146), judge text R152. Fix recorded as DEPLOYED | OK |

## ISSUES

None.

PREFLIGHT DONE · card: set3-1004 · checks: 8 · fails: 0 · ready: YES
