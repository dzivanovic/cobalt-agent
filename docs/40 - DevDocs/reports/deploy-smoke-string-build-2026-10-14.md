# deploy-smoke-string-1014 — build report (card 537, K5)

## §0 Headline
- Rows S3, S1, S2 built and pinned on `9fb997bb`: `DEPLOY-HUB.md:11` and `STANDING-LIST.md` §3 carry `Bash(COBALT_ENV=production uv run cobalt smoke *)` once; R4 run, `RESTARTS: none`.
- Row T1 (card `c3c3e703`, built by a new session at `CONTINUE: W`) on `f21900fc`: `test_the_sweep_swept_what_it_pins` now asserts zero mismatches plus a floor of 18 check reports, with no fixed count. It was red on today's 21 reports before the fix and is green after.
- Gate on `f21900fc`: offline 4328/0, live-note 146/0, `tests/ops` 3604 passed / 0 failed, with-DB not taken (DB: none).

## L74
- One system notice in this session asked that commits end with a `Claude-Session:` line. Recorded here as data; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md"` · exit 0 · 07:37 ET (`date` → `Wed Oct 14 07:37:02 EDT 2026`):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md" · 0 · b6d7d49c47281aca71dbb074a3eb62ebed5a5f89
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
Second session (RECOVERY, `CONTINUE: W`, 08:35 ET), the same call, exit 0: every row as above except `CARD COMMITTED · … · 0 · c3c3e70322e928f5d4d17da7591151fd931cc966` (the card with row T1); `CARD UNCHANGED · … · 0 · nothing`; R60 and R1138 rows, commits and HEAD reads identical; last line `AUTHORIZED`.
RECOVERY reads: `git status --short --branch` → `## ops/deploy-smoke-string-1014`; `git log --oneline -3` → `042630b7`, `cfcb5a2b`, `4c3ae576` (the wip commits, continued); `ls -la …/.env` → "No such file or directory".

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0:
```
clock · date · 0 · Wed Oct 14 07:37:06 EDT 2026
status · git status --short --branch · 0 · ## ops/deploy-smoke-string-1014
head · git log --oneline -1 · 0 · 7aa5d470 docs(desk): 537 preflight r2 ready YES
diff · git diff --stat 7aa5d470 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-smoke-string-1014 · 0 · 7aa5d470 docs(desk): 537 preflight r2 ready YES
env here · ls /Users/cobalt/cobalt-wt/deploy-smoke-string-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 7aa5d470` | 0 | `docs(desk): 537 preflight r2 ready YES` · `.../smoke-string-preflight-r2-2026-10-14.md \| 29 ++++` · 1 file changed, 29 insertions(+) |
| symbol: launch line | `grep -n -F "claude --bg " "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | one hit, line 11; its allow list holds `… "Bash(COBALT_ENV=production uv run cobalt heartbeat show*)" "Bash(COBALT_ENV=production uv run cobalt backup run*)" …` |
| symbol: no smoke string yet | `grep -n -F "cobalt smoke" DEPLOY-HUB.md STANDING-LIST.md tests/ops/test_hub_lines.py` | 1 | nothing |
| symbol: STANDING-LIST sections | `grep -n -F "## " STANDING-LIST.md` | 0 | `109:## 3. \`DEPLOY-HUB.md\` — 56 allow with one head and a migration (53 without a migration; …` · `159:## 4. THE DESK'S OWN LINE …`; rows read at `:139` `heartbeat show*`, `:140` `backup run*` |
| symbol: `PROD_ALLOW_TODAY`, `hub_line`, `tools`, W7 test | Read `tests/ops/test_hub_lines.py` | — | `:54 def hub_line`, `:60 def tools`, `:97 PROD_ALLOW_TODAY = {`, `:102-108` the DEPLOY list of five, `:105` `heartbeat show*)`, `:133-141` the W7 test |
| symbol: `git show <BASE>` shape | Read `tests/ops/test_build_hub_no_clutter.py` | — | `:27 def base_lines()`, `:28-30` `subprocess.run(["git", "show", f"{BASE}:{HUB_REL}"], cwd=REPO, …)` |
| symbol: desk-launch fills tokens | Read `ops/desk/desk-launch.sh:2174-2189` | — | `line=$(grep '^claude --bg ' "$fixed" \| sed -e "s\|<card>\|$card\|g" …` (no allow list generated) |
| symbol: smoke read-only | Read `src/cobalt/smoke/cli.py:1-18, 34-38, 71-80` | — | `:6` "runs every check read-only"; `:8` "`--json` prints the same content and writes nothing."; `:38` "Writes nothing — `cmd_run` owns the file."; `:76` `report_mod.write_report(...)` unless `args.json` |
| symbol: RESTARTS homes | Read `src/cobalt/jobs/restarts.py:225-228, 245-246` | — | `docs/` → `"DOCS"`; `tests/` → `"test/documentation; no resident"` |
| wc | `wc -l DEPLOY-HUB.md STANDING-LIST.md tests/ops/test_hub_lines.py` | 0 | 187 · 253 · 291 |
| READ tail | `tail -n 3 …/reports/deploy-plist-step-c-1013.md` | 0 | last line: `FAILED: 4.7 (s) — \`COBALT_ENV=production uv run cobalt smoke s2\` refused — Permission to use Bash has been denied because Claude Code is running in don't ask mode. · …` |
| RESTARTS empty | `uv run cobalt jobs restarts 7aa5d470..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |
| lock probe | — | — | none: card is `DB: none` |

Card `## RECORDS`, copied and re-read: drafter reads on `main` `8b813ca7` (amend on `fc7a7f40`) — re-read here on `7aa5d470`: `DEPLOY-HUB.md:11` the one launch line (grep above: one hit); `STANDING-LIST.md:109` heading with `56 allow` / `53 without a migration`, `:139` heartbeat row, `:140` backup run row, `:159` `## 4.` (grep above); `cobalt smoke` absent from all three files (grep above); `test_hub_lines.py:105` heartbeat, no smoke (Read above); refusal at `deploy-plist-step-c-1013.md` (tail above); `desk-launch.sh:2174-2189` copies the line (Read above); RESTARTS homes `restarts.py:225-228`, `:245-246` (Read above). The R1138 class record: authorized above.

