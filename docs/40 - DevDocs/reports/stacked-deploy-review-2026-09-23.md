# Stacked Deploy Review — 2026-09-23

## §0 Headline
- 2 of 3 houses answered (Gemini, Opus); Grok TIMEOUT at 15 min with no `REVIEW:` line — the L67 floor (≥1 of Grok/Gemini) is met by Gemini alone.
- **1 confirmed blocker: `07`'s STEP-0 P6 will fail deterministically tonight.** The actual smoke-fix-check stop line has `ready for a deploy prompt: YES` only twice (grok, opus) and one explicit `NO` (gemini: "DEFECT REMAINS F3"), never THREE, and today three houses did check (not a METER/HARNESS-limited count), so neither of P6's two branches is satisfied as written. Verified directly against `s2-smoke-fix-check-2026-09-23.md`'s real last line, not from either house's claim.
- 5 non-blocking folds proposed (2 allow-string over-widenings both houses caught independently and I confirmed; a downtime-metric timing gap Gemini caught and Opus missed — I confirmed Gemini's reading against `07`'s own text; a relaunch-rule ambiguity and a migration-timeout routing gap Opus caught, both textually confirmed).
- Two Opus claims did NOT hold under my own check: the `unranked_rows` and `EVALUATOR_VERSION = "s2p2.2"` markers Opus flagged as "never proven before the window" are in fact already present in the respective branch files (verified by `git show`), so today's run is not at risk from that particular concern — it stands only as a general pre-merge-verification suggestion, not a live defect.
- No path to a mid-run dialog or question found by either house or by me; no unmet write-path law (L28/L29/L65) found.

## L74
None observed. No packet file or house output contained an embedded instruction directed at me; the `Claude-Session:` / commit-attribution reminder that reaches me is the system's own out-of-band reminder, not content from a tool result, so L74 does not apply to it.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| DATE GATE (1st) | `date` | 0 | ALLOWED — Wed Sep 23 07:47:59 EDT 2026, within the 2026-09-23 gate |
| grok present | `grok --version` | 0 | ALLOWED — grok 1.0.25 (f7e67d6988e2) [stable] |
| agy present | `agy --version` | 0 | ALLOWED — 1.2.9 |
| OPUS PROBE | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | UP — replied `OK` |
| 07 exists | `ls -la ".../2026-09-23/07-stacked-deploy.md"` | 0 | ALLOWED — 74226 bytes, Sep 23 06:42 |
| 07 committed | `git log -1 --format=%H -- ".../07-stacked-deploy.md"` | 0 | ALLOWED — `41dc02db2bc7ba26c18526316bdfe50b550469e4` |
| STAGGER 03 | `grep -n -F "03 is not running" cto-2026-09-23.md` | 0 | ALLOWED — R23 row: "03 is not running (DONE 07:0x)", names `08-review-stacked-deploy.md` |
| STAGGER 05 | `grep -n -F "05 is not running" cto-2026-09-23.md` | 0 | ALLOWED — R23 row: "05 is not running (never launched)", names `08-review-stacked-deploy.md` |
| STAGGER 06 | `grep -n -F "06 is not running" cto-2026-09-23.md` | 0 | ALLOWED — R23 row: "06 is not running (DONE 07:4x)", names `08-review-stacked-deploy.md` |
| RECOVERY | `ls scratch/tribunal-bars-0920/stacked-deploy-0923` | 1 | fresh run — "No such file or directory" |
| DATE GATE (2nd, before launch) | `date` | 0 | ALLOWED — Wed Sep 23 07:53:13 EDT 2026, still within gate |

