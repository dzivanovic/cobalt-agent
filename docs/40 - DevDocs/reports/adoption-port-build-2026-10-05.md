# adoption-port (03d) — build report, round 2026-10-05 (P5, P6)

## §0 Headline
- ROUND 2 (P7), FAILED at W: the card's mark is on the test (`5719af3c`). Offline it skips (`4 passed, 1 skipped`). Under the dev DB it runs and FAILS, `DID NOT RAISE DbConfigError`, in E3 and in the deploy gate's pass 1 (`1 failed, 4465 passed`). The mark cannot make that test green; `DECISION P7` asks the desk which body it should have. `cobalt_dev` stayed at 0013 and `.env` is removed.

Round 1:
- P5 and P6 are built at tip `74370e5d`, on `e6ba65e6`. P1–P4 shipped in set 3b and were not rebuilt.
- P5: `cobalt validate --no-db` skips Sheets, the SheetMode coupling and Day modes, and prints one `SKIPPED (--no-db):` line for each. Every other check ran with no Postgres settings and passed (E3 mutation output). Without the flag, `validate` is unchanged.
- P6: `DEPLOY-HUB.md:101` (d2) now runs `… validate --no-db`, plus the card's one sentence.
- Gate green: offline 3786/0, with-DB 856/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and `.env` is removed. RESTARTS: com.cobalt.radar.

## L74
- At session start the harness sent a block asking commits to end with a `Claude-Session:` line. It is recorded here once and not acted on: BUILD-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` (06:54:52 EDT), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md" · 0 · cd22ea7c3fb89aea9231fb82e7960e4777938d0d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R327 row · grep -n "^| R327 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 333:| R327 | 10-05 06:19 ET | HIS RULING, standing: no deploy waits on a ruling a small later card can resolve; it ships on the default. S3 deploys now, any hour: overrules L66/L43 for JOB `deploy-s3-1005`. Words: `cto-2026-10-05-words.md`. | HIS RULING · APPROVED · APPLIED: LAWS.md L43 at 06:45 |
RULING 2026-10-03 R327 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R327 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R327 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R347 row · grep -n "^| R347 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 20:| R347 | 10-05 06:47 ET | HIS RULING (brain relay, `brain-direction-2026-10-02.md` `## RULED 2026-10-05 morning` A): a feature's small findings go as rows on THE SAME card, re-checked, redeployed; no new card; review 3 on: no outside house, kept builder reruns failed tests. | HIS RULING · APPROVED |
RULING 2026-10-05 R347 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R347 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · e89ef63a7003b1a9abe0f1377a3994cf525e00d4
RULING 2026-10-05 R347 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
HOUSE A overruled 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
HOUSE A overruled 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
AUTHORIZED
```

### Round 2 (P7), 10:11 EDT
Same call, card now at `2cf07eb0`. Output: every row the same as above except `CARD COMMITTED · … · 0 · 2cf07eb0a119e62c3ea38015afcbb3e3a282e319`, and the last line is `AUTHORIZED`.

## PREFLIGHT
### Round 2 (P7)
A NEW session at `CONTINUE: P7`, run as RECOVERY: `git status --short --branch` → `## ops/adoption-port-1005`. `git log --oneline -5` → `53b56384 fix(adoption-port): validate's no-flag path pinned by test; DevDocs line (check O2)` · `5ac157d5 wip(adoption-port): check red — O2 …` · `71829ddd docs(adoption-port): build report — 74370e5d` · `74370e5d …` · `ec98fada …`. `ls -la …/adoption-port-1005/.env` → `No such file or directory`. `date` → `Mon Oct  5 10:11:25 EDT 2026`.

