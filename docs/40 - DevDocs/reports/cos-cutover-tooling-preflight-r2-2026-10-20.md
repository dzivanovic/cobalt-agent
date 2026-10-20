# cos-cutover-tooling preflight r2 · 2026-10-20 (`date` not run; the run is after 17:55 ET)

Card 931 (`prompts/2026-10-20/931-cos-cutover-tooling-card.md`), K5, BAND HIGH. Read-only; nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 main` and `HEAD`; `git diff bd7bc0c9 main --stat -- ops/desk tests/ops <DEPLOY-HUB.md>` | both `4a9b60bd` (desk commits above BASE `bd7bc0c9`); the diff prints nothing, so every `file:line` is the BASE's. `git log bd7bc0c9..HEAD -- ops/desk tests/ops DEPLOY-HUB.md` is empty | OK |
| 2 | `git diff HEAD --stat -- <card>` and `<cto-2026-10-18.md>` | empty: the card is committed and unchanged | OK |
| 3 | header: JOB, CLASS K5, BRANCH `ops/cos-cutover-tooling`, WORKTREE `cos-cutover-tooling`, BASE `bd7bc0c9`, TIP empty (expected), BAND HIGH, DB none, HOUSE B, INSTALL none, RESTARTS none; `ls` of the worktree and the check report, `rev-parse --verify` of the branch | worktree, check report and branch absent; no FILL token in the card | OK |
| 4 | `RULINGS: 2026-10-18 R1863` vs `desk-launch.sh:1328-1332` | `:1329` pattern `20YY-MM-DD R<n>*` matches; the `none` refusal (`:1330`) no longer applies. Round-1 fail 1 closed | OK |
| 5 | R1863 is one row of his: `git grep -n -F R1863 main -- reports/cto-2026-10-18.md`; `git log -1 -S"\| R1863 \|"`; `authorize.sh:31`, `:115` | `cto-2026-10-18.md:90` `\| R1863 \| 07:09 ET \| HIS RULING · APPROVED (brain, L79) …`: one line holding `HIS RULING` then `APPROVED` (the `:115` pattern); introduced by commit `11563e82`; no uncommitted diff of the file | OK |
| 6 | `git diff 53ecf8a6 HEAD -- <card>` (the amend changed nothing else) | 3 hunks only: T1b row (neither-OFFLINE-nor-ONLINE fail added), T1c row ((f)-(h), test starts, line counting, `eight times`, files cell), NOT IN THIS JOB list (`:53`, `:155`, `:160` added), DEPLOY PROOF (one marker-count note line, hub `after 5` → `8`). `RULINGS`, header and every other row byte for byte | OK |
| 7 | `git grep -n -F "agent" main -- DEPLOY-HUB.md` and `git grep -n -E "ONLINE\|OFFLINE\|cobalt.sh status\|residents down"` against T1c's list | agent/status reads: `:3`, `:11` (allow strings), `:53`, `:65`, `:78`, `:89` (plist label refusal, no read), `:93`, `:95`, `:123`, `:140`, `:144`, `:150`, `:155`, `:160`, `:163`, `:169`. Covered by (a)-(h): `:53` (f), `:65` (a), `:93` (c), `:123` (b), `:150` (d), `:155` (g), `:160` (h), `:169` (e). Not covered and correct: `:3`, `:11`, `:78`, `:89`, `:95` (no agent read), `:140`, `:144`, `:163` (act only on an agent in `<restart set>`, which (c) empties) | OK |
| 8 | `DEPLOY-HUB.md:155` holds `RESTARTS:` minus deferred/not-loaded `= STEP-R's <restart set>`; `:160` holds `agent OFFLINE at tail 3`; `:53` (e) holds `cobalt.sh status → ONLINE`, `(e) false … run STEP-5 (3) NOW` | all three at the cited lines; the card's line starts (`- THE ONE RESUME`, ``- (f) `COBALT_ENV=production uv run cobalt validate` ``, `RED = a resident`) match (`:108` is `- (f) THE L76 RELEASE`, kept apart) | OK |
| 9 | `after 8` follows from the card's own edits: lines holding `com.cobalt.agent recorded retired` after T1c | one clause per place (a)-(h) = 8 places = 8 lines; `(a)` P8 repeats the literal in its `FAILED PREFLIGHT` text on the same line, and `grep -c -F` counts lines, so 8. The card says lines, not occurrences (T1c cell, DEPLOY PROOF note, test `eight times`) | OK |
| 10 | marker `before` values: `git grep -c -F` of `card 931 T2`, `is retired; a retired label is never restarted`, `retired (recorded)` in `ops/desk`; `com.cobalt.agent recorded retired` in the hub, at `HEAD` | no match for any (count `0` each) | OK |
| 11 | `desk-launch.sh` cites: `:1286`, `:1328-1332`, `:1350-1352`, `:1374`, `:1385`, `:1705`, `:1848`, `:1865`, `:2161`, `:2173-2175`, `:2203`, `:2206`, `:2208-2209`, `:2670` | each where the card says (`:2161 section SHIPS`, `:2173 hex8`, `:1865 agent\|aset\|radar … is a resident`, `:2670 worktree add -b … main`, `:2206 ships_checked`) | OK |
| 12 | `deploy-step0.sh`: `:41`, `:73`, `:875-886` | `:73 RESIDENTS=…`, `:875 for label in $RESIDENTS`, `:885 row "P8 census $label" … (recorded)" 0` | OK |
| 13 | `deploy-outage.sh`: `:18-27`, `:140`, `:233`, `:265`, `:432-436` | header, dry run `:140`, agent pre-check `:233`, kickstart `:265`, trap append `:432`, `fail com.cobalt.agent "cobalt.sh status is not ONLINE"` `:436` | OK |
| 14 | control tests exist at the cited lines: `test_deploy_step0.py:981`, `:996`, `:1029`; `test_deploy_outage.py:280`, `:319`, `:445`, `:557`; `test_hub_cos_restart_1019.py`, `test_hub_deferred_1018.py`, `test_desk_launch_launchd.py` | all present at those lines; the two NEW files (`test_hub_agent_retired_1020.py`, `test_desk_launch_bootstrap_only.py`) absent, as a card not yet built | OK |
| 15 | RED test first | T2: BASE refuses at `:2161` (`no '## SHIPS' section`); partial-form and refusal tests state in their docstrings that BASE refuses by another message. T1a: BASE prints `pid … state …` and runs the print. T1b: BASE final read fails OFFLINE and the set of two runs. T1c: count 0 on BASE | OK |
| 16 | retired agent found ONLINE fails loud (F-14); a status that is neither OFFLINE nor ONLINE | T1b(ii) now fails ONLINE and neither state (round-1 note 7 fixed); hub P8 and D1 `FAILED PREFLIGHT`; (h) makes a retired ONLINE agent RED | OK |
| 17 | every builder command vs `BUILD-HUB.md` allow strings | the card types `uv run pytest *`, `uv run cobalt jobs restarts *`, `grep *`, `sh /Users/cobalt/cobalt/ops/desk/*` only (unchanged by the amend) | OK |
| 18 | `## DEPLOY PROOF` forms | four `grep -c -F … · before … · after …` marker lines (mapped shape) plus the pytest line (same form as cards 869 and the cos-restart fr1; round-1 note 3, non-defect). The new note line has no `· before` / `· after`, so it is not read as a marker | OK |
| 19 | `RESTARTS: none` vs `restarts.py:38`, `:225-228`, `:230-232`, `:245-246`; installed copies | `ops/desk/` operator script, `docs/` DOCS, `tests/` no resident; no resident reads these files. R5 stays a run. `~/.claude/ops/` copies link into `ops/desk/` (round 1 check 17; the amend does not touch `INSTALL`) | OK |
| 20 | the card weakens no guard for another card | T2 relaxes `section SHIPS`, `hex8` / `commit_exists` on TIP, `$WT/none`, `ships_checked` and `worktree add` only on the whole form; FILL, committed-card, RULINGS, JOB, TAG, REPORT, `%`, report-exists, lock, line-token and `--add-dir` checks stay (round 1 check 19; text unchanged) | OK |
| 21 | what blocks the card's own build | nothing found: the launcher's `RULINGS` check passes (check 4), the card is committed, no worktree/branch/report exists, `TIP:` empty and BASE trailing main by desk commits are expected | OK |

## ISSUES

1. NOTE · round-1 notes 3, 6, 8 are non-defects (not re-raised). The rest of round 1 (4, 5, 7) are fixed by the amend.
2. NOTE · `date` was not run in this seat (the timestamp in the title is approximate).

PREFLIGHT DONE · card: cos-cutover-tooling · checks: 21 · fails: 0 · ready: YES
