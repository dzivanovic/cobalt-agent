# f5-x3-measure preflight — card 945 — 2026-10-20 (18:07 EDT)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 main` | `de8e7395`; BASE `5347f90e` trails by desk commits only; TIP empty | OK |
| 2 | `git diff HEAD --stat -- <card 945>` | empty (card committed) | OK |
| 3 | header: JOB, CLASS K2, INSTALL none, BAND HIGH, RESTARTS none, REPORT/CHECK REPORT paths, LADDER OFF-LADDER to R2217 | all present; R2217 row exists in `cto-2026-10-20.md:22` (DESK RECORD, brain L79) | OK |
| 4 | RULINGS `2026-10-18 R1863` | `cto-2026-10-18.md:90` `HIS RULING · APPROVED` | OK |
| 5 | `modelaccess.yaml` at main: route `:70`, `timeout_s: 60` `:78`, `max_output_tokens: 512` `:80`, `source: UNMEASURED` comments | match | OK |
| 6 | `prefill.yaml:38-39` | `route: checkpoint.narrative`, `narrative_max_lines: 3` | OK |
| 7 | `checkpoints.py` refs: `WRITER:91`, `parse_groups:200`, `compute_delta:283-323`, `_response_schema:394`, `_SYSTEM:405`, `narrate:413-439` | match | OK |
| 8 | `client.py` / `config.py`: `call_sync:89`, lowering rule `:99-106`, `think_leak:73/79/83`, `empty:85`, `output_tokens:159`, `load_routes:150`, `ModelAccessConfig:132` | match | OK |
| 9 | `test_checkpoints_offline.py:393-394` `IDX_0745` / `IDX_0815`; `groups_csv:65`, `ENTRIES:470` | match | OK |
| 10 | fixture line count: `git grep -c "" main -- …/groups_sector_v140.csv` | **13** (marker, header, 11 rows); card READ says "12 lines at BASE" | FAIL |
| 11 | F5-FINAL `:177` (X3), `:88`, `:138` | match the card's quotes | OK |
| 12 | BUILD-HUB `:14`/`:16`: `uv run pytest *`, `uv run cobalt jobs restarts *`, `git diff *`, `git status*`, `ls *`, `date*`, `sh …/ops/desk/*` | every command the card gives the builder is on the list; no `python`, `cat`, `mkdir`, `rm`, `curl` | OK |
| 13 | DECISION 1, WHO writes the script | card: "THE DESK stages … written from this card's R1". The drafter wrote no script (draft report: none); R1 describes the script but does not contain it. So it is neither a drafter-written file nor part of the RUN row's text. The desk writes no code (R236 spirit) | FAIL |
| 14 | DECISION 1, does the BUILD line admit running it | yes: `uv run pytest /tmp/f5-x3-measure-run/test_x3_calls.py` matches `Bash(uv run pytest *)`; `/tmp/<job>-run/` is the staging path `BUILD-HUB.md:72` names; `ls /tmp/…` matches `ls *`. Builder has no `rm`/`mkdir`, so the self-removing script is the only /tmp clean-up | OK |
| 15 | lifted timeout restored: config copy in process, no yaml edit; `git status*` and `git diff *--stat` admitted for C1; ROWS say NO config/src/plist/DB change | no file left changed | OK |
| 16 | time gate checkable with `date*` (admitted); stop lines `FAILED: X3 — outside…`, `window closed after <n> of 30`, `X3 DONE · …` form | present, checkable | OK |
| 17 | values rule in RECORDS (`VALUES CARD RULE`) and V1 | present, same formula, `# source:` text, HELD rule | OK |
| 18 | RESTARTS `none` (docs only) | consistent with card 912 precedent | OK |

## ISSUES
- FAIL 10: fix READ line `groups_sector_v140.csv` to "13 lines at BASE (line 1 marker, line 2 header, 11 rows)".
- FAIL 13: nobody sanctioned writes the calls script. Fix, either: (a) a drafter writes `test_x3_calls.py` and the card embeds or cites it, and the desk only copies it byte for byte to `/tmp/f5-x3-measure-run/`; or (b) drop the staging: the builder writes the RUN row's test itself in the worktree (`BUILD-HUB.md:70` "Write … each RUN row's test"), runs it `uv run pytest -q -rP …`, and removes it with `sh /Users/cobalt/cobalt/ops/desk/scratch-clean.sh` (`:72`). (b) needs no desk code and fits the admitted strings, but its PLACEMENT tests and "no file under the worktree at the tip" (X1) must still hold, so the card should name the path and say it is deleted before commit.
- NOTE: the probe may run long (30 calls, up to 300 s each); the builder's Bash call max is 600 s foreground, so the card should say how the run is kept alive (background, or the test is expected to finish in minutes; pytest is run once).
- NOTE: the builder must start at or after 20:35 ET; the desk should launch the build after that (now 18:07). Not a block.
- NOTE: the figures dict shape for `compute_delta` is not stated in R1 (the script author reads `test_checkpoints_offline.py` `figures()`); fine for a builder, not for a desk-staged copy.
- Blocks the card's own build: FAIL 13 only (no script has an author). The time gate is not a block.

PREFLIGHT DONE · card: f5-x3-measure · checks: 18 · fails: 2 · ready: NO
