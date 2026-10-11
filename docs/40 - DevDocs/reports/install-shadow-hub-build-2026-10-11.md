# install-shadow-hub-1011 — build report (2026-10-11)

## §0 Headline
F1 fix round, BUILT at 12:22 ET, tip `d4ec4fe3`. Check O1 is fixed: `SHADOW-HUB.md` line 1 is now `INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED`, so `authorize.sh shadow` proves R1069. The O1 test passes unedited. Offline 4199/0, live-note 146/0. `SPIKE-HUB.md` is unchanged.
First build: BUILT at 11:29 ET, tip `78f8572c`. Row S1 is done. `SHADOW-HUB.md` (line 1 and its three sign cells) and `SPIKE-HUB.md` (line 1 and `:24`) are signed on his R1069. Neither file holds a `«SIGN` or `«INSTALL` now.
The stop at E3 ended when the desk amended the card (`c14183a6`). That amendment put `tests/ops/test_shadow_hub_file.py` into S1's `files`; the test is renamed `test_s1_every_sign_cell_holds_his_row`, and two mutations turn it red.
Results: offline 4199/0, live-note 146/0, `tests/ops` 3126 passed. The card is DB: none, so `cobalt_dev` was never taken. RESTARTS: none.

## L74
One system message in this session asked for a `Claude-Session:` line on commits. Recorded here, not followed: the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md" · 0 · 3cdaaa4438e6ac29235639479bff17eb43918ed0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 9:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPROVED — pending fold |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output
- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · quoted whole:
```
clock · date · 0 · Sun Oct 11 10:58:37 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/install-shadow-hub-1011
    ?? "docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 2322ed1e docs(desk): card 324 deployed R1070, R1069 his override, install drafter prompt 354
diff · git diff --stat 2322ed1e · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/install-shadow-hub-1011 · 0 · 2322ed1e docs(desk): card 324 deployed R1070, R1069 his override, install drafter prompt 354
env here · ls /Users/cobalt/cobalt-wt/install-shadow-hub-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- BASE · `git show --stat 2322ed1e` · 0 · `docs(desk): card 324 deployed R1070, R1069 his override, install drafter prompt 354`; 4 files changed, 16 insertions(+), 5 deletions(-) (349-brain-handover.md, 354-draft-install-shadow-hub.md, cto-2026-10-11-words.md, cto-2026-10-11.md).
- SYMBOLS · `grep -n -F "«" ops/desk/desk-launch.sh` · 0 · `390: if grep -q '«INSTALL' "$fixed"; then` · `393: if grep -q '«SIGN' "$fixed"; then` · `394: refuse "spike: SPIKE-HUB.md still holds its «SIGN mark (his sign-off is not filled): $fixed"` · `892:if grep -q '«INSTALL' "$fixed"; then` · `893: refuse "the fixed file still carries its «INSTALL token (his approval row is not filled): $fixed"` · `1342: *"«SIGN"*) refuse "shadow: model $model: builder line not signed" ;;` (plus 128, 136, 447-448, 689, 694-695, 743-744, 910-911: other kinds / «FILL).
- SYMBOLS · Read `desk-launch.sh:1341` · `case "$(printf '%s\n' "$brows" | awk -F'|' '{print $6}')" in` (column 6 = the SIGN cell).
- SYMBOLS · `grep -n -F "«" ops/desk/install-fixed.sh` · 0 · `9:# $REPO/docs/40 - DevDocs/prompts/ whose FIRST line holds the token («INSTALL); it replaces,` · `39:TOKEN = "«INSTALL"`.
- SYMBOLS / CALLERS · `grep -rn -F "SHADOW-HUB" tests ops` · 0 · readers of the real file: `tests/ops/test_shadow_hub_file.py:19` (`SHADOW = PROMPTS / "SHADOW-HUB.md"`, REPO-rooted), `tests/ops/test_desk_launch_shadow.py:23` (`REAL`); constructed only: `test_stop_guard.py:182,197`, `test_bare_guard.py:2121,2202`, `test_authorize.py:296`; scripts: `desk-launch.sh:888`, `stop-guard.py:76`, `preflight.sh:4`, `bare-guard.py:95`, `authorize.sh:51`.
- SYMBOLS / CALLERS · `grep -rn -F "SPIKE-HUB" tests ops` · 0 · reader of the real file: `tests/ops/test_spike_hub_file.py:15`; constructed only: `test_bare_guard.py:2266,2295`, `test_desk_launch_spike.py:68,91`; scripts: `desk-launch.sh:387,394,397,408`, `bare-guard.py:96`.
- SYMBOLS · `grep -n -e SIGN -e INSTALL tests/ops/test_shadow_hub_file.py` · 0 · `21:SIGN = "«" + "SIGN"` · `149:    assert SIGN in builders(text())[model][4]` (in `test_s1_every_sign_cell_holds_the_mark`, `:148`). **This test reads the real file and is not in the row's `files`** → `## DECISIONS` ASK DESK 1.
- SYMBOLS · `grep -n -F "SIGN" tests/ops/test_desk_launch_spike.py` · 0 · `22:SIGN = …` · `149: desk.set_line(…{SIGN}: his row»…)` · `150: refused(…"spike: SPIKE-HUB.md still holds its {SIGN} mark …")` (constructed fixture).
- SYMBOLS · Read `tests/ops/test_desk_launch_shadow.py` · `:208 test_an_unsigned_model_is_refused_beside_a_signed_one`, `:233 test_the_install_title_is_refused`, `:276 test_the_real_file_launches_a_signed_grok`, `:291 refused(desk.run(str(desk.card_for("terra")), "--model", "gpt-5.6-terra"), "shadow: model gpt-5.6-terra: builder line not signed")`; Read `tests/ops/test_spike_hub_file.py:91-92` `test_p1_the_line_waits_for_his_sign_off`.
- READ · SHADOW-HUB.md `:1` ends `«INSTALL: his row»`; `:19`, `:20`, `:21` column 6 `NEEDS HIS SIGN-OFF «SIGN: his row»` (`:21` + ` · network: off (workspace-write default; X1 proves it)`). SPIKE-HUB.md `:1` ends `«INSTALL: his row»`; `:24` `THE LINE'S SIGN: NEEDS HIS SIGN-OFF «SIGN: his row» (R411: …)`.
- WC · `wc -l` · 0 · SHADOW-HUB.md 103 · SPIKE-HUB.md 26 · test_spike_hub_file.py 92 · test_desk_launch_shadow.py 306.
- RECORDS copied (card `## RECORDS`): drafter read against HEAD 2322ed1e; «SIGN on SHADOW-HUB.md lines 19, 20, 21 — re-read, holds; SPIKE-HUB `:1` «INSTALL, `:24` «SIGN — re-read, holds; launcher `:892-893`, `:1341-1342`, `:390-395` — re-read, holds; R1069 row "(`:8`)" — re-read by authorize.sh at **`:9`** (line number differs, row holds HIS RULING · APPROVED, commit 2322ed1e); no preflight ran (his override); authorize.sh serves kind shadow `:51` — re-read, holds; RESTARTS unproven at drafting — run below; BASE/TIP the desk's.
- RESTARTS · `uv run cobalt jobs restarts 2322ed1e..HEAD` · 0 · `docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md	A	DOCS	-` / `RESTARTS: none` (the only path is this untracked report; no code commit in the range).
- DB: none → no lock probe; no with-DB string is used in this build.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 647.61s (0:10:47)`; the one skip naming `COBALT_LIVE_VAULT_ROOT` is `tests/taxonomy/test_predicate.py:262` in the offline run, the live-note run covers it.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.38s`; skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- Extra, on BASE: the row's command plus `tests/ops/test_shadow_hub_file.py` → `127 passed, 15 warnings in 8.89s`.

