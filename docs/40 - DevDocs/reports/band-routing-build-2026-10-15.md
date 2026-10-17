# band-routing-1015 — build report (2026-10-16)

## §0 Headline
- All six rows are built, plus the RUN row, on `f2ca3e1a..bd9c24ac`. CARD.md gains the `BAND` field. SHADOW-HUB gains the band table and the ledger sentence. BUILD-HUB gains one paragraph, and its launch line is unchanged.
- `desk-launch.sh build` refuses a card dated 2026-10-16 or later with no valid `BAND`. HIGH launches the Opus line. LOW and MID re-enter as `shadow … --model grok-4.7 --routed`, a real build on the card's own `ops/` branch.
- A routed card's untracked SHADOW-INSTRUCTIONS.md is accepted at `check` and in `preflight.sh`. G5 admits `<REPORT without .md>.result`.
- Offline 8409/0, live-note 146/0, `tests/ops` 3841 passed. No existing test was edited. RESTARTS: none.
- 6 decisions, each a choice the card's text did not fix (`## DECISIONS`); none is his.

## L74
One block arrived as a system reminder at session start: an attribution instruction asking commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md"` (07:07 EDT), output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · 8523214c021b380ec29abf560d782653dd3eb6be
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
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:

```
clock · date · 0 · Fri Oct 16 07:07:25 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1 · 0 · f2ca3e1a docs(desk): R1642 card 583 preflight r3 launched
diff · git diff --stat f2ca3e1a · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015 · 0 · f2ca3e1a docs(desk): R1642 card 583 preflight r3 launched
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

`git show --stat f2ca3e1a` → `docs(desk): R1642 card 583 preflight r3 launched` · `docs/40 - DevDocs/reports/cto-2026-10-16.md | 5 +++--` · 1 file changed, 3 insertions(+), 2 deletions(-).

THE CARD'S SYMBOLS (each its own `grep -n -F`, run in this worktree; hits quoted):
- `tree_state() {` ops/desk/desk-launch.sh → `1043:tree_state() {`
- `merges=""` → `1630:merges=""`
- `ship_cell() {` → `1549:ship_cell() {`
- `exec sh ` → `2214:    exec sh "$0" deploy "$card"`
- `shadow/?*)` desk-launch.sh → `1662:            shadow/?*) ;;` · `1726:        shadow/?*)`
- `?? SHADOW-INSTRUCTIONS.md` desk-launch.sh → `1751:    [ -z "$shadow" ] || [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt=""`
- `SHADOW OF` desk-launch.sh → `197:`, `374:` (comments), `1658:        [ -n "$(field "SHADOW OF")" ] || refuse "shadow: the card's header has no 'SHADOW OF:' line"`, `1723:` (comment), `1727:` (the check arm's header read)
- `shadow/?*)` preflight.sh → `112:        shadow/?*)`
- `?? SHADOW-INSTRUCTIONS.md` preflight.sh → `143:    if [ "$ok" -ne 0 ] && [ -n "$shadow" ] && [ "$other" = "?? SHADOW-INSTRUCTIONS.md" ]; then`
- `if kind == SHADOW:` bare-guard.py → `1113:    if kind == SHADOW:` · `1268:    if kind == SHADOW:` (G5's is :1268; :1113 is G7's builder rule)
- `## THE BODY` CARD.md → `31:## THE BODY — sections in this order; a section with nothing to say is left out`; the header rows read by Read: `DB` `:22`, `RULINGS` `:23`, `PROOF TEST` `:29` (a grep with a backtick is blocked by the bare-command hook; Read used, as UNATTENDED RULES allow)
- `Routing takes effect only on his word` SHADOW-HUB.md → `73:` (the sentence ends `Routing takes effect only on his word on the result (L29).`)
- `accepted by HIS word 2026-10-11 (R1107).` SHADOW-HUB.md → `26:- Terra: …`
- `(1) it enters` BUILD-HUB.md → `10:(1) it enters `/Users/cobalt/cobalt-wt/<WORKTREE>`, then (2) runs the line below. The desk's own cwd does not move.`
- `BAND` over the six rows' files → no hit (exit 1)