| rule | command | exit | output |
|---|---|---|---|
| symbol | `grep -n -F "offline_skip" tests/cobalt/conftest.py` | 0 | `68:def offline_skip_marks(item) -> list:` · `75:def require_offline_skip(item) -> None:` · `77:    if not offline_skip_marks(item):` · `116:def offline_skip_guard():` · … The card's `:78` is the `raise AssertionError(UNMARKED_REACH…)` line of `require_offline_skip`, and its `:124` is `pytest.fail` in `offline_skip_guard` (Read `:55-144`). `:67-70` is the start of `offline_skip_marks` (`item.iter_markers(name="skipif")`) |
| symbol | `grep -n -F "skipif(" tests/cobalt/test_drc_d4_fix_r1_runs.py tests/cobalt/test_voice_plan.py` | 0 | `test_drc_d4_fix_r1_runs.py:59:@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")` · `test_voice_plan.py:102:` (the same) |
| deploy red | `grep -n -F "test_without_the_flag_validate_still_reads_the_db" "…/reports/deploy-deploy-03d-1005.md"` | 0 | `100:` `… FAILED: AssertionError: with-DB test without an offline skip mark: … (tests/cobalt/conftest.py:78, require_offline_skip) …` · `137:FAILED: gate — G (c) — … · rollback: not used · decisions: 1 · for Dejan: 0` |
| wc | `wc -l tests/cobalt/test_validate_no_db.py` | 0 | `136` |
| restarts, empty range | `uv run cobalt jobs restarts 53b56384..HEAD` | 0 | `docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	M	DOCS	-` · `RESTARTS: none` (the report edit was not yet committed) |

E0 was not re-run for round 2. The round entered at the row, and W's offline pass on the tip is the full-suite run.

### Round 1
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Mon Oct  5 06:54:54 EDT 2026
status · git status --short --branch · 0 · ## ops/adoption-port-1005
head · git log --oneline -1 · 0 · e6ba65e6 docs(desk): §5 plan for his restart order
diff · git diff --stat e6ba65e6 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/adoption-port-1005 · 0 · e6ba65e6 docs(desk): §5 plan for his restart order
env here · ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat e6ba65e6` | 0 | `docs(desk): §5 plan for his restart order` · `docs/40 - DevDocs/reports/cto-2026-10-05.md \| 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)` |
| restarts, empty range | `uv run cobalt jobs restarts e6ba65e6..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |
| symbol | `grep -n "def load_sheet_modes_config" src/cobalt/aset/config.py` | 0 | `251:def load_sheet_modes_config() -> SheetModesConfig:` |
| symbol | `grep -n "TraderSettings.from_db" src/cobalt/aset/config.py src/cobalt/daymode/config.py` | 0 | `src/cobalt/aset/config.py:267:        return TraderSettings.from_db().sheet_modes` · `src/cobalt/daymode/config.py:324:        return TraderSettings.from_db().daymode` |
| symbol | `grep -n "def load_daymode_config" src/cobalt/daymode/config.py` | 0 | `309:def load_daymode_config(sheet_modes=None) -> DayModeConfig:` |
| symbol | `grep -n "def from_db" src/cobalt/settings/models.py` | 0 | `319:    def from_db(cls, store=None) -> TraderSettings:` |
| symbol | `grep -n "db.connect" src/cobalt/settings/store.py` | 0 | `35:        return db.connect(self.db_name, side=self.SIDE)` |
| symbol | `grep -n -E "class DbConfigError\|def _open\|Missing Postgres settings" src/cobalt/db.py` | 0 | `136:class DbConfigError(RuntimeError):` · `160:def _open(dbname: str, credential: Credential = Credential.APP) -> psycopg.Connection:` · `183:            f"Missing Postgres settings for the {credential.name} credential: "` |
| callers | `grep -rn -F "_cmd_validate(" src tests` | 0 | `src/cobalt/cli.py:133:def _cmd_validate(args: argparse.Namespace) -> None:` (its one entry is `validate.set_defaults(func=_cmd_validate)`, `cli.py:519`, read) |
| symbol | `grep -n "validate_band" tests/cobalt/test_daymode.py` | 0 | … `882:        source = inspect.getsource(cobalt_cli._cmd_validate)` (read) · `883:        assert "validate_band" in source` |
| symbol | `grep -n -F "cobalt validate" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | `11:` (the launch line, `"Bash(COBALT_ENV=production uv run cobalt validate)"`) · `101:- (d2) VALIDATE, right before the gate call (seconds): \`COBALT_ENV=production uv run cobalt validate\` → exit 0; …` · `121:` (D1) · `141:4.5 …` · `151:- (f) …` |
| cli.py ranges | Read `src/cobalt/cli.py:125-534` | — | `:133` `def _cmd_validate`, `:144` taxonomy, `:178` `sheets = load_sheet_modes_config()`, `:194-205` coupling, `:207` `dm = load_daymode_config(sheets)` to `:226`, `:228-246` band, `:248-261` card states, `:273-293` redaction/guard/notify, `:298-438` jobs, `:440-446` heartbeat, `:452-455` archiver, `:460-469` placement, `:516-519` the `validate` parser: all as the card gives them |
| db.py | Read `src/cobalt/db.py:136-190` | — | `DbConfigError` `:136`; `_open` `:160`, raises at `:182-190` on a missing `POSTGRES_HOST` / user / password |
| DEPLOY-HUB `:74`, `:77` | Read | — | `:74` lists `validate` among the unstarred production strings; `:77` "an unstarred allow matches by PREFIX — … trailing arguments to the SAME command are admitted, never another command" |
| wc | `wc -l src/cobalt/cli.py "…/DEPLOY-HUB.md" "…/cobalt/cli.md"` | 0 | `546` · `182` · `100` |
| tail | `tail -n 3 reports/s3-d2-probe-2026-10-05.md` | 0 | `PROBE DONE · job: s3-d2-probe · cause: proven · fix: code · decisions: 1` |
| tail | `tail -n 3 reports/adoption-hubs-decisions-2026-10-03.md` | 0 | `FOR THE CHECK (card \`02\` \`## RECORDS\`): \`Build decisions 1–11 answered …\`` |
| tail | `tail -n 3 reports/deploy-hub-text-decisions-2026-10-03.md` | 0 | `FOR THE CHECK (card 02b \`## RECORDS\`): \`Grok's 8 findings answered …\`` |
| tail | `tail -n 3 reports/adoption-scripts-b-check-2026-10-03.md` | 0 | `CHECK DONE · job: adoption-scripts-b · pass: 1 · tip: b7eeb80c · … · ready: YES · decisions: 3 · for Dejan: 0` |
| probe read | Read `reports/s3-d2-probe-2026-10-05.md` whole | — | `## CAUSE` `:29`; step 3a: `cli.py:59 load_dotenv(Path(__file__).resolve().parents[2] / ".env")` — the settings come from `<tree root>/.env` only, which is absent in this worktree |

