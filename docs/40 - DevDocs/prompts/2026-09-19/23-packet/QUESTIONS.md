You are an independent reviewer from another house, one of three reading this packet
separately. Read ONLY the files in this folder; you cannot run commands — everything you need is
already here as a file. `p2-dark-settings.yaml` is the file currently loaded in production
(`radar.cards_enabled: false`, sha256 `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca`).
`p2-live-settings.yaml` is the desk's DRAFT go-live file (never applied to any database — this
check is of the artifact only), built from Dejan's own R17 ruling (11:33 ET,
`docs/40 - DevDocs/reports/cto-2026-09-19.md` §4, quoted in full in `facts.md` §0 — read it there
verbatim before judging anything). `golive.diff` is the unified diff between the two files.
`src-settings-card.py` is the full settings/schema module. `src-cards-scoring-grade_from_curve.py`
is the interpolation/rounding code that turns a curve + a raw value into a 1-10 grade.
`src-radar-evaluate-factor_observations.py` and `src-radar-anatomy-daily-htf_level_proximity.py`
show where each factor's raw number comes from (units, whether it can be fractional).
`src-radar-evaluate-desk_shadow.py`, `src-session-guard-assert_writable.py`,
`src-session-clock-windows_for.py`, `src-cards-shadow_report-excerpt.py`, `src-settings-store.py`
are supporting excerpts. `plan-s2-p2-excerpt-step5-10.md` is the design-of-record section.
`facts.md` is the desk's own pre-computed reading, with file:line, tagging each number RULED
(his literal number), DESK READING (an interpretation of an ambiguous clause, stated back to him
for correction), or PROVISIONAL (no source at all) — treat every claim in it as a CLAIM to verify
against the source files, never as settled fact, exactly like a builder's report.

This artifact would (if approved and applied) flip a live production trading-support system's
radar cards from dark to visible/advisory for Monday premarket. For every finding give SEVERITY
(BLOCKER = the code does not do what facts.md says, contradicts R17's verbatim words, or
contradicts a LAW: L1 fail-loud, L7 shadow-mode promotion, L28 vault/HITL, L32 user-side data,
L52 nothing here may touch scoring/ranking without tribunal / MAJOR / MINOR), FILE + LINE, the
EVIDENCE you read (quote it), and the FAILING SCENARIO. Say "none found" rather than inventing.

(Q1) Is `p2-live-settings.yaml` VALID against `CardSettings` as written in `src-settings-card.py`?
Trace `_enabled_needs_bands_and_curves` and every field validator (`ProposedKeyBands._descending`,
`Curve._increasing`, the `CurveAnchor`/`ProposedKeyBands` field bounds) against the file's actual
numbers by hand. `facts.md` §10 claims it satisfies the gate by inspection but was NOT re-run
through the live module this round (read-only-by-reading-only per the coordinator) — this is your
independent second check. Flag anything the desk's reading missed.

(Q2) Does `Curve._increasing` (`src-settings-card.py`) check anything besides `x` being strictly
increasing? `facts.md` §2 claims grade values may be non-monotonic, descending, or flat between
anchors (no rule on `.grade` at all) — verify from the validator's actual code, not the claim.

