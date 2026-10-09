# voice-clarify-fix-1009 — build report (2026-10-09)

## §0 Headline
- Card 193 built on `b7d37cdc`, tip `9feda305`: rows A, B, C1, C2 and the RUN row D, 5 of 5.
- A: the clarify sentence is spoken once. B: Confirm/Cancel show only while a change is pending. C1: a plan clarify records the candidates and history it was given. C2: the planner is told that answer and act always name a tool.
- Three suites green: offline 4060/0, with-DB 4947/0, live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0); `.env` removed.
- One decision: RESTARTS derives `com.cobalt.aset com.cobalt.radar`, where the card expected aset alone.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/193-voice-clarify-fix-card.md"` (18:58 EDT), exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/193-voice-clarify-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/193-voice-clarify-fix-card.md" · 0 · 933117a26f3b42ca06d2a657745583e9708efa47
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/193-voice-clarify-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Fri Oct  9 18:58:52 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/voice-clarify-fix-1009
    ?? "docs/40 - DevDocs/reports/voice-clarify-fix-build-2026-10-09.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · b7d37cdc docs(desk): successor 923058b9 takes over, voice drafter and https build launched, plan_shape joins row C (R774-R776)
diff · git diff --stat b7d37cdc · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/voice-clarify-fix-1009 · 0 · b7d37cdc docs(desk): successor 923058b9 takes over, voice drafter and https build launched, plan_shape joins row C (R774-R776)
env here · ls /Users/cobalt/cobalt-wt/voice-clarify-fix-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat b7d37cdc` | 0 | `docs(desk): successor 923058b9 takes over, …` — `docs/40 - DevDocs/reports/cto-2026-10-09.md \| 11 ++++++++---`, `docs/40 - DevDocs/reports/desk-wakeup-log.md \| 1 +`; 2 files changed, 9 insertions(+), 3 deletions(-) |
| A callers | `grep -rn -F "compose_reply(" src` | 0 | `turn.py:329: return done(tools.compose_reply(plan.say, CLARIFY_TEMPLATE), {"clarify": "plan"})` · `turn.py:346: reply = tools.compose_reply(plan.say, template)` · `tools.py:121: def compose_reply(say: Optional[str], template: str) -> str:` |
| A template | `grep -rn -F "CLARIFY_TEMPLATE" src` | 0 | `turn.py:52: CLARIFY_TEMPLATE = "I need a little more: which card, and what value?"` · `turn.py:329` · `turn.py:441` (`__all__`) |
| B style | `grep -n -F "#cv-voice .cv-row{display:flex" src/cobalt/voice/web.py` | 0 | `203: #cv-voice .cv-row{display:flex;gap:6px;align-items:center}` |
| C1 resolution | `grep -n -F "{\"clarify\": \"plan\"}" src/cobalt/voice/turn.py` | 0 | `329: …{"clarify": "plan"})` |
| C1 candidates | `grep -rn -F "card_candidates(" src` | 0 | `turn.py:290: candidates = card_candidates(cards)` · `resolve.py:37: def card_candidates(…)` |
| C2 build_messages | `grep -rn -F "build_messages(" src` | 0 | `agent.py:85: def build_messages(…)` · `agent.py:161: messages=build_messages(inputs, agent), …` |
| C2 validate_plan | `grep -rn -F "validate_plan(" src` | 0 | `agent.py:118: def validate_plan(…)` · `agent.py:168: plan = validate_plan(result.content, …)` |
| sizes | `wc -l …` | 0 | tools.py 258 · turn.py 441 · agent.py 175 · web.py 312 · test_voice_tools.py 252 · test_voice_turn.py 435 · test_voice_web.py 312 · test_voice_plan.py 180 · plan-replies.constructed.yaml 131 |
| READ 1 | `tail -n 3 …/voice-clarify-confirm-answer-2026-10-09.md` | 0 | last line: `FOR THE CHECK: "Brain 10-09: plan_shape joins card 193 row C; validate_plan unchanged; the fix gives the model the tool kinds and args, or corrects the tool spec, from production failure_detail."` |
| READ 2 | `tail -n 3 …/voice-turns-query-2026-10-09.md` | 0 | last line: `DESK READING (facts only, for the card's row C): (1) the transcripts are clear, … (4) Two other turns failed differently: plan_shape ("Cobalt can't think right now") and unsupported.` |
| 156 lines | `grep -n -F "web.py" …/156-https-only-card.md` | 0 | row B owns `start()` `:268`, on-load `:300`, `widget_html` `:306`–`:308`; none of `:199`–`:212` |
| RESTARTS empty | `uv run cobalt jobs restarts b7d37cdc..HEAD` | 0 | `docs/40 - DevDocs/reports/voice-clarify-fix-build-2026-10-09.md A DOCS -` · `RESTARTS: none` (the untracked report only; no code path) |

