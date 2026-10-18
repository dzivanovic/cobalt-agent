JOB: f4-refresh-1018
LADDER: S5 · F4
BRANCH: ops/f4-refresh-1018
WORKTREE: f4-refresh-1018
BASE: 75dcdb5f
TIP:
REPORT: /Users/cobalt/cobalt-wt/f4-refresh-1018/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md
CHECK REPORT:
HOUSE B:
BAND: HIGH
RULINGS: 2026-10-10 R849, 2026-10-10 R969, 2026-10-10 R971, 2026-10-18 R1833

## PORT JOB

Scope: rows PORT and CR3 only. Card 304 (`prompts/2026-10-10/304-f4-refresh-card.md`, job `f4-refresh-1010`) is built, checked and fix-rounded on `ops/f4-refresh-1010`; its deploy stopped at STEP-C with nothing merged (`reports/deploy-f4-refresh-1010.md`, R1373), and the plist route is now card 496's deferred bootstrap (R1379). Its branch cannot deploy as it stands: main holds a copy of its build report (`a9fcd08e`), and `ops/desk/deploy-card.sh:541` refuses a check tip that is not an ancestor of the fix tip. The route is a fresh job from main, the checked work re-applied by Edit/Write (no `git merge` on a build line; card 523 row FR-P1, R1485; card 671 row PORT). The work to port is `ops/f4-refresh-1010` between its merge-base with main (`d78c66a2`) and its CHECKED code tip `edd5c076` (the later head `b1ba47d8` adds only the build report: `git diff --stat edd5c076 b1ba47d8` lists that one file). Rows A1, C1, C2, M1, W1, O1, O2, S1, D1, G1, E1, U1, K1, R1 and DOC below are the content of that port: context, not rebuilt; their RED-on-BASE lines are the old job's (done and checked: `reports/f4-refresh-check-2026-10-10.md`; fix round R998, settled R1359). Their `file:line`s are re-proved on `BASE` (`## RECORDS`); the port still finds each place by content (BUILD-HUB E3). Launch: `build` at `PORT AND CR3`.

## ROWS

