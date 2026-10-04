JOB: dev-rebuild-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/dev-rebuild-port-1003
WORKTREE: dev-rebuild-port-1003
BASE: 5ff16b1f
TIP: f5689418
REPORT: /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/docs/40 - DevDocs/reports/dev-rebuild-port-build-2026-10-03.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/dev-rebuild-port-check-2026-10-03.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R157

## ROWS

WHY: cards `11` dev-rebuild (checked, head `07cc965f`) and `13` slot-guard (checked at `05c8b7fa`, built on `11`'s build tip `1df251b9`) both missed the 10-02 and 10-03 sets: `11` conflicts with the adoption chain in `cli.py`, and `13` conflicts with `11`'s check fix in `test_dev_rebuild_db.py` and `dev_rebuild.md`. One PORT lands both on `03d`'s tip (shape: card `13b`, which this card replaces). With-DB job: takes the lock.

| row | what | red first | files |
|---|---|---|---|
| P1 | `11` first: every file of `git diff --name-only 6ae3f133..07cc965f` written from `git show 07cc965f:<path>` and hash-proven, except the SHARED paths, settled by Edit with BOTH sides (BASE's lines and `11`'s; quote `git diff <BASE> -- <path>` showing only `11`'s lines, and `git diff 07cc965f -- <path>` showing only BASE's): `src/cobalt/db_migrations/cli.py` (BASE's `cmd_migrate` as it stands — the TABLES / FINGERPRINT lines only if BASE is `03d`'s tip — plus `11`'s `cmd_dev_rebuild`), `docs/40 - DevDocs/cobalt/db_migrations/cli.md` | `11`'s with-DB tests red on `BASE`, green at the tip (one E2 lock take) | `11`'s files |
| P2 | `13` on top, by Edit onto P1's result, never by overwriting a file P1 settled: every file of `git diff --name-only 1df251b9..05c8b7fa` from `git show 05c8b7fa:<path>`, hash-proven where neither `11`'s fix nor BASE touched it; hand-merged with BOTH sides: `src/cobalt/db_migrations/cli.py` and `cli.md` (`13`'s hunks onto P1's text), `tests/cobalt/conftest.py` (BASE's `01` guard lines and `13`'s slot-guard lines), `tests/cobalt/test_dev_rebuild_db.py` and `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` (test count = sum minus shared names, listed), `dev_rebuild.py` (`11`'s O1–O5 and `13`'s guard) | `13`'s guard tests red before, green after; the settled files' tests green inside the W take | `13`'s files |
| P3 | the `--proof-only` seam, two stub lines in neither parent (judge 10-04; exception to `## NOT IN THIS JOB` line 1 for these two lines only): (a) in `_migrate_output` of `tests/cobalt/test_dev_rebuild_cli.py`, after its `_probe_all` stub: `    monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])` (the stub `d483a417` added to `test_migrate_proof.py:1541`, `:1765`); (b) in `test_proof_only_ends_with_the_fingerprint_then_the_tables_line` of `tests/cobalt/test_migrate_level.py`, after its `_probe_all` stub: `    monkeypatch.setattr(cli, "_slot_lines", lambda conn: [])`. No `src/` line changes; printed order stays proof table, SLOTS, `code:`, FINGERPRINT, TABLES | the three reds of `## E3` P2 red before, green after; `git diff 05c8b7fa -- tests/cobalt/test_dev_rebuild_cli.py` and `git diff 5ff16b1f -- tests/cobalt/test_migrate_level.py` each show exactly that one line added | `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_migrate_level.py` |

## NOT IN THIS JOB
- A line in neither parent; `git merge` / `rebase` / `cherry-pick`; the devfix verbs (`03b`, which stacks on this card's tip).

## READ
- `prompts/2026-10-02/11-dev-rebuild-card.md`, `13-slot-guard-card.md`; `reports/dev-rebuild-check-2026-10-02.md` `## FIXES`; `reports/slot-guard-check-2026-10-02.md` `## §0`; `prompts/2026-10-03/13b-slot-guard-port-card.md` (withdrawn into this card).

## CHECK ASKS
- X1 Hash pairs for every non-settled file; `test_dev_rebuild_cli.py` = `05c8b7fa` plus the one P3 (a) line. X1b (P3) exactly two lines in neither parent, the `_level_lines` and `_slot_lines` stubs; no assert removed or loosened; `cli.py`'s proof-only order is proof table, SLOTS, `code:`, FINGERPRINT, TABLES (gate.sh's last-two-lines read, L1). X2 In the three settled files, is any line of `07cc965f` or `05c8b7fa` lost or weakened? X3 Do `13`'s guard tests still assert against the ported module?

## RECORDS
- RESTARTS class homes (L7a): `src/cobalt/db_migrations/*.py` → the class `11`'s build report `## RESTARTS` derived (`com.cobalt.radar` restart, its line quoted at PREFLIGHT); `tests/cobalt/*` → tests (`restarts.py:246`); `docs/**` → DOCS (`:228`) — cites at BASE `5ff16b1f`.
- TREE STATE: `unchanged` holds (precedent `11`, `13`, `01`, `03`, `03d`): the new with-DB test `tests/cobalt/test_dev_rebuild_db.py` runs in pass 1 as written at `0013`, no deselect, no pass-2 id.
- BASE: the card asked for `03d`'s CHECKED tip because `03d` and `11` both edit `cli.py`; on `main` `5ff16b1f` the set-3 merge of `03d` + `11b` conflicts in `cli.py` again. If `03d` is not checked when `11b` must launch, `11b` waits for it; the desk fills BASE from `03d`'s stop line.
- Preflight (desk, `11b-card-preflight-2026-10-03.md`): rows P1/P2 name every shared path and the merge order; cites `:228` / `:246`.
- Judge, 10-03 21:39 ET: replaces `13b`; set 3, Sunday after 13:00. `11` restarts `com.cobalt.radar` (its RESTARTS line): set 3's window is Sunday (iii).
