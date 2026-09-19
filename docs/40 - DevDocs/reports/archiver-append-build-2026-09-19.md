# Archiver append-only — BUILD (tribunal FINAL design), `archiver-append-0919`

DO NOT STOP until `ARCHIVER APPEND BUILT`
Seat `archiver-append-0919`, Opus 5, OFFLINE, worktree `/Users/cobalt/cobalt-wt/archiver-append`, branch `archiver/append-0919` off main `8838dda`.
Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` (committed on main `8838dda`).
Status: PREFLIGHT green (9/9 allowed, 0 denied). BASELINE running.
ESCALATE: pending.

## AUTHORIZATION

Verified 2026-09-19 09:44 ET, before any work.

| check | command | result |
|---|---|---|
| spec committed on main | `git -C /Users/cobalt/cobalt log --oneline -2 -- "docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md"` | `8838dda docs(design): archiver append-only FINAL design (tribunal-derived, option A per R8) + its build prompt (no new rule)` — present, not empty |
| report rows committed | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 8 commits, newest `e37bc12 docs(desk): 09-19 R8 'A on archiver' recorded + folded; ops-0919 launched (919e5970); archiver final design in work` |
| `cto-2026-09-18.md` §4 R1 (06:46 "Approved") | `grep -n "^| R1 "` | row present; list (2) = `02-ops-2026-09-18.md`'s launch-line allowlist as committed `5fd90e8`; "NEVER push, never `bypassPermissions`, no production write or restart, no vault write" — says what the prompt quotes |
| R14 / R15 (the nightly overwrite — the purpose of this build) | `grep -n "^| R14 \|^| R15 "` | present. R14 17:15 ET verbatim "…i want to know where the watermark is for each ticker and I want to only add the new [bars]…"; R15 17:22 ET HOLD LIFTED + directions. Says what the prompt quotes |
| R18–R21 (L67) | `grep -n "^| R18 …R21 "` | all four present; R18 17:30 ET four-house tribunal / three checkers; R19 emergency+override+law numbers; R20 rounds; R21 "Your assumption is correct." |
| `cto-2026-09-17.md` §4 R5 (unattended standard) | `grep -n "^| R5 "` | present, 06:03 ET, verbatim |
| `cto-2026-09-19.md` §4 R3 + R6 + R5 | `grep -n "^| R3 \|^| R5 \|^| R6 "` | present. R5 07:35 "Okay, I retract my approval…" (the law is followed, not re-asked); R3 07:12 three deploys; R6 07:38 no idle lane, never a skipped law step |
| `cto-2026-09-19.md` §4 **R8** (09:30 "A on archiver") | `grep -n "R8"` line 161 | verbatim: `"A on archiver"` — A = `restate --apply` / `backfill-missing` ONLY in a QUIET WINDOW (radar idle, ≥5 min after the last poll cycle completed, ≥10 min before the next session opens); the LIVE radar poller is NOT touched; covers FINAL design → build → three-house check → deploy in today's `upsert` mode → shadow nights. **NOT covered: switching the archiver to `append`.** Says exactly what the prompt quotes |

### `grep -c` of each rule string in `prompts/2026-09-18/02-ops-2026-09-18.md`

The prompt's test ("every one must count 1") does NOT pass literally on 5 of 7 strings. Every difference is
a NARROWING — the 09-19 line restricts more than the approved 09-18 line and grants nothing it did not.
The ALLOWLIST of this launch line is a STRICT SUBSET of the allowlist R1 approved as list (2). Verdict:
**not an authorization mismatch — proceed**, with the deltas recorded here and in `## ESCALATE` (item vi).
This is the same launch line `ops-0919` runs under (`16-ops-2026-09-19.md`), so the finding is shared.

| my launch line's rule string | `grep -c` in 02-ops-0918 | what 02-ops-0918 says | delta |
|---|---|---|---|
| ``never `bypassPermissions` `` | **1** | same | none |
| ``every launch resumes from the report's last `CONTINUE:` line`` | 0 | ``resumes from the report's `CONTINUE:` line`` (count 1) | reworded, same rule |
| `auto mode on; allowlist per session (L55, L61, L62)` | 0 | `auto mode on; allowlist per session (L55, L61)` (count 1) | adds the L62 citation |
| `push never in it` | 0 | absent — but R1 states "NEVER push" for all three lines, and no push rule is in either allowlist | narrowing |
| ``no production command, no `cobalt_dev`, no `.env`, no vault write, no other seat's config`` | 0 | `no production restart, no production write, no vault write, no other seat's config` (count 1) | narrowing (command ⊃ restart/write; `cobalt_dev` + `.env` added) |
| `a usage-limit message is not a failure` … | 0 | absent | a STOP protocol; grants nothing |
| `Codex = NONE; Grok = NONE` | 0 | `Codex = NONE` (count 1) | narrowing |
| `nobody sits at this session's terminal` | 0 | `nobody sits at this terminal` (count 1) | reworded, same rule |

Allowlist subset proof (this line vs R1 list (2), by rule): `uv run pytest *`, `uv run cobalt jobs restarts *`,
`git add/commit/diff/status/log/show *`, `git -C /Users/cobalt/cobalt log*`, `cd *`, `mkdir -p *`, `ls *`,
`grep *`, `tail *`, `wc *`, `date*` — all 16 appear in the committed 09-18 line. DROPPED here, as the line
says: the `.env` cp/rm, every `COBALT_ENV=dev` and `COBALT_ENV=production` command, `launchctl`, `curl`,
`chmod`, `ops/cto-desk.sh`, `shasum`, `git -C … tag --list`.

