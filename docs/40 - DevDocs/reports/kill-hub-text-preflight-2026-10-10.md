# Kill-hub-text card 284 — preflight (2026-10-10, read-only)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | Read card header | JOB `kill-hub-row-1010`, LADDER, BRANCH `ops/kill-hub-row-1010`, WORKTREE `kill-hub-row-1010` (same name as job and branch tail), BASE `6fe8d690`, REPORT under `cobalt-wt/kill-hub-row-1010/…/kill-hub-row-build-2026-10-10.md`, RULINGS `2026-10-10 R855`, `DB: none`. TIP, CHECK REPORT, HOUSE B empty (desk fills) | OK |
| 1b | `git -C … rev-parse --verify 6fe8d690` | `6fe8d69077fe2b7942ba74e59ed21fdb0e82f7b8` | OK |
| 1c | `git -C … diff HEAD --stat -- <card>`; `ls` | empty (committed); file is `284-kill-hub-card.md` | OK |
| 2a | `git diff 6fe8d690 --stat` both files; Read `DEPLOY-HUB.md:137`, `:162`, `STANDING-LIST.md:146-149` | diff empty (working file = BASE); K1 OLD and K2 OLD equal lines 137 and 162 whole line; 148 = `Bash(launchctl print gui/501/*)` row, 149 = `cobalt.sh status` row (K3 goes between) | OK |
| 2b | not run: `git show 6fe8d690:<file>` byte compare | proxy used (diff vs BASE empty plus Read); not a literal `git show` compare | NOTE |
| 3a | Read staged `kill-row/DEPLOY-HUB.md:137`, `:162`, `STANDING-LIST.md:149` vs card NEW blocks | K1 NEW, K2 NEW, K3 equal the staged text (read by eye, whole line) | OK |
| 3b | same five steps + both stop rules in K1, K2, K3 | K1: (1)-(5), "Any difference at (2), or any orphan at (4) → no second kill, STEP-5", exit 1 → STEP-5. K2: same, residents stay down, `DECISION 0 … FOR DEJAN`. K3: same, plus first dry run empty → no kill | OK |
| 3c | `grep -c -F "same call again, then STEP-5"` card | `0` | OK |
| 3d | `grep -n -i "DRAFT\|awaiting"` card | hits only at card line 21 ("carries no DRAFT or 'awaiting his yes' wording"); K3 text has none | OK |
| 4 | Read `orphan-clean.sh:1-90`, `:174`, `:245-253` | usage `[--kill] <label>`, table `aset` only (`:76-82`); text's calls `orphan-clean.sh aset` and `--kill aset` accepted; last lines match `:174` (`orphan-clean: aset · none found`) and `:252` (`dry-run · verified <n> · spared <m> · killed 0`); `WOULD KILL: <pid>` at `:250`; REFUSED/UNVERIFIED exit 1. `--kill com.cobalt.aset` in the NEW text and the staged copies: 0 (grep -c → 0 in DEPLOY-HUB staged, STANDING-LIST staged); no `sleep`, `pgrep`, radar call in the NEW text | OK |
| 5 | Read `DEPLOY-HUB.md:11` allow line | `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` covers both `orphan-clean.sh aset` and `orphan-clean.sh --kill aset`; `Bash(date*)` covers `date`. No other command in the text (`launchctl bootstrap`, `kickstart -k`, `cobalt.sh stop`, `ps -p`, `launchctl print` are already in the old line, unchanged). Card adds no command | OK |
| 6a | `grep -c -F` on BASE (working) file vs staged copy: "ORPHAN-CLEAN, aset only" | 0 → 1 | OK |
| 6b | "orphan-clean.sh --kill aset" DEPLOY-HUB / STANDING-LIST | 0 → 2 / 0 → 1 | OK |
| 6c | "--kill com.cobalt.aset" all four | 0, 0, 0, 0 (the card itself says it 3 times, in red-first prose only) | OK |
| 6d | "each resident booted out and not held DOWN" | 0 → 1 | OK |
| 6e | "orphan-clean.sh aset" / "the kill sequence:" | 0 → 2 / 0 → 2 | OK |
| 6f | `grep -n -F "killing the orphaned"` | BASE no hit; staged `STANDING-LIST.md:149` one hit | OK |
| 6g | `wc -l`; `git diff --no-index --numstat` | BASE 181 / 220, staged 181 / 221; numstat DEPLOY-HUB `2 2`, STANDING-LIST `1 0` | OK |
| 6h | `uv run pytest -q tests/ops/test_hub_lines.py` … `0 failed` | not run (no `uv` in this seat; read-only). `grep` of both tests shows only reads of the files (`test_hub_lines.py:30,41,117`, `test_desk_launch_brain.py:498`) | NOTE |
| 7a | `ls` of `BUILD-HUB.md`, `CHECK-HUB.md`, `DEVFIX-HUB.md`, `229-orphan-clean-card.md`, `26-hub-text-card.md`, the five reports in `## READ`, `restore-hub-text-2026-10-10.md`, `orphan-clean.sh`, `bare-guard.py`, both tests | all exist | OK |
| 7b | Read `bare-guard.py:1032-1035`, `:1082-1090` | `:1084-1089` is `is_fixed(path)` / G5 fixed (cited right); `:1034-1035` is the G2 return and `git_problem` check, not G9 or G7 — the card's note "the check hub's own G9 (`:1034-1035`)" does not name a G9 line | NOTE |
| 7c | X1–X5 cited lines `orphan-clean.sh:76-82`, `:174`, `:250`, `:252` | all as described | OK |
| 8 | K3 row text | who: deploy hub only ("ONLY in the deploy hub"); where: 4.2 after the bootout and STEP-5 (3) before the bootstrap; precondition: a prior dry run that printed a verified orphan (and the NO column says never without it); not standing elsewhere ("never standing outside those two steps", any other seat, any other label) | OK |

