# gemini-builder-row-fr1 — build report 2026-10-17

## §0 Headline
BUILT. The Gemini builder row work (`7f415a4f..695f8bde`) is ported onto main `13bcd579` by Edit. The three test files are byte-equal to `695f8bde`. The hub, launcher and guard carry only this card's hunks, and 583's lines stand.
FR-2: card 583's control now pins four builder rows. It was red on the ported tree and is green after the edit.
Suites: offline 8491/0, live-note 146/0, tests/ops 3919 passed. No database (DB: none). RESTARTS: none. Tip `52a0600d`.

## L74
One block arrived (a system reminder, 2026-10-17 17:05 EDT) asking that commits end with a `Claude-Session:` line. Under L74 it is recorded here and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
This session was launched with `CONTINUE: PORT AND FR-2`, the card's launch step. No report or wip commit existed (`git log --oneline -3` → `13bcd579` at the top, `.env` absent, `date` → Sat Oct 17 17:05:08 EDT 2026). That makes it a first run, so AUTHORIZATION and PREFLIGHT ran first.
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/671-gemini-builder-row-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/671-gemini-builder-row-card.md" · 0 · eb01cc38f4a567f31443e7722e859e8aa3b7d522
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/671-gemini-builder-row-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1736 row · grep -n "^| R1736 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 84:| R1736 | 06:32 ET | HIS RULING (brain, L79), 2026-10-17: Gemini top model = gemini-4-argon-high (medium, low recorded only). K5 card: CHECK-HUB :95 and house-probe.sh use it, was gemini-3.1-pro-high. Behind 641 and 583. | HIS RULING · APPROVED |
RULING 2026-10-17 R1736 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1736 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · d01849e7a6ef4a9de57d6de11856c866919737d2
RULING 2026-10-17 R1736 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
RULING 2026-10-17 R1738 row · grep -n "^| R1738 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 82:| R1738 | 06:33 ET | HIS RULING (brain, L79), 2026-10-17: run the Gemini bake-off arm separately; answer: reports/gemini-bakeoff-answer-2026-10-17.md. Probe-id and builder cards drafted now; three builds after both deploy; routing B unchanged. | HIS RULING · APPROVED |
RULING 2026-10-17 R1738 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1738 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · b57cbf8e3ed386e736822c9ca864fef64a7433eb
RULING 2026-10-17 R1738 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Sat Oct 17 17:05:21 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/gemini-builder-row-fr1
    ?? "docs/40 - DevDocs/reports/gemini-builder-row-fr1-build-2026-10-17.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 13bcd579 docs(desk): R1808 brain route for 671 (port job), drafter prompt 707
