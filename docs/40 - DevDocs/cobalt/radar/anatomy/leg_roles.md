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

**2026-09-22 — pullback, impulse, pre_test (STEP-6; FINAL §3 D3, §4).** `pullback_roles(legs)` works in the frame's coordinates, where the long-side text's trade direction is `up`:

- `pullback` is the latest DOWN leg that is not the first one: a pullback terminates an impulse or the opening drive.
- `index` is its ordinal among the pullbacks since the open.
- `before` is the leg it terminates: `before_role` is `opening_drive` when the pullback is the second leg, else `impulse`. `Leg(opening_drive OR impulse)` reads that leg, the FINAL's "most recent leg of either role that precedes the pullback".
- `pre_test_bars(run, roles)` is `Leg(pre_test)` (`A-14`, convention `leg.pre_test`): the run from the open to the pullback's first bar.

Because `legs()` alternates by construction (one opposing bar ends a leg), a pullback's preceding leg is always up. So in the long-side text `Leg(opening_drive OR impulse).direction == trade_direction` holds whenever a pullback exists. The magnitude of a role is not defined by the taxonomy, and no size rule is invented here.

**X15, run before wiring, both frames, constructed params.** 600 name-sessions: 241 drive-then-range, 36 form under A-07 and 5 under the literal reading. "The literal reading forms → `A-07` is not needed as worded" is an ESCALATE in the build report. `A-07` is kept as the FINAL words it.

**2026-09-22 (fix round 3, F3 — R49, `A-24`).** The roles now carry a minimum size: `MIN_SIZE_KEY = "leg.min_size_atr"` (engine row, unit `atr`, `value: null` in committed config — his to tune live, L53). `min_size(rows)` reads it; `pullback_roles(legs, *, min_size=None, atr=None)`: with no minimum (null) the roles are today's, byte for byte (a whole-day pin of every role on the committed day, both frames, is unchanged). With a value, a leg is "sized" when its high − low ≥ `min_size × atr` (the seeded working-TF ATR): the pullback is the latest SIZED down leg that is not the first leg; `index` counts only sized down legs; the leg it terminates is `opening_drive` when it is the first leg (no size rule) and `impulse` only when sized — else `before` / `before_role` are None, so `Leg(opening_drive OR impulse).direction == trade_direction` no longer holds on a small "impulse". A set minimum with no ATR yet returns `unavailable="insufficient_seed"`, never a guess. `leg.legs()` is unchanged (X16). `ROLE_TUNABLE_KEYS` joins the five role atoms' closure (`formation/atoms.py`), so a card formed with the key assumed carries it in `assumed_formation`.
