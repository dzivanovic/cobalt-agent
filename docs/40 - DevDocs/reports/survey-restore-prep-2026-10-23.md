# SURVEY — restore prep for `radar.cards_enabled` and `radar.benchmark` (2026-10-23)

Seat `survey-restore-prep`, read-only. Direction: DESK RECORD 2026-10-23 R2389 (brain 9b07db5a, L79); production reads standing R686 / L62. Start 08:30:12 ET, end 08:31:58 ET (`date`).

## §0 Headline
- `radar.cards_enabled` ← card file `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml`, recorded sha256 `5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17` (P1 `card.curves` source; `cards-htf-apply-2026-09-20.md:225-243`), value `true` (file:2). That was the last card load (2026-09-20 21:04:57 ET).
- `radar.benchmark` ← optional file `data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml`, recorded sha256 `10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880` (`radar-benchmark-load-2026-09-22.md:73-79`), value `{top_n: 20, min_move_pct: 10}` (file:2).
- Tree vs. recorded digest: not re-hashed, because no hashing command is allowed. Both files have an mtime from before their load (htf Sep 20 18:44, before the 21:05 apply; benchmark Sep 22 06:20, before the 07:04 apply). Their bytes read the same as the load reports' `file:` lines. The K3 `--sha256` re-proves the hash.
- Side effects: the htf card load writes only `radar.cards_enabled`. `card.proposed_key`, `card.curves` and `card.shadow_promotion_bar` stay `=` if production still holds the reviewed values: their sources and times have not changed since those loads (P1). `card.alignment_default` is absent from both the file and production, so nothing is deleted. The optional file touches only `radar.benchmark`.
- No hit on stored values: P1/P2 read no value. Tombstone shape: `survey-settings-writer-2026-10-23.md:6`.

## Q1/Q2 — files

| key | loaded path (ignored, `.gitignore:6`) | committed copy (`main`) | recorded digest | tree digest | match |
|---|---|---|---|---|---|
| `radar.cards_enabled` (and `card.*`) | `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml` | NONE on `main`. The packet copy `prompts/2026-09-20/16-packet/p2-live-settings-htf.yaml` exists on disk but not in `main` (`git show` exit 128; `git log` on the dir: empty) | `5993c57f…fbfc17` (P1 source of `card.curves`, 2026-09-20 21:04:57 ET; apply report `:225-243`) | not hashed (R2392) | the tree file and the uncommitted packet copy are line-for-line identical (Read, 9 lines). Same as the report's `file:` curves |
| (earlier card set) | `data/backups/cards-live-2026-09-19/p2-live-settings.yaml` | `prompts/2026-09-19/23-packet/p2-live-settings.yaml` | `f3663399…c65f0` (P1 source of `card.proposed_key`, `card.shadow_promotion_bar`, 2026-09-19 12:30:05 ET; `cards-golive-2026-09-19.md:4,116,122`) | not hashed | same as htf minus `htf_level_proximity` |
| (dark set, superseded) | `data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml` | `prompts/2026-09-19/23-packet/p2-dark-settings.yaml` | `945e42f8…3ca` (`cards-golive-2026-09-19.md:15`) | drafter finding, recorded | `radar.cards_enabled: false`, NOT the value to restore |
| `radar.benchmark` | `data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml` | `prompts/2026-09-22/01-packet/radar-benchmark.yaml` | `10aef996…0880` (load report `:73-79`, applied 2026-09-22 07:04 ET; the source label `optional:radar-benchmark.yaml` carries no digest, `cli.py:218`) | not hashed | committed copy = tree file, byte-for-byte as text (2 lines each) |

- Last load per key. Card: the htf apply on 2026-09-20 at 21:05 ET. It printed `= radar.cards_enabled` (report `:230`), so production held `true` from the 09-19 load (`cards-golive-2026-09-19.md:116`, `'radar.cards_enabled': 'updated'` false→true) until the tombstone. No later card load:
  - The three other `card.*` rows still carry their 09-19/09-20 sources (P1).
  - A dark-file load would have deleted them, because the dark file omits them (`card.py:296-303`).
  - `price-floor-draft-2026-10-08.md:66` grepped the 09-2x and 10-xx reports and found no later `--card … --apply`. My `git log -S` since 09-21 hits only design and desk docs, no apply report.
  - Benchmark: the 09-22 apply is the only load. `git log -S "radar-benchmark.yaml --sha256"` since 09-23 is empty.
- How the loader computes the digest: `hashlib.sha256(Path(path).read_bytes()).hexdigest()`, checked before parsing (`card.py:243-249`, `cli.py:166-178`).
- Vault: `cobalt-product-definition.md:33,38-40` and `cobalt-sprints.md:54,74` record the same three digests and values.

