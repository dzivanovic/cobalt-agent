# `cobalt.radar.formation.anchors` — what a formation hangs on

Added 2026-09-22 in STEP-4 of the setups one build (FINAL §2.4: `extension_direction` becomes `anchor {object, direction, bar_ts}`).

`ANCHORS` is one table, in order. `anchor_for(td)` returns the first row whose atom prefix one of the def's preconditions names. The choice is by the OBJECT the definition names, never by a trade name. Each row resolves on a frame, in frame coordinates, to a `FrameAnchor(object, direction, bar_ts)`, or to the note that says why there is nothing to form on:

- **`Extension`** is today's anchor, byte-identical: the culminating bar, and "no culminating bar to form on" otherwise. The stage applies A-01 to it in frame terms.
- **`Range(micro)`** is the live micro-Range's `instantiated_ts`. Its direction is the long-side text's trade side, `up` in frame coordinates, so the mirrored frame's formation is a short. With no instantiated Range the note is "no instantiated micro-Range to form on".

Adding an anchor for a new setup is one row here. The stage, the card and the registry are untouched.
