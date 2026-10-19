# Draft amend 3 — gemini-read-grant-1019 (prompt 836)

## §0 Headline
- Card 827 amended in place. `x1-transcript.sh`, its test file and P1's script calls are gone. No new script, allow string or `--add-dir`.
- T1 is now kind `x1-copy <worktree> <leg>` in `desk-launch.sh`, placed after `grant-sweep`. The gate seat runs it under its existing `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`. It copies only when the log holds exactly one `workspaceDirs=` line and every word in it is `<WT>/<worktree>`; anything else and the leg FAILS with nothing written.
- New tests in `test_desk_launch_shadow.py` (the `Desk` form; `sweep`'s shape): a foreign workspace, a copy where `grep -c -F X1_CANARY` prints `1`, a missing transcript, and zero or two workspace lines. The `x1-<leg>.log` soft-denying decision still applies and is kept.
- Preflight NOTES folded in: H3's bare `|`, and verdict (7) now counts whole lines only. The FOR THE CHECK line is added verbatim. BASE `0c79bbae` → `23130eb3` (main moved by docs only).

## DECISIONS
1. ASK DESK: a real leg run from the worktree lists the worktree twice: `workspaceDirs=[<wt> <wt>]`, the cwd plus the `--add-dir` (717 leg 0a log). A strict one-path test would refuse every real leg. Default taken: one `workspaceDirs=` line, at least one word, and every word equal to `<WT>/<worktree>` (`[ = ]`, `set -f`). Both shapes are tested. [2026-10-19 08:54 EDT]
2. ASK DESK: `desk-launch.sh` exits once the seat starts, so it cannot see a leg end. Default taken: a new kind that the gate seat calls after each leg, beside the grant code. It is not a new script and needs no new allow string. Any gate seat could already run `desk-launch.sh` under that allow; CHECK ASK X4 asks whether that matters. [2026-10-19 08:54 EDT]
3. ASK DESK: the desk-size guard (`:530`) runs for every kind but `desk`. On a large desk it would refuse the copy and fail a leg for no X1 reason. Default taken: `x1-copy` is exempt like `desk`, because it launches nothing. [2026-10-19 08:54 EDT]
4. ASK DESK: if the guard lets leg 0f's agy through, that agy runs with cwd x1-canary, so `x1-copy` refuses it as a foreign workspace. Default taken: verdict (1) records that refusal, does not raise a second STOP, and quotes the leg whole. [2026-10-19 08:54 EDT]
5. ASK DESK: the copy STOP now covers more than a missing file. Default taken: the text reads `transcript not copied (INCOMPLETE)`, and the H2 test strings follow it. [2026-10-19 08:54 EDT]
6. ASK DESK: R2015 is a DESK RECORD. `authorize.sh:115` proves each RULINGS row by `HIS RULING` and `APPROVED`. Default taken: R2015 is cited in `## RECORDS`, and RULINGS stays R1863 and R1942. [2026-10-19 08:54 EDT]

## RECORDS
- `date` 08:49 at start, 08:54 at the report.
- Read: prompt 836; `areas/cobalt.md` (What Cobalt is, Build rules); `writing-rules.md`; card 827 (clean against HEAD); the preflight `gemini-xsplit-preflight-2026-10-19.md`; my amend-2 report; `cto-2026-10-19.md:16` R2015 and `:19` R2012.
- `rev-parse main` → `23130eb3`. `git diff --stat 0c79bbae main` and `git diff --stat main` on `ops/desk`, `tests/ops`, `SHADOW-HUB.md`, `CHECK-HUB.md` → empty, so the tree equals `git show main:` on those paths. The guard refuses `git show … | sed`, so citations were read from the tree after that proof.
- Read from the tree: `desk-launch.sh` `:205-244`, `:380-409`, `:515-554`, `:1085-1180`, `:2560-2695` (2,695 lines); `bare-guard.py` `:1085-1219`, plus grep hits `:87`, `:128`; `authorize.sh:115`; `test_desk_launch_shadow.py` `:1-185`, `:476-500` (690 lines).
- agy, read with `ls -la`, `grep -c -F` and `grep -o` (paths only): `cli.log -> log/cli-20261019_080949.log`; `cli-20261019_080830.log` has 1 `workspaceDirs=` line, which lists the 717 worktree twice. Neither the settings file nor any decoy or transcript was read.
- Card `wc -c` 32,666 → 39,521 (+6,855). The growth is the T1 workspace test and its tests, the RECORDS lines (workspace proof, R2015, preflight, AMEND 836) and the FOR THE CHECK line.
- Only card 827 and this report were written. Nothing committed or launched.

DRAFTED · decisions: 6
