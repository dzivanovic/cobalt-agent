# band-routing-1015 — fix round 2, FR-6 to FR-8, build report (2026-10-16)

## §0 Headline
- Fix round 2 (FR-6 to FR-8) is built on `7bf43c2b..fda2300b`. A routed launch now prints `WATCH: … desk-watch.sh routed "<card>"`. The new `routed` kind watches `<job>-gate` for `^(BUILT ·|FAILED)` and closes through `desk-done.sh` as `build`.
- The launcher refuses a card outside `$PROMPTS/<YYYY-MM-DD>/`, naming the path. SHADOW-HUB `:28` cites the 429 clause as the brain's reading. The three strict xfails are gone and pass.
- Offline 8434/0 (tests/ops 3866 passed, 1 xfailed, pre-existing), live-note 146/0. With-DB not run (DB: none). RESTARTS: none.
- 3 decisions: FR-6's tip reds read `unknown kind: routed`, FR-7's arm form (a pass-through for FR-1's paths), and FR-7's card survey by Glob.

FIXED: O1 — tests/ops/test_band_routing_1015.py::test_o1_a_routed_builds_watch_line_waits_on_the_build_stop_line
FIXED: O1 — tests/ops/test_band_routing_1015.py::test_fr6_the_routed_watcher_admits_built_and_watches_the_gate_session
FIXED: O1 — tests/ops/test_band_routing_1015.py::test_fr6_a_routed_closeout_hands_build_to_desk_done
FIXED: G1 — tests/ops/test_band_routing_1015.py::test_x5_routed_build_watch_does_not_wait_on_built
FIXED: O3 — tests/ops/test_band_routing_1015.py::test_o3_a_card_outside_a_date_folder_still_needs_its_band
FIXED: O3 — tests/ops/test_band_routing_1015.py::test_fr7_a_card_outside_a_date_folder_is_refused_naming_it
FIXED: O2 — tests/ops/test_band_routing_1015.py::test_fr8_the_429_clause_is_cited_as_the_brains_reading
FIXED: G2 — tests/ops/test_band_routing_1015.py::test_fr8_the_429_clause_is_cited_as_the_brains_reading

## L74
- A system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md"` (13:08 EDT), exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · 3ee7bf7563274dec58504ac1989a8cc5438862db
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
RECOVERY first rows (13:08 EDT): `git status --short --branch` → `## ops/band-routing-1015`; `git log --oneline -3` → `7bf43c2b wip(band-routing-1015): check red — O1 O3 G1 (strict xfail: HELD, NOT FIXED, desk-launch.sh fenced)`, `3ac61a2f docs(band-routing-1015): build report — c8c5ca90 (fix round FR-1 to FR-5)`, `c8c5ca90 fix(band-routing-1015): …`; `ls -la …/band-routing-1015/.env` → `No such file or directory`.

The first `preflight.sh build` run (13:08:35) ended `FAILED PREFLIGHT: status`. Its only extra status line was `?? "docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md"`, this report's first write (RECOVERY). I committed it as `ac172ab9 wip(band-routing-1015): fix round 2 report opened (FR-6 to FR-8)` and ran the script again, exit 0, output whole:
```
clock · date · 0 · Fri Oct 16 13:08:42 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1 · 0 · ac172ab9 wip(band-routing-1015): fix round 2 report opened (FR-6 to FR-8)
diff · git diff --stat f2ca3e1a · 0 · (15 lines)
     docs/40 - DevDocs/prompts/BUILD-HUB.md             |   2 +
     docs/40 - DevDocs/prompts/CARD.md                  |   3 +
     docs/40 - DevDocs/prompts/CHECK-HUB.md             |   4 +-
     docs/40 - DevDocs/prompts/SHADOW-HUB.md            |  15 +-
     .../reports/band-routing-build-2026-10-15.md       | 201 ++++++
     .../reports/band-routing-build-2026-10-15.result   |  15 +
     .../reports/band-routing-build-fr1-2026-10-16.md   | 152 +++++
     .../band-routing-build-fr1-2026-10-16.result       |  15 +
     .../reports/band-routing-build-fr6-2026-10-16.md   |  36 ++
     ops/desk/bare-guard.py                             |   5 +
     ops/desk/desk-launch.sh                            |  72 ++-
     ops/desk/preflight.sh                              |  26 +-
     tests/ops/test_band_routing_1015.py                | 693 +++++++++++++++++++++
     tests/ops/test_check_hub_shadow.py                 |   3 +-
     14 files changed, 1230 insertions(+), 12 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015 · 0 · ac172ab9 wip(band-routing-1015): fix round 2 report opened (FR-6 to FR-8)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

THE CARD'S SYMBOLS on the tip, read in this worktree (Grep and Read; `wc -l`: desk-launch.sh 2403, desk-watch.sh 228, SHADOW-HUB.md 112, test_band_routing_1015.py 693):
- `desk-launch.sh`: `287:watch_line() {`, `379:routed=""`, `394: routed=1`, `991: "$PROMPTS"/*-card.md) ;;` (refusal `:992`), `996: *..*)`, `997: */./*|*//*)`, `1643:BAND_FROM=20261016`, `1667: exec sh "$0" shadow "$card" --model "$bid" --routed`, `2354:watch=$(watch_line "$kind" "$card")`. Callers of `watch_line`: `:546` (kind close) and `:2354`.
- `desk-watch.sh`: the two `case "$kind" in` at `:59` and `:70`. Arms `build` `:60` `^(BUILT|FAILED)`, `shadow` `:64` `^(SHADOW BUILT|SHADOW ROLE|FAILED)`, `:71` `build|check|devfix` session `$job-$kind`, `:72` shadow `$job-gate`. `close_worker() {` `:108`, `out=$(sh "$here/desk-done.sh" "$rid" "$report" "$kind")` `:151`.
- `SHADOW-HUB.md:28`, the `BAND ROUTING (` line, ends `never on a 429 (R1532: Terra backup; 2026-10-14 item 7: a 429 is retried, never a backup)):`.
- `test_band_routing_1015.py`: the xfail decorators at `:403`, `:411`, `:421` (each `def` directly below); `test_x5_…` `:426` asserts `desk-watch.sh build `.
- Every anchor is where the card's `## RECORDS` (FR-6 routed, FR-6 closeout) puts it. The card's records are copied by reference: drafters 645, 646, 651, all on the tip `7bf43c2b`, reads only.

## E0 BASELINE
Not re-run. The B rows' E0 on `f2ca3e1a` stands in `band-routing-build-2026-10-15.md`. A fix round reruns only the tests that touch the fixed part, then the gate.

## E2 RED
On the tip, in `tests/ops/test_band_routing_1015.py` only: nine new tests (twelve cases), `test_x5_…`'s one assertion `desk-watch.sh build ` → `desk-watch.sh routed `, and FR-4's two literals → `brain 2026-10-16, reading R1532's 'Terra backup'` and `R1471 (7) is recorded in the direction file`. The markers stayed in place for E2.

`uv run pytest -q -p no:cacheprovider --color=no --tb=line --runxfail tests/ops/test_band_routing_1015.py` → `10 failed, 51 passed, 15 warnings in 11.54s`. Each red, first line:
- O1 `test_o1_…` → `:408: assert 'desk-watch.sh shadow ' not in …` (`WATCH: sh …/desk-watch.sh shadow "…/2026-10-16/01-x-band-card.md"`).
- G1 `test_x5_…` → `assert ['WATCH: sh /...and-card.md"'] == []`.
- FR-6 `test_fr6_the_routed_watcher_…` → `:556: assert 'desk-watch.sh routed "…"' in …` (the launch prints `desk-watch.sh shadow`).
- FR-6 `test_fr6_a_routed_closeout_…` → `:577: AssertionError: REFUSED: unknown kind: routed` (`assert 1 == 0`). See DECISION FR-6.
- O3 `test_o3_…` → `:418: assert 0 == 1` (the Opus line, `CARD: '…/prompts/01-x-band-card.md'`).
- FR-7 `test_fr7_…[01-x-band-card.md]`, `[drafts/01-x-band-card.md]`, `[2026-10-16/sub/01-x-band-card.md]` → `:617: assert 0 == 1`. The first two launch on the Opus line. The sub-folder case is dated, so it routes and launches the gate seat (`MODEL: grok-4.7`, `WATCH: … shadow "…/2026-10-16/sub/01-x-band-card.md"`), quoted as it stands.
- FR-4 (literals) `test_fr4_…` → `:464` and FR-8 `test_fr8_the_429_clause_…` → `:637`: `assert "brain 2026-10-16, reading R1532's 'Terra backup'" in '…never on a 429 (R1532: Terra backup; 2026-10-14 item 7: …)):'`.

CONTROLS GREEN on the tip, inside the 51 passed: `test_fr6_control_a_shadow_card_closeout_still_passes_shadow`, `test_fr6_control_a_high_card_and_a_real_shadow_keep_their_watch`, `test_fr7_control_a_dated_card_still_launches`, `test_fr8_control_the_rest_of_the_line_and_the_table_stand`. No RUN row and no with-DB red; no lock. Commit `45b9d8c7 wip(band-routing-1015): fix round 2 red (FR-6 to FR-8)`.

## E3 THE ROWS
Anchors re-read by content before each edit (`## PREFLIGHT`).
- FR-6 `desk-launch.sh` (the one `watch=` line): `if [ -n "$routed" ]; then watch=$(watch_line routed "$card"); else watch=$(watch_line "$kind" "$card"); fi`. `routed` is set before any kind arm (`:379`), so every other kind keeps `watch_line "$kind"`. `desk-watch.sh`: `routed) report=$(header REPORT) || exit 1; re='^(BUILT ·|FAILED)' ;;` after the shadow arm of the first `case`, and `routed) job=…; wt=…; session="$job-gate" ;;` after the shadow arm of the second. The one mapping line in `close_worker`: `out=$(sh "$here/desk-done.sh" "$rid" "$report" "$([ "$kind" = routed ] && echo build || echo "$kind")")`. `desk-done.sh` is untouched. The two decorators above `test_o1_…` and `test_x5_…` are out; their bodies are unchanged (but for `test_x5_…`'s one assertion, E2).
- FR-7 `desk-launch.sh`, the first card `case` (DECISION FR-7):
  ```
      */./*|*//*) ;;  # refused by name in the case below (card 583 FR-1)
      "$PROMPTS"/*/*/*) refuse "the card must be $PROMPTS/<YYYY-MM-DD>/<nn>-<job>-card.md: $card" ;;
      "$PROMPTS"/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/*-card.md) ;;
      *) refuse "the card must be $PROMPTS/<YYYY-MM-DD>/<nn>-<job>-card.md: $card" ;;
  ```
  The decorator above `test_o3_…` is out; its body is unchanged. Without the pass-through line, the first edit refused `/./` and `//` paths with "the card must be" before FR-1's named arm (`test_o2_…` and `test_fr1_…` red, quoted under round 5 below).
- FR-8 `SHADOW-HUB.md:28`: `never on a 429 (R1532: Terra backup; 2026-10-14 item 7: a 429 is retried, never a backup)):` → `never on a 429 (brain 2026-10-16, reading R1532's 'Terra backup': a backup is for a probe OUT or a harness FAILED; a 429 is recorded and retried, never a backup, as the Grok-cap removal of 2026-10-14 R1471 (7) is recorded in the direction file)):`. Nothing else of the file changed (`git diff`, one line). Card proofs (the card is the desk's, not edited): `grep -n -F "a fallback on a 429 (brain 2026-10-16"` of the card → one line, `:70` (`## NOT IN THIS JOB`). `grep -c -F "(brain 2026-10-16, reading R1532's 'Terra backup'"` → `3`: the B3 row `:43`, FR-8's own row `:55` and `:70`. `R1532: Terra backup` remains in the card only at `:22` and `:51` (FR-4 history, as `## FIX ROUND 2` says) and not in the hub.
- FR-7 survey (DECISION FR-7-survey): `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts"` → 31 folders `2026-09-15` … `2026-10-16`, each `YYYY-MM-DD`, plus 18 hub `.md` files, no `-card.md` at the top. Glob `*/*/**/*-card.md` → none, and `[!0-9]*/*-card.md` → none. No live card sits outside a dated folder. The launcher tests' cards sit in `prompts/2026-01-02/` and `2026-10-16/` (green below).

THE MUTATIONS (Edit tool, the tests run alone, each undone with Edit):
- Round 1, every fix undone (the `watch=` line back; `routed` regex back to `SHADOW BUILT|…` and its session to `$job-build`; the mapping back to `"$kind"`; FR-7's arms back to `"$PROMPTS"/*-card.md) ;;`; FR-8's citation back) → `10 failed, 8 passed` over `-k "fr4 or fr6 or o1_ or x5 or fr7 or o3_ or fr8 or o2_ or fr1"`: o1 `:407`, o3 `:416 assert 0 == 1`, x5 `assert [...] == []`, fr4, fr6 watcher `:553` (the launch prints `shadow`), fr6 closeout `:574 assert 3 == 0` with stdout `GONE: x-job-build` and the `BUILT ·` line unmatched (the card's named reason), fr7 ×3 `:614 assert 0 == 1`, fr8 `:634`.
- Round 2, only the two `desk-watch.sh` arms mutated → the watcher test `:556` and the closeout `:574`: `assert 3 == 0`, `GONE: x-job-build`.
- Round 3, only the mapping line back to `"$kind"` → `1 failed, 3 passed`: `:576 assert ['sess… routed'] == ['sess… build']` (the card's named reason: the stub called with `routed`).
- Round 4, controls: mapping always `build`; the date arm's glob with `x` added; `never on a 429` → `never on 429`; the `watch=` test `true` → `4 failed`: shadow closeout `:585 … build != … shadow`; HIGH/shadow WATCH and the dated control `assert 1 == 0` (`REFUSED: the card must be …`, the date-arm mutation); FR-8 control `:643 assert 'never on a 429' in …`.
- Round 5, the date arm restored, `watch=` still forced to `routed`, the pass-through and the sub-folder arms removed → `4 failed, 4 passed`: `test_fr6_control_a_high…` `:592` (`desk-watch.sh routed` != `desk-watch.sh build`, the WATCH mutation alone); `test_o2_…` `:382` and `test_fr1_…` `:393` (`REFUSED: the card must be …` in place of the `/./` text); `test_fr7_…[2026-10-16/sub/…]` `:614 assert 0 == 1`.
- The 8-hex literals of the new tests were changed to `sess-x01`, `tip-x`, `base-x` (THE TEST RULE). Mutation again (the routed regex and the mapping) → `2 failed, 2 passed`: `:556` `GONE: x-job-gate`, `:574` `IDLE: x-job-gate — no WAKE line`. Undone.
- After the last undo, `git diff --stat` showed the fix only: 4 files, 16 insertions, 15 deletions.

GREEN:
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` (no `--runxfail`) → `61 passed, 15 warnings in 14.59s`. No `xfailed`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_watch.py tests/ops/test_close_automation_1015.py tests/ops/test_check_hub_shadow.py tests/ops/test_card_template_1014.py tests/ops/test_preflight.py` → `373 passed, 16 warnings in 175.42s (0:02:55)`. `git diff --stat 7bf43c2b -- <those eight>` → nothing.
- After the literal change: `test_band_routing_1015.py test_desk_watch.py test_close_automation_1015.py` → `129 passed in 105.29s`.
- `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → no output (exit 1).

DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` or the hubs (B rows' report, `## E3`); no dated line.

Commit `fda2300b fix(band-routing-1015): routed launch watched as kind routed on <job>-gate; card outside a dated folder refused; 429 clause cited as the brain's reading (FR-6 to FR-8, L1 L72)`.

## RESTARTS
`uv run cobalt jobs restarts 7bf43c2b..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `fda2300b`. (a0): `git diff --name-only --no-renames f2ca3e1a` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `…/CARD.md`, `…/CHECK-HUB.md`, `…/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md`, `….result`, `band-routing-build-fr1-2026-10-16.md`, `….result`, `band-routing-build-fr6-2026-10-16.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 15 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/BUILD-HUB.md)` · `offline 8434/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261016-132027.log`. Its two runs: `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 718.47s (0:11:58)` and `:959` (tests/ops whole) `3866 passed, 1 xfailed, 16 warnings in 855.20s (0:14:15)`. That is 3853 at FR-1's W, plus the ten cases this round adds, plus the three strict xfails of `7bf43c2b` now passing. The one xfail is the same as at every earlier W.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261016-134656.log`. The only SKIPPED is `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory`.
- The card's `uv run pytest -q tests/ops` whole is the gate's `:959` run (same tree). It was not typed a second time.
- With-DB: not run (DB: none).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. FR-6 to FR-8 and the three ex-xfails were red on the tip (`## E2 RED`) and again under their undo mutation (rounds 1-3). The four controls were red under rounds 4-5. FR-4's test went red on the tip with its new literals and green after FR-8. `test_x5_…` went red with its new assertion on the tip and under round 1.
(2) Entry paths: the WATCH line is built once (`desk-launch.sh:2356`) for every kind that reaches the launch tail. `routed` is set only by `--routed`, which a LOW/MID `build` re-enters through (`test_o1_…`, `test_x5_…`, `test_fr6_the_routed…`), and by the desk's hand launch (the same flag). HIGH `build` and a real `shadow` are pinned by `test_fr6_control_a_high…`. Kind close builds its line at `:546`, unchanged. `desk-watch.sh routed` is pinned for the stop line, idle, gone and closeout. `shadow`'s closeout is pinned by its control, and the other kinds by the green `test_desk_watch.py` and `test_close_automation_1015.py`. FR-7's `case` is crossed by every kind before the kind arms. It is pinned for `build` (flat, non-date, sub-folder, dated control) and for `/./` and `//` (`test_o2_…`, `test_fr1_…`). `check`/`shadow` cards in the existing launcher files (dated folders) are green.
(3) Re-read at the tip: `grep -n -F "watch_line routed"` desk-launch.sh → `2356:`; `grep -n -F "routed)"` desk-watch.sh → `65:`, `74:`; `grep -n -F "the card must be"` → `992:`, `994:`; `grep -n -F "brain 2026-10-16, reading R1532"` SHADOW-HUB → `28:`; `git log --oneline 7bf43c2b..HEAD` → the three commits below.

## FOR THE CHECK
- Range `7bf43c2b..fda2300b` (on BASE `f2ca3e1a`): `ac172ab9 wip(band-routing-1015): fix round 2 report opened (FR-6 to FR-8)` · `45b9d8c7 wip(band-routing-1015): fix round 2 red (FR-6 to FR-8)` · `fda2300b fix(band-routing-1015): routed launch watched as kind routed on <job>-gate; card outside a dated folder refused; 429 clause cited as the brain's reading (FR-6 to FR-8, L1 L72)`.
- Per row: reds in `## E2 RED`, mutations and greens in `## E3 THE ROWS`.
- No RUN row in this round. RESTARTS table: `## RESTARTS`, whole.
- Suites: `## W`. With-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- X13: `desk-watch.sh` changed only by the two `routed` arms and the one mapping line (`git diff`, 3 lines). `desk-done.sh` was not touched. X14: no live card outside a dated folder (`## E3`). X15: the hub and the card's `:43`, `:70` carry the citation. FR-4's test changed only in its two literals.
- Records copied at PREFLIGHT: the card's `## RECORDS` (drafters 645, 646, 651). Every anchor they name matched (`## PREFLIGHT`).

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION FR-6 (ASK DESK): the card names the tip reds of the two new watcher tests as "the stop line is not matched (SHADOW BUILT only) and the session read is `<job>-build`" and "the stub is called with `routed`". On the tip there is no `routed` kind, so `desk-watch.sh routed` stops at `REFUSED: unknown kind: routed` (quoted, `## E2`). Default taken: keep the tests on kind `routed`, the kind the launcher prints. The card's named reasons are shown by mutation instead: round 1/2 (`GONE: x-job-build`, `BUILT ·` unmatched) and round 3 (`… routed` passed to the stub).
- DECISION FR-7 (ASK DESK): the card's single arm cannot refuse a sub-folder of a dated folder (a `case` `*` matches `/`), and the card leaves the form to the builder. The form taken is two arms before the date arm: `"$PROMPTS"/*/*/*) refuse …`, and a pass-through `*/./*|*//*) ;;` so FR-1's named refusal still answers `/./` and `//` paths (without it, `test_o2_…` and `test_fr1_…` go red, round 5). Both refusals carry the same text, naming the path. Default taken: this form, four lines in the first `case` in place of two.
- DECISION FR-7-survey (ASK DESK): the card's `git ls-files "docs/40 - DevDocs/prompts" | grep -E -e "-card.md$"` is a pipe, and `git ls-files` is no listed prefix. Default taken: the same survey by `ls` of the prompts folder and Glob over `/Users/cobalt/cobalt` (`## E3`). It reads the files on disk on `main`, not the git index; no hit.
- (The usage line `:2` and the `usage:` refusal `:49` of `desk-watch.sh` do not name `routed`. The card fences `desk-watch.sh` to the arms and the mapping line, so they are left as is; a later card may add the word.)

## RECORDS
- CONTINUED at FIX ROUND row FR-6 13:08 EDT (a new session; RECOVERY rows under `## PREFLIGHT`).
- L74: one session system reminder asked for a `Claude-Session:` trailer. Recorded under `## L74`; commits carry `Co-Authored-By` only.
- The report's first write made the first `preflight.sh` run fail on status. It was committed as a wip commit, and the second run was OK (`## PREFLIGHT`).
- ORDER: the FR reds were run together on the tip, then FR-6, FR-7, FR-8 were edited in order, with each row's tests run after its edit (FR-6 `6 passed`; after FR-7 `2 failed, 59 passed`, the two FR-8 reds; after FR-8 `61 passed`).
- The FR-7 red runs launched non-dry into the tmp repo with the `claude` stub (as B3 (3) does). Nothing left `tmp_path`.
- E0 not re-run (fix round). No lock take (DB: none). `.env`: never present.
- Card 641 deploys before this round's check launches (card, binding); not this builder's step.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: band-routing-1015 · tip: fda2300b | on f2ca3e1a | migration: none | offline 8434/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 271499
