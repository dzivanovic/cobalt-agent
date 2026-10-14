## §0 Headline
Card `prompts/2026-10-14/537-deploy-smoke-string-card.md` written: K5, three rows (S3 pin, S1 `DEPLOY-HUB.md:11`, S2 `STANDING-LIST.md` §3) and a run row R4.
Source of truth is `DEPLOY-HUB.md:11`; `desk-launch.sh:2174-2189` only copies the line and fills tokens, so it changes not at all.
Finding: `cobalt smoke` is not write-nothing; without `--json` it writes `reports/<suite>-smoke-<date>.md` (ASK DESK 1).
Nothing run: no test, no `uv run` on this seat; every read is HEAD `8b813ca7`'s.

## DECISIONS
1. ASK DESK: the brain's words call the smoke "read-only", but `src/cobalt/smoke/cli.py:71-80` writes one report file in the main tree unless `--json`. The string `smoke *` admits both. Default: the brain's string byte for byte, the card's S1 and S2 cells say the one file truthfully, and the deploy proof's smoke read uses `--json`. The narrower `… smoke * --json*` changes the brain's string and is not drafted. [07:35 ET]
2. ASK DESK: `STANDING-LIST.md:109` counts `56 allow … (53 without a migration)`. Default: row S2 moves them to `57` and `54`; no test pins the counts. Strike the heading edit from S2 if the desk wants the new row only. [07:35 ET]
3. ASK DESK: `BASE` and `TIP` are left empty; the card's S1 negative control needs `BASE` as an 8-hex literal. Default: the desk fills `BASE` before the launch. [07:35 ET]

## RECORDS
- 2026-10-14 07:29 ET (`date`), `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `8b813ca7`; `git status --short` over `ops`, `tests`, `DEPLOY-HUB.md`, `BUILD-HUB.md` printed nothing.
- `DEPLOY-HUB.md`: the one `^claude --bg ` line is `:11` (`grep -c` → 1); production strings on it read by `grep -n -o`; `grep -c "cobalt smoke"` → 0.
- `STANDING-LIST.md` §3 rows `:137-141` and heading `:109` read whole; `grep "cobalt smoke" ops` → no match.
- `tests/ops/test_hub_lines.py:54-70, 97-141` read whole (`PROD_ALLOW_TODAY`, the W7 test); `desk-launch.sh:2174-2189`, `:1725-1770`, `:135-138` read; `src/cobalt/smoke/cli.py:1-91` read.
- `reports/deploy-plist-step-c-1013.md:5-6, 174, 199, 212`: the refusal of `cobalt smoke s2`.
- Not proved: the card's red-first test results and the `git show <BASE>` shape of the NEW test file (no `uv run`, no test run).

DRAFTED · decisions: 3