## E2 RED
Tests written (no `src/` edit): `tests/ops/test_spike_hub_file.py` `test_p1_the_line_waits_for_his_sign_off` → `test_p1_the_line_is_signed_on_his_row`. `tests/ops/test_desk_launch_shadow.py:291`: the Terra refusal becomes `assert terra.returncode == 0`. New: `test_the_real_file_holds_no_install_token_and_no_sign_mark`, with the token and the mark built as `"«" + "INSTALL"` / `"«" + "SIGN"`.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_spike_hub_file.py tests/ops/test_desk_launch_shadow.py` → `3 failed, 23 passed, 15 warnings in 3.70s`:
- `test_p1_the_line_is_signed_on_his_row`: `assert "THE LINE'S SIGN: 2026-10-11 R1069 · HIS RULING · APPROVED (R411:" in '# SPIKE-HUB — …` fails: the new text is missing (the row's reason).
- `test_the_real_file_launches_a_signed_grok`: `AssertionError: REFUSED: shadow: model gpt-5.6-terra: builder line not signed` (the row's reason: the Terra cell still holds the mark).
- `test_the_real_file_holds_no_install_token_and_no_sign_mark`: `AssertionError: SHADOW-HUB.md` / `assert '«INSTALL' not in …`. The card predicted the red on `«SIGN`; it fires first on `«INSTALL` because the test checks the token before the mark. Both are S1's reason. M1 below shows the `«SIGN` red on its own.
Commit `a3627bab wip(install-shadow-hub-1011): red`.

## E3 THE ROWS
S1, by hand (not `install-fixed.sh`), with the Edit tool:
- `SHADOW-HUB.md:1`: the trailing `«INSTALL: his row»` → `HIS RULING · APPROVED 2026-10-11 R1069`. Lines `:19`, `:20`, `:21`, column 6: `NEEDS HIS SIGN-OFF «SIGN: his row»` → `2026-10-11 R1069 · HIS RULING · APPROVED`. `:21` keeps ` · network: off (workspace-write default; X1 proves it)`.
- `SPIKE-HUB.md:1`: the same title change. `:24`: `THE LINE'S SIGN: 2026-10-11 R1069 · HIS RULING · APPROVED (R411: …` (the prose after it stands).
Red-first greps after: `grep -c -F -e "«SIGN"` → SHADOW-HUB 0, SPIKE-HUB 0. `«INSTALL` → 0, 0. `2026-10-11 R1069 · HIS RULING · APPROVED` → SHADOW-HUB 3, SPIKE-HUB 1. `git diff --numstat` → `4 4 SHADOW-HUB.md`, `2 2 SPIKE-HUB.md`. `wc -l` → 103, 26.
The row's command (`uv run pytest -q tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_spike.py tests/ops/test_spike_hub_file.py tests/ops/test_authorize.py tests/ops/test_install_fixed.py`) → `85 passed, 15 warnings in 8.74s`.
The test file beside them, `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_shadow_hub_file.py` → **`3 failed, 40 passed`**: `test_s1_every_sign_cell_holds_the_mark[grok-4.7|claude-sonnet-5-5|gpt-5.6-terra]`, `tests/ops/test_shadow_hub_file.py:149: AssertionError: assert '«SIGN' in '2026-10-11 R1069 · HIS RULING · APPROVED'`. → ASK DESK 1; the run stops here.
MUTATIONS (Edit tool, each undone):
- M1, the mark back in the `:21` Terra cell → `2 failed, 24 passed`: `test_desk_launch_shadow.py:292: AssertionError: REFUSED: shadow: model gpt-5.6-terra: builder line not signed` and `:300: AssertionError: SHADOW-HUB.md` (`'«SIGN' not in …`).
- M2, the mark back on `SPIKE-HUB.md:24` → `2 failed, 24 passed`: `test_desk_launch_shadow.py:300: AssertionError: SPIKE-HUB.md` (`'«SIGN' not in …`) and `test_spike_hub_file.py:93` (the new text missing).
- M3, the token back on `SPIKE-HUB.md:1` → `1 failed, 25 passed`: `test_desk_launch_shadow.py:299: AssertionError: SPIKE-HUB.md` (`'«INSTALL' not in …`).
- Undone: `git diff --stat` → `SHADOW-HUB.md | 8 ++++----`, `SPIKE-HUB.md | 4 ++--`, `2 files changed, 6 insertions(+), 6 deletions(-)` (the fix).
- No DevDocs module line: no `src/` module changed.

E3, after `CONTINUE: E3` (11:17 ET; the card at `c14183a6` names `tests/ops/test_shadow_hub_file.py` in S1's `files`):
- `tests/ops/test_shadow_hub_file.py:148` `test_s1_every_sign_cell_holds_the_mark` → `test_s1_every_sign_cell_holds_his_row`: `cell = builders(text())[model][4]`; `assert "2026-10-11 R1069 · HIS RULING · APPROVED" in cell`; `assert SIGN not in cell` (`SIGN = "«" + "SIGN"`, `:21`).
- The new test was not run on BASE: the fix was already committed in the wip commits. M4 puts BASE's cell text back, so it shows the BASE red. Mutations:
  - M4, `SHADOW-HUB.md:19` cell back to `NEEDS HIS SIGN-OFF «SIGN: his row»` → `1 failed, 2 passed, 40 deselected`: `tests/ops/test_shadow_hub_file.py:150: AssertionError: assert '2026-10-11 R1069 · HIS RULING · APPROVED' in 'NEEDS HIS SIGN-OFF «SIGN: his row»'`.
  - M5, `:19` cell `2026-10-11 R1069 · HIS RULING · APPROVED «SIGN: his row»` (ruling kept, mark added) → `1 failed, 2 passed, 40 deselected`: `tests/ops/test_shadow_hub_file.py:151: AssertionError: assert '«SIGN' not in '2026-10-11 ...GN: his row»'`.
  - Undone with the Edit tool: `git diff --numstat 2322ed1e` on the hubs → `4 4 SHADOW-HUB.md`, `2 2 SPIKE-HUB.md`.
- The row's command, now with `tests/ops/test_shadow_hub_file.py` (`uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_spike.py tests/ops/test_spike_hub_file.py tests/ops/test_shadow_hub_file.py tests/ops/test_authorize.py tests/ops/test_install_fixed.py`) → `128 passed, 15 warnings in 8.67s`.
- Commit `78f8572c feat(install-shadow-hub-1011): SHADOW-HUB and SPIKE-HUB installed and signed on his R1069 (S1, L28, L77)`. The hub and test edits from before the stop are in wip commits `af5ab4bb` / `d9e5cf5a`, and the tip holds them all.

### F1 — fix round for check O1 (after `CONTINUE: FIX ROUND row F1`, 12:09 ET)
- Red first. `test_f1_the_real_title_passes_the_authorize_line_one_gate` is new in `tests/ops/test_shadow_hub_file.py`. It builds a tmp repo as `COBALT_REPO_ROOT`, the shape of `test_authorize.py`'s `desk`, with a constructed R1069 row. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_authorize.py::test_check_o1_the_real_shadow_title_names_its_standing_row tests/ops/test_shadow_hub_file.py::test_f1_the_real_title_passes_the_authorize_line_one_gate` on `f6d698ab` + the new test → `2 failed, 15 warnings in 0.96s`:
  - O1: `tests/ops/test_authorize.py:317: AssertionError`, with stdout `STANDING LIST · sed -n 1p … · 1 · the title names no INSTALL: <date> R<n>: # SHADOW-HUB — … HIS RULING · APPROVED 2026-10-11 R1069` and `FAILED: authorization mismatch — STANDING LIST`.
  - F1: `tests/ops/test_shadow_hub_file.py:310: AssertionError: assert '# SHADOW-HUB...6-10-11 R1069' == 'INSTALL: 202...NG · APPROVED'`. This is the line-1 equality. The `STANDING LIST 2026-10-11 R1069 row` assert sits after it and is not reached on this tree.
  - Commit `f2177888 wip(install-shadow-hub-1011): F1 red`.
- Fix, Edit tool: `SHADOW-HUB.md:1` → `INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED` (the whole line).
- Greens: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_authorize.py tests/ops/test_shadow_hub_file.py` → `72 passed, 15 warnings in 3.88s`. S1's other files, `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_spike.py tests/ops/test_spike_hub_file.py tests/ops/test_install_fixed.py` → `58 passed, 15 warnings in 5.83s`.
- Row greps:
  - `grep -c -F -e "INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED"` on SHADOW-HUB.md → `1`.
  - `grep -c -F -e "«INSTALL"` → `0`.
  - `wc -l` → `103`.
  - `git diff --numstat 2322ed1e -- …SHADOW-HUB.md` → `4	4`.
  - `git diff --stat 78f8572c -- …SPIKE-HUB.md` → empty.
- M6, Edit tool: line 1 `«INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED` (a `«` before INSTALL) → `2 failed`:
  - `test_authorize.py:317`: `the title names no INSTALL: <date> R<n>: «INSTALL: …`, `FAILED: authorization mismatch — INSTALLED`.
  - `test_shadow_hub_file.py:310`: `assert '«INSTALL: 20...NG · APPROVED' == 'INSTALL: 202...NG · APPROVED'`.
  - Undone with the Edit tool. `git diff --stat` then showed only `SHADOW-HUB.md` (the fix) and this report.
- Commit `d4ec4fe3 fix(install-shadow-hub-1011): SHADOW-HUB line 1 names its INSTALL row for authorize.sh (F1, O1, L77)`.
- The O1 test was not edited: `git diff --stat f6d698ab HEAD -- tests/ops/test_authorize.py` → empty. `grep -n -F "def test_check_o1_the_real_shadow_title_names_its_standing_row" tests/ops/test_authorize.py` → `309:def test_check_o1_the_real_shadow_title_names_its_standing_row(desk):`. `git show --stat f6d698ab` → `tests/ops/test_authorize.py | 11 +++++++++++`. The check's O1 line (`install-shadow-hub-check-2026-10-11.md:5`: "the installed title … has none" of `INSTALL: <date> R<n>`) matches the test's assertion (`"the title names no INSTALL: <date> R<n>" not in done.stdout`), and the test passes at `d4ec4fe3` (the 72 passed above).

## RESTARTS
F1, `uv run cobalt jobs restarts 2322ed1e..HEAD` at `d4ec4fe3` → the same table as below, plus `tests/ops/test_authorize.py	M	test/documentation; no resident	-`; last line `RESTARTS: none`. No UNCLASSIFIED row.

First build, `uv run cobalt jobs restarts 2322ed1e..HEAD` → quoted whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/SPIKE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md	M	DOCS	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
tests/ops/test_spike_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
F1 fix round, `<tip>` = `d4ec4fe3` (the deploy gate's pass for a DB: none card, the card's F1 row):
- (a0) `git diff --name-only --no-renames 2322ed1e` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/prompts/SPIKE-HUB.md`, `docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md`, `tests/ops/test_authorize.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`, `tests/ops/test_spike_hub_file.py`. Every path starts with `docs/` or `tests/ops/`, so **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh install-shadow-hub-1011 offline` → exit 0, `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/install-shadow-hub-1011-offline-20261011-121109.log`. Executed (`:2`): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `:879` `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 624.90s (0:10:24)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh install-shadow-hub-1011 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/install-shadow-hub-1011-livenote-20261011-122146.log`. `:57` `146 passed, 1 skipped, 15 warnings in 25.20s`. Its one skip (`:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `tests/ops`: per the card, the fix round reran only the fixed part's tests (`## E3` F1: 72 passed + 58 passed). With-DB: not run (DB: none). No re-check (L75).

First build, `<tip>` = `78f8572c`.
- (a0) `git diff --name-only --no-renames 2322ed1e` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/prompts/SPIKE-HUB.md`, `docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`, `tests/ops/test_spike_hub_file.py`. Every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh install-shadow-hub-1011 offline` → exit 0, `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/install-shadow-hub-1011-offline-20261011-111823.log`. Executed (`:2`): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `:879` `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 639.64s (0:10:39)`. Skips naming `COBALT_LIVE_VAULT_ROOT` (`:620` test_radar_evaluate.py:695, `:697` test_s3_c4_experiments.py:95, `:877` test_catalyst.py:365, `:878` test_predicate.py:262). These are the offline run's live-note skips, and the BASE run had the same count (E0). No test this build adds runs in this suite: the added and renamed tests are all in `tests/ops`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0, `3126 passed, 1 xfailed, 15 warnings in 588.01s (0:09:48)`. This run holds the build's tests: `test_the_real_file_holds_no_install_token_and_no_sign_mark`, `test_p1_the_line_is_signed_on_his_row`, `test_s1_every_sign_cell_holds_his_row[×3]`, and the changed `test_the_real_file_launches_a_signed_grok`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh install-shadow-hub-1011 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/install-shadow-hub-1011-livenote-20261011-112916.log`. Executed (`:2`): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `:57` `146 passed, 1 skipped, 15 warnings in 25.24s`. Its skip (`:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` and does not name `COBALT_LIVE_VAULT_ROOT`.
- With-DB: not run (DB: none). (b)–(d), (f): not run (DB: none).

## PRE-STOP SELF-CHECK
F1:
- (1) The O1 test and `test_f1_…` were both red at F1's E2 (`:317`, `:310`) and again under M6.
- (2) `authorize.sh` is line 1's one reader with an INSTALL gate. The check's O7 grep names only `desk-launch.sh` and `authorize.sh`. `test_f1_…` pins it on the real title, and `test_desk_launch_shadow.py` (58 passed) pins `desk-launch.sh`'s token gate on the real file.
- (3) Re-read at `d4ec4fe3`: the greps, `wc -l`, numstat and `grep -n` in `## E3` F1.

First build:
(1) Each added or changed test was red for its reason. `test_p1_the_line_is_signed_on_his_row` failed at E2 (new text missing) and under M2. `test_the_real_file_launches_a_signed_grok` (Terra launch passes) failed at E2 (`REFUSED: … gpt-5.6-terra: builder line not signed`) and under M1. `test_the_real_file_holds_no_install_token_and_no_sign_mark` failed at E2 (`«INSTALL`) and under M1 / M2 / M3. `test_s1_every_sign_cell_holds_his_row` failed under M4 (`:150`, ruling missing) and M5 (`:151`, mark present). No test stayed green under its mutation.
(2) Every entry path is pinned. The callers grep from PREFLIGHT names two readers of the real `SHADOW-HUB.md` and one of `SPIKE-HUB.md`; the other hits use constructed fixtures:
  - `test_shadow_hub_file.py:19` is pinned by `test_s1_every_sign_cell_holds_his_row`.
  - `test_desk_launch_shadow.py:23` (`REAL`) is pinned by `test_the_real_file_launches_a_signed_grok` (Terra) and by `test_the_real_file_holds_no_install_token_and_no_sign_mark`.
  - `test_spike_hub_file.py:15` is pinned by `test_p1_the_line_is_signed_on_his_row`.
  - The launcher's three refusals stay pinned on constructed fixtures (`test_desk_launch_shadow.py:208`, `:233`, `test_desk_launch_spike.py:148`), all green in the row's run (128 passed).
(3) Re-read at tip `78f8572c`:
  - `grep -c -F -e "«SIGN"` → SHADOW 0, SPIKE 0; `«INSTALL` → 0, 0.
  - `grep -c -F -e "2026-10-11 R1069 · HIS RULING · APPROVED"` → 3, 1.
  - `wc -l` → 103, 26.
  - `git diff --numstat 2322ed1e` on the hubs → 4/4, 2/2.
  - `grep -n -F "def test_" tests/ops/test_shadow_hub_file.py` → `:148 def test_s1_every_sign_cell_holds_his_row(model):`.

## FOR THE CHECK
- Range `2322ed1e..78f8572c`: `a3627bab wip(install-shadow-hub-1011): red` · `af5ab4bb wip(install-shadow-hub-1011): E3 — test_shadow_hub_file.py pins the sign mark, outside the row's files` · `d9e5cf5a wip(install-shadow-hub-1011): E3 — CONTINUE widens files by message; card unchanged` · `78f8572c feat(install-shadow-hub-1011): SHADOW-HUB and SPIKE-HUB installed and signed on his R1069 (S1, L28, L77)`.
- S1 reds: `## E2 RED`. Mutations: M1–M3 (`## E3`, first session) and M4–M5 (`## E3`, after CONTINUE). Greens: 128 passed (row command), `tests/ops` 3126 passed.
- Caller greps: `## PREFLIGHT` SYMBOLS / CALLERS.
- RUN rows: none on this card.
- Suites: `## W` (executed commands quoted there). With-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT` RECORDS line.
- F1: range `78f8572c..d4ec4fe3`: `09768202 docs(…): build report — 78f8572c` · `f6d698ab wip(…): check red — O1` · `f2177888 wip(install-shadow-hub-1011): F1 red` · `d4ec4fe3 fix(install-shadow-hub-1011): SHADOW-HUB line 1 names its INSTALL row for authorize.sh (F1, O1, L77)`. Reds, mutation M6 and greens: `## E3` F1. Suites: `## W` F1.
- For X1: line 21 keeps ` · network: off (workspace-write default; X1 proves it)` (Read `SHADOW-HUB.md:21` at E3).

## CONTINUE
next: none (BUILT after the F1 fix round). The desk verifies the artifact. No re-check (L75).

## DECISIONS
none

## RECORDS
- ASK DESK 1 (settled by the card at `c14183a6`, no longer open) [11:12 ET]: `tests/ops/test_shadow_hub_file.py::test_s1_every_sign_cell_holds_the_mark` (`:147-149`, `assert SIGN in builders(text())[model][4]`) reads the tree's real `SHADOW-HUB.md` and pins the unsigned state. It fails for all three ids once S1 lands, and it would fail W's `tests/ops`. The row's `files` and `## READ` do not name it, and the card's X3 asks exactly this question. The fix is outside the row's files: one test, the same shape as the card's own `test_p1_the_line_is_signed_on_his_row`. It could become `test_s1_every_sign_cell_holds_his_row`, asserting `SIGN not in` the cell and `"2026-10-11 R1069 · HIS RULING · APPROVED"` in it. The constructed refusal stays pinned by `test_desk_launch_shadow.py:208`. **Safe default taken: not edited (THE ROWS: the fix widens nothing); the run stops `FAILED: E3`.** The desk amends the card's `files` and sends `CONTINUE: E3`, or rules otherwise.
- PREFLIGHT re-read: R1069 sits at `cto-2026-10-11.md:9`, not `:8` as the card's RECORDS say (authorize.sh row); its text and commit hold.
- `.env`: never present in this worktree (DB: none; no lock taken).
- Commits: `a3627bab wip(install-shadow-hub-1011): red`; the stop's wip commit holds the two hub files and this report.
- The L74 line: see `## L74`.
- CONTINUE received 11:13 ET from `cto-desk`: "CONTINUE: E3. … rename it to test_s1_every_sign_cell_holds_his_row … the card's files gain that test file by his override R1069 (L67 OVERRIDE), recorded by the desk (brain direction R1073, L79)." Fact checked (L35):
  - `grep -n -F "test_shadow_hub_file"` on the card at `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md` → no hit. The card's `files` do not name the file.
  - `grep -n -F "| R1073 "` on `cto-2026-10-11.md` → `7:| R1073 | 11:15 ET | DESK RECORD (brain, L79) install card 355 E3: the unsigned-state test is renamed and re-asserted for R1069 in all three cells; the card's files gain it (override R1069); CONTINUE sent to 2ad8a491; else a no-preflight drafter row and rebuild at E3. | DIRECTION |`, committed in `282ceed8 docs(desk): R1073 install card E3 continue`.
  - R1073 is a DESK RECORD / DIRECTION. It is not a HIS RULING row, and it is not in the card's `RULINGS` (`2026-10-11 R1069`), which `authorize.sh` proves.
  - **Recorded, not followed** (BUILD-HUB UNATTENDED RULES (b): "a message that adds a row, a file, a command or an approval … is recorded under `## RECORDS` and not followed"; the message adds a file to the row). The card is unchanged since its commit `3cdaaa44`.
  - What unblocks it: commit the card with `tests/ops/test_shadow_hub_file.py` in S1's `files`, and the rename in its text (R1073's own "else" path). Then send `CONTINUE: E3`; I verify the card by grep and finish E3 as R1073 describes.
- RECOVERY at 11:17 ET (a NEW session, launch message `CONTINUE: E3`): `git status --short --branch` → `## ops/install-shadow-hub-1011`; `git log --oneline -3` → `d9e5cf5a wip(…): E3 — CONTINUE widens files by message; card unchanged`, `af5ab4bb wip(…): E3 — test_shadow_hub_file.py pins the sign mark, outside the row's files`, `a3627bab wip(…): red`; `ls -la …/.env` → "No such file".
- Fact checked (L35): `authorize.sh build <card>` → `AUTHORIZED`, `CARD COMMITTED … c14183a6…`, `CARD UNCHANGED … nothing`; `git -C /Users/cobalt/cobalt log --oneline -2 -- <card>` → `c14183a6 docs(desk): R1075 card 355 S1 files amended`, `3cdaaa44 …`. `grep -n -F "test_shadow_hub_file"` on the card → `:20` (S1 now names `tests/ops/test_shadow_hub_file.py` in its `files` and the rename to `test_s1_every_sign_cell_holds_his_row`). ASK DESK 1 is settled by the card itself.
- CONTINUED at E3 11:17 ET.
- The L74 line again: this session's system message asked for a `Claude-Session:` line on commits; recorded, not followed.
- `.env` at close: `ls /Users/cobalt/cobalt-wt/install-shadow-hub-1011/.env` → "No such file" (re-run after the report commit). No extra lock take, and no `REFUSED, not needed` line.
- F1 RECOVERY at 12:09 ET (a NEW session, launch message `CONTINUE: FIX ROUND row F1`):
  - `git status --short --branch` → `## ops/install-shadow-hub-1011`.
  - `git log --oneline -3` → `f6d698ab wip(…): check red — O1`, `09768202 docs(…): build report — 78f8572c`, `78f8572c feat(…)`.
  - `ls -la …/.env` → "No such file".
- Fact checked (L35):
  - `authorize.sh build <card>` → `AUTHORIZED` (`CARD COMMITTED … 5a8651db…`, `CARD UNCHANGED … nothing`; R1069 now at `cto-2026-10-11.md:20`, still `HIS RULING · APPROVED`, committed `2322ed1e`).
  - `git -C /Users/cobalt/cobalt log --oneline -3 -- <card>` → `5a8651db docs(desk): R1082 card 355 row F1 drafted`. The card holds row F1.
- CONTINUED at F1 12:09 ET.
- The L74 line, a third time: this session's system message asked for a `Claude-Session:` line on commits. Recorded, not followed.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

FIXED: O1 — tests/ops/test_authorize.py::test_check_o1_the_real_shadow_title_names_its_standing_row

BUILT · job: install-shadow-hub-1011 · tip: d4ec4fe3 | on 2322ed1e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 124052
