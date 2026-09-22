## §0 Headline
- Grok and gemini ruled round 2 in full (2 of 3 houses); astra `SKIPPED — METER at probe` (R13, expected); the Fable seat rules blind, beside this hub, never read here.
- R2-1 (gates H1, TIER-BOUND vs POOL-WIDE): **SPLIT** — grok `ADOPT B` (pool-wide, withdrawing its own R1 tier-bound ruling); gemini `OWNER` (his call; would build A — tier-bound — if silent). R2-1.2 alone converged (`ADOPT B` 2-0).
- R2-2 (gates H2, storage + counterfactual): **CONVERGED** — both `ADOPT B` on storage (JSONB `decisive` flag, no CHECK/migration) and the same mechanism on the predicate (full second `decide()` with stickiness + held seats).
- Items converged: 1 of 2 · owner: 1 (R2-1.1 only) · ESCALATE: 0 · redactions: 0 (no value of his appeared in the packet or either ruling — checked).
- Closing lines: grok `TRIBUNAL R2: BUILD` · gemini `TRIBUNAL R2: BUILD AFTER the owner resolves the tier-bound versus pool-wide rank division`.

## AUTHORIZATION
- R13 (13:33 ET, `cto-2026-09-20.md:86`) — approves the strings this line carries. Found.
- R23 (17:47 ET, `cto-2026-09-20.md:206`) — extends `Bash(grok *)`/`Bash(agy *)` through 2026-09-21 23:59 ET. Found.
- R28 (12:40 ET, `cto-2026-09-21.md:39`) — soft-penalty ruling, carries "I don't want to exclude tickers". Found, phrase confirmed.
- R39 (16:48 ET, `cto-2026-09-21.md:50`) — extends `Bash(grok *)`/`Bash(agy *)` through 2026-09-22 23:59 ET, phrase "Bash(agy *) through 2026-09-22 23:59 ET" confirmed.
- R13 (09:4x ET, `cto-2026-09-22.md:39`) — "this week's design tribunals run on Grok · Gemini · Fable without Astra", phrase "without Astra" confirmed.
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-22 23:59 ET" -- "docs/40 - DevDocs/reports/cto-2026-09-21.md"` → `3ecbb278de133f1838d217e9745728ed6d6337e9` (non-empty). PASS.
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"FLOAT HANDICAP DERIVED v2" -- "docs/40 - DevDocs/reports/float-handicap-tribunal-derive-2026-09-21.md"` → `fd55746ddd25d8e83c478a0baa6173cf309249bc` (non-empty). PASS.
- `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/30 - Design/FLOAT-HANDICAP-v2-2026-09-21.md"` → `fd55746ddd25d8e83c478a0baa6173cf309249bc` (non-empty). PASS.
- `tail -n 3` of the derive report: last non-blank line is `FLOAT HANDICAP DERIVED v2 · folds: 26 · verbatim: 18 · needs round 2: 2 · owner items: 13 · ESCALATE: 6` — starts as required, carries "needs round 2: 2". PASS.
- No-new-rule check against `08-bars-chunk-e-check.md`: all 14 allow strings + 3 deny strings counted ≥1 (grok/agy strings counted 2 each; every other string counted 1). PASS — this launch line adds no rule.
- DATE GATE row 1: `date` → Tue Sep 22 11:24:15 EDT 2026 — before 2026-09-23, outside both blackout windows (19:25–20:45, ≥23:20 ET) → ALLOWED.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| date gate row 1 | `date` | 0 | Tue Sep 22 11:24:15 EDT 2026 — before 2026-09-23, outside both blackout windows → ALLOWED |
| grok present | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` → ALLOWED |
| agy present | `agy --version` | 0 | `1.2.8` → ALLOWED |
| round-1 folder exists | `ls scratch/tribunal-bars-0920/float-handicap-tribunal` | 0 | lists `r1` → ALLOWED |
| RECOVERY check | `ls scratch/tribunal-bars-0920/float-handicap-tribunal/r2` | 1 | "No such file or directory" → fresh run, not a resume |
| stagger | `tail -n 1 setups-blind-committed-day-2026-09-22.md` | 0 | last line starts `SETUPS BLIND COMMITTED DAY DONE ...` → not running → ALLOWED |
| astra probe (gate for astra ONLY) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 1 | usage-limit error, verbatim: "You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 26th, 2026 6:47 AM." → `astra: SKIPPED — METER at probe` (EXPECTED per R13); grok and gemini still run |
| date gate row 2 (pre-launch) | `date` | 0 | Tue Sep 22 11:34:18 EDT 2026 — still ALLOWED, outside both windows |

## Packet
Staged in `scratch/tribunal-bars-0920/float-handicap-tribunal/r2/`. `this shell's grep is ugrep, which honours .gitignore by default on a recursive search` (stated in `greps.txt`).

