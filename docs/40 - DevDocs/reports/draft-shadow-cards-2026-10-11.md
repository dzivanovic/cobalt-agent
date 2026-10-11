## §0 Headline
Nine shadow cards written, 365-373 (LOW, MID, HIGH × grok, sonnet, terra), under `prompts/2026-10-11/`.
ROWS byte for byte (checked by `grep -v -x -F -f`: only header lines differ), except X1 on 365 and 367 (desk, R1097).
Not committed: no git write in this seat. The launcher refuses an uncommitted card, so the desk commits all nine before any launch.
Launcher not run (L36); each requirement proved by reading `desk-launch.sh` at main HEAD `973406bf`.

## DECISIONS
- ASK DESK: JOB is the original's JOB plus the slug (`strike-fallback-env-1010-grok`, `radar-display-fix-1008-sonnet`, `s4-p1-1009-terra`), so REPORT and CHECK REPORT names carry the date suffix of the original job. Default: kept as written. [15:00]
- ASK DESK: `TIP:` stays as an empty line, as the launcher test fixture shows (`TIP: ""`); the desk fills it before each shadow check (`[F-18]`). Default: empty. [15:00]
- ASK DESK: the desk commits the nine cards (the launcher refuses a card not committed on main, `desk-launch.sh:974-976`). Default: desk commits, then launches each with `desk-launch.sh shadow <card> --model <id>`. [15:00]
- ASK DESK: `SHADOW-HUB.md` line 1 still carries `INSTALL: 2026-10-11 R1069 · … · APPROVED` and no `«INSTALL`; `desk-launch.sh:892` refuses only `«INSTALL`, so it passes. Default: none to do. [15:00]
- ASK DESK: the X1 row on 365 and 367 came from a peer message (cto-desk, R1097 and its correction), not from the prompt file; it supersedes "ROWS byte for byte" for that one row. Built from the correction: the third step appends `X1 WRITE OK` to the card's REPORT path, no `x1-probe.txt`; the report path is written out for each card. Default: kept; if the desk did not send it, delete the X1 row from 365 and 367. [15:00]
- Placeholder tokens: none. The original rows' own `<…>` text stays inside the byte-for-byte rows. The `«FILL` and `«INSTALL` tokens appear nowhere.

## RECORDS
Cards (all under `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/`):
1. `365-shadow-strike-fallback-env-1010-grok-card.md`
2. `366-shadow-strike-fallback-env-1010-sonnet-card.md`
3. `367-shadow-strike-fallback-env-1010-terra-card.md`
4. `368-shadow-radar-display-fix-1008-grok-card.md`
5. `369-shadow-radar-display-fix-1008-sonnet-card.md`
6. `370-shadow-radar-display-fix-1008-terra-card.md`
7. `371-shadow-s4-p1-1009-grok-card.md`
8. `372-shadow-s4-p1-1009-sonnet-card.md`
9. `373-shadow-s4-p1-1009-terra-card.md`

What changed, per card, against its original (read whole: 215, 118, 72):
- 365, 366, 368, 369, 371, 372 (and 367, 370, 373): JOB, BRANCH `shadow/<job>`, WORKTREE, REPORT, CHECK REPORT (shadow's own, `-2026-10-11`), RULINGS (original's plus `2026-10-11 R1069`), `TIP:` emptied, new `SHADOW OF:` (original's absolute path). BASE, LADDER, HOUSE B and every body line unchanged. Line count = original + 1.
- 365 and 367 also: first ROWS row X1, the sandbox proof (R1097). Line count = original + 2.
- Sonnet 366: no X1 (desk).

Reads and proofs:
- FINAL `## 2.1`, `### 2.2` step 1, `[F-18]`, `## SHADOW TRIAL PLAN`; `SHADOW-HUB.md` whole (launcher refusals, `## BUILDERS`: grok-4.7 `grok`, claude-sonnet-5-5 `sonnet`, gpt-5.6-terra `terra`, all three signed `2026-10-11 R1069 · HIS RULING · APPROVED`).
- Launcher shadow checks, `desk-launch.sh:1330-1363`: `SHADOW OF:` present (all nine); BRANCH starts `shadow/` (all nine); JOB ends `-<slug>` (all nine); `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` non-empty (`:936`); REPORT under `$WT/<worktree>/docs/40 - DevDocs/reports/*.md` (`:1317-1320`), WORKTREE equals JOB; card path `…/<nn>-<job>-card.md` with characters in `[A-Za-z0-9 ._/-]` (`:901-908`). `authorize.sh` and `preflight.sh` shadow arms reuse build's checks (`authorize.sh:51`, `preflight.sh:52`). Fixture header shape: `tests/ops/test_desk_launch_shadow.py:119-137`.
- BASE commits exist: `8f4bbe28`, `50b0cd87`, `e4586978` (`git rev-parse --verify`).
- RULINGS rows, one each, "HIS RULING" and "APPROVED", committed at HEAD (cto files clean against HEAD): R685 `cto-2026-10-08.md:38`; R598 `cto-2026-10-06.md:97`; R1069 `cto-2026-10-11.md:33`. `cto-2026-10-08.md` has an uncommitted one-line deletion in the working tree (not the R685 row); the launcher reads the row at HEAD.
- Not run: the launcher itself (L36) and `authorize.sh` or `preflight.sh`, which need the committed cards.

DRAFTED · decisions: 5
