# desk-ops-fixes preflight — 2026-10-08

Card `106` (rows G1-G5), main HEAD `b8b4f69c`. Read-only. Nothing was run: this seat has no pytest allow-line, so every RED and green below is proven by reading the code against the test, not by a run.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header vs `CARD.md` | JOB/LADDER/BRANCH/WORKTREE/BASE/TIP/REPORT/CHECK REPORT/HOUSE B/RULINGS/DB present. BASE is `«FILL: main HEAD at launch, 8 hex»`, the only fill token (`grep -c '«FILL'` → 1). TIP, CHECK REPORT and HOUSE B are empty. `DB: none` | OK |
| 2 | `git rev-parse --verify ops/desk-ops-fixes-1008`; `ls cobalt-wt` | branch not found; no `desk-ops-fixes-1008` in `cobalt-wt` (both new) | OK |
| 3 | `cto-2026-10-08.md` R657 and `cto-2026-10-08-words.md` R657 | R657 row: `HIS RULING … APPROVED`. Words: `> approved`. `git diff HEAD` of both files is empty; `git log` shows them committed (`96ee29b7`, `b8b4f69c`) | OK |
| 4 | R658, R660, R662, R664 rows | R658 `HIS RULING · APPROVED` (G5 and G6). R660 `HIS RULING · APPROVED` (D1 = A, D2 = B). R662 `HIS RULING · APPLIED: LAWS L79` (no new command unless the brain says so). R664 `DESK RECORD (brain's order)`: G4 also notifies when no `cto-desk` row is live, card `109` dropped | OK |
| 5 | card, draft, amend, amend2 committed | `git log` of the four paths: `96ee29b7`, `6cc234f6`, `ee9d8a8b`; `git diff --stat HEAD` of the four paths and `ops`, `tests/ops` is empty | OK |
| 6 | G1 cites in `stop-guard.py` | `is_desk` `:151-164`; `first_user_text` `:100-118`; `report_last_line` `:135-144`; header `:15-17`. All match. The one `isMeta` skip is at `:108` | OK |
| 7 | G1 test cites | `Desk.first` `:290-299`, first user entry `:294` has no `sessionKind`; control `test_g1_the_desk_with_no_owed_block_is_blocked` `:334-338`. On BASE the key is never read, so `Desk(kind=None).owed()` is blocked: `(2, "", missing(d))` → RED for the stated reason. Control green on BASE and after | OK |
| 8 | G1 callers of `first_user_text` | `grep`: `:123` (`report_path`), `:160` (`is_desk`), `:327` (`worker`). `idle-wake.py:42` calls `guard.report_last_line` only. The worker path and `idle-wake.py` keep `first_user_text` | OK |
| 9 | G1 key evidence | draft RECORDS: own `bg` transcript carries `"sessionKind":"bg"` on its first user entry, and no other value was found | OK |
| 10 | G2 cites | `listed()` `:219-229`; `desk()` `:269-299` (block and give-up `:290-299`); `watched()` `:232-240`; header `:29-30`; `main` catch-all `:312-318` | OK |
| 11 | G2 tests | `test_g5_a_failing_desk_list_fails_open` `:589-593`: `lister(ROW, code=1)` → on BASE `Unguarded("desk-list.sh exit 1")` → exit 0 with `stop-guard: desk not guarded — …` → RED. No `desk-list.sh` beside the hook → `sh` exits 127 → the same BASE result → RED. Three-block give-up shape `:513-523`. Controls: `:449` green; `owed: none` runs no list read (`unsettled` gets `[]`) → green | OK |
| 12 | G3 cites | block `desk-launch.sh:616-639`; keep test `:628-630`; header `:74-80` ("nothing there is ever replaced" `:78-79`); `ln -s` without `-f` comment `:617-618` | OK |
| 13 | G3 tests | `test_install_ops.py` is 153 lines; `world` stages `gamma.sh` as a plain `KEPT_BYTES` file (`:36`). BASE prints `KEPT gamma.sh` and leaves a plain file → RED for the stated reason. `:63-78`, `:81-95` (`KEPT_BYTES` read `:94`), `:97-104` match. A directory at the name is `-e`, not `-f` → KEPT, so the control holds. Tests use `COBALT_REPO_ROOT` and `COBALT_OPS_LINK_DIR` (`:43`) | OK |
| 14 | G3 scope | `install-fixed.sh:9-11,39` holds the `«INSTALL` token (card says `:1-14`, true); the card does not touch it | OK |
| 15 | G4 cites in `close-timer.sh` | 107 lines; `refuse` `:42-45`; launcher check `:72`; `:75` missing list, `:76` list read; hub loop `:77-91`; name field `:81`; header `:17-33`; `refuse` call sites `:64,68,72,75,76,101` (exactly six) | OK |
| 16 | G4 sender cites | `send_dm` `mattermost.py:130`; key check `:70-77`; `ops/README.md:400` "there is no `cobalt notify` command"; plist `PATH` only `:11-16`; `run_backup.sh:26-32` `KEY_FILE="$HOME/.cobalt_key"` + `source`. `cobalt.notify` exports `send_dm` (`__init__.py:26,36`). `uv` is at `~/.local/bin/uv`, which the plist `PATH` holds. The vault file is `REPO_ROOT/data/.cobalt_vault` (`secrets.py:43`), so no vault env is needed | OK |
| 17 | G4 tests | `box` `:65-115`, default `rows.txt` = `CTO` `:79`, `LOOKALIKE` `:60`, tests `:121,130,146,162,170`. `grep -c '^def test_'` → 15 (card: 15 → 18). BASE: no `COBALT_NOTIFY` hook, so no `notify.txt` → the two refused tests and the desk-missing test are RED. The free-evening, deferral and done-already fires hold a live `CTO` row → no `notify.txt` → controls green. Id-less row ` · cto-desk · …`: `${row#* · }` leaves `cto-desk · …`, the id is empty → counts for nothing, no crash | OK |
| 18 | G4 command rule (R411, R412, R660, R662) | The only new command is the vault-key form: `. $HOME/.cobalt_key` in a subshell, then `uv run --project "$REPO" python -c '…send_dm…' "close-timer: <line>"`. It runs inside `close-timer.sh` under launchd, so no seat allow-line changes. R660 approves it; R664 adds only a second message on the same sender. No other command or argument appears | OK |
| 19 | G4 key (L4) | The key is sourced in a subshell and reaches only its `uv` child. Argv holds the REFUSED or desk-missing line. No `echo`, `set -x` or log line carries it. Tests stub `COBALT_NOTIFY` and never read `~/.cobalt_key`. NOT IN THIS JOB bars the real send | OK |
| 20 | G5 cites | wake-up `OWED` line `:42`, WAIT `:16`; `wc -c` → 11608 (matches); `wait-stop-line.sh:94-95` `TIMEOUT after ${max}s …` / `exit 2`; `desk-launch.sh:333-341` the 21:00 ET rule | OK |
| 21 | G5 tests | (a) none of the three literals is in the wake-up today → RED. (b) missing file, max 1: the loop runs once, sleeps 20, then `TIMEOUT after 1s` and exit 2 → green. (c) a file that gains a `CLOSE PUSHED …` line → exit 0 → green (see NOTE 1). The stub `desk-context.sh` way is `test_install_ops.py:48-53`. `tests/ops/test_desk_wakeup_rule.py` does not exist yet | OK |
| 22 | rows vs rulings | G1-G4 = R657 plus R660 (G4 sender) and R664 (second notify); G5 = R658 (turn rule only). G6 is out. `grep` of the card for `G6`: only the "left this card" note and C8/C9; no G6 residue | OK |
| 23 | files outside the rows | NOT IN THIS JOB bars `install-fixed.sh`, `desk-list.sh`, the plist, settings, `src/`. Every row's files cell is `ops/desk/*` or `tests/ops/*` plus the wake-up | OK |
| 24 | tests use temp roots | Stop-guard tests stage under `tmp_path`; install-ops and close-timer use env roots; the G5 test copies the script under `tmp_path`. No `~/.claude` or `~/.cobalt_key` read | OK |
| 25 | drift since the draft | `git diff --stat c6b4a04d HEAD -- ops tests/ops CTO-DESK-WAKEUP.md src/cobalt/notify` is empty; every cite still holds | OK |
| 26 | RESTARTS class homes | `restarts.py`: `ops/desk/` → operator script, no reader (`:38,230`); `tests/` (`:245`); `docs/` (`:225`). Expected `RESTARTS: none` is right. The classes are stated in the card's RESTARTS paragraph, not in `## RECORDS` (see NOTE 3) | OK |

## ISSUES
- NOTE 1 (G5 c): `wait-stop-line.sh` checks the file once at once, then sleeps 20 s (`:74-91`). With `max` 1 the change is never seen, so test (c) needs `max` ≥ 21 (two polls). The card gives (c) no `max`; the builder must pick one.
- NOTE 2 (self-check 2): only `:76` and `:72` are pinned by a test. `:75` (list file missing) has no test, and `:64`, `:68`, `:101` have none. The card says to name any unpinned caller; it names none.
- NOTE 3 (RECORDS): the RESTARTS class of each path is in the card's `RESTARTS (K10)` paragraph, not `## RECORDS`; the wake-up under `docs/` has no class named (`restarts.py:225`). Wording only; not a failure.
- NOTE 4 (proof): no test was run here (no pytest allow-line). The REDs rest on reading the code; the builder's BASE run must quote them.
- NOTE 5 (R660): the words row is `approved brains dejan said`, and the desk reading maps it to D1 = A, D2 = B. The brain's R664 order covers the G4 second notify. Kept defaults, not failed.

PREFLIGHT DONE · card: desk-ops-fixes-106 · checks: 26 · fails: 0 · ready: YES
