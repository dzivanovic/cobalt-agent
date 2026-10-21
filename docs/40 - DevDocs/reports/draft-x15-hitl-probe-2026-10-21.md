# Drafter `draft-x15-hitl-probe` — card 977 `x15-hitl-probe` (prompt 976)

## §0 Headline
- Card written: `prompts/2026-10-21/977-x15-hitl-probe-card.md`, rows S1 (shared key script), P1 (`/hitl/x15-probe`, no store, registered before `/hitl/{row_id}`), P2 (readout above Approve), P3 (`cobalt hitl x15-send`, dev only), R1, D0.
- RESTARTS widened to `com.cobalt.aset com.cobalt.radar`: `hitl/cli.py` is in radar's import reach.
- Gate seat admitted string: `"Bash(COBALT_ENV=dev uv run cobalt hitl x15-send)"`.
- Four ASK DESK: node for the readout test, `deploy-smoke.sh` maps no https, one Mattermost bot, the seat's `COBALT_MASTER_KEY`.

## DECISIONS
1. RESTARTS `com.cobalt.aset com.cobalt.radar`, not aset alone: P3 edits `src/cobalt/hitl/cli.py`, imported by `src/cobalt/cli.py:88`, which `com.cobalt.radar` imports (`jobs.yaml:203`). Row R1's tool line is the record.
2. ASK DESK — the readout test runs the script under `node` (`/opt/homebrew/bin/node` present; no test on main runs JavaScript). Default: `pytest.fail` when `node` is absent, never a skip. Alternative: pin the script by content only (weaker: it pins text, not the seen/missing rule).
3. ASK DESK — the prompt says the smoke read is an https form `deploy-smoke.sh` maps; it maps `http://127.0.0.1:5010/*` only (`ops/desk/deploy-smoke.sh:135-136`). Default: the line uses the form `DEPLOY-HUB.md:11` admits (`https://cobalt.taild24291.ts.net/hitl/x15-probe`), as card 965 did (its DECISION 2).
4. ASK DESK — "the dev bot": new core has ONE bot, `MATTERMOST_CREDS` (`configs/cobalt/notify.yaml`; `configs/dev` holds no notify file). Default: `x15-send` uses `send_dm` as it is, so the DM comes from that bot. `send_dm` unlocks the credential from `COBALT_MASTER_KEY` in the process env (`mattermost.py` `_creds`); whether the gate seat's shell carries it is unknown — without it the line reads `X15 NOT SENT`.
5. Dev only = refused unless `COBALT_ENV=dev` (unset refused too, `env.resolve_env` raises on unset); stricter than "refuses production". Hence the `COBALT_ENV=dev` prefix in the admitted string.
6. The readout's server default is `k: missing`; the script turns it to `k: seen`. A page whose script did not run reads the same as a stripped fragment: do not trust the link.
7. `F20-FINAL-2026-10-11.md:42` in the prompt is `:43` on main (B); the card cites `:43`.
8. `CHECK REPORT` and `HOUSE B` are filled at the build, as the prompt gives them (CARD.md leaves them empty at a build launch).
9. BASE `41804777` = main HEAD at the drafter's read; the desk resets it at launch.

## RECORDS
- 2026-10-21 12:16 EDT (`date`): prompt 976 read; `CARD.md`, cards 877 and 965 read.
- 12:16–12:19: `git show main:` of `F20-FINAL-2026-10-11.md`, `src/cobalt/aset/web.py` (`:1383-1544`), `hitl/card.py`, `hitl/cli.py`, `notify/mattermost.py`, `env.py`, `redact/guard.py`, `configs/cobalt/notify.yaml`, `tests/cobalt/test_hitl_web.py`, `tests/cobalt/test_hitl_offline.py`; `git grep` on main for `page_base_url`, `cobalt cos probe`, `jobs.yaml` labels and imports, `deploy-smoke.sh` curl shapes, `DEPLOY-HUB.md` curl entry, `BUILD-HUB.md` allow entries, R2285 and R1863, the `808` card's X15, `RESTARTS:` header shapes; `tunables.yaml:1030-1050`; `ls /opt/homebrew/bin/node` → listed; `ls /Users/cobalt/cobalt-wt/` → no `x15-hitl-probe`; `git rev-parse --short=8 main` → `41804777`; `git diff --stat main` over the inputs → nothing.
- 12:20: card 977 written. Nothing committed, nothing run beyond reads.

DRAFTED · decisions: 9
