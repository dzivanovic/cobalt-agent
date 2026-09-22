# FACTS PACKET — float handicap H1 (NOT a prompt; the builder of `27-handicap-h1-build.md` reads it at STEP-0), 2026-09-22

Drafted by the Opus prompt seat `handicap-h1-draft-0922` (12:35 ET, `date`), from reads only: v3 `docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md`, the derive-r2 report `docs/40 - DevDocs/reports/float-handicap-tribunal-derive-r2-2026-09-22.md`, `cto-2026-09-22.md` §4 R26, and the code on main `d2d82e7`. **Keys only.** No threshold, factor, cap, time or filter value of his appears here (L32). Every `file:line` below is a CLAIM of this seat, re-read by you before you rely on it (L35).

## 1. THE RULING — R26 "B" (his, 12:28 ET, `cto-2026-09-22.md` §4 row R26)

He answered the desk's A/B on R2-1.1 with **"B" = POOL-WIDE division**. R2-1.2 stays converged ([R2F-02]: `_metric_position` untouched). The tribunal is CLOSED. v3 + R26 is the FINAL. Astra reads it Sat 2026-09-26 (R13); every `ASTRA PENDING (R13)` mark stays.

**Position B, verbatim, from the derive-r2 report's `## OPEN FOR DEJAN` block. This is the text you paste into v3 at STEP-0:**

> **B — POOL-WIDE, Fable (round-1 item (c), ADOPT WITH replacement); grok round 2 `ADOPT B`:** "`_ranked()` is untouched. After `pool.py:326`, when the block is present: `eff[t] = Decimal(raw_rank[t]) ÷ factor[t]` (`factor` = `handicap.factor` for an in-group name, 1 otherwise; a `Decimal` field, never a float); `ordered` is re-sorted by `(eff, in_group, raw_rank)` — on an exact tie the unhandicapped name wins; `ranks` is rebuilt from that order. In `mode: shadow` the re-sort is computed, stored as the would-be rank and NOT used. `raw_rank` and `rank` both ride the `Transition`. The group values come from the source `source_for[ticker]` names."

What B costs him, in the desk's words to him (R26): a list name can overtake a handicapped screen name, and after `first_from` another screen's name can overtake a handicapped `first_from` name. His `priority` and `first_from` are weakened for handicapped names only. That cost is his ruling, not a defect.

**What H1 builds of B:** the re-sort, computed and STORED as the would-be rank, never used (`mode: shadow` is the only mode H1 acts on). H1 also accepts `mode: live` in the schema, because the key's Literal is `shadow | live` ([F-12]). Under `live`, H1 still does NOT sort; the sort is H2's. See §6 for what H1 does if it reads `live`.

## 2. THE JSONB FIELD SET UNDER B (v3 §6 — the field NAMES are fixed; B fixes their MEANING)

Three nullable columns on `system.radar_membership` (v3 §6 table; one additive migration):

| Column | Meaning under B | When NULL |
|---|---|---|
| `raw_rank INTEGER` | the `_ranked()` index of this scan: `ranks[ticker]` from `pool.py:210-212`, no factor applied to anyone. Stored under either answer (v3 §1 common ground). | on rows that were not ranked this scan (HOLD, manual EXCLUDE/LEAVE, screen-inactive LEAVE, never-admitted LEAVE) |
| `handicap_factor NUMERIC(6,4)` | the factor `h` for this name: `handicap.factor` when the verdict applies it (`yes`, or `unknown` with `missing: apply`), otherwise 1. It is the would-be factor even in shadow: grok's O1 is taken; Fable's "applied = 1 in shadow" variant is owner item 9 and is NOT taken. | the block is absent, OR the handicap step failed (§5) |
| `handicap JSONB` | the Pydantic-validated object below | the block is absent, OR the handicap step failed |

The `handicap` object, `extra="forbid"`, exactly v3 §6's keys. `decisive` is H2's and is NOT written by H1:

| Key | Meaning under B |
|---|---|
| `float_m` | the `Shares Float` cell of the source `source_for[ticker]` names, parsed by `_number` (`runner.py:391-398`), in millions of shares (F5). `null` when blank, `-` or unparseable. |
| `market_cap_m` | the `Market Cap` cell of that same source, in $ millions (F5). `null` as above. |
| `verdict` | `yes` / `no` / `unknown` per [F-10] under the block's `combinator` (`any` / `all`). |
| `reason` | which test put it in the group (`float` / `cap` / both), or why it is `unknown` (which cell was blank). Plain words; no value of his. |
| `missing_rule` | the block's `missing` key as read (`apply` / `skip`). This is his value, stored as data on the row, never written in code. |
| `mode` | the block's `mode` as read (`shadow` / `live`). |
| `position` | **under B: the name's `raw_rank`**, the dividend of `eff = raw_rank ÷ factor`. It repeats the column so the JSONB replays alone (L57). |
| `effective_position` | **under B: the WOULD-BE POOL-WIDE RANK**, meaning the 1-based index of the name in `ordered` re-sorted by `(eff, in_group, raw_rank)`. This is v3 §6: "the would-be rank sits in `handicap.effective_position`". The quotient `eff` itself is not stored. It is recomputable exactly as `Decimal(position) ÷ handicap_factor` from stored inputs. |
| `source` | `source_for[ticker]` (`pool.py:208`), the source whose cells were read. |
| `block_sha256` | the sha256 of the parsed `handicap` sub-block (`canonical_sha256` of its `model_dump(mode="json")`, `evaluate.py:155-158`). No value is printed. |

`last_rank` and `rank_at_entry` keep their meaning: the rank that governed admission. In shadow that is the RAW rank, byte-identical to today's. `Transition.rank` is unchanged (v3 [F-16]: "H1 does not change `Transition.rank`"). `Transition` gains `raw_rank` and the handicap payload (B: "`raw_rank` and `rank` both ride the `Transition`").

## 3. OWNER ITEMS — his, read AFTER. The build ships WITHOUT every one of them

The 13 items of the derive-r2 report's `## OWNER ITEMS`. None is a precondition (R28 (c)). Tests use constructed blocks with the builder's own literals (L69). The build ships with the block ABSENT from his note, and proves both the loud refusal and the `h = 1` identity.

1. `handicap.float_below_m` and `handicap.market_cap_below_m`: his R28 / R29 values. The desk writes them (L65) only after the deployed parser accepts the block.
2. `handicap.factor`: the flat size, set after the H1 dry-run.
3. `handicap.missing`: `apply` / `skip`.
4. `handicap.combinator`: `any` / `all`. His to flip without a build (R29).
5. `handicap.mode`: `shadow` until his typed approve of `live`. That approve names the note path, the post-edit sha256 and the dry-run report path, and is not given before H3 is in production.
6. Shadow length, in sessions, before the approve.
7. A graded `shape:` key or a per-screen exempt. Later, not this build.
8. What `missing: apply` means on a DEAD column. grok's reading is taken: apply `h` to every name, and the banner says the order is unchanged.
9. Storage variant (applied factor = 1 in shadow). Not taken; §2 above stores the would-be factor.
10. Chunk shape (H1a / H1b split; one-place fail-soft catch). grok's chunk order is taken. The fail-soft catch is decided in §5 below from the code, as the drafting prompt ordered, and is not his item.
11. Whether a `decisive` name is shown apart on `/radar`. That is H2's concern.
12. Exact-tie rule: the unhandicapped name first. This lives INSIDE B's text (`(eff, in_group, raw_rank)`), so R26 carried it.
13. POOL-WIDE vs TIER-BOUND: **RULED — R26 "B".**

## 4. THE EXPERIMENTS H1 RUNS FIRST (v3 `## First-gate experiments (L70)`; STEP-1 of `27`)

Each one ends `AS EXPECTED` or `NOT AS EXPECTED`, with its output verbatim. Outputs carry counts and ratios only: no ticker next to a value of his, no cap, no time (L32). A NOT AS EXPECTED that changes the design is `FAILED: STEP-1 — X<n> — <what>` plus the design question for the desk, never a silent redesign.

