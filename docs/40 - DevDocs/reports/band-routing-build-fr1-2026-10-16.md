# band-routing-1015 — fix round FR-1 to FR-5, build report (2026-10-16)

## §0 Headline
- Fix round FR-1 to FR-5 is built on `ee21824d..c8c5ca90`. The launcher refuses a card path that holds `/./` or `//`, naming it, and `test_o2_…` is a plain passing test.
- CHECK-HUB `:64` and `:117` excuse a routed card's untracked SHADOW-INSTRUCTIONS.md. CARD.md's `BAND` check cell is required for a LOW or MID build. SHADOW-HUB sends a routed fix round to a fresh `BAND: HIGH` card and gives the routed exception at `:53` and `:70`.
- Offline 8421/0 (tests/ops 3853 passed, 1 xfailed), live-note 146/0, with-DB not run (DB: none). RESTARTS: none.
- 1 decision: FR-1's arm refuses a `/./` path before the BAND read, so `test_o2_…` could not pass on its old message assertion. That one assertion now checks the path refusal.

FIXED: O2 — tests/ops/test_band_routing_1015.py::test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band
FIXED: O2 — tests/ops/test_band_routing_1015.py::test_fr1_a_double_slash_card_path_is_refused_naming_it
FIXED: O4 — tests/ops/test_band_routing_1015.py::test_fr2_check_hub_excepts_a_routed_card_from_the_untracked_instructions_file
FIXED: O1 — tests/ops/test_band_routing_1015.py::test_fr3_card_md_requires_band_on_a_routed_builds_check_card
FIXED: O3 — tests/ops/test_band_routing_1015.py::test_fr4_the_routed_fix_round_is_a_fresh_high_card_and_the_backup_cites_its_rulings
FIXED: G3 — tests/ops/test_band_routing_1015.py::test_fr4_the_routed_fix_round_is_a_fresh_high_card_and_the_backup_cites_its_rulings
FIXED: G2 — tests/ops/test_band_routing_1015.py::test_fr5_the_procedure_excepts_a_routed_card_on_its_two_lines

## L74
- A system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md"` (10:09 EDT), exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · 1fd1c4991ad17235a48e4cd80f8d27ee5fc10337
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
RECOVERY first rows (10:08 EDT): `git status --short --branch` → `## ops/band-routing-1015`; `git log --oneline -3` → `ee21824d wip(band-routing-1015): check red — O2 …`, `115e1f37 docs(band-routing-1015): build report — bd9c24ac`, `bd9c24ac feat(band-routing-1015): …`; `ls -la …/band-routing-1015/.env` → `No such file or directory`.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, exit 0, output whole:
```
clock · date · 0 · Fri Oct 16 10:09:10 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1 · 0 · ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)
diff · git diff --stat f2ca3e1a · 0 · (10 lines)
     docs/40 - DevDocs/prompts/BUILD-HUB.md             |   2 +
     docs/40 - DevDocs/prompts/CARD.md                  |   3 +
     docs/40 - DevDocs/prompts/SHADOW-HUB.md            |  11 +-
     .../reports/band-routing-build-2026-10-15.md       | 201 +++++++
     .../reports/band-routing-build-2026-10-15.result   |  15 +
     ops/desk/bare-guard.py                             |   5 +
     ops/desk/desk-launch.sh                            |  71 ++-
     ops/desk/preflight.sh                              |  26 +-
     tests/ops/test_band_routing_1015.py                | 578 +++++++++++++++++++++
     9 files changed, 905 insertions(+), 7 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015 · 0 · ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
The diff is the built branch (a relaunch on a `wip(band-routing-1015):` commit), as the card's `## FIX ROUND` states.

## E0 BASELINE
Not re-run: the B rows' E0 on `f2ca3e1a` stands in `band-routing-build-2026-10-15.md` `## E0 BASELINE`. A fix round reruns only the tests that touch the fixed part, then the gate (BUILD-HUB STOP LINE, NEXT STEP).

## E2 RED
On the branch tip `ee21824d`, nine tests added to `tests/ops/test_band_routing_1015.py` (no other file): `test_fr1_a_double_slash_card_path_is_refused_naming_it`, `test_fr1_control_a_plain_card_path_still_launches`, `test_fr2_check_hub_excepts_a_routed_card_from_the_untracked_instructions_file`, `test_fr2_control_the_two_lines_stay_where_they_are`, `test_fr3_card_md_requires_band_on_a_routed_builds_check_card`, `test_fr3_control_an_opus_builds_check_card_without_band_still_launches[2026-10-16|2026-01-02]`, `test_fr4_the_routed_fix_round_is_a_fresh_high_card_and_the_backup_cites_its_rulings`, `test_fr4_control_the_band_table_stands`, `test_fr5_the_procedure_excepts_a_routed_card_on_its_two_lines`, `test_fr5_control_the_shadow_stop_line_stays`.

