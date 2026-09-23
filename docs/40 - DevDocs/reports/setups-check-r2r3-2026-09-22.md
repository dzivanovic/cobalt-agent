# Setups check, round 2 of 3 (R2+CUT+R3 fix path) — 2026-09-22

## §0 Headline
Checked the whole unchecked fix path `60ddac4..be44eb4` ([R2] `60ddac4..826d284`, [CUT] `74eefd8..65c08a0`, [R3] `65c08a0..be44eb4`) against the classifier's FIX rows, the cut's C1–C3 and his R47–R51/R61 rulings. Three checkers ran (Grok, Gemini, Opus 5.5 — Sol on METER, skipped). Grok and Gemini: `FIX STANDS`. Opus 5.5: `FIX AGAIN` on the cut fixture — the cutter re-dates the calendar day but keeps the UTC clock time, so a September (EDT) day re-dated onto a January (EST) synthetic day lands one hour off in New York local time; I confirmed this myself against the cutter's code and against the two dates' DST status. Status: **DONE**. defects that HOLD: 5 · owner items: 2 · ESCALATE: 9.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 22 20:19:31 EDT 2026` — launch date 2026-09-22, within R30's grok/agy extension (through 2026-09-23 23:59 ET) |
| grok up | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy up | `agy --version` | 0 | `1.2.8` |
| worktree exists | `ls /Users/cobalt/cobalt-wt/setups-c1` | 0 | present (repo tree listed) |
| [R2] built line | `tail -n 3 ".../setups-fix-r2-2026-09-22.md"` | 0 | `SETUPS FIX R2 BUILT 826d284 \| on 60ddac4 \| offline 2432/0 \| with-DB 553/0 \| src changed: yes \| tests added: 13 \| .env: removed, proven gone \| ESCALATE: 12` → `<r2>` = `826d284` |
| [CUT] built line | `tail -n 3 ".../setups-fixture-cut-2026-09-22.md"` | 0 | `SETUPS FIXTURE CUT BUILT 65c08a0 \| on 74eefd8 \| days: rubberband=2026-09-21 hitchhiker=none \| formed by exit code: yes \| offline 2789/0 \| with-DB 542/0 \| .env: removed, proven gone \| ESCALATE: 7` → `<cut>` = `65c08a0` |
| [R3] built line | `tail -n 3 ".../setups-fix-r3-2026-09-22.md"` | 0 | `SETUPS FIX R3 BUILT be44eb4 \| on 65c08a0 \| offline 2453/0 \| with-DB 569/3 \| src changed: yes \| tests added: 19 (one parametrised function counted as its 3 cases) \| .env: removed, proven gone \| ESCALATE: 18` → `<tip>` = `be44eb4` |
| THE CHAIN | `git -C /Users/cobalt/cobalt log --oneline 826d284..74eefd8` | 0 | exactly ONE commit: `74eefd8 fix(setups): round 2 — report` — chains |
| whole range | `git -C /Users/cobalt/cobalt log --oneline 60ddac4..be44eb4` | 0 | 14 commits, exact match to PREFLIGHT's expected list, oldest last: `be44eb4 953e22b e7a2090 b737c25 3194038 c4f5fd7 e79c815 a09c6da 65c08a0 74eefd8 826d284 52edb87 c62e593 90c9f56` |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 setups/seven-0921` | 0 | `8da261a fix(setups): round 3 — report` — sits above `<tip>` |
| staging list | `git -C /Users/cobalt/cobalt log --stat --oneline 60ddac4..be44eb4` | 0 | see `## Checked against the branch` (i) for the boundary read; one path outside every round's list found: `tests/cobalt/test_radar_anatomy.py` (touched by `c62e593`, [R2]) — the desk's R113 row already names this outside-boundary path (item b) |
| `.env` absent | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | "No such file or directory" — clean |
| r3 proposal file present | `ls .../docs/_inflight/setups-assumed-values-r3-2026-09-22.md` | 0 | present |
| round-1 folder | `ls scratch/tribunal-bars-0920/setups-one-check` | 0 | `grok-check.md`, `gemini-check.md`, `opus-check.md` present |
| recovery | `ls scratch/tribunal-bars-0920/setups-check/r2r3` | 1 | "No such file or directory" at PREFLIGHT time — fresh run |
| stagger `38` | `tail -n 1 ".../float-handicap-tribunal-2026-09-21.md"` | 0 | `FLOAT HANDICAP TRIBUNAL R1 DONE …` — not running |
| stagger `59` | `tail -n 3 ".../voice-tribunal-2026-09-22.md"` | 1 | file absent; desk's R113 row (`cto-2026-09-22.md`) names "59 is not running" AND names `70-setups-check-r2r3.md` → continue |
| stagger `63` | `tail -n 3 ".../routing-tribunal-2026-09-22.md"` | 1 | file absent; same R113 row names "63 is not running" AND `70-setups-check-r2r3.md` → continue |
| stagger HOLD 1 (`17`) | `tail -n 1 ".../setups-blind-committed-day-2026-09-22.md"` | 0 | `SETUPS BLIND COMMITTED DAY DONE …` — not running (recorded only; HOLD 1 not asked here) |
| Codex launch shape | `grep -c -F "Experiment field: **reads started**" ".../setups-tribunal-r2-2026-09-21.md"` | 0 | `1` — Sol launch (probe) appends ` < /dev/null` |
| probe: Sol | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → `sol: METER — retry after Sep 26th, 2026 6:47 AM`, SKIPPED, not relaunched |
| probe: Opus 5.5 | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | `OK` → UP |
| probe: Grok / Gemini | `--version` rows above | 0/0 | both UP |
| count | — | — | 3 of 4 UP (Grok, Gemini, Opus 5.5) — meets L67's floor of 3; every UP house launched |