Read with the Read tool at BASE: `tools.py:121`–`:124` compose_reply; `turn.py:52`, `:284`–`:380`; `agent.py:85`–`:149` (raise lines `:134`, `:137`, `:141`, `:143`; tool line `:92`); `store.py:179`–`:189`; `resolve.py:37`–`:45`; `web.py:199`–`:212`, `:216`, `:247`–`:251`, `:297`–`:298`; `voice.yaml` (4 tools); test fixtures `test_voice_turn.py:28`–`:162`; `test_voice_tools.py:120`–`:123`.

Card records, copied: VOICE TURNS (11 rows, 22:41:52–22:49:40 UTC; the clarify reply doubled on every turn from 22:44:54 on). PLAN_SHAPE ROWS: the only `plan_shape` row is 22:49:40Z, transcript "What can you do? What can I ask you?", failure_detail `plan_shape: kind answer names no tool` (`agent.py:134`). CODE AT DRAFTING `e4586978` = BASE for src/tests/configs. RESTARTS expected `com.cobalt.aset`. DB: all new tests offline. COMMANDS: none new. Re-read here: the line numbers above match the card at BASE; the production rows are not re-readable (no production string, by design).

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` — proven (authorize.sh, preflight.sh ran). The rest per BUILD-HUB's table.

## E0 BASELINE
- Offline on BASE `b7d37cdc`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4054 passed, 790 skipped, 1 xfailed, 36 warnings in 658.45s (0:10:58)` (exit 0; 0 failed, 0 errors; the skips are the with-DB and live-note ones, e.g. `test_voice_web.py:163: reaches cobalt_dev (lock-relief G1)`).
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.02s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Commit `5265a72f wip(voice-clarify-fix-1009): red` (tests only; no `src/` edit). `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_voice_tools.py tests/cobalt/test_voice_turn.py tests/cobalt/test_voice_web.py tests/cobalt/test_voice_plan.py` → `5 failed, 184 passed, 6 skipped in 1.29s`. Each red, first line:
- A `test_a_say_that_repeats_the_template_is_dropped` — `AssertionError: I need a little more: which card, and what value? I need a little more: which card, and what value?` / `assert 2 == 1` (template twice).
- A `test_a_clarify_after_a_clarify_is_not_doubled` — `AssertionError: I can hear you. What would you like to do? I need a little more: which card, and what value? I need a little more: which card, and what value?` / `assert 2 == 1`.
- C1 `test_a_plan_clarify_records_the_candidates_and_history_it_was_given` — `AssertionError: assert {'clarify': 'plan'} == {'candidates'... 'history': 0}`.
- B `test_a_hidden_widget_row_is_not_displayed` — `assert '#cv-voice .cv-row[hidden]{display:none}' in "\n<style>…` (rule absent).
- C2 `test_the_system_message_states_the_rule_the_stored_shape_broke` — `assert 'answer and act always name one tool from the list; …' in "You are Cobalt's voice desk: …"` (sentence absent).
- C2 fixture case `answer with no tool for a question about what voice can do` (`expect: plan_shape`) PASSES on BASE, as the card says (`validate_plan` unchanged).
- Row A's negative control (`"Which card did you mean?"` kept) sits after the failing loop; it is proven at E3's green and by its own mutation there.
No with-DB red: no lock taken.

