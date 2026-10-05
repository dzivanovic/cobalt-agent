# 03d validate rows — draft · 2026-10-05

## §0 Headline
- Card `prompts/2026-10-03/03d-adoption-port-card.md` edited by Edit: header for round 2026-10-05, P1–P4 marked shipped (`979ec797`), rows P5 and P6 added, fence, READ, X4, RECORDS lines.
- P5: `validate --no-db` skips the three DB checks (Sheets, SheetMode coupling, Day modes; `cli.py:178-226`); every other check in `_cmd_validate` reads files or env only.
- P6: (d2) runs `--no-db`; the skipped checks are named as made at 4.5 and smoke (f), not D2.4 (D2.4 is the backup snapshot) — decision 1.
- `DEPLOY-HUB.md` not touched. `05-validate-no-db-card.md` left as found.

## CARD
Header (lines 3–12):
```
BRANCH: ops/adoption-port-1005
WORKTREE: adoption-port-1005
BASE: «FILL: main, 8 hex»
TIP:
REPORT: /Users/cobalt/cobalt-wt/adoption-port-1005/docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: «FILL: 2026-10-03 R327, 2026-10-05 R347»
```
Under WHY (line 18): `THIS ROUND (2026-10-05): P1–P4 SHIPPED in set 3b (979ec797) and are on BASE; they are NOT rebuilt. The build builds P5 and P6 only. …`
Rows P1–P4: id cell `P<n> · SHIPPED set 3b `979ec797`, not rebuilt`.

| row | what | red first | files |
|---|---|---|---|
| P5 | `cobalt validate --no-db`: skips every check of `_cmd_validate` that opens a DB connection and prints ONE line per skipped check, each beginning `SKIPPED (--no-db):` and naming the check (L1). DB reads at main `e89ef63a`, each traced to `db._open` (`src/cobalt/db.py:160`): (1) SHEETS `src/cobalt/cli.py:178-182` → `aset/config.py:267` `TraderSettings.from_db()` → `settings/models.py:319` → `settings/store.py:35` `db.connect`; (2) SHEETMODE COUPLING `cli.py:194-205` (reads `sheets.order`); (3) DAY MODES with Hotkey files and Step-downs `cli.py:207-226` → `daymode/config.py:324` `TraderSettings.from_db()`. Every other call (`:144-161`, `:228-246`, `:248-261`, `:273-293`, `:298-438`, `:440-446`, `:452-455`, `:460-469`) runs unchanged. Flag on the parser at `cli.py:516-519`. Without the flag: unchanged. With it: no DB setting read | NEW `tests/cobalt/test_validate_no_db.py`, env deleted, `taxonomy_validate.main` stubbed. (a) RED: `no_db=True` returns, three `SKIPPED (--no-db):` lines, no `Sheets:` line; on `BASE` raises `DbConfigError`. (b) control: `no_db=False` → `DbConfigError`. (c) control: `no_db=True`, `validate_band` raises `BandError` → `SystemExit(1)`. (d) parser. Mutation: drop the branch → (a) red. `test_daymode.py:872` stays green | `src/cobalt/cli.py`, `tests/cobalt/test_validate_no_db.py`, `docs/40 - DevDocs/cobalt/cli.md` |
| P6 | `DEPLOY-HUB.md` (d2) (`:101`) runs `COBALT_ENV=production uv run cobalt validate --no-db`, plus: "The DB checks `--no-db` skips (Sheets, the SheetMode coupling, Day modes) are made after the merge by 4.5's `COBALT_ENV=production uv run cobalt validate` from `/Users/cobalt/cobalt`, on that tree's own `.env`, and again at smoke (f)." Allow string `:11` admits the flag by prefix | `grep -n -F "COBALT_ENV=production uv run cobalt validate --no-db"` → one hit (none on `BASE`); `grep -n -F "are made after the merge by 4.5"` → one hit; `tests/ops/test_hub_lines.py` → `0 failed` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |

Also added: four `## NOT IN THIS JOB` lines (P1–P4 and other files; no substitute check; no `.env` in the gate, L41, L76; no hub text beyond P6), a `## READ` line, `## CHECK ASKS` X4, four `## RECORDS` lines (round, RESTARTS homes, no `DB` key, literal guard).

## DECISIONS
1. ASK DESK: the prompt and the probe name "D2.4 (~:74)" as the post-merge validate. `DEPLOY-HUB.md:132` D2.4 is SNAPSHOT (`backup status` / `backup run`); `:74` is the allow table naming the steps that use `validate` among other strings. The post-merge `validate` from `/Users/cobalt/cobalt` is 4.5 (`:141`), and smoke (f) (`:151`). Default taken: P6's sentence names 4.5 and smoke (f). [06:50]
2. ASK DESK: no check is lost, but one is moved later. Under `--no-db`, the three DB checks of the merged code against production `trader_settings` move from before the merge (d2) to inside the outage (4.5); a failure there now goes to STEP-5 (rollback), not `FAILED: G (d2)` with nothing merged. D1's `<val0>` (`:121`) runs the old code, so it does not cover the new code's coupling check. No check needs the gate itself. Default taken: accept that per R343 (a); no substitute check is drafted. [06:50]
3. ASK DESK: P5's files add `docs/40 - DevDocs/cobalt/cli.md`, beyond the prompt's "cli.py, its test file". `BUILD-HUB.md:71` (E3) requires one dated line per changed module. There is no existing test file for `_cmd_validate` (only a source grep at `test_daymode.py:872`), so the test file is new. Default taken: both are in P5's files. [06:50]
4. ASK DESK: X1–X3 in `## CHECK ASKS` ask about P1–P4, which are not rebuilt. Default taken: left as written; X4 added for this round. [06:50]

## RECORDS
- main at draft: `e89ef63a` (`git -C /Users/cobalt/cobalt log --oneline -1 main`), 06:50 EDT.
- `979ec797` = `Merge branch 'main' into deploy/set3b-1004`.
- Validate chain read: `cli.py:133-519`; `aset/config.py:251-269`; `daymode/config.py:309-326`; `redact/secrets.py:120-144`; `heartbeat/runner.py:84-110`; `archiver/settings.py:252-264`. Grep for `db.connect|from_db(|_open(|psycopg|TraderSettings` over taxonomy, session, redact, notify, `jobs/config.py`, `heartbeat/runner.py`, `archiver/settings.py`, placement, `daymode/propose.py`, `cards/models.py`, `aset/models.py`: the only hits are in `*/store.py` and `session/cli.py:95`. No module on the non-DB path imports a store.
- `tests/ops/test_hub_lines.py`: no `validate` string (`grep -n -F "validate"` → nothing).
- RESTARTS home of `src/cobalt/cli.py`: `reports/deploy-2026-09-30-1.md:180` `src/cobalt/cli.py M static import reach com.cobalt.radar`.
- `05-validate-no-db-card.md`: used for V1's DB-read list and tests, then left alone.
- Read-path size: card 03d grows by rows P5–P6 and this round's lines.

03D ROWS DRAFTED · card: 03d · rows: P5, P6 · decisions: 4
