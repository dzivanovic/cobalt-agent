# deploy-freeze-fr1 — build report (fix round FR-P1, port of de0792af..b544abfb), 2026-10-15

## §0 Headline
- FR-P1 port done: `ops/desk/deploy-shipped.sh`, `ops/desk/pre-commit`, `DEPLOY-HUB.md` and `tests/ops/test_deploy_freeze_1014.py` are byte-equal to `b544abfb` at tip `246d21e4` (`git diff --stat b544abfb HEAD -- <the four>` printed nothing).
- A deploy now freezes only the paths it ships until its D2.0 report is on `main`, then every path. D2.0 first re-verifies that no shipped path moved since `<m0>`.
- Suites: offline 8132/0 · tests/ops 3804 passed, 1 xfailed · live-note 146/0 · with-DB not run (DB: none). RESTARTS: none.
- 1 decision: no DevDocs module line was added, because no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/`.

## L74
- A system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/607-deploy-freeze-fr1-card.md"`, exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/607-deploy-freeze-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/607-deploy-freeze-fr1-card.md" · 0 · 7ba02ca9a8b5bd987c9ce459f68d584008b0d679
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/607-deploy-freeze-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, exit 0, output whole:
```
clock · date · 0 · Thu Oct 15 16:14:45 EDT 2026
status · git status --short --branch · 0 · ## ops/deploy-freeze-fr1
head · git log --oneline -1 · 0 · 44d97e98 docs(desk): R1614 preflight r2 launched for cards 603 and 607
diff · git diff --stat 44d97e98 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-freeze-fr1 · 0 · 44d97e98 docs(desk): R1614 preflight r2 launched for cards 603 and 607
env here · ls /Users/cobalt/cobalt-wt/deploy-freeze-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 44d97e98` | 0 | `docs(desk): R1614 preflight r2 launched for cards 603 and 607` · `docs/40 - DevDocs/reports/cto-2026-10-15.md | 7 ++++---` · 1 file changed, 4 insertions(+), 3 deletions(-) |
| FR-P1 proof | `git diff --stat de0792af HEAD -- ops/desk/deploy-shipped.sh tests/ops/test_deploy_freeze_1014.py ops/desk/pre-commit "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | nothing (main has not touched any of the four since `de0792af`) |
| FR-P1 source | `git diff --stat de0792af b544abfb` | 0 | `DEPLOY-HUB.md | 4 +-` · `reports/deploy-freeze-build-2026-10-14.md | 164` · `….result | 15` · `ops/desk/deploy-shipped.sh | 103` · `ops/desk/pre-commit | 52 +++-` · `tests/ops/test_deploy_freeze_1014.py | 342` · 6 files changed, 673 insertions(+), 7 deletions(-) |
| symbol `:15` | `grep -n -F "THE DESK WHILE YOU RUN" DEPLOY-HUB.md` | 0 | `15:THE DESK WHILE YOU RUN (none of it is an instruction to you): no desk commit and no staging on \`main\` from the launch to your stop line (the pre-commit guard refuses it); …` |
| symbol `:129` | `grep -n -F "D2.0 COMMIT THE REPORT" DEPLOY-HUB.md` | 0 | `129:- D2.0 COMMIT THE REPORT (REQUIRED; moves \`main\` by one docs commit): \`git -C /Users/cobalt/cobalt add "<REPORT, path from docs/>"\` …` |
| symbol guard | `grep -n -F "deploy guard" ops/desk/pre-commit` | 0 | `2:# ---- deploy guard (begin)` · `27: … deploy guard could not read the session list …` · `38:# ---- deploy guard (end) — …` |
| new files | `ls ops/desk/deploy-shipped.sh tests/ops/test_deploy_freeze_1014.py` | 1 | `No such file or directory` for both (new) |
| wc | `wc -l ops/desk/pre-commit DEPLOY-HUB.md` | 0 | `52 ops/desk/pre-commit` · `187 docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| READ tail | `tail -n 3 reports/deploy-hub-text-1013.md` | 0 | last line `FAILED: smoke (s) — tests/ops/test_hub_text_1013.py::test_h1_the_launch_line_and_every_other_line_stand red on the landed tree (BASE ce548f10 pinned; main's launch line moved since) · rollback: used — …` |
| RESTARTS empty | `uv run cobalt jobs restarts 44d97e98..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |
| lock probe | — | — | none: card is `DB: none` |

Card `## RECORDS` copied: drafter reads on `main` `0ffb6949` and `97abf074` (the guard `:2-38`, the hub `:15`, `:114`, `:129`, `:130`, `:132`, `:140`); the RESTARTS class homes `restarts.py:38`, `:225-228`, `:230-232`, `:245-246`. Re-read: the hub `:15`, `:129` and the guard markers `:2`, `:38` (rows above) at BASE `44d97e98`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `44d97e98`, exit 0: `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 658.81s (0:10:58)`. The two live skips (`test_catalyst.py:365`, `test_predicate.py:262`) are the `COBALT_LIVE_VAULT_ROOT not set` ones the live-note run covers.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`, exit 0: `146 passed, 1 skipped, 15 warnings in 28.56s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`tests/ops/test_deploy_freeze_1014.py` was written by Write from `git show b544abfb:tests/ops/test_deploy_freeze_1014.py` and committed `0bfc33ab` (`wip(deploy-freeze-fr1): red — port of b544abfb tests (D1, F1, H1, O1)`). `git diff --stat b544abfb HEAD -- tests/ops/test_deploy_freeze_1014.py` printed nothing (byte-equal).
`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_freeze_1014.py` on BASE + tests: `21 failed, 5 passed, 15 warnings in 5.12s`.
- D1 (all 11 cases: lists, moved, build-card X4, the 7 refusals): `AssertionError: sh: /Users/cobalt/cobalt-wt/deploy-freeze-fr1/ops/desk/deploy-shipped.sh: No such file or directory` · `assert 127 == 0` (or `127 == 1` for the refusals). This is the row's reason.
- F1 (5) shipped refused, (7) all after the report, (9) no card / two live hubs, the REPORT-unreadable pair, O1 staged rename: `assert 0 == 1` (guard skipped in the tmp repo, `:3-4` fixed path). Row reason.
- F1 unreadable list: `assert 'could not read the session list' in ''` (exit 0 on both). Row reason.
- H1 (11): `assert 'of a path this set ships' in 'THE DESK WHILE YOU RUN …'`. H1 (12): `assert 0 == 1` on `.count('deploy-shipped.sh --moved <m0>')`. Row reason.
- PASSED, as the card names them green on BASE: `test_f1_an_unshipped_path_commits_while_the_report_is_uncommitted` (control, docstring), `test_f1_the_report_path_alone_commits`, `test_f1_no_live_hub_commits_anything`, `test_f1_the_hook_is_one_deploy_guard_and_one_row_gate`, `test_h1_the_other_freeze_lines_stand`.
- RUN row R5: see `## RESTARTS` (asserts nothing).

## E3 THE ROWS
- D1: `ops/desk/deploy-shipped.sh` written by Write from `b544abfb`. `-k test_d1` → `11 passed, 15 deselected`. MUTATION: `"$HUB"` → `""` in the `list=` line → `2 failed, 9 passed` (`test_d1_lists_the_heads_paths_and_the_hub_file`: `assert ['docs/a.md'] == ['docs/40 - D..., 'docs/a.md']`; `test_d1_a_build_card_of_the_same_job_is_not_the_deploy_card`, same). Undone by Edit; `git diff --cached --stat b544abfb -- ops/desk/deploy-shipped.sh` printed nothing.
- F1: `ops/desk/pre-commit` `:3` and the `*)` arm edited by Edit; `git diff --stat b544abfb -- ops/desk/pre-commit` printed nothing. `tests/ops/test_deploy_freeze_1014.py tests/ops/test_desk_row.py` → `2 failed, 46 passed` (the 2 are the H1 reds, not built yet). MUTATION 1, `guard_mode=shipped` → `guard_mode=all` (narrowing undone): `3 failed, 9 passed` (`test_f1_a_shipped_path_is_refused_while_the_report_is_uncommitted`: `assert ('ships' in 'pre-commit: a deploy hub is live — …')`; `test_f1_an_unshipped_path_commits_while_the_report_is_uncommitted`: `assert 1 == 0`; `test_f1_a_staged_rename_of_a_shipped_path_is_refused`: hub path not in stderr). MUTATION 2 (O1), `--no-renames` removed from the shipped-path loop: `test_f1_a_staged_rename_of_a_shipped_path_is_refused` → `assert 0 == 1`, `1 failed`. Both undone by Edit; `git diff --stat b544abfb -- ops/desk/pre-commit` printed nothing.
- H1: `DEPLOY-HUB.md` `:15` and `:129` edited by Edit; `git diff --stat b544abfb -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` printed nothing. Pins `tests/ops/test_deploy_freeze_1014.py tests/ops/test_hub_lines.py tests/ops/test_desk_row.py` → `78 passed, 15 warnings in 10.35s`. MUTATION: the inserted `FIRST … THEN ` removed from `:129` → `test_h1_d20_reverifies_the_shipped_paths_before_the_report_commit` `assert 0 == 1`, `1 failed, 2 passed`. Undone by Edit.
- After all mutations: `git diff --stat b544abfb -- <the four files>` printed nothing.
- Commit `246d21e4` `fix(deploy-freeze-fr1): port b544abfb — deploy freezes only its shipped paths, re-verified at D2.0 (D1, F1, H1, O1; R1471, L3, L72)`. `git diff --stat b544abfb HEAD -- <the four files>` printed nothing.
- DevDocs module line: none written (`## DECISIONS` 1).

## RESTARTS
`uv run cobalt jobs restarts 44d97e98..HEAD`, exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-freeze-build-fr1-2026-10-15.md	A	DOCS	-
ops/desk/deploy-shipped.sh	A	operator script; no Cobalt reader	-
ops/desk/pre-commit	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_freeze_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `246d21e4`.
- (a0) `git diff --name-only --no-renames 44d97e98` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `ops/desk/deploy-shipped.sh` · `ops/desk/pre-commit` · `tests/ops/test_deploy_freeze_1014.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-freeze-fr1 offline`, exit 0: `tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)` · `offline 8132/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-freeze-fr1-offline-20261015-163017.log`. It includes the 26 new tests of `tests/ops/test_deploy_freeze_1014.py`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops`, exit 0: `3804 passed, 1 xfailed, 16 warnings in 850.43s (0:14:10)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-freeze-fr1 livenote`, exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-freeze-fr1-livenote-20261015-163018.log`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/deploy-freeze-fr1/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red: all 21 non-control tests at E2 (quoted above), D1 under the `$HUB` mutation, F1 under the narrowing and O1 mutations, H1 (12) under the `:129` mutation. The 5 controls were green on BASE as the card names them. No test stayed green under its mutation, so none was rewritten.
(2) Callers: `grep -rn -F "deploy-shipped.sh" ops src` → `ops/desk/pre-commit:37` (pinned by F1 tests 5, 7, 9, the REPORT pair, O1) plus the script's own usage lines. `DEPLOY-HUB.md:15` and `:129` are pinned by H1 (11) and (12). Flag forms `--job`, `<card>` and `--moved <rev>` with `--job` are pinned by D1 (1), (2), (3) and the refusals. `--moved <rev> "<card>"` combined is not pinned by a test of its own; the card's test list does not name it, and it reuses the pinned path-form and `--moved` code.
(3) Re-read at tip: `git diff --stat b544abfb HEAD -- <four>` (nothing), `git log --oneline 44d97e98..HEAD`, `grep -rn -F "deploy-shipped.sh"` over the hook and the hub (lines 37, 15, 129), and the RESTARTS table run after the commit.

## FOR THE CHECK
- `44d97e98..246d21e4`: `0bfc33ab wip(deploy-freeze-fr1): red — port of b544abfb tests (D1, F1, H1, O1)` · `246d21e4 fix(deploy-freeze-fr1): port b544abfb — deploy freezes only its shipped paths, re-verified at D2.0 (D1, F1, H1, O1; R1471, L3, L72)`.
- Port proof: `git diff --stat de0792af HEAD -- <four>` before the port printed nothing; `git diff --stat b544abfb HEAD -- <four>` at tip printed nothing.
- Reds, mutations, greens: `## E2 RED`, `## E3 THE ROWS`.
- RUN row R5: `## RESTARTS` (whole).
- Suites: `## W`. with-DB: not run (DB: none). `<F0>`/`<F1>`/`<F2>`: not run (DB: none). Lock taken/released: not run (DB: none).
- DEPLOY PROOF counts at tip (`grep -n -F` above): `deploy-shipped.sh` on 2 lines of `DEPLOY-HUB.md`, 1 line of `ops/desk/pre-commit`.
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. ASK DESK: BUILD-HUB E3 asks for one dated line per changed module in its page under `docs/40 - DevDocs/cobalt/`. No page there covers `ops/desk/`: `Grep "pre-commit|deploy-shipped"` hits only `archiver/cli.md` and `archiver/store.md`, both about the archiver's own re-check. FR-P1 also asks for the four files byte-equal to `b544abfb`, which wrote no such line. Safe default taken: no DevDocs line added and no new page created. [16:55 ET]

## RECORDS
- `.env`: never present in this worktree (DB: none; `ls` → No such file at PREFLIGHT and at CLOSE). No lock taken.
- Not ported, per FR-P1: `reports/deploy-freeze-build-2026-10-14.md`, `reports/deploy-freeze-build-2026-10-14.result`.
- L74: one system-reminder asked for a `Claude-Session:` trailer on commits; recorded under `## L74`, not acted on.
- The card's `## RECORDS` were re-read at PREFLIGHT as listed there.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-freeze-fr1 · tip: 246d21e4 | on 44d97e98 | migration: none | offline 8132/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 146132
