# Desk wake-up log

One row per desk wake-up, appended by the waking desk (READ 7 of `prompts/CTO-DESK-WAKEUP.md`). Tokens = `desk-context.sh <id>` after the wake-up reads. Growth over 10% against the previous row OR the low-water mark (the lowest wake-up since the last reset; it resets only on his word) is explained and tuned before the plate.

| date | time ET | desk id | tokens | previous | change | low-water | change | note |
|---|---|---|---|---|---|---|---|---|
| 2026-09-27 | — | (baseline) | 136,059 | — | — | 136,059 | — | pre-redesign wake-up, the 09-27 sitting's measure |
| 2026-09-28 | 00:03 | 278c2faf | 121,474 | 136,059 | −10.7% | 121,474 | −10.7% (new mark) | old files; light §4 day (reconcile read small) |
| 2026-09-28 | 08:11 | 7a86cd02 | 63,833 | 121,474 | −47.5% | 63,833 | −47.5% (new mark) | first wake-up on the applied startup files (b0e5b903) |
| 2026-09-28 | 08:5x | 7a86cd02 | — | — | — | 63,833 | — | refresh line 500,000 → 250,000 (his R26 "A"); low-water unchanged |
| 2026-09-28 | 09:19 | 6f5275b5 | 61,406 | 63,833 | −3.8% | 61,406 | −3.8% (new mark) | applied startup files; HANDOVER from 7a86cd02 |
| 2026-09-28 | 10:42 | 0081a582 | 79,939 | 61,406 | +30.2% | 61,406 | +30.2% | read `_retired/cto-desk-contract.md` (16,887 B) by a `find` before the live `topics/` file; predecessor busy → live-hub work (merge-build dialog, pane reads, tool schemas) absorbed into the wake-up; R44 |
| 2026-09-28 | 11:07 | 9dcba8e3 | 76,806 | 79,939 | −3.9% | 61,406 | +25.1% | MEASURED per tool call from the transcripts (R52): base −1.9K. Four causes: (1) predecessor still busy → waiting (poll loop, 4 status checks, Monitor schema load, 2 pane reads, watch-checklist read) +9K; (2) §5 named no hub report paths → grep of prompts `16` / `21` +6.4K; (3) `## ` / HANDOVER heading grep printed the 1,200-char 00:01 HANDOVER line + 25-prompt listing +3.3K; (4) §4 rows R43–R49 after the 10:39 HANDOVER are long +2.2K; full agent JSON +1K. Tuning → his plate (R52) |
