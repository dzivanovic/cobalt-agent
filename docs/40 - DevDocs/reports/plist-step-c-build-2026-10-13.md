# plist-step-c-1013 — build report (2026-10-13)

## §0 Headline
Card 496 (`prompts/2026-10-13/496-plist-step-c-card.md`), BASE `5214e50b`, code tip `01fb7297`. Of the ten rows, nine are built whole. D1 is built except `STANDING-LIST.md:157`, which waits for the desk's answer, as the row says (DECISIONS 1).
The first W stopped at (a0) because the card said `DB: none` while row OW1 changes `src/`. The desk removed the key (`2ff41ff1`), and the gate then ran green: offline 4327/0, with-DB 5230/0, live-note 146/0; `cobalt_dev` 0013 with F2 = F0; `.env` removed.
RESTARTS: `com.cobalt.radar`. `tests/ops` at the tip: 1 failed, the pre-existing rule-sweep red outside the rows (DECISIONS 6).

FIX ROUND (15:09, rows FR-D1 FR-O2 FR-A4 FR-O2b, card at `148e8892`): stopped at PREFLIGHT `head` (DECISIONS 9); no file changed yet.

## L74
- One system notice in this session asked for a `Claude-Session:` line in commits. Recorded here once, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- Fix-round session (15:09): the same notice arrived again. It was not followed.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md" · 0 · 80f65fc92a0c67a81a6dbf961c7aa25e8a246594
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-13 R1341 row · grep -n "^| R1341 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · 68:| R1341 | 07:25 ET | HIS RULING · APPROVED: "Confirmed: R1323, R1324, R1330, R1340." Words: `cto-2026-10-13-words.md` R1341. Confirms the relays R1323, R1324, R1330, R1340. | APPLIED: LAWS, checklist, areas/cobalt.md at 07:27 |
RULING 2026-10-13 R1341 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1341 |" -- "docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · b399c9516e518b4d5a2b60b47382c9840c4130e6
RULING 2026-10-13 R1341 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output
- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · whole:
```
clock · date · 0 · Tue Oct 13 09:29:06 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/plist-step-c-1013
    ?? "docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 5214e50b docs(desk): R1402 card 496 preflight r3, row R1400 quotes the brain
diff · git diff --stat 5214e50b · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/plist-step-c-1013 · 0 · 5214e50b docs(desk): R1402 card 496 preflight r3, row R1400 quotes the brain
env here · ls /Users/cobalt/cobalt-wt/plist-step-c-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- BASE · `git show --stat 5214e50b` · 0 · `docs(desk): R1402 card 496 preflight r3, row R1400 quotes the brain`; 2 files (`reports/cto-2026-10-13.md` 5 +++--, `reports/plist-step-c-preflight-r3-2026-10-13.md` 26 +), 29 insertions, 2 deletions.
- RESTARTS empty range · `uv run cobalt jobs restarts 5214e50b..HEAD` · 0 · one row, the untracked report: `docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md	A	DOCS	-`, last line `RESTARTS: none` (the tool reads the working tree; no committed path in the range).
- SYMBOLS (each `grep -n -F`, exit 0):
  - DEPLOY-HUB `:87` `## STEP-C — THE CONFIGS AND THE JOBS (read-only; rule C)`; `:88` the STEP-C rule (read whole); `:117` `## STEP-D1 — PRODUCTION BASELINE…`; `:141` `4.6 for each label taken down at 4.2: …`; `:152` `- (s) THE SET'S SMOKE READS: …`; `:157` `## STEP-5 — ROLLBACK, ONE PATH …`; `:78` `| NO HARMLESS VARIANT, …`; `## Deploy table` at `:50`, `:133`, `:141`, `:167`, `:174`. `:3` `NO launchctl on any label but com.cobalt.aset / com.cobalt.radar / com.cobalt.agent` (Read). `:11` the launch line, `:13` its fill sentence (Read).
  - CARD.md `:62` `` `## SMOKE READS` (deploy) — … ``; `:135` `## A DEPLOY CARD, IN SHORT (the values `DEPLOY-HUB.md` reads; no example is filled here)`; `:136` `Header: … Body: …`.
  - STANDING-LIST.md `:157` holds `NOT ON THIS LIST, by design: retiring or installing a launchd job (a `bootout` of any other label, an `rm` of a plist)`.
  - desk-launch.sh `:2096` `-e "s|<tip merges>|$merges|" \`; deploy case `:1641-1682` (Read; `$merges` built `:1654-1659`); the fill `:2085-2100` (Read).
  - `src/cobalt/smoke/checks.py:415` `def _launchctl(check: LaunchctlCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:`; the registry branch `:422-435`.
  - `src/cobalt/jobs/watchdog.py:316` `def sweep(`; the `not status.loaded` branch `:385-398` (`:397` `findings.append(Finding(spec.label, False, "not loaded", status.detail))`).
  - `tests/cobalt/test_jobs.py:885` `def test_an_unloaded_one_shot_is_red(self, store, registry, monkeypatch):` (class `TestEveryPlistMustBeLoaded` `:844`, marked `@requires_db` `:842`); `tests/cobalt/test_jobs.py:667` the offline `class Store:` stub of `test_real_sweep_calls_launchctl_and_reports_missed_after_grace`.
  - `tests/cobalt/test_smoke.py:434` `def test_kind_launchctl_running_and_registry_match():` (the K18 case `:450-465`).
  - `configs/cobalt/smoke/s2.yaml:633` `mode: registry_match` (K18 `:630-636`).
  - `.gitignore:6` `data/`.
  - `src/cobalt/jobs/restarts.py:198-206` (Read): `if path.startswith("ops/com.cobalt.") and path.endswith(".plist"):` … `rule += f"; new one-shot, bootstrap once: {label}"`.
  - 304 card `:20` row C2 `files` names `ops/com.cobalt.prefill-refresh.plist`; `:35` row CR3 `BOOTSTRAP: deferred com.cobalt.prefill-refresh`; `:73` WRITER GATE (Read).
  - `reports/deploy-f4-refresh-1010.md:100` DECISIONS item 1 (Read).
- CALLERS: `grep -rn -F "sweep(" src` → `src/cobalt/heartbeat/runner.py:150` `beat.jobs = sweep(now=ts, probe=probe)`, `src/cobalt/jobs/cli.py:129` `findings = sweep()` (other hits are `start_sweep` / `_sweep`, other functions). `grep -rn -F "_launchctl(" src` → the definition only (`checks.py:415`; dispatched by `evaluate`).
- `wc -l`: desk-launch.sh 2170 · DEPLOY-HUB.md 181 · CARD.md 147 · STANDING-LIST.md 253 · checks.py 745 · watchdog.py 502 · test_smoke.py 1574 · test_jobs.py 932 · s2.yaml 636.
- READ tails: `tail -n 3 reports/survey-blockers-2026-10-12.md` → last line `SURVEYED · rows: 33 · decisions: 3`; `tail -n 3 reports/deploy-f4-refresh-1010.md` → last line `FAILED: C — ops/com.cobalt.prefill-refresh.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used · decisions: 1 · for Dejan: 1 · tokens: 95780`.
- CARD RECORDS copied: see `## RECORDS` (copied whole); re-read: R1341 row (AUTHORIZATION above), `.gitignore:6`, `restarts.py:198-206`, 304 `:73`, K18 anchors `checks.py:427-434`, `watchdog.py:397`, `test_jobs.py:885` — all as the card states.
- DB: none card: no lock probe, no with-DB string proven here.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 655.79s (0:10:55)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.94s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

### A1 (RUN — asserts nothing)
- `git -C /Users/cobalt/cobalt diff --name-status c7f06789 fc6a1e2a -- configs ops` → exit 0:
```
M	configs/cobalt/jobs.yaml
M	configs/cobalt/prefill.yaml
M	configs/cobalt/smoke/s2.yaml
M	configs/cobalt/taxonomy/tunables.yaml
M	configs/cobalt/templates/daily.md.j2
A	ops/com.cobalt.prefill-refresh.plist
```
- `git -C /Users/cobalt/cobalt show fc6a1e2a:ops/com.cobalt.prefill-refresh.plist` → REFUSED by the line (`dontAsk`, no listed string). Read instead: `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh-1010 diff --stat fc6a1e2a -- ops/com.cobalt.prefill-refresh.plist` → nothing (the gate worktree's file equals the blob at `fc6a1e2a`), then the Read tool on that file, `:5-6`:
```
    <key>Label</key>
    <string>com.cobalt.prefill-refresh</string>
```
C1's fixture copies the `A	ops/com.cobalt.prefill-refresh.plist` status and that Label pair (`tests/ops/test_deploy_step_c.py` `plist()`).

## E2 RED
Tests written (no `src/` edit): `tests/ops/test_deploy_step_c.py` (new; (a)–(i), (n), (o)–(t) plus C1 positives for `change` and `RETIRE OWED`), `tests/ops/test_desk_launch_launchd.py` (new; (j)–(m) plus a deferred-gets-no-string case), `tests/cobalt/test_smoke.py` (OW1 K18 half of (u), (w)–(z)), `tests/cobalt/test_jobs.py` (`TestBootstrapOwed`, the sweep half of (v), (w)–(z)). All offline (DB: none).
- Run: `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_launchd.py tests/cobalt/test_smoke.py tests/cobalt/test_jobs.py` → `48 failed, 77 passed, 19 skipped` (first pass).
- Rewritten for the row's reason (said here): the OW1 tests first redded on `AttributeError` (no `watchdog.BOOTSTRAP_OWED_PATH` on BASE); `monkeypatch.setattr(..., raising=False)` now, so each reds on its verdict and the pins pass. (k) first redded on the hub token count; that assert moved to (j), (k) is now the pin the card names. (m) first redded on a count; it is the pin now. (j) reordered so its first red is the bootstrap string.
- Second run, `-k "ow1 or l1_"` → `19 failed, 9 passed`. PASSED (pins green on BASE): `test_l1_no_section_no_new_string`, `test_l1_a_deferred_label_gets_no_string`, `test_l1_no_generated_launchctl_string_holds_a_wildcard`, smoke and sweep `test_ow1_an_entry_removed_and_still_unloaded_is_red_in_both`, `test_ow1_no_state_file_is_today`, `test_ow1_a_loaded_listed_label_is_a_match`. Also PASSED on BASE: (f) `test_c2_pin_step_c_still_refuses_an_unnamed_plist`.
- Red first lines (`--tb=line`):
  - (u) `AssertionError: enabled but not loaded: ['com.cobalt.prefill-refresh']; loaded but enabled: false: none` (FAIL, `checks.py:431-434`).
  - (x) K18 `assert 'com.cobalt.prefill-refresh' not in 'enabled but... false: none'` (FAIL names both).
  - (v) `Finding(label='com.cobalt.prefill-refresh', ok=False, state='not loaded', detail='NOT LOADED in launchd', amber=False).ok` → False (`watchdog.py:397`); (x) sweep the same.
  - (j) `('Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist)', …) assert 0 == 1` (the bootstrap string absent).
  - (l) each refusal case: `assert 0 != 0` (the dry launch exits 0; the section is not read).
  - (a)–(d), (o)–(t): `sh: /Users/cobalt/cobalt-wt/plist-step-c-1013/ops/desk/deploy-step-c.sh: No such file or directory`, `assert 127 == 0` / `assert 127 == 1`.
  - (e) `assert 0 == 1` (count of `ops/desk/deploy-step-c.sh` in STEP-C); (g) `ValueError: not enough values to unpack (expected 1, got 0)` (no `4.6L ` line); (h), (i) absent (`ValueError` / `assert False`); (n) `assert False` (no `` `## LAUNCHD` (deploy) `` line).
- Commit `b4793b17` `wip(plist-step-c-1013): red`.

## E3 THE ROWS
Commit `01fb7297` `feat(plist-step-c-1013): STEP-C as one script admits card-named launchd one-shots; deferred bootstrap owed and read as OWED (C1 C2 B1 R1 L1 D1 DF1 BO1 OW1, L1 L3 L42)`, 10 files, 509 insertions, 20 deletions.

| row | built | where |
|---|---|---|
| A1 | RUN, quoted under `## E0 BASELINE` | — |
| C1 | `ops/desk/deploy-step-c.sh` (new): STEP-C mode. Reads `git -C $REPO diff --name-status <m0> <BRANCH> -- configs ops`; the ops/desk exception is today's rule word for word (`EXCEPTION:`); `ops/com.cobalt.<label>.plist` is admitted by the five tests; `D` prints `RETIRE OWED:`; any other status or plist, and a `## LAUNCHD` line the diff does not touch, are refused; ends `STEP-C: ADMITTED <n>` or the `:88` `FAILED: C — …` text. No git write, no `launchctl`, no merge | script |
| C2 | DEPLOY-HUB `:3` (`and the labels of <launchd set>`), `:5` (`## LAUNCHD`, `<launchd set>`), STEP-C (`:88`, the diff --stat, then ONE script call; the sentence stays) | hub |
| B1 | DEPLOY-HUB D1 (THE LAUNCHD SET bullet), new `4.6L` after `4.6`, the P8 table row (`first used at 4.6L`), smoke (s) dry run, `## Deploy table` `LAUNCHD done:` (STEP-7 2) | hub |
| R1 | DEPLOY-HUB STEP-5 `(1L)`, `(2L)`, the (5) tail `— launchd: <label> out|restored, …`, ROLLBACK STRING 1 | hub |
| L1 | DEPLOY-HUB `:11` token ` <launchd strings>` after the radar `kickstart -k` string, `:13` the fill sentence; `desk-launch.sh` `launchd_line()` (validation and strings), the deploy case reads `## LAUNCHD`, fill `-e "s| <launchd strings>|$launchd|"` | hub, launcher |
| D1 | `CARD.md`: the `` `## LAUNCHD` (deploy) `` paragraph after `## SMOKE READS`; `## A DEPLOY CARD, IN SHORT` lists it. `STANDING-LIST.md:157` NOT edited (DECISIONS 1) | card format |
| DF1 | the `deferred` mode: a `## LAUNCHD` line `… · deferred · … · dry run: none · gate: <items>`; STEP-C prints `ADMITTED: … · add · deferred` and `BOOTSTRAP OWED: com.cobalt.<label> — <items>`, then writes `data/deploy/bootstrap-owed.json` (only on exit 0); desk-launch builds no string for it | script, hub, launcher |
| BO1 | `--bootstrap-only` (refused unless the label is named `add`, the plist on `main` carries the Label, the file lists it, and each gate item has a `GATE RESULT:` line) and `--owed-clear` (removes the entry); hub `4.6L-BO` | script, hub |
| OW1 | `watchdog.bootstrap_owed()` is the one reader (`BOOTSTRAP_OWED_PATH`, `src/cobalt/jobs/watchdog.py`); the sweep's not-loaded branch gives `OWED (deferred bootstrap)`, ok; K18 `_launchctl` adds `owed` to the raw row and puts `OWED (deferred bootstrap): <labels>` in the PASS detail; `s2.yaml` K18 `expect_text` gains the exception | src, config |

DevDocs: `cobalt/jobs/watchdog.md` and `cobalt/smoke/checks.md`, one `## 2026-10-13 — plist-step-c-1013` entry each.

Greens after the rows: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_launchd.py tests/ops/test_hub_lines.py tests/ops/test_deploy_step0.py tests/cobalt/test_smoke.py tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py` → `277 passed, 19 skipped`. Before that: `tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_launchd.py tests/ops/test_hub_lines.py tests/ops/test_deploy_card.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_launch_recut.py` → `424 passed`. The whole of `tests/ops` (run while CARD.md was half edited) → `2 failed, 3583 passed, 1 xfailed`: (n), fixed by the CARD.md wording (`` `## LAUNCHD` (deploy) — ``), and `test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches` (DECISIONS 6).

Tests rewritten after a mutation left them green (said here): (b) and (q) now assert `REFUSED: ops/com.cobalt.prefill-refresh.plist — no ## LAUNCHD line names com.cobalt.prefill-refresh`, because the files-cell test also refused the unnamed plist. (r) now asserts `REFUSED: com.cobalt.prefill-refresh — the card's ## LAUNCHD names no line for this label`, because the mode test also refused it. The BO1 fixture puts its results under `## GATE RESULTS`: the first draft put them inside `## LAUNCHD`, where they were parsed as bad lines.

THE MUTATIONS. Each one made with Edit, the row's tests run, then undone with Edit:

| row | mutation | run | result (first failing lines) |
|---|---|---|---|
| C1 status | `A:add|A:deferred|M:change) ;;` → `*:*) ;;` | `-k c1_` | `2 failed`: `test_c1_a_changed_plist_named_change_is_admitted` (`assert (0 == 1)`), `[add_on_m]` (`ADMITTED: com.cobalt.prefill-refresh · change … assert 0 == 1`) |
| C1 Label | `if [ "$got" != "$want" ]` → `if false` | `-k c1_` | `1 failed`: `[label_differs]` |
| C1 files cell | the `case "$files"` arms swapped | `-k c1_` | `1 failed`: `[row_lacks_path]` |
| C1 resident | `agent|aset|radar)` → `agent-x)` | `-k c1_` | `1 failed`: `[aset]` |
| C1 untouched line | that `refuse_path` → `: refuse_path` | `-k c1_` | `1 failed`: `[untouched]` |
| C1 unnamed + ops/desk | no-line → `lmode=add`; the jobs.yaml test → `false` | `-k "c1_ or df1_"` | first `1 failed` (ops/desk only; (b), (q) green, so they were rewritten), then `3 failed`: `test_c1_an_unnamed_plist_is_refused`, `test_c1_the_ops_desk_exception_stands`, `test_df1_an_unnamed_plist_is_refused_before_and_after` |
| DF1 | `owed_write "$keep$owed_new"` → `: owed_write …` | `-k "df1_ or bo1_"` | `2 failed`: `test_df1_304_with_deferred_merges_and_loads_nothing`, `test_bo1_a_named_label_with_results_bootstraps_and_merges_nothing` |
| BO1 | the gate-result `refuse_path` and the card-names `refuse_path` → `: refuse_path` | `-k "bo1_ or df1_an"` | first `1 failed` (`…without_recorded_gate_results`: `ADMITTED: com.cobalt.prefill-refresh · bootstrap-only … assert 0 == 1`; (r) green, so it was rewritten), then `2 failed`: (r), (s) |
| C2, B1, R1, D1 | hub `deploy-step-c.sh` → `deploy-step-x.sh` in STEP-C; `4.6L THE` → `4.6X THE`; `(1L)` → `(1X)`; D1 bullet `already loaded` → `loaded`, `<launchd set>` → `set`; CARD.md `## LAUNCHD` → `## LAUNCHX` | `-k "c2_ or b1_ or r1_ or d1_ or df1_304_without"` | `6 failed, 1 passed` (the pin (f) is the one pass): (e), (g), (h), (i), (n), (p) |
| C2 pin (f), negative control | `…is not on this list` → `…is MUTATED` (replace all) | `-k c2_pin` | `1 failed`: `assert 'installing or changing a launchd job is not on this list' in …` |
| L1 | fill → `-e "s| <launchd strings>||"` | whole file | `1 failed`: (j) |
| L1 (k), negative control | fill → `-e "s|<launchd strings>|$launchd|"` (space kept) | `-k no_section` | `1 failed`: (k) `assert 'claude --bg ...' == 'claude --bg ...'` (`t.radar)"  "Bash(launchctl print …` with a double space) |
| L1 (l) | `return 0` at the top of `launchd_line` | whole file | `14 failed, 4 passed`: (j) and the 13 refusals in `launchd_line` (`[TWO]` is outside it, next row) |
| L1 TWO, (m), deferred | section count `-le 1` → `-le 9`; bootout string `$lab*`; deferred `return 0` removed | `-k "TWO or wildcard or deferred_label"` | `3 failed` |
| OW1 | sweep and K18 `if spec.label in owed` → `if False and …` | `-k ow1` | `4 failed`: (u), smoke (x), (v), sweep (x) |
| OW1 negative control (w), (y) | `if True or spec.label in owed` | `-k ow1` | `6 failed`: smoke and sweep (w), (x), (y) |
| OW1 (z) | K18 `if spec.enabled:` (drops `not loaded`); sweep `if not status.loaded or spec.label in bootstrap_owed():` | `-k loaded_listed` | `2 failed`: both (z) |

After the undo: a grep for every mutation spelling (`MUTATED|if false|: refuse_path|agent-x|*:*)|lmode=add|-le 9` in the two scripts) prints nothing; `git diff --stat` showed only the rows' files, and the commit followed.

## RESTARTS
`uv run cobalt jobs restarts 5214e50b..HEAD` → exit 0, whole:
```
path	change	rule	restart
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
docs/40 - DevDocs/cobalt/jobs/watchdog.md	M	DOCS	-
docs/40 - DevDocs/cobalt/smoke/checks.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md	A	DOCS	-
ops/desk/deploy-step-c.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
src/cobalt/jobs/watchdog.py	M	static import reach	com.cobalt.radar
src/cobalt/smoke/checks.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs.py	M	test/documentation; no resident	-
tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step_c.py	A	test/documentation; no resident	-
tests/ops/test_desk_launch_launchd.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. (The report row is the untracked working-tree file.)

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 5214e50b` → exit 0, whole:
```
configs/cobalt/smoke/s2.yaml
docs/40 - DevDocs/cobalt/jobs/watchdog.md
docs/40 - DevDocs/cobalt/smoke/checks.md
docs/40 - DevDocs/prompts/CARD.md
docs/40 - DevDocs/prompts/DEPLOY-HUB.md
ops/desk/deploy-step-c.sh
ops/desk/desk-launch.sh
src/cobalt/jobs/watchdog.py
src/cobalt/smoke/checks.py
tests/cobalt/test_jobs.py
tests/cobalt/test_smoke.py
tests/ops/test_deploy_step_c.py
tests/ops/test_desk_launch_launchd.py
```
Paths that start with none of `ops/`, `tests/ops/`, `docs/`: `configs/cobalt/smoke/s2.yaml`, `src/cobalt/jobs/watchdog.py`, `src/cobalt/smoke/checks.py`, `tests/cobalt/test_jobs.py`, `tests/cobalt/test_smoke.py`. All are row OW1's `files`. The hub's (a0) rule: `FAILED: W — the card says DB: none but the diff holds <path>; the desk removes the key from the card and sends CONTINUE: W`. No gate call was made. `cobalt_dev` was not taken, the lock was not taken, and no `.env` was copied. Stopped `FAILED: W` (wip `2b39ef9d`). Resumed at 10:17 on the desk's `CONTINUE: W` (`## RECORDS`).
- THE GATE, after `CONTINUE: W` (the card now carries no `DB:` key): `ls -la /Users/cobalt/cobalt-wt/plist-step-c-1013/.env` → No such file; `sh /Users/cobalt/cobalt/ops/desk/gate.sh plist-step-c-1013 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`; no `--migration`) → exit 0. Verdict lines, whole:
```
offline 4327/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5230/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/plist-step-c-1013-all-20261013-101742.log
```
  - (a) offline: log `:2` `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `:885` `4327 passed, 806 skipped, 1 xfailed`. That is 10 more than E0's 4317: this build's offline tests in `tests/cobalt` (five K18 in `test_smoke.py`, five `TestBootstrapOwed` in `test_jobs.py`).
  - (b) log `:891` `lock taken: plist-step-c-1013`; `:902` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; LEVEL 0013.
  - (c) PASS 1, log `:956` `pass 1: whole (deploy)`, executed (`:958`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` plus the standing `--deselect`s of `ops/desk/gate-lists.md` (none of this build) → `:1115` `5025 passed, 7 skipped, 99 deselected, 3 xfailed`. Every SKIPPED line is quoted above. Each is in the allowed set (DEPLOY-HUB STEP-G (c): `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, the `COBALT_TEST_LIVE_DRC` skip of `test_replay_line.py`, `test_s3_c4_experiments.py` x14, `test_catalyst.py:365`, `test_predicate.py:262`); the gate marked none `OUTSIDE the allowed set`.
  - (c2) `:1117` **`dev forward: APPLIED 10:41:48`**; `:1195` `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c`.
  - (c3) PASS 2 (`:1197`, the gate-lists PASS 2 command) → `:1969` `205 passed, 1 deselected`. `with-DB 5230/0` = 5025 + 205.
  - (c3r) stray rows: not read (no `--tickers`; this build writes no ticker).
  - (f) `:2037` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`**; `:2091` `lock released`; `.env: removed`; `ls /Users/cobalt/cobalt-wt/plist-step-c-1013/.env` → No such file.
  - (e) live-note (`:2105`, `.env` absent) → `:2160` `146 passed, 1 skipped` (the `COBALT_TEST_LIVE_DRC` skip; none names `COBALT_LIVE_VAULT_ROOT`).
- `<tip>`: the gate ran at HEAD `2b39ef9d` (the wip report commit). `git diff --stat 01fb7297 HEAD -- . ":(exclude)docs"` → nothing, so the tree the suites proved is code tip `01fb7297`.
- `tests/ops` at the tip (the gate's offline pass does not run it; most of this build's tests live there): `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops` → `1 failed, 3584 passed, 1 xfailed`. The one red is `tests/ops/test_the_rule_sweep.py:134` `AssertionError: ['f4-refresh-build-2026-10-10.md']`, the red outside the rows in DECISIONS 6 (inputs unchanged since BASE).

## PRE-STOP SELF-CHECK
1. "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." — E2 reds: (a)–(e), (g)–(j), (l), (n)–(t), (u), (v), (x) (quoted under `## E2 RED`). Mutation reds for every test, including the pins (f), (k), (m), (w), (y), (z) and `test_l1_a_deferred_label_gets_no_string` (the THE MUTATIONS table). Rewritten after staying green: (b), (q), (r) (said under E3). The C1 positives `test_c1_a_changed_plist_named_change_is_admitted` (red under the status mutation) and `test_c1_a_removed_plist_is_retire_owed` (red on BASE, script absent) are included.
2. "Every entry path of each rule pinned by a test." — `sweep` callers `heartbeat/runner.py:150` and `jobs/cli.py:129` (PREFLIGHT grep) both call `sweep()`, which reads `BOOTSTRAP_OWED_PATH` through `bootstrap_owed()`. `TestBootstrapOwed` drives `watchdog.sweep` itself, with listed, unlisted, absent-file and loaded states. `_launchctl` is reached only through `checks.evaluate` (`grep -rn -F "_launchctl(" src` → the definition only), and the K18 tests call `checks.evaluate`. `deploy-step-c.sh` has no caller but the hub; each of its three modes and every refusal branch has a test. The `desk-launch.sh deploy` case is pinned by dry launches with and without a section, a deferred line, and 14 refusals. The missing-file, empty-file and loaded-label edges are pinned; the not-JSON edge of `bootstrap_owed` has no test, so it goes under DECISIONS 8.
3. "Every `file:line`, count and quote in the report re-read from tool output at the tip." — re-run at the tip: `grep -n -F "def bootstrap_owed" src/cobalt/jobs/watchdog.py` → `:63`; `grep -n -E "^4\.6L|^- \(1L\)|^- \(2L\)|…"` on DEPLOY-HUB → `:89` (STEP-C), `:144` (4.6L), `:145` (4.6L-BO), `:163` (1L), `:165` (2L); `grep -n -E "^launchd_line\(\)|s\| <launchd strings>" ops/desk/desk-launch.sh` → `:1511`, `:2184`; the gate's counts with their log line numbers (`grep -n -E … <log>`); `git diff --stat 01fb7297 HEAD -- . ":(exclude)docs"` → nothing.

## FOR THE CHECK
- Range `5214e50b..01fb7297` (code tip). Commits: `b4793b17 wip(plist-step-c-1013): red`; `01fb7297 feat(plist-step-c-1013): STEP-C as one script admits card-named launchd one-shots; deferred bootstrap owed and read as OWED (C1 C2 B1 R1 L1 D1 DF1 BO1 OW1, L1 L3 L42)`; `2b39ef9d wip(plist-step-c-1013): W — card says DB: none, the diff holds src/configs/tests/cobalt paths of row OW1` (report only); then the report commit.
- Per row, reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS` (THE MUTATIONS table, the greens).
- Caller greps: `## PREFLIGHT` CALLERS.
- RUN row A1, whole: `## E0 BASELINE` A1.
- The three suites and their executed commands, F0 / F1 / F2, and the lock take and release (log `:891`, `:2091`; forward at 10:41:48): `## W THE THREE SUITES`. A second W was not needed: there was no red at W from this build.
- RESTARTS table: `## RESTARTS`, `RESTARTS: com.cobalt.radar`.
- Records copied at PREFLIGHT: `## PREFLIGHT`, `## RECORDS`.
- For house A (card CHECK ASKS): this build changes `DEPLOY-HUB.md` (`:3`, `:5`, `:11`, `:13`, the P8 table, STEP-C `:89`, D1, 4.6L / 4.6L-BO, smoke (s), STEP-5 (1L) / (2L) / (5), ROLLBACK STRING 1, STEP-7 2) and does NOT change `STANDING-LIST.md` (DECISIONS 1).
- X1: a `## LAUNCHD` line holding `*`, `$`, a backtick, a quote, `;`, `|`, `&`, `<`, `>`, `\`, `(` or `)` is refused by `launchd_line` before any field is read. Labels are `[a-z0-9-]` and dry-run words `[a-z0-9-]` (at most 4). Tests: the `*` and `; rm x` refusal cases.

## FIX ROUND — AUTHORIZATION AND PREFLIGHT (2026-10-13 15:09)
- `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → `AUTHORIZED` twice, with the card at `2962d9b9` (15:09) and at `148e8892` (after the desk's message that row FR-O2b was added; `git -C /Users/cobalt/cobalt log --oneline -4 -- <card>` → `148e8892 docs(card): 496 row FR-O2b, step-c dry-run shape (brain R1418 follow-up)`). The second run's rows: `CARD COMMITTED · … · 0 · 148e88928ed81969868b18c7460d287d47d25fec`, `CARD UNCHANGED · … · 0 · nothing`, R60 and R1341 rows as above (R1341 now at `:102`), last line `AUTHORIZED`.
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 1, whole:
```
clock · date · 0 · Tue Oct 13 15:09:29 EDT 2026
status · git status --short --branch · 0 · ## ops/plist-step-c-1013
head · git log --oneline -1 · 0 · 6c3402af fix(plist-step-c-1013): STEP-C reads renames as adds, matches the files cell whole, clears an owed entry an add or change loads; a refusal at 4.6L goes to STEP-5 (check O1 O3 A1 A5)
diff · git diff --stat 5214e50b · 0 · (15 lines)
     (14 files changed, 1603 insertions(+), 18 deletions(-))
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/plist-step-c-1013 · 0 · 6c3402af fix(plist-step-c-1013): …
env here · ls /Users/cobalt/cobalt-wt/plist-step-c-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
FAILED PREFLIGHT: head
```
- Why `head` fails (`ops/desk/preflight.sh:156-166`, read): for `build` the rule accepts only HEAD = BASE (`5214e50b`) or a subject starting `wip(plist-step-c-1013):`. HEAD is the check's commit `6c3402af` (`fix(…)`), which is the card's `TIP:`. The script has no fix-round case.

## CONTINUE
next: PREFLIGHT (fix round: rows FR-D1, FR-O2, FR-A4, FR-O2b at TIP `6c3402af`), on the desk's `CONTINUE`.

## DECISIONS
1. ASK DESK [10:15 ET] — FOR DEJAN. `STANDING-LIST.md:157` is not edited. Row D1 says it is "Edited only after the desk's answer to report `## DECISIONS` item 1". No answer is in this session, and the file is his one approval (R60: a command string that changes returns to him). Safe default taken: the line stays as is. CARD.md and the hub are built. When the answer comes, the edit is one line: installing or changing one card-named one-shot is on the line through the strings `desk-launch.sh` generates from `## LAUNCHD` (`DEPLOY-HUB.md` 4.6L, STEP-5 (1L)); retiring one stays off.
2. DECISION W (answered at 10:17: the desk removed the key, `2ff41ff1`, and sent `CONTINUE: W`; the gate is green): the card's `DB: none` and row OW1 disagree. OW1 names `src/cobalt/smoke/checks.py`, `src/cobalt/jobs/watchdog.py`, `configs/cobalt/smoke/s2.yaml`, `tests/cobalt/test_smoke.py` and `tests/cobalt/test_jobs.py`, so (a0) fails (W above). Safe default: stop, as BUILD-HUB W (a0) says; the desk removes the key and sends `CONTINUE: W`.
3. DECISION OW1-v: the card places (v) at "`test_jobs.py:885`'s fixture". That class is `@requires_db` (`:842`), and E2 on a DB: none card holds no with-DB red. The sweep tests (`TestBootstrapOwed`) therefore run offline, on the `Store` stub shape of `test_jobs.py:667` (an existing offline sweep test), with the same one-shot `_spec` and card 304's label. Their reds and mutations are shown above. Safe default: offline. The with-DB `TestEveryPlistMustBeLoaded` is unchanged.
4. DECISION DF1/BO1 shape (the card leaves these open):
   - (a) `deferred` is a mode of the `## LAUNCHD` line. Such a line ends ` · gate: <item>, <item>`, and that is where `<the card's gate items>` come from; it is admitted only on an `A`.
   - (b) STEP-C prints `ADMITTED: com.cobalt.<label> · add · deferred`, so the line still holds (o)'s `ADMITTED: com.cobalt.prefill-refresh · add`. The hub takes a `· deferred` label out of `<launchd set>`, and desk-launch builds no string for it.
   - (c) An ops/desk plist that passes prints `EXCEPTION: <path> — …`, not `ADMITTED:`, so it never enters `<launchd set>`.
   - (d) Gate results are column-0 `GATE RESULT: com.cobalt.<label> · <item> · <result>` lines under a card section `## GATE RESULTS`.
   - (e) The owed entry is removed by a third mode, `--owed-clear`, which the hub calls after 4.6L's print. C1 says the script runs no `launchctl`, so (t) plays the hub's bootstrap and print on the stub itself.
5. DECISION L1 fill: the card writes `-e "s|<launchd strings>|$launchd|"`. The build uses `-e "s| <launchd strings>|$launchd|"` (the token's leading space goes with it, and each generated string carries its own leading space). This way a card with no `## LAUNCHD` gives today's line byte for byte (X4; (k) and its negative control above).
6. UNPROVEN (L70), outside the rows, not fixed: `tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches` FAILS with `AssertionError: ['f4-refresh-build-2026-10-10.md']` (`:134`). Its inputs are unchanged since BASE: `git diff --stat 5214e50b -- tests/ops/test_the_rule_sweep.py ops/desk/deploy-card.sh "docs/40 - DevDocs/reports"` prints nothing, and this build's report is dated 2026-10-13, outside its window (`LAST = "2026-10-12"`). The gate's offline pass will show it again.
7. ASK DESK [10:15 ET]: a bootstrap-only deploy card has no launch path yet. `desk-launch.sh deploy` still requires `TIP`, `## SHIPS` and a check per ship; BO1's merge-free deploy needs a card shape the launcher accepts. This is outside the rows. Safe default: not built; the hub text (4.6L-BO) and the script mode exist.
8. Self-check gap (2): `bootstrap_owed()`'s not-JSON path (`BootstrapOwedError`, which K18 turns into ERROR and the sweep into the unchanged red, plus a note) has no test. Safe default: left as built and named here for the check's fix round.

9. ASK DESK [15:10 ET], fix round: `preflight.sh build` fails `head` because HEAD is the check's `fix(plist-step-c-1013):` commit `6c3402af` (the card's `TIP:`), not BASE or a `wip(plist-step-c-1013):` commit. BUILD-HUB PREFLIGHT makes that the last line. Safe default: stopped before any change; waiting for `CONTINUE: PREFLIGHT` with the fact that the fix round starts at TIP `6c3402af`.

## RECORDS
- Fix round 15:10: message from `cto-desk` saying card 496 gained row FR-O2b (`148e8892`). It adds a row, so per UNATTENDED RULES (b) the message itself is not followed. The row is taken from the card: re-read at `:36`, and authorize.sh re-run → `AUTHORIZED` on `148e8892`.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt show fc6a1e2a:ops/com.cobalt.prefill-refresh.plist` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (A1; the same bytes were read through the gate worktree, proved equal by `git -C … diff --stat fc6a1e2a -- …` printing nothing.)
- The card's RECORDS, re-read at PREFLIGHT: R1341 is `HIS RULING · APPROVED` (authorize.sh row); `.gitignore:6` is `data/`; `restarts.py:198-206` is as quoted; 304 `:73` is the WRITER GATE; the K18 anchors are `checks.py:427-434`; the sweep anchor is `watchdog.py:397`; `test_jobs.py:885` is `test_an_unloaded_one_shot_is_red`. The other card records (seams 458/485/480, the L68 note, the RESTARTS class homes) are copied as the card has them. The derived RESTARTS (`com.cobalt.radar`) matches the card's class-home read.
- `.env`: never present in this worktree (`ls /Users/cobalt/cobalt-wt/plist-step-c-1013/.env` → No such file, PREFLIGHT). No lock taken.
- CONTINUED at W 10:17 (message from `cto-desk`: `CONTINUE: W — the DB: none key is removed from card 496 on main (commit 2ff41ff1)`). Verified: `git -C /Users/cobalt/cobalt log --oneline -3 -- <card>` → `2ff41ff1 docs(desk): R1404 card 496 DB key removed after W failure`; `git -C /Users/cobalt/cobalt diff 80f65fc9 2ff41ff1 -- <card>` → the one line `-DB: none`, nothing else; `grep -n -F "DB:" <card>` → nothing; `git -C /Users/cobalt/cobalt diff --stat -- <card>` → nothing (committed, clean).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

First build's stop line (kept for the record): `job: plist-step-c-1013 · tip: 01fb7297 | on 5214e50b | … | rows: 9 of 10 | self-check: 2 of 3 | decisions: 8 · for Dejan: 1 · tokens: 382312` (whole at `dfc2624f`).

FAILED PREFLIGHT: head — fix round: HEAD 6c3402af is the check's fix commit (the card's TIP), not BASE 5214e50b nor a wip(plist-step-c-1013): commit — preflight.sh build has no fix-round case
