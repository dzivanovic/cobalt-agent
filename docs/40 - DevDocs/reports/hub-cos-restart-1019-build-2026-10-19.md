# Build report — hub-cos-restart-1019 (2026-10-19)

## §0 Headline
BUILT at `d59fac71` on the re-cut card (`29250739`). STEP-R now admits `com.cobalt.cos`; a cos that is not loaded is skipped and named by no `launchctl` call after D1; a loaded cos stops the run at STEP-R.
No allow string, `STANDING-LIST.md` or `desk-launch.sh` changed, and `test_deploy_smoke_string_1014.py` is green.
Suites: offline `8822/0`, live-note `147/0`, `tests/ops` `4073 passed`, with-DB not run (DB: none). RESTARTS: none.
The first attempt stopped `FAILED: E3` at 15:50 EDT on the old R3's allow strings. The re-cut dropped them.

## L74
- One system-reminder in this session asks commits to end with a `Claude-Session:` line. Recorded here once, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · 1c3042150a6e8af18a75d5f53913dd3054257a06
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
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| BASE | `git show --stat bcbf08f9` | 0 | `bcbf08f9 docs(desk): F16 deploy FAILED at STEP-R cos, K5 hub-cos-restart drafter 868 R2068 R2069` · `868-draft-hub-cos-restart.md | 7 +++++++`, `cto-2026-10-19.md | 7 +++++--` · `2 files changed, 12 insertions(+), 2 deletions(-)` |
| restarts, empty range | `uv run cobalt jobs restarts bcbf08f9..HEAD` | 0 | one row, `docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md A DOCS -` (this report, untracked) · `RESTARTS: none` |
| symbol `loop stamping` | `grep -n -F "loop stamping" src/cobalt/heartbeat/probes.py` | 0 | `164:    return Probe("cos", True, f"loop stamping ({stale:.0f}s ago)")` |
| symbol `<radar pid>` (D1) | `grep -n -F "<radar pid>" DEPLOY-HUB.md` | 0 | `122:- \`launchctl print gui/501/com.cobalt.aset\` → … \`<radar pid>\`; …` (one hit) |
| cos `enabled: false` | `grep -n -F "enabled: false" configs/cobalt/jobs.yaml` | 0 | `214:    enabled: false` |
| `desk-launch.sh:1918` | Read `ops/desk/desk-launch.sh` 1860-1920 | — | `1865: agent|aset|radar) refuse …`; `1918: launchd="$launchd \"Bash(launchctl bootout gui/501/$lab)\" \"Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/$lab.plist)\""` |
| hub's readers | `grep -rln -F "DEPLOY-HUB" tests` | 0 | 20 `.py` files under `tests/ops` and `tests/cobalt/test_validate_no_db.py` (the `tests/ops` run of R3 covers them) |
| `wc -l` | `wc -l DEPLOY-HUB.md test_hub_deferred_1018.py test_desk_launch_launchd.py` | 0 | `187` · `108` · `240` |
| READ report tail | `tail -n 3 reports/deploy-f16-close-fr2.md` | 0 | `FAILED: RESTARTS — src/cobalt/taxonomy/loader.py → com.cobalt.cos (RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar; com.cobalt.cos outside agent/aset/radar) · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 93484` |
| F16 RESTARTS | Read `reports/deploy-f16-close-fr2.md` 61-80 | — | `:75 src/cobalt/taxonomy/loader.py M static import reach com.cobalt.aset,com.cobalt.cos,com.cobalt.radar` · `:77 RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` · `:79` set minus `<deferred set>` (empty) holds `com.cobalt.cos` → FAILED (STEP-R) |

