# `src/cobalt/radar/models.py`

Pydantic contracts for screen, pool, list, exclude, candidate, membership, and source-health data. Every config model forbids extra fields and validates identifiers, windows, filters, priorities, and ticker lists.

---

## 2026-09-17 — S2-P4

`RankMetricName = Literal["volume", "rvol"]` is the one spelling shared by
the pool note block, 0008's `rank_metric` CHECK, and the models that carry
the value. `OpenMember` gains nullable `rank_metric`/`rank_value` (default
None). They are NULL on episodes scanned before 0008, and a frozen HOLD
carries them unchanged (Astra R2-2).
