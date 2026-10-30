JOB: launcher-tip-prefix
LADDER: OFF-LADDER — reports/cto-2026-10-29.md R2571
BRANCH: ops/launcher-tip-prefix
WORKTREE: launcher-tip-prefix
BASE: 4f1c991f
TIP: 2edcf295
REPORT: /Users/cobalt/cobalt-wt/launcher-tip-prefix/docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-tip-prefix-check-2026-10-29.md
HOUSE B: as needed
DB: none
CLASS: K5
BAND: HIGH
RESTARTS: none
MIGRATIONS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: the brain ruled (L79, 2026-10-29, R2571 of `reports/cto-2026-10-29.md`): the check launcher admits a build whose stop line prints the card's 8-hex TIP followed by more hex. Git prints 9 hex when 8 are ambiguous, so a builder cannot avoid it; today `desk-launch.sh check` refuses it with `not built — <line>` (four recurrences on one day-chain, R2485, R2524, R2537, R2571; each cost a full builder round). K5 (ops script and tests only), no trading logic, no HITL step beyond the standing deploy approval. The launcher is `ops/desk/desk-launch.sh` in the repo; `/Users/cobalt/.claude/ops/desk-launch.sh` and `/Users/cobalt/.claude/ops/preflight.sh` are symlinks to `/Users/cobalt/cobalt/ops/desk/` (`ls -l`, read 2026-10-29 18:5x ET), so the build edits the two tracked files and `install-ops` has no new link to make.

THE RULE (all three rows): after the literal `BUILT · job: <JOB> · tip: <TIP>` (or `SHADOW BUILT · job: <JOB> · tip: <TIP>`), the line is admitted when what follows is nothing, or a space and anything (as today), or hex digits `[0-9a-f]` only up to the next space or the end of the line. Nothing looser: a different 8-hex prefix, a shorter tip, a non-hex tail (`<TIP>z`, `<TIP>9z`), another JOB or a JOB that only starts with the card's (`x-jobber`) stay refused. TIP is 8 hex by `hex8 TIP "$tip"` (`ops/desk/desk-launch.sh:2091`). A shape that works in POSIX `sh` (the files are `#!/bin/sh`): keep the existing `case` for the exact forms and add, before the refusal, `rest=${last#"BUILT · job: $job · tip: $tip"}; tail=${rest%% *}` then admit when `$last` starts with that literal and `case "$tail" in *[!0-9a-f]*) refuse;; esac`. The builder may choose another shape that passes the tests.

| row | what | red first | files |
|---|---|---|---|
| T1 | THE TESTS, first, in `tests/ops/test_desk_launch_prechecks.py` (the launcher's check-kind precheck home: `test_l2_*` at `:331-359`, `test_386_a2_*` at `:408-430`, `shadow_built` at `:391`, fixture tip `self.tip` at `:103`). (a) NEW `test_1085_t1_a_nine_hex_tip_on_the_built_line_launches`: `desk.write_build_report(desk.built_line(tip=desk.tip + "9"))`; `desk.launch("check", …)` returns 0 and `desk.called() == [str(desk.job_wt)]`. (b) NEW `test_1085_t1_a_different_eight_hex_prefix_refuses`: the line with `OTHER_TIP` (as `:341`) refuses `not built — <line>`; GREEN before and after. (c) NEW `test_1085_t1_a_nine_char_tip_with_a_non_hex_tail_refuses`, parametrized `desk.tip + "z"` and `desk.tip + "9z"`: refuses `not built — <line>`; GREEN before and after. (d) NEW `test_1085_t1_a_shorter_tip_refuses`: `desk.tip[:7]` refuses; GREEN before and after. (e) THE ONE EXISTING CASE THAT FLIPS: `test_l2_a_report_not_ending_in_its_built_line_refuses` carries `"BUILT · job: x-job · tip: TIP9 | on x"` (`:342`), which this rule admits; it becomes `"… tip: TIPz | on x"` (still refused). (f) SHADOW, `test_386_a2_job_and_tip_are_exact_as_for_built` (`:408-430`): the `("tip9", False)` case (`:411`, `:420`) becomes `("tip9", True)` and a `("tipz", False)` case with `shadow_built(desk, tip=desk.tip + "z")` is added | RUN on BASE's `ops/`: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py -k "1085 or test_386_a2"`, quoted whole. RED, by name: (a) `assert 1 == 0` on `done.returncode` with `stderr` `REFUSED: not built — BUILT · job: x-job · tip: <tip>9 | …`; (f) `tip9` `assert 1 == 0` the same way. (b), (c), (d) and `tipz` are GREEN on BASE and must stay so: the report quotes them as the boundary controls | `tests/ops/test_desk_launch_prechecks.py` |
| A1 | `ops/desk/desk-launch.sh` check kind, the L2 stop-line read: the two `case "$last"` arms at `:2133` (`BUILT`) and `:2134` (`SHADOW BUILT`, still refused unless `$shadow`, `:2135`) admit the rule above; `*) refuse "not built — $last"` (`:2136`) is unchanged. No other launcher site compares a stop-line tip with the card TIP: `:1523-1524` and `:1810` are `"BUILT ·"*"tip: $x"*` globs on a fix report (already admit a longer tip), and `:1773` is the deploy `.result` read, which shortens the result's tip with `git rev-parse --short=8` (a 9-hex tip there is already read as 8; nothing to change). A comment on the changed lines says `card 1085`: the stop-line tip is the card TIP or the TIP plus hex (git's 9-hex form), nothing looser | T1 (a) and (f) `tip9` GREEN; (b), (c), (d), (e) still green | `ops/desk/desk-launch.sh` |
| A2 | `ops/desk/preflight.sh`, the check PREFLIGHT `report` row's SHADOW arm `:285` (`"SHADOW BUILT · job: $job · tip: $tip"\|"SHADOW BUILT · job: $job · tip: $tip "*`): the same rule, so a shadow check the launcher admits does not then fail `FAILED PREFLIGHT: report`. Tests in `tests/ops/test_preflight.py`: NEW `test_1085_a2_a_shadow_check_with_a_nine_hex_tip_passes` beside `test_386_c1_…` (`:443`) using `SHADOW_LAST.replace("tip: {tip}", "tip: {tip}9")`: returncode 0, last line `PREFLIGHT OK`; the existing `:462` row `(SHADOW_LAST.replace("tip: {tip}", "tip: {tip}9"), "shadow/x-job", True)` of `test_386_c2_…` leaves the fail list and a `tip: {tip}z` row takes its place. The BUILT arm `:273` (`"BUILT · job: $job · tip: $tip"*"self-check: "[0-3]" of 3"*`) is a prefix glob and already admits a 9-hex tip: untouched (see NOT IN THIS JOB). A comment `card 1085` on the changed arm | RUN on BASE: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_preflight.py -k "1085 or test_386_c"`, quoted whole. RED, by name: the new `test_1085_a2_…` `assert 1 == 0` with last line `FAILED PREFLIGHT: report`. The `{tip}z` row is GREEN on BASE and after | `ops/desk/preflight.sh`, `tests/ops/test_preflight.py` |