## PREFLIGHT

Run 09:44 ET, first two minutes, before any work. Every probe sits inside its own rule's pattern.

| rule | command | exit | verdict |
|---|---|---|---|
| `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 09:44:09 EDT 2026` |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **EMPTY** |
| `Bash(git status*)` | `git status` | 0 | allowed — first two lines: `On branch archiver/append-0919` / `nothing to commit, working tree clean`. Branch correct, no rebase in progress |
| `Bash(git log*)` | `git log --oneline -1` | 0 | allowed — `8838dda …` = main's tip at worktree creation (FIRST LAUNCH) |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `8838dda` (main unchanged since the worktree was cut) |
| `Bash(ls *)` | `ls -la .env` | 1 | allowed — `ls: .env: No such file or directory`. **No `.env` in this worktree: the suite cannot reach `cobalt_dev`** |
| `Bash(ls *)` | `ls "docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md"` | 0 | allowed — the spec is in this worktree |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_archiver_store.py` | 0 | allowed — `2 tests collected` (venv built on first use) |
| `Bash(uv run cobalt jobs restarts *)` | `uv run cobalt jobs restarts main..HEAD` | 0 | allowed — header + `RESTARTS: none` (empty range on a first launch) |
| `Bash(grep *)` | the 12 authorization greps above | 0 | allowed |

0 DENIED. PREFLIGHT GREEN.

## BASELINE

Taken before any edit, 09:47 ET.

| suite | command | line |
|---|---|---|
| FULL | `uv run pytest -q tests/cobalt tests/taxonomy` | **`1562 passed, 297 skipped, 1 xfailed, 15 warnings in 43.84s`** — 0 failed |
| DIFFERENTIAL (chunk 5) | `uv run pytest -q tests/cobalt/test_archiver_store.py tests/cobalt/test_radar_poller.py tests/cobalt/test_archiver_report.py` | **`10 passed, 2 skipped in 0.09s`** |

Baseline is GREEN. Every later suite line is compared with it: `failed` stays 0, `passed` grows only by
this build's tests, `skipped` only by this build's `requires_db` tests.

## Chunk S — settings and the mode flag (spec §10)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_settings.py` before any code →
`ModuleNotFoundError: No module named 'cobalt.archiver.settings'`, `1 error in 0.10s` (collection error =
the module does not exist). Then GREEN: **`47 passed in 0.14s`**.

| what the spec asks (§10) | where it is | proven by |
|---|---|---|
| ONE model, ONE loader (L3) | `src/cobalt/archiver/settings.py`, reading `cobalt.taxonomy.loader.load_tunables()` | `test_there_is_exactly_one_yaml_reader_behind_the_settings` (no `yaml` import in the module) |
| the seven keys resolve from the SHIPPED file | `configs/cobalt/taxonomy/tunables.yaml` (new block before the S2-P2 card rows) | `test_the_seven_keys_resolve_from_the_shipped_tunables_file` |
| `write_mode` accepts EXACTLY `upsert`/`append` | `ArchiverSettings._exact_write_mode` — no `strip()`, no `lower()` | 7-case parametrize `Append`, `APPEND`, `" upsert"`, `"upsert "`, `""`, `both`, `"append\n"` + a non-string + a missing row → all refused NAMING `archiver.write_mode` |
| the shipped value is `upsert`, pinned | row `archiver.write_mode: upsert`, `status: solidified` | `test_the_shipped_write_mode_is_upsert_and_only_a_reviewed_commit_changes_it` (L7 tripwire) |
| `shadow_compare` on/off | `ShadowCompare` + `.shadow_enabled` | on/off parametrize, 5 illegal values refused, and `shadow_compare` IGNORED in `append` (§5) |
| three repair minutes are positive integers | `RepairSettings` | 3 keys × 5 bad values (`0`, `-1`, `1.5`, `"10"`, `None`) each refused naming the key; `bool` is not an integer here |
| `status: proposed` exactly where the spec says PROPOSED | 4 rows proposed, 3 solidified | `test_the_shipped_rows_carry_the_units_and_statuses_the_design_ruled` |
| `source: ruling` + citation `cto-2026-09-19.md §16 / R8` on the desk's numbers | `quiet_before_open_min`, `quiet_after_cycle_min` consumers | same test asserts the citation string |
| `cobalt validate` prints it | `validate_command_lines()`, called from `_cmd_validate` after the heartbeat block | `test_validate_prints_the_resolved_settings` — the function is unit-tested, the CLI is NOT run |

Tunables schema limit check (chunk instruction): `TunableUnit` already carries `LABEL`, `COUNT` and `MIN`
(`src/cobalt/taxonomy/tunables.py:32-53`) and `TunableRow.value` is `Any`. **No change to
`src/cobalt/taxonomy/tunables.py` was needed** — the chunk's STOP condition did not trigger.

Diff stat (chunk S): `configs/cobalt/taxonomy/tunables.yaml` +85, `src/cobalt/archiver/settings.py` +283 (new),
`src/cobalt/cli.py` +9, `tests/cobalt/test_archiver_settings.py` +280 (new),
`docs/40 - DevDocs/cobalt/archiver/settings.md` +95 (new).

SUITE: `uv run pytest -q tests/cobalt tests/taxonomy` → **`1609 passed, 297 skipped, 1 xfailed, 15 warnings
in 42.20s`**. Against BASELINE: failed 0 → 0 · passed 1562 → 1609 (+47 = this chunk's tests) · skipped
297 → 297 (this chunk adds no `requires_db` test).

CONTINUE: step 2
