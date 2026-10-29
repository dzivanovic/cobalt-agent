# draft-launcher-tip-prefix — 2026-10-29

## §0 Headline
- Card drafted: `prompts/2026-10-29/1085-launcher-tip-prefix-card.md` (K5, BAND HIGH, 3 rows: T1 tests, A1 launcher, A2 preflight).
- Rule: the stop-line tip is the card's 8-hex TIP, then nothing, a space, or hex only; a different prefix, a shorter tip or a non-hex tail stays refused.
- Sites: `ops/desk/desk-launch.sh:2133-2134` and `ops/desk/preflight.sh:285` (the SHADOW arm). `desk-launch.sh:1773` needs no change.
- Three existing tests flip (`test_desk_launch_prechecks.py:342`, `:411/:420`; `test_preflight.py:462`): the card names them.
- `BASE` is left `«FILL»`; `TIP`, `CHECK REPORT`, `HOUSE B` are empty for the desk.

## DECISIONS
- ASK DESK: include `preflight.sh:285` (SHADOW arm) in this job? Without it a shadow check the launcher admits fails `FAILED PREFLIGHT: report`. Default: yes, built as row A2 [18:58 ET]
- ASK DESK: tighten `preflight.sh:273` (the BUILT arm is a prefix glob that already admits any tail, hex or not)? Default: no, out of scope, carried as an item in `## NOT IN THIS JOB` [18:58 ET]

## RECORDS
- `date`: 2026-10-29 18:58 ET.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1084-draft-launcher-tip-prefix.md`, read whole.
- `prompts/CARD.md`, read whole (header keys, body sections, DEPLOY PROOF form); `prompts/2026-10-29/1082-sheet-check-warns-card.md` lines 1-22 (header and row shape); `prompts/2026-10-15/580-close-automation-card.md` `## DEPLOY PROOF` (form).
- `ops/desk/desk-launch.sh` lines 1700-1784 and 2115-2144 (working tree); `git grep … main` for `tip: $` in `ops/desk`: `desk-launch.sh:1523, 1810, 2133, 2134`; `preflight.sh:273, 285`; `deploy-step0.sh:275, 783`; `deploy-card.sh:264`.
- `ops/desk/preflight.sh` read whole via `git show main:ops/desk/preflight.sh`.
- `tests/ops/test_desk_launch_prechecks.py` lines 325-459; `tests/ops/test_preflight.py` lines 418-480; `git grep -l desk-launch main -- tests`: test home is `tests/ops/`.
- `ls -l /Users/cobalt/.claude/ops/desk-launch.sh /Users/cobalt/.claude/ops/preflight.sh`: both symlinks into `/Users/cobalt/cobalt/ops/desk/`.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main`: `c29d13e9`.
- No test run, nothing committed, no existing file edited.

DRAFTED · decisions: 2
