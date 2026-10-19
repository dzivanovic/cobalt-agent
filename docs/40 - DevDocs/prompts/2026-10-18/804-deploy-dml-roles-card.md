JOB: dml-roles
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1309, R1321
BRANCH: deploy/dml-roles
WORKTREE: deploy-dml-roles
BASE: main
TIP: b4d8dbf9
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-dml-roles.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-18-dml-roles
MIGRATIONS: 0025 · production at 0024 · creates: no table; the NOLOGIN roles `cobalt_apply_user` and `cobalt_apply_system` (cluster-wide, already present on this server from the build gates), `cobalt_app`'s membership in both, DML-only grants on each side's schema and default privileges · old code on the new schema: additive, the old `db apply` never sets the roles and runs as before; a code revert alone runs on 0025; the rollback revokes the grants and default privileges only, never a role or a membership
SET: radar
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/dml-roles-1013` | `ce3b9dc1` | `b4d8dbf9` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dml-roles-check-2026-10-13.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md` |

## MARKERS
- `grep -c -F "0025_dml_roles" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` · before `0` · after `4` (the migration in the docstring twice, FORWARD and REVERSE)

## READ-BACK
`COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT has_table_privilege('cobalt_apply_user', '\"user\".traders', 'UPDATE') AS m0025"`
- BEFORE `f` (the 0024 level: the apply role holds no grant on the user side)
- AFTER `t` (the DML grant exists). The roles and memberships are cluster-wide, so a role count reads the same before and after (card 448 `## RECORDS`).

## SMOKE READS
- the dml roles migration registered · `grep -c -F "0025_dml_roles" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` · exit 0, a count of 1 or more
- the apply verb sets the role · `grep -c -F "APPLY_ROLES" /Users/cobalt/cobalt/src/cobalt/db_apply.py` · exit 0, a count of 1 or more

Card 448 (dml-roles-1013, K3/K5; the brain's 417 D1 follow-up). RESTARTS: com.cobalt.radar (the check's stop line). The check's held id A2 is closed by the fix report's FIXED line (report prose: 13 to 11 ids); A1 and O1 are SETTLED R1953 (A1: TEMP is PUBLIC's session-only right, refused by check_file; O1: FIX1's exact-five pin is red only on a brand-new cluster where 0025 never ran, a DR rebuild; the robust pin is a HARNESS LIST question). Deploys alone, outside market hours (R1309), after card 304 (deployed).

## RECORDS
- dml-roles-1013: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md` at `b4d8dbf9` last line: BUILT · job: dml-roles-1013 · tip: ce3b9dc1 | on e7ef198a | migration: 0025, rolled back | offline 8653/0 | with-DB 5610/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 8 of 8 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 105131
- dml-roles-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dml-roles-check-2026-10-13.md` last line: CHECK DONE · job: dml-roles-1013 · pass: 1 · tip: ce3b9dc1 · house A: Grok FINDINGS: 2 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · house B: none available · suites: offline 8653/0 · with-DB 5610/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 255901
- dml-roles-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/dml-roles-1013` → `b4d8dbf9`; code tip `ce3b9dc1`
- written by deploy-card.sh at 2026-10-19 00:42 ET (`date`); trial merge of the heads onto main in order: clean
