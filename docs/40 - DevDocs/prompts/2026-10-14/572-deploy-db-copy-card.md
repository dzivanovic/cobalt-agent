JOB: db-copy-1014
LADDER: OFF-LADDER — reports/cto-2026-10-14.md R1471
BRANCH: deploy/db-copy-1014
WORKTREE: deploy-db-copy-1014
BASE: main
TIP: e27c520c
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-db-copy-1014.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-14-db-copy
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/db-copy-1014` | `51d83a3a` | `e27c520c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-copy-check-2026-10-14.md` | `held unfixed: 2` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-copy-build-fr1-2026-10-14.md` |

## MARKERS
- `grep -c -F "card 547 db-copy" /Users/cobalt/cobalt/ops/desk/gate.sh` · before `0` · after `1`
- `grep -c -F "card 547 db-copy" /Users/cobalt/cobalt/ops/desk/devdb-copy-env.sh` · before `0` · after `1`
- `grep -c -F "card 547 db-copy" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "card 547 db-copy" /Users/cobalt/cobalt/ops/desk/gate-lists.md` · before `0` · after `1`
- `grep -c -F "## COPY CREATE" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "## COPY CREATE" /Users/cobalt/cobalt/ops/desk/gate-lists.md` · before `0` · after `1` (the header paragraph only; no section line starts `## COPY`)
- `ls /Users/cobalt/cobalt/ops/desk/devdb-copy-env.sh` · before `No such file` · after the path

## SMOKE READS
`grep -c -F` counts lines: `card 547 db-copy` stands on ONE line (no wrap between its words) once in each of `gate.sh`, `devdb-copy-env.sh`, `desk-launch.sh` and `gate-lists.md`, and `## COPY CREATE` on ONE line once in the `gate-lists.md` paragraph and once in `BUILD-HUB.md:83`.
EXTRA READ (owed by 537): COBALT_ENV=production uv run cobalt smoke s2 --cutoff <this deploy's D1 merge time from this report, ISO 8601 with offset> --prod --json, once, after the merge; exit and first line recorded as 537's DEPLOY PROOF. Exit 0 closes it; exit 1 is a 537 fix round, not a hold on 547; exit 2 is a row error, reported to the brain, no retry with an invented value.

## RECORDS
- db-copy-1014: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-copy-build-fr1-2026-10-14.md` at `e27c520c` last line: BUILT · job: db-copy-1014 · tip: 51d83a3a | on 0a151491 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 207742
- db-copy-1014: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-copy-check-2026-10-14.md` last line: CHECK DONE · job: db-copy-1014 · pass: 1 · tip: a157d731 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 3 · fixed: 1 · held unfixed: 2 · open: 3 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 4 · for Dejan: 0 · tokens: 216923
- db-copy-1014: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/db-copy-1014` → `e27c520c`; code tip `51d83a3a`
- written by deploy-card.sh at 2026-10-14 18:51 ET (`date`); trial merge of the heads onto main in order: clean
