# Setups fixture cut — drafter report (2026-09-22, 09:56 ET)

Drafter `setups-fixture-cut-draft-0922` (Opus 5). Reads only; three files written with the Write tool; nothing launched, no DB, no git write.

## §0 DIGEST
- **Files written:** `prompts/2026-09-22/12-setups-fixture-cut.md` (the cut job, Sonnet 5, auto mode, worktree `setups-c1` at `60ddac4`) · `prompts/2026-09-22/13-setups-blind-values.md` (the blind seat, Sonnet 5 hub, cwd `~/cobalt-wt/agy-trial`) · this report. Both carry `R__` launch rows for the desk to fill in.
- **Production reads (READ only):** (1) `COBALT_ENV=production uv run cobalt db query --side system --prod …`, **NEW** string (the precedented `… db query *` narrowed). Runs from `~/cobalt` on main's code, as the P2 cut did (`01-p2-build.md:15-17`): the candidate-day list, the raw bars, the membership rows. (2) `COBALT_ENV=production uv run cobalt radar evaluate --replay *` is a **precedented** string (09-18 `10` / `19`, 09-19 `02`) in a **NEW USE**. It runs from the `setups-c1` worktree because the seven-setups evaluator exists only on the branch.
- **`.env`:** only `/Users/cobalt/cobalt-wt/setups-c1/.env`, through R41's two strings, which were approved for `cobalt_dev` tests. `12` also uses the copy for the production replay, and that NEW USE needs his approve (L41 / L61).
- **Non-production NEW strings in `12`:** the `ln -s` of production's `data/radar-cache` into the worktree and its `rm`, plus `uv run python tests/fixtures/radar/_cut_setups_fixtures.py *`.
- **Blind house:** the primary is **Gemini** (`agy`, R39), because it is a house other than the build's author (L67). The fallback is **Opus 5** (`claude -p`, R49), which has no calendar limit but is the same house as the builder, so `13` records it as "blind but same-house". `13` adds NO new string.
- **`DEF_WRITTEN_*` the seat must not see:** the table under `## KEEP OUT OF 13`. It lists 17 constants across 4 files, the future `_CUT_*` constants, and 4 files that quote them.
- **ESCALATE: 9.** The main ones: (1) hitchhiker is expected to fail a production replay on every day, because production's assumed holes are null. (2) Rubberband has ONE real candidate day, because the daily cache exists only for 09-21 and 09-22.

## FACTS READ (each a file:line or a tool output)
| # | fact | source |
|---|---|---|
| F1 | `--replay` takes its definitions from `TradeDefStore().loaded_for_evaluation`, which is `SELECT slug, md5, def FROM trade_defs` on `Side.USER`. That means production's synced notes, not the build's neutral shapes. | `setups-c1/src/cobalt/radar/evaluate_cli.py:415-419`; `src/cobalt/taxonomy/store.py:71,114-132` |
| F2 | The replay reads daily bars ONLY from `CachedDailyBars(Path(config.cache.dir))`, with `dir: data/radar-cache` relative to the cwd. It never fetches. | `evaluate_cli.py:414,244-256`; `configs/cobalt/radar.yaml:30-31` |
| F3 | An avoid that is unknown gives `input_stale` (when the cause is `no_daily_bars`) or `not_formed`, never `formed`. | `setups-c1/src/cobalt/radar/evaluate.py:1072-1076` |
| F4 | Production cache daily files per day: 09-15 0 · 09-16 0 · 09-17 0 · 09-18 0 · **09-21 116** · 09-22 110 (today). The `setups-c1` worktree has no `data/`. | `ls` outputs, 09:49 ET |
| F5 | Build ESCALATE (ix): "until it is written every numeric assumed hole is null, so only rubberband (convention `A-01` alone) can form in production" | `setups-one-build-2026-09-21.md` (prompt `65` line 120 asks for it) |
| F6 | `--expect-formed` gives `SystemExit` "formed 0 times … RED". An unknown slug gives `SystemExit` "no loaded trade_def …; loaded: […]". | `evaluate_cli.py:236-240,128-133` |
| F7 | The P2 precedent re-dates to one synthetic day, keeps tickers, trims daily bars to 40 rows, and reads raw input by path. Its raw reads ran from `~/cobalt` with `--prod --format json --limit 20000`. | `tests/fixtures/radar/_cut_p2_fixtures.py`; `prompts/2026-09-16/01-p2-build.md:15-21` |
| F8 | No prompt dated 09-2x carries a `cobalt db query --side system --prod` allow string. The `--prod` precedents are 09-16 through 09-19. | the index card's grep, run 09:48 ET |
| F9 | `Formation.anchor: Anchor \| None` exists (FINAL §2.4). The replay's FORMED line prints no anchor, so `12` takes the anchor from a printing pytest. | `evaluate.py:561-582`; `evaluate_cli.py:217-221` |