## Q3 — values, raw

| file | key | raw value |
|---|---|---|
| `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml:2` | `radar.cards_enabled` | `  radar.cards_enabled: true` |
| `data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml:2` | `radar.benchmark` | `  radar.benchmark: {top_n: 20, min_move_pct: 10}` |

The model `BenchmarkSettings` accepts only `top_n: int > 0` and `min_move_pct: Decimal > 0`, with `extra="forbid"` (`models.py:226-235`). There are no other fields. Stored form at load: `{"min_move_pct": "10", "top_n": 20}` (load report `:77`).

## Q4 — side effects

| file | key | effect |
|---|---|---|
| htf card | `radar.cards_enabled` | WRITE `~` (tombstone → `true`), source becomes `card:p2-live-settings-htf.yaml@sha256:5993…` |
| htf card | `card.proposed_key` | KEEP `=` if the value is unchanged since 09-19 (source/time unchanged, P1; value not read) |
| htf card | `card.curves` | KEEP `=` (htf is its own current source, P1) |
| htf card | `card.shadow_promotion_bar` | KEEP `=` (as proposed_key) |
| htf card | `card.alignment_default` | none: absent in the file and in production (P1/P2), so it is not in `deletes` |
| optional | `radar.benchmark` | WRITE `~` (tombstone → benchmark). No other key |

- `apply_settings` passes all four card rows. The store leaves equal rows `unchanged` with their old source, as the 09-20 apply did (`cards-htf-apply-2026-09-20.md:237`, and the P1 sources).
- Narrower restore (one key): no supported path. `--card` is the whole set (`card.py:28-29`), `--optional` accepts only `OPTIONAL_SETTING_KEYS` (`cli.py:194-199`), and `--from`/`--from-git` take sheet keys only.
- Using the 09-19 file instead of htf would rewrite `card.curves`, dropping `htf_level_proximity`. Do not use it.
- Exposure: the vault-note mirror re-tombstones non-note `radar.*` keys on the next radar note edit (`survey-settings-writer-2026-10-23.md:8,54`).

## Q5 — commands (text, NOT run)

| file | dry-run | apply |
|---|---|---|
| htf card | `COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml --sha256 5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17 --dry-run` | same with `--apply` |
| benchmark | `COBALT_ENV=production uv run cobalt settings load --optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880 --dry-run` | same with `--apply` |

Why these files:
- htf is the last reviewed card set: production's other `card.*` rows equal it, so only `radar.cards_enabled` moves.
- benchmark is the only reviewed optional file for this key.

