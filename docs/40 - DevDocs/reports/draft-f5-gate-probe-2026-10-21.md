# draft-f5-gate-probe — 2026-10-21

## §0 Headline
- Prompt 970 amended in place: three probe strings on the launch line (X6 with `--keep-groups`, X13, X4), a keep-root placeholder step 0a, X6 → new step 1b, X13 and X4 probes in steps 3–4, the redaction line in `## RECORDS`.
- X5, X7, X10, X12 stay NOT RUN (his hand). Commit nothing, nothing run.

## DECISIONS
1. ASK DESK: the LIVE COST bullet in `## RULES` still says "step 1 only"; steps 1b and 4 now also spend a gate check and 2 GETs, 1b four local calls, 4 twenty. I left the bullet (prompt said change nothing else); the cost is written in the steps. [default: the desk amends the bullet]
2. ASK DESK: I changed the `## RESULTS` X4 and X6 lines to `<step 4>` and `<step 1b>`, and moved X6's rules out of step 1 into 1b, since the old text said "no allowed command" and a dry-run verdict. Needed, else the prompt contradicts itself. [default: kept]
3. ASK DESK: step 0a sits after step 0 (needs step 0's lock/`ls` reads first) rather than before it. The lock bullet now also makes 1b and 4's X4 NOT RUN when the lock is held (a redact hit writes a counter row, check DECISIONS 2). [default: kept]
4. ASK DESK: X5 and X10 probe strings are not on the launch line; the probe only prints NOT RUN for them, so the lines stay as `## RESULTS` spells. X7's step 2 is unchanged. [default: kept]
5. ASK DESK: X4 needs ≥1 minute after X6 (L53). The seat has no sleep; steps 2–3 sit between and a too-early gate refusal reads NOT RUN, never retried. [default: kept]

## RECORDS
- Read 14:36–14:38 EDT (`date` 14:38:35): 985 prompt; `areas/cobalt.md`; 970 whole; 973 card; check report `f5-probe-check-2026-10-21.md`; build report in `cobalt-wt/f5-probe`; `main:src/cobalt/prefill/checkpoint_probe.py`.
- Proved on `main`: `git grep` of `checkpoints.py` → `:843 cmd_probe`, `:849 PROBE_ITEMS`, `:860-863` the `probe` parser with `item` and `--keep-groups`. Probe line forms and `KEEP_ROOT` read from `checkpoint_probe.py` on `main`.
- Not read: `writing-rules.md` (not opened; shape taken from the prompt's REPORT line). Not run: any probe, any git write.

DRAFTED · decisions: 5
