## §0 Headline
- Card `prompts/2026-10-19/820-f21-genesis-check-card.md` drafted: a CHECK of `ops/f21-genesis-1013`, BASE `40e646ed`, TIP `66439da6`, rows S0, G1-G6, X3, X4, X5, R2, W1.
- Proved by command: merge-base `40e646ed`; the head `817a07c3` adds only the build report and its `.result`; the build card header values and the build stop line match your facts.
- Nothing was run (no test, no mutation); commits: none.

## DECISIONS
1. ASK DESK: `HOUSE A: grok` is not in card 468; I copied it from the precedent card 817. Default taken: kept (Grok is the first house of the SEAT ORDER anyway). [07:29]
2. ASK DESK: no `BAND` line, because card 468 carries none (CARD.md requires it on a check only when the build card does). Default taken: left out. [07:29]
3. ASK DESK: `0026_genesis_chunk.sql` has no `GRANT` line; `0025_dml_roles.sql:48-75` has default privileges. Whether they cover the new table is unproven; I made it row G1 / ask X4 for the check to prove. Default taken: asked, not asserted. [07:29]
4. ASK DESK: F5's renumber. `main` `b6ede5c1` (R1993, prompt 821) already says K6 takes `0027`, and card 731 holds `0027` four times in the working tree, so the pending-direction wording in your prompt is stale. Default taken: the card says F5 takes `0027` and the check changes nothing for F5 (ask X7); the "desk takes 0026 back if Genesis fails" line is carried. [07:29]
5. ASK DESK: the REVERSE-mutation row (X3) names six test files by my own pick (archiver, dml_roles_offline, seam registry, p4, migrate_level, migrate_proof); I did not run it. Default taken: the check may widen the list. [07:29]

## RECORDS
- `date` 07:27:43 and 07:29:18 EDT; `main` HEAD at read `b6ede5c1`.
- `git -C /Users/cobalt/cobalt merge-base ops/f21-genesis-1013 main` → `40e646edf7264b21191b2b63f5fbbb2dede793c7`; `log --oneline 40e646ed..ops/f21-genesis-1013` → `817a07c3`, `66439da6`, `9f742f73`; `diff --name-only --no-renames 66439da6 ops/f21-genesis-1013` → the build report and its `.result`.
- Build stop line (last line of the build report): `BUILT · job: f21-genesis-1013 · tip: 66439da6 | on 40e646ed | migration: 0026, rolled back | … | self-check: 3 of 3 | decisions: 3`.
- Card written: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/820-f21-genesis-check-card.md`. Files read: 817 card, `CARD.md`, `CHECK-HUB.md`, 468 card, 821 prompt, the build report (`## E3` to `## DECISIONS`), `0026_genesis_chunk.sql`.

DRAFTED · decisions: 5
