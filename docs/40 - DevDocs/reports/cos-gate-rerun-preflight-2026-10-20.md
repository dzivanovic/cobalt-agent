# Cos gate-run prompt 873 (amended for the deployed probe) — preflight

§0: Prompt 873 is clean on all 10 checks. Nothing blocks the launch.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git show main:src/cobalt/cos/cli.py`; `sed -n 785,844p ops/desk/desk-launch.sh` | `PROBE_ITEMS = ("X2","X10","X11","X12","X3","X14","X17")`, positional `item` with those `choices`, no other flag. The prompt spells `uv run cobalt cos probe` for exactly X11 X12 X3 X2 X10 X14 X17, each with its own `--allowedTools` string, plus the one pytest string, `claude auth status` and `claude -p --model claude-sonnet-5-5 '…'`, each spelled twice, byte for byte. No `COBALT_ENV=`, `launchctl`, `-c`, `python -c` or script in the allow list. `uv run` and `Bash(git -C … status*)` pass the launcher's write-string scan only because RULINGS is a ruled row (check 2); `Bash(git *)` does not occur. | OK |
| 2 | `grep -rn "^| R1863 " reports/`; `git log -S"\| R1863 \|"` on `cto-2026-10-18.md` | `cto-2026-10-18.md:90`, one row: `HIS RULING · APPROVED (brain, L79)…`. Committed (`11563e82`); the file has an empty diff against HEAD. The prompt has one `RULINGS: 2026-10-18 R1863` line. | OK |
| 3 | prompt line 1 | `--permission-mode auto` | OK |
| 4 | prompt `## REPORT` block | 14 `GATE RESULT: com.cobalt.cos · <item> ·` lines in order D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20, each once. Path `reports/cos-gate-run-2026-10-20.md` in WRITE, REPORT and the heading. | OK |
| 5 | prompt RULES, steps 1–9, `## DECISIONS` | Rules say only exactly `OK` counts and cite `deploy-step-c.sh:185-186`. Each non-OK has its default: FAIL or NOT RUN → cos stays unloaded; `OK (…)` → the line does not count; X14 → shipped values stand. I confirmed `deploy-step-c.sh:185` is the `index($0, p) == 1 && length($0) > length(p)` test. | OK |
| 6 | prompt RULES, steps 6, 8, 9 | "Run each probe once… No retry." X14 and X17 run in the background, never in parallel, read once. No loop. | OK |
| 7 | `git grep` / `git ls-tree` on main | `probe.py`: `_live_scratch:308`, `_x11:340`, `_x12:354`, `_x3:375`, `_x14:413`, `_x17:422`, `ITEMS:430-433`, `_verdict:437` all match. `test_hitl_offline.py:146` is `test_x20_redact_keeps_the_card_fragment_key`. `F20-FINAL` (192 lines): `## First-gate experiments` at :72, D14 at :119. `deploy-step-c.sh:185-186`, `drc-d2-check-2026-09-25.md:44` (the `claude -p … OK` row), `877` row P1 and `cos-probe-fr1-check` `## OPEN` (:189) all exist. Cards 808 (35 lines), 730, and the three drafter reports, the 10-19 gate report and `writing-rules.md` exist. `bootstrap-owed.json` exists on disk (gitignored). | OK |
| 8 | prompt WRITE line | "WRITE only `…/cos-gate-run-2026-10-20.md`, with the Write tool." The probe's temp dir, pytest `tmp_path` and "delete nothing" are stated. | OK |
| 9 | prompt `## REPORT` | Last line `GATES DONE · ok: <n> · fail: <n> · not run: <n>` or `FAILED: <reason>`, with the counting rule. | OK |
| 10 | `git diff HEAD --stat -- …/873-cos-gate-run.md` | empty; last commit `bef79b02` | OK |

## ISSUES

- NOTE: Step 7 (X18) depends on `deploy-*.md` reports since 2026-10-15 stating both bootout and ready times. If none do, the line is `NOT RUN` by design. That is a result, not a block.
- NOTE: X3 is the item with a known gap. The check report's G3 says the killed turn starts `pgrep` (`session.py:146`), which the probe's own rig refused in a test. The check REJECTED it as inside the fence. A live X3 FAIL is therefore possible; the prompt's default handles it (cos stays unloaded).
- NOTE: Cost is real. X14 runs 20 sessions and X17 runs 40, on his subscription.

PREFLIGHT DONE · prompt: 873 · checks: 10 · fails: 0 · ready: YES
