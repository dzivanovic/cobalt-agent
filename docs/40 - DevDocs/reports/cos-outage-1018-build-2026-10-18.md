# cos-outage-1018 — build report (routed, BAND LOW, builder grok-4.7, gate cos-outage-1018-gate)

## §0 Headline
- K1, K2 built by grok-4.7 in two passes (T, S), no S2; gate seat Opus 5.5. Tip `de3e15c8` on `0bdb7089`.
- Suites at first run green: offline 8612/0, tests/ops 3966 passed, live-note 147/0; DB: none, no lock.
- Reds matched the card exactly (K1 `4 failed, 1 passed`, K2 `3 failed, 1 passed`); after the rows both files `112 passed`; DEPLOY PROOF counts `5` and `1`.
- Two decisions: the untracked `SHADOW-INSTRUCTIONS.md` in the HEAD RESTARTS table; the two byte-identical controls never shown red (self-check 2 of 3).

## L74
- The session's harness carries a `Claude-Session:` attribution line in its system reminders; DATA under L74, not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md" · 0 · e375f781044e3d1b357feb8b6c00d3c83c850c7f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 62:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"` → exit 0, whole:
```
clock · date · 0 · Sun Oct 18 16:35:13 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-outage-1018
head · git log --oneline -1 · 0 · 0bdb7089 docs(prompt): 783 drafter for cos-outage-1018 card
diff · git diff --stat 0bdb7089 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-outage-1018 · 0 · 0bdb7089 docs(prompt): 783 drafter for cos-outage-1018 card
env here · ls /Users/cobalt/cobalt-wt/cos-outage-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f20-cos-1018/.env
PREFLIGHT OK
```
Routed card (BAND: LOW, no `SHADOW OF:`): the stop line is BUILD-HUB's `BUILT ·` (SHADOW-HUB `:28`, `:57`, `:74`). DB: none: no lock probe.

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 0bdb7089` | 0 | `docs(prompt): 783 drafter for cos-outage-1018 card` · `docs/40 - DevDocs/prompts/2026-10-18/783-draft-cos-outage.md | 7 +++++++` |
| K1 `:90` | `grep -n -F "com.cobalt.aset\|com.cobalt.radar\|com.cobalt.agent)" ops/desk/deploy-outage.sh` | 0 | `90:        com.cobalt.aset\|com.cobalt.radar\|com.cobalt.agent) ;;` |
| K1 `plist_of` | `grep -n -F "plist_of" ops/desk/deploy-outage.sh` | 0 | `105:plist_of() {` · `140:` (dry run) · `236:` (rule E) · `284:` (`up_one`) |
| K2 `:73` | `grep -n -F "RESIDENTS" ops/desk/deploy-step0.sh` | 0 | `73:RESIDENTS="com.cobalt.aset com.cobalt.radar com.cobalt.agent"` · `875:for label in $RESIDENTS; do` |
| K2 `:41` | `grep -n -F "for aset, radar, agent" ops/desk/deploy-step0.sh` | 0 | `41:#   P8 census <label>    \`launchctl print gui/501/<label>\` for aset, radar, agent: pid and state,` |
| no cos at BASE | `grep -n -F "com.cobalt.cos" <the four files>` | 1 | nothing |
| cos plist | `git show fae30bbd:ops/com.cobalt.cos.plist` | 0 | Label `com.cobalt.cos`; comment `F20: BUILT, NOT LOADED (… BOOTSTRAP deferred)` |
| card 730 C4a / D8 | `grep -n -F "C4a"` / `"D8"` in `730-f20-card.md` | 0 | `:35` C4a row (NEW `ops/com.cobalt.cos.plist`); `:94` `D8 — DEPENDENCY: F20's deploy needs a K5 deploy-outage card first …` |
| wc | `wc -l` the four files | 0 | `442 ops/desk/deploy-outage.sh` · `908 ops/desk/deploy-step0.sh` · `492 tests/ops/test_deploy_outage.py` · `936 tests/ops/test_deploy_step0.py` |
| restarts | `uv run cobalt jobs restarts 0bdb7089..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

The card's RECORDS re-read: `:90-91`, `:105-110` (`:107` aset `$REPO/ops`, `:108` radar `$LAUNCHAGENTS`), step0 `:41`, `:73`, `:875-886` (`row … 0`), the cos plist at fae30bbd — each matches the read above.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4646 passed, 841 skipped, 4 xfailed, 36 warnings in 749.33s (0:12:29)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.06s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- The rows' test files on BASE: `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_outage.py tests/ops/test_deploy_step0.py` → `103 passed, 15 warnings in 87.85s (0:01:27)`.

## PASSES

| pass | env check | command as run | wall | tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls -la /Users/cobalt/cobalt-wt/cos-outage-1018/.env` → `ls: /Users/cobalt/cobalt-wt/cos-outage-1018/.env: No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/cos-outage-1018/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` (after `cd /Users/cobalt/cobalt-wt/cos-outage-1018`) | 16:49:46 → 16:57:22 EDT, 7.6 min | UNKNOWN (Grok prints none) | `tests/ops/test_deploy_outage.py | 116 +++` · `tests/ops/test_deploy_step0.py | 108 +++` · `2 files changed, 224 insertions(+)` | `1b11f128 wip(cos-outage-1018): red` |

| S | `ls -la /Users/cobalt/cobalt-wt/cos-outage-1018/.env` → `ls: /Users/cobalt/cobalt-wt/cos-outage-1018/.env: No such file or directory` | the same line with `Pass S: the rows.` in place of `Pass T: tests only under tests/.` (after `cd /Users/cobalt/cobalt-wt/cos-outage-1018`) | 16:57:55 → 16:58:36 EDT, 0.7 min | UNKNOWN | `ops/desk/deploy-outage.sh | 11 ++++++-----` · `ops/desk/deploy-step0.sh | 4 ++--` · `2 files changed, 8 insertions(+), 7 deletions(-)` | `de3e15c8 feat(cos-outage-1018): rows` |

Pass T reply: `- tests/ops/test_deploy_outage.py` · `- tests/ops/test_deploy_step0.py` · `[exited with code 0]`. Pass S reply: `- ops/desk/deploy-outage.sh` · `- ops/desk/deploy-step0.sh` · `[exited with code 0]`. No path outside the rows' files (no SCOPE). No S2. Passes: 2. Builder wall 8.3 min; builder tokens UNKNOWN.

## E2 RED
On the unchanged scripts (commit `1b11f128`, tests only):
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_outage.py -k k1` → `4 failed, 1 passed, 28 deselected, 15 warnings in 2.09s` (card: `4 failed, 1 passed`). First lines:
  - `test_k1_cos_goes_down_and_up_like_aset`: `AssertionError: REFUSED: 'com.cobalt.cos' is not a resident this script restores (com.cobalt.aset, com.cobalt.radar, com.cobalt.agent)`
  - `test_k1_dry_run_names_the_cos_bootout_and_the_repo_plist`: the same refusal
  - `test_k1_cos_loaded_from_launchagents_is_refused_before_anything_goes_down`: `assert 'is loaded from' in "REFUSED: 'com.cobalt.cos' is not a resident …"`
  - `test_k1_cos_not_loaded_is_refused_before_anything_goes_down`: `assert 'com.cobalt.cos is not running before the outage (gone)' in "REFUSED: 'com.cobalt.cos' is not a resident …"`
  - CONTROL 3 `test_k1_the_three_residents_print_the_same_lines`: PASSED on BASE.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py -k k2` → `3 failed, 1 passed, 75 deselected, 15 warnings in 4.07s` (card: `3 failed, 1 passed`). First lines:
  - `test_k2_census_lists_cos_after_the_agent`: `AssertionError: P8 census com.cobalt.cos is absent`
  - `test_k2_dry_run_names_the_cos_census`: `AssertionError: WOULD RUN: launchctl print gui/501/com.cobalt.cos is absent`
  - `test_k2_a_cos_not_loaded_is_recorded_and_fails_nothing`: `AssertionError: P8 census com.cobalt.cos is absent`
  - CONTROL 2 `test_k2_the_three_residents_rows_are_unchanged`: PASSED on BASE.
Each red is its row's named reason; no test rewritten.

## E3 THE ROWS
`git diff ops/desk` after pass S: exactly K1 (a) `:90`, (b) `:91`, (c) the new `plist_of` arm `:109` `com.cobalt.cos) printf '%s' "$REPO/ops/com.cobalt.cos.plist" ;;` after the radar arm, (d) `:4`, `:11` (`aset, radar and cos`), `:13` (`$REPO/ops/com.cobalt.cos.plist` after the aset plist); K2 (a) `:73`, (b) `:41`. No other line changed. Re-read at the tip with `grep -n -F "com.cobalt.cos" ops/desk/deploy-outage.sh ops/desk/deploy-step0.sh`:
```
ops/desk/deploy-outage.sh:4:# of <restart set> only (comma-separated: com.cobalt.aset, com.cobalt.radar, com.cobalt.agent, com.cobalt.cos).
ops/desk/deploy-outage.sh:13:#   ($REPO/ops/com.cobalt.aset.plist, $REPO/ops/com.cobalt.cos.plist, $LAUNCHAGENTS/com.cobalt.radar.plist), the plist present;
ops/desk/deploy-outage.sh:90:        com.cobalt.aset|com.cobalt.radar|com.cobalt.agent|com.cobalt.cos) ;;
ops/desk/deploy-outage.sh:91:        *) refuse "'$l' is not a resident this script restores (com.cobalt.aset, com.cobalt.radar, com.cobalt.agent, com.cobalt.cos)" ;;
ops/desk/deploy-outage.sh:109:        com.cobalt.cos) printf '%s' "$REPO/ops/com.cobalt.cos.plist" ;;
ops/desk/deploy-step0.sh:73:RESIDENTS="com.cobalt.aset com.cobalt.radar com.cobalt.agent com.cobalt.cos"
```
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_outage.py -k k1` → `5 passed, 28 deselected, 15 warnings in 3.49s`
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py -k k2` → `4 passed, 75 deselected, 15 warnings in 4.29s`
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_outage.py tests/ops/test_deploy_step0.py` → `112 passed, 15 warnings in 102.90s (0:01:42)` (103 on BASE + 9 new; the existing tests unedited)
- DEPLOY PROOF on the worktree: `grep -c -F "com.cobalt.cos" ops/desk/deploy-outage.sh` → `5`; `… deploy-step0.sh` → `1` (card: after `5`, `1`).
- MUTATIONS: the seat writes no `ops/` or `tests/` file (SHADOW-HUB RULES; guard G5), so no Edit-tool mutation was made. The undo of each row's fix is the tree at `1b11f128` (the scripts at BASE): the seven non-control tests are red there for their named reasons (E2) and green at `de3e15c8`. The two byte-identical controls are green on both by design: DECISION 2.
- No DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers these ops scripts (`Grep "deploy-outage|deploy-step0"` there → no files).

## RESTARTS
- `uv run cobalt jobs restarts 0bdb7089..HEAD` (worktree incl. untracked) → exit 1:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.md	A	DOCS	-
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
- The committed range at the tip: `uv run cobalt jobs restarts 0bdb7089..de3e15c8` → exit 0:
```
path	change	rule	restart
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
RESTARTS: none
```
The only UNCLASSIFIED path is the untracked, never-committed `SHADOW-INSTRUCTIONS.md`, as in `agy-read-1018-build-2026-10-18.md:130`. Not classified here (DECISION 1). The card's K10 record matches: `ops/desk/` operator script, `tests/` no resident.

## W THE THREE SUITES
DB: none card, on `<tip>` = `de3e15c8`.
- (a0) `git diff --name-only --no-renames 0bdb7089` → `ops/desk/deploy-outage.sh` · `ops/desk/deploy-step0.sh` · `tests/ops/test_deploy_outage.py` · `tests/ops/test_deploy_step0.py`: every path under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-outage-1018 offline` → exit 0: `tests/ops: run (ops/desk/deploy-outage.sh)` · `offline 8612/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/cos-outage-1018-offline-20261018-170101.log`. Tests this build adds: the five `test_k1_*` and the four `test_k2_*` named in E2.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-outage-1018 livenote` → exit 0: `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/cos-outage-1018-livenote-20261018-172958.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3966 passed, 1 xfailed, 16 warnings in 915.63s (0:15:15)`.
- (b)-(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/cos-outage-1018/.env` → `No such file or directory`.
Suites at first run: green.

## PRE-STOP SELF-CHECK
(1) 7 of 9 new tests shown red for their named reason on the unfixed scripts (`1b11f128`, E2 quotes); CONTROL 3 (K1) and CONTROL 2 (K2) are green-on-both by design and were never shown red; no Edit-tool mutation (the seat's fence). Gap: DECISION 2.
(2) Entry paths: `plist_of` callers by `grep -n -F "plist_of"` → `:140` dry run (pinned by `test_k1_dry_run_names_the_cos_bootout_and_the_repo_plist`), `:236` rule E (pinned by `test_k1_cos_loaded_from_launchagents_…` and `test_k1_cos_not_loaded_…`), `:284` `up_one`, used by step 2, step 3 and the trap (step 2 pinned by `test_k1_cos_goes_down_and_up_like_aset`'s bootstrap argv; the trap and step 3 paths for cos have no cos-specific test, but they are the same label-generic `up_one` call the existing signal tests pin for aset). `RESIDENTS` callers `:875` (run and dry run), pinned by the four `test_k2_*`.
(3) Re-read at the tip: `grep -n -F "com.cobalt.cos"` both scripts (E3), `git show de3e15c8:ops/desk/deploy-outage.sh`, `git log --oneline 0bdb7089..HEAD`, both `grep -c` counts, the restarts table on `0bdb7089..de3e15c8`.

## FOR THE CHECK
- `0bdb7089..de3e15c8`: `1b11f128 wip(cos-outage-1018): red` · `de3e15c8 feat(cos-outage-1018): rows`. The report commit follows them.
- Per row: reds in `## E2 RED`, greens in `## E3 THE ROWS`; mutation runs: none, see E3 and DECISION 2.
- Caller greps: `## PREFLIGHT` and self-check (2).
- RUN rows: none on this card.
- Suites: `## W`. With-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- X1 for the check: `git diff 0bdb7089 -- ops/desk` holds only K1 (a)-(d) and K2 (a)-(b), each line holding `com.cobalt.cos` once. X3: the only cos plist path is `plist_of`'s `:109` `$REPO/ops/com.cobalt.cos.plist`; rule E (`:236`), `up_one` (`:284`, so step 2, step 3 and the trap) and the dry run (`:140`) all call `plist_of`.
- CONTROL 2 of K2: the card says the rule column with cos removed equals "the full list of `:219-223` in its printed order (the builder takes that order from BASE's run)". Grok wrote the whole printed column (28 rules, P0's authorize rows and the P7 listings among them) as `K2_RULES_WITHOUT_COS`, with the comment that `:219-223` names a subset; it passed on BASE (E2), so it is BASE's printed order.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. ASK DESK: the HEAD-range RESTARTS table names the untracked `SHADOW-INSTRUCTIONS.md` as UNCLASSIFIED (exit 1). Safe default taken: not classified (it is never committed; X9 unsettled); the stop line carries the committed range's `RESTARTS: none`, as `agy-read-1018-build-2026-10-18.md` did.
2. ASK DESK: self-check (1) gap. `test_k1_the_three_residents_print_the_same_lines` and `test_k2_the_three_residents_rows_are_unchanged` are green on BASE and after by design, and the gate seat makes no Edit-tool mutation on `ops/` or `tests/` (SHADOW-HUB guard G5). Neither was shown red against a mutation. Safe default: `self-check: 2 of 3`; the check may run one mutation per control (e.g. change the aset pid literal, or reorder `RESIDENTS`).

## RECORDS
- `SHADOW-INSTRUCTIONS.md` written at the worktree root, never committed: the one untracked file.
- The gate seat ran AUTHORIZATION and PREFLIGHT with kind `shadow` (the hub's `:56-57`); this is a routed card (BAND: LOW, builder grok-4.7 from SHADOW-HUB `## BUILDERS` band table), so the stop line is BUILD-HUB's `BUILT ·`.
- Wall: 16:35:13 (preflight `date`) → 17:46:11 EDT, 71 min. Builder wall 8.3 min (T 7.6, S 0.7). Builder tokens UNKNOWN (L70).
- Gate seat tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 41081683` → `context 167789 of 400000 — ok`.
- No extra lock take (DB: none). No `REFUSED, not needed` line. No `CONTINUE` message received.
- The card's records as re-read at PREFLIGHT: `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-outage-1018 · tip: de3e15c8 | on 0bdb7089 | migration: none | offline 8612/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 167789
