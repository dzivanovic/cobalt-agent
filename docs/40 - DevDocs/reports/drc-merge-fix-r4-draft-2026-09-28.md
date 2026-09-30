# DRC merge fix r4 — classification and prompts 2026-09-28 — seat `drc-merge-fix-r4-draft-0928`

## §0 Headline
- `39`'s items (1)–(2) → FIX, ONE report-text row R4-1: `## FOR 08` re-issued whole; the three entries state their target (REVERSE's first ten, 0018…0008 → 0019…0009, read at `7cdc5774`); the RESTARTS bullet carries the `.clinerules` caveat; the ahead / behind count names branch head `84827649` and main at launch. `39` ESCALATE 4 → RECORD (packet discipline in `43`).
- Code change: none. With-DB: no. `42` runs the pin greps (P1–P12) and O only; no lock, no live-note leg.
- Written: `prompts/2026-09-28/42-drc-merge-fix-r4-build.md` (32,384 B) and `prompts/2026-09-28/43-drc-merge-fix-r4-check.md` (33,822 B; round 3 of ≤3, the last). New rule strings: 0.
- ESCALATE: 3.

## L74
A block arrived appended to the Bash tool result that printed `41-draft-drc-merge-fix-r4.md`. It asked every commit and PR body to carry a `Claude-Session:` line and named a file-send tool. It is data and was not followed. This seat commits nothing.

## Authorization
`grep -n -F "41-draft-drc-merge-fix-r4.md" ".../reports/cto-2026-09-28.md"` → `:110` `| R101 | 16:35 ET | — DESK LAUNCH ROW for \`41-draft-drc-merge-fix-r4.md\` …| LAUNCHED |` (and `:117`, the session row). Read Mon Sep 28 16:35:30 EDT 2026.

## Classification
Sources: `C3` = `reports/drc-merge-fix-r3-check-2026-09-28.md` (real lines); `R3` = `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-fix-r3-build-2026-09-28.md`; `R2` = the same folder's `drc-merge-fix-r2-build-2026-09-28.md`; `P39` = `prompts/2026-09-28/39-drc-merge-fix-r3-check.md`. Code lines at `7cdc5774` (`git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -3` at 16:39 ET: `84827649` over `509f19f5` over `7cdc5774`; no code above `7cdc5774`, `C3:27`).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | Three pin entries name a pin `0019` breaks but not the list `0019` makes it: `test_radar_score_migration.py:103–114` / `:116` / `:121` / `:126`, `test_tenancy.py:513–526`, `test_archiver_migrations.py:101–112` (`REVERSE[:10]`) | `C3:131`; walked `C3:112` (HOLDS); Opus `C3:65` | FIX — REPORT TEXT, row R4-1 | `R3:573` (the list's own rule: "→" = the slot or list once `0019` is `REVERSE[0]`; every sibling entry carries it); `P39:70` ("with the slot or list `0019` makes it"); L35 | `42` re-issues `## FOR 08` WHOLE (K16: the block sits in `42` verbatim); each of the three entries states 0018…0008 → 0019…0009 (or widened to eleven), with the list's name lines (`## PIN TARGETS`); P12 proves each line at the tip; the `## FOR 08` proof grep `0019…0009` must hit all four L-prefix entries. |
| 2 | RESTARTS bullet drops r2's "widened to all residents by the UNCLASSIFIED `.clinerules`" sentence; the ahead / behind count names no head it was read at | `C3:132`; walked `C3:113` (HOLDS); Opus `C3:83` | FIX — REPORT TEXT, in row R4-1 | `R2:603` (the sentence); `R3:605` (`38`'s own ESCALATE 1 names it; `R3:588` drops it); L42 ("unclassified → ESCALATE, never dropped"); `R3:71–72` (counts read on symbolic `main` / branch refs, heads unnamed) | Same row: the RESTARTS bullet ends "It is widened to all residents by the UNCLASSIFIED `.clinerules` (ESCALATE 1), OWED to the DRC deploy (R74)."; the counts are read by explicit shas `<main at launch>..84827649` / `84827649..<main at launch>` and the TIP bullet says "Counts read at branch head `84827649` against main `<sha>`". |
| E4 | Sol read files outside the packet folder (`CLAUDE.md`, INDEX, LAWS, `areas/cobalt.md` NOW) despite "Read ONLY the files in this folder" | `C3:139` | RECORD — packet discipline for round 3's staging | `P39:66` (the questions' read rule); L44 (same packet); L70 (a read, no write, no answer cites outside lines — not a defect) | `43`: every checker sentence carries "Open no path outside this folder."; THE READ FENCE records a path outside the folder from a checker's printed trail under `## ESCALATE`, never a stop, never a defect. |

`C3` ESCALATE 1–3 restate items (1)–(2); 5–10 are facts (no cut, no mismatch, no stray write, no L74 block, no moved line, Sol seated, the standing line): no class. Nothing here re-decides a resolution, F1–F8, G1, the guard, item (4) or the docs cells (`C3:3`).

## PIN TARGETS
Read by `git -C /Users/cobalt/cobalt show 7cdc5774:<path>` between 16:35:30 and 16:37:27 EDT, and re-grepped at the drc-d1 worktree (head `84827649`, tests = `7cdc5774`) at 16:37–16:39 EDT. REVERSE at `7cdc5774` begins 0018, 0017, 0016, 0015, 0014, 0013, 0011, 0010, 0009, 0008 (`src/cobalt/db_migrations/__init__.py:129–138`); with `0019` at `REVERSE[0]` its first ten are 0019…0009.

