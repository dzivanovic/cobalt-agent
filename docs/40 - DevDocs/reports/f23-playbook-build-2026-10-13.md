# f23-playbook-1013 — build report

## §0 Headline
F23 renderer built (rows P0–P8, E1, E2, B0, D0): `cobalt playbook render`, six decks per run, the Sunday 17:30 one-shot row and plist, `python-pptx==1.0.2` locked by the first `uv run` (no locked package moved).
Offline 8519/0, with-DB 5504/0, live-note 147/0 on tip `72c8a069`; `cobalt_dev` back at 0013, F2 = F0; `.env` removed.
W stopped once (the P8 live skip outside the deploy allowed set); FIX1 (the brain's ruling, card `5745b511`) put it in `DEPLOY-HUB.md:104` and `gate-lists.md` `## ALLOWED SKIPS`; W call 3 green with no OUTSIDE line.
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar. BOOTSTRAP: deferred (card 496).

## L74
A system reminder at 06:31 ET asked commits to carry a `Claude-Session:` line. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md" · 0 · 7d66b40b19ee8758e0cfbececcc51e014c537720
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Sun Oct 18 06:31:24 EDT 2026
status · git status --short --branch · 0 · ## ops/f23-playbook-1013
head · git log --oneline -1 · 0 · 749d48db docs(desk): prompt 744 amend card 721
diff · git diff --stat 749d48db · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f23-playbook-1013 · 0 · 749d48db docs(desk): prompt 744 amend card 721
env here · ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

PREFLIGHT rows (each its own call):

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 749d48db` | 0 | `docs(desk): prompt 744 amend card 721` · `docs/40 - DevDocs/prompts/2026-10-18/744-draft-721-amend.md \| 5 +++++` · 1 file changed, 5 insertions(+) |
| P0 anchor | `grep -n -F "python-multipart==0.0.22" pyproject.toml` | 0 | `35:    "python-multipart==0.0.22",` |
| P0 locked pkgs | `grep -n -E "^name = \"(lxml\|pillow\|typing-extensions\|python-pptx\|xlsxwriter)\"" uv.lock` | 0 | `2683:name = "lxml"` · `3725:name = "pillow"` · `5612:name = "typing-extensions"` (no python-pptx, no xlsxwriter) |
| P3 Family | `grep -n -F "class Family" src/cobalt/taxonomy/trade_def.py` | 0 | `116:class Family(str, Enum):` (Read: `:117-121` the five values; `:745` `family: list[Family] = Field(min_length=1)`) |
| P3 loader | Read `src/cobalt/taxonomy/vault_loader.py` | — | `:91` `STRATEGIES_DIR = "1 - Trading/4 - Strategies"`; `:131` `class VaultTaxonomyError`; `:175` `drafts: list[DraftNote]`; `:472` `def load_vault_trade_defs(vault_root: Optional[Path] = None)` |
| P3 SQL | Read `0007_radar_cards.sql` | — | `:78` `trade_def_slug IS NOT NULL` under origin radar; `:214-233` `radar_cards_v … WHERE c.origin = 'radar'` |
| P3 db | Read `src/cobalt/db.py` | — | `:227` `def connect(` `dbname: str, *, side: Side, allow_prod: bool = False` |
| P5 wrapper | Read `src/cobalt/jobs/wrapper.py` | — | `:125` `def job_run(` |
| P5 pattern | Read `src/cobalt/generated/cli.py` | — | `:54` `from cobalt.jobs.wrapper import job_run` inside `cmd_commit`; `:56` `with job_run(JOB_LABEL) as run:` |
| P5 seam | Read `src/cobalt/cli.py` | — | `:85` `from cobalt.strike import cli as strike_cli  # noqa: E402`; `:546` `strike_cli.add_parser(sub)`; `:548` `validate = sub.add_parser(`; `:334` CROSS-CHECK 1; `:350` CROSS-CHECK 2 |
| P6 jobs.yaml | Read `configs/cobalt/jobs.yaml` | — | `:242-247` cards-expire row; `:298-316` `com.cobalt.generated`; `:327` `no_resident_reads:` |
| P6 config.py | Read `src/cobalt/jobs/config.py` | — | `:27` `WEEKDAY_NAMES … 0: "Sun"`; `:358-372` `class NoResidentRead`; `:425` `def readers_of`; `:457` `unknown job label` |
| P7 world | Read `tests/cobalt/test_radar_cards_db.py` | — | `:44-97` `def world()`; `:57` `apply_0022(cards)` (a level above 0013 inside the rollback, so the file sits in PASS 2) |
| P7 create | `grep -n -F "def create_radar_card" src/cobalt/cards/store.py` | 0 | `1121:    def create_radar_card(self, spec, *, proposed_key_reason: Optional[str], now: Optional[datetime] = None,` |
| P7 callers | `grep -rn -F "create_radar_card(" src tests` | 0 | `src/cobalt/cards/store.py:1121` (def) · `src/cobalt/radar/evaluate.py:1992` · `tests/experiments/f15_p1/test_x12_transition_ids_db.py:93` · `tests/cobalt/test_radar_cards_db.py:158` · `tests/cobalt/radar_p2_support.py:248` (the fake) · `tests/cobalt/test_f15_p1_records_db.py:209`, `:217` · `tests/cobalt/test_x5_tap_refresh_db.py:130` |
| wc | `wc -l pyproject.toml src/cobalt/cli.py configs/cobalt/jobs.yaml ops/desk/gate-lists.md uv.lock` | 0 | 102 · 584 · 369 · 57 · 5962 |
| restarts | `uv run cobalt jobs restarts 749d48db..HEAD` | 0 | the only row is this report (`A`, `DOCS`, `-`); `RESTARTS: none` |

`## READ` names no report, so no `tail -n 3` row. The card's `## RECORDS` are copied under `## RECORDS` below; re-read: `pyproject.toml:35`, `uv.lock:2683` / `:3725` / `:5612`, `cli.py:85` / `:546` / `:548`, `jobs.yaml:298` / `:327` (rows above) all equal the card.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 768.15s (0:12:48)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.94s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`). The run's printed slugs are [user data] and are not copied here.

## E2 RED
Commit `4dbce187` `wip(f23-playbook-1013): red` (4 test files, no `src/` edit).

Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_playbook_offline.py tests/cobalt/test_playbook_registry.py tests/cobalt/test_playbook_db.py tests/cobalt/test_playbook_live.py` → `22 failed, 3 skipped, 5 errors in 1.42s`. Reds, first line each:
- P1 `test_python_pptx_is_pinned_exact`: `AssertionError: pyproject.toml must hold exactly one exact pin `python-pptx==<version>`, got []` (no entry).
- P2 `test_config_loads_the_committed_file` and the six `test_config_refuses_an_unknown_key_and_a_bad_type[…]` (`unknown-key`, `rows-per-slide-a-string`, `why-max-chars-a-float`, `latest-per-family-a-word`, `out-dir-a-number`, `missing-key-no-default`): `ModuleNotFoundError: No module named 'cobalt.playbook'`.
- P3 the five data tests: `ModuleNotFoundError: No module named 'cobalt.playbook'` (`test_playbook_offline.py:112`, `_book`).
- P4 the five deck tests: the same, `:112`.
- P5 `test_rerun_same_date_leaves_only_the_new_run`, `test_a_crash_before_the_swap_keeps_the_previous_folder`, `test_validation_error_exits_1_and_keeps_the_previous_folder`, `test_dry_run_writes_no_deck_and_no_row`, `test_no_vault_write`: ERROR at setup of the `seam` fixture, `ModuleNotFoundError: No module named 'cobalt.playbook'` (`:337`) — the five errors of the summary, red for the row's reason. `test_import_cobalt_cli_leaves_pptx_unloaded`: `assert ['False', 'False'] == ['False', 'True']` (the package is absent, so `cobalt.cli` does not load it). `test_the_cli_mounts_playbook_render`: `cobalt: error: argument group: invalid choice: 'playbook'` · `assert 2 == 0`.
- P6 `test_the_row_is_a_sunday_1730_one_shot`: `cobalt.jobs.config.JobConfigError: unknown job label 'com.cobalt.playbook'` (`src/cobalt/jobs/config.py:457`). `test_playbook_yaml_is_read_by_the_one_shot_only`: `AssertionError: configs/cobalt/playbook.yaml is not declared under no_resident_reads`.
- Skips: `tests/cobalt/test_playbook_db.py:92`, `:109` `Postgres env settings not available`; `tests/cobalt/test_playbook_live.py:31` `COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render`.

Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_playbook_live.py` → first run red for `ModuleNotFoundError: No module named 'pptx'` (`:33`), not the row's reason: the test was rewritten (the `cobalt.playbook` imports moved before `pptx`), rerun → `ModuleNotFoundError: No module named 'cobalt.playbook'` · `1 failed in 0.03s`.

With-DB (ONE lock take): `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh f23-playbook-1013 90` → `lock taken: f23-playbook-1013` (exit 0, 06:52:42 ET); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/f23-playbook-1013/.env`. `<FP>` → F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `TABLES 0011` · `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` (= `## LEVEL 0013` of `ops/desk/gate-lists.md`), `NOTHING WAS APPLIED`. `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_playbook_db.py` → first run `2 failed`: `cobalt: error: argument group: invalid choice: 'playbook'` · `assert 2 == 0` (the seeding through `world`, `create_radar_card` and `AsetStore.save` ran clean before it). Not the row's reason: `_render` was rewritten to import `cobalt.playbook.cli` first; rerun → `ModuleNotFoundError: No module named 'cobalt.playbook'` (`test_playbook_db.py:77`) for both · `2 failed in 0.87s`. `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh f23-playbook-1013` → `lock released` (06:53:19 ET); `ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env` → `No such file or directory`. `.env: removed, proven gone (E2)`.

RUN rows E1, E2: one probe file staged outside the worktree, `/Users/cobalt/.claude/jobs/eec8d5ba/tmp/f23-run/test_f23_e_runs.py`; run at E3 once the package exists (its output below). P0 is run at E3 as the first row (it edits no test).

## E3 THE ROWS
Commit `32424ff4` `feat(f23-playbook-1013): the Sunday playbook decks, cobalt playbook render (P0-P8, D0; L1 L3 L10 L28 L52)` (14 files).

**P0 (RUN, X1 of the lock seam).** `"python-pptx",` added after `"python-multipart==0.0.22",`. Then:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_jobs_reads.py` → `Building cobalt-agent …` · `Uninstalled 1 package in 1ms` · `Installed 3 packages in 2ms` · `25 passed in 2.71s`.
- `git diff --stat uv.lock` → ` uv.lock | 26 ++++++++++++++++++++++++++` · `1 file changed, 26 insertions(+)`.
- `git diff uv.lock` → only insertions: `{ name = "python-pptx" },` in the project's `dependencies` (`:818`) and `requires-dist` (`:876`); a new `[[package]] name = "python-pptx" version = "1.0.2"` with `dependencies = [lxml, pillow, typing-extensions, xlsxwriter]`; a new `[[package]] name = "xlsxwriter" version = "3.2.9"`. No `-` line: `lxml`, `pillow`, `typing-extensions` (and every other locked package) did not move.
- Case (a): `uv run` re-locks implicitly. The line became `"python-pptx==1.0.2",` (the version the lock names) with a two-line comment above it; the next run (`test_jobs_reads.py`, `25 passed`) left the lock with the one changed specifier line `{ name = "python-pptx", specifier = "==1.0.2" },`; `git diff --stat uv.lock` vs `749d48db` still `26 insertions(+)`. Then `git add uv.lock pyproject.toml`, a further run (`26 passed in 2.63s`) and `git diff --stat uv.lock` (worktree vs index) → empty: the run left `uv.lock` unchanged.

**P1.** Green: `uv run pytest … test_playbook_offline.py::test_python_pptx_is_pinned_exact tests/cobalt/test_jobs_reads.py` → `26 passed`. Mutation `"python-pptx>=1.0.2"` → `AssertionError: pyproject.toml must hold exactly one exact pin `python-pptx==<version>`, got ['python-pptx>=1.0.2']` · `1 failed`; undone → `1 passed`; `git diff --stat` → empty (the relock both ways, the tree back at the staged fix).

**P2.** `src/cobalt/playbook/__init__.py`, `config.py` (`PlaybookConfig`, `extra="forbid"`, `strict=True`, four required keys), `configs/cobalt/playbook.yaml`. `-k config` → `7 passed`. Mutation `extra="ignore"` → `[unknown-key]` `Failed: DID NOT RAISE <class 'pydantic_core._pydantic_core.ValidationError'>` · `1 failed, 6 passed`. Mutation `strict=False` → `[rows-per-slide-a-string]` `DID NOT RAISE` · `1 failed, 6 passed`. Undone.

**P3.** `data.py`. `-k "two_family or draft_is or no_cap or unfiled_rows or card_score"` → `5 passed`. Mutations: tie-break `-(c.card_score or 0)` for `-c.id` → `test_card_score_never_orders` `assert [1, 2, 3] == [3, 2, 1]`; `card.families[:1]` → `test_two_family_card_is_on_both_decks_with_k_1` `assert (13 in [13, 12, …] and 13 in [])`; reason always `no note` → `test_a_draft_is_listed_and_in_no_deck` `assert 'no note' == 'draft'` and `test_unfiled_rows_carry_slug_and_reason` `(15, 'draft-x', 'no note') != (15, 'draft-x', 'draft')`. A first null-order mutation (dropping `c.formed_at is None`) left `test_no_cap…` green: it was no mutation (a null maps to `0.0`, which already sorts after every negative timestamp); replaced by `c.formed_at is not None` (nulls first) → `assert [99, 12, 11, …] == [12, 11, 10, …]` · `1 failed, 4 passed`. Each undone.

**P4.** `deck.py`. `-k "walk_slide or table_rows or empty_family or why_is_cut or both_titles"` → `5 passed`. Mutations (one run): no `…` → `test_why_is_cut…` `'wwww…w' == 'wwww…w…'`; the K line removed → `test_both_titles…` `assert 'also in another family: 1' in 'opening_drive\nMon–Fri ET ending this Sunday: 2026-10-05 – 2026-10-09\n…'`; the `no setup in this family` slide skipped → `test_walk_slide_counts` `{'reversion': 1} != {'reversion': 2}` and `test_empty_family_deck_says_so` `IndexError: list index out of range` · `4 failed, 1 passed`. Then cards reversed → `test_table_rows_newest_first_8_per_slide` `['ZZPA', …] == ['ZZPQ', …]` · `1 failed, 4 passed`. Undone.

**P5.** `cli.py`, the two `src/cobalt/cli.py` lines (`:86` import, `:548` `playbook_cli.add_parser(sub)`). All offline playbook tests → `25 passed` (with P6's two red then). Mutations, batch A (one run): the rollback rename removed → `test_a_crash…` `assert {} == {'continuation.pptx': …}`; writing into a leftover `.tmp` → `test_rerun…` `'half-written.pptx' != 'opening_drive.pptx'`; a `job_run` in `--dry-run` → `test_dry_run…` `assert [('com.cobalt.playbook', 0, None)] == []`; `from cobalt.vaultwrite import VaultWriter` in `data.py` → `test_no_vault_write` `cobalt.playbook imports the vault writer: [('data.py', 'cobalt.vaultwrite')]` · `4 failed, 1 passed`. Batch B: module-level `import pptx` in `playbook/cli.py` → `test_import_cobalt_cli…` `assert ['True', 'True'] == ['False', 'True']`; `playbook_cli.add_parser(sub)` removed → `test_the_cli_mounts…` `invalid choice: 'playbook'` · `assert 2 == 0` (it also reddened the validation test, so that one was re-run alone:) the config and the load moved before `with job_run` → `test_validation_error…` `assert ('com.cobalt.playbook', 0) == ('com.cobalt.playbook', 1)` · `1 failed`. Undone.

**P6.** `jobs.yaml` row after `com.cobalt.generated` (+ `enabled: true`), the `no_resident_reads` item (`because:` cites `playbook/cli.py:140` inside `job_run` and `:130` `--dry-run`; re-read `grep -n -F "load_playbook_config()" src/cobalt/playbook/cli.py` → `130:`, `140:`), `ops/com.cobalt.playbook.plist`. `test_playbook_registry.py`, `test_jobs.py`, `test_jobs_reads.py`, `test_jobs_restarts.py` + the playbook offline file → `119 passed, 18 skipped`. Mutations (one run): `weekdays: [6]` → `test_the_row_is…` `assert [6] == [0]` and the generic `test_jobs.py::TestTheShippedRegistry::test_the_scheduled_times_match_the_plists` `assert [0] == [6]`; reader `com.cobalt.generated` → `test_playbook_yaml…` `assert ['com.cobalt.generated'] == ['com.cobalt.playbook']` · `3 failed`. Undone.

**P7.** `ops/desk/gate-lists.md`: `--deselect tests/cobalt/test_playbook_db.py` at the end of PASS 1, `tests/cobalt/test_playbook_db.py` at the end of PASS 2. Green at W (pass 2).

**P8.** `ops/desk/gate-lists.md` `## LIVE-NOTE`: `tests/cobalt/test_playbook_live.py` at the end. `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest … tests/cobalt/test_playbook_live.py` → `1 passed in 0.61s`. His per-family counts are not printed or copied ([user data]).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (gate-lists edited) → `3920 passed, 1 xfailed, 16 warnings in 974.31s (0:16:14)`.

**E1 (RUN), output WHOLE** (`uv run pytest -q -rP … test_f23_e_runs.py`, the probe staged at `/Users/cobalt/.claude/jobs/eec8d5ba/tmp/f23-run/`, removed after: `scratch-clean: removed /Users/cobalt/.claude/jobs/eec8d5ba/tmp/f23-run`):
```
E1 run 1: […/data/playbook-e1/2026-10-11/opening_drive.pptx, …/continuation.pptx, …/range_break.pptx, …/reversion.pptx, …/time_window.pptx, …/unfiled.pptx]
  2026-10-11/  6 files  ['continuation.pptx', 'opening_drive.pptx', 'range_break.pptx', 'reversion.pptx', 'time_window.pptx', 'unfiled.pptx']
E1 run 2: [the same six paths]
  2026-10-11/  6 files  ['continuation.pptx', 'opening_drive.pptx', 'range_break.pptx', 'reversion.pptx', 'time_window.pptx', 'unfiled.pptx']
E1 child said: 'BETWEEN'; kill -9 pid 1475
E1 child exit: -9
E1 ls after kill -9:
  2026-10-11.old/  6 files  ['continuation.pptx', 'opening_drive.pptx', 'range_break.pptx', 'reversion.pptx', 'time_window.pptx', 'unfiled.pptx']
  2026-10-11.tmp/  6 files  ['continuation.pptx', 'opening_drive.pptx', 'range_break.pptx', 'reversion.pptx', 'time_window.pptx', 'unfiled.pptx']
E1 next run after the kill: 6 decks
  2026-10-11/  6 files  ['continuation.pptx', 'opening_drive.pptx', 'range_break.pptx', 'reversion.pptx', 'time_window.pptx', 'unfiled.pptx']
```
(the "…" is `/Users/cobalt/cobalt-wt/f23-playbook-1013`; the run printed each path in full.) The viewer part is his, by day (`DECISION D2`): deck paths `/Users/cobalt/cobalt-wt/f23-playbook-1013/data/playbook-e1/2026-10-11/*.pptx`.

**E2 (RUN), output WHOLE:** `E2 deck: /Users/cobalt/cobalt-wt/f23-playbook-1013/data/playbook-e2/opening_drive.pptx (4 slides)` (title, two setup slides, one table of 8 rows: one `why` of exactly 120 characters shown whole, one of 300 cut to 120 + `…`). Opening it in PowerPoint and Keynote is his, by day; `rows_per_slide` and `why_max_chars` stay UNVERIFIED.

**B0 (RUN).** The line, at column 0, with the owed gate items under it:

BOOTSTRAP: deferred com.cobalt.playbook

Owed before the bootstrap: E1 viewer part (a deck open in Keynote and PowerPoint during the swap), E2 viewer part (the E2 deck above in PowerPoint and Keynote), E4 (a dev-labelled plist fires on this Mac at ET wall-clock), E5 (`uv sync` timing with and without network), E6 (heartbeat before the first Sunday).

**D0.** `docs/40 - DevDocs/cobalt/playbook/README.md` (the shape of `aset/web.md`: what it does, the command, the folder and C11 swap, config, the job, the laws, a dated line) and the dated line in `docs/40 - DevDocs/cobalt/cli.md`.

## RESTARTS
`uv run cobalt jobs restarts 749d48db..HEAD` (HEAD `32424ff4`, the report untracked) → WHOLE:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/playbook.yaml	A	no resident reads (one-shot: com.cobalt.playbook)	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/playbook/README.md	A	DOCS	-
docs/40 - DevDocs/reports/f23-playbook-build-2026-10-13.md	A	DOCS	-
ops/com.cobalt.playbook.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.playbook	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/playbook/__init__.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/config.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/data.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/deck.py	A	static import reach	com.cobalt.radar
tests/cobalt/test_playbook_db.py	A	test/documentation; no resident	-
tests/cobalt/test_playbook_live.py	A	test/documentation; no resident	-
tests/cobalt/test_playbook_offline.py	A	test/documentation; no resident	-
tests/cobalt/test_playbook_registry.py	A	test/documentation; no resident	-
uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED`; no `ESCALATE`. Equal to the card's `RESTARTS:` header.

## W THE THREE SUITES
**Call 1, on `32424ff4`:** `sh /Users/cobalt/cobalt/ops/desk/gate.sh f23-playbook-1013 all --deploy --tickers ZZPB,ZZPM` → exit 1, `RED (exit 1): 1 failed, 4598 passed, 809 skipped, 1 xfailed, 36 warnings in 771.09s (0:12:51)` (the offline step; nothing further ran, no lock taken), `log: /Users/cobalt/cobalt-wt/.gate-logs/f23-playbook-1013-all-20261018-071609.log`. The red (`grep -n -F "Error" <log>` → `:92`, `:98`): `tests/taxonomy/test_names_rule.py:81` `test_every_trade_slug_in_the_repo_is_an_example` — `L31 / ADR-0008 D5: a trade name is USER data and does not live in this repo. Every slug written under src/ or tests/ starts with 'example'` · `tests/cobalt/test_playbook_offline.py:44: slug 'draft-x' -> trade_def: draft-x` (and `:50`, `:51`). E2/E3 ran only the rows' files, so this neighbour did not show it. Fix inside the rows' test files: every fixture slug carries the `example-` prefix (`example-od-only`, `example-both`, `example-draft-x`, `example-gone`, `example-playbook-other`); `uv run pytest … tests/taxonomy/test_names_rule.py tests/cobalt/test_playbook_offline.py tests/cobalt/test_playbook_registry.py tests/cobalt/test_playbook_db.py` → `34 passed, 2 skipped`. Commit `e7de0669` `fix(f23-playbook-1013): fixture slugs carry the example- prefix (P3-P7, L31)`. RESTARTS run again on `e7de0669` → the same table, `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.

**Call 2, on `<tip>` = `e7de0669`:** the same command → exit 0, verdict lines WHOLE:
```
tests/ops: run (ops/com.cobalt.playbook.plist)
offline 8519/0
lock: waited 19 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (ZZPB,ZZPM)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5504/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f23-playbook-1013-all-20261018-072949.log
```
- (a) offline `8519/0` (log `:892` `4599 passed, 809 skipped, 1 xfailed` for `tests/cobalt tests/taxonomy`; `:964` `3920 passed, 1 xfailed` for `tests/ops`, run because `ops/com.cobalt.playbook.plist` is in the diff). Added offline tests: the 25 of `test_playbook_offline.py` (with the six config params) and the 2 of `test_playbook_registry.py`.
- (b) `lock taken: f23-playbook-1013` (`:970`) after `lock: waited 19 min`; F0 (`:981`) `664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`.
- (c) pass 1, `grep -n -F "pass 1: whole (deploy)" <log>` → `:1035`; executed command (`:1037`) WHOLE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py` → `5297 passed, 8 skipped, 101 deselected, 3 xfailed, 43 warnings in 932.90s` (`:1199`), 0 failed, 0 errors. **GATE (c) NOT MET:** the gate marks one skip `OUTSIDE the allowed set` — `tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render`. Under W (c) and DEPLOY-HUB.md STEP-G (c) (`DEPLOY-HUB.md:104`, the allowed set by test and reason) that skip is a RED. It is this build's P8 test, which the card specifies to skip without `COBALT_LIVE_VAULT_ROOT`; pass 1 runs without that variable, so it skips there by design. The allowed set is `DEPLOY-HUB.md:104` and its mirror `ops/desk/gate-lists.md` `## ALLOWED SKIPS` (kept byte-equal to the hub, `gate-lists.md:7-8`); neither is a row of this card, so the red is not fixed here (`## DECISIONS`, W).
- (c2) `dev forward: APPLIED 08:34:54` (`:1201`); F1 (`:1279`) `908 45 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2 → `207 passed, 1 deselected, 5 warnings in 244.66s` (`:2081`); this build's ids: `:2079` `PASSED tests/cobalt/test_playbook_db.py::test_render_reads_radar_cards_grouped_and_skips_manual`, `:2080` `PASSED tests/cobalt/test_playbook_db.py::test_job_run_stamps_a_done_row`. `<d>` = 5297 + 207 = 5504 = the gate's `with-DB 5504/0`.
- (c3r) `stray rows: none (ZZPB,ZZPM)`.
- (f) F2 (`:2155`) `664 35 272c95bbb12241e3611e4b36326ccf87` = F0 → `cobalt_dev: 0013 — F2 = F0`; `lock released` (`:2209`); `.env: removed`; `ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env` → `No such file or directory`.
- (e) live-note `147/0` (`:2279` `147 passed, 1 skipped`; the one skip names `COBALT_TEST_LIVE_DRC`, inside the allowed set; no skip names `COBALT_LIVE_VAULT_ROOT`). The run includes `tests/cobalt/test_playbook_live.py` (P8), passed.
- No `--deselect` on either call: `ops/desk/gate-lists.md` already holds this build's PASS 1 deselect and PASS 2 id (row P7), and `gate.sh:13` appends a flag's id to pass 2 again.

**Call 3, on `<tip>` = `72c8a069` (after FIX1):** the same command → exit 0, verdict lines WHOLE:
```
tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)
offline 8519/0
lock: waited 41 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (ZZPB,ZZPM)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5504/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f23-playbook-1013-all-20261018-084807.log
```
No line marked `OUTSIDE the allowed set`: the P8 skip now prints plain (FIX1's green by the gate's own check). From the log (`grep -n -E`): `:892` `4599 passed, 809 skipped, 1 xfailed` and `:964` `3920 passed, 1 xfailed` (offline + tests/ops); `:970` `lock taken: f23-playbook-1013`; `:981` F0 `664 35 272c95bbb12241e3611e4b36326ccf87`; pass 1 (the same command as call 2, `:1037`) `:1199` `5297 passed, 8 skipped, 101 deselected, 3 xfailed` → `<d1>` 5297; `:1201` `dev forward: APPLIED 10:12:04`; `:1279` F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c`; pass 2 `:2079` `PASSED tests/cobalt/test_playbook_db.py::test_render_reads_radar_cards_grouped_and_skips_manual`, `:2080` `PASSED tests/cobalt/test_playbook_db.py::test_job_run_stamps_a_done_row`, `:2081` `207 passed, 1 deselected` → `<d2>` 207, `<d>` 5504; `:2155` F2 = F0; `:2209` `lock released`; `:2279` live-note `147 passed, 1 skipped`. `ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env` → `No such file or directory`.

## FIX1 (on `CONTINUE: FIX1` from `cto-desk`, 08:46 ET)
- The fact verified: the card on `main` (`5745b511`) carries row FIX1 and three FIX1 `## RECORDS` lines; `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → `CARD COMMITTED … 5745b511b8affa1e7b641e9216fe2250489fac44` · `CARD UNCHANGED … nothing` · … · `AUTHORIZED`.
- RED (offline): the item added first at the end of `ops/desk/gate-lists.md` `## ALLOWED SKIPS` (`:54`, `tests/cobalt/test_playbook_live.py test_live_vault_renders_six_decks COBALT_LIVE_VAULT_ROOT not set`); `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_gate.py::test_the_hub_holds_no_gate_command_and_points_at_the_lists_file` → `AssertionError: ('tests/cobalt/test_playbook_live.py test_live_vault_renders_six_decks COBALT_LIVE_VAULT_ROOT not set', 'tests/cobalt/test_playbook_live.py')` · `1 failed`. RED (the gate's own check) on `e7de0669`: W call 2's `OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_playbook_live.py:31`.
- GREEN: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:104` gains, after `tests/taxonomy/test_predicate.py:262`, and before the `test_replay_line.py` item, `the skip of `test_live_vault_renders_six_decks` in `tests/cobalt/test_playbook_live.py` whose reason names `COBALT_LIVE_VAULT_ROOT not set``; the same test → `1 passed`.
- (2) `grep -n -F "test_playbook_live.py" ops/desk/gate-lists.md` → `:45` (the `## LIVE-NOTE` line, last file, once) and `:54` (the new item); nothing added. The LIVE-NOTE line run → `147 passed, 1 skipped` (the skip `test_replay_line.py:266 … COBALT_TEST_LIVE_DRC`).
- (3) `grep -n -E "print|capsys|caplog|assert .*," tests/cobalt/test_playbook_live.py` → `69:        assert len(setup_slides) == expected, family` (the message is a `Family` value) and `71:    assert [label for label, _ in runs] == ["com.cobalt.playbook"]`. No print, no capture, no note text: the file is unchanged.
- Commit `72c8a069` `fix(f23-playbook-1013): the P8 live skip joins the deploy allowed set (FIX1, L79)`. RESTARTS on `72c8a069` → the same rows plus `docs/40 - DevDocs/prompts/DEPLOY-HUB.md M DOCS -`; `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.

## PRE-STOP SELF-CHECK
(1) Every added test was red at E2 for its row's reason (quoted there, two rewritten until they were), and the E3 mutations above turned red: P1 (the `>=` pin), P2 (`extra="ignore"`, `strict=False`), P3 (four, one replaced because it was no mutation), P4 (four), P5 (seven), P6 (two, plus the generic parity test). The with-DB P7 tests and the live P8 test have their E2 reds only (a with-DB mutation would take a second lock).
(2) Callers: `create_radar_card(` hits from PREFLIGHT are the store and its existing tests; the new seeding caller is `test_playbook_db.py::_seed`, pinned by both P7 tests (passed at W pass 2). `load_playbook_config()` callers `playbook/cli.py:130` (`--dry-run`, pinned by `test_dry_run_writes_no_deck_and_no_row`) and `:140` (inside `job_run`, pinned by `test_validation_error…` through its mutation). `playbook_cli.add_parser(sub)` (`src/cobalt/cli.py:548`) pinned by `test_the_cli_mounts_playbook_render`. `data.fetch_radar_rows` pinned by P7 on `cobalt_dev`; `data.group` by the five P3 tests; `publish` by the three swap tests and E1.
(3) Re-read at the tip: `git diff src/cobalt/cli.py` (the two lines at `:86`, `:548`), `grep -n -F "load_playbook_config()" src/cobalt/playbook/cli.py` → `130:`, `140:`, the gate log lines by `grep -n -F` (`:981`, `:1035`, `:1201`, `:1279`, `:2079`, `:2080`, `:2155`), `uv run cobalt jobs restarts 749d48db..HEAD` on `e7de0669`.

## FOR THE CHECK
- `749d48db..72c8a069`: `4dbce187` `wip(f23-playbook-1013): red` · `32424ff4` `feat(f23-playbook-1013): the Sunday playbook decks, cobalt playbook render (P0-P8, D0; L1 L3 L10 L28 L52)` · `e7de0669` `fix(f23-playbook-1013): fixture slugs carry the example- prefix (P3-P7, L31)` · `f098ecf3` `wip(f23-playbook-1013): W — P8 live skip outside the deploy allowed set` (the report only) · `72c8a069` `fix(f23-playbook-1013): the P8 live skip joins the deploy allowed set (FIX1, L79)`.
- FIX1: `## FIX1`; its RED (`test_the_hub_holds_no_gate_command_and_points_at_the_lists_file` and the gate's OUTSIDE line on `e7de0669`) and GREEN (the same test, W call 3).
- Per row reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS`. RUN rows P0, E1, E2, B0 WHOLE: `## E3 THE ROWS`.
- Suites: `## W THE THREE SUITES` (call 3; call 2's commands are the same). F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 = F0. E2's take: F0 = F after, no forward. Lock: E2 06:52:42–06:53:19 ET; W `lock taken` after a 19-minute wait, released before the live-note pass.
- RESTARTS: `## RESTARTS`.
- X1: no path writes under `COBALT_VAULT_PATH`; `cobalt.playbook` imports no `cobalt.vaultwrite` module (`test_no_vault_write`); writes are `out_dir`/`--out` and the `jobs` row. X3: the five P3 tests. X4: the three swap tests and E1 (a `kill -9` between the renames leaves `<date>.old` + `<date>.tmp` and no `<date>`: `DECISION E1`). X5: P0 above; `test_import_cobalt_cli_leaves_pptx_unloaded`. X6: this report prints no count of his.
- Records copied at PREFLIGHT: `## RECORDS`.

## CONTINUE
next: none — BUILT. The desk verifies the artifact and launches the check (CHECK-HUB.md).

## DECISIONS
- DECISION W — ANSWERED: the brain's ruling 2026-10-18 (K5, L79) added row FIX1 to the card (`5745b511`); built in `72c8a069` (`## FIX1`). Kept for the record: the deploy pass 1 skips `tests/cobalt/test_playbook_live.py:31` (`COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render`), outside the allowed set of `DEPLOY-HUB.md:104`. The skip is the card's P8 design (a live-note test that "skips without `COBALT_LIVE_VAULT_ROOT`"), the same shape as the allowed `test_radar_evaluate.py:695` / `test_catalyst.py:365` / `test_predicate.py:262` / `test_s3_c4_experiments.py` x14 skips. The fix is outside this card's rows: add that test and reason to `DEPLOY-HUB.md:104` and to `ops/desk/gate-lists.md` `## ALLOWED SKIPS`. Safe default taken: nothing changed; stopped at W.
- DECISION E1 (RUN row E1): after `kill -9` between the two renames, the date folder is absent — `2026-10-11.old/` holds the previous six decks and `2026-10-11.tmp/` the complete new six — until the next run, whose first step renames `.old` back. A viewer opening `<date>` in that window finds nothing. Not fixed here.
- The five ASK DESK items below are ANSWERED: "The five ASK DESK defaults you took stand (DESK RECORD)" (`cto-desk`, the `CONTINUE: FIX1` message).
- ASK DESK 1 (07:10): the start of `publish` renames a stranded `<date>.old` back when `<date>` is missing, and deletes it when `<date>` exists; FINAL C11 names only the `.tmp` cleanup. Safe default taken: kept (X4: every ending ends with the previous or the complete new folder at `<date>` after the next run).
- ASK DESK 2 (07:10): a family with setups and no card renders title + its setup slides + `no cards yet`; the card's "Empty family → title + `no setup in this family`, or `no cards yet`" could be read as title + one slide. Safe default taken: setup slides kept (FINAL §2.2.2 "one slide per setup").
- ASK DESK 3 (07:10): P8 says `render` against his strategies folder "and `cobalt_dev`"; the live-note pass runs with `.env` absent (W (e)), so the test fakes the card store empty and proves the vault side; the cards side is P7's. It sets `COBALT_ALLOW_DEV_ENTRY=1` (a dev run reading the live vault path, read only; the strategies' mtimes are asserted unchanged). Safe default taken: as built.
- ASK DESK 4 (07:10): test 8's "`cobalt.vaultwrite` not reached from `cobalt.playbook`" is pinned as "no `cobalt.playbook` module imports `cobalt.vaultwrite`" plus the mtime snapshot: the one loader (`vault_loader.py:71-72`) itself imports the read parsers `cobalt.vaultwrite.frontmatter` and `.markers`, so a `sys.modules` check cannot pass under L3. Safe default taken: as built.
- ASK DESK 5 (08:41): the F-15 walk's slugs carry an `example-` prefix in the fixtures (`example-od-only`, `example-both`, `example-draft-x`, `example-gone`, `example-playbook-other`), forced by `tests/taxonomy/test_names_rule.py` (L31). Safe default taken: renamed; the walk's shape is unchanged.

## RECORDS
- The card's records, re-read at PREFLIGHT: R1055 row `cto-2026-10-11.md:88` `HIS RULING · APPROVED` (authorize.sh row above); `pyproject.toml:35`, `uv.lock:2683` `lxml`, `:3725` `pillow`, `:5612` `typing-extensions`, `cli.py:85` / `:546` / `:548`, `jobs.yaml:298` / `:327` equal the card; BOOTSTRAP deferred (card 496 DF1); lock seam rule 4 run as P0 (case (a)); `DB` key absent, the build took the lock.
- The L74 line: `## L74` (a system reminder asked for a `Claude-Session:` line; not acted on).
- `.env: removed, proven gone (E2)`; `.env: removed, proven gone (W)`.
- Extra gate calls: W ran three times (call 1 red on `test_names_rule.py`, fixed in `e7de0669`; call 2 the OUTSIDE skip, the stop; call 3 green after FIX1).
- `CONTINUE: FIX1` received from `cto-desk` (it names a step and states a fact: the card's new row FIX1, committed `5745b511`, preflight `93150333`); the fact verified by `authorize.sh` (AUTHORIZED) and a Read of the card. `CONTINUED at FIX1 08:46 ET`.
- `.env: removed, proven gone (W call 3)`.
- The RUN probe was staged at `/Users/cobalt/.claude/jobs/eec8d5ba/tmp/f23-run/` and removed by `scratch-clean.sh` before W. E1/E2 decks stay under the worktree's gitignored `data/playbook-e1/`, `data/playbook-e2/` for his viewer check.
- Cleanup owed: none in the tree.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f23-playbook-1013 · tip: 72c8a069 | on 749d48db | migration: none | offline 8519/0 | with-DB 5504/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | rows: 14 of 14 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 425373