`uv run pytest -q -p no:cacheprovider --color=no --tb=line --runxfail tests/ops/test_band_routing_1015.py` → `6 failed, 42 passed, 15 warnings in 8.80s`. Each red, first line:
- O2 / FR-1 `test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band` → `:384: … assert 0 == 1` (exit 0; stdout is the Opus line, `CARD: '…/prompts/./2026-10-16/01-x-band-card.md'`).
- FR-1 `test_fr1_a_double_slash_card_path_is_refused_naming_it` → `:395: … assert 0 == 1` (exit 0, the Opus line, `…/prompts//2026-10-16/…`).
- FR-2 `test_fr2_check_hub_excepts_…` → `:415: assert 0 == 2`.
- FR-3 `test_fr3_card_md_requires_band_…` → `:433: AssertionError:  optional` / `assert 'required' in ' optional '`.
- FR-4 `test_fr4_the_routed_fix_round_…` → `:444: AssertionError: its own fresh job card with BAND: HIGH`.
- FR-5 `test_fr5_the_procedure_excepts_…` → `:462: assert [0, 0] == [1, 1]`.
CONTROLS GREEN on the tip: the four FR controls above (five cases), inside the 42 passed. No RUN row and no with-DB red in the fix round; no lock. Commit `01b10bdd wip(band-routing-1015): fix round red (FR-1 to FR-5)`.

