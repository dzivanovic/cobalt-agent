JOB: note-daily-stop
LADDER: OFF-LADDER — cto-2026-10-01.md 2026-10-01 R15
BRANCH: s3/note-daily-stop-1001
WORKTREE: note-daily-stop-1001
BASE: 986e34c2
TIP:
REPORT: /Users/cobalt/cobalt-wt/note-daily-stop-1001/docs/40 - DevDocs/reports/note-daily-stop-build-2026-10-01.md
CHECK REPORT:
HOUSE B: mandatory — vault notes
TREE STATE: unchanged
RULINGS: 2026-10-01 R15

## ROWS

| row | what | red first | files |
|---|---|---|---|
| D1 | RUN — asserts nothing. Today's note (`1 - Trading/1- Daily Notes/2026-10-01.md`, his vault, READ ONLY) shows `Daily HARD Stop: full $210 · half $420`; his sizing is full = twice half (`B = $30 half / $60 full`), so full should carry the LARGER stop. Trace the value from `src/cobalt/prefill/daily.py:166` (`format_daily_stop`) to `cobalt.settings.drc.daily_risk_values` (`DAILY_STOP_KEYS`, `settings/models.py:173-174`: full → `account.daily_stop_full`, half → `account.daily_stop_half`) and quote each hop. Say plainly whether the code maps each sheet to its own key (the desk's read says it does, so the stored `account.daily_stop_full` / `account.daily_stop_half` rows hold 210 and 420: swapped data), and quote the `trader_settings` read (`COBALT_ENV=dev`, read only) or the sheet's own `DAILY STOP FULL NOW 210 · HALF NOW 420` read. He did NOT type these numbers (R16: the values were already in the sheet's boxes): find EVERY WRITER of `account.daily_stop_full` / `account.daily_stop_half` in code (`grep -rn` over `src/`, `configs/`, `ops/`, the morning and day-open scripts, `drc/` import, `cobalt settings load`, the ASET change line `/settings/daily/apply`, any template or optional-settings file) and for each say whether it can write the two keys in the swapped order, quoting the line. Production reads are refused to the desk and to this build (classifier `[Production Reads]`): the write history (`source`, `updated_at` of the two rows) is `## DECISIONS`, FOR DEJAN, never worked around. A code mapping that IS swapped is row D2's fix; swapped data is NOT touched by this build and is `## DECISIONS` | — (tool output quoted in the report) | none (read only) |
| D2 | If D1 finds a swapped mapping anywhere on a path that writes a daily note, a settings display or the DRC, fix it at its single owner and pin it. If D1 finds the code right, D2 is `none — data` and nothing changes | test: a fake settings source with full 420 / half 210 renders `full $420 · half $210` in the note line and in the sheet's daily-stop line; RED on `BASE` only if the mapping is wrong | `src/cobalt/prefill/daily.py`, `src/cobalt/settings/drc.py`, `tests/cobalt/` (the file that pins `format_daily_stop`) |
| D3 | AFTER HE ATTESTS a size (`POST /attest`, `src/cobalt/aset/web.py:1202`, which today strikes the attestation line at the bottom of the daily note), the note's `Daily HARD Stop:` value is also rewritten to the ATTESTED sheet's stop only: attested full → `Daily HARD Stop: full $<full>`; attested half → `Daily HARD Stop: half $<half>`; before any attestation it keeps both values (today's line). It goes through the vault writer's existing marker-bounded unit with its version and human-wins rules (L28), in the same call that strikes the attestation, so the two never disagree; a failed rewrite is a loud failure on the sheet (L1), never a silent skip, and the attestation itself still stands. A second attest (a changed size) rewrites it again. Values come from `daily_risk_values()` (L3), never typed | tests (a tmp_path vault, never his): (a) attest full → the line holds only the full value and the attestation is struck; (b) attest half → only the half value; (c) no attestation → both values, as today; (d) he edited the line by hand before the attest → his text wins and the sheet says so (L28); (e) the vault write fails → the banner is FAILED and the attestation is unchanged. RED on `BASE`: (a) the line still holds both values | `src/cobalt/aset/web.py`, `src/cobalt/prefill/daily.py` (the line's one renderer), `tests/cobalt/test_aset_web.py` and the daily-note test file that pins the template |

## NOT IN THIS JOB
- The stored settings values: if D1 shows them swapped, the build says so and writes nothing (his settings change line, or his word, fixes them).
- `/radar`, the card forms, the CLOSE button and form order of `aset-interim-close` (`04-aset-interim-close-card.md`): a different job on the same file `src/cobalt/aset/web.py`; this build rebases on its merge, never edits its rows.
- His vault: every test writes to a `tmp_path` vault; his notes are read only.
- Any other line of the daily note or the unit markers.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-01-words.md` `## R15`.
- `src/cobalt/prefill/daily.py` lines 80-200 and 400-480; `src/cobalt/aset/web.py` `/attest` (~1202-1300) and the daily-note write it makes; `src/cobalt/settings/drc.py`; `src/cobalt/settings/models.py` lines 90-180.
- L28 and L3 in `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` (`grep -n "^### L28 "`).

## DECISIONS ASKED
- DECISION D-A: the exact text of the attested line (`Daily HARD Stop: full $420`, or with a trailing `(attested)`); the card ships the shorter form and the builder names the one marker-bounded unit that holds the line.