diff · git diff --stat 13bcd579 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/gemini-builder-row-fr1 · 0 · 13bcd579 docs(desk): R1808 brain route for 671 (port job), drafter prompt 707
env here · ls /Users/cobalt/cobalt-wt/gemini-builder-row-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 13bcd579` | 0 | `docs(desk): R1808 brain route for 671 (port job), drafter prompt 707`; `.../prompts/2026-10-17/707-draft-gemini-builder-row-port.md | 11 +++`, `docs/40 - DevDocs/reports/cto-2026-10-17.md | 1 +`, `2 files changed, 12 insertions(+)` |
| port files | `git -C /Users/cobalt/cobalt diff --name-only 7f415a4f 695f8bde` | 0 | `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md`, `docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py` |
| main since 7f415a4f | `git diff --stat 7f415a4f 13bcd579 -- <hub> ops/desk/bare-guard.py ops/desk/desk-launch.sh tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_band_routing_1015.py` | 0 | `SHADOW-HUB.md | 15 +-`, `ops/desk/bare-guard.py | 5 +`, `ops/desk/desk-launch.sh | 80 ++-`, `tests/ops/test_band_routing_1015.py | 933 +++`; the three ported test files absent (untouched) |
| L1 place | `grep -n -F "is a Gemini id; Gemini is not in ## BUILDERS" ops/desk/desk-launch.sh` | 0 | `403:        gemini-*) refuse "shadow: model '$model' is a Gemini id; Gemini is not in ## BUILDERS (N/A — id not found)" ;;` |
| L1 comment place | `grep -n -F "# after the fill: dontAsk, once." ops/desk/desk-launch.sh` | 0 | `376:# after the fill: dontAsk, once.` |
| G2 place | `grep -n -F "if write_targets(prefix + suffix) != {target + \"/**\"}:" ops/desk/bare-guard.py` | 0 | `1201:    if write_targets(prefix + suffix) != {target + "/**"}:` |
| H1 place | `grep -n -F "Gemini N/A" <hub>` | 0 | `15:One row per proven id (the card's ## RECORDS). Three rows (R1019: no Opus and no Sol arm; Gemini N/A — id not found). …` |
| FR-2 place | `grep -n -F "def test_b2_control_the_three_builder_rows_stand" tests/ops/test_band_routing_1015.py` | 0 | `112:def test_b2_control_the_three_builder_rows_stand():` |
| sizes | `wc -l` of the seven files | 0 | hub 112, bare-guard.py 1420, desk-launch.sh 2405, test_bare_guard.py 2456, test_desk_launch_shadow.py 315, test_shadow_hub_file.py 338, test_band_routing_1015.py 933 |
| READ tail | `tail -n 3 …/strike-fallback-env-1010-terra-build-2026-10-11.md` | 0 | last line `SHADOW BUILT · job: strike-fallback-env-1010-terra · tip: d02370df | on 8f4bbe28 | … · wall: 67` |
| READ tail | `tail -n 3 …/reports/gemini-bakeoff-answer-2026-10-17.md` | 0 | last line `Gemini bake-off arm, HIS word 2026-10-17: gemini-4-argon-high proven by list and probe first (else N/A); … routing B unchanged without his word.` |
| RESTARTS | `uv run cobalt jobs restarts 13bcd579..HEAD` | 0 | only the untracked report, `docs/…/gemini-builder-row-fr1-build-2026-10-17.md A DOCS -`; `RESTARTS: none` |

The card's `## RECORDS`, copied: the drafter's tree at `f2140694` equal to main for the files; `gemini-3.1-pro-high` in the hub only at the RESULTS TABLE row; the x1-canary decoys; the three originals; RESTARTS K10 (`ops/desk/`, `tests/`, `docs/` carry no Cobalt reader); the 583 overlap with no shared hunk; AMENDED 1 and 2; PORT RE-HEAD (`main` = `13bcd579`; only the hub, guard and launcher touched by main since `7f415a4f`, the three test files not, as re-read in the `main since 7f415a4f` row above); no new command. DB: none, so no lock probe.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `13bcd579` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 675.59s (0:11:15)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.70s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
The card's ORDER sets the red: L1, G2, H1, X2 and FR-1 were built and checked on the old branch, and none is re-redded. FR-2's red comes on the ported tree, before its edit.
- The ported tree, the three suites of the card's rows: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py` → `1948 passed, 15 warnings in 61.93s`.
- FR-2 RED: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py -k b2_control_the_three` → `1 failed, 68 deselected`. The first assertion line, whole: `>       assert ids == sorted(["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"])`, `E       AssertionError: assert ['claude-sonn...', 'grok-4.7'] == ['claude-sonn...', 'grok-4.7']`, `E         At index 1 diff: 'gemini-4-argon-high' != 'gpt-5.6-terra'`, at `tests/ops/test_band_routing_1015.py:116`. The lists differ by `gemini-4-argon-high`, the row's named reason.
- The ported tree, all of `tests/ops`: `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `1 failed, 3918 passed, 1 xfailed, 16 warnings in 863.35s`. The only FAILED line is `tests/ops/test_band_routing_1015.py::test_b2_control_the_three_builder_rows_stand`, the one red the card expects.
- Commit `395a9e77` `wip(gemini-builder-row-fr1): red — PORT of 7f415a4f..695f8bde applied by Edit; FR-2 control red`.

