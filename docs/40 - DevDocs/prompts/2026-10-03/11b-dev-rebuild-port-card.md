JOB: dev-rebuild-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/dev-rebuild-port-1003
WORKTREE: dev-rebuild-port-1003
BASE: «FILL: 03d's checked tip (11b stacks on 03d: both edit src/cobalt/db_migrations/cli.py)»
TIP:
REPORT: /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/docs/40 - DevDocs/reports/dev-rebuild-port-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R157

## ROWS

WHY: cards `11` dev-rebuild (checked, head `07cc965f`) and `13` slot-guard (checked at `05c8b7fa`, built on `11`'s build tip `1df251b9`) both missed the 10-02 and 10-03 sets: `11` conflicts with the adoption chain in `cli.py`, and `13` conflicts with `11`'s check fix in `test_dev_rebuild_db.py` and `dev_rebuild.md`. One PORT lands both on `03d`'s tip (shape: card `13b`, which this card replaces). With-DB job: takes the lock.

| row | what | red first | files |
|---|---|---|---|
| P1 | `11` first: every file of `git diff --name-only 6ae3f133..07cc965f` written from `git show 07cc965f:<path>` and hash-proven, except `src/cobalt/db_migrations/cli.py`, settled by Edit so `03d`'s LEVEL/FINGERPRINT lines and `11`'s `cmd_dev_rebuild` both stand (quote `git diff <BASE> -- cli.py` showing only `11`'s lines) | `11`'s with-DB tests red on `BASE`, green at the tip (one E2 lock take) | `11`'s files |
| P2 | `13` on top: every file of `git diff --name-only 1df251b9..05c8b7fa` from `git show 05c8b7fa:<path>`, hash-proven where `11`'s fix did not touch it; `tests/cobalt/test_dev_rebuild_db.py` and `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` settled with BOTH sides (test count = sum minus shared names, listed); `dev_rebuild.py` with `11`'s O1–O5 lines and `13`'s guard lines both | `13`'s guard tests red before, green after; the settled test file green inside the W take | `13`'s files |

## NOT IN THIS JOB
- A line in neither parent; `git merge` / `rebase` / `cherry-pick`; the devfix verbs (`03b`, which stacks on this card's tip).

## READ
- `prompts/2026-10-02/11-dev-rebuild-card.md`, `13-slot-guard-card.md`; `reports/dev-rebuild-check-2026-10-02.md` `## FIXES`; `reports/slot-guard-check-2026-10-02.md` `## §0`; `prompts/2026-10-03/13b-slot-guard-port-card.md` (withdrawn into this card).

## CHECK ASKS
- X1 Hash pairs for every non-settled file. X2 In the three settled files, is any line of `07cc965f` or `05c8b7fa` lost or weakened? X3 Do `13`'s guard tests still assert against the ported module?

## RECORDS
- RESTARTS class homes (L7a): `src/cobalt/db_migrations/*.py` → the class `11`'s build report `## RESTARTS` derived (`com.cobalt.radar` restart, its line quoted at PREFLIGHT); `tests/cobalt/*` → test/documentation (`restarts.py:239`); `docs/**` → DOCS (`:219`).
- Judge, 10-03 21:39 ET: replaces `13b`; set 3, Sunday after 13:00. `11` restarts `com.cobalt.radar` (its RESTARTS line): set 3's window is Sunday (iii).