`preflight.sh` output:
```
clock · date · 0 · Mon Oct 19 15:19:11 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/hub-cos-restart-1019
    ?? "docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · bcbf08f9 docs(desk): F16 deploy FAILED at STEP-R cos, K5 hub-cos-restart drafter 868 R2068 R2069
diff · git diff --stat bcbf08f9 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/hub-cos-restart-1019 · 0 · bcbf08f9 docs(desk): F16 deploy FAILED at STEP-R cos, K5 hub-cos-restart drafter 868 R2068 R2069
env here · ls /Users/cobalt/cobalt-wt/hub-cos-restart-1019/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- The card's `## RECORDS`, copied: drafter `draft-hub-cos-restart` (868) 15:10 EDT, BASE `bcbf08f9`; `main`'s hub 188 lines, `:93` GATE within the three, `com.cobalt.cos` nowhere in it; `deploy-f16-close-fr2.md:74-79` (re-read above: `:75`, `:77`, `:79`); `ops/com.cobalt.cos.plist` Label `com.cobalt.cos`, bootstrapped by 4.6L-BO from `/Users/cobalt/cobalt/ops/com.cobalt.<label>.plist` (`desk-launch.sh:1918`, re-read above); `/Users/cobalt/.claude/ops/desk-launch.sh` a link (not re-read); `deploy-outage.sh:90,109`, `deploy-step0.sh:73` name cos, `orphan-clean.sh:76-82` aset only (not re-read: no row edits them); tests pinning the changed lines `test_hub_deferred_1018.py:17,:57,:74,:105`, `test_desk_launch_launchd.py:143-181`, `:160` (re-read: Read of both files); BAND HIGH; RESTARTS (K10) docs/tests → no resident; ORDER before the F16 relaunch.
- Re-read note: the worktree hub is 187 lines by `wc -l` (the card's "188 lines" counts the last line without a newline differently; the content of `:93`, `:122`, `:139`, `:143`, `:149`, `:153`, `:154` matched the card's quotes on Read).
- DB: none card: no lock probe, no with-DB string used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `4749 passed, 871 skipped, 4 xfailed, 36 warnings in 726.31s (0:12:06)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.86s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
- NEW `tests/ops/test_hub_cos_restart_1019.py` on BASE's hub: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_cos_restart_1019.py` → `3 failed, 2 passed, 15 warnings in 0.85s` (the card's `3 failed, 2 passed`). The two CONTROLs `test_c1_a_label_outside_the_four_is_refused` and `test_c2_no_launchctl_call_names_a_label_outside_the_four` pass on BASE. The reds:
  - `test_r1_the_f16_set_is_admitted` → `AssertionError: assert False is True` · `where False = admits({'com.cobalt.aset', 'com.cobalt.cos', 'com.cobalt.radar'})` (the span is the three).
  - `test_r2_a_not_loaded_cos_is_skipped_and_acts_on_nothing` → `AssertionError: no \`- NOT LOADED\` line`.
  - `test_r3_cos_is_restarted_after_radar` → `assert '\`com.cobalt.aset\`, \`com.cobalt.radar\`, \`com.cobalt.cos\` in \`<restart set>\`' in '4.2 for each of \`com.cobalt.aset\`, \`com.cobalt.radar\` in \`<restart set>\`: …'` (the 4.2 assert).
- Existing pins changed (`test_hub_deferred_1018.py:17` THREE → the four labels, `:74` → `admits({AGENT, ASET, HERDR}, set()) is False`, `:105` → `launch.count(COS) == 3`; `test_desk_launch_launchd.py:143` `TODAY_EIGHT = 8` → `TODAY_ELEVEN = 11`, uses `:149`, `:166`, `:181`). The three files on BASE's hub with `--tb=line` → `9 failed, 23 passed`: the 3 above; `test_hub_deferred_1018.py:57: AssertionError: com.cobalt.agent com.cobalt.aset com.cobalt.radar` ×2 (`rule()`'s span pin); `test_hub_deferred_1018.py:105: assert 0 == 3`; `test_desk_launch_launchd.py:149` / `:166` / `:181`: `assert 8 == 11`.
- Commit `7d05ffe0 wip(hub-cos-restart-1019): red — R1-R3 hub pins, the existing pins moved to the four (tests only)`.

