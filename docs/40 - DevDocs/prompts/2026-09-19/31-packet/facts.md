# Facts — cards go-live settings file, REBUILT with R17's numbers (11:33 ET)

Read-only, no `uv run`/no execution of repo Python this round (per the coordinator's message);
every claim below is verified by READING `src/cobalt/settings/card.py` and
`src/cobalt/cards/scoring.py` line-by-line, not by running them. Prior round's live-code proof
(load_card_file refusal on the alignment/shadow-bar-only draft) stands from the earlier commit of
this file and is not re-run here.

## 0. R17 — his own ruling, verbatim, and where it lives

`docs/40 - DevDocs/reports/cto-2026-09-19.md` §4 R17 (11:33 ET), his words: "Key bands A+ >= 90, A
>= 70, B >= 50, C >= 40 less than 40 = D and pass / ATR > 1 starts the rising count and => 3 is 10
/ RVOL > 1.2 startd count and >= 5 is a 10 / Leg count is oposit, if we already had 3 legs move is
probably done so 0-1 legs is 10, 1-2 legs is 6 and 3+ legs is 3 or below / Level proximity, closer
= higher." Background research: `docs/40 - DevDocs/reports/card-values-sheet-2026-09-19.md`
(found the real enable-gate is `card.proposed_key` + `card.curves`, `card.py:157-169` — not
`alignment_default`/`shadow_promotion_bar` as the prior round assumed).

## 1. Schema shape — proof by reading, file:line

- **Bands** — `ProposedKeyBands` (`card.py:85-100`): `a_plus_min`, `a_min`, `b_min`, `c_min`, each
  `Decimal, ge=0, le=1` (fraction of conviction, NOT a 0-100 percentage — his "90/70/50/40" are
  **÷100** in the file: `0.90/0.70/0.50/0.40`). `_descending` (card.py:94-100) requires
  `a_plus_min > a_min > b_min > c_min` strictly — `0.90 > 0.70 > 0.50 > 0.40` passes.
- **Curves** — `card.curves: dict[str, Curve]` (card.py:153), each `Curve.anchors` a
  `tuple[CurveAnchor,...]`, `min_length=2` (card.py:108-111). The file's shorthand `[[x, grade],
  ...]` is accepted by the before-validator `_pairs` (card.py:113-123), which turns each `[x,
  grade]` pair into `{x: ..., grade: ...}` — **list-of-pairs, not list-of-objects**, confirmed
  from the validator itself, not inferred. `CurveAnchor.x: Decimal` (unbounded — any real number,
  not just 0-10) and `CurveAnchor.grade: Decimal, ge=1, le=10` (card.py:103-105).
- **Factor key is literally `Extension.leg_count`** (a single flat string key inside the
  `card.curves` mapping, dot-and-all — same pattern as top-level `radar.cards_enabled` already
  being a flat dotted key, not a nested `radar: {cards_enabled: ...}`). Confirmed against
  `FACTOR_COMPUTERS = ("atrs_from_open", "rvol", "Extension.leg_count", "htf_level_proximity")`
  (`radar/evaluate.py:429`) and the real Definition unit `Rubberband.md:94` naming that exact
  factor name.

## 2. (b) Does the schema allow a DESCENDING or flat grade sequence?

**Yes — confirmed by reading, this is NOT a code change.** `Curve._increasing`
(`card.py:125-130`):
```python
def _increasing(self) -> Curve:
    xs = [a.x for a in self.anchors]
    if any(a >= b for a, b in zip(xs, xs[1:])):
        raise ValueError(f"curve anchors must be strictly increasing in x, got {xs}")
    return self
```
This checks **only `x`** — it never reads or compares `.grade`. There is no monotonicity
requirement on grade anywhere in `card.py`. So `Extension.leg_count`'s DESCENDING shape
`[[0,10],[1,10],[2,6],[3,3],[5,1]]` — including the flat segment `[[0,10],[1,10]]` — is legal
exactly as drafted: `x = [0,1,2,3,5]` is strictly increasing (the only rule checked); each grade
(10,10,6,3,1) independently satisfies `ge=1, le=10`. Nothing here needed a code change.

## 3. (c) Values outside the anchors — clamped, not an error

`grade_from_curve` (`src/cobalt/cards/scoring.py:117-133`):
```python
if value <= anchors[0].x:
    raw = anchors[0].grade
elif value >= anchors[-1].x:
    raw = anchors[-1].grade
else:
    ... linear interpolation between the bracketing pair ...
