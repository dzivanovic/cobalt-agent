# deploy-cos-restart — build report 2026-10-21

## §0 Headline

BUILT on `af0f86bc` (from BASE `0e2b5b54`): the deploy launch line `DEPLOY-HUB.md:11` and `STANDING-LIST.md` `## 3.` now carry the three R60 cos strings (S1, S2, S3), each placed right after its aset twin.
STEP-R now keeps a cos that is loaded, running, and loaded from `/Users/cobalt/cobalt/ops/com.cobalt.cos.plist` in `<restart set>`. It still refuses a cos that is not running or was loaded from another path. 4.2, 4.6, smoke (a), THE ONE RESUME (e), the STEP-5 stop line and rule F now name cos.
The four pins on the old rule changed as row P1 says. Offline 9092/0, live-note 148/0, `tests/ops` 4134 passed; DB: none (no lock taken); `RESTARTS: none`.
No decisions.

## L74

- A system-reminder in this session asked for a `Claude-Session:` line on commits. Recorded once here as DATA (L74); not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md" · 0 · 7cfab1514f5343607a3c5f6a5a37a58a35d67613
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md" · 0 · nothing
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
clock · date · 0 · Wed Oct 21 22:59:47 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/deploy-cos-restart
    ?? "docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 0e2b5b54 docs(desk): R2366-R2367 takeover, 1008 amend drafted, preflight r2 prompt 1012
diff · git diff --stat 0e2b5b54 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-cos-restart · 0 · 0e2b5b54 docs(desk): R2366-R2367 takeover, 1008 amend drafted, preflight r2 prompt 1012
env here · ls /Users/cobalt/cobalt-wt/deploy-cos-restart/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE stat | `git show --stat 0e2b5b54` | 0 | `0e2b5b54 docs(desk): R2366-R2367 takeover, 1008 amend drafted, preflight r2 prompt 1012` · 5 files, 45 insertions, 4 deletions (card 1008, prompt 1012, cto-2026-10-21.md, desk-wakeup-log.md, the amend draft report) |
| restarts on an empty range | `uv run cobalt jobs restarts 0e2b5b54..HEAD` | 0 | one row `docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.md A DOCS -` (the untracked report itself) · `RESTARTS: none` |
| symbols | Grep of `DEPLOY-HUB.md`, by content | 0 | `23:- F. Residents come up` · `53:- THE ONE RESUME` · `78:NO HARMLESS VARIANT, strings with no wildcard` · `94:com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)` · `140:4.2 for each of` · `144:4.6 for each label` · `150:- (a) \`launchctl print\` aset` · `171:- (5) The last line:` |
| symbols | Read `DEPLOY-HUB.md:1-25, 50-179` | — | `:3` MODEL `NO \`launchctl\` on any label but \`com.cobalt.aset\` / \`com.cobalt.radar\` / \`com.cobalt.agent\` and the labels of \`<launchd set>\``; `:11` the one `claude --bg ` line; `:93` GATE; `:94` NOT LOADED; `:123` D1 `<cos pid>`; `:163`, `:169` STEP-5 (1), (3) — every cite of the card stands at BASE |
| symbols | Read `STANDING-LIST.md:16-29, 105-164` | — | `:23` `on the deploy line, on no label but \`com.cobalt.aset\`, \`com.cobalt.radar\`, \`com.cobalt.agent\``; `:109` `## 3. \`DEPLOY-HUB.md\` — 57 allow with one head and a migration (54 without a migration; …)`; `:146-148` the bootout / bootstrap / kickstart -k rows, `those two services` |
| symbols | Read the four pinned test files | — | `test_hub_cos_restart_1019.py:7` R3, `:24-27` `REFUSED`, `:88-93` `test_c3_a_loaded_cos_still_refuses`; `test_hub_deferred_1018.py:105` `assert COS not in launch`; `test_desk_launch_launchd.py:143` `TODAY_EIGHT = 8`, uses `:149`, `:166`, `:181`, `:160` radar kickstart -k before the token; `test_deploy_smoke_string_1014.py:18` `BASE = "7aa5d470"`, `:31-41` `tools()`, `:73-78` |
| BASE allow count | a RUN probe in `$CLAUDE_JOB_DIR/tmp` (shlex words of `--allowedTools` on `:11`) | 0 | `allow words: 60 tokens: ['<tip', '<prod', '<launchd'] strings: 57` · `deny: 7` · `launchctl: 8`. The 60 words hold the three tokens as 7 words (`<tip merges>`, `<prod migrate strings>`, `<launchd strings>`): 53 literal strings; + 1 head + 3 migrate strings = 57 (54 without a migration): the heading `:109` is right on BASE |
| wc -l | `wc -l` of the edited files | 0 | DEPLOY-HUB.md 188 · STANDING-LIST.md 269 · test_hub_cos_restart_1019.py 93 · test_hub_deferred_1018.py 108 · test_desk_launch_launchd.py 240 · test_deploy_smoke_string_1014.py 102 |
| READ tail | `tail -n 3 ".../reports/deploy-x15-hitl-probe-port.md"` | 0 | `FAILED: RESTARTS — com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60), they are asked of Dejan · rollback: not used · decisions: 1 · for Dejan: 1 · tokens: 97803` |
| DB | — | — | DB: none: no lock probe, no with-DB string used |

