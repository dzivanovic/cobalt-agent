# Build report — hub-cos-restart-fr1 (card 869, row PORT) — 2026-10-19

## §0 Headline
- BUILT. PORT of card 869: `d59fac71`'s net change was re-applied by Edit/Write onto `c68efd65`. Tip `0bf28619`.
- PROOF: all 3 files (`DEPLOY-HUB.md`, `test_hub_cos_restart_1019.py`, `test_hub_deferred_1018.py`) are byte-equal to `d59fac71`. No merge commit, and the old report is not ported.
- Suites: offline 8822/0, live-note 147/0, `tests/ops` 4073 passed. DB: none, so the with-DB passes are the deploy gate's own.
- Markers on the hub: 2 / 1 / 0, matching the card's `after` values. RESTARTS: none. Decisions: 0.

## L74
- One system-reminder asked commits to carry a `Claude-Session:` line. Recorded here; not followed (BUILD-HUB L74: `Co-Authored-By` only).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · d3760950a87809c823551f8491bfcef6f961d07f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 19 18:23:45 EDT 2026
status · git status --short --branch · 0 · ## ops/hub-cos-restart-fr1
head · git log --oneline -1 · 0 · c68efd65 docs(desk): K5 port card 869 re-headed hub-cos-restart-fr1 (drafter 523522f0 DRAFTED), preflight prompt 882, R2097
diff · git diff --stat c68efd65 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/hub-cos-restart-fr1 · 0 · c68efd65 docs(desk): K5 port card 869 re-headed hub-cos-restart-fr1 (drafter 523522f0 DRAFTED), preflight prompt 882, R2097
env here · ls /Users/cobalt/cobalt-wt/hub-cos-restart-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat c68efd65` | 0 | `docs(desk): K5 port card 869 re-headed hub-cos-restart-fr1 …`; 4 files, all `docs/40 - DevDocs/` (card 869, prompt 882, cto-2026-10-19.md, draft-hub-cos-fr1 report), 47+ / 9- |
| PORT stat (card: re-run first) | `git diff --stat bcbf08f9 c68efd65 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py` | 0 | (empty) — main has not touched the three files since bcbf08f9; the revert `2acf267a` restored them whole |
| PORT files | `git diff --name-only bcbf08f9 d59fac71` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md` (not ported) · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py` |
| symbol `:93` | Grep `within \`com.cobalt.agent com.cobalt.aset com.cobalt.radar\`` on DEPLOY-HUB.md | — | `93:` (the `- GATE: exit 0` line) |
| symbol `:94` | Grep `^- THE SET DRIVES THE REST` | — | `94:` |
| symbol `:122` | `grep -n -F "<radar pid>" DEPLOY-HUB.md` | 0 | `122:- \`launchctl print gui/501/com.cobalt.aset\` → … \`<radar pid>\`; \`/Users/cobalt/cobalt/cobalt.sh status\` → …` |
| symbol `:154` | Grep `minus \`<deferred set>\` (as \`## RESTARTS\` records it)` | — | `154:- (f) \`COBALT_ENV=production uv run cobalt validate\` → as 4.5 · … \`RESTARTS:\` minus \`<deferred set>\` (as \`## RESTARTS\` records it) = STEP-R's \`<restart set>\`, no \`UNCLASSIFIED\`.` |
| symbol `:11` | Grep `^claude --bg ` | — | `11:` |
| pins `test_hub_deferred_1018.py` | Grep | — | `17:THREE = "com.cobalt.agent com.cobalt.aset com.cobalt.radar"` · `54:def rule()` · `61:def admits(` · `69:` · `74:    assert admits({AGENT, ASET, COS, RADAR}, set()) is False` · `105:    assert COS not in launch` |
| wc | `wc -l DEPLOY-HUB.md tests/ops/test_hub_deferred_1018.py` | 0 | `187` · `108` |
| READ report | `tail -n 3 "docs/40 - DevDocs/reports/deploy-f16-close-fr2.md"` | 0 | last line: `FAILED: RESTARTS — src/cobalt/taxonomy/loader.py → com.cobalt.cos (RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar; com.cobalt.cos outside agent/aset/radar) · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 93484` |
| RESTARTS | `uv run cobalt jobs restarts c68efd65..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |
| lock | DB: none | — | no lock probe |

Card records copied (re-read where the list can): drafter 868 BASE `bcbf08f9`; drafter 871 re-cut on build stop `FAILED: E3`; drafter 881 PORT BASE header `5b71dec9` (the card's BASE is now `c68efd65`, preflight's `head` row); `git diff --name-only bcbf08f9 d59fac71` re-read above (4 paths, as recorded); `git diff --stat bcbf08f9 <BASE> -- <three>` re-read above (empty, as recorded); marker fix: marker 1 after `2`, marker 2 after `1`, marker 3 after `0` (re-read at W).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `c68efd65` → `4749 passed, 871 skipped, 4 xfailed, 36 warnings in 730.51s (0:12:10)`; 0 failed, 0 errors. Skips: `Postgres env settings not available`, `reaches cobalt_dev (lock-relief G1)`, and two `COBALT_LIVE_VAULT_ROOT not set` (the live-note run covers those).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.98s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
The two test files were written byte-equal to `d59fac71` (the new file by Write from `git show d59fac71:tests/ops/test_hub_cos_restart_1019.py`; `test_hub_deferred_1018.py` by two Edits, `:17` `THREE` and `:74` control, as `git diff bcbf08f9 d59fac71` shows). They ran on BASE's hub:
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py` → `5 failed, 4 passed, 15 warnings in 0.91s`:
- `test_r1_the_f16_set_is_admitted`: `AssertionError: assert False is True … where False = admits({'com.cobalt.aset', 'com.cobalt.cos', 'com.cobalt.radar'})`. The row's reason: the span holds three labels.
- `test_r2_a_not_loaded_cos_is_skipped_and_acts_on_nothing`: `AssertionError: no \`- NOT LOADED\` line`. The row's reason.
- `test_c3_a_loaded_cos_still_refuses`: `AssertionError: no \`- NOT LOADED\` line`. The row's reason.
- `test_d1_card_730s_set_is_admitted` and `test_d1_a_label_outside_the_three_not_deferred_is_refused` (the `:17` pin): `AssertionError: com.cobalt.agent com.cobalt.aset com.cobalt.radar` at `rule()` `:57` (`- om.cobalt.cos com.cobalt.radar` / `+ om.cobalt.radar`). The row's reason: `THREE` now names the four.
- CONTROL `test_c1_a_label_outside_the_four_is_refused`: PASSED on BASE (the `.` in position 2 of `F.FFFF...`).
New file alone: 3 failed, 1 passed, as the card's R3 states.
Commit `049520c9` `wip(hub-cos-restart-fr1): red — PORT tests from d59fac71 (R1-R3)`. No RUN row. DB: none, so no with-DB red and no lock.

