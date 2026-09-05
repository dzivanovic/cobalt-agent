# `src/cobalt/daymode/note.py`

## What it does
The daily note's **sheet-mode line, both directions** (S1-P3, CTO review
of S1-P2).

## What it replaces
Slice 2 shipped one static string in `prefill/daily.py:76`:

```
Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half
```

Four markdown checkboxes that read nothing, compared nothing, persisted
nothing and refused nothing. A trader ticking one of them was talking to
a text file. It is **deleted**, not kept beside its replacement.

## Cobalt → note
A Cobalt-owned unit (`section daymode` / `unit sheet_mode`) written
through `VaultWriter`: stable id, updated in place, human text beside it
preserved, versioned to `vault_writes`, unified diff in every report
(L28). It carries the day mode in force, the stage it came from, the
sheet it sizes from, the keys it permits, and **one checkbox per
declared sheet** — derived from `cfg.hotkey_file_names`, so a sheet
added to `configs/cobalt/aset.yaml` gets a checkbox with no edit here.

## Note → Cobalt
A box he ticks in Obsidian — on the trading PC, through Sync — **is** an
attestation. `read_attestation()` parses it at the next sheet request
and `_read_back_note_attestation()` (in `aset/web.py`) persists it
through the same `attest_sheet` the banner selector calls. One write
path, two ways in.

Only boxes **inside Cobalt's own unit** count. A checkbox elsewhere in
his journal is his prose, and reading it would make any line containing
`[x] full.htk` into a risk decision.

## Conflict is a refusal, not a merge
| note | on record | result |
|---|---|---|
| silent | anything | the record stands |
| one tick | nothing | the tick **becomes** the attestation |
| one tick | same | agreed |
| one tick | different | **REFUSED**, both shown |
| two ticks | anything | **REFUSED** |

Picking one silently is how a full-size key gets pressed on a
reduced-size day. "The note is stale" and "the selector is stale" are
indistinguishable from inside the process. Two ticks is not a smaller
claim — it is no claim.

## It never creates a note
L28.1: only `create_if_absent` with a template may, and the 05:15
prefill is what does. A missing note is reported loudly and skipped.

## One renderer, three callers
`render_body()` is called by the 05:15 prefill (into the template and
the merge), by the ASET sheet's `/attest`, and by
`cobalt daymode attest|decide|propose`. Three copies of the words would
be three chances to disagree.