The card's `## RECORDS`, copied and re-read where the list can re-read them: the 994 stop line (re-read above, the same); `DEPLOY-HUB.md:94` the refusal sentence (re-read, present once); `:11` 8 `launchctl` strings (re-read by the probe: 8); `STANDING-LIST.md:23`, `:109`, `:146-148` (re-read, as recorded); the four pins (re-read, as recorded); `RESTARTS by class` (R1 runs it); the 869 card, the rulings and `desk-launch.sh` lines: not re-read (no change to them in this card).

## E0 BASELINE

- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4958 passed, 878 skipped, 4 xfailed, 36 warnings in 735.00s (0:12:15)` (exit 0; 0 failed, 0 errors).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.76s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (none names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED

CONTROLS on BASE first: `uv run pytest -q -p no:cacheprovider --color=no "tests/ops/test_hub_cos_restart_1019.py::test_r2_a_not_loaded_cos_is_skipped_and_acts_on_nothing" "tests/ops/test_hub_cos_restart_1019.py::test_c1_a_label_outside_the_four_is_refused"` → `2 passed, 15 warnings in 0.80s`.

Wrote NEW `tests/ops/test_deploy_cos_restart_1021.py` (8 tests) and NEW `tests/ops/test_desk_launch_launchd.py::test_f1_the_dry_deploy_line_carries_the_three_cos_strings`. `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_cos_restart_1021.py "tests/ops/test_desk_launch_launchd.py::test_f1_the_dry_deploy_line_carries_the_three_cos_strings"` → `FFFFFF.FF` · `8 failed, 1 passed, 15 warnings in 1.25s`. Each red's first line:

| test | first line of the red | the row's reason |
|---|---|---|
| `test_f1_the_hub_line_carries_the_three_cos_strings_once` | `AssertionError: Bash(launchctl bootout gui/501/com.cobalt.cos)` · `assert 0 == 1` | S1 count 0 |
| `test_f1_the_standing_list_names_the_three_strings` | `AssertionError: Bash(launchctl bootout gui/501/com.cobalt.cos)` · `assert 0 == 1` (on the `## 3.` text) | count 0 |
| `test_f2_a_loaded_running_cos_is_admitted_at_step_r` | `assert 'com.cobalt....y list (R60)' not in '- NOT LOADE...ing changed.'` | the refusal sentence is present |
| `test_f2_a_loaded_cos_the_strings_cannot_restore_is_still_refused` | `assert 'FAILED: RESTARTS — com.cobalt.cos loaded <state or path>; the bootstrap string would not restore it · rollback: not used' in '- NOT LOADED …'` | absent |
| `test_f2_the_outage_and_smoke_name_cos` | `assert '\`com.cobalt.cos\`' in 'MODEL: … \`com.cobalt.agent\` and '` | absent |
| `test_f3_the_one_resume_reads_cos_when_in_the_set` | ``assert "`…/com.cobalt.cos` → `state = running` when the report's `## RESTARTS` puts …" in '- THE ONE RESUME, …'`` | absent |
| `test_c_a_cos_outside_the_set_reads_and_prints_as_today` | PASSED (CONTROL) | green on BASE |
| `test_f4_the_stop_line_and_rule_f_carry_the_cos_field` | ``assert '`com.cobalt.cos` in `<restart set>` adds `— cos: <UP\|DOWN>` after the aset field' in '- (5) The last line: …'`` | absent |
| `test_desk_launch_launchd.py::test_f1_the_dry_deploy_line_carries_the_three_cos_strings` | `AssertionError: Bash(launchctl bootout gui/501/com.cobalt.cos)` · `assert 0 == 1` | count 0 |