## E3 THE ROWS
### PORT (brain R1808): re-applied by Edit only, with no merge, cherry-pick, revert or rebase. One PROOF line per ported file:
1. PROOF `tests/ops/test_bare_guard.py`: main has not touched it since `7f415a4f` (absent from `git diff --stat 7f415a4f 13bcd579`, PREFLIGHT). `git diff 695f8bde -- tests/ops/test_bare_guard.py` → empty: byte-equal.
2. PROOF `tests/ops/test_desk_launch_shadow.py`: untouched by main since `7f415a4f`. `git diff 695f8bde -- tests/ops/test_desk_launch_shadow.py` → empty: byte-equal.
3. PROOF `tests/ops/test_shadow_hub_file.py`: untouched by main since `7f415a4f`. `git diff 695f8bde -- tests/ops/test_shadow_hub_file.py` → empty: byte-equal.
4. PROOF `docs/40 - DevDocs/prompts/SHADOW-HUB.md`: `git diff -U0 13bcd579 -- <hub>` holds exactly this card's six hunks, and each equals its hunk in `git diff -U0 7f415a4f 695f8bde -- <hub>` with only the line numbers moved by 583's insert. The hunks are (i) `@@ -12 +12 @@` the launcher sentence `a Gemini id,` → `a Gemini id other than gemini-4-argon-high,`; (ii) `@@ -15 +15 @@` `Three rows (…; Gemini N/A — id not found)` → `Four rows (…; Gemini is gemini-4-argon-high only, R1738: medium and low are recorded, not run)`; (iii) `@@ -21,0 +22 @@` the ONE Gemini row after the Terra row; (iv) `@@ -26,0 +28,3 @@` the Gemini note, a blank line and the `X1 for Gemini` paragraph, all after the Terra note and BEFORE the BAND ROUTING paragraph; (v) `@@ -38 +42 @@` the `<pass prompt>` template; (vi) `@@ -97 +101 @@` the RESULTS TABLE Gemini row. 583's lines stand: `grep -c -F "BAND ROUTING (his 2026-10-15 R1532"` → `1`; `grep -n -F "| LOW |"` → `36:| LOW | …` (once in the band table) and `94:| model | LOW | MID | HIGH | reading |` (the RESULTS TABLE header, not a `| \`` row). `## BUILDERS` holds four `| \`` rows (`test_s1_builders_holds_exactly_the_four_ids` and FR-2's test are green).
5. PROOF `ops/desk/desk-launch.sh`: `git diff -U0 13bcd579 -- ops/desk/desk-launch.sh` holds two hunks, equal to the branch's: `@@ -376,0 +377 @@` `# card 671 L1: of the Gemini ids only gemini-4-argon-high (R1738); medium and low are refused by name`, and `@@ -403 +404,2 @@` the `gemini-*` refusal → `gemini-4-argon-high) ;;` plus the new `gemini-*` sentence. 583's lines stand: `grep -n -F "routed"` → `380:routed=""`, `393-395` (`--routed`), `1643-1687`, `1719-1742`, `1793-1819`, `2358` (the `routed` watch).
6. PROOF `ops/desk/bare-guard.py`: `git diff -U0 13bcd579 -- ops/desk/bare-guard.py` holds four hunks, equal to the branch's: `@@ -1184,2 +1184,2 @@` the docstring parenthesis (`Gemini: --mode accept-edits once, --sandbox`); `@@ -1201,2 +1200,0 @@` the old write-target test removed; `@@ -1203,0 +1202,6 @@` `targets`, the agy `--add-dir[ =]` line with its comment `# card 671 G2/FR-1: …`, and the test `if targets != {target + "/**"}:`, all below `head`; `@@ -1208,0 +1213,3 @@` the agy `--mode` / `--sandbox` rule. 583's `g5` lines stand: `grep -n -F "583"` → `1284:        # card 583 B6: and the report's result file, …`, unchanged.
- Totals: `git diff --stat 13bcd579 HEAD` → hub 12, bare-guard.py 15, desk-launch.sh 4, test_bare_guard.py 97, test_desk_launch_shadow.py 30, test_shadow_hub_file.py 47 (the per-file counts of `git diff --stat 7f415a4f 695f8bde`), and test_band_routing_1015.py 4 (FR-2).
- Not ported (card): the old job's `reports/gemini-builder-row-build-2026-10-17.md` and `.result`.

