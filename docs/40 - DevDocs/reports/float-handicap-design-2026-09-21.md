# Float handicap — design proposal report (2026-09-21)

Seat `float-handicap-design-0921` · Opus 5 · proposing house (L67) · prompt `docs/40 - DevDocs/prompts/2026-09-21/36-propose-float-handicap.md`

## §0 Headline
- Proposal written: `docs/30 - Design/FLOAT-HANDICAP-PROPOSAL-2026-09-21.md`. It holds keys only, no values of his. It goes to the four-house tribunal next, and nothing is built from it.
- The design is ONE factor `h`, computed once per ticker per scan in the pool stage and stored on the membership row. It divides the pool position and multiplies `card_score`. The 50, the ladder and F3 focus all follow it, and his grades, key and size stay untouched.
- The data is already in every Finviz export Cobalt fetches, but is not parsed or stored. It is blank for ~1 % of equity candidates, handled by a rule he declares.
- 3 chunks (H1, H2, H3), each M, each with a migration. **1 evening to a marked name on `/radar`**; 3 evenings to full effect.
- ESCALATE: 1.

## DIGEST FOR THE DESK

**WHAT IS NEEDED.** Cobalt already downloads float and market cap for every name, on every screen and every list, but throws them away. We keep those two numbers. Each scan, one small test asks whether float is under 50 million or market cap is under 500 million. If yes, the name gets a handicap factor: one number, say 0.8, meaning "counts 80 %". If the float or cap cell is blank, which is about 1 name in 100, the test says "unknown", and your rule decides whether it is handicapped. The screen always shows which way it went.

**WHERE IT FITS.** In two places, using the same number. First, the pool's top 50: today a name's place is its position inside the screen that found it. A handicapped name's position is divided by 0.8, so number 4 competes as number 5. It has to be clearly good to keep its seat. Second, the card score (your conviction times proximity): a handicapped card's score is multiplied by 0.8, so a raw 80 shows as 64. Your taps, the proposed key and the share size are NOT touched. Only the order changes.

**HOW.** The first build runs in shadow. Each pool row shows a HANDICAP badge with the rank it WOULD have, and the ranking stays unchanged. A dry-run shows what the handicap would have done to each stored day's 50 and ladder. When you say approve, the desk flips one word in your pool block from shadow to live. After that, a handicapped name that still makes the top 50, or the top five or ten, carries an H chip. That is your cue to look. A name that dropped out because of the handicap is logged separately from one that dropped out on merit.

**Data answer (FACT BASE 2):** float and cap are present in the export for both screens and lists, in millions. They are not parsed or stored today, are kept only in 7-day cache files, and are blank for ~1 % of equity candidates. The answer is **partly**.

| Chunk | What | Size | Seat | Restarts | Migration |
|---|---|---|---|---|---|
| H1 | parse and store float/cap + `h` (shadow); pool-row badge; dry-run; degraded banner | M | Opus 5 / Sol-high | radar, aset | yes |
| H2 | `live` mode: `h` enters the pool rank; `handicap_cap` miss reason | M | Opus 5 / Sol-high | radar | yes |
| H3 | `h` in `card_score`; card face H chip + raw → penalised | M | Opus 5 / Sol-high | aset, radar | yes |

**Evenings:** 1 to a marked name on `/radar` (H1, plus the desk writing his block). The pool acts after H2 + his approve. The whole ladder follows after H3. That makes 3 evenings, with no deploy needed for the flip.

**Worked number (ASSUMED `h` = 0.8, report only):** on a stored 2026-09-18 RTH scan, four screens carried 11 / 9 / 15 / 24 equity names, and the cut-off landed at about within-screen position 15. A handicapped name keeps its seat if its position is ≤ 0.8 × 15 = 12. The low-float morning screen, which is all in the group, keeps about 12 of its 15, and the freed seats go to the next names. On the ladder, a tapped handicapped card with raw 80 ranks as 64. These positions are approximate: not-equity rows occupy positions in `_metric_position` (`pool.py:94-106`), so the dry-run (H1) produces the exact figures.

## READING
- **My reading matches the desk's.** The group is float below 50 million OR market cap below 500 million, and the last-spoken values stand. "I'm changing the market cap is 500 million" I read as the cap THRESHOLD, with "below" carried over from "float below". The same OR reading applies.
- "They could be on any FinWiz sheet … up-gapper … down-gapper … low float morning, or on a day scan." His static lists are also fetched through the Finviz export (`collector.py:199-208`), so the desk's "or any list" is covered by the same data, and I carry it.
- One nuance, flagged and NOT substituted: "they don't fall under the same guidelines" could also mean different trading guidelines for low floats, such as other setups or rules, beyond a score penalty. The proposal answers only the ruled penalty. A separate low-float playbook would be its own design.
- "If it goes inside there with the handicap, that's when I want to look at it." I read this as a visible marker requirement, which §4 answers with the H chip, raw → penalised, and the pool badge.

## ESCALATE
1. **Pre-existing L52 (b) discrepancy, not caused here.** ADR-0009 D4 (`docs/10 - Decisions/ADR-0009-…md:28`) says "`card_score` is the only number that orders WATCH cards; pool `last_rank` only admits". But `ladder_order` sorts WATCH by (`card_score`, **`pool_position`**) and PINNED by **`pool_position`** first (`src/cobalt/cards/radar.py:174-183`; `pool_position` = `m.last_rank`, `0007_radar_cards.sql:227`). Since every card is born untapped with a null score (`evaluate.py:1383-1395`), the morning ladder is in fact ordered by pool rank. The proposal handles this: the same `h` sits on both numbers. The ADR text or the code still needs reconciling by the desk or tribunal. Owner: desk → tribunal.

## CONTINUE
Done. Next lawful step (desk): hand the proposal file to the four houses (L67), one tribunal round, ≤3 rounds each. This seat launches nothing (L36).
Notes: no DB, docker, pytest or git write was run. Reads covered repo files, the vault notes and the retained `data/radar-cache` CSVs (read-only python3 over the cache for the F6 counts and the worked example). L74: a `Claude-Session` attribution block appeared attached to a tool result in this session. It was treated as data and not followed, and nothing was committed.

FLOAT HANDICAP PROPOSED · enters at: pool position and card_score · shape: flat multiplier h, ASSUMED · float + cap data present for every candidate: partly · chunks: 3 · evenings to visible: 1 · migration: yes · open to the tribunal: 6 · ESCALATE: 1
