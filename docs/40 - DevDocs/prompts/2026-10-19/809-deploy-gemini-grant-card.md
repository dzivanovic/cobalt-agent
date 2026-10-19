JOB: gemini-grant
LADDER: OFF-LADDER — reports/cto-2026-10-18.md R1863
BRANCH: deploy/gemini-grant
WORKTREE: deploy-gemini-grant
BASE: main
TIP: 73a3f45a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gemini-grant.md
RULINGS: 2026-10-18 R1942
TAG: deploy-2026-10-19-gemini-grant
MIGRATIONS: none
SET: gemini-grant
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gemini-grant-1018` | `cd5e0d7c` | `73a3f45a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-grant-1018-check-2026-10-19.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md` |

## MARKERS
- `grep -c -F "holds no allow rule" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `1` · after `0`
- `grep -c -F "(card 759 serial rule)" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "the launcher adds and removes it (his 2026-10-18 A)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "with its Edit tool (write implies" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `1` · after `0`

## SMOKE READS
- sweep, dry · `DESK_LAUNCH_DRY=1 sh /Users/cobalt/.claude/ops/desk-launch.sh grant-sweep` · green: exit 0, last line `GRANT-SWEEP: 0 would be removed, 0 live`
- no fetch rule · `grep -c -F "read_url(" /Users/cobalt/.gemini/antigravity-cli/settings.json` · green: `0`

## RECORDS
- gemini-grant-1018: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md` at `73a3f45a` last line: BUILT · job: gemini-grant-1018 · tip: cd5e0d7c | on c0ebb874 | migration: none | offline 8679/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 76711
- gemini-grant-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-grant-1018-check-2026-10-19.md` last line: CHECK DONE · job: gemini-grant-1018 · pass: 1 · tip: cd5e0d7c · house A: Grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8679/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: NO · decisions: 1 · for Dejan: 0 · tokens: 202650
- gemini-grant-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-grant-1018` → `73a3f45a`; code tip `cd5e0d7c`
- written by deploy-card.sh at 2026-10-19 05:57 ET (`date`); trial merge of the heads onto main in order: clean