## E3 THE ROWS
- R1 (`:93` GATE span → the four + `(any of the four, or none; \`com.cobalt.cos\` then passes NOT LOADED below)`): `test_hub_cos_restart_1019.py` + `test_hub_deferred_1018.py` → `4 failed, 6 passed`. The admit passes; `test_r1`'s second clause (the NOT LOADED line, `:60`) waits on R2, and R2 / R3 / `:105` are still red.
- R2 (the new `- NOT LOADED` line after `:93`, D1 `:122` → now `:123`, smoke (f) `:154` → now `:155`): the same two files → `2 failed, 8 passed` (R3's `:93` and `test_hub_deferred_1018.py:105` left).
- R3 (`:3`, `:11`, `:78`, `:94` → `:95`, `:139` → `:140`, `:143` → `:144`, `:149` → `:150`, `:153` → `:154`): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py tests/ops/test_desk_launch_launchd.py` → `32 passed, 15 warnings in 12.04s`.
- The card's whole-`tests/ops` run: `uv run pytest -q -p no:cacheprovider --color=no tests/ops` (background) → `1 failed, 4073 passed, 1 xfailed, 16 warnings in 893.10s (0:14:53)`:
```
FAILED tests/ops/test_deploy_smoke_string_1014.py::test_s1_no_other_allow_or_deny_string_changes
>       assert [s for s in tools(line, "--allowedTools") if s != SMOKE] == tools(then, "--allowedTools")
E         At index 45 diff: 'Bash(launchctl bootout gui/501/com.cobalt.cos)' != 'Bash(launchctl kickstart -k gui/501/com.cobalt.aset)'
E         Left contains 3 more items, first extra item: 'Bash(tail *)'
tests/ops/test_deploy_smoke_string_1014.py:76: AssertionError
```
  That test (`BASE = "7aa5d470"`, `:18`) compares the deploy line's whole allow list, minus the smoke string, with `7aa5d470`'s. `grep -n -F "launchctl kickstart -k gui/501/com.cobalt.radar" STANDING-LIST.md` → `148:| \`Bash(launchctl kickstart -k gui/501/com.cobalt.aset)\` · \`Bash(launchctl kickstart -k gui/501/com.cobalt.radar)\` | one retry for a resident loaded but not running | those two services | — |`.
- `git diff --stat bcbf08f9` → `DEPLOY-HUB.md | 23 +++---`, `test_desk_launch_launchd.py | 8 +--`, `test_hub_cos_restart_1019.py | 119 +++`, `test_hub_deferred_1018.py | 6 +-` (`4 files changed, 138 insertions(+), 18 deletions(-)`).
- Not done: THE MUTATIONS, the fix commit, a DevDocs line. No `src/` module changes, so there is no `docs/40 - DevDocs/cobalt/` page to write; the hub is a prompt file.

## E2 / E3 AFTER THE RE-CUT (card `29250739`, rows R1-R2, R3 a stop)
- The desk's message (from `cto-desk`, 15:59 EDT) named E3 and the re-cut card. I checked the fact myself: `git -C /Users/cobalt/cobalt log --oneline -2 -- <card>` → `29250739 docs(desk): card 869 re-cut to rows 1-2, preflight 874 R2076`. `authorize.sh build <card>` ran again → `CARD COMMITTED · … · 292507398e7cbe69bc71d90f4c1a2ec871d03bd1`, `CARD UNCHANGED · … · nothing`, R60 and R1863 rows as before, `AUTHORIZED`. I read the card whole.
- The message narrows the job and adds nothing: drop the old R3. I removed it with Edit, not a git reset (no reset string is listed).
  - From the hub: the MODEL `:3` cos label, the three cos allow strings on `:11`, `:78` "three" back to "two", the `:94` cos sentence, 4.2 / 4.6 / smoke (a) / smoke (e) cos text.
  - From the tests: `test_hub_deferred_1018.py:105` back to `assert COS not in launch`; `test_desk_launch_launchd.py` back to `TODAY_EIGHT = 8` (it has no diff against BASE now); in the new file, `test_r3_cos_is_restarted_after_radar` and `test_c2_…` removed.
- New R3: the NOT LOADED line's `Exit 0` sentence now reads the card's refusal. NEW `test_c3_a_loaded_cos_still_refuses` checks that the line holds `FAILED: RESTARTS — com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60), they are asked of Dejan · rollback: not used`, that it does not hold `com.cobalt.cos loaded <state or path>`, and that the `claude --bg ` line holds no `com.cobalt.cos`.
- After the edits: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py tests/ops/test_desk_launch_launchd.py tests/ops/test_deploy_smoke_string_1014.py` → `35 passed, 15 warnings in 12.84s`.
- The red without the fix (BASE's GATE span, NOT LOADED line renamed): `3 failed, 1 passed, 15 warnings in 0.78s`.
  - Red: `test_r1_the_f16_set_is_admitted` (`:54: AssertionError: assert False is True … admits({'com.cobalt.aset', 'com.cobalt.cos', 'com.cobalt.radar'})`), `test_r2_…` (`:71: AssertionError: no \`- NOT LOADED\` line`), `test_c3_…` (`:90: AssertionError: no \`- NOT LOADED\` line`). The CONTROL `test_c1_…` passes.
  - This is the card's `3 failed, 1 passed`. It was run on the worktree hub with those two places mutated, not on a literal copy of BASE's hub: D1 `:123` and smoke (f) `:155` kept their R2 text, and no assert checked before the first failing one reads them. `test_c1` also passed on BASE's literal hub at the first E2 (above), with the same body.