## ISSUES
- NOTE X2 (a second kill is reachable): a 4.2 failure at (2) or (4) ends in STEP-5, and STEP-5 (3) (K2) then begins with its own dry run. A surviving orphan is verified again, `date`, same dry run, and `--kill aset` runs a second time. K1's "no second kill" holds only inside one sequence. K2 has no "unless 4.2 already ran it" clause, and `DEPLOY-HUB.md:164` ("STEP-5 is never entered twice") does not close it. The text as the card states it matches the brain's R927; the hole is the brain's wording. The desk should ask him: add a clause at K2 ("if 4.2 already ran the sequence, no kill here") or accept one more kill.
- NOTE X5: K2 says "not held DOWN" for aset; the stop line's `aset: <UP|DOWN>` (`DEPLOY-HUB.md:164`, F at `:23`) still reads the held-down aset as DOWN, so it reads right. Not proven by a test.
- NOTE: the card text for "6h" (`pytest … 0 failed`) was not run by this seat; the check seat runs it.
- NOTE: the card contains the string `--kill com.cobalt.aset` three times, all in the red-first / WHY prose saying it must be 0; none in a TEXT block. A grep of the card for it is not a valid 0 count.
- NOTE: the merge waits for his yes (brain R926, R937). BUILT and CHECK DONE stop at the branch tip.

## LAUNCH ROW
- CARD: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md` (committed, `git diff HEAD` empty)
- Literals the desk writes before the launch: `TIP:` (the build's branch tip, at BUILT), `CHECK REPORT:` (the check's path), `HOUSE B:` (empty or its report per the hub; the card says the check is house A Grok). `DB: none`, `BASE: 6fe8d690`.
- Launch: the build via `sh /Users/cobalt/.claude/ops/desk-launch.sh` with the build hub on the card, job `kill-hub-row-1010`, worktree `kill-hub-row-1010`, branch `ops/kill-hub-row-1010`.
- Merge: NOT in this job. The desk asks him after the check, the merge waits for his yes.

PREFLIGHT DONE · prompts: 1 · checks: 23 · fails: 0 · ready: YES
