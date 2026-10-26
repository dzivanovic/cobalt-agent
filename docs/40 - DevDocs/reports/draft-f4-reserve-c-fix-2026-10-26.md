# draft-f4-reserve-c-fix · card 1049-C · fix round for preflight fail #8

## §0 Headline
- R5(a) and R5(b) are now pytest proofs on the BUILD line: `COBALT_ENV=dev uv run pytest -q -rP <test>`. Each is preceded by the `.env` `ls`. R5(c) is unchanged.
- New R1 test `test_radar_check_prints_radar_finviz_rpm_37` calls `cobalt.radar.config.command`. R3's X15 test now has `print(line)`, so `-rP` shows the `PROBE X15 OK` line.
- The X15 load gate on the deployed code belongs to the F4 gate seat's THIRD PASS of `1045-f4-gate-run.md`, not the builder. This is stated in the WHY, in a NOT-IN-THIS-JOB line and in R5(b).
- R6 now states both strike paths for an unreadable cap: `read_plan` and `check_strike_demand`. Both fail safe: no fetch, and the interval never gets shorter. Each path has its own new test. `tick` is unchanged.
- Every command for the builder is on the BUILD line. The DEPLOY PROOF rows are unchanged and match `deploy-smoke.sh`. The card grew from 24365 to 28802 bytes (`wc -c`) because of the new proofs and the R6 path text.

## DECISIONS
- ASK DESK: `1045-f4-gate-run.md` has no THIRD PASS section (`grep -c "THIRD PASS"` → `0`), but the card now names it as the X15 load gate. Default: the desk adds that pass, running `COBALT_ENV=dev uv run prefill probe X15` on the deployed code, before the F4 deploy. This card does not edit 1045. [18:12]

## RECORDS
- 18:12 EDT (`date`). Edited `prompts/2026-10-26/1049-f4-strike-reserve-card.md` in place. Header unchanged. Changed: WHY, R1 (one new test, the R1(d) dry-run text), R6 (import, both SourceFailure paths, two new tests, RED), R3 (`print(line)`), R5 (a)/(b), NOT IN THIS JOB (one line), CHECK ASKS X6, `## RECORDS` (the brain line, word for word, and the fix-drafter read list).
- Every new `file:line` was proven with `git show main:<path>` or `git grep -n … main`. The list of reads is under the card's `## RECORDS`. `git diff --stat e015c97b main -- src tests configs "docs/30 - Design"` was empty, so the card's earlier cites still hold.
- BUILD-line check (`grep -n -o -E` over the card's backticked commands): the builder's commands are `ls -la …/.env`, `COBALT_ENV=dev uv run pytest …` ×2, `uv run cobalt jobs restarts <BASE>..HEAD`, `uv run pytest -q -p no:cacheprovider …`, and the `grep -c -F`/`ls` smoke reads. All are on `BUILD-HUB.md:14`. `uv run cobalt radar check` and `uv run prefill probe X15` appear only as the CLI being described, the gate seat's command and the fence.
- Nothing run beyond reads, `wc` and `date`. No git write.
DRAFTED · decisions: 1
