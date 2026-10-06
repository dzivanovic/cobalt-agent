# p2-repoint — 2026-10-05

## §0 Headline
- Card `prompts/2026-10-05/61-deploy-p2-card.md` re-pointed in place: P2 ships alone, 10 files (1822 insertions, 4 deletions), all P2's own; none is D5's or K3's.
- Merge base is now `3c1f75b8` (D5's built tip, on main). No overlap: `diff --name-only 3c1f75b8 main` over the ten files prints nothing.
- Header RULINGS: `2026-10-03 R326, 2026-10-05 R412` (R376, R390 dropped as LAWS). Gates still absent. `«FILL` count 0.

## DECISIONS
None.

## RECORDS
- Git proofs: `merge-base --is-ancestor` for `c96b5118`, `3c1f75b8`, `07a4b8fe`, `c8503415` against main → exit 0 each. `log 437c7299..f15/p2-replay-1004 -- tests src configs ops` → empty; head `6269f05e`. `diff --stat main...f15/p2-replay-1004` → 10 files: `docs/.../cards/cli.md`, `cards/predictions.md`, `reports/f15-p2-build-2026-10-04.md`, `ops/desk/gate-lists.md`, `src/cobalt/cards/cli.py`, `predictions.py`, `tests/cobalt/test_f15_p2_replay.py`, `test_f15_p2_replay_db.py`, `tests/experiments/f15_p2/conftest.py`, `test_x7_x10_x11_db.py`. The earlier draft said ten for P2's own and 23 for the stack; both agree now.
- Rulings: `grep -n "^| R412 "` → `cto-2026-10-05.md:109`, `APPROVED`; R326 → `cto-2026-10-03.md:332`, `HIS RULING · APPROVED` (kept: it binds P2's X11 follow-up). Neither file is modified or untracked in `git status`, so both are committed.
- Markers BEFORE on main now: `def corpus(` 0, `def replay(` 0 (predictions.py), `def cmd_replay` 0 (cards/cli.py); test file and `f15_p2/conftest.py` absent (`ls` exit 1). AFTER at `437c7299` (`git show` then grep): `def corpus(` 1, `def replay(` 1, `def cmd_replay` 1; `conftest.py` shown at that tip; the replay test file is a new file in the diff stat (471 lines). Dropped: the `drc/reconcile.py` marker (D5's; `ls` exit 0 on main now).
- Unchanged: check last line (`held unfixed: 0`, `ready: YES`), code tip `437c7299`, head `6269f05e`, RESTARTS `com.cobalt.aset com.cobalt.radar`, G (d2) wording, X11 `no_trigger` follow-up, K3-F1 mark record (kept in the card's RECORDS).
- Header gates absent: `rev-parse --verify` of `deploy/deploy-p2-1005` and `deploy-2026-10-05-p2` → `fatal: Needed a single revision`; `ls` of `/Users/cobalt/cobalt-wt/deploy-p2-1005` and the REPORT path → `No such file or directory`.
- Only the card and this report were written. No git write, no launch.

P2 DEPLOY CARD RE-POINTED · decisions: 0