Card records copied (re-read where the list can): the 10-03 judge set-3 line; the chain checks stand for byte-equal files; RESTARTS homes (`ops/desk/*`, `tests/*` → test/documentation, `docs/**` → DOCS); TREE STATE `unchanged` holds; STEP-G exit 4 reading of sentence (5); preflight 10-03 issues answered; R167 build defaults stand; ROUND 2026-10-05: P5–P6 from `deploy-s3-1005`'s (d2) failure (re-read: probe `## CAUSE`, above); expected `RESTARTS: com.cobalt.radar` for `src/cobalt/cli.py` (derived at RESTARTS); no `DB` key, the job takes the lock at W; under `--no-db` the literal guard prints `INACTIVE` without `COBALT_MASTER_KEY` (an environment read).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `e6ba65e6` → `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 589.53s (0:09:49)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.17s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`; no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
NEW `tests/cobalt/test_validate_no_db.py`. An autouse fixture removes `POSTGRES_HOST`, `COBALT_DB_USER`, `COBALT_DB_PASSWORD` and `POSTGRES_PORT` (`raising=False`) and sets `cli.taxonomy_validate.main` to `lambda: 0`. No with-DB red, so no lock was taken at E2.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_validate_no_db.py` on `BASE` → `3 failed, 1 passed in 0.43s`:
- (a) `test_no_db_skips_the_db_checks_and_exits_clean`: `E   cobalt.db.DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …` (the row's reason).
- (b) `test_without_the_flag_validate_still_reads_the_db`: PASSED (control).
- (c) `test_no_db_still_fails_a_config_error_it_does_not_skip`: `E   cobalt.db.DbConfigError: Missing Postgres settings for the APP credential: …` (the row's reason: on `BASE` the DB error comes first).
- (d) `test_the_parser_carries_the_flag`: `cobalt: error: unrecognized arguments: --no-db` → `SystemExit: 2`.

REWRITTEN once. The first run of (c) failed for another reason: `AttributeError: 'function' object at cobalt.daymode.propose has no attribute 'validate_band'`. The package's `propose` function shadows the module name in the dotted string. The test now patches the module object from `importlib.import_module("cobalt.daymode.propose")`, and its red became the row's `DbConfigError` above.

Commit `ec98fada wip(adoption-port): red — validate --no-db tests (P5)`.

### Round 2 (P7) — the red is the existing test at `53b56384`; no test file was written, so there is no red commit
- OFFLINE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py` → `5 passed in 0.68s`. No skip is printed, but the row wants `1 skipped`.
- WITH-DB, one lock take: `take-devdb-lock.sh adoption-port-1005 90` → `lock taken: adoption-port-1005` (exit 0, 10:12 EDT). `ls -la /Users/cobalt/cobalt-wt/*/.env` returned one line, this worktree's. `<FP>` → `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED` · `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. That is the fingerprint round 1's gate read as `LEVEL 0013` (log `:893-897`).
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_validate_no_db.py` → `1 failed, 4 passed, 1 error in 0.71s`: `conftest.py:78: AssertionError: with-DB test without an offline skip mark: tests/cobalt/test_validate_no_db.py::test_without_the_flag_validate_still_reads_the_db`, plus the teardown `E   Failed: with-DB test without an offline skip mark: …`. This is the row's reason, the deploy's G (c) red.

## E3 THE ROWS
**P5** (`src/cobalt/cli.py`): the Sheets / SheetMode coupling / Day modes block (`:178-226` at `BASE`) now sits under `else:` of `if args.no_db:` (`cli.py:183` at the tip). The flag branch prints a blank line, then three `SKIPPED (--no-db): …` lines (`:190`). The parser gets `validate.add_argument("--no-db", action="store_true", …)` (`:533`). The module docstring's synopsis reads `cobalt validate [--no-db]`. Without the flag, the same calls run in the same order, now one indent deeper.
- Test fix: on the first green run, (d) failed with `assert <built-in method append …> is <built-in method append …>`, because each `seen.append` lookup is a new bound method. It was rewritten with a named `_fake_validate`. This was a test-construction error, not a red for the row.
- Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py tests/cobalt/test_daymode.py` → `84 passed, 11 skipped in 0.92s`. `test_daymode.py:872` (`test_cobalt_validate_calls_the_same_validator`) is green.
- MUTATION 1 (the card's: drop the branch, `if args.no_db:` → `if False:`): `2 failed, 2 passed in 0.41s`. (a) and (c) failed with `E   cobalt.db.DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …`.
- MUTATION 2 (breaks control (b): `if True:`): `1 failed, 3 passed in 0.83s`, `test_validate_no_db.py:55: Failed: DID NOT RAISE <class 'cobalt.db.DbConfigError'>`. Its captured stdout is the whole validate run with no Postgres settings. The three `SKIPPED (--no-db):` lines are followed by `Tunable daymode.trade_count_band.min: 2 …`, `Card states: 8 states …`, `Redaction (F19): 17 pattern(s) …`, `literal guard: INACTIVE — COBALT_MASTER_KEY is not set …`, `Notify: …`, `Jobs (F17): 15 registered …`, `registry <-> ops/: 15 label(s), exact match.`, `registry <-> plists: … agree on every job.`, `reads: 12 config path(s) …`, `Heartbeat (F18): …`, `Archiver (spec §10): 7 tunables rows resolved.` and `Placement (docs/PLACEMENT.md): tree clean.` So no other check reaches `db._open` (X4).
- (d)'s mutation is its `BASE` red: with no `--no-db` argument, `unrecognized arguments: --no-db` (E2).
- Undone with Edit. `git diff --stat` → `src/cobalt/cli.py | 112 +++…---` and `tests/cobalt/test_validate_no_db.py | 8 ++-` (the fix plus the test fix only). `uv run pytest … tests/cobalt/test_validate_no_db.py` → `4 passed in 0.62s`.
- DevDocs: `docs/40 - DevDocs/cobalt/cli.md` gains `## 2026-10-05 — adoption-port`.

**P6** (`DEPLOY-HUB.md:101`): the command is now `COBALT_ENV=production uv run cobalt validate --no-db`, followed by the card's sentence verbatim. The rest of (d2) stands.
- RED on `BASE`: Grep tool, fixed string `COBALT_ENV=production uv run cobalt validate --no-db`, on the hub → `No matches found`. The card's `grep -n -F` form was blocked by the bare-guard hook (`## RECORDS`); the Grep tool ran the same fixed string.
- GREEN: the same Grep (count) → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:1`. `grep -n -F "are made after the merge by 4.5" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → one hit, `101:- (d2) VALIDATE, right before the gate call (seconds): \`COBALT_ENV=production uv run cobalt validate --no-db\` → exit 0; record \`Jobs (F17):\` as \`<jobsG>\`. The DB checks \`--no-db\` skips (Sheets, the SheetMode coupling, Day modes) are made after the merge by 4.5's \`COBALT_ENV=production uv run cobalt validate\` from \`/Users/cobalt/cobalt\`, on that tree's own \`.env\`, and again at smoke (f). A \`registry <-> plists\` line … \`FAILED: G (d2) — <line> · rollback: not used\`.`
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` → `19 passed, 15 warnings in 2.78s`. The launch line is unchanged (`:11`).

Commit `74370e5d fix(adoption-port): validate --no-db; DEPLOY-HUB (d2) runs it (P5, P6, L1, L41, L76)`.

### Round 2 — P7 (`tests/cobalt/test_validate_no_db.py`, inside the E2 lock take: the row edits no `src/`)
- The fix: `import os` was added to the imports, and the card's mark, verbatim, sits on the test's `def` (`:55`): `@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")`. No other line changed (`git diff --stat` → `tests/cobalt/test_validate_no_db.py | 2 ++`).
- WITH THE DEV DB ENV (same take), `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_validate_no_db.py` → `1 failed, 4 passed in 0.92s`, 0 skipped. The test is NOT skipped, as the row requires. It runs and **FAILS**: `test_validate_no_db.py:57: Failed: DID NOT RAISE <class 'cobalt.db.DbConfigError'>`. Its captured stdout shows the DB reads succeeding: `Sheets: 2 declared, low to high half < full …`, `Day modes: ladder reduced < half < full …`, through `Placement (docs/PLACEMENT.md): tree clean.` Inside the lock, the conftest serves the connection, so the autouse removal of `POSTGRES_HOST` / `COBALT_DB_USER` / `COBALT_DB_PASSWORD` raises nothing. The test's `pytest.raises(DbConfigError)` holds only where the mark now skips it. Reported as run (L1); `DECISION P7` below.
- `<FP>` again → `664 35 272c95bbb12241e3611e4b36326ccf87` = F0. `release-devdb-lock.sh adoption-port-1005` → `lock released`; `ls …/.env` → `No such file or directory` (10:13 EDT).
- OFFLINE, the row's green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py` → `4 passed, 1 skipped in 0.64s`, `SKIPPED [1] tests/cobalt/test_validate_no_db.py:55: reaches cobalt_dev (lock-relief G1)`.
- MUTATION (remove the mark): `5 passed in 0.67s`, no skip, so the row's `1 skipped` is red. Its with-DB red is E2's guard failure, on the same unmarked text. Undone with Edit; `git diff --stat` → `tests/cobalt/test_validate_no_db.py | 2 ++` (the fix only).
- Beside it: `uv run pytest … tests/cobalt/test_validate_no_db.py tests/cobalt/test_daymode.py` → `84 passed, 12 skipped in 0.96s`.
- No DevDocs line: the row changes a test, not a module.

Commit `5719af3c fix(adoption-port): the no-flag DB test carries the G1 offline skip mark (P7, L1, L76)`.

## RESTARTS
`uv run cobalt jobs restarts e6ba65e6..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_validate_no_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row.

Round 2, at `5719af3c`, `uv run cobalt jobs restarts e6ba65e6..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	M	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_validate_no_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `74370e5d`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh adoption-port-1005 all` (no `--deselect`: this build adds no with-DB test; no `--tickers`: its tests write no rows; no `--migration`) → exit 0. Verdict lines, whole:
```
offline 3786/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 856/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/adoption-port-1005-all-20261005-070841.log
```
- (a) offline `3786 passed, 755 skipped, 1 xfailed` (log `:828`): E0's 3782 plus this build's four tests in `tests/cobalt/test_validate_no_db.py`. They are offline tests, so none appears in the with-DB passes.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:845`). Lock: `lock taken: adoption-port-1005` (`:834`), `lock: waited 0 min`; LEVEL 0013.
- (c) PASS 1, executed command whole (`:899`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py` → `683 passed, 7 skipped, 3850 deselected, 2 xfailed` (`:968`). The SKIPPED lines are quoted above. `<d1>` = 683.
- (c2) `dev forward: APPLIED 07:20:44` (`:970`). `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1045`).
- (c3) PASS 2 → `173 passed, 1 deselected` (`:1527`). `<d2>` = 173; `<d>` = 856 = the gate's `with-DB 856/0`. This build adds no with-DB id.
- (c3r) `stray rows: not read (no --tickers given)`: this build's tests write no rows.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1592`) = F0 → **`cobalt_dev: 0013 — F2 = F0`**. `lock released` (`:1645`). `ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env` → `No such file or directory`.
- (e) live-note `146 passed, 1 skipped` (`:1714`) → `live-note 146/0`.

