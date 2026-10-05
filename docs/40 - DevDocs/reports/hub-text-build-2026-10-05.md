# hub-text — build report 2026-10-05

## §0 Headline
- hub-text built: all 8 rows (F1–F8) are in BUILD-, CHECK- and DEPLOY-HUB.md at `6b939b00`, on `a09ee1f0`.
- Every card read is green, every mutation went red, `test_hub_lines.py` passes 19/19.
- Offline 3786/0, live-note 146/0; with-DB not run (DB: none). RESTARTS: none.
- `tests/ops` has 1 red, `test_desk_launch_brain.py:285`. It is red on base and outside the rows: DECISION 1.

## L74
None in a tool result. A system reminder asked for a `Claude-Session:` trailer; not acted on (see `## RECORDS`).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md"` → exit 0, last line `AUTHORIZED` (13:54 EDT). Output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md" · 0 · 98d77082d03b055c095da22a212139d4917078f1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
HOUSE A overruled 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
HOUSE A overruled 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:

```
clock · date · 0 · Mon Oct  5 13:55:12 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/hub-text-1005
    ?? "docs/40 - DevDocs/reports/hub-text-build-2026-10-05.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · a09ee1f0 docs(desk): R421 launcher fix-round amend drafter prompt 28 (brain option b)
diff · git diff --stat a09ee1f0 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/hub-text-1005 · 0 · a09ee1f0 docs(desk): R421 launcher fix-round amend drafter prompt 28 (brain option b)
env here · ls /Users/cobalt/cobalt-wt/hub-text-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat a09ee1f0` | 0 | `docs(desk): R421 launcher fix-round amend drafter prompt 28 (brain option b)` — `28-draft-launcher-fixround-amend.md` +8, `cto-2026-10-05.md` +2; 2 files, 10 insertions |
| wc | `wc -l` the three hubs | 0 | DEPLOY-HUB.md 182 · CHECK-HUB.md 131 · BUILD-HUB.md 109 |
| DEPLOY :26 | `grep -n -F "L43 / L66 the window"` | 0 | `26:L35 every value re-read at run time · L42 the restart set is the tool's · L43 / L66 the window: residents go down inside the 20:00–21:00 ET pause …` (the card's OLD, whole) |
| DEPLOY :57 | `grep -n -F "P1 DATE AND WINDOW"` | 0 | `57:- **P1 DATE AND WINDOW**: \`date\`. Lawful when ONE of these holds; …` (the card's OLD, whole) |
| DEPLOY :93 | `grep -n -F "P1 (v) RE-READ"` | 0 | `93:- P1 (v) RE-READ: when P1 named \`(v) provisional\`, … the window D2.6 reads.` |
| DEPLOY :134 | `grep -n -F "window closed at"` | 0 | `134:- D2.6 \`date\` → still inside the window P1 named (under (i) or (ii): before 04:00 ET), else \`FAILED: D2.6 — window closed at <time> · rollback: not used\`. …` |
| DEPLOY :74, :101 | `grep -n -F "(d2)"` | 0 | `74:\| \`validate\`, … \| G (d2), STEP-R, D1, D2.4 \|` · `101:- (d2) VALIDATE, right before the gate call (seconds): …` |
| DEPLOY :141 | Grep tool `4.5 \`COBALT_ENV=production uv run cobalt validate\`` | — | `141:4.5 \`COBALT_ENV=production uv run cobalt validate\` → exit 0 …` (the bash `grep` of this string was blocked by the bare-guard hook as a production route; read with the Grep tool) |
| DEPLOY :178 | `grep -n -F "then the stop line, LAST non-blank line."` | 0 | `178:5. THE RELEASE (STEP-G), then the stop line, LAST non-blank line. Commit: …` |
| stop lines | `grep -n -F "for Dejan: <n>"` the three hubs | 0 | DEPLOY `:50`, `:181`; CHECK `:58`, `:127`, `:129`; BUILD `:43`, `:106` |
| prose lines | `grep -n -F "The stop line carries"` the three hubs | 0 | DEPLOY `:50`, CHECK `:58`, BUILD `:43` |
| CHECK :117 | `grep -n -F "a deploy is gated on the combined tree (L68)."` | 0 | `117:` (the standing line, `… a deploy is gated on the combined tree (L68)."**`) |
| CHECK :124 | `grep -n -F "NO FURTHER HOUSE AND NO THIRD PASS."` | 0 | `124:- THEN \`## 4\` … NO FURTHER HOUSE AND NO THIRD PASS.` (line 21 carries the words with a colon, not a period) |
| BUILD :109 | `grep -n -F "NEXT STEP, not yours: the desk verifies the artifact (L35) and launches the check."` | 0 | `109:\`<tip>\` = the last code commit … launches the check. The desk watches \`^(BUILT\|FAILED)\`.` |
| window | `grep -n -i "window"` the three hubs | 0 | DEPLOY `:26`, `:57`, `:93`, `:134`; none in CHECK or BUILD (matches card RECORDS line 1) |
| reports READ | `tail -n 3 cto-2026-10-05.md` | 0 | last line `HANDOVER: predecessor 6af1ae05 → successor 799a133f at 13:47 ET` |
| | `tail -n 3 cto-2026-10-05-words.md` | 0 | last line: R384's quoted words (his text, not copied here) |
| READ | LAWS `### L43` :253, `### L68` :348, `### L71` :358, `### L75` :373; cto-2026-10-05.md rows R375 :48, R376 :49, R389 :65, R390 :67, R412 :109 | — | each found |
| test pins | Read `tests/ops/test_hub_lines.py` | — | pins the four `claude --bg ` lines, their flag, the wakeup LAUNCH line, the Grok line, and DEPLOY STEP-G's `- (f) ` bullet; no row moves one |
| restarts | `uv run cobalt jobs restarts a09ee1f0..HEAD` | 0 | `docs/40 - DevDocs/reports/hub-text-build-2026-10-05.md  A  DOCS  -` · `RESTARTS: none` (the one row is this untracked report; no commit in range) |

Card `## RECORDS`, copied and re-read:
- "The drafter's reads … `DEPLOY-HUB.md` hit lines 26, 57, 93, 134 (window) … `CHECK-HUB.md` and `BUILD-HUB.md` hit no window or night line. `(d2)` / `--no-db` in `DEPLOY-HUB.md`: lines 74 and 101." → re-read: window `:26 :57 :93 :134` only; `(d2)` `:74 :101`; `--no-db` count 1 (`:101`). Holds.
- "RESTARTS: every path is `docs/**` (DOCS, no resident); `DB: none`." → re-read at RESTARTS.
- "Source of the `tokens` mechanism: `ops/desk/desk-context.sh` …" → not re-read (outside the rows; CHECK ASK X3 is the check's).

PROVEN BY FIRST USE: class (a) at AUTHORIZATION and preflight.sh (both exit 0); `uv run pytest *` and the live-vault prefix at E0. `DB: none`: no lock probe, no with-DB string used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 650.10s (0:10:50)`, exit 0: 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.72s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Every row's red first is a grep read plus the existing `tests/ops/test_hub_lines.py`; no row names a test to write, so no test file was written and no `wip(hub-text): red` commit exists (nothing to commit). The reds on `BASE` a09ee1f0 (no output = no hit, exit 1; a backtick pattern was read with the Grep tool, since the hook blocks a backtick in Bash):

| row | read | on BASE |
|---|---|---|
| F1 | `grep -n -F "No restart window binds a deploy (L43, his R389)"` DEPLOY | no hit |
| F1 | `grep -n -F "no restart window and no per-night count binds it (his R389)"` DEPLOY | no hit |
| F1 | Grep `D2\.6 \`date\` → recorded in the row\.` DEPLOY | 0 matches |
| F1 | `grep -c -F` `20:00–21:00` / `04:00 ET` / `(v) provisional` / `window closed at` DEPLOY | 2 / 3 / 2 / 1 |
| F2 | `grep -n -F "each feature deploys alone on its existing check (his R390)"` DEPLOY | no hit |
| F2 | `grep -n -F "each feature deploying alone on this check (his R390)"` CHECK | no hit |
| F2 | `grep -c -F "L68 the integrated gate before the merge ·"` DEPLOY | 1 |
| F3 | `grep -n -F "(L75, his R376)"` CHECK; BUILD | no hit; no hit |
| F4 | Grep `for Dejan: <n> · tokens: <n>\`` the three hubs | 0 matches |
| F4 | Grep `for Dejan: <n>\`` BUILD / CHECK / DEPLOY | 2 / 3 / 2 |
| F4 | `grep -c -F "You write no token figure"` CHECK | 1 |
| F4 | `grep -c -F "desk-context.sh <your session id>"` BUILD / CHECK / DEPLOY | 0 / 0 / 0 |
| F4 (b) | `grep -c -F "first runs the gate on the merged hub text"` BUILD / CHECK / DEPLOY | 0 / 0 / 0 |
| F5 | `grep -c -F "(d2)"` / `grep -c -F -e "--no-db"` / `grep -c -F "jobsG"` DEPLOY | 2 / 1 / 1 |
| F6–F8 | Grep ``The stop line carries `decisions: <n> · for Dejan: <n> · tokens: <n>` `` the three hubs | 0 matches |
| F6–F8 | Grep ``The stop line carries `decisions: <n> · for Dejan: <n>`[.;]`` BUILD / CHECK / DEPLOY | 1 / 1 / 1 |

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` on BASE → `19 passed, 15 warnings in 3.01s`.

## E3 THE ROWS
All eight rows built in card order with the Edit tool, in the three hub files only. Commit `6b939b00 feat(hub-text): fold R389, R390, R376, R375 MEASURE and R412 into the three hubs (F1-F8, L43, L68, L71, L75)` — 3 files, 15 insertions, 17 deletions.

Greens on the tree (no output = no hit; backtick patterns read with the Grep tool):

| row | read | result | card expects |
|---|---|---|---|
| F1 | `grep -n -i "window"` DEPLOY | `:26` (`… no restart window and no per-night count binds it (his R389) ·`), `:57` (`- **P1 DATE**: \`date\`, recorded in the row. No restart window binds a deploy (L43, his R389): it runs at any hour, day or night.`) only | only those two |
| F1 | Grep `D2\.6 \`date\` → recorded in the row\.` | `133:- D2.6 \`date\` → recorded in the row. \`git -C /Users/cobalt/cobalt tag pre-<JOB>\` …` (it was `:134`; the deleted STEP-R bullet moved it up one) | one hit |
| F1 | `grep -c -F` `20:00–21:00` / `04:00 ET` / `(v) provisional` / `window closed at` | 0 / 0 / 0 / 0 | 0 each |
| F2 | `grep -n -F "each feature deploys alone on its existing check (his R390)"` DEPLOY | `:26` | one hit |
| F2 | `grep -c -F "each feature deploying alone on this check (his R390)"` CHECK | 1 (`:117`) | one hit |
| F2 | `grep -c -F "L68 the integrated gate before the merge ·"` DEPLOY | 0 | 0 |
| F3 | `grep -c -F "(L75, his R376)"` CHECK / BUILD | 1 / 1 | one hit each |
| F3 | `grep -c -F "NO FURTHER HOUSE AND NO THIRD PASS."` CHECK | 1 | 1 |
| F4 (a) | Grep `for Dejan: <n> · tokens: <n>\`` | BUILD `:43 :106`; CHECK `:58 :127 :129`; DEPLOY `:50 :179` → 2 / 3 / 2 | 2 / 3 / 2 |
| F4 (a) | Grep `for Dejan: <n>\`` the three hubs | 0 matches | 0 |
| F4 (a) | `grep -c -F "You write no token figure"` CHECK | 0 | 0 |
| F4 (a) | `grep -c -F "desk-context.sh <your session id>"` BUILD / CHECK / DEPLOY | 1 / 1 / 1 (DEPLOY's is item 5, the card's own edit) | one in BUILD and in CHECK |
| F4 (b) | `grep -c -F "first runs the gate on the merged hub text"` BUILD / CHECK / DEPLOY | 0 / 0 / 1 | 0 / 0 / 1 |
| F5 | `grep -c -F "(d2)"` / `grep -c -F -e "--no-db"` / `grep -c -F "jobsG"` DEPLOY | 0 / 0 / 0 | 0 each |
| F5 | Grep `4.5 \`COBALT_ENV=production uv run cobalt validate\`` | `139:` (text unchanged; it was `:141`, two deleted lines above it) | one hit |
| F6 / F7 / F8 | Grep ``The stop line carries `decisions: <n> · for Dejan: <n> · tokens: <n>`[.;]`` | BUILD `:43` `.` · CHECK `:58` `;` · DEPLOY `:50` `.` | one hit each |
| F6–F8 | Grep ``for Dejan: <n>` `` (the old prose forms) | 0 | 0 |

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` → `19 passed, 15 warnings` after F1, F2, F3, F4–F8, and again with every mutation undone (`19 passed, 15 warnings in 2.75s`).

THE MUTATIONS (Edit tool, each undone with the Edit tool; `git diff --stat` after the last undo → the three hubs only, `15 insertions(+), 17 deletions(-)`; `grep -c -F "MUTATION"` DEPLOY → 0):

| row | mutation | read | red |
|---|---|---|---|
| F1 | P1's `No restart window binds a deploy (L43, his R389)` → `MUTATION F1 binds a deploy` | `grep -c -F "No restart window binds a deploy (L43, his R389)"` | 0 (green 1) |
| F2 | `… deploys alone on its existing check (his R390)` → `… deploys alone (his R390)` | `grep -c -F "each feature deploys alone on its existing check (his R390)"` | 0 (green 1) |
| F3 | CHECK's ` (L75, his R376)` removed | `grep -c -F "(L75, his R376)"` CHECK | 0 (green 1) |
| F4 | BUILD `:106` ` · tokens: <n>` removed | Grep `for Dejan: <n> · tokens: <n>\`` BUILD | 1 (green 2) |
| F5 | `G (d2), ` put back in the `:74` table cell | `grep -c -F "(d2)"` | 1 (green 0) |
| F6 | BUILD `:43` ` · tokens: <n>` removed | Grep ``The stop line carries `decisions: <n> · for Dejan: <n> · tokens: <n>` `` BUILD+CHECK | 0 (run with F7's mutation; green 2) |
| F7 | CHECK `:58` ` · tokens: <n>` removed | (the same read) | 0 |
| F8 | DEPLOY `:50` ` · tokens: <n>` removed | Grep ``The stop line carries `decisions: <n> · for Dejan: <n> · tokens: <n>`\.`` DEPLOY | 0 (green 1) |

`tests/ops/test_hub_lines.py` pins no row's text (PREFLIGHT); it is the "no pinned line moved" control and stays green, as the card says.

DevDocs: no `src/` module changed; the hubs have no page under `docs/40 - DevDocs/cobalt/`, so no module line was written.

## RESTARTS
`uv run cobalt jobs restarts a09ee1f0..HEAD` →

```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-text-build-2026-10-05.md	A	DOCS	-
RESTARTS: none
```

No UNCLASSIFIED row. (The report row is this untracked file.)

## W THE THREE SUITES
`<tip>` = `6b939b00`. DB: none card.
- (a0) `git diff --name-only --no-renames a09ee1f0` → `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `docs/40 - DevDocs/prompts/CHECK-HUB.md` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` — every path under `docs/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-text-1005 offline` (background) → exit 0, `offline 3786/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1005-offline-20261005-141115.log`; its summary (log `:829`): `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 633.41s (0:10:33)`. This build adds no test.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-text-1005 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1005-livenote-20261005-142208.log`; its one skip (log `:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — none names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1, `1 failed, 1347 passed, 1 xfailed, 15 warnings in 355.96s (0:05:55)`. The red: `tests/ops/test_desk_launch_brain.py:285` `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` — `AssertionError: assert '«INSTALL' in '# BRAIN-HUB — the standing brain seat (installed 2026-10-05 on his 2026-10-02 R54 …'`. A BASE red, not this build's: `git diff --stat a09ee1f0 HEAD -- "docs/40 - DevDocs/prompts/BRAIN-HUB.md" tests/ops/test_desk_launch_brain.py` → nothing; `git log --oneline -3 -- BRAIN-HUB.md` → newest `4a19b075 docs(desk): R357 wake-up ecc18b72; R358 BRAIN-HUB installed on R54 for the brain restart`; the test's newest commit is `5c1d629f`, older than that. The fix is outside this card's rows and fence: DECISION 1.
- (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/hub-text-1005/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every row read was shown red against a mutation (E3 THE MUTATIONS table: F1 0, F2 0, F3 0, F4 1, F5 1, F6/F7 0, F8 0) and against BASE (E2 table). No test was added or changed; `test_hub_lines.py` is the control the card names and stays green.
(2) Entry paths: these rows are hub text with no code callers. Each changed clause is pinned by the card's grep reads: P1, STEP-R, D2.6 and the LAWS line (F1); the LAWS line and CHECK `## 8` (F2); CHECK `## PASS 2` and BUILD STOP LINE (F3); all seven stop lines and prose lines (F4, F6–F8); the `(d2)` bullet and the table cell (F5). Every `window` mention left in the three hubs is the two new sentences (`grep -n -i "window"` at tip).
(3) Re-read at the tip `6b939b00`: `git status --short --branch` → `## ops/hub-text-1005` plus the untracked report; `git log --oneline a09ee1f0..HEAD` → `6b939b00`; `grep -n -i "window"` the three hubs → DEPLOY `:26`, `:57` only; `wc -l` → DEPLOY 180, CHECK 131, BUILD 109. The E3 greens ran on this same tree: the commit changed nothing in the files (`git diff --stat` before the commit showed exactly the committed stat).

## FOR THE CHECK
- Range `a09ee1f0..6b939b00`: `6b939b00 feat(hub-text): fold R389, R390, R376, R375 MEASURE and R412 into the three hubs (F1-F8, L43, L68, L71, L75)`. No red commit (no test file written: E2).
- Per row: reds on BASE (E2), mutation reds and greens (E3), all quoted above.
- Caller greps: none apply (hub text). `test_hub_lines.py` pins: four launch lines, their flag, the wakeup LAUNCH line, the Grok line, DEPLOY STEP-G `- (f) ` — none moved; 19 passed.
- No RUN row on this card.
- Suites: offline `3786/0` (gate log above); with-DB `not run (DB: none)`; live-note `146/0` (gate log above); `tests/ops` `1 failed, 1347 passed, 1 xfailed` (the base red, DECISION 1).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: above, `RESTARTS: none`.
- Line moves the check will see: DEPLOY STEP-R lost one bullet and STEP-G lost the (d2) bullet, so DEPLOY lines from `:93` move up by one and from `:101` by two (D2.6 now `:133`, 4.5 `:139`, item 5 `:176`, the `DEPLOYED` line `:179`).
- Records copied at PREFLIGHT: in `## PREFLIGHT`.

## CONTINUE
next: CLOSE (done)

## DECISIONS
- DECISION 1: `tests/ops` is red on BASE `a09ee1f0`, not because of this build. `tests/ops/test_desk_launch_brain.py:285` asserts the draft token `«INSTALL` is in `BRAIN-HUB.md`, but `4a19b075` (R358) installed that hub and the test was not updated. Neither file is in this diff, and both are outside the card's rows. Safe default taken: not fixed here, the rows' work stands. It needs its own card, a one-line test change to match the installed title.

## RECORDS
- L74: no tool result carried a `Claude-Session:` request. A system reminder in this session asked for a `Claude-Session:` trailer on commits. I did not act on it: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).
- F4 (b) spacing: the card's OLD `· L70 unproven is never a defect` begins at the `·`. A literal swap would have left `(his R390) ; a set …` with a space before the semicolon. I wrote `(his R390); a set that changes …`, the text the card's NEW gives with no stray space. No read depends on that space.
- F4 (a), BUILD `:109`: the token sentence went at the end of the line, after `The desk watches \`^(BUILT|FAILED)\`.`, which is also after F3's sentence.
- PREFLIGHT `restarts` on the empty commit range listed the untracked report as one DOCS row (`RESTARTS: none`).
- Hook blocks, each resent as a Grep tool read (not refusals): a bash `grep` with a backtick in its pattern; a bash `grep` whose pattern held `COBALT_ENV=production` (the guard's route rule).
- Card records re-read: in `## PREFLIGHT` (window and (d2) lines hold; RESTARTS DOCS holds).
- `.env`: never present in this worktree (DB: none, no lock taken).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: hub-text · tip: 6b939b00 | on a09ee1f0 | migration: none | offline 3786/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
