# Devfix report: cobalt db dev-rebuild user.aset_sizings — 2026-10-07

JOB: devfix-aset-sizings-1007 · BRANCH: ops/devfix-aset-sizings-1007 · WORKTREE: devfix-aset-sizings-1007 · BASE: 73cbf7a1 · TABLE: user.aset_sizings
CARD: `docs/40 - DevDocs/prompts/2026-10-07/99-devfix-aset-sizings-card.md`

## §0 Headline
- `user.aset_sizings` rebuilt on `cobalt_dev`: max_attnum 1538 → 54, rows 1 = 1, catalog digest equal.
- FP F1 = F0 (cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87); level 0013 (`TABLES 0011`, the gate's LEVEL 0013 row) before and after.
- S7 slot line: `SLOTS ok · highest user.card_stop_edits 369 of 1600`.
- Proof test PASSED; lock released; `.env` removed, proven gone.

## STEPS

### AUTHORIZATION — 13:47:54 ET
- `grep -n -E "«INSTAL[L]" ".../prompts/DEVFIX-HUB.md"` · exit 1 · no output
- `grep -n -E "«FIL[L]" ".../prompts/2026-10-07/99-devfix-aset-sizings-card.md"` · exit 1 · no output
- `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<card>"` · exit 0 · `58db5b54e4a0bdc8ccb1b81394bc55cccd44de62`
- `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` · exit 0 · no output
- `grep -n "^| R644 " cto-2026-10-07.md` · exit 0 · `38:| R644 | 13:47 ET | HIS RULING (words: ...R644, "approved"): install DEVFIX-HUB.md. ... | HIS RULING · APPROVED |` · `log -S"| R644 |"` → `71629bcb25617a0e9ae8ffd9fbe1011b0e976295`
- `grep -n "^| R625 " cto-2026-10-07.md` · exit 0 · `19:| R625 | 10:15 ET | HIS RULING (...): a radar card's header row and title are green for long, red for short; ... | HIS RULING · APPROVED |` · `log -S"| R625 |"` → `33a49ab6048bcc5ae6f489310beb5e99978eadfd`
- `grep -n "^| R26 " cto-2026-10-02.md` · exit 0 · `33:| R26 | 06:43 ET | HIS RULING: card 12's devfix line approved — ... | HIS RULING · APPROVED |` · `log -S"| R26 |"` → `d352171a04acf270d5c3c6159a69984c4b665ea3`
- `grep -n "^| R39 " cto-2026-10-02.md` · exit 0 · `46:| R39 | 07:57 ET | HIS RULING (direction row 2): permission by class — ... | HIS RULING · APPROVED |` · `log -S"| R39 |"` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`

### PREFLIGHT — 13:47:54 ET
- `date` · `Wed Oct  7 13:47:54 EDT 2026`
- `git status --short --branch` · exit 0 · `## ops/devfix-aset-sizings-1007`
- `git log --oneline -1` · exit 0 · `73cbf7a1 docs(desk): devfix drafter round 2 prompt 100, R640`
- `ls -la /Users/cobalt/cobalt-wt/*/.env` · exit 1 · `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`
- `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` · exit 1 · `ls: /Users/cobalt/cobalt-wt/.cobalt_dev.lock: No such file or directory`

FP (typed exactly):
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

### S1 THE LOCK — 13:48:29 ET
- `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh devfix-aset-sizings-1007 90` (background) · exit 0 · `lock taken: devfix-aset-sizings-1007`
- `ls -la /Users/cobalt/cobalt-wt/*/.env` · exit 0 · one line: `-rw-------  1 cobalt  staff  2186 Oct  7 13:48 /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007/.env`

### S2 F0 and level — 13:48:29 ET (each `COBALT_ENV=dev` call preceded by `ls -la /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007/.env` → the line above)
- `<FP>` · exit 0 · (uv venv creation lines, then)
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
- F0 = cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` · exit 0 · whole:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.64
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   323          cfe5bbb70cd4ef1d1271875a5c124089   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
drc_events           user    -        -            -                                  0.00
drc_fills            user    -        -            -                                  0.00
drc_imports          user    -        -            -                                  0.00
drc_rows             user    -        -            -                                  0.00
drc_stated_books     user    -        -            -                                  0.00
legs                 user    -        -            -                                  0.00
missed               user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
movers_daily         system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
picks                user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
prediction_records   user    -        -            -                                  0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.01
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
36 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 29 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.7 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
SLOTS WARN user.aset_sizings max_attnum 1538 of 1600 · dropped 1484 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)
code: 73cbf7a1 (clean) · /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007
FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87
TABLES 0011
```
- Level: no table of a migration above 0013 present (0016+ tables `drc_*`, `voice_turns`, `legs`, `prediction_records` absent); no `CHANGED`. `TABLES 0011` + FINGERPRINT equal `ops/desk/gate-lists.md:47-48` `## LEVEL 0013`: `TABLES 0011 · FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.

### S3 DRY RUN — 13:48:58 ET
- `COBALT_ENV=dev uv run cobalt db dev-rebuild user.aset_sizings --dry-run` · exit 0 · whole:
```
cobalt db dev-rebuild — user.aset_sizings on cobalt_dev (DRY RUN)
BEFORE max_attnum 1538 · dropped 1484 · live 54 · rows 1 · row digest 120caf7ae5902721259337f89978f50b · catalog digest 6a8f99dd5431708ecc645c5ebfeacf6b
AFTER  max_attnum 54 · dropped 0 · live 54 · rows 1 · row digest 120caf7ae5902721259337f89978f50b · catalog digest 6a8f99dd5431708ecc645c5ebfeacf6b
DRY RUN — ROLLED BACK · max_attnum 1538 → 54 · rows 1 = 1 · catalog digest equal
```
- AFTER max_attnum 54 = live 54; dropped 0; live, rows, row digest, catalog digest equal.

### S4 THE REBUILD — 13:49:01 ET
- `COBALT_ENV=dev uv run cobalt db dev-rebuild user.aset_sizings` · exit 0 · whole:
```
cobalt db dev-rebuild — user.aset_sizings on cobalt_dev (COMMIT IF EQUAL)
BEFORE max_attnum 1538 · dropped 1484 · live 54 · rows 1 · row digest 120caf7ae5902721259337f89978f50b · catalog digest 6a8f99dd5431708ecc645c5ebfeacf6b
AFTER  max_attnum 54 · dropped 0 · live 54 · rows 1 · row digest 120caf7ae5902721259337f89978f50b · catalog digest 6a8f99dd5431708ecc645c5ebfeacf6b
REBUILT user.aset_sizings · max_attnum 1538 → 54 · rows 1 = 1 · catalog digest equal
```

### S5 F1 — 13:49:01 ET
- `<FP>` · exit 0 ·
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
- F1 = F0: cols 664 = 664 · rels 35 = 35 · views_md5 272c95bbb12241e3611e4b36326ccf87 = 272c95bbb12241e3611e4b36326ccf87

### S6 PROOF — 13:49:09 ET
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py::test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings` · exit 0 ·
```
PASSED tests/cobalt/test_dev_rebuild_db.py::test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings
1 passed in 0.07s
```
- 0 failed, 0 errors, 1 PASSED.

### S7 level after — 13:49:09 ET
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` · exit 0 · table block identical to S2 (every rows and digest column equal; `bars` secs 5.50, `aset_sizings` secs 0.00; `Proof cost: total 5.6 s`); closing lines:
```
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
SLOTS ok · highest user.card_stop_edits 369 of 1600
code: 73cbf7a1 (clean) · /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007
FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87
TABLES 0011
```
- Level 0013, no `CHANGED`.

### S8 THE LOCK (d) — 13:49:20 ET
- `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh devfix-aset-sizings-1007` · exit 0 · `lock released`
- `ls /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007/.env` · exit 1 · `ls: /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007/.env: No such file or directory`
- `ls -la /Users/cobalt/cobalt-wt/*/.env` · exit 1 · `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`
- `.env: removed, proven gone (S8)`

## DECISIONS
none

## RECORDS
- Card `## RECORDS` as re-read: `user.aset_sizings` 1538 of 1600 at the `cobalt_dev` slot guard (`reports/deploy-radar-direction-color-1007.md:5`, `:86`, `:124`) · 1534 before the forward migrate of 0014–0022; the migrate took `max_attnum` 1534 → 1538 (`:93-95`) · the proof test asserts `slot_report` equals the slot read; the rebuild's `REBUILT … max_attnum <b> → <a>` line proves the drop.
- S2 SLOTS line confirms the card: `max_attnum 1538 of 1600 · dropped 1484 · live 54`.

REBUILT · user.aset_sizings max_attnum 1538 → 54 · rows 1 = 1 · FP F1 = F0 · proof test: PASSED · cobalt_dev: 0013 · .env: removed · decisions: 0 · for Dejan: 0
