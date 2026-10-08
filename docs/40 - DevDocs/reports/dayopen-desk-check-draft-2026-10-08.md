# dayopen-desk-check — draft report 2026-10-08

## §0 Headline
- Card `prompts/2026-10-08/109-dayopen-desk-check-card.md` written: rows K1 (C7 in `checks.py`) and K2 (`runner.run` calls it last). Both are ready.
- C7 runs the existing `ops/desk/desk-list.sh` (repo copy) from Python. It needs no new command and no Qwen allow change.
- No `cto-desk` row → FAIL `desk missing — relaunch with desk-launch.sh desk` → OVERALL AMBER. Unreadable list → ERROR → RED.
- Not committed. BASE is the only fill token.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/109-dayopen-desk-check-card.md` (7991 bytes).
- Lines and tokens are the drafter's estimates; the build reports the real ones.

| row | files touched | est. lines changed | est. build tokens | state |
|---|---|---|---|---|
| K1 | 3 (checks.py, its test, DevDocs page) | ~120 | ~30k | ready |
| K2 | 3 (runner.py, its test, DevDocs page) | ~40 | ~15k | ready |

## DECISIONS
- D1 ASK DESK: a missing desk is FAIL, so the day is AMBER, not RED (`models.py:49-71`: RED is for a broken probe). DEFAULT: AMBER as written [08:15 ET].
- D2 ASK DESK: C7 has no calendar guard. It FAILs on any date with no live desk, weekends included. DEFAULT: no guard [08:15 ET].
- D3 ASK DESK: the "six" / "C1-C6" docstrings in `dayopen/__init__.py:3,6`, `models.py:1,4` and `cli.py:6` go stale. The card leaves them out of its files. DEFAULT: left, no row [08:15 ET].

## RECORDS
All reads were at main HEAD `c364bc43` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`, 07:4x EDT).
- `reports/cto-2026-10-08.md:11` R658 and `:13` R660, both `HIS RULING · APPROVED`. `:24` names this drafter `345ea582`, prompt `108`.
- `reports/desk-ops-fixes-draft-2026-10-08.md:24` D2 (B: C7 in `checks.py`, its own card).
- `src/cobalt/dayopen/checks.py` (468 lines): C1 `:87-101`, C6 `:391-452`, `__all__` `:455-468`, docstring `:1`. `REPO_ROOT` `:42`.
- `src/cobalt/dayopen/runner.py` (47 lines): results list `:28-37`. `models.py`: `overall_verdict` `:49-71`. `report.py`: `_verdict_table` `:40-45`, `render_markdown` `:54-68`.
- `tests/cobalt/test_dayopen_checks.py` (472 lines): C1 tests `:91-110`. `tests/cobalt/test_dayopen_runner.py` (55 lines): `:18-41`, `:44-55`.
- Grep `runner\.run` (`*.py`): the one caller is `src/cobalt/dayopen/cli.py:42`. `tests/cobalt/test_dayopen_cli.py:56,85` patch it.
- `ops/desk/desk-list.sh` (19 lines): row shape `:2-3,16`, id-less skip on stderr `:5-6,13-18`. `ops/desk/stop-guard.py:219-229`: `sh desk-list.sh`, timeout 20, non-zero exit raises. `ops/desk/desk-context.sh:43-46`: name field equals `cto-desk`. `ops/desk/desk-launch.sh:395`: the desk is `--name cto-desk`.
- `src/cobalt/jobs/restarts.py:178-264`: `src/` → `static import reach` `:215-220`; `tests/` → `test/documentation; no resident` `:245-246`; `docs/` → `DOCS` `:225-229`. `configs/cobalt/jobs.yaml`: no `dayopen` entry (Grep).
- `prompts/DAY-OPEN-QWEN.md:8-9`: the seat runs `cobalt day-open` only. Grep `day-open` (case-insensitive) under `ops/`: no file.
- `docs/40 - DevDocs/cobalt/dayopen/` holds `checks.md` and `runner.md` (`ls`).
- `reports/day-open-2026-10-07.md:164-176`: the VERDICT shape. Card shape: `prompts/CARD.md` whole; precedent `prompts/2026-10-08/106-desk-ops-fixes-card.md`; `BUILD-HUB.md:73-74` RESTARTS, `:93-97` PRE-STOP SELF-CHECK.

DAYOPEN DESK CHECK CARD DRAFTED · decisions: 3