No red failed for another reason. Commit `eac16bee wip(deploy-cos-restart): red — F1-F4 tests (F1-F4, L67)`. R1 (RUN) is under `## RESTARTS`.

## E3 THE ROWS

Each place was re-found by its content and edited with Edit:
- F1: `DEPLOY-HUB.md:11` gets S1, S2 and S3, each right after its aset twin; the radar `kickstart -k` string still sits directly before ` <launchd strings>`. `STANDING-LIST.md:23` names `com.cobalt.cos`. `:109` reads `60 allow with one head and a migration (57 without a migration;` (BASE 57/54 +3; the BASE count was proven by the PREFLIGHT probe; tip probe: `allow words: 63 … strings: 60`, i.e. 56 literal strings + 1 head + 3 migrate = 60; `deny: 7`, `launchctl: 11`). `:146-148` each gain the cos string between aset and radar, and `those three services`.
- F2: (a) `:94` replaced from `Exit 0` to the end with the card's text; the line's first sentences stand. (b) `:3` reads `/ \`com.cobalt.agent\` / \`com.cobalt.cos\` and the labels of \`<launchd set>\``. (c) `:140` reads `for each of \`com.cobalt.aset\`, \`com.cobalt.cos\`, \`com.cobalt.radar\` in \`<restart set>\``. (d) `:144` gets the cos bootstrap `(cos), ` after aset. (e) `:150` reads `aset / radar, and cos when in \`<restart set>\`, → running`. (f) `:78` reads `the three` for bootout, bootstrap and kickstart -k.
- F3: `:53` (e) gets the cos read after the aset/radar read.
- F4: (a) `:171` gets `; \`com.cobalt.cos\` in \`<restart set>\` adds \`— cos: <UP|DOWN>\` after the aset field` inside the parenthesis; the backticked template stands. (b) `:23` gets `, and \`cos: DOWN\` when \`com.cobalt.cos\` is in \`<restart set>\`,`.
- P1: (a) `test_hub_cos_restart_1019.py` removes `test_c3_a_loaded_cos_still_refuses`, the docstring's `R3:` line and `REFUSED`; nothing else used `REFUSED`, while `COS` is still used by `test_r1`. (b) `test_hub_deferred_1018.py` now reads `assert launch.count(COS) == 3`. (c) `test_desk_launch_launchd.py` now reads `TODAY_ELEVEN = 11`, with its three uses renamed. (d) `test_deploy_smoke_string_1014.py` adds `COS_STRINGS`; the allow compare skips SMOKE and the three cos strings, and the whole-line compare removes each once (`BASE = "7aa5d470"` stands).
- `git diff --stat` after the edits: `DEPLOY-HUB.md | 20 +-` (10 lines: `:3 :11 :23 :53 :78 :94 :140 :144 :150 :171`), `STANDING-LIST.md | 10 +-` (5 lines: `:23 :109 :146 :147 :148`), the four pinned tests.
- DevDocs page: no `src/` module changed, so there is no module page to date. The two pages that mention the hub (`cobalt/jobs/restarts.md`, `cobalt/cli.md`) are module pages, not the hub's.

GREENS: the card's suite `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_cos_restart_1021.py tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py tests/ops/test_desk_launch_launchd.py tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_hub_agent_retired_1020.py tests/ops/test_hub_lines.py` → `89 passed, 15 warnings in 13.62s`; whole `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops` → `4134 passed, 1 xfailed, 16 warnings in 908.12s (0:15:08)`.