## E3 THE ROWS
PORT: three Edits to `DEPLOY-HUB.md`, each re-found by its content: `:93` span, the new `- NOT LOADED` line after it, `:122`→`:123` D1, and `:154`→`:155` smoke (f). The text is copied from `git diff bcbf08f9 d59fac71`.
- PROOF, per file: `git diff --stat d59fac71 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py` → empty, so 3 of 3 files are byte-equal to `d59fac71`. Re-run at the tip as `git diff d59fac71 0bf28619 -- <three>` → empty.
- Greens: `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_cos_restart_1019.py` → `4 passed, 15 warnings in 0.78s`. `uv run pytest -q -p no:cacheprovider tests/ops` → `4073 passed, 1 xfailed, 16 warnings in 924.60s (0:15:24)`.
- Markers (DEPLOY PROOF, worktree hub): `grep -c -F "com.cobalt.cos: not loaded — skipped"` → `2`; `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)"` → `1`; `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos"` → `0`.
- MUTATIONS (Edit tool, each undone):
  - M1 (R1): span back to the three → `3 failed, 6 passed` (tests/ops/test_hub_cos_restart_1019.py + test_hub_deferred_1018.py). Red: `test_r1…`, `test_d1_card_730s_set_is_admitted`, `test_d1_a_label_outside_the_three_not_deferred_is_refused`. First line: `test_hub_cos_restart_1019.py:54: AssertionError: assert False is True`.
  - M2 (R2 (b)): D1's cos clause removed → `1 failed, 3 passed`. Red: `test_r2_…`, `:80: assert '<cos pid>' in "- \`launchctl print gui/501/com.cobalt.aset\` …"`.
  - M3 (R3): the `- NOT LOADED` exit-0 sentence back to R2's old `com.cobalt.cos loaded <state or path>` refusal → `1 failed, 3 passed`. Red: `test_c3_…`, `:91: AssertionError: assert 'FAILED: RESTARTS — com.cobalt.cos is loaded; … (R60) …' in '- NOT LOADED …'`.
  - MC (control break): `com.cobalt.herdr` added to the span → `1 failed, 3 passed`. Red: `test_c1_…`, `:61: AssertionError: assert True is False … admits({'com.cobalt.aset', 'com.cobalt.herdr'})`.
  - After the undos: `git diff --stat d59fac71 -- <three>` → empty. Hub readers `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py tests/ops/test_hub_lines.py tests/ops/test_hub_text_1013.py tests/ops/test_deploy_smoke_string_1014.py` → `47 passed, 15 warnings in 2.91s`.
- Commit `0bf28619` `fix(hub-cos-restart-fr1): STEP-R admits cos, skips it when not loaded, refuses it when loaded — port of d59fac71 (PORT, R1-R3, L79, R60)`.