## E3 THE ROWS
Commit `9feda305 fix(voice-clarify-fix-1009): clarify spoken once, pending row hidden, clarify records its inputs, planner told answer/act name a tool (A, B, C1, C2; L1, L3, L45)` — 8 files, 28 insertions, 2 deletions (4 src files, 4 DevDocs pages).

| row | change | green |
|---|---|---|
| A | `tools.py`: `_fold` (casefold, whitespace collapsed); `compose_reply` keeps `say` only when `_fold(template) not in _fold(say)` (equal or containing); figures check unchanged | the four files: `189 passed, 6 skipped in 1.18s` |
| B | `web.py:204` (new, directly after `:203`): ` #cv-voice .cv-row[hidden]{display:none}`; no other `web.py` line | same run |
| C1 | `turn.py:329`–`:331`: resolution `{"clarify": "plan", "candidates": [c.id for c in candidates], "history": len(history)}`; no other resolution | same run |
| C2 | `agent.py` `build_messages` system message, after the `tool:` line: "answer and act always name one tool from the list; their tool is never null. A question no tool answers, such as what you can do, is clarify with tool null, and say tells the trader in words what the tools below can do." `validate_plan` and `voice.yaml` unchanged (the tool specs are right; the shape broke a rule the message never stated) | same run |