(Q3) Grade arithmetic — using ONLY `src-cards-scoring-grade_from_curve.py`'s actual clamp/
interpolate/round logic, compute by hand: (a) `atrs_from_open` `[[1,1],[3,10]]` at ATR = 0.5, 1,
2, 3, 5 — do the floor/ceiling values match his "ATR > 1 starts the rising count and => 3 is 10"?
(b) `rvol` `[[1.2,1],[5,10]]` at RVOL = 1.0, 1.2, 3, 5, 8 — match "RVOL > 1.2 … >= 5 is a 10"? (c)
`Extension.leg_count` `[[0,10],[1,10],[2,6],[3,3],[5,1]]` at 0, 1, 2, 3, 4, 5, 6 legs — does 2 legs
land EXACTLY on grade 6 (an anchor hit, not an interpolation), does 4 legs interpolate to grade 2,
and do 5+ legs floor at grade 1? Do these match his verbatim "0-1 legs is 10, 1-2 legs is 6 and 3+
legs is 3 or below" AND the two DESK READINGS in `facts.md` §0/§5 that resolve his ambiguous
clauses — say explicitly whether either desk reading looks like a misreading of his words, quoting
his exact clause you think it conflicts with. (d) `htf_level_proximity` `[[0,10],[2,1]]` — is the
DIRECTION (closer = higher, i.e. grade descends as the raw ATR-distance value rises) correctly
implemented by this curve, matching his "closer = higher"? Its endpoints are marked PROVISIONAL in
facts.md §6 — do you agree there is no ruled magnitude for them anywhere in this packet, and is a
provisional placeholder here a BLOCKER (an invented trading number) or acceptable for a shadow-only
run where nothing derived from it reaches sizing (facts.md §6/`plan-s2-p2-excerpt-step5-10.md`)?

(Q4) Is `Extension.leg_count` genuinely never fractional? `facts.md` §4 cites
`src-radar-evaluate-factor_observations.py`'s `Formation.leg_count: int | None` and
`Decimal(ext.leg_count)` as proof. Confirm from that file, and say whether that means
interpolation on this factor can ever actually fire for anything except leg count = 4 (the one
integer with no anchor of its own).

(Q5) `htf_level_proximity`'s raw unit — does `src-radar-anatomy-daily-htf_level_proximity.py`
support facts.md §6's claim that the value is `distance / daily_ATR(14)`, unitless, 0 = at the
level, with no fixed upper bound? Is there anything in this packet (there should not be) that
supplies a ruled or empirical range for this value beyond R17's direction-only ruling?

(Q6) Does enabling (if the file is valid) do ONLY what facts.md §0 (inherited from the prior
round) says — a `/radar` panel becoming visible with hollow, tappable dots and no card_score until
tapped — or does anything in these curve/band values change sizing, fire an alert, or let an
engine-computed grade replace Dejan's own tap on a card face (L7)? `facts.md` §3 says sizing comes
only from the tapped grade via `snap_down`/`dollars_for`, never from `card.curves`/
`card.proposed_key` directly — verify this claim is actually about a different, unseen file
(`aset/engine.py`, not in this packet) and mark it UNVERIFIABLE FROM READS if you cannot confirm it
from files given, rather than assuming it is true.

(Q7) `card.shadow_promotion_bar` unchanged from the prior round
(`{sessions:10, pairs:30, median_max:1, within2_min:0.90}`) — does `plan-s2-p2-excerpt-step5-10.md`
still support these as the "09-14 group-2 ruling," and does `src-cards-shadow_report-excerpt.py`
read this setting the way facts.md describes?

(Q8) Is the rollback still real? Confirm `p2-dark-settings.yaml`'s sha256 in this packet against
`945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` if your sandbox allows hashing a
read file, else UNVERIFIABLE FROM READS. Does `golive.diff` show ONLY the changes facts.md claims
(cards_enabled false→true, `card.proposed_key`, `card.curves`, `card.shadow_promotion_bar` added,
`card.alignment_default` still absent) with nothing else touched?

(Q9) Cross-cutting: any secret, credential, path, or connection string visible in any file? Does
the file touch any key outside the five in `CARD_SETTING_KEYS`? Does anything here look like a
second implementation of a rule that already exists elsewhere (L3)? Is the "no dry-run available
under this launch line's rules" claim in facts.md §11 correct — scan the `--allowedTools` list in
`23-review-cards-golive.md`'s own header (not in this folder — you were told it verbally in your
launch; if you cannot see it, say UNVERIFIABLE FROM READS) for any `uv run`/`cobalt` rule.

End with exactly one line:
`VERDICT: FILE VALID-AS-DRAFTED / FILE INVALID (name why) / UNSAFE TO APPLY (name why)`