## RESTARTS
`uv run cobalt jobs restarts c68efd65..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.md	A	DOCS	-
tests/ops/test_hub_cos_restart_1019.py	A	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `0bf28619`.
- (a0) `git diff --name-only --no-renames c68efd65` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-fr1 offline` → exit 0:
  ```
  tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)
  offline 8822/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-fr1-offline-20261019-185411.log
  ```
  In the log: `947:4749 passed, 871 skipped, 4 xfailed, 36 warnings in 770.03s (0:12:50)` and `1021:4073 passed, 1 xfailed, 16 warnings in 911.07s (0:15:11)`. 4749 + 4073 = 8822. Tests this build adds: `test_r1_the_f16_set_is_admitted`, `test_c1_a_label_outside_the_four_is_refused`, `test_r2_a_not_loaded_cos_is_skipped_and_acts_on_nothing`, `test_c3_a_loaded_cos_still_refuses` (tests/ops/test_hub_cos_restart_1019.py).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-fr1 livenote` → exit 0: `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-fr1-livenote-20261019-185412.log`. Its one SKIPPED line (`:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4073 passed, 1 xfailed, 16 warnings in 907.79s (0:15:07)`.
- The card's own suite (`## DEPLOY PROOF` hub-cos-restart tests line): `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_cos_restart_1019.py` → `4 passed, 15 warnings in 0.78s` (E3).
- The deploy gate's pass on the ported tree: this card is `DB: none`, so BUILD-HUB W (a0) runs offline and live-note only and `--deploy` is not typed. The with-DB passes stay with the deploy gate, under its dev lock (PORT: "say which"). with-DB here: `not run (DB: none)`.
- `ls /Users/cobalt/cobalt-wt/hub-cos-restart-fr1/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every test was shown red: r1, r2 and c3 red on BASE (E2) and under M1, M2 and M3 respectively; c1 green on BASE and red under MC. Both `test_hub_deferred_1018.py` d1 tests were red on BASE and under M1. No test stayed green under its mutation.
(2) Entry paths. The hub's readers are tests only. The STEP-R GATE span is pinned by r1, c1 and `test_hub_deferred_1018.py` `rule()` `:57`. The NOT LOADED line is pinned by r1 (count 1), r2 (position directly after GATE, the print, the plist path, no bootout/bootstrap/kickstart) and c3 (the R60 refusal). D1 `:123` is pinned by r2 (`<cos pid>`, `loaded since STEP-R`). Smoke (f) `:155` is pinned by r2; STEP-5 (4) re-runs (f). The launch line `:11` with no cos is pinned by c3 and `test_hub_deferred_1018.py:105`.
(3) Re-read at the tip: Grep on DEPLOY-HUB.md → `93:- GATE: exit 0`, `94:- NOT LOADED`, `123:<cos pid>`, `155:minus a label \`## RESTARTS\` records`. `git diff d59fac71 0bf28619 -- <three>` → empty. The marker `grep -c` calls → 2 / 1 / 0. `git log --merges --oneline c68efd65..HEAD` → empty.

## FOR THE CHECK
- `c68efd65..0bf28619`: `049520c9 wip(hub-cos-restart-fr1): red — PORT tests from d59fac71 (R1-R3)` · `0bf28619 fix(hub-cos-restart-fr1): STEP-R admits cos, skips it when not loaded, refuses it when loaded — port of d59fac71 (PORT, R1-R3, L79, R60)`.
- P1 PROOF: `git diff d59fac71 0bf28619 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py` → empty, so 3 of 3 files are byte-equal to `d59fac71`. The old build report `hub-cos-restart-1019-build-2026-10-19.md` is not in `git diff --name-only c68efd65`. `git log --merges --oneline c68efd65..HEAD` → empty. Main had not touched the three files since `bcbf08f9` (`git diff --stat bcbf08f9 c68efd65 -- <three>` → empty), so no hunk was folded.
- Per row, the reds, mutations and greens are under E2 and E3 above. No RUN row.
- Suites: offline 8822/0, live-note 147/0, `tests/ops` 4073 passed (W). with-DB: `not run (DB: none)`. F0/F1/F2: `not run (DB: none)`. Lock taken/released: `not run (DB: none)`.
- RESTARTS table: under `## RESTARTS` (`RESTARTS: none`).
- The records copied at PREFLIGHT are under `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- L74: one system-reminder asked commits to carry a `Claude-Session:` line. It is recorded under `## L74` and was not followed.
- DevDocs dated line: none written. The changed file is a hub prompt, not a module with a page under `docs/40 - DevDocs/cobalt/`. PORT also fixes the diff at the three files of `d59fac71`, and `d59fac71` holds no such line.
- The card's records were re-read at PREFLIGHT: `git diff --name-only bcbf08f9 d59fac71` (4 paths) and `git diff --stat bcbf08f9 c68efd65 -- <three>` (empty). The marker counts were re-read at E3 (2 / 1 / 0).
- Stop-line PROOF count: carried inside the `rows` field (`proof 3 of 3 byte-equal to d59fac71`), so the result file keeps BUILD-HUB's fixed keys.
- Extra lock takes: none (DB: none). REFUSED: none. CONTINUED: none.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: hub-cos-restart-fr1 · tip: 0bf28619 | on c68efd65 | migration: none | offline 8822/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: PORT 1 of 1 (R1-R3), proof 3 of 3 byte-equal to d59fac71 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 127555
