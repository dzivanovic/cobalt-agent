# install-shadow-hub-1011 — build report (2026-10-11)

## §0 Headline
Stopped at E3, 11:12 ET. Row S1 is built and its tests pass (85 passed). All three mutations go red as they should.
`tests/ops/test_shadow_hub_file.py::test_s1_every_sign_cell_holds_the_mark` (`:148`) reads the real `SHADOW-HUB.md` and asserts each sign cell still holds the mark. It fails three times after S1, and the file is not in the row's `files`.
The fix is one test the card does not name, so it widens the job: ASK DESK 1. The rows and the reds are in wip commits. No suite was run at W.

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

## RESTARTS
(pending)

## W THE THREE SUITES
(pending)

## PRE-STOP SELF-CHECK
(pending)

## FOR THE CHECK
(pending)

## CONTINUE
next: E3. Settle ASK DESK 1, finish the E3 commit (`fix(install-shadow-hub-1011): …`), then RESTARTS, then W as a DB: none card ((a0), (a), (e), `tests/ops`).

## DECISIONS
- ASK DESK 1 [11:12 ET]: `tests/ops/test_shadow_hub_file.py::test_s1_every_sign_cell_holds_the_mark` (`:147-149`, `assert SIGN in builders(text())[model][4]`) reads the tree's real `SHADOW-HUB.md` and pins the unsigned state. It fails for all three ids once S1 lands, and it would fail W's `tests/ops`. The row's `files` and `## READ` do not name it, and the card's X3 asks exactly this question. The fix is outside the row's files: one test, the same shape as the card's own `test_p1_the_line_is_signed_on_his_row`. It could become `test_s1_every_sign_cell_holds_his_row`, asserting `SIGN not in` the cell and `"2026-10-11 R1069 · HIS RULING · APPROVED"` in it. The constructed refusal stays pinned by `test_desk_launch_shadow.py:208`. **Safe default taken: not edited (THE ROWS: the fix widens nothing); the run stops `FAILED: E3`.** The desk amends the card's `files` and sends `CONTINUE: E3`, or rules otherwise.

## RECORDS
- PREFLIGHT re-read: R1069 sits at `cto-2026-10-11.md:9`, not `:8` as the card's RECORDS say (authorize.sh row); its text and commit hold.
- `.env`: never present in this worktree (DB: none; no lock taken).
- Commits: `a3627bab wip(install-shadow-hub-1011): red`; the stop's wip commit holds the two hub files and this report.
- The L74 line: see `## L74`.

FAILED: E3 — tests/ops/test_shadow_hub_file.py::test_s1_every_sign_cell_holds_the_mark reads the real SHADOW-HUB.md and asserts the sign mark; it is red after S1 and is not in the row's files — ASK DESK 1