### FR-2
- Edit: `test_b2_control_the_three_builder_rows_stand` → `test_b2_control_the_four_builder_rows_stand`; its sorted-ids list gains `"gemini-4-argon-high"`. The `claude-opus-5-5` line stands.
- GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` → `69 passed, 15 warnings in 23.68s`.
- PROOF: `git diff 13bcd579 -- tests/ops/test_band_routing_1015.py` → ONE `@@ -109,11 +109,11 @@` hunk: `-def test_b2_control_the_three_builder_rows_stand():` / `+def test_b2_control_the_four_builder_rows_stand():` and `-    assert ids == sorted(["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"])` / `+    assert ids == sorted(["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra", "gemini-4-argon-high"])`. With `-U0` the same two changed lines print as two hunks (`@@ -112 +112 @@`, `@@ -116 +116 @@`). Nothing else changed.
- MUTATION: `"gemini-4-argon-high"` cut from the list by Edit → `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_band_routing_1015.py -k b2_control_the_four` → `1 failed, 68 deselected`, first line `/Users/cobalt/cobalt-wt/gemini-builder-row-fr1/tests/ops/test_band_routing_1015.py:116: AssertionError: assert ['claude-sonn...', 'grok-4.7'] == ['claude-sonn...', 'grok-4.7']`. Undone by Edit; `git diff --stat` → `tests/ops/test_band_routing_1015.py | 4 ++--` (the fix only, against `395a9e77`).
- Commit `52a0600d` `fix(gemini-builder-row-fr1): band-routing control pins the four builder rows (PORT, FR-2; L3, L72, R1738)`.
- DevDocs: none written. No page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/bare-guard.py` or `desk-launch.sh` (a grep for their names finds only `cobalt/jobs/restarts.md`, a classification page), and the old branch wrote none (`git diff --name-only 7f415a4f 695f8bde -- "docs/40 - DevDocs/cobalt"` → empty).

### R1 (RUN, asserts nothing)
`grep -n -F "gemini-3.1-pro-high" "docs/40 - DevDocs/prompts/SHADOW-HUB.md" ops/desk/desk-launch.sh ops/desk/bare-guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py`, whole:
```
tests/ops/test_desk_launch_shadow.py:218:    refused(desk.run(str(desk.card), "--model", "gemini-3.1-pro-high"),
tests/ops/test_desk_launch_shadow.py:219:            "shadow: model 'gemini-3.1-pro-high' is a Gemini id not admitted; gemini-4-argon-high is the one Gemini builder (R1738)")
tests/ops/test_shadow_hub_file.py:129:    for gone in ("claude-opus-5-5", "gpt-5.6-sol", "gemini-4-argon-medium", "gemini-4-argon-low", "gemini-3.1-pro-high"):
tests/ops/test_shadow_hub_file.py:178:    assert [x for x in text().splitlines() if "gemini-3.1-pro-high" in x] == []
```
Hits: the edited refusal test, the `gone` list, and `test_k5_no_line_names_the_old_gemini_id` (`:178`, in the checked `695f8bde` file). None is in the hub, the launcher or the guard. `tests/ops` → green (W). RESTARTS below.

