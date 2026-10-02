# ops-seam build — the judge seat's answers (brain `776c834d`, 2026-10-02, under his R41)

Read: `/Users/cobalt/cobalt-wt/ops-seam-1002/docs/40 - DevDocs/reports/ops-seam-build-2026-10-02.md` §0, `## E3 THE ROWS`, `## RESTARTS`, `## DECISIONS`, `## RECORDS`, the stop line (`BUILT · … tip: 551f07e0 … decisions: 3 · for Dejan: 0`).

## §0 Headline
- Three answered, none for Dejan. None holds the check and none holds card `12`: `12` launches now on `551f07e0`.
- Decisions 1 and 2: KEEP both two-line test edits. Decision 3: recorded, right as built.
- One follow-up for tomorrow's list (the guard reads a script outside the repo).

## ANSWERS
1. DECISION P1 — KEEP. The two branches met in a place the card did not name: the size-guard test rewrote two literal lines of `desk-launch.sh` that the lock branch had changed. The builder re-pointed the two substitution keys at the new lines. No assertion changed and no script changed; the other choice (the keys match nothing) would point the staged launcher at the real repo. This is the same class of seam the card already allows for the `OPS_TOOLS` literal.
2. DECISION P2 — KEEP. The lock tests now run a launcher that runs the size guard first, and the guard's `claude agents` call reached the logging stub. Answering `agents` with an empty list makes the guard fail open and leaves the lock assertions untouched; the guard itself stays pinned by its own test file. FOLLOW-UP, not a hold: these tests still execute `/Users/cobalt/.claude/ops/desk-list.sh`, a file outside the repo and outside git. Tomorrow's adoption list gains one row: `desk-list.sh` is tracked under `ops/desk/` and the guard reads the copy beside it, so the ops tests need nothing outside their tmp roots.
3. DECISION P4 — recorded. Refusing a missing link folder is right (L1), and the folder exists on this machine. The card's predicted red belonged to the extra-argument test; the build shows both reds.

## FOR THE CHECK — one line the desk adds to card `16` `## RECORDS` before the check launches
- The judge seat's answers to the build's DECISIONS 1–3 (2026-10-02 R41, `reports/ops-seam-decisions-2026-10-02.md`): the two-line edits of `tests/ops/test_desk_size_guard.py` (the two substitution keys) and `tests/ops/test_devdb_lock.py` (the stub answers `agents` with an empty list) are KEPT; those two files are therefore not byte-equal to `ee667f3c` / `aeefb6df`, by exactly the diffs the build report quotes under `## DECISIONS`, and that is not a finding. Any OTHER difference in a ported file is one.

OPS-SEAM DECISIONS ANSWERED · 3 of 3 · for Dejan: 0 · holds: 0 · follow-up: 1
