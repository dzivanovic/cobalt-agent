# launcher-f5 deploy card draft — 2026-10-05

## §0 Headline
- Two files written: the F5 fix-report pointer record and the deploy card `57-deploy-launcher-f5-card.md` (one row, seven columns).
- Code tip `8d79d7c9`, head `fb2d95a2` (report-only above the tip: proved empty), check tip `a545a4d8` an ancestor (proved).
- Ship = 3 files: `desk-launch.sh`, `test_desk_launch_prechecks.py` (F5's) and the builder's report (not F5's, docs).
- BRANCH, WORKTREE, TAG and REPORT are all absent today. 0 decisions.

## CARD
- JOB `deploy-launcher-f5-1005` · BRANCH `deploy/deploy-launcher-f5-1005` · WORKTREE `deploy-launcher-f5-1005` · BASE `main` · TIP `fb2d95a2`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-launcher-f5-1005.md` · RULINGS `2026-10-05 R412` · TAG `deploy-2026-10-05-launcher-f5` · MIGRATIONS none · SET workflow2
- fix report: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-f5-fixround-2026-10-05.md` (its last line is the branch report's stop line, `tip: 8d79d7c9`).

## DECISIONS
None.

## RECORDS
- Markers (before on main / after at `8d79d7c9`): `ruling_items() {` 0/1; `tool_list() {` 0/1; the F5 comment string 0/1 (`desk-launch.sh`); `def test_f5_the_survey_prompt_launches_on_its_rulings_row` 0/1 (the test file). The after counts came from the `git show` output grepped from its saved copy, because a pipe is blocked.
- The fix report file is new and uncommitted: the desk commits it on main before the launch (the launcher requires it committed and unmodified).
- The card's `diff --stat main...ops/launcher-fixround-1005` shows 3 files; the report there is the builder's, extended by its F5 section.
- The builder's DECISIONS item 1 is carried as a record. The builder's stop line says `decisions: 2`; the report's DECISIONS list also keeps closed items 2-3.
- No `«FILL` token: both new files are free of it by construction. No other file edited. No commit made.

LAUNCHER-F5 DEPLOY CARD DRAFTED · decisions: 0
