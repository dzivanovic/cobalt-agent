# S3 card preflight r2 (D5 dropped) — card `02-deploy-s3-card.md`

Read-only. Card last commit `4133427e`. Time of run: 2026-10-05 (seat `s3-preflight`).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify 3e40359a^{commit}` | `3e40359ac99508105d7bed5dc849ca336f3bd1b3` | OK |
| 1b | `… rev-parse --verify 6269f05e^{commit}` | `6269f05e120c3f33a35951b2bdc7199e4a068fd9` | OK |
| 1c | `… rev-parse --verify 47ec01c5^{commit}` | `47ec01c5cc6ba97cda7caa8c516fe9dc25359b9b` | OK |
| 1d | SHIPS rows read from the card | exactly 3 rows: `3e40359a`/`3e40359a`, `437c7299`/`6269f05e`, `47ec01c5`/`47ec01c5`; heads = TIP `3e40359a 6269f05e 47ec01c5` in order | OK |
| 2 | `grep -n -i "d5\|c96b5118\|reconcile" <card>` | hits at lines 41, 42, 44, 45. 41 (trial merge) and 42 (desk answer) are the two history lines draft DECISIONS 1 names; 45 is the R378 drop record. **Line 44** (`the script refuses drc-d5: held unfixed: 1`) is a history line the draft report does NOT name. None of the hits is a SHIPS, MARKERS, SMOKE READS or TIP line | FAIL (44, non-binding) |
| 3a | `git merge-base --is-ancestor main main` (BASE is the literal `main`, `CARD.md` deploy) | exit 0, no output | OK |
| 3b | `git rev-parse --verify deploy/s3-1005-attempt2` | `aba673f1d206ea2bdacc145b9982aeeb9e8e8e8b` — the branch EXISTS | FAIL |
| 3c | `ls -d /Users/cobalt/cobalt-wt/deploy-1005-1-attempt2` | `/Users/cobalt/cobalt-wt/deploy-1005-1-attempt2` — the worktree dir EXISTS | FAIL |
| 3d | `git rev-parse --verify refs/tags/deploy-2026-10-05-1-attempt2` | `fatal: Needed a single revision` (tag absent) | OK |
| 3e | `ls "…/reports/deploy-s3-1005-attempt2.md"` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-s3-1005-attempt2.md` — the REPORT EXISTS (it is the failed attempt-2 report the drop record cites) | FAIL |
| 3f | grep `\| R(326\|327\|331\|368\|378) \|` in `cto-2026-10-03.md` / `cto-2026-10-05.md` | R326 `HIS RULING · APPROVED`; R327 `HIS RULING · APPROVED · APPLIED: LAWS.md L43`; R331 `HIS RULING · APPROVED · APPLIED`; R368 `HIS RULING · APPROVED`; R378 `DESK RECORD` (L43, R127), not his ruling. Card RULINGS = R326, R327, R368 (R331, R378 are not in the card's header) | OK |
| 3g | `git log -1 --format=%h -S"\| R<n> \|" -- <file>` | R326 `b1337431`; R327 `b1337431`; R331 `3114a37b`; R368 `797cd2ab`; R378 `c3f9f89a` — all committed | OK |
| 4a | `git grep -c -F "def superseded_stated_ids" 3e40359a -- src/cobalt/drc/store.py` | `3e40359a:src/cobalt/drc/store.py:1` (after `1`) | OK |
| 4b | `git grep -c -F "def corpus(" 6269f05e -- src/cobalt/cards/predictions.py` | `6269f05e:src/cobalt/cards/predictions.py:1` (after `1`) | OK |
| 4c | `git grep -c -F "@include" 47ec01c5 -- ops/desk/bare-guard.py` | `47ec01c5:ops/desk/bare-guard.py:3` (after `3`) | OK |
| 4d | `git grep -c -F "def test_" 3e40359a -- tests/cobalt/test_drc_k3.py` | `…:54` | OK |
| 4e | `git grep -c -F "def test_" 6269f05e -- tests/cobalt/test_f15_p2_replay.py` | `…:32` | OK |
| 4f | smoke read 3 = marker 3 (`@include` in `bare-guard.py`) | `…:3` (as 4c) | OK |
| 5 | RESTARTS homes (K10): `jobs.yaml` `com.cobalt.aset` `imports: [cobalt.aset.__main__, cobalt.aset.web]` reaches the `drc/*` and `aset/*` paths of K3; `com.cobalt.radar` `imports: [cobalt.cli]` reaches `cards/*` of P2; guard-b paths are `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` (no resident). The three check stop lines carry `RESTARTS: com.cobalt.aset com.cobalt.radar` / same / `none`, as the card says. I did not run `jobs restarts` (production command, not on this seat); STEP-R derives it at the gate | OK (read, not tool-run) |
| 6 | `grep -c -F "«FILL" <card>` | `0` | OK |
| 7a | `git log -1 --format=%h -- <card>` | `4133427e` | OK |
| 7b | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | empty | OK |

## ISSUES
- FAIL 3b: branch `deploy/s3-1005-attempt2` already exists at `aba673f1`; CARD `BRANCH` must be new. Needs a new name (`attempt3`) or the desk's ruling to delete the old one.
- FAIL 3c: worktree dir `/Users/cobalt/cobalt-wt/deploy-1005-1-attempt2` already exists; `WORKTREE` must be absent. Same fix.
- FAIL 3e: `REPORT` `reports/deploy-s3-1005-attempt2.md` already exists (the failed run's report, which the drop record cites by that name); `REPORT` must be new. Same fix; `TAG` `deploy-2026-10-05-1-attempt2` is free, but follow the new attempt number.
- FAIL 2: line 44 (`drc-d5` in the drafter's note) is a D5 mention the draft report's DECISIONS 1 does not name; history only, binds nothing. Reword it or add it to the named history lines.
- Info, not a FAIL: R378 is a `DESK RECORD`, not `HIS RULING · APPROVED`; the card does not list it in RULINGS, so no row is missing.

PREFLIGHT DONE · card: s3-02 · checks: 25 · fails: 4 · ready: NO