`wc -l` of each file a row edits: desk-launch.sh 2339 · preflight.sh 288 · bare-guard.py 1415 · CARD.md 158 · SHADOW-HUB.md 103 · BUILD-HUB.md 112.

`tail -n 3` of each report `## READ` names (last line quoted):
- `reports/routing-table-answer-2026-10-14.md` → `Recommended: A. After A, the desk records it, folds L27/L29, and a K5 card puts `BAND:` in CARD.md and the routing in the launcher.`
- `reports/cto-2026-10-15-words.md` → `Relayed by the brain (quoted, marked "Dejan said"; it counts under L79, confirmed by him at R1531): "low grok, terra backup / medium grok, terra backup / High opus, grok when I say so / Sonnett routing for now / JEV paralel run and learning". Full text: …`
- `reports/cto-2026-10-15.md` → `HANDOVER: predecessor f8f8324b → successor 8e552225 at 19:24 · pane w2:pV1`

The card's `## RECORDS`, copied by reference (the card file, committed `8523214c`): drafter reads at `main` HEAD 2026-10-15; amend 589; amend 2 (prompt 627) adding B5 and B6 from `reports/band-routing-answer-2026-10-16.md`; restart class `none`; owed after deploy: install-ops and the first LOW/MID dry launch. Re-read here: `reports/routing-table-answer-2026-10-14.md` whole (47 lines; `## HIS RULING — 2026-10-15 (B)` at `:33-43`, condition 3 at `:28`, condition 4 at `:29`) and `reports/band-routing-answer-2026-10-16.md` whole (Q2 `:10`, issue 6 `:11`).

`uv run cobalt jobs restarts f2ca3e1a..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md	A	DOCS	-
RESTARTS: none
```
(the one path is this report, written before the run; no commit in the range).

DB: none card → no lock probe; the with-DB strings are not used by this build.