### Round 2 (P7), `<tip>` = `5719af3c`
`sh /Users/cobalt/cobalt/ops/desk/gate.sh adoption-port-1005 all --deploy` (started 10:13:47 per the log name) → **exit 1**. Verdict lines, whole:
```
offline 3786/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 1): 1 failed, 4465 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 733.10s (0:12:13)
…(warnings summary, the 7 SKIPPED lines as in round 1, the summary again)
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/adoption-port-1005-all-20261005-101347.log
```
- (a) offline `3786/0`. The offline run printed `SKIPPED [1] tests/cobalt/test_validate_no_db.py:55: reaches cobalt_dev (lock-relief G1)` (log `:757`), which is P7's offline green.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:846`), `LEVEL 0013`.
- (c) PASS 1 whole (`--deploy`) is RED. The one failure is `tests/cobalt/test_validate_no_db.py:57: Failed` with `E       Failed: DID NOT RAISE <class 'cobalt.db.DbConfigError'>` (`:974-978`). This is P7's test, now run (not skipped, not refused by G1), failing the same way as at E3. The 7 SKIPPED lines are round 1's seven, all inside the allowed set.
- (c2)–(c3r), (f), (e): not reached. Pass 1 was red, so nothing was applied above `0013` and there was nothing to roll back; the gate's last proof-only before the red was F0 at `0013`. `lock released` (`:1132`), `.env: removed` (`:1136`). `ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env` → `No such file or directory` (10:36 EDT). Live-note was not run.
- Not fixed here: making this test green changes its assertion, and the row allows the mark only ("No other test, no fixture, no `src/` line changes"; THE ROWS: the fix widens nothing). See `DECISION P7`.

