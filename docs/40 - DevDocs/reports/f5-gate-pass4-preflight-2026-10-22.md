# F5 gate-run prompt 970 — FOURTH PASS preflight (2026-10-22)

Read-only. Subject: `prompts/2026-10-21/970-f5-gate-run.md` as committed (HEAD), against `HEAD~1`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read the file; `git diff HEAD~1 HEAD` of it | LAUNCH MODE line: "Run ONLY `## FOURTH PASS`; run no step of `## STEPS`, and write no other section." It names no pass 1–3 section. Missing pass-1 report → `FAILED: no pass-1 report`. | OK |
| 2 | compare each command string in `## FOURTH PASS` with the MODEL line's `--allowedTools` | Strings used: `ls -d …`, `ls -la …/*/.env`, `ls "<note>"`, `date`, `sh /Users/cobalt/cobalt/ops/desk/*` (take, release), `COBALT_ENV=dev uv run cobalt db *` (proof-only, migrate, rollback), the X6 and X4 probe strings (X6 is byte-identical to the MODEL line). All are on the line. No `rm`, no production command, no `.env` read (`ls` only). The section says "Every string used is on the MODEL line already". | OK |
| 3 | `ls` and `git grep` against `main` | Present: `ops/desk/take-devdb-lock.sh` (exit 4 after the wait, args `<worktree> <minutes>`), `ops/desk/release-devdb-lock.sh` (exit 3 on a failed remove), `checkpoint_probe.py` (`_x4`, `_x6`, `ITEMS`, `KEEP_ROOT`, `X4_GROUPS_FIXTURE`, `X4_GROUPS_KEPT`), `configs/dev/vault.yaml:23` (`~/dev-vault-cobalt`), `configs/dev/aset.yaml:23-24` (daily notes dir), `configs/cobalt/templates/daily.md.j2`, `src/cobalt/db_migrations/__init__.py`, `/Users/cobalt/cobalt-wt/f5-probe`, `.f5-probe/PLACEHOLDER`. `ops/desk/gate-lists.md:56` `## LEVEL 0013` is there. The row (b) fixture is absent from `main`, only `groups_sector_v140.csv`, as the prompt says. | OK |
| 4 | compare pass 4 steps 1–5, 8, 9 with pass 3 steps 1–5, 7, 8 | Same discipline: lock-held check, take (90 min, `.env` `ls -la`), note absent first, proof-only vs 0013, migrate up through 0029, X6, rollback `--down-to 0013` plus proof, release. Same failure handling. X4 (step 7) touches no database (`checkpoint_probe.py` docstring (c), `_x4` calls no store, `check_demand` or fetch). It holds no lock and runs in every path. | OK |
| 5 | step order; `_x4_figures` | X4 is step 7, after X6 (step 6). With neither Groups file present the probe prints `NOT RUN — no real Groups body …`, which is the NOT RUN case the prompt describes. Kept capture does not exist now (`.f5-probe/` holds only `PLACEHOLDER`), so X6 can write it. | OK |
| 6 | grep dates in `## FOURTH PASS` | The note path, `#### 2026-10-22 T 05:15` and the brain date are all 2026-10-22. `2026-10-21.md` appears only as "owed to the desk … neither read nor touched" (steps 3 and 10). `ls` shows `2026-10-22.md` absent and `2026-10-21.md` present. | OK |
| 7 | read step 11 | Edits the 8 X6/X4 lines, FIGURES, DECISIONS, RECORDS and the last line in place. The last line is `GATES DONE · ok: <n> · fail: <n> · not run: <n>`, or `FAILED: pass 4 …` on a rollback or release failure. | OK |
| 8 | `git diff HEAD~1 HEAD` of the file | Two hunks only: the LAUNCH MODE line (line 6) and the appended `## FOURTH PASS` (+19, −1). Nothing else differs. | OK |
| 9 | `ls -d /Users/cobalt/cobalt-wt/.cobalt_dev.lock` | "No such file": the `cobalt_dev` lock is free now. Pass 4 step 1 would proceed. | OK |

## ISSUES

- NOTE: step 7 says X4 runs "after the rollback of step 8" in one path. Step 7 comes before step 8, so that phrase is inaccurate. Harmless: the order is 6, 7, 8 and X4 needs no lock.
- NOTE: the LAUNCH MODE line says "run no step of `## STEPS`", but pass 4 step 6 runs "step 1b's command" and step 7 judges "by step 4 of `## STEPS`". Pass 3 had the same wording and ran. It reads as the command and rule reused by reference, not as a step to run.
- NOTE: the MODEL line's SESSION text still says "no database command". The pass overrides it for these steps, as pass 3 did. The `uv run cobalt db *` string is on the line.
- NOTE: pass 3 X6 ended `NOT RUN — finviz-screener degraded` (no Finviz token in the probe's cwd). 989 (`_at_repo`) is deployed per the prompt and the code on `main` has it. A real X6 token path is not provable offline, so this is the one live risk and not a launch block.
- NOTE: `2026-10-21.md` is still in the dev vault, owed to the desk, and pass 4 leaves it alone as written.

Blocks the launch: nothing.

PREFLIGHT DONE · prompt: 970 pass 4 · checks: 9 · fails: 0 · ready: YES
