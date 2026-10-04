# Card 10 cobalt-guard — preflight 2026-10-04

Card: `prompts/2026-10-03/10-cobalt-guard-card.md`. Read-only; every output below is from my own run.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a8d8a848 main`; then `git -C /Users/cobalt/cobalt diff --stat a8d8a848 main -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py` | both: no output, exit 0 (BASE is an ancestor of main; the two files unchanged) | OK |
| 2 | `git -C /Users/cobalt/cobalt rev-parse --verify ops/cobalt-guard-1004`; `ls /Users/cobalt/cobalt-wt/cobalt-guard-1004` | `fatal: Needed a single revision` (exit 128); `ls: /Users/cobalt/cobalt-wt/cobalt-guard-1004: No such file or directory` | OK |
| 3 | `git -C /Users/cobalt/cobalt show a8d8a848:ops/desk/bare-guard.py` and `…:tests/ops/test_bare_guard.py`; `grep -n "stdin.read\|return 2\|return 0\|def main" ops/desk/bare-guard.py` (file unchanged BASE→main, check 1) | both files print in full. Hook: line 95 `def main():`, line 97 `event = json.loads(sys.stdin.read())`, line 111 `return 2` (deny, after `sys.stderr.write(BLOCK.format(...))` at 110; `sys.exit(main())` at the foot) | OK |
| 4 | `git -C /Users/cobalt/cobalt diff --stat a8d8a848 <branch> -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py` for `ops/adoption-port-1003`, `ops/dev-rebuild-port-1003`, `ops/desk-tools-port-1003` | each: no output | OK |
| 5 | `grep -rn OPS_DESK_PREFIX /Users/cobalt/cobalt/src` | `src/cobalt/jobs/restarts.py:38:OPS_DESK_PREFIX = "ops/desk/"` and `:230: if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` | OK |
| 6 | `grep -n "OPERATIONS A HOOK CAN TAKE"` harness-mods-review; `grep -n -i "REFUSALS"` cto-2026-10-03; `Read` of `BUILD-HUB.md` 14, 29, `CHECK-HUB.md` 32, 50; `git diff --stat a8d8a848 -- BUILD-HUB.md CHECK-HUB.md` (empty: same at BASE) | `harness-mods-review…:51:## OPERATIONS A HOOK CAN TAKE (his ask, …)`; `cto-2026-10-03.md:233:REFUSALS 10-03 (R31; …)` (R31 row at 37). BUILD-HUB 29: "ONE command per Bash call, exactly a listed prefix: no pipe, no redirect, no `&&`, no `; echo`…" OK. BUILD-HUB 14: "THE LIST: 30 allow (4 file-tool strings — `dontAsk` grants nothing implicitly, and an…" NOT the sentence. CHECK-HUB 32: "L1 refuse loud, never guess · L3 one path · L28 test writes in `tmp_path` only; his vault…" NOT the sentence. CHECK-HUB 50: "Git writes as `git add <explicit paths>` then `git commit -m "…" -m "Co-Authored-By: Claude Opus…" NOT the sentence. The sentence is at CHECK-HUB line 48: "ONE command per Bash call, exactly a listed prefix: no pipe, no redirect, no `&&`, no `; echo`…" | FAIL |
| 7 | `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/"` | `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, `DEVFIX-HUB.md` all present (devfix = `DEVFIX-HUB.md`) | OK |
| 8 | `grep -n "^| R12 \|^| R32 \|^| R33 "` cto-2026-10-03; `grep -n "^| R47 "` cto-2026-10-02 | R12 (l.18) `HIS RULING … APPROVED — pending fold`; R32 (l.38) `HIS RULING · APPROVED`; R33 (l.39) `HIS RULING · APPROVED`; R47 (l.54) `HIS RULING · APPROVED` | OK |
| 9 | `grep -c -F "«FILL" …/10-cobalt-guard-card.md` | `0` | OK |

## ISSUES
- Check 6 FAIL: the card's `## READ` cites `BUILD-HUB.md` line 14, `CHECK-HUB.md` lines 32 and 50 as "ONE command per Bash call" sentences. They are not: BUILD-HUB 14 is THE LIST (allow/deny counts), CHECK-HUB 32 is the laws list, CHECK-HUB 50 is the git-writes sentence. The sentence is at BUILD-HUB 29 (correct) and CHECK-HUB 48 (not 32/50). Fix the card's `## READ` cite to `BUILD-HUB.md` 29 and `CHECK-HUB.md` 48 (line 50, git writes, does bear on G4 if kept as such).

PREFLIGHT DONE · card: 10 · checks: 9 · fails: 1 · ready: NO
