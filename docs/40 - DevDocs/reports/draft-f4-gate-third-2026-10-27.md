# Draft f4-gate-third (prompt 1078)

## §0 Headline
- Wrote `prompts/2026-10-27/1078-f4-gate-third.md`: 1045's shape, X15 only, Opus 5.5, seat `f4-gate-third`, nine allowed tools.
- Report target `reports/f4-gate-run-third-2026-10-27.md`; stop line `GATE THIRD DONE · X15: … · peak <n>/min · 429: <n> · main <8hex>`.
- X7 and X9 carried as two `NOT RUN` `[HIS HAND]` lines; X8 and X10 not repeated.
- No existing file edited; nothing committed.

## DECISIONS
- ASK DESK: should `## RESULTS` carry the X7 and X9 `NOT RUN` lines beside X15, or X15 alone? [00:34] Default: three lines (a `NOT RUN` never counts at `deploy-step-c.sh:185-186`).
- ASK DESK: a probe `NOT RUN` or an absent `PROBE` line is written `NOT RUN`, not `FAIL`, as 1045's second pass wrote it; an `OK` line with peak > 50 or 429 ≠ 0 is `FAIL`. [00:34] Default: as written.

## RECORDS
- `date` → `2026-10-27 00:34`.
- Read in full: 1077 (the task), `prompts/2026-10-26/1045-f4-gate-run.md`, `topics/writing-rules.md`.
- `git -C /Users/cobalt/cobalt show main:docs/40 - DevDocs/reports/f4-gate-run-2026-10-26.md` → X15 FAIL line `peak 53/min … 429 3 (radar=3)` (RESULTS, line 7 of that file).
- `git show main:src/cobalt/prefill/refresh_probe.py` → output shape `PROBE X15 OK|FAIL|NOT RUN`, exits 0/1/3; `_clause` prints `peak <n>/min at <m>` and `429 <n>`; the radar bucket reads `radar_bucket_rpm()`.
- `git show main:docs/40 - DevDocs/reports/deploy-f4-strike-reserve.md` → DEPLOYED `0ea89b17`, tag `deploy-2026-10-26-f4-strike-reserve`.
- `git log main --grep=strike-reserve` → `0ea89b176` is on main's history; main head now `ce0f60ee`.
- `git grep main` → `cto-2026-10-26.md:98` R2535 (F4 gate THIRD PASS after 1049-C DEPLOYED); `F4-FINAL-2026-10-10.md:221` X15; `tunables.yaml:711` `radar.finviz_rpm`.
- Not done: no run of the probe, no launch.

DRAFTED · decisions: 2
