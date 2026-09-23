§0 Headline: S2 smoke fix build check, round 1 of ≤3, `6f4da5e..b510b65` on `s2/smoke-fix-0922`. Checked by Grok, Gemini, Opus 5.5 (Sol METER-skipped). Grok and Opus: FIX STANDS, ready YES. Gemini: DEFECT REMAINS F3 (K3's new `last_rank IS NOT NULL` predicate could theoretically mask a write defect), ready NO — but the hub's own file-check of `src/cobalt/radar/pool.py:109-212` (`_ranked`) finds this DOES NOT HOLD: `last_rank` and `rank_metric` are set together, atomically, for every scan-candidate ticker, so a write defect on a genuinely-ranked row cannot null the metric without also leaving `last_rank` non-NULL (which K3 would still grade). defects that HOLD: 0. Three houses checked (L67 floor met) → branch is READY for today's stacked deploy per this report, pending the with-DB gate (68) before the deploy. ESCALATE: 1 (Gemini's claim, quoted in full despite not holding, per standing rule).

## L74
No L74 block arrived in this run.

## PREFLIGHT
- date: Wed Sep 23 07:08:00 EDT 2026 (within R30's window, through 2026-09-23 23:59 ET)
- grok --version: grok 1.0.25 (f7e67d6988e2) [stable]
- agy --version: 1.2.9
- AUTHORIZATION: all gates PASS — classification commit `aee67db`, R1 (`76` + "Also, both are approved.") and R6 (`S2 SMOKE FIX BUILT b510b65` + `9c12209`) present and committed (`dfc09cf`), R13 launch row present and committed (`fd258c9`), 70/66-chain gates (R13 09-20, R40, R44, R46+committed `53e0594`, R49 sol string present+committed `60147d4`, R32 opus-5.5 string present+committed `b8a72b5`) all PASS, THE THIRTEEN+THREE all present in `08-bars-chunk-e-check.md` (grok/agy count 2 each — one prose mention + one launch-line mention in that file itself, not a mismatch; all others count 1), Astra string absent from this launch line, DATE+EXTENSION GATE: R30 "Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" present + committed (`055242d`).
- `ls s2-smoke-fix` worktree: present.
- THE BUILT LINE (`tail -n 3` s2-smoke-fix-build-2026-09-23.md): `S2 SMOKE FIX BUILT b510b65 | on 6f4da5e | offline 1970/0 | with-DB: OWED (68) | RESTARTS: com.cobalt.aset com.cobalt.radar | F3: built | tests added: 12 | ESCALATE: 9` — `<tip>` = `b510b65`.
- THE RANGE `6f4da5e..b510b65`: `b510b65` F3 · `7ec24b2` F2 · `68e8f23` F1 · `fc16830` F1-FX — matches expected order exactly.
- Branch tip `s2/smoke-fix-0922` = `9c12209` (report commit, docs-only). `b510b65..s2/smoke-fix-0922 -- tests src configs` EMPTY — branch has not moved above tip.
- Staging boundary (`git log --stat --oneline 6f4da5e..b510b65`): touches only `configs/cobalt/smoke/s2.yaml`, `src/cobalt/replay/movers.py`, `src/cobalt/replay/models.py`, `src/cobalt/smoke/checks.py`, `tests/cobalt/test_replay_movers.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_smoke.py`, `tests/cobalt/test_smoke_k3_sql.py`, `tests/fixtures/replay/_cut_p4_fixtures.py`, `tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv`, and the DevDocs (`replay/models.md`, `replay/movers.md`, `smoke/checks.md`, `smoke/config.md`, `tests/fixtures/replay/_cut_p4_fixtures.md`) + the build report. All within the allowed CLOSE list — no boundary violation.
- `.env` in s2-smoke-fix: absent (correct).
- Recovery folder `scratch/tribunal-bars-0920/s2-smoke-fix-check`: absent — fresh run.
- STAGGER: 03 DONE (report present, `DEVDB REPAIR RE-ISSUE REVIEWED ...`); 05 and 08 have no report, and the desk's R13 launch row names `06-s2-smoke-fix-check.md` and states "05 is not running" and "08 is not running" and "no other house hub is running" — all clear.
- CODEX LAUNCH SHAPE: `Experiment field: **reads started**` count = 1 → Sol launch (if run) appends ` < /dev/null`.
- FOUR PROBES: grok UP (`--version` OK) · gemini UP (`--version` OK) · sol METER — retry after Sep 26th, 2026 6:47 AM (matches R13's Sat 2026-09-26 06:47 ET) · opus UP (`claude -p --model claude-opus-5-5` → `OK`, exit 0). Three UP (Grok, Gemini, Opus) ≥ 3 floor → launch every UP house.

## Packet
Staged in `scratch/tribunal-bars-0920/s2-smoke-fix-check/`: `build-diff-1.md`..`build-diff-4.md` (15535+21242+6932+34699 B; 4 commits, 13 `diff --git` lines summed, matches the range) · `devdoc-diff.md` (13050 B) · `movers-at-tip.md` (30300 B) · `models-at-tip.md` (4445 B) · `checks-at-tip.md` (3152 B) · `s2-at-tip.md` (5798 B) · `runner-at-tip.md` (1753 B) · `contract.md` (23061 B) · `build-report.md` (17471 B) · `classify.md` (4845 B) · `smoke-look.md` (4246 B) · `rows.md` (14427 B) · `fixture-counts.md` (719 B) · `QUESTIONS-S2FIX.md` (9343 B). Whole-packet total: 211,018 B (ceiling 230,000 B — under it). Per-checker estimate: 211018 ÷ 4 ≈ 52,755 B ≈ 13.2k tokens.

## Per FIX row
| row | what it fixes | grok | gemini | sol | opus | checkers answering CLOSED |
|---|---|---|---|---|---|---|
| F1-FX | cuts a real-shape fixture carrying the blank-`Change` tail | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| F1 | a blank `Change` cell is unranked, not fatal | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| F2 | K4.4 asks the pool API with `since`, percent-encoded | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| F3 | K3 grades only a ranked row that stored no metric | CLOSED | `NEW DEFECT INTRODUCED — configs/cobalt/smoke/s2.yaml:34`: "a write defect dropping both `last_rank` and `rank_metric` to NULL now falls into the ungraded `unranked_retained` bucket, so K3 completely misses it." | — | CLOSED | 2 of 3 |

## Build ESCALATE
| item | checker | answer verbatim |
|---|---|---|
| 2 (losers UNPROVEN) | grok | AGREE — the constructed test puts blanks above, between and under reversed ranked rows, so position is not assumed. |
| 2 | gemini | AGREE — the test's constructed order proves the logic handles blanks anywhere, regardless of where Finviz puts them. |
| 2 | opus | AGREE — blanks are covered both above and between ranked rows by constructed order; live losers placement stays unproven until a live losers export carries blank rows. |
| 5 (readers of `movers_by_side`) | grok | AGREE — the staged code only writes `movers_by_side`. Smoke grades `.expected`, which old rows have. No staged reader validates an old job row. |
| 5 | gemini | AGREE — ReplayResult is only used for fresh payloads; the smoke check reads raw JSON, so an old result lacking unranked breaks nothing. |
| 5 | opus | AGREE — the runner only writes `movers_by_side`. No prod job row carrying it exists yet, so no old row can lack `unranked`. The `src` grep itself is NOT CHECKABLE. |
| 6 (RESTARTS) | grok | NOT CHECKABLE FROM READS — would need `cobalt jobs restarts` or the residents' import graph; these excerpts do not show aset or radar importing the changed modules. |
| 6 | gemini | AGREE — checks.py and models.py import from aset and radar, so restarting the residents correctly picks up the code changes. |
| 6 | opus | NOT CHECKABLE FROM READS — needs `uv run cobalt jobs restarts 6f4da5e..b510b65` and a look at the static import walk. Restarting both residents is the conservative outcome in any case. |
| 7 (two deviations) | grok | AGREE — the loguru sink asserts one exact warning; `caplog` cannot see loguru. The constructed losers file still uses `retained_exports` → `parse_movers` and the same counts. Both SAME strength. |
| 7 | gemini | AGREE — a loguru sink is required to capture loguru; the constructed losers file tests the same unranked logic at the exact same strength. |
| 7 | opus | AGREE — both deviations keep the SAME strength (detailed reasoning per deviation, file:line cited). |

## Per not-fixed row
| row | class | grok | gemini | sol | opus |
|---|---|---|---|---|---|
| K9.2 · K9.3 · K9.5 · K9.6 | NOT REAL | AGREE WITH THE CLASS | AGREE WITH THE CLASS | — | AGREE WITH THE CLASS |
| NEW N1 (smoke-look clock) | OUT OF SCOPE | NOT TOUCHED | NOT TOUCHED | — | NOT TOUCHED |

## Assertions and boundary
| checker | (a) weaker assertions | (b) hunks outside files | (c) silent-failure answer |
|---|---|---|---|
| grok | NONE | NONE | NO PATH. All-blank still raises. A partial blank logs one warning and stores `unranked`. K3 still fails a ranked row with a NULL metric. K4.4 still requires HTTP 200. `unranked_retained` is selected the same way `value_null` was already printed. |
| gemini | NONE | NONE | `configs/cobalt/smoke/s2.yaml:34 DOES` — requiring `last_rank IS NOT NULL` for `metric_missing` means a write defect zeroing both columns is ignored in the ungraded `unranked_retained` bucket, making K3 read green on a broken night. |
| opus | NONE (each candidate weakening checked and found to be a strengthening, e.g. added `match=` clauses, a new required field) | NONE (diff covers only `s2.yaml`, `checks.py`, `models.py`, `movers.py`, four test files, the cutter, the new fixture, named DevDocs) | NO PATH outside what is already ruled (the heartbeat-AMBER-for-unranked and F3's print-not-grade posture are both `NOT A ROW`/ruled). |

## Checked against the branch
Gemini's F3 claim and its restated (c) silent-failure claim are the only NOT CLOSED / NEW DEFECT / silent-failure claim in this round; both rest on the same mechanism, checked together.

- **claim**: "A write defect dropping both `last_rank` and `rank_metric` to NULL now falls into the ungraded `unranked_retained` bucket, so K3 completely misses it." · **who**: gemini · **file:line**: `src/cobalt/radar/pool.py:109-212` (`_ranked`, read from the worktree — unchanged by this build) · **DOES NOT HOLD** · `_ranked`'s `key(ticker)` closure sets `values[ticker]` as a side effect of computing every candidate's sort key (`:168-171` screens, `:178` lists), and `ranks = {ticker: index+1 for index, ticker in enumerate(ordered)}` (`:211-212`) where `ordered = sorted(candidates, key=key)` runs `key()` — and therefore sets `values[ticker]` — for every ticker in `candidates` (`ranked_candidates`, the full scan-candidate set minus held). So `ranks[ticker]` and `values[ticker]` are populated TOGETHER, atomically, for every ticker the scan actually considered; `ranks.get(ticker)` returns `None` (→ `last_rank` NULL) ONLY for a ticker absent from `ranked_candidates` entirely — i.e. never a candidate this scan, the literal "no ranking happened" case the ruling names. There is no code path where a ticker is genuinely ranked (has a real `last_rank`) yet a write defect could still leave `rank_metric` unset via the SAME mechanism that nulls `last_rank` — the two are set by one closure call, not independently. A "write defect that nulls the metric on an actually-ranked row" would leave `last_rank` NON-NULL (it's set from the same `ranks` dict, unconditionally, by both the RETAIN and ADMIT/EXCLUDE write paths in `store.py:86-94,132-142`), so it lands in `metric_missing` / `rescanned_metric_missing` — GRADED, not silently absorbed into `unranked_retained`. The claim describes the exact designed class the ruling and the desk's `ranked_without_metric 0` proof already name, not a build-introduced gap.
- **claim**: same, restated under Gemini's FOURTH (c) · **who**: gemini · **file:line**: same · **DOES NOT HOLD** · same reasoning.
- A secondary, narrower possibility Gemini's wording gestures at — that `values[ticker]`'s metric NAME itself (`best_metric` / `session_metric`) could be `None` for a genuinely-ranked ticker by a *configuration* gap rather than a code defect (`pool.py:126,159`, `session_metric = getattr(pool.rank_metric, session)`) — is `NOT CHECKABLE FROM READS`: it depends on whether `PoolBlock.rank_metric`'s per-session fields are ever legitimately unset, and that model is not staged. If it can be `None` by valid config, such a row would still be GRADED (last_rank non-NULL, rank_metric NULL → `metric_missing`), consistent with the ruling's "only a write-path defect is a K3 failure" — it would not be silently hidden either way, so this does not change the DOES NOT HOLD verdict on Gemini's actual claim (which is specifically about a defect being *hidden* in `unranked_retained`).

Also checked, per the standing rule:
- (i) `git -C /Users/cobalt/cobalt log --stat --oneline 6f4da5e..b510b65` names only PREFLIGHT's boundary paths — confirmed, no other path (see PREFLIGHT above).
- (ii) PROTECTED PATHS: `git log --oneline 6f4da5e..b510b65 -- src/cobalt/radar src/cobalt/aset src/cobalt/cards src/cobalt/archiver src/cobalt/db_migrations` — EMPTY. `git log --oneline 6f4da5e..b510b65 -- tests/fixtures/replay/movers-gainers.real-shape.csv tests/fixtures/replay/movers-losers.real-shape.csv` — EMPTY.
- (iii) `grep` of `skip\|xfail` on every `+` line across `build-diff-1.md`..`build-diff-4.md`: one hit, a docstring prose word ("skipped, counted in `unranked_rows`", `build-diff-2.md:158`) — not a `pytest.mark.skip`/`xfail` marker. No real skip/xfail introduced.
- (iv) THE BLANK TEST'S WIDTH: at tip, `grep -n 'strip() == ""'` → `movers.py:203`; `grep -n "is not a percentage"` → `movers.py:137` (raise) and `:183` (docstring prose). At base `6f4da5e` (`git show`): no `strip() == ""` line exists at all (the check is new, F1's whole point); `is not a percentage` → one hit, `movers.py:128`, message text `f"movers: Change {raw!r} is not a percentage"` — **byte-identical** to the tip's `:137`. Error messages equal before and after: **yes**.
- (v) THE CUTTER'S OTHER MODES: `grep -n "^-"` on `build-diff-3.md` (the `_cut_p4_fixtures.py` hunk) shows exactly one content removal — the mode-dispatch error message (`:143`, `raise SystemExit(f"unknown mode {mode!r}; expected no argument, 'evidence' or 'movers'")` → widened to name `movers-blank`), which is the named acceptable dispatch change. No other `-` line; the three existing modes (no-argument, `evidence`, `movers`) are untouched.
- (vi) L32: this report was read once by the hub before its last line — no ticker written.
- (vii) RESTARTS (L42): the build report's line quoted: `RESTARTS: com.cobalt.aset com.cobalt.radar`. Grok and Opus mark the underlying import-reach claim `NOT CHECKABLE FROM READS` (would need `uv run cobalt jobs restarts 6f4da5e..b510b65` or the residents' static import walk); Gemini AGREEs from the staged imports alone. The hub did not independently re-run the import walk — recorded as reported by the builder and partially corroborated, not independently re-derived.

Where checkers agreed, nothing was smoothed; the one disagreement (F3) is recorded above with both sides quoted in full in their own check files.

## Ready for a deploy
| checker | CHECK S2 FIX line | ready | reason verbatim |
|---|---|---|---|
| grok | `CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | (no reason field — YES carries none) |
| gemini | `CHECK S2 FIX: DEFECT REMAINS F3 · ready for a deploy prompt: NO · K3 now reads green on a write defect dropping both.` | NO | K3 now reads green on a write defect dropping both. |
| opus | `CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | (no reason field — YES carries none) |

## FOR THE CLASSIFIER
none — Gemini's F3 claim (the only NOT CLOSED / NEW DEFECT / silent-failure claim raised this round) was checked against the branch above and DOES NOT HOLD.

## ESCALATE
- Gemini's `DEFECT REMAINS F3` — full text: `NEW DEFECT INTRODUCED — configs/cobalt/smoke/s2.yaml:34` ("A write defect dropping both `last_rank` and `rank_metric` to NULL now falls into the ungraded `unranked_retained` bucket, so K3 completely misses it. Furthermore, a row ranked with no value by design still gets a non-NULL `last_rank` with a NULL `rank_metric`, so K3 still reads red on that designed behaviour.") — checked against `pool.py:109-212` above: DOES NOT HOLD, but recorded here per standing rule regardless of the hub's file-check outcome.
- Grok printed its answer to stdout instead of writing `grok-check.md` itself via its approved `--allow "Write(...)"` (which did cover the folder) — a harness/behavior deviation, not a packet or access problem; no file was written or altered by Grok (written-nothing proof: `ls -la` of the packet folder and the `s2-smoke-fix` worktree before/after are identical except the hub's own writes). The hub wrote `grok-check.md` from its stdout, byte for byte, as it already does for Gemini and Opus.
- a standing line: **"This check covers the S2 smoke fix only, `6f4da5e..b510b65` (F1-FX, F1, F2, F3). It is round 1 of ≤3 (L67 / L39). With three houses checked and `defects that HOLD: 0`, the branch is READY for today's stacked deploy; a HOLD goes to a classifier and a fix round — and the branch waits out of tonight's set if that cannot land and be checked before the deploy (L43's drop rule)."**
- a standing line: **"Every with-DB claim of this build is UNPROVEN until `68-devdb-repair.md` lands and the with-DB set of `build-report.md` ESCALATE (iv) runs on `b510b65` (the stacked deploy's L68 gate)."**
- a standing line: **"The LOSERS side's blank-row placement stays UNPROVEN until the first live losers export carries one (build ESCALATE 2) — covered by a constructed-order test, not by a real export."**

S2 SMOKE FIX CHECK DONE · grok: CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES · gemini: CHECK S2 FIX: DEFECT REMAINS F3 · ready for a deploy prompt: NO · K3 now reads green on a write defect dropping both. · opus: CHECK S2 FIX: FIX STANDS · ready for a deploy prompt: YES · sol: METER — retry after Sep 26th, 2026 6:47 AM · defects that HOLD: 0 · ESCALATE: 1
