# `src/cobalt/vaultwrite/` — the ONE vault write path (LAW L28)

## What it does
Every byte Cobalt puts into an Obsidian note goes through this package.
Nothing else under `src/cobalt/` opens a vault file for writing — prove
it with:

```
grep -rn 'write_text\|open(.*"a"\|"w")\|os\.replace' src/cobalt/ --include="*.py"
```

which returns exactly three non-vault hits (`prefill/rules_gen.py` →
`configs/cobalt/rules.yaml`, `archiver/report.py` → `docs/30 - Design/`,
both inside the repo) plus this package's own `writer.py`.

Written 2026-09-03 in response to the daily-note incident (see
`docs/00 - Project/INCIDENT-2026-09-03-notes.md` and
`docs/10 - Decisions/ADR-0004-l28-one-vault-write-path.md`). Before it
there were five separate ways to write a vault file, none of which
recorded what they did, and one of which (`prefill/daily.py`'s
stub-upgrade branch) discarded everything above a banner line and
reported success.

## Files
| file | role |
|---|---|
| `markers.py` | marker syntax, parsing, and the pre-L28 read-compat shim |
| `merge.py` | the deterministic line-anchored three-way merge |
| `store.py` | the `vault_writes` / `vault_overrides` audit trail |
| `writer.py` | `VaultWriter` — the API, the fences, the guarded atomic write |
| `migrations/0001_vault_writes.sql` | the two tables |

`src/cobalt/cli.py` (`cobalt vault …`) is the rollback/inspection CLI
on top of it.

## The markers
```
<!-- cobalt:section NAME -->  …  <!-- /cobalt:section NAME -->
<!-- cobalt:unit ID -->       …  <!-- /cobalt:unit ID -->
```
A **section** is the only region Cobalt may write inside. A **unit** is
the atomic thing it writes and carries a stable id, so the same id
always updates in place instead of appending a second copy. Anything
inside a section that is not inside one of its units is human text and
is carried through verbatim, in position. Both are HTML comments, so
Obsidian's reading view hides them.

Marker names are validated against `^[A-Za-z0-9][A-Za-z0-9._:+-]*$` —
identifiers, never free text. Unbalanced, duplicated or wrongly-nested
markers raise `MarkerError` and the note is **not written to**.

## API
- `create_if_absent(path, template) -> WriteResult` — renders a template
  into a file that does not exist. An existing file is reported as
  `skipped_exists` and is never rewritten (L28.1). On a create it also
  seeds one baseline row per unit the template contained, so the first
  `upsert_unit` has a real `base` leg.
- `upsert_unit(path, section, unit_id, body, *, placement=None,
  skip_if=None) -> WriteResult` — the write path. Missing section →
  created at `placement` (default: end of note, nothing above touched).
  Missing unit → appended inside the section. Existing unit → merged.
- `upsert_region(path, section_label, region_id, body, *, locate)` —
  the ONE marker-less variant, for YAML frontmatter only (see below).
- `restore(write_id) -> WriteResult` — puts a section back to a recorded
  before-state, through this same writer.
- Every one of them honours `VaultWriter(dry_run=True)`: full diff
  computed, nothing written — not the note, not Postgres, not even the
  retention purge.

## The merge (`merge.py`)
Three inputs: `base` (what Cobalt wrote into this unit last time, from
`vault_writes.unit_after`), `human` (what is on disk now), `cobalt`
(what Cobalt wants to say now). `difflib` and nothing else — **no LLM in
the write path**, and the same three inputs always give the same output.

It is **line-anchored, not region-level**. A textbook diff3 resolves
whole unstable chunks at once, which conflates "the human edited this
line" with "the human typed a line next to one Cobalt changed" — and on
the real card shape that either froze Cobalt's update forever or threw
away the rest of the card. So:

- a base line the human left alone takes Cobalt's version;
- lines the human inserted are carried at their own anchor points, and
  are **not** overrides — an addition is not an edit;
- a base line the human changed or deleted keeps the human's version and
  produces one `Override` row (`conflict=True` when Cobalt also wanted
  to change it, `False` when it did not).

