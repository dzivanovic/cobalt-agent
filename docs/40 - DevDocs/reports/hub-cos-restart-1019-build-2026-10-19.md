# Build report — hub-cos-restart-1019 (2026-10-19)

## §0 Headline
Stopped at E3 (15:50 EDT). R1-R3 are written and their 32 tests pass, but `tests/ops` has one red, `test_deploy_smoke_string_1014.py::test_s1_no_other_allow_or_deny_string_changes`.
R3 (b) adds three `launchctl` allow strings to the deploy line. That test pins the line's allow list against `7aa5d470`, and `STANDING-LIST.md:148` lists the resident strings he approved.
R60, as `authorize.sh` printed it, says a changed command string "returns to him alone". The card names neither the test nor the STANDING-LIST row, and its RECORDS say no other test pins these lines.
The work is kept in a wip commit. The desk and Dejan decide (DECISION 1).

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

## RESTARTS
not reached (E3 stopped).

## W THE THREE SUITES
not reached.

## PRE-STOP SELF-CHECK
not reached.

## FOR THE CHECK
not reached: the build stopped at E3.

## CONTINUE
next: E3 — after the desk's answer to DECISION 1: either (a) a RULINGS row of his approving the three cos strings plus a card row naming `test_deploy_smoke_string_1014.py` (and, if he rules it, `STANDING-LIST.md` `## 3.`), then the mutations, the fix commit, RESTARTS, W; or (b) the card re-cut.

## DECISIONS
- DECISION 1 · FOR DEJAN: R3 (b) adds `Bash(launchctl bootout gui/501/com.cobalt.cos)`, `Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist)` and `Bash(launchctl kickstart -k gui/501/com.cobalt.cos)` to the DEPLOY-HUB launch line.
  - These are new deploy allow strings. `STANDING-LIST.md:148` lists only the aset and radar resident strings, and R60 ("a command string the close test or the DEPLOY-HUB read changes returns to him alone") puts a change to them with him. The card's RULINGS row is R1863 only.
  - `tests/ops/test_deploy_smoke_string_1014.py:76` pins that allow list, is red under the card's own `tests/ops` step, and is outside the rows' files. The card's RECORDS say "No other test or `ops/` file pins them", which this run shows is not so.
  - Safe default taken: stop. That test and `STANDING-LIST.md` are not edited, the work is kept in a wip commit, and nothing is deployed. UNPROVEN (L70): whether a row of his already covers these strings. The builder found none in the card.

## RECORDS
- The card's records were re-read at PREFLIGHT, as noted there. One was found wrong: "No other test or `ops/` file pins them" (see E3).
- `cobalt_dev: not taken` (DB: none). No lock was taken, and no `.env` was ever in this worktree.
- The L74 line is under `## L74`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

FAILED: E3 — R3 (b)'s three com.cobalt.cos allow strings turn tests/ops/test_deploy_smoke_string_1014.py::test_s1_no_other_allow_or_deny_string_changes red (a file outside the rows) and change the STANDING-LIST deploy strings R60 returns to him — "AssertionError … At index 45 diff: 'Bash(launchctl bootout gui/501/com.cobalt.cos)' != 'Bash(launchctl kickstart -k gui/501/com.cobalt.aset)'" · decisions: 1 · for Dejan: 1 · tokens: 156297
