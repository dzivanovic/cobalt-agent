## §0 Headline
M6 drafted: `DEPLOY-HUB.md` curl entries now use `https://cobalt.taild24291.ts.net/`.
Changed lines `:11`, `:123`, `:147` (`:147` holds three curls); line numbers matched the card.
`:146` (`Uvicorn running on http://0.0.0.0:5010`) untouched. No other file edited. Not committed (no git write).

## DECISIONS
- ASK DESK: `STANDING-LIST.md:153` lists the same old `http://127.0.0.1:5010/*` curl allow entry as `DEPLOY-HUB.md:11`; edit it in the same commit? Default: yes, the desk edits it with this commit. [2026-10-10]

## RECORDS
- `grep -n -F "127.0.0.1:5010"` before the edit: `:11`, `:123`, `:147`. Same as the card, no drift.
- One Edit call (`replace_all`) of `http://127.0.0.1:5010/` → `https://cobalt.taild24291.ts.net/`; the pattern occurred only on those three lines (five times in all: `:11` once, `:123` once, `:147` three times).
- `grep -c -F "http://127.0.0.1:5010" DEPLOY-HUB.md` → `0`
- `grep -c -F "0.0.0.0:5010" DEPLOY-HUB.md` → `1` (`:146`)
- `grep -n -o -F "https://cobalt.taild24291.ts.net" DEPLOY-HUB.md` → `:11`, `:123`, `:147` ×3 (five occurrences on three lines; `grep -c` would read `3`, counting lines)
- `git diff --stat -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `1 file changed, 3 insertions(+), 3 deletions(-)`

M6 DRAFTED · decisions: 1
