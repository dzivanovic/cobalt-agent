# Draft — CLEANUP card (C1, R1138) — 2026-10-12

## §0 Headline
- Card `prompts/2026-10-12/389-cleanup-class-card.md` drafted, uncommitted: C1 `scratch-clean.sh` with red-first tests, H1 the BUILD-HUB NO CLUTTER line, R1 RESTARTS. `CLASS: K1, K5`, `INSTALL: none`, `BASE` left for the desk.
- No allow string is added. CLASS (a) on the three seat lines already covers the script and `job-clean.sh salvage`. A named string there turns `test_hub_lines.py:82` red (R39), and the desk line's `check_paths` refuses it.
- The desk runs the script as `sh /Users/cobalt/.claude/ops/scratch-clean.sh "<path>"` on committed settings rule `HEAD:.claude/settings.json:29`, once `desk-launch.sh install-ops` links it after the deploy.

## DECISIONS
- ASK DESK: the prompt asks for `Bash(sh /Users/cobalt/cobalt/ops/desk/scratch-clean.sh *)` on BUILD-, CHECK- and SHADOW-HUB lines. CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` already covers it (`STANDING-LIST.md:36`), and `tests/ops/test_hub_lines.py:82` (his 2026-10-02 R39) refuses any other `Bash(sh …)` string on the BUILD and CHECK lines. Default: no string added; the card's rows change no line. [06:18 EDT]
- ASK DESK: the desk line (`CTO-DESK-WAKEUP.md:13`) has no `/Users/cobalt/cobalt` `--add-dir`, so `desk-launch.sh desk` refuses the string (`check_paths`, `:198-218`, `:519`). Default: no change to the desk line; the desk uses the installed spelling on `HEAD:.claude/settings.json:29`, so `INSTALL: none`. The desk runs `sh /Users/cobalt/.claude/ops/desk-launch.sh install-ops` after the deploy. [06:18 EDT]
- ASK DESK: the script accepts any registered worktree under `cobalt-wt`, not only the seat's own card WORKTREE (the script cannot know the seat). Default: as the prompt says; a per-seat fence is a later K5 guard card (`## NOT IN THIS JOB`). [06:18 EDT]
- ASK DESK: `agy-trial` is a registered worktree, the check hubs' shared house tree. Default: refused, as `job-clean.sh:45` refuses it. [06:18 EDT]
- ASK DESK: `/tmp/<job>-run/` is named in the hub line as a staging place, but it is not a root of the script (the prompt names two roots). Default: not a root. [06:18 EDT]
- ASK DESK: under `$CLAUDE_JOB_DIR/tmp`, git cannot prove "untracked". Default: `CLAUDE_JOB_DIR` must be exactly `$COBALT_JOBS_ROOT/<one plain name>`, and a path inside any git work tree is refused. [06:18 EDT]
- ASK DESK: the hub text's `\"<path>\"` is read as plain `"<path>"` (the prompt's own quote escapes). Default: plain quotes in the line. [06:18 EDT]
- ASK DESK: `HOUSE B` is left empty (CARD.md: build column empty; the prompt gives no value). Default: the desk fills it before the check. [06:18 EDT]

## RECORDS
- `main` HEAD `6468fb5e` (`git rev-parse --short=8 HEAD`, 06:15 ET).
- Read: `prompts/CARD.md`; LAWS L33 (`:222`), L62 (`:320`), L63 (`:326`), L76 (`:385`), L81 (`:403`); `reports/brain-direction-2026-10-02.md:214-229`; `reports/hands-off-answer-2026-10-12.md`; `reports/cto-2026-10-12.md:13` (R1138, HIS RULING · APPROVED); precedent `prompts/2026-10-11/386-launcher-shadow-check-card.md`.
- `ops/desk/job-clean.sh` whole (salvage `:12-26`, `:51-173`, `:175-177`; `agy-trial` `:45`).
- `ops/desk/bare-guard.py`: header `:1-46`, `is_env` `:836-843`, `bash_rules` `:1060-1103`, `shell_c` `:1125-1136`. A `sh <script> "<path>"` call passes G1, G4, G7; G3 denies a `.env` path.
- Launch lines (`grep -n "^claude --bg "`): `BUILD-HUB.md:12`, `CHECK-HUB.md:10`, `SHADOW-HUB.md:10`, each with `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`; desk `CTO-DESK-WAKEUP.md:13`, allow = 12 git strings, `--add-dir` Vault and cobalt-wt.
- `ops/desk/desk-launch.sh`: kinds read their fixed file `:884-888`, line fill `:1608-1622`, desk kind `:502-521`, `check_paths` `:198-218`, install-ops `:82-92`.
- `.claude/settings.json`: `HEAD:` holds `Bash(sh /Users/cobalt/.claude/ops/*)` at `:29`. The working tree's uncommitted lines (his: `job-clean.sh`, `gate-clean.sh` and five more repo-spelled scripts) were read and not touched.
- `ls -la /Users/cobalt/.claude/ops/`: one link per `ops/desk/` script, `job-clean.sh` among them; `scratch-clean.sh` is absent from `ops/desk/` and from `tests/ops/` (`ls`).
- `tests/ops/test_hub_lines.py:32` (CLASS_A), `:54` `hub_line`, `:77-84`; `tests/ops/test_gate_clean.py` fixture `:23-115`, `:676`; `tests/cobalt/test_placement.py` exists.
- `src/cobalt/jobs/restarts.py:225-246` (DOCS, operator script, tests).
- `git worktree list --porcelain`: `agy-trial` registered on `ops/agy-trial-0915`; no `scratch-clean-1012` worktree yet.
- The 386 `docs/_inflight` now holds `README.md` only (`ls -la`).

DRAFTED · decisions: 8
