## §0 Headline
- Four-house tribunal round 1 on the float/market-cap handicap design (`FLOAT-HANDICAP-PROPOSAL-2026-09-21.md`): grok and gemini both rule BUILD AFTER, converging on the same core blocker (amend ADR-0009 D4 to name `ladder_order`/`pool_position` correctly) plus a second, independently-found gap (no `combinator` key for R29's any/all rule).
- Astra SKIPPED at the preflight probe (usage limit, resets 2026-09-26 06:47 ET) — grok and gemini ran independently; floor (≥2 houses) met.
- Status: DONE.
- ESCALATE count: 3 (astra did not rule; gemini's item-(a) "none exists" answer does not hold against the code; ASK DESK re: astra relaunch).
- Redactions: 0 (no house's text quoted an actual R28/R29/digest value — all citations were by KEY, so nothing needed `[user data: ...]` substitution).

## AUTHORIZATION
- R13 found: `cto-2026-09-20.md:86`.
- R23 found: `cto-2026-09-20.md:206` (text there reads "THROUGH MONDAY 2026-09-21 23:59 ET" — the re-issue/extension to 2026-09-22 named in the launch prompt is asserted by the prompt file itself, not re-verified against a separate `cto-2026-09-21.md` R39 row in this step; the prompt's own required greps only name R13/R23/R28/R29, so this is recorded as-is, not escalated further here).
- R28 found: `cto-2026-09-21.md:39` — contains "I don't want to exclude tickers": YES.
- R29 found: `cto-2026-09-21.md:40` — contains "Finviz does offer both market cap and float": YES.
- `git log -1 -S"I don't want to exclude tickers" -- cto-2026-09-21.md` → `94a341c3233717209927e8074c40b134e27e22f1` (non-empty).
- `git log -1 -S"Finviz does offer both market cap and float" -- cto-2026-09-21.md` → `6b0cbfdbfad048f57074ab83b774c52e8dd5f083` (non-empty).
- `git log -1 -- "docs/30 - Design/FLOAT-HANDICAP-PROPOSAL-2026-09-21.md"` → `6b0cbfdbfad048f57074ab83b774c52e8dd5f083` (non-empty).
- No-new-rule check against `08-bars-chunk-e-check.md`: all 14 allow strings + 3 deny strings counted ≥1 (grok/agy strings counted 2 — once in that file's own launch line, once in its own prose citation of R9 — no string counted 0). PASS.
- AUTHORIZATION: PASS.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| date gate row 1 | `date` | 0 | Tue Sep 22 10:16:19 EDT 2026 — before 2026-09-23, outside both blackout windows (19:25–20:45, ≥23:20) → ALLOWED |
| grok present | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` → ALLOWED |
| agy present | `agy --version` | 0 | `1.2.8` → ALLOWED |
| base folder exists | `ls scratch/tribunal-bars-0920` | 0 | populated (many prior tribunal folders) → ALLOWED |
| RECOVERY check | `ls scratch/tribunal-bars-0920/float-handicap-tribunal/r1` | 0 | 4 files already staged: `cards-radar.py`, `pool.py`, `PROPOSAL.md`, `radar-models.py` — this is a RECOVERY resume, not a fresh run; no prior `float-handicap-tribunal-2026-09-21.md` report or `TRIBUNAL-R1.md` fallback exists, so no `## CONTINUE` breadcrumb to read — treated as resuming at staging with the 4 files kept (byte-verified below) |
| s1 stagger | `tail -n 3 setups-tribunal-r1b-2026-09-21.md` | 0 | last line starts `SETUPS TRIBUNAL R1B DONE ...` → not running → ALLOWED |
| s2 stagger | `ls degraded-line-deploy-review-r2-2026-09-21.md` then `tail -n 3` | 0 | file exists; last line starts `DEGRADED LINE DEPLOY REVIEW R2 DONE ...` → not running → ALLOWED |
| date gate row 2 | `date` | 0 | Tue Sep 22 10:17:25 EDT 2026 → still ALLOWED |
| astra probe (gate for astra ONLY) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 1 | usage-limit error, verbatim: "You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 26th, 2026 6:47 AM." → `astra: SKIPPED — METER at probe`; grok and gemini still run |

## Packet
Staged in `scratch/tribunal-bars-0920/float-handicap-tribunal/r1/` (gitignored). Whole files verified byte-identical (`wc -c` matches source exactly); excerpts verified by anchor (`grep -n`, every anchor found at its stated line, no boundary moved).

| file | kind | bytes | note |
|---|---|---|---|
| `PROPOSAL.md` | whole (recovered, byte-verified) | 29366 | `docs/30 - Design/FLOAT-HANDICAP-PROPOSAL-2026-09-21.md` |
| `design-digest.md` | excerpt [USER DATA] | 5854 | `float-handicap-design-2026-09-21.md:5-39`, values unredacted (scratch/ only, per L32) |
| `owner-rulings.md` | verbatim rows [USER DATA] | 3110 | `cto-2026-09-21.md` R28 (:39), R29 (:40), values unredacted (scratch/ only) |
| `laws-excerpt.md` | excerpt | 11618 | LAWS.md L1,L3,L7,L9,L10,L28,L32,L52,L53,L57,L61,L65,L70 |
| `ADR-0009-D3-D4.excerpt.md` | excerpt | 1119 | ADR-0009 D3–D4, :24-28 |
| `pool.py` | whole (recovered, byte-verified) | 17528 | `src/cobalt/radar/pool.py` |
| `radar-models.py` | whole (recovered, byte-verified) | 6954 | `src/cobalt/radar/models.py` |
| `cards-radar.py` | whole (recovered, byte-verified) | 8481 | `src/cobalt/cards/radar.py` |
| `radar-config.excerpt.py` | excerpt | 5533 | `config.py` :24-118, :144-180 |
| `radar-runner.excerpt.py` | excerpt | 8311 | `runner.py` :100-150, :172-232, :355-399 |
| `cards-scoring.excerpt.py` | excerpt | 7536 | `scoring.py` :1-72, :236-343 |
| `evaluate.excerpt.py` | excerpt | 5003 | `evaluate.py` :128-167, :1210-1237, :1383-1400 |
| `migrations.excerpt.sql` | excerpt | 4587 | `0004_radar_pool.sql` :25-55, `0007_radar_cards.sql` :210-245, `0009_picks_missed.sql` :70-80 |
| `picks-store.excerpt.py` | excerpt | 3842 | `picks.py` :55-62, :220-240; `store.py` :1185-1227 |
| `pool-tiers.excerpt.py` | excerpt, item (k) | 4230 | `pool.py` :125-137, :154-165, :206-212, :323-334; `models.py` :75-116 |
| `greps.txt` | pre-computed searches | 54876 | 15 commands, all ≤400 lines each, no file split needed; header states this shell's `grep` (ugrep) honours `.gitignore` |
| `QUESTIONS.md` | verbatim + files list | 14678 | §26 of the prompt, verbatim, plus the required files paragraph |
| **total** | | **192626** | drafter's ≈180 KB + ≈9 KB estimate was exceeded (mainly `greps.txt` 54876B and `QUESTIONS.md` 14678B, larger than estimated) — no file split was needed regardless, so this did not block the launch |

NOT STAGED (as instructed): `runner.py`, `evaluate.py`, `store.py`, `picks.py`, `radar_panel.py` whole; `data/radar-cache/` CSVs; the setups proposal whole.

Both houses answered inside the 20-min budget: GROK completed at 10:45 ET (wrote `grok-ruling.md` itself, 177 lines, 36059 B), GEMINI completed earlier (printed; hub wrote `gemini-ruling.md` byte for byte, 84 lines).

## Rulings table
| item | grok | gemini | astra | agreement | wording / reason (≤25 words/house) |
|---|---|---|---|---|---|
| O1 | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: `h` stored once, `mode:live` gates both consumers, shadow sorts on neither. gemini: applying `h` to both respects pre-tap and post-tap ordering; rejecting violates L52(b). |
| O2 | ADOPT | ADOPT | — | 2-0 ADOPT | grok: flat = one key, same sentence both places; graded needs two more unruled values. gemini: flat achieves soft penalty with fewer assumed values than a graded curve. |
| O3 | ADOPT | ADOPT | — | 2-0 ADOPT | grok: exemption is a no-op identical to a metric multiplier on an all-in-group screen. gemini: R28 explicitly names the low-float morning screen as a target. |
| O4 | ADOPT | ADOPT | — | 2-0 ADOPT | grok: `priority` is key component 0, ahead of position; a third tier would be a cliff (=exclusion). gemini: matches R28 "still falls within top 50" and respects his tiers (L53). |
| O5 | ADOPT | ADOPT | — | 2-0 ADOPT | grok: absent block + strict parse (`extra="forbid"`) is the loud, no-default path (L1). gemini: L53 forbids settling ceilings/cadences in config; block absence keeps only his values live. |
| O6 | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: additive `ExcludedBy` value only when a SECOND full `decide()` (stickiness included) admits the name at `h=1`; `winners`-membership alone is the wrong test (scenario given). gemini: additive enum value slots into existing miss-line counting without a second column. |
| (a) | ADOPT WITH | ADOPT | — | split reasoning, same ADOPT verdict | grok: one stored factor, but NOT one sort — `ladder_order`'s two numeric inputs can disagree once a tap exists AND for pinned cards; demonstrated with a concrete scenario. gemini: "None exists" — no consumer disagreement found. **File-check below: grok's claim HOLDS, gemini's blanket "none exists" DOES NOT HOLD as stated.** |
| (b) | ADOPT WITH | ADOPT WITH | — | 2-0 ADOPT WITH, converging wording | grok: amend ADR-0009 D4 pre-H1 — the claim holds only for an all-untapped WATCH ladder, not once any card is pinned; withdraw "last_rank only admits". gemini: amend ADR D4 to name `card_score` primary / `pool_position` secondary for WATCH pre-tap. |
| (c) | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: apply `h` once, after the cross-screen `min`; not-equity rows before exclusion distort `_metric_position` counts (scenario given, price: small `pool.py` edit, H2, no migration). gemini: dividing position works for both screens/lists; not-equity rows shift positions "equally" (weaker claim than grok's). |
| (d) | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: one function, `combinator`-aware verdict (yes/no/unknown), blank never silently "no"; `missing:apply` with a dead column is a provable un-handicap since one shared `h` doesn't reorder a tier. gemini: `_number` handles current format; live suffix risk `UNVERIFIED — X2`. |
| (e) | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: rule is enforceable only as a test beside `FACTOR_COMPUTERS`/declared inputs, not a runtime ban; a renamed factor slips the string match. gemini: no computed dot uses float/cap today; enforcement best as text per future tribunal. |
| (f) | ADOPT WITH | ADOPT WITH | — | 2-0 ADOPT WITH, same gap found | grok: full 6-key schema incl. `combinator: any|all`; his `approve` of shadow→live must name the note path, post-edit sha256, and dry-run report path. gemini: add `combinator: Literal["any","all"]="any"` to `HandicapBlock` per R29. **Both independently found the same missing key — file-check below confirms the proposal has no combinator key.** |
| (g) | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: replay claim is `UNVERIFIED` until X6 confirms `pool_unit` stores `SourceSet.metrics` today; `formula_sha256` branch needed for old-card replay. gemini: replay fully supported via `SourceSet.metrics`/`pool_unit`; counterfactual is a cheap memory-only check. |
| (h) | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: proves from code `proposed_key`/`snap_down`/shares don't read `card_score`; adds a same-dots-different-`h` equality test. gemini: `proposed_key` branches on conviction not `card_score`; sizing untouched. |
| (i) | ADOPT WITH | ADOPT | — | 2-0 ADOPT(WITH) | grok: H1→H2→H3 order; H1 dry-run must replay the FULL retained cache (not a sample), print the tier of every cut; C2 collision understates itself (`PROPOSAL.md:161`) — no other C-chunk touches `pool.py`/`scoring.py`. gemini: H1 shadow is inert for ranking; C2/H3 collision resolved by sequencing C2 first. |
| (j) | 11 experiments (X1–X11) | 3 experiments (X1–X3) | — | overlapping, not contradicting | see `## Experiments named` |
| (k) | ADOPT WITH — TIER-BOUND | ADOPT — TIER-BOUND | — | 2-0 TIER-BOUND | grok: names 5 tiers with file:line (`priority`, `first_from`, held seats, stickiness, pre-rank removals); flags that the proposal itself never says TIER-BOUND nor names `first_from`/held-seat tiers — those are the missed tiers, named as an owner item if POOL-WIDE is ever wanted. gemini: pool enforces tiers via the sort tuple; handicap reorders only within a tier, respecting R28 and L53. |
| closing line | `TRIBUNAL R1: BUILD AFTER ADR D4 names ladder_order` | `TRIBUNAL R1: BUILD AFTER <ADR-0009 D4 text is amended and combinator key is added to HandicapBlock>` | — | both BUILD AFTER, same core condition (ADR text); gemini also names the combinator key | |

## Wording offered, verbatim
Full `ADOPT WITH` replacement wording and `REJECT` text is reproduced unedited in each house's staged ruling file (no REJECT was issued by either house). Copied here for the derive step (§26 "pasted into the design verbatim"):

**O1 (grok):** "Option (c) stands. One factor `h` is computed once per ticker per scan, stored on the membership row, and consumed read-only at the pool key and at `card_score`. `handicap.mode: live` is not written until the H3 deploy is in production. In `shadow`, neither consumer sorts by `h`: `last_rank` stays the raw admission rank, and `card_score` stays `round(conviction × proximity × 100)`. The penalised rank and the penalised score are display-only would-be figures. In `live`, the pool key uses the effective position and `card_score` is `round(conviction × proximity × h × 100)`, rounded once."

**O6 (grok):** "`handicap_cap` is a new `ExcludedBy` value, additive, never a rename and never a boolean column. Add it to the `radar_membership` CHECK (`0004_radar_pool.sql:42-43`), the `"user".missed` CHECK (`0009_picks_missed.sql:76-82`), `replay/models.py` `ExcludedBy`, and `EPISODE_EXCLUSIONS` (`replay/movers.py:102`). Do not add it to the card-formation vocabulary (`replay/cards.py`). The miss line already counts by `excluded_by` (`replay/line.py:97`) and needs no second key. A `config_cap` EXCLUDE or LEAVE is relabelled `handicap_cap` only when that name's `h < 1` and a second `decide()` with that name's `h` set to 1, every other input unchanged, admits the name (`ADMIT`, `RETAIN`, or `HOLD`) where the real `decide()` does not. Both calls include stickiness and held seats. Membership in `winners` is not the test."

**(a) (grok):** "`h` is one computation, stored once on the membership row (L3), and read at two consumers. It is not one sort. The one ranking authority that reaches the card is `ladder_order`. In `live`, both of its numeric inputs carry this same stored `h`: `card_score` is multiplied by `h`, and `pool_position` is the admission rank from the key whose position was divided by `h`. The `/radar` pool view orders by that admission rank. Focus orders by `card_score`. The surfaces may disagree. The card does not re-sort to match the pool, and each surface shows the raw figure beside the penalised one."

**(b) (grok):** "Before H1, amend ADR-0009 D4 as a documentation change, not as a behaviour change. The one authority that reaches the card is `ladder_order` (`cards/radar.py:174-183`). Pinned cards order by `pool_position`, then `card_score`. WATCH orders by `card_score` nulls last, then `pool_position`. When every WATCH `card_score` is null, that block's order is `pool_position`. `last_rank` admits and is that `pool_position`. The sentence 'pool `last_rank` only admits' is withdrawn. Do not change `ladder_order`. In `live` both numeric inputs carry the stored `h`."

**(b) (gemini):** "ADR-0009 D4 is amended before H1 to reflect the existing tie policy: `card_score` orders WATCH cards, with `pool_position` as the secondary sort (which governs before any tap)."

**(c) (grok):** "`effective_position = position / h`, in `Decimal`, quantized to the `handicap_factor` scale (`NUMERIC(6,4)`), replaces `position` in the key at `pool.py:209`. Apply `h` once, to the winning position after the min at `pool.py:165`. `rank_value` stays the raw metric. Stickiness and `below_cap_streak` are unchanged. A tie on the quantized position breaks by `note_order`, then `ticker`."

**(d) (grok):** "The verdict is `yes`, `no`, or `unknown`, from one function. `combinator any`: `yes` when at least one known value meets its threshold... Blank, `-`, and unparseable are `unknown`, never a silent `no`. `handicap.missing` is required whenever the block exists. The pool row shows `unknown → applied` or `unknown → not applied`... A missing header, or every equity candidate on the scan `unknown`, appends `handicap` to `degraded_sources` with a reason the panel renders."

**(e) (grok):** "No float-derived dot is promoted into conviction while a `handicap` block exists, unless a later tribunal rules the composition. The check is a test beside `FACTOR_COMPUTERS` (`evaluate.py:429`): none of those names, and none of their declared input keys, is shares-float or market-cap. A factor that does not declare its inputs is not caught; it still cannot be promoted without that composition ruling."

**(f) (grok):** "The home is his vault pool block, sub-block `handicap`, model `HandicapBlock` nested on `PoolBlock`, `extra="forbid"`. Keys, all required, no code default: `float_below_m` Decimal `> 0`; `market_cap_below_m` Decimal `> 0`; `factor` Decimal `0 < factor ≤ 1`; `missing` Literal `apply` | `skip`; `mode` Literal `shadow` | `live`; `combinator` Literal `any` | `all`. ... His typed `approve` of `shadow → live` names the note path, the post-edit sha256, and the dry-run report path, and it is not given before H3 is in production."

**(f) (gemini):** "`combinator: Literal["any", "all"] = "any"` added to `HandicapBlock` to encode R29's explicit combinator rule."

**(g) (grok):** "The replay inputs for a penalised rank are `SourceSet.metrics` (float and cap included) and the membership columns `raw_rank`, `handicap_factor`, and `handicap` JSONB... `card_score` replays from stored conviction, proximity, and `handicap_factor`, rounded once, only when `formula_sha256` is an H3-or-later hash; an older hash recomputes without `h`. `handicap_cap` is additive to the sets in O6, with no renamed value."

**(h) (grok):** "The card face gains an `H` chip and the score reads raw → penalised, owner COBALT... In `shadow` the chip says would-be and `card_score` stays unpenalised (O1). `proposed_key`, `snap_down`, the tapped grade, `shares`, and `risk_budget` do not read `card_score` or `h`. A test scores the same dots at `h = 1` and at `handicap.factor` and asserts the proposed key, the tap, the share count, and the risk budget are equal."

**(i) (grok):** "Order is H1, then H2, then H3. Each is size M as proposed (not re-measured here), each ships its own migration, and the builder seat for each is Opus 5 or Sol-high... H1's dry-run, before that approve, replays every retained cached day and prints `n` as days and scans. Per scan: members in and out; handicapped names that kept a seat and names that lost one, with position and effective position; who took the seat; which tier the cut was... The `h = 1` pass must match stored membership."

**(k) (grok):** "The handicap is TIER-BOUND. It divides the within-source position. It does not change `priority`, `first_from`, or the held-seat reservation. A handicapped name in an earlier tier still beats every name in a later tier, whatever `h` is. Tiers, and what `h` does to each: (1) `priority`... inert for which group a name is in. (2) `first_from`... `h` does not cross that. (3) Held members... `h` is inert. (4) Stickiness... `h` does change who is evicted. (5) Removals before ranking... `h` never sees those names."

## Checked against the files
| claim | who | file:line | verdict | ≤30 words |
|---|---|---|---|---|
| F1 wording "position of the name inside the source that ranks it best" is imprecise — `min()` picks lowest `first` (past `first_from`) BEFORE position | grok (WRONG FACTS #1) | `pool.py:154-165`, `:209` | HOLDS | `min((first, position, note_order, source))`: a source with `first=0` wins regardless of a worse position on another source. |
| F2 "a name that loses its seat gets `excluded_by=config_cap`" is not universal | grok (WRONG FACTS #2) | `pool.py:351`, `:370` | HOLDS | Verified directly: line 351 sets `CONFIG_CAP` only `if ticker in candidate_map else None`; line 370 only `if rank else None`. |
| F11 "before any tap, the ladder order IS the pool rank" | grok (WRONG FACTS #3) | `cards/radar.py:174-185` | HOLDS | `active = [*pinned, *watch]` (line 185): a PINNED card always precedes every WATCH card regardless of relative `pool_position`; grok's BIG(pinned,30)/LOWF(watch,2) scenario is real. |
| §1 "neither can re-rank around the other" because both carry the same `h` | grok (WRONG FACTS #4) | `cards/radar.py:174-183` | HOLDS | Position and `card_score` are unrelated quantities from different domains even without `h`; `÷h` and `×h` create no coupling between them — the two sorts already diverge pre-proposal. |
| §4 "keeps its seat iff `p ≤ h × c`" | grok (WRONG FACTS #5) | `pool.py:209`, `:332-378` | HOLDS | Priority group and `first_from` are compared before position (component 0/1 of the key); stickiness/held-seat logic (verified lines 336-378) can retain or evict independent of the simple position cutoff. |
| item (a): grok's claim that pool order and card order can genuinely disagree once a tap exists, and always for pinned cards | grok | `cards/radar.py:174-183` | HOLDS | Confirmed by direct read: WATCH sorts `(card_score, pool_position)`, PINNED sorts `(pool_position, card_score)` — different primary keys, so orders can and do diverge. |
| item (a): gemini's "None exists. No consumer orders by a number that carries `h` differently from another" | gemini | `cards/radar.py:174-183` | DOES NOT HOLD as stated | Contradicted by the same file gemini's own item (b) answer correctly describes (`card_score` primary, `pool_position` secondary) — gemini's (a) answer is inconsistent with its own (b) answer. |
| item (f): the proposal has no `combinator` key in its 5-key schema | grok, gemini | `FLOAT-HANDICAP-PROPOSAL-2026-09-21.md:213-217` | HOLDS | Read directly: exactly 5 rows (`float_below_m`, `market_cap_below_m`, `factor`, `missing`, `mode`); `grep -i combinator` on the proposal returns 0 matches. |
| item (k): TIER-BOUND — `priority`/`first_from` sit ahead of position in the key, unaffected by `h` | grok, gemini | `pool.py:127`, `:154-165`, `:209` | HOLDS | Verified directly (also independently confirmed while staging `pool-tiers.excerpt.py`): `priority[group]` is key component 0, `first` is component 1, both computed independent of any handicap division. |
| item (h): `card_score`/`h` does not reach `proposed_key`, `snap_down`, sizing | grok, gemini | `cards-scoring.excerpt.py` `proposed_key`; `store.py:1185-1227` | HOLDS | `proposed_key(conv, bands, enabled)` takes conviction only, not `card_score`; the tap path (`store.py`) computes `key` from `conv`, not from the just-updated `score`. |
| item (b): claim holds only pre-tap / for an all-WATCH ladder, not once any card is pinned | grok | `cards/radar.py:167-185` | HOLDS | `active = [*pinned, *watch]` — pinned cards precede all WATCH cards unconditionally, so "the ladder order IS the pool rank" cannot describe the combined ladder even before any tap. |

## Experiments named (L70)
| experiment | named by | gates which chunk (house's claim) | result that would change the design |
|---|---|---|---|
| Count blank Shares Float / Market Cap on real fixtures + retained cache (`data/radar-cache/2026-09-18`, `2026-09-21`) | grok X1 | H1 dry-run / (d) missing-rule banner granularity | if one source is mostly blank, `missing: apply` is an un-handicap there and the banner must fire per-source, not per-scan |
| Re-run `decide()` on stored 2026-09-18 RTH cache, record the marginal seat's tier | grok X2 | H1 dry-run wording | if the marginal seat is a list/`first_from`/held/stickiness name, drop the "keeps seat iff `p≤h×c`" sentence from the dry-run summary |
| Print `Shares Float`/`Market Cap`/`Shares Outstanding`/`Price` for 10 rows of one live screen + one live list export, check units | grok X3, gemini X2 (same ask) | (d) `_number` correctness | a currency symbol, `B`/`M`/`K` suffix, or unit mismatch moves the thresholds out of the export's actual units |
| Time one `decide()` + one extra `decide()` per `config_cap` name on a retained candidate set | grok X4, gemini X3 (same ask) | O6 / (g) `handicap_cap` inline vs post-scan | if added time exceeds scan cadence, stamp `handicap_cap` in post-scan replay instead of inline |
| Parse a pool note containing `handicap:` on current main; record freeze vs crash | grok X5 | (f) deploy-order guard strength | changes how hard the deploy-order guard must be, not the home of the keys |
| Open one stored S5 receipt; check whether `pool_unit` includes `SourceSet.metrics` | grok X6 | (g) L57 replay claim | if metrics are absent, H1's receipt writer must add them or the "replayable from receipt alone" claim is false |
| Render a `degraded_sources` entry `{source: handicap, reason: column missing}` through the current panel joiner | grok X7 | (d) banner wording requirement | if the panel shows only the joined source name, H1's panel change must render the reason text |
| Read `poller.py:84` for `last_rank`/`pool_position` usage | grok X8 | (a) authority list completeness | if the poller doesn't order by the rank it was given, the proposal's §1 poller row is wrong |
| Count equity rows outside the ruled group on one cached low-float-morning CSV | grok X9 | O3 "in the group by construction" | if any exist, that sentence is deleted; the position penalty itself is unaffected |
| Compare `Decimal` vs `float` division against neighbouring integer positions on one retained screen, grid of factors | grok X10 | (c) whether `Decimal` wording is load-bearing | a single flipped comparison makes the `Decimal` requirement load-bearing in practice |
| Confirm one list cache file and one screen cache file both carry `Shares Float`/`Market Cap` headers | grok X11 | (d)/(g) "every source" claim (F4) | if lists lack the columns, every list-group name is `unknown` and the banner must say so explicitly |
| Dry-run on retained cache to verify not-equity rows don't distort `effective_position` destructively | gemini X1 | (c) not-equity interaction | overlaps grok's scenario in (c)(1) and X9; a distorting case would require a different not-equity handling order |

Beside the proposal's own dry-run (§7): H1's dry-run over the full retained cache is common ground — both houses require it to run BEFORE the shadow→live approve, not as a sample (L8 has no sample-size number to invoke here since `laws-excerpt.md` does not carry L8 in this packet).

## OWNER ITEMS (after the tribunal)
Deduplicated where two houses' lines are word-for-word the same; none is written by either house as a precondition to build.
- `handicap.float_below_m`, `handicap.market_cap_below_m` — his R28/R29 values (both houses).
- `handicap.factor` — the flat penalty size (both houses).
- `handicap.missing` — `apply`/`skip` (both houses).
- `handicap.mode` — stays `shadow` until his approve of `live` (both houses).
- `handicap.combinator` — `any`/`all`; both houses treat the KEY itself as required in the build (item f, ADOPT WITH), but the VALUE he writes is owner-only.
- Shadow length in sessions before the approve (grok, gemini).
- A graded `shape:` key, or a per-screen exempt, if he wants one after seeing shadow — not this build (grok, citing the proposal's own Open 2/Open 3).
- POOL-WIDE instead of TIER-BOUND, if after shadow he wants a handicapped name to compete across `priority`/`first_from` — not this build; building it would weaken his ruled tiers without him saying so (grok, item (k)).

No owner item was written as a precondition to build by either house — none flagged under `## ESCALATE` on that ground.

## WRONG FACTS claimed
All 5 claimed by grok; gemini claimed none ("WRONG FACTS: None found.").
| claim | file-check verdict |
|---|---|
| `PROPOSAL.md:13` (F1) — position-only wording ignores `first_from` override | HOLDS (see `## Checked against the files`) |
| `PROPOSAL.md:14` (F2) — blanket `excluded_by=config_cap` claim | HOLDS |
| `PROPOSAL.md:26` (F11) — "before any tap, the ladder order IS the pool rank" | HOLDS |
| `PROPOSAL.md:70` — "neither can re-rank around the other" | HOLDS |
| `PROPOSAL.md:85` — "keeps its seat iff `p ≤ h × c`" | HOLDS |

## Independence
`grep -c -F -e "-ruling"`:
- `gemini-ruling.md`: 0.
- `grok-ruling.md`: 3 — all three are citations of `owner-rulings.md` (a legitimate packet file, matched only because "owner-ruling**s**.md" contains the substring "-ruling"), never `grok-ruling.md`/`gemini-ruling.md`/`astra-ruling.md`. Read at lines 93, 160, 163 of `grok-ruling.md`: not an independence breach.
- Astra was never launched (SKIPPED at probe) — no file to check.
No independence breach found.

## ESCALATE
- No `DO NOT BUILD` from either house.
- No `REJECT` from either house (all items ADOPT or ADOPT WITH).
- Item (a): gemini's "None exists" answer DOES NOT HOLD against the code and is inconsistent with gemini's own (b) answer — flagged so the derive step does not cite gemini's (a) wording as settling the question; grok's (a)/(b) wording (which correctly threads the needle: one stored `h`, but a pre-existing two-key sort that needs the ADR fixed) is the one that HOLDS and should be preferred by the derive.
- No owner item was written as a precondition to build.
- No second ranking authority found that violates L52(b): `ladder_order` remains the single named authority per both houses' converging (b) wording; the pool_position/card_score dual-key sort is a PRE-EXISTING documentation/code mismatch (the author's own ESCALATE 1), not a new authority introduced by this proposal — both houses' fix is an ADR text amendment, not a code change to `ladder_order`.
- No packet mismatch (all whole-file `wc -c` matches confirmed; all excerpt anchors confirmed at their stated lines).
- Both houses ruled (2 of 3); astra did not (SKIPPED at probe, usage limit, resets 2026-09-26 06:47 ET) — named per L67's floor: two houses is the standing floor when a meter binds, and grok+gemini both ruled, so the floor is met.
- No independence breach.
- `ASK DESK: astra was on METER at the round-1 probe ("You've hit your usage limit... try again at Sep 26th, 2026 6:47 AM.") — astra is REQUIRED before the derive (per this file's own INDEX CARD, item (9) WHY ASTRA IS REQUIRED); relaunch this same file for astra alone after 2026-09-26 06:47 ET, inside a future day's window (it re-asks only astra — grok's and gemini's rulings above are kept, never re-asked), or take the two-house result to Dejan for the derive? [2026-09-22 10:46 ET]`

## 4. Close
Next step, not this hub's: the desk commits this report; `40-float-handicap-tribunal-derive.md` needs astra's ruling in full or in part before it can run (per this file's own §9 WHY ASTRA IS REQUIRED) — the ASK DESK above names the relaunch-for-astra-alone path.

FLOAT HANDICAP TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER ADR D4 names ladder_order · gemini: TRIBUNAL R1: BUILD AFTER <ADR-0009 D4 text is amended and combinator key is added to HandicapBlock> · astra: SKIPPED — METER at probe · houses that ruled: 2 of 3 · claims that HOLD: 10 · blockers to build: 2 · owner items: 8 · ESCALATE: 3
