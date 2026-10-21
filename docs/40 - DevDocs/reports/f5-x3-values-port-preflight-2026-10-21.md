# f5-x3-values-port — card 965 preflight (read-only)

Reads only. HEAD `461f2de8` (BASE `bac9b683` trails by desk commits; not a fail).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header of card 965 vs card 958 (`grep` of both) | JOB `f5-x3-values-port`, BRANCH `ops/f5-x3-values-port`, WORKTREE `f5-x3-values-port`, BAND `LOW`, CLASS `K2`, INSTALL `none`, RESTARTS `com.cobalt.aset`, RULINGS `2026-10-18 R1863` (958: same BAND/CLASS/RESTARTS/RULINGS); no migration | OK |
| 2 | `git diff --stat 20dd871d e9245a8e` | `modelaccess.yaml 8` · `checkpoints.md 3` · `test_checkpoints_offline.py 36` · 3 files, 43+, 4− | OK |
| 3 | `git diff --stat 20dd871d main --` the three spec paths | nothing (net unchanged). NOTE: `git log 20dd871d..main` on them lists `29e5fefb`, `e9245a8e`, `7e4f946d` (the merge and its revert, net zero) | OK |
| 4 | `git diff --stat main 20dd871d -- reports/f5-x3-measure-2026-10-20.md` | `182 +++++`, 1 file; the file exists at `20dd871d`, absent on main; card D1 ports it byte-equal | OK |
| 5 | `git grep -n` anchors on main: `modelaccess.yaml` | `:70 checkpoint.narrative:`, `:77` and `:79` the two UNMEASURED comments, `:78 timeout_s: 60`, `:80 max_output_tokens: 512` | OK |
| 6 | `git grep -n def test_route_is_loaded_and_local main` | `test_checkpoints_offline.py:553` | OK |
| 7 | `git grep -n aset main -- configs/cobalt/jobs.yaml` | `:39 com.cobalt.aset` resident; `:86` reads `configs/cobalt/modelaccess.yaml` | OK |
| 8 | `git merge-base --is-ancestor e9245a8e main` | exit 0 (why `deploy-card.sh:553` refuses the old tip; the port is the route) | OK |
| 9 | `BUILD-HUB.md:14`, `:16` | allow `Edit(//Users/cobalt/cobalt-wt/**)` (governs Write), `git show*`, `git diff *`; no `git apply`, `cherry-pick`, `git mv`; `rm` only of the `.env`. Card builder commands are Edit/Write plus those | OK |
| 10 | DEPLOY PROOF `before` on main HEAD: `source: UNMEASURED` / X3 source / `(warm model)` / cold-load string | `2` (`:77`, `:79`) / none / none / none = `2`, `0`, `0`, `0` | OK |
| 11 | DEPLOY PROOF `after` on `e9245a8e`: same four | UNMEASURED none (`0`); `# source: X3 reports/f5-x3-measure-2026-10-20.md` `2`; `(warm model)` `1`; cold-load string `1` | OK |
| 12 | smoke line vs `DEPLOY-HUB.md:11` | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` is exactly the admitted `Bash(curl … https://cobalt.taild24291.ts.net/*)`; section holds no `http://127.0.0.1:5010/` and no `uv run pytest` | OK |
| 13 | `deploy-card.sh:567-576` (read only) | `m` takes lines holding both `· before ` and `· after `; `s` takes the rest, so the https curl line and the `ls` line go to the smoke reads untouched; no refusal on their shape | OK |
| 14 | RED test first (diff of the test at `e9245a8e`) | on BASE's yaml (`timeout_s: 60`, `512`, jobs timeout 300): the integer, `%5`, `!=15`, `%64`, `300 > 120` asserts pass; the first to fail is `assert "UNMEASURED" not in "\n".join(block_lines)` (UNMEASURED at `:77`, `:79`), in `test_route_budgets_are_measured`. After P2 (`25`, `256`, `300 > 85`, 0 UNMEASURED, 2 sources) all hold | OK |
| 15 | E1 proof design | (a) stat tables, (b) `git diff e9245a8e <tip>` empty, (c) stat of `src tests configs ops` names two files, (d) X3 report vs `20dd871d` empty: all derivable from the spec above; main and `e9245a8e` differ over the three paths only by the revert, so BASE-to-tip equals the spec stat | OK |
| 16 | RESTARTS | `com.cobalt.aset` (`jobs.yaml:86`); test and docs restart nothing; R1 is the record | OK |
| 17 | `## RECORDS` brain line | present: "958 rolled back on a card-fault smoke string … brain 9b07db5a 2026-10-21" | OK |
| 18 | card committed, clean | `git log -1` on card → `a786484a`; `git diff HEAD --` card → nothing | OK |
| 19 | `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` | exists | OK |

## ISSUES
- NOTE: check 3, "unchanged on main since `20dd871d`" is true by net diff only; the merge and its revert sit in the log of those paths.
- NOTE: `deploy-smoke.sh` maps only `http://127.0.0.1:5010/`, so its `--dry-run` will print `WOULD REFUSE` on the https line (drafter D2); no hub step calls it, and `deploy-card.sh` does not.
- Blocks the card's own build: nothing.

PREFLIGHT DONE · card: f5-x3-values-port · checks: 19 · fails: 0 · ready: YES