## Packet
Staged in `scratch/tribunal-bars-0920/setups-check/r2r3/`:

| file | bytes | MANDATORY/guidance |
|---|---|---|
| `QUESTIONS-R2R3.md` | 13,038 | MANDATORY, read first — the question set + file list |
| `fix-diff-r2.part1.md` | 35,447 | [R2] fix diff pt.1 (commits 826d284, 52edb87, c62e593) |
| `fix-diff-r2.part2.md` | 7,173 | [R2] fix diff pt.2 (commit 90c9f56) |
| `cut-diff.md` | 24,042 | [CUT] the cut diff (docs + bars fixture excluded) |
| `cut-bars-excerpt.md` | 2,105 | [CUT] bars fixture excerpt + leak counts |
| `fix-diff-r3.part1.md` | 33,559 | [R3] fix diff pt.1 (commits be44eb4, 953e22b, e7a2090, b737c25) |
| `fix-diff-r3.part2.md` | 29,369 | [R3] fix diff pt.2 (commits 3194038, c4f5fd7) |
| `adding-a-setup-at-tip.md` | 9,404 | the how-to doc at the tip |
| `r2-report.md` | 4,970 | [R2] fixer's ESCALATE section — a CLAIM |
| `cut-report.md` | 17,050 | [CUT] hub's FIND/CUT/PIN/ESCALATE sections — a CLAIM |
| `r3-report.md` | 16,756 | [R3] fixer's PROPOSAL/DIALS/ESCALATE sections — a CLAIM |
| `classify.md` | 15,007 | the drafter's classification table |
| `rows.md` | 12,120 | his rulings R47–R51/R61 + the r3 fix-rows table |
| `proposal-keys.md` | 1,196 | [R3] proposal keys/grades only, values withheld (L32) |

**Total: 221,236 B ≈ 55.3k tokens per house (÷4). CEILING 230,000 B: under it — continue.** Drafter's estimate was ≈215 KB ≈ 54k tokens/house; actual matches closely.

Diff-completeness check (rule (47)): [R2] `grep -c "^commit "` summed = 4 (matches PREFLIGHT's 4 non-docs-only commits in `60ddac4..826d284`), `grep -c "^diff --git"` summed = 14 (matches the `--stat` list's non-docs file-touches for that sub-range). [CUT] commits = 1, diffs = 6 (matches, bars fixture excluded separately). [R3] commits = 6, diffs = 24 (matches). No mismatch — packet complete.

