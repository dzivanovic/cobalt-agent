JOB: cos-outage-1018
LADDER: OFF-LADDER — reports/f20-fix-preflight-2026-10-18.md ISSUES 5a 2026-10-18 R1863
CLASS: K5
INSTALL: none
BRANCH: ops/cos-outage-1018
WORKTREE: cos-outage-1018
BASE: 0bdb7089
TIP: de3e15c8
REPORT: /Users/cobalt/cobalt-wt/cos-outage-1018/docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md
HOUSE B: as needed
BAND: LOW
DB: none
RESTARTS: none
RULINGS: 2026-10-18 R1863

## ROWS

Scope: the label `com.cobalt.cos` in two deploy scripts (brain L79, desk row R1922; card 730 D8; preflight `f20-fix-preflight-2026-10-18.md` ISSUES 5a). No other resident's handling changes. Every `file:line` below was read with `git show main:<file>` at the drafting (`## RECORDS`); re-find each place by content before the edit (BUILD-HUB E3). Tests run the scripts against the stubs of their test files only: no real `launchctl`, no `cobalt.sh`, no production command.

| row | what | red first | files |
|---|---|---|---|
| K1 | `deploy-outage.sh` restores `com.cobalt.cos` as it restores `com.cobalt.aset`, the resident whose plist it bootstraps from the repo (`plist_of`, `:107`: `$REPO/ops/com.cobalt.aset.plist`; the cos plist is `ops/com.cobalt.cos.plist`, card 730 C4a, and `DEPLOY-HUB.md:144` bootstraps `/Users/cobalt/cobalt/ops/com.cobalt.<label>.plist`). Every launchd step is already label-generic (the `*)` arms: rule E `:226-242`, bootout `:381-403`, `up_one` bootstrap / `Bootstrap failed: 5` retry / `kickstart -k` `:259-312`, the final re-read `:413-427`, the dry run `:117-150`), so THE EDIT is: (a) `:90` the accepted case `com.cobalt.aset\|com.cobalt.radar\|com.cobalt.agent)` gains `\|com.cobalt.cos`; (b) `:91` the refusal's list `(com.cobalt.aset, com.cobalt.radar, com.cobalt.agent)` gains `, com.cobalt.cos`; (c) `plist_of` (`:105-110`) gains ONE arm after the radar arm (`:108`): `com.cobalt.cos) printf '%s' "$REPO/ops/com.cobalt.cos.plist" ;;`; (d) the header comment: `:4` `(comma-separated: com.cobalt.aset, com.cobalt.radar, com.cobalt.agent)` gains `, com.cobalt.cos`; `:11` `aset and radar` reads `aset, radar and cos`; `:13` the plist list gains `$REPO/ops/com.cobalt.cos.plist` after the aset plist. Each of (a)-(d) holds `com.cobalt.cos` at most once and on ONE line (the DEPLOY PROOF count). No other line of the script changes | In `tests/ops/test_deploy_outage.py`, `COS = "com.cobalt.cos"` beside `AGENT` (`:28`) and a helper that writes `<repo>/ops/com.cobalt.cos.plist` and adds `COS: {"pid": 504, "path": <that plist>}` to the `Box` launchd state (`:139-146`); the existing tests and `Box` stay as they are. NEW `test_k1_cos_goes_down_and_up_like_aset`: set `f"{ASET},{RADAR},{AGENT},{COS}"`; asserts exit 0, last line `OUTAGE DONE 0s`, `("bootout", COS)` after `("bootout", RADAR)` and `("bootstrap", COS)` after `("bootstrap", RADAR)` in `acts(box)` (`:190-200`), the bootstrap's argv `["bootstrap", "gui/501", str(<repo>/ops/com.cobalt.cos.plist)]`, a stdout line `com.cobalt.cos · pid before 504 · pid after <n>` with n ≠ 504. RED on BASE: exit 1, `REFUSED: 'com.cobalt.cos' is not a resident this script restores`. NEW `test_k1_dry_run_names_the_cos_bootout_and_the_repo_plist`: `--dry-run` with `COS` alone; asserts `WOULD RUN: launchctl bootout gui/501/com.cobalt.cos` and `WOULD RUN: launchctl bootstrap gui/501 <repo>/ops/com.cobalt.cos.plist`, no stub called. RED on BASE: the same refusal. CONTROL (red on BASE, green after): `test_k1_cos_loaded_from_launchagents_is_refused_before_anything_goes_down`: cos's state `path` set to `<LaunchAgents>/com.cobalt.cos.plist`; asserts exit 1, stderr holds `is loaded from` and the repo plist path, no call but `print` (as `:286-293`). RED on BASE: the refusal names `is not a resident`, not `is loaded from`. CONTROL 2 (red on BASE, green after): `test_k1_cos_not_loaded_is_refused_before_anything_goes_down`: the plist present, no cos entry in the launchd state; asserts exit 1, stderr holds `com.cobalt.cos is not running before the outage (gone)`, no call but `print`. CONTROL 3 (green on BASE and after, the other labels byte-identical): `test_k1_the_three_residents_print_the_same_lines`: set `f"{ASET},{RADAR},{AGENT}"`, real run then `--dry-run`; asserts the real run's stdout lines and `acts(box)` and the dry run's whole stdout equal literals the test builds from `box` paths (the pids the stub hands out from `next` 900 in bootstrap order). The builder runs CONTROL 3 on BASE first and quotes it green; a literal that BASE does not print is corrected from BASE's output, never from the edited script's. Quote whole: `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_outage.py -k k1` → `4 failed, 1 passed` on BASE, `0 failed` after; then the whole file `0 failed` | `ops/desk/deploy-outage.sh`, `tests/ops/test_deploy_outage.py` |
| K2 | `deploy-step0.sh` lists `com.cobalt.cos` in its P8 census. The script takes no restart set: `RESIDENTS` (`:73`, `"com.cobalt.aset com.cobalt.radar com.cobalt.agent"`) drives only the census loop (`:875-886`), RECORDED, never a gate (`:885`, last argument `0`), and its dry run (`:877-879`). THE EDIT: (a) `:73` gains ` com.cobalt.cos` after `com.cobalt.agent`, so the cos row is printed after the agent's and before `disk`; (b) the header comment `:41` `for aset, radar, agent` reads `for aset, radar, agent, cos`. A cos not loaded (BOOTSTRAP deferred) prints `pid none · state none (recorded)` and fails nothing. No other line of the script changes | In `tests/ops/test_deploy_step0.py`, NEW `test_k2_census_lists_cos_after_the_agent`: the `desk` fixture run (`:213-216`); asserts exit 0, the rule column (`:218`) holds `P8 census com.cobalt.cos` directly after `P8 census com.cobalt.agent` and directly before `disk`, and the row is `P8 census com.cobalt.cos · launchctl print gui/501/com.cobalt.cos · 0 · pid 1 · state running (recorded)` (the stub's default pid, `:46`). RED on BASE: the rule is absent. NEW `test_k2_dry_run_names_the_cos_census`: `--dry-run` as `:369-383`; asserts `WOULD RUN: launchctl print gui/501/com.cobalt.cos` directly after the agent's print line. RED on BASE: absent. CONTROL (red on BASE, green after): `test_k2_a_cos_not_loaded_is_recorded_and_fails_nothing`: a `launchctl` stub, defined in the test, that answers `Could not find service "com.cobalt.cos" in domain for user gui: 501` with exit 113 for cos and as `LAUNCHCTL` (`:42-49`) for the rest; asserts last line `STEP-0 OK — window: (iii)` and the row `P8 census com.cobalt.cos · launchctl print gui/501/com.cobalt.cos · 113 · pid none · state none (recorded)`. RED on BASE: the row is absent. CONTROL 2 (green on BASE and after, the other labels byte-identical): `test_k2_the_three_residents_rows_are_unchanged`: the three rows `P8 census com.cobalt.aset · launchctl print gui/501/com.cobalt.aset · 0 · pid 4101 · state running (recorded)` (radar 4102, agent 4103) each equal, and the rule column with the cos row removed equals the full list of `:219-223` in its printed order (the builder takes that order from BASE's run and quotes it). Quote whole: `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_step0.py -k k2` → `3 failed, 1 passed` on BASE, `0 failed` after; then the whole file `0 failed` | `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_step0.py` |

