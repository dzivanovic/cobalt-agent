# Float handicap tribunal — re-issue of `38` / `40` with question (k) (2026-09-21)

Seat: `float-handicap-tribunal-reissue-0921` · Opus 5 · prompt `prompts/2026-09-21/41-reissue-handicap-tribunal-q17.md` · LADDER `OFF-LADDER — ruled cto-2026-09-21 R28 / R29`

## §0 Headline
- `38` and `40` are re-issued in place (L19). The houses' question set now has 17 items: (k) TIERS is added after (j), in the desk's wording, unchanged.
- `38` gains one excerpt, `pool-tiers.excerpt.py` (≈ 5.5 KB), and one `greps.txt` search. The packet grows from ≈ 170 KB to ≈ 180 KB.
- Every `16` became `17`, and every `(a)–(j)` / `(a) … (j)` span became `(k)`. Nothing else changed. Both launch lines are proven unchanged, and `DERIVE ROW: R30` is intact.
- `39` was not touched, and the Fable round-1 report was not opened. No value of his appears in either file or in this report. No new rule string.
- ESCALATE: 2.

## DIGEST FOR THE DESK
- **`38`**: 62 lines both before and after (50,676 → 52,375 B).
  - (k) sits at the start of line 39, just before `THEN OWNER`, so no line number moves.
  - The excerpt was added to §1 (7), and the search to §1 (8).
  - Astra's reading order is now step (4): `pool.py` whole, then `pool-tiers.excerpt.py` whole.
  - Every PARTIAL count now reads `of 17`, the collate table covers O1 … O6 and (a) … (k), and the stop line reads `PARTIAL <k> of 17`.
- **`40`**: 29 lines and 15,177 B, both before and after (each swap was the same length). The fold-table item span is now `(a)–(k)`, and the astra requirement is `PARTIAL <k> of 17`. Line 1 is still `DERIVE ROW: R30`.
- **Excerpt choice.** The ranges are `pool.py` :125–137 (`priority` map and group), :154–165 (`first_from` and the min over screens), :206–212 (key tuple :209) and :323–334 (held members take seats before `ordered[:seats]`, :332–333), plus `models.py` :75–116 (`PoolOverride.first_from`, `PoolBlock.priority` and its validator).
  - The :323–334 range is there because (k) asks about "any other mechanism that admits a source's names ahead of the ranked competition". It is code only, with no comment on it.
  - The proposal names `priority group` and `first_from` in its F1 table (PROPOSAL :13), and I read it only to choose these ranges. I judged nothing.
- **New search:** `grep -rn -e first_from -e priority /Users/cobalt/cobalt/src/cobalt`. At drafting it returned 19 lines (≈ 2.1 KB) in `cards/radar.py`, `radar/models.py`, `radar/pool.py` and `aset/radar_panel.py`. `greps.txt` now has 14 searches (the draft counted 13). `38` states no search count, so no count sentence changed.
- **Tool used:** I made the changes with the Edit tool on the committed bytes, not the Write tool. That way every unchanged byte stays unchanged: Write strips trailing whitespace, and retyping 50 KB is a transcription risk. The disk copy of `38` equalled HEAD before the edit (50,676 B both).
- **Next:** the desk commits `38`, `40` and this report, then launches `38` when its stagger allows.

## EVERY CHANGED SENTENCE