## E3 THE ROWS
Anchors re-read by content before the edits (`grep -n -F`, this worktree): `*..*)` → `desk-launch.sh:996`; `is expected and recorded, not a finding` → `CHECK-HUB.md:64`, `:117` (`## PREFLIGHT` `:61`, `## 1.` `:72`, `## 7.` `:115`, `## 8.` `:120`); `` | `BAND` | `` → `CARD.md:23`; `BAND ROUTING (` → `SHADOW-HUB.md:28`; `2. PREFLIGHT:` → `:53`; `` `SHADOW BUILT · job: `` → `:70`; `test_o2_…` → `test_band_routing_1015.py:380` (marker `:377-379`); `L6_LINE` → `test_check_hub_shadow.py:27`, `:75`.
- FR-1 `desk-launch.sh`: one arm after `*..*)` in the second card-path `case`: `*/./*|*//*) refuse "the card path holds '/./' or '//': $card" ;;`. The strict xfail marker and its two comment lines above `test_o2_…` are out. ONE assertion of `test_o2_…` changed (DECISION FR-1): `BAND_REFUSAL in done.stderr` → `"REFUSED: the card path holds '/./' or '//'" in done.stderr`; its `returncode == 1` assertion and its setup are unchanged.
- FR-2 `CHECK-HUB.md` `:64` and `:117`: `on a shadow card,` → `on a shadow card or a routed card (BAND LOW or MID, dated on or after BAND_FROM),`; nothing else. `test_check_hub_shadow.py`: the one constant `L6_LINE` set to the new line (two string pieces became three; nothing else of the file).
- FR-3 `CARD.md:23`: the check cell `optional` → `required when the build card carries BAND: LOW or MID (copied from it); optional otherwise`.
- FR-4 `SHADOW-HUB.md:28`: `the fix round goes to the same builder, the backup is` → `a routed card's fix round is its own fresh job card with BAND: HIGH (brain 2026-10-16 note 7), the backup is`; `never on a 429):` → `never on a 429 (R1532: Terra backup; 2026-10-14 item 7: a 429 is retried, never a backup)):`.
- FR-5 `SHADOW-HUB.md` `:53` and `:70`: each gains ` (a routed card: no `SHADOW OF`; stop line `BUILT ·` as `:28`)` at its end (`:70` directly after the closing backtick).

The first run of the three launcher files (`test_band_routing_1015.py test_desk_launch_prechecks.py test_desk_launch_shadow.py`, background) began before the hub edits were made and read the hubs mid-edit: `3 failed, 245 passed` (FR-3, FR-4, FR-5 hub reads, the pre-edit text). Re-run after the edits, below.

THE MUTATIONS (Edit tool, `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_band_routing_1015.py -k "o2 or fr"`, undone with Edit):
- Round 1 — FR-1 arm deleted; `## 7. CHECKED` → `## 7x. CHECKED`; the `| MID |` band row deleted; `:70` `tip: <tip>` → `tipX: <tip>` → `5 failed, 7 passed`: `test_o2_…` `:381: assert 0 == 1` (the Opus line, `prompts/./2026-10-16/…`), `test_fr1_a_double_slash…` `:392: assert 0 == 1`, `test_fr2_control…` `:49: AssertionError: ('## 7. ', [])`, `test_fr4_control…` `:448: AssertionError: MID`, `test_fr5_control…` `:464: assert 'SHADOW BUILT · job: <JOB> · tip: <tip>' in '…tipX: <tip>…'`.
- Round 2 — the FR-1 arm widened to `*/*)`; FR-2, FR-3, FR-4 (first clause) and FR-5 (`:53`) undone → `7 failed, 5 passed`: `test_fr1_control…` `:399: … REFUSED: the card path holds '/./' or '//': …/prompts/2026-10-16/01-x-band-card.md`, `test_fr2_check_hub…` `:412: assert 0 == 2`, `test_fr3_card_md…` `:430: assert 'required' in ' optional '`, `test_fr4_the_routed…` `:441: … its own fresh job card with BAND: HIGH`, `test_fr5_the_procedure…` `:459: assert [0, 1] == [1, 1]`, `test_fr3_control…[2026-10-16]` and `[2026-01-02]` `:581: assert 'REFUSED' not in …`.
- After the undo, `git diff` showed exactly the fix (6 files, 10 insertions, 11 deletions) and nothing of either mutation.

GREEN:
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` (no `--runxfail`, the marker is out) → `48 passed, 15 warnings in 8.32s`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_build_hub_no_clutter.py tests/ops/test_hub_lines.py tests/ops/test_deploy_card.py tests/ops/test_check_hub_shadow.py tests/ops/test_card_template_1014.py tests/ops/test_preflight.py tests/ops/test_desk_done.py tests/ops/test_card_fill.py` (the nine files of FIX ROUND ORDER plus FR-5's `test_desk_done.py` and `test_card_fill.py`) → `550 passed, 16 warnings in 147.57s (0:02:27)`.
- `git diff --stat ee21824d -- <the nine files>` → ` tests/ops/test_check_hub_shadow.py | 3 ++-` · `1 file changed, 2 insertions(+), 1 deletion(-)` (FR-2's `L6_LINE` only).
- `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → no output (exit 1): no `git show`, no 8-hex literal.
- X8: `Grep` of `tests/ops` for a `/./` or `//` card path → only `test_band_routing_1015.py:379` (`test_o2_…`) and `:390` (`test_fr1_…`). No existing launcher test names a card through such a path.

DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` or the hubs (B rows' report, `## E3`); no dated line.

Commit `c8c5ca90 fix(band-routing-1015): card paths with /./ or // refused; routed card in CHECK-HUB, CARD.md check cell, SHADOW-HUB fix round and routed exception (FR-1 to FR-5, L1 L72)`.