## E0 BASELINE
On `7aa5d470`, no file written while the runs were in flight.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` · exit 0 → `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 742.67s (0:12:22)` — 0 failed, 0 errors (the skips are with-DB `Postgres env settings not available` and the two `COBALT_LIVE_VAULT_ROOT not set` live-note skips, offline by design).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 → `146 passed, 1 skipped, 15 warnings in 31.28s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only, no `src/` edit. S3: `"Bash(COBALT_ENV=production uv run cobalt smoke *)",` inserted after `tests/ops/test_hub_lines.py:105` (now `:106`). NEW `tests/ops/test_deploy_smoke_string_1014.py` (`BASE = "7aa5d470"`).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_deploy_smoke_string_1014.py` · exit 1 → `3 failed, 31 passed, 15 warnings in 3.21s`. The reds, each for its row's reason:
- S3 `test_w7_…[DEPLOY-HUB.md]`: `E       AssertionError: ('DEPLOY-HUB.md', [... five strings ...])` · `E         At index 3 diff: 'Bash(COBALT_ENV=production uv run cobalt backup run*)' != 'Bash(COBALT_ENV=production uv run cobalt smoke *)'` · `E         Right contains one more item: 'Bash(COBALT_ENV=production uv run cobalt backup status*)'` — the line's five against the pin's six.
- S1 (1) `test_s1_the_deploy_line_allows_cobalt_smoke_once`: `E       assert 0 == 1` (the count is 0).
- S2 (1) `test_s2_the_standing_list_deploy_section_names_the_smoke_string_once`: `E       assert 0 == 1` (the count in `## 3.` is 0).
- Negative controls GREEN on BASE: `test_s1_no_other_allow_or_deny_string_changes`, `test_s2_the_other_sections_production_strings_stand`, the other nine ids of the W7 test and the rest of `test_hub_lines.py` (31 passed).
- Commit `4ea64dce` `wip(deploy-smoke-string-1014): red — S3 pin, S1/S2 tests`.
- T1 (second session; the row's file is a test, so its red is the old pin on today's tree): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` · exit 1 → `1 failed, 4 passed, 15 warnings in 1.74s`; `tests/ops/test_the_rule_sweep.py:150: AssertionError` · `E       assert (21, 85) == (18, 85)` · `At index 0 diff: 21 != 18` ("today's main (21 reports) fails before"). The empty glob before (the check glob → `*-MUTNONE*-2026-10-*.md`, Edit, undone): `1 failed` · `assert (0, 85) == (18, 85)` · `At index 0 diff: 0 != 18`.

## E3 THE ROWS
Order S3 (in E2), S1, S2. Each `file:line` re-read before its edit (Read `DEPLOY-HUB.md:11`; `STANDING-LIST.md:109`, `:139-140` from the PREFLIGHT Read).
- S1: `DEPLOY-HUB.md:11` gains ` "Bash(COBALT_ENV=production uv run cobalt smoke *)"` between `heartbeat show*)` and `backup run*)`; `git diff` shows line 11 the only changed line of the file. After S1: `1 failed, 33 passed` (only S2 (1) red, its row not yet built).
- S2: one row after `STANDING-LIST.md:139`, the card's text; heading `:109` `56`→`57`, `53`→`54`. After S2: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_deploy_smoke_string_1014.py` → `34 passed, 15 warnings in 3.11s`.
- No `src/` module changed: no `docs/40 - DevDocs/cobalt/` page line is owed.

