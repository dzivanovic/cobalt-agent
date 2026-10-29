JOB: sheet-check-warns
LADDER: OFF-LADDER — reports/cto-2026-10-29.md R2563
BRANCH: ops/sheet-check-warns
WORKTREE: sheet-check-warns
BASE: 78a6ab4a
TIP: 01107570
REPORT: /Users/cobalt/cobalt-wt/sheet-check-warns/docs/40 - DevDocs/reports/sheet-check-warns-build-2026-10-29.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/sheet-check-warns-check-2026-10-29.md
HOUSE B: as needed
BAND: HIGH
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
MIGRATIONS: none
RULINGS: 2026-10-29 R2563

## ROWS

WHY: his ruling R2563, the desk's reading A: the `.htk` sheet check WARNS and never refuses. Today `assert_sheet_matches` (`src/cobalt/daymode/match.py:80-117`) raises `SheetMismatch` when the attested sheet is not the mode's sheet (`:110-116`) or nothing is attested (`:99-107`), and two card paths refuse on it: `/size` (`src/cobalt/aset/web.py:1033`, caught `:1035-1037`) and the radar key tap (`web.py:1771`, caught `:1783-1784`, 409). The banner calls it too (`web.py:608-614`). After this job the same two messages are a warning line, the card is written, and `day_modes.attested_sheet` is not written by either path. `assert_grade_allowed` (`match.py:120-143`) stays as it is.

