# draft-x15-hitl-probe-amend — card 977, three preflight FAILs closed (2026-10-21)

## §0 Headline
- Card `prompts/2026-10-21/977-x15-hitl-probe-card.md` amended in place: 3 lines changed (`git diff --stat`: 3 insertions, 3 deletions). Nothing committed.
- #2: `:3` reads `CLASS: K2 serving K4`.
- #19: P2 test pins the element `class="hitl-k-state"` once, index below `>Approve<`; S1 script unchanged.
- #21: P3 gains `::test_x15_line_survives_redact` (F20 X20): real `redact()` over the exact line is clean and returns it unchanged.
- Card grew to 16539 bytes (`wc -c`): growth is the X20 test text and the pin note.

## DECISIONS
- D1 (#19) Pin the element, not a new selector. The script keeps `.hitl-k-state`, so S1's node test and P1's "body holds `hitl-k-state`" stay as written. Non-pending page: holds no `hitl-k-state` and no `>Approve<` (forms, script included, are pending-only, `web.py:1465-1480`).
- D2 (#21) The X20 test runs the line `_x15_send` actually builds (send_dm recorder) with the REAL `card.page_base_url()` (tunables `:1038-1039`, not patched), plus the same line with the constructed key `"0123456789abcdef" * 2`. `record=False` (no counter DB row).
- D3 (#21) Literal half off in the test (`LiteralGuard({}, available=False, reason="test")`, the `test_redact.py:113-128` `no_literals` shape): the test never reads a vault value. Residual, UNPROVEN: a vault literal ≥8 chars inside the base URL would redact it in production; this row does not prove that case. A literal matching a fresh 32-hex key is not a practical risk.
- D4 X4 in `## CHECK ASKS` left unchanged (prompt: change nothing else); the X20 assertion is pinned by the P3 test row the checker already reads.

## RECORDS
- Seat `draft-x15-amend` (prompt 981), 2026-10-21 12:24–12:26 EDT (`date`). Reads and the card Edit only; no git write, nothing run.
- Preflight `reports/x15-hitl-probe-preflight-2026-10-21.md` `## ISSUES`: FAIL 2, 19, 21 read.
- Prompt 976 (`git show main:`): `:6` asks "CLASS K2 serving K4".
- `web.py` (`git show main:`): `hitl_detail` `:1451-1490`; `forms = ""` `:1465`, pending branch `:1466`, Approve button `:1471`, script `:1476-1479` (`.hitl-k` only today).
- `mattermost.py` (`git show main:`): `from cobalt.redact import redact` `:33`; rule `:13-17`; `send_dm` `:130`; `safe = redact(message, channel=CHANNEL)` `:140`; `safe.clean` `:141`; `safe.text` posted `:161`.
- `redact/guard.py` (`git show main:`): `RedactResult` `:56` (`text` `:59`, `clean` `:63` = no hits); `redact(text, *, channel, cfg, record)` `:80`; literals loaded via `load_literals` (min length from config); `_record` only on a hit and `record=True`.
- `redact/secrets.py:98`: `LiteralGuard.__init__(values, *, available, reason="")`.
- `configs/cobalt/redact.yaml` (`git grep` main): `literal_min_length: 8` `:45`; 17 pattern rows `:53-176`, `url_query_secret` `:125`, no bare-hex row.
- `tests/cobalt/test_redact.py` (`git show main:`): `no_literals` fixture `:113-128` (`LiteralGuard({}, available=False, reason="test")` `:126`); `TestCleanText` asserts a clean message comes back byte-identical.
- `hitl/card.py` (`git show main:`): `page_base_url` `:31` (https only, strips `/`).
- F20 FINAL (`git grep` main): B `:43`; X20 `:82` "`redact()` on a sample card line carrying `#k=<hex>` … redacted → the link is broken in the DM; B's carrier changes".
- `git diff --word-diff` of the card: `:3` `+serving K4`; P2 test cell rewritten; P3 test cell gains `::test_x15_line_survives_redact`. An X4 edit was made, then reverted; the stat confirms 3 lines.

DRAFTED · decisions: 4