raw = min(max(raw, ONE), TEN)
```
Below the first anchor → **flat at the first anchor's grade** (never an error, never null).
Above the last anchor → **flat at the last anchor's grade**. This is exactly what his "ATR ≤ 1 →
floor" and "≥ 3 is 10" / "≥ 5 is a 10" need: `atrs_from_open: [[1,1],[3,10]]` → ATR ≤ 1 clamps to
grade 1, ATR ≥ 3 clamps to grade 10, matching "=> 3 is 10" (≥3) literally. `rvol: [[1.2,1],[5,10]]`
→ RVOL ≤ 1.2 clamps to 1, RVOL ≥ 5 clamps to 10, matching "startd count [at 1.2] … >= 5 is a 10."
`Extension.leg_count`'s last anchor is `[5,1]`, so 5+ legs clamps flat at grade 1 ("3+ legs is 3 or
below" — 4 legs interpolates to 2, 5+ legs floors at 1; see §5).

## 4. (d) Interpolation — linear, rounded half-up once; is a fractional leg count possible

Same function, the `else` branch: `raw = lo.grade + (value - lo.x) * (hi.grade - lo.grade) / (hi.x
- lo.x)` — plain linear interpolation between the two bracketing anchors, in `Decimal` at
`ctx.prec = 28`, clipped to `[1,10]`, then **rounded half-up exactly once** to an integer:
`int(_half_up(raw))` where `_half_up` is `value.quantize(Decimal("1"), rounding=ROUND_HALF_UP)`
(`scoring.py:113-114,131-133`). So **2 legs is exactly grade 6** (an exact anchor hit, no rounding
needed — the loop's boundary condition `lo.x <= value <= hi.x` returns the anchor's own grade
verbatim when `value == lo.x`). **A fractional leg count is NOT possible**: `Extension.leg_count`'s
raw observation is `Decimal(ext.leg_count)` where `ext.leg_count: int | None`
(`radar/evaluate.py:336,458-460` — `Formation.leg_count: int | None`) — always a whole number or
null, never fractional. So interpolation on this factor only ever fires for an *observed* leg
count that has no exact anchor (only `4`, between anchors `3` and `5`): `raw = 3 + (4-3)*(1-3)/(5-3)
= 3 - 1 = 2` → **grade 2** at 4 legs, sliding toward the grade-1 floor at 5+ — consistent with his
"3+ legs is 3 or below."

## 5. Grades his ruled/desk-reading curves actually produce (worked, from §3/§4's exact code)

| Factor | Input | Grade | Matches his words? |
|---|---|---|---|
| `atrs_from_open` | ATR ≤ 1 | 1 (floor) | "ATR > 1 starts the rising count" ✓ |
| | ATR = 2 (midpoint) | 5 (interpolated, `1 + 1*9/2 = 5.5` → half-up → **6**, not 5 — flagged below) | see note |
| | ATR ≥ 3 | 10 (ceiling) | "=> 3 is 10" ✓ |
| `rvol` | RVOL ≤ 1.2 | 1 (floor) | "RVOL > 1.2 startd count" ✓ |
| | RVOL ≥ 5 | 10 (ceiling) | ">= 5 is a 10" ✓ |
| `Extension.leg_count` | 0 or 1 legs | 10 | "0-1 legs is 10" ✓ (DESK READING (i)) |
| | 2 legs | 6 | "1-2 legs is 6" read as 2=6 ✓ (DESK READING (i)) |
| | 3 legs | 3 | "3+ legs is 3 or below" ✓ (DESK READING (ii)) |
| | 4 legs | 2 (interpolated) | "sliding to 1" ✓ |
| | 5+ legs | 1 (floor) | "or below" ✓ |
| `htf_level_proximity` | 0 (at the level) | 10 | "closer = higher" ✓ (PROVISIONAL endpoint) |
| | ≥2 ATRs away | 1 (floor) | direction ✓, magnitude PROVISIONAL |

**Correction note on `atrs_from_open`'s midpoint**: I computed the ATR=2 grade above to show the
arithmetic is exact half-up rounding (`5.5 → 6`), not to claim he ruled a midpoint value — he only
ruled the two endpoints (1→1, ≥3→10); the midpoint is what LINEAR interpolation between them
produces, an artifact of the schema's shape (piecewise-linear only, no other curve family), not a
ruling. Flagged for the houses/him: if he meant something other than straight-line between the two
points, the schema cannot express it without a third anchor.

## 6. (e) `htf_level_proximity` — raw unit, range, proposed endpoints (PROVISIONAL)

Raw value (`radar/anatomy/daily.py:141-155`, `htf_level_proximity()`): `distance / daily_ATR(14)`
where `distance = min(|last − prior_high|, |last − prior_low|)` — an **ATR-normalized distance to
the nearer of yesterday's high/low**, unitless, `0` = price sitting exactly at that level,
increasing without a hard ceiling as price moves away. No fixture or doc in the repo gives a
realistic distribution of this value for Rubberband setups specifically (checked
`tests/cobalt/radar_p2_support.py:71-81` — factor is declared, no sample values shipped).

R17 ruled **direction only** ("closer = higher") — his own desk reading confirms: "level
proximity's END POINTS stay provisional — he ruled the direction only; the raw unit is read from
the code by the helper" (`cto-2026-09-19.md` R17 desk-reading (iv)). Proposed shape in the file:
`[[0, 10], [2, 1]]` — grade 10 at the level (0 ATRs away), grade 1 at 2+ ATRs away, PROVISIONAL on
both the "2" cutoff and the linear shape between; needs either his number or a Rubberband-setup
sample distribution before the shadow numbers on this one dot mean anything precise. This is the
**one fully-invented number** in the file (a shape, not a value he stated) — everything else above
either is his literal number or is arithmetic the code performs on his literal numbers.

## 7. `card.shadow_promotion_bar` — unchanged from the prior round

09-14 group-2 ruling, verbatim values: `{sessions: 10, pairs: 30, median_max: 1, within2_min:
0.90}` (`docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md:223`; `TAXONOMY-DRAFT-v0_8.md:69`). Not
required by the `cards_enabled=true` gate itself (`card.py:157-169` checks only `proposed_key`/
`curves`) but required by `cobalt cards shadow-report` (`cards/shadow_report.py:147-152`) — kept
in the file because it is a clean recorded ruling with no reason to leave it dark.

## 8. `card.alignment_default` — unchanged, still absent

Still left ABSENT: the plan's own designed fallback (ship N/A, Astra R2-6,
`plan-s2-p2-excerpt-step5-10.md:53`), and still unread by `desk_shadow()`
(`radar/evaluate.py:683-691`, unchanged since the prior round — not re-verified by execution this
round, verified by re-reading the same lines).

## 9. What the schema CANNOT express from his words

- **Discrete steps, not a ramp.** His description ("0-1 is 10, 1-2 is 6, 3+ is 3 or below") reads
  as step buckets; `card.curves` is piecewise-**linear** only (`card.py:108-133` — no step/
  constant-segment primitive besides two anchors sharing a grade, which is what `[[0,10],[1,10]]`
  exploits for the one flat "0-1" segment). Between named integer legs the file interpolates
  linearly (2→3 legs: 6 down to 3; 3→5 legs: 3 down to 1) — since `leg_count` is always an integer
  (§4) and every stated integer has its own anchor, this only shows up at the unstated integer 4
  (interpolates to grade 2, never asked about, but consistent with "or below").
- **No named default/starting value for the schema's own `flat_pct`-style partial object** — not
  relevant here since `alignment_default` stays absent.
- Nothing else in R17's words fails to fit the schema; every stated number is expressible exactly
  as an anchor or a band threshold.

## 10. Enable-gate re-confirmed by reading (not executed this round)

`CardSettings._enabled_needs_bands_and_curves` (`card.py:157-169`): `cards_enabled=True` requires
`proposed_key is not None` and `curves is not None` — both now present and non-empty in
`p2-live-settings.yaml`, so by inspection of the validator's own logic (not by running it) this
file satisfies the enable-gate. It was NOT re-run through the live module this round per the
coordinator's read-only-by-reading-only instruction; the three-house check's Q1 (below) is the
independent second read the loader itself has not yet performed.

## 11. Dry-run — not covered by 18's/23's `--allowedTools`

The loader's own command is `cobalt settings load --card <file> --sha256 <hash> --dry-run` — but
running it is a `cobalt`/`uv run` invocation, and **no rule in `18-review-ops-0919.md`'s
`--allowedTools` list (copied byte-for-byte into `23-review-cards-golive.md`) permits `uv run` or a
bare `cobalt` command.** So the hub CANNOT execute the dry run under this launch line — the
loader's own validation only happens at Dejan's later approved `--apply` step (or a dry run he or a
differently-authorized process runs). What the three houses + this schema read stand in for here
is the pre-check; the dry run itself remains outside this check's reach by design (no new rule was
added — none was needed for a files-only read).