| row | what | red first | files |
|---|---|---|---|
| T1 | THE TESTS, first. (a) `tests/cobalt/test_daymode.py` `TestMatchCheck` (`:394-428`) moves to `sheet_warning`: the full sheet on a reduced day RETURNS `"sheet FULL loaded, day mode REDUCED (= the HALF sheet) — reload half.htk or overrule"` (no raise); `half.htk` returns `None`; `{}` and `None` return a string holding `No hotkey file attested`; `reduced_day.htk` and `made_up.htk` still raise `ConfigError` `unknown hotkey file`. The import (`:31-33`) keeps `SheetMismatch` (the grade tests `:191`, `:436`, `:453` use it). (b) with-DB `:518-525`: attest `full.htk`, decide `reduced`: `sheet_warning(row, …)` returns the reload string AND `store.for_date(day)["attested_sheet"] == "full.htk"` after. (c) `tests/cobalt/test_aset_web.py` `TestMatchCheckAtTheSheet` `:432-448` (with-DB, skipif as today): `full.htk` on a reduced day, and nothing attested, each `POST /size` → `"never reach AsetStore" in r.text` (the card went on to persistence, as `:462`) and the warning text in `r.text`; the stub's `row` dict is unchanged after the call. (d) `tests/cobalt/test_radar_card_routes.py:113-119`: `full.htk` → `200`, `"reload half.htk" in body["sheet_warning"]`, one tap in `cards.calls`; a new test beside it, row `{}` → `200`, `"No hotkey file attested" in body["sheet_warning"]`; `:83-92` (matching sheet) asserts `body["sheet_warning"] is None`. Names end in `_warns` where they said `_refuses` | RUN on BASE's `src/`: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_daymode.py tests/cobalt/test_radar_card_routes.py`, quoted whole. RED, by name: (a) collection `ImportError: cannot import name 'sheet_warning'`; (d) `assert 409 == 200`. (b), (c) are with-DB: their red is read at the gate's pass on BASE only if the builder runs it; otherwise `UNPROVEN (L70)` under `## DECISIONS` | `tests/cobalt/test_daymode.py`, `tests/cobalt/test_aset_web.py`, `tests/cobalt/test_radar_card_routes.py`, `tests/cobalt/test_sheet_daymode_probe.py` (the docstring `:127-129` only) |
| M1 | `src/cobalt/daymode/match.py`: `assert_sheet_matches` becomes `sheet_warning(row, mode, *, cfg=None) -> Optional[str]`. Same reads (`:94-97`, `:109`); returns `None` when `attested_sheet == expected_sheet`; returns the mismatch string of `:112-113` unchanged; with nothing attested returns `f"No hotkey file attested for today — Cobalt cannot read DAS (it never touches a trading platform). Day mode is {mode.upper()} (= the {expected_sheet.upper()} sheet); the matching file is {expected}."`. It raises nothing of its own (`cfg.sheet_for_hotkey_file` keeps its `ConfigError`, `config.py:234-239`). `__all__` (`:146`) and `src/cobalt/daymode/__init__.py:27,62` name `sheet_warning` for `assert_sheet_matches`. `SheetMismatch` (`:71-77`) and `assert_grade_allowed` unchanged. The module docstring (`:1-59`) and the function's (`:86-93`) say: attested, not read; a mismatch or no attestation is a WARNING on the sheet and the card (R2563); `note.py`'s conflict refusal (`:57-59`) unchanged | T1 (a) GREEN | `src/cobalt/daymode/match.py`, `src/cobalt/daymode/__init__.py` |
| W1 | `/size` (`src/cobalt/aset/web.py:1025-1037`): `assert_sheet_matches(...)` → `sheet_warn = sheet_warning(dm["row"], dm["mode"], cfg=dm["cfg"])`; `assert_grade_allowed` (`:1034`) stays and still refuses. A warning is logged once, `logger.warning("aset.card SHEET WARNING (F6, attested not read): {}", sheet_warn)` (the refusal's `logger.error`, `:1036`, stays for `SheetMismatch` from the grade check and the unresolved day mode `:1011-1015`). Every `_render` return after the check (`:1049-1051`, `:1058-1062`, `:1076-1080`, `:1083-1088`, `:1089-1096`) carries ONE line before its banner: `<div class="warn">⚠ .htk: {html.escape(sheet_warn)} (attested, not read)</div>` when `sheet_warn` is set. The comment `:1025-1032` says the check warns | T1 (c) GREEN | `src/cobalt/aset/web.py` |
| W2 | radar key tap (`web.py:1769-1800`): `:1771` → `sheet_warn = sheet_warning(...)`, logged as W1; the tap goes on; both JSON answers after it (`:1795-1798`, `:1799-1800`) carry `"sheet_warning": sheet_warn` (`None` when it matches). `:1783` keeps `SheetMismatch` (raised by `_todays_rung` `:1745`) | T1 (d) GREEN | `src/cobalt/aset/web.py` |
| W3 | the banner (`web.py:606-614`): `sheet_warning(...)` → `None` renders `✓ {attested} matches` (`:610`), a string renders `⚠ {warning}` with `klass = "mode mismatch"` (`:613-614`); the `(attested, not read — Cobalt never touches DAS)` span (`:628`) stays. Comments `:536-538` and `:966-968` name `sheet_warning` and drop "refuses every card" for the sheet check (an unresolved mode still refuses, `:1011-1015`) | T1 (c) GREEN, the banner test files unchanged and green | `src/cobalt/aset/web.py` |
| D1 | DevDocs per changed `.py` (Build rules): `docs/40 - DevDocs/cobalt/daymode/match.md` and `docs/40 - DevDocs/cobalt/aset/web.md`, one dated section `## 2026-10-29 — sheet-check-warns` each: the sheet check warns, never refuses (R2563); the grade check and an unresolved mode still refuse | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/daymode/match.md`, `docs/40 - DevDocs/cobalt/aset/web.md` |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE; the header's `RESTARTS` is the drafter's reading (`## RECORDS`), the tool's last line is the record | — (tool output quoted in the report) | none |

ORDER: T1 (its RED run), M1, W1, W2, W3, the touched files' offline run `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_daymode.py tests/cobalt/test_radar_card_routes.py tests/cobalt/test_aset_web.py tests/cobalt/test_sheet_daymode_probe.py` (whole, quoted, `0 failed`), D1, the commit, R1, the `## DEPLOY PROOF` marker reads on the tree, the deploy gate (BUILD-HUB `## W`, `gate.sh … --deploy`), the stop line. No with-DB test needs a level above `0013`: no `ops/desk/gate-lists.md` edit.

## NOT IN THIS JOB
- `assert_grade_allowed` and `daymode.reduced_enabled_grades` (`match.py:120-143`): unchanged; a key outside the rung is still refused.
- `day_modes.attested_sheet`: no new write; `/attest` (`web.py:1226-1265`) unchanged, its empty-file refusal (`:1240-1245`) included.
- The unresolved day mode refusals (`web.py:597-599`, `:1011-1015`, `:1742-1748`) and `note.py`'s note/selector conflict (`NoteAttestationConflict`, `web.py:560-564`).
- The fill legs' `sheet_mismatch` flag (`tests/cobalt/test_fill_transaction_db.py:325-339`): read, not refused; unchanged.
- `daymode.enabled_modes` and any settings row: card 1081. Any production command, any migration, any plist.
- Option B (the check off): not drafted.

## READ
- `src/cobalt/daymode/match.py` whole; `src/cobalt/daymode/config.py:189-239` (`sheet_for`, `hotkey_file_for_sheet`, `sheet_for_hotkey_file`).
- `src/cobalt/aset/web.py:530-640`, `:993-1100`, `:1742-1800`.
- `tests/cobalt/test_daymode.py:390-456`, `:510-526`; `tests/cobalt/test_aset_web.py:40-100`, `:412-462`; `tests/cobalt/test_radar_card_routes.py:55-120`.

## CHECK ASKS
- X1 Does any card path still refuse on the sheet check: `git grep -n "assert_sheet_matches" <tip> -- src tests` prints nothing, and every `sheet_warning(` call in `web.py` is followed by the card's write, not a return?
- X2 Is `day_modes` written by `/size` or the key tap on the tip (any `attest_sheet`, `UPDATE day_modes`, `store.decide` on those paths)?
- X3 Is the warning visible on every `/size` banner after the check and in both key-tap JSON answers, escaped, with "attested, not read"?
- X4 Does `assert_grade_allowed` refuse A+ on the reduced rung on the tip (`test_daymode.py:435-440` green, `test_aset_web.py:451-456` green)?
- X5 RESTARTS re-derived: does `uv run cobalt jobs restarts <BASE>..<tip>` end `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`?
- X6 Scope: R2563 reading A stands; write no finding that rests on restoring the refusal.

## DEPLOY PROOF
- `grep -c -F "def sheet_warning(" /Users/cobalt/cobalt/src/cobalt/daymode/match.py` · before `0` · after `1`
- `grep -c -F "def assert_sheet_matches(" /Users/cobalt/cobalt/src/cobalt/daymode/match.py` · before `1` · after `0`
- `grep -c -F "assert_sheet_matches(" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `3` · after `0`
- the match module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/daymode/match.py` · exit 0, listed
- the web module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, listed

## RECORDS
- HITL: the sheet check is his own trading check (Charter §3 F6, `match.py:3-5`); the change is ruled, R2563 (`cto-2026-10-29.md:13`), the desk's reading A.
- Two card paths refuse on `SheetMismatch` from the sheet check (`git grep -n "assert_sheet_matches" main -- src`): `web.py:1033` (`/size`), `web.py:1771` (radar key); plus the banner `web.py:609`. Other `SheetMismatch` raises in `web.py` (`:1012`, `:1241`, `:1247`, `:1745`) are not the sheet check.
- `git grep -c -F "assert_sheet_matches(" main -- src/cobalt/aset/web.py` → `3`; `… src/cobalt/daymode/match.py` → `1`.
- RESTARTS reading: `cobalt.daymode` is imported by `src/cobalt/aset/*`, `src/cobalt/radar/runner.py`, `src/cobalt/radar/evaluate.py`, `src/cobalt/prefill/daily.py`, `src/cobalt/heartbeat/runner.py` (git grep, main); `prefill/daily.py` derived `com.cobalt.aset com.cobalt.cos com.cobalt.radar` (card 1049 R5). R1's table is the record.
- Independent of card 1081 (the settings load); either may deploy first.
