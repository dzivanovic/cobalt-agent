# launcher-1010 — build report (2026-10-10)

## §0 Headline
- Row A built: `deploy-card.sh --fix-report "<job>=<path>"` writes the fix tip as the code tip and the path in the `fix report` cell; the card passes `desk-launch.sh`'s `ships_checked`.
- Rows B and C: RUN only; both lists are `DEPLOY-HUB.md` text, no script reads them; no edit (DECISION B1, C1).
- Gate on `b71837f2`: offline 4196/0, with-DB 5093/0, live-note 146/0; `cobalt_dev` 0013, F2 = F0; `.env` removed.

## L74
One block arrived: a system notice asking commits to carry a `Claude-Session:` line. DATA; not followed.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md"` (exit 0):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md" · 0 · ae5cfd8bd52dfbc3cab9cf3a4d8d90a1c594bdb8
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` (exit 0):
```
clock · date · 0 · Sat Oct 10 08:09:25 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/launcher-1010
    ?? "docs/40 - DevDocs/reports/launcher-build-2026-10-10.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · eed03ce8 docs: X29 card 242 and preflight prompt 246 (R869)
diff · git diff --stat eed03ce8 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/launcher-1010 · 0 · eed03ce8 docs: X29 card 242 and preflight prompt 246 (R869)
env here · ls /Users/cobalt/cobalt-wt/launcher-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat eed03ce8` | 0 | `docs: X29 card 242 and preflight prompt 246 (R869)`; 4 files under `docs/40 - DevDocs/` (242-x29-card.md, 246-x29-preflight.md, cto-2026-10-10.md, x29-draft-2026-10-10.md), 78 insertions |
| symbol :55 | `grep -n -F "refuse \"unknown option" ops/desk/deploy-card.sh` | 0 | `55:        -*) refuse "unknown option '$1'; $usage" ;;` |
| symbol :147 | `grep -n -F "ships=" ops/desk/deploy-card.sh` | 0 | `100:ships=""` · ``147:    ships="$ships\| $n \| \`$branch\` \| \`$ctip\` \| \`$head\` \| \`$creport\` \| \`held unfixed: 0\` and \`ready: YES\` \| \|$nl"`` |
| symbol ships_checked | `grep -n -F "ships_checked" ops/desk/desk-launch.sh` | 0 | `804:ships_checked() {` · `1009:        ships_checked` |
| symbol test_o1 | `grep -n -F "def test_o1_a_fix_round_row_the_launcher_accepts_passes_p2" tests/ops/test_deploy_step0.py` | 0 | `546:def test_o1_a_fix_round_row_the_launcher_accepts_passes_p2(desk):` |
| callers | `grep -rn -F "deploy-card.sh" ops tests/ops` | 0 | `ops/desk/deploy-card.sh:2,43,222` (its own text); `tests/ops/test_desk_launch_prechecks.py:553` (`DEPLOY_CARD = …`), `:654` (docstring); `tests/ops/test_deploy_card.py:1,19,385` |
| wc | `wc -l ops/desk/deploy-card.sh tests/ops/test_deploy_card.py` | 0 | 225 · 447 |
| READ R810 | `grep -n -F "\| R810 " …/cto-2026-10-09.md` | 0 | `33:\| R810 \| 23:39 ET \| DESK RECORD (brain, L79): 156 deploys on the fix-round SHIPS row (CARD.md :48, K3 precedent), card by a drafter; follow-up row \`deploy-card.sh --fix-report\` goes to the launcher card. …` |
| READ R828 | `grep -n -F "\| R828 " …/cto-2026-10-10.md` | 0 | `52:\| R828 \| 03:40 ET \| DESK RECORD (brain, L79): … \`.bak\` stays his; D0 list row on the launcher card. …` |
| READ CARD.md | `grep -n -F "fix report" …/prompts/CARD.md` | 0 | `45:` the SHIPS header with `fix report`; `48:` "… On a fix-round row … the literals … are read from the CHECK report's last line, and `tip: <code tip>` is read from the fix report's `BUILT ·` stop line. … The `fix report` cell … is empty on a row with no fix round." |
| RESTARTS | `uv run cobalt jobs restarts eed03ce8..HEAD` | 0 | one row: `docs/40 - DevDocs/reports/launcher-build-2026-10-10.md A DOCS -` (the untracked report); `RESTARTS: none` |

Card records copied: RESTARTS none (`ops/desk/` → operator script; `tests/` → test/documentation); row A's current behaviour (`:55` refuses unknown, `:147` ends `| |`, tip from `:138`) — re-read above at `:55` and `:147`; rows B and C: the accepted list is `DEPLOY-HUB.md:113`, no `ops/desk/` script reads it — re-read at E2 (RUN rows); tests in `tests/ops/` run offline on fake repos.

Card header carries no `DB:` key, so W runs the full gate (`all --deploy`).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 722.22s (0:12:02)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.06s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (none names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Row A, `tests/ops/test_deploy_card.py`, on BASE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py -k "fix_report or fix_tip or no_fix_report"` → `7 failed, 1 passed, 34 deselected`. Every red's first line: `REFUSED: unknown option '--fix-report'; usage: …` (the row's reason):
- `test_a_fix_report_fills_the_ships_row_cell_and_code_tip` — `assert 1 == 0`, stderr `REFUSED: unknown option '--fix-report'`
- `test_a_fix_report_absent_at_the_head_is_refused`, `test_a_fix_report_whose_last_line_is_not_built_is_refused`, `test_a_fix_tip_not_past_the_check_tip_is_refused`, `test_a_fix_report_for_an_unknown_job_is_refused`, `test_a_fix_report_outside_the_reports_folder_is_refused` — `assert 'REFUSED: <reason>' in 'REFUSED: unknown option \'--fix-report\'; …'`
- `test_a_fix_report_round_trips_through_the_launchers_ships_checked` — `assert 1 == 0`, stderr `REFUSED: unknown option '--fix-report'`
- `test_no_fix_report_leaves_every_cell_empty` PASSED (the guard, green on BASE).
Commit `d2d79b19 wip(launcher-1010): red`. No with-DB red (card: no with-DB test).

RUN row B: `grep -rn "held" ops/desk/deploy-step0.sh ops/desk/desk-launch.sh ops/desk/authorize.sh` →
```
ops/desk/deploy-step0.sh:24:#   P2 check <n>         the ship's check report: its last non-blank line carries `held unfixed: 0`,
ops/desk/deploy-step0.sh:27:#                        neither starts `(run in progress` nor `FAILED`. A held defect carried by a
ops/desk/deploy-step0.sh:340:    lits=$(printf 'held unfixed: 0\nready: YES\n%s\n' "$lits")
ops/desk/desk-launch.sh:132:#   - a deploy while the cobalt_dev lock is held: any /Users/cobalt/cobalt-wt/*/.env, or the lock
ops/desk/desk-launch.sh:139:#     the cobalt_dev lock held (any worktree's .env, or the lock directory); a worktree on
ops/desk/desk-launch.sh:789:        [ ! -e "$f" ] || refuse "with-DB launch refused: the cobalt_dev lock is held ($f) (L76)"
ops/desk/desk-launch.sh:799:    refuse "with-DB launch refused: the cobalt_dev lock is held by ${holder:-unknown} ($WT/.cobalt_dev.lock) (L76)"
ops/desk/desk-launch.sh:912:    # a build launches while the lock is held (R20); a resume still refuses another worktree's .env
ops/desk/desk-launch.sh:969:    # a check launches while the lock is held (R20); a resume still refuses another worktree's .env
```
`grep -n "held" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → lines `8`, `32`, `41`, `50`, `58`, `101`, `109`, `175`. The held-item rule is `:32` ("A row of his is needed for two things only: a CARRIED HELD DEFECT — a `## SHIPS` row whose check line is not clean ships only on a row of `RULINGS` that rules it carried (P2) — and a SCHEMA ROLLBACK …") and `:58` (P2: "a line that carries a held defect ships only when a row of `RULINGS` rules it carried (name it)"). `grep -rn "named fixed\|accept" ops/desk/` → `desk-launch.sh:105`, `install-fixed.sh:8`, `bare-guard.py:1086`, `house-probe.sh:18`, `house-probe.sh:67`; none a held-item list. No script under `ops/desk/` holds a list of held items named fixed; no edit → `DECISION B1`.

RUN row C: `grep -rn "rules.yaml\|settings.json" ops/desk/` → `ops/desk/stop-guard.py:42:# in user settings ~/.claude/settings.json (not main's tracked .claude/settings.json), pasted` (a comment about another file). The ACCEPTED list is `DEPLOY-HUB.md:113` ("ACCEPTED: ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`"); `deploy-step0.sh:515-518` records `git status --short --branch` and counts `$dirty` with gate value `0` (recorded, never a gate). No script reads the list; no edit → `DECISION C1`.

## E3 THE ROWS
Row A, `ops/desk/deploy-card.sh` (re-read `:43-58`, `:106-164`, `:147` before the edit): the repeatable option `--fix-report "<job>=<path>"` (parsed with the other options; a line break refused); each entry checked before any git read (`<job>` `[a-z0-9-]`, named once, path `"$REPORTS"/*.md` with no `..`); per card, when its JOB has an entry: the report read at the branch head (`git show <head>:<rel>`), its last non-blank line must start `BUILT ·` and carry `tip: <8-40 hex>`, the check's tip must be an ancestor of the fix tip; the fix tip becomes the row's code tip, so the existing `:142-144` rules (code tip ancestor of the head; nothing outside `docs/` past it) read against the fix tip; the row's last cell is the backticked path and `## RECORDS` gains `- <job>: fix report … at <head> last line: …`. After the cards: a `--fix-report` job no card names is refused. A row with no entry: `$fixcell` empty, so `:147` writes `| |` as before.

Two tests rewritten after their first green run (test faults, not the script's): `test_a_fix_report_for_an_unknown_job_is_refused` (its alpha fix round tripped the head rule first; now alpha and beta stay clean and `gamma` names a path under reports) and the round trip (the alpha card's `## DEPLOY PROOF` gained a smoke-read line so the card carries no «FILL). Both still use `--fix-report`, so both stay RED on BASE for the row's reason.

Greens: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py` → `42 passed, 15 warnings in 13.21s`. The test files beside it, before the rewrite: `tests/ops/test_deploy_card.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py` → `2 failed, 212 passed` (the two rewritten tests; every other test of the three files green).

MUTATIONS (Edit tool, undone with Edit tool; `git diff --stat` after → `ops/desk/deploy-card.sh | 66`, `tests/ops/test_deploy_card.py | 8`, the fix):
- M1 `if [ -n "$frep" ]; then` → `if false; then` (the fix undone): `5 failed, 3 passed` — fills, absent, not-BUILT, not-past, round trip red, first line `REFUSED: alpha: the head … adds paths outside docs/ past the code tip …: src/alpha.py`; the three passing are the unknown-job and outside-reports tests (separate checks, M2/M3) and the guard.
- M2 the unknown-job case made always-match: `test_a_fix_report_for_an_unknown_job_is_refused` → `1 failed` — `assert 0 == 1`, `deploy-card: … written (2 job(s), …)`.
- M3 the `"$REPORTS"/*.md` case swapped to refuse only inside reports: `test_a_fix_report_outside_the_reports_folder_is_refused` → `1 failed` — `REFUSED: alpha: the fix report is absent at the branch head …`.
- M4 the check-tip ancestor refusal → `true`: `test_a_fix_tip_not_past_the_check_tip_is_refused` → `1 failed` — `REFUSED: alpha: the head 2b30c791 adds paths outside docs/ past the code tip 49bb9336: src/alpha.py`.
Commit `e046c2ac feat(launcher-1010): deploy-card.sh --fix-report fills the fix-round SHIPS row (A, L75 L1)`.

Rows B and C: RUN rows, read only; no edit (above).

## RESTARTS
`uv run cobalt jobs restarts eed03ce8..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/reports/launcher-build-2026-10-10.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row. Re-run at `b71837f2` (after the second commit): the same three rows, `RESTARTS: none`.

## W THE THREE SUITES
`<FP>` (typed by `gate.sh` from `ops/desk/gate-lists.md`; the BUILD-HUB text): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

THE GATE on `<tip>` = `b71837f2` (the second gate call; the first, on `e046c2ac`, is under `## RECORDS`): `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-1010 all --deploy` (no `--deselect`, no `--tickers`, no `--migration`), exit 0. Verdict lines WHOLE:
```
offline 4196/0
lock: waited 52 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-1010-all-20261010-090852.log
```
No line marked `OUTSIDE the allowed set`. From the log (`grep -n -F`): `944:code: b71837f2 (DIRTY: 1 path(s))` (the uncommitted report) · `896:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `1110:dev forward: APPLIED 10:25:43` (the existing migrations above `0013`; this build adds none) · `1188:F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` · `2030:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0. Pass 1, executed (log `:952`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect …` (the gate-lists PASS 1 deselects, none added by this build; the full line is in the log at `:952`). This build adds no with-DB test, so no `PASSED <id>` line is owed at pass 2.
`ls /Users/cobalt/cobalt-wt/launcher-1010/.env` → `No such file or directory`. `.env: removed, proven gone (W)`.
`tests/ops` (not in the gate's lists): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` at `e046c2ac` → `2709 passed, 1 xfailed, 15 warnings in 505.09s`; the three row files at `b71837f2` → `220 passed, 15 warnings in 92.42s`.

## PRE-STOP SELF-CHECK
(1) Every added test shown RED for its named reason: the seven `--fix-report` tests red on BASE with `REFUSED: unknown option '--fix-report'` (E2); the guard `test_no_fix_report_leaves_every_cell_empty` green on BASE and after (a negative control, its row says so). Under mutation: M1 → fills / absent / not-BUILT / not-past / round trip red; M2 → unknown job red; M3 → outside reports red; M4 → not-past red with its own reason gone; M5 (the shape loop skipped) → the four shape cases and `test_a_fix_report_naming_one_job_twice_is_refused` red; M6 (line-break refusal dropped) → the line-break case red (`REFUSED: alpha: the fix report is absent …`). All quoted in E3 / below.
(2) Every entry path pinned: the callers `grep -rn -F "deploy-card.sh" ops tests/ops` → the script itself and `tests/ops/test_desk_launch_prechecks.py:553` (`test_f1_deploy_card_writes_the_fix_report_column_and_its_empty_cell`, green in the 220 run: the no-fix row keeps `| |`). Flag combinations: a fix on one job beside a job with none (fills test asserts beta's empty cell); one card with a fix (round trip); no `--fix-report` (guard); the same job twice; a value with no `=`, an upper-case job, `..`, a line break, a non-`.md` path; an unknown job; a path outside reports; a report absent at the head; a non-BUILT last line; a tip not past the check's. The gap found here (the shape refusals unpinned) was pinned in `b71837f2` and the gate run again.
(3) Re-read at the tip: `grep -n -F "fixcell" ops/desk/deploy-card.sh` → `177`, `189`, `197`; `grep -n -F "def test_a_fix" tests/ops/test_deploy_card.py` → `468`, `509`, `516`, `523`, `531`, `537`, `545` (before the second commit; the two new tests sit above the round trip); `git log --oneline eed03ce8..HEAD`; the gate log values above by `grep -n -F` on the second log.

## FOR THE CHECK
- Range `eed03ce8..b71837f2`: `d2d79b19 wip(launcher-1010): red` · `e046c2ac feat(launcher-1010): deploy-card.sh --fix-report fills the fix-round SHIPS row (A, L75 L1)` · `b71837f2 fix(launcher-1010): pin the --fix-report shape refusals (A, self-check 2)`.
- Row A: reds, mutations and greens in E2 / E3 / PRE-STOP SELF-CHECK. M5: `5 failed, 1 passed` (the one passing is the line-break case, refused at option parse before the loop); first lines `deploy-card: … written (2 job(s), …)` / `REFUSED: alpha: the fix report is absent at the branch head …`. M6: `1 failed, 3 passed` (`-k line`). After every mutation the Edit was undone; `git diff --stat` before the second commit → `tests/ops/test_deploy_card.py | 19` only.
- X1: the guard test asserts both no-fix rows equal the `:147` string byte for byte; the card text block (`:199-222` at BASE) is unchanged in the diff.
- X2: every refusal test goes through `_fix_refused`: exit 1, `REFUSED: <reason>` on stderr, `desk.out` absent, `desk.state()` (status, refs, worktrees, branches, head) unchanged.
- X3: `test_a_fix_report_round_trips_through_the_launchers_ships_checked` runs `desk-launch.sh deploy <card>` with `DESK_LAUNCH_DRY=1` on the written card (real DEPLOY-HUB.md committed in the tmp repo): exit 0, no `REFUSED`, the dry `worktree add` line printed — `ships_checked` ran (`:1009`, a first launch) and passed `fixed_ok`.
- X4: rows B and C quoted in E2; no edit outside `ops/desk/deploy-card.sh` and `tests/ops/test_deploy_card.py` (`git diff --name-only eed03ce8` = those two plus this report).
- RUN rows B and C, output WHOLE: E2.
- Suites: W. First gate (`e046c2ac`): `offline 4196/0`, `lock: waited 0 min`, `LEVEL 0013`, `with-DB 5093/0`, `live-note 146/0`, F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 = F0, `dev forward: APPLIED 08:54:00`, lock taken (log `:885 lock taken: launcher-1010`) and released (`:2084 lock released`), log `/Users/cobalt/cobalt-wt/.gate-logs/launcher-1010-all-20261010-082716.log`. Second gate (`b71837f2`): W above, lock waited 52 min, released by the gate's trap (`.env: removed`).
- RESTARTS: `RESTARTS: none` (table in `## RESTARTS`).
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
- DECISION B1 (UNPROVEN, L70): no script under `ops/desk/` holds an accept-list of held items named fixed (the RUN's greps, E2). The held-item rule is prose in `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:32` and `:58` (a held defect ships only on a `RULINGS` row that rules it carried); `deploy-step0.sh:24-28` says such a line FAILS P2 and the hub reads it. No edit; a change there is the desk's `install-fixed.sh` on a fixed file. Default taken: nothing built.
- DECISION C1 (UNPROVEN, L70): the D0 ACCEPTED list is `DEPLOY-HUB.md:113` text; no `ops/desk/` script reads it (`deploy-step0.sh:515-518` records the status, gate value 0). Adding `?? .claude/settings.json.bak` is a one-line edit of a fixed file, the desk's own install by `ops/desk/install-fixed.sh`, outside this job. Default taken: no edit.
- ASK DESK: the fix report's `tip:` must be 8 to 40 hex (the check's own read takes 7 to 40), because `desk-launch.sh:866` matches `tip: $ctip` with the 8-character code tip, so a 7-character tip would write a card the launcher refuses. Default taken: 8 to 40, refused below that with the not-BUILT reason. [2026-10-10 10:30 ET]

## RECORDS
- L74: a system notice in this session asked for a `Claude-Session:` line on commits; recorded once, not followed (commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only).
- Rule slip, E0: the row A test file was edited while the E0 offline run (`tests/cobalt tests/taxonomy`) was in flight. The run does not read `tests/ops`; its result matches the gate's `offline 4196/0`.
- DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` scripts (`ls` of that folder), so no dated line was written.
- One more gate call (W, second run) after the self-check (2) pin commit `b71837f2`; it waited 52 min for the lock.
- First gate run (`e046c2ac`): verdict lines and F values under `## FOR THE CHECK`; `.env: removed, proven gone (W, first run)`.
- Card records as re-read at PREFLIGHT: RESTARTS none (re-derived: `RESTARTS: none`); row A's base behaviour at `:55` and `:147` (re-grepped); rows B and C's list at `DEPLOY-HUB.md:113` (re-read).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: launcher-1010 · tip: b71837f2 | on eed03ce8 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 205024