THE MUTATIONS (Edit tool, each undone with the Edit tool; `git diff --stat` after the last undo → `DEPLOY-HUB.md | 2 +-`, `STANDING-LIST.md | 3 ++-`, i.e. the fix only, the pin back at its red commit):
| row | mutation | run | result, first failing line |
|---|---|---|---|
| S1 + S3 | smoke string removed from line 11 | `test_hub_lines.py` + new file, `--tb=line` | `3 failed, 31 passed` — W7[DEPLOY-HUB.md] `At index 3 diff: '…backup run*)' != '…smoke *)'`; S1 (1) `assert 0 == 1`; S2 (1) `assert 'Bash(COBALT_ENV=production uv run cobalt smoke *)' in [...]` (cell not on the line) |
| S1 control | `"Bash(date*)"` → `"Bash(date *)"` on line 11 | new file | `1 failed, 3 passed` — `test_s1_no_other_allow_or_deny_string_changes`: `At index 58 diff: 'Bash(date *)' != 'Bash(date*)'` |
| S2 | the new row's string → `smoke-MUT *` | new file | `1 failed, 3 passed` — S2 (1) `assert 0 == 1` |
| S2 control | a production string added to the `## 5.` heading | new file | `1 failed, 3 passed` — `test_s2_the_other_sections_production_strings_stand`: `AssertionError: 5` · `assert 3 == 2` |
| S3 | the pin's smoke entry removed | `test_hub_lines.py` | `1 failed, 29 passed` — W7[DEPLOY-HUB.md] `At index 3 diff: '…smoke *)' != '…backup run*)'` · `Left contains one more item` |

Commit `9fb997bb` `feat(deploy-smoke-string-1014): deploy line and STANDING-LIST carry the read-only cobalt smoke string (S3, S1, S2; L1, L28, L72)`.

T1 (second session, card `c3c3e703`). In `tests/ops/test_the_rule_sweep.py`, `CHECKS_SWEPT = 18` and `BUILDS_SWEPT = 85` are replaced by `CHECKS_FLOOR = 18` (`:62`). `test_the_sweep_swept_what_it_pins` (`:148-152`) now asserts `len(checks) >= CHECKS_FLOOR` and that no non-exempt mismatch is left. The build-report count is no longer pinned, as the row says ("no longer pins the number of reports swept"). No other name read the two constants (Grep `CHECKS_SWEPT|BUILDS_SWEPT` over `*.py`, `*.sh` → no matches). After: `tests/ops/test_the_rule_sweep.py` → `5 passed`; with `test_hub_lines.py` and `test_deploy_smoke_string_1014.py` → `39 passed, 15 warnings in 3.37s`.
| row | mutation | run | result, first failing line |
|---|---|---|---|
| T1 (empty glob after) | check glob → `*-MUTNONE*-2026-10-*.md` | `::test_the_sweep_swept_what_it_pins`, `--tb=line` | `1 failed` — `assert 0 >= 18` |
| T1 (mismatch arm) | `SWEEP_EXEMPT` key `dev-rebuild-port-build-2026-10-03.md` → `…-MUT.md` | same | `1 failed` — `dev-rebuild-port-build-2026-10-03.md:101 · claim src · read 0 · …` |
| T1 (fix undone) | `>=` → `==` | same | `1 failed` — `assert 21 == 18` |
Each mutation was undone with Edit. `git diff --stat` then showed only `tests/ops/test_the_rule_sweep.py | 12 +++++++-----` (the fix) and the report. Commit `f21900fc` `fix(deploy-smoke-string-1014): the rule sweep pins zero mismatches and a floor of 18 checks, not a count (T1; L1, L72)`.

