# draft-402-seam-row-s — 2026-10-12

## §0 Headline
- Added ONE row `S` to `prompts/2026-10-12/392-prodwrite-seat-card.md` `## ROWS`, after W8 (1 line inserted, `git diff --stat`: 1 insertion).
- Row text is the brain's, byte for byte, in the `what` cell. Files: `ops/desk/desk-done.sh`, `tests/ops/test_desk_done.py`.
- Test column names 3 tests of this card and 3 functions (6 cases) of launcher-shadow-check (card 386 L9).
- Header (TIP, BASE) and every other line untouched; no placeholder token.

## DECISIONS
- ASK DESK: `1966c239` is a merge commit whose own diff is one report; the tests it brought to `test_desk_done.py` are card 386's `test_386_f1/f2/f3` (from `ba37c2a9`, merged in). Row S names those. Default: keep as written. [10:24 ET]
- ASK DESK: the row has 4 columns as this card's table does (row, what, red first, files), the shape of 156 row S; parametrized tests are named by function, with the case count in words, not by pytest param id. Default: keep. [10:24 ET]

## RECORDS
- Reads 10:24 ET, `main` HEAD `c1112721`... `git rev-parse main` = `c11127219081f8210c86c6d0509031ddb68e8082`.
- Row shape: `grep -rn "^| S "` over `prompts/`: 156 row S at `2026-10-09/156-https-only-card.md:25`, 231 row S at `2026-10-10/231-ops-hand-card.md:22`; the card's columns at `392-prodwrite-seat-card.md:17`.
- `git diff 86b9daa5 89fd13c5 --stat`: desk-done files are `ops/desk/desk-done.sh` (12 lines) and `tests/ops/test_desk_done.py` (32 insertions) only; this card touches no other desk-done file.
- This card's tests (tip `89fd13c5:tests/ops/test_desk_done.py`): `test_d1_a_written_prodwrite_report_stops_removes_and_closes_the_tab_in_order`, `test_d2_a_failed_prodwrite_is_refused_and_kept`, `test_d2_a_build_on_a_written_line_is_still_running`.
- Launcher-shadow-check's tests (`git diff 86b9daa5 1966c239 -- tests/ops/test_desk_done.py`, 42 insertions; on main `tests/ops/test_desk_done.py:166` (f1, 2 params), `:182` (f2, 3 params, def at `:187`), `:196` (f3)); `1966c239` is a merge (`git show --stat`: one report file).
- `ops/desk/desk-done.sh` on main holds `shadow` at `:2`, `:6`, `:9`, `:20`, `:27-28` and no `prodwrite` (Grep count 0): the hunks of both cards touch the same lines (usage, kind case), hence the seam.
- `git status --short` of both desk-done files: clean. Card diff: 1 insertion.

DRAFTED · decisions: 2
