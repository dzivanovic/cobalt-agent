# f21-genesis preflight · 2026-10-13 (08:18 ET)

Read-only. HEAD `240ac340`. `git diff --stat HEAD -- src tests configs ops/desk/gate-lists.md` shows only `configs/cobalt/rules.yaml`, so every `file:line` below was read from a working tree equal to HEAD on the cited paths.

## CHECKS

| # | card | command | output | OK/FAIL |
|---|---|---|---|---|
| 1 | 468 · 469 | `git diff --stat HEAD -- <both cards>` · `git log --oneline -- <both cards>` | empty diff; both committed in `81ee1c3e` | OK |
| 2 | 468 | `grep -nE "«FILL" 468-f21-card.md` | line 7 `BASE` only (the desk fills it after card 448 merges) | OK |
| 3 | 469 | `grep -nE "«FILL" 469-f21-vectors-card.md` | line 7 `BASE`; V2 X8 not-loaded shape; V3 `model`, `timeout_s`, `dim`; V4 X6 extension step; V5 T4 rule. All but `BASE` are the probe rows the drafter report D5 says wait for X2 X8 X3 X9 X6 | OK (named in ISSUES 2) |
| 4 | 468 · 469 | header `CLASS` / `LADDER` / `RULINGS` | `CLASS: K2`, `LADDER: S5-P4 · F21`, `RULINGS: 2026-10-11 R1055` on both | OK |
| 5 | 468 · 469 | `grep -nE "R1055" reports/cto-2026-10-11.md` | line 88: `\| R1055 \| 09:04 ET \| HIS RULING · APPROVED: … approves all that waits for him: F5, F21, F20, F23 FINALs …` | OK |
| 6 | 468 | anchors in `placement.py` (`CREATED_TABLES` :64, `strike_alerts` :116, `raise KeyError` :187, message :188) | match HEAD | OK |
| 7 | 468 | anchors in `db_migrations/__init__.py` (`FORWARD` :145 ends :168 `0024_strike_alerts.sql`, `)` :169; docstring 0024 lines :101-104; `REVERSE` :172) | match HEAD | OK |
| 8 | 468 | `0024_strike_alerts.sql:16-32` shape (id identity, `user_id` GUC default + FK, `OWNER TO cobalt_user`, index) | matches HEAD | OK |
| 9 | 468 | `aset/strike.py:145-154` (`class StrikeAlertStore` :145, `SIDE = Side.USER` :148); `cli.py:84` `strike_cli` import, mount `strike_cli.add_parser(sub)` :544 | match HEAD | OK |
| 10 | 468 | `gate-lists.md` PASS 1 :23-24, PASS 2 :29-30 | match; both end with `…test_strike_ack_db.py`, so the new `--deselect` and id append at the end | OK |
| 11 | 468 | the seven registry files of G1 (c): `grep -nE "0024\|strike_alerts"` on each | every cited line matches HEAD (`archiver_migrations` 98,106,138,154,192-195,518-519; `tenancy` 517; `radar_migration` 35; `voice_store` 58-62; `legs_migration` 29; `seam_drc_s3_registry` 20-24,32-33; `p4_migrations` 103,124,141) | OK |
| 12 | 468 · 469 | G1 (c) says "every migration-registry test that pins the tail"; `grep -nE "0024\|strike_alerts"` on the rest of `tests/` | NINE more files pin the tail and are not in the list: `test_f15_p1_records_offline.py:27-28`, `test_assumed_store.py:245-269`, `test_radar_handicap_store.py:85`, `test_drc_store.py:66,146`, `test_drc_k1_store.py:116,127`, `test_radar_score_migration.py:104`, `test_stale_score_db.py:153`, `test_radar_price_floor_db.py:45`, `test_drc_d3_experiments.py:49,79-86`, `test_drc_d2_fix_r1_db.py:164-183` (card 448 M1 lists all of them). They are outside G1's `files` column | FAIL |
| 13 | 468 | row reds, each for a named reason on BASE: G1 `KeyError` (`placement.py:187`) and missing relation; G2 / G3 / G4 `ModuleNotFoundError: cobalt.genesis`; G5 argparse `invalid choice: 'genesis'` (no `genesis` mount in `cli.py`); G6 RUN asserts nothing | each reason holds (no `src/cobalt/genesis/` exists); test ids are new files, spelled the same in every cell | OK |
| 14 | 469 | anchors: `config.py` `Route` :40-56, kind :44, loopback :58-76, fallback :94-103, :122-127; `models.py:68`; `adapters.py` :55, :68-121, :123; `client.py` `_record` :38, `_apply_think_policy` :62, `call_sync` :81; `test_modelaccess_config.py:49-51`; `modelaccess.yaml:17-42`, `# source:` :31-39 | all match HEAD | OK |
| 15 | 469 | reds: V1 first test `ModelAccessConfigError` (kind not `openai_compatible`, :44); V1 fallback test green on BASE (a fallback key already refuses, :94-103); V2 `ImportError: embed_sync`; V3 `["local.plan"]`; V4 no `embedding` column; V5 `invalid choice: 'embed'` (holds once 468 has merged) | each reason holds; V1's "chat key" test shares the :44 reason | OK |
| 16 | 468 · 469 | next free migration number: `ls src/cobalt/db_migrations` · `grep -rlE "00(2[5-9]\|3[0-9])_[a-z]"` over `prompts/` and `docs/30 - Design` | tail `0024`; `0025` claimed by card 448 (`0025_dml_roles`) and F5 FINAL (`F5-FINAL-2026-10-11.md:67`). Cards say "next free at BASE" and never name 0025 for genesis. 448 drops its F5 clash to F5's drafter (448 RECORDS, `## DECISIONS` 3) | OK |
| 17 | 468 · 469 | `configs/` paths added | none new. 469 edits the existing `configs/cobalt/modelaccess.yaml`; its class is `resident reads` of `com.cobalt.aset` (`jobs.yaml:86`) | OK |
| 18 | 468 · 469 | per-user data of his (L32) in either card | none: fixtures are synthetic; the figure is "synthetic, never his"; G6 writes his figures `[user data]`; the ledger is only named by path (tracked, 4216 lines, holds "stop buffer") | OK |
| 19 | 468 · 469 | new command on a seat's `--allowedTools` line (R411, R412) | none: G6 and the with-DB rows run through the gate and pytest; `cobalt genesis import/search/embed` run only inside tests and never on a production seat. The host probes (X2 X8 X3 X9 X6) are NOT in the cards; D5 makes them one separate K2 prompt | OK |
| 20 | 468 | RESTARTS home of every changed path in `## RECORDS` | `cli.py` mount → `com.cobalt.radar` (`jobs.yaml:203` `imports: [cobalt.cli]`); `.sql` → non-Python src asset; `tests/` → no resident; `gate-lists.md` → operator script; `docs/` → DOCS. `db_migrations/__init__.py` and `placement.py` are reached from `cobalt.cli` (`cli.py:66`) and `devdb.py:49`; nothing else I grepped imports them from aset's entrypoints. The card leaves aset to the build's `## RESTARTS` | OK |
| 21 | 469 | RESTARTS: `modelaccess.yaml` in aset `reads:` (`jobs.yaml:86`) → aset; `cobalt.cli` → `voice.cli` → `voice.turn` → `voice.agent` → `cobalt.modelaccess` → radar | header `RESTARTS: com.cobalt.aset com.cobalt.radar` matches `## RECORDS` | OK |
| 22 | 468 · 469 | FOR THE CHECK lines | the drafter report names none (`grep "FOR THE CHECK"` finds only 469's READ pointer to 468's future build report) | OK (n/a) |
| 23 | 468 · 469 | blockers | see ISSUES 3 | OK (named) |

