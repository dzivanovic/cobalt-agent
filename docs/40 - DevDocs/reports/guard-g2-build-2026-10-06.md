# guard-g2 — build report (2026-10-06)

CARD: `docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md` · BRANCH `ops/guard-g2-1006` · BASE `3c257bb9` · DB: none

## §0 Headline

- Row G2 built at `ce19a3fd`: `bare-guard.py` G2 passes `COBALT_ENV=production uv run cobalt db query --prod --side user|system …` only for a seat whose first user record holds ` PROD-READ: <date> R<n>`; `desk-launch.sh` (prompt kind) appends that stamp only for one committed HIS RULING + APPROVED row naming production reads, and refuses a typed marker that is not exactly it.
- Offline `3932/0`, live-note `146/0`, `tests/ops` `1447 passed, 1 xfailed`; with-DB not run (DB: none); `RESTARTS: none`.
- Two ASK DESK items (pipes after the query; a RULINGS list gets no stamp).

## L74

A system reminder at 07:13 EDT asked for a `Claude-Session:` line on commits. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md"` (07:13 EDT), output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md" · 0 · 992b8fee14c48713f57b413ce04452b07ab75a5d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R511 row · grep -n "^| R511 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 31:| R511 | 06:37 ET | HIS RULING: add the G2 row to `ops/desk/bare-guard.py`: a production read-only `db query` passes only for a seat citing an APPROVED HIS RULING row; all else refused. Words: `cto-2026-10-06-words.md` R511. Done by card, not a desk edit. | APPROVED — pending fold |
RULING 2026-10-06 R511 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R511 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 720c98b8555d085e1aeda2fb3932c2781354ff9d
RULING 2026-10-06 R511 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:

