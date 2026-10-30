# DRAFT — card 1082 fix row S1 — 2026-10-29

## §0 Headline
- Added ONE row, `S1`, to card 1082 (before `R1`): `scripts/smoke_s1.sh:101-108` calls `sheet_warning` and passes only on `reload half.htk`; backed by check O1.
- Proof named in the row: old snippet red (`ImportError`), new snippet green, `bash -n`, `grep` empty; no pytest or tests/ops pins the script.
- BASE/TIP/CHECK REPORT/HOUSE B/RULINGS/RESTARTS untouched. Two items for the desk below.

## DECISIONS
1. ASK DESK: the card's `ORDER:` line and the `## DEPLOY PROOF` list do not name `S1`; I was told no other edit. Default: the desk adds `S1` to `ORDER` after D1 (before the commit) and adds no DEPLOY PROOF line (a script, not a deployed module). [20:05]
2. ASK DESK: `load_daymode_config()` reads `cobalt_dev` settings, so S1's two snippet runs need the job's lock. Default: the builder runs them under the lock; otherwise `UNPROVEN (L70)` under its `## DECISIONS` (written into the row). [20:05]
3. ASK DESK: `RESTARTS` unchanged (`com.cobalt.aset com.cobalt.cos com.cobalt.radar`). A change to `scripts/smoke_s1.sh` may map to `-` or to its own rule in the `cobalt jobs restarts` table. Default: R1's table is the record; the header stands unless the table's last line differs. [20:05]

## RECORDS
- `date` → `Thu Oct 29 20:03:24 EDT 2026` (start); `Thu Oct 29 20:03:53 EDT 2026` (after edits).
- Read whole: the prompt 1090; card `1082-sheet-check-warns-card.md`; check report `sheet-check-warns-check-2026-10-29.md` (`## OWN FINDINGS` O1, `## RUNS`, `## OPEN`, `## DECISIONS`). `prompts/CARD.md`: row-table shape and `RUN`/`red first` conventions (grep of its lines, not whole).
- `git -C … show ops/sheet-check-warns:scripts/smoke_s1.sh`: step `:101-108`; `assert_sheet_matches` at `:103`, `:106`; grade steps import `SheetMismatch` at `:81,88,95`; selector step `:109-112`.
- `git -C … show ops/sheet-check-warns:src/cobalt/daymode/match.py`: `sheet_warning` `:84-117`, returns the reload string for `full.htk` on `reduced`, `None` on match; `assert_grade_allowed` `:120`.
- `git grep -n -E "sheet_warning|assert_sheet_matches" ops/sheet-check-warns -- src/cobalt/daymode/__init__.py` → `:28` import, `:63` `__all__`; no `assert_sheet_matches`.
- `git grep -n -E "assert_sheet_matches" ops/sheet-check-warns -- scripts` → only `smoke_s1.sh:103,106`.
- `git grep -n -E "smoke_s1|_smoke_cards" ops/sheet-check-warns -- tests` → no output: no test pins the script.
- `lowest_enabled` is `min(enabled_modes, key=rank)` (`config.py:178`), so `reduced` stays the step's mode when card 1081 enables more modes.
- Edit: `docs/40 - DevDocs/prompts/2026-10-29/1082-sheet-check-warns-card.md`, one row inserted; no other line changed. Nothing run against a database; nothing committed.

DRAFTED · decisions: 3