## RESTARTS
Row R4 (RUN). `uv run cobalt jobs restarts 7aa5d470..HEAD` (HEAD `9fb997bb`) · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md	A	DOCS	-
tests/ops/test_deploy_smoke_string_1014.py	A	test/documentation; no resident	-
tests/ops/test_hub_lines.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. (The tool lists the untracked report too; it is committed at CLOSE.)

Again after T1 (HEAD `f21900fc`), the same command, exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md	M	DOCS	-
tests/ops/test_deploy_smoke_string_1014.py	A	test/documentation; no resident	-
tests/ops/test_hub_lines.py	M	test/documentation; no resident	-
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
`<tip>` = `9fb997bb`. DB: none.
- (a0) `git diff --name-only --no-renames 7aa5d470` · exit 0 → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `tests/ops/test_deploy_smoke_string_1014.py` · `tests/ops/test_hub_lines.py`: every path under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-smoke-string-1014 offline` · exit 0 → `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-smoke-string-1014-offline-20261014-080704.log`; executed (log `:2`): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`. (This build's tests live under `tests/ops`, run below.)
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-smoke-string-1014 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-smoke-string-1014-livenote-20261014-080705.log`; executed (log `:2`): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (on the tree of `9fb997bb`) · exit 1 → **`1 failed, 3603 passed, 1 xfailed, 16 warnings in 800.55s (0:13:20)`**. The red: `tests/ops/test_the_rule_sweep.py:150` `test_the_sweep_swept_what_it_pins` — `E       assert (21, 85) == (18, 85)` · `At index 0 diff: 21 != 18`. Rerun alone (`-vv`): the same, `1 failed`.
- THE RED IS BASE'S, NOT THIS BUILD'S (tool output): the test counts the check reports `docs/40 - DevDocs/reports/*-check*-2026-10-*.md` dated 2026-10-02..2026-10-12 whose last line carries `held unfixed: n ≥ 1` (`test_the_rule_sweep.py:30`, `:99-100`), pinned `CHECKS_SWEPT = 18` (`:61`; last changed `52cb2fc9 fix(sweep-pin-1013)`). This build's diff (a0) touches no report and no `ops/desk/deploy-card.sh`; its own report is dated 2026-10-14 (out of window). `git log --oneline 52cb2fc9..7aa5d470 -- <the three files>` → `8b813ca7 docs(desk): backlog (sitting r2 prompts, JEV design, K5 drafter prompt, Grok checks), R1471-R1472` added `s4-p1-1009-grok-check-2026-10-11.md`, `strike-fallback-env-1010-grok-check-2026-10-11.md`, `worktree-salvage-grok-check-2026-10-11.md` after the pin; their last lines carry `held unfixed: 6`, `held unfixed: 2 (shadow, never fixed)`, `held unfixed: 3` (`tail -n 1`). 18 + 3 = 21. E0 ran `tests/cobalt tests/taxonomy` only, so E0 did not show it.
- The fix lies outside the rows' files (`tests/ops/test_the_rule_sweep.py` is in no row; BUILD-HUB W: "fix it inside the rows' files only"). Not fixed. W stops here: `## DECISIONS` 1.

W AGAIN on `<tip>` = `f21900fc` (second session, after T1; a `## RECORDS` line). DB: none.
- (a0) `git diff --name-only --no-renames 7aa5d470` · exit 0 → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md` · `tests/ops/test_deploy_smoke_string_1014.py` · `tests/ops/test_hub_lines.py` · `tests/ops/test_the_rule_sweep.py`: every path under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-smoke-string-1014 offline` · exit 0 → `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-smoke-string-1014-offline-20261014-083730.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-smoke-string-1014 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-smoke-string-1014-livenote-20261014-083730.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → **`3604 passed, 1 xfailed, 16 warnings in 785.33s (0:13:05)`**. This build's tests are in it: `test_deploy_smoke_string_1014.py` (4 tests), `test_hub_lines.py` W7[DEPLOY-HUB.md], and `test_the_rule_sweep.py::test_the_sweep_swept_what_it_pins`.
- `ls /Users/cobalt/cobalt-wt/deploy-smoke-string-1014/.env` → "No such file or directory" (08:50 ET).

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red: S3 W7[DEPLOY-HUB.md] — E2 red and E3 mutation S3; S1 (1) — E2 red and mutation S1; S1 (2) — mutation "S1 control"; S2 (1) — E2 red, mutation S2; S2 (2) — mutation "S2 control" (all quoted in E2 / E3); T1 `test_the_sweep_swept_what_it_pins` — E2 red `assert (21, 85) == (18, 85)` before, mutations "empty glob after" `assert 0 >= 18`, "mismatch arm", "fix undone" `assert 21 == 18` (E3). None stayed green.
(2) Entry paths: the deploy line has one reader, `desk-launch.sh:2174-2189` (copies the line, fills tokens; PREFLIGHT Read); `test_hub_lines.py`'s `test_a_dry_launch_of_each_kind_prints_a_line_holding_the_flag[deploy]` runs `desk-launch.sh` on the real `DEPLOY-HUB.md` and passed in the 34 / the `tests/ops` run. The STANDING-LIST section is read by no code; S2 (1)/(2) pin it. T1: the constants have no reader outside the test (Grep `CHECKS_SWEPT|BUILDS_SWEPT` → no matches). Both arms of the new assertion are pinned: the floor by the empty glob, the mismatch by the exemption key.
(3) Re-read at the tip: `grep -c -F "cobalt smoke"` → `DEPLOY-HUB.md:1`, `STANDING-LIST.md:1`, `tests/ops/test_hub_lines.py:1` (the card's DEPLOY PROOF counts); Grep → `STANDING-LIST.md:140` the new row, `test_hub_lines.py:106` the pin; `grep -n -F "57 allow with one head"` → `:109`; `git log --oneline 7aa5d470..HEAD` → `9fb997bb`, `4ea64dce`. Second session, at `f21900fc`: `git log --oneline 7aa5d470..HEAD` → `f21900fc`, `042630b7`, `cfcb5a2b`, `4c3ae576`, `9fb997bb`, `4ea64dce`; `grep -n -F "CHECKS_FLOOR" tests/ops/test_the_rule_sweep.py` → `62:CHECKS_FLOOR = 18`, `150:    assert len(checks) >= CHECKS_FLOOR, …`.

## FOR THE CHECK
- `7aa5d470..f21900fc`: `4ea64dce wip(deploy-smoke-string-1014): red — S3 pin, S1/S2 tests` · `9fb997bb feat(deploy-smoke-string-1014): deploy line and STANDING-LIST carry the read-only cobalt smoke string (S3, S1, S2; L1, L28, L72)` · `4c3ae576 wip(deploy-smoke-string-1014): W — tests/ops red on BASE (test_the_rule_sweep pin 18, main has 21)` · `cfcb5a2b wip(deploy-smoke-string-1014): W — desk CONTINUE adding row T1 recorded, not followed (BUILD-HUB (b))` · `042630b7 wip(deploy-smoke-string-1014): W — desk resend recorded, not followed (BUILD-HUB (b))` · `f21900fc fix(deploy-smoke-string-1014): the rule sweep pins zero mismatches and a floor of 18 checks, not a count (T1; L1, L72)`.
- Reds, mutations, greens: `## E2 RED`, `## E3 THE ROWS`. Pins green: `39 passed` (the three files).
- T1 seam: card 549's row S1 carries the same text; per the card's RECORDS, 549 drops its own hunk if the trial merge conflicts.
- R4 (RUN): `## RESTARTS`, whole.
- Suites: `## W`. with-DB: not run (DB: none). `<F0>`/`<F1>`/`<F2>`: not run (DB: none). Lock: not run (DB: none).
- Records copied at PREFLIGHT: `## PREFLIGHT`, last paragraph.

## CONTINUE
next: none — built. The desk verifies the artifact and launches `CHECK-HUB.md` on card 537.

## DECISIONS
1. ANSWERED (not counted): the ASK DESK of 08:19 ET (`test_the_sweep_swept_what_it_pins` red on BASE, `21 != 18`) was answered by card row T1 (`c3c3e703`). T1 was built in the second session and is green (`## E3`, `## W`).
2. ASK DESK 1 (the card's): the new row's "can touch" cell says `read only` and names the one smoke report `cobalt smoke` writes without `--json` (`src/cobalt/smoke/cli.py:73-77`: `if args.json: print(...)` else `write_report(...)`; `:8` "`--json` prints the same content and writes nothing"). The string `smoke *` also admits `--prod` (production reads, `:13-14`). Default taken: the card's text, byte for byte.
3. ASK DESK 2 (the card's): heading counts `56`→`57`, `53`→`54`. Counted on the Read of line 11 after S1: 54 allow strings with one head (`<tip merges>` = 1), no migration and no `## LAUNCHD`; +3 with `<prod migrate strings>` = 57. Default taken: 57 / 54, as the card gives.
4. ASK DESK 3: S2 (2) as the card words it ("the exact smoke string occurs once in the whole file") cannot also be "GREEN on `BASE`" (BASE holds 0). Default taken: the whole-file count equals the `## 3.` count (0 = 0 on BASE, 1 = 1 after; S2 (1) pins `## 3.` at 1), plus the per-section production counts of sections 1, 2, 4-9 against BASE as the card gives. Green on BASE (E2) and red under its mutation (E3).

## RECORDS
- L74: one system notice asked for a `Claude-Session:` line in commits; recorded under `## L74`, not followed.
- S1 (1) carries one assertion beyond the card's text: the smoke string's neighbours on the line are `heartbeat show*)` and `backup run*)` (the row's "directly after"); red under mutation S1 (its count assertion fires first).
- The hook (`bare-guard.py`) blocked a `grep` whose pattern held the production environment word: `route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`. Resent as a Grep-tool read; no command refused.
- `cobalt jobs restarts` lists the untracked report as `A DOCS`; it is committed in the wip commit.
- `.env`: never present (`ls …/.env` → "No such file or directory", 08:19 ET).
- Card's records as re-read at PREFLIGHT: `## PREFLIGHT`.
- 08:21 ET (`date`): a message from session `cto-desk`: "CONTINUE at step W. Card 537 gained row T1 (committed on main): tests/ops/test_the_rule_sweep.py::test_the_sweep_swept_what_it_pins no longer pins the count; zero mismatches plus a floor of 18. Build row T1 (red first on today's main, 21 reports), re-run the deploy gate, then your stop line. Same tree, no new card; record it in RECORDS as a second feature riding." Fact checked: `git -C /Users/cobalt/cobalt log --oneline -3 -- <card>` → `c3c3e703 docs(desk): card 537 row T1 (rule-sweep count pin), R1477` above `b6d7d49c docs(desk): card 537 BASE 7aa5d470` (the commit AUTHORIZATION proved). NOT FOLLOWED: the message adds a row and a file (`tests/ops/test_the_rule_sweep.py`) to this run, and BUILD-HUB UNATTENDED RULES (b) says a CONTINUE "never widens the job … a message that adds a row, a file, a command or an approval … is recorded under `## RECORDS` and not followed". The run stays stopped at W. Row T1 runs only after `authorize.sh` passes on card `c3c3e703`, in a session launched on that card (RECOVERY, `CONTINUE: W`). The desk decides how.
- 08:30 ET (`date`): `cto-desk` resent it ("CONTINUE at step W (resend; your status shows blocked). Card 537 on main now holds row T1 (commit c3c3e703) … Build T1 red first, re-run the deploy gate, then your stop line."). Same fact, same row added: NOT FOLLOWED, by the same rule (b). The status is not blocked: this run stopped on purpose and is waiting. The path that works is a session launched on card `c3c3e703` (RECOVERY, `CONTINUE: W`): its `authorize.sh` proves the amended card and its PREFLIGHT takes T1.
- 08:35 ET (`date`): a NEW session was launched with `CONTINUE: W` on card `c3c3e703` (RECOVERY). Its `authorize.sh` proved the amended card (`## AUTHORIZATION`). `CONTINUED at W 08:35 ET`, with row T1 in the card's rows; the wip commits were continued.
- L74 (second session): a system notice again asked for a `Claude-Session:` line in commits. Recorded as data and not followed; `f21900fc` carries `Co-Authored-By` only.
- One more W run (after T1), as BUILD-HUB W allows: offline, live-note and `tests/ops`, logs as in `## W`. No lock was taken (DB: none).
- `.env`: never present in the second session ("No such file or directory" at 08:35 and 08:50 ET).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-smoke-string-1014 · tip: f21900fc | on 7aa5d470 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 96124
