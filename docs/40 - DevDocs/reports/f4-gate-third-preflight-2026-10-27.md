# F4 gate third pass: preflight of 1078 (2026-10-27 00:36 ET)

Main tip read: `f1f92dc7`. Subject: `prompts/2026-10-27/1078-f4-gate-third.md`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | Read 1078 line 1 | tags MODEL · SEAT · launch line (one bare `sh desk-launch.sh prompt`) · SESSION in order; then CLASS, LADDER, RULINGS. No separate mode or METER tag; the precedent 1045 has none either | OK (NOTE 1) |
| 1b | `grep -c -E "«FIL[L]\|TODO\|XXX"` on 1078 | `0` (the `<step 1>`, `<time>`, `<n>` tokens are report-template slots the seat fills, not unfilled placeholders) | OK |
| 2a | Read 1078 step 1 and the launch line | the string is `COBALT_ENV=dev uv run prefill probe X15`, byte-identical on the allow line `Bash(COBALT_ENV=dev uv run prefill probe X15)` | OK |
| 2b | Read 1078 step 1 against `refresh_probe.py:381-383` | OK only for peak ≤ 50 and 429 0; an `OK` line with peak above 50 or 429 not 0 is written FAIL; `NOT RUN` or no PROBE line is written NOT RUN; rule line 18 says only exactly `OK` counts | OK |
| 3a | `sed -n 180,190p ops/desk/deploy-step-c.sh` | `:185` comment and `:186` awk: `GATE RESULT: <label> · <item> · ` at column 0 with a non-empty result after it; 1078 cites `:185-186` | OK |
| 3b | Read 1078 `## RESULTS` | 3 column-0 lines in the `GATE RESULT: com.cobalt.prefill-refresh · <item> · <result>` shape; X7 and X9 are `NOT RUN — [HIS HAND] …`, X15 is the step 1 result | OK |
| 3c | Read 1078 last line against `refresh_probe.py:372-375,463` | probe prints `PROBE X15 <verdict> peak <n>/min at <m> · … · 429 <n> …`; the stop line `GATE THIRD DONE · X15: … · peak <n>/min · 429: <n> · main <8hex>` takes both numbers from it, `-` when none | OK |
| 4a | Read the 1078 allow line against its steps | step 0 `date`, `git -C … rev-parse*`, `ls -d …` match `date*`, `git -C /Users/cobalt/cobalt rev-parse*`, `ls *`; step 1 matches the exact probe entry; the report goes through `Write` | OK |
| 4b | Read the 1078 allow line and `--disallowedTools` | no `Edit`, no git write beyond `rev-parse`, `git push*` disallowed, no `launchctl`, no database or production command; the probe is in process, mock transport (`refresh_probe.py:13-17,29-30`); 1078 line 14 forbids `prefill refresh` | OK |
| 4c | `ls /Users/cobalt/.claude/ops/desk-launch.sh` | present; the launch line is the standing one-bare-command shape | OK |
| 5a | `grep -n "X15" F4-FINAL-2026-10-10.md` | `:221` is the X15 row (strike loop and refresh in one minute) | OK |
| 5b | `grep -n "X7\|X9" F4-FINAL…` | X7 `:213`, X9 `:215` | OK |
| 5c | `grep -n "LAUNCHD" 778-deploy-f4-refresh-card.md` | `## LAUNCHD` is at `:20`; 1078 cites `:21` | OK (NOTE 2) |
| 5d | `grep -n "^\| R2535 \|^\| R2542 "` | R2535 at `cto-2026-10-26.md:98` (matches the `:98` cited); R2542 at `cto-2026-10-27.md:20` | OK |
| 5e | `git rev-parse --short=8` on `0ea89b17`, `deploy-2026-10-26-f4-strike-reserve`, `7e682889` | `0ea89b17`, `0ea89b17`, `7e682889`: tag and sha agree; the f4-probe sha exists | OK |
| 5f | `grep -n` on `reports/deploy-f4-strike-reserve.md` | `:166` tag set at `0ea89b17`; `:222` `DEPLOYED deploy-2026-10-26-f4-strike-reserve 0ea89b17` | OK |
| 5g | `ls` of `refresh_probe.py`, `deploy-f4-strike-reserve.md`, `draft-f4-gate-third-2026-10-27.md`, `f4-gate-run-2026-10-26.md`, `writing-rules.md` | all present | OK |
| 5h | `grep -n "X10 ·" f4-gate-run-2026-10-26.md` | `:7` is `X10 · OK — the attempt2 deploy gate, …:263`; 1078's RECORDS line ("X10 OK from the attempt2 deploy gate") is true | OK |
| 5i | `grep -n "PROBE\|peak\|429" refresh_probe.py` | the output shape and `PROBE_ITEMS = ("X15",)` (`:52`) are as 1078 states; `cli.py:96-107` registers `probe X15` | OK |
| 6a | Read 1078 line 1 | `MODEL: Opus 5.5 (claude-opus-5-5)` and `--model claude-opus-5-5` | OK |
| 6b | `sed -n 705,718p configs/cobalt/taxonomy/tunables.yaml` | `radar.finviz_rpm` value 37, ruled 2026-10-26 (R2512: C) | OK |
| 6c | Read `refresh_probe.py:23-25,411` | the probe's radar bucket is `radar_bucket_rpm()`, the tunable (37), not a hard-coded 50: it reads the deployed 1049-C cap | OK |
| 6d | `ls -d /Users/cobalt/cobalt-wt/.cobalt_dev.lock` | `No such file or directory`: no build holds `cobalt_dev` now, so step 1 would run | OK |

## ISSUES

- NOTE 1: line 1 has no separate mode or METER tag. The precedent 1045 passed without one, so I did not block on it.
- NOTE 2: `## LAUNCHD` is at `:20` of the 778 card, not `:21`; the same cite is in the precedent. It names a section a reader finds in one line.
- NOTE 3: RECORDS asks for the probe's exit status. `echo $?` is not on the allow line. The seat can take it from the Bash result (`Exit code 1` on FAIL, none on 0); it must not add a command.
- NOTE 4: the 37 cap is the working tree of `/Users/cobalt/cobalt`, whose changes are docs and `.claude` only, so it equals main. Nothing in the allow line proves the probe seat runs on that tree; `cd /Users/cobalt/cobalt` is in the launch line, which is enough.
- Blocks the launch: nothing.

PREFLIGHT DONE · cards: 1078 · checks: 24 · fails: 0 · ready: YES