## NOT IN THIS JOB
- Any line of `deploy-outage.sh` or `deploy-step0.sh` but those K1 and K2 name; the comments `deploy-outage.sh:15-30` (`aset / radar`) stand.
- `prompts/DEPLOY-HUB.md` (its STEP-R set `:93`, allow strings `:11`, P8 `:65`, `:122`, 4.2 `:139`, 4.6 `:143`), `ops/desk/desk-launch.sh`, `ops/desk/deploy-step-c.sh`, `ops/desk/orphan-clean.sh`, `src/cobalt/jobs/restarts.py`, `data/deploy/bootstrap-owed.json`: untouched.
- Loading, booting out or bootstrapping `com.cobalt.cos`, and any real `launchctl` (card 730 `BOOTSTRAP: deferred`).
- The handling of `com.cobalt.aset`, `com.cobalt.radar`, `com.cobalt.agent`.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `ops/desk/deploy-outage.sh` lines 1-45 (header), 85-115 (label case, `plist_of`, `key_of`), 117-150 (dry run), 226-242 (rule E), 259-312 (`up_one`), 381-427 (steps 1-3).
- `ops/desk/deploy-step0.sh` lines 36-50 (header P8), 73, 100-126 (`would`, `row`), 874-892 (census, dry-run end).
- `tests/ops/test_deploy_outage.py` lines 1-210 (stubs, `Box`, `acts`), 276-293, 374-392.
- `tests/ops/test_deploy_step0.py` lines 1-150 (stubs, `Desk`), 213-236, 369-383.
- `prompts/2026-10-18/730-f20-card.md` row C4a and `## DECISIONS` D8.