## E0 BASELINE
On `f2ca3e1a`:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 701.04s (0:11:41)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.13s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
I wrote ONE new file, `tests/ops/test_band_routing_1015.py`, and made no `src/` edit. Its first run had 10 setup ERRORs in the B5 `CheckDesk` (`FileExistsError` on the worktree's reports folder, which the tmp repo already tracks). That was a harness bug, not a row's red. I fixed it with `mkdir(..., exist_ok=True)` and ran again. On BASE, `uv run pytest -q -rfEp -p no:cacheprovider --color=no --tb=no -W ignore::DeprecationWarning tests/ops/test_band_routing_1015.py` gave `22 failed, 14 passed in 6.62s`.

REDS, each failing for its row's named reason (first lines from `--tb=line` runs):
- B1 `test_b1_card_md_names_band_once_in_the_header_table_and_once_in_its_paragraph` → `:70: assert 0 == 1` (no line starts `` | `BAND` | ``).
- B2 (1) `test_b2_builders_holds_the_band_table_once` → `:95: AssertionError: ('LOW', [])`.
- B2 (2) `test_b2_results_table_carries_the_ruling_and_the_ledger_triggers` → `:106: assert 'R1532' in 'The desk copies this shape …'`.
- B4 `test_b4_build_hub_names_the_band_routing_once_before_the_launch_line` → `:126: assert 0 == 1`.
- B3 (1)/(2) `test_b3_a_low_or_mid_card_launches_the_shadow_gate_seat_with_the_band_builder[LOW|MID]` → `:299: assert 'MODEL: grok-4.7' in 'git -C … worktree add -b ops/x-band … claude --bg "Read '…/BUILD-HUB.md' …"'` (the Opus line).
- B3 (3) `test_b3_a_missing_or_bad_band_is_refused_on_a_new_card[None|low|LOWISH|]` → `:308: assert 0 == 1` (each launched, exit 0, `RUN: claude --bg … BUILD-HUB.md …`).
- B3 (4) `test_b3_routed_flag_is_refused_off_its_band[HIGH-grok-4.7|None-grok-4.7|LOW-claude-sonnet-5-5]` → `:287: AssertionError: REFUSED: shadow: unknown argument '--routed'`.
- B3 (5) `test_b3_a_routed_launch_keeps_the_signed_row_and_the_mode_refusals` → `:286: assert 0 == 1` (stdout is the Opus build line, exit 0).
- B3 (6) `test_b3_a_resume_step_on_a_routed_card_is_refused` → `:286: assert 0 == 1` (`claude --bg "CONTINUE: STEP-X. Read '…/BUILD-HUB.md' …"`, exit 0).
- B3 (7) `test_b3_the_backup_is_a_hand_launch` → `:338: AssertionError: REFUSED: shadow: unknown argument '--routed'`.
- B3 (8) `test_b3_a_routed_launch_is_a_real_build_not_a_shadow` → `:349: AssertionError: REFUSED: shadow: unknown argument '--routed'`.
- B5 check `test_b5_a_routed_tree_with_its_untracked_instructions_reaches_its_check[LOW|MID]` → `:460: … REFUSED: …/wt/x-job is not clean (the check session commits there)`.
- B5 preflight `test_b5_a_routed_tree_with_its_untracked_instructions_passes_preflight_status[LOW|MID]` → `:474: assert 'FAILED PREFLIGHT: status' not in …` (status row `## ops/x-job` / `?? SHADOW-INSTRUCTIONS.md`).
- B6 `test_b6_the_gate_seat_writes_its_result_file` → `:539: AssertionError: route: this seat writes only inside its fence …` (`assert 2 == 0`).

CONTROLS GREEN on BASE (14): `test_b1_control_the_other_header_rows_stand`, `test_b2_control_the_three_builder_rows_stand`, `test_b4_control_the_launch_line_and_the_model_line_stand`, `test_b3_control_a_high_card_builds_on_the_build_hub_line`, `test_b3_control_an_old_card_with_no_band_builds_as_before`, `test_b3_control_shadow_without_routed_still_demands_its_own_header`, `test_b5_control_a_tree_that_is_not_routed_is_still_dirty_at_its_check[None-2026-10-16|HIGH-2026-10-16|LOW-2026-01-02]`, `test_b5_control_a_tree_that_is_not_routed_still_fails_preflight_status[same three]`, `test_b6_control_the_report_passes_and_every_other_path_is_still_fenced`, `test_b6_control_a_link_named_as_the_result_file_is_fenced`.

There is no RUN row with a test (R3 is the restarts table, `## RESTARTS`) and no with-DB red (DB: none), so no lock was taken. Commit `1be72d81 wip(band-routing-1015): red`.

## E3 THE ROWS
I built B1, B2, B4, then B3, then B5 and B6, re-reading every anchor from the file before each edit (PREFLIGHT greps and Read). The reds were run once on BASE before the first edit, not once more before each row's edit (`## RECORDS`).
- B1 `CARD.md`: one `` | `BAND` | `` row between `DB` and `RULINGS`, and one paragraph `BAND is set by the drafter …` between the `PROOF TEST` row's blank line and `## THE BODY`, byte for byte from the card. `grep -c -F "BAND"` → `2`.
- B2 `SHADOW-HUB.md`: the `BAND ROUTING (…)` paragraph and the four-row band table after the Terra bullet (`:26`), before `<pass prompt>`. The `## RESULTS TABLE` sentence `:73` is replaced by the card's text. Line `:1`, the launch line and the three builder rows are untouched.
- B4 `BUILD-HUB.md`: one paragraph `BAND (his 2026-10-15 R1532): …` at `:12`, between `(1) it enters` (`:10`) and the launch line (now `:14`). The launch line and `:3` are unchanged.
- B3 `desk-launch.sh`: `routed=""` beside `model=""`, and a `--routed)` arm in the shadow argument loop. A new block before `merges=""` holds `BAND_FROM=20261016`, the card's date (its first folder under `$PROMPTS`, dashes cut), `band_row()` (awk over SHADOW-HUB's `## BUILDERS`, blanks and backticks cut) and the build-kind call: HIGH → stderr `BAND: HIGH → Opus 5.5 (BUILD-HUB.md line)`; LOW/MID → refuse on a resume step, stderr `BAND: <band> → <builder> (backup <backup>)`, `exec sh "$0" shadow "$card" --model <builder> --routed`; anything else on a dated card → `refuse "incomplete card: BAND must be LOW, MID or HIGH"`. The same block holds the `--routed` check (a dated card, BAND LOW/MID, `--model` = the row's cell 3 or 4, else `refuse "shadow: --routed needs a card with BAND LOW or MID and its builder or backup id"`) and one stderr line `ROUTED: a real build — BRANCH <branch> · REPORT <report>`. Three skips under `--routed`: `SHADOW OF:`, the `shadow/` BRANCH and the JOB-ends-in-slug test. The launch tail (`:2218-2304` at BASE) and `install-ops` are not touched.
- B5 `desk-launch.sh` check arm: `routed_tree` is set for a dated LOW/MID card, and the one `?? SHADOW-INSTRUCTIONS.md` test accepts `shadow` or `routed_tree` (the literal still occurs once, `test_hub_text_1013.py:85`). `preflight.sh`: `BAND_FROM`, plus `routed` for a check whose card folder is dated on or after it with BAND LOW/MID. The status test accepts `shadow` or `routed`, and a routed card prints `status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)`.
- B6 `bare-guard.py` G5 `if kind == SHADOW:`: a path equal to `REPORT` with `.md` cut and `.result` added passes. The link test above it stands.

GREEN at the fix: `uv run pytest -q tests/ops/test_band_routing_1015.py` → `36 passed in 7.38s`. The six existing files `test_shadow_hub_file.py test_desk_launch_shadow.py test_desk_launch_prechecks.py test_build_hub_no_clutter.py test_hub_lines.py test_deploy_card.py` → `423 passed in 137.77s (0:02:17)`, and `git diff --stat f2ca3e1a -- <those six>` → nothing. Neighbours `test_band_routing_1015.py test_preflight.py test_bare_guard.py test_hub_text_1013.py` → `1948 passed in 77.53s`.

THE MUTATIONS (Edit tool, run alone, undone with Edit, then `git diff --stat` back to the fix):
- B1/B2/B4 (row `BANDX`; band table's LOW row deleted; RESULTS sentence back to `Routing takes effect only on his word`; `BAND (his R1532)`) → `4 failed, 3 passed`: `:70: assert 0 == 1`, `:95: ('LOW', [])`, `:106: assert 'R1532' in …`, `:126: assert 0 == 1`.
- B3 (exec line removed; `rok=1` forced) → `7 failed, 9 passed`: (1)[LOW], (1)[MID], (4)×3, (5), (8).
- B3 (dated-card refusal `*) ;;`; resume refusal → `true`; `SHADOW OF` skip removed) → `10 failed, 6 passed`: (1)×2, (3)×4, (5), (6), (7), (8).
- B5/B6 (`1LOWX|1MIDX`; preflight `LOWX|MIDX`; G5 compares `report + ".result"`) → `6 failed, 23 passed`: B5 check ×2, B5 preflight ×2, `test_b6_the_gate_seat_writes_its_result_file`, `test_b6_control_the_report_passes_and_every_other_path_is_still_fenced` (the `.md.result` path is now admitted).
- B5 controls (`routed_tree` and preflight `routed` set for any band) → `5 failed, 8 passed`: check controls ×3, preflight controls [None], [HIGH]. Preflight's date gate (`-ge 0`) → `1 failed`: `…still_fails_preflight_status[LOW-2026-01-02]`.
- The remaining controls (`JOBX`; `claude-opus-5-5` in the HIGH cell; `MODEL: Opus 5.6`; `band_dated=1` always; HIGH routed; `SHADOW OF` refusal off; G5 link test off) → `8 failed, 6 passed`: `test_b1_control…`, `test_b2_control…`, `test_b4_control…`, the three `test_b3_control…`, `test_b5_control…dirty_at_its_check[LOW-2026-01-02]`, `test_b6_control_a_link…`.
- After each undo, `git diff --stat` printed nothing past the fix commit and the file ran `36 passed`.

DevDocs: no page under `docs/40 - DevDocs/cobalt/` documents these ops scripts. A grep of `desk-launch|preflight\.sh|bare-guard` hits only `cobalt/jobs/restarts.md`, which is not their page, so there is no dated line to add (precedent: `close-automation-build-2026-10-15.md:99`).

Commit `bd9c24ac feat(band-routing-1015): BAND header, band table, launcher routing, routed check and result-file fence (B1-B6, L27 L29 L72)`. `grep -n -E -e "git show" -e "subprocess" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → `18: import subprocess`, `195`, `272/274`, `285`, `438/440`, `443/445`, `525/531` (the tmp-repo `git` helper and the runs of the launcher, preflight.sh and bare-guard.py, all on tmp paths). No `git show`, and no 8-hex hit.

## RESTARTS
R3 (RUN): `uv run cobalt jobs restarts f2ca3e1a..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `bd9c24ac`. (a0): `git diff --name-only --no-renames f2ca3e1a` →
```
docs/40 - DevDocs/prompts/BUILD-HUB.md
docs/40 - DevDocs/prompts/CARD.md
docs/40 - DevDocs/prompts/SHADOW-HUB.md
ops/desk/bare-guard.py
ops/desk/desk-launch.sh
ops/desk/preflight.sh
tests/ops/test_band_routing_1015.py
```
Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/BUILD-HUB.md)` · `offline 8409/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261016-073149.log`. Its two runs: `4568 passed, 806 skipped, 1 xfailed` (`:888`) and `3841 passed, 1 xfailed` (`:959`). The tests this build adds are the 36 of `tests/ops/test_band_routing_1015.py`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261016-075807.log`. The only SKIPPED is `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no -W ignore::DeprecationWarning tests/ops` → `3841 passed, 1 xfailed in 845.79s (0:14:05)`.
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red. The 22 row tests were red on BASE (`## E2 RED`) and red again under their row's mutation. The 14 controls were red under the control mutations (`## E3`, the last two mutation bullets). No test stayed green under its mutation.
(2) Entry paths: `desk-launch.sh build` (B3 (1)-(3), (5), (6), (8), HIGH control, old-card control); `desk-launch.sh shadow … --routed` ((4), (7), (8)) and without `--routed` (control); `desk-launch.sh check` (B5 ×2 + 3 controls); `preflight.sh check` (B5 ×2 + 3 controls); G5 Write as the gate seat (B6 + 2 controls). Callers: `grep -rn -F "desk-launch.sh build" ops/desk` hits only the usage comments `desk-launch.sh:17`, `:27`, because the desk types the command. `preflight.sh shadow` (build rows) is unchanged and pinned by `test_preflight.py::test_386_d4…`, green in the neighbour run. Edge inputs: no BAND, `low`, `LOWISH`, an empty value, a card dated before BAND_FROM, a HIGH card, a resume step, a non-band id, the `.md.result` spelling and a link.
(3) Re-read at the tip: `grep -n -F "BAND_FROM" ops/desk/desk-launch.sh` → `1636`, `1642`, `1648`, `1788`; `grep -n -F "card 583"` over the three scripts → `desk-launch.sh:392`, `:1714`, `:1788`, `preflight.sh:118`, `bare-guard.py:1277`; `grep -n -F "BAND"` of the two hubs → `SHADOW-HUB.md:28`, `BUILD-HUB.md:12`; `grep -c -F "BAND"` CARD.md → `2`; `git log --oneline f2ca3e1a..HEAD` → the two commits below.

## FOR THE CHECK
- Range `f2ca3e1a..bd9c24ac`: `1be72d81 wip(band-routing-1015): red` · `bd9c24ac feat(band-routing-1015): BAND header, band table, launcher routing, routed check and result-file fence (B1-B6, L27 L29 L72)`.
- Per row: reds in `## E2 RED`, mutations and greens in `## E3 THE ROWS`.
- RUN row R3: the table in `## RESTARTS`, whole.
- Suites: offline 8409/0 (`gate.sh band-routing-1015 offline`), live-note 146/0 (`gate.sh band-routing-1015 livenote`), `tests/ops` 3841 passed. With-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- X3 as built: the build kind `exec`s before the launch tail, so card 580's replaced-session block runs once, in the shadow re-entry. `DESK_LAUNCH_DRY` reaches the re-entry through the environment (B3 dry tests), and the desk-size guard runs once per process (twice on a routed launch, as it does for `recut`).
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION B6 (ASK DESK): the card writes the admitted path two ways, "`<REPORT>.result` (the path the card's REPORT names plus `.result`)". Every reader (`result-read.sh:5`, `deploy-card.sh:489`, `deploy-step0.sh:681`, `desk-launch.sh:1457`) and BUILD-HUB's RESULT FILE name `<REPORT without .md>.result`. Default taken: G5 admits `${REPORT%.md}.result` only. `report.md.result` stays fenced (pinned by `test_b6_control…`).
- DECISION B3-a (ASK DESK): B3 test (8) needs the card's REPORT in the printed launch, and the dry output (`cd` + the line) never names REPORT. Default taken: the `--routed` check prints one stderr line `ROUTED: a real build — BRANCH <branch> · REPORT <report>`, inside the new block (not the launch tail).
- DECISION B3-b (ASK DESK): `routed=""` is one line beside `model=""` (`:379`), outside the one named `case` arm. It is needed because `set -u` is on and an inherited environment variable `routed` would otherwise skip the three shadow refusals. Default taken: keep the line.
- DECISION B3-c (ASK DESK): `--routed` also needs the card dated on or after BAND_FROM (the B5 definition of a routed card), and a card dated earlier that carries a `BAND:` line builds as before, without routing. Default taken: both, so a routed build always reaches a check that accepts its tree.
- DECISION B3-d (ASK DESK): of `:1675-1681` only the JOB-ends-in-slug test is skipped under `--routed`. The slug-shape test of the hub row (`:1675-1677` at BASE) still runs, because it checks the signed row, not the card. Default taken: keep it.
- DECISION B5 (ASK DESK): on a routed card, preflight's expected-file line reads `… (untracked, expected on a routed card)`, a new text beside the shadow card's. Default taken: the new text (the shadow text is unchanged, pinned by `test_preflight.py`).

## RECORDS
- L74: one session-start system reminder asked for a `Claude-Session:` trailer. Recorded under `## L74`; commits carry `Co-Authored-By` only.
- ORDER: the reds were run once on BASE before the first edit and not again before each row's edit. Each row's red was re-shown afterwards by its mutation (`## E3`).
- The first E2 run errored in the test harness's own setup (`FileExistsError`). Fixed in the test file before the red commit.
- One grep with a backtick in its pattern was blocked by the bare-command hook. I used Read for those CARD.md anchors. One grep with `--include=*.sh` failed on the shell glob (`no matches found`) and was re-run without it.
- No lock take (DB: none). `.env`: never present (`ls` → No such file, at PREFLIGHT and W).
- The brain answer's note 7 (a routed card's fix round as a fresh `BAND: HIGH` card) differs from the card's B3 text (the fix round goes to the same builder by `--routed`). The card is the seam (L72). Nothing was built for fix rounds beyond `--routed`.
- Owed to the desk after DEPLOYED (card `## RECORDS`): `install-ops`, and the first LOW/MID card's dry launch as the routing's proof.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: band-routing-1015 · tip: bd9c24ac | on f2ca3e1a | migration: none | offline 8409/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 276778