Rules quoted:
- The hub (`ops/desk/authorize.sh:46,62` → `prompts/PRODWRITE-HUB.md`) allows "the ONE production write a card row names (K3), backup first, report after" (`:3`), in the order authorization → shape → `backup run` → rollback → count → write once → verify (`:22-46`).
- The write is "NEVER typed a second time" (`:43`).
- Only the card's `<command>`, `backup run`, `backup status` or the one `db query` passes the guard (`:12`).
- The hub has NO dry-run step, and its guard would refuse a `--dry-run` string that is not the card's command.
- The hub forbids `"` `'` `\` `$` and similar characters in the command (`:29`). Both lines above are clean.
- Window: `apply_settings` → `assert_writable` refuses inside `market_reset` 20:00–21:00 ET (`cli.py:88-100`, `session/guard.py:7,67`).
- HITL: "A trader-run `cobalt settings load --apply` … is exempt from the HITL token" (LAWS L28, `LAWS.md:199+`). Its trace is one dated ledger line.

## Q6 — differences

- `p2-dark-settings.yaml` (committed copy, `prompts/2026-09-19/23-packet/`) holds `radar.cards_enabled: false`. It was superseded by the 09-19 load false→true (`cards-golive-2026-09-19.md:116`), so it does not conflict with the restore value.
- `radar-no-cards-2026-09-28.md:8` raised "reading B: cards_enabled is false" as a hypothesis only, with the query left as an ASK (`:53`). It is not a record of the value.
- `survey-settings-writer-2026-10-23.md:48-49` has both pre-tombstone values `not recorded`. This survey takes them from the files and load reports above.
- No conflicting value was found.

## DECISIONS
- ASK DESK: the PRODWRITE hub runs ONE write per card and has no dry-run step (`PRODWRITE-HUB.md:3,12,43`). How is the brain's "dry-run before apply" met? Options: two cards per key (dry-run card, then apply card), or the dry-run run elsewhere. Also: one card per key, or the two applies as two cards. Default taken: none chosen; both line pairs reported as text. [08:31]
- ASK DESK: the htf card file has no committed copy on `main`. `prompts/2026-09-20/16-packet/p2-live-settings-htf.yaml` exists on disk but is untracked. The K3 seat uses `data/backups/…` with `--sha256 5993…`, so the hash, not git, proves the bytes. Should the packet copy be committed for the record? Default: reported only. [08:31]

## RECORDS
All commands were run from `/Users/cobalt/cobalt`. Times are from `date`.
- `date` → `Fri Oct 23 08:30:12 EDT 2026` (exit 0)
- `ls ".../reports/survey-restore-prep-2026-10-23.md"` → exit 1, absent
- P1 (exit 0): `COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT key, jsonb_typeof(value) AS vtype, source, (updated_at AT TIME ZONE 'America/New_York') AS updated_et FROM \"user\".trader_settings WHERE strpos(source, 'card:') = 1 OR strpos(source, 'optional:') = 1 OR key IN ('radar.cards_enabled', 'radar.benchmark') ORDER BY key"`. Five rows:
  - `card.curves` · `card:p2-live-settings-htf.yaml@sha256:5993c57f…fbfc17` · 2026-09-20 21:04:57.409735
  - `card.proposed_key` and `card.shadow_promotion_bar` · `card:p2-live-settings.yaml@sha256:f3663399…c65f0` · 2026-09-19 12:30:05.463731
  - `radar.benchmark` and `radar.cards_enabled` · object · `vault:radar-notes@8d09a14dd681` · 2026-10-21 18:12:55.649090
  - No `optional:` row.
- P2 (exit 0): `COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT key, source, (updated_at AT TIME ZONE 'America/New_York') AS updated_et FROM \"user\".trader_settings WHERE strpos(key, 'card.') = 1 OR strpos(key, 'radar.') = 1 ORDER BY key"`. 15 rows:
  - The same three `card.*` rows. No `card.alignment_default`.
  - At 2026-10-21 18:12:55.649090 (`vault:radar-notes@8d09a14dd681`): `radar.benchmark`, `radar.cards_enabled`, `radar.list.tier_a/b/c`, `radar.note.lists`.
  - At 2026-09-14 04:01:14.485689 (same source): `radar.note.screens`, `radar.pool`, `radar.screen.{day_scan,down_gappers,morning_low_float,up_gappers}`.
- `sed -n` (exit 0) on `card.py:20-40`, `:236-340`; `cli.py:84-140`, `:145-400`; `models.py:220-250`; `guard.py:60-95`; `authorize.sh:55-68`; `LAWS.md:199-212`; `cards-htf-apply-2026-09-20.md:200-260`; `radar-benchmark-load-2026-09-22.md:40-85`; `radar-no-cards-2026-09-28.md:1-14`.
- `git -C … show main:…/2026-09-19/23-packet/p2-live-settings.yaml` → exit 0. `…/2026-09-22/01-packet/radar-benchmark.yaml` → exit 0. `…/2026-09-20/16-packet/p2-live-settings-htf.yaml` → exit 128, "exists on disk, but not in 'main'".
- `git -C … log --all --oneline -- …/2026-09-20/16-packet` → empty (exit 0).
- `git -C … grep -l -e 5993c57f… -e f3663399… main` → 17 files (exit 0). `git -C … grep -l "card_settings:" main -- prompts` → 6 files.
- `git -C … log --since=2026-09-21 --oneline -S "settings load --card" -- reports prompts` → 17 commits, design and desk docs only. `git -C … log --since=2026-09-23 --oneline -S "radar-benchmark.yaml --sha256"` → empty.
- Two `git log` calls with a `--format=%h|%ad|%s` string were blocked by `bare-guard.py` ("NOT A REFUSAL … one bare command per call"). They were resent without the format string.
- `ls -la data/backups/{cards-htf-2026-09-20,radar-benchmark-2026-09-22,pre-s2-p2-2026-09-17}` → exit 0. htf 405 B Sep 20 18:44; benchmark 68 B Sep 22 06:20; dark 44 B Sep 17 07:18.
- Read: both `data/backups` files, the 16-packet htf copy, `PRODWRITE-HUB.md` (whole).
- Grep: `cards-golive-2026-09-19.md` (`:4,15,116,122`); `survey-settings-writer-2026-10-23.md` (`:6,8,48-51,54`); `price-floor-draft-2026-10-08.md:66`; the vault `Think` digest/command grep (3 files); `grep -n market_reset|… guard.py`; `grep -n assert_writable cli.py card.py store.py` (`cli.py:50,88,100`).
- No hashing command, no loader run, no write except this report.
- `date` → `Fri Oct 23 08:31:58 EDT 2026`

SURVEYED · files: 2 · decisions: 2