## The audit trail (`store.py`)
`vault_writes` — `ts, note, section, unit, before, after, unit_before,
unit_after, hash_before, hash_after, writer, run_id`. `before`/`after`
hold the touched **section** (what the law asks to persist, and what
`restore` puts back); `unit_before`/`unit_after` hold just that unit's
**body** (the next merge's `base` leg). They are not the same text — a
section carries its markers and any human lines between its units, and
merging a body against a section would read every marker as human text.
30-day retention, purged by the writer itself on every non-dry run.

`vault_overrides` — one row per place a human's text beat Cobalt's.
**Never purged.** An override is a calibration signal about Dejan's real
preferences, not an operational log.

`pending_write()` INSERTs the audit row, yields for the file write, and
commits only if that write succeeded — so a refused write leaves no
phantom row, and a committed row always corresponds to bytes on disk.

## The guard and the atomic write
`_commit()` re-reads the file and compares **both** sha256 and
`st_mtime_ns` against the snapshot the edit was computed from. On a
mismatch it raises `NoteChangedOnDisk` — the write ABORTS LOUDLY, the
run re-reads and retries **exactly once**, and a second failure raises.
The write itself is `tempfile.mkstemp` in the same directory, `fsync`,
then `os.replace` — atomic, and a partial file can never be observed.

`precommit_hook` on the constructor is a **test seam only** (it fires
between the guard read and the rename so a test can simulate a
concurrent writer). Never set it in production code.

## The fences (`assert_write_target`)
1. never inside the repo working tree (`cobalt.vault.assert_within_vault`);
2. a target under `/Users/cobalt/Vault/Think` is **refused** unless
   `COBALT_ENV=production` is set explicitly;
3. with `COBALT_ENV=production` set, a target *outside* that root is
   refused — a stale or misconfigured production process fails loud
   instead of writing to the wrong vault.

This is af83c6f's guard applied to the resolved **target**, not just to
the vault root, because callers pass paths directly.
`COBALT_ALLOW_DEV_ENTRY=1` is a read/entry opt-in and is deliberately
**not** a back door into writing the live vault.

## The one carve-out
Obsidian requires YAML frontmatter to be the very first bytes of a note:
a comment above `---` stops it being frontmatter, one inside stops it
being YAML. Trade-note frontmatter therefore cannot carry markers, so
`upsert_region` locates it structurally (`trade_note.frontmatter_span`)
instead. Everything else — merge, guard, atomicity, audit, diff,
dry-run, restore — is identical. It is the only such call site.

## Gotchas
- **Postgres is required for every write.** That is L28.3, and it is
  fail-loud by design: no audit row, no write. It also makes the prefill
  and ASET tests dev-DB tests.
- **No baseline is surfaced, not guessed.** If `vault_writes` has no
  prior body for a unit (never written, or purged past 30 days), the
  merge uses the on-disk body as base and the result carries
  `baseline_missing=True`, printed in the run report. An empty base
  would silently discard Cobalt's update on every run instead.
- **Historical notes are never retro-marked.** `legacy_slot_present()`
  and `drc.legacy_marker()` make a note carrying the pre-L28 markers
  read as already-filled, so it is skipped whole. Delete both shims once
  no un-retired note carries the old markers.
- `restore` refuses a whole-file create row (no section, no before-state
  — restoring would mean deleting the note) and refuses a row that
  created its section (before-state NULL).
- A no-op write that recorded an override still writes an audit row and
  advances the baseline, without touching the file — that is how an
  override is recorded exactly once rather than on every subsequent run.

## Tests
`tests/cobalt/test_vaultwrite.py` — 34 cases, run against the **dev
vault** (`~/dev-vault-cobalt/_l28-tests/`, created and removed per test,
with its own audit rows purged either side) and the **dev database**.
Organised by clause: L28.1 create-if-absent, L28.2 markers/units/human
text, L28.3 audit + guard + retry, L28.4 diff + dry-run, rollback,
L28.5 the vault fences, plus merge and marker unit tests with no I/O.
