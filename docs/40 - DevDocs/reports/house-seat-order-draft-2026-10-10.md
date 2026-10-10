# House seat order card — draft, 2026-10-10

## §0 Headline
- Card written: `prompts/2026-10-10/298-house-seat-order-card.md`, three rows (S1 SEAT ORDER lines 23-27, S2 probe step line 65 and Sol label line 90, S3 `house-probe.sh` plus tests).
- Script takes a new flag `--card <path>`: Grok and Gemini always; Sol only when the card header carries `HOUSE A: OpenAI — his <date> R<n>`; a named `sol` without that line is REFUSED.
- 3 decisions for the desk; the header `BASE` is the one `«FILL` left (the desk's). Nothing built, no git write, no launch.

## DECISIONS
1. ASK DESK: the OpenAI header line is not proved by `authorize.sh` or `desk-launch.sh` (they read only an `overruled` HOUSE line, `authorize.sh:195-206`, `desk-launch.sh:871-880`). Default taken: the hub proves it by hand (S2: `grep -n "^| R<n> "` plus `git log -S`), the two scripts stay out of the card. A later card can teach them. [18:37 EDT]
2. ASK DESK: house B "none (not needed)" when the card is not `mandatory` and Grok is up; the stop line keeps the literal `none available` so no parser changes. Lines 3, 16, 21, 87, 99-100 still say "two houses / both houses" and are NOT touched (brain named only the order, OpenAI lines and the probe). Default taken: leave them; the existing `none available` paths (`:100`, `:117`) already carry an absent house B. A follow-up card would reword them.
3. ASK DESK: the flag `--card <path>` is a new argument of an existing `ops/desk/` script, not a new command (R411, R412); `order-open.sh` calls the probe with no argument and so now probes Grok and Gemini only (R920's wanted effect). Default taken: proceed. If a new flag counts as a new command, the build stops with `decisions: 1`.

## RECORDS
- `date` → `Sat Oct 10 18:37:37 EDT 2026`; the card was written against `HEAD` `8ba5a819`.
- `git -C /Users/cobalt/cobalt diff HEAD --stat -- "docs/40 - DevDocs/prompts/CHECK-HUB.md" ops/desk/house-probe.sh tests/ops/test_house_probe.py` → nothing (working files = `HEAD`). `wc -l`: CHECK-HUB 123, house-probe.sh 109, test_house_probe.py 156.
- `grep -n -i OpenAI` over CHECK-HUB at HEAD → lines 23, 24 (twice), 25, 26, 90. `(all three` → line 65. `house-probe.sh --card` and `HOUSE A: OpenAI` → none.
- `grep -n "^| R920 \|^| R921 "` over `reports/cto-2026-10-10.md` → `48: R921`, `49: R920`, both `HIS RULING · APPROVED (via brain, L79)`; R963 is `:7` (a DESK RECORD).
- `grep -rl house-probe tests/` → `test_order_open.py` (stub), `test_house_probe.py`, `test_bare_guard.py` (comment `:1577`). Callers: `order-open.sh:133-134`, `preflight.sh:26-27` (comment).
- `grep -n -E "ops/desk|tests/ops" configs/cobalt/jobs.yaml` → no match: RESTARTS none expected; `uv run cobalt jobs restarts` UNPROVEN (no `uv` on the drafter's allow list).
- Precedent shape: `prompts/2026-10-10/284-kill-hub-card.md` (TEXT blocks, `DB: none`). G5 route: `ops/desk/bare-guard.py:71`, `:1122`.
- Header: `RULINGS: 2026-10-10 R920 R921` is read by `authorize.sh:125-146` as one date and two rows.

HOUSE SEAT ORDER CARD DRAFTED · decisions: 3