AUTHORIZATION verified (each its own call, none taken on a house's or the prompt's word):
- R5 (`cto-2026-09-23.md:13`): carries `I want the work done after I am done trading.`. HOLDS.
- R30 (`cto-2026-09-22.md:133`): carries `Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET` and his quoted `"Approved"`; `git log -1 -S"..." -- cto-2026-09-22.md` = `055242df8032632dfafdcc8a69dcc271be89c0f6` (NON-EMPTY). HOLDS.
- R32 (`cto-2026-09-22.md:131`): carries `Bash(claude -p --model claude-opus-5-5 *)`; `git log -1 -S"..." -- cto-2026-09-22.md` = `b3f70f8042bef47f27b7aafa2cfe1a9152901a99` (NON-EMPTY). HOLDS.
- R23 (`cto-2026-09-23.md:26`): names `08-review-stacked-deploy.md`; `git log -1 -S"..." -- cto-2026-09-23.md` = `b8a72b5300370e248cd6c7a8a732258fec03e6a0` (NON-EMPTY). HOLDS.
- `grep -n -E "R_[_]"` on `07-stacked-deploy.md` → 11 hits (the desk's unfilled `R__A`/`R__L` placeholders — expected before launch, not a mismatch).

## Packet
Staged in `scratch/tribunal-bars-0920/stacked-deploy-0923/`, Read → Write byte-identical, `wc -c` verified against source for every copy, trailing-whitespace lines disclosed (0 for every staged file except `branches.md`: 2 and `migration.md`: 2 — both present in the source files, not introduced by staging):
- `07-stacked-deploy.part1/2/3.md` — 26109 + 26691 + 21426 = 74226 B = source `07-stacked-deploy.md` (74226 B). Split at lines 124, 248.
- `05-ran.part1/2.md` — 30786 + 33496 = 64282 B = source `2026-09-22/05-stacked-deploy.md` (64282 B). Split at line 200.
- `05-outcome.md` — 33835 B = source `deploy-2026-09-22.md` (33835 B), whole.
- `d3-proven.part1/2.md` — 25016 + 26293 = 51309 B = source `2026-09-19/53-deploy-d3.md` (51309 B). Split at line 54.
- `branches.md`, `stop-lines.md`, `rulings.md`, `laws.md`, `migration.md`, `r119.md`, `restarts.md`, `clock.md`, `greps.txt`, `QUESTIONS.md` — built per spec (1.5)–(1.14), each command's FULL output included.
- `stop-lines.md`: `setups-blind-code-2026-09-23.md` is ABSENT (never launched, per R23's own stagger row); its stop-line SHAPE is quoted from `07`'s P8 text instead, as instructed — not a defect in `07`.
- Every house got the identical packet (L44); QUESTIONS.md named every file and pointed to `greps.txt` second.

## Houses launched
Launched 07:54:58 ET, `date` re-run immediately before launch (07:53:13 ET, still 2026-09-23). All three `run_in_background`, independent, one attempt each.
- **GEMINI** (`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"`): DONE 08:02:54 ET (~8 min). Answered all 7 questions, closed `REVIEW: RUN IT AFTER tightening jobs allowlist to jobs restarts *, tightening validate* to validate, recording <t up> after retries and kickstarts`. Written to `gemini-review.md` byte for byte.
- **OPUS** (`claude -p --model claude-opus-5-5 "…" --permission-mode plan --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`): DONE 08:06:1x ET (~11 min). Answered all 7 questions plus an UNVERIFIABLE list, closed `REVIEW: RUN IT AFTER P6 accepts smoke check's actual 2-YES, HOLD-0 line via R__L; P14 proves both markers ≥1 in the branch worktrees; preflight two-var prefix with read-only taxonomy tunables; relaunch: prior stop line present → FAILED, never re-enter STEP-5; 4.4: incomplete proof table → read-back, then STEP-5`. Written to `opus-review.md` byte for byte.
- **GROK** (`grok -p "…" --sandbox cobalt-job --allow "Write(.../stacked-deploy-0923/**)"`): TIMEOUT. Ran 07:54:58–08:09:58 ET (15 min exactly), stopped with `TaskStop` on task id `b65kvshaa`. Its only output, kept whole: "I'll start with QUESTIONS.md and follow it exactly, then open greps.txt.QUESTIONS.md is the brief and greps.txt is open. Next I'll read the three prompt parts and the law and evidence files they cite." No `grok-review.md` was ever written. No `REVIEW:` line = `NO REVIEW LINE` / `TIMEOUT`.
- **L67 floor**: met — Gemini (a non-author house) answered in full with a `REVIEW:` line. Grok's timeout does not fail the round.

## Per question
| Q | grok | gemini | opus |
|---|---|---|---|
| Q1 Allowlist | TIMEOUT | YES, every command covered; no unused strings; 2 strings wider than needed (`jobs *`, `validate*`) — `gemini-review.md:1` | Every command covered; only untested shape is the two-var taxonomy prefix (first used at 6.1); same 2 strings flagged wider than needed — `opus-review.md` Q1 |
| Q2 L68 gate | TIMEOUT | YES on all four sub-questions; no sequence lands untested code — `gemini-review.md:3` | NO sequence lands untested code; rebase-exclusion and shared-test-file seams both check out — `opus-review.md` Q2 |
| Q3 Residents-down window | TIMEOUT | YES down/up around merge+migration; window can cross 20:00 on a slow migration and STEP-5 permits crossing 21:10/21:40; **downtime claim NOT honest** — `4.6` records `<t up>` before retries/kickstarts — `gemini-review.md:5` | Down/up matches `restarts.md`; "NEVER crossed" (`part1:41`) is not guaranteed on a slow migration, but landing after 20:00 is harmless (L43's own window); **downtime claim is honest** — `opus-review.md` Q3 |
| Q4 Migration/rollback | TIMEOUT | YES 0013 safe, read-back correct, revert is one command and restores production, every failure path bootstraps residents, STEP-5 never entered twice — `gemini-review.md:7` | Mostly sound; two gaps: 4.4 has no explicit route for an incomplete proof table (a timeout after commit); relaunch rule (ii) can send a relaunch into a SECOND STEP-5 after an already-completed one — `opus-review.md` Q4 |
| Q5 Vault write | TIMEOUT | YES lawful under L28/L65; rows fill the engine holes; cannot harm production since `taxonomy load` never runs — `gemini-review.md:9` | Same conclusion; flags one UNVERIFIABLE (whether any resident reads the note without `taxonomy load`) — `opus-review.md` Q5 |
| Q6 Dialog/question paths | TIMEOUT | NO — allowlist covers everything, `--no-edit`/`-m` throughout, no waits — `gemini-review.md:11` | NO interactive editor or wait; residual risk is the same untested two-var prefix from Q1 — `opus-review.md` Q6 |
| Q7 Other | TIMEOUT | None found — `gemini-review.md:13` | **P6 fails deterministically tonight** (2 YES, 1 NO, not 3); markers not preflight-verified before the window; P8 currently blocked (precondition, not a flaw); first post-restart radar cycle risk; tonight's 21:10 replay mostly sees pre-`s2p2.2` receipts — `opus-review.md` Q7 |
| REVIEW | TIMEOUT / NO REVIEW LINE | `RUN IT AFTER` 3 folds | `RUN IT AFTER` 5 folds |

## Checked against the files
Every claim that something CAN happen was checked against the real file, not taken from either house's word (L35).

| claim | who | file:line | verdict | blocks launch? | why |
|---|---|---|---|---|---|
| STEP-0 P6 will fail: actual smoke-fix-check line has 2×YES + 1×NO, never 3×YES, and today isn't a METER/HARNESS-limited count | opus | `s2-smoke-fix-check-2026-09-23.md` last line (checked directly) | **HOLDS — CONFIRMED** | **yes** | Read directly: `grok: … ready for a deploy prompt: YES · gemini: … ready for a deploy prompt: NO · opus: … ready for a deploy prompt: YES · sol: METER — retry after Sep 26th, 2026 6:47 AM · defects that HOLD: 0`. P6 (`07` STEP-0) requires YES×3 AND `defects that HOLD: 0`; the first conjunct fails, and the "fewer than three could check" alternate branch does not apply (three non-Sol houses did check). Neither branch of P6 is satisfied. |
| `<t up>` recorded before the retry/kickstart branches resolve → downtime metric can undercount | gemini | `07-stacked-deploy.md:4.6` ("Then `date` = `<t up>`." precedes the `Bootstrap failed: 5 → retry` and `Loaded but not running → kickstart` bullets) | **HOLDS — CONFIRMED** | no | Read `07`'s STEP-4.6 text directly: `<t up>` is captured immediately after the two bootstrap calls, textually before both recovery branches. Opus's "downtime claim is honest" is the less precise reading on this specific point; Gemini's is correct as written. |
| `unranked_rows` marker (4.7(d)) is unconfirmed / "the smoke fix's own payload key is `unranked`" | opus | `s2/smoke-fix-0922:src/cobalt/replay/models.py` | **DOES NOT HOLD as a live risk today** | no | `git show s2/smoke-fix-0922:src/cobalt/replay/models.py \| grep -c -F "unranked_rows"` = 5. The field exists (line 344 of that blob); `"unranked"` is a *different*, unrelated dict key on `MoversBySideCounts`, not the marker string. The marker WILL be found post-merge. |
| `EVALUATOR_VERSION = "s2p2.2"` marker (4.7(d)) is unconfirmed | opus | `setups/seven-0921:src/cobalt/radar/evaluate.py` | **DOES NOT HOLD as a live risk today** | no | `git show setups/seven-0921:... \| grep -c -F 'EVALUATOR_VERSION = "s2p2.2"'` = 1. Present exactly once, as expected. |
| STEP-1.3's nine excluded paths fully capture main's non-docs movement since the setups cut | (my own check, not a house claim) | `git -C /Users/cobalt/cobalt log --stat --oneline 5b208a0..main -- . ':(exclude)docs'` | **HOLDS — CONFIRMED** | no | The nine paths touched are exactly `.gitignore`, `configs/cobalt/backup.yaml`, `configs/cobalt/jobs.yaml`, `configs/cobalt/rules.yaml`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_backup.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py` — an exact match to `07`'s own STEP-1.3 exclusion list, and to its line-30 claim. `6f4da5e..main -- . ':(exclude)docs'` (the smoke-fix cut) printed nothing, confirming "expected: none". |
| All 54 allow strings on `07`'s launch line are accounted for exactly as `07` claims (16 new / 0-0 in both precedents; 38 carried / ≥1 in at least one) | (my own check) | `07-stacked-deploy.md:6` vs `2026-09-22/05-stacked-deploy.md` and `2026-09-19/53-deploy-d3.md`, full substring count per string | **HOLDS — CONFIRMED** | no | All 16 strings `07` names NEW are 0/0 in both precedent files. All 38 strings `07` claims carried are ≥1 in at least one, with exactly the 6 named strings (`db migrate --proof-only` (dev), `backup run*`, `backup status*`, `db migrate --allow-prod --proof-only`, `db migrate --allow-prod`, `db query *`) present only in `53`, absent from `05` — matching `07`'s own bookkeeping exactly. |
| `Bash(COBALT_ENV=production uv run cobalt jobs *)` is wider than any step needs | gemini, opus | `07-stacked-deploy.md` STEP-2.5, STEP-4.7(f) | **HOLDS — CONFIRMED** | no | Both invocations in `07`'s own text are `jobs restarts <sha>..<sha>`; no other `jobs` subcommand is ever called, and line 1 explicitly forbids `jobs register`. The allow string as written would also permit `jobs register` etc. |
| `Bash(COBALT_ENV=production uv run cobalt validate*)` is wider than any step needs | gemini, opus | `07-stacked-deploy.md` STEP-2.3(d2), STEP-4.5, STEP-4.7(f) | **HOLDS — CONFIRMED** | no | Every call in `07`'s own text is bare `cobalt validate`, no arguments, in all three places it is invoked. |
| Relaunch rule (ii) cannot distinguish a completed, successful STEP-5 revert from an interrupted one, and could re-enter STEP-5 a second time | opus | `07-stacked-deploy.md` STEP-3.5 RELAUNCH RULE (ii) | **HOLDS — CONFIRMED (textual gap)** | no | Rule (ii) triggers on "main is neither `<pre-merge>` nor the gate tip AND `<pre-merge>` was recorded" — which is also exactly true right after a *successful* revert (main's new HEAD is the revert commit, a third sha). The rule does not check the report's own last non-blank line for a prior `FAILED: STEP-5` stop before deciding a revert was "interrupted". |
| STEP-4.4 has no explicit routing for an incomplete/missing proof table (e.g., a tool timeout after the migration committed) distinct from "non-zero exit / CHANGED / CREATED → STEP-5" | opus | `07-stacked-deploy.md` STEP-4.4, vs `2026-09-19/53-deploy-d3.md` §8 (per `d3-proven.md`) | **HOLDS — plausible ambiguity, not a hard defect** | no | `07`'s text says the read-back "decides `migrations applied: yes/no`" on any incomplete output but does not state a step number for that branch the way `53`'s "then go to §8" did. The general instruction likely covers it in spirit but the routing is less explicit than the precedent. |
| P8 (setups blind-code seat) currently blocks `07` from running tonight | (my own check, per stop-lines.md) | `docs/40 - DevDocs/reports/setups-blind-code-2026-09-23.md` — absent | **HOLDS — CONFIRMED, but not a defect in `07`** | n/a | `07`'s own P8 correctly requires this report; it is genuinely absent today (never launched, per the R23 stagger row read earlier). This is a precondition not yet met, not something to fold into `07`'s text. |
| No path to a mid-run dialog or question | gemini, opus | `07-stacked-deploy.md` (all merges/reverts, no waits) | **HOLDS — CONFIRMED** | no | Every merge/revert call in the text carries `--no-edit` or `-m`; every rebase is non-interactive; there is no sleep/wait command anywhere in the file (confirmed via `greps.txt`'s own search). |
| Migration 0013 is safe if code is reverted while 0013 stays applied | gemini, opus | `migration.md` (0013 SQL + rollback SQL) | **HOLDS — CONFIRMED** | no | The forward migration only drops a NOT NULL constraint (additive); the reverse migration refuses atomically while any NULL-slug row exists. Pre-deploy code never writes a NULL slug, so a code revert with 0013 applied is safe by construction. |
| STEP-6 rows validate and fill the engine holes | gemini, opus | `r119.md` (`_fills_hole`, engine rows at `tunables.yaml:393-418`) | **HOLDS — CONFIRMED** | no | Read the engine rows directly: `flat_threshold.ema9`/`flat_threshold.vwap`/`dist.k.vwap` are `value: null` with the exact scope/unit the STEP-6.2 rows file supplies, and `source: assumed` satisfies `_fills_hole`'s condition. `leg.min_size_atr` also reads `value: null` and correctly gets no row (per R119's ruling). |

## Folds proposed
1. **STEP-0 P6** (blocker): `carries `ready for a deploy prompt: YES` at least THREE times and `defects that HOLD: 0`` → also accept a check whose last line carries `defects that HOLD: 0` even when one house's individual `ready` answer is NO, provided the desk's R__L row names and accepts that specific line by quote.
2. **STEP-4.6**: `Then `date` = `<t up>`.` (placed before the retry/kickstart branches) → move the `<t up>` capture to immediately after the `Bootstrap failed: 5` retry and the `kickstart` branches resolve, so the downtime figure reflects confirmed-up time, not first-attempt time.
3. **STEP-3.5 RELAUNCH RULE (ii)**: `Main is neither `<pre-merge>` nor the gate tip AND `<pre-merge>` is a value this report already recorded … Go to STEP-5 (2) at once` → first check the report's own last non-blank line for an already-written `FAILED: STEP-5` stop; if present, do not re-enter STEP-5 — end `FAILED: relaunch — STEP-5 already completed; the desk decides`.
4. **STEP-4.4**: `A non-zero exit, a CHANGED, or a CREATED → STEP-5` → add `an incomplete or missing proof table (including a tool timeout) → the read-back decides applied yes/no, then STEP-5` (matching `53`'s "then go to §8" shape).
5. **`07`'s launch line**: `Bash(COBALT_ENV=production uv run cobalt jobs *)` → `Bash(COBALT_ENV=production uv run cobalt jobs restarts *)`.
6. **`07`'s launch line**: `Bash(COBALT_ENV=production uv run cobalt validate*)` → `Bash(COBALT_ENV=production uv run cobalt validate)`.

## ESCALATE
- `ASK DESK: fold 1 (P6) is the only one that changes whether tonight's run can start at all — the other five are safe to fold or defer without affecting tonight [as of 2026-09-23 08:10 ET]`.
- `ASK DESK: Opus's Q5 UNVERIFIABLE item — whether any resident reads "Assumed Defaults.md" without the desk's own `taxonomy load` — is worth a direct grep before tonight, even though nothing in `07` triggers it: `grep -rn "load_vault_trade_defs\|load_assumed_tunables" /Users/cobalt/cobalt-wt/setups-c1/src/cobalt` [as of 2026-09-23 08:10 ET]`.
- Grok TIMEOUT at 15:00 with no `REVIEW:` line — recorded as `NO REVIEW LINE` / `TIMEOUT`; does not fail the round (L67 floor met by Gemini).
- P8 (`setups-blind-code-2026-09-23.md`) is absent today — a precondition for `07` to run at all, unrelated to any fold above.

STACKED DEPLOY REVIEW DONE · houses: 2 of 3 · other houses: 1 of 2 · blockers: 1 · folds: 6