## RESTARTS
`uv run cobalt jobs restarts ee21824d..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	M	test/documentation; no resident	-
tests/ops/test_check_hub_shadow.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row (the report row is this file, untracked at the run).

## W THE THREE SUITES
`<tip>` = `c8c5ca90`. (a0): `git diff --name-only --no-renames f2ca3e1a` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 11 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/BUILD-HUB.md)` · `offline 8421/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261016-101623.log`. Its two runs: `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 667.28s (0:11:07)` and `:959` (tests/ops whole) `3853 passed, 1 xfailed, 16 warnings in 827.77s (0:13:47)`. That is 3841 at the B rows' W plus the 12 cases this round adds or turns from xfail. The tests this round adds are the eleven FR cases of `## E2 RED`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261016-104134.log`. The only SKIPPED is `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- The card's `uv run pytest -q tests/ops` whole is the gate's `:959` run (the same tree, the same path). It was not typed a second time.
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. The six row tests were red on the tip `ee21824d` (`## E2 RED`). Under the mutations: O2 and the FR-1 double slash went red in round 1, the FR-2 to FR-5 row tests in round 2, the five control cases in rounds 1 and 2 (`## E3`). `test_check_hub_shadow.py::test_l6_…` with the new `L6_LINE` went red under round 2's FR-2 undo by construction (exact-line equality), and it is green at the tip in the 550-passed run.
(2) Entry paths: the new arm sits in the one card-path `case` that every kind passes (`desk-launch.sh:994-998`, before the kind arms). Pinned for `build` by `test_o2_…` (`/./`) and `test_fr1_…` (`//`); plain paths by `test_fr1_control…` and the 550-passed launcher files. `check` and `shadow` cross the same `case` (one gate for every kind, as the two arms above it). The hub lines are read by `test_fr2_*` to `test_fr5_*` and the existing `test_check_hub_shadow.py`, `test_shadow_hub_file.py` and `test_card_template_1014.py`, all green. FR-3's check-card rule is drafter text that no code reads; its control pins the launcher's `optional otherwise` behaviour (a no-BAND check card on both dates).
(3) Re-read at the tip: `grep -n -F "*/./*" ops/desk/desk-launch.sh` → `997:`; `grep -c -F "a routed card: no"` SHADOW-HUB → `2`; `grep -c -F "or a routed card (BAND LOW or MID"` CHECK-HUB → `2`; `git log --oneline ee21824d..HEAD` → the two commits below; `git diff --stat ee21824d -- <nine files>` → `test_check_hub_shadow.py` only.

## FOR THE CHECK
- Range `ee21824d..c8c5ca90` (on BASE `f2ca3e1a`): `01b10bdd wip(band-routing-1015): fix round red (FR-1 to FR-5)` · `c8c5ca90 fix(band-routing-1015): card paths with /./ or // refused; routed card in CHECK-HUB, CARD.md check cell, SHADOW-HUB fix round and routed exception (FR-1 to FR-5, L1 L72)`.
- Per row: reds in `## E2 RED`, mutations and greens in `## E3 THE ROWS`.
- No RUN row in the fix round. RESTARTS table: `## RESTARTS`, whole.
- Suites: offline 8421/0, tests/ops 3853 passed / 1 xfailed, live-note 146/0. With-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- X8: every kind crosses the one card-path `case`. No existing launcher test names a `/./` or `//` card path (`## E3`, GREEN). X9: `L6_LINE` is the only change in `test_check_hub_shadow.py` (`git diff` in `## E3`). X12: G1 (PASS-2) is not touched.
- Records copied at PREFLIGHT: the card's `## RECORDS` (fix-round drafter, prompt 635, 2026-10-16 10:03 EDT, anchors on the branch tip). Re-read here: every anchor it names, by `grep` (`## E3`); all matched (`desk-launch.sh:996`, `CHECK-HUB.md:64`/`:117`, `CARD.md:23`, `SHADOW-HUB.md:28`/`:53`/`:70`, the marker at `test_band_routing_1015.py:377-379`, `L6_LINE` at `:27`).

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION FR-1 (ASK DESK): the card asks for two things that cannot both hold. Its byte-for-byte arm `*/./*|*//*) refuse "the card path holds '/./' or '//': $card"` refuses in the card-path gates, before any field is read. It also says `test_o2_…`'s body and assertions "do not change" and "that test passes". But `test_o2_…` asserts `BAND_REFUSAL in done.stderr`, and with the arm stderr is `REFUSED: the card path holds '/./' or '//': …` (quoted, `## E3`, first run after the arm). Default taken: the arm as written, and ONE assertion of `test_o2_…` changed to the path refusal. The test's intent stands: exit 1, no launch. Alternative for the desk: a refusal message that also carries the BAND text. That would change the card's arm text.

## RECORDS
- CONTINUED at FIX ROUND row FR-1 10:08 EDT (a new session; RECOVERY rows above).
- L74: one session system reminder asked for a `Claude-Session:` trailer. Recorded under `## L74`; commits carry `Co-Authored-By` only.
- ORDER: the five FR reds were run once together on the tip (`## E2 RED`). The edits followed back to back, without a re-run of each red before its own edit. Each row's red was re-shown by its mutation (`## E3`).
- The first background run of the three launcher files overlapped the hub edits and printed `3 failed, 245 passed` on pre-edit text. It was superseded by the 48-passed and 550-passed runs.
- E0 not re-run (fix round; `## E0 BASELINE`). No lock take (DB: none). `.env`: never present.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: band-routing-1015 · tip: c8c5ca90 | on f2ca3e1a | migration: none | offline 8421/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 187713