- THE MUTATIONS, each undone with Edit:
  - R1: GATE span back to the three → `3 failed, 6 passed` (`test_hub_cos_restart_1019.py:54` `assert False is True`; `test_hub_deferred_1018.py:57` `AssertionError: com.cobalt.agent com.cobalt.aset com.cobalt.radar` ×2).
  - R2 (c): smoke (f) back to BASE → `1 failed, 3 passed` (`:83: assert 'not loaded — skipped' in "- (f) …"`).
  - R3: the refusal back to the old "keeps it in `<restart set>`" sentence → `1 failed, 3 passed` (`:91: AssertionError: assert 'FAILED: RESTARTS — com.cobalt.cos is loaded; …' in '- NOT LOADED …'`).
  - After undoing: `git diff --stat bcbf08f9` → `DEPLOY-HUB.md | 7 +-`, report `| 118 +++`, `test_hub_cos_restart_1019.py | 93 +++`, `test_hub_deferred_1018.py | 4 +-`. This is the same stat as before the mutations.
- Commit `d59fac71 fix(hub-cos-restart-1019): STEP-R admits cos, a not-loaded cos is skipped, a loaded cos stops the run; no allow string (R1-R3, L42, R60)` (`4 files changed, 26 insertions(+), 52 deletions(-)`).
- DevDocs line: none. No `src/` module changed; the hub is a prompt file.

## RESTARTS
`uv run cobalt jobs restarts bcbf08f9..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md	M	DOCS	-
tests/ops/test_hub_cos_restart_1019.py	A	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames bcbf08f9` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md`, `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`. Every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-1019 offline` (background) → exit 0:
```
tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)
offline 8822/0
log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-1019-offline-20261019-160117.log
```
  The log's two summaries (`grep -n -F " passed"`): `947:4749 passed, 871 skipped, 4 xfailed, 36 warnings in 746.66s` · `1021:4073 passed, 1 xfailed, 16 warnings in 908.44s`. This build adds `test_r1_the_f16_set_is_admitted`, `test_c1_a_label_outside_the_four_is_refused`, `test_r2_a_not_loaded_cos_is_skipped_and_acts_on_nothing` and `test_c3_a_loaded_cos_still_refuses`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `4073 passed, 1 xfailed, 16 warnings in 896.37s (0:14:56)`, exit 0. `test_deploy_smoke_string_1014.py` is green, so the allow list is unchanged.
- with-DB: not run (DB: none).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-1019 livenote` → `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-1019-livenote-20261019-162908.log`. Its one skip (`grep -n -F "SKIPPED"`): `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
1. Every added or changed test was shown red for its named reason.
   - `test_r1`, `test_r2` and `test_c3` were red without the fix, and each was red under its own mutation (all quoted above).
   - `test_c1` is a control: it passed on BASE and passes after.
   - `test_hub_deferred_1018.py:17` / `:74` were red on BASE (`:57`, first E2) and under the R1 mutation (`:57` ×2).
