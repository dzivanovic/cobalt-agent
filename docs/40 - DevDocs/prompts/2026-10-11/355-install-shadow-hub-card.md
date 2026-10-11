JOB: install-shadow-hub-1011
LADDER: OFF-LADDER — reports/cto-2026-10-11.md R1069
BRANCH: ops/install-shadow-hub-1011
WORKTREE: install-shadow-hub-1011
BASE: 2322ed1e
TIP: 2322ed1e
REPORT: /Users/cobalt/cobalt-wt/install-shadow-hub-1011/docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/install-shadow-hub-check-2026-10-11.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-11 R1069

## ROWS

WHY: his override R1069 (row `R1069` of `reports/cto-2026-10-11.md`, `HIS RULING · APPROVED (via the brain, L79; words R1069)`: "install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel", committed at `HEAD` `2322ed1e`) installs the shadow gate seat. No preflight ran (his override; recorded). `SHADOW-HUB.md` holds three sign marks (the `## BUILDERS` rows, `:19-21`) and one install token (`:1`); `desk-launch.sh shadow` refuses on either (`ops/desk/desk-launch.sh:892-893` the token, `:1341-1342` the mark). `SPIKE-HUB.md` holds one token (`:1`) and one mark (`:24`); `desk-launch.sh spike` refuses on either (`:390-395`). Two fixed files change, so they change by card row, never in place. No row adds a command (R411, R412): the three builder allow strings and the spike line are signed as written.

| row | what | red first | files |
|---|---|---|---|
| S1 | Install, his R1069. `SHADOW-HUB.md`: the three sign cells (`:19`, `:20`, `:21`, column 6 of the `## BUILDERS` table) each replace the text `NEEDS HIS SIGN-OFF «SIGN: his row»` with `2026-10-11 R1069 · HIS RULING · APPROVED` (line 21 keeps its trailing ` · network: off (workspace-write default; X1 proves it)`); line 1's trailing `«INSTALL: his row»` becomes `HIS RULING · APPROVED 2026-10-11 R1069`. THE BUILD does line 1 by hand, as `306` I1 did, not `ops/desk/install-fixed.sh`: that script (`:10-11`, `:57`) would write `INSTALL: 2026-10-11 R1069 of his approval of STANDING-LIST.md`, a text about another file; `desk-launch.sh` reads line 1 only for the token (`:892`), so any title without `«INSTALL` passes. `SPIKE-HUB.md` (its `grep -c -F -e "«SIGN"` is 1, at `:24`): the same `NEEDS HIS SIGN-OFF «SIGN: his row»` becomes `2026-10-11 R1069 · HIS RULING · APPROVED`, and line 1 as in `SHADOW-HUB.md`. No other cell or line of either file changes (`wc -l` SHADOW-HUB 103, SPIKE-HUB 26 before and after). The tests that read the real files change with it: `tests/ops/test_spike_hub_file.py:91-92` (`test_p1_the_line_waits_for_his_sign_off`) becomes `test_p1_the_line_is_signed_on_his_row` (asserts the new cell text is in the file and `«SIGN` is not); `tests/ops/test_desk_launch_shadow.py:291` (the Terra refusal on the real file) becomes a launch that passes (`returncode == 0`), and ONE new test `test_the_real_file_holds_no_install_token_and_no_sign_mark` asserts `«INSTALL` and `«SIGN` (built as `"«" + "INSTALL"` and `"«" + "SIGN"`) are in neither real file. Backed by row `R1069` of `reports/cto-2026-10-11.md`, `SHADOW-HUB.md` `## BUILDERS` (`:15` "the launcher refuses a row that still holds it") | `grep -c -F -e "«SIGN" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → 3 on `BASE`, 0 after. `grep -c -F -e "«INSTALL"` on the same file → 1 on `BASE` (line 1), 0 after. `grep -c -F -e "2026-10-11 R1069 · HIS RULING · APPROVED"` on it → 0 on `BASE`, 3 after (the three cells; line 1's `HIS RULING · APPROVED 2026-10-11 R1069` is another string). `grep -c -F -e "«SIGN"` on `SPIKE-HUB.md` → 1 on `BASE`, 0 after; `grep -c -F -e "«INSTALL"` on it → 1 on `BASE`, 0 after. The launcher check that stops refusing: `desk-launch.sh:1341-1342` (`*"«SIGN"*) refuse "shadow: model $model: builder line not signed"`), `:892-893` (the token) and `:393-394` (spike). Tests that exist for those refusals and stay green, constructed fixtures: `test_an_unsigned_model_is_refused_beside_a_signed_one` (`tests/ops/test_desk_launch_shadow.py:208`), `test_the_install_title_is_refused` (`:233`), `test_the_sign_mark_is_refused` (`tests/ops/test_desk_launch_spike.py:148`). Red on `BASE`: the new `test_the_real_file_holds_no_install_token_and_no_sign_mark` fails on `«SIGN` in `SHADOW-HUB.md` (3 hits); `test_p1_the_line_is_signed_on_his_row` fails on the missing new text. Every row ends with `uv run pytest -q tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_spike.py tests/ops/test_spike_hub_file.py tests/ops/test_authorize.py tests/ops/test_install_fixed.py` → `0 failed` | `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (line 1 and lines 19-21), `docs/40 - DevDocs/prompts/SPIKE-HUB.md` (line 1 and line 24), `tests/ops/test_spike_hub_file.py`, `tests/ops/test_desk_launch_shadow.py` |

## NOT IN THIS JOB
- `ops/desk/desk-launch.sh`, `ops/desk/bare-guard.py`, `ops/desk/authorize.sh`, `ops/desk/install-fixed.sh`: built and deployed; this card reads them, never edits.
- Any other line or cell of `SHADOW-HUB.md` or `SPIKE-HUB.md`: the builder allow strings, the builder commands, the launch lines, `## RESULTS TABLE`, and `THE LINE'S SIGN` prose around the mark in `SPIKE-HUB.md:24` stand.
- The first shadow launch, its worktrees, the `grok`, `claude -p` and `codex exec` arms: the desk's, after this lands (only the lock serializes them).
- `STANDING-LIST.md`, LAWS, `NOW`, `.claude/settings.json`, any `settings.local.json`.
- A new command of any kind (R411, R412): a row that needs one is not built; the build stops with `decisions: 1`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md` whole (103 lines), lines 1, 15 and 17-21.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SPIKE-HUB.md` whole (26 lines), lines 1 and 24.
- `ops/desk/desk-launch.sh` lines 386-395 (spike gates), 888-893 (the token gate, kind shadow), 1327-1343 (the builder row and its sign check).
- `ops/desk/install-fixed.sh` lines 1-14 and 35-65.
- `tests/ops/test_desk_launch_shadow.py` lines 20-27, 205-213, 233-235, 276-291; `tests/ops/test_desk_launch_spike.py` lines 148-151; `tests/ops/test_spike_hub_file.py` lines 30-37 and 91-92.
- Precedent: `prompts/2026-10-10/306-ops-hand-install-card.md` (I1, I3).

