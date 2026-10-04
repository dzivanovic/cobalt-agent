# guard-b-judge-draft — 2026-10-04

## §0 Headline
Judge answer R254 (D1 CHANGE, D2 CHANGE, D3 KEEP) applied to `prompts/2026-10-04/06-cobalt-guard-b-card.md`.
B2 replaced, B4 added, the lone-command fence struck, one RECORDS line added, B1–B3 counts now B1–B4.
Fill placeholders and header values untouched. Two items for the desk are under DECISIONS.

## EDITS
- Row B2: old pipe-segment rule (`-o`, `--output*`, `--compress-program*`; uniq value rule) → the text given, byte for byte, with the two literal pipes inside backticks written `\|`.
- Row B4: absent → added after B3, byte for byte, with the `\|` in the G11 list escaped.
- `## NOT IN THIS JOB`: line "A lone `awk -f`, `sort -o` or `uniq <in> <out>` that is ONE command…" → struck.
- `## NOT IN THIS JOB`: "No rule beyond B1–B3" → "No rule beyond B1–B4".
- `## RECORDS`: "B1–B3 narrow its wording" → "B1–B4 narrow its wording".
- `## RECORDS`: added the line `judge 2026-10-04: D1 CHANGE (B2 by form), D2 CHANGE (B4), D3 KEEP — desk row R254; …` as the last bullet.

## DECISIONS
- ASK DESK: the card has no K25 self-check section, only "Mutation (K25 1)" inside rows, and states no row count beyond the B1–B3 mentions; I updated those two and added no mutation text for B2/B4 [any time]. Default: as done.
- ASK DESK: B2's new text says "(3)'s value rule" and "B2's existing clause", but the old B2 cell, the only place the uniq `-f`/`-s`/`-w` value rule was stated, is replaced, so the card no longer states that rule in words [before launch]. Default: byte for byte, rule not restated.
- ASK DESK: the files cell is "both files" as given, so `read_card` finds no backticked paths from B2 or B4; B1 and B3 still name both, so the fence is unchanged [any time]. Default: kept as given.

## RECORDS
- Card edited in place; no git write, no launch. Source: desk row R254 and prompt `09-draft-guard-b-judge.md`. Names checked against `bare-guard.py` at `a2e19ceb`.

GUARD-B JUDGE APPLIED · edits: 6 · decisions: 3
