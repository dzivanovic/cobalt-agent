JOB: f5-x2-fr1
LADDER: S5-P2 · F5
CLASS: K2
INSTALL: none
BRANCH: ops/f5-x2-fr1
WORKTREE: f5-x2-fr1
BASE: c87901c6
TIP:
REPORT: /Users/cobalt/cobalt-wt/f5-x2-fr1/docs/40 - DevDocs/reports/f5-x2-fr1-build-2026-10-20.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x2-fr1-check-2026-10-20.md
HOUSE B:
BAND: HIGH
RESTARTS: none
RULINGS: 2026-10-11 R1055, 2026-10-18 R1833

## ROWS

WHY: F5 is on main (deploy 25c51ca0) with its Groups parser built on a SYNTHETIC body: `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv:1` reads `# synthetic shape — X2 real capture owed before load` (card 731 DECISION 2, B0). X2 (`docs/30 - Design/F5-FINAL-2026-10-11.md:176`) owes ONE real Groups `g=sector&v=140` body as a committed real-shape fixture plus a test that the K2 parser reads it (L45: a divergence is fixed in the parser). THE CAPTURE IS NOT THE BUILDER'S (`## DECISIONS` 1): the builder's line (`BUILD-HUB.md:14`) admits no network command and no `cobalt` verb but `jobs restarts`; the desk captures, redacts and hands the builder ONE file (`## RECORDS`, the `«FILL»`). The builder writes it with Write only. Every `file:line` is `main` at BASE; re-find each by content before the edit (BUILD-HUB E3). Test rule (brain R1472): pins by content, no hash. The figures in the handed file are public sector figures, not his (L32); no date of the capture goes in any file, test or commit (L45 strips dates).

