# `src/cobalt/prefill/rules_gen.py`

## What it does
**New, Slice 2.1 (2026-08-31, ruled by Dejan).** `configs/cobalt/
rules.yaml` used to be hand-authored; it's now a GENERATED artifact.
The vault's own `1 - Trading/5 - Review/Rules.md` ("THE 12 RULES") is
the one source of truth — this module reads it fresh, parses it,
writes `rules.yaml` as a cache/audit trail (header + sha256 of the
source text + timestamp), and returns the parsed config. Called by
`daily.py` and `drc.py` on every prefill run — never call the old
static `config.load_rules_config()` for a live rules block, that just
reads whatever `rules.yaml` last had on disk.

**Tag contract:** each numbered rule line in Rules.md must end with
exactly one trailing Obsidian tag from `RECOGNIZED_TAGS` (`#process
#sizing #time_window #re_entry #circuit_breaker #hard_stop`). Zero
tags, more than one, or an unrecognized tag all raise `RulesSourceError`
naming the exact line and rule number — there is no default category,
ever. Migrated once by hand into the real Rules.md (2026-08-31): each
of the 12 lines got exactly one tag appended, text otherwise verbatim.
Daily.md's old "Trade Rules" list is explicitly NOT a source (ruled
outdated 2026-08-23) — dropped, not merged in.

Mantras (`**Label:** *text*` lines, e.g. "Tape check"/"Identity") are
parsed generically — not hardcoded to those two names — so a mantra
Dejan adds the same way later is picked up automatically.

## Key functions/classes
- `RulesSourceError(RuntimeError)` — the one error type; message always
  names the Rules.md line number and rule number.
- `_split_trailing_tags(text) -> (remaining_text, [tags])` — peels
  however many trailing `#word` tokens actually exist off the end of a
  line (0, 1, or many), so the caller enforces "exactly one" itself and
  can report the real count.
- `_parse_rules_md(text) -> (list[RuleItem], list[MantraItem])` — no
  hardcoded "must be 12" — parses however many numbered lines exist, so
  Rules.md stays editable (add/remove/reorder a rule) without a code
  change.
- `regenerate_rules_config() -> RulesConfig` — resolves the vault,
  reads Rules.md, parses + validates, computes the sha256, writes
  `configs/cobalt/rules.yaml`, returns the result.

## Data flow in/out
**In:** the vault's `1 - Trading/5 - Review/Rules.md` (via
`cobalt.vault.resolve_vault_path()` — a READ, not gated by
`assert_within_vault`, which is a write-only safety property).
**Out:** `configs/cobalt/rules.yaml` (overwritten every call — hand
edits there are lost on the next run, by design), or a raised
`RulesSourceError`/`VaultConfigError`.

## Config it reads
The vault's Rules.md (not really "config" in the repo sense — it's
Dejan's own vault content, read-only from this module's perspective).
Writes `configs/cobalt/rules.yaml`.