## NOT IN THIS JOB
- `ops/desk/preflight.sh:273`, the BUILT arm: its `"…tip: $tip"*"self-check: "` glob already admits ANY tail after the tip, hex or not. Tightening it is a separate item; it is a `## DECISIONS` line, not built here.
- `ops/desk/deploy-step0.sh:783`, `deploy-card.sh:264`, `desk-launch.sh:1523`, `:1810`: fix-report globs, not the build stop-line compare; no change.
- The stop-line shape in `BUILD-HUB.md` and `SHADOW-HUB.md` (the fixed files): no wording change, the builder still prints what git gives it. No `hex8` change on the card's TIP (`desk-launch.sh:2091`): the card TIP stays 8 hex.
- `desk-launch.sh install-ops`, any plist, any `src/` file, any migration, any restart.
- A red outside this fix: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `ops/desk/desk-launch.sh:2091-2138` (hex8 of TIP, the `last` read, the two `case` arms) and `:1523-1524`, `:1773`, `:1810` (the sites named above as not changed).
- `ops/desk/preflight.sh:263-296` (the check `report` row, both arms).
- `tests/ops/test_desk_launch_prechecks.py:96-215` (`Desk`, `built_line`, `write_build_report`, `launch`, `called`), `:331-359`, `:391-430`; `tests/ops/test_preflight.py:420-480` (`SHADOW_LAST`, `write_shadow_card`, `test_386_c1_…`, `test_386_c2_…`).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-29.md` R2571 (the fourth recurrence) and the brain direction L79.

## DEPLOY PROOF
- `grep -c -F "card 1085" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after the count the builder quotes from its `TIP` (at least `1`)
- `grep -c -F "card 1085" /Users/cobalt/cobalt/ops/desk/preflight.sh` · before `0` · after the count the builder quotes from its `TIP` (at least `1`)
- `grep -c -F "test_1085" /Users/cobalt/cobalt/tests/ops/test_desk_launch_prechecks.py` · before `0` · after the count the builder quotes from its `TIP` (at least `4`)
- `grep -c -F "test_1085" /Users/cobalt/cobalt/tests/ops/test_preflight.py` · before `0` · after the count the builder quotes from its `TIP` (at least `1`)
- ONE SMOKE READ after the merge: `uv run pytest -q -p no:cacheprovider tests/ops/test_desk_launch_prechecks.py tests/ops/test_preflight.py` → `0 failed`.
- AFTER DEPLOYED, the desk's: `sh /Users/cobalt/.claude/ops/desk-launch.sh install-ops` once (card 580); its last line quoted: `0 linked` (both scripts are linked already, symlinks into `/Users/cobalt/cobalt/ops/desk/`), and `grep -c -F "card 1085" /Users/cobalt/.claude/ops/desk-launch.sh` prints at least `1`. The first real check launch on a 9-hex build stop line is the live proof (L81 (3)); a refusal the desk did not expect is a `## RECORDS` line, never routed around.

## RECORDS
- Drafter `draft-launcher-tip-prefix`, 2026-10-29 18:5x ET (the machine's `date`), `main` HEAD `c29d13e9` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main`). Every `file:line` here read with `git -C /Users/cobalt/cobalt grep -n … main -- <path>` (`desk-launch.sh:2133-2134`, `:1523-1524`, `:1810`; `preflight.sh:273`, `:285`; `deploy-step0.sh:783`; `deploy-card.sh:264`), and the tests' lines on the working tree for the files not modified. Nothing was run but reads; no test was executed (every RED is UNPROVEN until the builder quotes it).
- `ls -l /Users/cobalt/.claude/ops/desk-launch.sh /Users/cobalt/.claude/ops/preflight.sh`: both symlinks to `/Users/cobalt/cobalt/ops/desk/<name>`.
- The tracked install source is `ops/desk/desk-launch.sh` (`git -C /Users/cobalt/cobalt ls-files ops/desk` lists it); the build edits it and `ops/desk/preflight.sh`; `install-ops` links by name and keeps an existing link.
