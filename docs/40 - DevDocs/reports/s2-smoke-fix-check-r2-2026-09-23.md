# S2 Smoke Fix — Check Round 2 (F3 only), 2026-09-23

§0 HEADLINE: Round 2 of ≤3, F3 only (`b510b65`). All three houses (Grok, Gemini, Opus 5.5) independently ruled F3 CLOSED, `ready for a deploy prompt: YES`; Gemini reversed its round-1 `NEW DEFECT INTRODUCED` after this round's file evidence. My own file-check against the real branch confirms every DOES NOT HOLD verdict — `defects that HOLD: 0`. Status: DONE. ESCALATE count: 2 (round-1 Gemini defect quoted with verdict; a staging defect of mine where the "do not open `*-check.md`" instruction also blocked the MANDATORY `hub-file-check.md`, leaving Gemini/Opus's SECOND unanswered — Grok answered it in full, and it changed no house's F3 ruling).

## L74
none — no block matching L74's shape has arrived in any tool result so far.

## PREFLIGHT
| # | rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|---|
| 1 | THE DATE + EXTENSION GATE | `date` | 0 | allowed — `Wed Sep 23 08:59:27 EDT 2026`, within the 2026-09-23 23:59 ET window for `Bash(grok *)`/`Bash(agy *)` per his R30 |
| 2 | probe | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 3 | probe | `agy --version` | 0 | allowed — `1.2.9` |
| 4 | worktree present | `ls /Users/cobalt/cobalt-wt/s2-smoke-fix` | 0 | allowed — worktree present |
| 5 | THE BUILT LINE | `tail -n 3 ".../s2-smoke-fix-build-2026-09-23.md"` | 0 | allowed — last line `S2 SMOKE FIX BUILT b510b65 \| on 6f4da5e \| offline 1970/0 \| with-DB: OWED (68) \| RESTARTS: com.cobalt.aset com.cobalt.radar \| F3: built \| tests added: 12 \| ESCALATE: 9` — `<tip>` = `b510b65` |
| 6 | F3 commit check | `git -C /Users/cobalt/cobalt log --oneline -1 b510b65` | 0 | allowed — subject `fix(s2-smoke): F3 K3 grades only a ranked row that stored no metric; unranked_retained printed` |
| 7 | branch not moved | `git -C /Users/cobalt/cobalt log --oneline b510b65..s2/smoke-fix-0922 -- tests src configs` | 0 | allowed — EMPTY |
| 8 | radar unchanged by build | `git -C /Users/cobalt/cobalt log --oneline 6f4da5e..b510b65 -- src/cobalt/radar` | 0 | allowed — EMPTY |
| 9 | .env absence | `ls /Users/cobalt/cobalt-wt/s2-smoke-fix/.env` | 1 | allowed — `No such file or directory` (required) |
| 10 | RECOVERY | `ls scratch/tribunal-bars-0920/s2-smoke-fix-check-r2` | 1 | allowed — `No such file or directory` — fresh run |
| 11 | THE STAGGER | `grep -n -F "05 is not running"` / `"08 is not running"` / `"no other house hub is running"` in `cto-2026-09-23.md` | 0 each | allowed — R32 (line 35) carries all three literals and names `17-s2-smoke-fix-check-r2.md` |
| 12 | THE PROBES | grok/agy `--version` (rows 2–3) + `claude -p --model claude-opus-5-5 "Reply with exactly: PONG"` (`run_in_background`) | 0 | allowed — Opus replied `PONG`; all three checkers UP, ≥3 ready |

## Packet
Staged in `scratch/tribunal-bars-0920/s2-smoke-fix-check-r2/`, all 8 files present, each below a one-line header naming its real path/range/`<tip>`. `f3-diff.md` checked `grep -c "^diff --git"` = 2 (pass).

| file | B |
|---|---|
| f3-diff.md | 8,569 |
| gemini-r1.md | 1,866 |
| hub-file-check.md | 3,812 |
| k3-at-tip.md | 4,081 |
| models-at-tip.md | 1,388 |
| pool-at-tip.md | 10,112 |
| QUESTIONS-S2FIX-R2.md | 4,756 |
| store-at-tip.md | 6,549 |
| **total** | **41,133** |

HONEST SIZE: 41,133 B ÷ 4 ≈ 10.3 KB ≈ 2.6k tokens estimated per house. Well under the 230,000 B ceiling.

## CONTINUE
Write-nothing proof BEFORE any launch: `scratch/tribunal-bars-0920/s2-smoke-fix-check-r2/` = 8 packet files only (09:04 ET); `/Users/cobalt/cobalt-wt/s2-smoke-fix` = unchanged build-worktree listing (06:05 ET newest).
Launched (all `run_in_background`, independent, one attempt each), `date` at launch = `Wed Sep 23 09:05:23 EDT 2026`:
- GEMINI (agy), task `bag871kk1`, launched first, 09:05:2x ET.
- GROK, task `b4j4ygd2c`, launched 09:05:4x ET.
- OPUS 5.5, task `b8fyy0vef`, launched 09:05:5x ET.
45-minute clock: deadline ≈ 09:50 ET for all three.

