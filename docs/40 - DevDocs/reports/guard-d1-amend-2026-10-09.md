# Guard D1 card 162 amended · 2026-10-09

## §0 Headline
- Preflight r2 FAIL (check 9) fixed: K1 (2) no longer lists T2 `--allow-{prod,x}`.
- Over-refusal NOTE added as one `## RECORDS` line.
- Nothing else in the card changed; `BASE`, `TIP`, `REPORT:` untouched.

## CHANGES
- `prompts/2026-10-09/162-guard-d1-card.md` K1 (2): `T1 …, --pr{od,od} and T2 --allow-{prod,x} fail` → `T1 …, --pr{od,od} fail (T2 --allow-{prod,x} stays green: PROD_OPTION matches the unexpanded word)`.
- Same card, `## RECORDS`: new line after the first over-refusal line naming `git commit -m "- fix prod notes"` and `echo "-- prod"` as refused for a non-deploy seat; accepted, not a block.

## DECISIONS
1. Drop the case from (2)'s list; keep T2's case `--allow-{prod,x}`. Smaller edit (one clause), T2 unchanged, and the case still fails under (4). (2) keeps two T1 cases that only the expansion catches. Not taken: `--allow-p{rod,x}` (rewrites a T2 case).

## RECORDS
- `ops/desk/bare-guard.py:111` `PROD` has no `--allow-prod` match (`(?<![\w-])--prod`); `:943` G2 tests `PROD.search(command)` only (BASE).
- `ops/desk/bare-guard.py:773-784` `braces()` expands `{a,b}`; `PROD_OPTION` is F1's new regex (absent on main, grep prints nothing), `^-.*(?<![a-z])prod(?![a-z])`: on `--allow-{prod,x}` `prod` follows `{` and precedes `,`, so it matches the unexpanded word. Mutation (2) leaves the case green; (4) drops the clause, so `--allow-prod` expanded hits neither regex and it fails.
- Read, not run (nothing was executed).

GUARD D1 CARD AMENDED · decisions: 1