| file:line | pin | value `0019` makes it |
|---|---|---|
| `tests/cobalt/test_radar_score_migration.py:103–114` (names `:104` 0018 … `:113` 0008) | L `newest_four` = 0018…0008 | 0019…0009 (or eleven, 0019…0008, with each slice `[:11]`) |
| `test_radar_score_migration.py:116` | `reverse_names[:10] == newest_four` | follows `newest_four` |
| `test_radar_score_migration.py:121` | `_rollback_paths("0005")[:10] == newest_four` | follows `newest_four` |
| `test_radar_score_migration.py:126` | `_rollback_paths("0006")[:10] == newest_four` | follows `newest_four` |
| `tests/cobalt/test_tenancy.py:513–526` (`:513` selection, `:515` assert, names `:516`–`:525`) | L `selected[:10]` of `_rollback_paths("0004")` = 0018…0008 | 0019…0009 (or the slice widened to eleven) |
| `tests/cobalt/test_archiver_migrations.py:101–112` (names `:102`–`:111`) | L `REVERSE[:10]` = 0018…0008 | 0019…0009 (the mirror of `:84–95`'s 0009…0019) |

Unmoved by `0019` (suffixes, already under NOT PINS): `test_radar_score_migration.py:122`, `:127`; `test_tenancy.py:527–534`. Grok's round-2 answer states the same three targets (`grok-check.md`, (ii) "Lists").

## RECORDS
- `42` = `38`'s shape with the LIVE-NOTE leg removed (the drafter prompt: pin greps and O only) and P12 added; `## FOR 08`'s COUNTS bullet says r4 ran no live-note and carries `38`'s 146. R0 = three greps against `R3` (dry-run here: `0019…0009` → `581:` only; the caveat → exit 1, `R2` → `603:`; `read at branch head` → exit 1).
- `42`'s PREFLIGHT: head `84827649` exactly (else `FAILED: preflight — tip moved`); `.env` gate narrowed to drc-d1 (the drafter prompt's rule; another worktree's `.env` is recorded, not a stop — answers r3 draft ESCALATE 1).
- `42`'s RESTARTS range `10163d51..84827649` = its preflight head; its report commit adds one `docs/` path (L42). Stop line = the drafter prompt's template, `<tip>` read as `report-only (code 7cdc5774; tip = this report's commit)`.
- `43` = `39` narrowed: packet `for-08.md` · `build-proof.md` · `code-at-tip.md` (three slices + the registry) · `rules.md` · questions (i)–(iv). `## FOR THE CLASSIFIER` → `## FOR DEJAN` (round 3 is the last; no classifier follows, L39). Added: THE ANSWER FILES and THE READ FENCE.
- `comm`: `42` vs `38` quoted Bash tokens → 26 common, 0 / 0; line 5 identical after substituting path and name. `43` vs `39` → 15 common, 0 / 0; the `claude --bg …` span identical after substitution.
- Placeholders (the launch-row token, `grep -c -F`): `42` → 1 line (`:22`); `43` → 1 line (`:15`). `FILL AT LAUNCH`: `42` `:3` + the gate `:21`; `43` `:1` (definition), `:12` (gate), `:42` (`42`'s stop line and `<r4 tip>`), `:61` (ceiling).

## OWNER ITEMS
NONE.

## FOR DEJAN
New strings: NONE. `42` carries `38`'s 25 allow + 3 deny unchanged; `43` carries `39`'s 14 allow + 3 deny unchanged.

## FOR THE DESK
- Fill: `42` `:3` (drc-d1 head, main head, ET) and the launch-row token at `:22`; `43` `:42` (after `42` BUILT: its stop line, read time, `<r4 tip>` = `git -C /Users/cobalt/cobalt log -1 --format=%h drc/d1-trading-log`), `:61` (ceiling; drafter's estimate ≈ 110,000 B) and the launch-row token at `:15`.
- The `08` re-point: its registry-pin list enters at `prompts/2026-09-28/08-drc-d2-fix-r1-build.md:106` (`THE REGISTRY PINS …`, F0's name grep and pre-merge slots). `08` has no `FOR 08` string (`grep -n -F "FOR 08"` exit 1).
- Order: commit this report, `41`, `42`, `43`; launch `42`; after `42` BUILT, fill `43` and launch it. A HOLD from `43` goes to Dejan (L39).

## ESCALATE
1. RECORD: round 2's packet folder holds `grok-check.md` only (`ls` at 16:44 EDT); `opus-check.md` and `sol-check.md` were never written though `P39:79`/`:81` required it. Opus's and Sol's answers are cited through `C3`'s verbatim rows. `43` carries THE ANSWER FILES.
2. RECORD: `42` runs no live-note leg (the drafter prompt names pin greps and O only); `38`'s 146 stands in `## FOR 08`.
3. RECORD: `42`'s `.env` gate is drc-d1 only, narrower than `38`'s any-worktree gate, per the drafter prompt's PREFLIGHT.

## CONTINUE
next: none — the desk commits this report, `41`, `42` and `43`.

DRC MERGE FIX R4 DRAFTED · FIX: 2 · NOT REAL: 0 · UNPROVEN: 0 · OUT OF SCOPE: 0 · OWNER ITEM: 0 · code change: none · with-DB: no · prompts: 2 · new rule strings: 0 · ESCALATE: 3