All three completed well inside the 45-minute clock: Opus 09:07:38 ET, Gemini 09:08:00 ET, Grok 09:12:14 ET (launch 09:05:23 ET). Write-nothing proof after each: only `gemini-check.md` / `opus-check.md` (written by me from stdout) and Grok's own `grok-check.md` (its approved `--allow` write) appeared; no other entry changed in either directory.

**Staging defect found (mine, not a checker's):** the "Do not open any `*-check.md` file" instruction in each launch sentence, meant to stop a checker reading another house's answer file, also matches this packet's own MANDATORY input `hub-file-check.md` by filename pattern. Gemini and Opus both declined to open it and left SECOND unanswered as a direct result; Grok opened it anyway and answered SECOND in full. Recorded under `## ESCALATE`.

## F3
| checker | round-1 F3 ruling | round-2 F3 ruling (≤30 words, file:line) | changed |
|---|---|---|---|
| grok | CLOSED | `CLOSED` — no line writes both `last_rank`/`rank_metric` NULL for a member the scan ranked (`store-at-tip.md:27-32,73-80,87-98`; `k3-at-tip.md:32,34,36,38-44`) | no |
| gemini | NEW DEFECT INTRODUCED | `CLOSED` — ranked rows always carry non-null `last_rank` and `rank_metric` (`pool-at-tip.md:108,159`; `models-at-tip.md:22-24`) | **yes** |
| opus | CLOSED | `CLOSED` — both graded counters carry the new predicate, `unranked_retained` absent from `expect`, offline test asserts it (`k3-at-tip.md:32,34,36`; `f3-diff.md:139-160`) | no |

## Round-1 sentences
| sentence | grok | gemini | opus |
|---|---|---|---|
| S1 (write defect → hidden in `unranked_retained`) | DOES NOT HOLD — `pool-at-tip.md:108,159`; `store-at-tip.md:27-32` | DOES NOT HOLD — `pool-at-tip.md:108,159`; `store-at-tip.md:27` | DOES NOT HOLD — `pool-at-tip.md:107-108,159`; `store-at-tip.md:27-32,94,98` |
| S2 (designed-NULL row still reads red) | DOES NOT HOLD — `models-at-tip.md:20-25`; `pool-at-tip.md:22,55` | DOES NOT HOLD — `models-at-tip.md:22-24`; `pool-at-tip.md:22` | DOES NOT HOLD — `models-at-tip.md:20-24,33`; `pool-at-tip.md:55,64-65,74` |

## Hub file-check rows
| row | grok | gemini | opus |
|---|---|---|---|
| 1. hub S1: DOES NOT HOLD (`pool.py:109-212`) | AGREE | NOT CHECKABLE FROM READS — declined to open `hub-file-check.md` (matched its own `*-check.md` do-not-open instruction) | NOT ANSWERED — same reason, stated explicitly in its §0 |
| 2. hub S1 restated under Gemini's FOURTH (c) | AGREE | NOT CHECKABLE FROM READS — same reason | NOT ANSWERED — same reason |
| 3. hub secondary (config-None metric name), hub marked NOT CHECKABLE | DISAGREE — now checkable with `models-at-tip.md` staged; the config-None path does not exist (`models-at-tip.md:20-25,33`) | NOT CHECKABLE FROM READS — same reason | NOT ANSWERED — same reason |
| 4. DESK READ (`models.py:92-97`, cannot be None) | AGREE | NOT CHECKABLE FROM READS — same reason | NOT ANSWERED — same reason |

## Checked against the branch
Verified by me directly against `/Users/cobalt/cobalt-wt/s2-smoke-fix/src/cobalt/radar/{pool,models,store}.py` (radar unchanged by the build, PREFLIGHT-proven) — real source line numbers, not the packet's internal numbering.

- **claim**: "No line writes `last_rank` NULL for a member ranked this scan." · **who**: grok, gemini, opus · **file:line**: `pool.py:211-212` (`ranks` built from `enumerate(ordered)`, always int for every candidate); `:323-326` (`ranked_candidates` = candidates minus held, fed to `_ranked`); `:341-347` (in-cap RETAIN: `rank=ranks[ticker]`); `:386-391` (ADMIT: `rank=ranks[ticker]`); `:393-398` (EXCLUDE: `rank=ranks[ticker]`) · **HOLDS** · every path assigning `rank` to a ticker present in `ranked_candidates`/`ordered` pulls it from the `ranks` dict comprehension, which can only hold ints ≥1; the sole None-rank path (`ranks.get(ticker)` at `:356`) fires only for a ticker excluded from `ranked_candidates` — not ranked this scan.
- **claim**: "`ranks` and `values` are populated together by `_ranked`'s `key()` closure." · **who**: grok, gemini, opus, hub · **file:line**: `pool.py:168-171` (screen branch sets `values[ticker]`), `:178` (list branch sets `values[ticker]`), `:211` (`sorted(candidates, key=key)` runs `key()` — and therefore sets `values[ticker]` — for every ticker in `candidates`), `:212` (`ranks` built from the same `ordered`) · **HOLDS** · both dicts are filled in the same `sorted(...)` call, one entry per candidate; a ticker present in `ranks` is always present in `values`.
- **claim**: "`store.py` writes `last_rank` and `rank_metric` together, unconditionally, on every write path that can carry a ranked value." · **who**: grok, gemini, opus · **file:line**: `store.py:86-94` (RETAIN UPDATE), `:132-142` (EXCLUDE UPDATE), `:145-161` (ADMIT/EXCLUDE INSERT) · **HOLDS** · each statement writes both columns from the SAME `Transition`'s `.rank`/`.rank_metric` in one statement, never one without the other. (HOLD, `:95-110`, uses `COALESCE` and can leave a prior pair unchanged, but a HOLD is excluded from "ranked this scan" by both the design comment at `pool.py:50-53` and `pool.py:381-385`, which sources its rank from `member.last_rank`, not from `ranks`.)
- **claim**: "`session_metric` (and therefore `rank_metric`'s name) can never be None for a ranked ticker." · **who**: grok, gemini, opus · **file:line**: `models.py:92-96` (`RankMetric`'s three fields are required `Literal["volume","rvol"]`, `extra="forbid"`); `pool.py:126` (`session_metric = getattr(pool.rank_metric, session)`), `:159` (`metric = override_metric or session_metric`), `:178` (list branch uses `session_metric` directly) · **HOLDS** · a required, `extra="forbid"` Pydantic literal field cannot validate to `None`; the `or` fallback in the screen branch guarantees a non-None name even when a per-source override omits `rank_metric`.
- **claim** (Grok's disagreement with the hub's round-1 "NOT CHECKABLE" on the secondary config-None possibility): "with `models.py` staged this round, the secondary possibility is checkable and does not hold." · **who**: grok · **file:line**: `models.py:92-96,99-106` · **HOLDS** (Grok's correction is itself correct) · the round-1 hub did not have `models.py` staged and correctly marked this `NOT CHECKABLE FROM READS` at the time; with `models.py:92-97` now in the packet, the required `Literal[...]` + `extra="forbid"` typing settles it — the metric name cannot be `None` by any valid config.

No checker raised a HOLDS, NOT CLOSED, or NEW DEFECT claim this round to check against the branch beyond the above (all three independently ruled F3 CLOSED).

(i) L32: this report contains no market ticker.

## Ready for a deploy
| checker | CHECK S2 FIX line | ready | reason verbatim |
|---|---|---|---|
| grok | `CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | (FIX STANDS line carries no separate reason field) |
| gemini | `CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | (FIX STANDS line carries no separate reason field) |
| opus | `CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | (FIX STANDS line carries no separate reason field) |

## FOR THE CLASSIFIER
none

## ESCALATE
- Round-1 Gemini's `DEFECT REMAINS`, quoted in full: `CHECK S2 FIX: DEFECT REMAINS F3 · ready for a deploy prompt: NO · K3 now reads green on a write defect dropping both.` — my round-2 file-check verdict: **DOES NOT HOLD** (see `## Checked against the branch`, claims 1-3). Gemini itself reversed this to CLOSED in round 2.
- FOR THE CLASSIFIER: none (nothing to restate).
- Packet mismatch (mine): the "Do not open any `*-check.md` file" instruction also matched the packet's own `hub-file-check.md`, a MANDATORY input, by filename. Gemini and Opus both left SECOND unanswered as a direct result; Grok opened it anyway and answered in full. This did not change any house's THIRD/F3 ruling or CHECK S2 FIX line (all three reached CLOSED independently via FIRST alone), so it does not block `07` P6, but it is a staging defect on this hub's part.
- No checker failed to check (all three produced a `CHECK S2 FIX:` line); no checker wrote a file it was not told to; no `ASK DESK` was needed — safe default taken: no retry.
- L74: no block matching that shape arrived in any tool result this run.
- Standing line: "This round covers F3 of the S2 smoke fix only (`b510b65`); F1-FX, F1 and F2 stand on round 1's rulings (`reports/s2-smoke-fix-check-2026-09-23.md`, 3 of 3 CLOSED). It is round 2 of ≤3 (L67 / L39). With three houses `ready … YES` and `defects that HOLD: 0`, the branch is READY for today's stacked deploy; a HOLD goes to a classifier and a fix round; a NO with `defects that HOLD: 0` leaves ONE round (3, the last — no fourth, L39) or his per-case override (L67 OVERRIDE / L73), and the branch waits out of tonight's set if neither lands before the deploy (L43's drop rule)."
- Standing line: "Every with-DB claim of this build is UNPROVEN until `68-devdb-repair.md` lands and the with-DB set runs on `<tip>` (the stacked deploy's L68 gate)."

S2 SMOKE FIX CHECK DONE · round: 2 · grok: CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES · gemini: CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES · opus: CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES · sol: NOT SEATED (round 1: METER — retry after Sep 26th, 2026 6:47 AM) · defects that HOLD: 0 · ESCALATE: 2
