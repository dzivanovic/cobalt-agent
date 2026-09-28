# SITTING PACKETS — DRAFT REPORT · 2026-09-24 (drafter `sitting-packets-draft-0924`, Opus 5.5, read-only)

## §0
- Written, in sitting order (R14 relay): (1) `reports/sitting-second-chance-2026-09-24.md` (85 lines), (2) `reports/sitting-vwap-continuation-2026-09-24.md` (80 lines).
- Decisions for him: Second Chance 4 (touch count, touch distance, wick under the level, the curl) · VWAP 3 (how near VWAP, close under VWAP, tries per day).
- Settled by the houses: 13 (Second Chance S1–S6, VWAP V1–V7), each with its source line.
- R14 additions applied to both: §2 quotes all three PDFs verbatim with pages, §3b design provenance with "NO CHEAT-SHEET SOURCE — design invention" rows, an empty `## HIS EXAMPLES`.
- Engine read from the unmerged branch `~/cobalt-wt/setups-c1` @ `c60a7f00` (`main` has no `range_break.py`); the packets cite that tree.

| Source | Read | Note |
|---|---|---|
| `VWAP Continuation.pdf` pp.1–2 | yes | quoted §2 |
| `the_second_chance_scalp_cheat_sheet.pdf` pp.1–2 | yes | quoted §2 |
| SMB PlayBook `<ticker>` Day 2 + VWAP Continuation pp.1–11 | yes | pp.6–10 quoted; ticker as `<ticker>`; no author named (L32) |
| His notes `VWAP Continuation.md`, `Second Chance Scalp.md` | yes | read-only |
| `cto-2026-09-23.md` R82 / R107 / R116 / R117 / R118; `cto-2026-09-24.md` R13 | yes | quoted whole in §1 |
| `1 - Trading/Assumed Defaults.md` | absent | expected: tonight's deploy STEP-6 creates it |

Findings a sitting should know about (in the packets, not decisions): VWAP's "resistance rejection" is a hard avoid in the design, but the sheet lists it as a factor that lowers the odds (V1). The radar does not count tries (`max_attempts` has no reader in `src/cobalt/radar`). The Second Chance redesign changes the A-17 level set, which VWAP's `rejected` check also reads — a shared seam to settle before either build (L72).

## ESCALATE
1. `docs/_inflight/setups-assumed-values-2026-09-2x` — the gitignored companion that `SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md:29` names as the home of the A-row values, quotes and confidence levels — is gone (`docs/_inflight/` holds only `README.md`). §3b therefore takes the A-16 / A-19 / A-20 values and confidence levels from the rulings (`areas/cobalt-product-definition.md`, R82 and R119), not from the companion. I did not guess any row it held.

SITTING PACKETS DRAFTED · packets: 2 · decisions: vwap 3 · second-chance 4 · settled by houses: 13 · ESCALATE: 1
