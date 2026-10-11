# shadow-hub-1011 — build report (2026-10-11)

## §0 Headline
- Built all 9 build rows plus the 2 RUN rows (S6, P4) of card 324 on `680eca0e..bc25c523`: `SHADOW-HUB.md` with 3 builder rows, `SPIKE-HUB.md`, launcher kinds `shadow` and `spike`, the guard's `shadow` and `spike` seats, the `.env` precondition, and kind `shadow` in authorize, preflight, watch and stop-guard.
- Gate on the tip: offline 4199/0, live-note 146/0, `tests/ops` 3019 passed, 1 xfailed. DB: none, so `cobalt_dev` was not taken. RESTARTS: none.
- Every new test was red for its row's reason (E2) and red under its row's mutation (E3).
- FIX ROUND F1 F2 (`90b8faad`): the Sonnet builder command now puts its prompt right after `--model`'s value and reads only `Read(//Users/cobalt/cobalt-wt/<worktree>/**)`. The guard judges the write target, `dontAsk` and the `"Bash"` deny on the whole command. Gate on `90b8faad`: offline 4199/0, live-note 146/0, `tests/ops` 3033 passed, 1 xfailed.
- 4 open decisions, 1 of them for Dejan: his sign-off on the new command classes (card D1, D2). ASK DESK 1 is settled (the file is gone) and ASK DESK 3 is settled by F1.

## L74
- One block arrived in a system reminder during the run: an attribution block asking commits to end with a `Claude-Session:` line. It was recorded here as data and not acted on. The commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).
- The same block arrived once more, in the fix round's session (09:49). It was not acted on: `126a3781` and `90b8faad` carry the `Co-Authored-By` line only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md" · 0 · 24abfa41fa79d7422575ad9d5b0ab63f049eaa25
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1009 row · grep -n "^| R1009 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 34:| R1009 | 06:13 ET | HIS RULING · APPROVED: Sol may sit as a seat in the checks the brain and desk require (317, 298 now); every build and every deploy waiting on his word is approved. Words `cto-2026-10-11-words.md` R1009. | APPLIED: LAWS L67 + NOW at 06:31 |
RULING 2026-10-11 R1009 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1009 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · aebcf44974dfbfd3e7eb7815b8a583c4f86e9e1c
RULING 2026-10-11 R1009 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:

```
clock · date · 0 · Sun Oct 11 06:44:57 EDT 2026
status · git status --short --branch · 0 · ## ops/shadow-hub-1011
head · git log --oneline -1 · 0 · 680eca0e fix(ops-hand-install-1010): the test module docstring counts the H3 real-file tests as they stand (check O1)
diff · git diff --stat 680eca0e · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/shadow-hub-1011 · 0 · 680eca0e fix(ops-hand-install-1010): the test module docstring counts the H3 real-file tests as they stand (check O1)
env here · ls /Users/cobalt/cobalt-wt/shadow-hub-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

- `git show --stat 680eca0e` → `fix(ops-hand-install-1010): the test module docstring counts the H3 real-file tests as they stand (check O1)`, `tests/ops/test_desk_launch_ops_hand.py | 5 +++--`, `1 file changed, 3 insertions(+), 2 deletions(-)`.
- `wc -l` at BASE: `desk-launch.sh` 1327 · `bare-guard.py` 1251 · `authorize.sh` 214 · `preflight.sh` 260 · `desk-watch.sh` 89 · `stop-guard.py` 415 · `idle-wake.py` 54 · `test_bare_guard.py` 2091 · `test_authorize.py` 241 · `test_preflight.py` 419 · `test_desk_watch.py` 541 · `test_stop_guard.py` 788 · `test_desk_launch_ops_hand.py` 353.
- The card's symbols at BASE, from grep. Each matches the card's line:
  - `desk-launch.sh`: `committed()` 186 · `check_paths()` 193 · `run_launch()` 222 · usage 311 · the guard `if [ "$kind" != "desk" ]` 321 · `:778` `kind '$kind' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops`.
  - Read whole, also matching the card: `:457-459` (the prompt kind's mode), `:711-719` (ops-hand's live check), `:758`, `:762-767`, `:790-799`, `:998-1014`, `:1263-1272`, `:1292-1294`, `:1319-1326`.
  - `bare-guard.py`: `HUBS` 85 · `WORKERS` 91 · `GIT_SHAPED` 92 · `LAUNCHERS` 96 · `STOP_HEADS` 128 · `HOUSE` 142 · `worktree_of` 685 · `seat` 748 · `if kind in WORKERS and launches` 1058 · `g6` 1084, with `lines[-1].startswith(STOP_HEADS)` at 1088 · `g5` 1113.
  - `stop-guard.py`: `STOP = (` 71 · `key = "CHECK REPORT: "` 155 · `report_last_line` 163.
  - `idle-wake.py:8`, `:42` `guard.report_last_line(...)`, with no STOP filter. So idle-wake reads both shadow heads as they stand (S4 "confirms").
  - `restarts.py`: `OPS_DESK_PREFIX` 38 · DOCS 225-228 · operator script 232 · `tests/` 245. The card says 246; the `if` is at 245.
  - `authorize.sh:42-47`, `preflight.sh:45-49` and `desk-watch.sh:37-47` were read whole.
- `tail -n 3` of the spike preflight report → `PREFLIGHT DONE · prompt: sdk-spike-live · checks: 7 · fails: 0 · ready: YES`.
- Prompt 330 is not in this worktree: it was committed on main after BASE. Its line was read from `/Users/cobalt/cobalt/...330-sdk-spike-live.md:1`. `test_spike_hub_file.py` carries it as a constant. `grep -c -F` of its whole tail, from `--model` to the closing backtick, in 330 → `1`.
- Card records copied: the ids are proven (sol `models_cache.json:224`, terra `:319`, grok `CHECK-HUB.md:91`, opus and sonnet from the drafter's model list); Gemini is N/A. R1011, R1014, R1016 and R1019 are not APPROVED, so they are folded, not in RULINGS. R1012, R1018, R1020 and R1021 belong to the spike. RESTARTS: S6. `«SIGN` and `«INSTALL` are the desk's to fill. `CHECK-HUB.md:91-92` was re-read: grok-4.7, gemini-3.1-pro-high.
- `uv run cobalt jobs restarts 680eca0e..HEAD` (empty range; it lists the untracked report) → `docs/40 - DevDocs/reports/shadow-hub-build-2026-10-11.md A DOCS -` / `RESTARTS: none`.
- No lock probe (DB: none).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 669.41s (0:11:09)`. The last skip reads `COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`, which is expected offline.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped`. The skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC ... not set`; no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Red commit `f107f926` `wip(shadow-hub-1011): red — S1-S5, S7, P1-P3 tests and the P4 RUN test` (9 test files).
- S1, S5, S7 file tests and P1: `74 failed, 1 passed` across the four new files. Each `test_shadow_hub_file.py` and `test_spike_hub_file.py` test fails with `FileNotFoundError: ... prompts/SHADOW-HUB.md` (or `SPIKE-HUB.md`): the file is absent, which is the rows' named reason.
- S2: each `test_desk_launch_shadow.py` refusal case fails its own reason assert against BASE's first refusal. Examples: `assert "REFUSED: shadow: permission mode 'auto' is not dontAsk" in "REFUSED: two resume steps: '--model' and 'grok-4.7'\n"`. The no-`--model` case meets `:778`'s "none of", and the dry run fails by exit code.
- P2: each `test_desk_launch_spike.py` case fails against `:778`'s reason. The negative control `test_the_prompt_kind_still_refuses_a_dont_ask_line` PASSED (the 1 passed).
- S3, S7, S4 (G6), P3 guard: `10 failed, 15 passed`.
  - The pass cases fail `assert 2 == 0` with `route: the desk launches` (kind `worker`, G7).
  - G5 `src/x.py` fails `assert 0 == 2`.
  - S7 (a) and (b) fail with `- route: no builder pass while .env ... + route: the desk launches`; (c) exits 2.
  - S4 G6 fails `assert 0 == 2`.
  - P3 fails `assert 'worker' == 'spike'`.
  - The deny shapes and the fences are green on BASE, as the card says.
- S4 scripts: `9 failed, 1 passed`.
  - `REFUSED: kind 'shadow' is none of build, check, deploy`.
  - `REFUSED: kind 'shadow' is neither build nor check`.
  - `REFUSED: unknown kind: shadow` (desk-watch).
  - stop-guard: `assert (2, 'NOT A RE...then stop.\n') == (0, '')` for both heads.
  - The stop-guard pin (`test_s4_a_shadow_gate_seat_reads_the_cards_report`) PASSED on BASE.
- Negative control: `tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_launch_ops_hand.py` → `89 passed` at E2.
- P4 RUN (`-rP`), quoted whole:
  ```
  P4 BRAIN-HUB from the repo: kind = None
  P4 a drafter's dated prompt from the repo: kind = 'brain'
  P4 SPIKE-HUB from sdk-spike-1010: kind = 'worker'
  ```
  After P3 the third prints `kind = 'spike'` (the same test, run at E3). The DECISION is below.

## E3 THE ROWS
Commit `bc25c523` `feat(shadow-hub-1011): SHADOW-HUB.md and SPIKE-HUB.md; launcher kinds shadow and spike; the guard's shadow and spike seats; the step scripts name kind shadow (S1-S5, S7, P1-P3; L29, L76, R411)`.
- S1, S5, S7: `prompts/SHADOW-HUB.md`.
  - The line is BUILD-HUB's with SHADOW-HUB read in its place, the gate seat named, and `<builder allow>` added.
  - `## BUILDERS` holds 3 rows, each SIGN cell unsigned. The Terra row reads `network: off (workspace-write default; X1 proves it)`.
  - The rules of the seat cover the `.env` precondition, no overlap, re-pass cap 2, INCOMPLETE and the frozen scored build. The procedure puts `ENV CHECK …ls -la …/.env → No such file` immediately before `pass T`, `pass S` and `pass S2`.
  - Role trials; `## RESULTS TABLE`.
  - Result: `37 passed`.
- P1: `prompts/SPIKE-HUB.md`. Seat, prompt, the pin rule (14 days, `https://pypi.org/pypi/<name>/json`, `<name>==<that version>`), the report, 330's line with the message replaced, and the line's `NEEDS HIS SIGN-OFF «SIGN: his row»`. Result: `8 passed`.
- S2 and P2: `ops/desk/desk-launch.sh`.
  - Kind `shadow`: its args are read after the size guard (`:330`), then dropped to `shadow <card>`. The card then meets build's own gates (`build|shadow)` arm, `:1107`). The arm adds `SHADOW OF:`, `shadow/`, the ONE `## BUILDERS` row (it refuses `«SIGN`, `:1139`) and the JOB slug. It fills `<model>` and `<builder allow>` (`:1415-1416`), checks `dontAsk` once after the fill (`:1438`), and adds the worktree at BASE as build does (`:1446`).
  - Kind `spike` (`:361`) carries every refusal of the row and makes the plain dir in a real launch only.
  - The usage line names both kinds. Every other kind is unchanged: devfix and ops-hand give `89 passed`.
  - Result: `30 passed` across the two new files.
- S3, S7, P3 and S4's G6: `ops/desk/bare-guard.py`.
  - `HUBS` + `SHADOW-HUB.md`/`SPIKE-HUB.md` (95-96). `WORKERS` + both (98). `GIT_SHAPED` + shadow (99). `STOP_HEADS` + both heads (144).
  - `seat()` also returns `hub` and `model`.
  - G7 exception, kind shadow only (1079): `builder_call` (1125) reads `MODEL`'s one row from the hub's `## BUILDERS` (`builder_command`, 1097). The whole command must equal that command with `<worktree>` set to the card's WORKTREE and ONE `"…"` prompt that holds no `"`, `\`, `$` or backtick. `write_targets` (1116) must equal `{<WT>/<worktree>/**}`. Claude needs `dontAsk` and `"Bash"` denied; Grok must not carry `--always-approve`. A `.env` judged by `os.path.lexists` (1151) gives the S7 route.
  - G5: shadow writes only `<WT>/SHADOW-INSTRUCTIONS.md` and its REPORT; spike writes only under `<WT>/sdk-spike-1010/` (1218).
  - Result: `1822 passed`.
- S4: `authorize.sh` (kind shadow → `SHADOW-HUB.md`), `preflight.sh` (shadow runs build's rows), `desk-watch.sh` (shadow: REPORT, `^(SHADOW BUILT|SHADOW ROLE|FAILED)`, session `<job>-gate`) and `stop-guard.py` (`STOP` + both heads). Result: `182 passed` across the four test files.
- All row files plus the two launcher controls → `2168 passed`.
- DevDocs: there is no page under `docs/40 - DevDocs/cobalt/` for these ops scripts, so none was made (the ops-hand build's precedent, `ops-hand-build-2026-10-10.md:223`).
- THE MUTATIONS. Each was made with Edit, its row's tests run, then undone. After all of them `git diff --stat` showed the tree back at the fix.
  - S1, `<builder allow>` dropped from the line: `2 failed` (`test_s1_the_allow_list_is_build_hubs_26_plus_the_builder_token`: `Right contains one more item: '<builder allow>'`; `test_s1_the_rest_of_the_line…`).
  - S5, the harness line cut: `test_s5_the_harness_difference_prints_once` `assert 0 == 1`.
  - S7 (hub), the env check before pass S removed: `test_s7_every_pass_is_preceded_by_the_env_check` `AssertionError: pass S — …`.
  - P1, deny `Bash(git *)` → `Bash(git push*)`: `3 failed` (lists, line, `no_git`).
  - S2, the `«SIGN` refusal disabled: `2 failed` (`test_an_unsigned_model_is_refused_beside_a_signed_one`, which printed the Sonnet line with exit 0; `test_the_real_file_launches_a_signed_grok`).
  - P2, the live-session refusal disabled: `test_a_live_spike_session_is_refused` `assert 0 == 1`.
  - S3, the G7 exception made a no-op: `4 failed` (the three `runs_its_models_builder_command` cases and `test_s7_no_env_lets_the_pass_through`, `route: the desk launches`).
  - S3 negative control, the exception widened to every worker kind: it first STAYED GREEN. A build seat has no `MODEL:` and its hub has no table, so the test did not isolate the kind. I rewrote it: a BUILD-HUB seat with `MODEL: grok-4.7` whose hub carries the same table. It is now red under the mutation (`assert 0 == 2`) and green at the fix.
  - S7 (guard), `lexists` → `exists`: `test_s7_a_dangling_env_symlink_counts_as_present` `assert 0 == 2`.
  - P3, `SPIKE-HUB.md` out of `HUBS`: `test_p3_the_spike_launch_is_its_own_kind` `assert 'worker' == 'spike'`.
  - S4 (G6), the shadow heads out of `STOP_HEADS`: both G6 cases `assert 0 == 2`.
  - S4 scripts, all four undone at once: `6 failed`. stop-guard gives `(2, 'NOT A RE…')` ×2; desk-watch `GONE: x-job-shadow` ×2; authorize `assert 'SHADOW-HUB.md' in …`; preflight `FAILED PREFLIGHT: head`.
  - My first S3 mutation (`hit is True and False`) sent `True` into the `elif hit:` branch. The guard then wrote a non-string route, raised, and failed open (exit 0), so the tests stayed green for the wrong reason. I found this with a temporary probe test. That branch now reads `elif isinstance(hit, str)` (1083), and the mutation was redone as above.

## RESTARTS
`uv run cobalt jobs restarts 680eca0e..HEAD`, quoted whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	A	DOCS	-
docs/40 - DevDocs/prompts/SPIKE-HUB.md	A	DOCS	-
docs/40 - DevDocs/reports/shadow-hub-build-2026-10-11.md	A	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	A	test/documentation; no resident	-
tests/ops/test_desk_launch_spike.py	A	test/documentation; no resident	-
tests/ops/test_desk_watch.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	A	test/documentation; no resident	-
tests/ops/test_spike_hub_file.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
tests/ops/test_zz_debug_tmp.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. This is S6's RUN, as expected. The report and `test_zz_debug_tmp.py` rows are untracked working-tree files.

## W THE THREE SUITES
`<tip>` = `bc25c523`.
- (a0) `git diff --name-only --no-renames 680eca0e` → 17 paths, each under `docs/`, `ops/` or `tests/ops/` (listed in RESTARTS, minus the two untracked files). **`cobalt_dev: not taken (DB: none — 17 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh shadow-hub-1011 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/shadow-hub-1011-offline-20261011-072547.log`. This build adds no `tests/cobalt` or `tests/taxonomy` test; its new tests are under `tests/ops` (below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh shadow-hub-1011 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/shadow-hub-1011-livenote-20261011-073644.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3019 passed, 1 xfailed, 15 warnings in 538.09s (0:08:58)`.
- A red at W first seen at E3, in my own test: the first full `tests/ops` run gave `1 failed, 3018 passed` (`test_s4_kind_shadow_does_not_stop_on_a_plain_built_line`: `GONE: x-job-gate`, because the default list stub has no `x-job-gate` row). The fix was in the test: it now answers `x-job-gate busy working`. That was before the code commit, so no second fix commit was needed.
- `.env`: `ls /Users/cobalt/cobalt-wt/shadow-hub-1011/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
1. Every added test was shown red for its named reason: at E2 (quoted above) and under its row's mutation at E3. One test stayed green under its mutation, the S3 negative control; it was rewritten and is now red. The S4 stop-guard pin and the deny or fence cases are green on BASE by the card's own statement. Their mutations (S4 STOP, the S3 exception) are quoted.
2. Entry paths pinned:
   - Launcher: no `--model`, two, Gemini, not in the table, unsigned beside signed, slug, branch, `SHADOW OF:`, `«INSTALL`, uncommitted, auto, two modes, bypass. Spike: 0 and 2 args, undated, uncommitted prompt or hub, sign, auto, two modes, bypass, git scratch, live session. Real launches for both kinds.
   - Guard: three models pass. Ten deny shapes cover X1's `..`-free wider glob, another worktree, a second `--allow`, `$'…'`, the other model, no Bash deny, danger-full-access, another `-C` and `claude --bg`. Also `.env` as a file and as a dangling link, G5, G4, G2, G6 for both heads, the negative control, and the spike kind, fence and G7.
   - The only callers of the changed scripts are the hubs and the desk (operator scripts; RESTARTS "no Cobalt reader").
3. Re-read at the tip: `grep -n -E` over `bare-guard.py` (90, 95-99, 144, 1079, 1083, 1097, 1116, 1125, 1151, 1218), over `desk-launch.sh` (330, 361, 405, 428, 886, 1107, 1139, 1415-1416, 1438, 1446), and `git log --oneline 680eca0e..HEAD`. The line numbers in E3 are the tip's.

## FOR THE CHECK
- Range `680eca0e..bc25c523`: `f107f926 wip(shadow-hub-1011): red — …` · `bc25c523 feat(shadow-hub-1011): …`. The report commit follows.
- Per row, the reds, mutations and greens are in E2 and E3. The P4 RUN output is in E2, quoted whole.
- Suites: offline 4199/0 (gate.sh offline); live-note 146/0 (gate.sh livenote); with-DB: not run (DB: none); `tests/ops` 3019 passed, 1 xfailed.
- `<F0>` / `<F1>` / `<F2>` and lock times: not run (DB: none).
- RESTARTS table: above. The PREFLIGHT records were copied there.
- CHECK ASKS context, as built (claims for the check to run, not findings):
  - X1: the guard pins the whole command to the row's literal prefix, one plain quoted prompt and the row's suffix, then re-derives the write target. A symlinked worktree directory is not judged; the guard reads text only.
  - X3 / D-codex: whether `workspace-write` runs a shell is not settled here (the hub says so).
  - X4: the guard's `lexists` check plus the hub's env-check lines.
  - X6: P1's line equals 330's tail byte for byte (grep -c = 1).

## FIX ROUND F1 F2 (check A9, O2 B5; card 324 rows F1, F2)
The desk's `CONTINUE: FIX ROUND rows F1 F2` arrived in a NEW session (RECOVERY), 09:49. `git status --short --branch` → `## ops/shadow-hub-1011`; `git log --oneline -3` → `cd302109` (the check's fix), `5b214968`, `397cd63b`; `ls -la <WT>/.env` → `No such file or directory`.
- Red commit `126a3781` `wip(shadow-hub-1011): fix-round red — F1 F2 (check A9, O2 B5)`. Its tests:
  - `tests/ops/test_shadow_hub_file.py`: `test_f1_the_sonnet_prompt_comes_right_after_the_model` and `test_f2_the_sonnet_read_is_its_worktree_only[<worktree>|x-job-sonnet]`. They use the file's own `builders` and `command` helpers, `shlex`-split, with the prompt filled by one plain word.
  - `tests/ops/test_bare_guard.py`: `SHADOW_ROWS["claude-sonnet-5-5"]` takes the prompt right after `--model`'s value and `"Read(//Users/cobalt/cobalt-wt/<worktree>/**)"`. New: `test_f1_a_sonnet_call_with_the_prompt_last_is_g7` and `test_f2_a_sonnet_call_with_a_bare_read_is_g7`.
- RED on `cd302109` (hub and guard unchanged) → `5 failed, 4 passed`:
  - F1 hub: `assert ['WebFetch', 'mcp__*'] == ['--model', '...e-sonnet-5-5']` (the prompt is the last token).
  - F2 hub, both cases: `assert ['Read'] == ['Read(//User...orktree>/**)']`.
  - `test_s3_the_gate_seat_runs_its_models_builder_command[claude-sonnet-5-5]`: `assert 2 == 0`, `route: the desk launches` (G7: `write_targets(prefix)` is empty).
  - `test_f2_a_sonnet_call_with_a_bare_read_is_g7`: its bare-Read deny held, and its scoped-call pass failed with the same G7. Its red is F1's reorder, not F2's: the card names it a pin that is green once the guard reads `prefix + suffix`, and it is.
  - Passed: `test_f1_a_sonnet_call_with_the_prompt_last_is_g7` (a pin), `test_s1_the_claude_builder_runs_no_command` (the negative control), and the Grok and Terra cases of `test_s3_…`.
- The fix, commit `90b8faad`:
  - `SHADOW-HUB.md:20`, the Sonnet `builder command` cell: `"<pass prompt>"` now follows `claude-sonnet-5-5`, and `"Read"` is `"Read(//Users/cobalt/cobalt-wt/<worktree>/**)"`. Nothing else changed. The `builder allow` and SIGN cells are unchanged.
  - `ops/desk/bare-guard.py` `builder_call`: `write_targets(prefix + suffix)` (`:1169`), and the `dontAsk` and `"Bash"` tests on `prefix + suffix` (`:1172-1173`). The head verb stays `verb(words(prefix))` (`:1171`).
- Green: `test_shadow_hub_file.py`, `test_bare_guard.py` and `test_desk_launch_shadow.py` → `1888 passed, 15 warnings in 59.81s`.
- MUTATIONS. Each was made with Edit, its tests run, then undone:
  - M1, `write_targets(prefix)`: `2 failed` (`test_s3_…[claude-sonnet-5-5]`, `test_f2_a_sonnet_call_with_a_bare_read_is_g7`, each `route: the desk launches` / `assert 2 == 0`).
  - M1b, the `dontAsk` and `"Bash"` tests back on `prefix`: the same `2 failed`.
  - M2, the hub's prompt back last: `test_f1_the_sonnet_prompt_comes_right_after_the_model` `assert ['WebFetch', 'mcp__*'] == ['--model', ...]`, `1 failed, 42 passed`.
  - M3, the hub's bare `"Read"`: both `test_f2_the_sonnet_read_is_its_worktree_only` cases `assert ['Read'] == [...]`, `2 failed, 41 passed`.
  - After all of them, `git diff --stat` showed only the fix's 2 files plus this report. The `f1_`, `f2_`, `test_s1_`, `test_s3_` and `test_s7_` tests → `48 passed`.
- F2 proofs: `grep -n -F -e "SHADOW-INSTRUCTIONS.md"` on the hub and the guard → hub `:29` (the pass prompt: "Read SHADOW-INSTRUCTIONS.md in this folder"), `:33`, `:46` (`/Users/cobalt/cobalt-wt/<worktree>/SHADOW-INSTRUCTIONS.md`; "The builder's sandbox reads only its workspace, so everything it needs is copied in"), `:57` and `:70`; guard `:18` and `:104` `SHADOW_FILE = "SHADOW-INSTRUCTIONS.md"`. The file sits inside the `Read(//…<worktree>/**)` glob.
- The FIXED lines' tests: `grep -n -F "def test_f1_the_sonnet_prompt_comes_right_after_the_model"` → `265:`; `grep -n -F "def test_f2_the_sonnet_read_is_its_worktree_only"` → `276:`.
- DevDocs: there is no `docs/40 - DevDocs/cobalt/` page for these ops scripts (as at E3).
- RESTARTS, `uv run cobalt jobs restarts 680eca0e..HEAD`: 18 rows, every one `DOCS`, `operator script; no Cobalt reader` or `test/documentation; no resident`, restart `-`. The last line is `RESTARTS: none`.
- W on `<tip>` = `90b8faad` (DB: none: (a0), (a), (e), `tests/ops`):
  - (a0) `git diff --name-only --no-renames 680eca0e` → 18 paths, each under `docs/`, `ops/` or `tests/ops/` → **`cobalt_dev: not taken (DB: none — 18 paths)`**.
  - (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh shadow-hub-1011 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/shadow-hub-1011-offline-20261011-095255.log`.
  - (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh shadow-hub-1011 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/shadow-hub-1011-livenote-20261011-095255.log`. `grep -n -F "COBALT_LIVE_VAULT_ROOT"` on the log finds only the command line (`:2`), so no skip names it.
  - `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3033 passed, 1 xfailed, 15 warnings in 531.65s (0:08:51)`. That is the check's 3028 plus this round's 5.
  - `--deploy` was not typed: BUILD-HUB W (a0) for a DB: none card.
  - `ls <WT>/.env` → `No such file or directory` (10:03).
- Self-check for the round:
  1. Each new test was red at `126a3781` or under its mutation (quoted above).
  2. `builder_call(` has two callers (`grep -n -F`: `:1086` the `sh -c` body, `:1089` the whole command).
     - `:1089` is pinned by `test_s3_…[claude-sonnet-5-5]`, by the F1 and F2 guard tests, and by the Grok and Terra cases.
     - `:1086` is pinned by the check's `test_x1_a_wider_write_glob_inside_sh_c_stays_g7` and `test_x4_sh_c_of_the_builder_command_while_env_is_present_is_denied`, both Grok and green in `tests/ops`. A Sonnet body under `sh -c` gets G7 either way (`:1087`).
  3. The line numbers above were re-read at the tip: `grep -n -F "prefix + suffix"` → `1169`, `1172`, `1173`; the hub row `grep -n -F "Read(//…<worktree>/**)"` → `20:`; the two `def` greps → `265:`, `276:`.

## CONTINUE
next: done (fix round F1 F2 closed; the report commit follows).

## DECISIONS
- ASK DESK 1: `tests/ops/test_zz_debug_tmp.py` is an untracked, now-empty probe file I wrote at E3. `rm` of it was refused (only the `.env` `rm` string is listed). It collects no test. Default: left in place; the desk removes it. Until then `git status --short --branch` shows `?? tests/ops/test_zz_debug_tmp.py` after the report commit. [07:46] SETTLED: the file is gone. `git status --short --branch` at the fix round's start → `## ops/shadow-hub-1011` alone (09:49).
- ASK DESK 2: the Sonnet row writes `Edit(//…)` / `Write(//…)` where the card writes `Edit(<wt>/**)`. In Claude Code's rules `//` marks an absolute path and a single `/` is relative to the settings file, so `//` is BUILD-HUB's own spelling. The write target stays `/Users/cobalt/cobalt-wt/<worktree>/**`, and the tests and guard read it so. Default: `//`, as built. [07:46]
- ASK DESK 3: on the Sonnet command (the card's spelling, kept under L72), the prompt `"<pass prompt>"` comes last, after the list option `--disallowedTools`. If the CLI reads that list greedily, the prompt is taken as a tool name and no prompt reaches the model. This is not run here (L70). Default: as written. The first Sonnet probe or X1/X3 settles it; a fix is one hub-row edit, which then needs his sign. [07:46] SETTLED by card row F1 at `90b8faad`: the prompt now follows `--model`'s value. The SIGN cell is still unsigned, as before.
- DECISION P4 (RUN, not fixed here):
  - A BRAIN-HUB launch from the repo gets kind `None`. The guard treats the real brain as UNKNOWN: only G1, G3 and G6, with no G2, G5 brain fence or G7.
  - A drafter's dated prompt from the repo gets `brain`.
  - The spike gets `spike` after P3 (`worker` on BASE).
  - Default: a later card, on the desk's DECISION.
- ASK DESK 4: SHADOW-INSTRUCTIONS.md stays untracked until X9 picks an ignored path. While it exists, `preflight.sh`'s status row on a gate-seat RECOVERY would show it as a second line and fail. Default: as built; X9 (the desk's) settles it before the first shadow check, as FINAL plans. [07:46]
- FOR DEJAN — card D1 and D2, not asked by this build: the three builder allow strings and SPIKE-HUB's line are new command classes (R411). They need his one sign-off, and his rows replace each `«SIGN` and `«INSTALL`. Default: none signed; the launchers refuse until then.

## RECORDS
- `.env`: never taken (DB: none); proven absent at PREFLIGHT and W.
- REFUSED, not needed: `rm tests/ops/test_zz_debug_tmp.py` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (ASK DESK 1).
- I edited this report's `## CONTINUE` line once while E0's offline run was in flight. The report is no test input, but BUILD-HUB E0 says no file is written then.
- E3 test changes after the red commit:
  - `test_desk_watch.py::test_s4_kind_shadow_does_not_stop_on_a_plain_built_line` gained the `x-job-gate busy working` answer (fixture miss, W).
  - `test_bare_guard.py::test_s3_negative_control_…` was rewritten (a mutation left it green).
- `context 405465 of 400000 — REFRESH` (`desk-context.sh d8838e9f`, 07:45). This is above BUILD-HUB's 250,000 line, which is the desk's to judge (UNATTENDED RULES (c)).
- The L74 line: one attribution block naming `Claude-Session:`, not acted on.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

- The first stop line, kept for the file: `BUILT · job: shadow-hub-1011 · tip: bc25c523 | on 680eca0e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 11 of 11 | self-check: 3 of 3 | decisions: 6 · for Dejan: 1 · tokens: 405465`
- CONTINUED at FIX ROUND F1 F2 09:49, in a NEW session (job `5b9d297d`). The desk's message named the step and the card. The card's rows F1 and F2 are committed on main: `git -C /Users/cobalt/cobalt log --oneline -2 -- <card>` → `b02889d8 docs(desk): card 324 fix rows F1 F2, preflight prompt 352`, and `diff --stat` → nothing. No lock was taken, and `.env` was absent at the start and the end.
- The fix round ran the three suites once on `90b8faad` (one gate call each; no second gate).
- `context 195234 of 400000 — ok` (`desk-context.sh 5b9d297d`, 10:04).

FIXED: A9 — tests/ops/test_shadow_hub_file.py::test_f1_the_sonnet_prompt_comes_right_after_the_model
FIXED: O2 B5 — tests/ops/test_shadow_hub_file.py::test_f2_the_sonnet_read_is_its_worktree_only
BUILT · job: shadow-hub-1011 · tip: 90b8faad | on 680eca0e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 13 of 13 | self-check: 3 of 3 | decisions: 4 · for Dejan: 1 · tokens: 195234
