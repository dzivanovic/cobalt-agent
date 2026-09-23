# DevDB Repair RE-ISSUE Review — 2026-09-23

## §0 Headline
- One-round read of `68-devdb-repair.md` as re-issued (`9857c30`, 2026-09-22 22:18 ET) before it runs today.
- Authorization verified: R4(c), R122's condition, R127, R30 (grok/agy through 2026-09-23 23:59 ET), R10 (this launch row).
- Date gate: 2026-09-23 — R30 covers today.
- Status: PREFLIGHT clear, staging packet next.
- (details below)

## L74
(none encountered yet)

## AUTHORIZATION
- R4 row (`cto-2026-09-23.md:12`): carries `Everything waiting for me is approved.` and `R122's condition` — CONFIRMED.
- R122's condition commit: `e3be48156bb8534d947dc80eaef361f8b57d380a` — NON-EMPTY, CONFIRMED.
- R127 row (`cto-2026-09-22.md:38`): carries `pg_database_size(current_database())` and `Gemini read` — CONFIRMED.
- R30 row (`cto-2026-09-22.md:133`): carries `Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET` with `"Approved"` — CONFIRMED. SHA `055242df8032632dfafdcc8a69dcc271be89c0f6` NON-EMPTY.
- R10 row (`cto-2026-09-23.md:18`): names `03-review-devdb-repair.md`, DESK LAUNCH ROW filled (not `__`). SHA `dfc09cfe81c8a10cf6fc6a6fe09bd436dc54f92e` (commit `docs(desk): 09-23 R7-R10 day-lane prompts 03/05/06, open-items drafter, 03 launch row`, touches `cto-2026-09-23.md`) — CONFIRMED, desk file only.
- No mismatch found.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| date gate | `date` | 0 | allowed — 2026-09-23 06:43 ET, R30 covers today |
| grok version | `grok --version` | 0 | allowed — grok 1.0.25 (f7e67d6988e2) [stable] |
| agy version | `agy --version` | 0 | allowed — 1.2.8 |
| prompt exists | `ls -la ".../68-devdb-repair.md"` | 0 | allowed — 22054 bytes, Sep 22 22:18 |
| re-issue committed | `git log --oneline -- 68-devdb-repair.md` | 0 | allowed — newest `9857c30` (R126-R127 re-issue) above `4830d80` (R124 launch row) above `e40f961` (73's read version); no newer commit |
| 68 has not run again | `tail -n 3 devdb-repair-2026-09-22.md` | 0 | allowed — last non-blank line starts `FAILED: PREFLIGHT Q3` |
| Q3 size probe literal (record only) | `grep -c -F "Q3 size probe"` on cto-2026-09-22.md and cto-2026-09-23.md | 1/1 (0 matches each) | allowed — both 0, expected (desk writes on 68's own launch row), not a blocker here |
| stagger s1/s2/s3 | `ls` on setups-blind-code-2026-09-23.md, s2-smoke-fix-check-2026-09-23.md, stacked-deploy-review-2026-09-23.md | 1/1/1 | allowed — none exist; R10 row (`cto-2026-09-23.md:18`) prints "05 is not running · 06 is not running · 08 is not running" naming `03-review-devdb-repair.md` |
| stagger s4 | `grep -n -F "no other house hub is running"` on cto-2026-09-23.md | 0 | allowed — same R10 row, same line naming `03-review-devdb-repair.md` |
| recovery check | `ls scratch/tribunal-bars-0920/devdb-repair-0923` | 1 (No such file or directory) | allowed — fresh run, no recovery |

## Packet
Staged in `scratch/tribunal-bars-0920/devdb-repair-0923/` (worktree `/Users/cobalt/cobalt-wt/agy-trial`), Read → Write byte-identical, each ≤ 38,000 B:
- `68-devdb-repair.md` (22054 B, matches source) — the prompt WHOLE as committed at `9857c30`. Working tree has zero drift from `9857c30` (`git diff`/`status --porcelain` on the path: empty).
- `reissue-diff.md` (word-diff `e40f961..9857c30`, run `run_in_background`, harness-saved output read then Written). `grep -c "^commit "` = 2, matching PREFLIGHT's git log count above `e40f961`.
- `failed-run.md` (10517 B, matches source) — secret-scan `grep -c -i "password\|postgresql://\|POSTGRES_PASSWORD"` = 0 before staging.
- `drafter.md` (8200 B, matches source).
- `code.md` — six excerpts: `env.py` whole, `devdb.py` whole, `db_query.py:98-178`, `test_tenancy.py:659-711`, `db.py` `apply_side` (202-226), `db.py` NOINHERIT docstring block (30-69).
- `rulings.md` — verbatim rows R110/R122/R125/R127/R30 (cto-2026-09-22.md) + R4 (cto-2026-09-23.md).
- `greps.txt` — 73 §1(5)'s twelve searches re-run against `<staged 68>` + source, plus this read's own required searches (pg_database_size, D0, Q3 size probe, R__/R124, dated names, R4(c) quote, SET ROLE/NOINHERIT/GRANT CONNECT/pg_read_all_stats). No password/DSN/`.env` content staged; long outputs replaced by counts and line lists, named as such.
- `QUESTIONS.md` — verbatim + the "Files in this folder" paragraph naming `reissue-diff.md` SECOND, `greps.txt` THIRD.
Second date gate (immediately before house launch): `date` → Wed Sep 23 06:56:36 EDT 2026 — still 2026-09-23, R30 covers it.

## Launch the houses
- GROK: launched 06:58:08 ET. `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" "You are GROK. The folder is scratch/tribunal-bars-0920/devdb-repair-0923/. Start with QUESTIONS.md and follow it exactly. Open reissue-diff.md SECOND and greps.txt THIRD."` — FAILED immediately (exit 1), completion noticed 06:58:26 ET. Output verbatim: `Error: Operation not permitted (os error 1)`. Recorded as HARNESS, not looped (ONE attempt per house, L67 needs only one answering).
- GEMINI: launched 06:58:30 ET, `run_in_background`, independent of GROK's failure. Command: `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"` (the GEMINI sentence per `73`'s §2 spelling, folder `devdb-repair-0923`). Awaiting completion.

- GEMINI completed 07:01:36 ET (launched 06:58:30 ET, well under the 20-min TIMEOUT). Full text kept whole in `## Per question` / `## ESCALATE` below.

## CONTINUE
next: none — collation and file-check complete, report closed below.

## Per question
| Q | grok | gemini |
|---|---|---|
| Q1 | NO REVIEW LINE (HARNESS: `Error: Operation not permitted (os error 1)`, exit 1) | `ONLY D0` — `reissue-diff.md:14` adds only the D0 launch-line string and resets the R124→R__ placeholder; no other allow/deny/`--model`/`--permission-mode`/`--add-dir` string changed. D0's unescaped string = the owner-approved string (`rulings.md`, `greps.txt`). `RUN IT` |
| Q2 | NO REVIEW LINE | `SAFE AND MATCHES` — D0 targets `cobalt_dev` directly via `-d`, prints one integer, `ON_ERROR_STOP=1`; D1's proven exit-0 shape (`failed-run.md:33`) shows the same `docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d cobalt_dev …'` pattern reaches the server. `RUN IT` |
| Q3 | NO REVIEW LINE | `RUNS` — `to_regclass` on a missing/unusable schema is `UNVERIFIABLE FROM READS from the packet alone`; Q3 no longer runs a database-level privilege check (`drafter.md`), so it cannot fail Q3's OLD way. A false `has_head` in PROOF triggers step 4's rollback (68-devdb-repair.md step 4). `RUN IT` |
| Q4 | NO REVIEW LINE | (a) `OK` — R122's approved strings hold; the first Write overwrites `devdb-repair-2026-09-22.md` byte for byte, and its `## CONTINUE` safely re-starts from AUTHORIZATION. (b) `FAILS` — the launch-row AUTHORIZATION bullet (`grep -n "68-devdb-repair.md"`) already matches yesterday's committed R124 row, so it can pass without a NEW today's row. (c) `OK` — lane free, HEAD `0011` matches. (d) `OK`. `RUN IT AFTER [STRING] change grep "68-devdb-repair.md" to "devdb-repair-0923"` |
| Q5 | NO REVIEW LINE | `NO` — every COMMANDS-list command (R0–R10, Q1–Q3, D0–D7, T1–T2) is covered by an exact or wildcarded allow string. `RUN IT` |
| ALSO | NO REVIEW LINE | 8 unused/wider strings named (below) |

## Checked against the files
| claim | who | file:line | verdict | blocks launch? | why |
|---|---|---|---|---|---|
| Q1 ONLY D0, no other launch string changed | gemini | `reissue-diff.md` (both commits, full word-diff) | HOLDS | no | Independently confirmed by my own read of the two-commit diff before staging: the only content changes are the D0 allow string insertion (between D2's and D3's strings), the R124↔R__ prose placeholder (SEAT text, not a command/flag), the Q3 typed-SQL shrink (stays under the pre-approved `db query … *` wildcard), the D3 gate re-point, step-1 ordering, and ESCALATE wording. |
| D0's typed string = R4(c)'s quoted string, character for character | gemini | `68-devdb-repair.md:28` vs `cto-2026-09-23.md:12` | HOLDS | no | Verified myself: both read `docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d cobalt_dev -v ON_ERROR_STOP=1 -Atc "SELECT pg_database_size(current_database())"'`, identical. D0 = R4(c): yes. |
| Q2 D1's proven shape implies D0 reaches the server | gemini | `failed-run.md:33` | HOLDS | no | D1 ran exit 0 with the identical `docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d cobalt_dev …'` structural shape (same container, same `-d cobalt_dev`, same `-v ON_ERROR_STOP=1 -Atc` flags) — only the SQL text and target differ. Reasonable inference, not a re-run; still UNPROVEN until D0 itself executes (L70). |
| Q3 to_regclass-on-missing-schema behavior | gemini | (no packet file states Postgres's own semantics) | UNVERIFIABLE FROM READS | no | Correctly self-labeled by gemini; no packet file documents `to_regclass` return semantics. Not a defect (L70). |
| Q4(b): launch-row gate can match a stale prior-day row | gemini | `cto-2026-09-22.md:41` (R124, committed, already names `68-devdb-repair.md`) | HOLDS | no | Confirmed: `grep -n "68-devdb-repair.md" cto-2026-09-22.md` matches R124 (22:1x ET, yesterday) right now, independent of any new row today. This is a real, pre-existing gap — already named in `drafter.md` ESCALATE 4 ("The launch-row gate is ambiguous… The desk may want a distinct literal") and already covered by R4(c)'s plan to write `68`'s launch row with the `Q3 size probe` literal plus his approve words. Not new to this re-issue. |
| Q4(b)'s proposed fold: `[STRING]` change `grep "68-devdb-repair.md"` → `grep "devdb-repair-0923"` | gemini | (no file — this is a suggested edit to `68`'s own AUTHORIZATION text) | DOES NOT HOLD | no | `devdb-repair-0923` is THIS review's own `--remote-control` seat name (this file's own header line), not a string that would ever appear on a desk report row for `68`'s launch. Grepping for it would never match anything and would make the gate fail-closed always, not fail-open. It is also mistagged: changing `68`'s own body text (not an allow/deny/`--model`/`--permission-mode`/`--add-dir` string) is a `[TEXT]` fold requiring a full re-issue (L19), never a `[STRING]` fold. The underlying concern (row above) survives; this specific replacement string does not. |
| Q5 no uncovered command | gemini | `68-devdb-repair.md` COMMANDS list vs launch line | HOLDS | no | Verified myself: every `docker exec cobalt_memory sh -c '…'` COMMANDS row (D0/D1/D2/D4/R7/D7/R8) has its own exact-match allow string (8 total `docker exec cobalt_memory sh -c` lines in the file: 1 launch-line + 7 COMMAND rows, 1:1). Bare-flag `docker exec cobalt_memory` commands (D3, D5, D6, R10) each have their own exact allow string too. No wildcard gap found. |
| `Bash(tail *)` UNUSED | gemini | `68-devdb-repair.md` (launch line + D6) | HOLDS | no | D6 runs `docker exec cobalt_memory tail -n 3 …`, which does not start with `tail` so `Bash(tail *)` never matches it; D6 is covered by its own distinct `Bash(docker exec cobalt_memory tail -n 3 /tmp/cobalt_dev-0922.sql)` string instead. No COMMANDS-list command is a bare `tail …`. |
| `Bash(git -C /Users/cobalt/cobalt show*)` UNUSED | gemini | `68-devdb-repair.md` COMMANDS list | HOLDS | no | No `git show` command appears anywhere in R0–R10/Q1–Q3/D0–D7/T1–T2. |
| `Bash(ls *)`, `Bash(grep *)`, `Bash(git -C /Users/cobalt/cobalt log*)`, `Bash(date*)`, the two `uv run … *)` wildcards — WIDER than their step needs | gemini | `68-devdb-repair.md` (R0, R1, R3/AUTH, R4, T1/T2, Q1–Q3) | HOLDS | no | Each does cover its named step(s) but is a wildcard broader than that one command; unchanged from the prior read (per `QUESTIONS.md`'s own note: "the previous read found eight such; they stood without a fold" — same count, same strings, not new to this re-issue). `COBALT_ENV=dev uv run cobalt db query … *`'s risk is bounded by `db_query.py`'s own `guard_select()` (SELECT/WITH-only, no multiple statements, refused functions) — code-level, not allowlist-level. |

## Folds proposed
- `[ROW]`: the desk's NEW launch row for `68` should carry a literal distinct from R124's plain filename mention — already planned (R4(c): the `Q3 size probe` literal + his approve words) and already named in `drafter.md` ESCALATE 4. No text change to `68` itself is needed for this; DOES NOT hold as a `[STRING]` or `[TEXT]` fold.

## String changes
none

## Blockers
none

## ESCALATE
- GROK: HARNESS — `grok --sandbox cobalt-job --allow "Write(…)" "<prompt>"` failed immediately with `Error: Operation not permitted (os error 1)` (exit 1), 06:58:08–06:58:26 ET. Not retried (ONE attempt per house; L67's floor is met by GEMINI alone).
- `[ROW]` (repeated from `drafter.md` ESCALATE 4, independently reconfirmed by GEMINI): when the desk writes `68`'s launch row today, it should carry a literal that cannot already be satisfied by yesterday's committed R124 row (e.g., a distinct string beyond the bare filename) — the AUTHORIZATION bullet that checks `grep -n "68-devdb-repair.md"` alone would otherwise pass on R124 without today's new row existing. Not a blocker today because `68`'s separate D0/"Q3 size probe" AUTHORIZATION bullet independently requires a NEW committed row (currently 0/0 — PREFLIGHT), which the desk must write regardless.
- No `ASK DESK` was raised by GEMINI or by this seat.
- No L74 block arrived in this run.

DEVDB REPAIR RE-ISSUE REVIEWED · grok: HARNESS (Error: Operation not permitted, os error 1) · gemini: REVIEW: RUN IT AFTER [STRING] change grep "68-devdb-repair.md" to "devdb-repair-0923" (fold DOES NOT HOLD on file-check — see ## Checked against the files) · blockers: 0 · string changes: 0 · ESCALATE: 2
