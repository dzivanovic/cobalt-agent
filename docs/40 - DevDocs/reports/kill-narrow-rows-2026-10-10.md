# kill-narrow-rows — report (2026-10-10)

## §0 Headline
- Card 284 rows K1, K2, K3 and their TEXT blocks rewritten for the narrowed route (brain R771, L79). The header stays the desk's; the card had no FIX ROUND section.
- `--kill` runs once, at 4.2, after the per-resident bootout loop, for `aset` only. STEP-5 (3) runs the dry run only.
- K3 now names 4.2 only. D1-D6 answered below: D2 and D3 gone by the narrowing, D1, D4, D5 and D6 fixed by new TEXT.
- No file but the card and this report was written; no command run beyond reads.

## DECISIONS
- D1 (second kill via STEP-5 (3)): gone by the narrowing. K2 NEW holds no kill, so a 4.2 failure that enters STEP-5 meets a dry run only.
- D2 (hold-down vs STEP-5 (4) re-run): gone by the narrowing. K2 NEW holds nothing down; (4) and "never entered twice" read as today.
- D3 (radar's state, rule F ending): gone by the narrowing. A verified orphan ends under the existing DECISION 0 path, residents per rule F unchanged.
- D4 ("go on to 4.3" skips radar and the agent stop): fixed by new TEXT K1. The sequence runs after the loop; (5) says "go on (the agent step below, then 4.3)".
- D5 (`FAILED: <pid> survived KILL` unnamed): fixed by new TEXT K1. Exit 1 lists `REFUSED:` / `UNVERIFIED:` / `FAILED: <pid> survived KILL` → STEP-5, no second kill. K3 names exit 1.
- D6 (4.2 pids not a `DECISION 0`): fixed by new TEXT K1. Pids go under `## RECORDS`; a stop writes `DECISION 0: aset orphan <pids or the line> — FOR DEJAN`, the form STEP-7 (3) fills.

## RECORDS
- Anchors against BASE `6fe8d690` (`git show`, read from the saved output): `DEPLOY-HUB.md:137` begins `4.2 for each`; `:162` begins `- (3) THE RESTORE:`; `:163` is STEP-5 (4); `:164` is STEP-5 (5), "STEP-5 is never entered twice"; `:172-175` STEP-7, (3) fills every `DECISION 0` line. BASE line counts unchanged by the rows (K1, K2 change lines, K3 adds one).
- `ops/desk/orphan-clean.sh` (worktree equals main per the check): label table `aset` only (`:9-12`); dry-run last lines `:174` (`none found`) and `:252` (`dry-run · verified <n>`); `FAILED: <pid> survived KILL` then `exit 1` at `:296-297`; `REFUSED:` / `UNVERIFIED:` exit 1 at `:39-40`, `:60`.
- Card line anchors after the edit: K1 OLD `:26`, K1 NEW `:32`; K2 OLD `:38`, K2 NEW `:44`; K3 `:50`.
- `grep -n -o "--kill"` over the card: the K1 NEW block (`:32`) holds it once; the K2 NEW block (`:44`) holds none; K3 (`:50`) names it for 4.2 only. Other hits are rows, header and RECORDS prose.
- Not read: `standing-list-kill-row-2026-10-10.md` (the K3 wording is the card's own round-1 text, edited down).
- Not run: `tests/ops/test_hub_lines.py` and the `grep -c` marker counts on the hub files; the card's row greps are updated for the builder: `orphan-clean.sh --kill aset` → 1 in DEPLOY-HUB, `survived KILL` → 1, `(dry run ONLY, no kill)` → 1, `not held DOWN` → 0.
- STANDING RULE: no new command; none run.

KILL ROWS NARROWED · decisions: 0