| X | What it proves | Run on | STOPS the build when |
|---|---|---|---|
| **X2 (FIRST)** | the marginal seat's tier on the retained 2026-09-18 RTH scans. After the `first_from` time: equity names on the `first_from` screen against `cap`, and all screen names against `cap`. This is his evidence for B's bite and the dry-run's "tier of the cut" line. | the retained cache `/Users/cobalt/cobalt/data/radar-cache/2026-09-18/` (read-only), his pool block through the existing reader (counts only) | never, alone. It changes the dry-run's WORDING: if the marginal seat is a list, `first_from`, held or stickiness seat, the sentence "keeps its seat iff `p ≤ h × c`" is NOT printed by the dry-run (grok X2). The day being gone from the cache = `UNPROVEN — day expired`, and it runs on the oldest retained day instead, named. |
| X4 | on MAIN's code, a pool note carrying `handicap:` freezes the pool (`pool_error`, F14) rather than crashing the cycle; under H1's code the same note parses. | offline: `notes.parse_note_bytes` on a scratch copy of `tests/fixtures/radar/radar-screens.real-shape.md` plus a constructed `handicap:` block (builder's literals) | if main CRASHES instead of freezing, the rollback hazard is worse than a freeze. That is an ESCALATE for the deploy's rollback order, not a build stop. |
| X1 | blank `Shares Float` / `Market Cap` on equity rows, per source, per retained day | the fixtures named in v3 X1 plus every retained cache day | a source that is MOSTLY blank means `missing: apply` un-handicaps that source, and the all-unknown banner must fire PER SOURCE (grok). STOP + ESCALATE: that is a design change. |
| X3 | the live export's cell format (currency symbol, B/M/K suffix, unit) through `_number`; `Price × Shares Outstanding` against `Market Cap` | every cached cell of the two headers | a suffix, a symbol or a unit mismatch. STOP + ESCALATE: the thresholds would leave the export's units. |
| X5 | the S5 receipt's `pool_unit` carries `SourceSet.metrics` (`runner.py:319-323` dumps `source_sets` whole: from reads, expected YES) | offline: build `pool_unit` from a constructed SourceSet and read the dump; `cobalt_dev`'s stored receipts where any exist | `metrics` absent. STOP + ESCALATE: the L57 claim is false after the cache expires. |
| X6 | a `degraded_sources` entry for `handicap` renders its reason on the panel (`radar_panel.py:586-588` joins names) | offline panel test | only the name renders. This is NOT a stop: H1's panel change renders the reason (v3 X6's own consequence). |
| X7 | whether `poller.py:84` orders by `last_rank` | a read, quoted | the poller does not order by it. NOT a stop: the §1 poller row is corrected in the report. |
| X8 | equity rows of the low-float morning screen that fall OUTSIDE the group under a constructed block | retained cache, counts only | never a stop. The dry-run does not print "in the group by construction" if any exist. |
| X9 | a list cache file and a screen cache file both carry both headers | retained cache | lists lack them. STOP + ESCALATE: every list name would be `unknown`. |
| X10 | one ticker in two sources in ONE scan: do the cells differ? | retained cache | they differ beyond noise. NOT a stop: the row already records `source` (B's last sentence). Recorded. |
| X11 | (ticker, day) pairs whose verdict flips between scans of one day, under a constructed block | retained cache | "more than a handful a day" means a latch on `OpenMember`. STOP + ESCALATE: that is a design change. |
| X15 (measure only) | not-equity rows ahead of a handicapped equity inside a screen (the pre-existing fund hole, [R2F-02]) | retained cache | never a stop in H1. X15 gates H2. "Do NOT fix it" ([R2F-02]). |
| X12 | the `h = 1` identity over EVERY retained day ([F-16]): delivered by H1 as the dry-run plus its test | STEP-6 of `27` | ANY mismatch voids every dry-run figure (Fable). That is `FAILED`. |

Not H1's: X13 (timing of the second `decide()`, H2), X14 (float vs `Decimal` division, H2 — though H1's `effective_position` is computed in `Decimal` and a unit test pins the exact-integer tie), X16 (moot under [R2F-03]).

## 5. RULINGS THIS SEAT TOOK FROM THE CODE (the drafting prompt ordered them decided in the prompt)

**FORMULA_FILES: the module that computes `h` does NOT join the hash in H1.** `src/cobalt/radar/evaluate.py:143-152` is the tuple `FORMULA_FILES`, commented at `:143` "The source files whose bytes ARE the formula (`formula_sha256`)". It lists `evaluate.py`, `anatomy/*.py`, `cards/scoring.py`, `cards/health.py`, `cards/radar.py`, `cards/expire.py` and `aset/engine.py`: the CARD formula. `radar/pool.py` has never been in it (C9 HOLDS). In H1 no card number reads `h`. `card_score` takes `h` only in H3 (v3 §9). H1's factor is stored on the membership row (`handicap_factor`, `handicap` JSONB) and in the receipt's `pool_unit` (`runner.py:319-323`). So the pool's decisions replay from stored inputs (L57), not from a hash. Adding the file now would change `formula_sha256` at the H1 deploy with no card-formula change, which is a false version split between old and new cards (`evaluate.py:161-166`). **H3 re-asks it**, when `card_score` gains `h`. `cards/scoring.py` is already hashed then, and `h` rides `aset_sizings`.