MUTATIONS (Edit tool, each undone with Edit; `git diff --stat` after → `4 files changed, 16 insertions(+), 2 deletions(-)`, the fix):
- A, fix undone (`and _fold(template) not in _fold(say)` removed): `2 failed` — `test_voice_tools.py:136: AssertionError: I need a little more: which card, and what value? I need a little more: which card, and what value?`; `test_voice_turn.py:195: AssertionError: I can hear you. What would you like to do? I need a little more: … I need a little more: …`.
- A negative control broken (drop a `say` sharing ANY word with the template — X3's case): `1 failed` — `test_voice_tools.py:138: AssertionError: assert 'I need a lit...d what value?' == 'Which card d...d what value?'`.
- B, rule removed: `1 failed` — `test_voice_web.py:257: assert '#cv-voice .cv-row[hidden]{display:none}' in "\n<style>…`.
- C1, resolution back to `{"clarify": "plan"}`: `1 failed` — `test_voice_turn.py:204: AssertionError: assert {'clarify': 'plan'} == {'candidates'... 'history': 0}`.
- C1, history hard-wired `0`: `1 failed` — `test_voice_turn.py:207: AssertionError: assert {'candidates'... 'history': 0} == {'candidates'... 'history': 1}`.
- C2, sentence removed: `1 failed, 28 passed, 5 skipped` — `test_voice_plan.py:84: assert 'answer and act always name one tool from the list; …' in "You are Cobalt's voice desk: …"`.
- C2 fixture case, `validate_plan :133` weakened (`and False`): `2 failed, 27 passed, 5 skipped` — `[answer with no tool]` and `[answer with no tool for a question about what voice can do]`, each `agent.py:140: KeyError: None` (the case is a pin that `validate_plan` stays strict).
DevDocs: one dated line each in `docs/40 - DevDocs/cobalt/voice/{tools,web,turn,agent}.md`.

## RESTARTS
`uv run cobalt jobs restarts b7d37cdc..HEAD` (tip `9feda305`; the untracked report appears as DOCS), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/voice/agent.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/tools.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/turn.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	M	DOCS	-
docs/40 - DevDocs/reports/voice-clarify-fix-build-2026-10-09.md	A	DOCS	-
src/cobalt/voice/agent.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/tools.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/turn.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_voice_plan.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_tools.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_turn.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
tests/fixtures/voice/plan-replies.constructed.yaml	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. Row D (RUN): the card expected `com.cobalt.aset`; the tool derives `com.cobalt.aset com.cobalt.radar` → DECISION D.

## W THE THREE SUITES
`<tip>` = `9feda305`. ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh voice-clarify-fix-1009 all --deploy` (no `--deselect`: no with-DB test added; no `--tickers`: no test writes a ticker to `cobalt_dev`; no `--migration`). Exit 0. Verdict lines, whole:
```
offline 4060/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4947/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/voice-clarify-fix-1009-all-20261009-191322.log
```
- (a) offline: log `:867` `4060 passed, 790 skipped, 1 xfailed, 36 warnings in 661.12s` → `<p>` = 4060 (BASE 4054 + this build's 6: `test_a_say_that_repeats_the_template_is_dropped`, `test_a_clarify_after_a_clarify_is_not_doubled`, `test_a_plan_clarify_records_the_candidates_and_history_it_was_given`, `test_a_hidden_widget_row_is_not_displayed`, `test_the_system_message_states_the_rule_the_stored_shape_broke`, the fixture case `[answer with no tool for a question about what voice can do]`).
- (b) `lock taken: voice-clarify-fix-1009` (`:873`), waited 0 min; `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's only (`:878`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:884`); proof-only `LEVEL 0013`.
- (c) pass 1 (`:937` `pass 1: whole (deploy)`), executed command (`:939`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py` → `:1093` `4752 passed, 7 skipped, 89 deselected, 3 xfailed, 43 warnings in 810.90s` → `<d1>` = 4752. The 7 skips are the seven SKIPPED lines above; no line marked `OUTSIDE the allowed set` (`grep -n -F "OUTSIDE"` → nothing).
- (c2) **`dev forward: APPLIED 19:38:22`** (`:1095`), 0001–0023 applied, every table `OK` or `CREATED`, "content UNCHANGED on every table"; `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1171`).
- (c3) pass 2 (`:1173`, the PASS 2 list of `ops/desk/gate-lists.md`; none of this build's) → `:1899` `195 passed, 1 deselected, 5 warnings in 235.99s` → `<d2>` = 195; `<d>` = 4752 + 195 = 4947 = `with-DB 4947/0`.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no row to `cobalt_dev`.
- (e) live-note `:2087` `146 passed, 1 skipped, 15 warnings in 28.37s` → `<l>` = 146; the skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1965`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:2018`); `ls /Users/cobalt/cobalt-wt/voice-clarify-fix-1009/.env` → `No such file or directory`.
- The log's ERROR lines `REFUSED (…): it is 20:30:00 ET on 2026-09-02 — inside MARKET RESET` (`:1202`–`:1358`) are tests' constructed clock driving the session guard; their suites passed.

## PRE-STOP SELF-CHECK
(1) Every added test shown red for its named reason: A tools — E2 red `assert 2 == 1` (template twice) and E3 mutation red at `:136`; A negative control — E3 mutation red at `:138` (`'Which card d...'` dropped); A turn — E2 red and E3 mutation red at `test_voice_turn.py:195`; B — E2 red and mutation red at `test_voice_web.py:257`; C1 — E2 red and mutation reds at `:204` (resolution) and `:207` (history); C2 sentence — E2 red and mutation red at `test_voice_plan.py:84`; C2 fixture case — mutation red (`validate_plan` weakened, `KeyError: None`). None stayed green.
(2) Every entry path pinned: `compose_reply` callers (PREFLIGHT grep) `turn.py:329` (clarify) → `test_a_clarify_after_a_clarify_is_not_doubled`; `turn.py:346` (read answers) → `test_voice_tools.py:121`–`:123` (kept `say`, figures drop, None) and the new tools test on the same function; `card_candidates` caller `turn.py:290` → C1 test with two cards and with `read_cards` `[]`; `build_messages` caller `agent.py:161` (`plan_turn`) → C2 test calls `build_messages` directly, `plan_turn`'s own tests in `test_voice_plan.py` pass (offline 4060/0); `validate_plan` caller `agent.py:168` → the fixture cases. Edge inputs: case/whitespace variant, containment with a prefix, other words (negative control), empty candidate list, history 0 and 1.
(3) Re-read at the tip `9feda305`: `grep -n -F "cv-row[hidden]" src/cobalt/voice/web.py` → `204`; `grep -n -F "_fold(" src/cobalt/voice/tools.py` → `121`, `129`; `grep -n -F "\"history\": len(history)" src/cobalt/voice/turn.py` → `331`; `grep -n -F "answer and act always name one tool" src/cobalt/voice/agent.py` → `103`; `git diff --stat b7d37cdc 9feda305 -- src/cobalt/voice/web.py` → `1 file changed, 1 insertion(+)`; the gate log lines quoted by `grep -n -F`.

## FOR THE CHECK
- Range `b7d37cdc..9feda305`: `5265a72f wip(voice-clarify-fix-1009): red`; `9feda305 fix(voice-clarify-fix-1009): clarify spoken once, pending row hidden, clarify records its inputs, planner told answer/act name a tool (A, B, C1, C2; L1, L3, L45)`. The report commit follows.
- Per row: reds at `## E2 RED`, mutations and greens at `## E3 THE ROWS`.
- X3: a `say` that only shares words with the template is KEPT (the negative control; the word-overlap mutation turns it red). A read reply (`turn.py:346`) changes only when its `say` holds the whole rendered template; otherwise unchanged.
- X4: `web.py` changes by one line, `:204`, directly after `:203`, inside `<style>`; card 156's `:268`–`:287`, `:300`, `:306`–`:308` untouched (now `:269`–`:288`, `:301`, `:307`–`:309` after the one-line shift).
- C2's reading of the stored row: failure_detail `plan_shape: kind answer names no tool` = `agent.py:134`. The tool specs in `voice.yaml` are correct for the question (no tool answers "what can you do"), so the fix is the system message's added rule, not a spec. `validate_plan` unchanged (`git diff b7d37cdc 9feda305 -- src/cobalt/voice/agent.py` adds only the 4 lines in `build_messages`).
- Callers: PREFLIGHT table. RUN row D: `## RESTARTS` table, whole.
- Suites: `## W`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. Lock taken (log `:873`, gate started 19:13 per the log name), released (`:2018`) before 19:43:44 (`date`).
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none — BUILT (the desk verifies and launches the check)

## DECISIONS
- DECISION D: `uv run cobalt jobs restarts b7d37cdc..9feda305` derives `RESTARTS: com.cobalt.aset com.cobalt.radar` (each `src/cobalt/voice/*` row: `static import reach` → `com.cobalt.aset,com.cobalt.radar`); the card's `## RECORDS` expected `com.cobalt.aset` only. Safe default taken: the stop line carries the derived table's line, unchanged; the deploy restarts both. Not fixed here (RUN row).

## RECORDS
- L74: a system reminder asked for a `Claude-Session:` line in commits; recorded under `## L74`, not acted on.
- Lock: one take, by `gate.sh` at W; no extra take. `.env: removed, proven gone (W)`.
- No `REFUSED, not needed` line; no `CONTINUED` line.
- Card records re-read: the code lines match BASE (PREFLIGHT); the production rows were not re-read (no production string).
- Row C2's sentence routes a "what can you do" question to clarify; its reply is the planner's `say` followed by `CLARIFY_TEMPLATE` ("which card, and what value?"), whose wording is outside this job (`## NOT IN THIS JOB`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: voice-clarify-fix-1009 · tip: 9feda305 | on b7d37cdc | migration: none | offline 4060/0 | with-DB 4947/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 179120
