# Card 929 (deploy-cos-bootstrap) — preflight after the fills and the wording amend

Card: `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md`, clean in git, HEAD `a4c0a3e2`. Read-only; nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---------|--------|---------|
| 1 | `grep -c "«FILL" <card>` | `0` | OK |
| 2 | `git diff 5dfea116~1..HEAD -- <card>` | five hunks only: TAG; agent-stopped row; X15 row; line 39 (NOT IN THIS JOB); HIS INPUTS line. No header, LAUNCHD, MARKERS, SMOKE, ORDER, ROLLBACK or other RECORDS line changed. (Prompt said lines 39 and 63; line 63 is the HIS INPUTS line, as expected.) | OK |
| 3 | TAG form, `git tag -l deploy-2026-10-21-cos-bootstrap` | form `deploy-<date>-<job>`; tag list empty | OK |
| 4 | `ls ops/desk/retired-labels`; `grep -c ""` | listed; 1 line, `com.cobalt.agent` | OK |
| 5 | WAITS: cutover-tooling `23e72289`, tunables `1d6f649e` | both ancestors of HEAD (`merge-base --is-ancestor` exit 0); deploy reports present | OK |
| 6 | WAITS: agent retired | `retired-labels` holds it (check 4) | OK |
| 7 | WAITS: `hitl.page_base_url` set; also the two K5 tunables | `tunables.yaml:1038` `value: "https://cobalt.taild24291.ts.net"` (a URL, no secret); `cos.poll_interval_s` 10 (:1009); `hitl.request_ttl_min` 30 (:1027) | OK |
| 8 | RULINGS rows R1112, R1854, R2232 | each one `\| R… \|` line in cto-2026-10-11 / -10-18 / -10-20 (existence only; HIS RULING + APPROVED text not re-read here) | OK |
| 9 | Card commands vs DEPLOY-HUB launch line | `sh /Users/cobalt/cobalt/ops/desk/*` covers deploy-step-c `--bootstrap-only` and `--owed-clear`; `launchctl bootstrap gui/501 …/com.cobalt.cos.plist` and `bootout` are generated from the `add` LAUNCHD line; `launchctl print gui/501/*`, `grep *`, `ls *`, `date*` listed | OK |
| 10 | RESTARTS / LAUNCHD lines unchanged | LAUNCHD line untouched in the diff; the card has no RESTARTS section (none in the diff either) | OK |
| 11 | `desk-launch.sh deploy` bootstrap-only GATE RESULTS rule (`desk-launch.sh:2182-2194`) | every `GATE RESULT:` line must split on ` · ` into `<label> · <item> · <result>` with the label exactly `com.cobalt.cos`. Card line 29 is `GATE RESULT: X15 · DEFERRED by his word (…) — … brain 9b07db5a R2322`: label `X15`, only two fields, no ` · ` before the result | **FAIL** |

## ISSUES

- FAIL (check 11): card line 29 would make `desk-launch.sh deploy` exit 1 with `REFUSED: deploy: bootstrap-only card: a GATE RESULT line is not GATE RESULT: com.cobalt.cos · <item> · <result>: …` (the awk finds `n < 3`; the label would also fail `f[1] != lab`). The fix is a desk edit, not this seat's: rewrite it as `GATE RESULT: com.cobalt.cos · X15 · DEFERRED by his word (…) …` (the old placeholder form). Keep the text free of a stray ` · `, and recommit before the launch (the card must be committed and unchanged).
- NOTE: X15 is a deferral on his relayed word (brain 9b07db5a R2322), not a result. CHECK ASKS X4 still calls X15 "his row". The desk should confirm that is what he wants the hub to accept.
- NOTE: the card's other refusal paths read clear: TIP, BRANCH, WORKTREE all `none`; no `## SHIPS`; MIGRATIONS `none`; one LAUNCHD line of mode `add`; label not `agent`, `aset` or `radar`; REPORT is `reports/deploy-*.md`; TAG is a plain name with no `pre-`/attempt tag. Not checked here: the live-session reads (`claude agents --json`), the cobalt_dev lock directory and the 300,000-token desk guard, all run-time state.

PREFLIGHT DONE · card: cos-bootstrap · checks: 11 · fails: 1 · ready: NO
