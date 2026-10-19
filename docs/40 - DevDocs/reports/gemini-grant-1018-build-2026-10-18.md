# gemini-grant-1018 — build report (card 800)

## §0 Headline
- `desk-launch.sh shadow … --model gemini-4-argon-high` now adds `write_file(<WT>/<wt>/)` to the agy settings on the real path only, and its EXIT trap removes it when the launch fails. A new kind, `grant-sweep`, removes the rules of gate seats that are gone and keeps live ones.
- One Gemini build at a time: another worktree's rule with a live gate refuses the launch, and an orphan rule is removed first. SHADOW-HUB.md lines 12 and 28 now say the launcher does this.
- Tip `fd9f0cb6` on `c0ebb874`. Offline 8678/0, live-note 147/0, with-DB not run (DB: none). RESTARTS: none. Two desk questions are under DECISIONS.

## L74
- One system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded here as data, per BUILD-HUB L74. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md" · 0 · 3b0723546e445b0d5416e134e9e86693b7faa4ea
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1942 row · grep -n "^| R1942 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 30:| R1942 | 20:47 ET | HIS RULING · APPROVED (relayed by the brain 20:46, L79): "A for gemini" — a K5 card in which desk-launch.sh shadow adds and removes the one write_file rule in the agy settings.json; NEEDS HIS HAND entry closed. | APPLIED: areas/cobalt.md NOW at wake-up 01:57 |
RULING 2026-10-18 R1942 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1942 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 55d8b50e607b5d4eb1b86354e336323252aec34c
RULING 2026-10-18 R1942 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 19 02:58:00 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/gemini-grant-1018
    ?? "docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · c0ebb874 docs(desk): preflight prompt 807, 806 cos-outage-attempt2 deployed
diff · git diff --stat c0ebb874 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/gemini-grant-1018 · 0 · c0ebb874 docs(desk): preflight prompt 807, 806 cos-outage-attempt2 deployed
env here · ls /Users/cobalt/cobalt-wt/gemini-grant-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat c0ebb874` | 0 | `docs(desk): preflight prompt 807, 806 cos-outage-attempt2 deployed`; `.../prompts/2026-10-19/807-f20-credtest-preflight.md` 9+, `docs/40 - DevDocs/reports/cto-2026-10-19.md` 11 +/-; 2 files changed, 16 insertions(+), 4 deletions(-) |
| symbol | `grep -n -F "holds no allow rule" ops/desk/desk-launch.sh` | 0 | `1759:            [ "$ngrant" -eq 1 ] \|\| refuse "shadow: gemini: ${AGY} holds no allow rule \"write_file(${grant})\" (SHADOW-HUB GRANT)"` |
| symbol | `grep -n -F "run_launch" ops/desk/desk-launch.sh` | 0 | 266, 269 (def), 481, 548, 569, 749, 821, 827, 921, 2397, 2443 |
| symbol | `grep -n -F "COBALT_AGY_SETTINGS" ops/desk/desk-launch.sh` | 0 | `216:` (comment), `1755:            AGY=${COBALT_AGY_SETTINGS:-/Users/cobalt/.gemini/antigravity-cli/settings.json}` |
| symbol | `grep -n -F "trap" ops/desk/desk-launch.sh` | 0 | `1564:` and `1636:` (the word "bootstrap"; no `trap` command): the launcher holds no trap, as `## RECORDS` says |
| symbol | `grep -n -F "antigravity-cli/settings.json" SHADOW-HUB.md` | 0 | `28:` only (the `- Gemini:` line); `:12` names "agy settings" (Read, line 12) |
| read | Read `desk-launch.sh` 200-419, 900-1079, 1690-1799, 2310-2443; tests `test_desk_launch_shadow.py` whole, `test_shadow_hub_file.py` 1-60 and 360-413 | — | the card's places found by content: the gemini block 1752-1787, the dry run 2395-2398, the agents read 2407-2420, the worktree add 2435-2442, the launch 2443, install-ops 929, the usage 358 |
| wc | `wc -l` of the four row files | 0 | 2443 desk-launch.sh, 472 test_desk_launch_shadow.py, 413 test_shadow_hub_file.py, 116 SHADOW-HUB.md |
| RESTARTS empty | `uv run cobalt jobs restarts c0ebb874..HEAD` | 0 | one row, the untracked report (`A DOCS -`); `RESTARTS: none` |
| P0 (a) | `grep -c -F "write_file(/Users/cobalt/cobalt-wt/strike-fallback-env-1018-gemini/)" /Users/cobalt/.gemini/antigravity-cli/settings.json` | 1 | `0` |
| P0 (b) | `grep -n -F "\"allow\"" /Users/cobalt/.gemini/antigravity-cli/settings.json` | 0 | `5:    "allow": [` |
| P0 (c) | `DESK_LAUNCH_DRY=1 sh ops/desk/desk-launch.sh shadow "<717 card>" --model gemini-4-argon-high` | — | REFUSED by the permission mode: `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` The `DESK_LAUNCH_DRY=1` prefix is on no listed string. DECISION 1 |