### `prompts/2026-09-21/38-float-handicap-tribunal.md`
| # | line | old | new |
|---|---|---|---|
| 1 | 1 (METER) | `the packet is ≈ 170 KB (≈ 43k tokens if a house reads every file whole — the drafter's estimate, … `## PACKET`)` | `the packet is ≈ 180 KB (≈ 45k tokens if a house reads every file whole — the drafter's estimate, … `## PACKET`, plus ≈ 9 KB for item (k), `reports/float-handicap-tribunal-reissue-2026-09-21.md`)` |
| 2 | 21 (§1 (7)) | `… `src/cobalt/cards/store.py` :1185–1227 (the tap path).` | `… (the tap path) · `pool-tiers.excerpt.py` (item (k), ≈ 5.5 KB) = `src/cobalt/radar/pool.py` :125–137 (anchor `priority = {name: index` at :127), :154–165 (anchor `first_from = (` at :154), :206–212 (anchor `return (priority[group]` at :209) and :323–334 (anchor `seats = max(0, pool.cap - len(held))` at :332), `src/cobalt/radar/models.py` :75–116 (anchor `first_from: str \| None = None` at :78, `priority: list[Literal` at :104).` |
| 3 | 22 (§1 (8)) | `… `grep -rn degraded_sources …/radar_panel.py` · `grep -n -e "Shares Float" …` | a new item between them: `grep -rn -e first_from -e priority /Users/cobalt/cobalt/src/cobalt` (item (k): the pool's tiers and every reader of them) |
| 4 | 39 (QUESTIONS) | `THEN `OWNER (after the tribunal):` …` | `**(k) TIERS.** Pool admission is tiered … name the ones it misses. THEN `OWNER (after the tribunal):` …`. The (k) text is the desk's, verbatim. |
| 5 | 47 (astra) | `This packet is about 170 KB; read in THIS ORDER …: … (4) pool.py whole; (5) cards-radar.py whole.` | `This packet is about 180 KB; …: … (4) pool.py whole, then pool-tiers.excerpt.py whole; (5) cards-radar.py whole.` |
| 6 | 47 (astra) | `Everything else - radar-models.py, the *.excerpt.* files, …` | `Everything else - radar-models.py, the other *.excerpt.* files, …` |
| 7 | 47 (astra) | `rule the items in the order O1, O2, ... O6, (a), (b), ... (j), then OWNER …` | `… (a), (b), ... (k), then OWNER …` |
| 8 | 47 (capture) | `… items ruled: <k> of 16 (<ids>)` … `O1–O6 and (a)–(j) are the 16` … `astra: PARTIAL <k> of 16 — …` | `<k> of 17` … `O1–O6 and (a)–(k) are the 17` … `astra: PARTIAL <k> of 17 — …` |
| 9 | 49 (house field) | `for astra also `PARTIAL <k> of 16 — <reason>`` | `… `PARTIAL <k> of 17 — <reason>`` |
| 10 | 52 (collate) | `one row per item — O1 … O6, (a) … (j):` | `one row per item — O1 … O6, (a) … (k):` |
| 11 | 62 (stop line) | `astra: <its TRIBUNAL R1 line\|PARTIAL <k> of 16 — <reason>\|…` | `… PARTIAL <k> of 17 — <reason> …` |

Left as they were, on purpose:
- :27 `name it as an experiment under (j)`: (j) is still the experiments item.
- :38, the (j) heading.
- :14 `Every file here is under 38,000 B: nothing is split` (see ESCALATE 1).

### `prompts/2026-09-21/40-float-handicap-tribunal-derive.md`
| # | line | old | new |
|---|---|---|---|
| 12 | 5 (ASTRA WAS REQUIRED) | `astra: PARTIAL <k> of 16 — …` with k ≥ 1 | `astra: PARTIAL <k> of 17 — …` with k ≥ 1 |
| 13 | 26 (fold table) | `item (O1–O6, (a)–(j), WRONG FACTS)` | `item (O1–O6, (a)–(k), WRONG FACTS)` |

## RULE PROOF
| check | command | result |
|---|---|---|
| `38` launch span, old | `grep -c -F -e "<claude --bg … --add-dir /Users/cobalt/cobalt-wt>"` on the saved `git show HEAD:` output (50,676 B, = disk before the edit) | **1** |
| `38` launch span, new | same `grep -c -F -e` on the re-issued `38` | **1** |
| `40` launch span, new | `grep -c -F -e "<claude --bg … --add-dir /Users/cobalt/cobalt-wt>"` on the re-issued `40` | **1** |
| `40` launch span, old | `git -C /Users/cobalt/cobalt log --format=%H -S"<same span>" -- <40>` returns ONE commit (`323ce515`, the one that added it); no later commit changes its count, and `git show HEAD:` shows it once on line 3 | **1** |
| `40` line 1 | `grep -c -x -F "DERIVE ROW: R30"` | **1** |
| `40` unfilled row | `grep -c -x -F "DERIVE ROW: R__"` | **0** |
| leftovers | `grep -o -E ".{50}(of 16\|\(j\)\|16\)\|170 KB\|43k).{30}"` on both files | only :27 `experiment under (j)`, which is correct |
| line counts | `wc -l` | `38`: 62 → 62, `40`: 29 → 29 |

The span is the whole first-line run from `claude --bg` to the last `--add-dir /Users/cobalt/cobalt-wt`, with every quote included. No edit touched line 1 of either file inside that span. `38`'s line-1 edit is in the METER clause, after it.

**NEW strings:** none. No `--allowedTools` / `--disallowedTools` string was added, removed or changed. No gate, window, stagger, AUTHORIZATION grep or rule string was touched.

## ESCALATE
1. `ASK DESK: greps.txt was estimated at ≈ 37,000 B (draft `## PACKET`). The (k) search adds ≈ 2.1 KB of output (19 lines at drafting), so the total may cross 38,000 B, and `38`:14 still says "Every file here is under 38,000 B: nothing is split" (left unchanged as instructed). Safe default: `04`'s §1 staging rule (parts ≤ 38,000 B, `wc -c` per part), which `38`'s INDEX CARD (2) already binds, covers a split, and the hub's `## Packet` records the real size. Do you want a re-issue to reword :14? [2026-09-21]`
2. **(k) has no Fable-seat ruling.** `39` ran on 16 items and is not touched, so in `40`'s fold table item (k) can be ruled by at most 3 of 4 seats (Grok, Gemini, Astra). `40`'s per-item seat count (`<n> of 4, named`) already carries this, and no text was changed for it. The desk may want to note it in the row it records for the derive.

Note, not an escalate: the desk's (k) wording says `models.py`, while the packet stages that file as `radar-models.py`. It is staged as written, and QUESTIONS' "Files in this folder:" paragraph (§1 (9)) maps the name.

## CONTINUE
next: done. Nothing launched, nothing committed. The desk commits `38`, `40` and this report.

FLOAT HANDICAP TRIBUNAL REISSUED · questions: 17 · files: 2 · sentences changed: 13 · launch lines unchanged: proven · packet: 180 KB · new rule strings: 0 · ESCALATE: 2
