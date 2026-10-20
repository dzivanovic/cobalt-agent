# draft-cos-gate-rerun — 2026-10-20

## §0 Headline
- AMENDED `prompts/2026-10-19/873-cos-gate-run.md` in place so it re-runs all 14 items on the deployed probe. The report is now `cos-gate-run-2026-10-20.md`.
- X2, X10, X11, X12, X3, X14 and X17 now run as `uv run cobalt cos probe <item>`, each with its own allow string; a plain `OK` counts. X20 now runs the shipped test `test_x20_redact_keeps_the_card_fragment_key`.
- Still not probes: D14, `agent stopped` and X15 (his), X1/X13 (CLI from the shell), X18 (deploy logs). The rules, item list and his question are unchanged. Model line unchanged: the probe gives no reason to change it.
- Live cost: 68 real sessions (X14 20, X17 40). X14 and X17 run once each, in the background, last. No flag or env the launcher refuses. 873 is 11155 → 11189 bytes (+34, the tag, drafter and probe cites). Committed nothing.

## DECISIONS
1. ASK DESK: this is the probe's first live run. Every item first runs `claude auth status` under a scratch `HOME` (`probe.py:130-134`, `:452-453`), with neither `~/.claude.json` nor `~/.claude/` there. If the CLI cannot find his login there, every probe line is `FAIL auth: claude auth status exit <n> under the scratch HOME` and spawns nothing, so the cost is near zero. Fixing that would need a credential in the env, which L41 bars, or a probe change (a build card). Default: run as written; a FAIL `auth:` goes to the brain with the bootstrap still blocked. [12:25]
2. ASK DESK: X13 will FAIL again exactly as on 10-19 (`cos-gate-run-2026-10-19.md:10`). `.claude/settings.local.json:24` still holds the deny rule `Bash(git push*:*)`, and the CLI prints its warning before `OK`. The rule is kept as you asked. Default: X13 FAILs again; a separate edit of `settings.local.json` to `Bash(git push*)` (his file, not this seat's) clears it before the run. [12:25]
3. ASK DESK: X17 passes on `sonnet >= opus` (`probe.py:427`), so 0/20 against 0/20 prints OK (check O4, carried open). The prompt writes that case as `OK (0 of 20 on both: nothing compared)`, which does not count. Default: as drafted. [12:25]
4. ASK DESK: check G4 (`cos-probe-fr1-check-2026-10-20.md:192`) said the gate's first live X2 would list what the CLI writes under the scratch HOME. The probe prints one line and deletes its scratch dir (`probe.py:176`), so the seat cannot list it without a script. Default: G4 stays open, for a probe follow-up card. [12:25]
5. ASK DESK: X12 and X3 move from the named fake-SDK tests (10-19: `OK (…)`, did not count) to the real-spawn probe, so a pass is now a plain `OK`. The dry run and options test were evidence only, and are dropped. Default: as drafted. [12:25]

## RECORDS
- `date` 12:22 start, 12:24 edit, 12:25 report. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `8c075815`; `git log --oneline -12 main` then showed `a200a36f` on top, docs only. `merge-base --is-ancestor 7e7bee6b main` → exit 0.
- `git diff --stat main --` 873, `src/cobalt/cos`, `test_cos_probe.py`, `test_hitl_offline.py`, `test_cos_offline.py` and `F20-FINAL-2026-10-11.md` → nothing, so the on-disk lines are main's.
- `git show main:` `src/cobalt/cos/probe.py` (read whole; `git grep -n` → `:130` `_auth_exit`, `:134` the auth argv, `:167` `_scratch`, `:176` its `rmtree`, `:452-453` the auth exit check, `:308` `_live_scratch`, `:333` the never-ran guard, `:340` `_x11`, `:354` `_x12`, `:375` `_x3`, `:413` `_x14`, `:419` its OK rule, `:422` `_x17`, `:427` its OK rule, `:430-431` `ITEMS`, `:437` `_verdict`). `src/cobalt/cos/cli.py:14` `PROBE_ITEMS = ("X2", "X10", "X11", "X12", "X3", "X14", "X17")`, `:39` `choices=PROBE_ITEMS`. `tests/cobalt/test_hitl_offline.py:146` the X20 test. `configs/cobalt/agents/cos.yaml` model `claude-sonnet-5-5`. `tunables.yaml:989-990` `cos.max_turns` 30, `:998-999` `cos.turn_timeout_s` 900. `F20-FINAL-2026-10-11.md:72-92` (X20 `:82`, X11 `:84`, X12 `:85`, X3/X14 `:86`, X17 `:87`, X1/X13 `:88`, X2/X10 `:91`, X18 `:92`).
- Read: prompt 915; 873 whole (before); `reports/draft-cos-gate-amend-2026-10-19.md`; `cos-probe-fr1-build-2026-10-20.md`; `cos-probe-fr1-check-2026-10-20.md`; card 877; `deploy-cos-probe-fr1.md` (Grep: `:4` DEPLOYED `7e7bee6b`); `cto-2026-10-20.md` (Grep: R2173, day plan goal 4); `cos-gate-run-2026-10-19.md` (Grep: the 14 results, X13 `:10`); `topics/writing-rules.md`.
- Launcher: `desk-launch.sh:785-844`. A `uv run` string passes on a prompt line when its one RULINGS line cites HIS RULING + APPROVED rows; R1863 is one (`cto-2026-10-18.md:90`). There is no `launchctl` or `COBALT_ENV` string. `ops/desk/bare-guard.py` Grep `uv run|cos probe` → only `:116-117`, `:997` (production lines).
- Grep `git push\*:\*` in `.claude/` → `settings.local.json:24`.
- `wc -c` 873: 11155 before, 11189 after. Edited only 873 (Write, after a whole Read) and wrote this report.

DRAFTED · decisions: 5