The card's records were copied here and re-read where the list allows: (a) and (b) are re-read above and match `## RECORDS`. The line numbers re-read from the worktree at BASE match the card. The card's drafting base (`55d8b50e`) differs from BASE `c0ebb874`, but the four row files' places are where the card puts them. A GEMINI RULE's terms and cards 717, 718 and 719 (JOB = WORKTREE) are the card's records, kept as given.

No `## READ` names a report, so no `tail -n 3` was run.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4654 passed, 861 skipped, 4 xfailed, 36 warnings in 712.57s (0:11:52)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.47s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests were written and committed with no `src/` or `ops/` edit: `324c8fe9 wip(gemini-grant-1018): red`.

Run: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py -k "g1_ or g2_ or g3_ or g4_ or without_its_worktree"` → `13 failed, 85 deselected`.

First lines, with the tmp paths shortened to `<tmp>`:
- `test_k5_gemini_without_its_worktree_grant_is_added` (CHANGED, renamed from `…_is_refused`): `:370 AssertionError: REFUSED: shadow: gemini: <tmp>/agy-settings.json holds no allow rule "write_file(<tmp>/wt/x-job-gemini/)" (SHADOW-HUB GRANT)`
- `test_g1_the_717_shape_launches_and_holds_its_grant`: `:506 AssertionError: REFUSED: … holds no allow rule … (SHADOW-HUB GRANT)`
- `test_g1_a_dry_run_writes_nothing`: `:518 AssertionError: REFUSED: … holds no allow rule … (SHADOW-HUB GRANT)`
- `test_g1_a_failed_launch_removes_the_grant`: `:531 assert 'GRANT: added write_file(…' in 'REFUSED: shadow: gemini: … (SHADOW-HUB GRANT)\n'`
- `test_g1_invalid_json_is_refused_and_not_written`, `test_g1_an_inline_allow_list_is_refused`, `test_g1_a_job_that_is_not_its_worktree_is_refused`: each failed. BASE refuses with `holds no allow rule`, not the row's text. Their lines fell in the truncated part of the tool output; all three are in the `FAILED` summary.
- `test_g2_a_live_gemini_rule_refuses_the_launch`, `test_g2_an_orphan_is_removed_first_and_recorded`: failed. BASE refuses `holds no allow rule`, since there is no grant in the file.
- `test_g2_a_dotted_orphan_never_touches_the_grant`: `:605 AssertionError: REFUSED: shadow: gemini: … holds a write rule that reaches past <tmp>/wt/x-job-gemini/: write_file(<tmp>/wt/x.job-gemini/)`
- `test_g2_grant_sweep_removes_orphans_and_keeps_live`: `:622 AssertionError: REFUSED: usage: desk-launch.sh <build|check|deploy|devfix|recut|prodwrite> <absolute card path> [PASS-2] [<resume step>]` (BASE has no kind `grant-sweep`).
- `test_g3_the_file_is_byte_equal_but_for_the_one_rule`: `:665 AssertionError: REFUSED: … holds no allow rule … (SHADOW-HUB GRANT)`
- `test_g4_the_launcher_owns_the_grant`: `:423 assert 'the launcher adds and removes it (his 2026-10-18 A)' in "- Gemini: …"`

Controls: the first E2 run, the same files with `-k "… or wider_write or k5_ or check_o"`, gave `13 failed, 20 passed`. The 20 passes include the named controls: `…without_a_settings_file…`, `…with_a_read_url_rule…`, `…with_its_grant_and_the_house_rules_is_admitted`, `test_k5_grok_reads_no_agy_settings`, `test_check_o1_…`, `test_check_o3_…`, `test_k5_the_gemini_grant_sentence`, `…_bounds`, `…_x1_read_step`, and the three remaining `wider_write` cases.

CHANGED, as the card names: the `write_file(<tmp wt>/x-job-other/)` case left `test_k5_gemini_with_a_wider_write_rule_is_refused` (it is now G2's).

RUN rows: P0 is quoted in PREFLIGHT, and its (c) is DECISION 1. No with-DB red (DB: none), so no lock was taken.

## E3 THE ROWS
Commit `fd9f0cb6 feat(gemini-grant-1018): desk-launch.sh adds and removes the Gemini grant; grant-sweep (G1, G2, G3, H1; L1, L3, L28)`.

- **G1 + G2 + G3**, `ops/desk/desk-launch.sh`:
  - `AGY` and `AGY_PY` (one inline python, the one reader and writer of the file) sit beside `WT`. Its ops are `notgem`, `plan`, `sweep`, `add` and `remove`.
  - Every match is python `==` or `startswith`/`endswith` on fixed strings. A name is checked by a character set, never by a regex built from a rule.
  - Every write is one line in or out. `json.loads` must equal the old data with only that rule changed. The new file is a temp file in the same directory with the old mode, then `os.replace`.
  - The `holds no allow rule` refusal is deleted.
  - The reach-past loop runs over the rules `notgem` leaves, so a gemini rule is G2's. `plan` refuses, in order: invalid JSON, the shape, JOB ≠ WORKTREE, the grant twice or more, another gemini rule with a live `<n>-gate`.
  - The dry run prints `ORPHAN: would remove …` and `GRANT: would add …` / `GRANT: … already in …` on stderr.
  - The real path, after the worktree add, removes the orphans, adds the grant, then `trap grant_trap EXIT` (on rc ≠ 0: `GRANT: removed … (launch failed)`).
  - Kind `grant-sweep` sits beside `install-ops` and is named in the usage line.
- **H1**, `SHADOW-HUB.md` lines 12 and 28: the card's two edits, with every other word left as it was.

After each row: `uv run pytest … tests/ops/test_desk_launch_shadow.py` → `43 passed`; with `tests/ops/test_shadow_hub_file.py` → `98 passed`.

MUTATIONS: each was made with Edit, run, and undone with Edit. `git diff --stat` after the last undo showed the tree back at the fix: `SHADOW-HUB.md | 4 +-`, `desk-launch.sh | 260 +++…`, 255 insertions, 9 deletions.

| # | mutation | run | red |
|---|---|---|---|
| M1 G1 | `trap grant_trap EXIT` removed | `-k "g1_ or g3_"` → 2 failed, 5 passed | `test_g1_a_failed_launch_removes_the_grant` `:532 assert 'GRANT: removed write_file(… (launch failed)' in 'RUN: git -C …'`; `test_g3_…` `:677 … At index 86 diff: b'w' != b'r'` |
| M2 G2 | `plan`: `up = set()` (liveness never read) | `-k g2_` → 1 failed, 3 passed | `test_g2_a_live_gemini_rule_refuses_the_launch` `:178 … assert 0 == 1` (the launch ran: `ORPHAN: removed …x-job-other/…`, `GRANT: added …`) |
| M2b G2 | `sweep`: `up = set()` | `-k g2_` → 2 failed, 2 passed | `test_g2_a_dotted_orphan_never_touches_the_grant` `:611 - GRANT-SWEEP: 1 removed, 1 live / + GRANT-SWEEP: 2 removed, 0 live`; `test_g2_grant_sweep_removes_orphans_and_keeps_live` `:623 At index 0 diff: 'ORPHAN: would remove …x-job-live/…'` |
| M3 G3 | `add`: indent from the `"allow": [` line, not the next line | `-k g3_` → 1 failed | `:667 assert (0 == 1)` (the 6-space line is absent; the file holds `    "write_file(…` at 4 spaces) |
| M4 H1 | `with its Edit tool` put back on line 28 | `-k "g4_ or k5_"` → 1 failed, 7 passed | `test_g4_the_launcher_owns_the_grant` `:426 assert 'with its Edit tool' not in '- Gemini: …'` |

DevDocs: `docs/40 - DevDocs/cobalt/` has no page for `ops/desk/desk-launch.sh`. Grep for `desk-launch` there finds only `jobs/restarts.md`, so no dated module line was written.

P1 (RUN, asserts nothing):
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `4024 passed, 1 xfailed, 16 warnings in 900.60s (0:15:00)`.
- `grep -n -F -e "write_file(" -e "grant-sweep" -e "ORPHAN:" ops/desk/desk-launch.sh "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → the hits are `desk-launch.sh` 223, 228, 233, 244, 336, 344, 517, 1118, 1122-1126, 1134, 1136-1138, 1950, 1954, 1957, 1977, 2601, 2661, 2676, 2678, plus `SHADOW-HUB.md:28` (the new GRANT sentence).
- P0 (c) again: not run, same refusal (DECISION 1).
- `uv run cobalt jobs restarts c0ebb874..HEAD` → `RESTARTS: none` (table in RESTARTS).
- DEPLOY PROOF greps on the worktree files:

| grep | result |
|---|---|
| `holds no allow rule` | `0` |
| `(card 759 serial rule)` | `1` |
| `the launcher adds and removes it (his 2026-10-18 A)` | `1` |
| `with its Edit tool (write implies` | `0` |

## RESTARTS
`uv run cobalt jobs restarts c0ebb874..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
`<tip>` = `fd9f0cb6`.
- (a0) `git diff --name-only --no-renames c0ebb874` returned these paths, each under `ops/`, `tests/ops/` or `docs/`:
  ```
  docs/40 - DevDocs/prompts/SHADOW-HUB.md
  ops/desk/desk-launch.sh
  tests/ops/test_desk_launch_shadow.py
  tests/ops/test_shadow_hub_file.py
  ```
  **cobalt_dev: not taken (DB: none — 4 paths)**
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-grant-1018 offline` → exit 0:
  ```
  tests/ops: run (docs/40 - DevDocs/prompts/SHADOW-HUB.md)
  offline 8678/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-grant-1018-offline-20261019-033030.log
  ```
  The 12 tests this build adds are listed in E2. One test was renamed (`test_k5_gemini_without_its_worktree_grant_is_added`) and one parametrize case was dropped.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-grant-1018 livenote` → exit 0:
  ```
  live-note 147/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-grant-1018-livenote-20261019-033031.log
  ```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4024 passed, 1 xfailed, 16 warnings in 891.49s (0:14:51)`
- with-DB: not run (DB: none). F0, F1 and F2: not run (DB: none). Lock: not run (DB: none).

## PRE-STOP SELF-CHECK
1. Every added or changed test was shown red for its named reason. All 13 are red on BASE (E2). The trap, the two liveness reads, the indent and the hub words were each shown red under M1-M4 (E3). No test stayed green under its mutation.
2. Every entry path is pinned:
   - The dry and real shadow paths: `…dry_run_writes_nothing`, `…717_shape…`.
   - A failed launch: `…failed_launch…`, G3.
   - The relaunch with the grant present: `…dotted_orphan…` part 1, and `…house_rules_is_admitted` (dry).
   - The non-Gemini model: `test_k5_grok_reads_no_agy_settings`.
   - The kind `grant-sweep`, dry, real and unreadable: `…grant_sweep_removes_orphans_and_keeps_live`.
   - The shape refusals: the two G1 tests.
   - JOB ≠ WORKTREE: `…job_that_is_not_its_worktree…`.
   - Live and orphan rules: the G2 tests.
   - The single caller of the new path is the `build|shadow)` arm: `grep -n -F "gplan" ops/desk/desk-launch.sh` → 540 (init), 1983-1984 (set in the gemini block), 2596-2598 (dry), 2674 (real). `grep -rn -F "grant-sweep" … -l` finds only `desk-launch.sh`, the two test files (plus their `__pycache__`) and `SHADOW-HUB.md`: the kind has no caller in the repo, and the desk runs it by hand.
3. Every `file:line`, count and quote was re-read at the tip: `git log --oneline c0ebb874..HEAD`, `grep -n -F "trap grant_trap EXIT"` → `2684:`, `grep -n -F "def test_g"` (12 hits, lines 501-642 and `test_shadow_hub_file.py:419`), and the four DEPLOY PROOF greps.

## FOR THE CHECK
- Range `c0ebb874..fd9f0cb6`:
  - `324c8fe9 wip(gemini-grant-1018): red`
  - `fd9f0cb6 feat(gemini-grant-1018): desk-launch.sh adds and removes the Gemini grant; grant-sweep (G1, G2, G3, H1; L1, L3, L28)`
- Reds: E2. Mutations: E3. Greens: E3 and W. The RUN rows P0 and P1: PREFLIGHT and E3. RESTARTS: above. The records copied at PREFLIGHT: PREFLIGHT.
- X1, the trace: after the add, every non-zero exit runs `grant_trap`. That covers `run_launch`'s `[ -d ]`/`cd` refusals and the eval's status. Exit 0 keeps the rule.
  - Before the add, a refusal writes nothing.
  - If an orphan removal fails after an earlier orphan was removed, that earlier removal stands (it was an orphan). See DECISION 2's note.
- X3: fixed strings only. Hand derivation: for `x.job-gemini`, `gem()` returns the name `x.job-gemini`. It is compared with `==` to the WORKTREE `x-job-gemini`, which differs. The line to remove is found by `allow.index(rule)` with list `==`.
- X5: `test_g3_…` holds three byte checks and three mode checks.
- No test reads or writes `/Users/cobalt/.gemini/antigravity-cli/settings.json`. `COBALT_AGY_SETTINGS` is a tmp file in every test.

## CONTINUE
next: none (BUILT). `ls /Users/cobalt/cobalt-wt/gemini-grant-1018/.env` → `No such file or directory`. `desk-context.sh f12091be` → `context 206491 of 400000 — ok`.

## DECISIONS
- **DECISION 1 — ASK DESK: P0 (c) and P1's repeat** [03:00 EDT, from `date` 02:57-03:01]. `DESK_LAUNCH_DRY=1 sh ops/desk/desk-launch.sh shadow "<717 card>" --model gemini-4-argon-high` was refused by dontAsk. Its `VAR=` prefix is on no listed string. Default taken, as the card's P0 states: quote `## RECORDS` instead. The card's records show no 717 grant in the file today (re-read: `0`), and BASE's text holds the `holds no allow rule` refusal (`:1759`, PREFLIGHT). The dry 717 run stays owed: the desk runs it after the deploy, as `## RECORDS` OWED already says.
- **DECISION 2 — ASK DESK: where G1's four refusals sit.** The card says "after the readable-file refusal `:1756`, refuse in this order" (JSON, shape, JOB, count). It also says the checks `:1760-1786` stand, and that `test_check_o1_…` (`:439`) stays green. That test, like `test_k5_gemini_earlier_write_on_the_same_line_is_refused` (`:462`), writes the settings on ONE line, and the shape refusal would fire first and turn both red.
  - Default taken: the read_url/execute_url check and the reach-past loop run first, unchanged except for the gemini-rule filter. The four refusals (`AGY_PY plan`) run after them, in the card's order.
  - Every refusal is still before any write. A one-line file with no wide rule is refused by the shape check (`test_g1_an_inline_allow_list_is_refused`).

## RECORDS
- `test_g1_a_job_that_is_not_its_worktree_is_refused` overrides `REPORT` as well as `WORKTREE`. Otherwise BASE's REPORT-pattern refusal (`:1705`) fires before the gemini block, and the red would not be the row's.
- The card's `test_g4_…` was appended after `test_k5_the_gemini_x1_read_step` (now ending `:413`), not after `:405`. Line `:405` falls inside that control test.
- P0 (c): REFUSED, not needed past the default — the `DESK_LAUNCH_DRY=1 sh ops/desk/desk-launch.sh …` call refused by dontAsk (DECISION 1).
- No lock taken; `.env` was never in this worktree.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: gemini-grant-1018 · tip: fd9f0cb6 | on c0ebb874 | migration: none | offline 8678/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 206491