```
clock · date · 0 · Tue Oct  6 07:13:37 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/guard-g2-1006
    ?? "docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 3c257bb9 docs(desk): rename drafter prompt 20 (a -card name is refused as a prompt)
diff · git diff --stat 3c257bb9 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/guard-g2-1006 · 0 · 3c257bb9 docs(desk): rename drafter prompt 20 (a -card name is refused as a prompt)
env here · ls /Users/cobalt/cobalt-wt/guard-g2-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/flake-fix-2-1006/.env
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 3c257bb9` | 0 | `3c257bb988f2683bb4b7a0286250b211eb77dd25` docs(desk): rename drafter prompt 20 …; `.../2026-10-06/{20-draft-guard-g2-card.md => 20-draft-guard-g2.md} \| 2 +-`, 1 file changed |
| PROD | `grep -n -F "PROD" ops/desk/bare-guard.py` | 0 | `106:PROD = re.compile(r"COBALT_ENV=production\|(?<![\w-])--prod(?![\w-])\|cobalt_brain")`; `856:    if kind is not None and kind != "deploy" and PROD.search(command):` |
| first_message | `grep -rn -F "first_message(" ops` | 0 | `bare-guard.py:666:def first_message(transcript):`; `bare-guard.py:725:    text = first_message(event.get("transcript_path"))` |
| seat | `grep -rn -F "seat(" ops/desk/bare-guard.py` | 0 | `722:def seat(event):`; `968:        hit = bash_rules(command, seat(event))`; `976:        s = seat(event)` |
| bash_rules | `grep -rn -F "bash_rules(" ops tests/ops` | 0 | `bare-guard.py:846:def bash_rules(command, s):`; `bare-guard.py:968:        hit = bash_rules(command, seat(event))` |
| words | `grep -n -F "def words(" ops/desk/bare-guard.py` | 0 | `283:def words(segment):` |
| committed | `grep -n -F "committed \"the prompt\"" ops/desk/desk-launch.sh` | 0 | `418:    committed "the prompt" "$pfile"` |
| ruling_row | `grep -n -F "ruling_row" ops/desk/desk-launch.sh` | 0 | 238 def; 266, 273, 453, 709, 710, 720, 723 |
| run_launch (prompt) | Grep tool `run_launch "\$dir"` | — | `499:    run_launch "$dir" "$line" "reminder: one Grok hub at a time (L15); …"`; 1144, 1155 (other kinds) |
| --side choices | `grep -n -F "choices=" src/cobalt/db_query.py` | 0 | `211:    query.add_argument("--side", choices=[s.value for s in Side], required=True)` |
| requires --prod | Read `src/cobalt/db_query.py` 145-216 (the grep was refused by G2, `## RECORDS`) | — | `157: if dbname == db.PROD_DB_NAME and not prod:` / `158: raise QueryRefused(f"database {db.PROD_DB_NAME} requires --prod")`; `212: query.add_argument("--prod", action="store_true")` |
| rows | `grep -n "^\| R511 \…\| R517 " cto-2026-10-06.md` (worktree, BASE) | 0 | `19:\| R511 \| 06:37 ET \| HIS RULING: add the G2 row … \| APPROVED — pending fold \|`; `22:\| R508 \| 06:29 ET \| HIS RULING: the radar-drought survey may run its four read-only DB queries …, production read included; no writes. … \| APPROVED \|`; R514 and R517 are not in the file at BASE (they stand on main after BASE; the card quotes their rules) |
| wc -l | `wc -l` on the four row files | 0 | bare-guard.py 1039 · desk-launch.sh 1155 · test_bare_guard.py 1262 · test_desk_launch_prechecks.py 907 |
| tail | `tail -n 3 cto-2026-10-06.md` | 0 | last line: `HANDOVER: predecessor b1968ff3 → successor 23d9137a at 06:22 ET` |
| RESTARTS | `uv run cobalt jobs restarts 3c257bb9..HEAD` | 0 | only the untracked report, `DOCS`; `RESTARTS: none` |
| record re-read | `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` | 1 | nothing (the card's RESTARTS record holds) |

The card's `## RECORDS`, copied: the row sits on his veto list (R511 approves this one row); RESTARTS expected `none` (re-read above); bare-guard.py is run from the main checkout by `/Users/cobalt/.claude/settings.json:22`, desk-launch.sh linked from `/Users/cobalt/.claude/ops/`, both live only after the deploy merges; a survey launch cites a row reading HIS RULING + APPROVED naming production reads (R508 does); BASE `3c257bb9…`; R2(ii) is R517's text; R511 committed in `720c98b8`; the guard never runs a command, so the commit proof is the launcher's.

DB: none — no lock probe; with-DB strings are not used in this build.

## E0 BASELINE

- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `3c257bb9` → `3932 passed, 785 skipped, 2 xfailed, 36 warnings in 626.17s (0:10:26)`; exit 0; 0 failed, 0 errors. The only skips naming `COBALT_LIVE_VAULT_ROOT` are the two the live-note run covers (`test_catalyst.py:365`, `test_predicate.py:262`).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.04s`; the one skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED

`uv run pytest -q -rf -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py tests/ops/test_desk_launch_prechecks.py` on BASE code → `27 failed, 671 passed, 15 warnings in 60.50s`. Commit `ff2d684a wip(guard-g2): red` (test files only).

| test | n red | first line of the red | named reason |
|---|---|---|---|
| `test_g2_a_marked_seat_runs_a_production_db_query` (RED c), 3 kinds × 3 query shapes | 9 | `AssertionError: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev` / `assert 2 == 0` (`test_bare_guard.py:273`) | G2 refuses every production string on BASE |
| `test_g2_a_marked_query_with_a_separator_is_g1s_to_deny` (CONTROL e), `; ls`, `\| sh`, `\| cat` | 3 | denied by G2 on BASE (exit 2 with `G2_ROUTE`); the test asserts G1's resend text | denied both times; on BASE by G2, not G1 — red only on the deny text (the card counts (e) a control; it is denied on BASE as the card says) |
| `test_r1_a_proven_row_stamps_the_launch_line` (RED d) | 1 | the dry line has no ` PROD-READ: 2026-01-02 R2` | no stamp on BASE |
| `test_r1_a_typed_marker_without_its_proving_row_is_refused` (RED g), 9 cases | 9 | `assert 0 == 1` (`test_desk_launch_prechecks.py:224`), the dry line printed with the typed marker | the typed marker launches on BASE |
| `test_r1_a_typed_marker_other_than_the_stamp_is_refused` (CONTROL h), R3, R21, twice, no row number | 4 | `assert 0 == 1`, the typed marker launches | equality clause absent on BASE |
| `test_r1_a_typed_marker_elsewhere_on_the_line_is_refused` | 1 | `assert 0 == 1`, a line with `--append-system-prompt "PROD-READ: 2026-01-02 R2"` launches | no `PROD-READ:` refusal on BASE |

Green on BASE, as the card names them: CONTROL (a) `test_g2_a_seat_without_the_marker_in_its_first_record_is_denied` (none, later record, prompt body; 3 kinds); CONTROLS (b), (f) and the rest `test_g2_a_marked_seat_is_denied_anything_but_the_one_query_shape` (17 commands); `test_r1_a_row_that_proves_nothing_stamps_nothing` (9 cases); REFUSAL (d2) `test_r1_an_uncommitted_prompt_is_refused` (uncommitted, changed); CONTROL (g2) `test_r1_a_typed_marker_with_its_proving_row_launches_stamped_once`; the existing G2 tests (389-413).

## E3 THE ROWS

Row G2, one commit `ce19a3fd feat(guard-g2): G2 passes a launcher-stamped seat's one production db query (G2 R1 R2, L1 L3 L72)`.

- R2, `ops/desk/bare-guard.py`: `seat()` returns `"first": text` (the text `first_message` already read; no second transcript read); new `marked_read(command, s)` beside `bash_rules`: the stamp ` PROD-READ: <date> R<n>` in `s["first"]`; `words(command)` opens `COBALT_ENV=production uv run cobalt db query`; exactly one later word `--prod`, none `--prod=…`; every `--side` value (and an argparse prefix of `--side`, three letters or more, `=`-joined or not) is `user` or `system`; `PROD` matches no other later word. G2 now denies when `PROD.search(command) and not marked_read(command, s)`. Header line 20 gets `, but a marked db query (R511)`; 36-37 untouched; ROUTE text untouched.
- R1, `ops/desk/desk-launch.sh`, prompt kind, after the cwd checks and before `check_paths`/`run_launch`: when the one `RULINGS:` line holds ONE `<date> R<n>` (no comma), `( ruling_row … )` passes (one row, HIS RULING + APPROVED, committed and equal at HEAD), `git diff --quiet` on its `cto-<date>.md`, and the row holds `production read` (case-insensitive), the stamp is ` PROD-READ: <date> R<n>`, inserted right after `Read '<pfile>' and follow it exactly.`. A line already holding `PROD-READ:` is refused unless the stamp exists, `PROD-READ:` occurs once, and the line holds `follow it exactly.<stamp>` with no digit after it; then it is not stamped again. One line added to the header's prompt-kind refusals.
- A test fixture fault fixed at E3 (said here): the `row approved uncommitted` case committed the working-tree row through `desk.commit` (`add -A`); both NO_PROOF tests now commit the prompt alone for the two uncommitted cases (`proof_prompt`). It was green on BASE and red on the fix for that reason only.
- DevDocs line: neither script has a page under `docs/40 - DevDocs/cobalt/` (Grep `bare-guard|desk-launch` there → only `jobs/restarts.md`, which is not their page); no line written (`## RECORDS`).

Greens after the row: `uv run pytest -q -p no:cacheprovider tests/ops/test_bare_guard.py tests/ops/test_desk_launch_prechecks.py` → `698 passed, 15 warnings in 60.53s`; `uv run pytest -q -p no:cacheprovider tests/ops` → `1447 passed, 1 xfailed, 15 warnings in 370.49s (0:06:10)`.

THE MUTATIONS (each made with Edit, run alone, undone with Edit; `git diff --stat` back to `bare-guard.py | 37`, `desk-launch.sh | 34`, test `| 28` after each set). Guard runs: `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf -k g2 tests/ops/test_bare_guard.py`; launcher runs: `… -k test_r1_ tests/ops/test_desk_launch_prechecks.py`.

| mutation | summary | first failing line | goes red |
|---|---|---|---|
| drop the marker test | `9 failed, 60 passed, 512 deselected` | `test_g2_a_seat_without_the_marker_in_its_first_record_is_denied[brain-none]` | CONTROL (a), all 9 |
| drop the leading-shape test | `5 failed, 64 passed` | `…the_one_query_shape[COBALT_ENV=production uv run cobalt db migrate --prod]` | CONTROL (b) with `--prod`, dev-rebuild, two assignments, `NAME=x`, `env` |
| drop the `--side` test | `4 failed, 65 passed` | `…[… --prod --side admin "SELECT 1"]` | `--side admin`, `--side=admin`, `--side "SELECT 1"`, `--si admin` |
| drop the no-other-production-string test | `2 failed, 67 passed` | `…[… --prod --side user "SELECT cobalt_brain"]` | `cobalt_brain`, `'--prod'` in the query |
| drop the exactly-one-`--prod` test | `2 failed, 67 passed` | `…[… db query --side user "SELECT 1"]` | no `--prod`; CONTROL (f) two `--prod` |
| launcher: drop the row HIS RULING test (`ruling_row` 258-261 to `*APPROVED*`) | `2 failed, 25 passed, 90 deselected` | `test_r1_a_row_that_proves_nothing_stamps_nothing[row not HIS RULING]` | both `row not HIS RULING` cases |
| launcher: drop the `production read` test | `2 failed, 25 passed` | `…stamps_nothing[row names no production read]` | both `row names no production read` cases |
| launcher: drop the row committed test (`ruling_row` 262-264 and the new `git diff --quiet`) | `4 failed, 23 passed` | `…stamps_nothing[row uncommitted]` | `row uncommitted`, `row approved uncommitted`, each in both tests |
| launcher: drop the `PROD-READ:` refusal | `9 failed, 18 passed` | `test_r1_a_typed_marker_without_its_proving_row_is_refused[row uncommitted]` | RED (g), all 9 |
| launcher: drop the equality test | `4 failed, 23 passed` | `test_r1_a_typed_marker_other_than_the_stamp_is_refused[ PROD-READ: 2026-01-02 R3]` | CONTROL (h) R3, R21, no row number; the elsewhere-on-the-line test (the stamp-twice case is held by the once-count, so it stays green here) |

Said, per the card: CONTROL (b) as typed (`db migrate`, no `--prod`) stays green under the leading-shape mutation (the exactly-one test refuses it), so the control carries a second command `db migrate --prod`, which goes red. CONTROL (e) is G1's: no G2 mutation turns it red. A first undo of the no-other-string mutation did not apply (the Edit matched 18 `return True` lines and refused); the next run had two mutations live, so it was discarded, the undo made with a unique match, and the exactly-one mutation re-run alone (the row above).

## RESTARTS

`uv run cobalt jobs restarts 3c257bb9..HEAD` (tip `ce19a3fd`):

```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```

No UNCLASSIFIED row.

## W THE THREE SUITES

`<tip>` = `ce19a3fd`. DB: none.

- (a0) `git diff --name-only --no-renames 3c257bb9` → `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`: every path under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-1006 offline` → `offline 3932/0`; `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-1006-offline-20261006-074329.log`; exit 0. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its tests are in `tests/ops` (below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-1006 livenote` → `live-note 146/0`; `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-1006-livenote-20261006-075344.log`; its one SKIPPED line (`grep -n -F "SKIPPED" <log>`): `56: tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` — none names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1447 passed, 1 xfailed, 15 warnings in 369.28s (0:06:09)`.
- with-DB: not run (DB: none). (b)–(d), (f): not run. `ls /Users/cobalt/cobalt-wt/guard-g2-1006/.env` → `No such file or directory`.

Tests this build adds (`tests/ops/test_bare_guard.py`): `test_g2_a_marked_seat_runs_a_production_db_query` (9), `test_g2_a_seat_without_the_marker_in_its_first_record_is_denied` (9), `test_g2_a_marked_seat_is_denied_anything_but_the_one_query_shape` (17), `test_g2_a_marked_query_with_a_separator_is_g1s_to_deny` (3); (`tests/ops/test_desk_launch_prechecks.py`): `test_r1_a_proven_row_stamps_the_launch_line` (1), `test_r1_a_row_that_proves_nothing_stamps_nothing` (9), `test_r1_an_uncommitted_prompt_is_refused` (2), `test_r1_a_typed_marker_without_its_proving_row_is_refused` (9), `test_r1_a_typed_marker_with_its_proving_row_launches_stamped_once` (1), `test_r1_a_typed_marker_other_than_the_stamp_is_refused` (4), `test_r1_a_typed_marker_elsewhere_on_the_line_is_refused` (1).

## PRE-STOP SELF-CHECK

1. Every added test shown red for its reason: RED (c), (d), (g), (h), the elsewhere test and (e)'s deny text red on BASE (`## E2 RED`, 27 reds); CONTROL (a), (b), (f), the `--side`, no-other-string and the launcher's HIS RULING / production-read / committed / refusal / equality checks each red under their mutation (`## E3` table). Stayed green under every mutation: (d2) `test_r1_an_uncommitted_prompt_is_refused` (the card: `committed` is not a mutation, and it is green on BASE as the card says), (g2) the stamped-once control, the stamp-twice case of (h) (held by the once-count; the R3 / R21 / no-number cases of the same test go red), and (e) (G1's, per the card). No test was rewritten for staying green; one fixture was fixed for a wrong red (`## E3`).
2. Entry paths: `bash_rules` has one caller (`bare-guard.py:968` at BASE → `decide`), pinned by every guard test through the hook's stdin; `seat()` callers 968 and 976 (Write/Edit: the new key is unused there; the G5/G6 suite stays green, 581 passed); `marked_read` one caller (887). The launcher's stamp sits in the prompt kind only (other kinds untouched; `tests/ops` 1447 passed); its paths: no RULINGS line, `none`, a list, absent, uncommitted, approved-uncommitted, not HIS RULING, not APPROVED, no production read, typed with and without proof, typed for another row, typed twice, typed without a number, typed elsewhere, uncommitted / changed prompt — each a test. Seat kinds: brain, worker, desk marked; deploy and UNKNOWN unchanged (`test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed`, green).
3. Re-read at the tip `ce19a3fd`: `grep -n -F "marked_read" ops/desk/bare-guard.py` → 854, 887; `grep -n -F "\"first\": text"` → 745; `grep -n -F "PROD-READ" ops/desk/desk-launch.sh` → 111, 502, 504, 514, 520, 521, 522, 528; `git log --oneline 3c257bb9..HEAD` → the two commits below; `uv run cobalt jobs restarts` at the tip (`## RESTARTS`).

## FOR THE CHECK

- `3c257bb9..ce19a3fd`: `ff2d684a wip(guard-g2): red`; `ce19a3fd feat(guard-g2): G2 passes a launcher-stamped seat's one production db query (G2 R1 R2, L1 L3 L72)`.
- Reds, mutations, greens: `## E2 RED`, `## E3 THE ROWS`. Caller greps: `## PREFLIGHT`. RUN rows: none on this card.
- Suites: offline `3932/0` (`gate.sh … offline`), live-note `146/0` (`gate.sh … livenote`), `tests/ops` `1447 passed, 1 xfailed`; with-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT`, last paragraph.
- For X1: `marked_read` reads `words(command)`, the guard's own splitter (`$'…'` decoded, quotes removed). A quoted or escaped `COBALT_ENV=production` word reads as the assignment there but is a command name to the shell (no production run); `env`, `NAME=x`, a second assignment and a wrapper fail the leading shape (tests). For X2: the proof is `MARKER.search(s["first"])`, the first non-meta user record only (tests: later record, prompt body, forged RULINGS line and row). For X3 / X4: `## E3`, the R1 tests.

## CONTINUE

next: none (BUILT; the desk launches the check)

## DECISIONS

1. ASK DESK: R2 as written does not forbid `|`; a marked `db query` piped into a G1 read-only filter (`… "SELECT 1" | grep x`, `| head`) passes G2 and then G1. The card's fence says no row passes a pipe; R2's text (R517, L72) and CONTROL (e) say G1 judges `;` and `|`. UNPROVEN (L70): read from the code, no test runs this command. Default taken: R2 built as written; the command is still the read-only query. [08:00 from date]
2. ASK DESK: R1 stamps only a RULINGS line holding ONE `<date> R<n>`; a list (`R2, R1`) gets no stamp and launches as today (pinned by the `RULINGS a list` cases). The card reads "cites `<date> R<n>`" and "that RULINGS row"; a survey prompt citing several rows needs its production row alone on the line. Default taken: one item only (fails safe). [08:00 from date]

## RECORDS

- L74: a system reminder at 07:13 EDT asked for a `Claude-Session:` line on commits; recorded once (`## L74`), not acted on.
- `REFUSED, not needed: grep -n -F "requires --prod" src/cobalt/db_query.py — PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev` (G2 matches `--prod` in a grep pattern; the line was read with the Read tool instead).
- A `grep -n -F "run_launch \"$dir\""` returned nothing (a `$` in a double-quoted argument, against UNATTENDED RULES); re-read with the Grep tool.
- No DevDocs line: `bare-guard.py` and `desk-launch.sh` have no module page under `docs/40 - DevDocs/cobalt/` (as in `cobalt-guard-b-build-2026-10-04.md`).
- The card's records, as re-read at PREFLIGHT: `## PREFLIGHT`. R514 and R517 are not in `cto-2026-10-06.md` at BASE; the card quotes their rules.
- No lock taken; no `.env` at any step of this build.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: guard-g2 · tip: ce19a3fd | on 3c257bb9 | migration: none | offline 3932/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 273887