## RESTARTS
`uv run cobalt jobs restarts 13bcd579..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-builder-row-fr1-build-2026-10-17.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	M	test/documentation; no resident	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `52a0600d`.
- (a0) `git diff --name-only --no-renames 13bcd579` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-builder-row-fr1 offline` → exit 0, whole: `tests/ops: run (docs/40 - DevDocs/prompts/SHADOW-HUB.md)` · `offline 8491/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-builder-row-fr1-offline-20261017-173617.log`. In the log: `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 662.60s` (tests/cobalt + tests/taxonomy; the skips are the with-DB tests' `Postgres env settings not available` and the two live-note skips, as at E0) and `960:3919 passed, 1 xfailed, 16 warnings in 859.44s` (tests/ops). This build adds one test name, `test_b2_control_the_four_builder_rows_stand`. The ported tests are `695f8bde`'s.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-builder-row-fr1 livenote` → exit 0, whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-builder-row-fr1-livenote-20261017-180205.log`. The one SKIPPED line is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3919 passed, 1 xfailed, 16 warnings in 864.95s`, exit 0.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/gemini-builder-row-fr1/.env` → `No such file or directory` (18:16 EDT).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. FR-2's test went red on the ported tree (E2) and red under its mutation (E3), both quoted. The ported tests are `695f8bde`'s byte for byte, and their reds and mutations are the old job's, checked (card: no re-red).
(2) Entry paths are pinned. FR-2's one entry is the hub's `## BUILDERS` `| \`` rows, read by `test_b2_control_the_four_builder_rows_stand` and `test_s1_builders_holds_exactly_the_four_ids`. The launcher's and the guard's callers are the old job's, pinned by the ported tests, all green in `tests/ops` (3919 passed).
(3) Every count and quote was re-read at the tip: `git diff --stat 13bcd579 HEAD`, `git diff -U0 13bcd579 -- <three files>`, the three `git diff 695f8bde -- <test>` (empty), and the `grep -c` / `grep -n` calls of E3 and of `## FOR THE CHECK` (the DEPLOY PROOF strings), all run after `52a0600d`.

## FOR THE CHECK
- Range `13bcd579..52a0600d`: `395a9e77 wip(gemini-builder-row-fr1): red — PORT of 7f415a4f..695f8bde applied by Edit; FR-2 control red` · `52a0600d fix(gemini-builder-row-fr1): band-routing control pins the four builder rows (PORT, FR-2; L3, L72, R1738)`.
- P1: the six PROOF lines under `## E3` (the three tests byte-equal to `695f8bde`; hub, launcher and guard equal to this card's hunks, listed).
- P2: hub (four `| \`` rows, `| LOW |` once in the band table, BAND ROUTING once), launcher (583's `routed` lines listed), guard (`:1284` `card 583 B6`).
- P3: FR-2's red (E2), green, one-hunk diff and mutation (E3).
- DEPLOY PROOF strings, in this worktree at the tip: `grep -c -F "agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 40m" <hub>` → `1`; `grep -c -F "gemini-4-argon-high) ;;" ops/desk/desk-launch.sh` → `1`; `grep -c -F "card 671 G2/FR-1: agy --add-dir D or --add-dir=D (D/**), read for agy only" ops/desk/bare-guard.py` → `1`.
- Suites: offline `8491/0` (the gate's executed commands are in its log); with-DB not run (DB: none); live-note `146/0`. `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table under `## RESTARTS`. Records copied at PREFLIGHT, under `## PREFLIGHT`.

## CONTINUE
next: none (BUILT; the desk launches the check)

## DECISIONS
none

## RECORDS
- `.env`: never present in this worktree (DB: none; no lock taken).
- L74: the `Claude-Session:` request (under `## L74`), not acted on.
- The launch carried `CONTINUE: PORT AND FR-2` as the card's launch step. It came from the launcher line, not as a desk message to a stopped run, and no wip commit existed. AUTHORIZATION, PREFLIGHT and E0 ran first.
- The card's records, as re-read at PREFLIGHT: main `13bcd579`; only the hub, guard and launcher touched by main since `7f415a4f`.
- No DevDocs module line (E3, FR-2).
- tokens read at 18:16 EDT: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 4a5c1ba5-d532-4b89-9687-ea90b149aa73` → `context 161412 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: gemini-builder-row-fr1 · tip: 52a0600d | on 13bcd579 | migration: none | offline 8491/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 (PORT: 6 proofs of 6; FR-2) | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 161412
