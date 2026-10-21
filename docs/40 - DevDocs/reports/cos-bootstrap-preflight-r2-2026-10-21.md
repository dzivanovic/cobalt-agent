# Card 929 (deploy-cos-bootstrap) — preflight round 2 (read-only)

Card: `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md`, clean in git (`git status --short` empty), HEAD `971dd96f`. Nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---------|--------|---------|
| 1 | `grep -c "«FILL" <card>` | `0` | OK |
| 2 | `git diff a4c0a3e2 HEAD -- <card>` (r1 preflight HEAD to now) | one hunk only: line 29 `GATE RESULT: X15 · DEFERRED …` → `GATE RESULT: com.cobalt.cos · X15 · DEFERRED …`; deferral text unchanged | OK |
| 3 | TAG `deploy-2026-10-21-cos-bootstrap` (unchanged since r1) | form `deploy-<date>-<job>`, plain name | OK |
| 4 | `ls ops/desk/retired-labels`; `grep -c ""` | listed; 1 line (`com.cobalt.agent`, per r1) | OK |
| 5 | WAITS cutover-tooling / tunables DEPLOYED | unchanged since r1 (`23e72289`, `1d6f649e` ancestors, reports present); card diff touches no WAITS | OK |
| 6 | WAITS agent retired | `retired-labels` holds it (check 4) | OK |
| 7 | WAITS `hitl.page_base_url` set | `tunables.yaml:1038-1039` `value: "https://cobalt.taild24291.ts.net"`; poll 10 / ttl 30 as r1 | OK |
| 8 | RULINGS R1112, R1854, R2232 | unchanged line in card; rows existed in r1 | OK |
| 9 | Card commands vs DEPLOY-HUB launch line | ORDER / ROLLBACK lines not in the diff; as r1 | OK |
| 10 | RESTARTS / LAUNCHD lines unchanged | not in the diff; one LAUNCHD line `com.cobalt.cos · add · …` (mode `add`, count 1) | OK |
| 11 | `desk-launch.sh deploy` bootstrap-only parse (`:2166-2196`) vs EVERY `GATE RESULT:` line: `grep -c "GATE RESULT:" <card>` | 14 lines (19–32), all column 0. Parse: strip, `substr(l,14)`, split on ` · `, needs n≥3, non-blank item and result, label == `com.cobalt.cos` | OK |
| 12 | `grep -c -E "^GATE RESULT: com\.cobalt\.cos · [^ ]+ · [^ ]"` | 13 of 14; the 14th is line 20 (`agent stopped`): item has a space, which the parse allows (only needs non-blank; its line-2180 grep needs only `[^ ]+` label) and its result `YES — …` is non-blank | OK |
| 13 | Line 29 (X15) | `GATE RESULT: com.cobalt.cos · X15 · DEFERRED by his word (…) …`: label ok, item `X15`, result starts `DEFERRED`, no stray ` · ` after the result start | OK |
| 14 | Stray ` · ` inside a result: `grep -c -E "^GATE RESULT: com\.cobalt\.cos · [^ ]+ · .* · "` | 2 (X14 line 26 `… · max num_turns …`, X17 line 30 `… · opus ok …`). The awk splits them into extra fields f[4]… but only f[1..3] are tested; f[3] is non-blank, so no refusal | OK (NOTE) |
| 15 | Other refusal paths (`:2166-2247`): TIP/BRANCH/WORKTREE `none`; no `## SHIPS`; MIGRATIONS `none`; `## GATE RESULTS`, MARKERS, SMOKE READS present; BASE `main`; REPORT `reports/deploy-*.md`; TAG plain; one `## LAUNCHD` section; no `db query` with `%` | all hold | OK |

## ISSUES

- NOTE: lines 26 (X14) and 30 (X17) carry extra ` · ` in their result text; the parse tolerates them today (checks 14), but a future edit that blanks the text before the first extra ` · ` would not be caught either way. Rewording them with `;` or `/` would remove the question; not required.
- NOTE: X15 is a deferral on his relayed word (brain 9b07db5a R2322), not a result; CHECK ASKS X4 still calls X15 "his row". The desk should confirm the hub accepts a DEFERRED row there.
- NOTE: not checked, run-time state: live-session reads (`claude agents --json`), cobalt_dev lock directory, the 300,000-token desk guard, `lock_free`/`lock_dir_free`, and that `reports/deploy-cos-bootstrap.md` does not yet exist.

PREFLIGHT DONE · card: cos-bootstrap · checks: 15 · fails: 0 · ready: YES