## CHECK ASKS
- X1 Are K1 (a)-(d) and K2 (a)-(b) the only changed lines of the two scripts (`git diff <BASE> -- ops/desk`), each holding `com.cobalt.cos` at most once?
- X2 Do the existing tests of both files pass unedited, and do the three other labels print byte for byte what BASE prints (CONTROL 3 of K1, CONTROL 2 of K2, run on BASE and after)?
- X3 Is `com.cobalt.cos` bootstrapped only from `$REPO/ops/com.cobalt.cos.plist`, in every path: rule E, `up_one`, the trap, the dry run?

## DEPLOY PROOF
- `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-outage.sh` · before `0` · after `5`
- `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `0` · after `1`
- deploy-outage tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_outage.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)
- deploy-step0 tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_step0.py` · green: `0 failed` (as above)

## RECORDS
- Drafter `draft-cos-outage` (prompt 783), 2026-10-18 16:27 EDT from `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `0bdb7089` (the BASE); `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk tests/ops` printed nothing.
- `git show main:ops/desk/deploy-outage.sh` read whole: `:4`, `:11`, `:13` header; `:90-91` the label case and refusal; `:105-110` `plist_of` (`:107` aset `$REPO/ops`, `:108` radar `$LAUNCHAGENTS`); every other launchd step label-generic.
- `git show main:ops/desk/deploy-step0.sh` read whole: `:41` header P8; `:73` `RESIDENTS`; `:875-886` the census, `row … 0` (never a gate).
- `git show fae30bbd:ops/com.cobalt.cos.plist`: Label `com.cobalt.cos`, the comment "BUILT, NOT LOADED … BOOTSTRAP deferred"; its path is `ops/` in the repo.
- DEPLOY PROOF counts after the edit: outage `5` = `:4`, `:13`, `:90`, `:91`, the new `plist_of` arm (`:11` names `cos`, not the label); step0 `1` = `:73` (`:41` names `cos`, not the label).
- BAND LOW: four files (`ops/desk/` two, `tests/ops/` two), six edited script lines and one new, no migration, no shared state (0-2).
- RESTARTS (K10): `ops/desk/` → operator script, no Cobalt reader; `tests/` → no resident (as card 721's record); the builder's `cobalt jobs restarts` line is the record.
- OPEN, the desk's (draft report `reports/draft-cos-outage-2026-10-18.md` DECISION 1): with `BOOTSTRAP: deferred`, cos is not loaded at the F20 deploy, so K1's rule E refuses it (CONTROL 2) if the hub passes it in `<restart set>`; and `DEPLOY-HUB.md:93` refuses a set holding it at STEP-R first.