| row | what | red first | files |
|---|---|---|---|
| C0 | RUN — asserts nothing. THE HANDED FILE. Read the file `## RECORDS` names (the Read tool) whole; quote `wc -l <file>` and its first line (the CSV header). Redaction proof, one `grep -c -i -F` per pattern on that file, each must print `0`: `auth`, `token`, `cookie`, `account`, `session`, `@`, `Bearer`. Any non-zero, a missing file, or a header with no `Name` or no `Change` column → STOP, `FAILED: C0 — handed capture <which>` (the desk re-captures; never redacted by the builder) | — (tool output quoted in the report) | none (read only) |
| X2 | THE FIXTURE, REPLACED (not a second fixture: L45, no invented fixture once the real one exists). Write `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` whole: line 1 `# real shape — X2 capture, redacted: no auth token, account field or cookie`, then the handed file's lines unchanged (header, row order, cell formats, as handed). `groups_csv()` (`tests/cobalt/test_checkpoints_offline.py:65-68`) drops `#` lines and so reads it as is. In the same test file: the module docstring (`:10-12`) and `groups_csv`'s docstring (`:66`) say real shape, X2 done; the four lines that pin synthetic values are re-pinned to the captured file by content: `:335` (`sectors["Energy"] == {…}`, now a named row's three stored strings read off the new file), `:336` (`Utilities` change), `:355` (the `.replace('"1.15","0.90%"', …)` that blanks one Change cell, now a blank of one row's Change found in the new file), `:370` (`"Energy +1.20%"`, now that row's rendered `<name> <signed change>%`). No other test line changes. One NEW test `TestNumbers::test_real_shape_fixture_parses_and_is_marked`: the fixture's first line starts `# real shape — X2`; `parse_groups(groups_csv())` returns exactly `SECTORS`; every `change` is a `Decimal` string; no line of the file holds `auth=`. Two NEW guard tests that a real-shape mismatch is degraded, never wrong figures: `::test_change_column_renamed_is_degraded` (the header's `Change` renamed → `fetch_groups` raises `PrefillFetchError` matching `Change`) and `::test_unknown_sector_name_is_degraded` (one `Name` cell altered → raises matching `11 sector`); each built from `groups_csv()` | `::test_real_shape_fixture_parses_and_is_marked` RED on BASE: the first-line assertion fails (line 1 is `# synthetic shape — X2 real capture owed before load`). The two guard tests may pass on BASE (`checkpoints.py:191-193`, `:206-212` already raise); the report says so, they are pins, not reds | `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv`, `tests/cobalt/test_checkpoints_offline.py` |
| K2F | THE PARSER, ONLY IF THE REAL BODY FAILS IT (L45: fix the parser, never the fixture). First `uv run pytest -q tests/cobalt/test_checkpoints_offline.py` after X2; quote the result. All green → this row is `RUN — not needed`, quoted, and no `src/` file changes. A red whose cause is the real shape (a BOM on `Name`, a header word, a `%` or thousands format, a trailing blank row, a quoted empty line) → the fix is inside `parse_groups` / `_decimal` (`src/cobalt/prefill/checkpoints.py:190-221`) only; `SECTORS` (`:107-110`), the column names (`:111`), `GROUPS_URL` (`:104`) and `fetch_groups` (`:224-235`) change only if the real header proves a name wrong, each named in the report with the header line quoted. A body the fixed parser still cannot read whole stays a `GroupsShapeError` (`degraded: finviz-groups`), never a partial rank. The module doc `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` gains one line naming the real-shape rule only if `src/` changed | the X2 test above, red on the unfixed parser with the real body; its failing assertion quoted | `src/cobalt/prefill/checkpoints.py`, `tests/cobalt/test_checkpoints_offline.py`, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE. Expected (`## RECORDS`): `RESTARTS: none` when K2F changed nothing; `com.cobalt.radar` (static import reach of `cobalt.prefill.checkpoints` through `cobalt.cli`, `configs/cobalt/jobs.yaml:203`) when it changed `checkpoints.py`. The builder's line is the record; an `ESCALATE` or `UNCLASSIFIED` → `## DECISIONS` | — (tool output quoted in the report) | none |

ORDER: C0, X2, K2F, R1, then the suites and the stop line.

## NOT IN THIS JOB
- Any network request, any `cobalt checkpoint` command, any Finviz token read, any `ops/desk/` script that fetches: the capture is the desk's (`## DECISIONS` 1).
- `git mv`, `git rm`, `rm`, `mv`, `cp` of a tracked file: Write and Edit only. No second Groups fixture beside `groups_sector_v140.csv`.
- X3 (`checkpoint.narrative` `timeout_s: 60` / `max_output_tokens: 512`, `configs/cobalt/modelaccess.yaml`): owed in the 20:35–07:00 window, its own card. X4–X7, X10, X12, X13: before load, not here.
- Any migration, plist, `launchctl`, `configs/` file, `jobs.yaml` row; the four checkpoint plists stay unloaded (731 `BOOTSTRAP: deferred`).
- `src/cobalt/prefill/market.py`, `vaultwrite/`, `daymode/`, `radar/`, `strike/`; any `checkpoints.py` line outside `:104-111` and `:190-235`.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with its output; never fixed here.

## READ
- `docs/30 - Design/F5-FINAL-2026-10-11.md` `## First-gate experiments` (`:176`, row X2).
- `prompts/2026-10-18/731-f5-card.md` row K2 (`:27`), B0 (`:40`), `## DECISIONS` 2 (`:108-110`).
- `src/cobalt/prefill/checkpoints.py:95-111`, `:185-256`.
- `tests/cobalt/test_checkpoints_offline.py:1-14`, `:37`, `:65-68`, `:290-386`.
- `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` whole (12 lines at BASE).

## CHECK ASKS
- X1 REDACTION: on the tip's `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv`, `grep -c -i -F` each of `auth`, `token`, `cookie`, `account`, `session`, `@`, `Bearer`, `Set-Cookie` prints `0`; no `elite.finviz.com` URL, query string or date of the capture in the file, the tests or the commit messages.
- X2 REPLACED, NOT BOTH: the synthetic marker `# synthetic shape — X2 real capture owed before load` is gone from `tests/` (Grep tool, the tip); `fixtures/checkpoints/` holds no second Groups file; every test that read the synthetic body reads the real-shape one; the four re-pinned lines are the only changed lines of the old tests.
- X3 Does the fixture equal the handed file line for line below its marker line (the Read tool on both)?
- X4 Is every real-shape mismatch path a `GroupsShapeError` / `degraded: finviz-groups` and never a ranked partial list: a renamed column, an unknown or missing name, a blank or unparseable Change? If K2F changed `src/`, re-derive each change from the real header.
- X5 Re-derive RESTARTS from `uv run cobalt jobs restarts <BASE>..<tip>`: `none` with no `src/` change, `com.cobalt.radar` with one; nothing ESCALATEs.

## DEPLOY PROOF
- `grep -c -F "# synthetic shape — X2 real capture owed before load" /Users/cobalt/cobalt/tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` · before `1` · after `0`
- `grep -c -F "# real shape — X2 capture, redacted" /Users/cobalt/cobalt/tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` · before `0` · after `1`
- `grep -c -F "def test_real_shape_fixture_parses_and_is_marked" /Users/cobalt/cobalt/tests/cobalt/test_checkpoints_offline.py` · before `0` · after `1`
- real-shape fixture · `ls /Users/cobalt/cobalt/tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` · green: the path printed
(No suite line: `deploy-smoke.sh` maps only `ls`, `grep -c -F`, `curl` and `db query`; STEP-G runs the suites.)

## DECISIONS
1. DECISION 1 — the capture cannot run on the builder's line. `BUILD-HUB.md:14` admits `uv run pytest`, `uv run cobalt jobs restarts` and `sh /Users/cobalt/cobalt/ops/desk/*`, no `uv run cobalt checkpoint`, no network tool; no script under `ops/desk/` fetches Finviz (`grep -rln -i -e checkpoint -e finviz ops/desk/` → only `gate-lists.md`). And the named dry run does not yield a fixture: `fetch_groups` hands `response.text` straight to `parse_groups` (`checkpoints.py:235`), `cmd_run` prints only `result.report()` (`:830-832`), so no raw body is ever printed or kept; it also sends TWO GETs (screener and groups, `:242`) and, when the note exists, one `mainframe` call (`:779`). Default: THE DESK captures, before the build launches, in market hours: ONE Groups GET of `GROUPS_URL` with `g=sector&v=140` (`:104`, `:228`), admitted first by the built gate (`check_demand("07:45")` returning `None` in the same process, `:576-584`; 2 rpm ceiling, L53), the token never printed or written; the desk strips any auth, account or cookie trace and any date, saves the body outside the repo, and fills `## RECORDS` with its absolute path (the `«FILL»` blocks the launch until then). The builder commits it with Write (row X2). The dry run `uv run cobalt checkpoint run --slot 0745 --dry-run` stays an optional desk smoke after deploy, not the capture. Rejected: a desk capture script under `ops/desk/` that the builder calls — it puts a Finviz-auth fetch on the builder's CLASS string (R39 approved step and lock scripts) for one request.

## RECORDS
- THE HANDED FILE: «FILL: absolute path of the desk's redacted Groups capture (outside the repo), its line count, and the desk's gate result line — no capture time in any committed file»
- Drafter `draft-f5-x2` (prompt 911), 2026-10-20 12:11 EDT (`date`); reads only, no network, no git write. `git rev-parse HEAD` → `b9f236e2` at 12:11; `git log -1 main` → `c87901c6` at 12:14 (a desk commit); `git diff --stat b9f236e2 c87901c6 -- src tests configs ops BUILD-HUB.md CARD.md` → nothing. BASE `c87901c6`. `git merge-base --is-ancestor 25c51ca0 c87901c6` → exit 0 (F5 on main).
- Anchors read at HEAD: `checkpoints.py:104` `GROUPS_URL`, `:107-111` `SECTORS` and column names, `:190-221` `_decimal` / `parse_groups`, `:224-235` `fetch_groups`, `:238-256` `fetch_figures`, `:576-584` `check_demand`, `:779` `narrate`, `:813-834` `cmd_run`; `test_checkpoints_offline.py:65-68` `groups_csv`, `:307-318` `groups_http`, `:328-386` `TestNumbers` (value pins `:335`, `:336`, `:355`, `:370`); fixture line 1 the synthetic marker, 11 data rows; `F5-FINAL:176` row X2; `BUILD-HUB.md:14` the launch line.
- RESTARTS, from `src/cobalt/jobs/restarts.py` `classify` (`:178-264`): `tests/` → `test/documentation; no resident` (`:245-246`); `docs/` → DOCS (`:225-228`); every resident in `configs/cobalt/jobs.yaml` declares `imports:` (`:99`, `:110`, `:125`, `:159`, `:190`, `:203`, `:226`), so the conservative set is empty unless an import is unresolved (not run here). A `src/cobalt/prefill/checkpoints.py` change → static import reach: `com.cobalt.radar` (`imports: [cobalt.cli]`, `jobs.yaml:203`; card 731 RECORDS). Header `none`: the expected case; the desk sets `com.cobalt.radar` at the check launch if K2F changed `src/`.
- BAND HIGH: the drafter's band (CARD.md: when unsure, the higher). A real-shape parser change on a deployed module, a desk/builder hand-off and a possible `src/` fix; L29 holds the build on Opus.
- RULINGS: card 731's (`:15`), the F5 deploy card's (`909-deploy-f5-checkpoints-fr2-card.md:8`).
