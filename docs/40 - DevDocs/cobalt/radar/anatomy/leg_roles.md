# `cobalt.radar.anatomy.leg_roles` — the opening drive's role and termination

Added 2026-09-22 in STEP-4 of the setups one build (FINAL §3 D3, [F-12]; taxonomy §3.1).

Roles are a separate function over `leg.legs()`'s output plus the Range(micro) observation. `leg.py` itself is byte-identical: X16 pins its sha256, `2f3b3abc…782c8`, inside `tests/cobalt/test_setups_hitchhiker.py`.

- `opening_drive(run, legs, micro, max_retrace=)` returns an `OpeningDrive`:
  - The drive is the first leg of the RTH run, and its `direction` is that leg's.
  - `terminated_by` follows `A-07` in Gemini's wording: "When a micro-Range instantiates from the drive's extreme within a bounded retrace, the termination is consolidation."
  - "From the drive's extreme" means the range's bound on the drive's side is the run's extreme so far.
  - The retrace is the range's depth as a share of the drive. It must be within `cfg(leg.consolidation_max_retrace)`.
  - Otherwise the result is `pullback` when the first leg has ended. A drive still running has no termination; the frame serves that as `null`.
- `opening_drive_literal` is the taxonomy's literal reading: the leg ends at the first opposing bar, so it is `consolidation` only when the Range already includes that bar. It exists only for X15.
- `max_retrace(rows)` returns `None` when the row is null. The frame then serves `leg.consolidation_max_retrace_unset`.

**X15, run before wiring, both frames, constructed params.** 600 name-sessions: 241 drive-then-range, 36 form under A-07 and 5 under the literal reading. "The literal reading forms → `A-07` is not needed as worded" is an ESCALATE in the build report. `A-07` is kept as the FINAL words it.
