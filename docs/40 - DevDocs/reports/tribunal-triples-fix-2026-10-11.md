# Tribunal triples fix · 2026-10-11

## §0 Headline
- All five items of prompt 339 edited with the Edit tool only; no command run beyond `grep` and `ls`.
- The 16 triple files (hubs `335`–`338`, seats `325b`–`328b`, derives `325c`–`328c`) hold 0 old hub filenames.
- `325c` now carries the one-line split rule copied from `326c`; no `DRAFT FINAL`, no `NEEDS ROUND 2`.
- One residue for the desk: the old names remain in records and drafting prompts (see DECISIONS).

## DECISIONS
- ASK DESK: the old hub names still appear in `325-draft`…`328-draft-*-tribunal.md`, `333-tribunal-triples-preflight.md`, `339-fix-tribunal-triples.md`, the four `reports/f*-tribunal-draft-2026-10-11.md` and the preflight report; the prompt's `grep -c -F` = 0 holds only for the 16 triple files. Re-point the drafting prompts too? [2026-10-11] Default: left as written (records).

## RECORDS
Proof: `grep -rl -F -e 325a-f5-tribunal.md -e 326a-f20-tribunal.md -e 327a-f21-tribunal.md -e 328a-f23-tribunal.md` over `prompts/2026-10-11/` and `reports/` lists only the residue files named in DECISIONS; none of the 16 triple files.

1. FAIL check 1, old hub name → new name (`replace_all`):
   - `335-f5-tribunal.md` (launch line, in-file launch line, cross-reference), `325b-f5-tribunal-opus-seat.md`, `325c-f5-tribunal-derive.md`.
   - `336-f20-tribunal.md`, `326b-f20-tribunal-opus-seat.md`, `326c-f20-tribunal-derive.md`.
   - `337-f21-tribunal.md`, `327b-f21-tribunal-opus-seat.md`, `327c-f21-tribunal-derive.md`.
   - `338-f23-tribunal.md`, `328b-f23-tribunal-opus-seat.md`, `328c-f23-tribunal-derive.md`.
   - Proof per file: 0 hits of its old name in the `grep -rl` above.
2. FAIL check 6, `325c-f5-tribunal-derive.md`: added the `THE REMAINING SPLIT — ONE LINE FOR DEJAN` bullet copied from `326c`. Header, §0, `## FOR DEJAN`, stop line and next-step text now read `FINAL — ONE SPLIT FOR DEJAN`, `split lines: <0|1>`. `NEEDS ROUND 2` and the round-2 hub path are removed. Proof: `grep` of `NEEDS ROUND|DRAFT FINAL|needs round` over `325c` prints no match.
3. NOTE check 5:
   - `335` and `338` stage the ladder from the working tree by anchor, as `337` does. `336` does the same. The `git show d0a5fbb8:<ladder>` instruction is replaced by a ban on it.
   - `335` stages the `configs/cobalt/taxonomy/tunables.yaml` rows found by `grep -n -F -e radar -e aset -e finviz`.
   - `336` items (e) and (g) name `cli.py` and `uv.lock` as NOT STAGED, each with a one-line reason; unread = UNKNOWN, L70.
4. NOTE check 9: `337` header, preflight floor and collate floor, and `327c`'s floor, now read Grok ruled AND the Opus seat's stop line present; Gemini counts too; a Gemini-only ruling does not let the derive run.
5. NOTE check 8: each hub (`335`–`338`) has a new `GROK SESSION CAP 3 (L15, R908)` line above `INDEX CARD`.

TRIBUNAL TRIPLES FIXED · decisions: 1
