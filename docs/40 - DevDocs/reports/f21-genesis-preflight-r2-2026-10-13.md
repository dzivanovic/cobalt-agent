# f21-genesis preflight r2 · 2026-10-13

Read-only. HEAD `b592b412`. `git diff --stat HEAD -- <both cards> src tests configs ops/desk/gate-lists.md` shows only `configs/cobalt/rules.yaml`, so every cited path is read from a working tree equal to HEAD (this stands in for `git show HEAD:<file>`, which cannot be piped into grep one bare command at a time).

## CHECKS

| # | card | command | output | OK/FAIL |
|---|---|---|---|---|
| 1 | 468 · 469 | `git diff --stat HEAD -- <both cards>` | empty; both committed | OK |
| 2 | 468 | `git diff a6c6335c HEAD -- 468-f21-card.md` | three hunks only: G1 row (c) text and its `files` cell, and two new `## RECORDS` lines (BASE re-proof, amend read). G2-G6, header, BASE, NOT IN THIS JOB, READ, CHECK ASKS untouched | OK |
| 3 | 469 | `git diff a6c6335c HEAD --stat -- 469-f21-vectors-card.md` | empty: unchanged | OK |
| 4 | 468 · 469 | `git diff a6c6335c HEAD --stat -- src tests configs ops/desk/gate-lists.md` | empty: the amend touched no code | OK |
| 5 | 468 | round-1 FAIL: `grep -rlE "0024\|strike_alerts" tests --include="*.py"` | 20 files; 3 only apply 0024 (`test_strike_ack_db.py`, `test_strike_stream_db.py`, `test_strike_week.py`) and are not tail pins; 17 pin the tail | OK |
| 6 | 468 | `grep -rnE "FORWARD\[\|REVERSE\[\|0024_strike_alerts" tests` and `grep -rnE "len\(FORWARD\)\|FORWARD\[-?[0-9]*:"` | every tail pin sits in one of the 17; the only other hit is `test_migrate_proof.py:1510` `FORWARD[0]` (not a tail pin) | OK |
| 7 | 468 | the 17 compared with G1 (c) | the card names all 17 (7 original + 10 added), each with a line that matches HEAD (archiver 98,106,138,154,192-195,518-519; tenancy 517; radar_migration 35; voice_store 58-62; legs 29; seam_drc_s3 20-24,32-33; p4 103,124,141; f15 27-28; assumed 245-269; handicap 85; drc_store 66,146; k1 116,127; score_migration 104; stale 153; price_floor 45; d3 49,79-86; d2 164-183). The round-1 FAIL is closed. The card's count word "sixteen" is wrong (17 listed) | OK (ISSUES 1) |
| 8 | 468 | G1 `files` cell | now "every registry test file the (c) grep finds" plus the list | OK |
| 9 | 468 | `grep -nE "R1055" reports/cto-2026-10-11.md` | line 88 `HIS RULING · APPROVED` … "F5, F21, F20, F23 FINALs" | OK |
| 10 | 468 · 469 | headers | `CLASS: K2`, `LADDER: S5-P4 · F21`, `RULINGS: 2026-10-11 R1055` on both | OK |
| 11 | 468 | `grep -n "«FILL"` | line 7 `BASE` only | OK |
| 12 | 469 | `grep -n "«FILL"` | line 7 `BASE`; V2 X8 shape; V3 `model`, `timeout_s`, `dim`; V4 X6; V5 T4 rule, all waiting for the K2 probe report (D5) | OK (ISSUES 2) |
| 13 | 468 | `placement.py` anchors | `CREATED_TABLES` :64, `strike_alerts` :116, `raise KeyError` :187, message :188 | OK |
| 14 | 468 | `db_migrations/__init__.py` anchors | `FORWARD` :145, tail `0024_strike_alerts.sql` :168, `)` :169; docstring 0024 :101-104; `REVERSE` :172 | OK |
| 15 | 468 | `0024_strike_alerts.sql` shape | identity :17, `trader_id` GUC default :19, FK :20, `OWNER TO cobalt_user` :31, index :32 | OK |
| 16 | 468 | `aset/strike.py` and `cli.py` anchors | `class StrikeAlertStore` :145, `SIDE = Side.USER` :148; `strike_cli` import :84, mount :544 | OK |
| 17 | 468 | `gate-lists.md` PASS 1 :24, PASS 2 :30 | both end with `tests/cobalt/test_strike_ack_db.py`; the new id appends at the end | OK |
| 18 | 468 | reds: `ls src/cobalt/genesis` | no such directory, so G2-G5 are `ModuleNotFoundError`; G1 `KeyError` (:187) and no relation; G5 `invalid choice: 'genesis'` | OK |
| 19 | 469 | anchors: `config.py` kind :44, `Route` :40, loopback :60-73, fallback :94-103,:122-125; `models.py:68`; `adapters.py` `_classify` :55, `OpenAICompatibleAdapter` :68, `ADAPTERS` :123; `client.py` `_record` :38, `_apply_think_policy` :62, `call_sync` :81; `test_modelaccess_config.py:49-51`; `modelaccess.yaml` `local.plan` :18, `# source:` :31-37 | all match HEAD | OK |
| 20 | 469 | reds: V1 `:44` kind refusal; V1 fallback test already green on BASE (:94-103); V2 `embed_sync` absent in `client.py`; V3 registry is `["local.plan"]` (`:51`); V4 no `embedding` column; V5 no `embed` verb | each holds | OK |
| 21 | 468 · 469 | next free migration number: `ls src/cobalt/db_migrations`; `grep -rlE "00(2[5-9]\|3[0-9])_[a-z]"` over prompts 2026-10-13 and `docs/30 - Design` | tail `0024`; `0025` claimed by `448-dml-roles-card.md` and `F5-FINAL-2026-10-11.md`. The cards say "next free at BASE" and the new RECORDS line says 0026 | OK |
| 22 | 468 · 469 | per-user data of his (L32) | none in either card; fixtures synthetic, G6 writes his figures `[user data]` | OK |
| 23 | 468 · 469 | a new command on a seat's `--allowedTools` | none; the host probes are a separate K2 prompt (D5) | OK |
| 24 | 468 | RESTARTS `com.cobalt.radar` | `jobs.yaml:203` `imports: [cobalt.cli]`; `cli.py` gains the genesis import | OK |
| 25 | 469 | RESTARTS `com.cobalt.aset com.cobalt.radar` | `jobs.yaml:86` lists `configs/cobalt/modelaccess.yaml` in aset's reads; radar by `cobalt.cli` → voice → `cobalt.modelaccess` | OK |
| 26 | 468 · 469 | FOR THE CHECK lines | the drafter names none; 469 READ points at 468's future build report | OK (n/a) |
| 27 | 468 · 469 | blockers: `grep -nE "448\|304" reports/cto-2026-10-13.md` | see ISSUES 3 | OK (named) |

