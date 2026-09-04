# ADR-0004 — LAW L28: one vault write path, marker-bounded and audited

Date: 2026-09-03
Status: Accepted
Supersedes: nothing. Retires `prefill/vault_writer.py`'s `write_new` /
`append_block` / `overwrite` and `aset/daily_note.py`'s append-mode
writer, plus `prefill/daily.py`'s stub-upgrade branch.

## Context

The 2026-09-03 forensics (`docs/00 - Project/INCIDENT-2026-09-03-notes.md`)
cleared Cobalt of the reported daily-note overwrite — Obsidian's editor
did it, twice — but found something worse than the reported bug: a code
path that *could* destroy human writing, silently, and report success.

`prefill/daily.py:475-485` handled a note ASET had stubbed by doing

```python
preserved_cards = existing.split(STUB_BANNER, 1)[1]
new_text = _render_template(context) + preserved_cards
```

Everything before the banner was discarded unconditionally, and the
branch was entered on a bare `if STUB_BANNER in existing` — a substring
test matching that line anywhere, at any depth, for the whole life of
the note. On 09-03 the prefix was two lines, so nothing was lost. Had
Dejan typed into the note before 14:22, it would all have gone, reported
as `action=upgraded_stub … filled: rules, trading, market_calendar`,
exit 0. The module docstring's standing promise ("never modify existing
note content") was honoured by the fill-in-place path and never
reconciled against this branch; the test that "proved" preservation only
ever wrote a pristine stub, so the discarded prefix was invisible to it.

Underneath that specific defect sat the structural problem: **five
different ways to put bytes into a vault file**, none of them recording
what they did.

| site | mechanism |
|---|---|
| `prefill/daily.py` | whole-file `write_text` (create, stub-upgrade, fill) |
| `prefill/drc.py` | `write_new` + blind `append_block` |
| `prefill/trade_note.py` | `write_new` + whole-file `overwrite` |
| `aset/daily_note.py` | `open(path, "a")`, stub-on-create inline |
| `aset/web.py` | calls the above, unconditionally |

None of them had identity for what they wrote, so a re-run appended a
duplicate rather than updating; none recorded a before-state, so nothing
could be diffed, reported or rolled back; and the only concurrency
defence was `_write_if_unchanged`, which guarded the read→write window
but happily wrote a `new_text` that had already thrown the prefix away.

## Decision

**LAW L28: there is ONE vault write path, `src/cobalt/vaultwrite/`, and
nothing under `src/cobalt/` writes a vault file any other way.**

1. **Create-if-absent only.** `create_if_absent(path, template)` renders
   a template into a file that does not exist. An existing file NEVER
   takes that path — not at 05:15, not for a stub, not ever. It takes
   `upsert_unit`, which merges. The stub-upgrade branch is **deleted**,
   not repaired, and so is the bare substring test that reached it.
2. **Marker-bounded, unit-addressed.** Cobalt writes only between
   `<!-- cobalt:section NAME -->` markers, and everything it writes is a
   `<!-- cobalt:unit ID -->` block with a stable id. Same id → update in
   place. Text Cobalt did not write — inside a section or outside one —
   is carried through verbatim, in position. A human edit to a Cobalt
   line WINS, is recorded in `vault_overrides`, and is surfaced in the
   run report. The merge is `difflib` only: **no LLM in the write path.**
3. **Audited and guarded.** Every write persists the touched section's
   before/after, that unit's before/after body, and the FULL-FILE hashes
   to `vault_writes` (30-day retention, purged by the writer itself);
   overrides go to `vault_overrides`, which never expires. The audit row
   is INSERTed first and committed only after the file write succeeds,
   so a refused write leaves no phantom row. The write itself is atomic
   (tmp + `os.replace` in the same directory) behind an mtime+hash
   guard: if the file changed since it was read, the write ABORTS
   LOUDLY, re-reads and retries exactly once.
4. **Diff-first.** Every `WriteResult` carries the unified diff, every
   run report prints it, and every entrypoint has `--dry-run`, which
   computes the whole edit and writes nothing — not the note, not
   Postgres (including the retention purge).
5. **Never the wrong vault.** `assert_write_target()` refuses a target
   under `/Users/cobalt/Vault/Think` unless `COBALT_ENV=production` is
   set explicitly, refuses a target *outside* it when that flag IS set,
   and refuses anything inside the repo working tree. This is af83c6f's
   guard applied to the resolved TARGET rather than only to the vault
   root, because callers pass paths directly.
   `COBALT_ALLOW_DEV_ENTRY=1` is a read/entry opt-in and is deliberately
   NOT a back door into writing the live vault.