## PRE-STOP SELF-CHECK
Round 2: (1) P7's test was red at E2 for the row's reason (G1 `conftest.py:78`) and offline (`5 passed`, no skip), and red under its mutation (`5 passed`). (2) The one caller is `_cmd_validate`, unchanged. The offline path and the with-DB path were both run: offline skipped, with-DB FAILED `DID NOT RAISE`. That gap is `DECISION P7`. (3) Re-read from tool output: `git log --oneline -5`, the gate output file, and the log by `grep -n -F` (`F0: `, `test_validate_no_db`, `lock released`) plus Read of `:840-859`, `:972-983` and `:1100-1137`.

Round 1:
(1) Every added test was shown red for its reason. (a): E2 `DbConfigError` and mutation 1 `DbConfigError`. (b): mutation 2, `DID NOT RAISE <class 'cobalt.db.DbConfigError'>`. (c): E2 and mutation 1, `DbConfigError`. (d): E2, `unrecognized arguments: --no-db`. Two tests were rewritten: (c) for a wrong-reason red at E2, and (d) for a bound-method identity error at the first green.
(2) `_cmd_validate` has one caller: `grep -rn -F "_cmd_validate(" src tests` → its def only. Its entry is `validate.set_defaults(func=_cmd_validate)`, and (d) pins it through `cli.main()` with and without `--no-db`. Both flag states are pinned: no_db=True by (a) and (c), no_db=False by (b). (c) pins the edge where a non-DB config error still fails under the flag. The `inspect.getsource` wiring check `test_daymode.py:872` is green.
(3) Re-read at the tip: `grep -n -F "if args.no_db:" src/cobalt/cli.py` → `183:`; `grep -n -F "SKIPPED (--no-db):" src/cobalt/cli.py` → `190:`, `537:`; `grep -n -F "validate.add_argument(" src/cobalt/cli.py` → `533:`; `grep -n -F "are made after the merge by 4.5" …DEPLOY-HUB.md` → `101:`; `git log --oneline e6ba65e6..HEAD` → `74370e5d`, `ec98fada`; gate log values by `grep -n -F` (`F0: `, `F1: `, `F2: `, `dev forward: APPLIED`, `passed`, the PASS 1 command).