## ISSUES

1. FAIL (468 G1 (c), and 469 V4, which says "card 468 G1 (c) list"): the list of tail-pinning tests is seven files but nine more pin `FORWARD[-1]` / `REVERSE[0]` or the newest-N lists (check 12). A builder who follows the card moves seven and leaves the rest red. Fix: add the nine to G1 (c) and to `files`, or write "re-run `grep -rn "0024" tests` and move every pin, as card 448 M1 does".
2. NOTE (469): `BASE` and six `«FILL»` cells wait for the host probes (X2 X8 X3 X9 X6, drafter D5) and for card 468's merge. Not a FAIL. `desk-launch.sh` will refuse 469 until they are filled.
3. NOTE (blocks): 468 BASE waits for card 448's merge (448 BASE waits for card 304's merge; 304 is at fix round row CR, R1357). 469 waits for 468's merge and the probe report. One deploy at a time; 448 deploys outside market hours after 304. 468 is not blocked by 469.
4. NOTE (anchors move): every `file:line` for the registry tests is read at HEAD. After card 448 merges, the pins say `0025_dml_roles` and 448 has moved them one place out, so G1 (c)'s line numbers shift and each pin goes to 0026. The desk re-proves these anchors at BASE (the same step 462 got after 446/304). The card does not say so; add one line.
5. NOTE (merge clash): F5's FINAL also claims `0025` and edits `configs/cobalt/modelaccess.yaml` (the route values, `F5-FINAL:235`); 469 V3 edits that file too. Whichever of F5 and 469 lands second takes the next number and rebases the yaml. F5's drafter owns the number (448 `## DECISIONS` 3); nothing here moves.
6. NOTE (469 V1): `test_an_embed_route_with_a_fallback_key_refuses` is new and green on BASE (the file's fallback refusal already fires), so it proves no change. The card says so ("stays green"); no fix.

PREFLIGHT DONE · cards: f21-genesis-1013 chunk 1 and 2 · checks: 23 · fails: 1 · ready: NO
