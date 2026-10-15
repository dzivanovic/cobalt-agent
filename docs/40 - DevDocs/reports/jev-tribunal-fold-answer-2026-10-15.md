# JEV design tribunal — the brain's fold (brain `0e848919`, 2026-10-15)

On `reports/jev-design-tribunal-2026-10-15.md` (Grok, Gemini, blind Opus seat; floor MET; all three `ADOPT AFTER …`, no REJECT). Every SPLIT is ADOPT vs ADOPT WITH, never a conflict of direction, so the fold takes the WITH texts where they agree and rules the two places they differ. Applied: R1467, R1532 (routing table), R1535 ("the key for JEV and nothing else"), `jev-design-decisions-2026-10-14.md`.

## §0 Headline
- ADOPTED WITH the folds below. The JEV card is written by a drafter from the design + `jev-design-decisions-2026-10-14.md` + this file.
- Two things come before the keyed runs, not before the build: check `74` on `jev/trial-0923` READY (decision 2), and HIS yes on the wrapper's allow string (F12, the one owner item that holds).
- Opus O2 is NOT his: R1535 covers every path to the key, upper and lower case.

## FOLDS (card rows; the drafter cites each by F-number)
| # | section | fold | from |
|---|---|---|---|
| F1 | §1 | Fix the cites that do not hold (CK6 `trial.py:158-187`, CK7 M5 count, CK8 rate, CK10/11 S6 "today"); the M5 repeat count is the trial plan's own, not the design's ×5. The call ceiling (S2) is set to cover the refresh's call count with margin; an engine tunable, no money. | Grok, Opus, ESC 18 |
| F2 | §1, §8 | ONE host-wide spend ledger, outside every checkout and worktree, seeded with the two paid lines (`$3.402e-05`); every keyed run on the host reads and books it. The $5 TOTAL (R42) binds across trial, refresh and shadow. | Grok, Opus, ESC 12 |
| F3 | §1 | The cap check runs BEFORE a call, on the worst-case cost of that call; a call that could cross $5 is not sent. Red: a ledger at $4.9999 refuses a call whose ceiling cost passes $5. | Grok, ESC 13 |
| F4 | §2 | Strip `BAND:` and `MODEL:` (with `TIP:`, `REPORT:`, `CHECK REPORT:`) from the card text before the call: JEV must not read the drafter's answer. | Opus |
| F5 | §2 | Route by the R1532 table ONLY. Rule 1 (`write_path`/`migration` ≥ 0.5 → Opus) and the `min_confidence` fallback are REMOVED from routing; the gates are recorded, never routed on. Migrations and money are HIGH by the drafter's band definition, so the Opus floor lives in the band, not in an unmeasured 0.5. | Opus, Grok (apart), Gemini (on fallback); ESC 8, 22 |
| F6 | §2 | The `## BUILDERS` load check accepts every model the R1532 table names (Opus included); no refusal of the table's own rows. | ESC 9 |
| F7 | §3 | ONE outcome store: JEV's ledger IS R1532 condition 4's results ledger; card 583's hand-filled file is retired when this card deploys (as 583 says). Record the drafter's `BAND:` beside JEV's band. | Opus, ESC 10 |
| F8 | §3, §4 | The ledger lives with the spend ledger, outside the repo and every worktree (blind: no builder, checker or tribunal seat reads it on its card); only the weekly read's aggregates are written to `reports/`. No write into `~/cobalt` by the close. | Grok, ESC 15, 16 |
| F9 | §4 | The batch runs after the close's verdict, over cards whose check has closed; every `ClassifyError` (401/403, transport, cap, ceiling) is caught and written as a `status` value (enum widened), exit 0; a wall-clock bound (engine tunable, set from X5). The close never fails or waits on JEV (decision 6). | Grok, Opus, ESC 14 |
| F10 | §5 | Predeclare the prediction method and loss in `route.yaml` before any outcome is read; the weekly read prints n and "insufficient data" under 30 (L8) and never retires JEV by itself; retirement is a card. | Grok, Opus |
| F11 | §6 | Replace `:140` (R1532 supersedes "every merged build is Opus"); add G7: JEV's band vs the drafter's `BAND:`; G5 is a share of decision rows. | Opus, Grok |
| F12 | §7, §8 S10 | The keyed wrapper's allow string on the runner's line is a permission that opens the vault inside the wrapper: HIS word, not K5 (LAWS :408). Asked of him now. | Opus O1, ESC 17, 24 |
| F13 | §7 | Close BOTH old-tree paths to the key: the lower-case mapping (`src/cobalt_agent/config.py:493-505`) and the upper-case path (`config.py:596-615` → `llm.py:108-115`, `configs/config.yaml:38`, `:56-63`). Red for each: a test environment holding the key reaches the old LLM config today, not after. Authority: R1535, his words cover any path. | Opus E1/O2, ESC 11 |

## OWNER ITEMS
- Opus O1 → F12, his (asked).
- Opus O2 → not his: R1535 ("the key for JEV and nothing else") covers it.
- Gemini's go-live line restates R1467: already his, nothing new.

## ORDER
1. Drafter writes the JEV card (MID band: new code, no migration, no money beyond the ruled cap). 2. Check `74` on the trial branch (its own check card) in parallel. 3. Build, check, deploy (shadow; nothing routes). 4. Keyed refresh runs and the nightly batch start only after `74` READY and his yes on F12.

## FOR THE CHECK
`JEV tribunal folded F1–F13: one host spend ledger checked before each call; BAND/MODEL stripped; route by R1532 only (rule 1 and min_confidence removed); one outcome ledger outside the repo; close never fails on JEV; both old-tree key paths closed (R1535); wrapper allow string is his — brain 0e848919 10-15`
