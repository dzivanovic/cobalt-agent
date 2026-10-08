# `src/cobalt/radar/models.py`

Pydantic contracts for screen, pool, list, exclude, candidate, membership, and source-health data. Every config model forbids extra fields and validates identifiers, windows, filters, priorities, and ticker lists.

---

## 2026-09-17 — S2-P4

`RankMetricName = Literal["volume", "rvol"]` is the one spelling shared by
the pool note block, 0008's `rank_metric` CHECK, and the models that carry
the value. `OpenMember` gains nullable `rank_metric`/`rank_value` (default
None). They are NULL on episodes scanned before 0008, and a frozen HOLD
carries them unchanged (Astra R2-2).

## 2026-09-24 — float handicap H1 (STEP-2)

`HandicapBlock` is the trader's `handicap:` sub-block of the pool note
(FLOAT-HANDICAP-v3 [F-12]): exactly six keys — `float_below_m` and
`market_cap_below_m` (Decimal, > 0, in the export's own units: millions of
shares and $ millions), `factor` (Decimal, 0 < factor ≤ 1), `missing`
(`apply`/`skip`), `mode` (`shadow`/`live`) and `combinator` (`any`/`all`) —
every one required, none with a code default, `extra="forbid"`, so a
present block missing a key is refused where the note is parsed and the
pool freezes loudly (L1, F14) rather than running on an assumed value.
`PoolBlock.handicap` is the one optional part: absent means off (v3 §5:
the block ships absent until he rules). A wrap serializer drops the key
when it is absent, so every dump of an absent-handicap block — the settings
mirror, the S5 receipt's `pool_unit` — stays byte-identical to the pre-H1
shape. The values are his and live only in his note (L32, L53).

## 2026-10-08 — price-floor-1008
`ExcludedBy.PRICE_FLOOR = "price_floor"` (R692, migration 0023): the reason an admitted member read at or below the price floor departs with.
