## §0
- Card 790 as PORT3 (`f16-close-fr3`, BASE `4aa0481d`) is ready: every check holds; 0 fails, 3 notes.
- The five files are untouched by main since `cb4e42ce`; the smoke read is the bare `validate`; nothing blocks the build.
- Read-only: reads of git, the card, the hub launch line and `jobs.yaml`; nothing run, nothing written but this report.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --name-only cb4e42ce 6fb73789` vs the card's PORT3 file list | `docs/40 - DevDocs/cobalt/cli.md`, `…/cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py` = the card's 5, no report | OK |
| 2 | `git diff --shortstat cb4e42ce 6fb73789` | `5 files changed, 161 insertions(+), 1 deletion(-)` = the card's 161 / 1 | OK |
| 3 | `git log --oneline cb4e42ce..6fb73789` | the one commit `6fb73789` | OK |
| 4 | `git diff --stat cb4e42ce main -- <the five>` | empty for all five (the drafter's claim holds) | OK |
| 5 | `git diff --name-only 4aa0481d main` (BASE drift) | the card, prompt 894, `cto-2026-10-20.md`, the drafter report: docs only | OK |
| 6 | `git rev-parse --short=8 main` / `HEAD` | `d1b83f5c` / `d1b83f5c`; BASE `4aa0481d` was main at drafting | OK |
| 7 | header: JOB / BRANCH / WORKTREE / REPORT / CHECK REPORT; `git branch --list ops/f16-close-fr3`, `git worktree list` | `f16-close-fr3` · `ops/f16-close-fr3` · `f16-close-fr3` · `…f16-close-fr3-build-2026-10-20.md` · `…f16-close-fr3-check-2026-10-20.md` agree; no such branch or worktree yet | OK |
| 8 | header BAND / TIP | `BAND: HIGH`; `TIP:` empty | OK |
| 9 | `grep -n -F "«FILL"` over the card | no match | OK |
| 10 | `git diff HEAD --stat -- <card>` | empty (committed) | OK |
| 11 | `git grep` of the three `## DEPLOY PROOF` strings on `main` / on `6fb73789` (`-- src`) | main: no hit (before `0`, `0`, `0`); `6fb73789`: `cli.py:347` `Playbook (F23): `, `cli.py:357` `Daily refresh (F4): `, `loader.py:91` `with no consumer (F16)` (after `1`, `1`, `1`) | OK |
| 12 | `main:src/cobalt/cli.py` anchors: `grep -n` `if disabled:` / `These are built and registered` / `# CROSS-CHECK 1` | `:332` / `:337` / `:339` = the card's PORT3 cites | OK |
| 13 | `main:docs/40 - DevDocs/cobalt/cli.md` section headings | last section `## 2026-10-19 — f21-genesis-1013` at `:141` (text `:142`) = the card's | OK |
| 14 | `6fb73789:src/cobalt/taxonomy/loader.py:88` | `keys = [row.key for row in registry.tunables if not any(name.strip() for name in row.consumers)]` (FIX1 line present) | OK |
| 15 | PORT is ONE row: rows of the PORT3 job | one PORT3 row; V1, V2, C1, FIX1, SEAM, PORT, SEAM, PORT2 stated as context, not rebuilt | OK |
| 16 | `grep -n -F -- "--no-db"` over the card | 5 hits: `:33` quotes the refused string, `:35` PORT3 "no --no-db spelling anywhere", `:67` X4 (code-path question), `:73` P8, `:97` RECORDS; all prose, no smoke read | OK |
| 17 | smoke read in `## DEPLOY PROOF` vs the hub launch line `prompts/DEPLOY-HUB.md:11` | card: `COBALT_ENV=production uv run cobalt validate`; launch line admits `Bash(COBALT_ENV=production uv run cobalt validate)`; hub `:75`, `:122`, `:143`, `:155` use the bare read | OK |
| 18 | the card's other reads / markers: `grep -c -F … cli.py` ×2, `loader.py` ×1; suites `uv run pytest *`; `ops/desk/gate-lists.md` `## OFFLINE` | the three greps are `grep` (admitted: `Bash(grep *)`); `uv run pytest *` admitted; `## OFFLINE` = `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`, as the card quotes | OK |
| 19 | K10: card RESTARTS record vs `configs/cobalt/jobs.yaml` (`:39` aset row `reads` tunables.yaml `:69`, `imports` `:99`; radar `imports: [cobalt.cli]` `:203`) and `reports/f16-close-fr2-check-2026-10-19.md:190` | the check's full set: `com.cobalt.aset com.cobalt.cos com.cobalt.radar` (cos not loaded by design, deferred); the card's `## RECORDS` names `com.cobalt.radar` only as class home and defers the full set to the builder's `jobs restarts` line | OK (NOTE 1) |
| 20 | CHECK ASKS: FIX1 tests and the merge-base proof | P6 names both tests (`test_c1_a_row_whose_consumers_are_blank_is_refused`, `test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded`, no `pptx_loaded` skip); P5 and the PORT3 SCOPE line carry `git merge-base main <tip>` → `<hash>` = `git rev-parse main` → `<hash>` | OK |
| 21 | overlap with open cards: F5 731 port (`prompts/2026-10-18/731-f5-card.md` row PORT) and cos probe 877 (`prompts/2026-10-19/877-cos-probe-card.md`) | shared files: `src/cobalt/cli.py` (731: import after `:90`, mount after `:557`, far from `_cmd_validate`; 877: named at `:64`) and `docs/40 - DevDocs/cobalt/cli.md` (731 section; 877 `:27`). No overlap on `taxonomy/loader.py`, `loader.md` or the test file. | OK (NOTE 2) |
| 22 | the three drafter decisions | 1 (469 touched `genesis/cli.md`, not `cli.md`; the diff over the five is empty: check 4): right. 2 (bare `validate` in the builder's worktree may fail on the DB without `.env`; quote as UNPROVEN, the hub's 4.5 run is the proof, no `--no-db`): right. 3 (`## PASS 1` / `## PASS 2` gain `test_genesis_vectors_db.py` from 469; `## OFFLINE` unchanged; with-DB passes stay the deploy gate's): right, `## OFFLINE` read in check 18 | OK |
| 23 | what blocks the card's own build | nothing: 469 is deployed (`0e3d45e6` in the log of `4aa0481d`), no branch or worktree collision, the five files are clean on main | OK |

## ISSUES
- NOTE 1: the card's `## RECORDS` RESTARTS line says the class home of `cli.py` and `loader.py` is `com.cobalt.radar` alone. The last check of the same net change recorded `com.cobalt.aset com.cobalt.cos com.cobalt.radar` (aset reads `tunables.yaml` and imports the loader; cos is not loaded by design). The card defers the full set to the builder's `jobs restarts` line, so it does not block. The check seat should expect aset and radar (cos deferred).
- NOTE 2: shared files with open work: `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` with the F5 731 port and the cos probe 877. F16's hunks are a `_cmd_validate` block and a section at the end of `cli.md`; whichever card lands second re-finds its anchor by content.
- NOTE 3: P8 lists the places that hold `--no-db` as the PORT3 JOB paragraph, X4, P8 and `## RECORDS`; it omits the PORT3 row (`:35`, "no --no-db spelling anywhere"). That hit is a ban, not a read. No edit needed.

PREFLIGHT DONE · card: f16-close-fr3 · checks: 23 · fails: 0 · ready: YES
