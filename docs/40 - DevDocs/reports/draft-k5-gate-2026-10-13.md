# draft-k5-gate — 2026-10-13

## §0 Headline
Card 446 written: `prompts/2026-10-13/446-k5-gate-card.md`, CLASS K5, header per the desk's values, `BASE` the only placeholder.
Rows RF (four seams in THE RULE), A1 (RUNS table `HELD, NOT FIXED`), B1 (`<Class>::<name>` ids, method read in its class), C1 (the sweep test), C2 (folds: lowercase spelling, several-id line), R2 (restarts RUN).
By reading: 304's check gives 0 ids on `BASE`, 2 after A1. The sweep cannot be pinned at zero without named exemptions for reports no mark resolves (ASK DESK 1, 2, 4).
Nothing was run; every count marked UNPROVEN in the card's `## RECORDS`. No new command, link or seat.

## DECISIONS
1. ASK DESK: a bare verdict `HELD` (kill-hub-row-check `:142-155` twelve table rows, n 12; s4-p1-1009-terra-check `:272-296`, n 2; radar-display-fix-1008-terra-check `:137-142`, n 6; `HELD (shadow …)`, `HELD: <why>`) carries no NOT FIXED mark, and CHECK-HUB `:104` writes `HELD` for a finding the check fixed too, so no reader can tell the two. Fold by counting them (over-counts fixed ones) or leave unread and name each report in `SWEEP_EXEMPT`? Default: leave unread, exempt by name with its reason, the `**HELD**` fixed-row over-count (gate-alignment-check `:137`, `:169`; held-table-row-check `:169`) kept as card 361 settled it. [05:54 ET]
2. ASK DESK: `SWEEP_EXEMPT` as a named, pinned table (an entry that stops mismatching fails the suite) so row (c) holds "zero mismatches" outside it; the alternative is no exemption and a rewrite of the reports, which R1157 forbids. Also one report the reader cannot resolve by any mark: the same defect under two ids in two passes (`drc-d5-check-2026-10-04.md:174`, `:354`, n 1, read 2). Default: yes, exempt table. [05:54 ET]
3. ASK DESK: the sweep's window is the files dated 2026-10-02 to 2026-10-12 with their count pinned, so a check report written later is not swept (a new report with a new shape would otherwise turn `tests/ops` red on main). Open-ended is the other reading of "since 10-02". Default: bounded. [05:54 ET]
4. ASK DESK: `f4-refresh-build-2026-10-10.md:262` (`- **CARRIED: O1 — …::TestCheckFindings::… — R998. FOR DEJAN.**`, bullet, bold, trailing sentence) stays unread and is a named exemption: folding it would count 304's O1 and A3 twice beside row CR's two plain lines, and the gate would refuse `has 2 FIXED or CARRIED lines`. The several-id line (`shadow-hub-build-2026-10-11.md:257`, `FIXED: O2 B5 — …`) IS folded, one line per id. Default: as written. [05:54 ET]
5. ASK DESK: a class-level `@pytest.mark.xfail` decorator on the class of a FIXED test is not read today (the plain form's CARRIED case is pinned, `test_h1_a_carried_class_decorator_is_not_the_defs_decorator`), so such a FIXED id passes. Out of scope here. Default: not fixed in card 446, a follow-up row. [05:54 ET]
6. ASK DESK: the lowercase spelling `HELD, not fixed` is folded (two spellings only, no case folding), because three 10-11 shadow check reports use it. Default: fold. [05:54 ET]

## RECORDS
- 05:54 ET (`date`), `main` HEAD `ffd5e7a8` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`); `git -C /Users/cobalt/cobalt status --short -- ops tests` → nothing.
- Read: `CARD.md`; `cto-2026-10-13.md` rows R1309-R1311 and `§5` first OWED; `f4-refresh-check-2026-10-10.md` `:133-171`, `:212-216`, `:246`; `f4-refresh-build-2026-10-10.md` `:200-290`; `deploy-card.sh` `:1-40`, `:130-394`, `:440-490`; `desk-launch.sh` `:1422-1444`; `deploy-step0.sh` `:640-664`; `test_deploy_card.py` `:1-46`, `:598-662`, `:770-818`, `:1048-1190`; precedents `397-gate-alignment-card.md`, `361-held-table-row-card.md`, `441-backup-flock-card.md`; `BUILD-HUB.md` `:7-75`; `restarts.py` (Grep).
- Greps: `held unfixed: [1-9]` and `HELD, NOT FIXED|HELD, not fixed|held, not fixed` over `*-check*-2026-1*.md` (full lines kept in the job's tool-results file); `^#+ .*RUNS|^#+ .*FIXES`; `(FIXED|CARRIED|SETTLED): …` over `*-build*`/`*-fix*`; `^BUILT ·|^FAILED:` over `*-build*` (86 files, two dated 10-01); RUNS/FIXES sections read in 20 reports (listed in the card's shapes).
- Reads that cut short: the digits of `n` beyond the first for reports grepped with `[1-9]` (kill-hub-row-check is `held unfixed: 12`, read whole at `:213`); RUNS shapes of adoption-hubs(-r2), brain-hub, held-closed, gate-alignment, held-table-row were NOT read (card shape 10).
- Allow lines: none new; `ls -la /Users/cobalt/.claude/ops/` shows the three scripts as symlinks into `ops/desk/` (INSTALL: none); `restarts.py:38,225-232,246` (RESTARTS: none).
- Card committed? No: written only, no git write (L36); the desk commits it before the launch.

DRAFTED · decisions: 6
