# House seat order card 298 — amend 2, 2026-10-10

## §0 Headline
- Card 298 amended for the three preflight FAILs (6, 9, 11) and the S1 line-2 NOTE; header untouched (BASE `«FILL»`; TIP, CHECK REPORT, HOUSE B empty).
- No other row touched.

## DECISIONS
1. FAIL 6: every `cto-2026-10-10.md` line cite (`:48`, `:49`, `:7`, `lines 7, 48, 49`, `:48-49`) became a row id (R921, R920, R963): WHY, S1 "Backed by", READ, RECORDS.
2. FAIL 9: S1 NEW line 4 now reads "…is present and OpenAI is UP → house A is OpenAI…"; the S1 test names that spelling, so `grep -c -F "OpenAI up"` → 0 after holds (`OpenAI is UP` is not `OpenAI up`).
3. FAIL 11: took the first option: the reason text is asserted. S3 (3) fixes the stderr to `REFUSED: --card needs a path` / `… <path> is not a readable file` / `… given twice`; T6 asserts it starts `REFUSED: --card ` and lacks `is none of`; T4 row 2 asserts the `house 'sol' is probed only when the card header carries` reason. Red-on-BASE line rewritten exactly: T2, T3, T5 red on rc; T6 and T4 row 2 red on the reason; T4 row 1 red on rc 0 + codex call.
4. NOTE: S1 NEW line 2 and the S1 row text: house B only when `mandatory`; "a Grok failure after launch seats no house B (A = Gemini, no B, `## 3`)". The overlapping "house A produced nothing" case is removed.

## RECORDS
- Read against `HEAD` `0a15e2c3` (`git log -1`); working `CHECK-HUB.md` and `house-probe.sh` unmodified in `git status`.
- `reports/cto-2026-10-10.md`: Grep `^\| (R921|R920|R963) ` → 3 rows, so each id resolves.
- `CHECK-HUB.md`: `OpenAI up` → one hit, line 24 (BASE count 1); `## 3` at line 98.
- `house-probe.sh`: `none of` at line 44 (the unknown-house refusal); `--card` → 0 hits at BASE.
- Card grep after edits: no `:48`, `:49`, `` `:7` ``, `produced nothing` remain.
- Not run: `uv run pytest` (not on this seat's allow list).

HOUSE SEAT ORDER CARD AMENDED 2 · decisions: 4