## ISSUES

1. NOTE (468 G1 (c) and `## RECORDS`): the card says "sixteen files" and the amend report says "seven plus nine", but 17 are named (7 plus 10: f15, assumed, handicap, drc_store, k1, score_migration, stale, price_floor, d3, d2). The list is complete and the rule says to re-grep, so a builder is not misled; fix the word to "seventeen" at the next touch.
2. NOTE (469): `BASE` and the six `«FILL»` cells wait for 468's merge and the K2 host-probe report (X2 X8 X3 X9 X6, D5). `desk-launch.sh` refuses 469 until they are filled.
3. NOTE (blocks): 468 BASE waits for card 448's merge (migration 0026); 448 BASE waits for card 304's merge. 304 is BUILT at row CR2 (`c748da49`, R1361) and its deploy card 491 is committed (`3aa481c0`) but refused for two FILL markers; drafter `draft-491-fill` is running (R1366). Then 304 deploys, 448 builds, checks and deploys outside market hours, then 468. 469 waits for 468 and the probe report. One deploy at a time. 468 is not blocked by 469.
4. NOTE (anchors move): after 448 merges the registry pins say `0025_dml_roles` and every one goes to 0026; the card's RECORDS now says the desk re-proves the anchors at BASE.
5. NOTE (merge clash, unchanged from round 1): F5's FINAL also claims `0025` and edits `modelaccess.yaml`; 469 V3 edits the same file. The later lander takes the next number; F5's drafter owns it.

PREFLIGHT DONE · cards: f21-genesis-1013 chunk 1 and 2 · checks: 27 · fails: 0 · ready: YES
