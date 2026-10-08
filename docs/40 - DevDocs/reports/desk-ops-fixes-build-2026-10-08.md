# desk-ops-fixes — build report 2026-10-08

## §0 Headline
G1–G5 are built at `d522f6f7` on `b8b4f69c`, DB: none:
- The desk guard now requires a background session (G1), and an unreadable session list blocks instead of failing open (G2).
- `install-ops` replaces a stale plain file with the link (G3). The close timer DMs every REFUSED line and a missing desk (G4). The wake-up gains the close-wait rule (G5, +452 bytes).
- Offline 3991/0, live-note 146/0, the four row files 110/0. `tests/ops` holds one red that was already red on BASE, outside the rows (DECISION W-1). RESTARTS: none.

## L74
A system reminder at session start asked that commits end with a `Claude-Session: https://claude.ai/code/session_01X38dFpKdmtDsfA3CNe52fx` line. Recorded here once as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md"` → exit 0, 07:50 EDT:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md" · 0 · b4800b1dbd1a599055c6c2b8e55a3393e18a8fa0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R657 row · grep -n "^| R657 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 10:| R657 | 07:13 ET | HIS RULING (words: `cto-2026-10-08-words.md` R657, "approved"): one ops card, rows G1-G4 from the brain's relay, no DB. LAUNCHING drafter `desk-ops-fixes-draft`, prompt `105`, card `106` to follow. | HIS RULING · APPROVED |
RULING 2026-10-08 R657 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R657 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · c6b4a04d639c181b21ff0af0b849c3bf938dcc4d
RULING 2026-10-08 R657 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
RULING 2026-10-08 R658 row · grep -n "^| R658 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 11:| R658 | 07:16 ET | HIS RULING (L79 relay, words: `cto-2026-10-08-words.md` R658): rows G5 (wake-up close-wait rule) and G6 (day-open fails when no desk is live) join card `106`; prompt `105` amended, drafter `914e0a53` told. | HIS RULING · APPROVED |
RULING 2026-10-08 R658 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R658 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 09bb065219f71aa0734be09eb83e8b6de9c6b2f3
RULING 2026-10-08 R658 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
RULING 2026-10-08 R660 row · grep -n "^| R660 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 13:| R660 | 07:41 ET | HIS RULING (words R660, desk reading: my recommendations): D1 = A, G4 stays on card `106` with one new command; D2 = B, G6 leaves for its own card (C7). LAUNCHING amend drafter (prompt `107`) and C7 drafter (prompt `108`). | HIS RULING · APPROVED |
RULING 2026-10-08 R660 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R660 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · c364bc43b0e86532cf59494d8d427e4f8f677454
RULING 2026-10-08 R660 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| base | `git show --stat b8b4f69c` | 0 | `b8b4f69c docs(desk): preflight 5094bee8 launched for card 106` · `docs/40 - DevDocs/reports/cto-2026-10-08.md \| 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)` |
| G1 callers | `grep -rn -F "first_user_text(" ops src` | 0 | `ops/desk/stop-guard.py:100:def first_user_text(transcript_path):` · `:123:    text = first_user_text(transcript_path)` · `:160:        text = first_user_text(transcript)` · `:327:        text = first_user_text(event.get("transcript_path") or "")` |
| G1 idle-wake | `grep -rn -F "report_last_line" ops` | 0 | `ops/desk/stop-guard.py:14`, `:135:def report_last_line(transcript_path, cwd):`, `:332`, `ops/desk/idle-wake.py:8`, `ops/desk/idle-wake.py:42:        last = guard.report_last_line(event.get("transcript_path") or "", cwd)` |
| G1 is_desk | `grep -rn -F "is_desk(" ops` | 0 | `ops/desk/stop-guard.py:151:def is_desk(event):` · `:312:    if is_desk(event):` |
| G2 Unguarded | `grep -n -F "Unguarded(" ops/desk/stop-guard.py` | 0 | `147:class Unguarded(Exception):` · 181 · 202 · 208 · 211 · 214 · `225:        raise Unguarded("desk-list.sh timed out")` · `227:        raise Unguarded("desk-list.sh exit %d" % out.returncode)` · `237: … pgrep timed out` · `239: … pgrep exit %d` · 277 · 279 |
| G3 install-ops | `grep -rn -F "install-ops" ops/desk/desk-launch.sh` | 0 | `:37`, `:74:#   install-ops: no launch. …`, `:80:#           \`install-ops: <n> linked, <m> kept\`, exit 0. …`, `:94`, `:303`, `:616:# ---- kind install-ops: …`, `:619:if [ "$kind" = "install-ops" ]; then`, `:620`, `:622`, `:632:            ln -s "$src" "$links/$name" \|\| refuse "install-ops: the link failed: $links/$name"`, `:637:    printf 'install-ops: %s linked, %s kept\n' "$linked" "$kept"`, `:661` |
| G4 refuse sites | `grep -n -F "refuse " ops/desk/close-timer.sh` | 0 | `64`, `68`, `72:[ -f "$LAUNCH" ] \|\| refuse "no launcher: $LAUNCH"`, `75:[ -f "$DESK_LIST" ] \|\| refuse "no session list: $DESK_LIST"`, `76:rows=$(sh "$DESK_LIST" 2>/dev/null) \|\| refuse "the session list is unreadable: $DESK_LIST"`, `101:mkdir -p "$logs" \|\| refuse "cannot make $logs"` |
| G4 README | `grep -n -F "send_dm" ops/README.md` | 1 | nothing. Read `ops/README.md:400`: `that lived here is void: there is no \`cobalt notify\` command and no heartbeat \`email\` probe` (the card's "no CLI" citation holds) |
| G4 plist | `grep -n -F "PATH" ops/desk/com.cobalt.close-timer.plist` | 0 | `13:        <!-- launchd's own PATH holds neither \`claude\` nor python3; desk-launch.sh runs both -->` · `14:        <key>PATH</key>` |
| G4 sender | Read `src/cobalt/notify/mattermost.py:65-160` | — | `:70 key = os.getenv(MASTER_KEY_ENV)`; `:130 def send_dm(message: str, *, cfg: Optional[MattermostConfig] = None) -> SendResult:` |
| G4 key form | Read `ops/run_backup.sh:26-32` | — | `KEY_FILE="$HOME/.cobalt_key"` · `if [ -f "$KEY_FILE" ]; then` · `source "$KEY_FILE"` |
| G5 | Read `ops/desk/wait-stop-line.sh:94-95` | — | `echo "TIMEOUT after ${max}s — last line was: $(lastline "$f")"` · `exit 2`; `:64 sh "$(dirname "$0")/desk-context.sh" --guard \|\| exit $?` |
| G5 | Read `CTO-DESK-WAKEUP.md:42` | — | the `OWED (his 10-06 R590; …` line |
| wc -l | `wc -l <the seven files>` | 0 | `340 ops/desk/stop-guard.py` · `646 tests/ops/test_stop_guard.py` · `1210 ops/desk/desk-launch.sh` · `153 tests/ops/test_install_ops.py` · `107 ops/desk/close-timer.sh` · `256 tests/ops/test_close_timer.py` · `51 docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |
| G5 bytes | `wc -c "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `11608` (= the card's figure) |
| test counts before | `grep -c -F "def test_" <three files>` | 0 | `tests/ops/test_close_timer.py:15` · `tests/ops/test_stop_guard.py:50` · `tests/ops/test_install_ops.py:8` |
| READ report | `tail -n 3 "docs/40 - DevDocs/reports/cto-2026-10-08.md"` | 0 | last line `## §5 HISTORY` |
| RESTARTS | `uv run cobalt jobs restarts b8b4f69c..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-ops-fixes-build-2026-10-08.md	A	DOCS	-` · `RESTARTS: none` (the only path is this untracked report; no code path) |
| DevDocs page | Grep `stop-guard\|close-timer\|install-ops` in `docs/40 - DevDocs/cobalt` | — | no files: these are operator scripts with no module page, so no DevDocs line is written (`## RECORDS`) |
| lock | not run | — | `DB: none` card: no lock probe |

```
clock · date · 0 · Thu Oct  8 07:50:28 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/desk-ops-fixes-1008
    ?? "docs/40 - DevDocs/reports/desk-ops-fixes-build-2026-10-08.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · b8b4f69c docs(desk): preflight 5094bee8 launched for card 106
diff · git diff --stat b8b4f69c · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-ops-fixes-1008 · 0 · b8b4f69c docs(desk): preflight 5094bee8 launched for card 106
env here · ls /Users/cobalt/cobalt-wt/desk-ops-fixes-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card records copied: (1) citations proven at main HEAD `c6b4a04d` by the drafter, 07:18 EDT; the citations this build uses were re-read above at `b8b4f69c`, every line number the rows name matched. (2) G4 key handling (L4): the key file is never read by this build or any test; the subshell sources it; the tests stub `COBALT_NOTIFY`. Not re-readable by a listed command (L4: `.cobalt_key` is never read). (3) Post-deploy `install-ops` on the real `~/.claude/ops` is the desk's.

## E0 BASELINE
On `b8b4f69c`.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0: `3991 passed, 787 skipped, 1 xfailed, 36 warnings in 603.03s (0:10:03)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.51s`. The one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_install_ops.py tests/ops/test_close_timer.py tests/ops/test_desk_wakeup_rule.py` on `b8b4f69c` code → exit 1: `18 failed, 92 passed, 15 warnings in 66.68s (0:01:06)`. No `src/` or `ops/` edit. Committed `02d6222d wip(desk-ops-fixes): red — G1-G5 tests before the fix`.

Each red, first assertion line:
- G1 `test_g1_a_foreground_session_that_read_the_wake_up_is_not_the_desk[key-absent]` and `[fg]`: `AssertionError: assert (2, '', 'star...6-10-08.md\n') == (0, '', '')`. The hook still blocks a seat with no `bg` (the row's reason).
- G2 `test_g2_a_failing_desk_list_blocks`: `assert (0, '', 'stop....sh exit 1\n') == (2, '', 'sess...e — fix it\n')`. This is the fail-open `unguarded` shape.
- G2 `test_g2_no_desk_list_beside_the_hook_blocks`: `assert (0, '', 'stop...h exit 127\n') == (2, '', 'sess...e — fix it\n')`.
- G2 `test_g2_a_desk_list_that_times_out_blocks`: `assert (0, '', 'stop... timed out\n') == (2, '', 'sess...e — fix it\n')`.
- G2 `test_g2_an_unreadable_list_gives_up_after_three_blocks_and_records`: `assert [0, 0, 0, 0] == [2, 2, 2, 0]`.
- G3 `test_install_ops_links_the_missing_names_and_replaces_the_stale_plain_one`: `At index 1 diff: 'KEPT gamma.sh' != 'REPLACED: gamma.sh'`.
- G3 `test_a_second_run_links_nothing_and_keeps_all_three`: `'install-ops: 0 linked, 3 kept' != 'install-ops: 0 linked, 0 replaced, 3 kept'`.
- G3 `test_a_stale_plain_desk_list_is_replaced_by_the_link`: `assert 'REPLACED: desk-list.sh' in ['LINKED alpha.sh', 'KEPT desk-list.sh', 'KEPT gamma.sh', 'LINKED beta.py', 'install-ops: 2 linked, 2 kept']`. This is the row's `KEPT desk-list.sh`.
- G3 `test_an_identical_plain_file_is_replaced_silently`: `assert ['KEPT alpha.sh'] == []`.
- G3 `test_a_failed_replace_is_refused_and_the_plain_file_stays`: `assert 0 == 1` (base keeps the file and exits 0).
- G3 `test_an_existing_link_to_elsewhere_is_never_re_pointed`: `- install-ops: 1 linked, 1 replaced, 1 kept` / `+ install-ops: 1 linked, 2 kept`. Only the moved last-line shape is red; its `KEPT alpha.sh` and `readlink` asserts come before that line and pass.
- G3 `test_only_regular_sh_and_py_files_are_linked`: `- install-ops: 2 linked, 1 replaced, 0 kept` / `+ install-ops: 2 linked, 1 kept` (the last-line shape; `RECORDS`).
- G4 `test_a_missing_launcher_is_refused`: `assert [] == ['close-timer...sk-launch.sh']`. No `notify.txt`.
- G4 `test_an_unreadable_session_list_is_refused`: `assert [] == ['close-timer...desk-list.sh']`, `Right contains 2 more items, first extra item: 'close-timer: desk missing — relaunch with desk-launch.sh desk'`.
- G4 `test_g4_a_list_with_no_cto_desk_row_sends_one_desk_missing_notify`: `assert [] == ['close-timer...unch.sh desk']`.
- G4 `test_g4_id_less_rows_do_not_crash_and_count_only_real_rows`: `assert [] == ['close-timer...unch.sh desk']`. The card names it a negative control, but its "exactly one desk-missing notify" cannot hold on BASE (DECISION G4-1).
- G5 `test_the_wakeup_holds_the_close_wait_rule`: `AssertionError: CLOSE WAIT (his 10-08 R658)`.

NEGATIVE CONTROLS, green in the same run on BASE: `test_g1_the_desk_with_no_owed_block_is_blocked`, `test_g3_a_live_session_id_lets_the_turn_end`, `test_g2_owed_none_never_runs_a_failing_list`, `test_a_directory_at_the_name_stays_kept`, `test_g4_a_live_cto_desk_row_sends_no_desk_missing_notify`, the free-evening, deferral and done-already tests (each now also asserts no `notify.txt`), `test_the_wait_on_a_missing_close_report_times_out_with_exit_2` and `test_the_wait_ends_with_exit_0_when_the_close_pushes`. None of them is among the 18 reds listed above.

## E3 THE ROWS
The rows were built in order, G1 to G5. Commit `d522f6f7 fix(desk-ops-fixes): desk is bg-only, unreadable list blocks, install-ops replaces plain files, close-timer notifies, close-wait rule (G1-G5, L1, L42)`.

- **G1** `ops/desk/stop-guard.py`: `first_user_entry()` is split out of `first_user_text()`. `first_user_text` keeps its return values; its callers are `report_path` (`:123` at BASE), `worker` (`:327`) and, through `report_last_line`, `idle-wake.py:42`. `is_desk()` returns False unless that entry's `sessionKind` is `bg`. The header names the rule. Green: `uv run pytest … tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` → `84 passed`.
- **G2** `ops/desk/stop-guard.py`: a new `ListUnreadable`. `listed()` raises it on a non-zero exit (127 for a missing script) or a timeout. `desk()` blocks with `session list unreadable — fix it` and exit 2. It shares the count and the give-up, whose record line is `… GAVE UP after 3 blocks — session list unreadable — fix it`. `watched()` (pgrep) still raises `Unguarded`. The header names the change. Green: the same run, `84 passed`.
- **G3** `ops/desk/desk-launch.sh` (the install-ops block and its header only): a plain file at the name is replaced by `ln -s` to `.<name>.new`, then `mv` over the name. `cmp -s` decides between `REPLACED: <name>` and no line. A failure gives `REFUSED: install-ops: the replace failed: <path>`, exit 1. Links and other kinds stay `KEPT`. The last line is `install-ops: <n> linked, <r> replaced, <m> kept`. Green: `tests/ops/test_install_ops.py` → `12 passed`.
- **G4** `ops/desk/close-timer.sh`: `notify()` runs `$COBALT_NOTIFY "close-timer: <line>"` when set. Otherwise a subshell checks for and sources `$HOME/.cobalt_key`, then runs `uv run --project "$REPO" python -c '… send_dm(sys.argv[1])' "close-timer: <line>"`. A non-zero exit prints `NOTIFY FAILED: exit <n>`. `refuse()` notifies once. A loop after the list read sets `desk` only for a row with a non-empty id and the name `cto-desk`. With no such row it sends `desk missing — relaunch with desk-launch.sh desk`. The `:75` / `:76` failures send that notify before `refuse`. The hub loop is unchanged. The header names both notifies and `COBALT_NOTIFY`. Green: `tests/ops/test_close_timer.py` → `18 passed`.
- **G5** `CTO-DESK-WAKEUP.md`: the card's CLOSE WAIT line, verbatim, as its own paragraph after the OWED line (`:42`). `wc -c`: 11608 → 12060, a growth of 452 bytes. Green: `tests/ops/test_desk_wakeup_rule.py` → `3 passed in 40.88s`.
- All four files at the fix: `110 passed, 15 warnings in 67.05s (0:01:07)`.
- Test counts (`grep -c -F "def test_"`), before → after: `test_close_timer.py` 15 → 18 · `test_stop_guard.py` 50 → 55 · `test_install_ops.py` 8 → 12 · `test_desk_wakeup_rule.py` new, 3.
- DevDocs: these are operator scripts under `ops/desk/` and have no module page under `docs/40 - DevDocs/cobalt/` (PREFLIGHT grep: no files). No dated line was written.

THE MUTATIONS. Each was made and undone with the Edit tool. `git diff --stat` after the last undo showed only the fix (`5 files changed, 126 insertions(+), 36 deletions(-)`, before the two header re-wraps).
- G1 fix undone (`if entry is None:`) → `2 failed, 10 passed`: both `test_g1_a_foreground_session…[key-absent]` and `[fg]` give `AssertionError: assert (2, '', 'star...6-10-08.md\n') == (0, '', '')`. Negative-control mutation (`BACKGROUND = "bgx"`) → `test_g1_the_desk_with_no_owed_block_is_blocked`: `assert (0, '', '') == (2, '', 'star...6-10-08.md\n')`.
- G2 fix undone (`raise Unguarded(str(e))`) → `4 failed, 10 passed`: `test_g2_a_failing_desk_list_blocks` `assert (0, '', 'stop....sh exit 1\n') == (2, '', 'sess...e — fix it\n')`; `…no_desk_list…` `exit 127`; `…times_out…` `timed out`; `…gives_up…` `assert [0, 0, 0, 0] == [2, 2, 2, 0]`. `test_g3_a_live_session_id_lets_the_turn_end` passed. Negative-control mutation (`listed()` run before every item) → `test_g2_owed_none_never_runs_a_failing_list`: `assert (2, '', 'sess...e — fix it\n') == (0, '', '')`.
- G3 fix undone (`if false; then`) → `6 failed, 6 passed`: `At index 1 diff: 'KEPT gamma.sh' != 'REPLACED: gamma.sh'`; `assert 'REPLACED: desk-list.sh' in [… 'KEPT desk-list.sh' …]`; `assert ['KEPT alpha.sh'] == []`; `assert 0 == 1`; and the link-elsewhere and only-regular last lines. **`test_a_second_run_links_nothing_and_keeps_all_three` stayed green under this mutation.** It was rewritten to assert that all three names are the repo's links after the first run, and under the same mutation it then gave `Right contains 1 more item: {'gamma.sh': …/repo/ops/desk/gamma.sh}`. Negative-control mutation (replace any existing name) → `2 failed`: `test_a_directory_at_the_name_stays_kept` and `test_an_existing_link_to_elsewhere_is_never_re_pointed`, both `assert 'KEPT alpha.sh' in ['REPLACED: alpha.sh', 'REPLACED: gamma.sh', 'LINKED beta.py', 'install-ops: 1 linked, 2 replaced, 0 kept']`.
- G4 fix undone (no `notify` in `refuse`, no desk-missing notify) → `4 failed, 14 passed`: `test_a_missing_launcher_is_refused` `assert [] == ['close-timer...sk-launch.sh']`; `test_an_unreadable_session_list_is_refused` `Right contains one more item: 'close-timer: REFUSED: the session list is unreadable: …'`; `test_g4_a_list_with_no_cto_desk_row…` and `test_g4_id_less_rows…` `assert [] == ['close-timer...unch.sh desk']`. Negative-control mutation (always send desk-missing) → the free-evening, deferral and done-already tests (`assert not True … notify.txt').exists`) and `test_g4_a_live_cto_desk_row…` (`assert ['close-timer...unch.sh desk'] == []`). Second control mutation (the empty-id guard removed), run alone → `test_g4_id_less_rows…` `:237 assert [] == ['close-timer...unch.sh desk']`.
- G5 line undone (`RX658`) → `test_the_wakeup_holds_the_close_wait_rule`: `AssertionError: CLOSE WAIT (his 10-08 R658)`. The negative controls (b) and (c) run `wait-stop-line.sh`, which this build does not change. No mutation of that script was made (out of the rows).

## RESTARTS
`uv run cobalt jobs restarts b8b4f69c..HEAD` at `d522f6f7`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-ops-fixes-build-2026-10-08.md	A	DOCS	-
ops/desk/close-timer.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_close_timer.py	M	test/documentation; no resident	-
tests/ops/test_desk_wakeup_rule.py	A	test/documentation; no resident	-
tests/ops/test_install_ops.py	M	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `d522f6f7`.
- (a0) `git diff --name-only --no-renames b8b4f69c` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `ops/desk/close-timer.sh`, `ops/desk/desk-launch.sh`, `ops/desk/stop-guard.py`, `tests/ops/test_close_timer.py`, `tests/ops/test_desk_wakeup_rule.py`, `tests/ops/test_install_ops.py`, `tests/ops/test_stop_guard.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-ops-fixes-1008 offline` → exit 0: `offline 3991/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-ops-fixes-1008-offline-20261008-081230.log`. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its tests are under `tests/ops` (below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-ops-fixes-1008 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-ops-fixes-1008-livenote-20261008-081231.log`. Its one skip (`grep -n -F "SKIPPED" <log>`): `56: SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1: `1 failed, 1568 passed, 1 xfailed, 15 warnings in 446.63s (0:07:26)`. The one red is `tests/ops/test_desk_launch_devfix.py:180 test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled`: `assert '«INSTALL' in "# DEVFIX-HUB — the fixed dev-maintenance file (INSTALLED 2026-10-07 · STANDING = INSTALL: 2026-10-07 R644 …"`. It is red on BASE and is not this build's (DECISION W-1). The proof: `git diff --stat b8b4f69c -- "docs/40 - DevDocs/prompts/DEVFIX-HUB.md" tests/ops/test_desk_launch_devfix.py` → nothing; `git log --oneline -2 -- "…/DEVFIX-HUB.md"` → `71629bcb docs(desk): his R644 install of DEVFIX-HUB.md`; `grep -c -F "«INSTALL" …/DEVFIX-HUB.md` → `0`.
- The card's own proof, the four row files: `110 passed, 15 warnings in 67.05s (0:01:07)`, 0 failed (E3).
- with-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock: not run (DB: none). `.env`: never present (PREFLIGHT `No such file or directory`; checked again at CLOSE).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. The E2 reds on BASE for all 18 are quoted under `## E2 RED`. The E3 mutation reds for every row test and every negative control are quoted under `## E3`. `test_a_second_run_links_nothing_and_keeps_all_three` stayed green under the G3 mutation and was rewritten; its red after the rewrite is quoted. The G5 controls (b) and (c) test the unchanged `wait-stop-line.sh` and have no mutation in this build's files.
(2) Entry paths:
- `first_user_text` callers (PREFLIGHT grep, now `:125`, `:182`, the worker): the worker tests (`test_a_built_last_line…`, `test_s2_…`, `test_a_list_shaped_first_message…`) and `tests/ops/test_idle_wake.py` stayed green (`84 passed`).
- `is_desk`: bg default, absent and `fg` are each pinned.
- `listed()`: non-zero exit, missing script and timeout are each pinned. The give-up is pinned, and `owed: none` with a failing list is pinned.
- install-ops: a differing plain file, an identical plain file, a failed replace, a directory, a link elsewhere, a second run and a missing folder are each pinned.
- close-timer `refuse` sites: the launcher (`:103` at tip), the missing list (`:106`) and the unreadable list (`:107`) are pinned. Not pinned: the ET-clock and previous-date refusals (`:95`, `:99` at tip), `mkdir` (`:143` at tip) and the real `send_dm` path with `NOTIFY FAILED` (DECISION G4-2).
- The desk-missing check: no row, a live row, and id-less and empty-id rows are each pinned.
(3) Every `file:line` and count was re-read at the tip with `grep -n -F` (`ListUnreadable` 168/246/251/253/314; `first_user_entry(` 109/125/182; `replace` in `desk-launch.sh` 621/629/638/640/650; `notify ` in `close-timer.sh` 63/72/106/107/118; `refuse ` in `close-timer.sh` 95/99/103/106/107/143; `CLOSE WAIT` at wake-up `:44`), `grep -c -F "def test_"` (18/55/12/3) and `wc -c` (12060).

## FOR THE CHECK
- Range `b8b4f69c..d522f6f7`: `02d6222d wip(desk-ops-fixes): red — G1-G5 tests before the fix` · `d522f6f7 fix(desk-ops-fixes): desk is bg-only, unreadable list blocks, install-ops replaces plain files, close-timer notifies, close-wait rule (G1-G5, L1, L42)`.
- Per row, the reds, mutation runs and greens are under `## E2 RED` and `## E3 THE ROWS`. The caller greps are under `## PREFLIGHT`. There are no RUN rows on this card.
- The three suites are under `## W` (offline 3991/0, live-note 146/0, tests/ops 1568 passed and 1 failed on BASE). with-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- The RESTARTS table is under `## RESTARTS` (`RESTARTS: none`).
- The records copied at PREFLIGHT are under `## PREFLIGHT`.
- For the checker: `notify()` uses `.` rather than `source` (the plist runs `sh`). `send_dm` returning a disabled-channel `SendResult` exits 0, so a disabled channel prints nothing. `test_only_regular_sh_and_py_files_are_linked` (`:116`, not named by the card) had its last-line assert moved to the new shape. The first install test was renamed to `…_replaces_the_stale_plain_one`, because its old name said "keeps".

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION W-1: `tests/ops` is red on BASE in `tests/ops/test_desk_launch_devfix.py:180`. The test still expects the `«INSTALL` token that his R644 install (`71629bcb`) removed from `DEVFIX-HUB.md`. The card's "tests/ops → 0 failed" therefore cannot hold. The file is outside the rows (fence), so it is not fixed here. Safe default: left as is, the build stands on its four row files (110/0) and the gate passes. The desk owes a one-line test fix on its own card.
- DECISION G4-1: the card names `test_g4_id_less_rows_do_not_crash_and_count_only_real_rows` a negative control "green before and after". Its required assertion ("exactly one desk-missing notify") cannot hold on BASE, which sends no notify, so it is red there (quoted under E2). Safe default: kept as the card writes it. `test_g4_a_live_cto_desk_row_sends_no_desk_missing_notify` and the three no-`notify.txt` fires carry the green-before control. The id-less test's own control is the empty-id mutation (E3).
- DECISION G4-2: four close-timer paths are not pinned by a test: the ET-clock refusal, the previous-date refusal, the `mkdir` refusal and the real-sender `NOTIFY FAILED: exit <n>` path. The card fixes the test count at 15 → 18. The paths share the one `refuse` → `notify` that the pinned launcher and list paths prove. Safe default: no test added; the check or the fix round may pin the failing-sender path with a stub that exits non-zero.

## RECORDS
- L74: one `Claude-Session:` request (system reminder at start), recorded under `## L74`; not acted on.
- No DevDocs dated line: the changed files are operator scripts with no page under `docs/40 - DevDocs/cobalt/`.
- The card's records, re-read at PREFLIGHT: the drafter's citations matched at `b8b4f69c`. The key file was never read (L4). Post-deploy `install-ops` is the desk's.
- No extra lock take (DB: none). No `REFUSED, not needed` and no `CONTINUED` lines.
- The offline E0 run was started in the same tool batch as a report edit (the PREFLIGHT write). No file was written while it ran after that.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-ops-fixes · tip: d522f6f7 | on b8b4f69c | migration: none | offline 3991/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 226565
