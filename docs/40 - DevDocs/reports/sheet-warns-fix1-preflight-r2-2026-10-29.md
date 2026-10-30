# Preflight r2 — card 1082 fix row S1 — 2026-10-29

Read: prompt 1093, the card (whole), drafter r2, round-1 preflight, `BUILD-HUB.md:14-16`. Refs: HEAD `107dc5a5d`, branch `ops/sheet-check-warns` = `d57714468` (rev-parse).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | round-1 FAIL 3a (`uv run python -c` runs) | `git diff HEAD~3 HEAD -U0 -- <card>`: row S1 now says no snippet run is made; the old red/green run text is gone | OK |
| 1b | round-1 FAIL 3b (`bash -n`) | `bash -n` appears only in "the BUILD line allows no … `bash -n`"; no run asked | OK |
| 1c | round-1 NOTE 1 (`ORDER:` lacks S1) | `ORDER:` now reads `… D1, S1 (its two greps), the commit, R1, …` | OK |
| 1d | round-1 NOTE 3 (`:80-98`) | the row now says `:80-100`; `git show ops/sheet-check-warns:scripts/smoke_s1.sh`: grade steps `:80` to the last `except SheetMismatch` at `:100` | OK |
| 1e | round-1 NOTE 2 (header TIP behind tip) | `TIP: 01107570` still; `git diff 01107570 ops/sheet-check-warns --stat`: only the build report, `.result`, `test_aset_web.py`, `test_radar_card_routes.py`; no `smoke_s1.sh`, no `match.py` | OK (desk-owned, NOTE 1) |
| 2a | every command S1 gives the builder vs `BUILD-HUB.md:14` | `grep -n -F "assert_sheet_matches" scripts/smoke_s1.sh`, `grep -n -F "sheet_warning" scripts/smoke_s1.sh` (`Bash(grep *)`); the test-pin read is `Read`; `git grep` named only as a past fact; no `uv run python`, `bash -n`, `sh -n` asked | OK |
| 2b | banned verbs in the row (`git mv`, `git rm`, `rm`, `mv`, `revert`, `cherry-pick`) | none in the row | OK |
| 2c | `git show ops/sheet-check-warns:scripts/smoke_s1.sh`, the old step | `assert_sheet_matches` only at `:103` (import) and `:106` (call); after the edit the first grep prints nothing (exit 1); `sheet_warning` is absent now, and the new import line and the `print(sheet_warning(` line give two hits | OK |
| 2d | `git grep -n -E "smoke_s1\|_smoke_cards\|assert_sheet_matches" ops/sheet-check-warns -- tests src ops` | no output: no test pins the script, no other user of the old name in `src`, `tests`, `ops` | OK |
| 3 | `git show ops/sheet-check-warns:tests/cobalt/test_daymode.py`, `:395-404` | `test_full_sheet_attested_on_a_reduced_day_warns` asserts `sheet_warning({"attested_sheet": "full.htk"}, "reduced", cfg=cfg) == "sheet FULL loaded, day mode REDUCED (= the HALF sheet) — reload half.htk or overrule"`; the string matches `match.py` `sheet_warning` (`:111-114`) | OK |
| 4 | `ORDER:` position | S1 after D1, before "the commit" | OK |
| 5a | `git diff HEAD~3 HEAD -U0 -- <card>` | exactly two changed lines: row S1 and `ORDER:`; `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`, `RULINGS` untouched | OK |
| 5b | row S1 `files` column | `scripts/smoke_s1.sh` only | OK |
| 6a | `UNPROVEN (L70)` wording | present: `UNPROVEN (L70) — S1 snippet not run (uv run python not on the BUILD line)`, to go under `## DECISIONS` | OK |
| 6b | buildable otherwise | new snippet has no `try`/`except`, so `None` prints `NO WARNING` and a raise prints a traceback; both lack the needle and FAIL; description and needle stay; row cites `d57714468` lines correctly | OK |

## ISSUES
- NOTE 1: header `TIP: 01107570` is behind the branch tip `d57714468`; the two commits between them do not touch `scripts/smoke_s1.sh` or `match.py`. The desk owns the header; S1 does not depend on it.
- NOTE 2: the new snippet's pass relies on `cfg.lowest_enabled` being the reduced rung in the dev settings (as the old step did); it is part of the `UNPROVEN (L70)` snippet run, not a blocker.

Nothing blocks the launch.

PREFLIGHT DONE · cards: 1082-S1 · checks: 14 · fails: 0 · ready: YES