| row | what | red first | files |
|---|---|---|---|
| A1 | RUN — asserts nothing (304 row A1: the §3 trace, X6, X16, X17 as data). Ported as the file `tests/cobalt/test_prefill_refresh_experiments.py`; its BASE runs are the old job's record (`reports/f4-refresh-build-2026-10-10.md`) | — (old job's output) | `tests/cobalt/test_prefill_refresh_experiments.py` |
| C1 | `DailyRefreshConfig` and its loader, the `daily_refresh:` block (304 row C1). Anchors on BASE: `prefill/config.py:121-127` (`_load_yaml_mapping`), `:29`, `:107-118` (`PrefillPathsConfig`); `configs/cobalt/prefill.yaml:7-17` | T6 config half (old job's) | `src/cobalt/prefill/config.py`, `configs/cobalt/prefill.yaml`, `tests/cobalt/test_prefill_refresh.py` |
| C2 | THE JOB ROW, TUNABLES, PLIST, SMOKE ROW (304 row C2). On BASE: `configs/cobalt/jobs.yaml` row `com.cobalt.prefill-daily` `:207-212` (the new row goes directly after it), the seat-usage row `:284-296`, the `daily.md.j2` readers entry `:330-335` (readers `:331`; NOT the `drc.md.j2` entry `:336-342`, whose readers line `:337` is identical); `tunables.yaml:1033`, `:1051`; `smoke/s2.yaml` K12.1 `:572-579`; `jobs/config.py:76`, `:88`, `:198`; `tests/cobalt/test_jobs.py:580-694`, `tests/cobalt/test_jobs_reads.py:38`, `:183`, `:230`. The plist `ops/com.cobalt.prefill-refresh.plist` is the deploy's `## LAUNCHD` row (`deferred`, CR3) | T10 (old job's) | `configs/cobalt/taxonomy/tunables.yaml`, `configs/cobalt/jobs.yaml`, `ops/com.cobalt.prefill-refresh.plist`, `configs/cobalt/smoke/s2.yaml`, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_jobs.py`, `tests/cobalt/test_jobs_reads.py` |
| M1 | `merge3`: an untouched replace of equal length emits an insert at its anchor (304 row M1). `vaultwrite/merge.py:100`, `:141-159`, `:156`, `:159` | T3b (old job's) | `src/cobalt/vaultwrite/merge.py`, `tests/cobalt/test_prefill_refresh.py` |
| W1 | `upsert_unit(…, body_fn=None)` (304 row W1). `vaultwrite/writer.py:556`, `:559`, `:564-569`, `:575-581`, `:718`, `:753`, `:836-839` | X4 / X12 (old job's) | `src/cobalt/vaultwrite/writer.py`, `tests/cobalt/test_prefill_refresh.py` |
| O1 | Ownership, market table (304 row O1). `vaultwrite/store.py:111`, `:232`; `writer.py:844`, `:892-918`; `prefill/daily.py:276-294`, `:328-355` | T1, T2, T2b, T3, T9, T15, T16a, T16b, T17 (old job's) | `src/cobalt/prefill/daily.py`, `tests/cobalt/test_prefill_refresh.py` |
| O2 | The calendar, whole unit (304 row O2). `daily.py:578-582` | T4 / X3 (old job's) | `src/cobalt/prefill/daily.py`, `tests/cobalt/test_prefill_refresh.py` |
| S1 | The stamp, template, rules and daymode (304 row S1). `session/clock.py:262-277`; `daily.py:479`; `daily.md.j2:5`, `:39-48`, `:41`, `:46`, `:55-59`; `daymode/note.py:83`, `:94-97`, `:163` | T13, X7 clock half, T6 render half (old job's) | `src/cobalt/prefill/daily.py`, `configs/cobalt/templates/daily.md.j2`, `src/cobalt/daymode/note.py`, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_prefill_daily.py`, `tests/cobalt/test_daymode_note.py` |
| D1 | Degraded, never blank, exit 1 (304 row D1). `daily.py:435`; `jobs/wrapper.py:177-198`, `:187` | T5 / X5 (old job's) | `src/cobalt/prefill/daily.py`, `src/cobalt/prefill/cli.py`, `tests/cobalt/test_prefill_refresh.py` |
| G1 | The shared Finviz gate, form B (304 row G1). `strike/detector.py:80`, `:104-105`, `:172`, `:313-319`; `radar/notes.py:26`, `:165`, `:173`, `:203`, `:215`, `:329-381`, `:357-363`, `:384-391`, `:440-446`, `:682`; `tunables.yaml:702`; `tests/cobalt/test_finviz_consumers.py:47-48`, `:65`, `:69-75` | L53 refusal, X13, X14, T14 (old job's) | `src/cobalt/prefill/daily.py`, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_finviz_consumers.py` |
| E1 | The entry point, absent note, stub, dry-run (304 row E1). `prefill/cli.py:34`, `:42-45`; `rules_gen.py:111-125`, `:128-159`; `prefill/config.py:130-139`; `daymode/note.py:238-256`, `:252`; `aset/daily_note.py:103-104`, `:184`; `daily.py:297`, `:313`, `:463-473`, `:482` | T8, X6, X16, T11, T12 (old job's) | `src/cobalt/prefill/daily.py`, `src/cobalt/prefill/cli.py`, `tests/cobalt/test_prefill_refresh.py` |
| U1 | The units refresh never touches (304 row U1). `daily.md.j2:51-52` | T7 (old job's) | `tests/cobalt/test_prefill_refresh.py` |
| K1 | Docstrings (304 row K1). `prefill/market.py:7-11`; `daily.py:4` | — | `src/cobalt/prefill/market.py`, `src/cobalt/prefill/daily.py` |
| DOC | DevDocs per changed `.py` and the F4 PDD (304 row DOC); `prefill/daily.md` `## SEAM` | `tests/cobalt/test_placement.py` green | `docs/40 - DevDocs/cobalt/prefill/*.md`, `docs/40 - DevDocs/cobalt/vaultwrite/README.md`, `docs/40 - DevDocs/cobalt/daymode/note.md` |
| PORT | `PORT (R1833, recut of card 304): BASE = main HEAD at launch. Re-apply by Edit/Write only (no git merge, no cherry-pick, no revert-of-revert, no rebase) the change of branch ops/f4-refresh-1010 between its merge-base with main (d78c66a2) and its CHECKED code tip edd5c076.` Files: `git -C /Users/cobalt/cobalt diff --name-only d78c66a2 edd5c076` → 27; 26 are ported (the rows' `files` above, plus `docs/40 - DevDocs/cobalt/prefill/cli.md`, `config.md`, `market.md`, `tests/cobalt/test_setups_d1.py`, `tests/cobalt/test_setups_registries.py`); `reports/f4-refresh-build-2026-10-10.md` is the old job's history, NOT ported (main holds it, `a9fcd08e`); this job writes its own report. ONE PROOF line per ported file, in the report. 24 files main has NOT touched since `d78c66a2` (`git diff --stat d78c66a2 <BASE> -- <file>` empty, proved at the drafting) are byte-equal to `edd5c076` after the port: `git diff edd5c076 -- <file>` empty. Two files main HAS touched keep main's lines; each one's diff against BASE equals 304's own hunks only, listed in the report: (1) `configs/cobalt/jobs.yaml` — main added the two `configs/cobalt/classify/*.yaml` entries to `no_resident_reads` after the `drc.md.j2` entry (card 591, BASE `:345-361`); 304's hunks are the `com.cobalt.prefill-refresh` row inserted after `:212` and `com.cobalt.prefill-refresh` appended to the `daily.md.j2` readers at `:331`; both cards' lines stand. (2) `configs/cobalt/smoke/s2.yaml` — main extended K18's `expect_text` (card 496 OW1, BASE `:635-637`, `data/deploy/bootstrap-owed.json`); 304's hunk is the K12.3 block inserted after K12.1 (`:572-579`) and before K13; both stand. Each seam is proved from `git diff -U0 d78c66a2 <BASE> -- <file>` against `git diff -U0 d78c66a2 edd5c076 -- <file>`. Then the deploy gate's suites run on the ported tree (BUILD-HUB): `0 failed`, `0 errors`; the strict xfails O1/A3, O2, T2b and X16's hand-typed-table leg stand as on the old tip. Then `uv run cobalt jobs restarts <BASE>..HEAD`, quoted whole | — (the port is the change; rows A1-DOC above are its content) | the 26 files above |
| CR3 | CR3: records only; write in this job's build report the plain line `BOOTSTRAP: deferred com.cobalt.prefill-refresh` (R1379, card 304 row CR3). No code | RUN — asserts nothing | the build report (`REPORT` above) |

ORDER (launch `build` at `PORT AND CR3`; A1-DOC are built and checked on the old branch, no re-red of them): PORT, file by file, one PROOF line each; the suites on the ported tree, `0 failed`; `uv run cobalt jobs restarts <BASE>..HEAD`; CR3. The stop line carries the PROOF count (26). No re-check after a fix round (L75).

RESTARTS (L42; the builder's `cobalt jobs restarts` table is the source of truth). Expected as card 304's RESTARTS paragraph, with these anchors moved on BASE: `cobalt/cli.py:68` is now `:70` (`from cobalt.drc import cli as drc_cli`; card 591 added `:64` `from cobalt.classify import cli as classify_cli`), and `pyproject.toml:68` is now `:69` (`prefill = "cobalt.prefill.cli:main"`; a `pglast` line added at `:54`). Derived set: `com.cobalt.aset com.cobalt.radar`, plus the new one-shot, merged and not loaded (`deferred`). Every other RESTARTS anchor of card 304 is unchanged on BASE (`## RECORDS`).

## NOT IN THIS JOB
- Rows A1-DOC rebuilt or re-judged; any change beyond `edd5c076`'s content and the two seams.
- Card 304's rows CR and CR2 (`CARRIED`/`SETTLED` lines): they answer the old check's THE RULE (`f4-refresh-check-2026-10-10.md`, tip `98174119`), which cannot bind a port off main (`deploy-card.sh:541`).
- The old job's build report, its branch `ops/f4-refresh-1010` and worktree `f4-refresh-1010`: history, never edited.
- Loading or bootstrapping `com.cobalt.prefill-refresh`; `data/deploy/bootstrap-owed.json`; any Finviz network call; any `uv run prefill` against his vault or the dev vault.
- F5, F20, F21, F23; `src/cobalt/strike/*`, `src/cobalt/radar/*`; a migration (none on BASE past `0024_strike_alerts.sql`).
- `src/cobalt/jobs/watchdog.py`, `src/cobalt/smoke/checks.py`, and card 496's OW1 tests (`tests/cobalt/test_jobs.py:943-1023`, `tests/cobalt/test_smoke.py:1583`).
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with its output; never fixed here.

## READ
- `prompts/2026-10-10/304-f4-refresh-card.md` whole (the rows' full text, `## NOT IN THIS JOB`, the RESTARTS paragraph, `## CHECK ASKS`).
- `docs/30 - Design/F4-FINAL-2026-10-10.md` `## SEAM`, `## CHUNKS`.
- `reports/f4-refresh-check-2026-10-10.md` `## RUNS` (held O1 `:140`, A3 `:146`).
- `git -C /Users/cobalt/cobalt diff -U0 d78c66a2 <BASE> -- configs/cobalt/jobs.yaml configs/cobalt/smoke/s2.yaml`.

## CHECK ASKS
- SCOPE OF THIS CHECK: PORT and CR3 only (the earlier check of this work is `reports/f4-refresh-check-2026-10-10.md`, ready NO, held O1 and A3 CARRIED R998, the rest SETTLED R988 R998 R1359; rows A1-DOC are not re-judged).
- P1 PORT PROOFS, per file: for the 24 files main has not touched since `d78c66a2`, `git diff --stat d78c66a2 <BASE> -- <file>` empty and `git diff edd5c076 -- <file>` empty at the tip. For `configs/cobalt/jobs.yaml` and `configs/cobalt/smoke/s2.yaml`, `git diff <BASE> -- <file>` equals 304's own hunks only, and no line of card 591's or card 496's hunks is lost.
- P2 SEAMS: `jobs.yaml` holds the `com.cobalt.prefill-refresh` row once, the `daily.md.j2` readers `[com.cobalt.prefill-daily, com.cobalt.prefill-refresh]`, the `drc.md.j2` readers unchanged, and both `classify/*.yaml` entries; `s2.yaml` holds K12.3 once and K18's owed clause.
- P3 The strict xfails of the old tip (O1, A3, O2, T2b, X16 hand-typed leg) stand strict and unedited; `reports/f4-refresh-build-2026-10-10.md` is unchanged.
- P4 The build report carries `BOOTSTRAP: deferred com.cobalt.prefill-refresh` at column 0.

## DEPLOY PROOF
- `grep -c -F "label: com.cobalt.prefill-refresh" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`
- `grep -c -F "key: prefill.refresh_interval_min" /Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml` · before `0` · after `1`
- `grep -c -F "key: prefill.refresh_window" /Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml` · before `0` · after `1`
- `grep -c -F "id: K12.3" /Users/cobalt/cobalt/configs/cobalt/smoke/s2.yaml` · before `0` · after `1`
- The refresh plist is on main · `grep -c -F "<string>com.cobalt.prefill-refresh</string>" /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` · prints 1 or more
- The refresh subcommand is registered · `grep -c -F "REFRESH_JOB = \"com.cobalt.prefill-refresh\"" /Users/cobalt/cobalt/src/cobalt/prefill/cli.py` · prints 1

## RECORDS
- Drafter `draft-304-recut` (prompt 725), 2026-10-18 06:24 EDT (`date`). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `75dcdb5f` (BASE). `git diff --stat 279c99ce 75dcdb5f -- src configs tests ops pyproject.toml` empty: the newest desk commits touch no code.
- `git diff --stat d78c66a2 main` over the 26 ported files → only `configs/cobalt/jobs.yaml | 17 +` and `configs/cobalt/smoke/s2.yaml | 3 +-`. Over every other module card 304 cites (`src/cobalt/{prefill,vaultwrite,daymode,jobs/config.py,jobs/wrapper.py,jobs/restarts.py,strike,radar,session,aset,drc,heartbeat}`, `tests/cobalt/test_vaultwrite.py`, `ops/com.cobalt.prefill-daily.plist`) → empty; `src/cobalt/db_migrations` → `cli.py` only (no new `.sql`). So every `src/` anchor in rows A1-DOC equals BASE.
- Re-proved with `git show main:` / `git grep -n … main`: `jobs.yaml:39`, `:69`, `:81`, `:193`, `:200`, `:203`, `:207`, `:284`, `:293-294`, `:330-331`, `:337`; `tunables.yaml:702`, `:1033`, `:1051`; `s2.yaml:572` (K12.1), `:630` (K18), `:633`; `cli.py:70` (was `:68`); `pyproject.toml:69` (was `:68`). `tests/cobalt/test_jobs.py` grew only after `:932` (card 496 OW1), `test_jobs_reads.py` changed one docstring line at `:100`, `test_jobs_restarts.py` added four set entries at `:271-274` and two at `:501`, `:511`: none of 304's cited lines moved.
- Main already reads 304's label: `tests/cobalt/test_jobs.py:943` and `tests/cobalt/test_smoke.py:1583` (`OWED_LABEL`), `tests/ops/test_deploy_step_c.py:37`, `tests/ops/test_desk_launch_launchd.py:33-34` (card 496, constructed fixtures); `tests/ops/test_deploy_card.py:1229`, `test_deploy_step0.py:881`, `test_desk_launch_prechecks.py:1000`, `test_the_rule_sweep.py:144` read the old check report. No F4 code is on main: no row of card 304 is satisfied there.
- Old job: build `799b6040` (R986), check ready NO tip `98174119` held 2 (R997), fix round `edd5c076` (R1004; R988, R998), CR/CR2/CR3 records (R1357, R1359, R1361, R1379), deploy card 491 FAILED STEP-C (R1373). `git diff main ops/f4-refresh-1010 -- "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md"` empty.
- For the deploy card (not this card's): `## LAUNCHD` line `com.cobalt.prefill-refresh · deferred · prompts/2026-10-18/726-f4-304-recut-card.md:C2 · dry run: none · gate: X7, X8, X9, X10, X15` (dry run `none`, R1442; gate items from card 304 `## RECORDS` WRITER GATE).