**FAIL-SOFT: caught in ONE place.** The place is `decide()` in `src/cobalt/radar/pool.py`, around the ONE call of the handicap step made after `_ranked()` (`pool.py:326`). On any exception from that step: ranks stay raw (they are, in shadow, by construction); `raw_rank` is still stored; `handicap_factor` and `handicap` are stored NULL; `handicap` is appended to `Decision.degraded_sources` with a reason naming the exception class; and one `logger.exception` line is written. NULL is chosen over factor 1 because 1 would CLAIM a verdict ("not in the group") that was never computed (L1: no plausible-empty artifact). **Why one place and not tests only:** `decide()` runs at `runner.py:186`, BEFORE the S1 `try` (`runner.py:189-206`). The resident loop `run_command` → `resident()` (`runner.py:453-460`) calls `await runner.cycle()` with no `except`. So an exception inside `decide()` ends the resident process, launchd respawns it into the same exception, and the whole pool is down for a feature that, in shadow, sorts nothing. That is the L9 case (a dead part = a loud degraded flag, never silent and never an outage). **Where L1 still binds:** a PRESENT block that is missing a key, or carries a bad value, fails `PoolBlock(**raw)` at `notes.py:108`. That sets `pool_error`, and the pool FREEZES loudly (F14, `notes.py:64-65`, `:408-415`). That is the config path, and it is a crash-shaped refusal, never caught by the fail-soft. A test proves each of the two paths.

## 6. MODE `live` READ BY H1 CODE

H1 never sorts on `h`. If his note carries `mode: live` while only H1 is deployed, the build stores exactly what shadow stores, keeps the order raw, and appends `handicap` to `degraded_sources` with the reason `mode live needs H2 — ranking raw`. It is a loud flag, never a silent `shadow` (L1). The panel header shows `handicap: degraded`. The promotion order in v3 §7 means the desk never writes `live` before H3. This is a guard, not a path.

## 7. THE ROLLBACK ORDER (v3 §5; derive-r2 ESCALATE 6; X4 proves the hazard)

1. **The desk removes the `handicap:` block from his pool note FIRST** (L65: a desk edit on his ruling, before/after diff, then `cobalt radar sources` as the read-only parser proof showing no `pool_error`).
2. THEN the code revert (L54: `git revert` of the merge range; L68's `git revert -m 2` for a stacked gate merge).
3. THEN the migration rollback: `0014_…rollback.sql` drops the three columns. It is additive and bounded; it drops only H1's columns.
4. Residents down before and up after, inside the 20:00–21:00 market_reset pause (L66, L43).

The reverse order (code reverted while the block is still in his note) makes main's `PoolBlock` (`extra="forbid"`, `models.py:99-100`) refuse the unknown key. That sets `pool_error` and the pool FREEZES (F14). X4 records whether it freezes or crashes.

The forward order at the deploy: code and migration live first, THEN the desk writes the block (with `mode: shadow`, his value, read after), THEN the parser proof.

## 8. THE MIGRATION NUMBER

main's newest is `0011_archive_incidents` (`ls src/cobalt/db_migrations/`). `0012` is taken by `bars/chunk-2-0920` (`0012_bars_partitioned_parent`) and `0013` by `setups/seven-0921` (`0013_tunables_slug_nullable`). Both are unmerged. **H1's is `0014`**: `0014_radar_handicap.sql` plus `0014_radar_handicap.rollback.sql`, registered in `src/cobalt/db_migrations/__init__.py` (both branches edit that file too, an L68 seam). If either branch has merged by build time, the number stays 0014. If a newer migration has landed on main, you take the next free number and say so.

## 9. v3 §6 vs the drafting prompt: one divergence, followed as v3

The drafting prompt paraphrased "absent block … every row stores `h = 1`, `raw_rank = rank`". v3 §6 (the FINAL) says `handicap_factor` is **NULL when the block is absent**. The build follows v3: absent block → `handicap_factor` NULL, `handicap` NULL, `raw_rank` stored (= `rank`, since nothing re-sorts). The `h = 1` identity test covers BOTH the absent block AND a present block whose every factor is 1. This is listed under the drafter's report `## ESCALATE` for the desk.
