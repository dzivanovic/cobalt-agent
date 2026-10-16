## §0 Headline
- Card 641 amended (card only) per R1712, option A: the `job` fixture card gains `HOUSE A: grok`, the one named existing-test edit.
- Fixture line proved at `tests/ops/test_stage_set.py:75-79` (`:78`) on `85eade55`; branch `tests/` equal to it.
- FIX ROUND ORDER restated: only the FR-1 test is red before the `clearable()` edit; existing clear tests quoted GREEN before and after.
- Guard placed in ORDER, FR-1 row and X5. `BASE` untouched. Nothing run but reads.

## DECISIONS
- ASK DESK: FR-1 control (ii) `test_fr1_control_this_jobs_own_check_folder_shape` expects a CLEAR (exit 0) for the this-JOB folder, which the tip refuses (two or more `*-card.md`), so it is red on the tip, not GREEN as the card says "controls GREEN on the tip and after". Default: left as written (ruling scope); the builder reports the real red in the tip run. [14:10]
- ASK DESK: the ORDER's total test count is not stated (none on the card); the builder quotes the run's own numbers. Default: no count added. [14:10]

## RECORDS
- Edited only `prompts/2026-10-16/641-check-scratch-card.md`: new FIXTURE LINE paragraph in `## CONTINUE FIX ROUND`; FR-1 row (test cell wording, guard, files cell); FIX ROUND ORDER; X5.
- Proof: `git show 85eade55:tests/ops/test_stage_set.py` read whole; line numbers by `grep` on the branch worktree (`job` `:52`, card write `:75-78`, `prior_staging` `:193`, `snapshot` `:225`); `git diff --stat 85eade55 ops/check-scratch-1016 -- tests` printed nothing.
- Ruling read: `reports/cto-2026-10-16.md` R1712.

DRAFTED · decisions: 2
