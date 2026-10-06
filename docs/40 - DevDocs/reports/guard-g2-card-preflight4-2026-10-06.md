# guard-g2 card preflight 4 — 2026-10-06

Card `21-guard-g2-card.md` (amend 4, commit `992b8fee`), BASE `3c257bb9`. Read only; I ran no test and no production command. The checks are those of preflight 3 (`reports/guard-g2-card-preflight3-2026-10-06.md`). Its only fail was 4h. I re-ran the checks that depend on the card text or on BASE. The `diff --stat` against BASE is empty for the four ops/test files and `src/cobalt/db_query.py`, so every file:line read in preflight 3 still holds.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat e78ac1c5 992b8fee -- <card>` | `1 file changed, 1 insertion(+), 1 deletion(-)`. One table row (G2) changed. The header lines (`BASE: 3c257bb9` line 5, `RULINGS: 2026-10-06 R511` line 11) are not in the diff | OK |
| 2 | `git diff --word-diff e78ac1c5 992b8fee -- <card>`, whole diff | Three edits, all in the red-first cell. (i) opening `Only (c), (d) and (g) are red on BASE` becomes `Only (c), (d), (g) and (h) are red on BASE`. (ii) CONTROL (h) is inserted after CONTROL (g2). (iii) the mutation `in desk-launch.sh drop the equality test (…control h goes red)` is appended after `the PROD-READ: refusal (red g)`. The text after CONTROL (h), `Controls, each run on the same seat that passes (c) …` and on, is kept word for word. The R1 and R2 text, the BUILD NOTES, the files column and the `NOT IN THIS JOB` section are unchanged. Nothing else in the card changed | OK |
| 3 | 4h: CONTROL (h) | Card: `CONTROL (h), the equality clause: a prompt whose RULINGS line cites <date> R<n> and whose launch line types  PROD-READ: <date> R<m> for another row (m differs from n; the row for R<m> is also committed, HIS RULING + APPROVED and naming production reads, so it is proven on its own; the row for R<n> proves too) is refused by desk-launch.sh: exit 1, no launch line (RED on BASE: the typed marker launches; green after; red again under the mutation drop the equality test)`. This is the control preflight 3 asked for: another `<date> R<m>`, its own row proven, refused, exit 1. It is paired with R1's `unless … the line holds exactly the stamp the launcher would append for that RULINGS row` | OK |
| 4 | 4h: mutation `drop the equality test` | Card mutations list: `in desk-launch.sh drop the equality test (the typed marker equals the stamp for the prompt's own RULINGS row; control h goes red)`. With the equality test dropped, the R<m> marker passes on its own proven row and the prompt launches, so (h) fails. The equality can no longer be removed with every named test green | OK |
| 5 | 4h: red-on-BASE claim for (h) | Card: `Only (c), (d), (g) and (h) are red on BASE`. BASE has no `PROD-READ:` refusal (preflight 3 4g: `desk-launch.sh:435` accepts any text after `follow it exactly.`; `grep PROD-READ` on BASE prints nothing), so the typed marker launches. (h) is red on BASE for the stated reason. The amend report DECISIONS 1 gives the same reading | OK |
| 6 | the card is internally consistent after the edit | The opening sentence names (h) among the reds; CONTROL (h) says RED on BASE; the mutation list says (h) goes red. CONTROLS (a), (b), (e), (f) are still listed green on BASE. (g2) is still the green control. No reference to a letter that does not exist | OK |
| 7 | preflight 3 checks 1a-1d, 2a-2c, 3a-3e, 4a-4g, 4i, 5a, 5b | Card text unchanged outside the three edits (check 2) and BASE files unchanged (`diff --stat 3c257bb9` on the five files empty). Their results from preflight 3 hold: all OK | OK |
| 8 | `grep -c -F "«FILL" <card>` | `0` | OK |
| 9 | `git log --oneline -4 -- <card>` | `992b8fee` (amend 4), `e78ac1c5`, `1503d5b6`, `e6c5ec90` | OK |

## ISSUES
None. 4h is closed.

Not counted, carried from preflight 3: `ruling_items` takes a comma list (`desk-launch.sh:267`) while R1 says `cites <date> R<n>` (singular), and the card does not say which item the stamp names when a RULINGS line cites several. An unquoted `$VAR`, brace or glob positional is one word to `words()`.

PREFLIGHT DONE · card: guard-g2-21 · checks: 9 · fails: 0 · ready: YES