## KEEP OUT OF 13 — `DEF_WRITTEN_*` and every file that quotes them
| file (in `/Users/cobalt/cobalt-wt/setups-c1/`) | lines | constants |
|---|---|---|
| `tests/cobalt/test_rubberband_forms.py` | :56 · :58 · :60 · :62 · :64 | `DEF_WRITTEN_RUBBERBAND_FORMED_BAR` · `_SIDE` · `_TRIGGER` · `_STOP` · `_LAST` |
| `tests/cobalt/test_setups_nine_ema.py` | :221 · :223 · :225 · :227 | `DEF_WRITTEN_NINE_EMA_SCALP_SIDE` · `_FORMED_BAR` · `_TRIGGER` · `_STOP` |
| `tests/cobalt/test_setups_vwap_cont.py` | :203 · :205 · :207 · :209 | `DEF_WRITTEN_VWAP_CONTINUATION_SIDE` · `_FORMED_BAR` · `_TRIGGER` · `_STOP` |
| `tests/cobalt/test_setups_second_chance.py` | :198 · :200 · :202 · :204 | `DEF_WRITTEN_SECOND_CHANCE_SIDE` · `_FORMED_BAR` · `_TRIGGER` · `_STOP` |
| `tests/cobalt/test_setups_fixture_cut.py` (made by `12`) | named in the cut report's `## FOR 13` | `DEF_WRITTEN_<SLUG>_CUT_SIDE` · `_FORMED_BAR` · `_TRIGGER` · `_STOP` · `_ANCHOR` |
| files that quote or hint at them | whole file unless a range is given | `docs/40 - DevDocs/reports/setups-one-build-2026-09-21.md` · `prompts/2026-09-21/65-setups-one-build.md` · `56-setups-c1-build.md` · `tests/cobalt/setups_shapes.py:40-42` (the committed day's formation bar) · `tests/cobalt/test_setups_lego.py` · `tests/cobalt/test_setups_hitchhiker.py` · the cut report's `## FIND` / `## CUT` / `## PIN` |

Hitchhiker has no `DEF_WRITTEN_*` today: it is pinned, not written. `13` enforces this list with `grep -c "DEF_WRITTEN_\|formed_bar_ts =\|FORMED "` = 0 on every staged file, and with the T1 < T2 ≤ T3 order proof.

## RULE PROOF
**`12` — 24 allow strings · 3 deny · `--add-dir` triplet**
| string | status |
|---|---|
| `"Bash(uv run pytest *)"` · `"Bash(uv run cobalt jobs restarts *)"` · `"Bash(git add *)"` · `"Bash(git commit *)"` · `"Bash(git diff *)"` · `"Bash(git status*)"` · `"Bash(git log*)"` · `"Bash(git show*)"` · `"Bash(git -C /Users/cobalt/cobalt log*)"` · `"Bash(cd *)"` · `"Bash(mkdir -p *)"` · `"Bash(ls *)"` · `"Bash(grep *)"` · `"Bash(tail *)"` · `"Bash(wc *)"` · `"Bash(date*)"` | PRECEDENTED: `65`'s line, from his 09-20 R25 |
| `"Bash(COBALT_ENV=dev uv run pytest *)"` | PRECEDENTED: `65`, from 09-19 R18 |
| `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)"` · `"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)"` | PRECEDENTED: `65`, from 09-21 R41. The copy now also serves the production replay, a NEW USE (ESCALATE 4) |
| `"Bash(COBALT_ENV=production uv run cobalt db query --side system --prod *)"` | **NEW** string: a narrowing of `"Bash(COBALT_ENV=production uv run cobalt db query *)"` (`2026-09-19/02-deploy-stack-3.md`, 25 prompt hits), in the command shape of `01-p2-build.md:17` |
| `"Bash(COBALT_ENV=production uv run cobalt radar evaluate --replay *)"` | PRECEDENTED string (`2026-09-18/10-deploy-stack.md`, `19-deploy-stack-2.md`, `2026-09-19/02-deploy-stack-3.md`). **NEW USE**: run from a worktree on the branch's code |
| `"Bash(ln -s /Users/cobalt/cobalt/data/radar-cache /Users/cobalt/cobalt-wt/setups-c1/data/radar-cache)"` | **NEW** |
| `"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/data/radar-cache)"` | **NEW** |
| `"Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)"` | **NEW**: a narrowing of `01-p2-build.md:32`'s `"Bash(uv run python *)"` |
| deny `"AskUserQuestion"` `"EnterWorktree"` `"Bash(git push*)"` · `--add-dir /Users/cobalt/Vault /Users/cobalt/cobalt /Users/cobalt/cobalt-wt` | PRECEDENTED: `65` |

**`13` — 9 allow strings · 3 deny · the triplet. Every one is byte-identical to `prompts/2026-09-21/66-setups-one-check.md`'s line, and none is NEW.**
| string | status |
|---|---|
| `"Bash(agy *)"` | PRECEDENTED: `66`, from 09-21 R39 |
| `"Bash(claude -p --model claude-opus-5 *)"` | PRECEDENTED: `66`, from 09-21 R49 |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` · `"Bash(git -C /Users/cobalt/cobalt log*)"` · `"Bash(ls *)"` · `"Bash(grep *)"` · `"Bash(tail *)"` · `"Bash(wc *)"` · `"Bash(date*)"` | PRECEDENTED: `66`. These are also the seven strings of this drafting session |
| deny ×3 · triplet | PRECEDENTED: `66` |

`12` spells production commands only in shapes read from the code's argparse (`src/cobalt/db_query.py:209-215`: `--side`, `--prod`, `--format`, `--limit`, sql) or from `evaluate_cli.py`'s docstring (`--replay`, `--trade-def`, `--expect-formed`). No flag was invented. The cutter's argv and its `--remove` mode belong to a new file that `12` writes, not to an existing CLI.

## ESCALATE
1. **Hitchhiker is expected to fail by construction.** The production replay evaluates production's `"user".trade_defs` with every numeric assumed hole null (F1, F5). Hitchhiker's shape reads those holes, so `12` will most likely end `hitchhiker=none` with `FAILED: no stored day forms hitchhiker — <n> days tried`, and the pin stays. It could also stop at 2.2(a) or (b) if production's store does not hold or evaluate the slug. **ASK DESK:** keep (A) the drafted gate, where the exit codes decide and the failure goes to him, or (B) re-issue with an OFFLINE selector: the build's neutral shape evaluated over cut raw days, with the day chosen by a pytest exit code. B selects by the build's definition rather than production's, needs a larger production read, and needs his ruling. Safe default: A.
2. **Rubberband has one real candidate.** The replay reads daily bars only from `data/radar-cache` (F2), and production has daily files only for 09-21 (116) and 09-22 (F4). Every other stored day is `input_stale` for its day-1 HTF avoid (F3). Without the NEW link strings it cannot form on ANY day from the worktree. If 09-21 does not form, or its cut fails STEP-4, rubberband ends `none`.
3. **Selection definition ≠ pin definition.** The replay selects by his production definition, which is FINAL §9 point 4's own gate and consistent with R24 (a definition, not a trade). The pins assert the build's NEUTRAL shape. `12` STEP-4 takes a day only if the neutral shape also forms on the cut. Otherwise it moves to the next day, and the rejection is recorded.
4. **NEW USE of the R41 `.env` for a production read from a worktree.** L41 routes production reads through Cobalt commands from `~/cobalt`. `12` keeps the db queries there and moves only the replay, which cannot run on main. His approve is needed on the launch row (the AUTHORIZATION gate greps it).
5. **Raw production rows are captured in harness background-output files outside the repo.** The unattended rules forbid `>`, so no redirect is possible. They hold system bars, not user data. `12` names the paths and the desk decides the cleanup. **ASK DESK** if a scratch-path capture is preferred: that needs a NEW redirect-style string.
6. **Gemini's window.** The drafting prompt says R39 covers `agy` through 09-22 23:59, and the `66` hub is also using it now. If `12` finishes after that, `13` falls to Opus 5, the builder's own house. It is still blind, but L67's other-house floor is then met only by `66`'s check. **ASK DESK:** accept that, or hold `13` for another house. Safe default: run it and record "same-house".
7. **Hand derivation may be UNDERIVABLE.** The atoms rest on EMA, VWAP, ATR and pivots over a few hundred RTH bars, and neither seat runs code (Opus in `plan` mode; Gemini in `--sandbox`, which `66` did not prove can execute). A code-capable independent checker, such as Sol read/write, is out until Sat 09-26 (`cto-2026-09-22.md` R13) and would need a NEW string.
8. **Timing (ASK DESK).** `12` makes production reads (1 + ≤2 per cut + up to one replay per stored day per slug). No time gate is written. The desk may prefer after 16:00 ET, given today's radar-benchmark-load report. Safe default: none.
9. **Unverified by me:** the exact offline and with-DB suite commands. `12` tells the hub to quote them from the build report's `## CLOSE` rather than inventing a spelling.

SETUPS FIXTURE CUT PROMPTS DRAFTED · prompts: 2 · production reads: 2 strings (1 NEW) · blind house: Gemini (fallback Opus 5) · ESCALATE: 9
