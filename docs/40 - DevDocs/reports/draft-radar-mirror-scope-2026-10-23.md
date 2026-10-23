# Draft: build card radar-mirror-scope
Seat `draft-radar-mirror-scope` (Opus 5.5), prompt `prompts/2026-10-23/1019-draft-radar-mirror-scope.md`. Read only; nothing committed.

## §0 Headline
- Card written: `prompts/2026-10-23/1020-radar-mirror-scope-card.md`, BAND HIGH, BASE `7487bb56`, RESTARTS `com.cobalt.radar`, OFF-LADDER (the ladder has no S5 radar line).
- M1: ownership is the stored row's `source` starting with `vault:radar-notes@`; the mirror reads `rows()` in place of `values()` (`notes.py:735`); a foreign or unknown source is left alone, an unknown one with a warning.
- M2 red-green and M3 no-regression rows as asked; M4 label fix taken in scope with a test (no reader parses the label).
- Row F1: five test fakes lack `rows()` and must gain it, or the radar suites go red.

## DECISIONS
1. Ownership by `source` prefix only, not also by key shape. Why: the brain's rule names the source; a key-shape list would duplicate `notes.py:106-118`. Effect: the already tombstoned `radar.cards_enabled`/`radar.benchmark` rows carry the mirror label, so the mirror re-tombstones them (written `unchanged`) until the K3 restore gives them the `card:`/`optional:` label back. [08:27]
2. "Unknown source" = a source matching neither the mirror's prefix nor one of six known writer prefixes (`card:`, `optional:`, `yaml:`, `git:`, `aset.change_line@`, `db_migration:`). `source` is `NOT NULL`, so no row lacks one. Such a row gets one `logger.warning` naming the key and the label, never the value. [08:27]
3. M4 fixed, not deferred. The label keeps its format and carries the changed note's hash; `git grep` finds no reader of `vault:radar-notes`. [08:28]
4. One `rows()` read replaces `values()`, so row F1 lists every fake on main that reaches the mirror; `CrossingSettingsStore.rows` (attribute, `test_radar_runner.py:310`) must be renamed. [08:28]
5. CHECK REPORT and HOUSE B filled at build time because the prompt names them; CARD.md leaves them empty for a build. ASK DESK if `desk-launch.sh build` refuses a filled one. [08:29]
6. RESTARTS: `com.cobalt.aset` not settled; R1 and X6 settle it. [08:29]

## RECORDS
- `date` → 2026-10-23 08:24:50 EDT (start); 08:30:11 EDT (report).
- Read: `prompts/CARD.md`; `prompts/2026-10-21/1000-cos-env-load-card.md`; `reports/survey-settings-writer-2026-10-23.md`; `topics/writing-rules.md`; `areas/cobalt.md` `## What Cobalt is` and from `## Build rules` down; `LAWS.md` L1 (`:107-108`), L69 (`:363-364`), index lines L32, L70, L80.
- `git show main:src/cobalt/radar/notes.py` (whole; `:686-751` read line by line), `main:src/cobalt/settings/store.py`, `main:src/cobalt/settings/cli.py`, `main:src/cobalt/radar/runner.py` (`:290-339`), `main:tests/cobalt/test_radar_notes.py`, `main:tests/cobalt/test_radar_runner.py`, `main:tests/fixtures/radar/radar-lists.example.md`.
- `git grep` on main: `mirror_sources|_mirror_rows|"removed"|radar-notes@` (src, tests); `settings_store=|def values|def rows` (tests); source labels in `card.py:324`, `web.py:1367`, `0004_radar_pool.sql:74`, `cli.py:218,280,283`; `"vault:|radar-notes` (only `notes.py:749`); `0001_trader_settings.sql:43` `source TEXT NOT NULL`; `logger.add(` tests; importers of `cobalt.radar.notes`; `jobs.yaml` labels and imports (`com.cobalt.radar` `:193`, `imports: [cobalt.cli]` `:203`); `notes.py:93` note hash; `test_drc_d4_fix_r1.py:61-67`.
- `git rev-parse --short=8 main` → `7487bb56`.
- `ls ops/com.cobalt.radar.plist` → listed; `ls docs/40 - DevDocs/cobalt/radar` → `notes.md` present; `ls prompts/2026-10-23/` → no `1020` card before this write.
- Grep `SPRINT-LADDER-v0_1.md` for `radar`, `S5`, `tombston` → no S5 radar line.
- Grep `cto-2026-10-23.md` R2388/R2389 → `:17` R2389 DESK RECORD, `:30` HOLD on radar-note edits.
- One shell call refused by `bare-guard.py` (a pipe); re-read with Read instead.

DRAFTED · decisions: 6
