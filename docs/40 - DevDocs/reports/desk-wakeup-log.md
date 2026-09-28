# Desk wake-up log

One row per desk wake-up, appended by the waking desk (READ 7 of `prompts/CTO-DESK-WAKEUP.md`). Tokens = `desk-context.sh <id>` after the wake-up reads. Growth over 10% against the previous row OR the low-water mark (the lowest wake-up since the last reset; it resets only on his word) is explained and tuned before the plate.

| date | time ET | desk id | tokens | previous | change | low-water | change | note |
|---|---|---|---|---|---|---|---|---|
| 2026-09-27 | — | (baseline) | 136,059 | — | — | 136,059 | — | pre-redesign wake-up, the 09-27 sitting's measure |
| 2026-09-28 | 00:03 | 278c2faf | 121,474 | 136,059 | −10.7% | 121,474 | −10.7% (new mark) | old files; light §4 day (reconcile read small) |
| 2026-09-28 | 08:11 | 7a86cd02 | 63,833 | 121,474 | −47.5% | 63,833 | −47.5% (new mark) | first wake-up on the applied startup files (b0e5b903) |
| 2026-09-28 | 08:5x | 7a86cd02 | — | — | — | 63,833 | — | refresh line 500,000 → 250,000 (his R26 "A"); low-water unchanged |
| 2026-09-28 | 09:19 | 6f5275b5 | 61,406 | 63,833 | −3.8% | 61,406 | −3.8% (new mark) | applied startup files; HANDOVER from 7a86cd02 |
