# Port card 1032 — preflight (2026-10-24)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read card 1032 vs `CARD.md` header table; `grep -n "^| R1863 " reports/cto-2026-10-18.md` | JOB `radar-mirror-scope-port`, LADDER, BRANCH `ops/radar-mirror-scope-port`, WORKTREE `radar-mirror-scope-port`, BASE `148b03ef` (8 hex), TIP empty (desk's), REPORT, CHECK REPORT, HOUSE B, BAND HIGH, RESTARTS, MIGRATIONS none, RULINGS `2026-10-18 R1863` all present; no other placeholder. `:90 \| R1863 \| … \| HIS RULING · APPROVED (brain, L79) …` | OK |
| 2 | `git diff --stat 11ed17b8 25994142` | 9 files, 561+/16−: radar/notes.md 32, build report 234, its `.result` 15, notes.py 46, test_radar_evaluate 4, test_radar_mirror_scope 201, test_radar_notes 7, test_radar_replay 21, test_radar_runner 17. Card rows: the same seven spec files (T1 five tests, C1 notes.py, D1 notes.md) with E1 (b) counts 46/201/7/17/4/21/32; the two report files excluded and listed. None extra, none missing. | OK |
| 3 | `git diff --stat 11ed17b8 HEAD --` the seven paths | nothing (main's HEAD now `0db910de`; `git diff --stat 148b03ef HEAD -- src tests configs ops` also nothing) | OK |
| 4 | read every command given to the builder | `git show 25994142:<path>`, `git diff 11ed17b8..main -- <path>`, `git diff 25994142 <tip> -- <path>`, `git diff --stat`, `uv run pytest -q …`, `uv run cobalt jobs restarts`; `git apply`, `cherry-pick`, `git mv`, `rm`, `mv`, `revert` appear only in `## NOT IN THIS JOB`/WHY as prohibitions. All within BUILD-HUB.md:14. | OK |
| 5 | `git grep -c -F "MIRROR_SOURCE_PREFIX = " 25994142 -- src/cobalt/radar/notes.py` / same on `HEAD`; same for the m2 test name on `25994142`; read `deploy-smoke.sh` :10, :118, :188 | `25994142`: `1` and `1`; HEAD notes.py: no match (before 0); test file absent on HEAD (before: marker 2 prints `No such file`, exit 2, card keeps `0` — card DECISIONS 4, deploy 1027 accepted absent). Markers 3 and 4 are `ls` (mapped `:10`/`:118`). Markers 1–2 are `grep -c -F "<string>" <path>` (mapped `:11`/`:122`). No curl, no `uv run`. | OK (NOTE 1) |
| 6 | `grep -n "RESTARTS: com" reports/radar-mirror-scope-check-2026-10-23.md` | `:192 RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`; card header identical; MIGRATIONS none | OK |
| 7 | read card `## RECORDS` | line "1020 FAILED (h) on the pre-existing radar CardSettingsError, rolled back clean; K3 restore runs before the re-ship on his "Restore yes"; 1020 re-ships as a fresh PORT — brain 9b07db5a 2026-10-24" present; HOLD line "no radar-note edit until the port is DEPLOYED (R2410…)" present, and in `## NOT IN THIS JOB` | OK |
| 8 | read card ORDER and T1 | ORDER suite lists `test_radar_mirror_scope, test_radar_notes, test_radar_runner, test_radar_evaluate, test_radar_price_floor, test_drc_d4_fix_r1, test_radar_replay`; T1 ports `test_radar_replay.py` (17+, 4−) | OK |

## ISSUES
- NOTE 1: marker 2 `before` is `0` on the card but the file is absent on main (grep exit 2); the card records it (DECISIONS 4) and deploy 1027 took absent as valid. Not a block.
- NOTE 2: BASE `148b03ef` is no longer main's HEAD (`0db910de`, docs-only since); the desk resets BASE at launch (card DECISIONS 7). Not a block.
- NOTE 3: card has no `CLASS` line (994 had one); CARD.md header has no such key. Not a block.
- Nothing blocks the launch.

PREFLIGHT DONE · card: 1032 · checks: 8 · fails: 0 · ready: YES