6. **Rollback through the same writer.** `cobalt vault restore
   --write-id N [--dry-run]` puts a section back to its recorded
   before-state using the same markers, guard, atomic rename and audit
   row. There is no second write path, not even for undo.

## Consequences, and the three judgement calls inside them

**Line-anchored merge, not textbook diff3.** A region-level diff3
resolves whole unstable chunks at once, which conflates "the human
edited this line" with "the human typed a line next to one Cobalt
changed". Measured on the real card shape, that either froze Cobalt's
update forever or threw away the rest of the card. `merge.py` therefore
classifies each base line independently against the human's diff, takes
Cobalt's text for every line the human left alone, carries the human's
insertions at their own anchors, and records an override only where the
human actually changed or deleted Cobalt-authored lines. Deterministic,
and covered line-by-line in `tests/cobalt/test_vaultwrite.py`.

**A missing anchor is no longer a run failure.** `SlotAnchorNotFound`
used to fail the whole prefill. L28's stated default — append the
section at the end, touch nothing above it — destroys nothing and
guesses nothing, so that is what happens now, reported in the run log
with the placement that was tried. The class survives as a type only.

**One marker-less carve-out, named and fenced.** Obsidian requires YAML
frontmatter to be the first bytes of a note: a comment above `---` stops
it being frontmatter, one inside stops it being YAML. Trade-note
frontmatter therefore cannot carry markers. `VaultWriter.upsert_region`
locates that one region structurally instead, and everything else L28
asks for still applies. It is the only such call site and its docstring
says so.

**No baseline = surfaced, not guessed.** When `vault_writes` has no
prior body for a unit (never written, or purged past 30 days), the merge
uses the on-disk body as its base and the result carries
`baseline_missing=True`, which the run report prints. The alternative —
an empty base — would silently discard Cobalt's update on every run.

**Historical notes are not retro-marked.** Notes carrying the pre-L28
`<!-- cobalt-slot:NAME -->` / `<!-- cobalt-prefill:drc:DATE -->` markers
read as already-filled and are skipped whole. Adding a second copy of a
block Dejan already has is exactly the damage this law exists to
prevent. Both compatibility shims are marked for deletion once no
un-retired note carries the old markers.

**Cost.** Every vault write now needs Postgres. That is the law's own
requirement (L28.3) and it is fail-loud by design: no audit row, no
write. It also means the prefill and ASET tests are dev-DB tests now.

## Also decided here (L28 step 3)

`aset_sizings` gains `status` plus the actual-fill columns (migration
`0003`). The fill recompute persisted **nothing** before — the 09-03
TSLA FILL UPDATE at 10:02:36 had no DB row at all — so Postgres could
not answer "which cards became trades" and any note rebuild from the DB
would have silently dropped it. It is now an UPDATE to the card row it
belongs to, addressed by an explicit `card_row_id` carried on the form,
never by nearest-timestamp matching. `status` is deliberately minimal —
`CARD` and `FILLED`; the full lifecycle ruled on 09-02 (WATCH / ARMED /
TRIGGERED / FILLED / CLOSED / PASSED / EXPIRED) is out of scope while
the sheet is beta. The DRC now shows **cards written** and **trades
taken** as two numbers, trades taken counting `FILLED` only —
DRC-2026-09-03 reported "17 cards" when 2 were real and none were
filled.

## Alternatives rejected

- **Patch the stub branch** (the incident report's proposals 6–7: refuse
  when the prefix is non-trivial, tighten the trigger to `startswith`).
  Correct as far as it goes, and it leaves four other unaudited writers
  and no rollback. L28 removes the class of defect, not the instance.
- **Sidecar note Cobalt owns alone** (incident proposal 9c). It removes
  the Obsidian race rather than narrowing it, and it remains the right
  answer for the *editor* race — which L28 does not solve. Deferred as
  a Vault-Session decision about note layout, not a write-path decision.
- **Rebuild a damaged note from Postgres.** Refused, permanently: the DB
  is an incomplete mirror (14 of 17 blocks for 09-02), so a rebuild
  would silently drop cards. That is a fail-loud violation.

## Follow-ups (not done here)

- The Obsidian-side race is untouched. L28 makes a Cobalt write
  non-destructive and reversible; it cannot stop an editor buffer flush.
- **The production vault has no backup.** No Time Machine destination,
  no git, no sync. Still the largest open risk in the incident report.
- Production ASET and prefill write their cards to **`cobalt_dev`**
  (`configs/dev/aset.yaml`'s `db_name`), so live trading data and test
  rows share one database — that is how 15 `TEST`/`FORDATE` rows came to
  pollute DRC-2026-09-03. Tests now clean up after themselves; the
  prod/dev database split itself needs a ruling.