## CHECK ASKS
- X1 Is each of the three `SHADOW-HUB.md` sign cells exactly `2026-10-11 R1069 · HIS RULING · APPROVED` (line 21 with its network note kept), and is the diff of each real file only those lines plus line 1 (`git diff --numstat`: `SHADOW-HUB.md` 4/4, `SPIKE-HUB.md` 2/2)?
- X2 Does `desk-launch.sh shadow` now pass its token gate and its sign check on the tree's own `SHADOW-HUB.md` for each of `grok-4.7`, `claude-sonnet-5-5` and `gpt-5.6-terra`, and `desk-launch.sh spike` on `SPIKE-HUB.md`; does `grep -c "^claude --bg "` stay 1 in each; no `<`, `>`, `\`, `$`, backtick, `;`, `&`, `|` newly on a launch line?
- X3 Does any other test or script read either file's line 1 or sign text (`grep -rn "SHADOW-HUB\|SPIKE-HUB" tests ops`)?
- X4 R1069 is his and approved: write no finding that rests only on the arms or the spike line being unsigned.

## RECORDS
- Read by the drafter `draft-install-shadow-hub`, 2026-10-11, against `HEAD` `2322ed1e` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`): `git -C /Users/cobalt/cobalt status --short` over `SHADOW-HUB.md`, `SPIKE-HUB.md`, `ops/desk/desk-launch.sh`, `ops/desk/install-fixed.sh` → empty, so the files equal `HEAD`.
- `grep -n -o "«SIGN"` on `SHADOW-HUB.md` → lines 19, 20, 21 (one each; three); the `## BUILDERS` table's column 6 is the cell the launcher reads (`desk-launch.sh:1341`, `awk -F'|' '{print $6}'`). `grep -n "«SIGN\|«INSTALL"` on `SPIKE-HUB.md` → `:1` (`«INSTALL: his row»`) and `:24` (`«SIGN: his row»`). `SHADOW-HUB.md` `«INSTALL` → `:1`. `SHADOW-HUB.md` has six `##` headings at `:7`, `:14`, `:31`, `:42`, `:65`, `:72`.
- The launcher's checks: kind shadow `desk-launch.sh:892-893` (`grep -q '«INSTALL'`, shared by every kind past `:888`), `:1341-1342` (`*"«SIGN"*) refuse "shadow: model $model: builder line not signed"`); kind spike `:390-395` (both greps). `install-fixed.sh` replaces only the span `«INSTALL … »` of line 1 and prints old and new (`:51-64`); it does not touch a `«SIGN`.
- Row `R1069` of `reports/cto-2026-10-11.md` (`:8`) holds `HIS RULING` and `APPROVED`; its last commit is `2322ed1e` (`git log -1 --format=%h -- <report>`), equal to `HEAD`. It names `SHADOW-HUB` and not `SPIKE-HUB` (see the report's `## DECISIONS`).
- No preflight ran: his override R1069, brain direction, L79.
- `authorize.sh` serves kind shadow (`:3`, `:51`: `shadow) hub=SHADOW-HUB.md`); `grep -n "SHADOW-HUB\|shadow" ops/desk/authorize.sh` → `:3`, `:4`, `:51`, `:45`, `:52`.
- RESTARTS: every path is `docs/` or `tests/ops/` (`DB: none`); `uv run cobalt jobs restarts <BASE>..HEAD` is UNPROVEN at drafting (no `uv` on the drafter's allow list), the build hub runs it.
- `BASE` and `TIP` are the desk's: `BASE` is `main` at the launch, the desk re-writes it if `main` has moved; `TIP` starts as BASE and is rewritten after the build, before the check. Docs and ops tests only: house A is Grok, `HOUSE B: as needed`, never OpenAI (R920).