2. Every entry path is pinned:
   - STEP-R GATE `:93`: `test_r1`, `test_c1`, `test_hub_deferred_1018` d1 tests.
   - NOT LOADED `:94`, both exits: `test_r2` (not loaded) and `test_c3` (loaded).
   - D1 `:123`: `test_r2`.
   - Smoke (f) `:155`: `test_r2`. STEP-5 (4) re-runs (f) by reference, so it needs no own pin.
   - The launch line has no cos: `test_c3` and `test_hub_deferred_1018.py:105`.
   - The allow list is unchanged: `test_deploy_smoke_string_1014.py` (green), plus the empty `git diff bcbf08f9 --stat -- ops/desk/ STANDING-LIST.md test_deploy_smoke_string_1014.py test_desk_launch_launchd.py`.
3. Every `file:line` was re-read at the tip: `grep -n -F "com.cobalt.cos" DEPLOY-HUB.md` → `:93`, `:94`, `:123` only; `git show --stat d59fac71`; `git log --oneline bcbf08f9..HEAD`.

## FOR THE CHECK
- Range `bcbf08f9..d59fac71`:
  - `7d05ffe0 wip(hub-cos-restart-1019): red — R1-R3 hub pins, the existing pins moved to the four (tests only)`
  - `bb5332c3 wip(hub-cos-restart-1019): E3 — R3 (b) allow strings red in test_deploy_smoke_string_1014, outside the rows; FOR DEJAN`
  - `d59fac71 fix(hub-cos-restart-1019): STEP-R admits cos, a not-loaded cos is skipped, a loaded cos stops the run; no allow string (R1-R3, L42, R60)`
  - The two wip commits carry the old R3, and `d59fac71` removes it. Read the net diff `git diff bcbf08f9 d59fac71`, not the commits one by one.
- Hub changes at the tip: `:93` (the GATE span and its parenthesis), the new `:94` NOT LOADED line, D1 `:123` (the cos insertion), smoke (f) `:155`. The `Anything else (…)` sentence stands byte for byte; the full diff is quoted at E3.
- An observation, not a decision: the card kept R2 (b)'s D1 clause `com.cobalt.cos in <restart set>: … <cos pid>`. With R3 a loaded cos stops at STEP-R, so cos never reaches D1 inside `<restart set>`, and that clause cannot run. It is the card's text (L72), and I did not re-decide it.
- Reds, mutations and greens: under E2, E3 and `## E2 / E3 AFTER THE RE-CUT`. Callers: the grep above.
- Suites: offline `8822/0`, live-note `147/0`, with-DB not run (DB: none). F0 / F1 / F2 and the lock times: not run (DB: none).
- The RESTARTS table and the card's records (PREFLIGHT) are copied above.

## CONTINUE
next: none — the stop line is below.

## DECISIONS
none

## RECORDS
- Stopped once at 15:50 EDT: `FAILED: E3 — R3 (b)'s three com.cobalt.cos allow strings turn test_deploy_smoke_string_1014.py red and change the STANDING-LIST deploy strings R60 returns to him` (decisions: 1 · for Dejan: 1 · tokens: 156297). That DECISION 1 was answered by the card's re-cut (`29250739`): no cos allow string is added, and a loaded cos stops the run at STEP-R. Asking Dejan for those strings is the desk's job, apart from this card.
- CONTINUED at E3 15:59 EDT, on the `cto-desk` message, after checking the re-cut card myself (above).
- The card's records were re-read at PREFLIGHT. The first card's line "No other test or `ops/` file pins them" was wrong, and the re-cut card's `:64` records that.
- `cobalt_dev: not taken` (DB: none). No lock was taken; no `.env` was in this worktree at any point (`ls` → No such file, 15:50 EDT and at CLOSE).
- The L74 line is under `## L74`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: hub-cos-restart-1019 · tip: d59fac71 | on bcbf08f9 | migration: none | offline 8822/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 204595
