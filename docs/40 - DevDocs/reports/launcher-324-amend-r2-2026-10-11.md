## §0 Headline
- Card 324 amended per preflight ISSUES, three edits, Edit tool only.
- FAIL 12: P3 now has the RED assertion `seat(event)["kind"] == "spike"` (BASE gives `worker`).
- FAIL 3: S2 prose no longer spells the fill token; the card holds it once, line 5 (BASE).
- NOTE 7: "no word `failed`" pinned to `## RESULTS TABLE`.

## DECISIONS
None.

## RECORDS
- Card `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md`; BASE of my reads = HEAD `11029471` (`git rev-parse --short HEAD`).
- Edit 1 (P3, FAIL 12): added the RED assertion; replaced "RED on `BASE`: none, this row is a PIN" with the RED on `seat(event)["kind"]`; the fence tests stay as greens. Reads: `ops/desk/bare-guard.py:746-775` — `:767` `elif wt:`, `:768` `kind = "worker"`, no `spike` in that chain. The cited `:685-689`, `:1124-1135`, `:1127-1128` were not re-read; they are carried from the preflight (checks 6, 10), unchanged by me. Proof: Grep count of `seat\(event\)\["kind"\] == "spike"` finds it in the card.
- Edit 2 (S2, FAIL 3): "`«FILL` `:799`" → "the launcher's placeholder token, `:799`". Read `ops/desk/desk-launch.sh:788-801` — `:799` `if grep -n '«FILL' "$card"`. Proof: `grep -c -F '«FILL' <card>` → `1`; `grep -n -o -F '«FILL' <card>` → `5:«FILL` (BASE line only).
- Edit 3 (S5, NOTE 7): "no word `failed` or `rank`" → "within `## RESULTS TABLE` only, no word `failed` or `rank` (the file's `FAILED:` stop line stays)". Proof: Grep finds `within `## RESULTS TABLE` only`.
- Also read whole: the card, the preflight `reports/shadow-hub-preflight-2026-10-11.md`, `Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`, prompt 341.
- Nothing else changed; no new command, no git write.

CARD 324 AMENDED · decisions: 0