THE MUTATIONS (each made with Edit, its tests run, undone with Edit):

| # | mutation | run | result, first failing line |
|---|---|---|---|
| M1 | remove S1 from `:11` | f1 hub, f1 dry, f2 admitted | `3 failed` · `AssertionError: Bash(launchctl bootout gui/501/com.cobalt.cos)` `assert 0 == 1` (each of the three) |
| M2 | `STANDING-LIST.md:23` without cos | f1 list, f1 hub | `1 failed, 1 passed` · ``AssertionError: - `launchctl` on a build or check line; … on no label but `com.cobalt.aset`, `com.cobalt.radar`, `com.cobalt.agent`.`` |
| M3 | `:94` back to BASE's refusal | f2 admitted, f2 refused, CONTROL r2 | `2 failed, 1 passed` (r2 green) · `assert 'com.cobalt....y list (R60)' not in '- NOT LOADE...ing changed.'` |
| M4 | the cos bootstrap removed from 4.6 | the new file | `1 failed, 7 passed` · `assert 'launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist' in '4.6 for each label …'` |
| M5 | `:3` MODEL without cos | the new file | `1 failed, 7 passed` · ``assert '`com.cobalt.cos`' in 'MODEL: …'`` (`test_f2_the_outage_and_smoke_name_cos`) |
| M6 | the cos read removed from `:53` (e) | the new file | `1 failed, 7 passed` · `test_f3_the_one_resume_reads_cos_when_in_the_set`; CONTROL `test_c_…` green |
| M7 | the cos clause removed from rule F `:23` | the new file | `1 failed, 7 passed` · ``assert 'and `cos: DOWN` when `com.cobalt.cos` is in `<restart set>`' in '- F. Residents come up …'`` |
| M8 | CONTROL broken: `— cos: <UP\|DOWN>` put inside the `:171` template | the new file | `1 failed, 7 passed` · `test_c_a_cos_outside_the_set_reads_and_prints_as_today` · `assert '— aset: <UP\|DOWN\|not in the set> — radar: <UP\|DOWN\|not in the set> — launchd: ' in '- (5) The last line: …'` |

After M8 was undone: `git diff --stat` → the 6 files of the fix, 31 insertions and 37 deletions; the card's suite was re-run on that tree → `89 passed, 15 warnings in 13.72s`. No named test stayed green under its mutation. Commit `af0f86bc feat(deploy-cos-restart): the deploy line restarts a loaded cos from its repo plist (F1-F4, P1, L42, L60, L67)`.

## RESTARTS

R1 (RUN, asserts nothing): `uv run cobalt jobs restarts 0e2b5b54..HEAD` → exit 0:

```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.md	A	DOCS	-
tests/ops/test_deploy_cos_restart_1021.py	A	test/documentation; no resident	-
tests/ops/test_deploy_smoke_string_1014.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_launchd.py	M	test/documentation; no resident	-
tests/ops/test_hub_cos_restart_1019.py	M	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```

There is no UNCLASSIFIED row, and the tool's last line agrees with the card header's `RESTARTS: none`.

## W THE THREE SUITES

`<tip>` = `af0f86bc`.
- (a0) `git diff --name-only --no-renames 0e2b5b54` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `tests/ops/test_deploy_cos_restart_1021.py` · `tests/ops/test_deploy_smoke_string_1014.py` · `tests/ops/test_desk_launch_launchd.py` · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-restart offline` → exit 0: `tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)` · `offline 9092/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-restart-offline-20261021-233401.log`. In the log: `957:4958 passed, 878 skipped, 4 xfailed, 36 warnings in 716.94s (0:11:56)` and `1032:4134 passed, 1 xfailed, 16 warnings in 898.45s (0:14:58)`. The 9 tests this build adds: the 8 of `test_deploy_cos_restart_1021.py` and `test_desk_launch_launchd.py::test_f1_the_dry_deploy_line_carries_the_three_cos_strings`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-restart livenote` → exit 0: `live-note 148/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-restart-livenote-20261022-000116.log`; its one skip is `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, and none names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4134 passed, 1 xfailed, 16 warnings in 908.75s (0:15:08)`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/deploy-cos-restart/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK

1. "Every added or changed test was shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." Evidence: E2's table gives each new F test's BASE red, and E3's M1-M8 give each its mutation red. The CONTROL went red under M8, and the existing CONTROL r2 stayed green under M3, as it should. The P1 pins are the old rule's pins moved by the card; each one's BASE red follows from the new count (`launch.count(COS) == 3`, and `TODAY_ELEVEN` against BASE's 8), and each is green at the tip in the card's suite. — 3 of 3.
2. "Every entry path of each rule pinned." Evidence: `desk-launch.sh` copies `:11` (card `## RECORDS` `:207-211`, `:2652-2667`; unchanged here), pinned by the dry `test_f1_the_dry_deploy_line_carries_the_three_cos_strings`, `test_l1_no_section_no_new_string` and `test_l1_a_deferred_label_gets_no_string` (11 strings). The hub text paths STEP-R `:94`, 4.2, 4.6, smoke (a), `:3`, `:78`, `:53` (e), `:171` and `:23` are each pinned by an F test. The STEP-5 (1)/(3) and D1 lines are unchanged ("stand" in the card) and D1 is pinned by `test_hub_agent_retired_1020.py::test_c_d1_still_reads_cos`. The approved list is pinned by `test_f1_the_standing_list_names_the_three_strings`, and `test_deploy_smoke_string_1014.py` pins the line against `7aa5d470`.
3. "Every file:line, count and quote re-read at the tip." Evidence: the DEPLOY PROOF reads were re-run on the tree at `af0f86bc`. `grep -c -F` gives `1` for S1, S2 and S3 in `DEPLOY-HUB.md`, `0` for the old refusal, `1` for S3 in `STANDING-LIST.md`, and `1` each for `(a cos outside it is not read)`, `— cos: <UP|DOWN>`, `cos: DOWN` and `def test_f2_a_loaded_running_cos_is_admitted_at_step_r`. `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` → listed. The count probe was re-run at the tip (`strings: 60`, `deny: 7`, `launchctl: 11`), and `git log --oneline 0e2b5b54..HEAD` → the two commits below.

## FOR THE CHECK

- Range `0e2b5b54..af0f86bc`: `eac16bee wip(deploy-cos-restart): red — F1-F4 tests (F1-F4, L67)` · `af0f86bc feat(deploy-cos-restart): the deploy line restarts a loaded cos from its repo plist (F1-F4, P1, L42, L60, L67)`.
- Per row: the reds are in E2's table, the mutations in E3's M1-M8, and the greens in E3 and W.
- Callers: `desk-launch.sh` (the line's one copier, not changed) is pinned by the dry tests in `test_desk_launch_launchd.py`. The hub is read only as text: there is no script reader of STEP-R (card `## ROWS` WHERE THE LINE LIVES).
- R1's output, WHOLE: under `## RESTARTS`.
- The suites: offline `9092/0` (gate log above), live-note `148/0`, tests/ops `4134 passed`. With-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- The records copied at PREFLIGHT: under `## PREFLIGHT`.
- The DEPLOY PROOF `after` values read on the branch tree are under PRE-STOP SELF-CHECK 3. Run against `/Users/cobalt/cobalt` (main) they read `before` until the deploy.

## CONTINUE

next: CLOSE (done)

## DECISIONS

none

## RECORDS

- Build started 22:59:37 EDT 2026-10-21 (`date`); W ended 00:17:07 EDT 2026-10-22 (`date`).
- L74: a `Claude-Session:` commit line was asked in a system-reminder; it is recorded under `## L74` and was not acted on.
- The RUN probe `test_count_probe.py` was staged in `$CLAUDE_JOB_DIR/tmp` (`/Users/cobalt/.claude/jobs/adb624fb/tmp`), outside the worktree.
- The PREFLIGHT `jobs restarts` showed the untracked report as `A DOCS` on the empty range; it restarts nothing.
- No lock take (DB: none). `.env`: never present in this worktree.
- The card's `## RECORDS`, as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-cos-restart · tip: af0f86bc | on 0e2b5b54 | migration: none | offline 9092/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 187734