## FOR THE CHECK
- `e6ba65e6..74370e5d`: `ec98fada wip(adoption-port): red — validate --no-db tests (P5)` · `74370e5d fix(adoption-port): validate --no-db; DEPLOY-HUB (d2) runs it (P5, P6, L1, L41, L76)`.
- Per row: reds, mutations and greens are under `## E2 RED` and `## E3 THE ROWS`. Caller grep is in `## PREFLIGHT`. No RUN row.
- Suites, the executed PASS 1 command, F0 / F1 / F2 and the lock lines are under `## W`. The lock was taken and released inside `gate.sh` (log `:833-834`, `:1644-1645`); the log prints no clock on those lines. The gate started 07:08:41 (log name), and the forward ran at 07:20:44.
- The RESTARTS table is above. The card's records were copied at PREFLIGHT.
- Round 2: `53b56384..5719af3c`: `5719af3c fix(adoption-port): the no-flag DB test carries the G1 offline skip mark (P7, L1, L76)`. The reds, the mutation and the offline green are under `## E2 RED` / `## E3 THE ROWS` (Round 2). The gate is under `## W` (Round 2), with log `/Users/cobalt/cobalt-wt/.gate-logs/adoption-port-1005-all-20261005-101347.log`. F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87` at the E2 take (10:12–10:13 EDT). At the gate take only F0 was read (`:846`): pass 1 was red, so no forward ran.
- X4: mutation 2's captured stdout is the whole `--no-db` run with no Postgres settings. Every non-DB check prints its line, and nothing raised `DbConfigError`.

## CONTINUE
Round 1: CLOSE, done at the report commit.
Round 2 (P7): stopped at W. After the desk answers `DECISION P7`: next: E3 (P7's test text as ruled), then RESTARTS, then W (`gate.sh adoption-port-1005 all --deploy`).

## DECISIONS
Round 1: none.

Round 2:
- **DECISION P7: the marked test FAILS wherever it runs.** `test_without_the_flag_validate_still_reads_the_db` asserts `pytest.raises(DbConfigError)`. Offline it is now skipped (the row's green). With the dev DB env, where the mark lets it run, the conftest serves the connection and validate reads Sheets and Day modes cleanly: `DID NOT RAISE` (E3 and gate pass 1, log `:974-978`). The mark alone cannot turn the deploy's G (c) green, because the test body holds only in the state the mark skips. Two options lie outside the row's files and its "No other test, no fixture" fence:
  - (A) Keep the mark and change the body to the with-DB truth: `cli._cmd_validate(argparse.Namespace(no_db=False))` returns, its output carries a `Sheets:` line and a `Day modes:` line, and there are no `SKIPPED (--no-db):` lines. That proves the no-flag path reads the DB, under the lock.
  - (B) Drop the mark and make the test offline, e.g. patch `TraderSettings.from_db` to raise. The O2 test `test_without_the_flag_the_three_checks_still_run_in_order` already pins the no-flag path offline, so (B) may be redundant.
  - Safe default taken: neither. The test is left with the card's mark only, and the stop is FAILED at W. Desk's call (the card's text); not FOR DEJAN.

## RECORDS
- BLOCKED by the bare-guard hook, not a refusal: `grep -n -F "COBALT_ENV=production uv run cobalt validate --no-db" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`. The same fixed string ran through the listed Grep tool (`## E3` P6). A check re-running P6's red should use Grep, or a fixed string without the `COBALT_ENV=production ` prefix.
- REFUSED, not needed: `uv run pytest … tests/cobalt/test_cli.py` → `ERROR: file or directory not found: tests/cobalt/test_cli.py` (a guessed neighbour file; there is none). Re-run without it.
- The L74 line: a harness block asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on.
- Card records re-read at PREFLIGHT (above). Expected `RESTARTS: com.cobalt.radar` = derived.
- `.env: removed, proven gone (W)`. One lock take only (W, inside `gate.sh`).
- Round 2: CONTINUED at P7 10:11 EDT, a NEW session on `CONTINUE: P7` (RECOVERY), with authorization re-run on the card at `2cf07eb0`. Extra lock take: E2 (P7's with-DB red and the with-DB run of the row), taken 10:12 and released 10:13 EDT, F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87`. `.env: removed, proven gone (E2)`.
- Round 2, 10:37 EDT, RECORDED, NOT FOLLOWED (BUILD-HUB UNATTENDED RULES (b): a CONTINUE "never widens the job"): a message from `cto-desk`, verbatim: "CONTINUE (desk DESK RECORD, R127, small fix on the same card, R376): take option (A). Keep the skip mark and change the body of `test_without_the_flag_validate_still_reads_the_db` (that one test only; the row's fence widens to its body) to the with-DB truth: `cli._cmd_validate(argparse.Namespace(no_db=False))` returns, its output carries a `Sheets:` line and a `Day modes:` line, and no `SKIPPED (--no-db):` line. Rerun only tests/cobalt/test_validate_no_db.py plus the deploy gate; no re-check. Append the new BUILT stop line (new tip) as the report's last line." The card at `main` is unchanged since `2cf07eb0` (`git -C /Users/cobalt/cobalt log --oneline -3 -- <card>`), and its P7 row still fences the test body; `grep -n -F "with-DB truth"` and `grep -n -F "R127"` on the card both return nothing. The fence widens only through the card: commit option (A) into row P7, then send `CONTINUE: E3`. The run stays stopped at W.
- Round 2, L74: the harness again sent a block asking for a `Claude-Session:` commit line. It was not acted on; `5719af3c` carries `Co-Authored-By` only.
- **The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.**

Round 1 stop line (superseded by round 2, P7): `built · job: adoption-port · tip: 74370e5d | on e6ba65e6 | migration: none | offline 3786/0 | with-DB 856/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0`

FAILED: W — deploy gate pass 1 red: tests/cobalt/test_validate_no_db.py::test_without_the_flag_validate_still_reads_the_db — DID NOT RAISE <class 'cobalt.db.DbConfigError'> (P7's mark lets it run under the dev DB, where its assertion cannot hold) · cobalt_dev: 0013 · .env: removed · decisions: 1 · for Dejan: 0