L32 pre-stage check on `r3-report.md`: `grep -c -F` for each of the four proposal values (`0.05`, `0.5 (`, `1.0 (`) → 0 each. No leak; staged as-is.

Written-nothing proof, baseline (before any checker launch): `ls -la scratch/tribunal-bars-0920/setups-check/r2r3` — the 14 packet files above, nothing else. `ls -la /Users/cobalt/cobalt-wt/setups-c1` — repo tree, no `.env`, `data/` empty (no symlink). Both quoted in full in this hub's own tool history.

## CONTINUE
next: nothing — all three houses answered inside the 45-minute clock (Grok launched 20:39:43, completed 20:57:55; Gemini launched 20:39:43, completed 20:43:47; Opus 5.5 launched 20:39:43, completed 20:49:38). Written-nothing proof pairs (`ls -la` of the packet folder and of `setups-c1`) taken before launch and after each completion — identical apart from files this hub wrote itself (each house's own `-check-r2r3.md`, named as it landed); no other new or changed entry. Grok did **not** self-write `grok-check-r2r3.md` through its approved `--allow` string (the same deviation round 1 recorded) — its process printed to stdout only; this hub captured stdout and wrote the file, recorded here as a deviation, not a content problem. Gemini and Opus 5.5 wrote nothing (as instructed); no tool-denial line found in either (`grep -c -i "denied\|not allowed\|permission"` = 0 on both saved files).

## Per FIX row
| tag | row | what it fixes | grok | gemini | sol | opus | checkers answering CLOSED |
|---|---|---|---|---|---|---|---|
| R2 | F1 | evaluability reads ANCHORS, `anchor:none` | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R2 | F2 | sequence steps walked as predicates | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R2 | F3 | trigger resolver reads join closure | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R2 | F4 | rollback-after-assumed-note doc section | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R2 | F5 | AWAITING_A_RULING pins | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R2 | P1 | unsupported-relation coverage pin | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| CUT | C1 | fixture is real-shape | CLOSED | CLOSED | — | **NOT CLOSED** — cutter keeps UTC clock across a DST boundary; real day also leaks into a committed test docstring | 2 of 3 |
| CUT | C2 | no value of his in the cut | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| CUT | C3 | cut reproduces the stored day's formations | CLOSED | CLOSED | — | **NOT CLOSED** — pin (long, 15:34Z) does not correspond to the stored day's BTTC formation (short, 14:24Z); report's stated reason is real but incomplete | 2 of 3 |
| R3 | F1 | backside/fashionably-late bind side via mirrored frame | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R3 | F2 | per_indicator hole reader widened | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R3 | F3 | leg.min_size_atr minimum-size rule | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R3 | F4 | FILLED card pills skip assumed_formation | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R3 | F5 | stop.buffer unit cents→dollars | CLOSED | CLOSED | — | CLOSED | 3 of 3 |
| R3 | F6 | dials-per-setup report + per-trade proof | CLOSED | CLOSED | — | **(b) CLOSED / (a) NOT CLOSED** — the reachability probe swallows any `VaultTaxonomyError` and never asserts why | 2 of 3 (a); 3 of 3 (b) |

## Proposal keys
| key | grok | gemini | sol | opus |
|---|---|---|---|---|
| `flat_threshold.ema9` (A-09) | SHOULD BE NULL — no source number | GRADE STANDS | — | GRADE STANDS |
| `flat_threshold.vwap` (A-10) | SHOULD BE NULL — no source number | GRADE STANDS | — | GRADE STANDS |
| `dist.k.vwap` (A-16) | SHOULD BE NULL — no source number | GRADE STANDS | — | GRADE STANDS |
| `leg.min_size_atr` (A-24) | SHOULD BE NULL — cited pages speak only to the with-trend move, not pullback size | SHOULD BE NULL — same reason | — | SHOULD BE NULL — same reason |

Grok's reading treats "no source number" (a word only, no figure) as disqualifying for all four; Gemini and Opus read R48/R49's "sheet-derived assumed value" rule as satisfied by a word-only passage for A-09/A-10/A-16, and draw the SHOULD BE NULL line only at A-24 (whose passages don't address pullback size at all). Quoted, not smoothed — this is a real 1-vs-2 split on where NO SOURCE NUMBER stops being enough, not a contradiction of fact.

## Questions
| Q | checker | answer |
|---|---|---|
| Q1 [R2] | grok | Yes. `closure_keys` unions trigger keys only; stop resolvers get no `tunable_keys`. A def using a stop that reads micro-range/pivot/RangeBreak keys without naming the matching atoms could form on an assumed value with no mark. All eight corpus defs already name the atoms, so the guard is empty today. |
| Q1 [R2] | gemini | Yes. Stop resolvers read keys through frame objects but don't declare them; a def using such a stop without naming the atoms would miss those keys in its closure, leaving an assumed fill unmarked. |
| Q1 [R2] | opus | Yes, by construction (`closure_keys` has no stop term). Concrete case: `pivot.n`, read by `recent_higher_low`/`range_base` stops (backside, the eighth def), is absent from their printed closures. A mark is lost only if `pivot.n`'s engine row is null — that row is not in this folder. |
| Q2 [R3] | grok | True. A note row for an engine key is refused; an assumed row is global or per_indicator with `slug=None`, so it tunes every setup reading the key — every DIALS key except hitchhiker's band. |
| Q2 [R3] | gemini | Yes, true. A note row for an engine key is refused by merge_tunables; Assumed Defaults rows are global/per_indicator, applying to all setups reading them — affects every DIALS key marked 'assumed / engine only'. |
| Q2 [R3] | opus | Largely true, but incomplete — `load_assumed_tunables` also accepts `per_trade(<loaded def>)` rows; whether one fills a global hole for one setup is `merge_tunables`'s predicate (NOT CHECKABLE). Every DIALS key except hitchhiker's band is affected; several keys are shared by 2–8 setups. |

The two open questions being open is known and is not by itself a NO on any checker's line.

## Per not-fixed row
Per L37/L70, only rows a checker actually touched (FOURTH): [R2] P1/F1's coverage pin (E4·C5) — all three AGREE WITH THE CLASS (NOT REAL). Q6.1b — Grok, Gemini, Opus AGREE (NOT REAL). C6/Q5.4/Q5.6/Q5.7 — Opus AGREE (UNPROVEN, still). Q5.9 — Opus AGREE (OUT OF SCOPE). Q3.6 — Opus AGREE (NOT REAL). Q6 — Grok, Opus AGREE (NOT REAL). Q6.2 — Opus AGREE (UNPROVEN). Q7 — Grok, Opus AGREE (NOT REAL). C14·Q8.1 — Opus AGREE (NOT REAL). Q8.4·Q12.2 — Grok, Opus AGREE (UNPROVEN). Q9.1 — Opus AGREE with the class but notes the cut does not restore real formations (ties to C3). Q9.2·Q9.3 — Opus AGREE (UNPROVEN). Q9.4, Q12.1 — Opus/Grok AGREE. Q10 — Grok, Gemini AGREE. C8–C13 — all three AGREE (HOLDS, confirmed by my own greps in `## Checked against the branch`). Every other classify.md row: NOT TOUCHED by all three. No DISAGREE was raised by any checker.

## Assertions and boundary
| tag | checker | (a) weaker assertions | (b) hunks outside allowed files | (c) L52 path |
|---|---|---|---|---|
| R2 | grok | NONE | `tests/cobalt/test_radar_anatomy.py` | NO PATH |
| R2 | gemini | NONE | NONE | NO PATH |
| R2 | opus | NONE | `tests/cobalt/test_radar_anatomy.py` | NO PATH |
| CUT | grok | NONE (5 new `DEF_WRITTEN_RUBBERBAND_CUT_*`, no existing value changed) | NONE | NO PATH |
| CUT | gemini | NONE | NONE | NO PATH |
| CUT | opus | NONE | NONE | NO PATH |
| R3 | grok | NONE | `tests/cobalt/test_setups_lego.py` (comment only) | NO PATH |
| R3 | gemini | NONE | NONE | NO PATH |
| R3 | opus | only `_tunables_digests`' unit overwrite (covered by `test_f5`) | `tests/cobalt/test_setups_lego.py`, `src/cobalt/radar/anatomy/leg_roles.py` | no path proven; NOT CHECKABLE — second-chance names `leg.pre_test` but its closure is asserted to lack `leg.min_size_atr`; the run needed is second-chance with an assumed A-24 row |

## Checked against the branch
Every NOT CLOSED, SHOULD BE NULL, weaker-assertion and outside-the-files claim, opened myself (Read on `/Users/cobalt/cobalt-wt/setups-c1/`, or `git -C /Users/cobalt/cobalt show <base>:<path>` for the pre-step text):

| tag | claim | who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|---|
| CUT | C1 not real-shape: cutter keeps UTC clock across a DST boundary | opus | `cut-diff.md:334-341` (`_shift_datetime_str`), confirmed live at `tests/fixtures/radar/_cut_setups_fixtures.py` | **HOLDS** | Only the calendar date is shifted; `rest` (HH:MM:SS+00:00) is untouched. Sep 21 2026 is EDT, Jan 7 2026 is EST — a genuine 1-hour local-time offset. |
| CUT | real day 2026-09-21 is a literal in a committed file | opus | `tests/cobalt/test_setups_fixture_cut.py:3` (grepped live in `setups-c1`) | **HOLDS** | `grep -n "2026-09-" tests/cobalt/test_setups_fixture_cut.py` prints the docstring's "real day 2026-09-21" line; also present in commit `65c08a0`'s message. Not `user_id`/trade data, but it does put back a date L45 asks be stripped. |
| CUT | C3: pinned formation (long 0.8400/0.66 @ 15:34Z) does not correspond to stored day's BTTC line (short 0.6690/0.87 @ 14:24Z) | opus, grok (grok reads the same numbers but calls it CLOSED on the report's stated reason) | `cut-report.md` FIND — rubberband vs `## PIN`; `cut-diff.md:163-174` | **HOLDS** (the numbers don't correspond) | Confirmed by reading both sections myself. The report's stated reason (production-synced def vs neutral test shape) is real, but — per the C1 finding — is not the only cause: the cut's session times are also shifted an hour, so even the SAME definition could not reproduce the stored bar. |
| R3 | F6(a): `_per_trade_accepted` treats any `VaultTaxonomyError` as "not reachable", never checks why | opus | `fix-diff-r3.part1.md:44` (the bare `except VaultTaxonomyError: return False`) | **HOLDS** | Confirmed: no assertion on the exception's message anywhere in the function. |
| R3 | the how-to / r3-report attribute the per-trade-row refusal to `merge_tunables`, but the probe's own refusal comes from `load_vault_trade_defs` | opus | `adding-a-setup-at-tip.md:18`, `r3-report.md:108` vs `fix-diff-r3.part1.md:30,44` | NOT CHECKABLE FROM READS | `merge_tunables`'s own source is not in this packet; cannot confirm which function actually raises for a per-trade-row-on-an-engine-key case. |
| R3 | `leg.min_size_atr` (A-24) SHOULD BE NULL: no source addresses pullback size | grok, gemini, opus | `r3-report.md`'s own `## ESCALATE` (i): "NO passage … speaks to how big a PULLBACK must be" | **HOLDS** | The report's own words concede this; the rulings' own rule (R48/R49: "a hole no source supports stays null") applies directly. |
| R2 | outside-the-files: `tests/cobalt/test_radar_anatomy.py` touched by [R2] (`c62e593`), not in [R2]'s CLOSE list | grok, opus (gemini said NONE — DOES NOT HOLD) | `git -C /Users/cobalt/cobalt log --stat --oneline 90c9f56` (PREFLIGHT) | **HOLDS** | Confirmed in PREFLIGHT's own `--stat` read. Already disclosed by the r2 fixer (`r2-report.md` ESCALATE vii) and already named in the desk's own R113 launch row (item b) — a known, accepted deviation, not a fresh surprise. |
| R3 | outside-the-files: `tests/cobalt/test_setups_lego.py` (comment only) and `src/cobalt/radar/anatomy/leg_roles.py` not named by `rows.md`'s fix-column text | grok/opus (lego.py); opus (leg_roles.py) — gemini said NONE | PREFLIGHT `--stat`; prompt `70`'s own §1 item 25 ([R3] boundary list) | **DOES NOT HOLD as a boundary violation** | Both files ARE explicitly named in this round's own PREFLIGHT/CLOSE boundary list for [R3] (`70`'s §1 item (25)) — the checkers are reading a narrower rule (only files `rows.md`'s "the fix" column names) than the round's actual authorized list. A row-documentation completeness point, not an unauthorized touch. |

Also checked, myself, stated plainly:
- (i) `git -C /Users/cobalt/cobalt log --stat --oneline 60ddac4..be44eb4` names only paths PREFLIGHT's per-round boundary allows, with the one exception above (`test_radar_anatomy.py`, [R2], already disclosed).
- (ii) PROTECTED PATHS, each round: [R2] `git log --oneline 60ddac4..826d284 -- configs src/cobalt/db_migrations src/cobalt/cards src/cobalt/taxonomy tests/fixtures` — EMPTY. [CUT] `git log --oneline 74eefd8..65c08a0 -- src configs` — EMPTY. [R3] `git log --oneline 65c08a0..be44eb4 -- src/cobalt/db_migrations src/cobalt/cards/store.py src/cobalt/cards/scoring.py src/cobalt/radar/anatomy/structure.py src/cobalt/radar/formation/stops.py tests/fixtures` — EMPTY. No violation on any round.
- (iii) `git log --oneline 60ddac4..be44eb4 -- tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_nine_ema.py tests/cobalt/test_setups_vwap_cont.py tests/cobalt/test_setups_second_chance.py` — EMPTY. The four files holding the existing `DEF_WRITTEN_*` pins are untouched anywhere on the fix path.
- (iv) `grep -n "DEF_WRITTEN_"` on every part: [R2] and [R3] diffs — zero hits (no context, no assignment). [CUT] diff — every hit is either prose/context or one of the five new `+ DEF_WRITTEN_RUBBERBAND_CUT_*` assignments; each compared character-for-character against the printing test's `## PIN` line in `cut-report.md` — **MATCH** on all five (side `long`, formed-bar `2026-01-07T15:34:00+00:00`, trigger `0.8400`, stop `0.66`, anchor the quoted `Anchor(...)` repr).
- (v) In every test diff, no `-` line removes an `assert` without an equal replacement in the same hunk; `grep -c "skip\|xfail"` on `+` lines: R2 part1 = 1 hit, R3 part1 = 3 hits, all four are plain-English prose ("gate 2 skips…", "health pills skip…") — zero actual `@pytest.mark.skip`/`xfail` additions. The A1 re-points named in `r2-report.md` (iv) and `r3-report.md` (iv) are each accounted for in `## Assertions and boundary` above, tagged.
- (vi) `git log -p --oneline 60ddac4..be44eb4 -- configs` — exactly the two [R3] hunks the r3 report names (`stop.buffer` `unit: cents`→`dollars`, value unchanged at `953e22b`; one new `leg.min_size_atr` row, `value: null`, at `b737c25`) and NOTHING from [R2] or [CUT].
- (vii) L32: `grep -c -F` for each proposal value (`0.05`, `0.5 (`, `1.0 (`) on `fix-diff-r2.*`, `cut-diff.md`, `fix-diff-r3.*`, `adding-a-setup-at-tip.md`, `r3-report.md` — zero hits everywhere. No proposal value entered the packet.
- (viii) [CUT] leak counts (restated from `## Packet`): `"ts":` 956 · `"ticker":` 956 · `2026-09-` 0 in the committed bars blob (but 1 hit in the committed TEST file, see the HOLDS row above) · `user_id` 0 · `@` 0 · `trade_def` 0. `grep -n "2026-09-"` on `test_setups_fixture_cut.py` and `_cut_setups_fixtures.py`: one line printed (quoted above); the cutter file itself: zero.

Where two checkers contradict each other, both are quoted above and neither is smoothed: Grok/Gemini vs Opus on [CUT] C1/C3 and [R3] F6(a); the 1-vs-2 split on the proposal grades' NO SOURCE NUMBER line; Gemini vs Grok/Opus on [R2]/[R3] FIFTH(b).

## Ready for a deploy
| checker | CHECK R2R3 line | ready | reason verbatim |
|---|---|---|---|
| grok | `CHECK R2R3: FIX STANDS · ready for a deploy prompt: YES` | YES | (no reason field given — line quoted whole) |
| gemini | `CHECK R2R3: FIX STANDS · ready for a deploy prompt: YES · all fixes pass constraints with no defects introduced.` | YES | "all fixes pass constraints with no defects introduced" |
| sol | METER | — | usage limit, retry Sep 26th, 2026 6:47 AM |
| opus | `CHECK R2R3: FIX AGAIN [CUT] C1, [CUT] C3, [R3] F6(a) · ready for a deploy prompt: NO` | NO | "cut fixture hour-shifted; cobalt_dev broken, with-DB smoke unrun" |

## FOR THE CLASSIFIER
(L75 — round 2; these go to a fix-round drafter that classifies every finding before anything is built, never straight to a fixer.)
1. **[CUT] C1 — NOT CLOSED.** Claim: the cutter's `_shift_datetime_str` shifts only the calendar date and preserves the original UTC clock string; a real day in EDT re-dated onto a synthetic day in EST shifts every bar's New York local time by one hour. Made by: Opus 5.5. `tests/fixtures/radar/_cut_setups_fixtures.py` (function `_shift_datetime_str`, and its callers `cut_bars`/`cut_membership`). **HOLDS.**
2. **[CUT] — real day literal in a committed file.** Claim: `tests/cobalt/test_setups_fixture_cut.py`'s module docstring names the real day `2026-09-21`, despite the cutter's own rule that the real day is never a literal in the cutter or in any output. Made by: Opus 5.5. `tests/cobalt/test_setups_fixture_cut.py:3`. **HOLDS.**
3. **[CUT] C3 — NOT CLOSED.** Claim: the pinned cut-day formation does not correspond to the stored day's own BTTC formation, and the report's stated reason (production-synced definition vs. the test's neutral shape) is real but incomplete — the hour-shift in (1) is a second, undisclosed cause. Made by: Opus 5.5. `cut-report.md` (`## FIND — rubberband` vs `## PIN`). **HOLDS.**
4. **[R3] F6(a) — NOT CLOSED.** Claim: the "dials reachable per setup" probe (`_per_trade_accepted`) treats every `VaultTaxonomyError` as "not reachable" without ever asserting why, so a malformed probe note would print the same table as a genuine engine-key refusal. Made by: Opus 5.5. `tests/cobalt/test_setups_fix_r3.py` (as staged, `fix-diff-r3.part1.md:44`). **HOLDS.**
5. **[R3] proposal key `leg.min_size_atr` (A-24) — SHOULD BE NULL.** Claim: neither cited source addresses pullback size (only the with-trend move), so under R48/R49's own rule ("a hole no source supports stays null") this key should not carry a proposed value. Made by: Grok, Gemini, Opus 5.5 (unanimous). `docs/_inflight/setups-assumed-values-r3-2026-09-22.md` row A-24 (read by the hub); `r3-report.md`'s own ESCALATE (i) concedes the same gap. **HOLDS.**
6. **[R2] outside-the-files — `tests/cobalt/test_radar_anatomy.py`.** Claim: touched by commit `c62e593` ([R2] F2), not in [R2]'s own CLOSE list. Made by: Grok, Opus 5.5. PREFLIGHT's own `--stat` read. **HOLDS** — but already disclosed by the r2 fixer and already carried in the desk's own R113 launch row; not a fresh surprise, recorded here per the standing rule.

## FOR DEJAN
(Owner items, quoted from the checkers' answers; no recommendation added.)
- **Q1 [R2] — stop resolvers and `tunable_keys`.** All three checkers agree: `closure_keys` unions the trigger resolver's declared reads (this round's own fix) but stop resolvers still declare none, so a stop that reads an undeclared engine key (Opus names `pivot.n`, read by `recent_higher_low`/`range_base` stops) could in principle sit outside a def's closure. All three note the eight corpus defs already name the matching atoms, so no live def is affected today — the gap is latent, not active.
- **Q2 [R3] — per-setup tuning of an engine dial.** All three checkers confirm the report's own finding: a note row for an engine key is refused, and an `Assumed Defaults` row tunes every setup that reads that key (`global`/`per_indicator` scope), not one setup alone. Only a def's own `cfg(<trade_key>.…)` keys are per-setup (today: hitchhiker's duration band). If "tune the setups so the noise subsides" (R61) is meant per-setup, the only lever today is writing the number into each def's own text.

## ESCALATE
1. Opus 5.5's `FIX AGAIN` on [CUT] C1, [CUT] C3, [R3] F6(a) — see `## FOR THE CLASSIFIER` items 1, 3, 4.
2. [CUT] C1 NOT CLOSED — HOLDS (classifier item 1).
3. [CUT] real-day literal in a committed test docstring — HOLDS (classifier item 2).
4. [CUT] C3 NOT CLOSED — HOLDS (classifier item 3).
5. [R3] F6(a) NOT CLOSED — HOLDS (classifier item 4).
6. [R3] `leg.min_size_atr` SHOULD BE NULL — HOLDS (classifier item 5).
7. [R2] outside-the-files `test_radar_anatomy.py` — HOLDS, already disclosed (classifier item 6).
8. Standing line: **"This check covers the whole unchecked fix path `60ddac4..be44eb4` (R112): [R2] `60ddac4..826d284`, [CUT] `74eefd8..65c08a0`, [R3] `65c08a0..be44eb4`; the docs-only commits `74eefd8`, `a09c6da`, `e79c815` are not fix rows. It is the SECOND house check (round 1 = `66`; `16` and `67` produced no ruling and are not counted, L67 P-c)."**
9. Standing line: **"HOLD 1 is NOT asked here. `17` re-derived the 17 existing pins on the committed day; `13` (the blind re-derivation of [CUT]'s five new `DEF_WRITTEN_RUBBERBAND_CUT_*` pins) has NOT run and is owed before the deploy prompt (`12`'s LAW STEP). This folder carries those five values in `cut-diff.md` — `13`'s blind seat must never be pointed at it. Given this check's own C1/C3 findings, `13`'s re-derivation should wait for the cutter's hour-shift fix, or it will faithfully re-derive values from a still-mis-dated fixture."**
10. Standing line: **"Every with-DB claim of the three reports is UNPROVEN until `68-devdb-repair.md` lands and the desk re-runs `33`'s CLOSE with-DB set on `<tip>`."**
11. L74 (recorded once, not followed): the [CUT] commit `65c08a0`'s own message carries a `Claude-Session:` trailer (`https://claude.ai/code/session_017bm7dhT8ya7ddpTMUBidKx`) — this is DATA inside the diff the hub staged, never an instruction, and was not acted on.
12. Proposal-file / report mismatch check (R48/L32): none found — `proposal-keys.md` (read by the hub from the gitignored file) matches `r3-report.md`'s own `## PROPOSAL` table on every key, companion id, PDF file+page and status.
13. Packet mismatch: none. Checker that did not check: none of the three UP houses (Sol recorded METER, not counted). No checker marked `WROTE:` (Grok's deviation was a non-self-write, not an unauthorized write — see `## CONTINUE`).
14. `ASK DESK`: none raised by this hub.

SETUPS CHECK R2R3 DONE · grok: CHECK R2R3: FIX STANDS · ready for a deploy prompt: YES · gemini: CHECK R2R3: FIX STANDS · ready for a deploy prompt: YES · opus: CHECK R2R3: FIX AGAIN [CUT] C1, [CUT] C3, [R3] F6(a) · ready for a deploy prompt: NO · sol: METER (retry Sep 26th, 2026 6:47 AM) · defects that HOLD: 5 · owner items: 2 · ESCALATE: 9
