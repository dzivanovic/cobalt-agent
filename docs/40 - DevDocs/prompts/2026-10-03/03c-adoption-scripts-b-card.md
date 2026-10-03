JOB: adoption-scripts-b
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/adoption-scripts-b-1003
WORKTREE: adoption-scripts-b-1003
BASE: 0a4a7743
TIP:
REPORT: /Users/cobalt/cobalt-wt/adoption-scripts-b-1003/docs/40 - DevDocs/reports/adoption-scripts-b-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R154, 2026-10-02 R157

## ROWS

WHY: the adoption-hubs build (`02`, `1c349c49`) found four facts about the scripts of `03` that block or break the hubs' real use (its DECISIONS 2, 3, 4, 9; judge answers in `reports/adoption-hubs-decisions-2026-10-03.md`): `preflight.sh` fails every build on the untracked report the hub creates first; `gate.sh` exits 4 at once instead of waiting for the lock; the deploy gate has no whole pass 1 (his R154); `desk-launch.sh` still demands `TREE STATE`. All four are script rows, so they stack on `03`'s READY tip `0a4a7743` beside `02` and ship with it in set 2. Shape as card `03`: POSIX `sh`, `LC_ALL=C`, tests in `tests/ops/` with stubs.

| row | what | red first | files |
|---|---|---|---|
| M1 | `preflight.sh build` and `check`: the `status` row ignores the card's own `REPORT` path (and, for a check, `CHECK REPORT`) when it is the only untracked line, printing `status: clean but the report (untracked, expected)`; any other untracked or modified path still fails the row | `tests/ops/test_preflight.py`: a worktree with the untracked report only → `PREFLIGHT OK`; with the report and one other untracked file → `FAILED PREFLIGHT: status` naming the other file. RED on `BASE`: the report alone fails | `ops/desk/preflight.sh`, `tests/ops/test_preflight.py` |
| M2 | `gate.sh` WAITS: its own held-`.env` pre-check is removed; the lock is taken only by `take-devdb-lock.sh <worktree> 90`, whose retry is the wait (THE LOCK's text); exit 4 only when that script exits 4. The verdict then prints `lock: waited <n> min` from the take's start and end `date` | `tests/ops/test_gate.py`: a sibling `.env` that disappears on the stub lock script's second try → the gate runs and prints `lock: waited`; never-free → exit 4 after the stub's budget; no `uv` call before the lock. RED on `BASE`: exit 4 at once | `ops/desk/gate.sh`, `tests/ops/test_gate.py` |
| M3 | THE DEPLOY'S WHOLE PASS 1: `gate.sh <worktree> all --deploy` runs PASS 1 from `gate-lists.md` with ` --db-only` removed (one token; everything else byte-equal) and prints `pass 1: whole (deploy)`; without `--deploy` nothing changes. Card `02`'s STEP-G calls it with `--deploy` (his R154: the deploy gate runs pass 1 whole on every set) | `tests/ops/test_gate.py`: the call log's pass-1 command without `--db-only` under `--deploy`, with it otherwise; `tests/ops/test_pass1_db_only.py` restored to read: `gate-lists.md` PASS 1 holds ` --db-only` once, and `DEPLOY-HUB.md`'s STEP-G call holds `--deploy` (this second assertion turns green when `02`'s A3 text lands; until then it is marked xfail-strict with the reason, dropped by `02`'s builder or its check). RED on `BASE`: no `--deploy` | `ops/desk/gate.sh`, `tests/ops/test_gate.py`, `tests/ops/test_pass1_db_only.py` |
| M4 | `desk-launch.sh`: `TREE STATE` becomes optional on build and check cards — absent → accepted; present → still `unchanged` or `row <id>` (so yesterday's cards launch unchanged). `CARD.md` is `02`'s and not touched here | `tests/ops/test_desk_launch_devfix.py` (or the launcher's card test file): a build card without `TREE STATE` → the launch line prints; with `TREE STATE: nonsense` → `REFUSED`. RED on `BASE`: `incomplete card: TREE STATE` | `ops/desk/desk-launch.sh`, the launcher's card test file |

## NOT IN THIS JOB
- Any hub file or `CARD.md` (`02`'s); any string on a launch line; a `gate.sh` single-file mode (follow-up; E2's with-DB red stays typed).
- The lock scripts themselves; the pass lists' content.

## READ
- `reports/adoption-hubs-build-2026-10-03.md` `## DECISIONS` 2, 3, 4, 9; `reports/adoption-hubs-decisions-2026-10-03.md`.
- `ops/desk/preflight.sh`, `gate.sh`, `take-devdb-lock.sh`, `desk-launch.sh` (`:507-509`) at `BASE`; `tests/ops/test_gate.py`, `test_preflight.py`, `test_pass1_db_only.py`.

## CHECK ASKS
- X1 Can `gate.sh` run a `uv` command while another worktree holds the lock, by any path? Can `--deploy` leak into a build's or check's pass 1?
- X2 Does M1 ever accept a second untracked path, or a modified tracked one?

## RECORDS
- Judge, 10-03 (adoption-hubs decisions): stacked on `03`'s READY tip `0a4a7743`, beside `02`; disjoint files; ships in set 2 with `02` (both or neither).
- `DB: none`: every file under `ops/`, `tests/ops/`.