| file | bytes | note |
|---|---|---|
| `NEEDS-ROUND-2.md` | 3682 | derive report lines 76-87 verbatim |
| `v2-sections.excerpt.md` | 31436 | v2 design doc sections carrying R2-1/R2-2 |
| `hub-checks.md` | 1527 | round-1 hub file-checks the two items cite |
| `fable-r1.excerpt.md` | 8637 | Fable seat round-1 wording, whole, on both items |
| `grok-r1-own.excerpt.md` | 14792 | [RAW RULING — Grok's own, for Grok only] |
| `gemini-r1-own.excerpt.md` | 2721 | [RAW RULING — Gemini's own, for Gemini only] |
| `pool.excerpt.py` | 12017 | src/cobalt/radar/pool.py excerpts |
| `models.excerpt.py` | 2694 | src/cobalt/radar/models.py excerpts |
| `runner.excerpt.py` | 1006 | src/cobalt/radar/runner.py excerpt |
| `replay.excerpt.py` | 5120 | replay/movers.py, replay/models.py, replay/line.py excerpts |
| `migrations.excerpt.sql` | 1600 | 0004/0009 CHECK excerpts |
| `store.excerpt.py` | 3814 | src/cobalt/radar/store.py excerpt |
| `evaluate.excerpt.py` | 1185 | src/cobalt/radar/evaluate.py FORMULA_FILES excerpt |
| `greps.txt` | 15680 | full pre-run search output |
| `QUESTIONS-R2.md` | 8949 | verbatim + Files-in-this-folder paragraph |
| **total** | **114860** | ≈112.2 KB — under the 115 KB drop threshold; no files dropped |

NOT RESTAGED: `../r1/` (round 1's packet) — named as open-only-if-a-ruling-turns-on-it, by line range.

## CONTINUE
Both houses launched together, `run_in_background`, one attempt each, 20-minute timeout. Launch time (from `date`): Tue Sep 22 11:35:54 EDT 2026 (both grok and gemini launched within the same minute, sequential Bash calls in one message). 20-minute deadline: **11:55:54 ET**. next: await completion notifications; enforce TIMEOUT at 11:55:54 ET if either house has not finished.

## Clock
| time | trigger | running houses (min since launch) | action |
|---|---|---|---|
| 11:24:15 ET | date gate row 1 | — | preflight |
| 11:34:18 ET | date gate row 2 (pre-launch) | — | preflight |
| 11:35:54 ET | both houses launched | grok 0m, gemini 0m | launched, background |
| 11:36:25 ET | Fable-claims file-check step (C1/C2) | grok <1m, gemini <1m | continuing file-check while houses run |
| 11:36:28 ET | Fable-claims file-check step (C3/C4) | grok <1m, gemini <1m | continuing |
| 11:36:31 ET | Fable-claims file-check step (C5/C6) | grok <1m, gemini <1m | continuing |
| 11:36:33 ET | Fable-claims file-check step (C7/C8) | grok <1m, gemini <1m | continuing |
| 11:36:35 ET | Fable-claims file-check step (C9) | grok <1m, gemini <1m | continuing |

## Fable round-1 claims, file-checked
| claim | file:line | verdict | ≤30 words |
|---|---|---|---|
| C1: after the `first_from` time the screen whose override sets it gets `first = 0` (`pool.py:161`) and the `min` at `:165` sorts on `first` before `position` | `pool.py:161`, `:165` | HOLDS | `first = 0 if first_from and now...>= first_from else 1`; `min(positions)` where tuple is `(first, position, ...)` — `first` compares first. |
| C2: the key tuple is `(priority[group], first, position, order, ticker)` (`pool.py:209`) | `pool.py:209` | HOLDS | Read directly: `return (priority[group], first if group == "screens" else 0, position, order, ticker)`. |
| C3: under the proposal's division, a `first_from`-screen name ranked last of N < `cap` equity names is still admitted whatever `handicap.factor` is (`pool.py:209`, `:332-333`) | `pool.py:209`, `:332-333` | HOLDS (logic); N<cap on real scans UNVERIFIABLE FROM READS | All N screen names share `first=0`, beating every `first=1` name at same priority; if N<seats all N are in `winners`. Real-scan N<cap is v2 X2. |
| C4: `movers.py:444-447` raises `ReplayInputError` when a never-admitted episode's `excluded_by` is outside `EPISODE_EXCLUSIONS` (`:102`) | `movers.py:102`, `:444-447` | HOLDS | Read directly: `if chosen.excluded_by not in EPISODE_EXCLUSIONS: raise ReplayInputError(...)`. |
| C5: "no rollback in the tree has ever narrowed a CHECK — `0004`/`0008`/`0009` rollbacks checked" | `0004_radar_pool.rollback.sql`, `0008_radar_value_movers.rollback.sql`, `0009_picks_missed.rollback.sql` | HOLDS | `grep -n CHECK` on all three rollback files: zero matches; `0004`'s rollback DROPs the whole table instead of narrowing a CHECK. |
| C6: `line.py:97` counts CARD gates only; the mover line prints `excluded_by` at `:119` | `line.py:97`, `:119` | HOLDS | `:97` `counts[row["excluded_by"]]` iterates `card_rows` only; `:119` is inside the separate `mover_rows` block, prints `r['excluded_by']`. |
| C7: `movers.py:452-458` builds the episode entries of `gate_detail.episodes` a `decisive` flag would be copied into | `movers.py:452-458`, `:461-466`, `:480` | HOLDS | `episode_json` built at `:452-458` is assigned to `gate_detail["episodes"]` at `:466` and `:480`. |
| C8: a newcomer inside `winners` can still lose its seat to a sticky member (`pool.py:366-378`) | `pool.py:366-378` | HOLDS | `retained_below` (sticky, within grace) evicts `loser = max(available, key=ranks[ticker])`, the worst newcomer still in `provisional`/`winners`. |
| C9: `FORMULA_FILES` (`evaluate.py:144-152`) does not list `radar/pool.py` | `evaluate.py:144-152` | HOLDS | Read directly: `evaluate.py`, `anatomy/*.py`, `cards/scoring.py`, `cards/health.py`, `cards/radar.py`, `cards/expire.py`, `aset/engine.py` — no `radar/pool.py`. |

Fable R1 claims checked: 9 HOLD of 9 checked (C3's real-scan sub-claim named UNVERIFIABLE FROM READS, per the derive's own X2).

| time | trigger | running houses (min since launch) | action |
|---|---|---|---|
| 11:38:00 ET | gemini completion notice | grok ~2m, gemini done | wrote `gemini-ruling-r2.md` byte-for-byte |
| 11:38:18 ET | pre-write clock check | grok ~2m | awaiting grok |
| 11:48:02 ET | scheduled fallback wakeup | grok ~12m | grok `grok-ruling-r2.md` present on disk, mid-write; still under 20m budget, continued waiting |
| 11:50:07 ET | grok completion notice | both done | read and staged `grok-ruling-r2.md` |

Both houses answered inside the 20-minute budget (launch 11:35:54 ET; deadline 11:55:54 ET). GEMINI printed at 11:38:00 ET (hub wrote `gemini-ruling-r2.md` byte for byte, 30 lines, no `[exited with code 0]` trailer). GROK wrote `grok-ruling-r2.md` itself, completing at 11:50:07 ET (59 lines).

## Rulings table
| question | grok | gemini | agreement | ADOPT WITH / OWNER gist (≤25 words/house) |
|---|---|---|---|---|
| R2-1.1 | ADOPT B (POOL-WIDE) | OWNER (his — tier breach vs penalty bite; defaults to A if silent) | split, 1 of 2 ruled a clean verdict | grok: R28's "earns the seat" reading is pool-wide; withdraws R1 tier-bound. gemini: both A and B compromise a ruled requirement — his call; would build A if silent. |
| R2-1.2 | ADOPT B | ADOPT B | 2-0 ADOPT B | grok: the position-basis hole already exists in `raw_rank` at `h=1`; fixing it would break the `h=1`/stored-membership dry-run invariant. gemini: changing the basis breaks X12's `h=1` parity requirement; `_metric_position` stays as-is. |
| R2-2.1 | ADOPT B | ADOPT B | 2-0 ADOPT B | grok: withdraws R1 enum; `line.py:97` never counted pool exclusions; a reverted enum crashes replay, a JSONB flag does not. gemini: enum fails the revert scenario at `movers.py:444-447`; grok's own R1 `line.py:97` support was wrong. |
| R2-2.2 | ADOPT WITH (full second `decide()`, pool-wide re-sort, stickiness + held seats; `decisive` lives in H1's JSONB, not a new column) | ADOPT A (full second `decide()`) | 2-0 same mechanism (A) | grok: walks own 11:00 ET scenario — B does not mislabel it as originally claimed, but a second pool (factor 0.4) shows B ignoring stickiness does mislabel. gemini: same scenario, same correction of R1's own claim; B "deliberately ignores stickiness". |
| closing line | `TRIBUNAL R2: BUILD` | `TRIBUNAL R2: BUILD AFTER the owner resolves the tier-bound versus pool-wide rank division` | — | — |

Per-item summary:
| item | verdict | why |
|---|---|---|
| R2-1 (R2-1.1 + R2-1.2) | **SPLIT** | R2-1.1 answers differ in kind (ADOPT B vs OWNER); R2-1.2 converges but R2-1 as a whole needs both questions to match. |
| R2-2 (R2-2.1 + R2-2.2) | **CONVERGED** | Both questions: same answer (R2-2.1 ADOPT B 2-0) or the same mechanism shown identical (R2-2.2: grok's ADOPT WITH text and gemini's ADOPT A are both "full second `decide()` including stickiness and held seats" — same test, same inputs). No supporting claim for either answer DOES NOT HOLD in the file-check below. |

Items converged: 1 of 2. The Fable seat is not counted here (never read); the second derive counts it.

## Wording offered, verbatim

**R2-1.1 — grok, ADOPT B:**
"R28's seat is earned on the lowered score ("still in the pool if it earns it"), whatever source brought the name in. That is pool-wide. I withdraw R1's ADOPT of O4 / (k)."
"Fable's claim holds once `N < cap` is corrected to `N ≤ seats`. After `first_from`, screens before lists (`models.py:104`; key `pool.py:209`): `first = 0` (`pool.py:161`) and `min` (`:165`) put that screen's name at `(0, 0, N/h)`, which beats every `(0, 1, …)` at any finite `h`. If `N ≤ seats` (`pool.py:332-333`) every one of those names is in `winners` whatever `handicap.factor` is, so under A it did not earn the seat. Literal "N < cap" fails when held seats consume the cap: 11:00 ET, `cap = 50`, 45 held, that screen has 10 equity names — `seats = 5`, five names are outside `winners` at `h = 1`. The substance stands: `h` still cannot put any of the ten behind another screen or a list."
"Grok's claim also holds, and it is the requirement, not a defect. 10:00 ET, `priority` screens then lists, `cap = 50`, held empty, 30 screen names. LOWF `raw_rank` 30, LISTY `raw_rank` 31, `handicap.factor` 0.9 → `eff` 33.3 > 31, so the re-sort after `pool.py:326` places the screen name behind the list name. That weakens `priority` and, by the same division, `first_from`. R28 is his word for it; O4 was the proposal's question. Named here, not silent (L53)."
"Smaller mechanism: `_ranked()` untouched, one re-sort in `decide()` after `:326`, same file, chunk H2, no migration. Held names stay out of `ordered`. B's text is taken whole, including shadow (would-be stored, not used) and the unhandicapped-wins tie."

**R2-1.1 — gemini, OWNER (his — L53 dictates priority and first_from are his, but strict tier bounds can nullify R28's penalty intent):**
"Under A (TIER-BOUND), Fable's scenario holds: after `first_from`, an equity on that screen gets `first=0` (`pool.py:161`) and its key `(0, 0, N/h, ...)` beats all other screens `(0, 1, ...)` (`pool.py:209`). A handicapped name there auto-admits regardless of `h`, rendering R28's "competes on its LOWERED score" false. Under B (POOL-WIDE), `h` divides `raw_rank`, allowing a screen name to fall behind a list name `(1, ...)`, which weakens his `priority` tier (L53). Since both choices compromise a requirement, only he can weigh the tier breach against the penalty's bite. If silent, I build A to strictly preserve his L53 tiers."

**R2-1.2 — grok, ADOPT B:**
"Under B the basis still moves `raw_rank`, which is why H2 must not "fix" it. Not-equity is appended to `source.tickers` before `is_not_equity` (`runner.py:139-145`) and is gone from `candidate_map` before `_ranked`, but `_metric_position` still sorts `source.tickers` (`pool.py:94-106`). Those holes already change cross-screen order at `h = 1`. `raw_rank` is the dense index among candidates; the hole is already inside it. Dividing that index does not require an edit to `_metric_position`. X15 measures the hole. It does not license an `h = 1` order change (X12)."
"H1 stores, from R2-1 B: `raw_rank` (the `_ranked()` index, no factor), `handicap_factor`, and `handicap` JSONB whose `position` / `effective_position` are the would-be pool-wide rank. Shadow does not use that rank. `decisive` is a key in that same JSONB, written at H2, not a new column."

**R2-1.2 — gemini, ADOPT B:**
"Changing the position basis (A) to drop not-equity and manual-exclude rows before computing `_metric_position` alters the raw rank order even when `h = 1`. This directly violates the dry-run invariant (X12) where the `h = 1` pass must perfectly reproduce the stored `radar_membership` of past days. As X15 shows, a basis change breaks historical parity, masking the handicap's true impact and voiding the dry-run. `_metric_position` (`pool.py:97-105`) must stay exactly as it is over `source.tickers`."

**R2-2.1 — grok, ADOPT B:**
"I withdraw R1's enum. `line.py:97` counts `card_rows` into `CARD_GATES`. It does not group mover exclusions. The mover segment prints `excluded_by` at `:119`. A JSONB flag is invisible there only if that print is left alone; B changes `:119` to `config_cap (handicap)`. The card counts need no new key."
"Evening N writes nothing but `config_cap` under B, so this is A's failure, not B's. Evening N, H2 live, LOWF never admitted, `radar_membership.excluded_by = 'handicap_cap'`. Evening N+1, H2 reverted. Replay of day N hits `movers.py:444-447`: `handicap_cap` is not in `EPISODE_EXCLUSIONS` (`:102`) → `ReplayInputError`. That night's miss line does not run. B's row still says `config_cap`, which the reverted set accepts, and `decisive` remains in H1's JSONB."
"No second copy (L3), no CHECK edit (`0004:42`, `0009:76`), no migration. Two edits: the episode JSON in `movers.py` and `line.py:119`. X16 is the enum rollback; it is not a gate for B."

**R2-2.1 — gemini, ADOPT B:**
"Grok's `handicap_cap` Enum value fails Fable's rollback scenario. If H2 is reverted on evening N+1, the `EPISODE_EXCLUSIONS` set in `movers.py:102` shrinks to four values, but day N's rows still carry `handicap_cap`. Replaying day N crashes at `movers.py:444-447` with `ReplayInputError`, failing the miss line. Furthermore, grok's claim that `line.py:97` counts pool exclusions is factually wrong; it counts card gates. A JSONB flag safely avoids both the migration and the revert crash."

**R2-2.2 — grok, ADOPT WITH:**
"`handicap.decisive` is set true only on a `config_cap` EXCLUDE or LEAVE whose applied factor is below 1, and only when a second `decide()` — that name's factor set to 1, every other input unchanged — admits that name (`ADMIT`, `RETAIN`, or `HOLD`) where the real `decide()` does not. Both calls use the pool-wide re-sort and include stickiness and held seats. Membership in `winners` is not the test. `excluded_by` is not changed. The module that computes `h` is added to `FORMULA_FILES` (`evaluate.py:144`). `pool.py` is not."
"Grok's 11:00 ET pool, walked on `:332-378`. `cap = 3`, held empty, `seats = 3`. Order OLD1, OLD2, LOWF, STICKY. `winners` includes LOWF (`:333`). STICKY's streak goes 1 → 2, not past `stickiness_scans` 3 (`:349-356`); LOWF is the only newcomer, so STICKY takes that seat (`:366-375`) and LOWF is EXCLUDE (`:397`). LOWF is not outside `winners`, so B is false and the label stays `config_cap`. B does not mislabel this pool. The definition says what it labels, and here it matches full admission."
"B mislabels the next pool, same clock. Opens: OLD1, BIG, STICKY (`below_cap_streak` 1). Raw order OLD1, LOWF, BIG, STICKY; LOWF is the only newcomer. At factor 1, LOWF is inside `winners` and stickiness still excludes LOWF. At `handicap.factor` 0.4, `eff` is 5, order OLD1, BIG, STICKY, LOWF, and `(2, 0, 2)` beats `winners[-1]`. B sets `decisive`. The second `decide()` does not admit LOWF, so the cause is stickiness at both factors. The miss line must not say otherwise."
"`winners[-1]` is also undefined when `seats = 0` (`held` fills `cap`, `ordered[:0]`). Price of the replacement: one extra `decide()` per `config_cap` name, same function, H2, no migration. X13 chooses inline or post-scan and does not change the test."

**R2-2.2 — gemini, ADOPT A:**
"Walking grok's scenario through `pool.py:332-378`: with `cap=3`, LOWF is inside `winners`, so B evaluates `outside winners` as false, correctly yielding `config_cap` (grok's math fails his own objection). However, if adjusted so LOWF falls outside `winners` (`cap=2`), B evaluates `raw_rank < winners[-1]` as true and flags it `decisive`. Yet a full `decide()` with `h=1` shows stickiness evicts LOWF anyway (`pool.py:366-375`). B deliberately ignores stickiness, mislabeling the true cause. A's second `decide()` natively computes the true counterfactual, and as an in-memory sort, it is cheap enough to run per `config_cap` name (X13)."

## Fable round-1 claims, file-checked
(see table above, run WHILE the houses ran)

## Checked against the files
| claim | who | file:line | verdict | ≤30 words |
|---|---|---|---|---|
| screens before lists is `priority` key component 0 | grok | `models.py:104`, `pool.py:209` | HOLDS | = C2. `priority: list[Literal["screens","lists"]]`; key tuple starts `priority[group]`. |
| `first = 0` after `first_from`; `min` sorts `first` before `position` | grok, gemini | `pool.py:161`, `:165` | HOLDS | = C1. Read directly, same as Fable's claim. |
| `seats = max(0, pool.cap - len(held))`, `winners = ordered[:seats]` | grok | `pool.py:332-333` | HOLDS | Read directly in `pool.excerpt.py`; supports grok's "N ≤ seats" correction to Fable's "N < cap". |
| one re-sort point after `_ranked()` call | grok | `pool.py:326` | HOLDS | `pool.excerpt.py`: `ordered, ranks, source_for, values = _ranked(ranked_candidates, pool, source_rows, now)` is exactly at that call site. |
| not-equity rows enter `tickers`/`metrics` before `is_not_equity` excludes them | grok | `runner.py:139-145` | HOLDS | Read directly: `tickers.append`/`metrics[ticker]=` at :137-142, `is_not_equity(...)` check and `excluded.add` at :144-145, after. |
| `_metric_position` sorts `source.tickers`, unaffected by candidate-level exclusion | grok, gemini | `pool.py:94-106` | HOLDS | = staged `_metric_position` excerpt; sorts `source.tickers` directly, no `candidate_map` filter. |
| `line.py:97` counts `card_rows` into `CARD_GATES`, not pool/mover exclusions | grok, gemini | `line.py:97` | HOLDS | = C6, = F-24 in the derive. Confirms grok's own R1 claim ("miss line already counts by `excluded_by`") DOES NOT HOLD, as both houses now state themselves. |
| mover segment prints `excluded_by` at `:119` | grok | `line.py:119` | HOLDS | = C6. |
| revert of `EPISODE_EXCLUSIONS` after a `handicap_cap` write raises `ReplayInputError` on replay | grok, gemini | `movers.py:102`, `:444-447` | HOLDS | = C4, = Fable's O6 dissent. |
| CHECK locations for a hypothetical enum addition | grok | `0004_radar_pool.sql:42`, `0009_picks_missed.sql:76` | HOLDS | = migrations excerpt; both CHECKs list the current four values only. |
| stickiness eviction of the only newcomer inside `winners` | grok, gemini | `pool.py:332-378` (`:333`, `:349-356`, `:366-378`, `:397`) | HOLDS | = C8. Walked scenario matches code: `winners` includes LOWF, `retained_below` sticky member displaces the worst newcomer via `loser = max(...)`. |
| `winners[-1]` undefined when `seats = 0` | grok | `pool.py:332-333` | HOLDS | `held` is trimmed to at most `pool.cap` (eviction block above `:332`, not excerpted further but consistent with `:312-321`); `seats = max(0, cap-len(held))` can be 0, `ordered[:0]` is `[]`. |
| `FORMULA_FILES` does not list `radar/pool.py` today | grok (forward citation) | `evaluate.py:144-152` | HOLDS | = C9. A design recommendation for H2, not a claim about current behavior. |

No claim from either house DOES NOT HOLD.

## Experiments named (L70)
| experiment | named by | = v2 X<n> or NEW | gates which chunk | result that would change the design |
|---|---|---|---|---|
| X2 | grok (cited, not restated), gemini (cited, not restated; also listed under EXPERIMENTS) | = v2 X2 | R2-1, H1 dry-run wording | grok: does not move R2-1.1 either way — a `first_from` screen that fills `cap` only hides A's failure, it does not revive it. |
| X12 | gemini (cited, listed under EXPERIMENTS) | = v2 X12 | H1's `shadow → live` approve | Any `h=1` / stored-membership mismatch voids the dry-run figures. |
| X13 | grok, gemini (both cited) | = v2 X13 | R2-2, H2 | Chooses inline vs. post-scan timing for the second `decide()`; does not change the predicate itself. |
| X15 | grok, gemini (both cited) | = v2 X15 | R2-1 (position basis), H2 | grok: does not license an `h=1` order change to `_metric_position`. gemini: confirms not-equity rows don't break `h=1` parity. |
| X16 | grok (cited, not restated) | = v2 X16 | R2-2, H2 rollback file | grok: not a gate under ADOPT B (no CHECK is narrowed under the JSONB-flag mechanism). |

No new (non-v2) experiment was named by either house.

## OWNER answers
**grok:**
- "`handicap.factor`, `handicap.missing`, `handicap.combinator` — his values, read after this tribunal, not a precondition; H1 ships the keys with the block absent until he writes them." — precondition to build: no.
- "Shadow length, and the typed approve that sets `handicap.mode` live — his; until that approve the re-sort is stored and not used." — precondition to build: no.

**gemini:**
- R2-1.1 answered `OWNER (his — L53 dictates priority and first_from are his, but strict tier bounds can nullify R28's penalty intent)`, with "If silent, I build A to strictly preserve his L53 tiers." — precondition to build: no (a default is named).
- OWNER list (7 items, verbatim): (1) pool-wide vs tier-bound — does the lowered rank cross `priority`/`first_from` boundaries; (2) `handicap.factor` — numeric size, after H1 dry-run; (3) `handicap.combine` — `any`/`all`; (4) `handicap.missing` — `apply`/`skip`; (5) shadow mode duration before approving H2 live; (6) tie rule confirmation (unhandicapped name wins on exact tie); (7) whether a `handicap_cap` exclusion gets a separate badge on the `/radar` pool view. — precondition to build: no.

## Independence
- `grep -c -F -e "-ruling" grok-ruling-r2.md` → 0.
- `grep -c -F -e "-ruling" gemini-ruling-r2.md` → 0.
- `grep -c -F -e "gemini-r1-own" grok-ruling-r2.md` → 0.
- `grep -c -F -e "grok-r1-own" gemini-ruling-r2.md` → 0.
No independence breach. Neither house opened the other's ruling or the other's round-1-own excerpt.

## ESCALATE
None triggered: no `DO NOT BUILD`; no supporting claim DOES NOT HOLD; no second ranking authority found to HOLD (L52 b); no OWNER item written as a precondition; packet 114860 B, under the 115 KB drop threshold; both houses ruled (2 of 3, astra SKIPPED per R13, floor met); no independence breach; astra's probe row is exactly `SKIPPED — METER at probe`; no `ASK DESK` needed this run.

Note for the second derive, not an ESCALATE trigger under this file's own list: R2-1 is SPLIT (R2-1.1: grok ADOPT B vs gemini OWNER-leaning-A-if-silent) — per L39, if this does not converge in the round-2 derive it goes to Dejan, never a vote, never a round 3.

## 4. Close
| time | trigger | running houses | action |
|---|---|---|---|
| 11:52:49 ET | close | none (both done) | replacing in-progress last line, writing final stop line |

FLOAT HANDICAP TRIBUNAL R2 DONE · grok: TRIBUNAL R2: BUILD · gemini: TRIBUNAL R2: BUILD AFTER the owner resolves the tier-bound versus pool-wide rank division · astra: SKIPPED — METER at probe · houses that ruled: 2 of 3 · items converged: 1 of 2 · owner: 1 · ESCALATE: 0
